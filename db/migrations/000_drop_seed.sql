-- 000_drop_seed.sql — remove the demo rows shipped in db/init/002_seed.sql. Idempotent.
DELETE FROM fitment_pages WHERE vehicle_id IN (SELECT id FROM vehicles WHERE model_slug='f-150' AND gen_slug='2021-2025');
DELETE FROM clicks WHERE product_id IN (SELECT id FROM products WHERE asin IN ('B0CJNNB5GP','B07EXAMPLE1','B07EXAMPLE2','B07EXAMPLE3','B07EXAMPLE4'));
DELETE FROM products WHERE asin IN ('B0CJNNB5GP','B07EXAMPLE1','B07EXAMPLE2','B07EXAMPLE3','B07EXAMPLE4');  -- cascades fitments/deals
-- seed F-150 used a year-bounded slug; 003_vehicles.sql re-creates it as 2021-present
DELETE FROM vehicles WHERE model_slug='f-150' AND gen_slug='2021-2025';
