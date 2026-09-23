"""Generate pipeline/data/fitments.csv from fitments_v1.py (consumed by pipeline/import_fitments.py)."""
import csv, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from fitments_v1 import F

dest = os.path.join(os.path.dirname(__file__), "..", "..", "pipeline", "data", "fitments.csv")
with open(dest, "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["asin","name","brand","category_slug","price_band","make_slug","model_slug","gen_slug","condition_json","note","source","confidence","rank"])
    for asin, name, brand, cat, band, make, model, gen, cond, note, rank in F:
        conf = 1 if "confirm" in note.lower() else 2
        w.writerow([asin, name, brand, cat, band, make, model, gen, json.dumps(cond), note, "amazon-listing", conf, rank])
print(f"wrote {dest}: {len(F)} rows")
