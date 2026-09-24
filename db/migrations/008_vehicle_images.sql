-- 008_vehicle_images.sql — licensed hero photos per vehicle generation (filled by pipeline/fetch_images.py). Idempotent.
SET client_min_messages = warning;
CREATE TABLE IF NOT EXISTS vehicle_images (
  id           SERIAL PRIMARY KEY,
  vehicle_id   INT NOT NULL REFERENCES vehicles(id) ON DELETE CASCADE,
  file         TEXT NOT NULL,              -- relative to IMG_DIR, e.g. vehicles/ford-f-150-2021-present.webp
  width        INT, height INT,
  source       TEXT NOT NULL DEFAULT 'wikimedia-commons',
  source_url   TEXT NOT NULL,              -- file description page (attribution link)
  title        TEXT,
  author       TEXT,
  license      TEXT NOT NULL,              -- e.g. CC BY-SA 4.0
  license_url  TEXT,
  score        NUMERIC,
  status       TEXT NOT NULL DEFAULT 'candidate',   -- candidate | approved | rejected
  created_at   TIMESTAMPTZ DEFAULT now(),
  UNIQUE (vehicle_id, source_url)
);
CREATE UNIQUE INDEX IF NOT EXISTS vehicle_images_one_approved ON vehicle_images(vehicle_id) WHERE status = 'approved';
