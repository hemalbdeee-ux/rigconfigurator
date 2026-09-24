-- RigConfigurator schema v1 — runs once on first Postgres start
CREATE EXTENSION IF NOT EXISTS pg_trgm;

CREATE TABLE makes (
  id          SERIAL PRIMARY KEY,
  slug        TEXT UNIQUE NOT NULL,        -- toyota
  name        TEXT NOT NULL                -- Toyota
);

CREATE TABLE vehicles (
  id              SERIAL PRIMARY KEY,
  make_id         INT NOT NULL REFERENCES makes(id),
  model_slug      TEXT NOT NULL,           -- 4runner
  model_name      TEXT NOT NULL,           -- 4Runner
  gen_slug        TEXT NOT NULL,           -- 2010-2024
  gen_name        TEXT NOT NULL,           -- 5th Gen (N280)
  year_from       INT NOT NULL,
  year_to         INT,                     -- NULL = current
  body_style      TEXT NOT NULL,           -- truck | suv | sedan | ev
  -- fit attributes
  bed_lengths_in  NUMERIC[] DEFAULT '{}',  -- trucks: {66, 78, 96}
  roof_type       TEXT,                    -- bare | raised-rails | flush-rails | fixed-points | track
  roof_load_lb    INT,
  hitch_class     TEXT,                    -- none | 1 | 2 | 3 | 4 | 5
  receiver_in     NUMERIC,                 -- 1.25 | 2 | 2.5
  tow_rating_lb   INT,
  tire_size       TEXT,
  bolt_pattern    TEXT,                    -- 6x139.7
  rows_seating    INT DEFAULT 2,
  attrs           JSONB DEFAULT '{}',      -- anything else (rambox, utility track, etc.)
  summary         TEXT,
  updated_at      TIMESTAMPTZ DEFAULT now(),
  UNIQUE (make_id, model_slug, gen_slug)
);

CREATE TABLE categories (
  id          SERIAL PRIMARY KEY,
  slug        TEXT UNIQUE NOT NULL,        -- tonneau-covers
  name        TEXT NOT NULL,               -- Tonneau Covers
  body_styles TEXT[] DEFAULT '{truck,suv,sedan,ev}',
  fit_rule    TEXT,                        -- bed_length | roof_type | receiver | rows | none
  sort        INT DEFAULT 100
);

CREATE TABLE products (
  id          SERIAL PRIMARY KEY,
  asin        TEXT UNIQUE NOT NULL,
  category_id INT NOT NULL REFERENCES categories(id),
  name        TEXT NOT NULL,
  brand       TEXT,
  image_url   TEXT,
  price_cents INT,                         -- last seen price
  price_band  TEXT,                        -- "$250–$350" shown when no live price
  rating      NUMERIC(2,1),
  reviews     INT,
  weight_lb   NUMERIC,
  attrs       JSONB DEFAULT '{}',          -- type, material, etc.
  pros        TEXT[] DEFAULT '{}',
  cons        TEXT[] DEFAULT '{}',
  active      BOOLEAN DEFAULT TRUE,
  price_checked_at TIMESTAMPTZ,
  updated_at  TIMESTAMPTZ DEFAULT now()
);
CREATE INDEX products_category_idx ON products(category_id) WHERE active;

-- A product fits a vehicle generation, optionally narrowed by a condition
CREATE TABLE fitments (
  id          SERIAL PRIMARY KEY,
  product_id  INT NOT NULL REFERENCES products(id) ON DELETE CASCADE,
  vehicle_id  INT NOT NULL REFERENCES vehicles(id) ON DELETE CASCADE,
  year_from   INT,                         -- NULL = whole generation
  year_to     INT,
  condition   JSONB DEFAULT '{}',          -- {"bed_length_in": 66} / {"roof_type":"raised-rails"}
  note        TEXT,                        -- "Not for models with bed utility track"
  source      TEXT,                        -- manufacturer | amazon-listing | verified
  confidence  SMALLINT DEFAULT 2 CHECK (confidence BETWEEN 1 AND 3),
  rank        INT DEFAULT 100,             -- editorial order on the page
  UNIQUE (product_id, vehicle_id, condition)
);
CREATE INDEX fitments_vehicle_idx ON fitments(vehicle_id);

-- Editorial layer for each fitment page (AI draft + human QA)
CREATE TABLE fitment_pages (
  id            SERIAL PRIMARY KEY,
  vehicle_id    INT NOT NULL REFERENCES vehicles(id) ON DELETE CASCADE,
  category_id   INT NOT NULL REFERENCES categories(id),
  title         TEXT,
  meta_desc     TEXT,
  intro_md      TEXT,
  gotchas_md    TEXT,                      -- vehicle-specific fit gotchas (unique content)
  install_md    TEXT,
  faq           JSONB DEFAULT '[]',        -- [{q,a}]
  verdict_md    TEXT,
  article       JSONB,                     -- long-form article (playbook standard); see db/content/articles
  status        TEXT DEFAULT 'draft',      -- draft | review | published | noindex
  verified_at   DATE,
  updated_at    TIMESTAMPTZ DEFAULT now(),
  UNIQUE (vehicle_id, category_id)
);

-- /go/[id] click tracking
CREATE TABLE clicks (
  id          BIGSERIAL PRIMARY KEY,
  product_id  INT REFERENCES products(id),
  page        TEXT,
  placement   TEXT,
  ua          TEXT,
  country     TEXT,
  created_at  TIMESTAMPTZ DEFAULT now()
);
CREATE INDEX clicks_created_idx ON clicks(created_at);

-- Deals board (Keepa / PA-API price drops)
CREATE TABLE deals (
  id            SERIAL PRIMARY KEY,
  product_id    INT NOT NULL REFERENCES products(id) ON DELETE CASCADE,
  price_cents   INT NOT NULL,
  avg90_cents   INT,
  drop_pct      NUMERIC(5,1),
  seen_at       TIMESTAMPTZ DEFAULT now(),
  active        BOOLEAN DEFAULT TRUE
);

CREATE OR REPLACE VIEW v_fitment AS
SELECT f.id, f.vehicle_id, f.year_from, f.year_to, f.condition, f.note, f.source, f.confidence, f.rank,
       p.id AS product_id, p.asin, p.name, p.brand, p.image_url, p.price_cents, p.price_band,
       p.rating, p.reviews, p.weight_lb, p.attrs, p.pros, p.cons,
       c.slug AS category_slug, c.name AS category_name
FROM fitments f
JOIN products p ON p.id = f.product_id AND p.active
JOIN categories c ON c.id = p.category_id;
