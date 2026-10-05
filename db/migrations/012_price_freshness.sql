-- 012_price_freshness.sql — Amazon Creators API content may be shown for at most 24 hours after it was fetched.
-- The view hides a price, or an Amazon image link, that pipeline/refresh_prices.py has not refreshed in the
-- last 23 hours, and exposes price_checked_at so the site can print the required "as of" time next to a price.
-- Idempotent: safe to re-run. New column is appended last (CREATE OR REPLACE VIEW cannot reorder columns).
CREATE OR REPLACE VIEW v_fitment AS
SELECT f.id, f.vehicle_id, f.year_from, f.year_to, f.condition, f.note, f.source, f.confidence, f.rank,
       p.id AS product_id, p.asin, p.name, p.brand,
       CASE WHEN p.image_url ~* 'amazon' AND (p.price_checked_at IS NULL OR p.price_checked_at < now() - interval '23 hours')
            THEN NULL ELSE p.image_url END AS image_url,
       CASE WHEN p.price_checked_at >= now() - interval '23 hours' THEN p.price_cents END AS price_cents,
       p.price_band,
       p.rating, p.reviews, p.weight_lb, p.attrs, p.pros, p.cons,
       c.slug AS category_slug, c.name AS category_name,
       CASE WHEN p.price_checked_at >= now() - interval '23 hours' THEN p.price_checked_at END AS price_checked_at
FROM fitments f
JOIN products p ON p.id = f.product_id AND p.active
JOIN categories c ON c.id = p.category_id;
