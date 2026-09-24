"""Long-form article — Best Trailer Hitches for 2017–2026 Tesla Model 3 (pre-Highland and 2024+ Highland).
Mirrors the approved pilot (ford_f150_2021_tonneau.py), adapted to hitch logic: Highland vs pre-Highland replaces
bed length, and Tesla's US rating (Tesla Shop + owner's manual) caps every hitch rating. No invented hands-on
testing: specs come from the Tesla Shop, Tesla owner's manual, CURT, Stealth Hitches and etrailer pages in
sources (checked 2026-09-24).
"""

KEY = ("tesla", "model-3", "2017-present", "hitches")

TITLE = "Best Hitches for 2017–2026 Tesla Model 3: 6 Picks for Bike Racks, Highland vs Pre-Highland"
META = ("Six Model 3 hitches for bike racks, hidden or bolt-on, matched to 2017–2023 and 2024+ Highland cars, "
        "plus Tesla's $1,300 tow package and 121 lb rack limit.")

FAQ = [
 ("Can a Tesla Model 3 tow in the US?",
  "Only the 2024 and later (Highland) cars have a US tow option from Tesla. The Tesla Shop sells a $1,300 Model 3 Tow Package for Rear-Wheel Drive and All-Wheel Drive cars built in 2024 or later, rated up to 2,200 lb, and says it is not compatible with the Model 3 Performance. Tesla's current owner's manual gives 1,650 lb without trailer brakes, 2,200 lb with them and 200 lb tongue weight. Tesla offered a tow bar on European Model 3s from 2019, but not on 2017–2023 US cars."),
 ("What is the best hitch for a Model 3 bike rack?",
  "For most owners, the Stealth Hitches rack package. Stealth lists it for the 2017–2025 Model 3, the 2 in rack receiver detaches, and nothing shows under the bumper when it's off. If you'd rather spend less and don't mind a visible receiver, CURT's 13431 is the brand-name bolt-on for 2017–2023 cars. etrailer lists it at $335.78, with 2,000 lb GTW and 300 lb tongue weight."),
 ("How much weight can a bike rack put on a Model 3?",
  "Tesla's current Model 3 owner's manual limits accessory carriers to 121 lb (55 kg) of vertical load on the 2 in receiver. That figure covers the rack and the bikes together, so a 45–50 lb two-bike platform rack leaves about 70 lb for bikes. That is fine for two light road or mountain bikes and too little for most pairs of e-bikes. Stealth rates its rack receiver higher, but the car's figure is the one to follow."),
 ("Do 2017–2023 Model 3 hitches fit the 2024 Highland?",
  "Mostly no. CURT lists 13431, 13449 and 11581 for the 2017–2023 Model 3 only, and the maXpeedingrods listing stops at 2023. The Highland refresh reshaped the rear, including taillights that no longer break between trunk and side. Stealth Hitches is the exception: it lists its SHR09001 for 2017–2025. For a 2024 or later car, buy a listing that names Highland or 2024+, such as the TIOYAR, or Tesla's own package."),
 ("Is a 1-1/4 in or 2 in receiver better on a Model 3?",
  "Two inch, for most people. More bike racks come in 2 in, and the rack stays steadier in the larger receiver. Tesla's own tow package and the Stealth hitch both use 2 in. The 1-1/4 in CURT 11581 still makes sense for a light one- or two-bike rack you already own, and it has the same 2,000 lb GTW as CURT's 2 in part, but a lower 200 lb tongue weight."),
 ("What does 'hidden hitch' mean on a Model 3?",
  "The visible parts come off when you're not using them. Stealth Hitches bolts a hitch beam and a stainless latch block behind the bumper. The 2 in rack receiver and the ball mount lock into the latch block and detach, so the car looks stock when they're out. Stealth says installation needs no welding or drilling and quotes about four hours. CURT's 13431 has a concealed cross tube, but the receiver stays under the bumper."),
 ("Can I add towing to a Stealth rack package later?",
  "Yes. Stealth sells a towing conversion kit, SHT25048, for $269 on its own store. It adds safety-chain anchors, harness and controller kits, a magnetic clip, a zero-play ball mount and a 2 in ball, and uses the same latch block as the rack receiver. On a 2017–2023 US Model 3 there is still no Tesla tow rating, so treat towing as your own decision and check your insurance and warranty position."),
 ("Do I need to remove the bumper to install a Model 3 hitch?",
  "Yes, on every hitch here. etrailer notes that CURT's 13431 needs the rear bumper fascia and an undercarriage trim panel removed, and reviewers there report tight tolerances and some trimming when the fascia goes back on. CURT rates its Model 3 hitches as a professional-level install. Stealth quotes about four hours with no welding or drilling. Tesla installs its own package at a Service Center, included in the $1,300."),
 ("Will a hitch bike rack block the Model 3's lights or trunk?",
  "A loaded rack usually covers part of the lower rear and can hide the plate. Most platform racks tilt down so the trunk opens, but check the tilt clearance on a Model 3 before you buy. Tesla's package includes a trailer harness and a 4-pin connector. With an aftermarket hitch, add a light board for the rack if your state requires visible lights and plate."),
 ("Can I use a vertical-hanging bike rack on a Model 3 hitch?",
  "Not on the CURT hitches: CURT says its Model 3 hitches are not compatible with racks that hang bikes vertically. Those racks put the most leverage on the receiver, and Tesla's 121 lb vertical limit rules out most of them once four or five bikes are loaded. Use a platform rack sized to your bikes."),
]

