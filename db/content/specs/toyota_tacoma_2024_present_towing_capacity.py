"""Generation spec page (SAMPLE, not published): 2024-present Toyota Tacoma towing capacity, model year by model year.
Figures copied from Toyota's 2024 brochure specification table and Toyota's 2025 press release."""
KIND = "generation"
GEN = "2024-present"
KEY = ("toyota", "tacoma", "towing-capacity")
MAKE, MODEL, TOPIC_LABEL = "Toyota", "Tacoma", "Towing capacity"
PUBLISH = False

TITLE = "2024–2025 Toyota Tacoma Towing Capacity by Model Year"
SEO_TITLE = "2024–2025 Toyota Tacoma Towing Capacity by Year"
META = ("2024 and 2025 Toyota Tacoma towing capacity from Toyota's own tables: 3,500 lb for the SR, 6,000 to 6,500 lb "
        "for every other grade.")

FAQ = [
 ("What is the towing capacity of a 2024 Toyota Tacoma?",
  "Between 3,500 and 6,500 lb. Toyota's 2024 table lists 3,500 lb for the SR, 6,500 lb for the XtraCab SR5 and TRD PreRunner, 6,400 lb for the Double Cab SR5, TRD Sport and TRD Off-Road, 6,300 lb for the Limited and 6,000 lb for the Trailhunter and TRD Pro."),
 ("What is the towing capacity of a 2025 Toyota Tacoma?",
  "Toyota's 2025 release states a maximum of up to 6,500 lb for the lineup. It does not break the figure down by grade."),
 ("Does the 2024 Tacoma hybrid tow more?",
  "Not in Toyota's table. The TRD Pro and Trailhunter, which come only with the i-FORCE MAX hybrid, are listed at 6,000 lb."),
 ("Is this the limit for my truck?",
  "It is the figure Toyota published for that cab and grade. The limit for your truck is in its owner's manual and on its door-jamb labels."),
]

PAGE = {
 "gen_label": "2024–2025",
 "answer": "A 2024 Toyota Tacoma tows 3,500 lb as an SR and 6,000 to 6,500 lb in every other grade, by Toyota's specification table. For 2025 Toyota states a lineup maximum of up to 6,500 lb.",
 "reviewed": "2026-11-20",
 "covers": "Model years 2024 and 2025",
 "not_covered": "2026: Toyota's table for this year is not on this page yet.",
 "years": {"2025": "y2025", "2024": "y2024"},
 "sections": [
  {"id": "y2025", "h": "2025 Tacoma towing capacity",
   "table": {"head": ["What Toyota states", "Figure"], "rows": [
     ["Maximum towing capacity, whole lineup", "Up to 6,500 lb", 2]]},
   "notes": ["Toyota's 2025 release gives the lineup maximum only."]},
  {"id": "y2024", "h": "2024 Tacoma towing capacity",
   "intro": "Toyota's 2024 brochure lists one maximum towing weight per cab and grade.",
   "table": {"head": ["Cab", "Grade", "Maximum towing"], "rows": [
     ["XtraCab", "SR", "3,500 lb", 1],
     ["XtraCab", "SR5", "6,500 lb", 1],
     ["XtraCab", "TRD PreRunner", "6,500 lb", 1],
     ["Double Cab", "SR", "3,500 lb", 1],
     ["Double Cab", "SR5", "6,400 lb", 1],
     ["Double Cab", "TRD Sport", "6,400 lb", 1],
     ["Double Cab", "TRD Off-Road", "6,400 lb", 1],
     ["Double Cab", "Limited", "6,300 lb", 1],
     ["Double Cab", "Trailhunter", "6,000 lb", 1],
     ["Double Cab", "TRD Pro", "6,000 lb", 1]]},
   "notes": ["Toyota's footnote on this row: never tow beyond a vehicle's published towing capacities."]},
 ],
 "check": [
  "Pick your model year above, then find your cab and grade in the table.",
  "Read the labels on the driver's door jamb and the towing section of your owner's manual for the limits of your own truck.",
  "Check the tongue weight limit in the manual before choosing a hitch or ball mount.",
  "Your owner's manual and the labels on your truck override this page.",
 ],
 "related": ["hitches", "bed-racks", "tonneau-covers"],
 "sources": [
  ("Toyota, 2024 Tacoma eBrochure, specifications table", "https://www.toyota.com/content/dam/toyota/brochures/pdf/2024/tacoma_ebrochure.pdf"),
  ("Toyota Newsroom, The 2025 Toyota Tacoma is Ready for Adventure (17 Dec 2024)", "https://pressroom.toyota.com/?generate_pdf=97924"),
 ],
}
