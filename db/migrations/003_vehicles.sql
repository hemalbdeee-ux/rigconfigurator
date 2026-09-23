-- 003_vehicles.sql — 32 vehicle generations (US market), fit attributes for the configurator
-- Idempotent: safe to re-run. Values compiled from manufacturer spec sheets (2026-09); verify flagged attrs before publishing.
-- Conventions: bed_lengths_in = inside bed length rounded to whole inches; roof_type ∈ bare | raised-rails | flush-rails | fixed-points | removable
--              hitch_class = factory/most-common aftermarket receiver class; receiver_in = 1.25 | 2 | 2.5; tow_rating_lb = max with factory tow package

INSERT INTO makes (slug, name) VALUES
 ('ford','Ford'),('chevrolet','Chevrolet'),('gmc','GMC'),('ram','Ram'),('toyota','Toyota'),('jeep','Jeep'),
 ('nissan','Nissan'),('honda','Honda'),('subaru','Subaru'),('tesla','Tesla'),('kia','Kia'),('hyundai','Hyundai')
ON CONFLICT (slug) DO NOTHING;

INSERT INTO vehicles (make_id, model_slug, model_name, gen_slug, gen_name, year_from, year_to, body_style,
  bed_lengths_in, roof_type, roof_load_lb, hitch_class, receiver_in, tow_rating_lb, tire_size, bolt_pattern, rows_seating, attrs, summary)
VALUES
-- ===================== TRUCKS =====================
((SELECT id FROM makes WHERE slug='ford'),'f-150','F-150','2021-present','14th Gen (P702)',2021,NULL,'truck',
 '{66,78,96}','bare',NULL,'4',2,14000,'275/65R18','6x135',2,
 '{"bed_utility_track":"optional (XLT+)","tailgate_step":"optional","variants":["Lightning 2022+","Raptor","Tremor"],"bed_material":"aluminum","verify":["tow max is 3.5L EcoBoost Max Tow"]}',
 'Three bed lengths (5.5 / 6.5 / 8 ft). Check for the optional bed utility track before buying rail-clamp covers; Lightning shares the 5.5 ft bed.'),

((SELECT id FROM makes WHERE slug='ford'),'f-150','F-150','2015-2020','13th Gen (P552)',2015,2020,'truck',
 '{66,78,96}','bare',NULL,'4',2,13200,'275/65R18','6x135',2,
 '{"bed_utility_track":"optional","bed_material":"aluminum","variants":["Raptor 2017+"]}',
 'Aluminum-bed generation with 5.5 / 6.5 / 8 ft beds. Most 2015–2020 tonneau and bed-rack fitments carry over to 2021+ 5.5 and 6.5 ft beds but always match the year range on the listing.'),

((SELECT id FROM makes WHERE slug='chevrolet'),'silverado-1500','Silverado 1500','2019-present','4th Gen (T1)',2019,NULL,'truck',
 '{70,79,98}','bare',NULL,'4',2,13300,'275/60R20','6x139.7',2,
 '{"tailgate":"Multi-Flex optional (2021+)","bed_names":{"70":"Short 5ft 8in","79":"Standard 6ft 6in","98":"Long 8ft"},"bed_material":"steel (Durabed)","variants":["Trail Boss","ZR2 2022+"]}',
 'Beds are 5''8", 6''6" and 8 ft. Multi-Flex tailgate (2021+) changes tailgate-side clamp fit on some covers — check the listing.'),

((SELECT id FROM makes WHERE slug='gmc'),'sierra-1500','Sierra 1500','2019-present','5th Gen (T1)',2019,NULL,'truck',
 '{70,79,98}','bare',NULL,'4',2,13200,'275/60R20','6x139.7',2,
 '{"tailgate":"MultiPro standard on most trims","bed_material":"steel or CarbonPro composite (option)","carbonpro_fit_warning":true,"variants":["AT4","AT4X","Denali"]}',
 'Same beds as Silverado (5''8" / 6''6" / 8 ft). MultiPro tailgate and the CarbonPro composite bed both affect tonneau fit — many covers exclude CarbonPro.'),

