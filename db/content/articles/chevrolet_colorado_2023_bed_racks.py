"""Long-form article — Best Bed Racks for 2023–2026 Chevrolet Colorado (3rd gen).
Mirrors ford_ranger_2024_bed_racks.py. No invented hands-on testing: specs come from Yakima, RealTruck and Putco pages
checked 2026-09-26. Bed dimensions, StowFlex tailgate, Trail Boss sport bar and towing notes match
chevrolet_colorado_2023_tonneau.py and db/migrations/003_vehicles.sql.
Few brand-name racks name the 2023+ Colorado in Amazon titles, so most picks are universal or multi-generation
listings marked "confirm".
"""

KEY = ("chevrolet", "colorado", "2023-present", "bed-racks")

TITLE = "Best Bed Racks for 2023–2026 Chevy Colorado: 6 Picks for the 5'2\" Bed, Trail Boss and ZR2"
META = ("Six bed racks for the 2023+ Colorado's 5'2\" bed, with load ratings, rack heights, tonneau pairings, "
        "and the sport bar and StowFlex tailgate notes that affect fit.")

FAQ = [
 ("What is the best bed rack for a 2023+ Chevy Colorado?",
  "For a rooftop tent, Yakima's OverHaul HD towers: 19–30 in adjustable height, 500 lb on-road and 300 lb off-road, with a limited lifetime warranty. They clamp to the bed rails rather than using a truck-specific frame, so confirm the Colorado in Yakima's fit lookup. The fixed 13 in OutPost HD has the same ratings for $799 and suits owners who want the load lower."),
 ("Do 2015–2022 Colorado bed racks fit the 2023 Colorado?",
  "Not automatically. The 2023 Colorado has a new bed: Chevrolet gives 61.7 in at the floor and 45.4 in between the wheelhouses, and the old long box is gone. Tonneau makers such as BAK split their Colorado parts at 2023. Putco's Venture TEC listing for the Colorado reads 2015–2022, for example. Treat \"2015–2025\" rack listings as a claim to confirm with the seller."),
 ("Can I use a bed rack on a Colorado Trail Boss or ZR2 with a sport bar?",
  "Check first. The factory sport bar sits at the front of the bed, where a headache rack or a rack's front uprights normally go. Rough Country says its hard tonneau covers don't fit Trail Boss models for this reason, and ColoradoFans owners discuss the same issue on Trail Boss, ZR2 and Z71 trucks. Clamp towers you can slide rearward, like Yakima's, are the easiest to work around it, but ask the maker."),
 ("Can I keep a tonneau cover under a Colorado bed rack?",
  "Yes, with the right pairing. Yakima's HD towers need Tonneau Kit 1 for select covers, and a railed cover such as the TruXedo Pro X15 TS or a RetraxPRO XR takes crossbars directly. BackRack sells separate tonneau hardware kits for its headache racks. Several budget racks say outright that they're not for trucks with bed covers, including the YZONA listing here."),
 ("How tall should a bed rack be on a Colorado?",
  "Match the rack to the load. The Thule Xsporter Pro Low stays below the cab for boats and bikes. Yakima's OutPost HD sits at 13 in, near the roofline on a midsize truck. The OverHaul HD adjusts from 19 to 30 in, and the Hooke Road listing here is 18.8 in. Taller racks leave room under a tent for gear but add drag and can hide the third brake light."),
 ("What load rating do I need for a rooftop tent?",
  "Look at the moving rating first. Yakima's HD towers are 500 lb on-road and 300 lb off-road, and the Thule Xsporter Pro Low is 220 lb, too little for a tent with people in it. Add the tent, bedding and gear and keep them under the on-road figure. Parked, the tent's own rating and the rack's static limit, where published, cover the people sleeping in it."),
 ("Does the StowFlex tailgate work with a bed rack?",
  "It should. Bed racks mount ahead of the tailgate, so the StowFlex compartment, the gate itself and Chevrolet's mid-position opening, rated at 500 lb, aren't touched by the rack. The things to check are rear uprights that stand at the very back of the bed and a long load hanging over the tailgate, which can stop the StowFlex lid from opening with the gate down."),
 ("Is the Colorado's payload enough for a rack and rooftop tent?",
  "Usually, if you add it up. The rack comes out of payload before anything goes on it: Yakima lists the OverHaul HD towers at 59.52 lb before crossbars. Then add the tent, gear and passengers, and check the payload on your door-jamb sticker. Payload differs by trim, including the ZR2 and ZR2 Bison, so use your own truck's sticker figure, not a brochure number."),
 ("Is a headache rack useful on a midsize truck?",
  "Yes, for work loads. A BackRack Original guards the rear window, carries lights and gives a front support for ladders. RealTruck lists the frame at $239.99 in 12-gauge steel, and the combo here pairs it with the standard-bed hardware for the 2023–2025 Colorado and Canyon. It won't carry a tent, and on trucks with a factory sport bar you need to confirm it fits."),
]

