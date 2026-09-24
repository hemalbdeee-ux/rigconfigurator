"""Long-form article — Best Trailer Hitches for 2020–2025 Subaru Outback (6th gen, BT).
Mirrors the approved pilot (ford_f150_2021_tonneau.py). No invented hands-on testing: every spec below
comes from the manufacturer/dealer pages listed in sources (checked 2026-09-24).
"""

KEY = ("subaru", "outback", "2020-present", "hitches")

TITLE = "Best Trailer Hitches for 2020–2025 Subaru Outback: 5 Picks for 2,700 and 3,500 lb Trims"
META = ("Five 2 in hitches for the 2020–2025 Outback, from the Subaru OEM kit to CURT and Draw-Tite, with the "
        "2,700 vs 3,500 lb tow split, Wilderness fascia and wiring notes.")

FAQ = [
 ("How much can a 2020–2025 Subaru Outback tow?",
  "It depends on the engine, not the hitch. Subaru's hitch documentation lists 2,700 lb with a 270 lb maximum tongue weight for the 2.5-liter Outback, and 3,500 lb with a 350 lb tongue weight for the 2.4-liter turbo used in XT trims and the Wilderness. Every hitch on this page is rated at 3,500 lb or more, so on a 2.5-liter car the vehicle, not the hitch, sets the limit. Check the towing section of your owner's manual for your exact trim."),
 ("Does a 3,500 lb or 4,500 lb hitch let a 2.5-liter Outback tow more?",
  "No. A hitch rating is the most the hitch itself can hold. The vehicle rating covers the frame, brakes, cooling and transmission, and the lower of the two numbers always wins. The Draw-Tite 76597 is rated for 4,500 lb and 675 lb of tongue weight, but bolted to a 2.5-liter Outback it is still a 2,700 lb, 270 lb hitch. Buying a stronger hitch gives you margin and longevity, not towing capacity."),
 ("Is the Subaru factory hitch better than CURT or Draw-Tite?",
  "It is different, not stronger. The Subaru L101SAN000 is a Class II, 2 in receiver engineered around the Outback's bumper, and Subaru dealer Subaru Parts Pros lists it with a wiring harness included, which aftermarket hitches don't have. It is also the most expensive option at a $529.95 MSRP before the ball mount. CURT and Draw-Tite hitches carry higher published hitch ratings and cost much less, but you buy the wiring separately. Some owners pick the OEM part because a dealer can install it and it's covered with the car."),
 ("Does the same hitch fit the 2020–2025 Subaru Legacy?",
  "Often, yes. CURT lists both the 13494 and the 13570 for the 2020–2025 Legacy sedan as well as the Outback, because the two share the same platform and rear structure. The Draw-Tite 76597 and the Subaru L101SAN000 are listed for the Outback only, so don't assume those cross over. The tow rating does not carry over either: the Legacy has its own rating in its owner's manual, and some Subaru dealer towing guides list the Legacy as not recommended for towing. Treat a Legacy hitch as a bike rack or cargo carrier mount unless your manual says otherwise."),
 ("What changes on the Outback Wilderness?",
  "The Wilderness uses the 2.4-liter turbo, so it carries the 3,500 lb rating. Its rear bumper fascia is its own design, though. Subaru's notes for the L101SAN000 say a Wilderness-specific bumper fascia panel and a cutting template are required to install the factory hitch on a Wilderness. CURT lists the 13494 and 13570 for all Outback trims, but read the instructions for Wilderness-specific steps before you start, and confirm the Wilderness in the listing if you buy a budget brand."),
 ("Will a 2020–2025 Outback hitch fit a 2026 Outback?",
  "The 2026 Outback is a new generation. Subaru sells separate factory hitches for it (L101SAR000 for non-turbo and L101SAR001 for turbo models), which tells you the factory part changed. CURT and Draw-Tite, however, list the 13494 and 76597 for 2020–2026. If you have a 2026, trust the maker's fitment checker with your exact model year and trim, and confirm with the seller before ordering. Don't carry a 6th-gen hitch over to a new car on assumption."),
 ("Do I need to drill or cut the bumper to install one?",
  "Draw-Tite lists the 76597 as bolt-on with no drilling and about 60 minutes of install time. CURT rates the exposed-tube 13570 as an advanced install of about 90 minutes. CURT doesn't publish a drilling or trimming note for the 13494 on its product page, so read the instructions before you commit. The Subaru OEM hitch needs no trimming on standard trims, but the Wilderness requires a specific fascia panel and template cut. Any install that uses existing frame holes may still need the exhaust lowered or a heat shield moved for access."),
 ("What wiring do I need for a trailer on an Outback?",
  "Most small trailers use a 4-way flat connector for tail, brake and turn lights. The Subaru factory hitch is listed with a harness included. For CURT, Draw-Tite, and budget hitches, buy a vehicle-specific T-connector harness that plugs into the Outback's tail-light connectors, so you don't need to splice. If you plan to tow near 3,500 lb with an XT or Wilderness, check whether your trailer needs electric brakes under your state's rules; that means a 7-way connector and a brake controller."),
 ("Can I use a 2 in bike rack on the Outback?",
  "Yes. Every hitch here has a 2 in receiver, which fits most platform bike racks. The limit is tongue weight: 270 lb on the 2.5-liter car and 350 lb on the turbo. Add up the rack weight and the bikes before you load it, especially with e-bikes. CURT notes that its round-tube 13570 is an exposed design; the concealed 13494 and 76597 keep more of the receiver tucked under the bumper, which matters for rack ground clearance."),
 ("Can I tow a pop-up camper or small boat with an Outback?",
  "Within the ratings, yes. A 2.5-liter Outback can tow 2,700 lb and the XT and Wilderness up to 3,500 lb, per Subaru's hitch documentation. Weigh the loaded trailer, not the brochure dry weight, and keep tongue weight around 10–15% of trailer weight so the car stays stable. Remember that passengers and cargo also count against the Outback's payload. A small aluminum boat or a light teardrop fits well, but a camper near the limit leaves little margin on hills and in wind."),
]

