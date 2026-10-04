"""Long-form article — Best Rooftop Cargo Boxes for 2023–2026 Honda CR-V (6th gen).
Mirrors the approved cargo-box pages (RAV4, Telluride). No invented hands-on testing: box specs come from Thule,
Rhino-Rack, Yakima, SportRack and etrailer pages fetched 2026-09-27; vehicle facts from db/migrations/003_vehicles.sql
(bare roof, hybrid shares fit, 1.25 in hitch) plus etrailer's CR-V roof-type listing and Honda accessory-rail parts pages.
Boxes are universal; the CR-V-specific part is the bare roof (clamp kits) vs Honda's accessory rails (165 lb total),
fixed clamp spread, and a compact roof in front of the liftgate.
Source fixes 2026-10-04: roof statements now follow Honda's 2023 and 2026 specification tables (black roof rails standard on the hybrid trims, none on LX, EX and EX-L), so the hybrid FAQ, takeaways, fit_table and look_for no longer say hybrids share the bare-roof setup; the hitch-carrier FAQ and verdict no longer call the CR-V hitch 1.25 in (the aftermarket hitches in the hitch guide are 2 in; Honda rates towing at 1,500 lb gas and 1,000 lb hybrid); the reference to a CR-V roof rack page that does not exist was removed.
"""

KEY = ("honda", "cr-v", "2023-present", "cargo-boxes")

TITLE = "Best Rooftop Cargo Boxes for 2023–2026 Honda CR-V: 6 Picks for Its Bare Roof and Compact Hatch"
META = ("Five Thule, Rhino-Rack, INNO, Yakima and SportRack boxes plus bare-roof crossbars for the 6th-gen CR-V: "
        "clamp kits, 165 lb rail limit, liftgate fit.")

FAQ = [
 ("Does the 2023–2026 Honda CR-V have roof rails?",
  "It depends on the trim. Honda's 2023 and 2026 specifications list black roof rails as standard on the hybrid trims (Sport, TrailSport, Sport-L and Sport Touring) and none on the gas LX, EX and EX-L. We did not read Honda's 2024 or 2025 tables. etrailer's fit guide splits the 2023 CR-V into two roof types: no rails or crossbars, and flush rails that run front to back. Honda also sells accessory rails (part 08L02-3A0-100, listed for 2023–2027) for a CR-V without them. Look at your roof: a smooth roof needs a clamp kit, and rails need a flush-rail kit."),
 ("How much weight can a CR-V roof box carry?",
  "Honda's accessory roof rails are marked 165 lb total capacity, and that total covers the crossbars, the box and everything inside it. On a bare roof, use the lower of your owner's manual figure and the clamp kit's rating. The boxes on this page weigh 31 lb (Thule Pulse 2 M) to 47 lb (SkyBox 16), so after a set of bars a CR-V typically has roughly 100 to 120 lb left for gear. Soft bags, yes; a full cooler, no."),
 ("What crossbars do I need for a bare-roof CR-V?",
  "A kit whose feet clamp into the door openings and whose fit kit is listed for the 2023 and later CR-V. etrailer lists the Yakima BaseLine with JetStream bars, the Thule WingBar Evo and a steel INNO Square Bar kit for the bare-roof 2023 CR-V. Budget bars such as the Wonderdriver set on this page name the CR-V in their listing. Bars made for the 2017–2022 CR-V don't carry over; our fitment data flags that older racks don't fit."),
 ("What size cargo box fits a 2023–2026 CR-V?",
  "Think length first. The CR-V is a compact SUV, and its liftgate swings up toward the back of a short roof. The Thule Pulse 2 M (68.9 in, 14 cu ft) and the SportRack Vista XL (63 in, 18 cu ft) sit well forward. The Rhino-Rack MasterFit 440L (76 in) and INNO Wedge Plus (80 in) still fit most setups if mounted forward, while an 81 in box like the SkyBox 16 needs a careful liftgate check."),
 ("Will a roof box hit the CR-V liftgate?",
  "A long box mounted too far back can. Mount the box as far forward as the windshield allows, then open the liftgate slowly the first time and watch the gap at the tail of the box. Thule publishes a front-clearance figure for each box, more than 44 13/16 in for the Pulse 2 M, so you can measure your CR-V before buying. If your trim has a power liftgate with a height setting, a lower opening height adds margin."),
 ("Does a roof box fit the CR-V Hybrid?",
  "Yes. A box clamps to crossbars, so every box here fits once the bars are on. The bars are what differ: Honda's 2023 and 2026 specifications list black roof rails on the hybrid trims, so a hybrid takes a kit made for rails, not the door-clamp kit a bare-roof gas CR-V needs. Look at your roof and confirm the kit in the maker's fit guide. The trade-off is efficiency: any roof box adds drag, which shows up as lower mpg on a gas or hybrid CR-V. Take the box off between trips if you don't need it."),
 ("Can I use the cheaper budget boxes with a door-clamp kit?",
  "Check the spread before you buy. Clamp kits on a bare roof sit at fixed points on the door openings, so the distance between the bars is set by the kit, not by you. Boxes with a wide range, such as the Rhino-Rack MasterFit 440L (620–930 mm, about 24.4 to 36.6 in) or the Yakima SkyBox 16 (24–34.5 in), are easier to match. The SportRack Vista XL mounts only at 25-7/8, 27-7/8 or 29-7/8 in, so confirm your kit lands on one of those."),
 ("Are the Honda accessory roof rails worth adding?",
  "They are if you want flexibility. Honda's rails (08L02-3A0-100) are listed for the 2023–2027 CR-V with a list price of $435 at one Honda parts dealer, and they're marked 165 lb total capacity. With rails, flush-rail crossbars from Yakima or Thule can slide to suit a box's spread. Without them, a clamp kit is cheaper and works fine for occasional trips; just accept a fixed spread."),
 ("Can I carry skis in a roof box on a CR-V?",
  "Yes, if the box is long enough. Yakima rates the SkyBox 16 for skis and boards up to 185 cm, while the short Thule Pulse 2 M takes skis up to 155 cm. Longer skis mean a longer box, and on a compact roof that's exactly where liftgate clearance gets tight, so measure before you choose a ski box."),
 ("Is a roof box or a hitch cargo carrier better on a CR-V?",
  "Honda rates the sixth-gen CR-V at 1,500 lb of towing on gas trims and 1,000 lb on hybrids, and we could not confirm that any CR-V ships with a receiver, so a hitch carrier usually means adding a hitch first. The aftermarket hitches in the CR-V hitch guide have a 2 in receiver. A roof box keeps the rear camera and liftgate clear, locks, and keeps gear dry, but it costs roof weight and mpg. For soft bags and skis, go roof; for a small cooler or bins, a hitch carrier within the tongue-weight limit in your owner's manual works."),
]