ARTICLE = {
 "dek": "Six racks for the 2023+ Colorado's single 5'2\" bed, from a budget rack with LED bars to Yakima's 19–30 in towers. For each one we list height, load ratings and mounting, plus what the Trail Boss and ZR2 sport bar, StowFlex tailgate and your tonneau cover mean for fit.",
 "author": "jake-morrison",
 "reviewed": "2026-09-26",
 "method": "We did not install these racks ourselves. We ranked them on published specs (load ratings, height, material, warranty), on fitment from the maker and Amazon listing title, and on what the 2023 bed changes. Few brand-name racks carry the 2023+ Colorado in their titles yet, so most picks are universal clamp systems or multi-generation listings marked to confirm. Prices were checked at Yakima and RealTruck in September 2026. Amazon prices move daily, so the button shows the live price.",
 "takeaways": [
  "**One bed, new dimensions.** Chevrolet lists 61.7 in at the floor and 45.4 in between the wheelhouses. Racks listed \"2015–2025\" need confirming.",
  "**Sport bars get in the way.** Trail Boss and ZR2 sport bars sit where front uprights and headache racks go.",
  "**Read the moving rating.** Yakima's HD towers are 500 lb on-road and 300 lb off-road; the Thule Xsporter Pro Low is 220 lb.",
  "**Covers and racks must be planned together.** Yakima needs Tonneau Kit 1; some budget racks say they're not for covered beds.",
  "**StowFlex keeps working.** Racks mount ahead of the tailgate.",
 ],
 "top_picks": [
  {"asin": "B07MDSP8T8", "role": "Best overall", "why": "19–30 in towers, 500 lb on-road, track and tonneau kits"},
  {"asin": "B07MRHDLS4", "role": "Best mid-height value", "why": "Fixed 13 in Yakima towers for $799"},
  {"asin": "B0CDK1Q3R7", "role": "Best headache rack", "why": "BackRack listed for 2023–2025 Colorado/Canyon, no drilling"},
  {"asin": "B09VFXD8CW", "role": "Best low profile", "why": "Thule rack below the cab for boats and bikes"},
  {"asin": "B0DDHFH5YW", "role": "Best budget", "why": "Clamp rack with two LED light bars, lists Colorado to 2025"},
 ],
 "fit_table": {
  "caption": "2023–2026 Colorado bed details that affect a rack",
  "head": ["Item", "Spec", "Applies to", "What it means for a rack"],
  "rows": [
   ["Cargo box", "61.7 in floor, 45.4 in between wheelhouses", "All 2023+ trims", "Differs from 2015–2022; confirm multi-gen listings."],
   ["Retail labels", "5'2\", 5'1\", 5'", "Same bed", "Trust the model year, not the inch label."],
   ["Sport bar", "Factory bar at the front of the bed", "Trail Boss, some ZR2/Z71", "Blocks headache racks and front uprights; confirm."],
   ["StowFlex tailgate", "Lockable compartment in the gate", "Standard on ZR2, optional elsewhere", "Unaffected by racks; keep long loads off the lid."],
   ["Towing", "Up to 7,700 lb", "With trailering package", "Rack weight counts against payload, not towing."],
  ],
 },
 "look_for": [
  {"h": "A listing that covers the 2023 bed",
   "body": "The third-generation Colorado got a new bed, and Chevrolet's brochure lists one cargo box for every trim: 61.7 in long at the floor, 45.4 in between the wheelhouses and 41.9 cu ft. The old truck's 6'2\" long box is gone. Accessory makers have split their parts at 2023, and Putco's Venture TEC listing for the Colorado still reads 2015–2022. Budget racks often list 2015–2025 on one part. That may fit, since many adjust in width, but the title alone doesn't prove it. For every multi-generation pick on this page, get the seller to confirm the 2023+ bed in writing."},
  {"h": "Sport bars on Trail Boss and ZR2",
   "body": "Trail Boss trucks, and some ZR2 and Z71 trucks, carry a factory sport bar at the front of the bed. It sits exactly where a headache rack mounts and where most overland racks put their front uprights. Rough Country says its hard tonneau covers don't fit Trail Boss models because of the bar, and ColoradoFans has a thread on the same problem. None of the rack pages we read mention it. Clamp towers that slide along the rail, such as Yakima's, can often be set behind it, but a fixed-frame rack or a BackRack may not fit at all. If your truck has a sport bar, ask the maker before buying."},
  {"h": "Load ratings on a midsize truck",
   "body": "Payload is tighter on a midsize truck, so the rack's moving rating and its own weight both matter. Yakima rates the OverHaul HD and OutPost HD at 500 lb on-road and 300 lb off-road, and lists the towers at 59.52 lb and 44.09 lb before crossbars. RealTruck gives the Thule Xsporter Pro Low 220 lb, fine for kayaks but not a tent with occupants. The budget racks quote single figures, or none, on the pages we could read. For a tent, favor a rack with published on-road and off-road numbers, and add rack, tent, gear and passengers against your door-jamb payload."},
  {"h": "Height against the cab",
   "body": "The Colorado's cab is low enough that a mid-height rack puts a tent near the roofline without much extra drag. Yakima's OutPost HD sits at 13 in, and the OverHaul HD adjusts from 19 to 30 in. The Hooke Road rack on this page is 18.8 in, and the Thule Xsporter Pro Low stays below the cab for boats and bikes. Taller racks leave room under a tent for a fridge and bins but catch more wind. At full height, check the view of the third brake light from behind the truck, because crossbars and a tent at cab height can hide it."},
  {"h": "Tonneau covers and the StowFlex tailgate",
   "body": "On a 5'2\" bed, most owners want the bed covered and a rack on top, so choose them together. A railed cover such as the TruXedo Pro X15 TS takes crossbars directly. Yakima's HD towers need Tonneau Kit 1 for select covers. BackRack sells separate tonneau hardware kits. Budget racks are the risk: the YZONA listing here says it's not for trucks with bed covers. At the back, the StowFlex tailgate is a lockable, drained compartment in the gate. Racks mount ahead of it, so it keeps working, as does the 500 lb mid-position tailgate opening. Just keep long loads off the StowFlex lid."},
 ],
 "look_table": {
  "head": ["Feature", "Look for", "Avoid"],
  "rows": [
   ["Fitment", "2023+ Colorado named, or a seller's written confirmation", "\"2015–2025\" with no mention of the new bed"],
   ["Sport bar", "Clamp towers that can sit behind it, or maker confirmation", "Front uprights that land on the bar"],
   ["Load rating", "Published on-road and off-road figures", "No rating on the listing"],
   ["Tonneau", "A tonneau kit or railed cover listed by the maker", "\"Not for trucks with bed cover\""],
   ["Height", "13–20 in for a tent on a midsize cab", "Full height that hides the third brake light"],
   ["Warranty", "Limited lifetime (Yakima)", "No warranty stated"],
  ],
 },
 "types_table": {
  "caption": "Bed rack styles on the 2023–2026 Colorado",
  "head": ["Type", "Example on this page", "Typical use", "Rooftop tent", "Tonneau", "Trade-off"],
  "rows": [
   ["Headache rack", "BackRack Original", "Window guard, lights", "No", "With tonneau kit", "Sport bar conflict"],
   ["Low profile", "Thule Xsporter Pro Low", "Kayaks, bikes", "No (220 lb)", "Check listing", "Little room underneath"],
   ["Fixed mid towers", "Yakima OutPost HD (13 in)", "Tent, bikes", "Yes (500 lb on-road)", "Tonneau Kit 1", "Crossbars extra"],
   ["Adjustable towers", "Yakima OverHaul HD (19–30 in)", "Changing loads", "Yes (500 lb on-road)", "Tonneau Kit 1", "Highest price here"],
   ["Budget overland", "YZONA, Hooke Road", "Lights, light gear", "Confirm rating", "Often not", "Thin specs"],
  ],
 },
 "picks": [
  {"asin": "B07MDSP8T8", "role": "Best overall", "price": "$1,200 (towers)",
   "pros": ["Height adjusts from 19 to 30 in", "500 lb on-road / 300 lb off-road", "BedGrip clamps can sit behind a sport bar", "Track Kit and Tonneau Kit adapters", "Limited lifetime warranty"],
   "cons": ["Towers only; HD Bar crossbars extra", "59.52 lb before crossbars", "Universal; confirm the Colorado in Yakima's lookup"],
   "body": "Few brand-name racks list the 2023 Colorado yet, which makes Yakima's clamp-on OverHaul HD the most dependable premium choice. Its four towers adjust from 19 to 30 in, so it can carry kayaks just above the rails or raise a rooftop tent high enough for bins and a fridge underneath. Yakima rates it at 500 lb on-road and 300 lb off-road, lists the towers at 59.52 lb and $1,200, and covers them with a limited lifetime warranty. BedGrip clamps, SKS locks and T-slots come standard, and you add HD Bar crossbars in 60, 68 or 78 in lengths.\n\nClamps also solve the sport bar problem better than a fixed frame, since you can position the front towers behind the bar, as long as the rail length allows the spacing Yakima specifies. The listing doesn't name the Colorado, so run your truck through Yakima's fit lookup. Tracked beds need Track Kit 1 or 2, and select tonneau covers need Tonneau Kit 1. On a 5'2\" bed, the 59.52 lb towers plus bars come straight out of payload, so do the math before adding a heavy tent.",
   "who": "Trail Boss and ZR2 owners who want a brand-name tent rack that adjusts and works around a sport bar.",
   "specs": [["Type", "Adjustable-height clamp towers"], ["Height", "19–30 in"], ["Load rating", "500 lb on-road / 300 lb off-road"], ["Weight", "59.52 lb (towers)"], ["Mounting", "BedGrip clamps; Track Kit 1/2 for tracked beds"], ["Tonneau", "Tonneau Kit 1 for select covers"], ["Crossbars", "HD Bar 60/68/78 in, sold separately"], ["Warranty", "Limited lifetime"], ["Price", "$1,200 towers (Yakima)"]]},
  {"asin": "B07MRHDLS4", "role": "Best mid-height value", "price": "$799 (towers)",
   "pros": ["Fixed 13 in height near the roofline", "500 lb on-road / 300 lb off-road", "44.09 lb towers, lighter than OverHaul", "Tonneau and track kits available", "Limited lifetime warranty"],
   "cons": ["Towers only; crossbars extra", "Height is fixed", "Universal; confirm Colorado fit"],
   "body": "The OutPost HD gives you Yakima's ratings without paying for adjustability. The four towers sit at a fixed 13 in, which on a midsize truck puts crossbars near the cab roofline, a good height for a tent that doesn't stick up into the wind. Yakima rates it at 500 lb on-road and 300 lb off-road, the same as the OverHaul HD, and lists the towers at 44.09 lb and $799 with a limited lifetime warranty. Add HD Bar crossbars in 60, 68 or 78 in lengths.\n\nThe lighter towers matter on a Colorado, where payload runs out sooner than on a full-size truck. Fit rules are the same as the OverHaul: Yakima's lookup for the truck, Track Kit 1 or 2 for tracked beds and Tonneau Kit 1 for select covers. Because the towers clamp anywhere along the rail, they can usually be set behind a factory sport bar, but check the spacing. If you later need more room underneath, the towers move to a different truck or can be swapped for the OverHaul.",
   "who": "Owners who want a low-drag Yakima platform for a tent or bikes at a lower price.",
   "specs": [["Type", "Fixed-height clamp towers"], ["Height", "13 in"], ["Load rating", "500 lb on-road / 300 lb off-road"], ["Weight", "44.09 lb (towers)"], ["Mounting", "Clamp; Track Kit 1/2 for tracked beds"], ["Tonneau", "Tonneau Kit 1 for select covers"], ["Warranty", "Limited lifetime"], ["Price", "$799 towers (Yakima)"]]},
  {"asin": "B0CDK1Q3R7", "role": "Best headache rack", "price": "From $239.99 (frame)",
   "pros": ["Listing names 2023–2025 Colorado/Canyon", "Frame and standard-bed hardware in one combo", "12-gauge steel, black powder coat", "No drilling on most trucks", "Guards the rear window; light mounts available"],
   "cons": ["Not a tent rack", "Sport bar trucks: confirm fit", "1-year workmanship warranty; finish not covered"],
   "body": "The BackRack Original is the one brand-name rack here whose Amazon listing names the new truck: frame 15002 with hardware kit 30226, listed for the 2023–2025 Chevrolet and GMC Colorado/Canyon standard bed. RealTruck lists the frame at $239.99 in 12-gauge steel with a semi-gloss black powder coat, and says it mounts without drilling on most trucks using vehicle-specific brackets and clamps. It guards the rear glass from shifting cargo, carries work lights, and gives ladders or lumber a front support.\n\nIt isn't a tent rack, and the front of the bed is where a Trail Boss or ZR2 sport bar lives, so owners of those trucks should confirm with the seller before ordering. Trucks with a tonneau cover need a different hardware kit, and RealTruck notes the low-profile kit requires drilling two holes per side. The warranty is one year on workmanship, and the powder coat isn't covered. Paired with a rear crossbar, it makes a simple ladder rack that leaves the bed open.",
   "who": "Work-truck owners without a sport bar who want window protection, lights and a ladder support.",
   "specs": [["Type", "Headache rack"], ["Fits", "2023–2025 Colorado/Canyon, standard bed (per listing)"], ["Part numbers", "15002 frame + 30226 hardware"], ["Material", "12-gauge steel, black powder coat"], ["Mounting", "No drill on most trucks"], ["Warranty", "1 year workmanship"], ["Price", "From $239.99 frame (RealTruck)"]]},
  {"asin": "B09VFXD8CW", "role": "Best low profile", "price": "$599.95",
   "pros": ["Stays below the cab for less wind", "Corrosion-resistant aluminum", "Thule One-Key locks", "No cutting or drilling, per listing", "Tools included"],
   "cons": ["220 lb capacity; not a tent rack", "Universal brackets; confirm Colorado fit", "Warranty wording on RealTruck is mixed"],
   "body": "If your loads are kayaks, bikes and lumber rather than a tent, the Thule Xsporter Pro Low keeps them below the cab, which cuts wind noise and keeps the truck's height down. RealTruck lists it at $599.95 with a 220 lb capacity. It's corrosion-resistant aluminum, includes Thule One-Key locks and ships with the tools for assembly. This Amazon listing is the compact-bed version and says no cutting or drilling is needed.\n\nThe 220 lb limit rules out a rooftop tent with people in it. The rack uses universal brackets that grip the bed rails, and neither the listing nor RealTruck's page names the Colorado, so run the 2023+ truck through Thule's fit guide before ordering and check that the brackets clear a sport bar. RealTruck's page mentions a limited lifetime warranty and, separately, a two-year defect term, so confirm the terms at purchase.",
   "who": "Owners who haul boats and bikes and want a clean, low rack instead of an overland frame.",
   "specs": [["Type", "Low-profile truck rack"], ["Bed size", "Compact bed (per listing)"], ["Material", "Aluminum"], ["Capacity", "220 lb"], ["Locks", "Thule One-Key"], ["Mounting", "Universal brackets, no drilling (per listing)"], ["Price", "$599.95 (RealTruck)"]]},
  {"asin": "B0DDHFH5YW", "role": "Best budget", "price": "Check listing",
   "pros": ["Two LED light bars included", "Rear crossbars for ladders and boards", "Clamp-on install", "Lists the Colorado and Canyon to 2025", "Lowest price band here"],
   "cons": ["Title spans 2015–2025; confirm the 2023 bed", "Listing says not for trucks with a bed cover", "No load rating on the pages we could read"],
   "body": "The YZONA rack is a light-duty clamp-on rack that comes with two LED light bars and rear crossbars, which covers lights and a ladder support in one box at a fraction of Yakima's price. Its Amazon title names the 2015–2025 Chevy Colorado and GMC Canyon, and it clamps to the bed rails rather than using stake pockets or drilling.\n\nThree caveats. The title covers two bed designs, so ask the seller to confirm the 2023+ bed. It says it is not for trucks with a bed cover, so it rules out a tonneau. And we couldn't find a static or dynamic rating on the pages we read, so treat it as a rack for light gear and lights until the seller gives you a figure that supports more. Light bars count as auxiliary lights, so check your state's rules before running them on the road.",
   "who": "Owners on a budget who want lights and a light-duty rack on an uncovered bed.",
   "specs": [["Type", "Clamp-on overland rack"], ["Fits", "2015–2025 Colorado/Canyon (per listing; confirm 2023+)"], ["Extras", "2 LED light bars, rear crossbars"], ["Tonneau", "Not for trucks with a bed cover (per listing)"], ["Load rating", "Not published on pages we read; confirm"], ["Price", "Check listing"]]},
  {"asin": "B0BPM78J1M", "role": "Budget full height", "price": "Check listing",
   "pros": ["18.8 in height for room under a tent", "Lists the Colorado and Canyon by name", "Clamp-on install", "Lower price than branded racks", "Sister 12.3 in low version sold"],
   "cons": ["No model years in the title; confirm 2023+", "Listing is for trucks without bed rails", "Load rating not confirmed on the pages we read"],
   "body": "Hooke Road's 18.8 in rack is a budget way to get tent height on a midsize truck. Its Amazon title names the Chevrolet Colorado and GMC Canyon along with the Ranger and Gladiator, and says it's for mid-size trucks without bed rails. At 18.8 in it sits in the same range as Yakima's OverHaul HD at its lowest setting, leaving room for a fridge or bins under a tent. Hooke Road also sells a 12.3 in low-profile version under a separate listing.\n\nThe title doesn't give model years, so confirm the 2023+ bed with the seller, and if your truck has accessory bed rails, the listing's \"without bed rails\" wording means you should ask before ordering. We didn't find a published static or dynamic rating on the pages we read, so get one from the seller before loading a tent. Check front upright placement against a sport bar as well.",
   "who": "Budget buyers who want tent height and will confirm the rating and 2023 fit first.",
   "specs": [["Type", "Full-height overland rack"], ["Height", "18.8 in"], ["Fits", "Colorado/Canyon, Ranger, Gladiator (per listing; confirm 2023+)"], ["Bed rails", "For trucks without bed rails (per listing)"], ["Load rating", "Not published on pages we read; confirm"], ["Price", "Check listing"]]},
 ],
 "install": [
  "Confirm the 2023+ bed (61.7 in floor, 45.4 in between wheelhouses) with the seller, and check for a factory sport bar or accessory bed rails.",
  "If you want a cover, fit it first: a railed cover or one that the rack maker's tonneau kit supports.",
  "Set clamp towers or the rack's feet along the rails, behind any sport bar, using the track kit the maker lists.",
  "Assemble loosely, square and center the rack, then torque every bolt to the maker's spec.",
  "Check the tailgate, StowFlex lid and third brake light for clearance with a load on.",
  "Re-check fasteners after the first drive and the first trail, and keep tent plus gear under the on-road rating.",
 ],
 "avoid": [
  {"h": "Buying a 2015–2022 rack", "body": "The 2023 bed is new. A \"2015–2025\" title needs the seller's confirmation, and a 2015–2022 part won't fit."},
  {"h": "Forgetting the sport bar", "body": "Trail Boss and many ZR2s have a bar at the front of the bed where headache racks and front uprights go."},
  {"h": "A tent on a 220 lb rack", "body": "The Thule Xsporter Pro Low is for boats and bikes. Tents need a rack rated for the tent, gear and occupants."},
  {"h": "A cover-less budget rack on a covered bed", "body": "Some budget racks say they're not for trucks with bed covers. Read the title before you buy both."},
 ],
 "verdict": {
  "thesis": "Yakima's OverHaul HD is the best tent rack for the 2023+ Colorado, the OutPost HD is the value pick, and the BackRack is the only brand-name rack here listed for the new truck by name.",
  "body": "The 2023 Colorado is still new enough that most rack listings either don't name it or span both generations, so confirmation is part of every purchase. Yakima's HD towers clamp to the rail, publish real on-road and off-road ratings, and can usually be set behind a Trail Boss or ZR2 sport bar. The BackRack is the headache rack for work trucks without a sport bar, the Thule Xsporter Pro Low suits boats and bikes, and the YZONA and Hooke Road racks cover budget builds on an uncovered bed.\n\nIf you want the bed covered as well, our Colorado tonneau cover guide lists railed covers that take crossbars. With up to 7,700 lb of towing capacity, a proper trailer hitch is the other early upgrade, and laser-fit floor liners keep trail mud off the carpet.",
 },
 "sources": [
  ["Yakima OverHaul HD towers (Yakima)", "https://yakima.com/products/overhaul-hd"],
  ["Yakima OutPost HD towers (Yakima)", "https://yakima.com/products/outpost-hd"],
  ["BackRack Original Headache Rack (RealTruck)", "https://realtruck.com/p/backrack-original-headache-rack/"],
  ["BackRack Original 15019 specs and hardware kits (RealTruck)", "https://realtruck.com/p/backrack-original-headache-rack/bkr-15019/"],
  ["Thule Xsporter Pro Low Truck Rack (RealTruck)", "https://realtruck.com/p/thule-xsporter-pro-low-truck-rack/"],
  ["2023 Chevrolet Colorado eBrochure: cargo box and tailgate (Chevrolet)", "https://www.chevrolet.com/content/dam/chevrolet/na/us/english/index/shopping-tools/download-catalog/11-pdf/2023-chevrolet-colorado-ebrochure.pdf"],
  ["2023 Chevrolet Colorado specs and StowFlex tailgate (GM Authority)", "https://gmauthority.com/blog/gm/chevrolet/colorado/2023-chevrolet-colorado/"],
  ["Rough Country Hard Tri-Fold, 2015–2026 Colorado/Canyon, Trail Boss note (Rough Country)", "https://www.roughcountry.com/product/configurable/gm-flip-up-bed-cover-49120500c"],
 ],
}

