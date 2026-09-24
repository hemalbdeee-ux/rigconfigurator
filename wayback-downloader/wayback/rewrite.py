"""Find and rewrite links inside HTML and CSS without re-serialising the document.

Regex-based on purpose: a parser round-trip would reformat the archived markup, and
old sites are full of broken HTML we want to keep byte-for-byte apart from the links.
"""
from __future__ import annotations

import html
import re
from typing import Callable
from urllib.parse import urljoin

from .urls import unwrap_wayback

# fn(absolute_url) -> replacement link, or None to leave the reference as it is
LinkFn = Callable[[str], "str | None"]

SKIP_PREFIXES = ("#", "data:", "javascript:", "mailto:", "tel:", "about:", "blob:", "{{", "{%")

TAG_RE = re.compile(r"""<[a-zA-Z][a-zA-Z0-9:-]*(?:[^>"']|"[^"]*"|'[^']*')*>""", re.S)
TAG_NAME_RE = re.compile(r"<([a-zA-Z][a-zA-Z0-9:-]*)")
URL_ATTRS = (
    "href|src|action|poster|background|data|longdesc|formaction|"
    "data-src|data-href|data-original|data-lazy-src|data-bg|data-background|data-url"
)
SRCSET_ATTRS = "srcset|data-srcset|imagesrcset|data-lazy-srcset"
ATTR_RE = re.compile(
    rf"""(?P<pre>\s(?P<name>{URL_ATTRS}|{SRCSET_ATTRS}|style|content)\s*=\s*)"""
    r"""(?:(?P<q>["'])(?P<v1>.*?)(?P=q)|(?P<v2>[^\s"'>]+))""",
    re.I | re.S,
)
SRCSET_NAMES = set(SRCSET_ATTRS.split("|"))
BASE_RE = re.compile(r"""<base\s[^>]*?href\s*=\s*["']?([^"'\s>]+)[^>]*>""", re.I)
STYLE_BLOCK_RE = re.compile(r"(<style\b[^>]*>)(.*?)(</style\s*>)", re.I | re.S)
REFRESH_RE = re.compile(r"(^\s*\d+\s*;\s*url\s*=\s*)(['\"]?)(.+?)\2\s*$", re.I | re.S)

CSS_URL_RE = re.compile(r"""url\(\s*(?P<q>["']?)(?P<u>[^"')]*?)(?P=q)\s*\)""", re.I)
CSS_IMPORT_RE = re.compile(r"""(@import\s+)(?P<q>["'])(?P<u>[^"']+)(?P=q)""", re.I)


def _resolve(raw: str, base: str) -> str | None:
    raw = raw.strip()
    if not raw or raw.lower().startswith(SKIP_PREFIXES):
        return None
    raw = unwrap_wayback(raw)
    try:
        return urljoin(base, raw)
    except ValueError:
        return None


def _swap(raw: str, base: str, fn: LinkFn) -> str | None:
    absolute = _resolve(raw, base)
    if absolute is None:
        return None
    return fn(absolute)


# ---- CSS -----------------------------------------------------------------------


def transform_css(text: str, css_url: str, fn: LinkFn) -> str:
    def url_sub(m: re.Match) -> str:
        new = _swap(m.group("u"), css_url, fn)
        return m.group(0) if new is None else f'url("{new}")'

    def import_sub(m: re.Match) -> str:
        new = _swap(m.group("u"), css_url, fn)
        return m.group(0) if new is None else f'{m.group(1)}"{new}"'

    text = CSS_IMPORT_RE.sub(import_sub, text)
    return CSS_URL_RE.sub(url_sub, text)


# ---- HTML ----------------------------------------------------------------------


def _srcset(value: str, base: str, fn: LinkFn) -> str:
    out = []
    for cand in re.split(r",\s+|,(?=\S+\s)", value.strip()):
        bits = cand.strip().split(None, 1)
        if not bits:
            continue
        new = _swap(bits[0], base, fn)
        out.append(" ".join([new if new is not None else bits[0]] + bits[1:]))
    return ", ".join(out)


def transform_html(text: str, page_url: str, fn: LinkFn) -> str:
    base = page_url
    m = BASE_RE.search(text)
    if m:
        base = urljoin(page_url, unwrap_wayback(html.unescape(m.group(1))))
        # Links are made relative to each file, so a <base> would now point them astray.
        text = text[: m.start()] + text[m.end() :]
        inner = fn

        def fn(u: str, _inner=inner) -> str:  # unresolved links stay absolute, not base-relative
            return _inner(u) or u

    def rewrite_attr(tag_name: str, tag: str) -> str:
        is_refresh = tag_name == "meta" and re.search(r"http-equiv\s*=\s*['\"]?refresh", tag, re.I)

        def attr_sub(am: re.Match) -> str:
            name = am.group("name").lower()
            quoted = am.group("q") is not None
            value = am.group("v1") if quoted else am.group("v2")
            raw = html.unescape(value)
            if name == "style":
                new = transform_css(raw, base, fn)
            elif name == "content":
                if not is_refresh:
                    return am.group(0)
                rm = REFRESH_RE.match(raw)
                if not rm:
                    return am.group(0)
                link = _swap(rm.group(3), base, fn)
                new = raw if link is None else f"{rm.group(1)}{link}"
            elif name in SRCSET_NAMES:
                new = _srcset(raw, base, fn)
            else:
                new = _swap(raw, base, fn)
            if new is None or new == raw:
                return am.group(0)
            q = am.group("q") or '"'
            return f"{am.group('pre')}{q}{html.escape(new, quote=True)}{q}"

        return ATTR_RE.sub(attr_sub, tag)

    def tag_sub(tm: re.Match) -> str:
        tag = tm.group(0)
        name = TAG_NAME_RE.match(tag).group(1).lower()
        return rewrite_attr(name, tag)

    def style_sub(sm: re.Match) -> str:
        return sm.group(1) + transform_css(sm.group(2), base, fn) + sm.group(3)

    text = STYLE_BLOCK_RE.sub(style_sub, text)
    return TAG_RE.sub(tag_sub, text)


def strip_archive_leftovers(text: str) -> str:
    """Remove Wayback toolbar/script injections if a non-raw copy slipped through."""
    text = re.sub(
        r"<!-- BEGIN WAYBACK TOOLBAR INSERT -->.*?<!-- END WAYBACK TOOLBAR INSERT -->",
        "",
        text,
        flags=re.S,
    )
    text = re.sub(
        r"<script[^>]*(?:archive\.org|wombat\.js|playback\.bundle)[^>]*>\s*</script>\s*", "", text
    )
    text = re.sub(r"<link[^>]*(?:banner-styles|iconochive)[^>]*>\s*", "", text)
    text = re.sub(r"\n<!--\s+FILE ARCHIVED ON.*?-->\s*$", "\n", text, flags=re.S)
    return text


def decode(body: bytes) -> tuple[str, str]:
    """Decode losslessly: UTF-8 if it is valid, otherwise latin-1 (round-trips any bytes)."""
    try:
        return body.decode("utf-8"), "utf-8"
    except UnicodeDecodeError:
        return body.decode("latin-1"), "latin-1"
