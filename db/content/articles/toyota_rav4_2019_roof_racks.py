"""Long-form article — Best Roof Racks / Crossbars for the 2019–2025 Toyota RAV4 (5th gen, XA50).
Mirrors the approved pilot (ford_f150_2021_tonneau.py). No invented hands-on testing: vehicle facts come from
our vehicle data, Wikipedia and the etrailer fit guide; product facts come from the Amazon listing titles recorded
in FITS (carried over from fitments_v2) plus the retailer pages in SOURCES (checked 2026-09-24).
Note: the DB gen slug is "2019-present", but the XA50 ended with MY2025 (6th gen XA60 is MY2026).
Source fixes 2026-10-04: Adventure / TRD Off-Road / Woodland rail wording limited to what the listings and Toyota say (no unconfirmed rail profile claim); TRD Off-Road years set to 2020-2024; roof load attributed (165 lb working figure, 176.4 lb from RAV4Resource, owner manual is the authority); Hybrid and Prime shared-roof claim replaced with what the titles say; Woodland factory cross bars noted from Toyota.
Text fixes 2026-10-04 (round 2): 165 lb is no longer called a working figure or stated as the roof limit; it is named as this site's vehicle data number, not confirmed from Toyota (no Toyota roof figure could be confirmed; RAV4Resource's 176.4 lb kept with attribution; the owner's manual is the authority); VEVOR 160 lb bar rating no longer compared with an unconfirmed roof limit; Toyota Adventure cross bars PT278-42191 added from a Toyota dealer catalog (Adventure-specific part, no load figure printed).
"""

KEY = ("toyota", "rav4", "2019-present", "roof-racks")

TITLE = "Best Roof Racks for 2019–2025 Toyota RAV4: 5 Crossbars by Rail Type (Standard, Adventure/TRD, LE)"
META = ("Five crossbars for the 5th-gen RAV4, split by rail: standard raised rails, Adventure/TRD Off-Road rails and "
        "the bare-roof LE, with load limit, spread and noise notes.")

