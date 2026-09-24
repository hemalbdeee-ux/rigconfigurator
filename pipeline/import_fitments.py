"""Import fitments from a CSV compiled from manufacturer fit guides / Amazon listings.

CSV columns (data/fitments.csv):
asin,name,brand,category_slug,price_band,make_slug,model_slug,gen_slug,condition_json,note,source,confidence,rank
Run: docker exec rigconfigurator-pipeline python import_fitments.py data/fitments.csv
"""
import csv, json, sys
from common import conn, revalidate

path = sys.argv[1] if len(sys.argv) > 1 else "data/fitments.csv"
touched = set()
with conn() as c, open(path, newline="", encoding="utf-8") as f:
    for r in csv.DictReader(f):
        c.execute(
            """INSERT INTO products (asin, category_id, name, brand, price_band)
               VALUES (%s, (SELECT id FROM categories WHERE slug=%s), %s, %s, %s)
               ON CONFLICT (asin) DO UPDATE SET active=TRUE, category_id=EXCLUDED.category_id, name=EXCLUDED.name, brand=EXCLUDED.brand, price_band=EXCLUDED.price_band, updated_at=now()""",
            (r["asin"], r["category_slug"], r["name"], r["brand"], r["price_band"]))
        c.execute(
            """INSERT INTO fitments (product_id, vehicle_id, condition, note, source, confidence, rank)
               VALUES ((SELECT id FROM products WHERE asin=%s),
                       (SELECT v.id FROM vehicles v JOIN makes m ON m.id=v.make_id WHERE m.slug=%s AND v.model_slug=%s AND v.gen_slug=%s),
                       %s::jsonb, %s, %s, %s, %s)
               ON CONFLICT (product_id, vehicle_id, condition) DO UPDATE SET note=EXCLUDED.note, source=EXCLUDED.source, confidence=EXCLUDED.confidence, rank=EXCLUDED.rank""",
            (r["asin"], r["make_slug"], r["model_slug"], r["gen_slug"], r.get("condition_json") or "{}", r.get("note"), r.get("source"), int(r.get("confidence") or 2), int(r.get("rank") or 100)))
        touched.add(f"/vehicles/{r['make_slug']}/{r['model_slug']}/{r['gen_slug']}/{r['category_slug']}")
        touched.add(f"/vehicles/{r['make_slug']}/{r['model_slug']}/{r['gen_slug']}")
print(f"imported; revalidating {len(touched)} pages")
revalidate(touched)
