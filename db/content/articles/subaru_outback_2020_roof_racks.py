"""Long-form article — Best Roof Racks / Crossbars for the 2020–2025 Subaru Outback (6th gen, BT).
Mirrors the approved pilot (ford_f150_2021_tonneau.py). No invented hands-on testing: vehicle facts come from
Subaru press material, Wikipedia and retailer fit guides; product facts come from the Amazon listing titles
recorded in FITS plus the retailer pages in SOURCES (checked 2026-09-24).
Note: the DB gen slug is "2020-present", but the 6th-gen Outback ended with MY2025 (the 7th gen is MY2026).
Source fixes 2026-10-04: roof load statements corrected to Subaru's 2022, 2023 and 2025 trim comparison sheets (150 lb for the rails with integrated and retractable cross bars; Wilderness 200 lb dynamic / 700 lb static); 165 lb now labelled as a kit rating; 176 lb and the AHG Auto Service source removed; Wilderness crossbar wording matched to Subaru's sheets; factory bars named "retractable crossbars" throughout; socket wording matched to Autoblog; unconfirmed 2026 on-sale date removed.
"""

KEY = ("subaru", "outback", "2020-present", "roof-racks")

TITLE = "Best Roof Racks for 2020–2025 Subaru Outback: 6 Crossbars Split by Standard vs Wilderness Rails"
META = ("Six crossbars for the 6th-gen Outback, split by rail type: retractable-crossbar rails vs Wilderness ladder rails, "
        "with load limits, spread, noise and tent notes.")

FAQ = [
 ("Do I even need aftermarket crossbars on a 2020–2025 Outback?",
  "Maybe not. Non-Wilderness Outbacks of this generation have raised side rails with Subaru's retractable crossbars built in: you lift a tab, pull the bar out of its socket and swing it across. For a light cargo bag, a single bike or skis, those bars do the job. Owners move to aftermarket bars when they want a wider bar for two items side by side, a T-slot channel for modern accessories, or a quieter aero profile. Subaru's 2022, 2023 and 2025 spec sheets list no built-in crossbars on the Wilderness, so it needs a set before anything that mounts to bars can go on. The 2022 sheet lists a Thule crossbar set as an option on that trim."),
 ("Will Outback Wilderness crossbars fit a regular Outback, or the other way around?",
  "No. The Wilderness (2022–2025) uses a fixed ladder-type rail with a different profile, and the listings on this page say so plainly: the Tuyoung, BougeRV and 300 lb lockable bars are titled \"Only Fit Wilderness.\" Bars sold for the standard raised rails, such as the ERKUL lockable set or the Thule kit here, are not listed for the Wilderness. Look at your roof: if the rails have the copper-finish tie-down points and no built-in crossbars, you have the Wilderness rail."),
 ("What is the roof load limit on a 6th-gen Outback?",
  "It depends on the roof. Subaru's trim comparison sheets for 2022, 2023 and 2025 list the roof rails with integrated and retractable cross bars, fitted to every trim except the Wilderness, at a 150 lb maximum capacity. The same sheets list the Wilderness rails at 200 lb dynamic, meaning while driving, and 700 lb static, meaning parked, which is what makes a rooftop tent practical. We did not read Subaru's sheets for 2020, 2021 or 2024, so use the number in your owner's manual; it is the authority and it overrides every crossbar rating. The 165 lb that The Rack Shop lists is the rating of its Yakima kit, not a Subaru roof figure."),
 ("Can I put a rooftop tent on a regular (non-Wilderness) Outback?",
  "Owners do it, and SubaruOutback.org has a thread on tents mounted to the factory crossbars, but it is the harder case. The tent's weight plus any added bars has to stay under Subaru's 150 lb figure for the standard roof while driving. The Subaru sheets we read give a 700 lb static figure only for the Wilderness rails, and we could not confirm a parked figure for the standard roof. If a tent is the goal, the Wilderness is the safer route. Ask the tent maker whether it approves the Outback, and check your owner's manual."),
 ("Is a 2026 Outback the same generation?",
  "No. The 2026 Outback is a new, seventh generation, with a boxier body and new rails. Wikipedia notes the retractable crossbars were dropped, and The Drive reports the 2026 Wilderness rack at 800 lb static and 220 lb dynamic. Several Wilderness crossbar listings on this page say \"NOT for 2026\" in the title. Buy bars listed for 2020–2025 only if your car is a 2020–2025."),
 ("Why are aftermarket bar ratings (300 lb, 330 lb) higher than the Outback's limit?",
  "A 300 or 330 lb rating on a listing is the bar's own strength, tested without the car. The car's rails and roof set the real ceiling, and that ceiling is the lower number. A 330 lb Wilderness bar still only lets you carry what Subaru rates the rails for while driving, which is 200 lb in the spec sheets we read. The higher bar rating mainly means less flex, which helps with long loads and tents parked at camp."),
 ("How far apart should Outback crossbars be?",
  "On the standard car, the factory retractable crossbars plug into round sockets in the rails, and Autoblog notes they are narrower than aftermarket bars. None of the sources we read describe a way to slide them, so treat their spread as fixed. Clamp-on aftermarket bars can slide along the rail, so you can set the spread to what your accessory needs. Cargo boxes and tents list a minimum and maximum bar spread; kayak carriers work better with more spread. Set the spread first, then tighten. Recheck the clamps after the first drive."),
 ("Will crossbars make my Outback noisy on the highway?",
  "Usually some. Autoblog points out that leaving any crossbars on increases wind noise and costs fuel economy, which is the point of the Outback's retractable design. Aero (teardrop) bars are quieter than square or round bars; The Rack Shop recommends Yakima's JetStream over its steel CoreBar for that reason. Bars that overhang the rails, or a missing end cap, are the usual whistlers. Take bars off between trips if you can."),
 ("Do these crossbars need drilling?",
  "No. Every set here clamps around the existing raised rails, with no drilling. The standard-rail bars replace the retractable crossbars' job; you simply stow the factory bars along the rails first. Keep the factory bars' sockets clean, since Autoblog notes they can fill with gunk over time, which makes them stiff when you want them back."),
 ("Thule or Yakima kit vs a $100 lockable Amazon set?",
  "A Thule or Yakima system buys a fit-guide-backed part number, a known warranty, lockable towers and a large accessory range. etrailer prices Thule WingBar Evo for this Outback at $704.85, and The Rack Shop sells a Yakima SkyLine kit at $653.85. The lockable ERKUL and Tuyoung sets cost a fraction of that and work well for bags and bikes, but their specs come from the listing alone. For a rooftop tent or daily use, the name-brand kit is the safer buy."),
]

