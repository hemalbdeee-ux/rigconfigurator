"""Long-form article — Best LED Light Bars & Light Kits for 2020–2026 Jeep Gladiator (JT).
Mirrors the approved pilot (ford_f150_2021_tonneau.py) and the JL / Bronco light-bar pages. No invented hands-on
testing: every spec comes from maker/retailer pages listed in sources (checked 2026-09-27). Bars are mostly
universal; what is Gladiator-specific is the mount (windshield/roof line, A-pillar/cowl, factory bumper and fog
pockets), the Mojave exclusions, and the bumper type, so the picks are JT kits and brackets whose Amazon titles
name the Gladiator. The JT shares its front end with the Wrangler JL, but fit is confirmed per listing.
"""

KEY = ("jeep", "gladiator", "2020-present", "led-light-bars")

TITLE = "Best LED Light Bars for 2020–2026 Jeep Gladiator: 5 JT Kits and Mounts Checked by Location"
META = ("Five Gladiator JT light kits and mounts, from $135 A-pillar pods to a 50 in roof bar, with lumens, amp "
        "draw, Mojave exclusions, bumper fit and road-use rules.")

FAQ = [
 ("What is the best LED light kit for a Jeep Gladiator?",
  "For most owners, the Baja Designs LP6 Pro bumper kit. RealTruck lists it for the 2020–2024 Gladiator JT at $1,159.95, with two LP6 Pro lights, 11,225 lumens of primary output at 103.5 watts, OEM-style brackets that mount to factory locations, a harness and a limited lifetime warranty. Bumper lights sit low, which keeps glare off the hood and keeps them closer to the mounting heights most states use. Buy the version for your bumper: the Amazon listing here is for the OEM steel bumper."),
 ("Do Wrangler JL light bar kits fit the Gladiator?",
  "Many do, because Wikipedia notes the Gladiator shares its platform and everything forward of the front seats with the Wrangler JL. Baja Designs lists its A-pillar, 40 in cowl and 50 in roof kits for both the 2018–2026 JL and 2020–2026 Gladiator, and ZROADZ and Hawkley name both trucks in their titles. Don't assume it, though. Some JL brackets never list the JT, and several JT-compatible kits exclude the Mojave. Buy a listing that names the Gladiator and your model year."),
 ("Which light bar mounts don't fit the Gladiator Mojave?",
  "Several. Baja's S8 50 in roof kit is listed as not fitting Mojave or 392 models, Quadratec says the ZROADZ A-pillar kit will not fit the Mojave, and Hawkley's windshield kit is listed as not for Mojave. Baja's A-pillar and 40 in cowl kits do fit, but Baja says the Mojave cowl is taller and needs longer M6 x 80 mm flange bolts. If you drive a Mojave, check the exclusion line on every listing before anything else."),
 ("Are LED light bars legal on a Gladiator?",
  "Usually only off-road. KC HiLiTES says it is illegal to have off-road-only lights turned on while on the roadway, and that many states also require them to be covered, with California and Pennsylvania among those requiring opaque covers. States also limit how many auxiliary lamps you can run and how high they sit. A 50 in roof-line bar is off-road lighting almost everywhere. SAE-marked fog lights, like Baja's Squadron-R SAE fog pocket kits, are the road-friendly option. Check your own state's rules."),
 ("How much current does a Gladiator light bar draw?",
  "It depends on the light. Baja lists its S8 50 in roof bar at 300 watts and 20 amps, and the S8 40 in cowl bar at 240 watts and 16 amps. The LP6 Pro bumper kit's primary lights are listed at 7.5 amps, and each Squadron Sport A-pillar pod at 2.2 amps. Add up everything on one switch or fuse. A 20 amp bar needs its own relay and fuse from the battery; never run it through a dash switch that isn't built for the load."),
 ("Do I need to drill to mount lights on a Gladiator?",
  "Not for most kits here. Baja says its S8 50 in roof kit needs no drilling, cutting or trimming and that its A-pillar kit mounts to factory locations without trimming. Quadratec says the ZROADZ A-pillar kit needs no cutting, drilling or welding. RealTruck describes the LP6 Pro bumper kit as OEM-style brackets on factory mounting points. One exception: Baja's page for its 40 in S8 cowl kit says it requires vehicle-specific drilling, so read the install sheet first."),
 ("Will a roof light bar cause wind noise on a Gladiator?",
  "It can. Baja's own S8 50 in roof kit page warns that installation may cause wind noise depending on vehicle configuration, and that's the maker being honest about a bar sitting in the airflow above the windshield. None of the pages publish a decibel figure. If you spend long stretches on the highway, A-pillar pods or bumper lights stay out of that airflow. Light covers change the shape of the bar and can change the sound too."),
 ("Should I pick a bumper kit or a fog pocket kit for my Gladiator's factory bumper?",
  "Match the bumper first. Amazon listings for Baja's Squadron-R SAE fog pocket kits are sold separately for the OEM Sport bumper and the OEM Sahara bumper, and Baja's LP6 Pro and XL80 bumper kits are listed for the OEM steel bumper, with a separate plastic-bumper LP6 kit. Wikipedia notes the Mojave comes with a steel front bumper. Look at your bumper, or your window sticker, and buy the kit that names it."),
 ("What light bar length fits a Gladiator windshield?",
  "The common sizes are 50 and 52 in over the windshield and 40 in at the cowl. Baja's roof kit uses a 50 in S8 bar, Hawkley's brackets take a 50–52 in bar, and Baja's cowl kit uses a 40 in S8. For hood mounting, JL-style cowl brackets take a 20 in bar, but check the listing for the Gladiator. Measure against the bracket spacing in the listing, not just the bar's nominal length, because end-bracket designs vary between brands."),
 ("Is a Gladiator 4xe light bracket something I need to worry about?",
  "No. Wrangler owners see 4xe exclusions on many bracket listings, but Wikipedia reports the planned Gladiator 4xe hybrid was cancelled in September 2025, so there is no 4xe Gladiator to fit. The trim that matters on the JT is the Mojave, whose taller cowl and different setup show up as exclusions or bolt notes on several light kits. If a listing only mentions 4xe and Mojave exclusions together, the Mojave part is the one that applies to you."),
]