((SELECT id FROM makes WHERE slug='ram'),'1500','1500','2019-present','5th Gen (DT)',2019,NULL,'truck',
 '{67,76}','bare',NULL,'4',2,12750,'275/55R20','6x139.7',2,
 '{"rambox":"optional — needs RamBox-specific covers/racks","bed_names":{"67":"5ft 7in","76":"6ft 4in"},"tailgate":"multifunction split optional","variants":["TRX 2021-2024","RHO 2025+","Classic (DS) sold alongside 2019-2024"]}',
 'Two beds: 5''7" and 6''4". RamBox trucks need RamBox-specific covers and racks. Do not confuse with the Ram 1500 Classic (DS) sold alongside — different bed rails.'),

((SELECT id FROM makes WHERE slug='toyota'),'tacoma','Tacoma','2016-2023','3rd Gen (N300)',2016,2023,'truck',
 '{61,74}','bare',NULL,'3',2,6800,'265/70R16','6x139.7',2,
 '{"bed_rail_system":"factory deck rails with cleats","bed_material":"composite (SMC)","bed_names":{"61":"5ft short","74":"6ft long"},"variants":["TRD Pro","Trail Edition"]}',
 'Composite bed with factory deck-rail system — most bed racks clamp to those rails. 5 ft and 6 ft beds; the 6 ft is Access Cab / some Double Cab.'),

((SELECT id FROM makes WHERE slug='toyota'),'tacoma','Tacoma','2024-present','4th Gen (N400)',2024,NULL,'truck',
 '{60,74}','bare',NULL,'3',2,6500,'265/70R18','6x139.7',2,
 '{"bed_rail_system":"deck rails","bed_material":"composite","hybrid":"i-FORCE MAX option","fit_note":"few 3rd-gen covers carry over; buy 2024+ listings only","verify":["tow max by trim"]}',
 'All-new 2024 platform: 5 ft and 6 ft composite beds with deck rails. 2016–2023 fitments do NOT carry over — buy 2024+ listings only.'),

((SELECT id FROM makes WHERE slug='toyota'),'tundra','Tundra','2022-present','3rd Gen (XK70)',2022,NULL,'truck',
 '{66,79,98}','bare',NULL,'4',2,12000,'265/70R18','6x139.7',2,
 '{"bed_rail_system":"deck rails","bed_material":"composite (SMC)","bed_names":{"66":"5.5 ft","79":"6.5 ft","98":"8.1 ft"},"variants":["TRD Pro","Capstone","i-FORCE MAX hybrid"]}',
 'Composite bed with deck rails, three lengths (5.5 / 6.5 / 8.1 ft). 2007–2021 fitments do not carry over.'),

((SELECT id FROM makes WHERE slug='jeep'),'gladiator','Gladiator','2020-present','JT',2020,NULL,'truck',
 '{60}','removable',NULL,'3',2,7700,'255/75R17','5x127',2,
 '{"trail_rail":"optional Trail Rail cargo system — affects bed rack + cover fit","roof":"removable hardtop/soft top — no roof racks, use bed racks","spare":"under-bed","variants":["Rubicon","Mojave"]}',
 'Single 5 ft bed; optional Trail Rail system changes cover and rack fit. Roof is removable, so overland loads go on a bed rack.'),

((SELECT id FROM makes WHERE slug='ford'),'ranger','Ranger','2019-2023','4th Gen (T6, US)',2019,2023,'truck',
 '{61}','bare',NULL,'4',2,7500,'265/65R17','6x139.7',2,
 '{"bed_names":{"61":"5 ft (SuperCrew)"},"supercab_bed":"6 ft (72 in) on SuperCab — add condition if stocking","variants":["Tremor 2021+"]}',
 'US-market SuperCrew has a 5 ft bed (SuperCab: 6 ft). Class IV factory hitch on most trims.'),

((SELECT id FROM makes WHERE slug='ford'),'ranger','Ranger','2024-present','5th Gen (P703)',2024,NULL,'truck',
 '{60}','bare',NULL,'4',2,7500,'265/65R17','6x139.7',2,
 '{"bed_names":{"60":"5 ft"},"variants":["Raptor 2024+"],"fit_note":"2019-2023 covers do not fit"}',
 'All-new 2024 Ranger with a 5 ft bed. 2019–2023 tonneau fitments do not carry over.'),

((SELECT id FROM makes WHERE slug='chevrolet'),'colorado','Colorado','2023-present','3rd Gen',2023,NULL,'truck',
 '{62}','bare',NULL,'4',2,7700,'265/70R17','6x120',2,
 '{"bed_names":{"62":"5ft 2in"},"tailgate":"optional storage tailgate","variants":["Trail Boss","ZR2","ZR2 Bison"],"fit_note":"confirm 2023+ fit on multi-generation cover listings"}',
 'One 5''2" bed on all 2023+ cabs. Many sellers list 2015–2026 on one cover SKU; buy 2023+-specific listings or confirm with the seller.'),

