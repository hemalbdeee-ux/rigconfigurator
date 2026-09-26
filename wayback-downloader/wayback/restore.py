"""Restore a whole website from the Wayback Machine.

Pipeline: CDX index -> pick one snapshot per URL -> download raw files (resumable)
-> discover referenced-but-unlisted assets and fetch them too -> rewrite links to
relative local paths -> write the site folder (+ optional ZIP).
"""
from __future__ import annotations

import json
import os
import shutil
import threading
import time
import zipfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Callable
from urllib.parse import urlsplit

from .archive import Archive, ArchiveError, Capture
from .rewrite import decode, strip_archive_leftovers, transform_css, transform_html
from .urls import (
    Target,
    bare_host,
    local_path,
    parse_target,
    relative_link,
    strip_fragment,
    url_key,
    with_fragment,
)

HTML_MIMES = ("text/html", "application/xhtml+xml")


@dataclass
class Options:
    timestamp: str | None = None  # restore the site as it looked at this moment (closest capture)
    from_ts: str | None = None  # only consider captures in this window
    to_ts: str | None = None
    include_subdomains: bool = False
    fetch_missing: bool = True  # follow links/assets the index missed
    missing_rounds: int = 3
    max_files: int | None = None
    workers: int = 4
    min_interval: float = 0.25  # seconds between requests (archive.org rate-limits hard)
    make_zip: bool = True
    exclude_mimes: tuple[str, ...] = ()  # e.g. ("video/", "audio/")


@dataclass
class Progress:
    stage: str = "queued"  # queued, indexing, downloading, missing, rewriting, zipping, done, error
    found: int = 0
    downloaded: int = 0
    failed: int = 0
    skipped: int = 0
    bytes: int = 0
    rewritten: int = 0
    message: str = ""
    log: list[str] = field(default_factory=list)


@dataclass
class Entry:
    url: str
    timestamp: str
    mimetype: str
    path: str = ""
    status: str = "pending"  # pending, ok, failed


