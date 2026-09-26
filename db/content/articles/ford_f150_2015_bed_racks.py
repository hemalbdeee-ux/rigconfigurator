"""Long-form article — Best Bed Racks for 2015–2020 Ford F-150 (P552).
Mirrors the approved pilot (ford_f150_2021_tonneau.py) and the ford_ranger_2024_bed_racks.py category page.
No invented hands-on testing: every spec below comes from the manufacturer/retailer pages listed in sources
(checked 2026-09-26). Bed lengths and Raptor bed notes match ford_f150_2015_tonneau.py and
db/migrations/003_vehicles.sql. BoxLink owner comments come from the F150Forum thread cited in sources.
"""

KEY = ("ford", "f-150", "2015-2020", "bed-racks")

TITLE = "Best Bed Racks for 2015–2020 Ford F-150: 6 Picks for the 5.5, 6.5 and 8 ft Aluminum Beds"
META = ("Six bed racks for the 13th-gen F-150 and 2017–2020 Raptor, with static vs dynamic ratings, heights, "
        "stake pocket vs BoxLink mounting and tonneau fit.")

FAQ = [
 ("What is the best bed rack for a 2015–2020 F-150?",
  "For a rooftop tent on the 5.5 ft box, the Putco Venture TEC Rack (184100). Putco lists that one part for 2015–2027 F-150 5'7\" beds, including the 2017–2020 Raptor, and rates it at 1,000 lb static, 600 lb dynamic and 300 lb off-road with a no-drill stake pocket install. For roughly half the price, the RealTruck GoRack gives the same 1,000 lb static and 600 lb dynamic figures, and the Rough Country 10406 is the rated budget pick at $499.95."),
 ("Will a rack I buy now move to a 2021+ F-150 later?",
  "Some will. Ford kept the 5.5 and 6.5 ft bed lengths for the 2021 truck, and several makers list one part across both generations: Putco's Venture TEC 184100 covers 2015–2027 5'7\" beds, the GoRack 9250101 listing reads 2015–2024, and Rough Country lists the 10406 for 2015–2026. Others split at 2021, including Putco's Quick Rack. Yakima's clamp towers aren't tied to one truck at all, which makes them the easiest to carry over."),
 ("Does the Raptor need a different bed rack?",
  "Not usually, as long as you buy for the 5.5 ft box. Every 2017–2020 Raptor, SuperCab or SuperCrew, has the 5.5 ft bed. Putco lists the Venture TEC 184100 for the 2017–2027 Raptor 5'7\" bed, and Rough Country lists the 10406 for the 2017–2026 Raptor. What differs is how the truck gets used: on rough trails, the off-road rating matters more than the static one, and Putco publishes 300 lb off-road for the Venture TEC."),
 ("Can I mount a bed rack to the BoxLink cleats?",
  "Not with most off-the-shelf racks. BoxLink is Ford's cleat system in the bed sides, and on F150Forum a 13th-gen owner calls it mostly useless for anything but tie-downs; the rack ideas in that thread were homemade brackets for 2x4 or 2x6 uprights. The branded racks on this page bolt into the stake pockets instead. RealTruck says the GoRack can also mount to a utility rail, which helps if your truck has Ford's bed track."),
 ("What is the difference between static and dynamic load ratings?",
  "Dynamic is what the rack should carry on the move, when bumps and braking multiply the load. Static is the parked figure, which matters for people sleeping in a rooftop tent. The racks here range from Putco's 1,000 lb static / 600 lb dynamic / 300 lb off-road to Rough Country's 750 lb static / 400 lb dynamic and Yakima's 500 lb on-road / 300 lb off-road. Keep the tent and gear under the moving figure and count all of it against payload."),
 ("Can I use a tonneau cover and a bed rack together?",
  "Yes, with the right pairing. Putco says the Venture TEC works with most inside-rail roll-up covers. RealTruck says Putco's Quick Rack works with roll-ups like the BAK Revolver and Extang Revolution but must be removed to open hard folders such as the BAKFlip and Gator FX, and doesn't suit many tri-folds and retractables. The GoRack suits covers with a T-slot rail system. Yakima's Tonneau Kit 1 covers select covers for its towers."),
 ("Is there a bed rack for the 6.5 ft or 8 ft 2015–2020 bed?",
  "Yes, but fewer one-piece racks. Putco sells the Venture TEC Quick Rack for the 2015–2020 6'7\" bed under its own listing. The Putco 184100, GoRack 9250101 and Rough Country 10406 in this guide are 5.5 ft parts, and Rough Country says the 10406 fits only the 5'7\" bed. For 8 ft work trucks, Yakima's clamp towers are the practical choice; confirm the fit kit and HD Bar length with Yakima's fit lookup."),
 ("What rack height works for a rooftop tent?",
  "Most tent owners aim for the tent at or just above the cab roof, which means a mid or full-height rack. Putco's Quick Rack places its crossbars about 13 in above the bed, and Yakima's OutPost HD is fixed at 13 in. Yakima's OverHaul HD adjusts from 19 to 30 in, high enough to keep a fridge or bins under the tent. Low racks that stay under the cab are better for boats and bikes than tents."),
 ("Should I worry about the aluminum bed with a rack?",
  "It deserves some care. The 13th-gen F-150 was the first with an aluminum bed, so over-tightened clamps or bolts can mark or deform the rail, and mixed metals in salty climates can corrode. Stake pocket mounts, used by the Putco and GoRack racks, spread the load without clamping the rail edge. Tighten every fastener to the maker's torque, and recheck after the first drive and after rough roads."),
 ("Does a tall rack load block the third brake light?",
  "It can. The F-150's third brake light sits at the top of the cab, and a rack behind it usually won't hide it by itself. A rooftop tent, cargo box or tall stack of gear that rises above the cab roof line can block following drivers' view, though. Keep tall loads toward the back of the rack where possible, and check your state's rules before adding lights to the rack."),
]

