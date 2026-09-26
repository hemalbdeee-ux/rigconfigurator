"""Long-form article — Best Bed Racks for 2021–2026 Ford F-150 (P702).
Mirrors the approved pilot (ford_f150_2021_tonneau.py) and the ford_ranger_2024_bed_racks.py category page.
No invented hands-on testing: every spec below comes from the manufacturer/retailer pages listed in sources
(checked 2026-09-26). Bed lengths match ford_f150_2021_tonneau.py and db/migrations/003_vehicles.sql.
BoxLink / Bed Utility Package notes come from the F150gen14 thread cited in sources.
"""

KEY = ("ford", "f-150", "2021-present", "bed-racks")

TITLE = "Best Bed Racks for 2021–2026 Ford F-150: 6 Picks for Tents, Bikes and BoxLink Beds"
META = ("Six bed racks for the 2021+ F-150's 5.5, 6.5 and 8 ft aluminum beds, with static vs dynamic ratings, "
        "rack heights, BoxLink mounting and tonneau fit.")

FAQ = [
 ("What is the best bed rack for a 2021–2026 F-150?",
  "For a rooftop tent on the 5.5 ft bed, the Putco Venture TEC Rack (184100). Putco rates it at 1,000 lb static, 600 lb dynamic and 300 lb off-road, it bolts to the stake pockets without drilling, and it ships with four tent brackets. Putco lists it for 2015–2027 F-150, Raptor and Lightning 5'7\" beds. If that price is too steep, the RealTruck GoRack carries the same 1,000/600 lb static and dynamic figures for about half the money."),
 ("Do 2015–2020 F-150 bed racks fit the 2021+ truck?",
  "Often, yes, because Ford kept the 5.5 and 6.5 ft bed lengths. Putco sells one Venture TEC part (184100) for 2015–2027 5'7\" beds, and Rough Country lists its 10406 rack for 2015–2026. Not every maker carries parts across, though: Putco's Venture TEC Quick Rack has separate 2015–2020 and 2021–2025 listings. Buy the part the maker lists for your model year rather than assuming a carry-over."),
 ("Does my F-150 have BoxLink, and does a bed rack need it?",
  "BoxLink is Ford's set of cleat mounting points along the bed sides. On F150gen14, owners explain that from 2022 the Bed Utility Package became optional, and trucks without it have unthreaded holes where the cleats go; Ford's BoxLink kit uses self-tapping bolts to fill them. Most racks on this page mount to the stake pockets instead, so they don't need BoxLink. RealTruck's GoRack can also mount to a utility rail."),
 ("What is the difference between static and dynamic load ratings?",
  "Dynamic is what the rack should carry while the truck is moving, when bumps and braking multiply the load. Static is the parked figure, which matters when people sleep in a rooftop tent. Putco rates the Venture TEC at 1,000 lb static, 600 lb dynamic and 300 lb off-road; Rough Country rates the 10406 at 750 lb static and 400 lb dynamic. Keep the tent and gear under the moving number, and count the rack against payload too."),
 ("Can I keep a tonneau cover with a bed rack on a 2021+ F-150?",
  "Yes, if you match the pair. Putco says the Venture TEC works with most inside-rail roll-up covers. RealTruck says the Putco Quick Rack works with roll-ups such as the BAK Revolver and Extang Revolution but has to come off to open hard-folding covers such as the BAKFlip and Gator FX, and it doesn't suit many tri-fold and retractable covers. The GoRack also fits covers that have a T-slot rail system. Yakima sells Tonneau Kit 1 for select covers."),
 ("What rack height suits a rooftop tent on an F-150?",
  "Most tent owners want the tent at or just above the cab roof, so the rack clears the cab and the tent doesn't catch the wind at the windshield. Putco's Quick Rack puts its crossbars about 13 in above the bed, a mid height. Yakima's OutPost HD is fixed at 13 in and the OverHaul HD adjusts from 19 to 30 in. On F150gen14, owners post tent setups on Leitner, Adarac and Front Runner racks, and several prefer a raised rack for the bed room underneath."),
 ("Will a bed rack fit the 6.5 ft or 8 ft F-150 bed?",
  "Some will. The Putco Venture TEC 184100, RealTruck GoRack 9250101 and Rough Country 10406 listed here are 5.5 ft (5'7\") parts, and Rough Country says the 10406 only fits the 5'7\" bed. Putco sells a separate 6'7\" Quick Rack for 2021–2025. Yakima's clamp towers work by bed rail rather than by part number, so they are the easier route on an 8 ft bed; confirm with Yakima's fit lookup and pick the matching HD Bar length."),
 ("Does the Pro Access tailgate change which rack I can use?",
  "Ford added the Pro Access tailgate with the 2024 refresh, per the F-Series reference page. The racks on this page mount at the stake pockets or bed rails, not the tailgate, so the tailgate doesn't decide fit. What to check is overhang: if a tent or long load sticks out past the rear of the rack, make sure the tailgate door can still swing or drop fully before you commit to a mounting position."),
 ("Is a clamp-on rack safe on the F-150's aluminum bed?",
  "A clamp rack is fine when it is within its ratings and tightened to the maker's torque. The F-150's bed is aluminum, so over-tightening a clamp or a bolt can mark or deform the rail, and dissimilar metals in wet climates need attention. Racks that bolt into the stake pockets, like the Putco and GoRack, spread the load without clamping the rail edge. Recheck fasteners after the first drive and after rough roads."),
 ("Will a bed rack hide my third brake light?",
  "The rack itself usually won't, because the F-150's third brake light sits at the top of the cab and racks sit behind it. A tall load on the rack can, though. A rooftop tent or cargo box that stands above the cab roof line may block following drivers' view of the light. Keep tall loads toward the rear of the rack, and check state rules before adding lights to the rack itself."),
]

