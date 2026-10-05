"""Talks to the Wayback Machine: the CDX index (what was captured) and raw snapshots."""
from __future__ import annotations

import os
import random
import threading
import time
from dataclasses import dataclass
from typing import Callable, Iterator

import requests

DEFAULT_BASE = os.environ.get("WAYBACK_BASE", "https://web.archive.org")
USER_AGENT = os.environ.get(
    "WAYBACK_USER_AGENT", "wayback-restore/1.0 (+https://github.com/; website restoration tool)"
)
RETRY_STATUS = {429, 500, 502, 503, 504, 520, 522, 524}


@dataclass
class Capture:
    urlkey: str
    timestamp: str
    original: str
    mimetype: str
    length: int = 0


class ArchiveError(Exception):
    pass


class RateLimiter:
    """Spaces requests at least `interval` seconds apart across all threads."""

    def __init__(self, interval: float):
        self.interval = interval
        self._lock = threading.Lock()
        self._next = 0.0

    def wait(self) -> None:
        with self._lock:
            now = time.monotonic()
            delay = self._next - now
            self._next = max(now, self._next) + self.interval
        if delay > 0:
            time.sleep(delay)

    def backoff(self, seconds: float) -> None:
        """Push every thread back after the archive says 'slow down'."""
        with self._lock:
            self._next = max(self._next, time.monotonic() + seconds)


class Archive:
    def __init__(
        self,
        base: str = DEFAULT_BASE,
        min_interval: float = 0.25,
        retries: int = 6,
        timeout: float = 60,
        log: Callable[[str], None] = lambda _m: None,
    ):
        self.base = base.rstrip("/")
        self.retries = retries
        self.timeout = timeout
        self.limiter = RateLimiter(min_interval)
        self.log = log
        self._local = threading.local()

    @property
    def session(self) -> requests.Session:
        s = getattr(self._local, "session", None)
        if s is None:
            s = requests.Session()
            s.headers["User-Agent"] = USER_AGENT
            self._local.session = s
        return s

    def _get(self, url: str, params: dict | None = None) -> requests.Response:
        last: Exception | None = None
        for attempt in range(self.retries + 1):
            self.limiter.wait()
            try:
                r = self.session.get(url, params=params, timeout=self.timeout, allow_redirects=True)
            except requests.RequestException as e:
                last = e
                wait = min(60, 2**attempt + random.random())
                self.log(f"network error ({e.__class__.__name__}), retrying in {wait:.0f}s")
                self.limiter.backoff(wait)
                continue
            if r.status_code in RETRY_STATUS:
                last = ArchiveError(f"HTTP {r.status_code} for {url}")
                retry_after = r.headers.get("Retry-After", "")
                wait = float(retry_after) if retry_after.isdigit() else min(90, 2 ** (attempt + 1))
                wait += random.random()
                self.log(f"archive.org returned {r.status_code}, backing off {wait:.0f}s")
                self.limiter.backoff(wait)
                continue
            return r
        raise ArchiveError(str(last))

    # ---- index -----------------------------------------------------------------

    def iter_captures(
        self,
        url_pattern: str,
        match_type: str = "prefix",
        from_ts: str | None = None,
        to_ts: str | None = None,
        page_size: int = 10000,
    ) -> Iterator[Capture]:
        """Yield every successful (HTTP 200) capture matching the pattern, paging with resumeKey."""
        params = {
            "url": url_pattern,
            "matchType": match_type,
            "output": "json",
            "fl": "urlkey,timestamp,original,mimetype,statuscode,length",
            "filter": "statuscode:200",
            "showResumeKey": "true",
            "limit": str(page_size),
        }
        if from_ts:
            params["from"] = from_ts
        if to_ts:
            params["to"] = to_ts
        resume = None
        while True:
            if resume:
                params["resumeKey"] = resume
            r = self._get(f"{self.base}/cdx/search/cdx", params)
            if r.status_code != 200:
                raise ArchiveError(f"CDX query failed: HTTP {r.status_code}: {r.text[:200]}")
            rows = r.json() if r.text.strip() else []
            resume = None
            header = True
            for i, row in enumerate(rows):
                if header:  # first row is the field list
                    header = False
                    continue
                if not row:  # [] separates data from the resume key
                    if i + 1 < len(rows) and rows[i + 1]:
                        resume = rows[i + 1][0]
                    break
                urlkey, ts, original, mime, _status, length = (row + [""] * 6)[:6]
                yield Capture(urlkey, ts, original, mime, int(length) if length.isdigit() else 0)
            if not resume:
                return

    def homepage_snapshots(self, host: str) -> list[str]:
        """One timestamp per month in which the home page was captured (for a date picker)."""
        r = self._get(
            f"{self.base}/cdx/search/cdx",
            {
                "url": f"{host}/",
                "output": "json",
                "fl": "timestamp",
                "filter": "statuscode:200",
                "collapse": "timestamp:6",
            },
        )
        if r.status_code != 200 or not r.text.strip():
            return []
        return [row[0] for row in r.json()[1:] if row]

    # ---- content ---------------------------------------------------------------

    def snapshot_url(self, timestamp: str, original: str) -> str:
        # "id_" asks for the original bytes: no toolbar, no rewritten links.
        return f"{self.base}/web/{timestamp}id_/{original}"

    def fetch(self, timestamp: str, original: str) -> tuple[bytes, str, str] | None:
        """Return (body, content-type, final original url) or None when the archive has no copy."""
        r = self._get(self.snapshot_url(timestamp, original))
        if r.status_code != 200:
            return None
        ctype = r.headers.get("Content-Type", "")
        return r.content, ctype, original
