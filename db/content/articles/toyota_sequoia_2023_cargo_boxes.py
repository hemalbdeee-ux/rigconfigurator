"""Long-form article — Best Rooftop Cargo Boxes for 2023–2026 Toyota Sequoia (3rd gen, XK80).
Mirrors the approved Tahoe/Highlander cargo-box pages. No invented hands-on testing: box specs are the Yakima, Thule,
Rhino-Rack, INNO and SportRack figures already verified for those pages (maker pages plus etrailer); vehicle facts from
db/migrations/003_vehicles.sql, etrailer's 2023 Sequoia roof page (lists BOTH raised and flush rails), Rack Warehouse
(Yakima TimberLine FX for raised rails), Rave Offroad (TRD Pro factory rack, 132 lb evenly distributed), Cars.com
(75 in tall, 208 in long), Wikipedia (trims, towing) and owner threads on ToyotaSequoia.net (checked 2026-09-28).
Not verified: a Toyota-published roof load figure and the OEM PT767-0C660 crossbar rating/spread — readers are sent
to the owner's manual.
Text fixes 2026-10-04: removed the reference to a Sequoia roof rack page (none exists); rail-type wording now follows
etrailer's 2023 page as re-read (two types, no grades named) and notes that Rack Warehouse's raised-rail page covers
2001-2025 without splitting generations; tow figure now Toyota's (2025 release, 9,520 lb; January 2022 reveal 9,000 lb);
Toyota accessory bars no longer described as fitting either rail type without a dealer check; META "rails by trim" fixed.
"""

KEY = ("toyota", "sequoia", "2023-present", "cargo-boxes")

TITLE = "Best Rooftop Cargo Boxes for 2023–2026 Toyota Sequoia: 7 Picks for a 75-Inch-Tall Hybrid SUV"
META = ("Six Yakima, Thule, Rhino-Rack, INNO and SportRack boxes plus Toyota crossbars for the 3rd-gen Sequoia: rail "
        "type, TRD Pro rack, weight and garage height.")

FAQ = [
 ("What is the best cargo box for a 2023–2026 Toyota Sequoia?",
  "The Yakima SkyBox 16 Carbonite is the best overall pick for most Sequoia families. It holds 16 cu ft, weighs 47 lb, stands 15 in tall and opens from both sides. The INNO Wedge 660 is the lowest profile box at 11 in tall, for tall garages and highway fuel economy. The Rhino-Rack MasterFit 440L is the lightest at 38.6 lb, leaving the most weight for gear. The Thule Motion 3 XXL is the biggest box at 21 cu ft if you pack light, and the SportRack Vista XL is the budget pick if you have a ladder. Before any box, fit crossbars matched to your rail type, since etrailer lists both raised and flush rails for this Sequoia, and confirm the roof figure in your owner's manual."),
 ("Does the 2023–2026 Sequoia have raised rails or flush rails?",
  "Check your own roof. etrailer lists two roof types for the 2023 Sequoia: factory installed raised rails and flush mounted rails, both running front to back. It does not say which grades have which, and the Toyota releases we read do not describe the roof rails, so we could not confirm rail type by grade. Rack Warehouse sells Yakima's raised-rail TimberLine FX kit for the Sequoia, but its page covers 2001–2025 models without separating this generation. If you can slide your fingers under the rail between its end mounts, it's a raised rail and strap-style towers fit. If the rail sits tight to the roof with no gap, it's a flush rail, so buy flush-rail feet listed for the Sequoia."),
 ("What is the roof load limit on a 2023–2026 Sequoia?",
  "We couldn't confirm a Toyota-published roof figure for this generation, so read the roof-load section of your owner's manual before you load a box. The figures we did find are lower than many owners expect: Rave Offroad lists the TRD Pro factory roof rack at 132 lb evenly distributed, and a budget crossbar listing for the 2023–2026 Sequoia claims 165 lb. Use the lowest of the manual, crossbar and box ratings, and count bars, box and cargo against it."),
 ("Do the Toyota factory crossbars work with a cargo box?",
  "Yes. Toyota sells accessory cross bars for the 2023-on Sequoia under part number PT767-0C660, and an owner on ToyotaSequoia.net reports running them with a Thule box on top. Owners describe a low-profile bar with plastic caps hiding the mounting screws. Toyota's rating and adjustment range weren't on any page we could open, so confirm both with your dealer and set the bars inside the box's spread range."),
 ("Will a Sequoia with a roof box fit in my garage?",
  "Not through a standard 7 ft (84 in) door. Cars.com lists the 2023 Sequoia at 75 in tall, and the boxes here add 11 in (INNO Wedge 660) to 19 in (SportRack Vista XL) on top of the crossbars, so the lowest box puts the top at 86 in before the bars are counted. One owner on ToyotaSequoia.net reports the garage door catching the crossbar with bars alone. Measure your Sequoia with bars fitted before the first trip home."),
 ("Can I put a cargo box on the TRD Pro's factory roof rack?",
  "Possibly, but confirm first. Rave Offroad describes the TRD Pro rack as a factory option that secures into the roof rails, 67.5 in long and about 48 to 51 in wide, with a 132 lb evenly distributed limit. A box's clamps have to wrap the rack's cross members, and the box's weight plus cargo has to fit under 132 lb. Many owners find it simpler to fit conventional crossbars for box trips; check the box maker's clamp range against the rack's tubes."),
 ("How do I load a roof box on a vehicle this tall?",
  "Choose a dual-side opening box so you can load from whichever side you're standing on, and keep a sturdy step stool in the cargo area. Aftermarket running boards help, since you can stand on the board to reach the near half of the box. A rear-opening box like the SportRack Vista XL means reaching over the back of a 75 in roof with the liftgate closed, which really needs a ladder. Put light, bulky gear at the far side and heavier bags between the bars."),
 ("Will a roof box hit the Sequoia's power liftgate?",
  "Rarely, if the box sits forward. Cars.com lists the Sequoia at 208 in long, and even the 91.3 in Thule Motion 3 XXL has room ahead of the liftgate when mounted forward. Thule lists a front-clearance figure of more than 54 13/16 in for that box; measure from your front bar to the liftgate seam and compare. Open the power liftgate slowly the first time, and if your manual shows how to set a lower opening height, use it on box trips."),
 ("Is the Sequoia roof the same as the Tundra's?",
  "No. The Sequoia shares the TNGA-F platform with the Tundra, but our fitment notes flag a different roof, and a pickup cab has no long roof for rails. Buy crossbars listed for the 2023-on Sequoia, not the Tundra, and not the 2008–2022 Sequoia, whose roof and rails are a different generation. The box itself carries over between vehicles because it clamps to crossbars."),
 ("How much does a roof box hurt the i-FORCE MAX hybrid's fuel economy?",
  "fueleconomy.gov estimates that a rooftop cargo box can cut fuel economy by 2 to 8 percent in city driving, 6 to 17 percent on the highway and 10 to 25 percent at interstate speeds of 65 to 75 mph. Every 3rd-gen Sequoia is a hybrid, but a box's drag hurts most at highway speed, where the hybrid system helps least. A low box like the INNO Wedge 660 adds the least frontal area. Take the box off between trips."),
 ("Should I use a roof box or a hitch cargo carrier on a Sequoia?",
  "Toyota's release for the 2025 model year gives a maximum towing capacity of up to 9,520 lb (its January 2022 reveal said up to 9,000 lb), and our fitment data lists a Class IV hitch with a 2 in receiver. If your Sequoia has that receiver, a hitch cargo carrier is easy to add and keeps coolers, bins and water low and reachable. An owner on ToyotaSequoia.net notes that you need to switch off rear obstacle detection with a hitch carrier fitted. The roof box is better for soft, bulky gear you load once per trip, and it keeps the liftgate and camera clear."),
]