ARTICLE = {
 "dek": "Six racks for the 2021–2026 F-150, from a Rough Country aluminum rack near $500 to Putco's 1,000 lb Venture TEC. For each one we list the height, the static and dynamic ratings, how it mounts on the aluminum bed, and whether you can keep a tonneau cover underneath.",
 "author": "jake-morrison",
 "reviewed": "2026-09-26",
 "method": "We did not install these racks ourselves. We ranked them on published specs (static, dynamic and off-road ratings, height, material, warranty), on the fitment the maker or the Amazon listing gives for the 14th-gen F-150, and on what owners report on the F150gen14 forum about BoxLink cleats, tonneau pairings and tent setups. Picks with a universal or cross-generation listing carry a confirm note. Prices were checked at Putco, RealTruck, Rough Country and Yakima in September 2026. Amazon prices move daily, so the button shows the live price.",
 "takeaways": [
  "**Buy by bed length.** The F-150 has 5.5, 6.5 and 8 ft beds (about 67, 79 and 98 in at the rail). Most one-piece racks are 5.5 ft parts.",
  "**Read both ratings.** Putco rates the Venture TEC at 1,000 lb static, 600 lb dynamic and 300 lb off-road; the Rough Country 10406 is 750 lb static and 400 lb dynamic.",
  "**BoxLink is optional from 2022.** Trucks without the Bed Utility Package have unthreaded cleat holes; most racks here use the stake pockets instead.",
  "**Match the cover to the rack.** Putco's racks suit inside-rail roll-ups; hard folders like the BAKFlip must be worked around. T-slot covers pair with the GoRack.",
  "**Treat the aluminum bed gently.** Torque clamps and bolts to spec and recheck them; stake pocket mounts avoid clamping the rail edge.",
 ],
 "top_picks": [
  {"asin": "B07VRF2J2Q", "role": "Best overall", "why": "1,000/600/300 lb ratings, no-drill stake pocket mount, 4 tent brackets included"},
  {"asin": "B0CNS9P8RQ", "role": "Best value for a tent", "why": "Same 1,000 lb static / 600 lb dynamic as the Putco, T-slots and MOLLE panels, $1,089.99"},
  {"asin": "B0C2S5HDM8", "role": "Best with a roll-up cover", "why": "Bars about 13 in above the bed; works with roll-ups such as BAK Revolver"},
  {"asin": "B0C7D1PDYD", "role": "Best budget", "why": "Powder-coated aluminum, 750 lb static / 400 lb dynamic, $499.95"},
  {"asin": "B07MDSP8T8", "role": "Best for 6.5 and 8 ft beds", "why": "Clamp towers adjust from 19 to 30 in; not tied to one bed length"},
 ],
 "fit_table": {
  "caption": "2021–2026 F-150 bed details that affect a rack",
  "head": ["Item", "Spec", "Applies to", "What it means for a rack"],
  "rows": [
   ["5.5 ft bed (sold as 5'7\")", "About 67.1 in at the rail", "SuperCrew; only bed on Raptor and Lightning", "Most one-piece racks (Putco 184100, GoRack 9250101, RC 10406) are made for this bed."],
   ["6.5 ft bed (sold as 6'7\")", "About 78.9 in at the rail", "SuperCrew, SuperCab, Regular Cab", "Order the 6'7\" part (Putco Quick Rack) or use clamp towers."],
   ["8 ft bed", "About 97.6 in at the rail", "Regular Cab; SuperCab through 2023", "Few one-piece racks; clamp towers such as Yakima's are the usual route."],
   ["BoxLink / Bed Utility Package", "Cleat points along the bed sides", "Optional from 2022 (owner report)", "Unthreaded holes on trucks without it; Ford's kit uses self-tapping bolts."],
   ["Pro Access tailgate", "Swing-out tailgate option", "2024+ refresh", "Doesn't affect rail mounts; check tent or load overhang clears it."],
   ["Bed material", "Aluminum", "All", "Torque clamps to spec; stake pocket mounts avoid loading the rail edge."],
  ],
 },
 "look_for": [
  {"h": "A part for your bed length, not your cab",
   "body": "A one-piece bed rack is built for one bed length, and the F-150 has three. The 5.5 ft box, sold as 5'7\", runs about 67.1 in at the rail and is the only bed on the Raptor and Lightning. The 6.5 ft box, sold as 6'7\", is about 78.9 in, and the 8 ft box about 97.6 in. Cab is only a clue, because a SuperCrew can have either the 5.5 or 6.5 ft box. The Putco Venture TEC 184100, the RealTruck GoRack 9250101 and the Rough Country 10406 are 5.5 ft parts, and Rough Country says its rack only fits the 5'7\" bed. On a 6.5 or 8 ft bed, look for a 6'7\" part number or use clamp towers."},
  {"h": "Stake pockets, BoxLink and the utility track",
   "body": "The 14th-gen F-150 gives a rack three possible anchors. The stake pockets are the most common: Putco's Venture TEC and Quick Rack and the RealTruck GoRack all bolt into them without drilling. BoxLink is Ford's system of cleat points along the bed sides, and on F150gen14 owners explain that from 2022 the Bed Utility Package that includes it became optional. Trucks without it have unthreaded holes, and Ford's BoxLink kit uses self-tapping bolts to fill them. RealTruck says the GoRack can also mount to a utility rail. Before ordering, look in your bed, note which of these you have, and pick a rack whose instructions use them."},
  {"h": "Static, dynamic and off-road ratings",
   "body": "A rack that will carry a rooftop tent should publish more than one number. Dynamic is the most it should carry while moving, when braking and bumps multiply the load. Static is the parked figure, which counts when people are asleep up top. Off-road is the rough-trail figure. Putco rates the Venture TEC at 1,000 lb static, 600 lb dynamic and 300 lb off-road. RealTruck gives the GoRack 1,000 lb static and 600 lb dynamic, Rough Country rates the 10406 at 750 lb static and 400 lb dynamic, and Yakima gives its HD towers 500 lb on-road and 300 lb off-road. Then check payload on the door-jamb sticker, since the rack, tent and gear all count against it."},
  {"h": "Rack height against the cab",
   "body": "Racks fall into three heights. Low racks stay below the cab and suit kayaks, bikes and lumber with less wind noise. Mid-height racks, like Putco's Quick Rack with its crossbars about 13 in above the bed and Yakima's 13 in OutPost HD, put a load near the cab roof line. Full or adjustable racks, like Yakima's 19–30 in OverHaul HD, lift a tent above the cab and leave room for bins underneath. On F150gen14, owners who run tents say a raised rack keeps full use of the bed and the rear-view mirror. A tall tent or box can hide the cab's third brake light from following traffic, so check the view from behind."},
  {"h": "Tonneau cover plans",
   "body": "Pick the cover and the rack together. Putco says the Venture TEC works with most inside-rail roll-up covers. RealTruck says the Putco Quick Rack works with roll-ups such as the BAK Revolver and Extang Revolution, but must be removed to operate hard-folding covers such as the BAKFlip and Gator FX, and it doesn't suit many tri-fold and retractable covers. The GoRack is compatible with covers that have a T-slot rail system, and Yakima sells Tonneau Kit 1 for select covers. On F150gen14, owners report pairing BAKFlip covers with bed bars that require removing the cover first. If you already own a hard folder, check the rack's cover list before you buy."},
 ],
 "look_table": {
  "head": ["Feature", "Look for", "Avoid"],
  "rows": [
   ["Fitment", "A part number for your bed length (5'7\", 6'7\" or 8 ft) and model year", "A listing that names only the cab"],
   ["Mounting", "No-drill stake pocket mounts or a stated BoxLink / utility rail option", "Clamps with no torque spec on an aluminum rail"],
   ["Load rating", "Separate static, dynamic and off-road figures", "One number with no context"],
   ["Height", "A height that matches your load: low for boats, mid or adjustable for tents", "A full-height rack for bikes you'll lift overhead"],
   ["Tonneau", "A stated cover list or tonneau kit", "Silence about covers if you own one"],
   ["Warranty", "Limited lifetime (Putco, RealTruck, Yakima, Rough Country)", "No warranty stated"],
  ],
 },
 "types_table": {
  "caption": "Bed rack styles compared on the 2021–2026 F-150",
  "head": ["Type", "Example on this page", "Typical use", "Rooftop tent", "Tonneau", "Trade-off"],
  "rows": [
   ["Full overland system", "Putco Venture TEC", "Tent, awning, recovery gear", "Yes (1,000 lb static)", "Most inside-rail roll-ups", "Highest price"],
   ["Mid-height overland", "RealTruck GoRack", "Tent, MOLLE gear, fuel packs", "Yes (1,000 lb static)", "T-slot rail covers", "5.5 ft bed only on this listing"],
   ["Mid-height bars", "Putco Venture TEC Quick Rack", "Bikes, boards, light tent", "Check with Putco", "Roll-ups; not most hard folders", "Lower-profile uprights"],
   ["Aluminum budget rack", "Rough Country 10406", "Tent, ladders, gear", "Yes (750 lb static)", "Check the listing", "5'7\" bed only; nutserts"],
   ["Clamp towers", "Yakima OverHaul HD / OutPost HD", "Changing loads, any bed length", "Yes (500 lb on-road)", "With Tonneau Kit 1", "Crossbars cost extra"],
  ],
 },
 "picks": [
  {"asin": "B07VRF2J2Q", "role": "Best overall", "price": "About $2,069–$2,399",
   "pros": ["1,000 lb static / 600 lb dynamic / 300 lb off-road", "6061-T6 aluminum, CNC-bent to the cab contour", "No-drill stake pocket mounts", "Four tent brackets included", "Listed for F-150, Raptor and Lightning 5'7\" beds"],
   "cons": ["The most expensive rack here", "5'7\" bed only; no 6.5 or 8 ft version on this listing", "Powder-coat finish terms are shorter than the structural warranty; read them"],
   "body": "Putco's Venture TEC is the rack to beat on the 5.5 ft bed. Putco lists part 184100 for 2015–2027 F-150 5'7\" beds, including the 2017–2027 Raptor and 2022–2026 Lightning, which covers every 14th-gen truck with the short box. It rates the rack at 1,000 lb static, 600 lb dynamic and 300 lb off-road dynamic, the strongest published figures on this page. The frame is 6061-T6 aluminum in a matte black powder coat, CNC-bent to follow the cab contour, and it mounts in the stake pockets with no drilling. A dual T-slot rail system takes third-party accessories, and Putco includes four tent brackets at no extra cost.\n\nThe price is the catch. Putco's own site showed $2,068.89 on sale in September 2026, against a regular price of $2,980.78, and RealTruck lists the Venture TEC line from $2,398.99. For tonneau owners, Putco says it works with most inside-rail roll-up covers, so a hard folder or retractable may need a rethink. Putco describes a limited lifetime warranty, but the page gives shorter coverage for the powder-coat finish, so read the finish terms. On the aluminum bed, stake pocket mounting avoids clamping the rail edge.",
   "who": "Short-bed, Raptor and Lightning owners building a serious rooftop tent setup who want the highest ratings and a no-drill install.",
   "specs": [["Part", "Putco 184100"], ["Fits", "2015–2027 F-150 5'7\" bed, incl. Raptor and Lightning (per Putco)"], ["Material", "6061-T6 aluminum, matte black powder coat"], ["Load rating", "1,000 lb static / 600 lb dynamic / 300 lb off-road"], ["Mounting", "Stake pockets, no drilling"], ["Included", "4 tent brackets"], ["Tonneau", "Most inside-rail roll-up covers"], ["Price", "$2,068.89 sale (Putco); from $2,398.99 (RealTruck)"]]},
  {"asin": "B0CNS9P8RQ", "role": "Best value for a tent", "price": "$1,089.99",
   "pros": ["1,000 lb static / 600 lb dynamic", "T-slots on all four sides of the side rails", "Integrated MOLLE side panels", "Stake pocket or utility rail mounting", "Limited lifetime warranty"],
   "cons": ["Listing reads 2015–2024; confirm 2025–2026", "5.5 ft bed only on this listing", "No off-road rating or exact height published on the page read"],
   "body": "RealTruck's GoRack is the value pick for a tent because it matches the Putco's static and dynamic figures for about half the money. RealTruck rates it at 1,000 lb static and 600 lb dynamic and lists it at $1,089.99. It is a hybrid of aluminum and steel, and the extruded side rails carry T-slots on all four sides, so lights, awnings and tie-downs can go almost anywhere. Integrated MOLLE side panels take fuel packs, traction boards, jacks and tools, which is more organizer than most racks offer at this price.\n\nFor the F-150, the mounting options are the draw. RealTruck says the GoRack mounts directly to the bed's stake pockets or to a utility rail, so it suits trucks with or without Ford's bed track, and it is compatible with covers that use a T-slot rail system. The Amazon listing is part 9250101 for the 2015–2024 F-150 5.5 ft bed, so confirm fit for a 2025 or 2026 truck with the seller before ordering, and don't try it on a 6.5 or 8 ft bed. RealTruck doesn't publish an off-road rating or an exact height on the page we read, so ask if you plan on rough trails.",
   "who": "Short-bed owners who want Putco-level static and dynamic ratings and MOLLE storage at about half the price.",
   "specs": [["Part", "RealTruck GoRack 9250101"], ["Fits", "2015–2024 F-150 5.5 ft bed (per listing; confirm 2025–2026)"], ["Material", "Aluminum and steel"], ["Load rating", "1,000 lb static / 600 lb dynamic"], ["Mounting", "Stake pockets or utility rail"], ["Extras", "T-slots on four sides, MOLLE side panels"], ["Tonneau", "Covers with a T-slot rail system"], ["Warranty", "Limited lifetime"], ["Price", "$1,089.99 (RealTruck)"]]},
  {"asin": "B0C2S5HDM8", "role": "Best with a roll-up cover", "price": "From $1,051.99",
   "pros": ["Crossbars about 13 in above the bed", "Works with roll-ups such as BAK Revolver and Extang Revolution", "No-drill stake pocket install", "Separate 5'7\" and 6'7\" parts for 2021–2025", "Made in the USA; limited lifetime warranty"],
   "cons": ["Must come off to open hard folders such as BAKFlip and Gator FX", "Not for many tri-fold and retractable covers", "Listing reads 2021–2025; confirm 2026"],
   "body": "The Venture TEC Quick Rack is Putco's lighter take on the idea, and it is the pick for owners who want to keep a roll-up tonneau. RealTruck says the cross rails sit 9 in above the side rails, which puts them about 13 in above the bed, a mid height that suits bikes, boards and ladders. It is 6061-T6 aluminum with a textured matte black coat, bolts to the stake pockets with no drilling, has removable, adjustable crossbars and uprights, and uses a dual T-slot rail system. RealTruck gives a 1,000 lb capacity, starts it at $1,051.99 and lists a limited lifetime warranty.\n\nThe cover list is the reason to choose it. RealTruck says it works with roll-ups such as the Access, BAK Revolver and Extang Revolution. It has to be removed to operate hard-folding covers such as the BAKFlip and Gator FX, and it doesn't suit many tri-folds and retractables. Putco lists a 2021–2025 5'7\" version here and a separate 2021–2025 6'7\" version, so 6.5 ft owners have an option too. RealTruck doesn't split the 1,000 lb figure into static and dynamic, so confirm a moving rating before carrying a tent.",
   "who": "Owners with a roll-up tonneau who want a mid-height rack for bikes, boards and ladders on the 5.5 or 6.5 ft bed.",
   "specs": [["Type", "Mid-height rack"], ["Fits", "2021–2025 F-150 5'7\" bed (6'7\" version listed separately)"], ["Height", "Cross rails about 13 in above the bed"], ["Material", "6061-T6 aluminum"], ["Capacity", "1,000 lb (RealTruck; no static/dynamic split)"], ["Mounting", "Stake pockets, no drilling"], ["Tonneau", "Roll-ups; remove for hard folders"], ["Price", "From $1,051.99 (RealTruck)"]]},
  {"asin": "B0C7D1PDYD", "role": "Best budget", "price": "$499.95",
   "pros": ["750 lb static / 400 lb dynamic", "Powder-coated aluminum", "Rough Country lists 2015–2026 incl. Raptor and Tremor", "Configurable height; half-height version listed", "Molded end caps and T-slot covers"],
   "cons": ["5'7\" bed only", "Install uses nutserts; a nutsert tool is recommended", "Rough Country says it doesn't work with its own hard-shell rooftop tent"],
   "body": "Rough Country's 10406 is the budget rack with real numbers behind it. Rough Country rates it at 750 lb static and 400 lb dynamic and lists it at $499.95, which is less than half the GoRack. It is powder-coated aluminum with molded end caps and T-slot covers, and Rough Country describes endless mounting adjustability while keeping rear visibility. Rough Country lists it for the 2015–2026 F-150, including the 2017–2026 Raptor and 2021–2026 Tremor, and it is configurable by height; a half-height version is sold under its own Amazon listing.\n\nMind two limits. Rough Country says the rack only fits models with the 5'7\" bed, so 6.5 and 8 ft owners need another option. And its installation calls for nutserts, with a nutsert tool recommended, so read the instructions to see whether your truck needs any holes before you commit on an aluminum bed. Rough Country also notes the rack doesn't work with its own hard-shell rooftop tent, so check other tents against the rack's bar spacing. The Amazon title reads 2015–2023; Rough Country's page covers through 2026.",
   "who": "Short-bed owners who want a rated aluminum rack for a tent or gear at the lowest price among branded options.",
   "specs": [["Part", "Rough Country 10406"], ["Fits", "2015–2026 F-150 5'7\" bed, incl. Raptor and Tremor (per Rough Country)"], ["Material", "Powder-coated aluminum"], ["Load rating", "750 lb static / 400 lb dynamic"], ["Height", "Configurable (half-height version listed)"], ["Mounting", "Nutserts; nutsert tool recommended"], ["Warranty", "Lifetime (per Rough Country policy)"], ["Price", "$499.95 (Rough Country)"]]},
  {"asin": "B07MDSP8T8", "role": "Best for 6.5 and 8 ft beds", "price": "$1,200 (towers)",
   "pros": ["Height adjusts from 19 to 30 in", "500 lb on-road / 300 lb off-road", "Not tied to one bed length", "Track Kit and Tonneau Kit adapters", "Limited lifetime warranty"],
   "cons": ["Towers only; HD Bar crossbars extra", "59.52 lb before crossbars", "Universal fit; confirm the F-150 kit with Yakima"],
   "body": "If your F-150 has the 6.5 or 8 ft bed, or you want a rack that moves between trucks, Yakima's OverHaul HD is the flexible choice. Its four towers clamp to the bed rails instead of bolting into one bed's stake pockets, and they adjust from 19 to 30 in, so the same rack can carry kayaks just above the cab or lift a tent high enough for a fridge and bins underneath. Yakima rates it at 500 lb on-road and 300 lb off-road, lists the towers at 59.52 lb and $1,200, and covers them with a limited lifetime warranty.\n\nThe total cost is higher than the tower price. You add HD Bar crossbars in 60, 68 or 78 in lengths, and Yakima says tracked beds need Track Kit 1 or 2 and select tonneau covers need Tonneau Kit 1. That makes it the rack to consider on a truck with Ford's bed utility track or a cover you want to keep. Yakima's page doesn't list the F-150 by name, so confirm the kit and crossbar length in Yakima's fit lookup, and torque the clamps to spec on the aluminum rails.",
   "who": "Owners of 6.5 and 8 ft beds, or anyone whose loads change often, who want one rack that goes from boat height to tent height.",
   "specs": [["Type", "Adjustable clamp towers"], ["Height", "19–30 in"], ["Load rating", "500 lb on-road / 300 lb off-road"], ["Weight", "59.52 lb (towers)"], ["Mounting", "Bed rail clamps; Track Kit 1/2 for tracked beds"], ["Tonneau", "Tonneau Kit 1 for select covers"], ["Crossbars", "HD Bar 60/68/78 in, sold separately"], ["Warranty", "Limited lifetime"], ["Price", "$1,200 towers (Yakima)"]]},
  {"asin": "B07MRHDLS4", "role": "Best fixed mid height", "price": "$799 (towers)",
   "pros": ["Fixed 13 in mid height", "500 lb on-road / 300 lb off-road", "44.09 lb towers", "Track Kit and Tonneau Kit adapters", "Limited lifetime warranty"],
   "cons": ["Towers only; crossbars extra", "Universal fit; confirm the F-150 kit with Yakima", "Lower ratings than the Putco or GoRack"],
   "body": "Yakima's OutPost HD is the simpler sibling of the OverHaul HD: four towers at a fixed 13 in, rated 500 lb on-road and 300 lb off-road. Yakima lists them at 44.09 lb and $799, with a limited lifetime warranty. With HD Bar crossbars in 60, 68 or 78 in lengths, it gives a brand-name mid-height platform for a light tent, bikes or a cargo box, and it works on any of the F-150's three bed lengths because the towers clamp to the rails rather than matching one bed.\n\nThe same homework applies as with the OverHaul. Yakima says tracked beds need Track Kit 1 or Track Kit 2 and select tonneau covers need Tonneau Kit 1, and its page doesn't name the F-150, so confirm the kit and bar length with Yakima's fit lookup. Thirteen inches sits below or near the cab roof on most F-150s, so a tent may need to be positioned so it clears the cab when it opens. For a heavy tent with people in it, the Putco and GoRack have much higher static ratings.",
   "who": "Owners who want a brand-name, lighter mid-height rack for bikes, boards and a light tent on any bed length.",
   "specs": [["Type", "Fixed-height clamp towers"], ["Height", "13 in"], ["Load rating", "500 lb on-road / 300 lb off-road"], ["Weight", "44.09 lb (towers)"], ["Mounting", "Bed rail clamps; Track Kit 1/2 for tracked beds"], ["Tonneau", "Tonneau Kit 1 for select covers"], ["Warranty", "Limited lifetime"], ["Price", "$799 towers (Yakima)"]]},
 ],
 "install": [
  "Measure the bed at the rail (about 67, 79 or 98 in) and order the rack part for that bed length and your model year.",
  "Note what the bed has: stake pockets, BoxLink cleat points, or a bed utility track. Choose the mounting hardware the rack maker specifies for it.",
  "If you plan a tonneau cover, fit it first and confirm it is on the rack's compatible list, or buy the maker's tonneau kit.",
  "Set the rack or towers in place, square them to the cab and center them side to side before tightening anything.",
  "Tighten every bolt and clamp evenly to the maker's torque; on the aluminum bed, don't over-tighten clamps on the rail edge.",
  "Fit crossbars and tent brackets, check the tent or load clears the cab and the tailgate, and look at the third brake light from behind.",
  "Recheck all fasteners after the first drive and after rough roads, and keep tent plus gear under the dynamic rating.",
 ],
 "avoid": [
  {"h": "Buying by cab instead of bed", "body": "A SuperCrew can have a 5.5 or 6.5 ft box. Most one-piece racks here are 5'7\" parts, so measure the bed first."},
  {"h": "Driving at the static rating", "body": "Static is for a parked truck. On the road, stay under the dynamic figure: 600 lb for the Putco and GoRack, 400 lb for the Rough Country, 500 lb for the Yakima towers."},
  {"h": "Assuming BoxLink is there", "body": "The Bed Utility Package became optional for 2022, per owners. Check for threaded cleat points before buying hardware that needs them."},
  {"h": "Ignoring the tonneau cover", "body": "The Putco Quick Rack has to come off to open a BAKFlip or Gator FX. Check the cover list before you buy either one."},
 ],
 "verdict": {
  "thesis": "Match the rack to the bed length, then pick: the Putco Venture TEC for the strongest tent rack, the RealTruck GoRack for the same static and dynamic ratings at half the price, and Yakima's towers for 6.5 and 8 ft beds.",
  "body": "On the 5.5 ft bed, the Putco Venture TEC has the best published ratings and covers the Raptor and Lightning, and the GoRack gets close for much less. The Putco Quick Rack is the one to pair with a roll-up tonneau cover, and the Rough Country 10406 is the rated budget choice. Owners of 6.5 and 8 ft beds get the most flexibility from Yakima's OverHaul HD and OutPost HD towers. Whichever you buy, count the rack, tent and passengers against payload and recheck the fasteners on the aluminum bed.\n\nIf you're building a camping rig, a trailer hitch and floor liners are worth sorting at the same time, and running boards help when you're reaching up to a rack. Owners of the previous 2015–2020 F-150 can use several of these racks too, but should shop from that truck's own list. The vehicle hub lists every fit-checked accessory for your F-150.",
 },
 "sources": [
  ["Putco Venture TEC Rack 184100, F-150 5'7\" bed (Putco)", "https://www.putco.com/product/venture-tec-rack/184100/"],
  ["Putco Venture TEC Rack (RealTruck)", "https://realtruck.com/p/putco-venture-tec-rack/"],
  ["Putco Venture TEC Quick Rack (RealTruck)", "https://realtruck.com/p/putco-venture-tec-quick-rack/"],
  ["RealTruck GoRack (RealTruck)", "https://realtruck.com/p/realtruck-gorack/"],
  ["Rough Country Bed Rack 10406 (Rough Country)", "https://www.roughcountry.com/product/configurable/ford-bed-rack-10406"],
  ["Yakima OverHaul HD towers (Yakima)", "https://yakima.com/products/overhaul-hd"],
  ["Yakima OutPost HD towers (Yakima)", "https://yakima.com/products/outpost-hd"],
  ["2022 without Bed Utility Package: BoxLink options (F150gen14)", "https://www.f150gen14.com/forum/threads/2022-without-bed-utility-package-box-link-options.10144/"],
  ["Let's see your tent setups (F150gen14)", "https://www.f150gen14.com/forum/threads/lets-see-your-tent-setups-%E2%9B%BA%EF%B8%8F.17958/page-4"],
  ["Ford F-Series 14th generation (Wikipedia)", "https://en.wikipedia.org/wiki/Ford_F-Series_(fourteenth_generation)"],
 ],
}

