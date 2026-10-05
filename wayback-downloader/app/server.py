"""Web front end: submit a site, watch progress, preview the restored site, download the ZIP."""
from __future__ import annotations

import os
import re
import shutil
import threading
import time
import uuid
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from wayback import Archive, ArchiveError, Options, Restorer, parse_target

DATA_DIR = Path(os.environ.get("DATA_DIR", "data")).resolve()
MAX_JOBS = int(os.environ.get("MAX_PARALLEL_JOBS", "2"))
MAX_FILES = int(os.environ.get("MAX_FILES_PER_JOB", "0")) or None
JOB_TTL_HOURS = float(os.environ.get("JOB_TTL_HOURS", "48"))
SITE_NAME = os.environ.get("SITE_NAME", "Wayback Restore")
STATIC = Path(__file__).parent / "static"
TS_RE = re.compile(r"^\d{4,14}$")

app = FastAPI(title=SITE_NAME)
pool = ThreadPoolExecutor(max_workers=MAX_JOBS)
jobs: dict[str, dict] = {}
jobs_lock = threading.Lock()


class JobRequest(BaseModel):
    url: str
    timestamp: str | None = None
    from_ts: str | None = None
    to_ts: str | None = None
    include_subdomains: bool = False
    skip_media: bool = False


def _ts(value: str | None) -> str | None:
    value = (value or "").replace("-", "").strip()
    if not value:
        return None
    if not TS_RE.match(value):
        raise HTTPException(400, "Dates must look like 2019, 201906 or 20190615")
    return value


def _cleanup() -> None:
    cutoff = time.time() - JOB_TTL_HOURS * 3600
    with jobs_lock:
        for jid, job in list(jobs.items()):
            if job["created"] < cutoff and job["progress"].stage in ("done", "error"):
                shutil.rmtree(DATA_DIR / jid, ignore_errors=True)
                del jobs[jid]


def _run(jid: str) -> None:
    job = jobs[jid]
    try:
        job["restorer"].run()
    except Exception:  # already recorded in progress.stage/log
        pass
    finally:
        job["finished"] = time.time()


@app.post("/api/jobs")
def create_job(req: JobRequest):
    _cleanup()
    try:
        target = parse_target(req.url)
    except ValueError as e:
        raise HTTPException(400, str(e))
    opts = Options(
        timestamp=_ts(req.timestamp) or target.timestamp,
        from_ts=_ts(req.from_ts),
        to_ts=_ts(req.to_ts),
        include_subdomains=req.include_subdomains,
        exclude_mimes=("video/", "audio/") if req.skip_media else (),
        max_files=MAX_FILES,
    )
    signature = (target.host, target.path_prefix, opts.timestamp, opts.from_ts, opts.to_ts,
                 opts.include_subdomains, req.skip_media)
    with jobs_lock:
        for jid, job in jobs.items():  # same request already running: share it
            if job["signature"] == signature and job["progress"].stage not in ("error",):
                return {"id": jid}
        jid = uuid.uuid4().hex[:12]
        restorer = Restorer(target, DATA_DIR / jid, opts)
        jobs[jid] = {
            "id": jid,
            "signature": signature,
            "target": f"{target.host}{target.path_prefix}",
            "timestamp": opts.timestamp,
            "created": time.time(),
            "finished": None,
            "restorer": restorer,
            "progress": restorer.progress,
        }
    pool.submit(_run, jid)
    return {"id": jid}


def _job(jid: str) -> dict:
    job = jobs.get(jid)
    if not job:
        raise HTTPException(404, "Job not found (jobs are deleted after a while)")
    return job


@app.get("/api/jobs/{jid}")
def job_status(jid: str):
    job = _job(jid)
    p = asdict(job["progress"])
    p["log"] = p["log"][-30:]
    queued = sum(1 for j in jobs.values() if j["progress"].stage == "queued" and j["created"] < job["created"])
    return {
        "id": jid,
        "target": job["target"],
        "timestamp": job["timestamp"],
        "queue_position": queued if p["stage"] == "queued" else 0,
        "zip_ready": job["restorer"].zip_path.exists() and p["stage"] == "done",
        **p,
    }


@app.post("/api/jobs/{jid}/cancel")
def cancel_job(jid: str):
    _job(jid)["restorer"].cancel()
    return {"ok": True}


@app.get("/api/jobs/{jid}/download")
def download(jid: str):
    r = _job(jid)["restorer"]
    if not r.zip_path.exists():
        raise HTTPException(409, "ZIP not ready yet")
    return FileResponse(r.zip_path, filename=r.zip_path.name, media_type="application/zip")


@app.get("/api/snapshots")
def snapshots(url: str):
    try:
        target = parse_target(url)
        stamps = Archive(min_interval=0).homepage_snapshots(target.host)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except ArchiveError as e:
        raise HTTPException(502, f"Wayback Machine unavailable: {e}")
    return {"host": target.host, "snapshots": stamps}


@app.get("/preview/{jid}/{path:path}")
def preview(jid: str, path: str = ""):
    site = _job(jid)["restorer"].site_dir.resolve()
    f = (site / path).resolve()
    if site not in f.parents and f != site:
        raise HTTPException(404)
    if f.is_dir():
        f = f / "index.html"
    if not f.is_file():
        raise HTTPException(404, "Not in the restored site")
    # Archived pages run their own scripts: sandbox them so they can't act as this app's origin.
    return FileResponse(f, headers={"Content-Security-Policy": "sandbox allow-scripts allow-forms allow-popups"})


@app.get("/", response_class=HTMLResponse)
def index():
    return (STATIC / "index.html").read_text().replace("{{SITE_NAME}}", SITE_NAME)


app.mount("/static", StaticFiles(directory=STATIC), name="static")
DATA_DIR.mkdir(parents=True, exist_ok=True)
