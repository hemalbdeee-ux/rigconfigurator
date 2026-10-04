"""Long-form article — Best Rooftop Cargo Boxes for 2021–2026 Chevrolet Tahoe (5th gen, T1).
Mirrors the approved cargo-box pages (RAV4, Telluride). No invented hands-on testing: box specs come from Yakima,
Thule, Rhino-Rack, SportRack and etrailer pages fetched 2026-09-27; vehicle facts from db/migrations/003_vehicles.sql
plus etrailer's Tahoe roof guide, The Rack Shop kits, Cars.com (76 in height), KBB and Wikipedia.
Roof: flush side rails, as stored in 003_vehicles.sql and listed by etrailer and The Rack Shop (Z71 has its own fit
kit). Roof load limit not verified: owner's manual.
Source fixes 2026-10-04: removed the stale raised-rails remarks (docstring, look_for); verdict no longer points to a
Tahoe roof rack page that is not published; added the RST Performance Edition "Removes roof rack" exception from
Edmunds' 2025 trim page (fit_table, look_for, sources). Wikipedia's "largest SUV in the full-size length segment"
wording was re-read and the FAQ claim kept as attributed.
"""

KEY = ("chevrolet", "tahoe", "2021-present", "cargo-boxes")

TITLE = "Best Rooftop Cargo Boxes for 2021–2026 Chevy Tahoe: 7 Picks for a 76-Inch-Tall SUV"
META = ("Six Yakima, Thule, Rhino-Rack and SportRack boxes plus crossbars for the 5th-gen Tahoe: flush rails, Z71 fit "
        "kits, loading height and garage clearance.")

FAQ = [
 ("Does the 2021–2026 Tahoe have raised rails or flush rails?",
  "Retailer fit guides list the fifth-generation Tahoe with flush-mounted side rails that run front to back, not raised rails with a gap underneath. etrailer shows only that roof type for the 2021 Tahoe, and The Rack Shop sells separate flush-rail kits for the regular Tahoe and for the Z71, which uses its own Thule fit kit. Buy crossbar feet made for flush rails and listed for your trim; raised-rail towers won't clamp on."),
 ("What is the roof weight limit on a 2021–2026 Tahoe?",
  "We couldn't confirm a published Chevrolet figure, so check the roof-load section of your owner's manual. The crossbar kits give a working ceiling: The Rack Shop's Yakima and Thule flush-rail kits for the Tahoe are rated at 165 lb, and etrailer lists the Thule flush-rail feet at 165 lb even though the WingBar Evo bars are rated at 220 lb. Use the lowest of the manual, feet and bar figures, and count bars, box and cargo against it."),
 ("Will a Tahoe with a roof box fit in my garage?",
  "Almost certainly not through a standard 7 ft door. Cars.com lists the 2021 Tahoe at 76 in tall, and the boxes here add 15 in (SkyBox 16) to 19 in (SportRack Vista XL) on top of the crossbars, so even the lowest box puts the top past 91 in before you count the bars. An 8 ft door may work with a low box, but measure the Tahoe with bars fitted and add the box height first. Watch parking garages and drive-thrus too."),
 ("How do I load a roof box on a vehicle this tall?",
  "Pick a dual-side opening box so you can load from either side, and use a sturdy step stool or step on the door sill. Put light, bulky items in the far side of the box first and heavy items in the middle between the bars. A rear-opening box like the SportRack Vista XL means reaching up and over the back of a 76 in roof, which is hard without a ladder. Running boards help with reach on the sides."),
 ("What size cargo box fits a Tahoe?",
  "The Tahoe's long roof suits the biggest boxes: the Yakima CBX XXL (91 in, 21.5 cu ft) and Thule Motion 3 XXL (91.3 in, 21 cu ft) both fit lengthwise. The limit is weight, not space. Both boxes weigh over 57 lb, and the kits we found are rated at 165 lb, so a 21 cu ft box can take only about 90 lb of gear. A 16 cu ft box like the GrandTour 16 leaves more room for cargo."),
 ("Does the Z71 need different crossbars?",
  "Yes, per The Rack Shop, which sells a separate Thule flush-rail setup for the 2021–2026 Tahoe Z71 using Thule Fit Kit 186117, rated at 165 lb, with a maximum bar spread of 58 in. The regular flush-rail Tahoe uses a different fit kit (etrailer lists TH95JW). Match the fit kit to your trim; the box itself clamps to any of them."),
 ("Does a Tahoe box fit a Suburban?",
  "Yes. Boxes clamp to crossbars, not to the vehicle, and our fitment data notes that the Suburban shares the Tahoe's roof and hitch fit. The Suburban's longer body gives even more room between the box and the liftgate. Buy crossbars listed for your exact vehicle and year, and check its owner's manual for the roof figure."),
 ("How far apart should the crossbars be?",
  "Every box publishes a range. Yakima lists 24–38 in for the CBX XXL, 24–36 in for the GrandTour 16 and 24–34.5 in for the SkyBox 16. etrailer gives 21-13/16 to 36-9/16 in for the Thule Motion 3, Rhino-Rack gives 620–930 mm for the MasterFit 440L, and the SportRack Vista XL mounts at 25-7/8, 27-7/8 or 29-7/8 in. On the Tahoe's flush rails, the bars slide, so you can usually match any of them."),
 ("Will a roof box hit the Tahoe's liftgate?",
  "Rarely, if you mount it forward. The Tahoe is 210.7 in long, the largest in its segment per Wikipedia, and its long roof gives even a 91 in box room ahead of the liftgate. Thule lists a front-clearance figure of more than 54 13/16 in for the Motion 3 XXL; measure that on your Tahoe, mount the box forward and open the liftgate slowly the first time."),
 ("Should I use a roof box or a hitch cargo carrier on a Tahoe?",
  "Our fitment data lists a Class IV, 2 in receiver and an 8,400 lb tow rating on the fifth-gen Tahoe, so a hitch cargo carrier is easy to add and keeps heavy items low and reachable. On a vehicle this tall, that is a big advantage: nobody climbs a step stool to reach a cooler. The roof box is better for soft, bulky gear that you load once per trip, and it keeps the liftgate and rear camera clear."),
]