# Product list for this page. (asin, name, brand, band, cond, note)
FITS = [
 ("B07VRF2J2Q","Putco Venture TEC Rack, Ford F-150 2015-2027 5'7\" Bed","Putco","$2,000–$2,400",{"bed_length_in":66},"5.5 ft bed incl. Raptor and Lightning; 1,000/600/300 lb."),
 ("B0CNS9P8RQ","RealTruck GoRack Overland Truck Rack 9250101, 2015-2024 Ford F-150 5.5' Bed","RealTruck","$1,000–$1,150",{"bed_length_in":66},"Listing ends at 2024; confirm 2025-2026 with seller."),
 ("B0C2S5HDM8","Putco Venture TEC Quick Rack, Ford F-150 2021-2025 5'7\" Bed","Putco","$1,000–$1,150",{"bed_length_in":66},"Roll-up covers OK; remove to open hard folders. Confirm 2026."),
 ("B0C7D1PDYD","Rough Country Aluminum Bed Rack 10406, 2015-2023 Ford F-150","Rough Country","$450–$550",{"bed_length_in":66},"5'7\" bed only; Rough Country lists through 2026 — confirm on listing."),
 ("B07MDSP8T8","Yakima OverHaul HD Adjustable Truck Bed Rack (towers only)","Yakima","$1,100–$1,250",{},"Universal clamp towers; confirm F-150 track kit and crossbar length in Yakima's fit lookup."),
 ("B07MRHDLS4","Yakima OutPost HD Fixed Mid Height Truck Bed Rack (towers only)","Yakima","$750–$850",{},"Universal clamp towers; confirm F-150 track kit and crossbar length in Yakima's fit lookup."),
 ("B0C2S78YNB","Putco Venture TEC Quick Rack, Ford F-150 2021-2025 6'7\" Bed","Putco","$1,000–$1,200",{"bed_length_in":78},"6.5 ft bed version; confirm 2026."),
 ("B0DC13ST7Y","Rough Country Aluminum Bed Rack, Ford F-150 2015-2024, Half Height","Rough Country","$450–$550",{"bed_length_in":66},"Half-height configuration; 5'7\" bed — confirm 2025-2026."),
]
