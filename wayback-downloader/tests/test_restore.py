import json
import zipfile

import pytest

from wayback import Archive, Options, Restorer, parse_target
from wayback.rewrite import transform_css, transform_html
from wayback.urls import local_path, unwrap_wayback, url_key

from .fake_archive import serve


@pytest.fixture(scope="module")
def base():
    server, url = serve()
    yield url
    server.shutdown()


def restore(base, tmp_path, target="example.com", **opts):
    opts.setdefault("min_interval", 0)
    r = Restorer(target, tmp_path, Options(**opts), Archive(base=base, min_interval=0))
    r.run()
    return r


# ---- units -------------------------------------------------------------------------


def test_parse_target_variants():
    t = parse_target("https://web.archive.org/web/20190615000000*/www.Example.com/")
    assert (t.host, t.path_prefix, t.timestamp) == ("example.com", "/", "20190615000000")
    t = parse_target("https://web.archive.org/web/2019id_/http://example.com/blog/")
    assert (t.host, t.path_prefix, t.timestamp) == ("example.com", "/blog/", "2019")
    assert parse_target("example.com/about.html").path_prefix == "/"
    with pytest.raises(ValueError):
        parse_target("not a site")


def test_local_paths():
    h = "example.com"
    assert local_path("http://example.com/", "text/html", h) == "index.html"
    assert local_path("http://www.example.com/about", "text/html", h) == "about/index.html"
    assert local_path("http://example.com/a/b/", "text/html", h) == "a/b/index.html"
    assert local_path("http://example.com/p.php?id=3&x=1", "text/html", h) == "p_q_id=3_x=1.php.html"
    assert local_path("http://example.com/feed", "application/rss+xml", h) == "feed.xml"
    assert local_path("http://example.com/x.png", "image/png", h) == "x.png"
    assert local_path("http://cdn.example.com/x.png", "image/png", h) == "_hosts/cdn.example.com/x.png"


def test_url_key_and_unwrap():
    assert url_key("https://www.example.com:443/a#frag") == url_key("http://example.com/a")
    assert unwrap_wayback("https://web.archive.org/web/2019im_/http://example.com/x.png") == "http://example.com/x.png"
    assert unwrap_wayback("/web/20190101000000/https:/example.com/") == "https://example.com/"


def test_rewrite_leaves_other_markup_alone():
    html = '<p class=x>Hi</p><img alt="a" src=/a.png><a href="#top">t</a><a href="mailto:x@y">m</a>'
    out = transform_html(html, "http://example.com/", lambda u: "LOCAL")
    assert out == '<p class=x>Hi</p><img alt="a" src="LOCAL"><a href="#top">t</a><a href="mailto:x@y">m</a>'
    css = 'a{background:url(img/a.png)} b{background:url("data:image/png;base64,xx")}'
    assert transform_css(css, "http://e.com/c/s.css", lambda u: u) == (
        'a{background:url("http://e.com/c/img/a.png")} b{background:url("data:image/png;base64,xx")}'
    )


# ---- end to end ----------------------------------------------------------------------


def test_full_restore(base, tmp_path):
    r = restore(base, tmp_path, target="https://web.archive.org/web/20200101000000/http://example.com/")
    site = tmp_path / "site"

    home = (site / "index.html").read_text()
    assert "<base" not in home and "WAYBACK TOOLBAR" not in home
    assert 'href="css/site_q_v=2.css"' in home
    assert 'href="about/index.html"' in home
    assert 'href="blog/post_q_id=3_x=1.php.html#top"' in home
    assert 'src="img/logo.png"' in home and 'srcset="img/logo.png 1x, img/logo@2x.png 2x"' in home
    assert 'href="contact/index.html"' in home  # web.archive.org link unwrapped
    assert 'href="http://other.org/"' in home  # external link untouched
    assert 'href="http://www.example.com/never-archived"' in home  # base removed -> absolute
    assert 'url(&quot;img/bg.jpg&quot;)' in home
    assert 'content="300; url=about/index.html"' in home

    # timestamp picks the 2019 capture, not the 2025 one
    assert "NEW about" not in (site / "about/index.html").read_text()
    assert 'href="../index.html"' in (site / "about/index.html").read_text()

    # latin-1 page kept byte-exact apart from links
    contact = (site / "contact/index.html").read_bytes()
    assert b"caf\xe9" in contact and b'src="../img/logo.png"' in contact

    css = (site / "css/site_q_v=2.css").read_text()
    assert '@import "fonts.css"' in css and 'url("../img/bg.jpg")' in css
    # files that were never in the index were discovered through links (3 levels deep)
    assert (site / "css/fonts.css").exists()
    assert (site / "fonts/a.woff2").read_bytes() == b"wOF2"
    assert (site / "img/logo@2x.png").exists()
    assert (site / "img/bg.jpg").read_bytes() == b"\xff\xd8 bg"  # survived a 429

    with zipfile.ZipFile(r.zip_path) as zf:
        assert "example.com/index.html" in zf.namelist()
    report = json.loads((tmp_path / "report.json").read_text())
    assert report["files"] == 10 and report["failed"] == []


def test_latest_and_resume(base, tmp_path):
    restore(base, tmp_path, make_zip=False)
    assert "NEW about" in (tmp_path / "site/about/index.html").read_text()
    # Second run resumes from the manifest and downloads nothing again.
    r = restore(base, tmp_path, make_zip=False)
    assert r.progress.downloaded == 0 and r.progress.skipped > 0


def test_paging_and_prefix(base, tmp_path):
    arch = Archive(base=base, min_interval=0)
    caps = list(arch.iter_captures("example.com/", page_size=2))
    assert len(caps) == 9
    r = restore(base, tmp_path, target="example.com/img/", fetch_missing=False, make_zip=False)
    assert sorted(e.path for e in r.entries.values()) == ["img/bg.jpg", "img/logo.png"]


def test_unknown_site(base, tmp_path):
    with pytest.raises(Exception, match="no captures"):
        restore(base, tmp_path, target="nothing-here.com")
