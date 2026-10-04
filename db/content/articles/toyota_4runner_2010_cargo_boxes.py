"""Long-form article — Best Rooftop Cargo Boxes for 2010–2024 Toyota 4Runner (5th gen, N280).
Mirrors the approved RAV4/Telluride cargo-box pages. No invented hands-on testing: box specs come from Thule
(via etrailer), Rhino-Rack, INNO (via etrailer), Yakima and SportRack pages, and vehicle facts from
db/migrations/003_vehicles.sql, the 5th-gen 4Runner roof-rack article and the references in SOURCES
(checked 2026-09-27). Boxes are universal; the 4Runner-specific part is the 120 lb roof figure, factory
crossbars vs baskets and platforms, crossbar spread and hatch clearance.
Source fixes 2026-10-04: the hitch FAQ now follows Toyota's 2017, 2019 and 2020 releases (receiver and wiring harness standard on all grades, 5,000 lb towing, 500 lb tongue weight, no hitch class named) in place of "Class III receiver on tow-package trucks"; the 120 lb roof figure is attributed to a reader comment on Trail4Runner citing a 2016 SR5 owner's manual and marked as not confirmed from a Toyota document; etrailer's 24–42 in spread is tied to the Yakima SkyBox 12 it was given for; TRD Pro and special-edition roof wording follows Toyota's 2019, 2020 and 2021 releases, which are added to sources with the 2017 release.
Text fixes 2026-10-04 (round 2): one search found no Toyota owner's manual wording for the roof load, so the TITLE, META, dek and verdict no longer state 120 lb as the roof's limit (TITLE now says "a Low Roof Limit", META "roof load math to check in your manual"); the 120 lb math stays and is labeled as the reader-cited figure; a Toyota dealer parts page for the Genuine Toyota cross bar kit PT278-89170 (132 lb evenly distributed across both bars, see owner's manual) is added as a bar rating, not a roof limit, and added to sources; "more gear than the roof can legally carry" reworded.
"""

KEY = ("toyota", "4runner", "2010-2024", "cargo-boxes")

TITLE = "Best Rooftop Cargo Boxes for 2010–2024 Toyota 4Runner: 6 Light Boxes for a Low Roof Limit"
META = ("Six Thule, Rhino-Rack, INNO, Yakima and SportRack cargo boxes for the 5th-gen 4Runner: roof load math to check "
        "in your manual, factory crossbars and hatch gap.")

