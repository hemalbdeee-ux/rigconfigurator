"""A tiny stand-in for web.archive.org: CDX API (with resumeKey paging) + id_ snapshots."""
from __future__ import annotations

import json
import re
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlsplit

# (timestamp, original url, mimetype, body) -- one row per capture
CAPTURES = [
    ("20150101000000", "http://www.example.com/", "text/html",
     b'<html><head><title>OLD</title></head><body>old home</body></html>'),
    ("20190101000000", "http://www.example.com/", "text/html",
     b'<html><head><base href="http://www.example.com/">'
     b'<link rel="stylesheet" href="/css/site.css?v=2">'
     b'<meta http-equiv="refresh" content="300; url=http://example.com/about">'
     b'<!-- BEGIN WAYBACK TOOLBAR INSERT -->junk<!-- END WAYBACK TOOLBAR INSERT -->'
     b'</head><body>'
     b'<a href="about">About</a> <a href="https://www.example.com/blog/post.php?id=3&amp;x=1#top">Post</a>'
     b'<img src="//example.com/img/logo.png" srcset="/img/logo.png 1x, /img/logo@2x.png 2x">'
     b'<a href="https://web.archive.org/web/2019/http://example.com/contact/">Contact</a>'
     b'<a href="http://other.org/">Other</a> <a href="/never-archived">Gone</a>'
     b'<div style="background:url(/img/bg.jpg)">x</div>'
     b'</body></html>'),
    ("20190102000000", "http://example.com/about", "text/html",
     b'<html><body><a href="/">Home</a><a href="contact/">Contact</a></body></html>'),
    ("20190103000000", "http://example.com/contact/", "text/html",
     b'<html><body>caf\xe9 contact <img src="../img/logo.png"></body></html>'),  # latin-1 body
    ("20190104000000", "https://www.example.com/blog/post.php?id=3&x=1", "text/html",
     b'<html><body>post <a href="../about">about</a></body></html>'),
    ("20190105000000", "http://example.com/css/site.css?v=2", "text/css",
     b'@import "fonts.css"; body{background:url("../img/bg.jpg")}'),
    ("20190106000000", "http://example.com/img/logo.png", "image/png", b"\x89PNG logo"),
    ("20190107000000", "http://example.com/img/bg.jpg", "image/jpeg", b"\xff\xd8 bg"),
    ("20250101000000", "http://example.com/about", "text/html",
     b'<html><body>NEW about page from 2025</body></html>'),
]
# Captured, but missing from the CDX index: only reachable by following links.
UNLISTED = {
    "http://example.com/css/fonts.css": ("text/css", b'@font-face{src:url(/fonts/a.woff2)}'),
    "http://example.com/img/logo@2x.png": ("image/png", b"\x89PNG logo2x"),
    "http://example.com/fonts/a.woff2": ("font/woff2", b"wOF2"),
}


class Handler(BaseHTTPRequestHandler):
    throttled_once: set[str] = set()

    def log_message(self, *a):  # keep test output quiet
        pass

    def _send(self, code: int, body: bytes, ctype: str = "text/plain") -> None:
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        if code == 429:
            self.send_header("Retry-After", "0")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        parts = urlsplit(self.path)
        if parts.path == "/cdx/search/cdx":
            return self._cdx(parse_qs(parts.query))
        m = re.match(r"^/web/(\d+)id_/(.+)$", self.path)
        if not m:
            return self._send(404, b"not found")
        original = m.group(2).replace("://www.", "://")  # the archive ignores www.
        if original not in self.throttled_once and original.endswith("bg.jpg"):
            self.throttled_once.add(original)  # prove the client retries 429s
            return self._send(429, b"slow down")
        for ts, url, mime, body in CAPTURES:
            if url.replace("://www.", "://") == original and ts == m.group(1):
                return self._send(200, body, mime)
        if original in UNLISTED:
            mime, body = UNLISTED[original]
            return self._send(200, body, mime)
        return self._send(404, b"not archived")

    def _cdx(self, q):
        exact = "matchType" not in q  # the real API defaults to an exact URL match
        pattern = q["url"][0].rstrip("*")
        host = pattern.split("/")[0]
        to_ts = q.get("to", ["99999999999999"])[0].ljust(14, "9")
        fields = ["urlkey", "timestamp", "original", "mimetype", "statuscode", "length"]
        rows = []
        for ts, url, mime, body in CAPTURES:
            u = urlsplit(url)
            h = u.hostname.removeprefix("www.")
            key = f"{','.join(reversed(h.split('.')))})" + u.path + (f"?{u.query}" if u.query else "")
            here = h + u.path + (f"?{u.query}" if u.query else "")
            if h != host or ts > to_ts:
                continue
            if (here != pattern) if exact else not here.startswith(pattern):
                continue
            rows.append([key, ts, url, mime, "200", str(len(body))])
        rows.sort()
        if "collapse" in q:  # e.g. timestamp:6 -> first capture per month
            n = int(q["collapse"][0].split(":")[1])
            seen, kept = set(), []
            for row in rows:
                if row[1][:n] not in seen:
                    seen.add(row[1][:n])
                    kept.append(row)
            rows = kept
        wanted = q.get("fl", [",".join(fields)])[0].split(",")
        rows = [[row[fields.index(f)] for f in wanted] for row in rows]
        limit = int(q.get("limit", ["100000"])[0])
        start = int(q.get("resumeKey", ["0"])[0])
        page = rows[start:start + limit]
        out = [wanted] + page
        if start + limit < len(rows):
            out += [[], [str(start + limit)]]
        self._send(200, json.dumps(out).encode(), "application/json")


def serve():
    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server, f"http://127.0.0.1:{server.server_address[1]}"
