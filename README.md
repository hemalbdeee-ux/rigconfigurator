# RigConfigurator.com — Next.js + Postgres + Python pipeline (Docker)

Fit-checked vehicle accessory site (Amazon Associates). Stack: Next.js 15 (App Router, ISR, standalone) · Postgres 16 · Python cron pipeline · Traefik (Hostinger) for HTTPS.

## Layout

```
docker-compose.yml        web + db + pipeline, Traefik labels (no ports 80/443 bound)
.env.example              copy → .env (or Hostinger "Environment variables")
web/                      Next.js app
  app/page.tsx            home (vehicle picker)
  app/vehicles/           /vehicles, /vehicles/[make]/[model]/[gen] (hub), /.../[category] (money page)
  app/go/[id]/route.ts    /go/123 → logs click → 302 Amazon with ?tag=
  app/api/catalog/item/   public JSON per ASIN (allowed for AI crawlers in robots.txt)
  app/api/revalidate/     pipeline calls this to refresh ISR pages
  app/sitemap.ts, robots.ts
  app/[section]/page.tsx  placeholders: /build /guides /tools /deals /laws /about … (noindex) — replace as you build
  lib/db.ts, lib/queries.ts
  components/ProductCard.tsx, VehiclePicker.tsx
db/init/001_schema.sql    vehicles · categories · products · fitments · fitment_pages · clicks · deals
db/init/002_seed.sql      3 vehicles, 4 products, 1 published page (delete before real launch)
pipeline/                 Python: import_fitments.py (CSV→DB), refresh_prices.py (PA-API), deals.py (hourly), cron
```

## Deploy on Hostinger VPS (Docker Manager)

1. Push this folder to a GitHub repo (public, or private with a token URL).
2. hPanel → VPS → Docker Manager → **Deploy Traefik** (once). It creates the `traefik-proxy` network and owns ports 80/443.
3. DNS: `A rigconfigurator.com → VPS IP`, `A www → VPS IP` (Hostinger DNS Manager).
4. Docker Manager → **Compose → Compose from URL** → paste the raw URL of `docker-compose.yml`
   (`https://raw.githubusercontent.com/<you>/rigconfigurator/main/docker-compose.yml`).
   Project name: `rigconfigurator`. Add environment variables from `.env.example` (change both passwords).
5. Deploy. First build ≈ 3–5 min (Next.js build inside Docker). Postgres runs `db/init/*.sql` on first start only.
6. Open `https://rigconfigurator.com` → home → F-150 → Tonneau Covers page. Click "View on Amazon" → check `clicks` table:
   `docker exec -it rigconfigurator-db psql -U rig -d rigconfigurator -c 'select * from clicks'`

Update: push to GitHub → Docker Manager → project → **Rebuild/Update** (or `docker compose up -d --build` in Web console).

## Data v1 (32 vehicles · 30 money pages · 147 products)

```
db/migrations/000_drop_seed.sql     removes demo rows
db/migrations/003_vehicles.sql      32 vehicle generations with fit attributes (idempotent upsert)
db/migrations/004_fitment_pages.sql editorial for 30 pages — GENERATED from db/content/pages_v1.py
db/migrations/005_publish.sql       publishes pages with ≥2 products, drafts the rest (noindex)
db/content/fitments_v1.py           product shortlist → build_fitments_csv.py → pipeline/data/fitments.csv
db/apply.sh                         runs all migrations against the running container + revalidates
```

Apply on the VPS after `git pull`:
```
bash db/apply.sh
docker exec rigconfigurator-pipeline python import_fitments.py data/fitments.csv
docker exec -i rigconfigurator-db psql -U rig -d rigconfigurator < db/migrations/005_publish.sql
```
Edit content in `db/content/*.py`, regenerate (`python3 db/content/build_pages_sql.py`, `python3 db/content/build_fitments_csv.py`), commit, pull, re-run the three lines. ASIN fitments are `confidence 2` (from listing titles) — bump to 3 in `fitments_v1.py` once checked against the manufacturer fit guide; `confidence 1` rows show an "unverified" pill.

## Data flow

```
manufacturer fit guides / Amazon listings ──(Python, CSV)──▶ pipeline/import_fitments.py ──▶ Postgres
                                                                                         └──▶ POST /api/revalidate → ISR page refresh
PA-API (after 3 sales) ──6h cron──▶ refresh_prices.py ──▶ products.price_cents/image_url
Keepa (optional) ──hourly──▶ deals.py ──▶ deals table ──▶ /deals
```

Import fitments: put CSV at `pipeline/data/fitments.csv` (columns in the script docstring), then
`docker exec rigconfigurator-pipeline python import_fitments.py data/fitments.csv`.

Editorial per money page lives in `fitment_pages` (`intro_md`, `gotchas_md`, `faq` JSON, `verdict_md`, `status`).
Pages with `status <> 'published'` render but are `noindex` — your AI-draft → QA → publish gate.

## Amazon TOS notes baked in

- No price is stored as text on the page unless it came from PA-API within 24 h; otherwise `price_band` ("$300–$350") is shown.
- Product images only from PA-API URLs (`m.media-amazon.com` allowed in `next.config.ts`).
- `/go/` links are `rel="nofollow sponsored"`, disclosure in footer + page header.

## Local dev

```
docker compose up db -d
cd web && cp ../.env.example .env.local   # set DATABASE_URL=postgres://rig:...@localhost:5432/rigconfigurator
npm install && npm run dev
```

## Next build steps (in order)

1. Replace seed with real vehicle rows (30 models × generations) — `vehicles` table.
2. Fitment CSV for the first 30 money pages (see blueprint doc) → import → write `fitment_pages` rows.
3. `/tools/*` routes (hitch class finder, bed-length checker) as client components reading `vehicles` attrs.
4. `/build` configurator (vehicle → category slots → fit-filtered products → total; save to localStorage first).
5. `/laws/[topic]/[state]` programmatic pages from a `laws` table.
6. `/deals` page reading `deals` view; Keepa in `deals.py`.