ARTICLE = {
 "dek": "The 6th-generation Outback came with two different roofs: retractable crossbars built into the standard rails, and a fixed ladder rack on the 2022–2025 Wilderness. They take different crossbars. Here are six sets split by rail type, with the load limits, spread and noise notes that decide which one you need.",
 "author": "jake-morrison",
 "reviewed": "2026-09-24",
 "method": "We did not install these crossbars ourselves. We matched each set to the Outback rail type named in its Amazon listing title, then checked vehicle facts against Subaru's 2022, 2023 and 2025 Outback trim comparison sheets, Subaru's Wilderness press release, Wikipedia and the etrailer and Rack Shop fit guides. Where the only spec source is the Amazon listing, we say so. Owner comments come from SubaruOutback.org threads. Prices were checked in September 2026 where a retailer published one; Amazon prices move daily, so the button shows the live price.",
 "takeaways": [
  "**Check your rail first.** Standard 2020–2025 Outbacks have raised rails with retractable crossbars built in; the 2022–2025 Wilderness has a fixed ladder rail with no built-in crossbars. Bars for one don't fit the other.",
  "**The factory bars may be enough.** For a cargo bag, one bike or skis, the built-in bars work. Buy aftermarket bars for width, T-slot accessories or a quieter profile.",
  "**The car's limit beats the bar's.** Listings quote 220–330 lb bar ratings, but Subaru's 2022, 2023 and 2025 spec sheets list 150 lb for the standard roof and 200 lb while driving for the Wilderness. Use the owner's manual figure for your year.",
  "**Wilderness is the tent trim.** Subaru rates the Wilderness ladder rails at 700 lb static for rooftop tents; the Subaru sheets we read give no static figure for the standard rails.",
  "**2026 is a different car.** The 7th-gen Outback drops the retractable crossbars, and several Wilderness listings here say \"NOT for 2026.\"",
 ],
 "top_picks": [
  {"asin": "B0BZ5L38P3", "role": "Best for standard rails", "why": "Thule aero bars built for the Outback's stowable factory rack; 165 lb kit rating per the listing"},
  {"asin": "B0FGYC7XCH", "role": "Best value, standard rails", "why": "Lockable aluminum bars listed for 2020–2025 Outback raised rails"},
  {"asin": "B0CSW8LPBZ", "role": "Best for Wilderness", "why": "330 lb-rated all-aluminum bars listed only for the 2022–2025 Wilderness"},
  {"asin": "B0BPY41QBK", "role": "Best lockable Wilderness set", "why": "BougeRV aluminum bars with locks, listed only for the Wilderness"},
  {"asin": "B0CYWRY9SH", "role": "Wilderness budget pick", "why": "300 lb lockable bars whose title warns off the 2026 model"},
 ],
 "fit_table": {
  "caption": "2020–2025 Outback roof types (the crossbar must match the rail, not the engine or year)",
  "head": ["Roof type", "Trims / years", "Crossbars from the factory", "What to buy"],
  "rows": [
   ["Raised rails with integrated, retractable crossbars", "Non-Wilderness trims, 2020–2025", "Yes, stowable in the rails", "Bars listed for 2020–2025 Outback raised rails (Thule, ERKUL); not Wilderness bars"],
   ["Wilderness ladder-type rails", "Wilderness, 2022–2025", "None built in", "Bars titled \"Only Fit Wilderness\" (Tuyoung, BougeRV, 300 lb lockable)"],
   ["Flush rails / fixed points", "Not offered on this generation", "n/a", "Ignore flush-rail and fixed-point kits for this car"],
   ["Bare roof", "Not offered on this generation", "n/a", "If rails are missing, check for damage or a replacement roof"],
   ["7th-gen rails", "2026+ (new generation)", "No retractable crossbars", "Buy 2026-specific parts; this page doesn't apply"],
  ],
 },
 "look_for": [
  {"h": "Standard rail or Wilderness rail — decide this first",
   "body": "The 6th-gen Outback has two roof designs, and nearly every crossbar listing is written for only one of them. Standard trims have what Subaru calls roof rails with integrated and retractable cross bars, also described as swing-out bars: lift a tab, pull the bar from its round socket, swing it across. The Wilderness, sold for 2022–2025, replaced that with what Subaru calls a fixed ladder-type roof rack system, with copper-finish tie-down points and no built-in crossbars. Look for \"Only Fit Wilderness\" or \"Compatible with Raised Rails\" in the title and match it to your roof. The etrailer fit guide lists the 2020 Outback as factory raised rails, so the brand kits here are sold for that rail."},
  {"h": "Subaru's roof figure, not the bar rating",
   "body": "Crossbar listings quote the bar's strength: 165 lb on the Thule kit, 220 lb on the OMAC, 300 to 330 lb on the Wilderness bars. The number that matters is the Outback's own roof figure, and it is lower. Subaru's trim comparison sheets for 2022, 2023 and 2025 list a 150 lb maximum capacity for the roof rails with integrated and retractable cross bars, and 200 lb dynamic (700 lb static) for the Wilderness rails. The Rack Shop's 165 lb is the rating of its Yakima kit, not Subaru's figure for the roof. We did not read the sheets for other years, and a SubaruOutback.org thread argues over 150 lb versus a lower manual figure for the factory bars, so the owner's manual is the authority. Subtract the weight of any added bars, then your cargo box or bikes, and stay under the lowest figure in the manual."},
  {"h": "Width and spread",
   "body": "Autoblog's look at the factory crossbars notes they aren't as wide as aftermarket bars, which makes two bikes or a box plus a kayak side by side hard. That is the most common reason owners upgrade. Clamp-on aftermarket bars also slide along the rail, so you choose the spread instead of living with where the factory sockets sit. Cargo boxes, bike trays and tents each publish a spread range; check it against where the rails let you clamp, especially at the rear where the rail curves down toward the hatch."},
  {"h": "Wind noise and fuel economy",
   "body": "Subaru designed the retractable bars so you don't drive around with crossbars up; Autoblog notes that bars left in place add wind noise and hurt fuel economy. If you go aftermarket, the profile matters. The Rack Shop says Yakima's teardrop JetStream bars cut wind noise better than its steel CoreBar. Aero aluminum bars like the Thule and most of the Amazon sets here are the quieter shape. Trim any overhang, keep the end caps on, and pull the bars off between trips if you want the quietest cabin."},
  {"h": "Rooftop tents: the Wilderness is the trim built for them",
   "body": "Subaru says the Wilderness ladder rails carry 700 lb static, which it explicitly ties to using a roof-top tent on the trail. That static number covers the tent plus sleepers while parked. The driving limit, 200 lb in Subaru's spec sheets, still caps the weight of the tent and bars on the road. For standard Outbacks the sheets we read list 150 lb and no static figure, and SubaruOutback.org has threads on putting tents on the factory crossbars. If a tent is the plan, buy Wilderness bars with a high rating and a tent the maker approves for the Outback."},
 ],
 "look_table": {
  "head": ["Feature", "Look for", "Avoid"],
  "rows": [
   ["Fitment", "Title naming 2020–2025 Outback and your rail: raised rails or \"Only Fit Wilderness\"", "\"Universal\" bars, 2026-only listings, or Legacy sedan bundles"],
   ["Load", "A stated bar rating, then your owner's manual roof limit", "Assuming a 330 lb bar lets you carry 330 lb"],
   ["Profile", "Aero/teardrop aluminum bars for less noise", "Square or round steel bars if you drive highways daily"],
   ["Security", "Lock cores on the towers or clamps", "Bars that come off with a hex key while parked"],
   ["Accessory fit", "T-slot channel that takes current bike, box and kayak mounts", "Bars that only take wrap-around U-bolts"],
   ["Width", "Bar length that covers the accessory you plan, without big overhang", "Long overhang past the rails: more noise, dented hatch"],
  ],
 },
 "types_table": {
  "caption": "Roof-rack options on the 2020–2025 Outback",
  "head": ["Option", "Price guide", "Rail type", "Bar rating (per maker/listing)", "Noise", "Best for"],
  "rows": [
   ["Factory retractable crossbars", "Included", "Standard rails", "150 lb (Subaru spec sheets)", "Low; stow when unused", "Occasional bag, bike, skis"],
   ["Thule aero bars for stowable rack", "About $500–$750", "Standard rails", "165 lb", "Low (aero)", "Daily-use accessories, T-slot mounts"],
   ["Budget lockable aluminum bars", "About $80–$150", "Standard or Wilderness (check title)", "220–330 lb", "Low to medium", "Budget cargo bags, bikes, kayaks"],
   ["Yakima SkyLine / Thule WingBar Evo system", "$653.85–$704.85 (retailer)", "Standard rails", "Vehicle limit", "Low (aero)", "Buyers who want a fit-guide part number"],
   ["Platform or basket on Wilderness bars", "Varies", "Wilderness rails", "Vehicle limit", "Higher", "Overland gear, rooftop tents"],
  ],
 },
 "picks": [
  {"asin": "B0BZ5L38P3", "role": "Best for standard rails", "price": "$500–$750",
   "pros": ["Thule-branded bars listed specifically for the Outback's stowable factory rack", "Aerodynamic profile the listing describes as quiet", "165 lb capacity stated in the title", "Wide Thule accessory ecosystem for bikes, boxes and kayaks", "Replaces narrow factory bars with wider aero bars"],
   "cons": ["Listing spans 2010–2023; confirm 2024–2025 fit with the seller", "Costs several times the budget sets", "Not for the Wilderness ladder rails"],
   "body": "If you drive a standard 2020–2025 Outback and want better bars than the factory retractable set, a Thule kit is the most conservative upgrade. This listing is titled for the Subaru Outback with the stowable factory rack, states a 165 lb load capacity, and describes the bars as quiet and aerodynamic. The 165 lb figure is the kit's rating. Subaru's 2022, 2023 and 2025 spec sheets list 150 lb for this roof, and we could not confirm that aftermarket bars raise it, so plan around 150 lb unless your owner's manual says otherwise. The upgrade over the factory bars is width and accessory fit: the Autoblog piece on this rack notes the built-in bars are narrower than aftermarket bars, which makes two items side by side awkward.\n\nThe title covers 2010–2023, so 2024 and 2025 owners should confirm fit with the seller before ordering, and nothing in the title covers the Wilderness. For comparison, etrailer prices the Thule WingBar Evo system for this Outback at $704.85 and the steel SquareBar Evo at $604.85, and it adds a warning common to all Thule roof systems: don't open or vent the sunroof with the rack installed. Check the live Amazon price against those figures before you buy.",
   "who": "Standard-rail Outback owners who carry gear every weekend and want a name-brand, low-noise bar with a large accessory range.",
   "specs": [["Type", "Aero crossbars for factory stowable rack"], ["Fits", "Subaru Outback with stowable factory rack (title: 2010–2023)"], ["Not for", "Outback Wilderness ladder rails"], ["Capacity", "165 lb kit rating (per listing); Subaru lists 150 lb for the roof"], ["Profile", "Aerodynamic, described as quiet"], ["Brand", "Thule"], ["Retailer benchmark", "Thule WingBar Evo system $704.85 (etrailer)"], ["Drilling", "None"]]},
  {"asin": "B0FGYC7XCH", "role": "Best value, standard rails", "price": "$80–$130",
   "pros": ["Listed for 2020–2025 Outback raised rails, the full standard-rail span", "Anti-theft locks", "Aluminum construction", "Black finish matches the factory rails", "A fraction of the Thule price"],
   "cons": ["Load rating and warranty only on the listing, not a maker spec sheet", "No fit-guide part number like Thule or Yakima", "Not the Wilderness version (ERKUL sells that separately)"],
   "body": "ERKUL sells two Outback versions, and the difference is the rail. This one is titled for the 2020–2025 Outback \"Compatible with Raised Rails,\" which is the standard car with the retractable crossbars; the silver ERKUL set in the FITS list is the Wilderness-only version. It is aluminum, has anti-theft locks, and costs a fraction of a Thule or Yakima system. For a cargo bag, a roof bike mount or a pair of kayak saddles, that is the sensible buy, and the locks mean the bars don't have to come off every time you park at a trailhead.\n\nThe trade-off is paperwork. There is no maker fit guide or published test standard, so the load rating and warranty come from the Amazon listing alone. Read them there, and keep your load under the Outback's own roof figure, 150 lb in the Subaru sheets we read, regardless of the bar's number. Before the first trip, check that the clamps close fully around the rail without contacting the factory crossbars' sockets, and re-tighten after the first drive, since clamp-on bars settle.",
   "who": "Standard-rail Outback owners who want wider, lockable bars for occasional gear without paying for a name-brand system.",
   "specs": [["Type", "Clamp-on aluminum crossbars"], ["Fits", "2020–2025 Outback with raised rails (per title)"], ["Not for", "Wilderness (separate ERKUL listing)"], ["Lock", "Anti-theft locks"], ["Finish", "Black"], ["Load rating", "See listing"], ["Drilling", "None"]]},
  {"asin": "B0DH51LV3Z", "role": "Adjustable-width option", "price": "$80–$130",
   "pros": ["Telescopic bars adjust to rail width", "220 lb bar rating in the title", "Aluminum construction", "Silver finish", "Listed for 2020–2025 Outback"],
   "cons": ["Title doesn't say which rail type; the listing URL mentions Wilderness, so confirm your trim with the seller", "No locks mentioned in the title", "Telescopic joints can loosen; recheck them"],
   "body": "OMAC's set is the odd one here because the bars are telescopic: the length adjusts, so the listing covers the Outback without being built around one exact rail spacing. The title gives a 220 lb bar rating, heavy-duty aluminum construction and a silver finish, and lists cargo carriers, kayaks, canoes, bikes and snowboards as intended loads. As with every bar on this page, 220 lb is what the bar can hold, not what the Outback's roof allows while driving.\n\nWe include it with a caution. The title says 2020–2025 Outback but does not name a rail type, while the listing's web address refers to the 2022–2025 Wilderness. That makes it a set to confirm with the seller before you order, especially on a standard-rail car. Telescopic bars also have one more joint to check: once you set the length, tighten the adjusting hardware and recheck it after the first few drives, because a bar that slowly extends will start to whistle and can shift a load.",
   "who": "Owners who want an adjustable, silver aluminum bar and will confirm the rail type with the seller first.",
   "specs": [["Type", "Telescopic aluminum crossbars"], ["Fits", "2020–2025 Outback (rail type: confirm)"], ["Bar rating", "220 lb (per title)"], ["Adjustment", "Telescopic length"], ["Finish", "Silver"], ["Lock", "Not listed in title"], ["Drilling", "None"]]},
  {"asin": "B0CSW8LPBZ", "role": "Best for Wilderness", "price": "$100–$140",
   "pros": ["Listed only for the 2022–2025 Wilderness ladder rails", "330 lb bar rating, the highest on this page", "All-aluminum", "Suits the Wilderness's tent-friendly 700 lb static roof", "Tuyoung also sells rail-specific bars for other SUVs, so the fit is built around the rail"],
   "cons": ["Won't fit standard-rail Outbacks", "Bar rating doesn't raise the car's driving limit", "Specs and warranty are listing-only"],
   "body": "The Wilderness is the Outback built for a heavy roof: Subaru's press release gives its ladder-type rails a 700 lb static limit and says it's meant to let you use a roof-top tent on the trail. It has no built-in crossbars, so you need a set, and it has to be one made for the ladder rail. Tuyoung's is titled for the 2022–2025 Wilderness only and rated at 330 lb, the highest bar rating on this page. For a tent, a platform or a loaded basket, a stiffer bar means less flex, which matters when the load is parked and people are climbing in.\n\nKeep the numbers straight. The 330 lb rating covers the bar. The Wilderness's driving limit is much lower: Subaru's 2022, 2023 and 2025 spec sheets list 200 lb dynamic, and your owner's manual is the authority for your year. Your tent and bars have to fit under that on the road, and the 700 lb figure only applies when parked. The bars are all aluminum and clamp to the rails without drilling. Check the listing for locks and warranty terms, since Tuyoung doesn't publish them on a separate spec sheet.",
   "who": "Wilderness owners planning a rooftop tent, platform or heavy basket who want the highest bar rating on offer.",
   "specs": [["Type", "Clamp-on aluminum crossbars"], ["Fits", "2022–2025 Outback Wilderness only"], ["Bar rating", "330 lb (per title)"], ["Vehicle limit", "700 lb static, 200 lb dynamic (Subaru, Wilderness)"], ["Material", "All aluminum"], ["Use", "Tents, platforms, kayaks, boxes"], ["Drilling", "None"]]},
  {"asin": "B0BPY41QBK", "role": "Best lockable Wilderness set", "price": "$90–$130",
   "pros": ["Locks included", "Aluminum bars", "Title says \"Only Fit Wilderness\"", "Aimed at the same Wilderness ladder rail as our other Wilderness picks", "Lists cargo carriers, kayaks, canoes, bikes and snowboards"],
   "cons": ["Title says 2020–2025, but the Wilderness only exists for 2022–2025", "Load rating not in the title", "Not for standard-rail Outbacks"],
   "body": "BougeRV's set is the Wilderness pick for anyone who parks at trailheads and wants the bars locked on. The title names the Outback Wilderness, says \"Only Fit Wilderness,\" and includes locks. The bars are aluminum and the listing mentions cargo carriers, luggage, kayaks, canoes, bikes and snowboards, which covers most Wilderness owners' plans short of a heavy tent. It has been on our Outback list since the page launched, and it is still titled for the right rail.\n\nOne oddity: the title says 2020–2025, but Subaru launched the Wilderness in May 2021 as a 2022 model, so in practice it fits 2022–2025. The title doesn't state a load rating. Read the listing for it, and if you're choosing between this and the 330 lb Tuyoung for a tent, the Tuyoung's published number is the easier one to plan around. Either way the Wilderness's own driving limit is the ceiling, so check the owner's manual before loading the roof.",
   "who": "Wilderness owners who want lockable bars for bikes, boats and boxes more than a maximum-rated tent bar.",
   "specs": [["Type", "Lockable aluminum crossbars"], ["Fits", "Outback Wilderness only (2022–2025 in practice)"], ["Lock", "Yes"], ["Material", "Aluminum"], ["Load rating", "See listing"], ["Use", "Cargo carriers, kayaks, bikes, snowboards"], ["Drilling", "None"]]},
  {"asin": "B0CYWRY9SH", "role": "Wilderness budget pick", "price": "$90–$130",
   "pros": ["300 lb bar rating", "Lockable", "Heavy-duty aluminum", "Title explicitly excludes 2026, which prevents a common mistake", "Wilderness-only fit"],
   "cons": ["No brand-level spec sheet", "Not for standard-rail Outbacks", "Warranty terms only on the listing"],
   "body": "This set earns its place with an honest title: 2022–2025 Outback Wilderness, \"Only Fit Wilderness, NOT for 2026.\" The 2026 Outback is a new generation with different rails, and a buyer searching \"Outback Wilderness crossbars\" can easily land on the wrong one. The bars are rated at 300 lb in the title, are lockable and are heavy-duty aluminum, which is the same core spec as the Soruci and 300 lb lockable sets in our FITS list.\n\nWhat you give up against the Tuyoung is 30 lb of bar rating, which rarely matters since the car's driving limit is lower than either. What you give up against a Thule or Yakima system is a published fit guide and a warranty you can read before you buy. For kayaks, bikes and a cargo box on a 2022–2025 Wilderness, it is a sensible budget set. Recheck the clamps after the first drive and before every long trip.",
   "who": "Wilderness owners who want a lockable 300 lb bar at a budget price and value a title that rules out the 2026.",
   "specs": [["Type", "Lockable aluminum crossbars"], ["Fits", "2022–2025 Outback Wilderness only"], ["Not for", "2026 Outback; standard-rail Outbacks"], ["Bar rating", "300 lb (per title)"], ["Lock", "Yes"], ["Material", "Heavy-duty aluminum"], ["Drilling", "None"]]},
 ],
 "install": [
  "Identify your rail: retractable crossbars built into the side rails means a standard Outback; ladder rails with copper tie-down points and no built-in crossbars means Wilderness.",
  "On a standard Outback, stow the factory crossbars along the rails first and clean the bar sockets, which Autoblog notes can fill with gunk.",
  "Set the bars on the rails loosely and space them to your accessory's spread range, keeping clear of the curve where the rail drops toward the hatch.",
  "Center each bar so the overhang is equal on both sides, then tighten the clamps evenly, alternating sides.",
  "Open the rear hatch fully and check it clears the rear bar and any accessory. Don't open or vent the sunroof with a Thule system on.",
  "Lock the clamps, drive a short loop, then re-torque. Check again before every long trip and after rough roads.",
 ],
 "avoid": [
  {"h": "Wilderness bars on a standard Outback (or vice versa)", "body": "The rails are different shapes. Bars titled \"Only Fit Wilderness\" won't clamp properly to the standard rails, and standard-rail bars aren't listed for the ladder rail."},
  {"h": "2026 Outback parts on a 2020–2025 car", "body": "The 7th generation has new rails and drops the retractable crossbars. Buy parts titled for 2020–2025, and on a Wilderness look for the \"NOT for 2026\" wording."},
  {"h": "Loading to the bar rating", "body": "A 300 or 330 lb bar doesn't raise the Outback's limit: 150 lb on the standard roof and 200 lb while driving on the Wilderness in the Subaru sheets we read. The owner's manual figure, minus any added bars, is what you can carry on the road."},
  {"h": "Leaving bars on year-round when you don't need them", "body": "Autoblog notes bars add wind noise and cost fuel economy. On a standard Outback, the retractable factory bars exist so you don't have to."},
 ],
 "verdict": {
  "thesis": "Match the rail first: a Thule kit or the lockable ERKUL set for standard rails with retractable crossbars, and the 330 lb Tuyoung or lockable BougeRV for the 2022–2025 Wilderness.",
  "body": "Most standard 2020–2025 Outbacks can start with the factory retractable crossbars and only upgrade when width or accessory fit gets in the way. When they do, the Thule kit is the quiet, name-brand route and the ERKUL lockable set is the value route. The Wilderness has no built-in crossbars, so it needs a set, and its 700 lb static roof makes it the trim for tents. The Tuyoung's 330 lb rating is the one to plan a tent around, while the BougeRV and the 300 lb lockable set cover bikes, boats and boxes.\n\nOnce the bars are on, most owners add a cargo box for road trips; our Outback box guide lists the Yakima boxes that clamp to these bars. If the roof is full, a trailer hitch with a bike carrier is the next step, and the vehicle hub has every fit-checked accessory for the 6th-gen Outback.",
 },
 "sources": [
  ["2022 Outback trim comparison: roof rails and roof capacity by trim (Subaru)", "https://www.subaru.com/services/vehicles/pdf/trimComparison/2022/OBK"],
  ["2023 Outback trim comparison: roof rails and roof capacity by trim (Subaru)", "https://www.subaru.com/services/vehicles/pdf/trimComparison/2023/OBK"],
  ["2025 Outback trim comparison: roof rails and roof capacity by trim (Subaru)", "https://www.subaru.com/services/vehicles/pdf/trimComparison/2025/OBK"],
  ["Subaru debuts 2022 Outback Wilderness (Subaru U.S. Media Center)", "https://media.subaru.com/newsrelease.do?fIId=1724&id=1762&mid="],
  ["Subaru announces pricing on all-new 2026 Outback (Subaru U.S. Media Center)", "https://media.subaru.com/pressrelease/2353/subaru-announces-pricing-all-new-2026-outback-suv"],
  ["2022 Outback Wilderness specs (Automotive Fleet)", "https://www.automotive-fleet.com/10144161/subaru-debuts-new-2022-outback-wilderness"],
  ["2020 Outback roof rack systems (etrailer)", "https://www.etrailer.com/roof-2020_Subaru_Outback+Wagon.htm"],
  ["2020–2025 Outback Yakima SkyLine kit (The Rack Shop)", "https://therackshop.com/2020-2025-subaru-outback-w-raised-rails-yakima-crossbar-complete-roof-rack-1/"],
  ["2020 Outback roof rack design (Autoblog)", "https://www.autoblog.com/2019/04/18/2020-subaru-outback-roof-rack/"],
  ["Outback roof rack driveway test (Autoblog)", "https://www.autoblog.com/2020/10/15/subaru-outback-roof-rack-driveway-test/"],
  ["2026 Outback roof rack ratings (The Drive)", "https://www.thedrive.com/news/why-the-2026-subaru-outbacks-roof-rack-has-three-different-weight-ratings"],
  ["Subaru Outback generations (Wikipedia)", "https://en.wikipedia.org/wiki/Subaru_Outback"],
 ],
}

