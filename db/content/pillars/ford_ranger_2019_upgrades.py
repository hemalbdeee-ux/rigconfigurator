"""Upgrades pillar: 2019–2023 Ford Ranger (4th gen, T6, US market). Ended generation, so every truck is a used truck.
Hub page: ranks the three published Ranger category guides and links to them. No product picks or ASINs here
(the site pulls each guide's #1 pick). Every price comes from the linked guides' picks[].price fields or price text in
those guides (the RetraxPRO XR band is the guide's product-list band and is worded "confirm on the listing").
Vehicle facts come from db/migrations/003_vehicles.sql (61 in SuperCrew bed, SuperCab 6 ft noted at 72 in, Class IV
hitch, 2 in receiver, 7,500 lb with the factory tow package, "Class IV factory hitch on most trims", Tremor 2021+;
2024-present row: 2019–2023 tonneau fitments do not carry over), from the three guides and their sources, and from
three pages opened on 2026-10-04: Wikipedia's Ford Ranger (T6) page (North American cabs are a four-door SuperCab and
a four-door SuperCrew; one powertrain, 2.3 L EcoBoost with a 10-speed automatic), Ford's October 2018 announcement
as republished by ForConstructionPros (1,860 lb maximum payload; 7,500 lb
"when equipped with the tow package and a trailer brake controller") and MotorWeek's report of Ford's 2024 Ranger
launch (SuperCrew with a 5 ft bed only). Wikipedia's Ford Ranger (Americas) page was also read; it added nothing
that is used here, so it is not cited.
Not verified, and worded as such in the text: which trims and model years left the factory with the receiver (the
"most trims" wording is our vehicle data only); which cab and drivetrain carry the 1,860 lb and 7,500 lb figures, and
whether they held for 2020–2023; ZROADZ Z835201 fit on 2022–2023 trucks (the Amazon title stops at 2021); whether the
TruXedo Lo Pro is one of the "select covers" for Yakima's Tonneau Kit 1, and Putco's approval of the Lo Pro by name
(Putco names the cover type, not the model); prices of the 6 ft cover versions and of the JOYTUTUS and OBNAUX
listings; warranty transfer for brands other than BAK and Retrax; which cabs the Tremor package was sold on
(the page does not say). The 2024 facts were read on a press outlet's page, not on Ford's own site. No running board
or hitch listing was checked for this generation, so none is named.
"""

KIND = "upgrades"
KEY = ("ford", "ranger", "2019-2023")
CATEGORIES = ["floor-mats", "tonneau-covers", "bed-racks"]

TITLE = "2019–2023 Ford Ranger Upgrades, Ranked: 3 Mods in Order, With Cab-Bed and 2024 Listing Traps"
META = ("Three 2019–2023 Ranger upgrades in buying order: floor liners, tonneau cover and bed rack, with SuperCrew "
        "and SuperCab beds, 2024 listing traps and price bands.")