ARTICLE = {
 "dek": "Five Gladiator light setups, from a $135 A-pillar pod kit to a 50 in roof bar and a factory-point bumper kit. Bars are mostly universal, so we focus on what is specific to the 2020–2026 JT: the mount, the Mojave exclusions, the steel, plastic, Sport and Sahara bumpers, the wiring and amp draw, and the road rules that decide when you can switch them on.",
 "author": "jake-morrison",
 "reviewed": "2026-09-27",
 "method": "We did not install these lights ourselves. We ranked them on published specs (lumens, watts, amps, sealing, harness, warranty), on the fitment each maker, retailer or Amazon listing gives for the 2020–2026 Gladiator JT and its trims, and on KC HiLiTES' general guidance on auxiliary lighting. Gladiator facts come from Wikipedia and the retailer fitment notes. Prices were checked at Baja Designs, RealTruck and Quadratec in September 2026. Amazon prices change daily, so the button shows the live price.",
 "takeaways": [
  "**Choose the mount first.** Roof line, A-pillar/cowl, bumper or fog pocket. The bar is universal; the bracket has to name the Gladiator.",
  "**Mojave owners, check exclusions.** Baja's 50 in roof kit, the ZROADZ A-pillar kit and Hawkley's brackets are listed as not fitting the Mojave; Baja's A-pillar kit needs longer bolts on its taller cowl.",
  "**Match the bumper.** Baja sells steel- and plastic-bumper LP6 kits, and fog pocket kits for the Sport and Sahara bumpers.",
  "**Size the wiring to the draw.** Baja's 50 in S8 bar pulls 20 A; it needs a relay, fuse and switch or a proper upfitter circuit.",
  "**Roof bars are off-road lights.** Keep them off, and covered where your state requires it, on public roads.",
 ],
 "top_picks": [
  {"asin": "B0CCXF7N84", "role": "Best overall", "why": "Two LP6 Pro lights on factory steel-bumper points, 11,225 lm, harness included"},
  {"asin": "B0CCX9M9K9", "role": "Best roof light bar", "why": "50 in S8, 31,750 lm, IP69K, no drilling, listed 2020–2026 JT (not Mojave)"},
  {"asin": "B07G1CSP2M", "role": "Best A-pillar kit", "why": "Two 3,200 lm pods at factory points, fits Mojave with longer bolts, from $398.95"},
  {"asin": "B07GNNCQFM", "role": "Best budget complete kit", "why": "Brackets, two 3 in pods and harness, no drilling, $134.50 at Quadratec"},
  {"asin": "B0B2LTBF3T", "role": "Best budget windshield brackets", "why": "50–52 in bar brackets plus A-pillar spots, listed 2019–2026 Gladiator"},
 ],
 "fit_table": {
  "caption": "2020–2026 Gladiator JT details that affect light mounting",
  "head": ["Item", "Applies to", "What it means for lights"],
  "rows": [
   ["Shared front end with Wrangler JL", "All JT", "Many JL kits also list the JT, but confirm the Gladiator is named on the listing."],
   ["Mojave", "Mojave trims", "Excluded by Baja's 50 in roof kit, ZROADZ A-pillar and Hawkley brackets. Baja A-pillar needs M6 x 80 mm bolts on the taller cowl."],
   ["Front bumper", "Steel, plastic, OEM Sport or Sahara bumper by trim", "Bumper and fog pocket kits are bumper-specific. Know which one you have."],
   ["Windshield / roof line", "All JT; top is removable", "50–52 in bars mount on windshield-frame brackets, not the roof panels."],
   ["4xe", "None; Gladiator 4xe cancelled (Wikipedia)", "Ignore 4xe notes; Mojave notes still apply."],
  ],
 },
 "look_for": [
  {"h": "Mount location comes before the bar",
   "body": "On a Gladiator, the light itself is rarely what goes wrong. Most 50 and 52 in bars bolt to a pair of end brackets, and dozens of brands make them. What has to match your truck is the mount. Windshield-frame brackets hold a long bar above the windshield. A-pillar or cowl brackets hold two pods, or a 40 in bar, at the base of the windshield. Bumper kits put pods into the factory bumper, and fog pocket kits replace the fog lamps. Each location gives a different beam, glare and road-use picture, so pick the location first, then a mount whose listing names the Gladiator JT and your model year, then the light."},
  {"h": "Mojave exclusions and the shared JL front end",
   "body": "Wikipedia notes that the Gladiator shares its platform and everything forward of the front seats with the Wrangler JL, which is why so many JL light kits also list the JT. The Mojave is the exception to watch. Baja lists its S8 50 in roof kit for the 2020–2026 Gladiator but says it does not fit Mojave or 392 models. Quadratec says the ZROADZ A-pillar kit will not fit the Mojave, and Hawkley lists its windshield brackets as not for Mojave. Baja's A-pillar and 40 in cowl kits do fit, but Baja says the Mojave cowl is taller and needs longer M6 x 80 mm flange bolts. Filter by trim before you add anything to the cart."},
  {"h": "Bumper type: steel, plastic, Sport or Sahara",
   "body": "Bumper kits and fog pocket kits bolt into the factory bumper, so they are only as good as the match. Baja sells its LP6 Pro bumper kit in separate versions for the OEM steel bumper and the OEM plastic bumper, and its XL80 bumper kit is also listed for the steel bumper. Its Squadron-R SAE fog pocket kits are sold as separate listings for the OEM Sport bumper and the OEM Sahara bumper. Wikipedia notes the Mojave has a steel front bumper, and other trims vary. Look at your bumper, or your window sticker, before ordering. If you've fitted an aftermarket bumper, buy lights for that bumper's own light mounts instead."},
  {"h": "Wiring, relay, fuse and amp draw",
   "body": "A proper harness has a relay so the switch carries a small signal, an inline fuse sized for the light, and a switch you can reach from the seat. Baja and ZROADZ include harnesses; with bracket kits, check what's in the box. Then check the draw. Baja lists its S8 50 in bar at 300 watts and 20 amps, and the S8 40 in cowl bar at 16 amps. The LP6 Pro bumper kit lists 7.5 amps of primary draw, and each Squadron Sport pod 2.2 amps. Baja sells toggle and upfitter harness versions; the upfitter version is for Jeeps with a factory auxiliary switch bank. If you don't have one, buy the toggle version and add up every load on each fuse."},
  {"h": "Road rules, covers, sealing and wind noise",
   "body": "Nearly every bar and spot pod here is an off-road light. KC HiLiTES says off-road-only lights must be off on the roadway and that many states also require them covered, with California and Pennsylvania requiring opaque covers. KC adds that states commonly limit auxiliary driving lights to about 16–42 in above the ground and fog lamps to about 12–30 in, which is why low bumper lights are the easiest to live with. SAE J583 fog lamps are the road-friendly choice. For sealing, Baja rates its S8 bars IP69K and IK10. Baja also warns its 50 in roof kit may cause wind noise depending on configuration."},
 ],
 "look_table": {
  "head": ["Feature", "Look for", "Avoid"],
  "rows": [
   ["Fitment", "Listing names the Gladiator JT and your model year", "JL-only brackets with no JT mention"],
   ["Trim", "Stated Mojave fit or exclusion", "Listings that ignore the Mojave's taller cowl"],
   ["Bumper", "Kit matched to steel, plastic, Sport or Sahara bumper", "Fog pocket kits for the wrong bumper"],
   ["Wiring", "Harness with relay, fuse and switch; published amps", "Bare lights with no relay or fuse"],
   ["Sealing", "IP69K or IP68 stated", "\"Waterproof\" with no rating"],
   ["Covers", "Covers available for any roof bar", "No cover option in a covers-required state"],
  ],
 },
 "types_table": {
  "caption": "Gladiator light mount locations compared",
  "head": ["Mount", "Example on this page", "Beam use", "Glare", "Road use", "Trade-off"],
  "rows": [
   ["Windshield / roof line", "Baja S8 50 in roof kit", "Long-range distance", "Most (off hood)", "Off-road only in most states", "Wind noise, Mojave excluded"],
   ["A-pillar / cowl pods", "Baja Squadron Sport, ZROADZ 3 in pods", "Wide, trail edges and corners", "Some", "Usually off-road only", "Less reach than a big bar"],
   ["Cowl bar (40 in)", "Baja Squadron Sport/S8 40 in kit (in list)", "Mid- to long-range", "Moderate", "Off-road only in most states", "Baja lists drilling"],
   ["Front bumper pods", "Baja LP6 Pro bumper kit", "Driving and fill", "Least", "Closer to legal mounting heights", "Steel vs plastic kits"],
   ["Fog pockets", "Baja Squadron-R SAE kits (in list)", "Fog and near fill", "Least", "SAE fog lamps usable on road", "Sport vs Sahara bumper kits"],
  ],
 },
 "picks": [
  {"asin": "B0CCXF7N84", "role": "Best overall", "price": "$1,160",
   "pros": ["Mounts to factory bumper points with OEM-style brackets", "11,225 lm primary output at 103.5 W (RealTruck)", "Modest 7.5 A primary draw", "Harness, brackets and stainless hardware included", "Replaceable optics, limited lifetime warranty"],
   "cons": ["Most expensive bumper option here", "Steel and plastic bumpers need different kits", "Amazon title reads 2020–22 JT; RealTruck lists 2020–2024"],
   "body": "If you want strong light on a Gladiator without a bar in the airflow above the windshield, Baja's LP6 Pro bumper kit is the one to buy. RealTruck lists two LP6 Pro lights with 11,225 lumens of primary output and 1,972 lumens of backlighting, at 103.5 watts and 7.5 amps of primary draw, in a driving/combo pattern. The lights mount to factory locations with OEM-style brackets, so the result looks fitted rather than bolted on. The housings are hard-anodized machined aluminum with hard-coated polycarbonate lenses, the optics and lenses are replaceable, the hardware is stainless, and Baja's MoistureBlock sealing is built in.\n\nRealTruck lists the upfitter version (447671UP) at $1,159.95 for the 2020–2024 Gladiator JT and 2018–2024 Wrangler JL, with a limited lifetime warranty. This Amazon listing is the OEM steel bumper version with a toggle-switch harness, and its title reads 2020–22, so check your year and bumper before ordering; Baja sells a separate kit for the OEM plastic bumper. RealTruck's page doesn't mention 2025–2026 trucks, so newer owners should confirm fit with the seller. Bumper-height lights throw far less glare off the hood and sit closer to the heights KC says most states allow, though you still need to follow your state's auxiliary-lamp rules.",
   "who": "Steel-bumper Gladiator owners who want the best all-round light with a factory look and the least glare.",
   "specs": [["Type", "Bumper pod kit (2 lights)"], ["Part #", "447671UP (RealTruck, upfitter)"], ["Fits", "2020–2024 Gladiator JT, 2018–2024 JL (RealTruck)"], ["Output", "11,225 lm primary, 103.5 W"], ["Current", "7.5 A primary"], ["Beam", "Driving/combo"], ["Harness", "Toggle (this listing) or upfitter"], ["Warranty", "Limited lifetime"], ["Price", "$1,159.95 (RealTruck)"]]},
  {"asin": "B0CCX9M9K9", "role": "Best roof light bar", "price": "From $2,054",
   "pros": ["50 in S8 bar at 31,750 lumens", "IP69K and IK10 rated", "No drilling, cutting or trimming (Baja)", "Stainless brackets and pre-sized wiring included", "Listed for 2020–2026 Gladiator JT"],
   "cons": ["Not for Mojave (or 392) per Baja", "20 A draw needs a proper relay circuit", "Baja warns of possible wind noise"],
   "body": "For maximum reach, Baja's S8 50 in roof mount kit is the premium answer. Baja lists the 50 in S8 bar at 31,750 lumens, 300 watts and 20 amps, with 40 Cree LEDs at 5000K in a driving/combo pattern. The bar is 1.6 in tall and 3 in deep and weighs 10.75 lb, in an aircraft-grade aluminum housing with a mil-spec hard anodize. Baja rates it IP69K (waterproof to 9 ft and pressure washable) and IK10 for impact, and says it exceeds MIL-STD-810G. The kit includes stainless brackets and pre-sized wiring, with an upfitter harness for compatible models, and Baja says it needs no drilling, cutting or trimming.\n\nBaja lists fit for the 2020–2026 Gladiator and 2018–2026 JL, but not for Mojave or 392 models. It starts at $2,053.95 with a limited lifetime warranty and 30-day money-back guarantee. Two cautions. At 20 amps, the bar needs its own relay and fuse, or a circuit rated for it. And Baja's own page warns the install may cause wind noise depending on configuration, which is the trade-off of any roof-line bar. The Amazon title reads 2020–23, so confirm the year and lens. This is an off-road light: keep it off, and covered where required, on public roads.",
   "who": "Non-Mojave owners who run open desert or fast fire roads at night and want the most reach.",
   "specs": [["Type", "50 in roof-line light bar kit"], ["Part #", "705003 (Baja SKU)"], ["Fits", "2020–2026 JT, 2018–2026 JL; not Mojave or 392 (Baja)"], ["Output", "31,750 lm, 300 W"], ["Current", "20 A"], ["Beam", "Driving/combo, 5000K"], ["Sealing", "IP69K, IK10"], ["Mounting", "No drilling, cutting or trimming"], ["Price", "From $2,053.95 (Baja)"]]},
  {"asin": "B07G1CSP2M", "role": "Best A-pillar kit", "price": "From $399",
   "pros": ["Two pods at 3,200 lm, 30 W, 2.2 A each", "Driving combo and wide cornering lenses included", "Factory mounting points, no trimming", "Fits Mojave with longer M6 x 80 mm bolts", "Lifetime limited warranty, 30-day guarantee"],
   "cons": ["Less reach than a 50 in bar", "Amazon title is older (2020–22 JT, Spot); confirm version", "Still off-road lighting in most states"],
   "body": "A-pillar pods light the trail edges and the corners you steer into, which is where a long-range bar is least useful. Baja's Squadron 2.0 Sport A-pillar kit is the cleanest way to add them to a Gladiator. Baja lists two pods at 3,200 lumens, 30 watts and 2.2 amps each, and includes both driving combo and wide cornering lens kits so you can change the pattern. There are nine selectable backlight colors, the brackets use factory JL/JT locations with extra vertical adjustment, and Baja says no trimming or other modification is needed. The kit starts at $398.95 with a lifetime limited warranty and a 30-day satisfaction guarantee.\n\nFit is the broadest on this page. Baja lists the 2020–2026 Gladiator and 2018–2026 JL, and it covers the Mojave with one note: the Mojave cowl is taller and needs longer M6 x 80 mm flange bolts. The toggle version uses a 4-pin Deutsch two-light harness; the upfitter version adds a 55 in Deutsch splitter. This Amazon listing is titled for the 2020–22 Gladiator with spot lenses, which may be the earlier Squadron Sport, so confirm the version before ordering. At about 4.4 amps for the pair, it sits comfortably on a modest fused circuit.",
   "who": "Owners on slow, twisty trails, including Mojave owners, who want wide light with a factory-fit mount.",
   "specs": [["Type", "A-pillar pod kit (2 lights)"], ["Part #", "44-0043 (Baja)"], ["Fits", "2020–2026 JT, 2018–2026 JL (Baja)"], ["Output", "3,200 lm, 30 W, 2.2 A each"], ["Lenses", "Driving combo and wide cornering"], ["Harness", "Toggle (4-pin Deutsch) or upfitter"], ["Mojave note", "M6 x 80 mm flange bolts"], ["Warranty", "Lifetime limited"], ["Price", "From $398.95 (Baja)"]]},
  {"asin": "B07GNNCQFM", "role": "Best budget complete kit", "price": "About $135",
   "pros": ["Brackets, two 3 in pods, harness and hardware in one box", "No cutting, drilling or welding (Quadratec)", "Uses factory A-pillar mounting points", "Under an hour to install, per Quadratec", "Limited lifetime warranty"],
   "cons": ["Will not fit the Mojave (Quadratec)", "No published lumens, watts or IP rating", "Harness details not listed; confirm relay and fuse"],
   "body": "ZROADZ's Z364941-KIT2 is the cheapest complete A-pillar kit on this page from a brand that makes vehicle-specific mounts. Quadratec lists it with two 3 in LED pod lights, the lower A-pillar brackets, a wiring harness and installation hardware, and says it bolts to the factory A-pillar mounting locations with no cutting, drilling or welding. Quadratec rates the install as intermediate and under an hour, and lists a limited lifetime warranty. When we checked, Quadratec showed an in-cart price of $134.50 against a $280 list price, which is about a third of Baja's A-pillar kit.\n\nThe trade-offs are fit and data. Quadratec lists the kit for the 2020 and newer Gladiator JT and the JL, but says it will not fit the Mojave. Neither Quadratec's page nor the listing publishes lumens, watts, beam pattern or a sealing rating for the pods, so you're buying on the bracket and the brand rather than on output figures. Check the harness in the box for a relay and inline fuse before you connect it. For owners who mostly want corner and trail-edge light at a low price, it's a sensible first step, and the brackets can take better 3 in pods later.",
   "who": "Non-Mojave owners who want a complete A-pillar kit for the least money.",
   "specs": [["Type", "Lower A-pillar kit with 2x 3 in pods"], ["Part #", "Z364941-KIT2"], ["Fits", "2020+ Gladiator JT, JL; not Mojave (Quadratec)"], ["Included", "Brackets, 2 pods, harness, hardware"], ["Mounting", "Factory points, no drilling"], ["Install", "Under 1 hr (Quadratec)"], ["Warranty", "Limited lifetime"], ["Price", "$134.50 in cart (Quadratec)"]]},
  {"asin": "B0B2LTBF3T", "role": "Best budget windshield brackets", "price": "Check listing",
   "pros": ["Brackets for a 50–52 in bar plus A-pillar mounts", "Two 4 in spot lights included", "Listed for 2019–2026 Gladiator and 2018–2026 JL", "Choose any bar with standard end brackets", "Far cheaper than a complete branded roof kit"],
   "cons": ["Not for Mojave, per listing", "Bar, relay harness and covers sold separately", "Specs limited to the listing"],
   "body": "Hawkley's kit is the budget route to a bar above the windshield plus a pair of A-pillar spots. The listing includes brackets for a 50–52 in bar across the windshield frame, A-pillar brackets, and two 4 in LED spot lights, and names the 2018–2026 Wrangler JL and the 2019–2026 Gladiator JT. The Gladiator went on sale as a 2020 model, so read that year range as covering every JT to date. The broad range is useful, because several cheaper brackets stop at 2020 or 2023. You supply the bar, which lets you pick any 50 or 52 in light that uses standard end brackets, from a budget bar to a branded one.\n\nThe listing excludes the Mojave, which lines up with what Baja, ZROADZ and Quadratec say about that trim's windshield and cowl area. Hawkley's listing is the only spec source, so check the bracket material and hardware before ordering. Budget for a harness with a relay, fuse and switch, sized for the bar you choose; a big 50 in bar can pull 20 amps. Keep in mind that a windshield-height bar reflects the most light off the hood and sits well above the mounting heights KC says most states use, so it's off-road lighting.",
   "who": "Non-Mojave owners who want a 50–52 in bar plus A-pillar spots for the lowest cost.",
   "specs": [["Type", "Windshield + A-pillar bracket kit"], ["Bar size", "50–52 in (bar not included)"], ["Included", "Brackets, 2x 4 in spot lights"], ["Fits", "2019–2026 Gladiator JT, 2018–2026 JL (per listing)"], ["Exclusions", "Not Mojave or 4xe"], ["Price", "Check listing"]]},
 ],
 "install": [
  "Confirm your mount location, your trim (Mojave or not) and your bumper (steel, plastic, Sport or Sahara) against the listing, and check that it names the Gladiator JT and your model year.",
  "Disconnect the negative battery terminal before any wiring work.",
  "Fit the brackets at the factory points the instructions show (windshield frame, A-pillar/cowl or bumper), using the longer bolts if a Mojave note applies, and leave them loose for aiming.",
  "Route the harness away from the exhaust, steering and suspension, mount the relay and fuse near the battery, and put the switch within reach. Use an upfitter harness only if your Jeep has a factory auxiliary switch bank.",
  "Reconnect the battery, test the lights, then aim them at night on level ground and tighten every bracket bolt.",
  "Fit covers where your state requires them, keep off-road lights off on public roads, and re-check bracket bolts after the first trail run.",
 ],
 "avoid": [
  {"h": "Assuming a Mojave fits like any JT", "body": "Baja's 50 in roof kit, ZROADZ's A-pillar kit and Hawkley's brackets exclude the Mojave, and Baja's A-pillar kit needs longer bolts on its taller cowl."},
  {"h": "Buying a JL kit that never names the Gladiator", "body": "The front ends are shared, but only a listing that names the JT and your year is a safe buy. Ask the seller when it doesn't."},
  {"h": "Running a 20 A bar without a relay", "body": "Baja's 50 in S8 bar draws 20 amps. Use a harness with a relay, a correctly sized fuse and a switch."},
  {"h": "The wrong bumper kit", "body": "Baja sells different kits for steel and plastic bumpers, and fog pocket kits for Sport and Sahara bumpers. Check yours first."},
 ],
 "verdict": {
  "thesis": "Pick the mount before the light: Baja's LP6 Pro bumper kit for the best all-round setup, Baja's Squadron Sport A-pillar kit for trail corners (Mojave included), and the S8 50 in roof kit only if you need maximum reach and don't drive a Mojave.",
  "body": "On a 2020–2026 Gladiator, the bar is the easy part and the mount is where fit goes wrong. Baja's LP6 Pro bumper kit is the best all-round choice because it uses factory mounting points, draws a modest 7.5 amps and keeps glare low. The Squadron Sport A-pillar kit lights the trail edges for about $400 and is the one premium kit here that fits the Mojave. Baja's S8 50 in roof kit gives the most reach, at a high price and with a warned-about wind-noise risk. ZROADZ and Hawkley cover the budget end with JT-specific brackets, as long as you don't own a Mojave. Whatever you choose, wire it with a relay and fuse, and follow your state's cover and aux-light rules.\n\nThe Gladiator's roof comes off, so there's no roof rack to hang lights from; the windshield frame and bumper do that job, and a bed rack is where many owners add rear-facing scene lights. If you're outfitting the truck at the same time, the same fit rules apply to a tonneau cover, a trailer hitch and floor liners. Wrangler owners should see our 2018–2026 Wrangler light bar guide, which covers the 4xe and 392 notes the JT doesn't need.",
 },
 "sources": [
  ["Baja Designs LP6 Pro Bumper Kit 447671UP, JL/JT (RealTruck)", "https://realtruck.com/p/baja-designs-jeep-lights-bumper-kits/bdi-447671up/"],
  ["Jeep JL/JT S8 50 in Roof Mount Light Kit (Baja Designs)", "https://www.bajadesigns.com/products/jeep-jl-jt-s8-50-inch-roof-mount-light-kit-jeep-2020-gladiator-2018-22-wrangler-jl-exc-rubicon-392/"],
  ["Squadron Sport A-Pillar Light Kit, JL/JT (Baja Designs)", "https://www.bajadesigns.com/products/2018-Jeep-JL-A-Pillar-Sportsmen-Kit.asp"],
  ["Jeep JL/JT Squadron Sport/S8 40 in A-Pillar/Cowl Mount Kit (Baja Designs)", "https://www.bajadesigns.com/products/jeep-jl-jt-squadron-sport-s8-40-inch-a-pillar-cowl-mount-light-kit-jeep-2020-2022-gladiator-2018-2022-wrangler-jl/"],
  ["ZROADZ Z364941-KIT2 A-Pillar LED Light Mounts with 3 in Pods (Quadratec)", "https://www.quadratec.com/p/zroadz/pillar-lower-led-light-mounts-2-3-pod-led-lights-jeep-wrangler-jl"],
  ["Are LED light bars and auxiliary lights street legal? (KC HiLiTES)", "https://www.kchilites.com/campfire/post/are-led-light-bars-and-auxiliary-lights-street-legal"],
  ["Jeep Gladiator (JT) — trims, Mojave, shared JL platform, 4xe cancellation (Wikipedia)", "https://en.wikipedia.org/wiki/Jeep_Gladiator_(JT)"],
 ],
}