ARTICLE = {
 "dek": "Five 2 in receiver hitches that fit the 6th-generation Outback, from a budget Class 3 to Subaru's own factory kit. We list hitch ratings, weight and install time, and explain why the engine under the hood, not the hitch, decides whether you can tow 2,700 or 3,500 lb.",
 "author": "jake-morrison",
 "reviewed": "2026-09-24",
 "method": "We did not install these hitches ourselves. We ranked them on published specs (class, gross trailer and tongue weight ratings, product weight, finish, warranty, install time), on the fitment each maker lists for the 2020–2025 Outback, and on Subaru's own accessory documentation for tow ratings and trim notes. Specs were read on the CURT, Draw-Tite and Subaru dealer parts pages in September 2026. Amazon prices move daily, so the button shows the live price.",
 "takeaways": [
  "**The engine sets the limit.** Subaru lists 2,700 lb (270 lb tongue weight) for the 2.5-liter Outback and 3,500 lb (350 lb) for the 2.4-liter turbo in XT trims and the Wilderness. A stronger hitch doesn't raise either number.",
  "**All the picks use a 2 in receiver.** That fits most ball mounts, bike racks and cargo carriers without an adapter.",
  "**The Wilderness is the fit exception.** Subaru's factory hitch needs a Wilderness-specific fascia panel and a cutting template on that trim.",
  "**Legacy shares the hitch, not the rating.** CURT lists the 13494 and 13570 for the 2020–2025 Legacy too, but the Legacy's tow rating is its own.",
  "**Budget for wiring.** The Subaru kit is listed with a harness included; CURT and Draw-Tite hitches need a separate 4-flat T-connector.",
 ],
 "top_picks": [
  {"asin": "B0B9N5FMBQ", "role": "Best overall", "why": "Concealed square-tube Class 3, 3,500 lb/350 lb, 31 lb, listed for Outback and Legacy, all trims"},
  {"asin": "B0B9T39SYC", "role": "Highest hitch rating", "why": "4,500 lb/675 lb, weight-distribution compatible, no-drill, 60-minute install"},
  {"asin": "B07YNWTWQ4", "role": "Best factory option", "why": "Subaru's own 2 in hitch, listed with a wiring harness; dealer-installable"},
  {"asin": "B0CDN61T4X", "role": "Best exposed round-tube", "why": "CURT's round-tube Class 3 with A-coat inside and out, Outback and Legacy"},
  {"asin": "B0FWC1VHNS", "role": "Best budget", "why": "Class 3, 2 in, listed for 2020–2026 Outback and 2020–2025 Legacy for well under $200"},
 ],
 "fit_table": {
  "caption": "2020–2025 Outback: what sets your towing limit",
  "head": ["Version", "Engine", "Max tow (Subaru)", "Max tongue weight", "Hitch notes"],
  "rows": [
   ["Base, Premium, Limited, Touring", "2.5 L flat-four, 182 hp", "2,700 lb", "270 lb", "Any 2 in hitch here fits; the vehicle rating is the limit."],
   ["XT trims (Onyx Edition XT, Limited XT, Touring XT)", "2.4 L turbo, 260 hp", "3,500 lb", "350 lb", "Every pick is rated at 3,500 lb or more."],
   ["Wilderness (2022–2025)", "2.4 L turbo, 260 hp", "3,500 lb", "350 lb", "Own rear fascia; OEM hitch needs a Wilderness panel and cutting template."],
   ["2020–2025 Legacy sedan", "2.5 L or 2.4 L turbo", "See owner's manual", "See owner's manual", "CURT 13494 and 13570 list Legacy; Draw-Tite 76597 and OEM do not."],
  ],
 },
 "look_for": [
  {"h": "Your engine's rating, not the hitch's",
   "body": "Every hitch has its own gross trailer weight (GTW) and tongue weight (TW) rating, and so does the car. The lower number is your limit. On the 6th-gen Outback, Subaru splits the rating by engine: the 2.5-liter car is rated for 2,700 lb and 270 lb of tongue weight, while the 2.4-liter turbo in XT trims and the Wilderness gets 3,500 lb and 350 lb. That means the Draw-Tite 76597's 4,500 lb rating is headroom, not extra capacity. Look at the badge on the tailgate before you plan the trailer. The XT and Wilderness badges mean the turbo; everything else is the 2.5-liter. Remember that tongue weight is its own limit: a loaded hitch cargo carrier or bike rack counts entirely against 270 or 350 lb, even with no trailer attached. Passengers and luggage also reduce what the car can safely carry behind it."},
  {"h": "Concealed vs exposed receiver",
   "body": "Hitches for the Outback come in two shapes. Concealed designs such as the CURT 13494 and Draw-Tite 76597 tuck the cross tube behind the bumper so only the receiver mouth shows. Exposed designs such as the CURT 13570 run a round cross tube visibly under the bumper. Concealed looks cleaner and keeps the cross tube out of sight and out of the way. Exposed tubes tend to be heavier (37 lb for the 13570 against 31 lb for the 13494) and CURT rates the 13570 as a harder install. Both styles use the same 2 in receiver, so ball mounts, bike racks and carriers work the same on either. The choice is mainly looks, weight and install effort, not capability."},
  {"h": "Trim-specific fascia and underguards",
   "body": "The Wilderness has its own rear bumper fascia. Subaru's notes for the factory L101SAN000 say a Wilderness-specific fascia panel and a cutting template are needed to install the hitch on that trim, and that the hitch is not compatible with Subaru's rear bumper underguard accessory. Aftermarket makers list their hitches for all trims, but read the instructions for any Wilderness-only step. If your car wears a rear underguard or skid plate, plan on removing or changing it before any hitch goes on. Trim-specific steps can add time beyond the maker's quoted install time, so read them the night before rather than halfway through the job."},
  {"h": "Wiring is a separate purchase on aftermarket hitches",
   "body": "A hitch without lights is a bike rack mount. To tow legally, you need at least a 4-way flat connector for tail, brake and turn signals. The Subaru factory hitch is listed by Subaru Parts Pros with a wiring harness included, which narrows the price gap with CURT and Draw-Tite. For aftermarket hitches, buy a vehicle-specific T-connector that plugs into the Outback's tail-light connectors rather than a splice-in kit. If you tow a trailer that needs electric brakes, you will need a 7-way connector and a brake controller. Mount the plug where a bike rack or carrier won't pinch the cable, and add a dust cap so road salt doesn't corrode the pins over winter."},
  {"h": "Legacy sharing and the 2026 cutoff",
   "body": "The Outback and the 2020–2025 Legacy share a platform, and CURT sells the 13494 and 13570 for both. That's handy if you're shopping used parts, but the Legacy has its own tow rating in its manual. At the other end, the 2026 Outback is a new generation with its own Subaru factory hitches (L101SAR000 and L101SAR001). CURT and Draw-Tite list the 13494 and 76597 through 2026, but check the maker's fit checker with your exact year before ordering for a 2026. Model-year cutoffs in a listing are the maker's tested fitment. If the range stops before your year, don't assume it fits, even if the car looks the same from behind."},
 ],
 "look_table": {
  "head": ["Feature", "Look for", "Avoid"],
  "rows": [
   ["Fitment", "Listing that names the 2020–2025 Outback (and Wilderness if you have one)", "\"Fits most SUVs\" or a range that stops at 2019"],
   ["Receiver", "2 in square receiver for racks and ball mounts", "1.25 in adapters on a car that has a 2 in option"],
   ["Ratings", "Published GTW and TW at or above 3,500 lb / 350 lb", "\"Heavy duty\" with no numbers"],
   ["Finish", "Powder coat over e-coat or A-coat against road salt", "Bare paint on a car that sees winter roads"],
   ["Install", "Bolt-on to existing frame points, instructions published", "Kits that require welding or new frame holes"],
   ["Wiring", "Vehicle-specific plug-in 4-flat harness", "Splice-in wiring on a newer Subaru"],
  ],
 },
 "types_table": {
  "caption": "Hitch types for the 2020–2025 Outback",
  "head": ["Type", "Example on this page", "Hitch rating", "Looks", "Price band", "Best for"],
  "rows": [
   ["Concealed square-tube Class 3", "CURT 13494", "3,500 lb / 350 lb", "Clean, receiver only", "$200–$280", "Most owners"],
   ["High-rated concealed Class 3", "Draw-Tite 76597", "4,500 lb / 675 lb", "Clean, receiver only", "$230–$320", "Turbo owners who want margin, WD setups"],
   ["Factory Class II", "Subaru L101SAN000", "Per vehicle rating", "Integrated with bumper", "$460–$530", "Dealer install, harness in the box"],
   ["Exposed round-tube Class 3", "CURT 13570", "3,500 lb / 350 lb", "Cross tube visible", "$180–$260", "Owners who don't mind the tube"],
   ["Budget Class 3", "TUZILLA", "Per listing", "Varies", "$130–$190", "Bike racks and light use"],
  ],
 },
 "picks": [
  {"asin": "B0B9N5FMBQ", "role": "Best overall", "price": "$200–$280",
   "pros": ["Concealed main body keeps the look clean", "3,500 lb GTW / 350 lb TW matches the turbo Outback's rating", "31 lb, the lightest of the name-brand picks", "Listed for all 2020–2026 Outback and 2020–2025 Legacy trims", "Open-back receiver is easy to clean out"],
   "cons": ["Wiring sold separately", "Limited lifetime warranty covers finish and parts for one year only", "CURT publishes no install time for this part"],
   "body": "The CURT 13494 is the hitch most Outback owners should start with. It is a Class 3 with a 2 in square receiver and a concealed main body, so the cross tube sits behind the bumper and only the receiver shows. CURT rates it for 3,500 lb gross trailer weight and 350 lb tongue weight, which lines up exactly with Subaru's rating for the 2.4-liter turbo XT and Wilderness. On a 2.5-liter car you are limited to Subaru's 2,700 lb and 270 lb, and the hitch has room to spare.\n\nAt 31 lb, it weighs less than the Draw-Tite 76597 (32 lb) and CURT's own round-tube 13570 (37 lb). It is carbon steel in gloss black powder coat and has an open-back receiver that doesn't trap dirt and salt. CURT lists it for every 2020–2026 Outback wagon and the 2020–2025 Legacy sedan, all trims. The warranty is CURT's limited lifetime, which covers the finish and parts for one year. Installation hardware is included; the 4-flat wiring is not. For most owners, that combination of a clean look, a full-rating match with the turbo car and Legacy compatibility makes it the default choice.",
   "who": "Most Outback owners who want a clean-looking 2 in hitch for a bike rack, cargo carrier or small trailer.",
   "specs": [["Class", "3"], ["Part #", "CURT 13494"], ["Receiver", "2 in square, open back"], ["Ratings", "3,500 lb GTW / 350 lb TW"], ["Fits", "2020–2026 Outback, 2020–2025 Legacy, all trims (per CURT)"], ["Weight", "31 lb"], ["Style", "Concealed main body"], ["Finish", "Gloss black powder coat, carbon steel"], ["Warranty", "Limited lifetime (1 yr finish, 1 yr parts)"]]},
  {"asin": "B0B9T39SYC", "role": "Highest hitch rating", "price": "$230–$320",
   "pros": ["4,500 lb GTW / 675 lb TW, the highest rating here", "Weight-distribution compatible", "Bolt-on, no drilling, about 60 minutes (Draw-Tite's figure)", "Concealed design", "Powder coat over e-coat; limited lifetime warranty"],
   "cons": ["The extra rating doesn't raise the Outback's 2,700 or 3,500 lb limit", "Listed for the Outback wagon only, not the Legacy", "Wiring sold separately"],
   "body": "The Draw-Tite 76597 is the strongest hitch on this page on paper. Draw-Tite rates it for 4,500 lb gross trailer weight and 675 lb tongue weight, and it is one of the few Outback hitches listed as weight-distribution compatible. That rating does not let the car tow more. Bolted to a 2.5-liter Outback, it is still limited to Subaru's 2,700 lb and 270 lb, and on a turbo XT or Wilderness to 3,500 lb and 350 lb. What you get is margin: the hitch is working well inside its own limits, which matters with heavy hitch-mounted cargo carriers and bumpy trailheads.\n\nDraw-Tite lists it for the 2020–2026 Outback wagon, bolt-on to the vehicle frame with no drilling, and gives an install time of 60 minutes. The body is concealed. It weighs 32 lb and is finished in black powder coat over e-coat, which is the better corrosion treatment for cars in salt states. It carries a limited lifetime warranty and is tested to V-5 and SAE J684 standards. It is not listed for the Legacy, so sedan owners should look at the CURT picks instead. As with every aftermarket hitch here, add a plug-in 4-flat harness to the order if you plan to tow.",
   "who": "XT and Wilderness owners who tow near the limit or run a heavy cargo carrier and want the most hitch margin.",
   "specs": [["Class", "III"], ["Part #", "Draw-Tite 76597"], ["Receiver", "2 in square"], ["Ratings", "4,500 lb GTW / 675 lb TW (WD same)"], ["Fits", "2020–2026 Outback wagon (per Draw-Tite)"], ["Weight", "32 lb"], ["Install", "About 60 min, bolt-on, no drilling"], ["Finish", "Black powder coat over e-coat"], ["Warranty", "Limited lifetime"]]},
  {"asin": "B07YNWTWQ4", "role": "Best factory option", "price": "$460–$530",
   "pros": ["Genuine Subaru part designed around the Outback bumper", "Subaru Parts Pros lists a wiring harness in the box", "Dealer can install it", "2 in receiver", "Subaru notes cover the Wilderness install"],
   "cons": ["Most expensive hitch here at a $529.95 MSRP", "Ball mount and ball not included", "Wilderness needs an extra fascia panel and template cut; not compatible with the rear bumper underguard"],
   "body": "Subaru's own hitch, L101SAN000, is the choice for owners who want the dealer to handle it or who want everything to match the car. It is a Class II hitch with a 2 in receiver. Subaru's documentation ties its ratings to the engine: 2,700 lb and 270 lb of tongue weight on the 2.5-liter, and 3,500 lb and 350 lb on the 2.4-liter turbo. The dealer listing at Subaru Parts Pros says a wiring harness is included; the hitch mount and ball are not. Aftermarket hitches need that harness bought separately, which narrows the price gap slightly.\n\nThe price is still the highest here: Subaru Parts Pros shows a $529.95 MSRP, discounted to $463.66. The fit notes matter. On a Wilderness, the factory hitch requires a Wilderness-specific rear bumper fascia panel and a cutting template, and Subaru says it is not compatible with the rear bumper underguard accessory. The Amazon listing names the 2020–2024 Outback, and Subaru dealer parts catalogs also list the part for the 2025 model. Ask the seller to confirm by VIN if you have a Wilderness or a 2025. A dealer can also order the Wilderness fascia panel at the same time, which avoids a second trip.",
   "who": "Owners who want a dealer-installed factory part with the harness in the box and don't mind paying for it.",
   "specs": [["Class", "II (per dealer listing)"], ["Part #", "Subaru L101SAN000"], ["Receiver", "2 in"], ["Ratings", "Per engine: 2,700 lb / 270 lb (2.5 L), 3,500 lb / 350 lb (2.4 L turbo)"], ["Includes", "Wiring harness (per dealer); ball mount not included"], ["Wilderness", "Needs Wilderness fascia panel and cutting template"], ["Not compatible", "Rear bumper underguard"], ["MSRP", "$529.95"]]},
  {"asin": "B0CDN61T4X", "role": "Best exposed round-tube", "price": "$180–$260",
   "pros": ["3,500 lb GTW / 350 lb TW", "Rust-resistant A-coat inside and out, plus gloss black powder coat", "Listed for the 2020–2025 Outback and Legacy, all trims", "Round cross tube is simple and strong", "Designed and welded by CURT"],
   "cons": ["Exposed cross tube is visible under the bumper", "CURT rates the install advanced, about 90 minutes", "37 lb, the heaviest name-brand pick"],
   "body": "The CURT 13570 is the alternative for owners who don't mind seeing the hitch. It uses a round cross tube that runs under the bumper, where the 13494 hides a square tube behind it. CURT rates it for the same 3,500 lb and 350 lb as the 13494, so either one covers the turbo Outback's full rating and is overkill for the 2.5-liter. The coating is the feature here: CURT co-cures the tube in a liquid A-coat inside and out before the gloss black powder coat, which is extra protection against salt.\n\nThe trade-offs are weight and install time. It weighs 37 lb against the 13494's 31 lb, and CURT rates the install as advanced at about 90 minutes, versus 60 minutes for the Draw-Tite. CURT lists it for all 2020–2025 Outback and Legacy trims. Because the tube is exposed, Wilderness owners who drive rough trails may prefer a concealed hitch that keeps the cross tube tucked away. Warranty is CURT's limited lifetime with one year on finish and parts. Installation hardware is included, and the 2 in receiver takes the same accessories as the concealed hitches.",
   "who": "Outback and Legacy owners in salt states who want an extra layer of coating and don't mind an exposed tube.",
   "specs": [["Class", "3"], ["Part #", "CURT 13570"], ["Receiver", "2 in"], ["Ratings", "3,500 lb GTW / 350 lb TW"], ["Fits", "2020–2025 Outback and Legacy, all trims (per CURT)"], ["Weight", "37 lb"], ["Style", "Exposed round tube"], ["Install", "Advanced, about 90 min (CURT)"], ["Finish", "A-coat inside and out + gloss black powder coat"]]},
  {"asin": "B0FWC1VHNS", "role": "Best budget", "price": "$130–$190",
   "pros": ["Lowest price on this page", "2 in Class 3 receiver", "Listing names both 2020–2026 Outback and 2020–2025 Legacy", "Fine for bike racks and light cargo carriers", "Bolt-on design per listing"],
   "cons": ["No maker spec page to check ratings, weight or coating against", "Warranty terms thinner than CURT or Draw-Tite", "Wilderness fit not spelled out"],
   "body": "If the hitch will mostly carry a bike rack or a small cargo tray, a budget Class 3 like this TUZILLA saves roughly $70–$150 against the name brands. The listing names the 2020–2026 Outback (all) and the 2020–2025 Legacy and calls it a 2 in Class 3. What you give up is documentation. CURT and Draw-Tite publish GTW, tongue weight, product weight, finish and install time on their own sites, and budget brands generally don't publish a full spec sheet outside the listing.\n\nThat matters less than it sounds if you stay inside the Outback's own limits, since the vehicle rating of 2,700 or 3,500 lb is the ceiling either way. Before you buy, confirm on the listing the published tongue weight, the coating (you want powder coat over e-coat for winter roads), whether the hardware is included, and whether the Wilderness is covered. If you plan to tow a trailer near the limit every weekend, spend the extra on the CURT 13494 or Draw-Tite 76597 instead. The WOLFSTORM and AUTOFREE hitches listed for the same years are similar budget alternatives, with the same caveats.",
   "who": "Owners who mainly need a 2 in receiver for a bike rack or cargo tray and want to spend under $200.",
   "specs": [["Class", "3 (per listing)"], ["Receiver", "2 in"], ["Fits", "2020–2026 Outback, 2020–2025 Legacy (per listing)"], ["Ratings", "Confirm on listing; vehicle limit still applies"], ["Finish", "Confirm on listing"], ["Price band", "$130–$190"]]},
 ],
 "install": [
  "Confirm your engine (2.5-liter or XT/Wilderness turbo) and trim, and check whether the car has a rear bumper underguard or Wilderness-specific fascia. Those decide the rating and any extra parts.",
  "Park on level ground and read the maker's instructions. Some installs need the exhaust lowered or a heat shield loosened for access to the frame mounting points.",
  "Clean the threads in the existing frame holes with a wire brush or penetrating spray. Rusty or dirty weld nuts are the usual reason a bolt won't start.",
  "Lift the hitch into place with a helper or a jack, start every bolt by hand, then torque to the value in the instructions.",
  "Install the wiring. Plug-in T-connectors go between the Outback's tail-light connectors; mount the 4-flat plug where it won't drag.",
  "Test the lights with a tester or trailer, then re-check the hitch bolt torque after the first 50–100 miles of driving.",
 ],
 "avoid": [
  {"h": "Towing to the hitch rating instead of the car's", "body": "A 4,500 lb hitch on a 2.5-liter Outback is still a 2,700 lb setup. Plan every trailer around Subaru's number for your engine."},
  {"h": "Assuming Legacy means Legacy's rating", "body": "Several hitches fit both cars, but the sedan's tow rating is its own. Read the Legacy owner's manual before you hook up a trailer."},
  {"h": "Skipping the Wilderness notes", "body": "The Wilderness fascia is different. The factory hitch needs a separate panel and a template cut; check aftermarket instructions for trim-specific steps too."},
  {"h": "Splice-in wiring", "body": "Cutting into the Outback's tail-light wiring causes faults later. A vehicle-specific plug-in harness costs little and comes out cleanly."},
 ],
 "verdict": {
  "thesis": "Buy the CURT 13494 for most Outbacks, the Draw-Tite 76597 if you want maximum margin on an XT or Wilderness, and Subaru's L101SAN000 if you want the dealer to fit it with the harness included.",
  "body": "The best hitch for a 2020–2025 Outback is a 2 in Class 3 that the maker lists for your model year and trim, plus a plug-in wiring harness. The CURT 13494 does that with a concealed body, 31 lb of steel and a rating that matches the turbo car. The Draw-Tite 76597 is worth it for owners who want 4,500 lb of hitch behind a 3,500 lb car. The factory hitch costs the most, but the harness is in the box and the dealer handles fit, including the Wilderness fascia. Whatever you choose, the engine badge sets the tow limit.\n\nA hitch pairs well with a hitch cargo carrier or bike rack, and many Outback owners add a roof rack crossbar set or a cargo box on top for skis and camping gear. If you are shopping for the new generation instead, the 2026 Outback uses different factory hitch parts.",
 },
 "sources": [
  ["CURT 13494 Class 3 hitch (CURT)", "https://www.curtmfg.com/part/13494"],
  ["CURT 13570 Class 3 hitch (CURT)", "https://www.curtmfg.com/part/13570"],
  ["Draw-Tite 76597 Class III hitch (Draw-Tite)", "https://www.draw-tite.com/product/76597_class-3-trailer-hitch"],
  ["Subaru L101SAN000 trailer hitch (Subaru Parts Pros)", "https://www.subarupartspros.com/sku/l101san000.html"],
  ["Subaru L101SAN000 trailer hitch (Subaru parts catalog)", "https://parts.subaru.com/p/Subaru__Outback/Trailer-Hitch/78905090/L101SAN000.html"],
  ["Subaru Outback, sixth generation (Wikipedia)", "https://en.wikipedia.org/wiki/Subaru_Outback"],
  ["Subaru Legacy, seventh generation (Wikipedia)", "https://en.wikipedia.org/wiki/Subaru_Legacy_(seventh_generation)"],
  ["How much can my Subaru tow? (Wilsonville Subaru)", "https://www.wilsonvillesubaru.com/how-much-can-my-subaru-tow/"],
 ],
}