# (asin, name, brand, band, cond, note) — picks first, then variants.
FITS = [
 ("B07MDSP8T8","Yakima OverHaul HD Adjustable Truck Bed Rack (towers only)","Yakima","$1,100–$1,250",{},"Universal clamp towers; confirm 2023+ Colorado fit, sport bar spacing and crossbars in Yakima's fit lookup."),
 ("B07MRHDLS4","Yakima OutPost HD Fixed Mid Height Truck Bed Rack (towers only)","Yakima","$750–$850",{},"Universal 13 in towers; confirm 2023+ Colorado fit and crossbars in Yakima's fit lookup."),
 ("B0CDK1Q3R7","RealTruck BackRack Original Rack + Standard Bed Hardware 15002 & 30226, 2023-2025 Colorado/Canyon","BackRack","$350–$450",{},"Headache rack; confirm fit on trucks with a factory sport bar."),
 ("B09VFXD8CW","Thule Xsporter Pro Low Truck Rack, Compact Bed, no drilling","Thule","$550–$650",{},"220 lb; universal brackets — confirm 2023+ Colorado in Thule's fit guide."),
 ("B0DDHFH5YW","YZONA Overland Bed Rack with 2 LED Light Bars, 2015-2025 Colorado & Canyon (not for bed covers)","YZONA","Check listing",{},"Multi-generation clamp rack; confirm 2023+ bed and load rating with seller."),
 ("B0BPM78J1M","Hooke Road 18.8 in High Overland Bed Rack, Mid-Size Trucks Without Bed Rails (Colorado, Canyon, Ranger, Gladiator)","Hooke Road","Check listing",{},"No years in title; confirm 2023+ Colorado and load rating with seller."),
 ("B0BPM8R6GQ","Hooke Road 12.3 in Overland Bed Rack, Tacoma 5 ft / Gladiator / Ranger / Colorado","Hooke Road","$350–$450",{},"Low-profile version; confirm 2023+ Colorado with seller."),
]