FAQ = [
 ("What is the roof weight limit for a 2010–2024 4Runner with a cargo box?",
  "A reader comment on Trail4Runner cites 120 lb from a 2016 SR5 owner's manual, and that is the figure in our fitment data. We could not confirm it from a Toyota document, and the comment doesn't say whether it is the limit for the factory rails or for the roof itself. A Toyota dealer's parts page for the Genuine Toyota roof cross bar kit for the 4Runner (PT278-89170) says the bars support a maximum of 132 lb with the weight spread evenly across both bars, and tells buyers to see the owner's manual for weight limits. That page lists no model years, and 132 lb is a rating for the bars, not for the roof. This guide does its math with the lower 120 lb figure and treats it as a driving (dynamic) limit that covers everything above the roof: crossbars or platform, the box and the gear inside. A 36 lb Thule Pulse L leaves about 84 lb before you count the bars, so plan for roughly 60 to 75 lb of gear in practice. Check your own year's manual, because figures can differ."),
 ("Can I mount a cargo box on the 4Runner's factory crossbars?",
  "Usually, yes. Most SR5, TRD Off-Road, TRD Sport, Limited and Nightshade trucks came with raised rails and factory crossbars. In an etrailer answer about a 2015 4Runner Limited, the expert says the Yakima SkyBox 12 fits the factory bars as long as they are no larger than 3-1/2 in wide by 1-11/16 in tall and are spread between 24 and 42 in. Those figures belong to the SkyBox 12, which is not a pick here, so check your chosen box's own clamp size and spread range the same way."),
 ("How far forward does a box need to sit to clear the 4Runner hatch?",
  "That depends on the box. etrailer's expert says the Yakima SkyBox 12 needs at least 57 in between the center of the front crossbar and the line where the roof meets the rear hatch on a 4Runner. Thule publishes its own front-clearance figures, such as more than 50 5/8 in for the Force 3 L. Measure your truck from the front bar to the hatch seam and compare before you buy."),
 ("Will a roof box fit a TRD Pro with the factory basket?",
  "Not directly in most cases. Toyota's 2019, 2020 and 2021 releases put a TRD roof rack on the TRD Pro only, and the 2021 release lists Yakima cargo baskets on the Trail and Venture Special Editions. Box clamps are designed to wrap around crossbars of a set size, not basket tubing. Either fit crossbars or a platform that uses the factory mounting points, or ask the box maker whether its clamps are approved for your basket before loading it."),
 ("Can I put a cargo box on a Front Runner or Rough Country platform?",
  "Yes, as long as the box's clamps can wrap the platform slats or crossbars, but the weight math gets tight. A Front Runner Slimline II 3/4 kit installs at about 59 lb. Add a 36 lb Pulse L and you have used about 95 lb of the reader-cited 120 lb figure before any gear goes in. On a platform, a light box and soft gear are the only way to stay inside the manual's figure."),
 ("What size cargo box is best for a 5th-gen 4Runner?",
  "Size by weight, not volume. The 120 lb roof figure this guide works from is low for a truck this size, so a light 14 to 16 cu ft box is the sweet spot. The Thule Pulse L gives 16 cu ft at 36 lb, the Rhino-Rack MasterFit 440L gives 15.5 cu ft at 38.6 lb, and the Pulse M gives 14 cu ft at 34 lb. Big 18 to 21 cu ft boxes hold far more gear than that figure allows."),
 ("Do 2010–2024 4Runner crossbars and boxes carry over to the 2025–2026 4Runner?",
  "The box does; the bars don't. Boxes clamp to crossbars, so any box here moves to a new truck. The 2025–2026 4Runner has a new roof and rail geometry, and makers sell separate rack parts for it, so crossbars and platforms from the 2010–2024 4Runner won't fit. Our 2025–2026 4Runner cargo box guide covers the new truck's figures."),
 ("Will a cargo box fit in my garage on a 4Runner?",
  "Measure first. The 4Runner is already a tall SUV, and factory rails, a platform or a basket all lift the box higher. The boxes here add 11 in (INNO Wedge 660), 15 in (SkyBox 16), about 16 to 17 in (Pulse, DeepSpace 10, MasterFit 440L) or 19 in (SportRack Vista XL) on top of the bars. Measure the truck with bars fitted, add the box height and compare with the door opening."),
 ("Does a roof box block the 4Runner's roll-down rear window?",
  "No. The power rear window drops into the tailgate, so it isn't affected by the box. The concern is the hatch itself when you swing it open, because the top of the gate moves up and back toward the rear of the roof. Keep the box forward, open the gate slowly the first time, and check the gap at the box's tail."),
 ("Is a roof box or a hitch cargo carrier better on a 5th-gen 4Runner?",
  "For heavy gear, the hitch. Toyota's 2017, 2019 and 2020 releases list an integrated tow-hitch receiver and wiring harness as standard on all grades, with a 5,000 lb maximum tow rating and a 500 lb maximum tongue weight, so a hitch carrier can take coolers, fuel and recovery gear that would blow through the 120 lb roof figure used in this guide. Look under the rear bumper to confirm the receiver is there, and check the carrier's own rating and your owner's manual before loading it. A roof box is better for light, bulky, dry-storage items like sleeping bags and jackets. Many owners use both: soft gear up top, heavy items on the hitch."),
]