ARTICLE = {
 "dek": "Seven picks for the third-generation Sequoia: six rooftop boxes from Yakima, Thule, Rhino-Rack, INNO and SportRack, from an 11 in low-profile box to a 21 cu ft giant, plus Toyota's own crossbars. For each box we list volume, length, weight, height and crossbar spread, and what they mean on a 75 in tall hybrid SUV where rail type varies, the TRD Pro rack is rated at 132 lb, and garage clearance runs out fast.",
 "author": "jake-morrison",
 "reviewed": "2026-10-04",
 "method": "We did not mount these boxes ourselves. We ranked them on the makers' published specs (Yakima, Thule, Rhino-Rack, INNO and SportRack: volume, exterior dimensions, box weight, load rating, crossbar spread, warranty), on etrailer's figures for the Thule, INNO and SportRack boxes, on etrailer's and Rack Warehouse's Sequoia roof fit data, on Rave Offroad's TRD Pro rack listing, on vehicle dimensions from Cars.com and Wikipedia, on Toyota's newsroom releases for the tow figure, and on owner reports we read on ToyotaSequoia.net. Prices were checked on maker and retailer pages in September 2026. Amazon prices move daily, so the button shows the live price.",
 "takeaways": [
  "**Check your rail type.** etrailer lists both raised and flush rails for the 2023 Sequoia and does not say which grades have which. Look before you buy feet.",
  "**Toyota's roof figure isn't published where we could find it.** The TRD Pro factory rack is listed at 132 lb evenly distributed; confirm your number in the owner's manual.",
  "**75 in tall means no standard garage.** Even the 11 in INNO Wedge 660 puts the top at 86 in before the bars.",
  "**The long roof takes a long box.** At 208 in overall, the Sequoia fits a 91 in box ahead of the liftgate. Weight, not length, is the limit.",
  "**Load from the side.** Dual-side boxes and a step stool beat a rear-opening lid on a roof this high.",
 ],
 "top_picks": [
  {"asin": "B001PUZXGK", "role": "Best overall", "why": "SkyBox 16: 16 cu ft, 15 in tall, 47 lb, dual-side, $599 on sale"},
  {"asin": "B06VX9L59C", "role": "Lowest profile", "why": "INNO Wedge 660: 11 in tall for garages and hybrid fuel economy"},
  {"asin": "B07B4P7WYX", "role": "Lightest", "why": "Rhino-Rack MasterFit 440L: 38.6 lb, leaves most weight for gear"},
  {"asin": "B0F8PNL8H9", "role": "Biggest box", "why": "Thule Motion 3 XXL: 21 cu ft, uses the 208 in long body"},
  {"asin": "B0C26KKRF3", "role": "Factory crossbars", "why": "Toyota PT767-0C660, made for the 2023-on Sequoia rails"},
 ],
 "fit_table": {
  "caption": "2023–2026 Sequoia roof setups (what the box mounts to)",
  "head": ["Roof", "Trims", "Crossbar notes", "Box notes"],
  "rows": [
   ["Raised side rails (listed by etrailer for 2023)", "Not stated by grade; a gap under the rail", "Yakima TimberLine FX ($599.90 at Rack Warehouse), budget bars; Toyota PT767-0C660 (dealer to confirm rail match)", "Bars set inside the box's spread range"],
   ["Flush rails (also listed by etrailer for 2023)", "Not stated by grade; no gap under the rail", "Flush-rail feet listed for the Sequoia", "Same boxes"],
   ["TRD Pro factory roof rack", "TRD Pro option (Rave Offroad)", "67.5 in basket in the rails, 132 lb evenly distributed", "Confirm clamp fit on the rack tubes"],
   ["All trims: SR5, Limited, Platinum, 1794 Edition, TRD Pro, Capstone", "Hybrid i-FORCE MAX", "Roof figure: owner's manual", "Bars + box + gear under the lowest figure"],
   ["Height", "75 in (Cars.com, 2023)", "Bars add height", "Box adds 11–19 in; no standard 7 ft garage"],
  ],
 },
 "look_for": [
  {"h": "Rail type varies, so look before buying feet",
   "body": "etrailer lists two roof types for the 2023 Sequoia: factory installed raised rails and flush mounted rails, both running front to back. It does not say which grades have which, and the Toyota releases we read do not describe the roof rails. Rack Warehouse sells Yakima's raised-rail TimberLine FX kit for the Sequoia at $599.90, on a page that covers 2001–2025 models without separating this generation. So the rail type is the first thing to settle. Slide your fingers under the rail between its end mounts: if there's a gap, strap-style raised-rail towers clamp on; if the rail sits tight to the roof, you need flush-rail feet. Toyota's PT767-0C660 accessory bars are sold for the 2023-on Sequoia; ask the dealer to confirm they suit the rails on your vehicle. Every box here clamps to the bars once they're on."},
  {"h": "A roof figure you have to confirm",
   "body": "We couldn't open a Toyota page that states the Sequoia's roof load, so the owner's manual is the authority; read its roof-load section before loading a box. The figures we did find are modest for a vehicle this size. Rave Offroad lists the TRD Pro factory roof rack at 132 lb evenly distributed, and a budget crossbar listing for the 2023–2026 Sequoia claims 165 lb. The boxes here weigh 38.6 lb (MasterFit 440L) to 57.2 lb (Motion 3 XXL). Against 132 lb, a 47 lb SkyBox 16 plus bars leaves well under 85 lb for gear. Use the lowest number you find."},
  {"h": "Loading height on a 75 in roof",
   "body": "Cars.com lists the 2023 Sequoia at 75 in tall, and a box sits on top of that and the crossbars. Reaching the far side of a 36 in wide box from the ground is not realistic for most adults, so dual-side opening matters more here than on a crossover: open the box from whichever side you're standing on. Keep a sturdy step stool in the cargo area, or stand on a running board to reach the near half. A rear-opening box like the SportRack Vista XL means reaching over the back of the roof with the liftgate closed, which really calls for a small ladder."},
  {"h": "Garage and parking-structure clearance",
   "body": "This is the Sequoia's biggest roof-box gotcha. At 75 in tall, the vehicle plus the lowest box here, the 11 in INNO Wedge 660, is at 86 in before the crossbars, already over a standard 7 ft (84 in) door. The SkyBox 16 puts it at 90 in, the MasterFit 440L at 92 in, the Motion 3 XXL past 93 in and the Vista XL at 94 in, all before bars. One owner on ToyotaSequoia.net reports the garage door catching the crossbar with bars alone. Measure the Sequoia with bars fitted, add the box height, and leave a reminder on the dash."},
  {"h": "Using the long roof without overloading it",
   "body": "Cars.com lists the Sequoia at 208 in long, so the roof has room for the longest boxes sold: the Thule Motion 3 XXL at 91.3 in sits ahead of the power liftgate if mounted forward, and Thule's front-clearance figure of more than 54 13/16 in is easy to meet. The trap is weight. A 57.2 lb box on a roof you may find rated around 132 to 165 lb leaves far less weight than space. Fill big boxes with sleeping bags, jackets and soft duffels, and put coolers and bins on a hitch cargo carrier."},
 ],
 "look_table": {
  "head": ["Feature", "Look for", "Avoid"],
  "rows": [
   ["Crossbars", "Toyota PT767-0C660 or feet matched to your rail type", "Tundra or 2008–2022 Sequoia bars"],
   ["Height", "11–15 in boxes (Wedge 660, SkyBox 16) for tall doors and fuel", "Any box through a standard 7 ft door"],
   ["Opening", "Dual-side, so you load from either side with a step stool", "Rear-only lids on a 75 in roof"],
   ["Box weight", "Under 48 lb to keep weight for gear under a modest roof figure", "Filling a 57 lb, 21 cu ft box with heavy gear"],
   ["Crossbar spread", "A range your bars can meet; confirm the OEM bars' adjustment", "Buying before checking where your bars sit"],
   ["Warranty", "Limited lifetime (Yakima, Thule, INNO) or 5 years (Rhino-Rack)", "No terms stated; ask the seller"],
  ],
 },
 "types_table": {
  "caption": "Box sizing for the Sequoia (makers' published specs; Thule, INNO and SportRack figures per etrailer)",
  "head": ["Box", "Volume", "L × W × H", "Box weight", "Crossbar spread", "Top height on a 75 in Sequoia"],
  "rows": [
   ["Yakima SkyBox 16 Carbonite", "16 cu ft", "81 × 36 × 15 in", "47 lb", "24–34.5 in", "90 in before bars"],
   ["INNO Wedge 660", "11 cu ft", "80 × 33 × 11 in", "42 lb", "24–39 in", "Lowest: 86 in before bars"],
   ["Rhino-Rack MasterFit 440L", "15.5 cu ft", "76 × 32 × 17 in", "38.6 lb", "620–930 mm (about 24.4–36.6 in)", "92 in before bars"],
   ["Yakima GrandTour 16", "16 cu ft", "79 × 35 × 18 in", "51.5 lb", "24–36 in", "93 in before bars"],
   ["Thule Motion 3 XXL", "21 cu ft", "91.3 × 36.2 × 18.1 in", "57.2 lb", "21-13/16 to 36-9/16 in", "Past 93 in before bars"],
   ["SportRack Vista XL", "18 cu ft", "63 × 38 × 19 in", "Not published", "Fixed at 25-7/8, 27-7/8 or 29-7/8 in", "Tallest: 94 in before bars"],
  ],
 },
 "picks": [
  {"asin": "B001PUZXGK", "role": "Best overall", "price": "$599 on sale at Yakima (regular $749)",
   "pros": ["16 cu ft at 47 lb", "15 in tall, low for a full-size box", "Dual-side opening with SuperLatch and SKS locks", "24–34.5 in spread suits most crossbar setups", "Limited lifetime warranty; installs without assembly"],
   "cons": ["Still puts a Sequoia at 90 in before bars", "36 in wide, filling much of a bar", "Leaves under 85 lb for gear against a 132 lb figure"],
   "body": "For most Sequoia families, the Yakima SkyBox 16 Carbonite balances the three things this roof cares about: height, weight and reach. Yakima lists it at 81 x 36 x 15 in with 16 cu ft and a 47 lb box weight, with dual-side opening, SuperLatch security, SKS locks, skis and boards up to 185 cm and a limited lifetime warranty. It installs without assembly and clamps to most crossbars, including factory bars, and it was $599 on sale (regular $749) on Yakima's store when we checked. An owner on ToyotaSequoia.net reports running a SkyBox on a 2023 and finding it no louder than the factory rack alone.\n\nOn a 75 in tall Sequoia, those 15 in matter. The box puts the top at 90 in before the crossbars, which still rules out a 7 ft door but is 3 to 4 in lower than the GrandTour 16 or Motion 3 XXL at tall doors, hotel canopies and parking structures. At 47 lb it also leaves more of a modest roof figure for gear than the big boxes do, and dual-side opening lets you load from either side off a step stool. Its 24 to 34.5 in spread range suits Toyota's accessory bars or raised-rail towers; confirm where your bars sit before ordering.",
   "who": "Sequoia families who want a full-size, easy-loading box that stays as low as a 16 cu ft box gets.",
   "specs": [["Volume", "16 cu ft"], ["Exterior", "81 × 36 × 15 in"], ["Box weight", "47 lb"], ["Crossbar spread", "24–34.5 in"], ["Opening", "Dual-side"], ["Ski length", "Up to 185 cm"], ["Lock", "SKS, SuperLatch"], ["Warranty", "Limited lifetime"]]},
  {"asin": "B06VX9L59C", "role": "Lowest profile", "price": "$917.61 at etrailer (sale)",
   "pros": ["11 in tall, the lowest box here", "Least frontal area for highway fuel economy", "24–39 in spread, the widest range here", "Dual-side opening with push buttons", "Limited lifetime warranty"],
   "cons": ["11 cu ft for about $918", "Own 110 lb rating caps contents", "Still 86 in tall on a Sequoia before bars"],
   "body": "The INNO Wedge 660 is the box for Sequoia owners who worry most about height and fuel. etrailer lists it at 80 x 33 x 11 in with 11 cu ft, a 42 lb box weight and a 110 lb weight capacity, a 24 to 39 in crossbar spread and a dual-side lid with push-button release. It takes 6 to 8 pairs of skis up to 182 cm, carries a limited lifetime warranty, and etrailer had it at $917.61 on sale. At 11 in tall it is 4 in lower than the SkyBox 16 and 8 in lower than the Vista XL.\n\nOn a 75 in Sequoia that puts the top at 86 in before bars. It won't clear a standard 7 ft door, but it is the box most likely to slip under an 8 ft door or a low parking structure once you measure. The low, flat shape also adds the least frontal area, and fueleconomy.gov puts a roof box's penalty at 10 to 25 percent at 65 to 75 mph, where the i-FORCE MAX hybrid system helps least. Its 24 to 39 in spread is the easiest to meet on any bar here. The trade-off is space: 11 cu ft suits skis, jackets and flat duffels rather than camp chairs. Keep contents under its 110 lb rating, and count its 42 lb against your roof figure.",
   "who": "Owners who park in tall garages or drive long highway trips and want the lowest box possible.",
   "specs": [["Volume", "11 cu ft"], ["Exterior", "80 × 33 × 11 in"], ["Box weight", "42 lb"], ["Max load", "110 lb"], ["Crossbar spread", "24–39 in"], ["Opening", "Dual-side"], ["Ski length", "Up to 182 cm"], ["Warranty", "Limited lifetime"]]},
  {"asin": "B07B4P7WYX", "role": "Lightest", "price": "Confirm on listing",
   "pros": ["38.6 lb, the lightest box here", "165 lb rated load, published by Rhino-Rack", "32 in wide, leaving bar room beside it", "Dual-side opening, three locking points", "5-year warranty"],
   "cons": ["15.5 cu ft is modest for a full-size SUV", "Some bar systems need a separate mounting kit", "Rhino-Rack's page doesn't list a price"],
   "body": "If the roof figure in your manual turns out as modest as the 132 lb TRD Pro rack rating, the Rhino-Rack MasterFit 440L is the box that leaves the most for gear. Rhino-Rack lists it at 440 L (15.5 cu ft), 76 x 32 x 17 in and 38.6 lb, with a published 165 lb maximum load, dual-side opening with a key lock, three locking points and a 5-year warranty. It is more than 8 lb lighter than the SkyBox 16 and nearly 19 lb lighter than the Motion 3 XXL, and on a Sequoia every pound saved is a pound of cargo.\n\nThe 32 in width leaves bar length free on the Sequoia's wide roof, enough for a ski mount beside it if the combined weight still fits your figure. Rhino-Rack gives a crossbar spacing of 620 to 930 mm, about 24.4 to 36.6 in, which suits most bar setups. Its page says it fits Rhino-Rack's Vortex and Euro bars directly and needs a separate RUBK-MF kit for Heavy Duty bars, so confirm the hardware clamps Toyota's accessory bars or whatever bars you run. At 17 in tall it puts the Sequoia at 92 in before bars. Rhino-Rack doesn't list a price, so compare on the listing.",
   "who": "Owners who carry dense gear and want the most of a modest roof figure left for it.",
   "specs": [["Volume", "440 L / 15.5 cu ft"], ["Exterior", "76 × 32 × 17 in"], ["Box weight", "38.6 lb"], ["Max load", "165 lb (75 kg)"], ["Crossbar spread", "620–930 mm (about 24.4–36.6 in)"], ["Opening", "Dual-side, key lock"], ["Locking points", "3"], ["Warranty", "5 years"]]},
  {"asin": "B0F8PNL8H9", "role": "Biggest box", "price": "$1,249.95 (box alone)",
   "pros": ["21 cu ft, the most volume here", "Skis up to 215 cm", "One-hand dual-side opening, PowerClick mounts, SlideLock", "21-13/16 to 36-9/16 in spread (etrailer)", "Front clearance over 54 13/16 in is easy on a 208 in SUV"],
   "cons": ["57.2 lb, the heaviest box here", "18.1 in tall; past 93 in before bars", "This Amazon listing bundles GoPack duffels, so it costs more than the box alone"],
   "body": "The Sequoia's long roof is one of the few that can carry the Thule Motion 3 XXL with room to spare ahead of the liftgate. Thule lists it at 21 cu ft with exterior dimensions of 91.3 x 36.2 x 18.1 in, a 57.2 lb box weight and a 165 lb maximum load. It takes skis up to 215 cm, opens from both sides with one hand, locks with SlideLock and clamps on with PowerClick mounts that click when tight. etrailer lists a crossbar spread of 21-13/16 to 36-9/16 in and a limited lifetime warranty. Thule lists the box alone at $1,249.95; this Amazon listing bundles it with a GoPack duffel set. An owner on ToyotaSequoia.net reports a Thule Motion XL on a 2023, so Thule's clamps do go on the factory bars.\n\nThe number to plan around is 57.2 lb. If your manual's figure lands near the TRD Pro rack's 132 lb, box plus bars leaves perhaps 60 lb or less for gear, so this is a box for volume, not weight: sleeping bags, jackets, long skis and soft bags for eight passengers. Mount it forward; Thule's front-clearance figure of more than 54 13/16 in is easy to meet on a 208 in long SUV, but open the power liftgate slowly the first time. At 18.1 in tall it comes off before the garage.",
   "who": "Big families and ski crews who need the most space and will pack it light.",
   "specs": [["Volume", "21 cu ft"], ["Exterior", "91.3 × 36.2 × 18.1 in"], ["Box weight", "57.2 lb"], ["Max load", "165 lb"], ["Crossbar spread", "21-13/16 to 36-9/16 in (etrailer)"], ["Ski length", "Up to 215 cm"], ["Front clearance", "Over 54 13/16 in (Thule)"], ["Warranty", "Limited lifetime (etrailer)"]]},
  {"asin": "B083KP48XC", "role": "Deepest 16", "price": "$709",
   "pros": ["18 in deep for bulky family gear", "Dual-side opening", "24–36 in spread", "Made in the USA; limited lifetime warranty", "Skis and boards up to 185 cm"],
   "cons": ["51.5 lb, 4.5 lb more than the SkyBox 16", "18 in tall; 93 in before bars", "About $110 more than the SkyBox 16 on sale"],
   "body": "The Yakima GrandTour 16 has the same 16 cu ft as the SkyBox but a deeper shell, which suits the bulky, awkward gear a three-row family hauls: camp chairs, a folded stroller, a pack-and-play. Yakima lists it at 79 x 35 x 18 in and 51.5 lb, with dual-side opening, skis and boards up to 185 cm, SKS locks, a removable torque-limiting knob and a limited lifetime warranty. It is made in the USA and lists at $709.\n\nOn the Sequoia, its 79 in length sits well forward of the liftgate on a 208 in long body, and the 24 to 36 in spread range suits Toyota's accessory bars or raised-rail towers. The costs are height and weight. At 18 in it puts the Sequoia at 93 in before bars, 3 in higher than the SkyBox 16, so it is strictly a road-trip box. At 51.5 lb it also takes 4.5 lb more of your roof figure than the SkyBox, and roughly 13 lb more than the Rhino-Rack. If you haul tall, light items and park outside, the extra depth is worth it; if you juggle garage clearance or a tight roof figure, choose the SkyBox 16 instead.",
   "who": "Families who carry tall, bulky gear and park outdoors.",
   "specs": [["Volume", "16 cu ft"], ["Exterior", "79 × 35 × 18 in"], ["Box weight", "51.5 lb"], ["Crossbar spread", "24–36 in"], ["Opening", "Dual-side"], ["Ski length", "Up to 185 cm"], ["Lock", "SKS locks included"], ["Warranty", "Limited lifetime"]]},
  {"asin": "B00BCLL8C0", "role": "Best budget", "price": "$449.95",
   "pros": ["18 cu ft for $449.95 at SportRack", "63 in long, the shortest box here", "Tool-free mounting hardware and a lock", "Fits square, round and most factory bars, per SportRack", "Three fixed positions up to 29-7/8 in (etrailer)"],
   "cons": ["Rear-opening lid on a 75 in roof needs a ladder", "19 in tall; 94 in before bars", "Box weight, load rating and warranty not published; confirm"],
   "body": "The SportRack Vista XL is the cheapest way to add real space to a Sequoia. SportRack lists it at 63 x 38 x 19 in with 18 cu ft, UV-resistant ABS, tool-free mounting hardware and a lock, for $449.95, well under half the price of the Motion 3 XXL. SportRack says it fits square bars, round bars and most factory racks, and etrailer gives three fixed mounting positions, 25-7/8, 27-7/8 and 29-7/8 in center to center. At 63 in it sits far forward of the liftgate on a 208 in long SUV.\n\nThe drawbacks are sharper on a Sequoia than on a crossover. The lid opens at the rear, so you load it by reaching over the back of a 75 in roof with the liftgate shut; a sturdy step or small ladder behind the vehicle is a must. At 19 in it is the tallest box here and puts the Sequoia at 94 in before bars. SportRack doesn't publish a box weight, load rating or warranty terms, so confirm all three on the listing before planning a load against a roof figure that may be as low as 132 lb. If you can adjust your crossbars, set them to one of the three positions.",
   "who": "Budget buyers who load once per trip and have a ladder to reach it.",
   "specs": [["Volume", "18 cu ft"], ["Exterior", "63 × 38 × 19 in"], ["Opening", "Rear"], ["Mounting positions", "25-7/8, 27-7/8 or 29-7/8 in (etrailer)"], ["Hardware", "Tool-free; lock included"], ["Material", "UV-resistant ABS"], ["Box weight / max load", "Not published; confirm"], ["Price", "$449.95 (SportRack)"]]},
  {"asin": "B0C26KKRF3", "role": "Factory crossbars", "price": "Confirm on listing",
   "pros": ["Genuine Toyota part PT767-0C660 for the 2023-on Sequoia", "Low-profile design with caps over the mounting screws, per owners", "Owners report running Thule boxes on them", "Needed before any box goes on", "Easy to remove, per an owner report"],
   "cons": ["Load rating not on any page we could open; confirm with a dealer", "Adjustment range not published; confirm against your box's spread", "Adds wind noise, per an owner report"],
   "body": "Every box here needs crossbars, and Toyota's own PT767-0C660 set is the most direct fit. Dealer parts catalogs list it as roof rack cross bars for the 2023-on Sequoia, and owners on ToyotaSequoia.net describe a low-profile bar that attaches to the side rails, with plastic caps hiding the screws; one owner says removal is just prying off the caps with a plastic tool. Another owner reports a Thule cargo box on top of the factory bars, and one early buyer says he bought the factory bars because aftermarket kits weren't out yet.\n\nWhat we couldn't find is a published load rating or adjustment range for these bars; the dealer pages we tried would not load. Ask your dealer for both, confirm the roof figure in your owner's manual, and use the lowest number. If you'd rather use a brand-name system, Rack Warehouse sells Yakima's TimberLine FX kit for Sequoias with raised rails at $599.90, and budget bars listed for the 2023–2026 Sequoia claim 165 lb. Owners also report extra wind noise from bars alone and a garage door catching the bar, so take them off between trips if you can.",
   "who": "Owners who want Toyota's own bars under a box and will confirm the rating with a dealer.",
   "specs": [["Part number", "PT767-0C660"], ["Fits", "2023-on Sequoia with side rails (dealer listings)"], ["Mounting", "Clamps to factory side rails; caps cover screws"], ["Load rating", "Not published where we looked; confirm"], ["Spread", "Not published; confirm"], ["Alternative", "Yakima TimberLine FX, $599.90 (Rack Warehouse)"]]},
 ],
 "install": [
  "Look at your roof: raised rails (gap underneath) or flush rails. Fit Toyota PT767-0C660 bars or feet listed for the 2023–2026 Sequoia and your rail type, and bring a step stool.",
  "Read the roof-load section of your owner's manual and note the crossbar rating; plan on the lowest figure (132 lb on the TRD Pro rack, per Rave Offroad).",
  "Set the bars inside the box's spread range (24–34.5 in for the SkyBox 16, 24–39 in for the Wedge 660, or one of the Vista XL's fixed positions).",
  "With a helper on each side, lift the box onto the bars, center it side to side and slide it forward on the long roof.",
  "Fit the clamps loosely, open the power liftgate slowly to check the gap, then tighten the clamps to the box maker's instructions.",
  "Lock the box, rock it from each corner, re-check the clamps after the first drive, and put a garage reminder on the dash.",
 ],
 "avoid": [
  {"h": "Buying feet before checking the rails", "body": "etrailer lists both raised and flush rails for the 2023 Sequoia. Look under the rail, and have a dealer confirm Toyota's accessory bars against your roof."},
  {"h": "Assuming a big SUV has a big roof rating", "body": "The TRD Pro factory rack is listed at 132 lb evenly distributed. Confirm your figure in the manual and count bars, box and gear."},
  {"h": "Driving into a 7 ft garage with the box on", "body": "A 75 in Sequoia plus an 11–19 in box is 86 to 94 in before bars. Measure and leave yourself a reminder."},
  {"h": "Tundra or 2008–2022 Sequoia bars", "body": "The 3rd-gen Sequoia has its own roof. Buy bars that name 2023 or later Sequoia."},
 ],
 "verdict": {
  "thesis": "Fit crossbars matched to your rail type, confirm the roof figure in your manual, then choose the Yakima SkyBox 16 for most Sequoia families, the INNO Wedge 660 if height is tight, or the Rhino-Rack MasterFit 440L if weight is.",
  "body": "On the third-gen Sequoia the roof has room for any box, but three things set the rules: rails that etrailer lists as raised or flush depending on the vehicle, a roof figure you have to confirm (the TRD Pro rack is listed at only 132 lb), and a 75 in body that puts any box past a standard garage door. The SkyBox 16 balances those best with 16 cu ft, a 15 in profile and dual-side loading. The Wedge 660 is the lowest box for tall doors and hybrid highway mileage, the MasterFit 440L leaves the most weight for gear, the Motion 3 XXL uses the long roof if you pack light, the GrandTour 16 suits tall, bulky gear, and the Vista XL is the budget pick if you have a ladder.\n\nStart with the bars: Toyota's PT767-0C660 set or feet matched to your rail type. Running boards make the side reach to the box easier on a roof this high, and for heavy gear a hitch cargo carrier suits the Class IV, 2 in receiver our data lists, if your Sequoia has one. If you're shopping the previous 2008–2022 Sequoia, its roof and rails differ, so buy bars for that generation.",
 },
 "sources": [
  ["2023 Toyota Sequoia roof types: raised and flush rails (etrailer)", "https://www.etrailer.com/roof-2023_toyota_sequoia.htm"],
  ["Yakima TimberLine FX raised-rail rack for Toyota Sequoia (Rack Warehouse)", "https://www.rackwarehouse.com/products/yakima-timberline-fx-complete-rack/vehicle/toyota/sequoia/"],
  ["TRD Pro factory roof rack for 2023+ Sequoia, 132 lb evenly distributed (Rave Offroad)", "https://raveoffroad.com/products/trd-pro-roof-rack-for-2023-sequoia"],
  ["Genuine Toyota Sequoia roof rack cross bars PT767-0C660 (Amazon)", "https://www.amazon.com/Genuine-Toyota-Sequoia-Cross-PT767-0C660/dp/B0C26KKRF3"],
  ["Owner thread: 2023 cross bars (ToyotaSequoia.net)", "https://www.toyotasequoia.net/threads/cross-bars.71/"],
  ["Owner thread: 2023 roof rack or cargo box (ToyotaSequoia.net)", "https://www.toyotasequoia.net/threads/2023-roof-rack-or-cargo-box.121/"],
  ["2023 Toyota Sequoia specs, 75 in height and 208 in length (Cars.com)", "https://www.cars.com/research/toyota-sequoia-2023/specs/"],
  ["Toyota Sequoia third generation: trims, i-FORCE MAX (Wikipedia)", "https://en.wikipedia.org/wiki/Toyota_Sequoia"],
  ["2025 Sequoia Adds 1794 Grade and More: 9,520-pound maximum towing capacity; no roof rail details (Toyota Newsroom)", "https://pressroom.toyota.com/2025-sequoia-adds-1794-grade-and-more/"],
  ["Standing Tall: All-New 2023 Sequoia, January 2022 reveal: up to 9,000 lb; no roof rail details (Toyota Newsroom)", "https://pressroom.toyota.com/standing-tall-all-new-2023-sequoia-full-size-suv-is-ready-to-make-its-mark/"],
  ["Yakima SkyBox 16 Carbonite (Yakima)", "https://yakima.com/collections/roof-boxes/products/skybox-16-carbonite-2014-2023"],
  ["Yakima GrandTour 16 (Yakima)", "https://yakima.com/products/grandtour-16"],
  ["INNO Wedge 660 specs (etrailer)", "https://www.etrailer.com/Roof-Box/INNO/INBRM660BK.html"],
  ["Rhino-Rack MasterFit Roof Box 440L (Rhino-Rack)", "https://www.rhinorack.com/en-us/products/roof-racks/roof-boxes/roof-boxes/masterfit-roof-box-440l-black-_rmft440"],
  ["Thule Motion 3 XXL (Thule)", "https://www.thule.com/en-us/cargo-carrier/car-top-carrier/thule-motion-3-xxl-_-639950"],
  ["Thule Motion 3 spread and warranty (etrailer)", "https://www.etrailer.com/Roof-Box/Thule/TH59PN.html"],
  ["SportRack Vista XL (SportRack)", "https://www.sportrack.com/product/vista-xl-cargo-box/"],
  ["Cargo box fuel economy impact (fueleconomy.gov)", "https://www.fueleconomy.gov/feg/driveHabits.jsp"],
 ],
}

