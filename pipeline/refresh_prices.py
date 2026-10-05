"""Refresh price and image link from the Amazon Creators API (the replacement for PA-API 5).

Needs three values from Associates Central > Tools > Creators API, set in .env next to docker-compose.yml:
  CREATORS_CREDENTIAL_ID, CREATORS_CREDENTIAL_SECRET, CREATORS_VERSION   (plus AMAZON_TAG)
Without them this script exits quietly and pages show price_band text.

Amazon's Associates Program Policies decide the storage rules used here:
- price data may be cached for up to 24 hours, and an image link may be stored for up to 24 hours;
- a price shown from the API needs a date/time stamp next to it (the site adds it from price_checked_at).
So every run re-checks products older than REFRESH_AFTER and then clears any price or Amazon image link
older than EXPIRE_AFTER. The v_fitment view (migration 012) applies the same cutoff on the read side.

Usage:
  python refresh_prices.py            # normal run (cron, every 6 hours)
  python refresh_prices.py --check    # one small API call, prints the result, writes nothing
"""
import os, sys, time
from common import conn, revalidate

CID = os.environ.get("CREATORS_CREDENTIAL_ID")
CSECRET = os.environ.get("CREATORS_CREDENTIAL_SECRET")
CVERSION = os.environ.get("CREATORS_VERSION")
TAG = os.environ.get("AMAZON_TAG")
REFRESH_AFTER = "5 hours"    # cron runs every 6 hours, so every active product is re-checked on every run
EXPIRE_AFTER = "23 hours"    # stay inside Amazon's 24 hour limit even if a run is late
CHECK = "--check" in sys.argv

EXPIRE_SQL = f"""UPDATE products SET price_cents=NULL,
       image_url=CASE WHEN image_url ~* 'amazon' THEN NULL ELSE image_url END
 WHERE price_checked_at < now() - interval '{EXPIRE_AFTER}'
   AND (price_cents IS NOT NULL OR image_url ~* 'amazon')"""


def expire(c):
    n = c.execute(EXPIRE_SQL).rowcount
    if n:
        print(f"expired {n} stale price/image value(s)")


missing = [k for k, v in (("CREATORS_CREDENTIAL_ID", CID), ("CREATORS_CREDENTIAL_SECRET", CSECRET),
                          ("CREATORS_VERSION", CVERSION), ("AMAZON_TAG", TAG)) if not v]
if missing:
    print("Creators API not configured (missing " + ", ".join(missing) + "); skipping price refresh")
    if not CHECK:
        with conn() as c:
            expire(c)
    raise SystemExit(0)

from amazon_creatorsapi import AmazonCreatorsApi, Country
from amazon_creatorsapi.models import GetItemsResource as R
from amazon_creatorsapi.errors import (AccessDeniedError, AmazonCreatorsApiError, AssociateValidationError,
                                       AuthenticationError, ItemsNotFoundError, TooManyRequestsError)

RESOURCES = [R.ITEM_INFO_DOT_TITLE, R.IMAGES_DOT_PRIMARY_DOT_LARGE, R.OFFERS_V2_DOT_LISTINGS_DOT_PRICE,
             R.OFFERS_V2_DOT_LISTINGS_DOT_CONDITION]
FATAL = (AuthenticationError, AccessDeniedError, AssociateValidationError)
api = AmazonCreatorsApi(CID, CSECRET, CVERSION, TAG, Country.US, throttling=1.1)


def price_cents(item):
    """Lowest new-condition USD price in cents (Associates policy: show the lowest new price), or None."""
    listings = (getattr(item.offers_v2, "listings", None) or []) if item.offers_v2 else []
    cents = []
    for l in listings:
        cond = getattr(getattr(l, "condition", None), "value", None)
        if cond and str(cond).lower() != "new":
            continue
        money = getattr(getattr(l, "price", None), "money", None)
        if money and money.amount is not None and (not money.currency or money.currency == "USD"):
            cents.append(int(round(float(money.amount) * 100)))
    return min(cents) if cents else None


def image_url(item):
    try:
        return item.images.primary.large.url
    except AttributeError:
        return None


def explain(e):
    print(f"Creators API refused the request: {type(e).__name__}: {e}")
    print("Check CREATORS_CREDENTIAL_ID / CREATORS_CREDENTIAL_SECRET / CREATORS_VERSION and AMAZON_TAG in .env, "
          "and that the credential is active for the US store in Associates Central.")


if CHECK:
    with conn() as c:
        asins = [a for (a,) in c.execute("SELECT asin FROM products WHERE active ORDER BY id LIMIT 3").fetchall()]
    try:
        items = api.get_items(asins, resources=RESOURCES, include_unavailable=True)
    except FATAL as e:
        explain(e); raise SystemExit(2)
    except AmazonCreatorsApiError as e:
        print(f"Creators API error: {type(e).__name__}: {e}"); raise SystemExit(1)
    for it in items:
        title = getattr(getattr(getattr(it, "item_info", None), "title", None), "display_value", None)
        cents = price_cents(it)
        print(f"{it.asin} | {'$%.2f' % (cents / 100) if cents else 'no offer'} | image {'yes' if image_url(it) else 'no'} | {(title or '')[:60]}")
    print(f"check OK: {len(items)} item(s) returned; nothing was written")
    raise SystemExit(0)

touched, done, priced, throttled = set(), 0, 0, 0
with conn() as c:
    rows = c.execute(f"""SELECT id, asin FROM products WHERE active
                          AND (price_checked_at IS NULL OR price_checked_at < now() - interval '{REFRESH_AFTER}')
                          ORDER BY price_checked_at NULLS FIRST LIMIT 1500""").fetchall()
    for i in range(0, len(rows), 10):
        batch = rows[i:i + 10]
        asins = [asin for _, asin in batch]
        try:
            items = list(api.get_items(asins, resources=RESOURCES, include_unavailable=True))
        except ItemsNotFoundError:
            items = []                      # none of this batch is sold any more: clear them below
        except FATAL as e:
            explain(e); break               # wrong or inactive credential: stop instead of retrying 80 times
        except TooManyRequestsError as e:
            throttled += 1
            print("rate limited:", e)
            if throttled >= 3:
                print("stopping this run after 3 rate-limit errors; the next run continues"); break
            time.sleep(30); continue
        except AmazonCreatorsApiError as e:
            print("creators api error:", type(e).__name__, e); time.sleep(5); continue
        got = {it.asin: it for it in items}
        for pid, asin in batch:
            it = got.get(asin)
            cents = price_cents(it) if it else None
            c.execute("UPDATE products SET price_cents=%s, image_url=%s, price_checked_at=now() WHERE id=%s",
                      (cents, image_url(it) if it else None, pid))
            done += 1; priced += 1 if cents else 0
            for (p,) in c.execute("""SELECT DISTINCT unnest(ARRAY[
                                       '/vehicles/'||m.slug||'/'||v.model_slug||'/'||v.gen_slug,
                                       '/vehicles/'||m.slug||'/'||v.model_slug||'/'||v.gen_slug||'/'||cat.slug])
                                     FROM fitments f JOIN vehicles v ON v.id=f.vehicle_id JOIN makes m ON m.id=v.make_id
                                     JOIN products p ON p.id=f.product_id JOIN categories cat ON cat.id=p.category_id
                                     WHERE f.product_id=%s""", (pid,)):
                touched.add(p)
    expire(c)
print(f"checked {done} of {len(rows)} products ({priced} with a price); revalidating {len(touched)} pages")
revalidate(touched)