FAQ = [
 ("What should I upgrade first on a 2019–2023 Ford Ranger?",
  "Floor liners, then a tonneau cover, then a bed rack if you need one. Liners cost the least, about $80–$120 for "
  "OMAC's SuperCrew set in our guide, and need one fact: SuperCrew or SuperCab. The cover comes second because the "
  "bed is small and often the only lockable storage. It needs the bed length, which follows the cab, and a "
  "2019–2023 part number. Decide on the rack before paying for the cover, since most folding covers leave nowhere "
  "to mount one. OMAC liners and Tyger's T3 soft cover at about $223 come to about $303–$343."),
 ("Do 2019–2023 Ranger accessories fit the 2024 and newer Ranger?",
  "Don't count on it. The 2024 truck has a new cab and a different bed, about 59.6 in long and 48.2 in between the "
  "wheel wells, against about 61 in and 44.8 in on the older SuperCrew bed. BAK, Retrax, TruXedo and Tyger sell "
  "separate 2024+ covers, and Husky sells separate 2024+ liners. A few listings span both. Husky's 13411 "
  "front pair reads 2019–2024, Putco's Venture TEC reads 2019–2025, and one Gator EFX title reads 2019–2025 while "
  "RealTruck lists that part for 2019–2023 only. Get the maker to confirm before carrying a part over."),
 ("I have a Ranger SuperCab. What changes on this list?",
  "All three purchases. Every budget liner set in our guide is cut for the SuperCrew, so the SuperCab answer is "
  "Husky's 93801 three-piece set at about $150–$210, or the 13411 front pair with Husky's 14421 rear piece. For the "
  "cover, order 6 ft parts. Our guide names the RetraxPRO MX 80336, TruXedo Lo Pro 531101, Gator EFX GC24023 and "
  "UnderCover SE UC2196. For the rack, Putco's listing is for the 5'1\" bed, so Yakima's clamp towers are the "
  "easier route. Confirm 6 ft prices on the listings."),
 ("Can I run a tonneau cover and a bed rack together on a 2019–2023 Ranger?",
  "Yes, if you choose them as a pair. Putco says its Venture TEC works with roll-up covers that mount inside the bed "
  "rails, which points to a roll-up such as the TruXedo Lo Pro at about $540; confirm it with Putco. Yakima says select covers need its "
  "Tonneau Kit 1 under the OutPost HD and OverHaul HD towers. Retrax sells the RetraxPRO XR, part T-80335, with "
  "T-slot rails for crossbars over the cover. Ranger5G owners note that a rolled cover takes about 5–6 in, so the "
  "bars must sit higher. Most folding covers leave no place for a rack."),
 ("Do I need to buy a trailer hitch for a 2019–2023 Ranger?",
  "Maybe not. Look under the rear bumper first. Our vehicle data lists a Class IV factory hitch with a 2 in receiver "
  "on most trims and a maximum of 7,500 lb with the factory tow package. Ford's 2018 announcement gives the same "
  "7,500 lb for trucks equipped with the tow package and a trailer brake controller. We could not confirm which "
  "trims and model years had the receiver as standard, so we print no trim list. If your truck has a receiver, an "
  "aftermarket trailer hitch adds nothing."),
 ("How much payload do a bed rack and rooftop tent use on a Ranger?",
  "Ford announced the 2019 Ranger with a maximum payload of 1,860 lb, a best-case figure. Yours is on the door-jamb "
  "label. The rack comes out of it first. ZROADZ lists the Z835201 at 125 lb, and Yakima lists the OverHaul HD "
  "towers at 59.52 lb and the OutPost HD towers at 44.09 lb before crossbars. Then add the tent, gear, passengers "
  "and any cover. Keep tent and gear under the rack's on-road rating: 500 lb for Yakima's towers, 600 lb for "
  "the Putco and 800 lb for the ZROADZ."),
 ("How much does it cost to add all three upgrades to a 2019–2023 Ranger?",
  "From the prices on our guides' picks, a budget build without a rack runs about $303–$343: OMAC liners and Tyger's "
  "T3 soft cover. A mid build runs about $1,449–$1,489 before crossbars and Yakima's tonneau kit, with a 3W or "
  "LASFIT liner set, the TruXedo Lo Pro and Yakima's OutPost HD towers. A premium SuperCrew build starts at about "
  "$3,089–$3,159 with Husky's front and rear pieces, the Lo Pro and Putco's Venture TEC. Owners who skip the rack "
  "can buy a hard cover instead: Husky liners plus the RetraxPRO MX come to about $2,100–$2,170."),
 ("Does a Ranger Tremor or FX4 need different parts?",
  "Mostly no. Our floor liner guide says the Tremor package, which it dates to 2021–2023, and the FX4 package change "
  "suspension, tires and trim, not the cab floor. Our tonneau guide says covers are listed by model year and bed "
  "length, not by trim, and that none of the makers it checked names the Tremor. If the truck has extra bed "
  "accessories such as tie-down rails or a divider, confirm the clamps clear them. The fit line for ZROADZ's "
  "Z835201 rack names XL, XLT and Lariat trucks with the standard bed, so ask ZROADZ about any package it doesn't "
  "mention."),
 ("My used Ranger came with a tonneau cover. Should I keep it, and is the warranty still good?",
  "Keep it if it matches the bed, seals at the tailgate and suits how you load the truck, but don't assume the "
  "warranty came with it. Our tonneau guide notes that BAK's 5-year warranty on the BAKFlip MX4 runs from the "
  "original purchase date and is not transferable, and that Retrax's limited lifetime warranty covers the original "
  "buyer. For other brands, ask the maker. Then close the tailgate and check the rear seal along its whole width, "
  "including the ends. Ranger5G owners cited in our guide report water getting in at the tailgate corners."),
]