# Product list for this page. (asin, name, brand, band, cond, note)
FITS = [
 ("B0B9N5FMBQ","CURT 13494 Class 3 Hitch 2 in, 2020-2026 Outback Wagon & 2020-2025 Legacy, 3,500 lb GTW, concealed","CURT","$200–$280",{},"31 lb; Subaru rates the car 2,700 lb (2.5L) or 3,500 lb (XT/Wilderness)."),
 ("B0B9T39SYC","Draw-Tite 76597 Class 3 Trailer Hitch 2 in, 2020-2026 Subaru Outback","Draw-Tite","$230–$320",{},"4,500 lb hitch rating; Outback wagon only, not Legacy."),
 ("B07YNWTWQ4","Subaru 2020-2024 Outback Trailer Hitch Kit L101SAN000, Genuine OEM","Subaru","$460–$530",{},"Harness included per dealer; Wilderness needs extra fascia panel. Confirm 2025 by VIN."),
 ("B0CDN61T4X","CURT 13570 Class 3 Trailer Hitch 2 in, select Outback (2020-2025 Outback & Legacy)","CURT","$180–$260",{},"Exposed round tube; about 90 min install."),
 ("B0FWC1VHNS","TUZILLA Class 3 Trailer Hitch 2 in, 2020-2026 Outback (all) / 2020-2025 Legacy","TUZILLA","$130–$190",{},"Budget; confirm Wilderness fit and ratings on listing."),
 ("B0G24ZSLKC","WOLFSTORM Class 3 Trailer Hitch 2 in, 2020-2025 Outback & Legacy","WOLFSTORM","$120–$180",{},"Budget alternative."),
 ("B0G12TJSRT","AUTOFREE Class III Tow Hitch 2 in, 2020-2025 Outback & Legacy","AUTOFREE","$120–$180",{},"Budget alternative."),
]