FAQ = [
 ("Which crossbars fit my RAV4 — how do I tell my rail type?",
  "Look at the roof and the badge. Our vehicle data puts standard raised rails on XLE and up, which is what most crossbar listings mean by \"2019–2025 RAV4.\" Listings treat the Adventure and TRD Off-Road rails as a separate fit, and the Autekcomma title excludes the Woodland as well. Our vehicle data lists the LE with a bare roof. Match the listing's exclusions to your badge: several bars here say \"not Adventure / TRD Off-Road\" in the title."),
 ("Do regular RAV4 crossbars fit the Adventure or TRD Off-Road?",
  "Not the ones sold for standard rails. The Autekcomma, FLYCLE and VEVOR titles all exclude the Adventure and TRD Off-Road, and the Autekcomma also excludes the Woodland and LE. The listings don't say what differs, and we could not confirm the rail profile from Toyota, but three sellers exclude those trims, so don't count on a standard-rail clamp fitting. A Toyota dealer's parts catalog (North Park Toyota) also lists Toyota's own Adventure cross bars, PT278-42191, as made specifically for RAV4 Adventure models. The ROKIOTOEX set is the one here sold specifically for the Adventure and TRD rails."),
 ("What can I put on a RAV4 LE with no rails?",
  "None of the clamp-on bars on this page, because they need raised rails. A bare-roof LE needs a door-jamb clamp system. etrailer lists Thule WingBar Evo for the 2021 RAV4's naked roof at $704.85 and SquareBar Evo at $604.85. The other route is fitting factory-style side rails first, then buying raised-rail bars; ask a Toyota dealer about that. The clamp kits are the simpler route."),
 ("What is the RAV4's roof load limit?",
  "We could not confirm a roof load figure from a Toyota document, so read the Cargo and Luggage section of your owner's manual. RAV4Resource lists 176.4 lb (80 kg) for 2019–2024 models and points to that section. This site's vehicle data lists 165 lb, which we could not trace to Toyota. A Toyota dealer's catalog page for Toyota's Adventure cross bars prints no load figure and says to see the owner's manual for weight limits. The limit covers the crossbars, the accessory and the cargo together while driving. A 260 lb or 160 lb rating on a crossbar listing describes the bar, not what the RAV4's roof can carry."),
 ("Can a RAV4 carry a rooftop tent?",
  "Owners fit light tents, but the RAV4 gives you less margin than a truck or a Wilderness Subaru. The tent and bars have to stay under the driving limit in your owner's manual (165 lb in our vehicle data, 176.4 lb on RAV4Resource, neither confirmed from Toyota), and Toyota doesn't publish a headline static rating for the rails that we could confirm. Ask the tent maker whether it approves the RAV4, use a strong bar such as the 260 lb Autekcomma, and check your owner's manual before committing."),
 ("Do these crossbars fit the RAV4 Hybrid and Prime?",
  "Yes, when the rail matches. The crossbar titles here go by rail and trim, not powertrain. None excludes the Hybrid or Prime (renamed Plug-in Hybrid for 2025). What they exclude are the LE, Adventure, TRD Off-Road and, on the Autekcomma, the Woodland. The Woodland Edition is a hybrid-only grade, and Toyota's 2024 release gives it high profile black roof rails with standard cross bars. Buy the bars for your rail, not your powertrain, and ask the seller if your grade isn't named."),
 ("Do 2019–2025 RAV4 crossbars fit a 2026 RAV4?",
  "Don't assume so. The 2026 RAV4 is an all-new sixth generation, revealed in May 2025. Some Amazon listings stretch their year range as models change, so a bar that says \"2019–2026\" may or may not have been checked on the new roof. For a 2026, buy bars that name the 2026 and confirm the rail type with the seller."),
 ("How far apart should RAV4 crossbars be?",
  "Clamp-on bars slide along the raised rail, so you set the spread. Every cargo box publishes a minimum and maximum spread, and our RAV4 cargo box guide lists them for the Yakima boxes we cover. Kayak and bike mounts are steadier with more spread. Set the bars inside the accessory's range before tightening. Keep the rear bar forward of where the rail drops toward the liftgate, and check that the open liftgate clears the rear bar and anything on it."),
 ("Which crossbars are quietest on a RAV4?",
  "Aero (teardrop) aluminum bars are quieter than square or round steel ones. The Rack Shop says Yakima's teardrop JetStream bars cut wind noise better than its steel CoreBar. Most of the Amazon sets here are aluminum aero bars. For the cleanest look, etrailer lists the flush Yakima TimberLine FX for the RAV4 at $599.90. Trim overhang, keep the end caps in, and remove the bars between trips if noise bothers you."),
 ("Can I open the sunroof with crossbars on?",
  "etrailer attaches a note to the Thule systems it fits to the RAV4: it is not recommended to open, vent or retract the sun, moon or glass roof while the product is installed. A loaded bar can sit near the glass panel's path. Treat that as the rule for any rack on a RAV4 with a sunroof or panoramic roof."),
]

