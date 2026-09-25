-- 009_published_at.sql — stable first-publish date for Article JSON-LD datePublished.
-- verified_at/updated_at move on every apply; published_at is written once (in 005_publish.sql) and never changed.
ALTER TABLE fitment_pages ADD COLUMN IF NOT EXISTS published_at DATE;
