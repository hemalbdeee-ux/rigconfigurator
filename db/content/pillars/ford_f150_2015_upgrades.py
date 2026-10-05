"""Upgrades pillar: 2015–2020 Ford F-150 (13th gen, P552). This generation has ended, so the real span is used.
Hub page: ranks the three published 2015–2020 F-150 category guides and links to them. No product picks or ASINs
here (the site pulls each guide's #1 pick). Every price band comes from the linked guides' picks[].price fields;
vehicle facts from db/migrations/003_vehicles.sql (beds stored as 66/78/96 in, aluminum bed, bed utility track
optional, Class IV, 2 in receiver, 13,200 lb, Raptor 2017+), the three guides and their sources, and four pages
opened for this page on 2026-10-03:
- Wikipedia, F-Series thirteenth generation: model years 2015–2020, three cabs, which cab gets which bed, all Raptors
  5.5 ft, Raptor back for 2017 in SuperCab and SuperCrew, the 2018 refresh (grille, tailgate emblem, taillamps,
  engines, 10-speed, diesel), power running boards on the Limited trim.
- Wikipedia, F-Series fourteenth generation: the 2021 redesign changed 92% of parts and carried over only the cab,
  the pickup box structure and the font design.
- Ford's 2020 RV and Trailer Towing Guide (the PDF on Ford of Canada's site, read through a text extraction): F-150
  hitch receiver "included with Trailer Tow Packages" 53A, 53B and 53C; 5,000 lb bumper-only limit; tow package
  required over 5,000 lb; 13,200 lb top figure under the 3.5L EcoBoost.
- Motor Authority report on the 2018 F-150: 13,200 lb towing with the 3.5L EcoBoost, 3,270 lb payload with the 5.0L V8.
Not verified, and worded as such in the text: factory receiver and tow package content for 2015–2019 and for US
trucks specifically (only the 2020 guide was read, so the page prints no trim list); the receiver's class and size
in Ford's guide (the extraction did not show them; Class IV and 2 in come from our vehicle data); the maximum tow
and payload figures for 2015–2017; which trims other than the Limited had factory running boards; why BAK, Retrax
and Gator split hard cover part numbers at 2021 when the box structure carried over; whether any maker treats the
2018 tailgate differently; whether rack warranties transfer to a second owner; a Regular Cab liner part (no pick in
the floor liner guide); whether a given roll-up is on Putco's "inside-rail" list.
Disagreements stated on the page: vehicle data beds (66/78/96 in) vs the guides' rail lengths (67.1/78.9/97.6 in);
the vehicle data note that "most" tonneau and bed rack fitments carry over to 2021+ vs the tonneau guide's finding
that 2021+ hard covers usually do not fit; Rough Country's 2015–2026 range for the 10406 vs the Amazon title's
2015–2023; Tyger's 2015–2020 range on the 5.5 ft T3 vs 2015–2026 on the 6.5 ft T3.
Source fixes 2026-10-04: 003_vehicles.sql now stores the beds as 67/79/98 in (rounded rail lengths, not the nominal
66/78/96) and its carry-over note now says hard covers split at 2021, so the page no longer reports those two as
disagreements.
"""

KIND = "upgrades"
KEY = ("ford", "f-150", "2015-2020")
CATEGORIES = ["floor-mats", "tonneau-covers", "bed-racks", "running-boards"]

TITLE = "2015–2020 Ford F-150 Upgrades, Ranked: 3 Mods in Order, With Bed Length and 2021 Part-Number Traps"
META = ("Three 2015–2020 F-150 upgrades in buying order: floor liners, tonneau cover and bed rack, with bed length, "
        "cab, 2021 part-number splits and price notes.")