ARTICLE = {
 "dek": "Three upgrades for the 2019–2023 Ranger, in the order most owners should buy them. This generation has ended, "
        "so every one of these trucks is a used truck. The order is shaped by two cabs that each come with one bed, "
        "and by listings that stretch across the 2019–2023 truck and the redesigned 2024 one.",
 "author": "jake-morrison",
 "reviewed": "2026-10-04",
 "method": "We did not install any of these parts ourselves. The order comes from our three fit-checked 2019–2023 "
           "Ranger guides, weighing how many trucks each upgrade suits, what it costs, how often it is used and how "
           "much of its fit is confirmed for this generation (cab, bed length, model year). Price bands are the "
           "prices listed on those guides' picks, checked at maker and retailer stores in September 2026, and are "
           "approximate. Vehicle facts come from our vehicle data, the guides' sources, Wikipedia's Ranger page, "
           "Ford's 2018 announcement of the 2019 truck and MotorWeek's report of the 2024 launch. Where we could "
           "not confirm a factory detail, the text says so.",
 "takeaways": [
  "**Count the doors first.** SuperCrew, with four full doors, has the 5 ft bed (61 in). SuperCab has the 6 ft bed (72.7 in).",
  "**Treat 2024 as a different truck.** Its bed is about 59.6 in long and wider between the wheel wells, and makers sell separate 2024+ parts.",
  "**Read the part number, not only the year range.** Titles on Husky, Gator, Putco and budget rack listings run to 2024 or 2025.",
  "**Choose the rack before the cover.** Putco names inside-rail roll-up covers for its rack, and most folding covers leave nowhere to mount one.",
  "**Look under the bumper before hitch shopping.** Our data lists a Class IV hitch on most trims, which we could not confirm trim by trim.",
 ],
 "priority": [
  {"category": "floor-mats",
   "h": "1. Floor liners first: one question about the cab, and the lowest price on the page",
   "why": "Floor liners lead because they cost the least, they protect the cab floor of a used truck "
          "and they have the shortest fit rule. The cab did not change from 2019 to 2023, and every US "
          "truck has the 10-speed automatic, so there is no clutch-pedal version to match. The "
          "SuperCrew has four full-size doors and a rear bench. The SuperCab has small rear-hinged doors and a short "
          "rear area with jump seats. The front footwells are shared, which is why Husky lists its WeatherBeater "
          "13411 front pair for both cabs. The rear floors are not: Husky's 14411 rear is SuperCrew only, its 93801 "
          "three-piece set is SuperCab only, and every budget TPE set in our guide is SuperCrew only. Prices in our "
          "guide run about $80–$120 for OMAC's full set, about $110–$150 for 3W's or LASFIT's, about $150–$220 for "
          "Husky front plus rear and about $150–$210 for the SuperCab set. The trade-off is price against written "
          "terms: Husky states a lifetime warranty against cracks and breaks, and the budget brands publish little.",
   "skip_if": "The truck came with fitted liners in good shape that hook onto the driver-side retention posts."},
  {"category": "tonneau-covers",
   "h": "2. Tonneau cover second: buy by cab and bed, then by a 2019–2023 part number",
   "why": "A tonneau cover ranks second because a mid-size bed is small and, on a truck parked in town, often the "
          "only lockable storage. Two checks decide fit. The first is bed length, which follows the cab. Makers "
          "list the SuperCrew bed as 5'1\" or 61 in and the SuperCab bed as 6'1\" or 72.7 in. "
          "The second is generation. The 2024 truck's bed is about 59.6 in long and "
          "wider between the wheel wells, and BAK, Retrax, TruXedo and Tyger sell separate 2024+ parts. Prices in "
          "our guide are about $223 for Tyger's T3 soft tri-fold, about $540 for the TruXedo Lo Pro roll-up, about "
          "$549 for the Gator EFX hard tri-fold, about $1,100 for the BAKFlip MX4, about $1,300 for the one-piece "
          "UnderCover SE and about $1,950 for the RetraxPRO MX. The rated hard covers carry 300 to 500 lb spread "
          "flat. The trade-off on this truck is water: our "
          "guide cites Ranger5G owners who describe leaks at the tailgate corners with folding covers. If a rack is "
          "likely, read slot three before paying.",
   "skip_if": "You haul tall loads most days, or you plan a rack and haven't yet picked a cover that works with it."},
  {"category": "bed-racks",
   "h": "3. Bed rack last: decide it early, buy it when you need it",
   "why": "The bed rack comes last because the fewest owners need one, it costs the most and it uses the most "
          "payload. Most one-piece racks are 5 ft parts: Putco's Venture "
          "TEC listing reads 5'1\" bed, and ZROADZ lists its Access Overland Rack Z835201 for the standard bed. "
          "SuperCab owners are better served by Yakima's clamp towers, which fit by bed rail and not by bed length. "
          "The makers' ratings are 1,500 lb static, 800 lb on-road and 400 lb off-road for the ZROADZ, 1,000, 600 "
          "and 300 lb for the Putco, and 500 lb on-road and 300 lb off-road for Yakima's towers. Prices in our "
          "guide run about $799 for the OutPost HD towers and about $1,200 for the OverHaul HD towers, both before "
          "crossbars, about $1,871–$2,495 for the ZROADZ and from about $2,399 for the Putco. The JOYTUTUS and "
          "OBNAUX clamp racks are priced on their listings. The trade-off is weight, since "
          "ZROADZ lists its rack at 125 lb before any load. Its Amazon title also stops at 2021, so confirm a 2022 "
          "or 2023 truck. If you camp from the truck, move this slot up and choose the cover around the rack.",
   "skip_if": "Your loads fit under a cover and you don't carry boats, ladders or a tent."},
 ],
 "tier_table": {
  "caption": "Approximate price bands from the picks in our 2019–2023 Ranger guides (September 2026; Amazon prices move daily). Each column lists SuperCrew 5 ft parts that can be ordered together",
  "head": ["Upgrade", "Budget", "Mid", "Premium"],
  "rows": [
   ["Floor liners", "About $80–$120 (OMAC 3D TPE full set)", "About $110–$150 (3W or LASFIT full set)", "About $150–$220 (Husky WeatherBeater 13411 front plus 14411 rear)"],
   ["Tonneau cover", "About $223 (Tyger T3 soft tri-fold, TG-BC3F1066)", "About $540 (TruXedo Lo Pro roll-up, 531001)", "About $540 (TruXedo Lo Pro roll-up, the cover type Putco names for its rack)"],
   ["Bed rack", "None in this tier. The budget clamp racks in our guide don't state cover fit", "About $799 (Yakima OutPost HD towers; crossbars and Tonneau Kit 1 extra; confirm the cover in Yakima's fit lookup)", "From about $2,399 (Putco Venture TEC, 5'1\" bed, tent kit included)"],
   ["Total", "About $303–$343 (liners and cover)", "About $1,449–$1,489 before crossbars and tonneau kit", "From about $3,089–$3,159"],
  ],
 },
 "sections": [
  {"h": "Buying for a used Ranger: five checks at the truck before you order",
   "body": "Every 2019–2023 Ranger is now a used truck, and a used truck comes with someone else's choices. The fit "
           "rules in our guides turn into five checks you can do in the driveway.\n\n"
           "- **Cab.** Count the doors. Four full-size doors is a SuperCrew. Small rear-hinged doors is a SuperCab. "
           "Wikipedia describes both North American cabs as four-door, so read \"four-door\" in a classified ad "
           "with care.\n"
           "- **Bed.** Measure inside the bed at the rail from the bulkhead to the inside of the closed tailgate. "
           "Expect about 61 in or about 72.7 in.\n"
           "- **Bedliner.** Tyger says an over-rail bedliner needs small holes cut for the T3's clamps, while "
           "under-rail and spray-in liners need nothing. On a spray-in liner, a Ranger5G owner cited in our tonneau "
           "guide advised an adhesive prep so a hard cover's seals stick.\n"
           "- **Bed hardware.** Tie-down cleats, bed-divider brackets and the edge of an over-rail liner sit where "
           "cover clamps land. Take them out, or confirm clearance with the seller.\n"
           "- **Floor.** Lift out whatever mats came with the truck. A fitted driver liner hooks onto Ford's "
           "retention posts and clears both pedals at full travel. Never stack a new liner on an old mat.\n\n"
           "Then think about warranties. Our "
           "tonneau guide notes that BAK's 5-year warranty on the BAKFlip MX4 runs from the original purchase date "
           "and is not transferable, and that Retrax's limited lifetime warranty covers the original buyer. Price a "
           "cover that came with the truck as a part with no warranty unless the maker tells you otherwise."},
  {"h": "SuperCrew or SuperCab: each cab comes with one bed",
   "body": "On the US-market 2019–2023 Ranger the cab decides the bed, so one fact answers two questions. The "
           "SuperCrew has the 5 ft bed and the SuperCab has the 6 ft bed. Our vehicle data stores the SuperCrew bed "
           "as 61 in and notes the SuperCab bed at 72 in, rounded to whole inches. Cover makers print 61 in and "
           "72.7 in, sold as 5'1\" and 6'1\".\n\n"
           "The newer truck removes the choice. MotorWeek's report of Ford's launch says the 2024 Ranger comes only "
           "as a SuperCrew with a 5 ft bed. A SuperCab owner who trades up changes cab, bed and every bed part at "
           "once.",
   "table": {"caption": "2019–2023 Ranger cab and bed combinations, with the newer truck for comparison",
             "head": ["Cab / bed", "Floor liners", "Tonneau cover", "Bed rack"],
             "rows": [
              ["SuperCrew, 5 ft bed (listed as 5'1\" or 61 in)", "Husky 13411 front plus 14411 rear, or a 3W, LASFIT, OMAC or MAXPRO full set", "Most choice: BAKFlip MX4 448332, Gator EFX GC24022, RetraxPRO MX 80335, Lo Pro 531001, Tyger T3 TG-BC3F1066, UnderCover SE UC2186", "Every rack in our guide. Putco's and ZROADZ's are made for this bed"],
              ["SuperCab, 6 ft bed (listed as 6'1\" or 72.7 in)", "Husky 93801 full set, or 13411 front with the 14421 rear", "6 ft parts: RetraxPRO MX 80336, Lo Pro 531101, Gator EFX GC24023, UnderCover SE UC2196", "Yakima OutPost HD or OverHaul HD towers. Ask budget sellers whether the rack covers the 6 ft bed"],
              ["2024–2026 Ranger, SuperCrew, 5 ft bed (about 59.6 in)", "Separate Husky parts: 13791 front and 14791 rear", "Separate parts, such as BAKFlip MX4 448342, Lo Pro 531701 and Tyger T3 TG-BC3F1205", "A different bed. Confirm any rack listed for both generations"],
             ]}},
  {"h": "Year ranges that cross the line between 2023 and 2024",
   "body": "On the Ranger the year line that matters sits between 2023 and 2024. The 2024 truck has a new cab and a bed our guides list at about "
           "59.6 in long and 48.2 in between the wheel wells, against about 61 in and 44.8 in on the 2019–2023 "
           "SuperCrew bed. Our tonneau guide notes that a cover that is off by an inch won't seal at the tailgate.\n\n"
           "Branded cover makers answer the redesign with a new part number. Some liner and rack listings answer it "
           "with a longer title. On a 2019–2023 truck, a title that runs past 2023 is usually harmless. "
           "It matters when the title is the only evidence of fit, and "
           "when you trade up and expect the part to move with you.",
   "table": {"caption": "What the parts in our Ranger guides say about model years",
             "head": ["Part", "What the listing or maker says", "What to do"],
             "rows": [
              ["BAKFlip MX4", "448332 for 2019–2023; 448342 for 2024+", "Order 448332 for the 5 ft bed"],
              ["TruXedo Lo Pro", "531001 for 2019–2023; 531701 for 2024+", "Order 531001, or 531101 for the 6 ft bed"],
              ["Tyger T3", "TG-BC3F1066 for 2019–2023; TG-BC3F1205 for 2024+", "Order TG-BC3F1066; that part is 5 ft only"],
              ["Gator EFX GC24022", "RealTruck lists 2019–2023 and says it does not include 2024+; one Amazon title reads 2019–2025", "Fine on a 2019–2023 truck. Don't count on it for a 2024"],
              ["Husky WeatherBeater 13411 front pair", "Listed for 2019–2024, both cabs; Husky sells 13791 and 14791 for the 2024+ SuperCrew", "Fine on a 2019–2023 truck. Treat 2024 as that listing's claim"],
              ["LASFIT full set", "Title starts at 2020", "Ask the seller about a 2019"],
              ["ZROADZ Z835201", "Amazon title reads 2019–2021; ZROADZ's own page lists later years", "Confirm a 2022 or 2023 truck with the seller"],
              ["Putco Venture TEC", "Listing reads Ford Ranger 2019–2025, 5'1\" bed", "Fits the SuperCrew bed. Ask Putco before moving it to a 2024"],
              ["JOYTUTUS and OBNAUX clamp racks", "Listings span 2019–2025 and 2004–2025", "Confirm the rating and your bed with the seller"],
             ]}},
  {"h": "Choose the cover and the rack together, then count the payload",
   "body": "The bed rack is last on the buying list and first on the deciding list. Our tonneau guide says most "
           "folding covers leave nowhere to mount a rack, so the cover you were about to buy can rule out the rack "
           "you want later. The pairings our guides could document:\n\n"
           "- **Roll-up under a rack.** Putco says the Venture TEC works with roll-up covers that mount inside the "
           "bed rails. The TruXedo Lo Pro, about $540, is a roll-up with internal mounting. Putco names the cover "
           "type and not the model, so confirm the pairing before ordering. Ranger5G owners describe the same "
           "layout and note that a rolled cover takes about 5–6 in, so the bars need more clearance than that.\n"
           "- **Tower rack with a tonneau kit.** Yakima says select covers need its Tonneau Kit 1 under the OutPost "
           "HD and OverHaul HD towers. Its product pages don't name the Ranger, so run the truck and the cover "
           "through Yakima's fit lookup.\n"
           "- **Railed cover.** Retrax sells the RetraxPRO XR, part T-80335, for the 5'1\" bed with T-slot rails for "
           "crossbars and racks over the cover. Our product list bands it at about $2,000–$2,400. Confirm the price "
           "on the listing.\n"
           "- **Not stated.** Our bed rack guide says to check with ZROADZ about covers under the Z835201, and the "
           "JOYTUTUS and OBNAUX listings don't mention covers.\n\n"
           "Payload is the second limit. Ford's 2018 announcement of the 2019 truck gave a maximum payload of "
           "**1,860 lb**. That is a best-case figure, and we could not confirm which cab and drivetrain carry it, so "
           "use the number on your door-jamb label. Everything comes out of that one figure:\n\n"
           "- **The rack.** ZROADZ lists the Z835201 at 125 lb. Yakima lists the OverHaul HD towers at 59.52 lb and "
           "the OutPost HD towers at 44.09 lb, both before crossbars.\n"
           "- **The cover.** Tyger lists the soft T3 at 27.56 lb, and the one-piece UnderCover SE weighs about "
           "58 lb.\n"
           "- **The tent, gear and passengers,** plus tongue weight if a trailer is hooked up.\n\n"
           "Fit things in this order. Floor liners go in first. The cover goes on next, since our bed rack guide "
           "says to fit the cover before the rack. Then square the rack to the cab, tighten every clamp to the "
           "maker's torque and recheck the fasteners after the first drive."},
  {"h": "Towing and side steps: what the truck may already have",
   "body": "There is no trailer hitch guide and no running boards guide for the 2019–2023 Ranger on this site, so "
           "neither is ranked here. This is what the truck may already have.\n\n"
           "**The receiver.** Our vehicle data lists a **Class IV factory hitch with a 2 in receiver** on most "
           "trims. We could not confirm trim by trim, or year by year, which trucks left the factory with it. Ford's "
           "2018 announcement ties the top tow figure to a tow package, which suggests some trucks were built "
           "without one. Don't go by trim name. Look under the rear bumper. If a receiver is there, an aftermarket "
           "trailer hitch adds nothing.\n\n"
           "**The rating.** Our vehicle data lists a maximum of **7,500 lb with the factory tow package**. Ford's "
           "announcement words it as 7,500 lb when equipped with the tow package and a trailer brake controller. We "
           "read that figure for the 2019 model year only. Your figure is in the owner's manual, and a receiver "
           "never raises it.\n\n"
           "**Running boards.** We have not checked any running board listing for this generation, so we name none. "
           "If you shop for them, the listing should name your cab, because the SuperCrew has four full-size doors "
           "and the SuperCab has small rear-hinged ones. The year range should sit inside 2019–2023, or the seller "
           "should confirm the brackets for your year in writing."},
 ],
 "avoid": [
  {"h": "SuperCrew parts on a SuperCab", "body": "Rear liners, 5 ft covers and Putco's 5'1\" rack are SuperCrew parts. The SuperCab needs Husky's 93801 or 14421, a 6 ft cover and a rack that fits by bed rail."},
  {"h": "Trusting a year range that crosses 2024", "body": "Branded makers sell separate parts for the 2024 bed. A title that reads 2019–2025 or 2004–2025 deserves a question to the seller."},
  {"h": "Paying for a folding cover when a rack is planned", "body": "Our tonneau guide says most folding covers leave nowhere to mount a rack. Decide on the rack first, then buy an inside-rail roll-up, the RetraxPRO XR or a cover the rack maker confirms."},
  {"h": "Loading a rack without counting payload", "body": "ZROADZ lists its rack at 125 lb before a tent goes on, and the JOYTUTUS listing's 900 lb has no static and dynamic split. Add rack, tent, gear and passengers against the door-jamb payload."},
 ],
 "verdict": {
  "thesis": "On the 2019–2023 Ranger, buy floor liners matched to the cab first and a tonneau cover with a 2019–2023 part number for your bed second, and buy a bed rack only after choosing a cover that works with it.",
  "body": "The fourth-generation Ranger is an easy used truck to accessorize once three facts are written down: cab, "
          "bed length and model year. Floor liners need only the cab and cost the least, so they go first. The "
          "tonneau cover needs the bed, which follows the cab, and a part number from the right side of the 2024 "
          "redesign. Wikipedia lists one powertrain, a 2.3 L EcoBoost with a 10-speed automatic, and "
          "our guides found that the FX4 and Tremor packages don't change liner or cover fit.\n\n"
          "The bed rack sits last because few owners need one and a mid-size payload limits what it can carry, but "
          "the rack decision still has to be made before the cover is paid for. Skip the trailer hitch shopping "
          "until you have looked under the bumper, and ask any running boards seller the same cab and year "
          "questions. Owners of a 2024–2026 Ranger should not order from this page, since makers split their "
          "catalogs at 2024. Each linked guide covers the fit details for its category.",
 },
 "sources": [
  ["Ford Ranger (T6), North American model: cabs, powertrain, trims (Wikipedia)", "https://en.wikipedia.org/wiki/Ford_Ranger_(T6)"],
  ["2019 Ford Ranger payload and towing announcement, Ford Motor Company release (ForConstructionPros)", "https://www.forconstructionpros.com/equipment/trucks/pickup-trucks-vans/product/21026174/ford-motor-company-2019-ford-ranger-promises-classleading-payload-and-towing-capability"],
  ["2024 Ford Ranger launch: SuperCrew with 5 ft bed only (MotorWeek)", "https://motorweek.org/this_just_in/all-new-2024-ford-ranger-debuts-stateside-with-better-looks-more-power-and-first-ever-raptor"],
  ["2024 Ford Ranger bed dimensions (Sutton Ford)", "https://www.suttonford.com/ford-research/2024-ford-ranger-bed-size/"],
  ["BAKFlip MX4 448332 (RealTruck)", "https://realtruck.com/p/bakflip-mx4-tonneau-cover/bak-448332/"],
  ["RetraxPRO MX 80335 (RealTruck)", "https://realtruck.com/p/retraxpro-mx-tonneau-cover/rtx-80335/"],
  ["Gator EFX GC24022 (RealTruck)", "https://realtruck.com/p/gator-efx-hard-fold-tonneau-cover/guc-gc24022/"],
  ["TruXedo Lo Pro 531001 (RealTruck)", "https://realtruck.com/p/truxedo-lo-pro-tonneau-cover/trx-531001/"],
  ["Tyger T3 TG-BC3F1066 (Tyger Auto)", "https://www.tygerauto.com/tonneau-cover/tyger-t3-soft-trifold/tg-bc3f1066/tyger-t3-soft-tri-fold-fit-2019-2023-ford-ranger-5-bed.html"],
  ["ZROADZ Access Overland Rack Z835201 (ZROADZ)", "https://zroadz.com/i-23910365-2019-2023-ford-ranger-access-overland-rack-with-three-lifting-side-gates-part-z835201.html"],
  ["Putco Venture TEC Rack (RealTruck)", "https://realtruck.com/p/putco-venture-tec-rack/"],
  ["Yakima OutPost HD towers (Yakima)", "https://yakima.com/products/outpost-hd"],
  ["Yakima OverHaul HD towers (Yakima)", "https://yakima.com/products/overhaul-hd"],
  ["Show me your tonneau cover bed rack combo (Ranger5G)", "https://www.ranger5g.com/forum/threads/show-me-your-tonneau-cover-bed-rack-combo.15304/page-2"],
  ["Husky Liners: WeatherBeater vs X-act Contour (Husky Liners)", "https://huskyliners.com/blog/husky-liners-weatherbeater-vs-xact-contour/"],
 ],
}
