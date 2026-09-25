-- 005_publish.sql — publish every fitment page that has at least 2 fit-checked products; keep the rest draft (noindex).
-- Safe to re-run after each CSV import.
UPDATE fitment_pages fp SET status = 'published', updated_at = now()
WHERE status = 'draft'
  AND (SELECT count(*) FROM fitments f JOIN products p ON p.id = f.product_id AND p.active
       WHERE f.vehicle_id = fp.vehicle_id AND p.category_id = fp.category_id) >= 2;

UPDATE fitment_pages fp SET status = 'draft', updated_at = now()
WHERE status = 'published'
  AND (SELECT count(*) FROM fitments f JOIN products p ON p.id = f.product_id AND p.active
       WHERE f.vehicle_id = fp.vehicle_id AND p.category_id = fp.category_id) < 2;

-- Stamp the first-publish date once. Long-form pages use the article's first review date; others use today.
UPDATE fitment_pages SET published_at = COALESCE((article->>'reviewed')::date, CURRENT_DATE)
WHERE status = 'published' AND published_at IS NULL;