ARTICLE = {
 "dek": "Six racks for the 13th-gen F-150 and the 2017–2020 Raptor, from Rough Country's $500 aluminum rack to Putco's 1,000 lb Venture TEC. For each one we list the height, the static and dynamic ratings, how it mounts on the aluminum bed, and which tonneau covers can stay.",
 "author": "jake-morrison",
 "reviewed": "2026-09-26",
 "method": "We did not install these racks ourselves. We ranked them on published specs (static, dynamic and off-road ratings, height, material, warranty), on the fitment the maker or Amazon listing gives for the 2015–2020 F-150, and on owner discussion of BoxLink rack mounting on F150Forum. Several racks here are sold across both the 13th- and 14th-gen trucks, and universal clamp towers carry a confirm note. Prices were checked at Putco, RealTruck, Rough Country and Yakima in September 2026. Amazon prices move daily, so the button shows the live price.",
 "takeaways": [
  "**Buy by box, not cab.** Beds are 5.5, 6.5 and 8 ft (about 67.1, 78.9 and 97.6 in at the rail), and every 2017–2020 Raptor has the 5.5 ft box.",
  "**Stake pockets beat BoxLink for racks.** Branded racks here bolt into the pockets; 13th-gen owners call BoxLink mostly a tie-down system.",
  "**Read static and dynamic.** Putco: 1,000 / 600 lb plus 300 lb off-road. Rough Country 10406: 750 / 400 lb. Yakima towers: 500 lb on-road.",
  "**Several racks carry over to 2021+.** Putco 184100 and Rough Country 10406 are listed across both generations; the Putco Quick Rack is not.",
  "**Plan the tonneau at the same time.** Roll-ups pair with Putco racks; hard folders like the BAKFlip must be removed around the Quick Rack.",
 ],
 "top_picks": [
  {"asin": "B07VRF2J2Q", "role": "Best overall", "why": "1,000/600/300 lb, no-drill stake pockets, tent brackets included, Raptor listed"},
  {"asin": "B0CNS9P8RQ", "role": "Best value for a tent", "why": "1,000 lb static / 600 lb dynamic with MOLLE panels for $1,089.99"},
  {"asin": "B0C7D1PDYD", "role": "Best budget", "why": "750 lb static / 400 lb dynamic aluminum rack for $499.95"},
  {"asin": "B0C2SCFWHH", "role": "Best for the 6.5 ft bed", "why": "Putco Quick Rack part made for the 2015–2020 6'7\" box"},
  {"asin": "B07MDSP8T8", "role": "Best for 8 ft beds", "why": "19–30 in clamp towers not tied to one bed length"},
 ],
 "fit_table": {
  "caption": "2015–2020 F-150 bed details that affect a rack",
  "head": ["Item", "Spec", "Applies to", "What it means for a rack"],
  "rows": [
   ["5.5 ft bed (sold as 5'7\")", "About 67.1 in at the rail", "SuperCrew; all 2017–2020 Raptors", "The bed most one-piece racks are built for (Putco 184100, GoRack 9250101, RC 10406)."],
   ["6.5 ft bed (sold as 6'7\")", "About 78.9 in at the rail", "SuperCrew, SuperCab, Regular Cab", "Order a 6'7\" part such as the Putco Quick Rack, or use clamp towers."],
   ["8 ft bed (sold as 8'2\")", "About 97.6 in at the rail", "SuperCab, Regular Cab", "Few one-piece racks; clamp towers are the usual route."],
   ["BoxLink cleats", "Ford cleat points in the bed sides", "2015–2020 trucks so equipped", "Owners call it mainly a tie-down system; racks here use stake pockets."],
   ["Bed utility track", "Optional Ford track", "Trucks so equipped", "GoRack can mount to a utility rail; Yakima needs a Track Kit."],
   ["Bed material", "Aluminum", "All", "Torque fasteners to spec; stake pocket mounts avoid clamping the rail edge."],
  ],
 },
 "look_for": [
  {"h": "The right box length",
   "body": "The 13th-gen F-150 has three beds, and a one-piece rack fits only one of them. The 5.5 ft box, sold as 5'7\", is about 67.1 in at the rail and is on every 2017–2020 Raptor, SuperCab or SuperCrew. The 6.5 ft box, sold as 6'7\", is about 78.9 in, and the 8 ft box, often listed as 8'2\", is about 97.6 in. A SuperCab can have the 6.5 or 8 ft box, so the cab won't settle it. The Putco 184100, GoRack 9250101 and Rough Country 10406 are all short-box parts, and Rough Country states the 10406 fits only the 5'7\" bed. Measure from the bulkhead to the closed tailgate before you order."},
  {"h": "Stake pockets, BoxLink and the utility track",
   "body": "Racks need solid anchors, and the stake pockets are the usual answer on this truck. Putco's Venture TEC and Quick Rack and the RealTruck GoRack bolt into them without drilling. Ford's BoxLink cleats look like an obvious alternative, but on F150Forum a 13th-gen owner describes BoxLink as mostly useless for anything but tie-downs, and the rack ideas in that thread were homemade brackets holding 2x4 or 2x6 uprights. If your truck has Ford's optional bed utility track, RealTruck says the GoRack can mount to a utility rail, and Yakima says tracked beds need its Track Kit 1 or 2. Check which anchors your truck has before buying hardware."},
  {"h": "Three load ratings, not one",
   "body": "Static, dynamic and off-road figures answer different questions. Dynamic is the most the rack should carry while moving. Static is the parked limit, the one that matters when two people are asleep in a tent. Off-road is the limit on rough trails, which is the number Raptor owners should watch. Putco rates the Venture TEC at 1,000 lb static, 600 lb dynamic and 300 lb off-road. RealTruck gives the GoRack 1,000 lb static and 600 lb dynamic, Rough Country rates the 10406 at 750 lb static and 400 lb dynamic, and Yakima gives both HD towers 500 lb on-road and 300 lb off-road. Add the rack, tent and gear, and check the total against the payload on the door-jamb sticker."},
  {"h": "Height against the cab roof",
   "body": "A rack's height decides what it is good for. Low racks stay below the cab for kayaks, bikes and lumber, with less wind noise and better fuel economy. Mid-height racks, like Putco's Quick Rack with crossbars about 13 in above the bed or Yakima's 13 in OutPost HD, put a load near the roof line. Adjustable racks such as the 19–30 in OverHaul HD can lift a tent clear of the cab and leave room below for a fridge or bins. Taller loads catch more wind and can hide the cab's third brake light from drivers behind, so check the view from the rear after loading."},
  {"h": "Covers that live under the rack",
   "body": "If a tonneau cover is part of the plan, choose it alongside the rack. Putco says the Venture TEC works with most inside-rail roll-up covers. RealTruck says the Putco Quick Rack works with roll-ups including the Access, BAK Revolver and Extang Revolution, has to come off to operate hard-folding covers such as the BAKFlip and Gator FX, and doesn't suit many tri-fold and retractable covers. The GoRack suits covers with a T-slot rail system, and Yakima's Tonneau Kit 1 fits select covers. If you already own a hard-folding cover, a rack that clears it or uses its rails will save a lot of frustration."},
 ],
 "look_table": {
  "head": ["Feature", "Look for", "Avoid"],
  "rows": [
   ["Fitment", "A part number for your box (5'7\", 6'7\" or 8 ft) covering 2015–2020", "Listings that name only the cab"],
   ["Mounting", "No-drill stake pocket mounts or a stated utility rail option", "Homemade BoxLink brackets for a tent load"],
   ["Load rating", "Separate static, dynamic and off-road figures", "A single capacity number"],
   ["Height", "Low for boats and bikes; mid or adjustable for tents", "More height than the load needs"],
   ["Tonneau", "A published cover list or tonneau kit", "No mention of covers when you own one"],
   ["Warranty", "Limited lifetime (Putco, RealTruck, Yakima, Rough Country)", "Unstated coverage"],
  ],
 },
 "types_table": {
  "caption": "Bed rack styles compared on the 2015–2020 F-150",
  "head": ["Type", "Example on this page", "Typical use", "Rooftop tent", "Tonneau", "Trade-off"],
  "rows": [
   ["Full overland system", "Putco Venture TEC", "Tent, awning, recovery gear", "Yes (1,000 lb static)", "Most inside-rail roll-ups", "Highest price"],
   ["Mid-height overland", "RealTruck GoRack", "Tent, MOLLE gear", "Yes (1,000 lb static)", "T-slot rail covers", "5.5 ft listing"],
   ["Aluminum budget rack", "Rough Country 10406", "Tent, ladders, gear", "Yes (750 lb static)", "Check the listing", "5'7\" bed only"],
   ["Mid-height bars", "Putco Venture TEC Quick Rack", "Bikes, boards, ladders", "Check with Putco", "Roll-ups; not most hard folders", "Separate part per bed"],
   ["Clamp towers", "Yakima OverHaul HD / OutPost HD", "Changing loads, 8 ft beds", "Yes (500 lb on-road)", "With Tonneau Kit 1", "Crossbars extra"],
  ],
 },
 "picks": [
  {"asin": "B07VRF2J2Q", "role": "Best overall", "price": "About $2,069–$2,399",
   "pros": ["1,000 lb static / 600 lb dynamic / 300 lb off-road", "One part for 2015–2027 5'7\" beds, incl. Raptor", "6061-T6 aluminum, CNC-bent to the cab", "No-drill stake pocket mounts", "Four tent brackets included"],
   "cons": ["Highest price on this page", "5.5 ft box only", "Finish coverage is shorter than the structural warranty"],
   "body": "The Venture TEC is the strongest rack on this page and one of the few that covers the whole 13th generation with a single part. Putco lists 184100 for 2015–2027 F-150 5'7\" beds, including the 2017–2027 Raptor, so a 2016 XLT and a 2019 Raptor buy the same rack, and it will move to a 2021-or-later short-box truck. Putco rates it at 1,000 lb static, 600 lb dynamic and 300 lb off-road dynamic. The off-road figure is the one to watch on a Raptor that sees real trails. The frame is 6061-T6 aluminum in a matte black powder coat, CNC-bent to follow the cab contour, and it bolts into the stake pockets with no drilling.\n\nPutco includes four tent brackets and a dual T-slot rail for third-party accessories, and it says the rack works with most inside-rail roll-up covers. The cost is high: Putco's site showed $2,068.89 on sale in September 2026, down from $2,980.78, and RealTruck lists the line from $2,398.99. On an older truck, weigh that against the truck's remaining life, though the carry-over fitment softens the blow. Putco describes a limited lifetime warranty with shorter finish coverage, so read those terms.",
   "who": "Short-box and Raptor owners who want the highest published ratings and a rack that can move to their next F-150.",
   "specs": [["Part", "Putco 184100"], ["Fits", "2015–2027 F-150 5'7\" bed, incl. Raptor (per Putco)"], ["Material", "6061-T6 aluminum"], ["Load rating", "1,000 lb static / 600 lb dynamic / 300 lb off-road"], ["Mounting", "Stake pockets, no drilling"], ["Included", "4 tent brackets"], ["Tonneau", "Most inside-rail roll-ups"], ["Price", "$2,068.89 sale (Putco); from $2,398.99 (RealTruck)"]]},
  {"asin": "B0CNS9P8RQ", "role": "Best value for a tent", "price": "$1,089.99",
   "pros": ["1,000 lb static / 600 lb dynamic", "Listing covers 2015–2024 5.5 ft beds", "T-slots on all four sides", "Integrated MOLLE side panels", "Stake pocket or utility rail mount"],
   "cons": ["5.5 ft box only", "No off-road rating on the page read", "Height not published on RealTruck's page"],
   "body": "RealTruck's GoRack is the pick for tent owners who want strong numbers without the Putco's price. RealTruck rates it at 1,000 lb static and 600 lb dynamic, the same pair of figures, and lists it at $1,089.99. The Amazon listing is part 9250101 for the 2015–2024 F-150 5.5 ft bed, which covers the whole 13th generation and carries over to later short-box trucks. It uses aluminum and steel, with extruded side rails that have T-slots on all four sides and integrated MOLLE side panels for fuel packs, traction boards, a jack and tools.\n\nMounting suits this truck well. RealTruck says the GoRack mounts directly to the stake pockets or to a utility rail, so it works on trucks with or without Ford's bed track, and it is compatible with covers that use a T-slot rail system. RealTruck backs it with a limited lifetime warranty. What's missing is an off-road figure and a published height on the page we read, so if you run rough trails or need a specific clearance for a tent, ask the seller before ordering. Remember it is a 5.5 ft part only.",
   "who": "5.5 ft box owners who want tent-grade ratings and built-in MOLLE storage at about half the Putco's price.",
   "specs": [["Part", "RealTruck GoRack 9250101"], ["Fits", "2015–2024 F-150 5.5 ft bed (per listing)"], ["Material", "Aluminum and steel"], ["Load rating", "1,000 lb static / 600 lb dynamic"], ["Mounting", "Stake pockets or utility rail"], ["Extras", "T-slots on four sides, MOLLE panels"], ["Warranty", "Limited lifetime"], ["Price", "$1,089.99 (RealTruck)"]]},
  {"asin": "B0C7D1PDYD", "role": "Best budget", "price": "$499.95",
   "pros": ["750 lb static / 400 lb dynamic", "Powder-coated aluminum", "Listed for 2015–2026 incl. 2017+ Raptor", "Configurable height; half-height version listed", "Lifetime warranty per Rough Country"],
   "cons": ["5'7\" bed only", "Nutsert install; a nutsert tool is recommended", "Not compatible with Rough Country's hard-shell rooftop tent"],
   "body": "At $499.95, the Rough Country 10406 is the cheapest rack here with published static and dynamic ratings: 750 lb static and 400 lb dynamic. It is powder-coated aluminum with molded end caps and T-slot covers, and Rough Country says it keeps rear visibility and offers endless mounting adjustability. Rough Country lists it for the 2015–2026 F-150, including the 2017–2026 Raptor, so it also carries over to a newer short-box truck. The height is configurable, and a half-height version has its own Amazon listing.\n\nThere are trade-offs to check before ordering. Rough Country says the rack only fits models with the 5'7\" bed. The install uses nutserts, with a nutsert tool recommended, so read the instructions to see whether your truck needs any holes in the aluminum bed. Rough Country also says the rack doesn't work with its own hard-shell rooftop tent, so compare your tent's mounting footprint to the rack's bars. For a budget rack that still publishes a dynamic figure, it is the clear choice on the short box.",
   "who": "Short-box owners who want a rated aluminum rack for ladders, gear or a light tent for about $500.",
   "specs": [["Part", "Rough Country 10406"], ["Fits", "2015–2026 F-150 5'7\" bed, incl. Raptor (per Rough Country)"], ["Material", "Powder-coated aluminum"], ["Load rating", "750 lb static / 400 lb dynamic"], ["Height", "Configurable"], ["Mounting", "Nutserts; nutsert tool recommended"], ["Warranty", "Lifetime (per Rough Country policy)"], ["Price", "$499.95 (Rough Country)"]]},
  {"asin": "B0C2SCFWHH", "role": "Best for the 6.5 ft bed", "price": "From $1,051.99",
   "pros": ["Made for the 2015–2020 6'7\" box", "Crossbars about 13 in above the bed", "No-drill stake pocket install", "Works with many roll-up covers", "Made in the USA; limited lifetime warranty"],
   "cons": ["Remove it to open hard folders like BAKFlip and Gator FX", "Not for many tri-fold and retractable covers", "Capacity not split into static and dynamic"],
   "body": "Most one-piece racks skip the 6.5 ft bed, which makes Putco's Venture TEC Quick Rack for the 2015–2020 6'7\" box worth knowing about. RealTruck puts the cross rails 9 in above the side rails, about 13 in above the bed, a mid height that suits bikes, boards and ladders, and possibly a light tent. It is 6061-T6 aluminum with a textured matte black coat, bolts to the stake pockets without drilling, uses removable, adjustable crossbars and uprights, and has dual T-slot rails. RealTruck gives it a 1,000 lb capacity, starts it at $1,051.99 and lists a limited lifetime warranty.\n\nNote that Putco splits the Quick Rack by generation: this 2015–2020 6'7\" part is separate from the 2021–2025 versions, so it won't follow you to a newer truck the way the 184100 can. On covers, RealTruck says it works with roll-ups such as the BAK Revolver and Extang Revolution, but must be removed to operate hard folders like the BAKFlip and Gator FX. RealTruck doesn't split the 1,000 lb figure into static and dynamic, so confirm a moving rating with Putco before loading a tent.",
   "who": "6.5 ft bed owners with a roll-up cover who want a mid-height rack for bikes, boards and ladders.",
   "specs": [["Type", "Mid-height rack"], ["Fits", "2015–2020 F-150 6'7\" bed (per listing)"], ["Height", "Cross rails about 13 in above the bed"], ["Material", "6061-T6 aluminum"], ["Capacity", "1,000 lb (RealTruck; no static/dynamic split)"], ["Mounting", "Stake pockets, no drilling"], ["Tonneau", "Roll-ups; remove for hard folders"], ["Price", "From $1,051.99 (RealTruck)"]]},
  {"asin": "B07MDSP8T8", "role": "Best for 8 ft beds", "price": "$1,200 (towers)",
   "pros": ["Adjusts from 19 to 30 in", "500 lb on-road / 300 lb off-road", "Works by bed rail, not by bed length", "Track Kit and Tonneau Kit options", "Limited lifetime warranty"],
   "cons": ["Towers only; crossbars cost extra", "59.52 lb before crossbars", "Universal fit; confirm the F-150 kit with Yakima"],
   "body": "Work trucks with the 8 ft box have few one-piece rack options, and Yakima's OverHaul HD solves that by clamping to the bed rails rather than matching a bed length. The four towers adjust from 19 to 30 in, so they can carry ladders or kayaks just above the cab or raise a tent well above it. Yakima rates the system at 500 lb on-road and 300 lb off-road, lists the towers at 59.52 lb and $1,200, and backs them with a limited lifetime warranty. They also move between trucks, which suits owners likely to replace an older F-150.\n\nAdd the crossbars to the budget: Yakima's HD Bar comes in 60, 68 and 78 in lengths and is sold separately. Yakima says tracked beds need Track Kit 1 or 2, which applies if your truck has Ford's bed utility track, and select tonneau covers need Tonneau Kit 1. The product page doesn't name the F-150, so run your bed and cover through Yakima's fit lookup before ordering, and torque the clamps to spec on the aluminum bed rails.",
   "who": "8 ft and 6.5 ft bed owners, and anyone who wants an adjustable rack that moves to the next truck.",
   "specs": [["Type", "Adjustable clamp towers"], ["Height", "19–30 in"], ["Load rating", "500 lb on-road / 300 lb off-road"], ["Weight", "59.52 lb (towers)"], ["Mounting", "Bed rail clamps; Track Kit 1/2 for tracked beds"], ["Tonneau", "Tonneau Kit 1 for select covers"], ["Crossbars", "HD Bar 60/68/78 in, sold separately"], ["Price", "$1,200 towers (Yakima)"]]},
  {"asin": "B07MRHDLS4", "role": "Best lightweight mid height", "price": "$799 (towers)",
   "pros": ["Fixed 13 in height", "500 lb on-road / 300 lb off-road", "Only 44.09 lb for the towers", "Fits any bed length with the right bars", "Limited lifetime warranty"],
   "cons": ["Crossbars extra", "Universal fit; confirm the F-150 kit with Yakima", "Much lower static capacity than the Putco or GoRack"],
   "body": "Yakima's OutPost HD is the lighter, cheaper route to a brand-name rack on any 13th-gen bed. The four towers sit at a fixed 13 in and are rated 500 lb on-road and 300 lb off-road. Yakima lists them at 44.09 lb and $799, with a limited lifetime warranty, and you add HD Bar crossbars in 60, 68 or 78 in lengths. Because the towers clamp to the bed rails, the same set works on the 5.5, 6.5 or 8 ft box, and it moves to a later truck without a new part number.\n\nAs with the OverHaul HD, Yakima says tracked beds need Track Kit 1 or Track Kit 2 and select tonneau covers need Tonneau Kit 1. Its page doesn't name the F-150, so confirm the kit and bar length with Yakima's fit lookup before buying. Thirteen inches is a mid height, so a tent may sit close to the cab roof; check that it can open without touching the cab. For a heavy tent with two sleepers, the higher static ratings of the Putco and GoRack are the safer choice.",
   "who": "Owners who want a light, brand-name mid-height rack for bikes, boats and gear on any bed length.",
   "specs": [["Type", "Fixed-height clamp towers"], ["Height", "13 in"], ["Load rating", "500 lb on-road / 300 lb off-road"], ["Weight", "44.09 lb (towers)"], ["Mounting", "Bed rail clamps; Track Kit 1/2 for tracked beds"], ["Tonneau", "Tonneau Kit 1 for select covers"], ["Warranty", "Limited lifetime"], ["Price", "$799 towers (Yakima)"]]},
 ],
 "install": [
  "Measure the bed at the rail from the bulkhead to the closed tailgate (about 67, 79 or 98 in) and buy the rack part for that box.",
  "Check for stake pockets, BoxLink cleats and Ford's bed utility track, and use the mounting hardware or track kit the rack maker specifies.",
  "If you run a tonneau cover, fit it first and confirm it's on the rack's compatible list, or order the maker's tonneau kit.",
  "Set the rack, square it to the cab, and center it side to side before tightening any fastener.",
  "Torque bolts and clamps to the maker's figures; on the aluminum bed, don't over-tighten clamps on the rail edge.",
  "Fit crossbars and tent brackets, check clearance to the cab and tailgate, and confirm the third brake light is visible from behind.",
  "Recheck every fastener after the first drive and after trail use, and keep the load under the dynamic or off-road rating.",
 ],
 "avoid": [
  {"h": "Ordering by cab", "body": "A SuperCab can have a 6.5 or 8 ft box, and every Raptor has the 5.5 ft box. Measure the bed and buy for it."},
  {"h": "Hanging a tent on BoxLink brackets", "body": "Owners describe BoxLink as mainly a tie-down system. For a tent load, use a rack that bolts into the stake pockets."},
  {"h": "Loading to the static number on the road", "body": "Static is parked only. Stay under 600 lb dynamic on the Putco and GoRack, 400 lb on the Rough Country, and 500 lb on-road on the Yakima towers."},
  {"h": "Forgetting the hard-folding cover", "body": "The Putco Quick Rack has to be removed to open a BAKFlip or Gator FX. Match the cover and rack before buying."},
 ],
 "verdict": {
  "thesis": "Buy for the box length first: the Putco Venture TEC for the strongest short-box rack, the GoRack for tent ratings at half the price, the Rough Country 10406 on a budget, and Putco's Quick Rack or Yakima towers for longer beds.",
  "body": "On the 5.5 ft box and every 2017–2020 Raptor, the Putco Venture TEC has the best published ratings and will move to a newer truck, the GoRack matches its static and dynamic figures for less, and the Rough Country 10406 is the rated budget rack. The 6.5 ft box gets Putco's 2015–2020 Quick Rack, and 8 ft work trucks are best served by Yakima's OverHaul HD or OutPost HD. Use the stake pockets rather than BoxLink for heavy loads, and count everything against payload.\n\nIf the truck is turning into a camping rig, pair the rack with a tonneau cover that suits it, and look at a trailer hitch and floor liners while you're outfitting it. Owners of the newer 2021–2026 F-150 should shop that truck's rack list, since some parts split at 2021. The vehicle hub lists every fit-checked accessory for your F-150.",
 },
 "sources": [
  ["Putco Venture TEC Rack 184100, F-150 5'7\" bed (Putco)", "https://www.putco.com/product/venture-tec-rack/184100/"],
  ["Putco Venture TEC Rack (RealTruck)", "https://realtruck.com/p/putco-venture-tec-rack/"],
  ["Putco Venture TEC Quick Rack (RealTruck)", "https://realtruck.com/p/putco-venture-tec-quick-rack/"],
  ["RealTruck GoRack (RealTruck)", "https://realtruck.com/p/realtruck-gorack/"],
  ["Rough Country Bed Rack 10406 (Rough Country)", "https://www.roughcountry.com/product/configurable/ford-bed-rack-10406"],
  ["Yakima OverHaul HD towers (Yakima)", "https://yakima.com/products/overhaul-hd"],
  ["Yakima OutPost HD towers (Yakima)", "https://yakima.com/products/outpost-hd"],
  ["Bed rack using BoxLink cleats (F150Forum)", "https://www.f150forum.com/f118/bed-rack-using-boxlink-cleats-500089/"],
  ["Ford F-Series 13th generation (Wikipedia)", "https://en.wikipedia.org/wiki/Ford_F-Series_(thirteenth_generation)"],
 ],
}

