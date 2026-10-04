"""Upgrades pillar: 2023–2026 Toyota Sequoia (3rd gen, XK80; hybrid-only full-size three-row SUV, so there is no bed).
Hub page: ranks the three published Sequoia category guides and links to them. No product picks or ASINs here
(the site pulls each guide's #1 pick). Every price band comes from the linked guides' picks[].price fields or price
text in the cargo box guide (Yakima TimberLine FX crossbar kit, $599.90 at Rack Warehouse); vehicle facts from
db/migrations/003_vehicles.sql (SUV, raised-rails roof type, no stored roof load figure, hitch class 4 with a 2 in
receiver, three rows, i-FORCE MAX standard, TRD Pro and Capstone variants, "shares Tundra platform; different
roof/mats"), the three guides and their sources, and six pages opened for this page on 2026-10-04:
Wikipedia's Sequoia page (five trims at launch, 1794 Edition added for 2025, seven or eight seats with a split bench
or dual captain's chairs "depending on trims", towing 9,300–9,520 lb "depending on the trim level", i-FORCE MAX
standard, Trailhunter package for 2027) and five Toyota Newsroom releases:
- 25 January 2022 reveal of the 2023 Sequoia ("up to an impressive 9,000-pound maximum towing capacity, a nearly 22%
  increase over the prior generation"; Tow Tech Package "available on all grades but standard on TRD Pro and
  Capstone"; available power folding, extending tow mirrors and Load-Leveling Rear Height Control Air Suspension;
  Capstone "standard power running boards"; captain's chairs on Platinum and standard on TRD Pro; Sliding Third Row
  with 6 inches of adjustment and Adjustable Cargo Shelf System; frame "shares architecture with the all-new Tundra").
- 8 June 2022 launch release ("Maximum Towing Capacity of up to 9,520 lbs."; 437 hp and 583 lb-ft).
- 13 August 2024 release for 2025 (six grades; up to 9,520 lbs; Tow Tech standard on TRD Pro, Platinum, 1794 and
  Capstone; Limited "gives you the choice of a bench seat or captains chairs"; captain's chairs on Platinum, 1794 and
  TRD Pro; Capstone "standard power running boards").
- 22 July 2025 release for 2026 (up to 9,520 lbs; "Power folding 3rd row seats are now standard on all grades").
- 23 July 2026 release for 2027 (update of the current generation: new front-end design, rectangular fog lights in
  the bumper, upgraded grille light bar, 14-inch screen, Trailhunter package based on SR5; production in fall 2026).
The Toyota pages were read through a text extraction, so the page says "as we read". Three more Toyota pages were
tried and gave nothing usable: toyota.com/sequoia (no model year or specs in the extracted text), the newsroom's
2026 Sequoia vehicle page (only a link to a specifications PDF) and that PDF (403). None is cited.
Not verified, and worded as such in the text: Toyota's roof load figure (no owner's manual page was read; 132 lb is
Rave Offroad's figure for the TRD Pro rack and 165 lb is a budget crossbar listing's claim); which grades have
raised rails, flush rails or no rails (our data says raised, etrailer lists both, Toyota's releases say nothing);
whether every TRD Pro carries the factory roof rack; the rating and adjustment range of Toyota's PT767-0C660 bars;
factory running boards on any grade other than the Capstone, and whether all grades share rocker mounting points;
second-row layout on the SR5 and Capstone, and by model year; whether a center console is fitted with captain's
chairs on a given grade; whether every grade and year has a factory receiver, and its class (Class IV, 2 in is our
vehicle data only); which grade and drivetrain reaches which tow figure; whether the 2027 update changes floor,
rocker or roof fit; 2025–2026 fit of listings whose titles stop at 2024 or 2025; 2023 fit of Husky's 18571.
The pages cited only through the guides (etrailer, Rack Warehouse, Rave Offroad, Cars.com, ToyotaSequoia.net,
RealTruck, Husky, Smartliner) were not re-opened for this page; their facts are as recorded in the guides.
No Sequoia guide exists for roof racks or trailer hitches; neither is ranked.
Text fixes 2026-10-04 (after the guide corrections of the same day): rail wording now follows etrailer's 2023 page as
re-read (factory installed raised rails and flush mounted rails, no grades named) and no longer leans on our stored
roof type; Rack Warehouse's raised-rail page covers 2001-2025 without splitting generations; "aftermarket boards
replace factory ones" removed (unsourced) in favor of Go Rhino's fit list for its Sequoia RB30 drop-step kit
6964397320T (2023-2024 SR5, Limited, Platinum, TRD Pro; Capstone not listed), opened 2026-10-04.
"""

