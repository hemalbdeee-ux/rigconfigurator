-- 010_pillar_pages.sql — hub pages that are not vehicle x category guides:
--   kind 'upgrades'  → /vehicles/<make>/<model>/<gen>/upgrades  (one per vehicle, links to that vehicle's category guides)
--   kind 'explainer' → /learn/<slug>                            (X vs Y / how-it-works, links to every guide in its categories)
-- Content lives in db/content/pillars/*.py → db/content/build_pillars_sql.py → 011_pillars.sql.
CREATE TABLE IF NOT EXISTS pillar_pages (
  id             SERIAL PRIMARY KEY,
  kind           TEXT NOT NULL CHECK (kind IN ('upgrades', 'explainer')),
  slug           TEXT NOT NULL UNIQUE,            -- explainer: url slug; upgrades: '<make>/<model>/<gen>'
  vehicle_id     INT REFERENCES vehicles(id) ON DELETE CASCADE,
  category_slugs TEXT[] NOT NULL DEFAULT '{}',    -- categories this page links to / is about
  title          TEXT NOT NULL,
  meta_desc      TEXT,
  faq            JSONB NOT NULL DEFAULT '[]',
  article        JSONB NOT NULL,
  status         TEXT NOT NULL DEFAULT 'published',
  published_at   DATE NOT NULL DEFAULT CURRENT_DATE, -- set on first insert, never updated
  updated_at     TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS pillar_pages_vehicle ON pillar_pages (vehicle_id);