ARTICLE = {
 "dek": "Crossbar listings split the 5th-generation RAV4 into three roofs: standard raised rails on XLE and up, the Adventure and TRD Off-Road rails that standard-rail listings exclude (one also excludes the Woodland), and a bare roof on the LE. Here are five crossbar sets matched to the first two, what the LE needs instead, and the load, spread and noise details that decide which set you buy.",
 "author": "jake-morrison",
 "reviewed": "2026-10-04",
 "method": "We did not install these crossbars ourselves. We matched each set to the RAV4 rail type named in its Amazon listing title and checked the vehicle facts against our vehicle data, Wikipedia and the etrailer fit guide. Where the only spec source is the Amazon listing, we say so. Retailer prices were checked in September 2026; Amazon prices move daily, so the button shows the live price.",
 "takeaways": [
  "**Rail type decides fit, not year.** Standard raised rails (XLE and up), Adventure/TRD Off-Road rails, and the LE's bare roof each need different crossbars.",
  "**Read the exclusions.** Most budget listings say \"not Adventure / TRD Off-Road\"; one also excludes the LE and Woodland. The ROKIOTOEX set is for the Adventure/TRD rails.",
  "**The roof limit is modest, and the bars count toward it.** We could not confirm a Toyota figure. RAV4Resource lists 176.4 lb for 2019–2024 and this site's vehicle data lists 165 lb, so read the owner's manual. A 260 lb bar rating doesn't change the roof's limit.",
  "**The LE needs a clamp kit.** etrailer prices Thule's naked-roof WingBar Evo for the RAV4 at $704.85.",
  "**2026 is a new generation.** Buy 2026-named bars for a 2026 RAV4.",
 ],
 "top_picks": [
  {"asin": "B081J9P2KY", "role": "Best overall (standard rails)", "why": "260 lb lockable bars with a title that lists every trim it excludes"},
  {"asin": "B07WGHX1K5", "role": "Best for Adventure / TRD Off-Road", "why": "Titled for the Adventure and TRD factory raised rails"},
  {"asin": "B08LG42HL8", "role": "Best value lockable", "why": "Lockable bars for 2019–2025 standard rails at a lower price"},
  {"asin": "B0CGRJFWDV", "role": "Budget lockable", "why": "VEVOR lockable bars with a 160 lb rating in the title"},
  {"asin": "B0GDYBR15P", "role": "Cheapest no-drill set", "why": "Basic aluminum bars titled 2019–2025 RAV4; confirm trim"},
 ],
 "fit_table": {
  "caption": "2019–2025 RAV4 roof types (the crossbar must match the rail, not the powertrain)",
  "head": ["Roof type", "Trims", "Crossbars on this page", "Notes"],
  "rows": [
   ["Standard raised rails", "XLE, XLE Premium, Limited, XSE (gas, Hybrid, Prime)", "Autekcomma, FLYCLE, VEVOR, generic aluminum", "Most common; titles exclude Adventure/TRD"],
   ["Adventure / TRD Off-Road raised rails", "Adventure (2019–2024), TRD Off-Road (2020–2024); the Autekcomma title also excludes the Woodland (Hybrid, from 2023)", "ROKIOTOEX", "Listed separately from standard rails; both trims discontinued for 2025 (Wikipedia)"],
   ["Flush rails", "Listed by etrailer for some 2021 RAV4s", "None; use a Thule/Yakima flush-rail kit", "Rails sit tight to the roof with no gap underneath"],
   ["Bare roof", "LE (per our vehicle data)", "None; use a clamp kit", "Thule WingBar Evo naked-roof kit $704.85 at etrailer"],
   ["6th-gen roof", "2026+ (new generation)", "None", "Buy 2026-named parts"],
  ],
 },
 "look_for": [
  {"h": "Three roof types, three kinds of bars",
   "body": "The RAV4 is the trickiest of the popular compact SUVs for crossbars because Toyota fitted different roofs by trim. Standard raised rails on the XLE and up are what most listings are built for. Listings treat the Adventure and TRD Off-Road rails as a separate fit, and the Autekcomma title also excludes the Woodland. Our vehicle data lists the LE with a bare roof. etrailer's fit guide also shows a flush-rail configuration for some 2021 RAV4s. Before you shop, look at your roof: a gap under the rail means raised rails; no gap means flush rails; no rail means a clamp kit."},
  {"h": "Load limit, including the bars",
   "body": "We could not confirm a roof load figure for the 5th-gen RAV4 from a Toyota document. RAV4Resource lists 176.4 lb (80 kg) for 2019–2024 models and points to the owner's manual. This site's vehicle data lists 165 lb, which we could not trace to Toyota. Your owner's manual is the authority. The limit covers everything above the rails while driving: crossbars, the mount or box, and the cargo. Crossbar listings quote their own ratings, from 160 lb on the VEVOR to 260 lb on the Autekcomma. Those numbers describe bar strength, not what the RAV4 can carry. A stronger bar flexes less; it doesn't lift the roof's limit."},
  {"h": "Crossbar spread and the liftgate",
   "body": "Clamp-on bars slide along the raised rail, so you choose the spread. Each box, tent or platform publishes a minimum and maximum spread, and a set of bars is only useful if the rails let you reach it. On the RAV4 the rear limit is set by the rail curving down and by the liftgate, which swings up toward the back of the roof. Set the rear bar forward enough that the open liftgate clears it and anything on it. Measure and mark the spread with tape so you can put the bars back in the same place."},
  {"h": "Noise and the flush-mount option",
   "body": "The Rack Shop says Yakima's teardrop JetStream bars cut wind noise better than its steel CoreBar, and the same rule holds for any brand: aero aluminum beats square or round steel. Most Amazon sets here are aluminum aero bars. If you want the quietest, cleanest look, flush-mount systems sit inside the rails rather than over them. etrailer lists the Yakima TimberLine FX for the RAV4 at $599.90. Long overhang and missing end caps are the usual sources of whistle."},
  {"h": "Tents, platforms and heavier loads",
   "body": "A driving limit of 165 lb (our vehicle data) or 176.4 lb (RAV4Resource), bars included, rules out many heavy rooftop tents and makes platform racks a careful calculation. etrailer lists Yakima's LockNLoad platform for the RAV4 at $913.80 to $1,017.90, but the platform's own weight eats into the roof limit before you add gear. If you want a tent, start with the tent's weight and the maker's approval for the RAV4, then choose bars. For most RAV4 owners, a cargo box, bikes or boats are the realistic roof loads."},
 ],
 "look_table": {
  "head": ["Feature", "Look for", "Avoid"],
  "rows": [
   ["Fitment", "Title naming the RAV4 years and your rail (standard or Adventure/TRD)", "Listings that don't say which trims they exclude"],
   ["Trim exclusions", "\"Not LE / Adventure / TRD Off-Road / Woodland\" matched to your badge", "Standard-rail bars on an Adventure or TRD Off-Road"],
   ["Load", "Bar rating stated, plus your load under the owner's manual roof figure, bars included", "Loading to a 260 lb bar rating"],
   ["Security", "Lock cores on the clamps", "Hex-key-only clamps if you park in public"],
   ["Profile", "Aero aluminum bars; flush-mount for the quietest", "Long square steel bars on a daily driver"],
   ["Year range", "2019–2025 (or the specific years you own)", "Assuming 2026 fit from a 2019–2025 listing"],
  ],
 },
 "types_table": {
  "caption": "Roof-rack options on the 2019–2025 RAV4",
  "head": ["Option", "Price guide", "Roof type", "Bar rating (per maker/listing)", "Noise", "Best for"],
  "rows": [
   ["Budget clamp-on aluminum bars", "About $60–$130", "Standard raised rails", "160–260 lb", "Low to medium", "Cargo bags, bikes, kayaks"],
   ["Adventure/TRD-specific bars", "About $100–$150", "Adventure-style rails", "See listing", "Low to medium", "Adventure and TRD Off-Road owners"],
   ["Thule SquareBar / WingBar Evo (raised rails)", "$444.90–$579.90 (etrailer)", "Standard raised rails", "Vehicle limit", "Low (WingBar)", "Name-brand fit guide and warranty"],
   ["Thule WingBar Evo (bare roof)", "$704.85 (etrailer)", "LE bare roof", "Vehicle limit", "Low", "LE owners"],
   ["Yakima LockNLoad platform", "$913.80–$1,017.90 (etrailer)", "Raised rails", "Vehicle limit", "Higher", "Flat platforms; watch the weight"],
  ],
 },
 "picks": [
  {"asin": "B081J9P2KY", "role": "Best overall (standard rails)", "price": "$90–$130",
   "pros": ["260 lb bar rating, the highest here", "Lockable", "Title spells out every trim it excludes: LE, Adventure, TRD Off-Road, Woodland", "Covers 2019–2025, the whole XA50 run", "Aluminum clamp-on bars, no drilling"],
   "cons": ["Won't fit the Adventure, TRD Off-Road, Woodland or LE", "Specs and warranty come from the listing only", "260 lb is far above the car's own limit, so the extra rating mostly means stiffness"],
   "body": "Autekcomma's set is the best starting point for most RAV4 owners because its title does the fit-checking for you. It's listed for 2019–2025 RAV4s with standard raised rails and names every trim it doesn't fit: the bare-roof LE, the Adventure, the TRD Off-Road and the Woodland. If your RAV4 is an XLE, XLE Premium, XSE or Limited, gas, Hybrid or Prime, this is the rail it's built for. It is lockable, and at 260 lb it has the highest bar rating on this page.\n\nThat rating needs context. Our vehicle data lists the RAV4's roof at 165 lb while driving, including the bars, and RAV4Resource lists 176.4 lb. We could not confirm either from Toyota. A 260 lb bar doesn't raise the roof's limit; it gives you a stiffer bar that flexes less under a cargo box or a pair of kayaks. As with every Amazon set here, the specs and warranty come from the listing, so read those terms before ordering. Set the spread for your accessory, check liftgate clearance, and re-tighten after the first drive.",
   "who": "Owners of XLE-and-up RAV4s with standard raised rails who want lockable, stiff bars.",
   "specs": [["Type", "Lockable clamp-on aluminum crossbars"], ["Fits", "2019–2025 RAV4 with standard raised rails"], ["Not for", "LE, Adventure, TRD Off-Road, Woodland"], ["Bar rating", "260 lb (per title)"], ["Vehicle limit", "See owner's manual (165 lb in our data, not confirmed)"], ["Lock", "Yes"], ["Drilling", "None"]]},
  {"asin": "B07WGHX1K5", "role": "Best for Adventure / TRD Off-Road", "price": "$100–$150",
   "pros": ["Titled for the Adventure and TRD Off-Road factory raised rails", "The only set here for those trims", "Clamp-on, no drilling", "Covers 2019–2024, the full Adventure run", "Lets Adventure owners use standard crossbar accessories"],
   "cons": ["Not for standard rails", "Woodland isn't named in the title; confirm with the seller", "Load rating and locks not in the title"],
   "body": "The Adventure and TRD Off-Road are the RAV4s most likely to carry gear on the roof, and they're the ones most budget crossbars skip. ROKIOTOEX's set is titled for the 2019–2024 RAV4 Adventure and TRD factory raised rails, which covers the full run of both trims: Wikipedia's RAV4 page says the TRD Off-Road was added for 2020 and both trims were discontinued for 2025. Because standard-rail listings exclude these trims, a set titled for their rails is the safer choice over trying a standard-rail bar and hoping the clamp closes.\n\nThe title doesn't give a bar rating or mention locks, so check both on the listing. The Adventure's 3,500 lb tow rating in our data doesn't change the roof limit either; use the roof figure in your owner's manual (our vehicle data lists 165 lb, not confirmed from Toyota). Woodland owners should confirm fit with the seller: the Autekcomma title excludes the Woodland along with the Adventure and TRD Off-Road, but this title doesn't name it. Toyota's 2024 release lists standard cross bars on the Woodland Edition, so check the roof before buying any.",
   "who": "Adventure and TRD Off-Road owners who need bars made for their rail.",
   "specs": [["Type", "Clamp-on crossbars"], ["Fits", "2019–2024 RAV4 Adventure / TRD Off-Road factory rails"], ["Not for", "Standard raised rails, LE"], ["Woodland", "Confirm with seller"], ["Bar rating", "See listing"], ["Vehicle limit", "See owner's manual (165 lb in our data, not confirmed)"], ["Drilling", "None"]]},
  {"asin": "B08LG42HL8", "role": "Best value lockable", "price": "$80–$120",
   "pros": ["Lockable", "Titled for 2019–2025 RAV4", "Excludes Adventure and TRD Off-Road in the title", "Lower price band than the Autekcomma", "Clamp-on, no drilling"],
   "cons": ["Title doesn't mention the LE or Woodland; check your roof", "Load rating not in the title", "Specs and warranty from the listing only"],
   "body": "FLYCLE's lockable set covers the same standard raised rails as the Autekcomma, usually for a little less. The title names the 2019–2025 RAV4 and excludes the Adventure and TRD Off-Road, so XLE, XLE Premium, XSE and Limited owners are covered. The lock cores mean a thief can't take the bars, and whatever is clamped to them, off with a hex key, which matters for bikes left on the roof at a trailhead.\n\nThe title is less thorough than the Autekcomma's. It doesn't mention the bare-roof LE, which can't take any raised-rail bar, or the Woodland, which the Autekcomma title excludes. If you have either, choose a different set. It also doesn't state a bar rating, so read the listing, and keep your total roof load, including about the weight of the bars themselves, under the RAV4's limit.",
   "who": "Standard-rail RAV4 owners who want locks at a slightly lower price.",
   "specs": [["Type", "Lockable clamp-on crossbars"], ["Fits", "2019–2025 RAV4 standard raised rails"], ["Not for", "Adventure, TRD Off-Road (and LE, which has no rails)"], ["Lock", "Yes"], ["Bar rating", "See listing"], ["Vehicle limit", "See owner's manual (165 lb in our data, not confirmed)"], ["Drilling", "None"]]},
  {"asin": "B0CGRJFWDV", "role": "Budget lockable", "price": "$60–$90",
   "pros": ["Lowest price band on this page", "Lockable", "160 lb bar rating stated in the title", "Clamp-on, no drilling", "Excludes Adventure and TRD Off-Road in the title"],
   "cons": ["Title covers 2020–2023 only; confirm 2019, 2024 and 2025 with the seller", "Lowest bar rating here", "Specs and warranty from the listing only"],
   "body": "VEVOR's set is the cheapest lockable option for standard-rail RAV4s. The title gives a 160 lb bar rating. That is below the 176.4 lb RAV4Resource lists for the roof, so on this set the bar may be the lower limit. Load to whichever is lower: the bar rating or the roof figure in your owner's manual. It's lockable and excludes the Adventure and TRD Off-Road, so XLE-and-up owners with standard rails are the audience.\n\nThe catch is the year range: the title covers 2020–2023. The standard rail didn't change across the generation as far as the other listings here indicate, but that's an inference, so 2019, 2024 and 2025 owners should confirm fit with the seller before ordering. For a cargo bag, a bike tray or a pair of skis, it is enough bar. For a loaded cargo box on long highway trips, the stiffer Autekcomma is worth the small premium.",
   "who": "Budget buyers with a 2020–2023 standard-rail RAV4 who want locks.",
   "specs": [["Type", "Lockable clamp-on crossbars"], ["Fits", "2020–2023 RAV4 standard raised rails (per title)"], ["Not for", "Adventure, TRD Off-Road"], ["Bar rating", "160 lb (per title)"], ["Lock", "Yes"], ["Other years", "Confirm with seller"], ["Drilling", "None"]]},
  {"asin": "B0GDYBR15P", "role": "Cheapest no-drill set", "price": "$70–$110",
   "pros": ["Titled for 2019–2025 RAV4", "Aluminum", "No drilling", "Covers the full generation", "Simple clamp-on design"],
   "cons": ["Title doesn't name the rail type or trims; confirm with the seller", "No locks mentioned", "No bar rating in the title"],
   "body": "This unbranded aluminum set is titled for the 2019–2025 RAV4 and described as no-drill, which covers the full generation. It's the most basic set here: no locks mentioned, no bar rating in the title, and no brand behind it. That makes it a set for light, occasional loads such as a soft cargo bag or a pair of skis in winter, where the price matters more than the rating.\n\nThe title doesn't say which rail it's built for. Because other listings exclude the Adventure and TRD Off-Road, and the LE has no rails at all, confirm your trim with the seller before ordering. If your car sits at trailheads or on the street, spend the extra on one of the lockable sets. Whatever you carry, keep the total, bars included, under the roof limit in your owner's manual. Our vehicle data lists 165 lb, which we could not confirm from Toyota.",
   "who": "Owners who need bars a few times a year and want the lowest-cost RAV4-titled set.",
   "specs": [["Type", "Clamp-on aluminum crossbars"], ["Fits", "2019–2025 RAV4 (rail type: confirm)"], ["Lock", "Not listed in title"], ["Bar rating", "Not listed in title"], ["Vehicle limit", "See owner's manual (165 lb in our data, not confirmed)"], ["Drilling", "None"]]},
 ],
 "install": [
  "Identify your roof: raised rails with a gap underneath (XLE and up), the Adventure/TRD-style rail, flush rails, or the LE's bare roof.",
  "Clean the rails where the clamps will sit so the pads grip on paint and aluminum, not road grit.",
  "Set both bars loosely on the rails and space them to your accessory's range, keeping the rear bar clear of the liftgate's swing.",
  "Center the bars so the overhang is equal on each side, then tighten the clamps evenly, alternating sides.",
  "Open the liftgate fully to check clearance, and keep the sunroof closed with the rack installed, as etrailer advises for Thule systems.",
  "Lock the clamps, drive a short loop, re-tighten, and check again before long trips.",
 ],
 "avoid": [
  {"h": "Standard-rail bars on an Adventure or TRD Off-Road", "body": "Three standard-rail titles here exclude those trims. Buy the Adventure/TRD set or a fit-guide kit."},
  {"h": "Any raised-rail bar on an LE", "body": "The LE's bare roof has nothing to clamp to. It needs a door-jamb clamp kit such as Thule's naked-roof WingBar Evo."},
  {"h": "Loading to the bar rating", "body": "A 260 lb bar rating is above both roof figures we found (165 lb in our vehicle data, 176.4 lb on RAV4Resource). The roof's limit applies, and the bars count toward it."},
  {"h": "2019–2025 bars on a 2026 RAV4", "body": "The 2026 is a new generation. Buy bars that name it and confirm the rail."},
 ],
 "verdict": {
  "thesis": "Match the rail: the lockable 260 lb Autekcomma for standard raised rails, the ROKIOTOEX for the Adventure and TRD Off-Road, and a Thule clamp kit for the bare-roof LE.",
  "body": "The best RAV4 crossbar is the one sold for your rail. For XLE-and-up owners, the Autekcomma's clear exclusions and 260 lb rating make it the default, with the FLYCLE and VEVOR sets as cheaper lockable options. Adventure and TRD Off-Road owners should buy the ROKIOTOEX set built for their rail. The LE needs a clamp system, and etrailer's Thule naked-roof kit is the straightforward route. Whatever you choose, the roof limit in your owner's manual includes the bars.\n\nWith bars on, a cargo box is the natural next step, and our RAV4 cargo box guide lists Yakima boxes by length and spread. If the roof is full, a trailer hitch with a bike carrier takes the bikes off it. The vehicle hub lists every fit-checked accessory for the 5th-gen RAV4.",
 },
 "sources": [
  ["2021 RAV4 roof rack systems by roof type (etrailer)", "https://www.etrailer.com/roof-2021_Toyota_RAV4.htm"],
  ["Toyota RAV4 XA50 trims and generation change (Wikipedia)", "https://en.wikipedia.org/wiki/Toyota_RAV4_(XA50)"],
  ["Yakima crossbar kit notes on teardrop vs steel bars (The Rack Shop)", "https://therackshop.com/2020-2025-subaru-outback-w-raised-rails-yakima-crossbar-complete-roof-rack-1/"],
  ["Autekcomma 260 lb Lockable Cross Bars listing title (Amazon)", "https://www.amazon.com/dp/B081J9P2KY"],
  ["ROKIOTOEX Adventure / TRD cross bars listing title (Amazon)", "https://www.amazon.com/dp/B07WGHX1K5"],
  ["VEVOR 160 lb Lockable Cross Bars listing title (Amazon)", "https://www.amazon.com/dp/B0CGRJFWDV"],
  ["Crossbars, wind noise and fuel economy (Autoblog)", "https://www.autoblog.com/2020/10/15/subaru-outback-roof-rack-driveway-test/"],
  ["RAV4 roof rack weight limit by model year (RAV4Resource)", "https://rav4resource.com/toyota-rav4-roof-rack-weight-limit/"],
  ["2024 Toyota RAV4 release: grades, Woodland Edition roof rails and cross bars (Toyota Newsroom)", "https://pressroom.toyota.com/?generate_pdf=87387"],
  ["Toyota Adventure cross bars PT278-42191: Adventure fit, no load figure printed (North Park Toyota parts catalog)", "https://parts.northparktoyota.com/oem-parts/toyota-roof-rack-cross-bars-pt27842191"],
 ],
}