ARTICLE = {
 "dek": "Six hitches for the 2017–2026 Model 3, hidden and bolt-on, sorted by pre-Highland (2017–2023) and Highland (2024+) fit, with Tesla's $1,300 US tow package, its 2,200 lb rating and the 121 lb bike-rack limit that rules them all.",
 "author": "jake-morrison",
 "reviewed": "2026-09-24",
 "method": "We did not install these hitches ourselves. We ranked them on published ratings (class, receiver, gross trailer weight, tongue weight), on the Model 3 years each maker or listing names, and on install details from CURT, Stealth Hitches and etrailer. Tesla's US tow status and limits come from the Tesla Shop and Tesla's current Model 3 owner's manual. Prices were checked at Tesla, Stealth and etrailer in September 2026. Amazon prices move daily, so the button shows the live price.",
 "takeaways": [
  "**Only 2024+ Highland cars have a US tow option from Tesla:** a $1,300 package rated up to 2,200 lb, not offered on the Performance.",
  "**The bike-rack limit is 121 lb** of vertical load, per Tesla's current manual. Rack plus bikes must fit inside it.",
  "**Most aftermarket hitches are pre-Highland only.** CURT 13431, 13449 and 11581 list 2017–2023. Stealth lists 2017–2025.",
  "**Hidden or visible is the big choice.** Stealth's receiver detaches; CURT's receiver stays under the bumper.",
  "**Every install means the rear fascia comes off.** CURT calls its Model 3 hitches a professional-level install.",
 ],
 "top_picks": [
  {"asin": "B09DGB75RL", "role": "Best hidden hitch for bike racks", "why": "Detachable 2 in rack receiver; nothing shows when off; listed for 2017–2025"},
  {"asin": "B09DG9SX4S", "role": "Best if you'll also tow", "why": "Same hidden hitch plus ball mount, 4-way wiring and chain anchors"},
  {"asin": "B07YXHNHHW", "role": "Best brand-name bolt-on (2017–2023)", "why": "CURT 13431: 2 in, 2,000 lb GTW, 300 lb TW, limited lifetime warranty"},
  {"asin": "B086RQQGF2", "role": "Best 1-1/4 in", "why": "CURT 11581 for small racks; 2,000 lb GTW, 36 lb hitch"},
  {"asin": "B0FY6GS5L5", "role": "Budget pick for Highland", "why": "Listed for 2024–2026 Model 3 with a 2 in receiver"},
 ],
 "fit_table": {
  "caption": "Model 3 years and hitch options (Highland changed the rear; match the listing to your car)",
  "head": ["Years", "Tesla US tow option", "Hitches that list it", "Notes"],
  "rows": [
   ["2017–2023 (pre-Highland)", "None", "CURT 13431, 13449, 11581; Stealth SHR09001; maXpeedingrods", "No Tesla US tow rating. Use for bike racks and carriers."],
   ["2024–2025 Highland RWD / AWD", "Tow Package, $1,300, up to 2,200 lb", "Stealth SHR09001 (to 2025), TIOYAR", "Manual: 200 lb tongue weight, 121 lb carriers."],
   ["2024+ Highland Performance", "Not compatible (Tesla Shop)", "Confirm with the seller", "Treat as rack-only unless a listing names it."],
   ["2026", "Tow Package (2024+ RWD/AWD)", "TIOYAR (2024–2026)", "Stealth lists to 2025; confirm 2026."],
  ],
 },
 "look_for": [
  {"h": "Pre-Highland or Highland",
   "body": "Tesla sold the refreshed Model 3, known as Highland, in the US from January 2024. Its redesigned taillights no longer break between the trunk and the sides, and the rear changed enough that most hitches were not carried over. CURT lists its 13431, 13449 and 11581 for 2017–2023 only, and the maXpeedingrods listing stops at 2023. Stealth Hitches lists its SHR09001 for 2017–2025, and the TIOYAR is sold for 2024–2026. Check your model year on the registration, then buy the listing that names it."},
  {"h": "Tesla's US tow status",
   "body": "In the US, Tesla's tow option starts with 2024 cars. The Tesla Shop lists a $1,300 Model 3 Tow Package for Rear-Wheel Drive and All-Wheel Drive cars built in 2024 or later, rated up to 2,200 lb, with a 2 in receiver, 4-pin connector, harness and tow mode software, installed at a Service Center. It is not compatible with the Performance. Tesla sold a tow bar on European Model 3s from 2019, but 2017–2023 US cars never got a rating. For them, a hitch is a rack mount."},
  {"h": "The 121 lb bike-rack limit",
   "body": "Tesla's current owner's manual limits accessory carriers on the 2 in receiver to 121 lb of vertical load, whether or not the rear seats are full. Stealth rates its 2 in rack receiver at 350 lb and CURT's 13431 carries 300 lb tongue weight, but the car's figure is lower and it's the one that counts. A 45–50 lb two-bike platform rack leaves about 70 lb for bikes. Two e-bikes usually weigh more than that, so plan around the rack's weight first."},
  {"h": "Hidden vs visible receiver",
   "body": "The Model 3 sits low, and a receiver under the bumper is what most owners notice. Stealth's hitch beam and stainless latch block stay behind the bumper, and the rack receiver and ball mount detach, so the car looks stock when they're off. Stealth says the design doesn't scrape and doesn't cost ground clearance. CURT's 13431 has a concealed cross tube, but the receiver stays visible below the bumper. It costs less and there's nothing to take on and off."},
  {"h": "Receiver size and rack choice",
   "body": "Two inch receivers take the widest choice of platform racks and hold them more firmly. Tesla's package and Stealth's hitch are 2 in, and so is the CURT 13431. CURT's 11581 is 1-1/4 in, fine for a light rack you already own, with 2,000 lb GTW and 200 lb tongue weight. CURT says none of its Model 3 hitches take vertical-hanging bike racks, and Tesla's 121 lb limit rules out most of those anyway."},
 ],
 "look_table": {
  "head": ["Feature", "Look for", "Avoid"],
  "rows": [
   ["Fitment", "Listing names 2017–2023 or 2024+ Highland, and your drivetrain", "\"Fits Model 3\" with no years"],
   ["Receiver", "2 in for platform racks", "1-1/4 in if you plan a heavier rack later"],
   ["Ratings", "Published GTW and tongue weight, read against Tesla's 121 lb carrier limit", "Treating a hitch rating as permission to tow a pre-2024 car"],
   ["Look", "Detachable receiver if you care about the rear view", "Low-hanging receivers on a lowered car"],
   ["Install", "Maker's instructions and hardware list; professional install if unsure", "Listings with no instructions"],
   ["Lights", "Harness or light board when a rack hides the lights", "Racks that cover the plate with no board"],
  ],
 },
 "types_table": {
  "caption": "Hitch types on the Model 3",
  "head": ["Type", "Price on this page", "Visible when not in use", "Towing", "Years", "Best for"],
  "rows": [
   ["Tesla Tow Package", "$1,300 installed", "Receiver visible", "Up to 2,200 lb", "2024+ RWD/AWD", "Highland owners who tow"],
   ["Hidden (Stealth)", "$568 on Stealth's store", "No", "With tow package or $269 kit", "2017–2025", "Bike racks, clean look"],
   ["Brand-name bolt-on 2 in (CURT 13431)", "$335.78 (etrailer)", "Receiver only", "Hitch 2,000 lb; no Tesla rating pre-2024", "2017–2023", "Bike racks on a budget"],
   ["Brand-name 1-1/4 in (CURT 11581)", "About $180–$260", "Receiver only", "Hitch 2,000 lb", "2017–2023", "Light racks"],
   ["Budget 2 in", "About $120–$200", "Receiver visible", "Confirm", "By listing", "Lowest cost"],
  ],
 },
 "picks": [
  {"asin": "B09DGB75RL", "role": "Best hidden hitch for bike racks", "price": "$450–$600",
   "pros": ["Nothing visible under the bumper when the receiver is off", "Detachable 2 in rack receiver on a stainless latch block with integral lock", "Listed for 2017–2025, covering both pre-Highland and Highland", "No welding or drilling, about 4 hours (Stealth)", "Lifetime guarantee for as long as you own the car; made in the USA"],
   "cons": ["Costs more than a CURT bolt-on", "Rack only; towing needs the $269 conversion kit", "2026 cars not listed; confirm"],
   "body": "The Model 3's low, clean rear is the reason Stealth Hitches exists. The SHR09001 bolts a hitch beam behind the bumper with a stainless steel latch block and an integral lock. The 2 in rack receiver slides into the latch block and comes out when you're done, so the car looks stock between trips and there's nothing to scrape on driveways. Stealth rates the 2 in rack receiver at 350 lb and the 1-1/4 in adapter at 300 lb, says the install needs no welding or drilling, and quotes about four hours. It is finished in stainless and powder coat, made in the USA, and guaranteed for as long as you own the car.\n\nStealth lists it for the 2017–2025 Model 3, which makes it one of the few hitches that spans pre-Highland and Highland cars. Its store shows $568 for the SHR09001; this Amazon listing is the rack package, so compare what's in the box before you buy. However strong the receiver, Tesla's manual caps bike racks at 121 lb of vertical load. If you want to tow later, Stealth's SHT25048 kit adds a ball mount and wiring for $269.",
   "who": "Owners who carry bikes a few times a month and want the car to look untouched the rest of the time.",
   "specs": [["Type", "Hidden, detachable 2 in rack receiver"], ["Part #", "Stealth SHR09001"], ["Fits", "2017–2025 Model 3"], ["Rack receiver rating", "350 lb (2 in) / 300 lb (1-1/4 in adapter)"], ["Car's limit", "121 lb carriers (Tesla manual)"], ["Install", "About 4 hr, no welding or drilling"], ["Lock", "Integral lock in latch block"], ["Warranty", "Lifetime, while you own the car"], ["Made in", "USA"]]},
  {"asin": "B09DG9SX4S", "role": "Best if you'll also tow", "price": "$550–$700",
   "pros": ["Rack receiver and ball mount on the same latch block", "Includes 4-way connector with magnetic clip and harness", "Chain anchors and 2 in ball included", "Stealth rates it 3,500 lb GTW and 350 lb tongue weight", "Same hidden look as the rack package"],
   "cons": ["Hitch rating is far above Tesla's 2,200 lb (2024+) and there's no Tesla US rating for 2017–2023", "Most expensive aftermarket pick", "Doesn't include Tesla's Trailer Mode software"],
   "body": "This is the same Stealth hitch with the towing parts added. Stealth's combo package for the SHR09001 lists the bolt-up hitch beam, stainless latch with integral lock, detachable 2 in rack receiver, detachable ball mount at an 18 in standard height, 2 in ball, chain anchors, and a wiring harness with a 4-way connector on a magnetic clip. Stealth rates the hitch at 3,500 lb gross trailer weight and 350 lb tongue weight. etrailer lists a Stealth hidden hitch with towing kit at 3,500 lb and 350 lb as well.\n\nThe car sets the real limits. On a 2024 or later RWD or AWD Model 3, Tesla's own figures are 2,200 lb with trailer brakes, 1,650 lb without, and 200 lb tongue weight. On a 2017–2023 US car Tesla publishes no tow rating at all, so towing with any aftermarket hitch is your call. Buy this package if you want a bike rack now and a small trailer later without paying Tesla's $1,300, and stay under Tesla's numbers.",
   "who": "Highland owners who want a hidden rack mount now and occasional light towing within Tesla's limits.",
   "specs": [["Type", "Hidden, detachable rack receiver + ball mount"], ["Fits", "2017–2025 Model 3 (per listing)"], ["Hitch rating", "3,500 lb GTW / 350 lb TW (Stealth)"], ["Car's limit (2024+)", "2,200 lb braked / 1,650 lb unbraked / 200 lb TW"], ["Wiring", "4-way connector, magnetic clip, harness"], ["Ball mount", "Detachable, 18 in to top of ball"], ["Install", "About 4 hr, no welding or drilling"], ["Warranty", "Lifetime, while you own the car"]]},
  {"asin": "B07YXHNHHW", "role": "Best brand-name bolt-on (2017–2023)", "price": "$300–$360",
   "pros": ["Class 3, 2 in receiver for platform racks", "2,000 lb GTW and 300 lb tongue weight", "Concealed cross tube, gloss black powder coat", "Made in the USA; limited lifetime warranty", "etrailer lists it at $335.78, down from $608.95"],
   "cons": ["2017–2023 only; not for Highland", "Rear fascia and undertray come off; owners report tight refit", "Not for vertical-hanging bike racks"],
   "body": "CURT's 13431 is the straightforward choice for a pre-Highland Model 3: a fully welded Class 3 hitch with a 2 in receiver, 2,000 lb gross trailer weight and 300 lb tongue weight. The cross tube is concealed behind the bumper, the finish is gloss black powder coat, and it's made in the USA with a limited lifetime warranty. etrailer lists it at $335.78 against a regular $608.95 and fits it to the 2017–2023 Model 3 only.\n\netrailer notes the install means removing the rear bumper fascia and an undercarriage trim panel. Several reviewers there describe tight tolerances when the bumper goes back on, including trimming plastic and filing holes to line things up. Budget time or a shop. CURT says its Model 3 hitches don't take vertical-hanging bike racks. The 300 lb tongue rating is well above Tesla's 121 lb carrier limit, so use the car's number. CURT's 13449 is a similar Class 3 hitch for 2017–2023 with the same 2,000 lb and 300 lb ratings.",
   "who": "2017–2023 owners who want a brand-name 2 in receiver for a platform bike rack at a mid-range price.",
   "specs": [["Class / receiver", "Class 3, 2 in"], ["Part #", "CURT 13431"], ["Fits", "2017–2023 Model 3 (etrailer)"], ["Hitch rating", "2,000 lb GTW / 300 lb TW"], ["Car's limit", "121 lb carriers; no US tow rating pre-2024"], ["Install", "Fascia and undertray removal"], ["Warranty", "Limited lifetime"], ["Made in", "USA"]]},
  {"asin": "B086RQQGF2", "role": "Best 1-1/4 in", "price": "$180–$260",
   "pros": ["1-1/4 in receiver suits light racks you already own", "2,000 lb GTW, 200 lb tongue weight", "36 lb hitch weight", "Concealed main body, gloss black powder coat with Bonderite rust coating", "Made in Wisconsin; limited lifetime warranty"],
   "cons": ["Fewer racks come in 1-1/4 in", "2017–2023 only", "Sold here by a reseller; confirm it's CURT 11581 in the box"],
   "body": "If your bike rack already has a 1-1/4 in shank, CURT's 11581 fits the Model 3 without an adapter. It is a Class 1 hitch with a 1-1/4 in receiver, 2,000 lb gross trailer weight and 200 lb tongue weight, weighing 36 lb. The main body is concealed for a factory look, the finish is gloss black powder coat over a rust-resistant Bonderite coat, and CURT makes it in Wisconsin with a limited lifetime warranty (one year on finish and parts).\n\nCURT lists it for the 2017–2023 Model 3 and rates the install as professional. Like its other Model 3 hitches, it's not for vertical-hanging bike racks. The 200 lb tongue rating is still above Tesla's 121 lb carrier limit, so the car sets the load. This Amazon listing is from a reseller, so check the part number when it arrives. For a new rack purchase, a 2 in hitch gives you more choice.",
   "who": "Pre-Highland owners with a light 1-1/4 in rack who don't want an adapter.",
   "specs": [["Class / receiver", "Class 1, 1-1/4 in"], ["Part #", "CURT 11581"], ["Fits", "2017–2023 Model 3"], ["Hitch rating", "2,000 lb GTW / 200 lb TW"], ["Hitch weight", "36 lb"], ["Install", "Professional (CURT)"], ["Warranty", "Limited lifetime (1-yr finish, 1-yr parts)"]]},
  {"asin": "B0FY6GS5L5", "role": "Budget pick for Highland", "price": "$120–$200",
   "pros": ["Listing names the 2024, 2025 and 2026 Model 3", "2 in receiver for platform racks", "Black steel construction", "A fraction of Tesla's $1,300 package", "Covers 2026, which Stealth's listing doesn't"],
   "cons": ["Thin published specs; confirm ratings with the seller", "No wiring and no Trailer Mode", "Confirm Performance fit"],
   "body": "Highland owners have fewer choices, because most brand-name hitches stop at 2023. The TIOYAR listing is written for the 2024–2026 Model 3 and has a 2 in receiver in black steel. That makes it the cheapest way here to put a platform bike rack on a Highland, and one of the few listings that names 2026.\n\nIt doesn't publish the detail CURT and Stealth do, so ask the seller for the tongue-weight rating, what hardware comes in the box and whether the install needs trimming. For a bike rack the limit is Tesla's anyway: 121 lb of vertical load including the rack. If you plan to tow, Tesla's $1,300 package is rated to 2,200 lb for RWD and AWD cars and comes with wiring and the tow mode software. Tesla says it doesn't fit the Performance, so Performance owners should confirm fit for this hitch too.",
   "who": "2024–2026 owners who need a receiver for a bike rack and don't plan to tow.",
   "specs": [["Receiver", "2 in"], ["Fits", "2024–2026 Model 3 (per listing)"], ["Material", "Black steel"], ["Ratings", "Confirm with seller"], ["Car's limit", "121 lb carriers; 2,200 lb with Tesla package"], ["Wiring", "Not included"]]},
  {"asin": "B0FXGN3CF9", "role": "Budget pick for 2017–2023", "price": "$120–$180",
   "pros": ["Lowest price for a pre-Highland 2 in receiver", "Listing names 2017–2023 Model 3", "Class II rating is realistic for a bike-rack car", "Takes 2 in platform racks", "Leaves budget for a better rack"],
   "cons": ["Pre-Highland only", "Less install documentation than CURT", "No wiring"],
   "body": "For a pre-Highland car that will only ever carry a bike rack, the maXpeedingrods Class II hitch is the low-cost alternative to CURT's 13431. The listing names the 2017–2023 Model 3 and uses a 2 in receiver, so standard platform racks fit without an adapter. A Class II hitch is a sensible match for a car that Tesla doesn't rate to tow in the US: the realistic job is a rack within the 121 lb vertical limit, not a trailer.\n\nThe savings over CURT come from what you don't get: CURT's published ratings detail, made-in-USA welding and the lifetime warranty. Ask the seller for the instruction sheet and the hardware list, and expect the same fascia and undertray removal as any Model 3 hitch. The money saved can go toward a better rack or a light board.",
   "who": "2017–2023 owners who want the cheapest receiver for a bike rack and accept thinner specs.",
   "specs": [["Class / receiver", "Class II, 2 in"], ["Fits", "2017–2023 Model 3 (per listing)"], ["Ratings", "Confirm on listing"], ["Car's limit", "121 lb carriers; no US tow rating"], ["Install", "Fascia removal expected"], ["Wiring", "Not included"]]},
 ],
 "install": [
  "Confirm your model year and drivetrain. 2017–2023 and 2024+ Highland cars take different hitches, and Tesla's tow package excludes the Performance.",
  "For Tesla's package, book it through the Tesla Shop. Installation at a Service Center is included in the $1,300. The steps below are for aftermarket hitches.",
  "Remove the rear bumper fascia and undercarriage trim panel as the maker's sheet describes. Have a second person hold the fascia; it's wide and the clips are easy to break.",
  "Bolt the hitch beam to the mounting points and torque to the maker's figures. Stealth's latch block mounts at this stage.",
  "Refit the fascia, trimming only where the instructions say. etrailer reviewers report tight tolerances on the Model 3, so dry-fit before trimming.",
  "Load the rack and check its total weight against Tesla's 121 lb limit. Re-torque the hitch bolts after the first few hundred miles.",
 ],
 "avoid": [
  {"h": "Towing on a 2017–2023 US car as if it were rated", "body": "Tesla publishes no US tow rating for those years. A hitch rated 2,000 or 3,500 lb doesn't change that."},
  {"h": "Pre-Highland hitches on a 2024+ car", "body": "CURT's Model 3 hitches list 2017–2023. On a Highland, buy a listing that names 2024+ or use Tesla's package."},
  {"h": "Overloading the rack", "body": "Tesla's 121 lb vertical limit includes the rack. Two e-bikes on a 50 lb rack is usually over it."},
  {"h": "Vertical-hanging racks", "body": "CURT rules them out on its Model 3 hitches, and they put the most leverage on a low, short-overhang car."},
 ],
 "verdict": {
  "thesis": "For bikes, get the Stealth rack package on 2017–2025 cars or CURT's 13431 on a pre-Highland; to tow, only a 2024+ RWD or AWD with Tesla's $1,300 package has a rating.",
  "body": "The Model 3 is a bike-rack car first. Stealth's hidden hitch suits it best: it covers 2017–2025, the receiver comes off, and nothing shows. CURT's 13431 gives a brand-name 2 in receiver for less on 2017–2023 cars, and TIOYAR is the budget option for 2024–2026. Whichever you choose, Tesla's 121 lb carrier limit sets the load, and only Highland RWD and AWD cars with Tesla's package are rated to tow.\n\nA hitch bike rack keeps bikes off the glass roof and out of the airflow over it, which is why many owners pick it instead of a roof rack. Once the hitch is sorted, all-weather floor mats are the other common add-on. The vehicle hub lists every fit-checked accessory for your Model 3.",
 },
 "sources": [
  ["Model 3 Tow Package (Tesla Shop)", "https://shop.tesla.com/product/model-3-tow-package"],
  ["Model 3 Owner's Manual: Towing and Accessories (Tesla)", "https://www.tesla.com/ownersmanual/model3/en_us/GUID-BD9A38D5-4410-45A3-8337-BDF7342750F3.html"],
  ["Stealth Hitches SHR09001, 2017–2025 Model 3 (Stealth Hitches)", "https://stealthhitches.com/products/tesla-hitch-shr09001"],
  ["Stealth towing conversion kit SHT25048 (Stealth Hitches)", "https://stealthhitches.com/products/towing-conversion-kit-sht25048"],
  ["CURT 13431 Model 3 hitch (etrailer)", "https://www.etrailer.com/Trailer-Hitch/CURT/C13431.html"],
  ["CURT 13449 Class 3 hitch, Model 3 (CURT)", "https://www.curtmfg.com/part/13449"],
  ["CURT 11581 Class 1 hitch, Model 3 (CURT)", "https://www.curtmfg.com/part/11581"],
  ["2021 Tesla Model Y hitches incl. Stealth with towing kit (etrailer)", "https://www.etrailer.com/Trailer-Hitch/Tesla/Model+Y/2021/DT58MR.html?vehicleid=202120216003159"],
  ["Tesla Model 3 (Highland refresh dates, European tow bar)", "https://en.wikipedia.org/wiki/Tesla_Model_3"],
 ],
}

