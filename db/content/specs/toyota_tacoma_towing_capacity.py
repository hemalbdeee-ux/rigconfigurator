"""Spec page: Toyota Tacoma towing capacity. Figures copied from Toyota's brochure specification tables and press releases.
DRAFT: model years 2016-2020, 2022 and 2026 are not read yet; do not publish until they are, or the title is narrowed.
"""
KEY = ("toyota", "tacoma", "towing-capacity")
MAKE, MODEL, TOPIC_LABEL = "Toyota", "Tacoma", "Towing capacity"
PUBLISH = False

TITLE = "Toyota Tacoma Towing Capacity by Year, Cab and Grade"
SEO_TITLE = "Toyota Tacoma Towing Capacity by Year, Cab and Grade"
META = ("Toyota Tacoma towing capacity from Toyota's spec tables: 3,500 to 6,500 lb for 2024, up to 6,800 lb for 2021 "
        "and 2023, by cab, grade and engine.")

FAQ = [
 ("How much can a Toyota Tacoma tow?",
  "It depends on the year and the build. Toyota's 2024 specification table lists 3,500 lb for the SR and up to 6,500 lb for the XtraCab SR5 and TRD PreRunner. For 2021 and 2023, Toyota lists 3,500 lb with the 2.7L four-cylinder and 6,400 to 6,800 lb with the 3.5L V6, depending on cab and drivetrain."),
 ("Which Tacoma tows the most?",
  "In the brochures we read, the highest figure is 6,800 lb: a 2021 or 2023 Access Cab with the 3.5L V6, automatic transmission and 4x2. For the 2024 truck the highest figure is 6,500 lb, on the XtraCab SR5 and TRD PreRunner."),
 ("Does the hybrid Tacoma tow more?",
  "Not in Toyota's 2024 table. The TRD Pro and Trailhunter, which come only with the i-FORCE MAX hybrid, are listed at 6,000 lb, below the 6,400 lb of the non-hybrid Double Cab SR5."),
 ("Is the towing capacity on this page the limit for my truck?",
  "No. It is the figure Toyota published for that configuration. The limit for your truck is on its door-jamb labels and in its owner's manual, and it drops with passengers and cargo on board."),
]

PAGE = {
 "answer": "A Toyota Tacoma tows between 3,500 and 6,800 lb, depending on model year, engine, cab and drivetrain. The 2024 Tacoma is rated at 3,500 lb (SR) to 6,500 lb (XtraCab SR5 and TRD PreRunner). The 2021 and 2023 trucks are rated at 3,500 lb with the 2.7L four-cylinder and 6,400 to 6,800 lb with the 3.5L V6.",
 "reviewed": "2026-11-16",
 "covers": "Model years 2021, 2023, 2024 and 2025",
 "not_covered": "2016 to 2020, 2022 and 2026: Toyota's tables for these years are not on this page yet.",
 "sections": [
  {"id": "2024", "h": "2024 Tacoma (4th generation)",
   "intro": "Toyota's 2024 brochure lists one maximum towing weight per cab and grade.",
   "table": {"head": ["Cab", "Grade", "Maximum towing (lb)"], "rows": [
     ["XtraCab", "SR", "3,500", 1],
     ["XtraCab", "SR5", "6,500", [1, 3]],
     ["XtraCab", "TRD PreRunner", "6,500", [1, 3]],
     ["Double Cab", "SR", "3,500", 1],
     ["Double Cab", "SR5", "6,400", 1],
     ["Double Cab", "TRD Sport", "6,400", 1],
     ["Double Cab", "TRD Off-Road", "6,400", 1],
     ["Double Cab", "Limited", "6,300", 1],
     ["Double Cab", "Trailhunter", "6,000", 1],
     ["Double Cab", "TRD Pro", "6,000", 1]]},
   "notes": ["Trailhunter and TRD Pro come only with the i-FORCE MAX hybrid powertrain."]},
  {"id": "2025", "h": "2025 Tacoma",
   "table": {"head": ["What Toyota states", "Figure"], "rows": [
     ["Maximum towing capacity, whole lineup", "Up to 6,500 lb", 2]]},
   "notes": ["Toyota's 2025 release gives the lineup maximum only. It does not break the figure down by cab or grade."]},
  {"id": "2021-2023", "h": "2021 and 2023 Tacoma (3rd generation)",
   "intro": "Toyota's 2021 and 2023 brochures print the same figures. The table shows 4x2 and 4x4; a dash means Toyota lists no figure for that combination.",
   "table": {"head": ["Engine and transmission", "Cab", "Grade", "4x2 (lb)", "4x4 (lb)"], "rows": [
     ["2.7L four-cylinder, automatic", "Access Cab", "SR, SR5", "3,500", "3,500", [4, 5]],
     ["2.7L four-cylinder, automatic", "Double Cab", "SR, SR5", "3,500", "—", [4, 5]],
     ["3.5L V6, automatic", "Access Cab", "SR, SR5, TRD Sport", "6,800", "6,500", [4, 5]],
     ["3.5L V6, automatic", "Access Cab", "TRD Off-Road", "—", "6,500", [4, 5]],
     ["3.5L V6, automatic", "Double Cab", "SR", "—", "6,400", [4, 5]],
     ["3.5L V6, automatic", "Double Cab", "SR5, TRD Sport, TRD Off-Road", "6,700", "6,400", [4, 5]],
     ["3.5L V6, automatic", "Double Cab", "Limited", "6,600", "6,400", [4, 5]],
     ["3.5L V6, automatic", "Double Cab", "TRD Pro", "—", "6,400", [4, 5]],
     ["3.5L V6, manual", "Access Cab", "TRD Sport, TRD Off-Road", "—", "6,500", [4, 5]],
     ["3.5L V6, manual", "Double Cab", "TRD Sport, TRD Off-Road, TRD Pro", "—", "6,400", [4, 5]]]},
   "notes": ["Double Cab long-bed trucks have their own row in Toyota's table. We could not match its values to grades with certainty, so they are left out."]},
 ],
 "check": [
  "Find your cab, grade, engine and drivetrain in the table. The figure applies to that combination only.",
  "Read the labels on the driver's door jamb. The trailer you can pull also depends on your truck's gross combined weight rating, minus the truck, passengers and cargo.",
  "Check the tongue weight limit in your owner's manual before choosing a hitch or a ball mount.",
  "Your owner's manual and the labels on your truck override this page.",
 ],
 "related": ["hitches", "bed-racks", "tonneau-covers"],
 "sources": [
  ("Toyota, 2024 Tacoma eBrochure, specifications table", "https://www.toyota.com/content/dam/toyota/brochures/pdf/2024/tacoma_ebrochure.pdf"),
  ("Toyota Newsroom, The 2025 Toyota Tacoma is Ready for Adventure (17 Dec 2024)", "https://pressroom.toyota.com/?generate_pdf=97924"),
  ("Toyota Newsroom, All-New 2024 Toyota Tacoma is Adventure Ready Out of the Box", "https://pressroom.toyota.com/all-new-2024-toyota-tacoma-is-adventure-ready-out-of-the-box/"),
  ("Toyota, 2023 Tacoma eBrochure, specifications table", "https://www.toyota.com/content/dam/toyota/brochures/pdf/2023/tacoma_ebrochure.pdf"),
  ("Toyota, 2021 Tacoma eBrochure, specifications table", "https://www.toyota.com/content/dam/toyota/brochures/pdf/2021/tacoma_ebrochure.pdf"),
 ],
}