KIND = "upgrades"
KEY = ("toyota", "sequoia", "2023-present")
CATEGORIES = ["floor-mats", "running-boards", "cargo-boxes"]

TITLE = "2023–2026 Toyota Sequoia Upgrades, Ranked: 3 Mods in Order, With Seat-Layout and Tundra Fit Traps"
META = ("Three 2023–2026 Sequoia upgrades in buying order: floor liners, running boards and cargo box, with 7 vs 8 "
        "seats, Tundra mix-ups, factory steps and roof notes.")

FAQ = [
 ("What should I upgrade first on a 2023–2026 Toyota Sequoia?",
  "Start with floor liners, add running boards next and leave the cargo box for last. The three-row liner sets in "
  "the floor liner guide run about $100–$220, the lowest price of the three, and the only thing to settle is the "
  "second row: a bench, or captain's chairs with or without a center console. Running boards follow because the "
  "Sequoia sits high, but check under the doors before ordering, since Toyota lists power running boards as "
  "standard on the Capstone. The cargo box is the dearest of the three, it cannot go on until crossbars are fitted, "
  "and it takes a 75 in tall Sequoia past a standard 7 ft garage door."),
 ("Do Tundra parts fit the 2023+ Sequoia?",
  "Only one part in the three guides crosses over. Husky lists its WeatherBeater 18571 front pair for the 2022–2026 "
  "Tundra CrewMax and Double Cab and the 2024–2026 Sequoia, because the two share a front footwell. Everything "
  "behind the front seats is Sequoia-only, since the Tundra is a pickup. Running boards don't cross over either: "
  "the running board guide says the body length and doors differ, and Go Rhino sells separate Sequoia kits. "
  "Crossbars must name the 2023 or later Sequoia, because a pickup cab has no long roof with side rails."),
 ("How do I tell a seven-passenger Sequoia from an eight-passenger one, and which grades have captain's chairs?",
  "Count the second-row seats. Two separate seats are captain's chairs, the seven-passenger layout, with either an "
  "open walkway or a center console between them. One wide seat is the bench, the eight-passenger layout. As we "
  "read Toyota's 2025 release, captain's chairs are standard on the Platinum, 1794 Edition and TRD Pro, and the "
  "Limited offers a choice of bench or captain's chairs. The releases we read do not state the layout for the SR5 "
  "or the Capstone, so go by the seats, not the badge."),
 ("Does my Sequoia already have running boards or power steps from the factory?",
  "It may. Toyota's releases for the 2023 and 2025 model years list power running boards as standard on the "
  "Capstone. As we read them, they do not say what the other grades carry, and we could not confirm a list by grade "
  "and year, so check the rocker under the doors on your own Sequoia before you shop. A catalog fit list for a Go Rhino "
  "Sequoia RB30 drop-step kit names the 2023–2024 SR5, Limited, Platinum and TRD Pro but not the Capstone, so "
  "ask the seller before buying boards for a Sequoia that already has them."),
 ("Does the 2023–2026 Sequoia have raised or flush roof rails, and do I need crossbars for a cargo box?",
  "You need crossbars for any cargo box, and the rail type decides which ones. etrailer lists two roof types for "
  "the 2023 Sequoia: factory installed raised rails and flush mounted rails. It names no grades, and Toyota's "
  "releases do not describe the roof rails, so we could not confirm rails by grade. "
  "Slide your fingers under the rail between its end mounts. A gap means raised rails. No gap means flush rails and "
  "flush-rail feet. Toyota's accessory cross bars, part PT767-0C660, are sold for the 2023-on Sequoia's rails; "
  "ask a dealer to confirm they suit yours."),
 ("What is the roof weight limit on a 2023–2026 Sequoia?",
  "Toyota's figure is in the roof-load section of the owner's manual. No page we could open states it, and our "
  "vehicle data holds none, so read the manual before loading a box. Rave Offroad lists the TRD Pro factory roof "
  "rack at 132 lb evenly distributed, and a budget crossbar listing for the 2023–2026 Sequoia "
  "claims 165 lb, which is a seller's claim for the bars. Use the lowest of the manual, the crossbars and the box. "
  "Bars, box and cargo all count against it."),
 ("Will a Sequoia with a cargo box fit in a garage?",
  "No, if the door is a standard 7 ft one, which is 84 in. Cars.com lists the 2023 Sequoia at 75 in tall. The boxes "
  "in the cargo box guide add 11 in (INNO Wedge 660) to 19 in (SportRack Vista XL), so the lowest one puts the top "
  "at 86 in before the crossbars are counted. Measure the Sequoia with the bars fitted, add the box height, and "
  "take the box off between trips."),
 ("How much can the Sequoia tow, and do I need to buy a trailer hitch?",
  "Toyota's releases for the 2023, 2025 and 2026 model years give a maximum towing capacity of up to 9,520 lbs, and "
  "Wikipedia lists 9,300–9,520 lb depending on trim. Toyota's first announcement in January 2022 said up to 9,000 "
  "lb. All of these are ceilings; the figure for your build is in the owner's manual. For the hitch, our vehicle "
  "data lists Class IV with a 2 in receiver. The Toyota releases we read do not describe the receiver, so we could "
  "not confirm that every grade has one. Look under the rear bumper before shopping."),
 ("Do the TRD Pro and Capstone need different parts?",
  "For floor liners, the second-row layout matters, not the badge. Toyota lists captain's chairs as standard on the "
  "TRD Pro, so start with a seven-passenger set. For running boards, Toyota lists power running boards as standard "
  "on the Capstone, so most Capstone owners can skip that purchase. On a TRD Pro the running board guide suggests "
  "Go Rhino's RB30 Slim, about $430–$550, for clearance, or rock sliders for trail use. The roof differs most. Rave "
  "Offroad describes a TRD Pro factory roof rack rated at 132 lb evenly distributed, so a box's clamps and its "
  "loaded weight both need checking."),
 ("How much does it cost to add all three upgrades to a Sequoia?",
  "From the prices on the three guides' picks, a budget build runs about $700–$810: Auxko's TPE set, POFENZE boards "
  "and SportRack's Vista XL. A mid build runs about $1,169–$1,469 with HAFIDI's three-row liners, a Go Rhino RB30 "
  "or RB20 and a Yakima SkyBox 16 Carbonite or GrandTour 16. A premium build with Smartliner's three-row set, Go "
  "Rhino's RB20 drop-step kit and an INNO Wedge 660 or Thule Motion 3 XXL runs about $1,688–$2,220. All three "
  "totals are before crossbars. The one crossbar price in the cargo box guide is about $600 for Yakima's TimberLine "
  "FX raised-rail kit."),
]