FAQ = [
 ("What should I upgrade first on a 2015–2020 F-150?",
  "Floor liners, then a tonneau cover. Liners cost the least, about $80–$220 for a full set in our guide, and they "
  "need three facts from you: SuperCrew or SuperCab, bench or buckets, and whether fold-flat storage sits under the "
  "rear seat. The cover comes second and needs two: bed length at the rail and a part number listed for 2015–2020. "
  "The bed rack comes last, but decide on it before you pay for the cover, since a standard folding cover leaves "
  "no place to mount most racks. On a tight budget, a budget liner set and Tyger's T3 soft tri-fold at about $228 "
  "come to about $308–$348."),
 ("Do tonneau covers and other parts for the 2021 and later F-150 fit a 2015–2020 truck?",
  "Some do, and the part number tells you which. Wikipedia says the 2021 redesign carried over the cab and the "
  "pickup box structure, and several makers list one part across both trucks: Husky's WeatherBeater 94041 and 94051 "
  "liners for 2015–2026, TruXedo's Lo Pro 597701 cover for 2015–2026 and Putco's Venture TEC 184100 rack for "
  "2015–2027 5'7\" beds. Hard covers are the exception. BAK sells the MX4 as 448329 for 2015–2020 and 448339 for "
  "2021 and later, and Retrax sells the PRO MX as 80373 and 80378. Our tonneau guide's answer for a 2021+ hard "
  "cover on this truck is usually not. Buy the number listed for your model year."),
 ("Do I need to buy a trailer hitch for a 2015–2020 F-150, and how much can it tow?",
  "Maybe not. Look under the rear bumper. Our vehicle data lists a Class IV hitch with a 2 in receiver for "
  "this generation, but Ford's 2020 RV and Trailer Towing Guide lists the F-150's receiver as included with the "
  "trailer tow packages, codes 53A, 53B and 53C. A truck ordered without one may have no receiver. We read only "
  "the 2020 guide, so we can't say how 2015–2019 trucks were equipped. Our data lists a 13,200 lb maximum, which "
  "Motor Authority reported for the 2018 truck with the 3.5L EcoBoost. We did not confirm the 2015–2017 figure. "
  "Your number is on the door-jamb label. If your truck has a receiver, an aftermarket trailer hitch adds "
  "nothing."),
 ("Can I run a tonneau cover and a bed rack together on a 2015–2020 F-150?",
  "Yes, if you plan them as a pair. Our guides document five routes. Putco says its Venture TEC rack works with "
  "most inside-rail roll-up covers. RealTruck says Putco's Quick Rack works with roll-ups such as the BAK Revolver "
  "and Extang Revolution but must come off to open hard folders like the BAKFlip and Gator FX. The RealTruck GoRack "
  "suits covers with a T-slot rail system, and Retrax sells the PRO in an XR version, T-80373, with those rails. "
  "Rough Country says its low-profile hard cover works with bed racks. Yakima's towers need Tonneau Kit 1 for "
  "select covers."),
 ("How much does it cost to add all three upgrades to a 2015–2020 F-150?",
  "From the prices on our three guides' picks, a budget build runs about $808–$848: Motor Trend's contour mats or "
  "Broryan's TPE set, Tyger's T3 soft tri-fold and Rough Country's 10406 rack. A mid build runs about $1,409–$1,920 "
  "with OEDRO or AKM liners, a TruXedo Lo Pro, Gator EFX or Rough Country hard cover, and Yakima's OutPost HD towers "
  "or the RealTruck GoRack. A premium build with Husky's WeatherBeater set, a BAKFlip MX4 or RetraxPRO MX, and "
  "either Yakima's OverHaul HD towers or Putco's Venture TEC runs about $2,400–$4,769. Yakima crossbars are extra, "
  "and all figures are approximate."),
 ("Does the 2017–2020 Raptor need different parts?",
  "It needs 5.5 ft parts and a listing that names it. Every Raptor of this generation, SuperCab or "
  "SuperCrew, has the 5.5 ft bed. RealTruck lists the BAKFlip MX4 448329, the RetraxPRO MX 80373 and the TruXedo "
  "Lo Pro 597701 for the 2017–2020 Raptor, and Putco lists the Venture TEC 184100 for the Raptor's 5'7\" bed. "
  "Floor liners follow the cab, so a SuperCab Raptor needs a SuperCab set, and our floor liner guide says to confirm Raptor fit with the seller because some interiors and "
  "seat options differ. On rough trails, load a rack to its off-road figure: 300 lb on the Venture TEC."),
 ("Did the 2018 refresh change which accessories fit?",
  "Not in any way our three guides found. Wikipedia describes the 2018 update as a new grille, an embossed F-150 "
  "emblem on the tailgate, revised taillamps, new engines and a 3.0L Power Stroke diesel during the model year. None of the liners, covers or racks in our guides is listed with a split "
  "at 2018: the makers give 2015–2020 or a longer span as one range. We did not find a maker statement about the "
  "2018 tailgate, so if a listing stops at 2017 or starts at 2018, ask the seller why."),
 ("Is a used tonneau cover or bed rack a safe buy for this truck?",
  "It can be, with two checks. First, the part number. Our tonneau guide's rule is to read it off the frame label "
  "and look it up before paying: 448329, 80373 and GC24019 are the 2015–2020 5.5 ft numbers for the BAKFlip MX4, "
  "RetraxPRO MX and Gator EFX, and a cover pulled off a 2021+ truck may carry a different one. Second, the "
  "warranty. Our guide notes that none of its covers' warranties transfers to a second owner, so a used cover has "
  "none. For a used rack, confirm the bed length it was made for and get all the hardware."),
 ("I have a SuperCab or an 8 ft bed. What changes on this list?",
  "More than on a SuperCrew short box. For floor liners, most budget brands in our guide cut SuperCrew sets only; "
  "Husky's 94051 is the SuperCab set, about $150–$210, and the 18361 front pair is listed for both cabs. For a "
  "cover, the SuperCab came with the 6.5 or 8 ft box, so order 6.5 ft parts such as the RetraxPRO MX 80374 or Tyger "
  "TG-BC3F1042, and expect fewer premium choices at 8 ft. For a rack, the one-piece "
  "picks are 5.5 ft parts. Putco's Quick Rack covers the 2015–2020 6'7\" bed, and Yakima's clamp towers are the "
  "usual route on the 8 ft box."),
]

