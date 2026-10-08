import os, json, requests, psycopg

DB = os.environ["DATABASE_URL"]
SITE = os.environ.get("SITE_URL", "http://web:3000")
SECRET = os.environ.get("REVALIDATE_SECRET", "")
INDEXNOW_KEY = os.environ.get("INDEXNOW_KEY", "")


def conn():
    return psycopg.connect(DB, autocommit=True)


def revalidate(paths):
    """Ask Next.js to rebuild these ISR pages now."""
    if not paths:
        return
    try:
        requests.post(f"{SITE}/api/revalidate", params={"secret": SECRET}, json={"paths": list(paths)}, timeout=30)
    except Exception as e:  # never crash the pipeline on a cache miss
        print("revalidate failed:", e)
    indexnow(paths)


def indexnow(paths):
    """Tell IndexNow (Bing, Yandex, DuckDuckGo, Naver...) these pages changed. No-op without INDEXNOW_KEY.
    Google does not use IndexNow; its sitemap and GSC are separate. Max 10,000 URLs per call; we send up to 2,000."""
    if not INDEXNOW_KEY or not paths or not SITE.startswith("https://"):
        return
    host = SITE.split("//", 1)[1].split("/", 1)[0]
    urls = sorted({SITE.rstrip("/") + (p if p.startswith("/") else "/" + p) for p in paths})[:2000]
    body = {"host": host, "key": INDEXNOW_KEY, "keyLocation": f"{SITE.rstrip('/')}/indexnow-key.txt", "urlList": urls}
    try:
        r = requests.post("https://api.indexnow.org/indexnow", json=body, headers={"Content-Type": "application/json; charset=utf-8"}, timeout=30)
        print(f"indexnow: {len(urls)} url(s) -> HTTP {r.status_code}")
    except Exception as e:
        print("indexnow failed:", e)