ARTICLE = {
 "dek": "Six rooftop boxes from Thule, Rhino-Rack, INNO, Yakima and SportRack, ranked for the 5th-generation 4Runner's real constraint: a low roof load figure that has to cover the bars, the box and the gear. We use 120 lb, which a reader cites from a 2016 SR5 owner's manual and we could not confirm with Toyota. For each one we list volume, length, box weight, load rating and crossbar spread, and what those numbers mean for factory crossbars, TRD Pro baskets, platform racks and the rear hatch.",
 "author": "jake-morrison",
 "reviewed": "2026-10-04",
 "method": "We did not mount these boxes ourselves. We ranked them on the makers' published specs (Thule, Rhino-Rack, INNO, Yakima and SportRack: volume, exterior dimensions, box weight, load rating, crossbar spread, opening, warranty), on etrailer's listings and its expert answer about 4Runner factory crossbars, and on how those numbers fit the 120 lb roof figure that a reader comment on Trail4Runner cites from a 2016 SR5 owner's manual. Rack weights and roof types come from our 5th-gen 4Runner roof rack guide. Prices were checked on maker and retailer pages in September 2026. Amazon prices move daily, so the button shows the live price.",
 "takeaways": [
  "**Weight is the whole story.** A Trail4Runner reader comment cites 120 lb from a 2016 SR5 manual; confirm yours. Bars, box and gear all count, so a 36–39 lb box beats a 50–57 lb one on this truck.",
  "**Factory crossbars usually work.** etrailer says the Yakima SkyBox 12 fits 4Runner factory bars no larger than 3-1/2 × 1-11/16 in, spread 24–42 in. Check each box's own spread range.",
  "**Baskets and platforms change the math.** TRD Pro trucks with the TRD roof rack (new for 2019) have a rack that box clamps aren't made for, and a 59 lb 3/4 platform plus a box leaves little of the 120 lb for gear.",
  "**Measure front bar to hatch seam.** etrailer gives 57 in for the SkyBox 12; Thule quotes more than 50 5/8 in for the Force 3 L. Shorter boxes (63–76 in) leave the most margin.",
  "**The box carries over; the bars don't.** Boxes move to the 2025–2026 4Runner, but 5th-gen crossbars and platforms do not fit the new roof.",
 ],
 "top_picks": [
  {"asin": "B009NN4ZDS", "role": "Best overall", "why": "Thule Pulse L: 16 cu ft at 36 lb, 110 lb rating, 76 in long, 23-5/8 to 34-3/8 in spread"},
  {"asin": "B07B4P7WYX", "role": "Best dual-side", "why": "Rhino-Rack MasterFit 440L: 15.5 cu ft at 38.6 lb, opens both sides, 5-year warranty"},
  {"asin": "B06VX9L59C", "role": "Lowest profile", "why": "INNO Wedge 660: 11 in tall, 24–39 in spread, dual-side; best for garages"},
  {"asin": "B09HC2LWX8", "role": "Lightest", "why": "Yakima DeepSpace 10: 30.2 lb, 60 in long; needs 32–46 in spread"},
  {"asin": "B00BCLL8C0", "role": "Best budget", "why": "SportRack Vista XL: 18 cu ft in 63 in for $449.95; confirm its weight"},
 ],
 "fit_table": {
  "caption": "2010–2024 4Runner roof setups (what the box mounts to; weight notes use the reader-cited 120 lb figure)",
  "head": ["Roof as delivered", "Typical trucks", "Box mounting", "Weight notes"],
  "rows": [
   ["Raised rails with factory crossbars", "Most SR5, TRD Off-Road, TRD Sport, Limited, Nightshade", "Clamp directly to the factory bars; etrailer: bars up to 3-1/2 × 1-11/16 in, 24–42 in spread for the Yakima SkyBox 12", "Lightest setup; most of the 120 lb goes to box and gear"],
   ["Raised rails, no crossbars", "Bars removed or lost", "Add clamp-on crossbars listed for 2010–2024 raised rails", "Count the bars' weight against 120 lb"],
   ["Factory basket / cargo rack", "TRD Pro (TRD roof rack, new for 2019 per Toyota); Trail and Venture Special Editions (Yakima basket)", "Box clamps aren't made for basket tubing; fit bars or a platform, or ask the box maker", "Basket weight already counts against the limit"],
   ["Aftermarket platform", "Front Runner, Rough Country, Rhino-Rack", "Clamp to slats or crossbars if the box's clamp size allows", "A 59 lb 3/4 platform plus a 36 lb box uses about 95 lb"],
  ],
 },
 "look_for": [
  {"h": "The roof load figure comes first",
   "body": "The 5th-gen 4Runner looks like a truck that could carry anything on its roof, but the roof figure we could find is modest. A reader comment on Trail4Runner cites 120 lb from a 2016 SR5 owner's manual, and that is the value in our fitment data. We could not confirm it from a Toyota document. A Toyota dealer's parts page for the Genuine Toyota roof cross bar kit for the 4Runner (PT278-89170) says the bars support a maximum of 132 lb with the weight spread evenly across both bars, and tells buyers to see the owner's manual for weight limits. That page lists no model years, and 132 lb is a rating for the bars, not for the roof. We use the lower 120 lb figure and treat it as a driving limit that includes the crossbars, the box and everything inside. That turns box weight into the most important spec on this page. The Thule Pulse M (34 lb), Pulse L (36 lb) and Rhino-Rack MasterFit 440L (38.6 lb) leave roughly 80 lb before bars, while a 51 to 57 lb premium box leaves closer to 65. Check your own year's manual and plan around the lower figure."},
  {"h": "Factory crossbars, baskets and platforms",
   "body": "Look at the roof before you shop. Most trucks have raised rails with factory crossbars, and an etrailer expert answer for a 2015 4Runner Limited says the Yakima SkyBox 12 fits those bars if they are no larger than 3-1/2 in wide and 1-11/16 in tall and are spread 24 to 42 in apart. TRD Pro trucks with the TRD roof rack (new for 2019) and the Trail and Venture Special Editions carry a factory rack or basket, and box clamps are made for crossbars, not basket tubing. On a Front Runner or Rough Country platform, the box can clamp to the slats or bars if its clamp opening fits, but the platform's weight eats into the 120 lb before the box goes on."},
  {"h": "Crossbar spread vs the box's mounting range",
   "body": "Every box lists a minimum and maximum distance between the bars. Thule gives 23-5/8 to 34-3/8 in for the Pulse L, Rhino-Rack gives 620 to 930 mm (about 24.4 to 36.6 in) for the MasterFit 440L, INNO gives 24 to 39 in for the Wedge 660, and Yakima gives 24 to 34.5 in for the SkyBox 16 and 32 to 46 in for the DeepSpace 10. The SportRack Vista XL mounts only at 25-7/8, 27-7/8 or 29-7/8 in, per etrailer. Measure your factory bars center to center and confirm that the box's range covers it, sliding the bars if the rails allow."},
  {"h": "Hatch clearance on a long roof",
   "body": "The 4Runner's rear hatch swings up and back, and a long box mounted too far back can sit in its path. etrailer's expert says the SkyBox 12 needs at least 57 in between the center of the front crossbar and the line where the roof meets the hatch on a 4Runner. Thule publishes a similar front-clearance figure for its boxes, such as more than 50 5/8 in for the Force 3 L. The boxes here run from 60 in (DeepSpace 10) and 63 in (Vista XL) to 76 in (Pulse L, MasterFit 440L), 80 in (Wedge 660) and 81 in (SkyBox 16). Mount forward, then open the hatch slowly the first time."},
  {"h": "Height and the garage door",
   "body": "The 4Runner is already tall, and factory rails, platforms and baskets lift the box further. Box height ranges from 11 in on the INNO Wedge 660 to 19 in on the SportRack Vista XL, with the Thule Pulse L at 16-1/2 in, the MasterFit at 17 in and the SkyBox 16 at 15 in. If you park in a home garage or use parking structures, measure the truck with its bars fitted, add the box height and compare with the opening. The 8 in between the Wedge and the Vista XL can decide whether the box stays on between trips or has to come off."},
 ],
 "look_table": {
  "head": ["Feature", "Look for", "Avoid"],
  "rows": [
   ["Box weight", "Under 40 lb (Pulse M 34 lb, Pulse L 36 lb, MasterFit 38.6 lb)", "50 lb+ boxes that leave little of the reader-cited 120 lb roof figure for gear"],
   ["Load rating", "A published figure (110 lb Pulse and Wedge, 165 lb MasterFit, 100 lb DeepSpace)", "Using the box rating as the roof limit; the lower figure wins"],
   ["Crossbar spread", "A range that covers your factory bars (most start at 24 in or less)", "32 in-minimum boxes without measuring your bars"],
   ["Length", "76 in or less for the most hatch margin", "Long ski boxes without measuring front bar to hatch seam"],
   ["Height", "11–15 in if you park in a garage", "A 19 in box on a platform without measuring"],
   ["Opening", "Dual-side for curb loading on a tall truck", "Single-side boxes if you park on busy streets"],
  ],
 },
 "types_table": {
  "caption": "Box sizing for the 5th-gen 4Runner (makers' published specs; Thule, INNO and SportRack figures per etrailer)",
  "head": ["Box", "Volume", "L × W × H", "Box weight", "Load rating", "Crossbar spread"],
  "rows": [
   ["Thule Pulse L", "16 cu ft", "76 × 33 × 16.5 in", "36 lb", "110 lb", "23-5/8 to 34-3/8 in"],
   ["Thule Pulse M", "14 cu ft", "67 × 35 × 16 in", "34 lb", "110 lb", "23-5/8 to 33-3/8 in"],
   ["Rhino-Rack MasterFit 440L", "15.5 cu ft", "76 × 32 × 17 in", "38.6 lb", "75 kg (165 lb)", "620–930 mm (about 24.4–36.6 in)"],
   ["INNO Wedge 660", "11 cu ft", "80 × 33 × 11 in", "42 lb", "110 lb", "24–39 in"],
   ["Yakima DeepSpace 10", "10 cu ft", "60 × 23 × 16 in", "30.2 lb", "100 lb", "32–46 in"],
   ["Yakima SkyBox 16 Carbonite", "16 cu ft", "81 × 36 × 15 in", "47 lb", "Not published", "24–34.5 in"],
   ["SportRack Vista XL", "18 cu ft", "63 × 38 × 19 in", "Not published", "Not published", "Fixed at 25-7/8, 27-7/8 or 29-7/8 in"],
  ],
 },
 "picks": [
  {"asin": "B009NN4ZDS", "role": "Best overall", "price": "$786.47 at etrailer (sale)",
   "pros": ["16 cu ft at 36 lb, the best volume-to-weight ratio here", "Published 110 lb load rating", "23-5/8 to 34-3/8 in spread suits most factory bars", "76 in long, leaving hatch margin", "Limited lifetime warranty and Thule One-Key lock"],
   "cons": ["Opens from the passenger side only", "Priced near premium dual-side boxes", "16-1/2 in tall, so measure the garage"],
   "body": "On a truck with a roof figure as low as the reader-cited 120 lb, the Thule Pulse L makes the most of every pound. etrailer lists it at 16 cu ft with exterior dimensions of 76 x 33 x 16-1/2 in, a box weight of 36 lb and a maximum load of 110 lb. That is a full-size box for about 11 lb less than a Yakima SkyBox 16 and about 21 lb less than a CBX 16, and those pounds go straight to gear on a 4Runner. Its 23-5/8 to 34-3/8 in crossbar spread and clamps that take bars up to 3-5/16 x 1-1/2 in suit round, square, aero and factory bars. It locks with Thule's SecureLock and One-Key cylinder, carries a limited lifetime warranty, and etrailer had it at $786.47 on sale.\n\nOn the 4Runner, using that 120 lb figure, the numbers work out like this: 120 lb minus a 36 lb box leaves 84 lb, and the factory crossbars come off that too, so plan on roughly 60 to 75 lb of gear. That suits sleeping bags, jackets and duffels for a family weekend. The 76 in length is short enough to sit forward of the hatch on most setups, but measure front bar to hatch seam. The main trade-off is access: the lid opens from the passenger side only, so on a tall truck parked on a busy street you load from the curb side and nowhere else.",
   "who": "5th-gen owners who want a full 16 cu ft while keeping the most of the 120 lb roof figure for gear.",
   "specs": [["Volume", "16 cu ft"], ["Exterior", "76 × 33 × 16.5 in"], ["Box weight", "36 lb"], ["Max load", "110 lb"], ["Crossbar spread", "23-5/8 to 34-3/8 in"], ["Max bar size", "3-5/16 × 1-1/2 in"], ["Opening", "Passenger side"], ["Warranty", "Limited lifetime"]]},
  {"asin": "B07B4P7WYX", "role": "Best dual-side", "price": "Rhino-Rack doesn't list a price; check the listing",
   "pros": ["15.5 cu ft at 38.6 lb", "Dual-side opening with a key lock and three locking points", "75 kg (165 lb) load rating, above the roof figure", "620–930 mm spread covers most factory bars", "Fits Rhino-Rack Heavy Duty bars with the RUBK-MF kit"],
   "cons": ["5-year warranty, shorter than Thule's and Yakima's lifetime terms", "Rhino-Rack's page doesn't list a price", "17 in tall"],
   "body": "The Rhino-Rack MasterFit 440L is the light box that opens from both sides. Rhino-Rack lists it at 440 L (15.5 cu ft), 76 x 32 x 17 in outside, a 38.6 lb box weight and a 75 kg (165 lb) maximum load. It opens from either side with a key lock and three locking points, and it needs a crossbar spacing of 620 to 930 mm, about 24.4 to 36.6 in. Rhino-Rack lists it as compatible with its Vortex and Euro bars, Thule square and aero bars, Whispbar and others, and with its Heavy Duty bars using the RUBK-MF fitting kit. It carries a 5-year warranty.\n\nFor the 4Runner, the MasterFit has two things going for it. First, 38.6 lb is only 2.6 lb more than the Pulse L, so it leaves nearly the same margin under the 120 lb roof figure. Second, dual-side opening matters on a tall truck: you can reach in from whichever side faces the curb. It also makes sense if you already run a Rhino-Rack backbone or bars. Its 165 lb rating is higher than the roof can use, so the roof figure is the one that counts. Rhino-Rack's page doesn't list a price, so compare on the listing.",
   "who": "Owners who want a light, 15.5 cu ft box that loads from either side, especially on Rhino-Rack bars.",
   "specs": [["Volume", "440 L / 15.5 cu ft"], ["Exterior", "76 × 32 × 17 in"], ["Box weight", "38.6 lb"], ["Max load", "75 kg (165 lb)"], ["Crossbar spacing", "620–930 mm (about 24.4–36.6 in)"], ["Opening", "Dual-side, key lock, 3 locking points"], ["Warranty", "5 years"]]},
  {"asin": "B06VX9L59C", "role": "Lowest profile", "price": "$917.61 at etrailer (sale)",
   "pros": ["Only 11 in tall, the lowest box here", "24–39 in spread, the widest range here", "Dual-side opening with push buttons", "110 lb load rating", "Limited lifetime warranty"],
   "cons": ["11 cu ft for about $918", "42 lb, heavier than the Pulse and MasterFit", "80 in long; measure the hatch gap"],
   "body": "If your 4Runner has to fit under a garage door or into a parking structure with the box on, the INNO Wedge 660 is the answer. etrailer lists it at 80 x 33 x 11 in outside, the lowest box on this page by 4 in, with 11 cu ft inside, a 42 lb box weight and a 110 lb weight capacity. The lid opens from both sides with push buttons, and the 24 to 39 in crossbar spread is the widest range here, so it suits nearly any factory bar position. It takes 6 to 8 pairs of skis up to 182 cm. etrailer had it at $917.61 on sale, and it carries a limited lifetime warranty.\n\nThe trade-off is volume per pound and per dollar. At 42 lb, it leaves about 78 lb of the 120 lb figure before the bars, a little less than the Thule and Rhino-Rack boxes, and 11 cu ft is modest for the money. The 80 in length also needs a check against the hatch, so measure from the center of the front bar to the hatch seam. Choose it when height matters more than capacity, such as on a truck already lifted by a platform.",
   "who": "Owners who park in a garage or use a platform and need the lowest box, even at a higher price per cubic foot.",
   "specs": [["Volume", "11 cu ft"], ["Exterior", "80 × 33 × 11 in"], ["Box weight", "42 lb"], ["Max load", "110 lb"], ["Crossbar spread", "24–39 in"], ["Opening", "Dual-side"], ["Ski length", "Up to 182 cm"], ["Warranty", "Limited lifetime"]]},
  {"asin": "B09HC2LWX8", "role": "Lightest", "price": "$649",
   "pros": ["30.2 lb, the lightest box here", "Published 100 lb max load", "60 in long, well clear of the hatch", "Integrated tie-down points", "Made in the USA; limited lifetime warranty"],
   "cons": ["Needs a 32–46 in crossbar spread", "10 cu ft; no skis", "23 in wide leaves bar space but less volume"],
   "body": "If you want the most gear allowance under the 120 lb figure, the Yakima DeepSpace 10 is the lightest box here. Yakima lists it at 60 x 23 x 16 in with 10 cu ft, a 30.2 lb box weight and a 100 lb load rating, with tie-down points inside, a limited lifetime warranty and made-in-USA construction, at $649. At 60 in it sits well forward of the hatch, and at 23 in wide it leaves room on the bars for a bike or ski mount, as long as the combined weight still works.\n\nThe spread is the catch. Yakima's range is 32 to 46 in, wider than any other box here. The 24 to 42 in spread in etrailer's 4Runner answer is for the Yakima SkyBox 12, not this box, and neither range tells you where your bars actually sit, so measure yours center to center. If the factory rails can't place the bars at least 32 in apart, the DeepSpace won't mount. On a platform, the clamps can often go farther apart. Once it's on, 120 lb minus 30.2 lb leaves about 90 lb before bars, the most of any box here.",
   "who": "Owners with bars that can spread 32 in or more who want the lightest locking box and the most gear allowance.",
   "specs": [["Volume", "10 cu ft"], ["Exterior", "60 × 23 × 16 in"], ["Box weight", "30.2 lb"], ["Max load", "100 lb"], ["Crossbar spread", "32–46 in"], ["Made in", "USA"], ["Warranty", "Limited lifetime"], ["Price", "$649 (Yakima)"]]},
  {"asin": "B001PUZXGK", "role": "Best Yakima 16", "price": "$599 on sale at Yakima",
   "pros": ["16 cu ft, dual-side opening", "15 in tall, low for a 16 cu ft box", "24–34.5 in spread suits most factory bars", "Skis and boards up to 185 cm", "$599 on sale (regular $749); limited lifetime warranty"],
   "cons": ["47 lb, 11 lb more than the Pulse L", "81 in long, the longest box here", "No published load rating"],
   "body": "The Yakima SkyBox 16 Carbonite is the pick if you want Yakima's dual-side opening and 16 cu ft at a sale price. Yakima lists it at 81 x 36 x 15 in and 47 lb, with a 24 to 34.5 in crossbar spread, skis and boards up to 185 cm and a limited lifetime warranty. It was $599 on sale (regular $749) on Yakima's store. The 15 in height keeps it lower than most 16 cu ft boxes, which helps on a tall truck.\n\nOn the 4Runner, two numbers need planning. The 47 lb weight leaves 73 lb of the 120 lb figure before the bars, so you have roughly 50 to 60 lb for gear in practice, about 11 lb less than with a Pulse L. And at 81 in it is the longest box here, so mount it well forward and measure from the center of the front bar to the hatch seam before the first trip. Yakima doesn't publish a load rating for it on the product page, so the roof figure is the one to plan around.",
   "who": "Owners who want Yakima's dual-side 16 cu ft box at the sale price and will pack light.",
   "specs": [["Volume", "16 cu ft"], ["Exterior", "81 × 36 × 15 in"], ["Box weight", "47 lb"], ["Crossbar spread", "24–34.5 in"], ["Opening", "Dual-side"], ["Ski length", "Up to 185 cm"], ["Warranty", "Limited lifetime"]]},
  {"asin": "B00BCLL8C0", "role": "Best budget", "price": "$449.95",
   "pros": ["18 cu ft for $449.95 at SportRack", "63 in long, clear of the hatch on most setups", "Tool-free mounting hardware and a lock", "Fits square, round and most factory bars, per SportRack", "Rear opening keeps you out of traffic"],
   "cons": ["Box weight and load rating not published; confirm", "Fixed mounting positions must match your bars", "19 in tall, the tallest here"],
   "body": "The SportRack Vista XL is the lowest-priced box here. SportRack lists it at 63 x 38 x 19 in with 18 cu ft, UV-resistant ABS, tool-free mounting hardware and a lock, for $449.95, and says it fits square bars, round bars and most factory racks. etrailer lists three fixed mounting positions, 25-7/8, 27-7/8 and 29-7/8 in center to center, so your 4Runner's factory bars need to sit at one of them. At 63 in, it leaves more room for the hatch than any box here except the DeepSpace 10.\n\nThe reason it ranks last on a 4Runner is weight. SportRack doesn't publish a box weight or a load rating, and 18 cu ft of gear can far exceed what's left of a 120 lb roof figure. Confirm the box weight on the listing before you plan a load, and fill it with light, bulky items. It opens at the rear, which means reaching over the back of a tall truck, so a step helps, and at 19 in tall it needs the most garage clearance of any box here.",
   "who": "Budget buyers who want a short, lockable box and will fill it with light, bulky gear.",
   "specs": [["Volume", "18 cu ft"], ["Exterior", "63 × 38 × 19 in"], ["Opening", "Rear"], ["Mounting positions", "25-7/8, 27-7/8 or 29-7/8 in (etrailer)"], ["Hardware", "Tool-free; lock included"], ["Material", "UV-resistant ABS"], ["Box weight / max load", "Not published; confirm"], ["Price", "$449.95 (SportRack)"]]},
 ],
 "install": [
  "Identify your roof: factory crossbars, bare raised rails, a TRD Pro basket or a platform. Fit crossbars listed for 2010–2024 raised rails if you have none.",
  "Weigh the setup on paper: bars or platform plus box must leave enough of the 120 lb figure (or your manual's number) for the gear you plan to carry.",
  "Measure the bar spread center to center and set it inside the box's range, such as 23-5/8 to 34-3/8 in for the Pulse L or 24–39 in for the Wedge 660.",
  "With a helper, set the box on the bars, center it side to side and slide it forward, keeping the front clear of the windshield and sunroof.",
  "Fit the clamps loosely, open the hatch slowly to check the gap at the tail of the box, then tighten the clamps to the maker's instructions.",
  "Lock the box, rock it from each corner, and re-check the clamps after the first drive and after any trail miles.",
 ],
 "avoid": [
  {"h": "Treating the box rating as the roof rating", "body": "The Pulse L is rated for 110 lb and the MasterFit for 165 lb, but the reader-cited roof figure of 120 lb covers bars, box and gear together. The lower number always applies."},
  {"h": "Clamping to a TRD Pro basket", "body": "Box clamps are made to wrap crossbars of a set size. Fit bars or a platform, or get the box maker's approval before clamping to basket tubing."},
  {"h": "A box on a platform with a full load", "body": "A 59 lb 3/4 platform plus a 36 lb box uses about 95 lb of 120 lb. On a platform, carry soft, light gear only."},
  {"h": "Skipping the hatch measurement", "body": "Measure from the center of the front bar to the hatch seam and compare with the box maker's figure, such as etrailer's 57 in for the SkyBox 12."},
 ],
 "verdict": {
  "thesis": "Keep the box light: the Thule Pulse L is the best all-round box for a low roof limit, the Rhino-Rack MasterFit 440L if you want dual-side opening, the INNO Wedge 660 for garages, and the SportRack Vista XL on a budget.",
  "body": "On the 2010–2024 4Runner, the roof figure decides more than the badge. We work from a reader-cited 120 lb and could not confirm Toyota's own number, so read your owner's manual before loading. At 36 lb with 16 cu ft, the Pulse L leaves the most gear allowance of any full-size box here, and the MasterFit 440L adds dual-side opening for only 2.6 lb more. The Wedge 660 is the low-profile choice at 11 in tall, the DeepSpace 10 is the lightest box if your bars spread 32 in, the SkyBox 16 gives Yakima's dual-side 16 cu ft at a sale price, and the Vista XL is the budget box once you confirm its weight. Most trucks can clamp any of them to the factory crossbars; TRD Pro basket trucks need bars or a platform first.\n\nIf you still need bars or want a platform, our 4Runner roof rack guide lists fit-checked options, and a trailer hitch with a hitch cargo carrier is the place for heavy coolers and fuel. Owners of the 2025–2026 4Runner should use the separate guide, because 5th-gen bars don't fit the new roof.",
 },
 "sources": [
  ["Thule Pulse L TH615 specs (etrailer)", "https://www.etrailer.com/Roof-Box/Thule/TH615.html"],
  ["Thule Pulse M TH614 specs (etrailer)", "https://www.etrailer.com/Roof-Box/Thule/TH614.html"],
  ["Rhino-Rack MasterFit Roof Box 440L RMFT440 (Rhino-Rack)", "https://www.rhinorack.com/en-us/products/roof-racks/roof-boxes/roof-boxes/masterfit-roof-box-440l-black-_rmft440"],
  ["INNO Wedge 660 specs (etrailer)", "https://www.etrailer.com/Roof-Box/INNO/INBRM660BK.html"],
  ["Yakima DeepSpace 10 (Yakima)", "https://yakima.com/collections/roof-boxes/products/deepspace-10"],
  ["Yakima SkyBox 16 Carbonite (Yakima)", "https://yakima.com/collections/roof-boxes/products/skybox-16-carbonite-2014-2023"],
  ["SportRack Vista XL (SportRack) and mounting positions (etrailer)", "https://www.sportrack.com/product/vista-xl-cargo-box/"],
  ["Yakima SkyBox 12 on 2015 4Runner Limited factory crossbars, expert answer (etrailer)", "https://www.etrailer.com/question-239020.html"],
  ["Top 5th Gen 4Runner Roof Racks; the 120 lb figure is in a reader comment citing a 2016 SR5 owner's manual (Trail4Runner)", "https://trail4runner.com/2017/12/04/5th-gen-4runner-roof-racks/"],
  ["Genuine Toyota Roof Cross Bar Kit PT278-89170 for the 4Runner: 132 lb maximum evenly distributed across both bars, see owner's manual (North Park Toyota parts)", "https://parts.northparktoyota.com/oem-parts/toyota-roof-cross-bar-kit-pt27889170"],
  ["2017 Toyota 4Runner: tow-hitch receiver and wiring harness standard on all grades, 5,000 lb towing, 500 lb tongue weight (Toyota Newsroom)", "https://pressroom.toyota.com/2017-toyota-4runner-everday-suv-explore-where-when-you-want/"],
  ["2019 Toyota 4Runner: receiver standard on all grades; new TRD roof rack on the TRD Pro only (Toyota Newsroom)", "https://pressroom.toyota.com/2019-toyota-4runner-strengthens-legacy-35-year/"],
  ["2020 Toyota 4Runner: receiver standard on all models; TRD roof rack exclusive to the TRD Pro (Toyota Newsroom)", "https://pressroom.toyota.com/the-adventurer-toyota-4runner-gains-new-safety-and-multimedia-tech-for-2020/"],
  ["2021 Toyota 4Runner: Yakima cargo baskets on the Trail and Venture Special Editions (Toyota Newsroom, PDF view)", "https://pressroom.toyota.com/?generate_pdf=64905"],
  ["Thule Force 3 L front clearance (Thule)", "https://www.thule.com/en-us/cargo-carrier/car-top-carrier/thule-force-3-l-_-645750"],
 ],
}

