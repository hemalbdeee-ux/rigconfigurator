#!/usr/bin/env bash
# Apply all db/migrations/*.sql, import fitments.csv, publish pages, against the running rigconfigurator-db container, then revalidate pages.
# Usage (on the VPS): cd /docker/rigconfigurator && bash db/apply.sh
set -euo pipefail
cd "$(dirname "$0")/.."
set -a; source .env; set +a
psqlf() { echo "== $1"; docker exec -i rigconfigurator-db psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -v ON_ERROR_STOP=1 -q < "$1"; }
# 1) schema/content migrations (publish step last, after products exist)
for f in db/migrations/*.sql; do
  [ "$(basename "$f")" = "005_publish.sql" ] && continue
  psqlf "$f"
done
# 2) products + fitments from pipeline/data/fitments.csv (mounted into the pipeline container)
echo "== import fitments.csv"
docker exec rigconfigurator-pipeline python import_fitments.py data/fitments.csv
# 3) publish every page with >= 2 fit-checked products
psqlf db/migrations/005_publish.sql
docker exec rigconfigurator-db psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c \
  "SELECT (SELECT count(*) FROM vehicles) vehicles, (SELECT count(*) FROM products WHERE active) products, (SELECT count(*) FROM fitments) fitments, (SELECT count(*) FROM fitment_pages WHERE status='published') published_pages"
curl -s -X POST "https://${DOMAIN}/api/revalidate?secret=${REVALIDATE_SECRET}" -H 'Content-Type: application/json' -d '{"paths":["/","/vehicles"]}'; echo
# 4) retire products no page links to any more (import re-activates them if they come back)
docker exec rigconfigurator-db psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -qc "UPDATE products SET active=false WHERE active AND id NOT IN (SELECT product_id FROM fitments);"
