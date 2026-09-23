-- Seed: 12 categories, 3 vehicles, 4 products, fitments — enough to see every page type render
INSERT INTO categories (slug, name, body_styles, fit_rule, sort) VALUES
 ('tonneau-covers','Tonneau Covers','{truck}','bed_length',10),
 ('bed-racks','Bed Racks','{truck}','bed_length',20),
 ('roof-racks','Roof Racks & Crossbars','{truck,suv,sedan,ev}','roof_type',30),
 ('cargo-boxes','Cargo Boxes','{suv,sedan,ev,truck}','roof_type',40),
 ('hitches','Trailer Hitches','{truck,suv,sedan,ev}','receiver',50),
 ('bike-racks','Bike Racks','{truck,suv,sedan,ev}','receiver',60),
 ('floor-mats','Floor Mats & Liners','{truck,suv,sedan,ev}','rows',70),
 ('seat-covers','Seat Covers','{truck,suv,sedan,ev}','rows',80),
 ('running-boards','Running Boards & Steps','{truck,suv}','none',90),
 ('led-light-bars','LED Light Bars','{truck,suv}','none',100),
 ('dash-cams','Dash Cams & Hardwire Kits','{truck,suv,sedan,ev}','none',110),
 ('lift-kits','Lift & Leveling Kits','{truck,suv}','none',120);

INSERT INTO makes (slug, name) VALUES ('ford','Ford'), ('toyota','Toyota');

INSERT INTO vehicles (make_id, model_slug, model_name, gen_slug, gen_name, year_from, year_to, body_style,
  bed_lengths_in, roof_type, roof_load_lb, hitch_class, receiver_in, tow_rating_lb, tire_size, bolt_pattern, rows_seating, attrs, summary)
VALUES
 ((SELECT id FROM makes WHERE slug='ford'),'f-150','F-150','2021-2025','14th Gen (P702)',2021,NULL,'truck',
  '{66,78,96}','bare',NULL,'4',2,14000,'275/65R18','6x135',2,
  '{"bed_utility_track":true,"tailgate_step":"optional","lightning_variant":"2022-"}',
  'The 14th-gen F-150 comes in 5.5, 6.5 and 8 ft beds; check for the optional bed utility track before buying rail-mounted covers.'),
 ((SELECT id FROM makes WHERE slug='toyota'),'4runner','4Runner','2010-2024','5th Gen (N280)',2010,2024,'suv',
  '{}','raised-rails',165,'3',2,5000,'265/70R17','6x139.7',2,
  '{"trd_pro_factory_rack":true,"rear_window_rolls_down":true}',
  'Fifth-gen 4Runner has factory raised rails on most trims; TRD Pro ships with a factory basket rack that changes crossbar fit.'),
 ((SELECT id FROM makes WHERE slug='toyota'),'tacoma','Tacoma','2016-2023','3rd Gen (N300)',2016,2023,'truck',
  '{61,73}','bare',NULL,'3',2,6800,'265/70R16','6x139.7',2,
  '{"bed_rail_system":true,"composite_bed":true}',
  'Third-gen Tacoma uses a composite bed with a factory deck rail system — many bed racks clamp to those rails.');