ARTICLE = {
 "dek": "Seven picks for the fifth-generation Tahoe: six rooftop boxes from Yakima, Thule, Rhino-Rack and SportRack, from a 63 in budget box to two 21 cu ft giants, plus crossbars listed for the Tahoe. For each box we list volume, length, weight, height and crossbar spread, and what they mean on a 76 in tall SUV with flush rails, where loading height and garage clearance matter as much as volume.",
 "author": "jake-morrison",
 "reviewed": "2026-09-27",
 "method": "We did not mount these boxes ourselves. We ranked them on the makers' published specs (Yakima, Thule, Rhino-Rack and SportRack: volume, exterior dimensions, box weight, load rating, crossbar spread, ski length, front clearance), on etrailer's figures for the Thule and SportRack boxes and its Tahoe roof guide, on The Rack Shop's Tahoe crossbar kits, and on vehicle dimensions from Cars.com, KBB and Wikipedia. Prices were checked on the makers' stores and retailers in September 2026. Amazon prices move daily, so the button shows the live price.",
 "takeaways": [
  "**Flush rails, not raised.** etrailer and The Rack Shop list the 2021+ Tahoe with flush rails; the Z71 takes its own Thule fit kit. Buy flush-rail feet listed for your trim.",
  "**Crossbar kits cap you at 165 lb.** The Yakima and Thule flush-rail kits we found are rated at 165 lb. Confirm the roof figure in your owner's manual and use the lowest number.",
  "**Height is the real constraint.** At 76 in tall, a Tahoe with any box won't clear a standard 7 ft garage door. Measure before the first trip home.",
  "**The long roof takes a giant box.** The Yakima CBX XXL and Thule Motion 3 XXL fit lengthwise, but at 57–65 lb they leave only about 90 lb or less for gear.",
  "**Load from the side.** Dual-side opening and a step stool beat a rear-opening lid on a roof this high.",
 ],
 "top_picks": [
  {"asin": "B083KP48XC", "role": "Best overall", "why": "16 cu ft, 51.5 lb, dual-side, 24–36 in spread; leaves weight for gear"},
  {"asin": "B0F3LF5P6D", "role": "Biggest box", "why": "Yakima CBX XXL: 21.5 cu ft, 215 cm skis, 24–38 in spread"},
  {"asin": "B001PUZXGK", "role": "Lowest 16 cu ft", "why": "SkyBox 16: 15 in tall, 47 lb, $599 on sale"},
  {"asin": "B07B4P7WYX", "role": "Lightest", "why": "Rhino-Rack MasterFit 440L: 38.6 lb, 165 lb rating, 5-year warranty"},
  {"asin": "B0FK4RLXN3", "role": "Budget crossbars", "why": "Listed for 2021–2026 Tahoe, Suburban, Yukon XL, Escalade ESV"},
 ],
 "fit_table": {
  "caption": "2021–2026 Tahoe roof setups (what the box mounts to)",
  "head": ["Trim", "Rails", "Crossbar notes", "Box notes"],
  "rows": [
   ["LS, LT, RST, Premier, High Country", "Flush rails front to back (etrailer, The Rack Shop)", "Flush-rail kits: Thule Evo Flush Rail + fit kit TH95JW, Yakima SightLine; 165 lb", "Bars slide on the rails; set inside the box's spread"],
   ["Z71", "Flush rails, own fit kit", "Thule Fit Kit 186117 setup: 165 lb, 58 in max bar spread (The Rack Shop)", "Same boxes"],
   ["RST with the Performance Edition package", "Edmunds' 2025 trim page: the package \"Removes roof rack\"; we could not confirm whether the side rails stay", "Look at the roof before ordering feet; ask the dealer what is fitted", "A box needs crossbars first"],
   ["Suburban (same generation)", "Shares roof fit (our data)", "Bars listed for Suburban", "Same boxes, more liftgate room"],
   ["All 2021–2026", "Roof figure: check the owner's manual", "Kits we found: 165 lb", "Bars + box + gear under the lowest figure"],
   ["Height", "76 in (Cars.com, 2021)", "Bars add height", "Box adds 15–19 in; no standard 7 ft garage"],
  ],
 },
 "look_for": [
  {"h": "Flush rails and trim-specific fit kits",
   "body": "The retailers who fit racks to the fifth-gen Tahoe list flush-mounted side rails that run front to back, with no gap underneath for a strap-style tower. etrailer shows only that roof type for the 2021 Tahoe, with a Thule setup of WingBar Evo bars, Evo Flush Rail feet and fit kit TH95JW. The Rack Shop sells separate flush-rail kits for the regular Tahoe and the Z71, whose Thule setup uses Fit Kit 186117. Buy feet made for flush rails and a fit kit listed for your trim; every box here clamps to the bars once they're on. One exception to check: Edmunds' 2025 trim page says the RST Performance Edition package \"Removes roof rack\". We could not confirm whether the side rails stay on that package, so look at the roof before ordering feet."},
  {"h": "165 lb kits and the missing roof figure",
   "body": "We couldn't confirm a published Chevrolet roof figure for this generation, so read the roof-load section of your owner's manual before loading anything. The crossbar kits set a working ceiling in the meantime. The Rack Shop's Yakima and Thule flush-rail kits for the Tahoe are rated at 165 lb, and etrailer lists the Thule flush-rail feet at 165 lb even though the WingBar Evo bars are rated at 220 lb. The feet decide it. The boxes here weigh 38.6 lb (MasterFit 440L) to 65 lb (CBX XXL), so after the bars you may have as little as 90 lb or less for gear."},
  {"h": "Loading height on a 76 in roof",
   "body": "Cars.com lists the 2021 Tahoe at 76 in tall, and the box sits on top of that and the crossbars. Reaching the far side of a 38 in wide box from the ground is not realistic for most people, so dual-side opening matters more on a Tahoe than on a smaller SUV: open the box from whichever side you're standing on. A sturdy step stool, or standing on the door sill, puts the lid at chest height. Rear-opening boxes like the SportRack Vista XL mean reaching over the back of the roof, which is hard on a vehicle this tall."},
  {"h": "Garage and parking-structure clearance",
   "body": "This is the Tahoe's biggest roof-box gotcha. At 76 in tall, the vehicle plus even the lowest box here (15 in for the SkyBox 16) is past 91 in before you count the crossbars, which is well over a standard 7 ft (84 in) garage door. The other boxes add 17 in (CBX XXL, MasterFit 440L), about 18 in (GrandTour 16, Motion 3 XXL) or 19 in (Vista XL). An 8 ft door might work with a low box, but measure the Tahoe with bars fitted, add the box height, and put a note on the dash so nobody drives into the garage with the box on."},
  {"h": "Using the long roof without overloading it",
   "body": "The Tahoe is 210.7 in long, and its roof has room for the biggest boxes on the market: the Yakima CBX XXL at 91 in and the Thule Motion 3 XXL at 91.3 in both fit ahead of the liftgate if mounted forward. The trap is weight. Those boxes weigh 65 lb and 57.2 lb, and with a 165 lb kit rating and the bars counted, they have far less weight budget than space. Fill a 21 cu ft box with sleeping bags, jackets and soft duffels; put coolers and bins on a hitch carrier or inside the cargo area."},
 ],
 "look_table": {
  "head": ["Feature", "Look for", "Avoid"],
  "rows": [
   ["Crossbars", "Flush-rail feet with a fit kit for your trim (Z71 has its own)", "Raised-rail towers on flush rails"],
   ["Height", "Low boxes (15 in SkyBox 16) if you use 8 ft doors or garages", "Any box through a standard 7 ft door"],
   ["Opening", "Dual-side, so you load from either side with a step stool", "Rear-only lids on a 76 in roof"],
   ["Box weight", "Under 52 lb to keep gear weight inside a 165 lb kit rating", "Filling a 65 lb 21.5 cu ft box with heavy gear"],
   ["Crossbar spread", "A range your sliding bars can meet (24–38 in for the CBX XXL)", "Buying before checking the kit's max spread"],
   ["Warranty", "Limited lifetime (Yakima, Thule Motion 3) or 5 years (Rhino-Rack)", "No terms stated; ask the seller"],
  ],
 },
 "types_table": {
  "caption": "Box sizing for the Tahoe (makers' published specs; Thule spread and SportRack positions per etrailer)",
  "head": ["Box", "Volume", "L × W × H", "Box weight", "Crossbar spread", "Height note on a 76 in Tahoe"],
  "rows": [
   ["Yakima GrandTour 16", "16 cu ft", "79 × 35 × 18 in", "51.5 lb", "24–36 in", "Past 94 in before bars"],
   ["Yakima CBX XXL", "21.5 cu ft", "91 × 38 × 17 in", "65 lb", "24–38 in", "Past 93 in before bars"],
   ["Yakima SkyBox 16 Carbonite", "16 cu ft", "81 × 36 × 15 in", "47 lb", "24–34.5 in", "Lowest here: past 91 in before bars"],
   ["Rhino-Rack MasterFit 440L", "15.5 cu ft", "76 × 32 × 17 in", "38.6 lb", "620–930 mm (about 24.4–36.6 in)", "Past 93 in before bars"],
   ["Thule Motion 3 XXL", "21 cu ft", "91.3 × 36.2 × 18.1 in", "57.2 lb", "21-13/16 to 36-9/16 in", "Past 94 in before bars"],
   ["SportRack Vista XL", "18 cu ft", "63 × 38 × 19 in", "Not published", "Fixed at 25-7/8, 27-7/8 or 29-7/8 in", "Tallest: past 95 in before bars"],
  ],
 },
 "picks": [
  {"asin": "B083KP48XC", "role": "Best overall", "price": "$709",
   "pros": ["16 cu ft at 51.5 lb, leaving weight for gear under a 165 lb kit", "Dual-side opening for loading from either side", "18 in deep for bulky family gear", "24–36 in spread suits sliding flush-rail bars", "Limited lifetime warranty; made in the USA"],
   "cons": ["18 in tall, so a Tahoe with it on is past 94 in before bars", "Smaller than the 21 cu ft boxes the roof can hold", "About $110 more than the SkyBox 16"],
   "body": "On a Tahoe, the best box isn't the biggest one the roof can hold. It's the one that leaves weight for gear. The Yakima GrandTour 16 does that. Yakima lists it at 79 x 35 x 18 in with 16 cu ft and 51.5 lb, with dual-side opening, skis and boards up to 185 cm, SKS locks, a removable torque-limiting knob and a limited lifetime warranty, made in the USA, at $709. The deep 18 in shell swallows camp chairs, strollers and soft duffels.\n\nThe fit works well on the Tahoe's flush rails. Bars on those rails slide, so the 24–36 in spread range is easy to meet, and at 79 in the box sits far forward of the liftgate on a 210.7 in long SUV. Against the 165 lb rating of the flush-rail kits we found, the box and bars leave roughly 100 lb for gear, more than the 21 cu ft boxes can. Dual-side opening is the other reason to choose it: on a 76 in roof you load from whichever side you're standing, with a step stool. The cost is height. At 18 in, the Tahoe with this box on is past 94 in before the bars, so it won't go through a standard garage door.",
   "who": "Tahoe families who want a big, easy-loading box without using up the weight budget.",
   "specs": [["Volume", "16 cu ft"], ["Exterior", "79 × 35 × 18 in"], ["Box weight", "51.5 lb"], ["Crossbar spread", "24–36 in"], ["Opening", "Dual-side"], ["Ski length", "Up to 185 cm"], ["Lock", "SKS locks included"], ["Warranty", "Limited lifetime"]]},
  {"asin": "B0F3LF5P6D", "role": "Biggest box", "price": "$1,149 (sale; regular $1,499.99)",
   "pros": ["21.5 cu ft, the most volume here", "Skis and boards up to 215 cm", "24–38 in spread, the widest Yakima range here", "Dual-side opening, SKS locks, internal tie-downs", "Made in the USA; limited lifetime warranty"],
   "cons": ["65 lb, the heaviest box here", "At a 165 lb kit rating, well under 100 lb left for gear", "91 in long and 38 in wide"],
   "body": "The Tahoe's long roof is one of the few that can take a box the size of the Yakima CBX XXL without crowding the liftgate. Yakima lists it at 91 x 38 x 17 in with 21.5 cu ft, skis and boards up to 215 cm, dual-side opening, internal tie-down points, SKS locks and a removable torque-limiting knob. It is made in the USA with a limited lifetime warranty, and Yakima had it at $1,149 on sale (regular $1,499.99) when we checked. Its 24–38 in spread range is the widest of the Yakima boxes here and easy to meet with bars that slide on flush rails.\n\nThe number to plan around is 65 lb. That is the box alone, and with the flush-rail kits we found rated at 165 lb, box plus bars leaves well under 100 lb for gear. So this is a box for volume, not weight: sleeping bags, jackets, long skis and soft duffels for a full crew. Mount it forward, where the Tahoe's length gives it plenty of room ahead of the liftgate. At 17 in tall it is lower than the GrandTour 16 but still puts the Tahoe past 93 in before bars. Confirm the roof figure in your manual before loading it.",
   "who": "Ski crews and big families who need the most space and will pack it light.",
   "specs": [["Volume", "21.5 cu ft"], ["Exterior", "91 × 38 × 17 in"], ["Box weight", "65 lb"], ["Crossbar spread", "24–38 in"], ["Ski length", "Up to 215 cm"], ["Opening", "Dual-side"], ["Lock", "SKS locks included"], ["Warranty", "Limited lifetime"]]},
  {"asin": "B001PUZXGK", "role": "Lowest 16 cu ft", "price": "$599",
   "pros": ["15 in tall, the lowest box here", "47 lb for 16 cu ft", "$599 on sale at Yakima (regular $749)", "Dual-side opening with SuperLatch and SKS locks", "No-assembly install; limited lifetime warranty"],
   "cons": ["Still past 91 in on a Tahoe before bars", "24–34.5 in spread is the narrowest Yakima range here", "36 in wide, filling most of the bars"],
   "body": "Height is the Tahoe's biggest roof-box problem, and the SkyBox 16 Carbonite is the lowest full-size box here. Yakima lists it at 81 x 36 x 15 in with 16 cu ft and 47 lb, with dual-side opening, SuperLatch security, SKS locks, skis and boards up to 185 cm and a limited lifetime warranty. It installs without assembly and fits most crossbars, including factory bars. It was on sale for $599 (regular $749) on Yakima's store when we checked, and Yakima builds it in the USA with up to 80% recycled material.\n\nThose 3 in less than the GrandTour 16 won't get a boxed Tahoe through a 7 ft door, but they can matter at an 8 ft door, a tall parking structure or a hotel entrance. Measure the Tahoe with bars fitted and add 15 in. At 47 lb, it also leaves a little more of a 165 lb kit rating for gear, roughly 100 lb after the bars. Its 24–34.5 in spread suits the sliding bars on the Tahoe's flush rails, and dual-side opening lets you load from either side from a step stool.",
   "who": "Tahoe owners who need the lowest full-size box for tall doors and parking structures.",
   "specs": [["Volume", "16 cu ft"], ["Exterior", "81 × 36 × 15 in"], ["Box weight", "47 lb"], ["Crossbar spread", "24–34.5 in"], ["Opening", "Dual-side"], ["Ski length", "Up to 185 cm"], ["Lock", "SKS, SuperLatch"], ["Warranty", "Limited lifetime"]]},
  {"asin": "B07B4P7WYX", "role": "Lightest", "price": "Confirm on listing",
   "pros": ["38.6 lb, the lightest box here", "165 lb rated load, published by Rhino-Rack", "32 in wide, leaving bar room on a wide roof", "Dual-side opening, three locking points", "5-year warranty"],
   "cons": ["15.5 cu ft is modest for a full-size SUV", "Heavy Duty bars need the separate RUBK-MF kit", "Rhino-Rack's page doesn't list a price"],
   "body": "The Rhino-Rack MasterFit 440L is the box for Tahoe owners who want the most gear weight under a 165 lb kit rating. Rhino-Rack lists it at 440 L (15.5 cu ft), 76 x 32 x 17 in and 38.6 lb, with a published 165 lb maximum load, dual-side opening with a key lock, three locking points and a 5-year warranty. It is nearly 13 lb lighter than the GrandTour 16 and 26 lb lighter than the CBX XXL, and on a Tahoe those pounds go straight to cargo: roughly 110 lb after the bars.\n\nThe 32 in width also leaves bar length free on the Tahoe's wide roof, enough for a ski or bike mount beside it if the combined weight still fits the kit rating. Rhino-Rack gives a crossbar spacing of 620 to 930 mm, about 24.4 to 36.6 in, which sliding bars on flush rails meet easily. The page says it fits Rhino-Rack's Vortex and Euro bars directly and needs a separate RUBK-MF kit for its Heavy Duty bars, so confirm the hardware suits your bars. At 17 in tall, a Tahoe with it on is past 93 in before bars. Rhino-Rack doesn't list a price on its page; compare on the listing.",
   "who": "Tahoe owners who carry dense gear and want the most weight left for it.",
   "specs": [["Volume", "440 L / 15.5 cu ft"], ["Exterior", "76 × 32 × 17 in"], ["Box weight", "38.6 lb"], ["Max load", "165 lb (75 kg)"], ["Crossbar spread", "620–930 mm (about 24.4–36.6 in)"], ["Opening", "Dual-side, key lock"], ["Locking points", "3"], ["Warranty", "5 years"]]},
  {"asin": "B0F8PNL8H9", "role": "Premium big box", "price": "$1,249.95 (box alone)",
   "pros": ["21 cu ft, skis up to 215 cm", "57.2 lb, about 8 lb lighter than the CBX XXL", "One-hand dual-side opening, PowerClick mounts, SlideLock", "Thule rates it for 165 lb; limited lifetime warranty per etrailer", "21-13/16 to 36-9/16 in spread (etrailer)"],
   "cons": ["18.1 in tall; the Tahoe is past 94 in before bars", "This Amazon listing bundles GoPack duffels, so it costs more than the box alone", "Only about 90 lb left for gear on a 165 lb kit"],
   "body": "The Thule Motion 3 XXL is the other box that makes full use of the Tahoe's long roof. Thule lists it at 21 cu ft with exterior dimensions of 91.3 x 36.2 x 18.1 in, a 57.2 lb box weight and a 165 lb maximum load. It takes skis up to 215 cm, opens from both sides with one hand, locks with SlideLock and clamps on with PowerClick mounts whose torque indicator clicks when tight. etrailer lists a crossbar spread of 21-13/16 to 36-9/16 in and a limited lifetime warranty. Thule lists the box alone at $1,249.95; this Amazon listing bundles it with a GoPack duffel set.\n\nCompared with the CBX XXL, it gives up half a cubic foot but saves about 8 lb, which is 8 lb more for gear under a 165 lb kit rating. Thule gives a front-clearance figure of more than 54 13/16 in; on a 210.7 in long Tahoe that's easy to meet with the box mounted forward, but measure anyway. The one-hand opening helps when you're on a step stool at a 76 in roof. At 18.1 in tall, it puts the Tahoe past 94 in before bars, so it's a road-trip box that comes off before the garage.",
   "who": "Tahoe owners who want the biggest box with the easiest opening and will pay for it.",
   "specs": [["Volume", "21 cu ft"], ["Exterior", "91.3 × 36.2 × 18.1 in"], ["Box weight", "57.2 lb"], ["Max load", "165 lb"], ["Crossbar spread", "21-13/16 to 36-9/16 in (etrailer)"], ["Ski length", "Up to 215 cm"], ["Front clearance", "Over 54 13/16 in (Thule)"], ["Warranty", "Limited lifetime (etrailer)"]]},
  {"asin": "B00BCLL8C0", "role": "Best budget", "price": "$449.95",
   "pros": ["18 cu ft for $449.95 at SportRack", "63 in long, far from the liftgate", "Tool-free mounting hardware and a lock", "Fits square, round and most factory bars, per SportRack", "Fixed positions are easy to meet with sliding bars"],
   "cons": ["Rear-opening lid on a 76 in roof means a ladder or tall step", "19 in tall, the tallest box here", "Box weight, load rating and warranty not published; confirm"],
   "body": "The SportRack Vista XL is the cheapest way to add serious space to a Tahoe. SportRack lists the SR7018 at 63 x 38 x 19 in with 18 cu ft, UV-resistant ABS, tool-free mounting hardware and a lock, for $449.95, well under half the price of the 21 cu ft boxes. etrailer gives three fixed mounting positions, 25-7/8, 27-7/8 and 29-7/8 in center to center, and because bars slide on the Tahoe's flush rails, setting them to one of those is straightforward.\n\nThe drawbacks are sharper on a Tahoe than on a smaller SUV. The lid opens at the rear, so you load it by reaching over the back of a 76 in roof; you'll want a sturdy step or small ladder behind the vehicle, and the liftgate has to be closed while you do it. At 19 in, it is the tallest box here and puts the Tahoe past 95 in before bars. SportRack's page doesn't publish a box weight, a load rating or warranty terms, so confirm all three on the listing before you plan a load against a 165 lb kit rating.",
   "who": "Budget buyers who load the box once per trip and have a step to reach it.",
   "specs": [["Volume", "18 cu ft"], ["Exterior", "63 × 38 × 19 in"], ["Opening", "Rear"], ["Mounting positions", "25-7/8, 27-7/8 or 29-7/8 in (etrailer)"], ["Hardware", "Tool-free; lock included"], ["Material", "UV-resistant ABS"], ["Box weight / max load", "Not published; confirm"], ["Price", "$449.95 (SportRack)"]]},
  {"asin": "B0FK4RLXN3", "role": "Budget crossbars", "price": "Confirm on listing",
   "pros": ["Listing names the 2021–2026 Tahoe plus Suburban, Yukon XL and Escalade ESV", "Lockable aluminum bars", "Far cheaper than a Thule or Yakima flush-rail kit", "Needed before any box goes on", "One set for GM T1 SUVs listed"],
   "cons": ["The 350 lb figure in the title is a bar claim, not the roof limit", "No maker spec sheet for spread or bar weight; confirm", "Confirm Z71 fit on the listing"],
   "body": "Every box here needs crossbars, and these lockable aluminum bars are the budget route. The listing names the 2021–2026 Tahoe along with the Suburban, Yukon XL and Escalade ESV. For brand-name kits, etrailer lists a Thule setup of WingBar Evo bars (60 in, rated at 220 lb), Evo Flush Rail feet (165 lb) and fit kit TH95JW at $704.85, and The Rack Shop sells a Yakima SightLine kit rated at 165 lb for $653.85 on sale and a separate Thule setup for the Z71 at $604.85 on sale.\n\nThe listing's 350 lb claim should not change your plan. The flush-rail feet on the brand-name kits are rated at 165 lb, and we couldn't confirm Chevrolet's roof figure, so check your owner's manual and use the lowest number. There is no maker spec sheet for these bars, so confirm the bar weight, the length and how far apart they can be set against your box's spread range. The Z71 uses a different fit kit on the brand-name systems, so confirm Z71 fit on the listing before ordering.",
   "who": "Tahoe owners who need bars first and want to spend less than a Thule or Yakima kit.",
   "specs": [["Fits (per listing)", "2021–2026 Tahoe, Suburban, Yukon XL, Escalade ESV"], ["Material", "Aluminum"], ["Lock", "Lockable"], ["Listed load", "350 lb (bar claim)"], ["Brand-name kit rating", "165 lb (flush-rail feet)"], ["Spread / bar weight", "Not published; confirm"]]},
 ],
 "install": [
  "Fit flush-rail crossbars with the fit kit for your trim (Z71 has its own) and torque the feet to spec. Bring a step stool; the Tahoe's roof is 76 in up.",
  "Slide the bars to a spread inside the box's range (24–38 in for the CBX XXL, 24–36 in for the GrandTour 16, or one of the Vista XL's fixed positions).",
  "With a helper on each side, lift the box onto the bars, center it side to side and slide it forward on the long roof.",
  "Fit the clamps loosely, open the liftgate slowly to check the gap, then tighten the clamps to the box maker's instructions.",
  "Lock the box and mounts, rock it from each corner, re-check the clamps after the first drive, and put a garage reminder on the dash.",
  "Keep bars + box + gear under the lowest of your manual's roof figure and the kit rating (165 lb on the kits we found), with heavy items between the bars.",
 ],
 "avoid": [
  {"h": "Raised-rail towers on the flush rails", "body": "Retailers list the 2021+ Tahoe with flush rails. Buy flush-rail feet and a fit kit for your trim."},
  {"h": "Driving into a 7 ft garage with the box on", "body": "A 76 in Tahoe plus a 15–19 in box and bars is well over 84 in. Measure, and leave yourself a reminder."},
  {"h": "Treating a 21 cu ft box as a 21 cu ft load", "body": "The CBX XXL weighs 65 lb and the Motion 3 XXL 57.2 lb. On a 165 lb kit, pack them with light, bulky gear."},
  {"h": "A rear-opening box with no way to reach it", "body": "The Vista XL loads from the back of a 76 in roof. Plan on a ladder or step, or choose a dual-side box."},
 ],
 "verdict": {
  "thesis": "Fit flush-rail crossbars for your trim, then choose the Yakima GrandTour 16 for most Tahoe families, the Yakima CBX XXL for the most space, or the SkyBox 16 if height is tight.",
  "body": "On the fifth-gen Tahoe, the roof has room for anything, but three things set the rules: flush rails with trim-specific fit kits, 165 lb ratings on the kits we found, and a 76 in body that puts any box well past a standard garage door. The GrandTour 16 balances those best, with 16 cu ft, dual-side loading and weight left for gear. The CBX XXL and Thule Motion 3 XXL use the long roof fully if you pack them light, the SkyBox 16 is the lowest full-size box, the Rhino-Rack MasterFit 440L is the lightest, and the SportRack Vista XL is the budget pick if you have a step to load it from the rear.\n\nStart with the bars: the flush-rail kits in this guide are sold by trim, and the Z71 takes its own fit kit. Running boards make the side reach to the box easier, and for heavy gear the Tahoe's Class IV trailer hitch takes a hitch cargo carrier. The vehicle hub lists every fit-checked accessory for your Tahoe.",
 },
 "sources": [
  ["2021 Chevrolet Tahoe roof types (etrailer)", "https://www.etrailer.com/roof-2021_chevrolet_tahoe.htm"],
  ["Thule flush-rail rack for 2021 Tahoe, 165 lb feet / 220 lb bars (etrailer)", "https://www.etrailer.com/multi-product.aspx?pc1=th711500&pc2=th710601&pc3=th95jw&vehicleid=20217016669&hhyear=2021&hhmake=chevrolet&hhmodel=tahoe"],
  ["Yakima flush-rail rack for 2021–2026 Tahoe, 165 lb (The Rack Shop)", "https://therackshop.com/2021-2026-chevrolet-tahoe-w-flush-rails-yakima-crossbar-complete-roof-rack/"],
  ["Thule rack for 2021–2026 Tahoe Z71, 165 lb / 58 in max spread (The Rack Shop)", "https://therackshop.com/2021-2026-chevrolet-tahoe-z71-w-flush-rails-thule-crossbar-complete-roof-rack/"],
  ["2021 Chevrolet Tahoe specs, 76 in height (Cars.com)", "https://www.cars.com/research/chevrolet-tahoe-2021/specs/"],
  ["Chevrolet Tahoe fifth generation, 210.7 in length, trims (Wikipedia)", "https://en.wikipedia.org/wiki/Chevrolet_Tahoe"],
  ["Yakima GrandTour 16 (Yakima)", "https://yakima.com/products/grandtour-16"],
  ["Yakima CBX XXL (Yakima)", "https://yakima.com/products/cbx-xxl"],
  ["Yakima SkyBox 16 Carbonite (Yakima)", "https://yakima.com/collections/roof-boxes/products/skybox-16-carbonite-2014-2023"],
  ["Rhino-Rack MasterFit Roof Box 440L (Rhino-Rack)", "https://www.rhinorack.com/en-us/products/roof-racks/roof-boxes/roof-boxes/masterfit-roof-box-440l-black-_rmft440"],
  ["Thule Motion 3 XXL (Thule)", "https://www.thule.com/en-us/cargo-carrier/car-top-carrier/thule-motion-3-xxl-_-639950"],
  ["Thule Motion 3 spread and warranty (etrailer)", "https://www.etrailer.com/Roof-Box/Thule/TH59PN.html"],
  ["SportRack Vista XL (SportRack) and mounting positions (etrailer)", "https://www.sportrack.com/product/vista-xl-cargo-box/"],
  ["2025 Chevrolet Tahoe trims: RST Performance Edition package (Edmunds)", "https://edmunds.com/chevrolet/tahoe/2025/trims"],
 ],
}