class Restorer:
    def __init__(
        self,
        target: str | Target,
        out_dir: str | Path,
        options: Options | None = None,
        archive: Archive | None = None,
        on_progress: Callable[[Progress], None] | None = None,
    ):
        self.target = parse_target(target) if isinstance(target, str) else target
        self.opts = options or Options()
        if self.target.timestamp and not self.opts.timestamp:
            self.opts.timestamp = self.target.timestamp
        self.out = Path(out_dir)
        self.raw_dir = self.out / ".raw"
        self.site_dir = self.out / "site"
        self.progress = Progress()
        self._on_progress = on_progress or (lambda _p: None)
        self._lock = threading.Lock()
        self._cancel = threading.Event()
        self.archive = archive or Archive(min_interval=self.opts.min_interval, log=self._log)
        if archive is not None:
            archive.log = self._log
        self.entries: dict[str, Entry] = {}  # url_key -> Entry

    # ---- bookkeeping -------------------------------------------------------------

    def _log(self, msg: str) -> None:
        with self._lock:
            stamp = time.strftime("%H:%M:%S")
            self.progress.log.append(f"{stamp} {msg}")
            del self.progress.log[:-200]
            self.progress.message = msg
        self._emit()

    def _emit(self) -> None:
        self._on_progress(self.progress)

    def _stage(self, stage: str, msg: str) -> None:
        self.progress.stage = stage
        self._log(msg)

    def cancel(self) -> None:
        self._cancel.set()

    @property
    def manifest_path(self) -> Path:
        return self.out / "manifest.json"

    def _save_manifest(self) -> None:
        data = {
            "target": asdict(self.target),
            "options": asdict(self.opts),
            "entries": [asdict(e) for e in self.entries.values()],
        }
        tmp = self.manifest_path.with_suffix(".tmp")
        tmp.write_text(json.dumps(data, indent=1))
        tmp.replace(self.manifest_path)

    def _load_manifest(self) -> bool:
        if not self.manifest_path.exists():
            return False
        data = json.loads(self.manifest_path.read_text())
        for e in data.get("entries", []):
            entry = Entry(**e)
            if entry.status == "ok" and not (self.raw_dir / entry.path).exists():
                entry.status = "pending"
            self.entries[url_key(entry.url)] = entry
        return bool(self.entries)

    # ---- stage 1: index ----------------------------------------------------------

    def _wanted(self, url: str, mime: str) -> bool:
        parts = urlsplit(url)
        host = bare_host(parts.hostname or "")
        if host != self.target.host and not (
            self.opts.include_subdomains and host.endswith("." + self.target.host)
        ):
            return False
        if host == self.target.host and not (parts.path or "/").startswith(self.target.path_prefix):
            return False
        mime = (mime or "").lower()
        return not any(mime.startswith(x) for x in self.opts.exclude_mimes)

    def index(self) -> None:
        self._stage("indexing", f"Listing archived files for {self.target.host}{self.target.path_prefix}")
        target_ts = (self.opts.timestamp or "").ljust(14, "9") if self.opts.timestamp else None
        best: dict[str, Capture] = {}

        def better(new: Capture, old: Capture) -> bool:
            if target_ts is None:  # newest capture wins
                return new.timestamp > old.timestamp
            new_before, old_before = new.timestamp <= target_ts, old.timestamp <= target_ts
            if new_before != old_before:
                return new_before  # prefer what existed at the chosen moment
            if new_before:
                return new.timestamp > old.timestamp
            return new.timestamp < old.timestamp  # nothing earlier: take the first one after

        if self.opts.include_subdomains:
            patterns = [(self.target.host, "domain")]
        else:
            patterns = [(f"{self.target.host}{self.target.path_prefix}", "prefix")]
        count = 0
        for pattern, match_type in patterns:
            for cap in self.archive.iter_captures(
                pattern, match_type, self.opts.from_ts, self.opts.to_ts
            ):
                if self._cancel.is_set():
                    raise ArchiveError("cancelled")
                if not self._wanted(cap.original, cap.mimetype):
                    continue
                key = url_key(cap.original)
                if key is None:
                    continue
                count += 1
                old = best.get(key)
                if old is None or better(cap, old):
                    best[key] = cap
                if count % 5000 == 0:
                    self.progress.found = len(best)
                    self._log(f"…{count} captures scanned, {len(best)} unique files")

        items = sorted(best.items(), key=lambda kv: (kv[1].mimetype not in HTML_MIMES, kv[0]))
        if self.opts.max_files:
            items = items[: self.opts.max_files]
        for key, cap in items:
            if key not in self.entries:
                mime = cap.mimetype.split(";")[0].strip().lower()
                self.entries[key] = Entry(cap.original, cap.timestamp, mime)
        self.progress.found = len(self.entries)
        self._log(f"Found {len(self.entries)} unique files ({count} captures)")

    # ---- stage 2: download -------------------------------------------------------

    def _assign_path(self, entry: Entry) -> None:
        if not entry.path:
            entry.path = local_path(entry.url, entry.mimetype, self.target.host)

    def _download_one(self, entry: Entry) -> None:
        if self._cancel.is_set():
            return
        try:
            result = self.archive.fetch(entry.timestamp, entry.url)
        except ArchiveError as e:
            result = None
            self._log(f"failed {entry.url}: {e}")
        with self._lock:
            if result is None:
                entry.status = "failed"
                self.progress.failed += 1
                return
            body, ctype, _ = result
            mime = ctype.split(";")[0].strip().lower()
            if mime and (not entry.mimetype or entry.mimetype in ("unk", "warc/revisit")):
                entry.mimetype = mime
                entry.path = ""
            self._assign_path(entry)
            dest = self.raw_dir / entry.path
            try:
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(body)
            except OSError as e:  # e.g. a file already sits where this needs a folder
                entry.status = "failed"
                self.progress.failed += 1
                self.progress.message = f"could not save {entry.path}: {e}"
                return
            entry.status = "ok"
            self.progress.downloaded += 1
            self.progress.bytes += len(body)
        self._emit()

    def _resolve_path_clashes(self) -> None:
        """A file at 'a/b' and a folder 'a/b/' can't coexist: move the file aside."""
        dirs = set()
        for e in self.entries.values():
            parts = e.path.split("/")
            for i in range(1, len(parts)):
                dirs.add("/".join(parts[:i]))
        for e in self.entries.values():
            if e.path in dirs and e.status != "ok":  # never move a file already on disk
                e.path += ".file"

    def download(self, entries: list[Entry]) -> None:
        for e in entries:
            self._assign_path(e)
        self._resolve_path_clashes()
        todo = [e for e in entries if e.status != "ok"]
        self.progress.skipped += len(entries) - len(todo)
        if not todo:
            return
        self._log(f"Downloading {len(todo)} files with {self.opts.workers} workers")
        last_save = time.monotonic()
        with ThreadPoolExecutor(max_workers=self.opts.workers) as pool:
            futures = [pool.submit(self._download_one, e) for e in todo]
            for _ in as_completed(futures):
                if time.monotonic() - last_save > 10:
                    with self._lock:
                        self._save_manifest()
                    last_save = time.monotonic()
        self._save_manifest()
        if self._cancel.is_set():
            raise ArchiveError("cancelled")

    # ---- stage 3: things the index missed -----------------------------------------

    def _is_local_host(self, url: str) -> bool:
        host = bare_host(urlsplit(url).hostname or "")
        return host == self.target.host or (
            self.opts.include_subdomains and host.endswith("." + self.target.host)
        )

    def _references(self, entry: Entry) -> set[str]:
        found: set[str] = set()

        def record(u: str) -> None:
            found.add(strip_fragment(u))
            return None

        text, _ = decode((self.raw_dir / entry.path).read_bytes())
        if entry.mimetype in HTML_MIMES:
            transform_html(text, entry.url, record)
        elif entry.mimetype == "text/css":
            transform_css(text, entry.url, record)
        return found

    def fetch_missing(self) -> None:
        checked: set[str] = set()
        for round_no in range(1, self.opts.missing_rounds + 1):
            new: list[Entry] = []
            for entry in list(self.entries.values()):
                if entry.status != "ok" or entry.mimetype not in HTML_MIMES + ("text/css",):
                    continue
                for ref in self._references(entry):
                    key = url_key(ref)
                    if not key or key in self.entries or key in checked:
                        continue
                    checked.add(key)
                    if not self._wanted(ref, ""):
                        continue
                    ts = self.opts.timestamp or entry.timestamp
                    e = Entry(ref, ts, "")
                    self.entries[key] = e
                    new.append(e)
            if self.opts.max_files and len(self.entries) > self.opts.max_files:
                break
            if not new:
                return
            self._stage("missing", f"Round {round_no}: fetching {len(new)} linked files not in the index")
            self.progress.found = len(self.entries)
            self.download(new)
            # drop what the archive does not have so it isn't linked to a missing file
            for e in new:
                if e.status != "ok":
                    self.entries.pop(url_key(e.url), None)
                    self.progress.failed -= 1
            self._save_manifest()

    # ---- stage 4: rewrite ---------------------------------------------------------

    def _link_fn(self, entry: Entry) -> Callable[[str], str | None]:
        def fn(url: str) -> str | None:
            target = self.entries.get(url_key(url) or "")
            if target is not None and target.status == "ok":
                return with_fragment(relative_link(entry.path, target.path), url)
            if self._is_local_host(url):
                return url  # absolute, so it still works once the <base> is gone
            return None

        return fn

    def rewrite(self) -> None:
        self._stage("rewriting", "Rewriting links so the site works offline")
        if self.site_dir.exists():
            shutil.rmtree(self.site_dir)
        for entry in self.entries.values():
            if entry.status != "ok":
                continue
            src = self.raw_dir / entry.path
            dest = self.site_dir / entry.path
            dest.parent.mkdir(parents=True, exist_ok=True)
            if entry.mimetype in HTML_MIMES or entry.mimetype == "text/css":
                text, enc = decode(src.read_bytes())
                if entry.mimetype in HTML_MIMES:
                    text = transform_html(strip_archive_leftovers(text), entry.url, self._link_fn(entry))
                else:
                    text = transform_css(text, entry.url, self._link_fn(entry))
                dest.write_bytes(text.encode(enc))
                self.progress.rewritten += 1
            else:
                shutil.copyfile(src, dest)
        self._write_extras()

    def _write_extras(self) -> None:
        # Server configs so the restored site also works on Apache/Nginx hosting.
        (self.site_dir / ".htaccess").write_text(
            "DirectoryIndex index.html\nOptions -MultiViews\nErrorDocument 404 /404.html\n"
        )
        report = {
            "site": self.target.host,
            "restored_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            "snapshot": self.opts.timestamp or "latest",
            "files": sum(1 for e in self.entries.values() if e.status == "ok"),
            "failed": [e.url for e in self.entries.values() if e.status == "failed"],
        }
        (self.out / "report.json").write_text(json.dumps(report, indent=1))

    # ---- stage 5: zip ------------------------------------------------------------

    @property
    def zip_path(self) -> Path:
        return self.out / f"{self.target.host}.zip"

    def make_zip(self) -> Path:
        self._stage("zipping", "Packing ZIP")
        tmp = self.zip_path.with_suffix(".zip.tmp")
        with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
            for root, _dirs, files in os.walk(self.site_dir):
                for name in files:
                    full = Path(root) / name
                    zf.write(full, f"{self.target.host}/{full.relative_to(self.site_dir)}")
        tmp.replace(self.zip_path)
        return self.zip_path

    # ---- run ---------------------------------------------------------------------

    def run(self) -> Progress:
        self.out.mkdir(parents=True, exist_ok=True)
        try:
            if self._load_manifest():
                self._log(f"Resuming: {len(self.entries)} files already indexed")
                self.progress.found = len(self.entries)
            else:
                self.index()
                self._save_manifest()
            if not self.entries:
                raise ArchiveError(
                    f"The Wayback Machine has no captures for {self.target.host}{self.target.path_prefix}"
                )
            self._stage("downloading", "Downloading files")
            self.download(list(self.entries.values()))
            if self.opts.fetch_missing:
                self.fetch_missing()
            self.rewrite()
            if self.opts.make_zip:
                self.make_zip()
            ok = sum(1 for e in self.entries.values() if e.status == "ok")
            self._stage("done", f"Restored {ok} files ({self.progress.failed} could not be downloaded)")
        except Exception as e:  # surface every failure to the UI/CLI
            self.progress.stage = "error"
            self._log(f"Error: {e}")
            raise
        return self.progress