ARTICLE = {
 "dek": "Three upgrades for the 13th-generation F-150, in the order most owners should buy them. The truck went out "
        "of production in 2020, so the order is shaped by three bed lengths, three cabs, an aluminum bed, and "
        "listings that blur this generation with the 2021 redesign: some parts span both trucks, and the big-name "
        "hard covers do not.",
 "author": "jake-morrison",
 "reviewed": "2026-10-03",
 "method": "We did not install any of these parts ourselves. The order comes from our three fit-checked 2015–2020 "
           "F-150 guides, weighing how many trucks each upgrade suits, what it costs, how often it's used and how "
           "much of its fit is confirmed for this generation (bed length, cab, year range). Price bands "
           "are the prices listed on those guides' picks, checked at maker and retailer stores in September 2026. Vehicle facts come from our vehicle data, the guides' sources, Wikipedia's "
           "thirteenth- and fourteenth-generation F-Series pages, Ford's 2020 RV and Trailer Towing Guide and a "
           "Motor Authority report on the 2018 truck. Where we couldn't confirm a factory detail, the text says so.",
 "takeaways": [
  "**Match the year range, part by part.** Hard covers from BAK, Retrax and Gator split at 2021; Husky liners, the TruXedo Lo Pro and Putco's Venture TEC span both generations.",
  "**Bed decides the bed parts.** The boxes measure 67.1, 78.9 and 97.6 in at the rail, and a SuperCrew or SuperCab can have either of two.",
  "**Cab and rear floor decide the liners.** Rear liners are cab-specific, and several SuperCrew sets exclude fold-flat storage under the rear seat.",
  "**Choose the cover and the rack as a pair.** Putco's Quick Rack must come off to open a BAKFlip; roll-ups and T-slot covers leave more options.",
  "**Look for a receiver before shopping for a hitch.** Our data lists a Class IV, 2 in receiver, and Ford's 2020 towing guide ties it to the tow packages.",
 ],
 "priority": [
  {"category": "floor-mats",
   "h": "1. Floor liners first: the lowest price, and the part most likely to move to your next truck",
   "why": "Floor liners lead because they cost the least on this page and carry the least risk on a truck that is "
          "out of production. Three facts decide fit: cab, front seat and rear floor. Husky's WeatherBeater 94041 "
          "is the SuperCrew set and the 94051 is the SuperCab set, while the 18361 front pair is listed for both cabs. A 40/20/40 front bench leaves a "
          "center strip of carpet that most two-piece front liners don't reach, and AKM's set is cut for bucket seats. "
          "On a SuperCrew, lift the rear cushion: the 94041, OEDRO and Broryan listings all exclude fold-flat "
          "storage. Wikipedia says the 2021 redesign kept the cab, and "
          "Husky lists the 94041 and 94051 for 2015–2026, so the set can move to a newer truck. Prices in our guide "
          "run about $80–$120 for Motor Trend's contour mats or Broryan's TPE, about $90–$130 for OEDRO or AKM, and "
          "about $150–$220 for the 94041, which Husky makes in the USA with a lifetime warranty against cracks and "
          "breaks. The trade-off: Husky is firmer, and the TPE brands publish less about warranty.",
   "skip_if": "Your XL has the vinyl work floor, which cleans easily, or the truck came with a molded set that hooks to the retention posts."},
  {"category": "tonneau-covers",
   "h": "2. Tonneau cover second: buy by rail length, then by the 2015–2020 part number",
   "why": "A tonneau cover ranks second because every bed benefits from being dry and out of sight. It is also where "
          "an ended generation causes the most wrong orders. Two checks decide fit. First, bed length at the rail: 67.1 in for the 5.5 ft box, 78.9 in for the 6.5 ft and 97.6 in for the "
          "8 ft. Second, the year range. BAK, Retrax and Gator "
          "sell separate parts for each generation: the BAKFlip MX4 is 448329 for 2015–2020 and 448339 for 2021 and "
          "later, and the RetraxPRO MX is 80373 against 80378. TruXedo's Lo Pro 597701 is the exception, one part "
          "for 2015–2026. Prices in our guide run about $228 for Tyger's T3 soft tri-fold, about $520 for the Lo "
          "Pro, about $549 for the Gator EFX, about $700 for Rough Country's low-profile hard cover, about $1,050 "
          "for the MX4 and about $2,150 for the RetraxPRO MX. Spread evenly, the Retrax carries 500 lb, the BAK "
          "400 lb and the Gator 300 lb; Rough Country publishes no figure. The trade-off is price against the "
          "truck's age, since none of these warranties transfers to the next owner. If a bed rack is likely, read "
          "slot three before paying.",
   "skip_if": "You haul tall loads most days and would spend more time removing the cover than using it."},
  {"category": "bed-racks",
   "h": "3. Bed rack last: decide it early, buy it when you need it",
   "why": "The bed rack comes last because the fewest owners need one and it costs the most. It also ages well on "
          "this truck: Putco lists the Venture TEC 184100 for 2015–2027 5'7\" beds, Rough "
          "Country lists the 10406 for 2015–2026, and Yakima's clamp towers aren't tied to one truck. Bed length "
          "comes first. The 184100, the RealTruck GoRack 9250101 and the 10406 are all 5.5 ft "
          "parts, the 6.5 ft box gets Putco's 2015–2020 Quick Rack, and 8 ft owners are mostly pointed to Yakima's "
          "towers. Anchors come second: the Putco racks and the GoRack bolt into the stake pockets, not the BoxLink "
          "cleats. The bed is aluminum, so torque figures matter. Prices run about $500 for the "
          "Rough Country rack, about $799 for Yakima's OutPost HD towers, about $1,052–$1,090 for the Quick Rack or "
          "GoRack, about $1,200 for the OverHaul HD towers and about $2,069–$2,399 for the Venture TEC. Putco and "
          "RealTruck rate their racks at 1,000 lb static and 600 lb dynamic, Rough Country at 750 and 400 lb, and "
          "Yakima at 500 lb on-road. If you camp from the truck, move this slot up to second and choose the cover "
          "around the rack.",
   "skip_if": "Your loads fit under a cover and you don't carry boats, ladders or a tent."},
 ],
 "tier_table": {
  "caption": "Approximate price bands from the picks in our 2015–2020 F-150 guides (September 2026; Amazon prices move daily)",
  "head": ["Upgrade", "Budget", "Mid", "Premium"],
  "rows": [
   ["Floor liners", "About $80–$120 (Motor Trend contour mats or Broryan TPE)", "About $90–$130 (OEDRO or AKM TPE)", "About $150–$220 (Husky WeatherBeater 94041)"],
   ["Tonneau cover", "About $228 (Tyger T3 soft tri-fold)", "About $520 (TruXedo Lo Pro), $549 (Gator EFX) or $700 (Rough Country low-profile hard cover)", "About $1,050 (BAKFlip MX4) to $2,150 (RetraxPRO MX)"],
   ["Bed rack", "About $500 (Rough Country 10406)", "About $799 (Yakima OutPost HD towers, crossbars extra) to $1,090 (RealTruck GoRack); Putco's Quick Rack starts at about $1,052", "About $1,200 (Yakima OverHaul HD towers, crossbars extra) to $2,069–$2,399 (Putco Venture TEC)"],
   ["Total", "About $808–$848", "About $1,409–$1,920", "About $2,400–$4,769"],
  ],
 },
 "sections": [
  {"h": "Towing and steps: check what the truck already has",
   "body": "There is no trailer hitch guide for the 2015–2020 F-150 on this site, so hitches are not ranked here. "
           "Running boards now have their own guide for this truck, sorted by cab, so they are not ranked again here.\n\n"
           "**The receiver.** Our vehicle data lists a **Class IV hitch with a 2 in receiver** for this generation. "
           "Not every truck has one. Ford's 2020 RV and Trailer Towing Guide lists "
           "the F-150's hitch receiver as included with the trailer tow packages, option codes 53A, 53B and 53C. We "
           "read the 2020 guide only, as a text extraction of the copy on Ford of Canada's site, so we can't speak "
           "for 2015–2019 trucks. Look under the rear bumper and read the window sticker. If a receiver is there, an aftermarket trailer hitch adds nothing.\n\n"
           "**The rating.** Our vehicle data lists a maximum of **13,200 lb**. Motor Authority reported that figure "
           "for the 2018 truck with the 3.5L EcoBoost, and Ford's 2020 guide shows the same top number under that "
           "engine. We did not confirm the maximum for 2015–2017. Your figure is on the door-jamb label and in the "
           "owner's manual, and a receiver bolted on later never raises it. As we read the 2020 guide, Ford says "
           "not to exceed a 5,000 lb trailer when towing on the bumper alone, and requires the Trailer Tow Package "
           "or Max Trailer Tow Package above 5,000 lb.\n\n"
           "**The steps.** Wikipedia's page lists power running boards on the Limited trim. We did not confirm which "
           "other trims had factory boards, so look before pricing a set."},
  {"h": "SuperCrew, SuperCab or Regular Cab, and three bed lengths",
   "body": "Cab decides the floor liners. Bed length decides the cover and, for one-piece racks, the rack. The cab "
           "doesn't tell you the bed. Wikipedia and our tonneau guide agree that the SuperCrew came with the 5.5 or "
           "6.5 ft box, the SuperCab and Regular Cab with the 6.5 or 8 ft box, and every 2017–2020 Raptor with the "
           "5.5 ft box, the SuperCab Raptor included.\n\n"
           "The 5.5, 6.5 and 8 ft names are nominal. Both bed guides give 67.1, 78.9 and 97.6 in at the rail, our vehicle data rounds those to 67, 79 and 98 in, and retailers print 5'7\", 6'7\" and 8'2\". Measure inside the bed at the "
           "rail, from the bulkhead to the inside of the closed tailgate.",
   "table": {"caption": "2015–2020 F-150 cab and bed combinations",
             "head": ["Cab / bed", "Covers and racks", "Floor liners", "Notes"],
             "rows": [
              ["SuperCrew, 5.5 ft (67.1 in)", "Covers: MX4 448329, RetraxPRO MX 80373, Gator EFX GC24019, Lo Pro 597701, Tyger TG-BC3F1041. Racks: Putco 184100, GoRack 9250101, Rough Country 10406", "Every SuperCrew set in our guide", "The bed most one-piece racks fit"],
              ["SuperCrew, 6.5 ft (78.9 in)", "Covers: RetraxPRO MX 80374, Gator EFX GC24020, Tyger TG-BC3F1042. Rack: Putco's 6'7\" Quick Rack or Yakima towers", "Same SuperCrew sets", "Order by bed, not by cab"],
              ["SuperCab, 6.5 ft", "Same 6.5 ft covers and racks", "Husky 94051 set, or the 18361 front pair", "Most budget brands cut SuperCrew sets only"],
              ["SuperCab, 8 ft (97.6 in)", "Fewer premium covers; soft roll-ups are common. Yakima towers for a rack", "Husky 94051 set", "Fleet and work trucks"],
              ["Regular Cab, 6.5 or 8 ft", "Match the bed length", "No Regular Cab set in our guide; ask the seller", "Front row only"],
              ["Raptor, 2017–2020, 5.5 ft", "5.5 ft parts that name the Raptor, such as MX4 448329, Lo Pro 597701 and Putco 184100", "The set for your cab; confirm Raptor with the seller", "SuperCab or SuperCrew"],
             ]}},
  {"h": "What carries over to the newer truck, and what stops at 2020",
   "body": "The parts catalog for this truck is tangled with the newer truck's. "
           "Wikipedia says the 2021 redesign changed 92% of the F-150's parts and carried over only the cab, the "
           "pickup box structure and the font design. That fits what the listings show: floor liners cut for the cab "
           "and racks that bolt into the stake pockets often span both generations.\n\n"
           "Not everything interchanges. BAK, Retrax and Gator sell their hard covers under separate "
           "part numbers on each side of 2021. We could not confirm why. Our tonneau guide's finding is that a 2021+ hard cover usually does not fit this truck, so go by the part number. Owners of the newer truck should use the 2021–2026 F-150 page.",
   "table": {"caption": "Year ranges the makers and listings give for the parts in our 2015–2020 F-150 guides",
             "head": ["Part", "Listed years", "Moves to a 2021+ truck?"],
             "rows": [
              ["Husky WeatherBeater 94041 and 94051", "2015–2026", "Yes; check the rear storage option"],
              ["OEDRO and Broryan TPE liners", "2015–2025", "Yes, per the listings"],
              ["AKM TPE liners; Motor Trend contour mats", "2015–2020", "Not listed for it"],
              ["BAKFlip MX4 448329", "2015–2020; 448339 is the 2021+ part", "No"],
              ["RetraxPRO MX 80373", "2015–2020; 80378 is the 2021+ part", "No"],
              ["Gator EFX GC24019", "2015–2020", "No"],
              ["TruXedo Lo Pro 597701", "2015–2026", "Yes"],
              ["Tyger T3", "5.5 ft TG-BC3F1041: 2015–2020. 6.5 ft TG-BC3F1042: 2015–2026", "Only the 6.5 ft part is listed for it"],
              ["Putco Venture TEC 184100", "2015–2027", "Yes"],
              ["RealTruck GoRack 9250101", "2015–2024 on the Amazon listing", "Yes, to the years listed"],
              ["Rough Country 10406", "2015–2026 per Rough Country; the Amazon title reads 2015–2023", "Yes; confirm later years"],
              ["Putco Quick Rack, 6'7\" bed", "2015–2020; 2021–2025 versions are separate", "No"],
              ["Yakima HD towers", "Not tied to one truck", "Yes, with the right kit"],
             ]}},
  {"h": "Choose the cover and the rack together, then install in this order",
   "body": "The bed rack is last on the buying list and first on the deciding list, because it can rule out the "
           "tonneau cover you were about to buy. The pairings our guides could document:\n\n"
           "- **Roll-up under a full rack:** Putco says the Venture TEC works with most inside-rail roll-up covers. "
           "Ask whether yours is one.\n"
           "- **Roll-up under the Quick Rack:** RealTruck says it works with roll-ups such as the BAK Revolver and "
           "Extang Revolution but has to come off to operate hard folders such as the BAKFlip and Gator FX.\n"
           "- **T-slot cover:** Retrax sells the PRO in an XR version, T-80373, with T-slot rails, and RealTruck "
           "says the GoRack suits covers with a T-slot rail system.\n"
           "- **Hard tri-fold:** Rough Country says its low-profile cover, about $700, can be used with bed racks "
           "but not with OEM cargo systems.\n"
           "- **Clamp towers:** Yakima says select covers need its Tonneau Kit 1.\n\n"
           "Anchors matter as much as the pairing. The Putco racks and the GoRack bolt into the stake pockets "
           "without drilling. Our bed rack guide cites a 13th-gen owner on F150Forum who calls BoxLink, Ford's "
           "cleat system, mostly useless for anything but tie-downs. Our vehicle data lists a bed utility track as "
           "optional. If you have it, RealTruck says the GoRack can mount to a utility rail and Yakima says tracked "
           "beds need its Track Kit 1 or 2. Rough Country's 10406 installs with nutserts, so read its instructions "
           "to see whether your bed needs holes.\n\n"
           "Install in this order. Floor liners go in first, with the factory carpet mats out. The cover goes on "
           "next, with BoxLink cleats and rail caps cleared from the clamp points. The rack goes on last, torqued "
           "to the maker's figures, because an over-tightened clamp can mark or deform the aluminum rail."},
  {"h": "A truck out of production: used parts, warranties and payload",
   "body": "**Used parts.** Our tonneau guide's rule is to read the part number off the frame label and check it "
           "against the maker's fitment before paying. For a rack, confirm the bed length it was built for.\n\n"
           "**Warranties.** Our tonneau guide notes that none of its covers' warranties transfers to the next "
           "owner: 2 years on the Gator EFX, 5 years on the BAKFlip MX4, Tyger T3 and Rough Country cover, and "
           "limited lifetime on the RetraxPRO MX and TruXedo Lo Pro. A used cover has none. Putco, RealTruck and "
           "Yakima describe limited lifetime warranties on their racks; we did not confirm whether those transfer, "
           "so ask.\n\n"
           "**Spend against the truck.** Our tonneau guide's view is that the RetraxPRO MX, about $2,150, pays off "
           "only if you open the bed many times a day. Parts listed across both generations keep their use if you "
           "trade up: the Husky sets, the Lo Pro, the Venture TEC and Yakima's towers.\n\n"
           "**Payload.** Motor Authority reported a maximum payload of 3,270 lb for the 2018 truck with the 5.0L "
           "V8. That is a best case. Your figure is on the door-jamb label, and passengers, tongue weight, rack, "
           "tent and cover all count against it. Yakima lists the OverHaul HD towers at 59.52 lb before crossbars, and Tyger lists the T3 at 33.2 lb. Load a rack to its moving "
           "figure: 600 lb dynamic on the Venture TEC and GoRack, 400 lb on the Rough Country 10406 and 500 lb "
           "on-road on Yakima's towers. RealTruck gives the Quick Rack a single 1,000 lb figure, so confirm a "
           "moving rating with Putco before a tent goes on it."},
 ],
 "avoid": [
  {"h": "Trusting a year range without the part number", "body": "BAK, Retrax and Gator sell different hard covers for 2015–2020 and 2021+, while some liners, soft covers and racks span both. Match the number to your model year."},
  {"h": "Ordering by cab name", "body": "A SuperCrew can have the 5.5 or 6.5 ft box and a SuperCab the 6.5 or 8 ft. Covers and one-piece racks go by bed length, so measure at the rail."},
  {"h": "A hard folding cover first, a rack later", "body": "A standard folding cover leaves no place to mount most racks, and Putco's Quick Rack has to come off to open a BAKFlip or Gator FX."},
  {"h": "A used cover with no frame label", "body": "Without the part number you can't check the bed length or the generation, and the maker's warranty did not transfer to you."},
 ],
 "verdict": {
  "thesis": "On the 2015–2020 F-150, buy floor liners matched to cab and rear floor first and a tonneau cover matched to rail length and the 2015–2020 part number second, and buy a bed rack only after choosing the cover around it.",
  "body": "The 13th-generation F-150 is an easy truck to accessorize once five facts are written down: cab, front "
          "seat layout, what sits under the rear seat, bed length at the rail and model year. Floor liners need the "
          "first three and cost the least, so they go first. The tonneau cover needs the last two, and it is where this "
          "generation's biggest trap sits: a hard cover for the 2021 truck has a different part number even though the bed lengths read the "
          "same.\n\n"
          "The bed rack sits last because few owners need one, but the rack decision has to be made before the "
          "cover is paid for, and on the aluminum bed the stake pockets and the maker's torque figures do the work. "
          "Skip the trailer hitch shopping until you have looked under the bumper, and check for factory running "
          "boards before pricing a set. Owners of a 2021–2026 F-150 should treat this page as a list of questions, "
          "not part numbers, since the hard cover catalogs split at 2021. Each linked guide covers its category's "
          "fit details.",
 },
 "sources": [
  ["Ford F-Series, thirteenth generation: model years, cabs, beds, Raptor, 2018 refresh (Wikipedia)", "https://en.wikipedia.org/wiki/Ford_F-Series_(thirteenth_generation)"],
  ["Ford F-Series, fourteenth generation: what the 2021 redesign carried over (Wikipedia)", "https://en.wikipedia.org/wiki/Ford_F-Series_(fourteenth_generation)"],
  ["2020 Ford RV and Trailer Towing Guide: F-150 hitch receiver, tow packages, bumper towing (Ford of Canada, PDF)", "https://www.ford.ca/cmslibs/content/dam/brand_ford/en_ca/brand/resources/towing-guides/2020%20Ford%20RV&TTGuide%20EN%20AODA.pdf"],
  ["2018 Ford F-150 towing and payload figures (Motor Authority)", "https://www.motorauthority.com/news/1112031_2018-ford-f-150-boasts-best-in-class-towing-rating-improved-fuel-economy"],
  ["Husky Liners: WeatherBeater vs X-act Contour (Husky Liners)", "https://huskyliners.com/blog/husky-liners-weatherbeater-vs-xact-contour/"],
  ["BAKFlip MX4 448329 (RealTruck)", "https://realtruck.com/p/bakflip-mx4-tonneau-cover/bak-448329/"],
  ["RetraxPRO MX 80373 (RealTruck)", "https://realtruck.com/p/retraxpro-mx-tonneau-cover/rtx-80373/"],
  ["Gator EFX GC24019 (RealTruck)", "https://realtruck.com/p/gator-efx-hard-fold-tonneau-cover/guc-gc24019/"],
  ["TruXedo Lo Pro 597701 (RealTruck)", "https://realtruck.com/p/truxedo-lo-pro-tonneau-cover/trx-597701/"],
  ["Tyger T3 TG-BC3F1041 (Tyger Auto)", "https://www.tygerauto.com/tonneau-cover/tyger-t3-soft-trifold/tg-bc3f1041/tyger-t3-soft-tri-fold-fit-2015-2020-ford-f-150-55-bed.html"],
  ["Putco Venture TEC Rack 184100, F-150 5'7\" bed (Putco)", "https://www.putco.com/product/venture-tec-rack/184100/"],
  ["Putco Venture TEC Quick Rack (RealTruck)", "https://realtruck.com/p/putco-venture-tec-quick-rack/"],
  ["RealTruck GoRack (RealTruck)", "https://realtruck.com/p/realtruck-gorack/"],
  ["Rough Country Bed Rack 10406 (Rough Country)", "https://www.roughcountry.com/product/configurable/ford-bed-rack-10406"],
  ["Yakima OverHaul HD towers (Yakima)", "https://yakima.com/products/overhaul-hd"],
 ],
}