# Product list for this page (boxes + Tahoe crossbars). (asin, name, brand, band, cond, note)
FITS = [
 ("B083KP48XC","Yakima GrandTour 16 Premium Rooftop Cargo Box, 16 cu ft, dual-side opening","Yakima","$700–$900",{},"Universal box, 18 in tall; confirm garage clearance and spread."),
 ("B0F3LF5P6D","Yakima CBX XXL 21.5 Cubic Foot Rooftop Cargo Box, dual-sided opening, SKS locks","Yakima","$1,100–$1,500",{},"Universal box, 65 lb; confirm roof figure in manual before loading."),
 ("B001PUZXGK","Yakima SkyBox 16 Carbonite Rooftop Cargo Box, 16 cu ft (15 in tall)","Yakima","$550–$750",{},"Universal box, lowest here; confirm garage clearance."),
 ("B07B4P7WYX","Rhino-Rack MasterFit Roof Box 440L (15.5 cu ft), Black","Rhino-Rack","See listing",{},"Universal box, 38.6 lb; confirm mounting kit suits your bars."),
 ("B0F8PNL8H9","Thule Motion 3 XXL 21 cu ft Rooftop Cargo Box with GoPack Duffel Set, 165 lb load capacity","Thule","$1,200–$1,500",{},"Bundle listing; confirm front clearance and garage height."),
 ("B00BCLL8C0","SportRack Vista XL Rear Opening Cargo Box, 18 cu ft, Black","SportRack","$400–$500",{},"Rear opening on a tall roof; confirm box weight and load rating."),
 ("B0FK4RLXN3","Roof Rack Cross Bars for Chevy Tahoe 2021-2026, Suburban, Yukon XL, Escalade ESV, lockable aluminum","Generic","See listing",{"roof_type":"flush-rails"},"Confirm Z71 fit, spread and bar weight."),
]
