"""Chart page (SAMPLE, not published): towing capacity of midsize and compact pickups, one row per truck, each from its maker.
Only trucks whose maker document has been read twice are listed; the others are named under not_covered."""
KIND = "chart"
KEY = ("chart", "midsize-truck-towing-capacity-chart", "towing-capacity")
MAKE, MODEL, TOPIC_LABEL = "", "", "Midsize truck towing capacity"
PUBLISH = False

TITLE = "Midsize Truck Towing Capacity Chart: Each Truck, From Its Maker"
SEO_TITLE = "Midsize Truck Towing Capacity Chart by Model"
META = ("Towing capacity of midsize and compact pickups side by side, each figure from the maker's own spec sheet: "
        "Ford Ranger, Toyota Tacoma, Ford Maverick.")

FAQ = [
 ("Which truck on this chart tows the most?",
  "The Ford Ranger, at up to 7,500 lb with the 2.3L or 2.7L EcoBoost for 2026. The 2024 Toyota Tacoma tops out at 6,500 lb."),
 ("Why does one truck have a range?",
  "Makers rate each build separately. The low figure is the least capable build the maker lists and the high figure the most capable; the condition column says which."),
 ("Are these figures comparable?",
  "They are each maker's own published maximum for the model year shown. The years differ between trucks, so check the year column before comparing."),
]

PAGE = {
 "answer": "Among the trucks on this chart, the Ford Ranger tows the most: up to 7,500 lb for 2026. The 2024 Toyota Tacoma is rated at 3,500 to 6,500 lb, and the compact Ford Maverick at 2,000 lb, or 4,000 lb with its tow package.",
 "reviewed": "2026-11-20",
 "covers": "Ford Ranger 2026, Toyota Tacoma 2024, Ford Maverick 2026",
 "not_covered": "Chevrolet Colorado, GMC Canyon, Nissan Frontier, Honda Ridgeline, Jeep Gladiator and Hyundai Santa Cruz are added as their maker documents are read.",
 "links": {"Ford Ranger": "/specs/ford/ranger/towing-capacity", "Ford Ranger Raptor": "/specs/ford/ranger/towing-capacity",
           "Toyota Tacoma": "/specs/toyota/tacoma/towing-capacity", "Ford Maverick": "/specs/ford/maverick/towing-capacity"},
 "sections": [
  {"id": "chart", "h": "Towing capacity by truck",
   "table": {"head": ["Truck", "Model year", "Maximum towing", "Maker's condition"], "rows": [
     ["Ford Ranger", "2026", "7,500 lb", "2.3L EcoBoost or 2.7L EcoBoost V6, when properly equipped", 1],
     ["Ford Ranger Raptor", "2026", "5,510 lb", "3.0L EcoBoost V6", 1],
     ["Toyota Tacoma", "2024", "3,500 to 6,500 lb", "3,500 lb SR; 6,500 lb XtraCab SR5 and TRD PreRunner", 2],
     ["Ford Maverick", "2026", "2,000 lb; 4,000 lb optional", "4,000 lb needs AWD and the 4K Tow Package (compact truck)", 3]]},
   "notes": ["Each truck name links to its own page, where the figure is broken down by engine, cab or grade."]},
 ],
 "check": [
  "Compare the model year column first: the trucks are not all from the same year.",
  "A maximum is for one specific build. Open the truck's own page for the figure by engine, cab and grade.",
  "The limit for a truck you own or are buying is in its owner's manual and on its door-jamb labels.",
 ],
 "sources": [
  ("Ford, 2026 Ranger Technical Specifications (v1.0, 13 Jan 2026)", "https://www.fromtheroad.ford.com/content/dam/fordmediasite/us/en/library/2026/specs/2026_Ford_Ranger%20Technical_Specs.pdf"),
  ("Toyota, 2024 Tacoma eBrochure, specifications table", "https://www.toyota.com/content/dam/toyota/brochures/pdf/2024/tacoma_ebrochure.pdf"),
  ("Ford, 2026 Maverick Technical Specifications (v1.2, 20 Jul 2026)", "https://www.fromtheroad.ford.com/content/dam/fordmediasite/us/en/library/2026/specs/2026_Ford_Maverick_Specs.pdf"),
 ],
}
