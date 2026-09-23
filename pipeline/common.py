import os, json, requests, psycopg

DB = os.environ["DATABASE_URL"]
SITE = os.environ.get("SITE_URL", "http://web:3000")
SECRET = os.environ.get("REVALIDATE_SECRET", "")


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
