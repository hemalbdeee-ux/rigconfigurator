"""Submit every URL in the live sitemap to IndexNow once (first-time seeding, or after a big content push).
Usage: docker exec rigconfigurator-pipeline python indexnow_all.py
Needs INDEXNOW_KEY in .env; the regular cron jobs then keep IndexNow updated page by page via common.revalidate().
"""
import re, requests
from common import SITE, INDEXNOW_KEY, indexnow

if not INDEXNOW_KEY:
    raise SystemExit("INDEXNOW_KEY is not set; add it to .env and `docker compose up -d web pipeline`")
xml = requests.get(f"{SITE}/sitemap.xml", timeout=60).text
urls = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", xml)
paths = [u.split("//", 1)[1].split("/", 1)[1] if "/" in u.split("//", 1)[1] else "" for u in urls]
print(f"sitemap: {len(urls)} url(s)")
indexnow(["/" + p for p in paths])