# Product list for this page. (asin, name, brand, band, cond, note)
FITS = [
 ("B09DGB75RL","Stealth Hitches Receiver Hitch Rack Package, 2017-2025 Tesla Model 3, hidden 2 in receiver","Stealth Hitches","$450–$600",{"year_to":2025},"Hidden receiver; bike racks within Tesla's 121 lb."),
 ("B09DG9SX4S","Stealth Hitches Receiver Hitch Rack & Tow Package, 2017-2025 Tesla Model 3","Stealth Hitches","$550–$700",{"year_to":2025},"Adds ball mount + 4-way wiring; Tesla US rating only on 2024+ RWD/AWD."),
 ("B07YXHNHHW","CURT 13431 Class 3 Trailer Hitch 2 in, 2017-2023 Tesla Model 3","CURT","$300–$360",{"year_to":2023},"Pre-Highland only; 2,000 lb GTW / 300 lb TW."),
 ("B086RQQGF2","CURT 11581 Class 1 Trailer Hitch 1-1/4 in, 2017-2023 Tesla Model 3","CURT","$180–$260",{"year_to":2023},"Reseller listing; confirm part 11581 on arrival."),
 ("B0FY6GS5L5","TIOYAR Trailer Hitch 2 in Receiver, 2024-2026 Tesla Model 3 (Highland)","TIOYAR","$120–$200",{"year_from":2024},"Confirm ratings and Performance fit with seller."),
 ("B0FXGN3CF9","maXpeedingrods Class II Hitch 2 in, 2017-2023 Model 3","maXpeedingrods","$120–$180",{"year_to":2023},"Pre-Highland only."),
]