((SELECT id FROM makes WHERE slug='ford'),'maverick','Maverick','2022-present','1st Gen',2022,NULL,'truck',
 '{54}','bare',NULL,'3',2,4000,'225/65R17','5x108',2,
 '{"bed_names":{"54":"4.5 ft FLEXBED"},"hitch":"2 in receiver with 4K Tow Package; else 1.25 in Class I","flexbed_slots":true,"hybrid":"standard 2.5L hybrid"}',
 'Compact 4.5 ft FLEXBED with slots for DIY dividers. Receiver is 2 in only with the 4K Tow Package — otherwise Class I.'),

((SELECT id FROM makes WHERE slug='nissan'),'frontier','Frontier','2022-present','3rd Gen (D41)',2022,NULL,'truck',
 '{60,73}','bare',NULL,'3',2,6720,'265/70R17','6x114.3',2,
 '{"bed_rail_system":"Utili-track optional","bed_names":{"60":"5 ft","73":"6 ft"},"variants":["PRO-4X"]}',
 '5 ft (Crew Cab) and 6 ft (King Cab / Crew LB) beds; optional Utili-track channels affect clamp-style covers.'),

-- ===================== SUVs =====================
((SELECT id FROM makes WHERE slug='toyota'),'4runner','4Runner','2010-2024','5th Gen (N280)',2010,2024,'suv',
 '{}','raised-rails',165,'3',2,5000,'265/70R17','6x139.7',2,
 '{"trd_pro_factory_rack":"basket rack replaces rails on TRD Pro","rear_window":"power roll-down","third_row":"optional (Limited/SR5)","fit_note":"crossbar kits for raised rails; TRD Pro needs basket-compatible mounts"}',
 'Factory raised rails on most trims (TRD Pro has a basket rack instead). Long generation = huge aftermarket; hitch is Class III on tow-package trucks.'),

((SELECT id FROM makes WHERE slug='toyota'),'4runner','4Runner','2025-present','6th Gen (N410)',2025,NULL,'suv',
 '{}','raised-rails',NULL,'4',2,6000,'265/70R18','6x139.7',2,
 '{"hybrid":"i-FORCE MAX on TRD Pro/Trailhunter","fit_note":"new roof + rail geometry — 5th-gen crossbars do not fit","verify":["roof load rating","rail style by trim"]}',
 'All-new 2025 platform on TNGA-F. 5th-gen roof racks, mats and hitches do NOT carry over.'),

((SELECT id FROM makes WHERE slug='jeep'),'wrangler','Wrangler','2018-present','JL',2018,NULL,'suv',
 '{}','removable',NULL,'2',2,3500,'255/75R17','5x127',2,
 '{"doors":["2-door","4-door Unlimited"],"roof":"removable hardtop / soft top / Sky One-Touch","spare":"tailgate-mounted — bike racks need spare-tire clearance","hitch":"factory Class II 2 in on tow package; aftermarket Class III common","variants":["Rubicon","392","4xe"]}',
 'Removable roof means roof racks bolt to the hardtop or a cage-style rack. Tailgate spare tire dictates bike-rack and cargo-carrier choice.'),

((SELECT id FROM makes WHERE slug='ford'),'bronco','Bronco','2021-present','6th Gen (U725)',2021,NULL,'suv',
 '{}','removable',NULL,'2',2,3500,'285/70R17','6x139.7',2,
 '{"doors":["2-door","4-door"],"roof":"removable hardtop / soft top; hardtop has factory rail mounting points on some trims","spare":"tailgate-mounted","variants":["Raptor","Badlands","Sasquatch pkg (35 in tires)"]}',
 'Removable hardtop/soft top; roof racks mount to hardtop rails or exo-racks. Tailgate spare affects bike racks.'),

((SELECT id FROM makes WHERE slug='toyota'),'rav4','RAV4','2019-present','5th Gen (XA50)',2019,NULL,'suv',
 '{}','raised-rails',165,'2',1.25,3500,'225/65R17','5x114.3',2,
 '{"rails":"raised rails standard on XLE and up; LE has bare roof","hitch":"1.25 in Class I/II factory; aftermarket 2 in Class III common","tow":"1,500 lb std; 3,500 lb Adventure/TRD Off-Road","hybrid":"RAV4 Hybrid + Prime share fit"}',
 'Best-selling SUV. Raised rails on XLE+ (LE is bare roof — different crossbar kit). Tow rating depends heavily on trim.'),

