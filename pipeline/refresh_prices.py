"""Refresh price/image/rating from Amazon PA-API 5 (needs an approved Associates account with 3+ sales).
Until then this script exits quietly and pages show price_band text — which is TOS-safe.
"""
import os, time
from common import conn, revalidate

KEY, SECRET, TAG = os.environ.get("PAAPI_ACCESS_KEY"), os.environ.get("PAAPI_SECRET_KEY"), os.environ.get("AMAZON_TAG")
if not KEY or not SECRET:
    print("PA-API keys not set; skipping price refresh")
    raise SystemExit(0)

from amazon_paapi import AmazonApi  # python-amazon-paapi

api = AmazonApi(KEY, SECRET, TAG, "US", throttling=1.1)
touched = set()
with conn() as c:
    rows = c.execute("SELECT id, asin FROM products WHERE active AND (price_checked_at IS NULL OR price_checked_at < now() - interval '24 hours') ORDER BY price_checked_at NULLS FIRST LIMIT 500").fetchall()
    for i in range(0, len(rows), 10):
        batch = rows[i:i + 10]
        try:
            items = api.get_items([asin for _, asin in batch])
        except Exception as e:
            print("paapi error:", e); time.sleep(5); continue
        for item in items:
            price = getattr(getattr(item.offers, "listings", [None])[0], "price", None) if item.offers else None
            cents = int(round(price.amount * 100)) if price and price.amount else None
            img = item.images.primary.large.url if item.images and item.images.primary else None
            c.execute("UPDATE products SET price_cents=%s, image_url=COALESCE(%s, image_url), price_checked_at=now() WHERE asin=%s", (cents, img, item.asin))
        for pid, _ in batch:
            for (p,) in c.execute("""SELECT '/vehicles/'||m.slug||'/'||v.model_slug||'/'||v.gen_slug||'/'||cat.slug
                                     FROM fitments f JOIN vehicles v ON v.id=f.vehicle_id JOIN makes m ON m.id=v.make_id
                                     JOIN products p ON p.id=f.product_id JOIN categories cat ON cat.id=p.category_id WHERE f.product_id=%s""", (pid,)):
                touched.add(p)
print(f"refreshed {len(rows)} products; revalidating {len(touched)} pages")
revalidate(touched)
