"""URL helpers: parse user input, normalise URLs, map URLs to local file paths."""
from __future__ import annotations

import hashlib
import posixpath
import re
from dataclasses import dataclass
from urllib.parse import quote, unquote, urlsplit, urlunsplit

# https://web.archive.org/web/20200101000000*/example.com, .../web/2020id_/http://x, /web/2020/x ...
WAYBACK_RE = re.compile(
    r"^(?:(?:https?:)?//(?:web\.)?archive\.org)?/web/(\d{1,14})[a-z_]*\*?/(.+)$", re.I
)

HTML_EXTS = {".html", ".htm", ".xhtml"}
MIME_EXT = {
    "text/html": ".html",
    "application/xhtml+xml": ".html",
    "text/css": ".css",
    "application/javascript": ".js",
    "text/javascript": ".js",
    "application/x-javascript": ".js",
    "application/json": ".json",
    "application/xml": ".xml",
    "text/xml": ".xml",
    "application/rss+xml": ".xml",
    "application/atom+xml": ".xml",
    "text/plain": ".txt",
    "image/jpeg": ".jpg",
    "image/png": ".png",
    "image/gif": ".gif",
    "image/webp": ".webp",
    "image/svg+xml": ".svg",
    "image/x-icon": ".ico",
    "image/vnd.microsoft.icon": ".ico",
    "application/pdf": ".pdf",
    "font/woff": ".woff",
    "font/woff2": ".woff2",
    "application/font-woff": ".woff",
    "font/ttf": ".ttf",
    "application/x-font-ttf": ".ttf",
    "application/vnd.ms-fontobject": ".eot",
}
UNSAFE_CHARS = re.compile(r'[<>:"\\|?*\x00-\x1f]')


@dataclass
class Target:
    """What the user asked for."""

    host: str  # bare host, no www., lowercase
    path_prefix: str  # "/" for the whole site, or a sub-path like "/blog/"
    timestamp: str | None  # 1-14 digit wayback timestamp the user pointed at


def parse_target(text: str) -> Target:
    """Accept 'example.com', 'https://www.example.com/blog/' or a full Wayback URL."""
    text = text.strip()
    timestamp = None
    m = WAYBACK_RE.match(text)
    if m:
        timestamp, text = m.group(1), m.group(2)
    if "://" not in text:
        text = "http://" + text.lstrip("/")
    parts = urlsplit(text)
    host = bare_host(parts.hostname or "")
    if not host or "." not in host:
        raise ValueError(f"Not a valid website address: {text!r}")
    path = parts.path or "/"
    if not path.endswith("/"):
        # "example.com/about" means "that page and below" only when it looks like a folder
        path = path if "." not in path.rsplit("/", 1)[-1] else path.rsplit("/", 1)[0] + "/"
    return Target(host=host, path_prefix=path, timestamp=timestamp)


def bare_host(host: str) -> str:
    host = host.lower().rstrip(".")
    return host[4:] if host.startswith("www.") else host


def unwrap_wayback(url: str) -> str:
    """Turn a web.archive.org/web/<ts>/<original> link back into <original>."""
    m = WAYBACK_RE.match(url.strip())
    if not m:
        return url
    inner = m.group(2)
    if inner.startswith(("http:/", "https:/")) and not inner.startswith(("http://", "https://")):
        inner = inner.replace(":/", "://", 1)  # archive sometimes collapses the double slash
    return inner


def url_key(url: str) -> str | None:
    """Scheme/www/port/fragment-insensitive key used to match links to downloaded files."""
    try:
        parts = urlsplit(url)
    except ValueError:
        return None
    if parts.scheme not in ("http", "https", ""):
        return None
    if not parts.hostname:
        return None
    host = bare_host(parts.hostname)
    path = quote(unquote(parts.path or "/"), safe="/%:@!$&'()*+,;=~-._")
    query = parts.query
    return f"{host}{path}" + (f"?{query}" if query else "")


def _sanitize_segment(seg: str) -> str:
    seg = UNSAFE_CHARS.sub("_", unquote(seg))
    if seg in ("", ".", ".."):
        seg = "_"
    if len(seg.encode()) > 150:
        stem, ext = posixpath.splitext(seg)
        seg = stem[:80] + "_" + hashlib.sha1(seg.encode()).hexdigest()[:8] + ext[:10]
    return seg


def local_path(url: str, mimetype: str, primary_host: str) -> str:
    """Map an original URL to a relative file path inside the restored site.

    / -> index.html, /about/ -> about/index.html, /about (html) -> about/index.html,
    /page.php (html) -> page.php.html, /p?id=3 -> p_q_id=3/index.html,
    files on other hosts (subdomains) -> _hosts/<host>/...
    """
    parts = urlsplit(url)
    host = bare_host(parts.hostname or "")
    path = parts.path or "/"
    is_dir = path.endswith("/")
    raw_segs = path.split("/")[1:]
    if is_dir:
        raw_segs = raw_segs[:-1]
    segs = [_sanitize_segment(s) for s in raw_segs]
    mime = (mimetype or "").split(";")[0].strip().lower()
    is_html = mime in ("text/html", "application/xhtml+xml")

    if parts.query:
        q = re.sub(r"[^A-Za-z0-9._=-]", "_", unquote(parts.query))
        if len(q) > 60:
            q = hashlib.sha1(parts.query.encode()).hexdigest()[:12]
        if is_dir or not segs:
            segs.append("_q_" + q)
        else:
            stem, ext = posixpath.splitext(segs[-1])
            segs[-1] = f"{stem}_q_{q}{ext}"
        is_dir = False

    if is_dir:
        segs.append("index.html")
    else:
        ext = posixpath.splitext(segs[-1])[1].lower()
        if is_html:
            if not ext:
                segs.append("index.html")
            elif ext not in HTML_EXTS:
                segs[-1] += ".html"
        elif not ext and mime in MIME_EXT:
            segs[-1] += MIME_EXT[mime]

    prefix = [] if host == primary_host else ["_hosts", host]
    return "/".join(prefix + segs)


def relative_link(from_file: str, to_file: str) -> str:
    rel = posixpath.relpath(to_file, posixpath.dirname(from_file) or ".")
    return quote(rel, safe="/._-~!$*+,;=:@%")


def with_fragment(link: str, url: str) -> str:
    frag = urlsplit(url).fragment
    return f"{link}#{frag}" if frag else link


def strip_fragment(url: str) -> str:
    p = urlsplit(url)
    return urlunsplit((p.scheme, p.netloc, p.path, p.query, ""))