((SELECT id FROM makes WHERE slug='honda'),'cr-v','CR-V','2023-present','6th Gen',2023,NULL,'suv',
 '{}','bare',NULL,'2',1.25,1500,'235/60R18','5x114.3',2,
 '{"rails":"none factory (accessory rails available) — use door-jamb clamp crossbars","hitch":"1.25 in; some 2 in aftermarket","hybrid":"Sport/Sport-L/Sport Touring hybrid share fit","fit_note":"2017-2022 mats and racks do not fit"}',
 'Bare roof from the factory — crossbars use door-jamb clamps. 2017–2022 fitments do not carry over.'),

((SELECT id FROM makes WHERE slug='toyota'),'highlander','Highlander','2020-present','4th Gen (XU70)',2020,NULL,'suv',
 '{}','raised-rails',NULL,'3',2,5000,'235/65R18','5x114.3',3,
 '{"rails":"raised rails standard on most trims","third_row":true,"hybrid":"Hybrid shares fit","grand_highlander":"different vehicle (2024+) — do not mix"}',
 'Three-row family SUV with raised rails; Class III hitch and 5,000 lb tow. Grand Highlander is a different vehicle.'),

((SELECT id FROM makes WHERE slug='subaru'),'outback','Outback','2020-present','6th Gen (BT)',2020,NULL,'suv',
 '{}','raised-rails',176,'2',1.25,3500,'225/60R18','5x114.3',2,
 '{"rails":"raised rails with integrated swing-out crossbars (most trims); Wilderness has fixed ladder-style rack","hitch":"1.25 in factory; 2 in aftermarket common","tow":"2,700 lb std; 3,500 lb XT/Wilderness","fit_note":"crossbars for integrated-rail Outbacks differ from standard raised rails"}',
 'Integrated swing-out crossbars on most trims (Wilderness has a fixed rack) — check which rail style before buying a crossbar kit.'),

((SELECT id FROM makes WHERE slug='subaru'),'forester','Forester','2019-2024','5th Gen (SK)',2019,2024,'suv',
 '{}','raised-rails',176,'2',1.25,1500,'225/60R17','5x114.3',2,
 '{"rails":"raised rails standard","tow":"1,500 lb; 3,000 lb Wilderness","variants":["Wilderness 2022+"],"fit_note":"2025 is a new generation"}',
 'Raised rails on every trim; Wilderness doubles the tow rating. 2025+ is a new generation.'),

((SELECT id FROM makes WHERE slug='tesla'),'model-y','Model Y','2020-present','1st Gen incl. 2025 Juniper refresh',2020,NULL,'ev',
 '{}','fixed-points',165,'3',2,3500,'255/45R19','5x114.3',2,
 '{"roof":"glass roof with 4 fixed mounting points (Tesla-spec crossbars only)","hitch":"2 in receiver with Tow Package (retrofit available)","juniper_2025":"refreshed 2025 — some mats/liners differ","third_row":"optional 7-seat"}',
 'Glass roof with fixed points — only Tesla-spec crossbar kits fit. Tow Package adds a 2 in receiver. 2025 Juniper refresh changes some interior fitments.'),

((SELECT id FROM makes WHERE slug='tesla'),'model-3','Model 3','2017-present','1st Gen incl. 2024 Highland refresh',2017,NULL,'ev',
 '{}','fixed-points',NULL,'none',NULL,NULL,'235/45R18','5x114.3',2,
 '{"roof":"glass roof with fixed points","hitch":"no factory hitch in US; aftermarket 1.25 in (bike racks only)","highland_2024":"refreshed 2024 — different mats/liners","verify":["roof load"]}',
 'Glass roof with fixed points; no factory hitch in the US (aftermarket 1.25 in for bike racks). 2024 Highland refresh changes interior fitments.'),

((SELECT id FROM makes WHERE slug='ford'),'explorer','Explorer','2020-present','6th Gen (U625)',2020,NULL,'suv',
 '{}','raised-rails',NULL,'3',2,5600,'255/55R20','5x114.3',3,
 '{"rails":"raised rails standard","third_row":true,"hybrid":"Hybrid 2020-2024","fit_note":"2025 facelift keeps roof/hitch fit"}',
 'RWD-based three-row with raised rails and Class III hitch (5,600 lb with tow package).'),