ARTICLE = {
 "dek": "Six picks for the sixth-generation CR-V: five rooftop boxes from Thule, Rhino-Rack, INNO, Yakima and SportRack, from a 68.9 in Pulse 2 M to an 81 in SkyBox 16, plus a set of crossbars listed for the CR-V. For each box we list volume, length, weight and crossbar spread, and what those numbers mean for a bare roof, Honda's accessory rails and the compact liftgate.",
 "author": "jake-morrison",
 "reviewed": "2026-09-27",
 "method": "We did not mount these boxes ourselves. We ranked them on the makers' published specs (Thule, Rhino-Rack, Yakima and SportRack: volume, exterior dimensions, box weight, load rating, crossbar spread, ski length, front clearance), on etrailer's figures for the INNO and SportRack boxes and its CR-V roof-type guide, on Honda accessory-rail parts listings, and on how those specs fit the CR-V's bare roof and liftgate. Prices were checked on the makers' stores, REI and etrailer in September 2026. Amazon prices move daily, so the button shows the live price.",
 "takeaways": [
  "**Gas trims have a bare roof; hybrids have rails.** Honda's 2023 and 2026 tables list black roof rails on the hybrid trims only. A bare roof needs a door-clamp crossbar kit listed for the 2023+ CR-V, or Honda's accessory rails plus flush-rail bars; a roof with rails needs a kit made for them. Racks for the 2017–2022 CR-V don't carry over.",
  "**Clamp kits fix the spread.** Bars on a bare roof sit where the kit puts them, so pick a box with a wide spread range. The SportRack Vista XL's fixed positions need checking.",
  "**Short boxes suit the short roof.** The Thule Pulse 2 M is 68.9 in and the Vista XL 63 in; an 81 in SkyBox 16 needs a careful liftgate check.",
  "**165 lb total on Honda's rails.** The rails are marked 165 lb total capacity. Bars, box and gear all count, so a 31–47 lb box leaves roughly 100–120 lb for cargo.",
  "**Hybrids take the same boxes, not always the same bars.** Sport, TrailSport, Sport-L and Sport Touring hybrids have black roof rails in Honda's 2023 and 2026 tables, so check the roof before buying bars.",
 ],
 "top_picks": [
  {"asin": "B0G8C5LHQ5", "role": "Best overall", "why": "Thule Pulse 2 M: 68.9 in, 31 lb, 165 lb rating, 14 cu ft"},
  {"asin": "B07B4P7WYX", "role": "Most space for the weight", "why": "Rhino-Rack MasterFit 440L: 15.5 cu ft, 38.6 lb, wide 24.4–36.6 in spread"},
  {"asin": "B00BCLL8C0", "role": "Best budget", "why": "SportRack Vista XL: 18 cu ft in 63 in for $449.95"},
  {"asin": "B001PUZXGK", "role": "Best for skis", "why": "Yakima SkyBox 16: 185 cm skis, 15 in tall, 24–34.5 in spread"},
  {"asin": "B0CRR2R73W", "role": "Budget crossbars", "why": "Wonderdriver bars whose listing names the 2023–2026 CR-V EX, LX, EX-L"},
 ],
 "fit_table": {
  "caption": "2023–2026 CR-V roof setups (what you need before any box goes on)",
  "head": ["Roof", "How to tell", "Crossbars needed", "Box notes"],
  "rows": [
   ["Bare roof (gas LX, EX and EX-L in Honda's 2023 and 2026 tables)", "Smooth roof, no rails", "Door-clamp kit listed for 2023+ CR-V (Yakima BaseLine, Thule WingBar Evo, INNO, budget bars)", "Fixed spread; pick a box with a wide range"],
   ["Honda accessory rails (08L02-3A0-100)", "Low-profile rails front to back", "Flush-rail kit (Yakima SightLine, Thule WingBar Evo flush) or Honda crossbars", "Bars slide to suit the box"],
   ["Hybrid trims", "Sport, TrailSport, Sport-L, Sport Touring: black roof rails in Honda's 2023 and 2026 tables", "A kit made for rails; confirm the rail profile in the maker's fit guide", "Same boxes"],
   ["2017–2022 CR-V racks", "Previous generation", "Do not fit the 2023+", "Boxes carry over; bars don't"],
   ["All 2023–2026", "Honda rails marked 165 lb total", "Weigh the bars", "Bars + box + gear under the lower of manual and kit ratings"],
  ],
 },
 "look_for": [
  {"h": "Bare roof or Honda accessory rails",
   "body": "Honda's 2023 and 2026 specifications list no roof rails on the gas LX, EX and EX-L and black roof rails on the hybrid trims, and etrailer's fit guide splits the 2023 CR-V into two roof types: no rails at all, or flush rails that run front to back. Honda also sells accessory rails, part 08L02-3A0-100, listed for 2023–2027. On a bare roof you need a kit whose feet clamp into the door openings, such as the Yakima BaseLine, Thule WingBar Evo or INNO kits etrailer lists. With the rails fitted, a flush-rail kit or Honda's own crossbars go on instead. Every box here clamps to either once bars are on. Racks for the 2017–2022 CR-V don't carry over."},
  {"h": "The 165 lb total and the box's own weight",
   "body": "Honda marks its accessory roof rails at 165 lb total capacity, which covers everything above them: crossbars, box and gear. On a bare roof, the working limit is the lower of your owner's manual figure and the clamp kit's rating, so check both. Budget bar listings often quote 220 lb or more, but those are bar claims, not the roof's limit. The boxes here weigh 31 lb (Thule Pulse 2 M), 38.6 lb (MasterFit 440L), 44 lb (INNO Wedge Plus) and 47 lb (SkyBox 16). After the bars, a CR-V has roughly 100 to 120 lb left for cargo."},
  {"h": "Fixed spread on door-clamp kits",
   "body": "Clamp kits sit on fixed points at the door openings, so the space between the bars is set by the kit and the car, not by you. That makes a box's spread range important. Rhino-Rack gives 620 to 930 mm (about 24.4 to 36.6 in) for the MasterFit 440L, and Yakima gives 24–34.5 in for the SkyBox 16. The SportRack Vista XL has only three positions, 25-7/8, 27-7/8 and 29-7/8 in, per etrailer. Thule doesn't publish a spread for the Pulse 2 M; check it with Thule's fit guide. Measure your installed bars center to center before ordering."},
  {"h": "Box length vs the compact liftgate",
   "body": "On a compact SUV, length matters more than volume. The CR-V's liftgate swings up toward the back of a short roof, and a long box mounted too far back sits in its path. The boxes here run from 63 in (SportRack Vista XL) and 68.9 in (Thule Pulse 2 M) to 76 in (MasterFit 440L), 80 in (INNO Wedge Plus) and 81 in (SkyBox 16). Thule lists a front-clearance figure of more than 44 13/16 in for the Pulse 2 M, which you can measure against your CR-V. Mount every box forward and open the liftgate slowly the first time."},
  {"h": "Drag, noise and the hybrid",
   "body": "Any roof box adds drag, and on a CR-V Hybrid that shows up as lost mpg on every trip, not only the ones where the box is full. Low, narrow boxes help: the INNO Wedge Plus is 13-3/4 in tall and the Pulse 2 M is 32.1 in wide. Mounting the box level and centered, with the nose forward, keeps wind noise down. The simplest fix is to take the box off between trips. Thule's PowerClick mounts and Yakima's quick-release hardware make that a few minutes' work."},
 ],
 "look_table": {
  "head": ["Feature", "Look for", "Avoid"],
  "rows": [
   ["Crossbars", "A kit listed for the 2023+ CR-V and your roof (bare or accessory rails)", "2017–2022 CR-V racks"],
   ["Crossbar spread", "A wide range (MasterFit 440L: about 24.4–36.6 in) for fixed clamp kits", "Fixed-position boxes without measuring your bars"],
   ["Length", "Under about 76 in for the most liftgate room (Pulse 2 M: 68.9 in)", "Long ski boxes without checking the hatch"],
   ["Box weight", "Under 40 lb to save the 165 lb total for gear", "Heavy boxes on a light-duty roof"],
   ["Opening", "Dual-side, so you load from the curb", "Single-side boxes on a street-parked car"],
   ["Warranty", "Limited lifetime (Yakima, INNO) or 5 years (Rhino-Rack)", "No terms stated; ask the seller"],
  ],
 },
 "types_table": {
  "caption": "Box sizing for the CR-V (makers' published specs; INNO and SportRack figures per etrailer)",
  "head": ["Box", "Volume", "L × W × H", "Box weight", "Crossbar spread", "Liftgate guidance"],
  "rows": [
   ["Thule Pulse 2 M", "14 cu ft", "68.9 × 32.1 × 16.6 in", "31 lb", "Not published; confirm", "Front clearance over 44 13/16 in"],
   ["Rhino-Rack MasterFit 440L", "15.5 cu ft", "76 × 32 × 17 in", "38.6 lb", "620–930 mm (about 24.4–36.6 in)", "Mount forward"],
   ["INNO Wedge Plus", "13 cu ft", "80 × 33 × 13-3/4 in", "44 lb", "Not published; confirm", "Mount forward, test the hatch"],
   ["Yakima SkyBox 16 Carbonite", "16 cu ft", "81 × 36 × 15 in", "47 lb", "24–34.5 in", "Longest here; test the hatch"],
   ["SportRack Vista XL", "18 cu ft", "63 × 38 × 19 in", "Not published", "Fixed at 25-7/8, 27-7/8 or 29-7/8 in", "Shortest; rear-opening lid"],
  ],
 },
 "picks": [
  {"asin": "B0G8C5LHQ5", "role": "Best overall", "price": "$699.95",
   "pros": ["68.9 in long, well clear of the compact liftgate", "31 lb, the lightest box here", "Thule rates it for 165 lb of cargo", "Dual-side opening with central locking", "PowerClick mounts with a torque indicator"],
   "cons": ["14 cu ft, not 16", "Skis only up to 155 cm", "Thule doesn't publish a crossbar spread; confirm with its fit guide"],
   "body": "The Thule Pulse 2 M is sized for a roof like the CR-V's. Thule lists it at 400 L (14 cu ft) with exterior dimensions of 68.9 x 32.1 x 16.6 in, a 31 lb box weight and a 165 lb maximum load. It opens from both sides, locks centrally, and clamps on with PowerClick mounts whose torque indicator clicks when the box is secure. The shell is ASA-ABS plastic, and Thule and REI both list it at $699.95.\n\nOn a CR-V, the length and the weight are what matter. At 68.9 in it sits well forward on a compact roof, and Thule gives a front-clearance figure of more than 44 13/16 in, which you can measure against your CR-V to confirm the liftgate clears. At 31 lb it leaves the most of Honda's 165 lb rail total for gear, roughly 120 lb after a typical set of bars. The trade-offs are volume and ski length: 14 cu ft suits weekend bags and a stroller, and skis over 155 cm won't fit. Thule doesn't publish a crossbar spread on the product page, so check your clamp kit's spacing against Thule's fit guide before ordering.",
   "who": "CR-V owners who want a light, short box that stays clear of the liftgate.",
   "specs": [["Volume", "400 L / 14 cu ft"], ["Exterior", "68.9 × 32.1 × 16.6 in"], ["Box weight", "31 lb"], ["Max load", "165 lb"], ["Ski length", "Up to 155 cm"], ["Front clearance", "Over 44 13/16 in (Thule)"], ["Mount / lock", "PowerClick / central locking"], ["Crossbar spread", "Not published; confirm"]]},
  {"asin": "B07B4P7WYX", "role": "Most space for the weight", "price": "Confirm on listing",
   "pros": ["15.5 cu ft at 38.6 lb", "Wide 620–930 mm spread suits fixed clamp kits", "165 lb rated load", "Dual-side opening, three locking points", "5-year warranty"],
   "cons": ["76 in long; mount it forward", "Rhino-Rack's page doesn't list a price", "Heavy Duty bars need the separate RUBK-MF kit"],
   "body": "The Rhino-Rack MasterFit 440L gives a CR-V nearly the space of a 16 cu ft box without the weight. Rhino-Rack lists it at 440 L (15.5 cu ft), 76 x 32 x 17 in and 38.6 lb, with a 165 lb (75 kg) maximum load, dual-side opening with a key lock, three locking points and a 5-year warranty. It works directly with Rhino-Rack's Vortex and Euro bars and needs a separate RUBK-MF fitting kit for its Heavy Duty bars, so confirm the hardware suits your bar shape on the listing.\n\nIts best feature on a bare-roof CR-V is the spread range. Rhino-Rack gives a minimum crossbar spacing of 620 mm and a maximum of 930 mm, about 24.4 to 36.6 in, one of the widest windows here. That matters because a door-clamp kit fixes the distance between the bars, and a wide window gives the best chance the box lines up without moving anything. At 76 in, mount it forward and check the liftgate gap. At 38.6 lb it leaves roughly 110 lb of Honda's 165 lb rail total for gear. Rhino-Rack's page doesn't show a price, so compare on the listing.",
   "who": "Bare-roof CR-V owners who want the most space with the least spread and weight risk.",
   "specs": [["Volume", "440 L / 15.5 cu ft"], ["Exterior", "76 × 32 × 17 in"], ["Box weight", "38.6 lb"], ["Max load", "165 lb (75 kg)"], ["Crossbar spread", "620–930 mm (about 24.4–36.6 in)"], ["Opening", "Dual-side, key lock"], ["Locking points", "3"], ["Warranty", "5 years"]]},
  {"asin": "B00BCLL8C0", "role": "Best budget", "price": "$449.95",
   "pros": ["18 cu ft for $449.95 at SportRack, the most volume here", "63 in long, the shortest box here", "Tool-free mounting hardware and a lock", "Fits square, round and most factory bars, per SportRack", "Rear opening keeps you out of traffic"],
   "cons": ["Mounts only at 25-7/8, 27-7/8 or 29-7/8 in (etrailer)", "38 in wide and 19 in tall", "Box weight, load rating and warranty not published; confirm"],
   "body": "The SportRack Vista XL is the budget box that suits a compact roof. SportRack lists the SR7018 at 63 x 38 x 19 in with 18 cu ft, UV-resistant ABS, tool-free mounting hardware and a lock, for $449.95. The shape is the point: short and wide instead of long, so it holds more than any other box here while sitting far forward of the CR-V's liftgate. It is 5.9 in shorter than the Thule Pulse 2 M and 18 in shorter than the SkyBox 16.\n\nThe spread is the thing to check on a CR-V. etrailer gives three fixed mounting positions, 25-7/8, 27-7/8 and 29-7/8 in center to center. With Honda's accessory rails and a flush-rail kit you can slide the bars to one of them, but a door-clamp kit on a bare roof puts the bars where the kit dictates, so measure your installed bars first. The lid opens at the rear, which SportRack pitches as loading away from traffic. SportRack's page doesn't publish a box weight, a load rating or warranty terms, so confirm all three before planning a load against the 165 lb rail total.",
   "who": "Budget buyers whose bars land on one of the Vista XL's mounting positions.",
   "specs": [["Volume", "18 cu ft"], ["Exterior", "63 × 38 × 19 in"], ["Opening", "Rear"], ["Mounting positions", "25-7/8, 27-7/8 or 29-7/8 in (etrailer)"], ["Hardware", "Tool-free; lock included"], ["Material", "UV-resistant ABS"], ["Box weight / max load", "Not published; confirm"], ["Price", "$449.95 (SportRack)"]]},
  {"asin": "B001PUZXGK", "role": "Best for skis", "price": "$599",
   "pros": ["Skis and boards up to 185 cm", "15 in tall, low for its volume", "24–34.5 in spread", "Dual-side opening, SuperLatch, SKS locks", "$599 on sale at Yakima (regular $749); limited lifetime warranty"],
   "cons": ["81 in long, the longest box here", "47 lb, the heaviest box here", "36 in wide, filling most of the bars"],
   "body": "If you ski, the SkyBox 16 Carbonite is the CR-V box that takes full-length skis. Yakima lists it at 81 x 36 x 15 in with 16 cu ft and 47 lb, with skis and boards up to 185 cm, dual-side opening, SuperLatch security, SKS locks and a limited lifetime warranty. Yakima says it installs without assembly and fits most crossbars, including factory bars. It was on sale for $599 (regular $749) on Yakima's store when we checked, and Yakima builds it in the USA with up to 80% recycled material.\n\nOn a CR-V, length is the catch. At 81 in it reaches further back than any other box here, so mount it as far forward as the windshield allows and open the liftgate slowly the first time. Its 24–34.5 in spread range suits most flush-rail and clamp kits, but measure your installed bars to be sure. The 15 in height keeps it low for its volume, which helps with drag and garages. At 47 lb, it leaves roughly 100 lb of Honda's 165 lb rail total for gear after the bars.",
   "who": "Skiers and snowboarders who need 185 cm of length and can mount the box well forward.",
   "specs": [["Volume", "16 cu ft"], ["Exterior", "81 × 36 × 15 in"], ["Box weight", "47 lb"], ["Crossbar spread", "24–34.5 in"], ["Opening", "Dual-side"], ["Ski length", "Up to 185 cm"], ["Lock", "SKS, SuperLatch"], ["Warranty", "Limited lifetime"]]},
  {"asin": "B0B57PG4LR", "role": "Lowest profile", "price": "About $888",
   "pros": ["13-3/4 in tall, the lowest box here", "Tool-free Memory Mount clamps", "Fits round, square, aero, elliptical and most factory bars", "Dual-side opening; key can't come out unless the lid is shut", "Limited lifetime warranty"],
   "cons": ["13 cu ft for a premium price", "110 lb cargo limit (per etrailer)", "80 in long; test the liftgate"],
   "body": "The INNO Wedge Plus is the low-drag choice for a CR-V. etrailer lists it at 80 x 33 x 13-3/4 in with 13 cu ft, a 44 lb box weight and a 110 lb cargo capacity, with a dual-side opening lid, push-button handles and a lock whose key can't be removed unless the lid is properly closed. Its Memory Mount clamps go on without tools and fit round, square, aero, elliptical and most factory crossbars. INNO backs it with a limited lifetime warranty. etrailer's figures are for the BRM864, which the BRM865 in this listing replaces, and etrailer listed it at $888.11.\n\nOn a CR-V, the low profile is the point. At 13-3/4 in tall it sits closer to the roof than any other box here, which means less wind noise and less drag, useful on a hybrid that you drive every day with the box on. At 33 in wide, it leaves a little bar space. The trade-offs are volume and length: 13 cu ft for close to $900, and 80 in that needs a liftgate check. Its 110 lb cargo limit fits inside Honda's 165 lb rail total with the 44 lb box and bars, but only just, so weigh your load. Confirm the spread against your bars on the listing.",
   "who": "Hybrid and daily drivers who keep the box on and want the lowest drag and noise.",
   "specs": [["Volume", "13 cu ft"], ["Exterior", "80 × 33 × 13-3/4 in (etrailer)"], ["Box weight", "44 lb"], ["Max load", "110 lb"], ["Mount", "Memory Mount, tool-free"], ["Opening", "Dual-side"], ["Crossbar spread", "Not published; confirm"], ["Warranty", "Limited lifetime"]]},
  {"asin": "B0CRR2R73W", "role": "Budget crossbars", "price": "Confirm on listing",
   "pros": ["Listing names the 2023–2026 CR-V EX, LX and EX-L", "Aluminum bars with anti-theft locks", "Far cheaper than a Yakima or Thule clamp kit", "Needed before any box goes on", "Black finish to match the roof"],
   "cons": ["The 330 lb figure in the title is a bar claim, not the roof limit", "No maker spec sheet for spread or bar weight; confirm", "Confirm it's the bare-roof version for your car"],
   "body": "A box needs crossbars, and on a gas CR-V that means a kit for a bare roof. The Wonderdriver bars are the budget option: the listing names the 2023–2026 CR-V EX, LX and EX-L, and describes heavy-duty aluminum bars with anti-theft locks. For a brand-name kit, etrailer lists the Yakima BaseLine with JetStream bars at $694.80, the Thule WingBar Evo at $704.85 and a steel INNO Square Bar kit at $468.34 for the bare-roof 2023 CR-V, and flush-rail versions for CR-Vs with Honda's accessory rails.\n\nTreat the listing's numbers with care. The 330 lb figure in the title is what the seller claims for the bars; the roof's limit is what counts, and Honda marks its accessory rails at 165 lb total. Use the lower of your owner's manual figure and the bar rating, and count the bars, box and gear against it. There is no maker spec sheet, so confirm the bar weight, the bar length and the spread the feet produce on your CR-V before choosing a box, and confirm on the listing that it's the version for your roof.",
   "who": "Bare-roof CR-V owners who need bars first and want to spend less than a Yakima or Thule kit.",
   "specs": [["Fits (per listing)", "2023–2026 CR-V EX, LX, EX-L"], ["Material", "Aluminum"], ["Lock", "Anti-theft"], ["Listed load", "330 lb (bar claim)"], ["Honda rail rating", "165 lb total (accessory rails)"], ["Spread / bar weight", "Not published; confirm"]]},
 ],
 "install": [
  "Identify your roof: smooth (bare) or with Honda's accessory rails. Fit a clamp kit listed for the 2023+ CR-V on a bare roof, or a flush-rail kit on the rails, and torque it to spec.",
  "Measure the installed bars center to center and check the number against the box's spread range (about 24.4–36.6 in for the MasterFit 440L, or one of the Vista XL's fixed positions).",
  "Lift the box on with a helper, center it side to side, and slide it as far forward as the windshield and antenna allow.",
  "Fit the clamps loosely, open the liftgate slowly and check the gap at the tail of the box, then tighten the clamps to the box maker's instructions.",
  "Lock the box and mounts, rock it from each corner, and re-check the clamps after the first drive.",
  "Keep bars + box + gear under the lower of your manual's figure and the bar rating (165 lb total on Honda's accessory rails), with heavy items low and between the bars.",
 ],
 "avoid": [
  {"h": "Racks for the 2017–2022 CR-V", "body": "The sixth-gen CR-V has a new body, and our fitment data flags that older racks don't fit. Buy bars listed for 2023 and later."},
  {"h": "Assuming clamp bars can move", "body": "A door-clamp kit fixes the spread. Pick a box with a wide range, or measure your bars before buying a fixed-position box like the Vista XL."},
  {"h": "Planning around a bar's 330 lb claim", "body": "Honda's accessory rails are marked 165 lb total. The lower figure applies to bars, box and gear together."},
  {"h": "An 81 in box without a liftgate check", "body": "Long boxes reach toward the liftgate's arc on a compact roof. Mount forward and open the liftgate slowly the first time."},
 ],
 "verdict": {
  "thesis": "Fit a crossbar kit for your CR-V's roof, then choose the Thule Pulse 2 M for the shortest, lightest box, the Rhino-Rack MasterFit 440L for more space, or the SportRack Vista XL on a budget.",
  "body": "On the sixth-gen CR-V, the roof sets the rules: gas trims have a bare roof that takes a door-clamp kit with a fixed spread, hybrid trims have rails in Honda's tables, and Honda's accessory rails are marked 165 lb total. The Thule Pulse 2 M fits that best, with 14 cu ft in a 68.9 in shell at 31 lb. The Rhino-Rack MasterFit 440L adds space and has one of the widest spread ranges here, which suits fixed clamp kits. The SportRack Vista XL gives 18 cu ft for $449.95 if your bars land on one of its three positions, the SkyBox 16 is the ski box if you mount it well forward, and the INNO Wedge Plus is the low-drag option for a hybrid that keeps its box on.\n\nStart with the bars: a clamp kit for a bare roof or a kit made for rails, confirmed in the maker's fit guide. For a cooler or bins, a trailer hitch takes a small hitch cargo carrier within the tongue-weight limit in your owner's manual. The vehicle hub lists every fit-checked accessory for your CR-V.",
 },
 "sources": [
  ["2026 Honda CR-V Specifications & Features: roof rails and towing by trim (Honda Newsroom)", "https://hondanews.com/en-US/honda-automobiles/releases/release-2ecca7d29f72bf212c56033cca000993-2026-honda-cr-v-specifications-features-updated"],
  ["2023 Honda CR-V Specifications & Features: roof rails and towing by trim (Honda Newsroom)", "https://hondanews.com/en-US/honda-automobiles/releases/release-74895511bca6e7abc42504d7581990ac-2023-honda-cr-v-specifications-features"],
  ["2023 Honda CR-V roof types and crossbar kits (etrailer)", "https://www.etrailer.com/roof-2023_honda_cr-v.htm"],
  ["Honda CR-V accessory roof rails 08L02-3A0-100, 165 lb total (Bernardi Parts)", "https://www.bernardiparts.com/Products/Honda-Roof-Rails-(CRV-2023-2026)__08L02-3A0-100.aspx"],
  ["Thule Pulse 2 M (Thule)", "https://www.thule.com/en-us/cargo-carrier/car-top-carrier/thule-pulse-2-m-_-610250"],
  ["Thule Pulse 2 M (REI)", "https://www.rei.com/product/C07625/thule-pulse-2-m-roof-box"],
  ["Rhino-Rack MasterFit Roof Box 440L (Rhino-Rack)", "https://www.rhinorack.com/en-us/products/roof-racks/roof-boxes/roof-boxes/masterfit-roof-box-440l-black-_rmft440"],
  ["Yakima SkyBox 16 Carbonite (Yakima)", "https://yakima.com/collections/roof-boxes/products/skybox-16-carbonite-2014-2023"],
  ["INNO Wedge Plus 13 cu ft (etrailer)", "https://www.etrailer.com/Roof-Box/Inno/INBRM864MBK.html"],
  ["SportRack Vista XL (SportRack)", "https://www.sportrack.com/product/vista-xl-cargo-box/"],
  ["SportRack Vista XL mounting positions (etrailer)", "https://www.etrailer.com/question-156482.html"],
 ],
}

