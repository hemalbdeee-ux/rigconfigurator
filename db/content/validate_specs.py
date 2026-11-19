"""Validate db/content/specs/*.py. Exit 1 on any error. Rules: db/content/specs/WRITING_BRIEF.md."""
import glob, importlib.util, os, re, sys
here = os.path.dirname(__file__)
TOPICS = {"towing-capacity", "payload-capacity", "bed-dimensions", "cargo-space", "bolt-pattern", "tire-size", "wiper-blade-size",
          "oil-type-capacity", "battery-size", "gas-tank-size", "headlight-bulb-size", "ground-clearance", "hitch-receiver-size",
          "roof-load-limit", "air-filters", "dimensions"}
BAD_HOSTS = ("amazon.", "reddit.", "forum", "wikipedia.", "carid.", "realtruck.")   # not sources for a maker figure

def modules():
    for p in sorted(glob.glob(os.path.join(here, "specs", "*.py"))):
        spec = importlib.util.spec_from_file_location(os.path.basename(p)[:-3], p)
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); yield os.path.basename(p), m

def check(name, m):
    e = []
    for k in ("KEY", "MAKE", "MODEL", "TOPIC_LABEL", "PUBLISH", "TITLE", "SEO_TITLE", "META", "FAQ", "PAGE"):
        if not hasattr(m, k): e.append(f"missing {k}")
    if e: return e
    make, model, topic = m.KEY
    if topic not in TOPICS: e.append(f"unknown topic {topic}")
    if not re.fullmatch(r"[a-z0-9-]+", make + model): e.append("slugs must be lowercase a-z, 0-9, -")
    if len(m.SEO_TITLE) > 60: e.append(f"SEO_TITLE {len(m.SEO_TITLE)} > 60")
    if not 70 <= len(m.META) <= 155: e.append(f"META length {len(m.META)} not 70-155")
    at = getattr(m, "PUBLISH_AT", None)
    if at is not None and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", at): e.append("PUBLISH_AT must be YYYY-MM-DD")
    p = m.PAGE
    for k in ("answer", "reviewed", "covers", "sections", "check", "sources"):
        if not p.get(k): e.append(f"PAGE.{k} empty")
    if e: return e
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", p["reviewed"]): e.append("reviewed must be YYYY-MM-DD")
    n_src = len(p["sources"])
    for label, url in p["sources"]:
        if not url.startswith("https://"): e.append(f"source not https: {url}")
        if any(b in url for b in BAD_HOSTS): e.append(f"not a maker source: {url}")
    used = set()
    for s in p["sections"]:
        t = s.get("table")
        if not t or not t.get("rows"): e.append(f"section {s.get('id')} has no table rows"); continue
        for r in t["rows"]:
            if len(r) != len(t["head"]) + 1: e.append(f"section {s['id']}: row width {len(r)} != head {len(t['head'])} + source"); continue
            src = r[-1] if isinstance(r[-1], list) else [r[-1]]      # one source number, or several when sources agree
            if not src or not all(isinstance(x, int) and 1 <= x <= n_src for x in src): e.append(f"section {s['id']}: row {r[0]!r} has no valid source number")
            else: used.update(src)
            if any(isinstance(c, str) and re.search(r"\b(TBD|TODO|unknown|approx)\b", c, re.I) for c in r[:-1]): e.append(f"section {s['id']}: placeholder in row {r[0]!r}")
    for i in range(1, n_src + 1):
        if i not in used: e.append(f"source {i} is cited by no row")
    words = len(" ".join([p["answer"], *p["check"], *[s.get("intro", "") for s in p["sections"]], *[n for s in p["sections"] for n in s.get("notes", [])], *[a for _, a in m.FAQ]]).split())
    if words > 900: e.append(f"{words} words outside tables (> 900)")
    return e

if __name__ == "__main__":
    bad = 0
    for name, m in modules():
        errs = check(name, m)
        print(("FAIL " if errs else "PASS ") + name + ("" if not errs else "\n   · " + "\n   · ".join(errs)) + ("" if errs or m.PUBLISH else "  (draft, not published)"))
        bad += bool(errs)
    sys.exit(1 if bad else 0)