# Product list for this page (boxes only; crossbars live on the 4Runner roof-racks page). (asin, name, brand, band, cond, note)
FITS = [
 ("B009NN4ZDS","Thule 615 Pulse Cargo Box, Large, Black (16 cu ft, 36 lb)","Thule","$700–$900",{},"Universal box; confirm your factory bars sit 23-5/8 to 34-3/8 in apart."),
 ("B07B4P7WYX","Rhino-Rack MasterFit Roof Box 440L (Black), 15.5 cu ft","Rhino-Rack","$600–$900",{},"Universal box; confirm 620-930 mm bar spacing and hatch gap."),
 ("B06VX9L59C","INNO BRM660BK Wedge Cargo Box - 11 Cubic FT (Gloss Black)","INNO","$850–$1,000",{},"Universal box, 11 in tall; confirm hatch gap (80 in long)."),
 ("B09HC2LWX8","Yakima DeepSpace 10 Hard Shell Cargo Box, 10 cu ft (100 lb max)","Yakima","$550–$700",{},"Needs 32-46 in spread; confirm your factory bars reach 32 in."),
 ("B001PUZXGK","Yakima SkyBox 16 Carbonite Rooftop Cargo Box, 16 cu ft (81 in long)","Yakima","$550–$750",{},"Universal box; confirm hatch gap and 24-34.5 in spread."),
 ("B00BCLL8C0","SportRack Vista XL Rear Opening Cargo Box, 18 cu ft, Black","SportRack","$400–$500",{},"Fixed mounting positions; confirm box weight against the roof load figure in your owner manual."),
 ("B009NN4SBM","Thule 614 Pulse Cargo Box, Medium, Black (14 cu ft, 34 lb)","Thule","$650–$850",{},"Smaller Pulse; confirm 23-5/8 to 33-3/8 in spread."),
]