# Product list for this page (boxes + CR-V crossbars). (asin, name, brand, band, cond, note)
FITS = [
 ("B0G8C5LHQ5","Thule Pulse 2 M Roof-Mounted Box, 14 Cubic Ft, Dual-Side Opening","Thule","$650–$750",{},"Universal box, 68.9 in long; confirm spread with Thule's fit guide."),
 ("B07B4P7WYX","Rhino-Rack MasterFit Roof Box 440L (15.5 cu ft), Black","Rhino-Rack","See listing",{},"Universal box; wide spread suits clamp kits, confirm mounting kit."),
 ("B00BCLL8C0","SportRack Vista XL Rear Opening Cargo Box, 18 cu ft, Black","SportRack","$400–$500",{},"Fixed mounting positions; confirm your bars' spread and the load rating."),
 ("B001PUZXGK","Yakima SkyBox 16 Carbonite Rooftop Cargo Box, 16 cu ft (81 in long)","Yakima","$550–$750",{},"Universal box, 81 in; confirm liftgate gap on a CR-V."),
 ("B0B57PG4LR","INNO Wedge Plus 865 Cargo Box, 13 cu ft, Matte Black","INNO","$800–$950",{},"Universal low-profile box; confirm crossbar spread on the listing."),
 ("B0CRR2R73W","Wonderdriver Roof Rack Cross Bars for Honda CR-V EX LX EX-L 2023-2026, aluminum, lockable","Wonderdriver","See listing",{"roof_type":"bare"},"Confirm roof version, spread and bar weight."),
 ("B0BX692P1F","ANTS PART Roof Rack Cross Bars for 2023-2026 Honda CR-V & CR-V Sport Hybrid (need roof rails)","ANTS PART","See listing",{"roof_type":"flush-rails"},"Only for CR-Vs with rails fitted; confirm."),
]
