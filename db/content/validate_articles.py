"""Quality gate for db/content/articles/*.py — run before building 007_articles.sql.
python db/content/validate_articles.py [file ...]   → prints PASS/FAIL per article; exit 1 on any FAIL.
"""
import glob, importlib.util, json, os, re, sys

HERE = os.path.dirname(__file__)
BANNED = [r"\bwe tested\b", r"\bour test(ing|s)?\b", r"\bwe installed\b", r"\bhands-on\b", r"\bin our experience\b",
          r"\bwe drove\b", r"\bwe put .* through\b", r"\bafter \d[\d,]* miles\b", r"\bour (truck|rig|suv)\b"]
REQ_ART = ["dek", "author", "reviewed", "method", "takeaways", "top_picks", "look_for", "look_table", "picks", "install", "avoid", "verdict", "sources"]
ASIN = re.compile(r"^B0[A-Z0-9]{8}$")


def words(x):
    return len(re.findall(r"[A-Za-z0-9']+", re.sub(r"https?://\S+", "", json.dumps(x, ensure_ascii=False))))


def check(path):
    spec = importlib.util.spec_from_file_location("m", path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    errs, warn = [], []
    for k in ("KEY", "TITLE", "META", "FAQ", "ARTICLE", "FITS"):
        if not hasattr(m, k): errs.append(f"missing {k}")
    if errs: return errs, warn, 0
    A = m.ARTICLE
    for k in REQ_ART:
        if k not in A: errs.append(f"ARTICLE missing '{k}'")
    if A.get("author") != "jake-morrison": errs.append("author must be 'jake-morrison'")
    fit_asins = [r[0] for r in m.FITS]
    for r in m.FITS:
        if len(r) != 6: errs.append(f"FITS row wrong shape: {r[:2]}")
        if not ASIN.match(r[0]): errs.append(f"bad ASIN {r[0]}")
        if not isinstance(r[4], dict): errs.append(f"cond not dict for {r[0]}")
    if len(set(fit_asins)) != len(fit_asins): errs.append("duplicate ASIN in FITS")
    for p in A.get("picks", []):
        if p["asin"] not in fit_asins: errs.append(f"pick {p['asin']} not in FITS")
        for k in ("asin", "role", "price", "pros", "cons", "body", "who", "specs"):
            if k not in p: errs.append(f"pick {p.get('asin')} missing {k}")
        if len(p.get("pros", [])) < 3 or len(p.get("cons", [])) < 2: errs.append(f"pick {p['asin']} needs ≥3 pros, ≥2 cons")
        if words(p.get("body", "")) < 120: warn.append(f"pick {p['asin']} body short ({words(p.get('body',''))}w)")
        if len(p.get("specs", [])) < 5: warn.append(f"pick {p['asin']} <5 spec rows")
    for t in A.get("top_picks", []):
        if t["asin"] not in [p["asin"] for p in A.get("picks", [])]: errs.append(f"top_pick {t['asin']} not in picks")
    if not (4 <= len(A.get("picks", [])) <= 8): errs.append(f"picks count {len(A.get('picks', []))} (want 4-8)")
    if len(m.FAQ) < 8: errs.append(f"FAQ {len(m.FAQ)} (<8)")
    if len(A.get("sources", [])) < 5: errs.append(f"sources {len(A.get('sources', []))} (<5)")
    if len(A.get("takeaways", [])) < 4: errs.append("takeaways < 4")
    if not (40 <= len(m.TITLE) <= 110): warn.append(f"title length {len(m.TITLE)}")
    if not (110 <= len(m.META) <= 170): warn.append(f"meta length {len(m.META)}")
    text = json.dumps([A, m.FAQ], ensure_ascii=False)
    for b in BANNED:
        if re.search(b, text, re.I): errs.append(f"banned claim /{b}/")
    if "$a$" in text or "$t$" in text or "$f$" in text or "$m$" in text: errs.append("dollar-quote delimiter inside text")
    n = words([A, m.FAQ])
    if n < 3000: errs.append(f"only {n} words (<3000)")
    return errs, warn, n


if __name__ == "__main__":
    files = sys.argv[1:] or sorted(f for f in glob.glob(os.path.join(HERE, "articles", "*.py")) if not f.endswith("__init__.py"))
    bad = 0
    for f in files:
        e, w, n = check(f)
        print(f"{'PASS' if not e else 'FAIL'} {os.path.basename(f)} ({n}w)" + "".join(f"\n   ✗ {x}" for x in e) + "".join(f"\n   · {x}" for x in w))
        bad += bool(e)
    sys.exit(1 if bad else 0)
