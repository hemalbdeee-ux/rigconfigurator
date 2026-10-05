-- 013_price_history.sql — one row per product per Creators API price check, so /deals can compare today's price
-- with a real 30-day high instead of guessing from an editorial band. Idempotent.
CREATE TABLE IF NOT EXISTS price_history (
  id          BIGSERIAL PRIMARY KEY,
  product_id  INT NOT NULL REFERENCES products(id) ON DELETE CASCADE,
  price_cents INT NOT NULL,
  checked_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS price_history_product_idx ON price_history(product_id, checked_at DESC);
-- the band-midpoint "deals" the old deals.py flagged were not real price drops; clear them
UPDATE deals SET active=false WHERE active AND avg90_cents IS NOT NULL AND seen_at < '2026-10-05';