# Product list for this page (replaces the v1 Wilderness-only list). (asin, name, brand, band, cond, note)
FITS = [
 ("B0BZ5L38P3","Thule Roof Rack Crossbars for Subaru Outback, compatible with stowable factory rack (2010-2023), 165 lb","Thule","$500–$750",{"roof_type":"raised-rails"},"Standard rails, not Wilderness; confirm 2024-2025 with seller."),
 ("B0FGYC7XCH","ERKUL Lockable Aluminum Cross Bars, 2020-2025 Subaru Outback with raised rails, black","ERKUL","$80–$130",{"roof_type":"raised-rails"},"Standard rails; Wilderness version is a separate listing."),
 ("B0DH51LV3Z","OMAC Telescopic Cross Bars, 2020-2025 Subaru Outback, 220 lb, silver","OMAC","$80–$130",{"roof_type":"raised-rails"},"Rail type not in title; confirm trim with seller."),
 ("B0CSW8LPBZ","Tuyoung 330 lb Cross Bars, 2022-2025 Subaru Outback Wilderness only","Tuyoung","$100–$140",{"roof_type":"raised-rails","trim":"Wilderness"},"Wilderness ladder rails only."),
 ("B0BPY41QBK","BougeRV Lockable Cross Bars, Subaru Outback Wilderness only","BougeRV","$90–$130",{"roof_type":"raised-rails","trim":"Wilderness"},"Wilderness only (2022-2025 in practice)."),
 ("B0CYWRY9SH","300 lb Lockable Cross Bars, 2022-2025 Subaru Outback Wilderness only (not 2026)","Generic","$90–$130",{"roof_type":"raised-rails","trim":"Wilderness"},"Wilderness only; not 2026."),
 ("B0DR2MZ7JW","ERKUL Lockable Aluminum Cross Bars, 2020-2025 Subaru Outback Wilderness only, silver","ERKUL","$80–$130",{"roof_type":"raised-rails","trim":"Wilderness"},"Wilderness version of the ERKUL set."),
 ("B0CSW5W542","Soruci 300 lb Cross Bars, 2022-2025 Subaru Outback Wilderness only","Soruci","$90–$130",{"roof_type":"raised-rails","trim":"Wilderness"},"Wilderness only."),
 ("B0C1B1M96H","300 lb Lockable Cross Bars, 2022-2025 Subaru Outback Wilderness","Generic","$90–$130",{"roof_type":"raised-rails","trim":"Wilderness"},"Wilderness only."),
]