# Product list for this page. (asin, name, brand, band, cond, note)
FITS = [
 ("B07VRF2J2Q","Putco Venture TEC Rack, Ford F-150 2015-2027 5'7\" Bed","Putco","$2,000–$2,400",{"bed_length_in":66},"5.5 ft bed incl. 2017-2020 Raptor; 1,000/600/300 lb."),
 ("B0CNS9P8RQ","RealTruck GoRack Overland Truck Rack 9250101, 2015-2024 Ford F-150 5.5' Bed","RealTruck","$1,000–$1,150",{"bed_length_in":66},"5.5 ft bed; 1,000 lb static / 600 lb dynamic."),
 ("B0C7D1PDYD","Rough Country Aluminum Bed Rack 10406, 2015-2023 Ford F-150","Rough Country","$450–$550",{"bed_length_in":66},"5'7\" bed only; 750 lb static / 400 lb dynamic."),
 ("B0C2SCFWHH","Putco Venture TEC Quick Rack, Ford F-150 2015-2020 6'7\" Bed","Putco","$1,000–$1,200",{"bed_length_in":78},"6.5 ft bed; remove to open hard-folding covers."),
 ("B07MDSP8T8","Yakima OverHaul HD Adjustable Truck Bed Rack (towers only)","Yakima","$1,100–$1,250",{},"Universal clamp towers; confirm F-150 track kit and crossbar length in Yakima's fit lookup."),
 ("B07MRHDLS4","Yakima OutPost HD Fixed Mid Height Truck Bed Rack (towers only)","Yakima","$750–$850",{},"Universal clamp towers; confirm F-150 track kit and crossbar length in Yakima's fit lookup."),
 ("B0DC13ST7Y","Rough Country Aluminum Bed Rack, Ford F-150 2015-2024, Half Height","Rough Country","$450–$550",{"bed_length_in":66},"Half-height configuration; 5'7\" bed."),
 ("B08L3KT9XJ","Hooke Road Overland Bed Rack, 2009-2021 Ford F-150 & Raptor","Hooke Road","Check listing",{},"Budget rack; load rating and bed length not verified — confirm on listing."),
]
