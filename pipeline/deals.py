"""Hourly deals board: a product is a deal when today's Amazon price is at least 10% under its own 30-day high in
price_history (written by refresh_prices.py), and that history is at least MIN_DAYS old. No editorial bands, no
guessing: every figure shown on /deals was returned by the Creators API and carries its time stamp.
"""
from common import conn, revalidate

MIN_DAYS = 14      # do not call anything a drop until two weeks of prices exist for that product
MIN_DROP = 10.0    # percent under the 30-day high

with conn() as c:
    c.execute("UPDATE deals SET active=false WHERE seen_at < now() - interval '48 hours'")
    rows = c.execute("""
        SELECT p.id, p.price_cents, h.hi, h.first_seen
        FROM products p
        JOIN LATERAL (SELECT max(price_cents) AS hi, min(checked_at) AS first_seen
                      FROM price_history WHERE product_id=p.id AND checked_at > now() - interval '30 days') h ON true
        WHERE p.active AND p.price_cents IS NOT NULL AND p.price_checked_at > now() - interval '23 hours'
          AND h.first_seen < now() - make_interval(days => %s)
          AND p.price_cents <= h.hi * (1 - %s / 100.0)""", (MIN_DAYS, MIN_DROP)).fetchall()
    n = 0
    for pid, cents, hi, _ in rows:
        drop = round((1 - cents / hi) * 100, 1)
        # one active row per product; refresh it rather than stacking duplicates every hour
        c.execute("UPDATE deals SET active=false WHERE product_id=%s AND active", (pid,))
        c.execute("INSERT INTO deals (product_id, price_cents, avg90_cents, drop_pct) VALUES (%s,%s,%s,%s)", (pid, cents, int(hi), drop))
        n += 1
print(f"{n} deals flagged")
revalidate(["/deals"])
