"""Hourly deals board: flag products whose live price is ≥20% under their 90-day average (Keepa) or stored band.
Keepa optional — without a key, uses price_cents vs price_band midpoint as a crude proxy.
"""
import os, re
from common import conn, revalidate

KEEPA = os.environ.get("KEEPA_KEY")


def band_mid(band):
    nums = [int(n.replace(",", "")) for n in re.findall(r"\$?(\d[\d,]*)", band or "")]
    return (sum(nums) / len(nums)) * 100 if nums else None


with conn() as c:
    c.execute("UPDATE deals SET active=false WHERE seen_at < now() - interval '48 hours'")
    rows = c.execute("SELECT id, asin, price_cents, price_band FROM products WHERE active AND price_cents IS NOT NULL").fetchall()
    n = 0
    for pid, asin, cents, band in rows:
        avg = None
        if KEEPA:
            pass  # TODO: keepa.Keepa(KEEPA).query(asin) → stats['avg90'] (in cents) — add when key is set
        avg = avg or band_mid(band)
        if not avg:
            continue
        drop = round((1 - cents / avg) * 100, 1)
        if drop >= 20:
            c.execute("INSERT INTO deals (product_id, price_cents, avg90_cents, drop_pct) VALUES (%s,%s,%s,%s)", (pid, cents, int(avg), drop))
            n += 1
print(f"{n} deals flagged")
revalidate(["/deals"])
