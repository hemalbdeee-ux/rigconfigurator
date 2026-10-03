"""Validate db/content/pillars/*.py modules. Usage: python3 db/content/validate_pillars.py [files...]"""
import importlib.util, json, re, sys, glob, os

FORBIDDEN = re.compile(r"\b(we tested|our testing|we installed|hands-on test|our truck|our car|after \d[\d,]* miles|we drove)\b", re.I)
CATS = {"tonneau-covers","bed-racks","roof-racks","cargo-boxes","hitches","bike-racks","floor-mats","seat-covers","running-boards","led-light-bars","dash-cams","lift-kits"}

def words(o):
    if isinstance(o, str): return len(o.split())
    if isinstance(o, dict): return sum(words(v) for k, v in o.items() if k not in ("author", "reviewed", "category", "sources"))
    if isinstance(o, (list, tuple)): return sum(words(v) for v in o)
    return 0

def check(path):
    spec = importlib.util.spec_from_file_location("m", path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    errs, a = [], m.ARTICLE
    for k in ("KIND", "CATEGORIES", "TITLE", "META", "FAQ", "ARTICLE"):
        if not hasattr(m, k): errs.append(f"missing {k}")
    if errs: return errs, 0
    if m.KIND not in ("upgrades", "explainer"): errs.append("KIND must be upgrades|explainer")
    if m.KIND == "upgrades" and not (hasattr(m, "KEY") and len(m.KEY) == 3): errs.append("upgrades needs KEY=(make, model, gen)")
    if m.KIND == "explainer" and not (hasattr(m, "SLUG") and re.fullmatch(r"[a-z0-9-]+", m.SLUG)): errs.append("explainer needs SLUG (a-z0-9-)")
    if not set(m.CATEGORIES) <= CATS: errs.append(f"unknown categories {set(m.CATEGORIES) - CATS}")
    if len(m.TITLE) > 100: errs.append(f"TITLE {len(m.TITLE)} > 100 chars")
    if not 110 <= len(m.META) <= 165: errs.append(f"META {len(m.META)} chars (110-165)")
    if not 8 <= len(m.FAQ) <= 12: errs.append(f"FAQ {len(m.FAQ)} (8-12)")
    if len(a.get("takeaways", [])) != 5: errs.append("takeaways must be 5")
    for k in ("dek", "verdict", "author", "reviewed"):
        if k not in a: errs.append(f"ARTICLE missing {k}")
    if len(a.get("sources", [])) < 4: errs.append("need >= 4 sources")
    if m.KIND == "upgrades":
        pr = a.get("priority", [])
        if not 3 <= len(pr) <= 8: errs.append(f"priority {len(pr)} (3-8)")
        for p in pr:
            if p.get("category") not in m.CATEGORIES: errs.append(f"priority category {p.get('category')} not in CATEGORIES")
            if len(p.get("why", "").split()) < 90: errs.append(f"priority '{p.get('h')}' why < 90 words")
        if "tier_table" not in a: errs.append("upgrades needs tier_table")
        need = 2800
    else:
        if len(a.get("sections", [])) < 5: errs.append("explainer needs >= 5 sections")
        if "compare_table" not in a: errs.append("explainer needs compare_table")
        if len(a.get("decision", [])) < 3: errs.append("explainer needs >= 3 decision rows")
        need = 2500
    blob = json.dumps(a, ensure_ascii=False) + json.dumps(m.FAQ, ensure_ascii=False) + m.TITLE + m.META
    if "$p$" in blob: errs.append("content contains $p$")
    for hit in FORBIDDEN.findall(blob): errs.append(f"forbidden phrase: {hit}")
    n = words(a) + words(m.FAQ)
    if n < need: errs.append(f"{n} words < {need}")
    return errs, n

if __name__ == "__main__":
    files = sys.argv[1:] or sorted(p for p in glob.glob(os.path.join(os.path.dirname(__file__), "pillars", "*.py")) if not p.endswith("__init__.py"))
    bad = 0
    for f in files:
        errs, n = check(f)
        print(("PASS " if not errs else "FAIL ") + os.path.basename(f) + f" ({n}w)")
        for e in errs: print("   ✗", e)
        bad += bool(errs)
    sys.exit(1 if bad else 0)