# Product list for this page (boxes + Sequoia crossbars). (asin, name, brand, band, cond, note)
FITS = [
 ("B001PUZXGK","Yakima SkyBox 16 Carbonite Rooftop Cargo Box, 16 cu ft (15 in tall)","Yakima","$550–$750",{},"Universal box; confirm spread on your bars and garage clearance."),
 ("B06VX9L59C","INNO BRM660BK Wedge Cargo Box - 11 Cubic FT (Gloss Black)","INNO","$850–$1,000",{},"Universal box, 11 in tall; confirm 24-39 in spread on your bars."),
 ("B07B4P7WYX","Rhino-Rack MasterFit Roof Box 440L (15.5 cu ft), Black","Rhino-Rack","See listing",{},"Universal box, 38.6 lb; confirm mounting kit suits your bars."),
 ("B0F8PNL8H9","Thule Motion 3 XXL 21 cu ft Rooftop Cargo Box with GoPack Duffel Set, 165 lb load capacity","Thule","$1,200–$1,500",{},"Bundle listing, 57.2 lb box; confirm roof figure in manual before loading."),
 ("B083KP48XC","Yakima GrandTour 16 Premium Rooftop Cargo Box, 16 cu ft, dual-side opening","Yakima","$700–$900",{},"Universal box, 18 in tall; confirm garage clearance and spread."),
 ("B00BCLL8C0","SportRack Vista XL Rear Opening Cargo Box, 18 cu ft, Black","SportRack","$400–$500",{},"Rear opening on a tall roof; confirm box weight and load rating."),
 ("B0C26KKRF3","Genuine Toyota Sequoia Roof Rack Cross Bars PT767-0C660","Toyota","See listing",{"roof_type":"raised-rails"},"OEM bars for 2023-on Sequoia rails; confirm load rating and spread with dealer."),
 ("B0DJZZLPPT","ROSY PIXEL Roof Rack Cross Bars for Toyota Sequoia 2023-2026, 165 lbs, aluminum","ROSY PIXEL","See listing",{"roof_type":"raised-rails"},"Budget bars; 165 lb is a listing claim, confirm rail type and roof figure."),
]
