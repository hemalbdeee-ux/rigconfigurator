"""Spec page: Ford Maverick bed size. Figures copied from Ford's technical specification sheets and ford.com.
"""
KEY = ("ford", "maverick", "bed-dimensions")
MAKE, MODEL, TOPIC_LABEL = "Ford", "Maverick", "Bed size"
PUBLISH = True
PUBLISH_AT = "2026-11-19"

TITLE = "Ford Maverick Bed Size: Length, Width and Height in Inches"
SEO_TITLE = "Ford Maverick Bed Size: Length, Width and Height"
META = ("Ford Maverick bed size from Ford's spec sheets: 54.4 in long, 42.6 in between the wheelhouses, 20.3 in deep, "
        "33.3 cu ft, plus lift-in height and payload.")

FAQ = [
 ("How long is the Ford Maverick bed?",
  "54.4 in (about 4.5 ft) at the floor with the tailgate closed, according to Ford's 2025 and 2026 specification sheets. Ford's website gives 72 in (6 ft) of floor length with the tailgate open."),
 ("How wide is the Maverick bed between the wheel wells?",
  "42.6 in. The bed is 53.3 in wide wall to wall, so a 48 in sheet lies flat above the wheelhouses but not between them."),
 ("Is the bed the same on the Tremor and Lobo?",
  "Yes for the box itself: Ford's sheets list one set of bed dimensions for every Maverick. What changes is the lift-in height and the payload."),
 ("Does every Maverick have the same bed length?",
  "In the model years on this page, yes. The Maverick is sold in one cab and one bed length."),
]

PAGE = {
 "answer": "The Ford Maverick bed is 54.4 in (about 4.5 ft) long at the floor, 42.6 in wide between the wheelhouses, 53.3 in wide wall to wall and 20.3 in deep, with 33.3 cu ft of volume. With the tailgate open the floor is 72 in (6 ft) long. The Maverick comes with one bed size.",
 "reviewed": "2026-11-16",
 "covers": "Model years 2025, 2026 and 2027",
 "not_covered": "2022 to 2024: Ford's sheets for these years are not on this page yet.",
 "sections": [
  {"id": "bed", "h": "Maverick bed dimensions",
   "table": {"head": ["Measurement", "Figure"], "rows": [
     ["Bed length at the floor, tailgate closed", "54.4 in", [1, 2, 3]],
     ["Floor length with the tailgate open", "72 in", 3],
     ["Bed length at the top of the body", "53.1 in", [1, 2]],
     ["Width between the wheelhouses", "42.6 in", [1, 2, 3]],
     ["Width, wall to wall", "53.3 in", [1, 2, 3]],
     ["Rear opening width, top of the box", "49.8 in", [1, 2]],
     ["Rear opening width, lower", "48.8 in", [1, 2]],
     ["Bed height", "20.3 in", [1, 2]],
     ["Cargo volume", "33.3 cu ft", [1, 2, 3]]]}},
  {"id": "lift-in", "h": "Lift-in height by powertrain (2026)",
   "intro": "The lift-in height is how far the open tailgate sits above the ground.",
   "table": {"head": ["Powertrain or trim", "Lift-in height"], "rows": [
     ["2.5L Hybrid, FWD", "30.4 in", [1, 2]],
     ["2.5L Hybrid, AWD", "29.4 in", 1],
     ["2.0L EcoBoost, FWD", "30.5 in", 1],
     ["2.0L EcoBoost, AWD", "29.4 in", [1, 2]],
     ["Tremor", "30.0 in", [1, 2]],
     ["Lobo", "28.2 in", [1, 2]]]}},
  {"id": "payload", "h": "Maximum payload by powertrain (2026)",
   "table": {"head": ["Powertrain or trim", "Maximum payload"], "rows": [
     ["2.5L Hybrid, FWD", "1,500 lb", [1, 2]],
     ["2.5L Hybrid, AWD", "1,400 lb", [1, 2]],
     ["2.0L EcoBoost, FWD", "1,500 lb", 1],
     ["2.0L EcoBoost, AWD", "1,500 lb", [1, 2]],
     ["Tremor", "1,140 lb", [1, 2]],
     ["Lobo", "1,045 lb", [1, 2]]]},
   "notes": ["Payload includes passengers. The figure for your truck is on the yellow tire and loading label on the driver's door jamb."]},
 ],
 "check": [
  "Measure the floor from the bulkhead to the inside of the closed tailgate. It should read about 54 in.",
  "Buying a tonneau cover or a bed rack: order by model year and the 4.5 ft bed. Covers for other trucks do not fit.",
  "Carrying long loads: with the tailgate open the floor is 72 in long; anything longer overhangs the tailgate.",
  "Your owner's manual and the labels on your truck override this page.",
 ],
 "related": ["tonneau-covers", "bed-racks"],
 "sources": [
  ("Ford, 2026 Maverick Technical Specifications", "https://www.fromtheroad.ford.com/content/dam/fordmediasite/us/en/library/2026/specs/2026_Ford_Maverick_Specs.pdf"),
  ("Ford, 2025 Maverick and Lobo Technical Specifications", "https://www.fromtheroad.ford.com/content/dam/fordmediasite/us/en/library/2025/specs/2025-Ford-Maverick-and-Lobo-Technical-Specs.pdf"),
  ("Ford.com, Maverick specifications (2027 model year page, read 16 Nov 2026)", "https://www.ford.com/trucks/maverick/specs/"),
 ],
}