INSERT INTO products (asin, category_id, name, brand, image_url, price_cents, price_band, rating, reviews, weight_lb, attrs, pros, cons) VALUES
 ('B0CJNNB5GP',(SELECT id FROM categories WHERE slug='tonneau-covers'),'Hard Tri-Fold Tonneau Cover, 5.5 ft Bed','Tyger',NULL,32999,'$300–$350',4.5,2100,70,
  '{"type":"hard tri-fold","material":"aluminum + FRP"}','{Tool-free install,Holds 400 lb distributed,Full bed access}','{Not for utility track beds,No lock on tailgate side}'),
 ('B07EXAMPLE1',(SELECT id FROM categories WHERE slug='tonneau-covers'),'Soft Roll-Up Tonneau Cover, 6.5 ft Bed','MaxMate',NULL,17999,'$170–$200',4.4,9800,25,
  '{"type":"soft roll-up","material":"vinyl"}','{Cheapest reliable option,20-min install}','{Vinyl sags in heat,Less secure}'),
 ('B07EXAMPLE2',(SELECT id FROM categories WHERE slug='roof-racks'),'Aero Crossbars for Raised Side Rails','Yakima',NULL,24999,'$230–$270',4.6,3400,12,
  '{"type":"crossbar","mount":"raised-rails","load_lb":165}','{Quiet aero profile,Fits most raised rails}','{Not for TRD Pro factory rack}'),
 ('B07EXAMPLE3',(SELECT id FROM categories WHERE slug='bed-racks'),'Mid-Height Bed Rack, Tacoma 2005-2023','Leitner-style',NULL,54999,'$500–$600',4.3,800,60,
  '{"type":"mid-height","mount":"deck-rail"}','{Clamps to factory deck rails,Tent-ready}','{Heavy,Needs 2 people to install}');

INSERT INTO fitments (product_id, vehicle_id, condition, note, source, confidence, rank) VALUES
 ((SELECT id FROM products WHERE asin='B0CJNNB5GP'),(SELECT id FROM vehicles WHERE model_slug='f-150' AND gen_slug='2021-2025'),
  '{"bed_length_in":66}','Only for 5.5 ft bed without the optional bed utility track.','manufacturer',3,1),
 ((SELECT id FROM products WHERE asin='B07EXAMPLE1'),(SELECT id FROM vehicles WHERE model_slug='f-150' AND gen_slug='2021-2025'),
  '{"bed_length_in":78}','6.5 ft bed only.','amazon-listing',2,2),
 ((SELECT id FROM products WHERE asin='B07EXAMPLE2'),(SELECT id FROM vehicles WHERE model_slug='4runner' AND gen_slug='2010-2024'),
  '{"roof_type":"raised-rails"}','Skip if your TRD Pro has the factory basket rack.','manufacturer',3,1),
 ((SELECT id FROM products WHERE asin='B07EXAMPLE3'),(SELECT id FROM vehicles WHERE model_slug='tacoma' AND gen_slug='2016-2023'),
  '{}','Clamps to the factory deck rail system; both bed lengths.','verified',3,1);

INSERT INTO fitment_pages (vehicle_id, category_id, title, meta_desc, intro_md, gotchas_md, faq, verdict_md, status, verified_at) VALUES
 ((SELECT id FROM vehicles WHERE model_slug='f-150' AND gen_slug='2021-2025'),(SELECT id FROM categories WHERE slug='tonneau-covers'),
  'Best Tonneau Covers for 2021–2025 Ford F-150 (5.5 / 6.5 / 8 ft Bed)',
  'Fit-checked tonneau covers for the 14th-gen F-150, sorted by bed length. Prices, pros/cons and the utility-track gotcha most listings miss.',
  'Every cover below is matched to a specific F-150 bed length. Measure inside the bed from bulkhead to tailgate: 66 in = 5.5 ft, 78 in = 6.5 ft, 96 in = 8 ft.',
  '- **Bed utility track** (optional on XLT and up) blocks most clamp-on rails — look for "utility track compatible" or remove the track.\n- **Lightning (2022+)** shares the 5.5 ft bed but has a different tailgate; most covers still fit.\n- **Tailgate step** does not affect cover fit.',
  '[{"q":"Do 5.5 ft F-150 covers fit the Lightning?","a":"Most do — the bed dimensions are identical; confirm the listing says 2022+ Lightning."},{"q":"Will a cover fit with the bed utility track?","a":"Only covers that state utility-track compatibility. Others require removing the track (four bolts per side)."}]',
  '**Budget:** MaxMate soft roll-up. **Best overall:** Tyger hard tri-fold. **Premium:** retractable aluminum (coming to this list).',
  'published', CURRENT_DATE);