ARTICLE = {
 "dek": "Three upgrades for the third-generation Sequoia, in the order most owners should buy them. Four things "
        "decide what fits: seven seats or eight, a 2023 or later listing that names the Sequoia and "
        "not the Tundra, the running boards the factory may already have fitted, and a 75 in tall body whose roof "
        "rails and roof load need checking before a cargo box goes on.",
 "author": "jake-morrison",
 "reviewed": "2026-10-04",
 "method": "We did not install any of these parts ourselves. The ranking is built from the three fit-checked 2023–2026 "
           "Sequoia guides on this site. For each upgrade we weighed how many Sequoias it suits, its cost, how often "
           "it gets used and how much of its fit is confirmed for this generation. Price bands are the prices on "
           "those guides' picks, checked at maker and retailer stores in September 2026, and are approximate. "
           "Vehicle facts come from our vehicle data, the guides' sources, Wikipedia's Sequoia page and five Toyota "
           "Newsroom releases covering the 2023, 2025, 2026 and 2027 model years. Factory details we "
           "could not confirm are marked as such.",
 "takeaways": [
  "**Seven seats or eight.** A bench, captain's chairs with a console and captain's chairs with a walkway each take a different floor liner.",
  "**A Sequoia is not a Tundra.** Husky's front liner pair is the only shared part; rear liners, running boards and crossbars must name the Sequoia.",
  "**Check for factory boards.** Toyota lists power running boards as standard on the Capstone. We could not confirm the other grades, so look under the doors.",
  "**Check the rails and the manual before a cargo box.** etrailer lists both raised and flush rails for the 2023 Sequoia, and we could not confirm Toyota's roof load figure.",
  "**Every one is a hybrid, and every one is tall.** No gas version to filter out, and a 75 in body puts any box past a 7 ft garage door.",
 ],
 "priority": [
  {"category": "floor-mats",
   "h": "1. Floor liners first: three rows of carpet, and one question about the second row",
   "why": "Floor liners take the top slot because no Sequoia is excluded and nothing else here costs as little. "
          "Powertrain is not a fit question. Every third-generation Sequoia is an i-FORCE MAX hybrid, so listings "
          "have no gas or hybrid split. The second row is the question. "
          "Eight-passenger Sequoias have a bench; seven-passenger ones have captain's chairs with a center console "
          "or an open walkway, and the second-row liner is cut for one of the three. Cartist's set is listed for "
          "seven seats without a console, Smartliner asks you to confirm seven or eight, and HAFIDI's and Auxko's "
          "titles state no layout. Listings must start at 2023 and name the Sequoia. Only Husky's 18571 front pair "
          "is shared with the Tundra, and its title covers 2024–2026 Sequoias, so confirm a 2023. Prices in the "
          "guide run about $100–$140 for Auxko's set, about $110–$150 for Cartist, about $120–$160 for HAFIDI and "
          "about $170–$220 for Smartliner's one-piece TPE set with a limited lifetime warranty. Husky's front pair "
          "is about $90–$130 and its 14281 third-row liner about $50–$80. The trade-off is documentation: the "
          "cheaper sets publish no warranty terms.",
   "skip_if": "Your Sequoia stays on dry pavement, the back rows are seldom used and the factory mats are holding up."},
  {"category": "running-boards",
   "h": "2. Running boards second: a tall step-in, unless the factory already fitted boards",
   "why": "Running boards take the middle slot. The Sequoia sits high, so a step helps on every trip, yet part of "
          "the fleet leaves the factory with boards already fitted. Toyota's releases list power running boards as "
          "standard on the Capstone, and a catalog fit list for a Go Rhino Sequoia kit names the SR5, Limited, Platinum and "
          "TRD Pro but not the Capstone, so check the rocker first. Two more facts decide fit. The part must name the Sequoia, since Tundra CrewMax boards don't suit the SUV's "
          "body and doors. And it must start at 2023, because the 2008–2022 body and rocker are different. Prices "
          "run about $150–$220 for POFENZE's carbon-steel boards, about $180–$260 for an OE-style two-piece set, "
          "about $430–$550 for Go Rhino's RB30 Slim, about $450–$600 for the RB30 or RB20, about $600–$750 for the "
          "RB20 with two pairs of drop steps and about $700–$1,000 for generic power steps that need wiring. "
          "RealTruck lists the RB30 as galvanized 16-gauge steel with a 7 in step and a 600 lb per side rating, the "
          "only published load figure in the group. Go Rhino's Amazon titles stop at 2024, so confirm 2025 and "
          "2026. Any fixed board costs side clearance, and drop steps hang lowest.",
   "skip_if": "Factory boards or the Capstone's power running boards are already under the doors and working, or your TRD Pro sees rocks, where sliders suit it better."},
  {"category": "cargo-boxes",
   "h": "3. Cargo box last: a long roof with room to spare, limited by rails, weight and height",
   "why": "The cargo box is the third purchase. It has the highest price here, it waits on crossbars, and once it is "
          "on, some garages are off limits. Roof space is not the problem. Cars.com lists the Sequoia at 208 in long, and the cargo box "
          "guide says even the 91.3 in Thule Motion 3 XXL sits ahead of the liftgate when mounted forward. Three "
          "things decide the purchase. First, crossbars. etrailer lists both raised and flush rails for the 2023 "
          "Sequoia, so look at the roof, then buy Toyota's PT767-0C660 bars or feet matched to the rail. Second, "
          "weight. We could not confirm Toyota's roof figure; the TRD Pro factory rack is listed at 132 lb evenly "
          "distributed, and bars, box and cargo all count. Third, height. At 75 in, the Sequoia stands 86 to 94 in "
          "tall with one of these boxes, before the bars. Prices run about $450 for SportRack's rear-opening Vista "
          "XL, about $599 on sale for Yakima's SkyBox 16 Carbonite, about $709 for the GrandTour 16, about $918 on "
          "sale for the 11 in tall INNO Wedge 660 and about $1,250 for the Motion 3 XXL, all before crossbars.",
   "skip_if": "Everything you carry fits inside with the third row folded, or the Sequoia is parked each night behind a 7 ft door."},
 ],
 "tier_table": {
  "caption": "Approximate price bands from the picks in the 2023–2026 Sequoia guides (September 2026; Amazon prices move daily)",
  "head": ["Upgrade", "Budget", "Mid", "Premium"],
  "rows": [
   ["Floor liners", "About $100–$140 (Auxko TPE full set; confirm rows and seating)", "About $120–$160 (HAFIDI TPE, first to third row)", "About $170–$220 (Smartliner one-piece TPE, three rows)"],
   ["Running boards", "About $150–$220 (POFENZE carbon-steel boards)", "About $450–$600 (Go Rhino RB30 or RB20)", "About $600–$750 (Go Rhino RB20 with two pairs of drop steps)"],
   ["Cargo box", "About $450 (SportRack Vista XL, rear opening)", "About $599 on sale (Yakima SkyBox 16 Carbonite) to $709 (Yakima GrandTour 16)", "About $918 on sale (INNO Wedge 660) to $1,250 (Thule Motion 3 XXL, box alone)"],
   ["Crossbars (needed under any box)", "Not in the total. Budget bars are priced on the listing", "Not in the total. Toyota's PT767-0C660 bars are priced on the listing", "Not in the total. Yakima TimberLine FX kit, about $600 at Rack Warehouse, for raised rails"],
   ["Total", "About $700–$810 before crossbars", "About $1,169–$1,469 before crossbars", "About $1,688–$2,220 before crossbars"],
  ],
 },
 "sections": [
  {"h": "Seven seats or eight: the second row, the console and the sliding third row",
   "body": "Floor liner fit starts with the second row. Wikipedia says the Sequoia seats seven or eight "
           "depending on trim, with a split bench or two captain's chairs in the second row. "
           "As we read Toyota's 2025 release, captain's chairs are standard on the Platinum, "
           "1794 Edition and TRD Pro, and the Limited gives a choice of bench or captain's chairs. The releases we "
           "read do not state the layout for the SR5 or the Capstone, and equipment can change by model year, so "
           "count the seats in your own vehicle. Then look between the captain's chairs for a center console or an "
           "open walkway.\n\n"
           "Toyota describes a Sliding Third Row with an Adjustable Cargo "
           "Shelf System: the row slides through 6 in of adjustment, and a removable shelf sets up the cargo area "
           "behind it. Toyota's 2026 release says power-folding third-row seats are standard on all grades that "
           "year. A third-row liner sits on the floor in front of the seat, so slide the row through its range "
           "after fitting. The guide ranks no cargo liner; if you buy one, confirm it suits your shelf setup.",
   "table": {"caption": "2023–2026 Sequoia seating layouts and what the floor liner guide lists for each",
             "head": ["Layout", "How to spot it", "Sets in the guide", "Watch for"],
             "rows": [
              ["Eight-passenger: bench", "One wide seat in row two", "Smartliner three-row (about $170–$220); the listing asks you to confirm seven or eight seats", "Cartist's set is not for the bench; HAFIDI and Auxko state no layout, so ask the seller"],
              ["Seven-passenger: captain's chairs, open walkway", "Two seats with floor between them", "Cartist three-row (about $110–$150), listed for 2023–2026", "The second-row piece should bridge the walkway"],
              ["Seven-passenger: captain's chairs with a center console", "Two seats with a console between them", "No listing in the guide names this layout", "Ask the seller for a photo of the second-row piece"],
              ["Third row, any layout", "The row slides 6 in (Toyota)", "Husky WeatherBeater 14281 (about $50–$80), listed for 2023–2026", "Slide the seat through its range after fitting"],
             ]}},
  {"h": "What the factory may already have fitted: power running boards, side rails and a TRD Pro rack",
   "body": "**Running boards.** Toyota's releases for the 2023 and 2025 model years describe the Capstone with "
           "standard power running boards. As we read them, they do not mention boards on the SR5, Limited, "
           "Platinum, 1794 Edition or TRD Pro, and we could not confirm a list by grade and year. So "
           "look under the doors. If boards are there and working, skip slot two. A catalog fit list for the Go Rhino "
           "Sequoia RB30 drop-step kit names the 2023–2024 SR5, Limited, Platinum and TRD Pro under one part "
           "number and does not list the Capstone. We could not confirm that every grade uses the same rocker "
           "mounting points, so ask the seller if your Sequoia left the factory with boards.\n\n"
           "**Side rails.** etrailer lists two roof types for the 2023 Sequoia, factory installed raised rails and "
           "flush mounted rails, and names no grades. The Toyota releases we read do not describe roof rails. "
           "Rack Warehouse sells raised-rail kits for the Sequoia on pages that cover 2001–2025 models without "
           "separating this generation. So check your own roof, as described in the next section.\n\n"
           "**The TRD Pro rack.** Rave Offroad describes the TRD Pro roof rack as a factory part that secures into "
           "the roof rails, 67.5 in long and about 48 to 51 in wide, with a 132 lb evenly distributed limit. We "
           "could not confirm from Toyota that every TRD Pro carries it. If yours does, a box's clamps have to wrap "
           "the rack's cross members, and box plus cargo has to stay under 132 lb. There is no roof rack guide for "
           "this Sequoia on this site yet, so racks are not ranked here."},
  {"h": "On the roof: rail type, crossbars, an unconfirmed load figure and a 75 in body",
   "body": "Of the three upgrades, only the cargo box depends on a second purchase.\n\n"
           "**Rail type.** Slide your fingers under the side rail between its end mounts. A gap means raised rails, "
           "which strap-style towers clamp around. A rail that sits tight to the roof is a flush rail and needs "
           "flush-rail feet listed for the Sequoia.\n\n"
           "**Crossbars.** The cargo box guide found three routes:\n\n"
           "- **Toyota's accessory bars**, part PT767-0C660, sold for the 2023-on Sequoia's rails. The guide cites "
           "an owner on ToyotaSequoia.net who runs a Thule box on them. It found no published load rating or "
           "adjustment range, so ask a dealer for both.\n"
           "- **Yakima's TimberLine FX kit** for raised rails, about $600 at Rack Warehouse.\n"
           "- **Budget bars** listed for the 2023–2026 Sequoia, priced on the listing. The 165 lb in the title is a "
           "seller's claim for the bars, not a roof limit.\n\n"
           "**Weight.** We could not confirm a Toyota roof figure, so the owner's manual is the authority. The only "
           "rack figure the guide found for this roof is the 132 lb on the TRD Pro factory rack. If your manual's "
           "figure were that low, a 47 lb SkyBox 16 would leave 85 lb for crossbars and gear together, and the 57.2 "
           "lb Motion 3 XXL about 75 lb.\n\n"
           "**Height.** Cars.com lists the 2023 Sequoia at 75 in tall. A standard 7 ft door is 84 in.",
   "table": {"caption": "Boxes in the cargo box guide on a 75 in tall Sequoia",
             "head": ["Box", "Volume", "Box weight", "Box height", "Top of box before bars", "Price in the guide"],
             "rows": [
              ["INNO Wedge 660", "11 cu ft", "42 lb", "11 in", "86 in", "About $918 on sale"],
              ["Yakima SkyBox 16 Carbonite", "16 cu ft", "47 lb", "15 in", "90 in", "About $599 on sale"],
              ["Rhino-Rack MasterFit 440L", "15.5 cu ft", "38.6 lb", "17 in", "92 in", "Priced on the listing"],
              ["Yakima GrandTour 16", "16 cu ft", "51.5 lb", "18 in", "93 in", "About $709"],
              ["Thule Motion 3 XXL", "21 cu ft", "57.2 lb", "18.1 in", "Just over 93 in", "About $1,250, box alone"],
              ["SportRack Vista XL", "18 cu ft", "Not published", "19 in", "94 in", "About $450"],
             ]}},
  {"h": "Towing: what the Sequoia has from the factory",
   "body": "There is no trailer hitch guide for the 2023+ Sequoia on this site, so hitches are not ranked.\n\n"
           "**The rating.** Toyota's launch release for the 2023 model and its 2025 and 2026 releases each give a "
           "maximum towing capacity of up to **9,520 lbs**. Toyota's first announcement, in January 2022, said up "
           "to 9,000 lb. Wikipedia lists 9,300–9,520 "
           "lb depending on trim. We could not open Toyota's specification sheet, so we can't say which grade and "
           "drivetrain reaches which figure. Your number is in the owner's manual.\n\n"
           "**The receiver.** Our vehicle data lists a **Class IV hitch with a 2 in receiver**. The Toyota releases "
           "we read do not describe the receiver, so we could not confirm it is fitted to every grade and year. "
           "Look under the rear bumper. If it is there, an aftermarket trailer hitch adds nothing, and a receiver "
           "never raises the rating.\n\n"
           "**The towing equipment Toyota does describe.** The Tow Tech Package adds Trailer Backup Guide and "
           "Straight Path Assist. Toyota's 2023 releases list it as standard on the TRD Pro and Capstone and "
           "available on other grades; the 2025 release adds the Platinum and 1794 Edition to the standard list. "
           "These are backing aids, not a hitch. Toyota also lists available power-folding, "
           "extending tow mirrors and an available load-leveling rear air suspension."},
  {"h": "Tundra, old Sequoia or new: where listings and model years go wrong",
   "body": "**Tundra parts.** Toyota says the Sequoia's frame shares its architecture with the Tundra, and sellers "
           "lean on that. The three guides found one shared part: Husky's 18571 front liner pair. Go Rhino sells "
           "Sequoia running board kits such as the RB20 69443973PC apart from its Tundra CrewMax kits.\n\n"
           "**2008–2022 Sequoia parts.** The 2023 model is a new generation, and the guides rule out older liners, "
           "boards and bars because the floor, body, rocker and roof changed. A cargo box is the one item that "
           "carries over, because it clamps to whatever crossbars are fitted.\n\n"
           "**Where listings stop.** In the guides, Cartist's liners, "
           "Husky's 14281, POFENZE's boards and the generic power steps run to 2026. Smartliner, HAFIDI, Auxko and "
           "the OE-style boards stop at 2025. Go Rhino's kits stop at 2024. Husky's 18571 starts at 2024 for the "
           "Sequoia. If a title stops short of your model year, ask the seller.\n\n"
           "**The 2027 model.** Toyota announced an updated 2027 Sequoia in July 2026. "
           "Toyota's release describes a new front-end design, rectangular fog lights set into the "
           "bumper, an upgraded grille light bar, a 14 in screen and a Trailhunter package based on the SR5. It "
           "reads as an update of this generation, and it does not mention the floor, rocker or roof. No listing in "
           "the guides names 2027, so wait for makers to publish 2027 fitment."},
 ],
 "avoid": [
  {"h": "Tundra or 2008–2022 Sequoia parts", "body": "Only Husky's 18571 front liner pair is shared with the Tundra. Rear liners, running boards and crossbars must name the 2023 or later Sequoia."},
  {"h": "A liner set that doesn't state the second row", "body": "A bench, a console and a walkway each need their own second-row piece. Ask before buying a set whose title names no layout."},
  {"h": "New boards for a Sequoia that already has them", "body": "Toyota lists power running boards as standard on the Capstone, so look under the doors first. On budget power steps, confirm the wiring kit and warranty first."},
  {"h": "A big box on a roof figure you haven't read", "body": "The TRD Pro factory rack is listed at 132 lb evenly distributed, and we could not confirm Toyota's figure for the roof. A 75 in Sequoia with any box in the guide stands 86 in or taller before the bars."},
 ],
 "verdict": {
  "thesis": "On the 2023–2026 Sequoia, buy floor liners matched to the second row first, add running boards only if none are already under the doors, and buy a cargo box last, after checking the rail type, the roof figure in the owner's manual and the garage door.",
  "body": "Five facts settle most of the fit questions on a third-generation Sequoia: bench or captain's chairs, console or walkway, model year, what the factory bolted under "
          "the doors and which rails are on the roof. Powertrain is not on that list, since every one is a hybrid. "
          "Floor liners depend on the first three and carry the lowest price, which puts them first. Running "
          "boards depend on the year, the Sequoia name on the listing and what is already bolted to the rocker.\n\n"
          "The cargo box waits until the end for two reasons. With crossbars added it is the largest bill on this "
          "page, and the roof sets its limits: rails that may be raised or flush, a load figure we could not "
          "confirm and a 75 in body. This site has no Sequoia guide yet for a roof rack or a trailer hitch, so "
          "neither is ranked, and a receiver may already be under the rear bumper. In every category, the listing "
          "to distrust is one written for the Tundra or for the 2008–2022 Sequoia. Each linked guide covers the "
          "fit details for its category.",
 },
 "sources": [
  ["Toyota Sequoia, third generation: trims, seating, towing, i-FORCE MAX, 2027 update (Wikipedia)", "https://en.wikipedia.org/wiki/Toyota_Sequoia"],
  ["Live Legendary with the All-New 2023 Sequoia: 9,520 lbs, Tow Tech Package, Capstone power running boards, sliding third row (Toyota Newsroom)", "https://pressroom.toyota.com/live-legendary-with-the-all-new-2023-sequoia-full-size-suv/"],
  ["Standing Tall: All-New 2023 Sequoia, January 2022 reveal: 9,000 lb, captain's chairs by grade, shared architecture with Tundra (Toyota Newsroom)", "https://pressroom.toyota.com/standing-tall-all-new-2023-sequoia-full-size-suv-is-ready-to-make-its-mark/"],
  ["2025 Sequoia Adds 1794 Grade and More: grades, second-row seating, Tow Tech Package (Toyota Newsroom)", "https://pressroom.toyota.com/2025-sequoia-adds-1794-grade-and-more/"],
  ["2026 Sequoia Elevates the Driving Experience: 9,520 lbs, power-folding third row (Toyota Newsroom)", "https://pressroom.toyota.com/2026-sequoia-elevates-the-driving-experience/"],
  ["Toyota Updates 2027 Sequoia: front-end design, grille light bar, Trailhunter package (Toyota Newsroom)", "https://pressroom.toyota.com/toyota-updates-2027-sequoia-with-elevated-style-advanced-technology-and-newly-available-trailhunter-package/"],
  ["2023 Toyota Sequoia roof types: raised and flush rails (etrailer)", "https://www.etrailer.com/roof-2023_toyota_sequoia.htm"],
  ["Yakima TimberLine FX raised-rail rack for Toyota Sequoia (Rack Warehouse)", "https://www.rackwarehouse.com/products/yakima-timberline-fx-complete-rack/vehicle/toyota/sequoia/"],
  ["TRD Pro factory roof rack for 2023+ Sequoia, 132 lb evenly distributed (Rave Offroad)", "https://raveoffroad.com/products/trd-pro-roof-rack-for-2023-sequoia"],
  ["2023 Toyota Sequoia specs, 75 in height and 208 in length (Cars.com)", "https://www.cars.com/research/toyota-sequoia-2023/specs/"],
  ["Owner thread: 2023 cross bars (ToyotaSequoia.net)", "https://www.toyotasequoia.net/threads/cross-bars.71/"],
  ["Owner thread: 2023 roof rack or cargo box (ToyotaSequoia.net)", "https://www.toyotasequoia.net/threads/2023-roof-rack-or-cargo-box.121/"],
  ["Go Rhino RB30 running boards (RealTruck)", "https://realtruck.com/p/go-rhino-rb30-running-boards/"],
  ["Go Rhino RB30 running boards with drop steps 6964397320T: 2023-2024 Sequoia fit list by grade (parts catalog page)", "https://gor.webshopmanager.com/i-30508347-rb30-running-boards-with-brackets-2-pairs-drop-steps-kit.html"],
  ["Husky Liners: WeatherBeater vs X-act Contour (Husky Liners)", "https://huskyliners.com/blog/husky-liners-weatherbeater-vs-xact-contour/"],
  ["SMARTLINER home page (SMARTLINER)", "https://www.smartliner-usa.com/"],
 ],
}
