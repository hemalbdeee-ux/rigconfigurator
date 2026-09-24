"""Generate pipeline/data/fitments.csv from fitments_v1.py + fitments_v2.py (consumed by pipeline/import_fitments.py)."""
import csv, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from fitments_v1 import F as F1
from fitments_v2 import F as F2
from build_articles_sql import modules
F3 = []
for m in modules():
    make, model, gen, cat = m.KEY
    for i, (asin, name, brand, band, cond, note) in enumerate(m.FITS, 1):
        F3.append((asin, name, brand, cat, band, make, model, gen, cond, note, i))
owned = {m.KEY for m in modules()}  # pages whose product list is owned by an article module
F = [r for r in F1 + F2 if (r[5], r[6], r[7], r[3]) not in owned] + F3

dest = os.path.join(os.path.dirname(__file__), "..", "..", "pipeline", "data", "fitments.csv")
with open(dest, "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["asin","name","brand","category_slug","price_band","make_slug","model_slug","gen_slug","condition_json","note","source","confidence","rank"])
    for asin, name, brand, cat, band, make, model, gen, cond, note, rank in F:
        conf = 1 if "confirm" in note.lower() else 2
        w.writerow([asin, name, brand, cat, band, make, model, gen, json.dumps(cond), note, "amazon-listing", conf, rank])
print(f"wrote {dest}: {len(F)} rows (v1 {len(F1)} + v2 {len(F2)} + articles {len(F3)})")