((SELECT id FROM makes WHERE slug='jeep'),'grand-cherokee','Grand Cherokee','2022-present','5th Gen (WL)',2022,NULL,'suv',
 '{}','flush-rails',NULL,'4',2,6200,'265/60R18','5x127',2,
 '{"rails":"factory flush side rails on most trims","grand_cherokee_l":"3-row L variant — longer roof, different rear mats","4xe":"PHEV shares fit","tow":"6,200 lb V6; 7,200 lb V8 (2022-2024)"}',
 'WL generation; two-row (L is three-row with a longer roof). Class IV hitch, up to 6,200 lb V6.'),

((SELECT id FROM makes WHERE slug='chevrolet'),'tahoe','Tahoe','2021-present','5th Gen (T1)',2021,NULL,'suv',
 '{}','raised-rails',NULL,'4',2,8400,'275/60R20','6x139.7',3,
 '{"rails":"raised rails standard","third_row":true,"suburban":"same fit for roof/hitch; different cargo mats","variants":["Z71","RST","High Country"]}',
 'Full-size three-row; raised rails, Class IV hitch, 8,400 lb tow. Suburban shares roof and hitch fit.'),

((SELECT id FROM makes WHERE slug='kia'),'telluride','Telluride','2020-present','1st Gen',2020,NULL,'suv',
 '{}','raised-rails',NULL,'3',2,5000,'245/60R18','5x114.3',3,
 '{"rails":"raised rails standard","third_row":true,"variants":["X-Line","X-Pro 2023+"],"fit_note":"2026 is a new generation"}',
 'Three-row with raised rails and 5,000 lb tow (Class III). 2026 model year is a redesign.'),

((SELECT id FROM makes WHERE slug='hyundai'),'palisade','Palisade','2020-2025','1st Gen (LX2)',2020,2025,'suv',
 '{}','raised-rails',NULL,'3',2,5000,'245/60R18','5x114.3',3,
 '{"rails":"raised rails standard","third_row":true,"variants":["XRT 2023+"],"fit_note":"2026 is a new generation"}',
 'Telluride twin: raised rails, Class III, 5,000 lb. 2026 is a new generation.'),

((SELECT id FROM makes WHERE slug='honda'),'pilot','Pilot','2023-present','4th Gen',2023,NULL,'suv',
 '{}','raised-rails',NULL,'3',2,5000,'255/60R18','5x120',3,
 '{"rails":"raised rails on TrailSport/Elite; other trims bare roof (accessory rails)","third_row":true,"tow":"5,000 lb AWD; 3,500 lb FWD","variants":["TrailSport"]}',
 'Raised rails only on TrailSport/Elite — other trims are bare-roof. Tow 5,000 lb AWD, 3,500 lb FWD.'),

((SELECT id FROM makes WHERE slug='toyota'),'sequoia','Sequoia','2023-present','3rd Gen (XK80)',2023,NULL,'suv',
 '{}','raised-rails',NULL,'4',2,9000,'265/70R18','6x139.7',3,
 '{"rails":"raised rails standard","third_row":true,"hybrid":"i-FORCE MAX standard","variants":["TRD Pro","Capstone"],"fit_note":"shares Tundra platform; different roof/mats"}',
 'Hybrid-only full-size three-row on the Tundra platform; Class IV, 9,000 lb tow, raised rails.')

ON CONFLICT (make_id, model_slug, gen_slug) DO UPDATE SET
  gen_name=EXCLUDED.gen_name, year_from=EXCLUDED.year_from, year_to=EXCLUDED.year_to, body_style=EXCLUDED.body_style,
  bed_lengths_in=EXCLUDED.bed_lengths_in, roof_type=EXCLUDED.roof_type, roof_load_lb=EXCLUDED.roof_load_lb,
  hitch_class=EXCLUDED.hitch_class, receiver_in=EXCLUDED.receiver_in, tow_rating_lb=EXCLUDED.tow_rating_lb,
  tire_size=EXCLUDED.tire_size, bolt_pattern=EXCLUDED.bolt_pattern, rows_seating=EXCLUDED.rows_seating,
  attrs=EXCLUDED.attrs, summary=EXCLUDED.summary, updated_at=now();