# Product list for this page. (asin, name, brand, band, cond, note)
FITS = [
 ("B0CCXF7N84","Baja Designs LP6 Pro LED Bumper Light Kit for Jeep Gladiator 2020-22, Wrangler JL 2018-22 with OEM Steel Bumper (Toggle Switch Wiring Harness)","Baja Designs","$1,100–$1,250",{"mount":"bumper","bumper":"steel"},"Steel bumper only; RealTruck lists 2020-2024 JT — confirm 2025-2026."),
 ("B0CCX9M9K9","Baja Designs S8 50-Inch LED Bar Roof Mount Light Kit for Jeep Gladiator 2020-23, Wrangler JL 2018-23 (Driving/Combo Clear Lens)","Baja Designs","$1,950–$2,150",{"mount":"windshield"},"Baja: not for Mojave; title to 2023 — confirm year."),
 ("B07G1CSP2M","Baja Designs Squadron Sport LED A-Pillar Light Kit for Jeep Gladiator 2020-22, Wrangler JL 2018-22 (Spot; Clear)","Baja Designs","$380–$450",{"mount":"a-pillar"},"Mojave needs M6 x 80 mm bolts; confirm Squadron version on listing."),
 ("B07GNNCQFM","ZROADZ Jeep JL, Gladiator A Pillar LED Kit with (2) 3 Inch LED Pod Lights, Z364941-KIT2","ZROADZ","$130–$280",{"mount":"a-pillar"},"Not for Mojave (Quadratec)."),
 ("B0B2LTBF3T","Hawkley A-Pillar Light Bar Windshield Mount Brackets, JL 2018-2026 / Gladiator JT 2019-2026, 50-52 in bar mount + 2x 4 in spot lights (not 4xe / Mojave)","Hawkley","$80–$120",{"mount":"windshield"},"Not for Mojave; bar sold separately."),
 ("B0CCXMBVZ3","Baja Designs XL80 LED Bumper Light Kit for Jeep Gladiator 2020-22, Wrangler JL 2018-22 with OEM Steel Bumper (Driving/Combo Clear)","Baja Designs","Check listing",{"mount":"bumper","bumper":"steel"},"Steel bumper only; confirm year."),
 ("B0CCXHJXP3","Baja Designs OnX6+ 50-Inch LED Bar Roof Mount Light Kit for Jeep Gladiator 2020-23, Wrangler JL 2018-23 (Driving/Combo Clear)","Baja Designs","Check listing",{"mount":"windshield"},"Baja lists exc. 392; confirm Mojave fit."),
 ("B08759C2MZ","Baja Designs Squadron-R SAE LED Fog Pocket Light Kit for Jeep Gladiator JT 2020-24, Wrangler JL, OEM Sahara Bumper (Amber)","Baja Designs","Check listing",{"mount":"fog-pocket","bumper":"sahara"},"Sahara bumper only; SAE fog."),
 ("B07YYND5YF","Baja Designs Squadron-R SAE Fog Pocket LED Light Kit, Jeep Gladiator 2020-22, Wrangler JL, OEM Sport Bumper (Wide Cornering; Amber)","Baja Designs","Check listing",{"mount":"fog-pocket","bumper":"sport"},"Sport bumper only; confirm year."),
 ("B0BMTXQZLT","Hawkley 50/52 in A-Pillar Light Bar Mounting Brackets, 2018-2026 Wrangler JL/JLU & Gladiator JT 2019-2026","Hawkley","$50–$80",{"mount":"windshield"},"Brackets only; confirm Mojave fit."),
 ("B07M5K9LMX","AUXMART 52 in Windshield Light Bar Brackets with A-pillar mounts, 2018-2022 JL / Gladiator (not Mojave)","AUXMART","$50–$80",{"mount":"windshield","year_to":2022},"Listed to 2022; confirm later years."),
 ("B07VBKHKC8","omotor 52 in LED Light Bar Upper Windshield A-Pillar Mounting Brackets, Jeep Wrangler JL / Gladiator JT 2020","omotor","Check listing",{"mount":"windshield"},"Title names 2020 only; confirm year and Mojave fit."),
 ("B0BW4WD653","KC HiLiTES 7328 50 in Light Bar Overhead Bracket Set, Jeep 392 / Mojave","KC HiLiTES","Check listing",{"mount":"windshield","trim":"mojave"},"Brackets only; for Mojave — confirm Gladiator fit with seller."),
]
