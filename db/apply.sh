#!/usr/bin/env bash
# Apply all db/migrations/*.sql in order against the running rigconfigurator-db container, then revalidate pages.
# Usage (on the VPS): cd /docker/rigconfigurator && bash db/apply.sh
set -euo pipefail
cd "$(dirname "$0")/.."
set -a; source .env; set +a
for f in db/migrations/*.sql; do
  echo "== $f"
  docker exec -i rigconfigurator-db psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -v ON_ERROR_STOP=1 -q < "$f"
done
docker exec rigconfigurator-db psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c \
  "SELECT (SELECT count(*) FROM vehicles) vehicles, (SELECT count(*) FROM products WHERE active) products, (SELECT count(*) FROM fitments) fitments, (SELECT count(*) FROM fitment_pages WHERE status='published') published_pages"
curl -s -X POST "https://${DOMAIN}/api/revalidate?secret=${REVALIDATE_SECRET}" -H 'Content-Type: application/json' -d '{"paths":["/","/vehicles"]}'; echo