# Product list for this page (carried over from fitments_v2; all five kept). (asin, name, brand, band, cond, note)
FITS = [
 ("B081J9P2KY","Autekcomma 260 lb Lockable Cross Bars, 2019-2025 RAV4 (not LE / Adventure / TRD Off-Road / Woodland)","Autekcomma","$90–$130",{"roof_type":"raised-rails"},"Standard raised rails only."),
 ("B07WGHX1K5","ROKIOTOEX Cross Bars, 2019-2024 RAV4 Adventure / TRD factory raised rails","ROKIOTOEX","$100–$150",{"roof_type":"raised-rails","trim":"Adventure/TRD Off-Road"},"Adventure / TRD rails only; confirm Woodland."),
 ("B08LG42HL8","FLYCLE Lockable Cross Bars, 2019-2025 RAV4 (not Adventure / TRD Off-Road)","FLYCLE","$80–$120",{"roof_type":"raised-rails"},"Standard rails only."),
 ("B0CGRJFWDV","VEVOR 160 lb Lockable Cross Bars, 2020-2023 RAV4 (not Adventure / TRD Off-Road)","VEVOR","$60–$90",{"roof_type":"raised-rails"},"Listed 2020-2023; confirm other years."),
 ("B0GDYBR15P","Aluminum Cross Bars, 2019-2025 RAV4, no-drill","Generic","$70–$110",{"roof_type":"raised-rails"},"Confirm trim on listing."),
]
