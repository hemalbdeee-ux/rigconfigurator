"""Upgrades pillar: 2020–2025 Kia Telluride (1st gen; three-row SUV, no bed; not the redesigned 2027 Telluride).
Hub page: ranks the four published Telluride category guides and links to them. No product picks or ASINs here
(the site pulls each guide's #1 pick). Every price band comes from the linked guides' picks[].price fields or price
text in those guides (etrailer prices for the Thule, Yakima and Malone crossbar systems in the roof rack guide, the
harness bands in the hitch guide's FITS); vehicle facts from db/migrations/003_vehicles.sql (SUV, year_to 2025,
flush-rails, no stored roof load figure, hitch class 3 with a 2 in receiver, 5,000 lb, three rows, rails attr "flush
side rails on LX/S/EX/SX/SX-P; raised rails with a gap on X-Line/X-Pro (2023+)", fit_note "Kia skipped the 2026
model year; the next generation is the 2027 Telluride"), the four guides and their sources, and eight pages opened
for this page on 2026-10-04: Wikipedia's Kia Telluride page (2026 model year entirely skipped; second generation
revealed online on November 10, 2025, deliveries from early 2026 for the 2027 model year; production from February
2019; shares components with the Hyundai Palisade "including its engine, transmission, and wheelbase"; three-seat
bench standard, captain's chairs drop capacity from eight to seven; 2023: 12.3-inch instrument panel, available
smart power liftgate with auto-close, redesigned grille, headlights and front bumper, X-Line and X-Pro since the
2023 model year; standard towing 5,000 lb), Kia Media's 2023 Telluride press kit ("Raised, bridge-type roof rails"
as an X-Line feature; "Standard towing rated up to 5,000 pounds (5,500 pounds for X-Pro trim)"; "Available
self-leveling rear suspension"; seven or eight passengers), Kia Media's 2023 Telluride specifications (5,500 lb on
AWD SX X-Pro and SXP X-Pro, 5,000 lb elsewhere; LX 8-passenger, EX 8-passenger with a 7-passenger option, other
grades 7-passenger, read through a text extraction), Kia's online 2024 owner's manual, roof rack topic ("220 lbs.
(100 kg) EVENLY DISTRIBUTED"; crossbars may be obtained from an authorized Kia dealer; do not operate the sunroof
with cargo on the roof rack), that manual's index and trailer towing topic (no figures on the towing topic),
etrailer's question 481662 (a 2020 Telluride owner quoting 220 lb from the manual; 165 lb Thule and Yakima systems;
the feet can be rated lower than the roof) and Kia of Cerritos' towing page (X-Pro 5,500 lb for 2023, 2024 and
2025, other trims 5,000 lb; 2022 maximum 5,000 lb). That dealer page also describes the hitch as an accessory and
lists tow mode and self-leveling rear suspension as standard on X-Line and X-Pro trims for 2024; both were read as
a summary, not a quote, and are not printed on this page.
Model-year span: three of the four guides are titled 2020–2025 and the floor liner guide is titled 2020–2026; this
page uses 2020–2025, which matches the vehicle data and Wikipedia.
Manual caveat: the owner's manual pages we opened sit under Kia's "ON" directory (index title
"ONa_STD_PE_NA_enus_24MY") and do not print the model name; the floor liner guide's docstring gives ON as the
Telluride's code and the 220 lb figure matches the etrailer owner quote. The text calls it Kia's 2024 owner's manual
and tells readers to check the roof rack page in their own.
Not verified, and worded as such in the text: the roof figure for model years other than 2024; the Telluride's
tongue weight limit from any Kia document (500 lb is an owner report); whether any trim or year left the factory
with a receiver; ratings of Kia's genuine hitch; seating by trim for years other than 2023, and which seven-seat
models have a console; 2025 fit of listings titled to 2023 or 2024; which trims the WeiSen 2023–2025 harness fits
beyond LX and S; SportRack Vista XL weight and load rating; fit of any first-generation part on the 2027 Telluride.
No Telluride guide exists for running boards, lighting or bike racks; none are ranked.
"""

KIND = "upgrades"
KEY = ("kia", "telluride", "2020-present")
CATEGORIES = ["floor-mats", "roof-racks", "cargo-boxes", "hitches"]

TITLE = "2020–2025 Kia Telluride Upgrades, Ranked: 4 Mods in Order, With Roof-Rail and Second-Row Fit Traps"
META = ("Four 2020–2025 Telluride upgrades in buying order: floor liners, roof rack, cargo box and trailer hitch, "
        "with rail type, 7 vs 8 seats, roof load and X-Pro towing.")

FAQ = [
 ("What should I upgrade first on a 2020–2025 Kia Telluride?",
  "Floor liners, then crossbars. Liners cost the least, about $110–$150 for TOUGHPRO's three-row rubber set, and "
  "need one fact from you: a second-row bench, captain's chairs with a console, or captain's chairs with an open "
  "walkway. A roof rack is second because Amazon bars cost about $90–$190 and the only fit question is which rail "
  "is on the roof. A cargo box is third, since it clamps to those bars. A trailer hitch is last for most owners; if "
  "you tow or carry heavy bikes, move it up to second."),
 ("Does my Telluride have flush or raised roof rails?",
  "It depends on the trim. Kia's 2023 press kit lists raised, bridge-type roof rails as an X-Line feature, and the "
  "roof rack guide found the X-Pro sold with the same rails. The LX, S, EX, SX and "
  "SX-Prestige have low rails that sit close to the roof, which Thule and Yakima treat as flush rails. Look along "
  "the rail from the side: daylight under it means raised, none means flush. Bars for one design don't fit the "
  "other."),
 ("How much weight can a Telluride roof carry with crossbars and a cargo box?",
  "Use the lowest of three numbers. The roof rack page of Kia's 2024 owner's manual prints 220 lb (100 kg), evenly "
  "distributed. The brand-name crossbar systems etrailer lists for the Telluride are rated at 165 lb. The box may have its own cargo limit, such as 100 lb for Yakima's DeepSpace 10. "
  "On 165 lb bars, a 51.5 lb Yakima GrandTour 16 leaves 113.5 lb for gear at most. We read the 2024 manual only, so "
  "check the page in yours."),
 ("Do 7-seat and 8-seat Tellurides take the same floor liners?",
  "The front row does; the second row may not. Eight-seat Tellurides have a second-row bench. Seven-seat Tellurides "
  "have two captain's chairs, with a center console between them or an open walkway. In the floor liner guide, "
  "SUPER LINER's three-row set is listed for buckets without a console, and WeatherTech asks buyers to confirm the "
  "layout. Husky's 95691 and Smartliner's set name the Telluride broadly, so compare the second-row piece in the "
  "listing photos with your own floor. Count the seats; don't go by trim."),
 ("How much can a 2020–2025 Telluride tow, and does a hitch change it?",
  "A hitch never raises it. The vehicle data lists 5,000 lb with a Class III hitch and a 2 in receiver. Kia's 2023 "
  "press kit says towing is rated up to 5,000 lb, and 5,500 lb for the X-Pro trim. CURT's 13420 and Draw-Tite's "
  "76420 are rated at 5,000 lb without weight distribution, so on an X-Pro the hitch is the lower number. Owners on "
  "TellurideForum cite a 500 lb maximum tongue weight. We could not confirm that from a Kia document, so read your "
  "owner's manual."),
 ("Does the Telluride come with a trailer hitch from the factory?",
  "Don't assume it. Kia sells its own Telluride hitch with a harness as a genuine accessory. Owners describe a tow "
  "package with self-leveling rear shocks on some builds, and one owner on KiaTelluride.org reported in January "
  "2023 that a dealer could not supply the package for the 2023 model. We could not confirm from Kia which trims "
  "and years left the factory with a receiver. Look under the rear bumper for a square 2 in opening and read the "
  "window sticker before ordering anything."),
 ("Did the 2023 refresh change which Telluride accessories fit?",
  "In two places. The refresh added the X-Line and X-Pro, whose raised rails take different crossbars from the "
  "flush rails on other trims. And the trailer wiring split: CURT lists its 56420 4-way harness for 2020–2022 only, "
  "so a 2023–2025 Telluride needs a harness that names those years. Elsewhere the guides found no split. Floor "
  "liner titles run from 2020 to 2024 or 2025, and CURT lists the 13420 hitch for 2020–2025, all styles."),
 ("Will 2020–2025 Telluride parts fit the 2027 Telluride?",
  "Assume not, with one exception. Wikipedia says Kia skipped the 2026 model year and revealed the "
  "second-generation Telluride on November 10, 2025, for the 2027 model year. The roof rack and hitch guides treat "
  "its body as new, and every crossbar, hitch and harness in them is listed for the first generation. Buy floor "
  "liners that name 2027. The exception is the cargo box, which clamps to crossbars, not to the vehicle, so it "
  "moves over once the 2027 has bars listed for it."),
 ("Do Hyundai Palisade parts fit the Telluride?",
  "Sometimes, so read the listing. Wikipedia says the two share components, including the engine, transmission and "
  "wheelbase. Hitches overlap: Draw-Tite lists the 76420 for both the 2020–2025 Palisade and the Telluride, while "
  "CURT sells 13420 for the Telluride and 13427 for the Palisade. Roof parts don't: Thule uses fit kit 6008 on the "
  "Palisade and 6095 on the Telluride's flush rails, with 50 in and 53 in bars. The floor liner guide says most "
  "makers sell separate liner sets because the cabins differ."),
 ("How much does it cost to add all four upgrades to a Telluride?",
  "From the prices on the four guides' picks, a budget build on a flush-rail trim runs about $780–$920: TOUGHPRO "
  "mats, Snailfly crossbars, SportRack's Vista XL and the Wsays hitch. A mid build runs about $1,129–$1,299 with "
  "Smartliner's set, BRIGHTLINES bars, Yakima's SkyBox 16 Carbonite and CURT's 13420. A premium build with "
  "WeatherTech's set, Thule's WingBar Evo system, the Thule Motion 3 XXL and Kia's own hitch runs about "
  "$2,685–$2,965. An X-Line or X-Pro pays about $20 more in the mid build and about $160 less in the premium one."),
]

ARTICLE = {
 "dek": "Four upgrades for the first-generation Telluride, in the order most owners should buy them. Fit on this "
        "three-row SUV turns on a short list of facts: flush rails or the raised rails of the X-Line and X-Pro, "
        "seven seats or eight, a receiver under the bumper or not, and which side of 2023 and 2027 the listing was "
        "written for.",
 "author": "jake-morrison",
 "reviewed": "2026-10-04",
 "method": "We did not install any of these parts ourselves. The order comes from the four fit-checked 2020–2025 "
           "Telluride guides on this site, weighing how many Tellurides each upgrade suits, what it costs and how "
           "much work or doubt sits in the fit. Price bands are the prices on those guides' picks, checked in "
           "September 2026, and are approximate. Vehicle facts come from the site's vehicle data, the guides' "
           "sources, Wikipedia, Kia's 2023 press kit and specifications, Kia's 2024 owner's manual, a Kia dealer's "
           "towing page and etrailer. Where we couldn't confirm a factory detail, the text says so.",
 "takeaways": [
  "**Look at the roof rails first.** The LX, S, EX, SX and SX-Prestige have low, flush rails; the 2023–2025 X-Line and X-Pro have raised rails with a gap, and crossbars fit one or the other.",
  "**Count the second-row seats.** A bench makes eight seats and captain's chairs make seven, with a console or an open walkway, and each layout takes its own second-row floor liner.",
  "**The bars set the roof limit.** Kia's 2024 owner's manual prints 220 lb, evenly distributed, but brand-name Telluride crossbar systems are rated at 165 lb.",
  "**No hitch raises the tow rating.** Kia lists 5,000 lb, and 5,500 lb for the X-Pro; CURT's and Draw-Tite's hitches are rated at 5,000 lb without weight distribution.",
  "**Read the years on every listing.** Trailer wiring splits at 2023, Kia skipped 2026, and the 2027 Telluride is a new generation.",
 ],
 "priority": [
  {"category": "floor-mats",
   "h": "1. Floor liners first: count the second-row seats, then choose how many rows to cover",
   "why": "Floor liners lead on the Telluride because they cost the least, every trim can use them and nothing else "
          "on this page depends on them. One fact decides fit: the second row. It comes three ways: a bench for "
          "eight seats, captain's chairs with an open walkway, or captain's chairs with a center console. SUPER "
          "LINER's three-row set is listed for buckets without a console, WeatherTech asks buyers to confirm "
          "seating, and Husky's 95691 and Smartliner's set name the Telluride broadly, so compare the listing "
          "photos with your floor. Prices in the guide run about $110–$150 for TOUGHPRO's three-row rubber mats, "
          "about $130–$170 for SUPER LINER's set or Husky's front and second-row 95691, about $180–$230 for "
          "Smartliner's three rows plus a cargo liner and about $280–$360 for WeatherTech's three-row set. The "
          "trade-off is coverage and wall height against price: the rubber mats have lower edges, and Husky's set "
          "stops at the second row.",
   "skip_if": "The factory mats are holding up, the cabin stays dry and the third row rarely carries muddy shoes."},
  {"category": "roof-racks",
   "h": "2. Roof rack second: low-cost crossbars, once you know which rail is on the roof",
   "why": "A roof rack ranks second because a three-row SUV with every seat in use has little room left behind the "
          "third row, crossbars are the cheapest way to add carrying space, and the next slot depends on them. Rail "
          "type decides fit, and it follows trim. The vehicle data records flush side rails on the LX, S, EX, SX "
          "and SX-Prestige and raised rails with a gap on the X-Line and X-Pro, both sold for 2023–2025. Bars for "
          "one don't fit the other. Prices in the roof rack guide run about $90–$130 for Snailfly's standard-trim "
          "set or its X-Line set, about $100–$140 for Tuyoung's X-Line set, about $130–$170 for BRIGHTLINES' "
          "flush-rail set and about $150–$190 for its raised-rail set. etrailer lists Thule's WingBar Evo system at "
          "about $705 for flush rails and about $545 for raised rails. The trade-off is proof: the brand-name "
          "systems publish a 165 lb rating, while the 300 lb on Tuyoung's listing is the seller's own figure.",
   "skip_if": "Everything you carry fits behind the third row or on a hitch carrier, and no cargo box, skis or boats are planned."},
  {"category": "cargo-boxes",
   "h": "3. Cargo box third: it fits any Telluride with bars, inside the bar rating and the bar spread",
   "why": "A cargo box comes third because it needs the crossbars from slot two. It clamps to the bars, not to the "
          "Telluride, so the vehicle-specific part is two numbers. The first is weight. Brand-name Telluride "
          "crossbar systems are rated at 165 lb, below the 220 lb roof figure in Kia's 2024 owner's manual, and the "
          "boxes in the cargo box guide weigh 30.2 lb to 57.2 lb. The second is spread, the distance between the "
          "bars. The Rack Shop lists a 27.5 in maximum for its Thule flush-rail setup, which suits the SkyBox 16 "
          "Carbonite (24–34.5 in) and GrandTour 16 (24–36 in) but not the DeepSpace 10, which needs 32–46 in. "
          "Prices run about $450 for SportRack's Vista XL, about $599 for the SkyBox 16 on sale, about $649 for the "
          "DeepSpace 10, about $709 for the GrandTour 16 and about $1,250 for the Thule Motion 3 XXL alone. The "
          "trade-off is height at the garage door: the boxes add 15 to 19 in on top of the bars.",
   "skip_if": "Your extra loads are heavy more than bulky; coolers and bins belong on a hitch carrier, not on the roof."},
  {"category": "hitches",
   "h": "4. Trailer hitch last: one part fits every trim, but the wiring goes by year and the X-Pro gives up 500 lb",
   "why": "A trailer hitch sits last for most owners because it takes the most work, needs a wiring harness bought "
          "with it and may already be on the vehicle: Kia sells its own hitch as an accessory, so look under the "
          "rear bumper first. Fit of the hitch itself is simple. CURT lists the 13420 for the 2020–2025 Telluride, "
          "all styles, at 5,000 lb and 750 lb of tongue weight, about $220–$300. Draw-Tite's 76420, in the same "
          "price band, is rated at 5,000 lb and 500 lb, and Draw-Tite quotes a 30-minute install with no drilling. "
          "Budget hitches run about $130–$190 with seller-supplied ratings, and Kia's own hitch with harness runs "
          "about $450–$650. Two things on this SUV change the buy. Kia lists the X-Pro at 5,500 lb, so a 5,000 lb "
          "hitch becomes the limit. And CURT's 56420 4-way harness is listed for 2020–2022 only, so 2023–2025 "
          "models need a harness that names those years.",
   "skip_if": "A square 2 in receiver is already under your rear bumper; buy a ball mount and check the wiring instead."},
 ],
 "tier_table": {
  "caption": "Approximate price bands from the picks in the 2020–2025 Telluride guides (September 2026; Amazon prices move daily). Totals are for a flush-rail trim, the cargo box sits on the same column's crossbars, and a harness, about $20–$60, is extra with the Budget and Mid hitches",
  "head": ["Upgrade", "Budget", "Mid", "Premium"],
  "rows": [
   ["Floor liners", "About $110–$150 (TOUGHPRO rubber mats, three rows)", "About $180–$230 (Smartliner, three rows plus cargo liner)", "About $280–$360 (WeatherTech set, three rows)"],
   ["Roof rack", "About $90–$130 (Snailfly bars; same band for flush rails or X-Line and X-Pro)", "About $130–$170 (BRIGHTLINES flush-rail set). X-Line and X-Pro: about $150–$190", "About $705 (Thule WingBar Evo flush-rail system on etrailer). X-Line and X-Pro: about $545"],
   ["Cargo box", "About $450 (SportRack Vista XL, on the Snailfly bars)", "About $599 (Yakima SkyBox 16 Carbonite on sale, on the BRIGHTLINES bars)", "About $1,250 (Thule Motion 3 XXL, box alone, on the Thule bars)"],
   ["Trailer hitch", "About $130–$190 (Wsays; confirm ratings on the listing)", "About $220–$300 (CURT 13420, 5,000 lb / 750 lb)", "About $450–$650 (Kia genuine hitch with harness; ask for its ratings)"],
   ["Total", "About $780–$920", "About $1,129–$1,299; about $1,149–$1,319 on an X-Line or X-Pro", "About $2,685–$2,965; about $2,525–$2,805 on an X-Line or X-Pro"],
  ],
 },
 "sections": [
  {"h": "Two roofs on one generation: flush rails, or the raised rails of the X-Line and X-Pro",
   "body": "The first-generation Telluride was built with two rail designs, and nearly every crossbar listing is "
           "written for one of them.\n\n"
           "**Standard trims.** The vehicle data records flush side rails on the LX, S, EX, SX and SX-Prestige. "
           "They sit close to the roof with no gap underneath. Thule and Yakima fit them with flush-rail feet plus "
           "a Telluride fit kit; Thule's is kit 6095.\n\n"
           "**X-Line and X-Pro.** Kia's 2023 press kit lists raised, bridge-type roof rails as an X-Line feature, "
           "and the roof rack guide found the X-Pro listed with the same rails by every X-Line bar seller it "
           "checked. A clamp wraps around a raised rail through the gap, so no vehicle-specific kit is needed and "
           "the systems cost less.\n\n"
           "etrailer's Telluride lists show both kinds of system for every year, because the catalog doesn't know "
           "your trim. Look along the rail from the side: daylight under it means raised.",
   "table": {"caption": "2020–2025 Telluride rails and what the roof rack guide lists for each",
             "head": ["Rail", "Trims and years", "Amazon sets in the guide", "Brand-name systems on etrailer"],
             "rows": [
              ["Low rails, treated as flush", "LX, S, EX, SX, SX-Prestige, 2020–2025", "Snailfly, about $90–$130; BRIGHTLINES, about $130–$170, 165 lb", "Thule WingBar Evo, about $705; Yakima SightLine from about $605"],
              ["Raised, bridge-type rails", "X-Line and X-Pro, 2023–2025", "Snailfly, about $90–$130, 165 lb; Tuyoung, about $100–$140; BRIGHTLINES, about $150–$190, 165 lb", "Malone AirFlow2, about $246–$261; Thule WingBar Evo or Yakima TimberLine, about $545"],
             ]}},
  {"h": "220 lb on the roof, 165 lb on the bars: the math under a cargo box",
   "body": "Three limits stack under a cargo box: the roof figure, the bar rating and the box's own cargo limit. The "
           "lowest one applies.\n\n"
           "**The roof figure.** The roof rack page of Kia's 2024 owner's manual prints **220 lb (100 kg), evenly "
           "distributed**, and a 2020 Telluride owner quoted the same figure to etrailer. We read the 2024 manual "
           "only, so check the page in yours. The figure covers bars, box and cargo together.\n\n"
           "**The bar rating.** The Thule, Yakima and Malone systems on etrailer's Telluride list are rated at "
           "**165 lb**. etrailer's expert explains the gap: the roof may be rated for 220 lb, but the feet that "
           "attach the bars can be rated for less, and that becomes the limit for the whole system. Amazon sets "
           "print 165 lb (BRIGHTLINES) to 300 lb (Tuyoung). A higher bar rating doesn't raise the roof figure.\n\n"
           "On 165 lb bars, the box's weight comes off first:\n\n"
           "- **Yakima DeepSpace 10:** 30.2 lb, leaving 134.8 lb, but Yakima caps the box at 100 lb of cargo.\n"
           "- **Yakima SkyBox 16 Carbonite:** 47 lb, leaving 118 lb.\n"
           "- **Yakima GrandTour 16:** 51.5 lb, leaving 113.5 lb.\n"
           "- **Thule Motion 3 XXL:** 57.2 lb, leaving 107.8 lb, well under the 165 lb Thule rates the box for.\n"
           "- **SportRack Vista XL:** weight and load rating not published; ask the seller.\n\n"
           "**Spread.** etrailer lists about 29.5 in center to center for Thule's WingBar Evo flush-rail system on "
           "a 2023 Telluride, and The Rack Shop lists a 27.5 in maximum for its Thule flush-rail setup. The SkyBox "
           "16 (24–34.5 in), GrandTour 16 (24–36 in) and Motion 3 XXL (21-13/16 to 36-9/16 in, per etrailer) fit "
           "either. The Vista XL mounts at 25-7/8, 27-7/8 or 29-7/8 in. The DeepSpace 10 needs 32–46 in.\n\n"
           "**Liftgate and sunroof.** The Motion 3 XXL is 91.3 in long. Mount any box forward and open the "
           "liftgate slowly the first time. Kia's manual says not to operate the sunroof with cargo on the roof "
           "rack."},
  {"h": "Towing: 5,000 lb, the X-Pro's 5,500 lb, tongue weight and the receiver you may already have",
   "body": "**The rating.** The vehicle data lists **5,000 lb** with a Class III hitch and a 2 in receiver. Kia's "
           "2023 press kit says towing is rated up to 5,000 lb, and **5,500 lb for the X-Pro trim**. Kia's 2023 "
           "specifications show the higher figure on the all-wheel-drive SX X-Pro and SX-Prestige X-Pro, and a Kia "
           "dealer page repeats it for 2024 and 2025. The X-Line is listed at 5,000 lb.\n\n"
           "**What a bolt-on hitch changes.** It adds a receiver, not rating, and the lower of hitch and vehicle "
           "applies. CURT's 13420 and Draw-Tite's 76420 are rated at 5,000 lb, so on an X-Pro the hitch is the "
           "lower number. Both makers publish 6,000 lb with weight distribution. That is the hitch's rating, not "
           "Kia's, so ask a Kia dealer which hitch the X-Pro figure assumes.\n\n"
           "**Tongue weight.** Owners on TellurideForum cite a 500 lb maximum. We could not confirm it from a Kia "
           "document, so read the trailer section of your manual. A loaded bike rack or cargo carrier counts as "
           "tongue weight.\n\n"
           "**The receiver.** Kia sells its own hitch with a harness as a genuine accessory, and owners describe a "
           "tow package with self-leveling rear shocks on some builds. We could not confirm from Kia which trims "
           "and years left the factory with a receiver, so look under the rear bumper. Owners on TellurideForum "
           "say the self-leveling suspension does not raise the tow rating or the tongue limit.\n\n"
           "**Wiring.** CURT lists its 56420 4-way harness for 2020–2022 only, and an Amazon copy says the factory "
           "tow package is required. For 2023–2025, the hitch guide names WeiSen's harness, listed for the LX and "
           "S; ask that seller about other trims. Harnesses in the guide run about $20–$60.",
   "table": {"caption": "2020–2025 Telluride towing figures as the sources report them (your owner's manual is the authority)",
             "head": ["Item", "Figure", "Source", "What it means"],
             "rows": [
              ["Telluride, most trims", "5,000 lb", "Vehicle data; Kia's 2023 press kit", "Matches CURT's and Draw-Tite's hitches"],
              ["X-Pro, 2023–2025", "5,500 lb", "Kia's 2023 press kit; Kia of Cerritos for 2024 and 2025", "A 5,000 lb hitch becomes the limit"],
              ["Tongue weight", "500 lb", "Owner reports on TellurideForum; not confirmed from Kia", "Trailer tongue plus anything carried in the receiver"],
              ["CURT 13420", "5,000 lb / 750 lb", "CURT", "Telluride only, all styles; not for vertical-hanging bike racks"],
              ["Draw-Tite 76420", "5,000 lb / 500 lb; 6,000 lb / 750 lb with weight distribution", "Draw-Tite", "Also listed for the 2020–2025 Palisade"],
             ]}},
  {"h": "Seven seats or eight: the second row decides the floor liners",
   "body": "The Telluride's second row comes three ways, and each takes a different second-row liner.\n\n"
           "- **Bench, eight seats.** One liner spans the rear floor.\n"
           "- **Captain's chairs with an open walkway, seven seats.** The liner bridges the walkway to the third "
           "row. SUPER LINER's three-row set is listed for this layout only.\n"
           "- **Captain's chairs with a center console, seven seats.** The liner wraps around the console. No set "
           "in the guide names this layout, so ask WeatherTech or Husky for a console-specific piece.\n\n"
           "Don't go by trim. Wikipedia says a three-seat bench is standard and captain's chairs can be added, "
           "dropping capacity from eight to seven. As we read Kia's 2023 specifications, the LX is an 8-passenger "
           "model, the EX is 8-passenger with a 7-passenger option and most other grades are 7-passenger. That "
           "table covers 2023 only and doesn't say which seven-seat models have a console, so open the rear door "
           "and look.\n\n"
           "Then decide how many zones to cover. WeatherTech's and TOUGHPRO's sets cover three rows, Smartliner's "
           "adds a cargo liner behind the third row, and Husky's 95691 stops at the second row. X-Line and X-Pro "
           "trims share the cabin floor, so they take the same liners."},
  {"h": "Model years: the 2023 refresh, the skipped 2026 and the redesigned 2027 Telluride",
   "body": "All four guides treat the first generation as one body from 2020 through 2025. Three kinds of listing "
           "blur that.\n\n"
           "**The 2023 refresh.** Wikipedia describes a 12.3 in instrument panel, an available smart power "
           "liftgate, a redesigned grille, headlights and front bumper, and the new X-Line and X-Pro trims. For "
           "buyers it changed the rails on those two trims and the trailer wiring. The guides found no split in "
           "liners or hitches.\n\n"
           "**Titles that stop early.** SUPER LINER's liners stop at 2024. BRIGHTLINES' X-Line and "
           "X-Pro bars name 2023 in the title, and the retailer adds 2024.\n\n"
           "**No 2026, then a new 2027.** Wikipedia says the 2026 model year was skipped entirely and deliveries "
           "began in early 2026 for the 2027 model year. A title that runs to 2026 covers a model year Kia didn't "
           "build, so read it as a first-generation listing and confirm with the seller. A listing that names 2027 "
           "is for a different vehicle.\n\n"
           "Fit the four in the order they are ranked: liners, crossbars, cargo box, hitch. Running boards, "
           "lighting and bike racks have no Telluride guide on this site, so they aren't ranked."},
 ],
 "avoid": [
  {"h": "Crossbars bought by year instead of by rail", "body": "A 2023 EX and a 2023 X-Line need different bars. Look for a gap under the rail, then match the trim names in the listing."},
  {"h": "Loading the roof to 220 lb, or to a 300 lb bar rating", "body": "Kia's manual figure covers bars, box and cargo together, and brand-name Telluride bar systems are rated at 165 lb. The lowest number applies."},
  {"h": "A 2020–2022 harness on a 2023–2025 Telluride", "body": "CURT's 56420 lists 2020–2022 only. And a hitch doesn't add rating: an X-Pro with a 5,000 lb hitch is a 5,000 lb setup."},
  {"h": "Palisade liners and 2027 listings", "body": "Palisade liners are cut for a different cabin, and the 2027 Telluride is a new generation. Buy parts that name the 2020–2025 Telluride."},
 ],
 "verdict": {
  "thesis": "On the 2020–2025 Telluride, buy floor liners by second-row layout first, crossbars by rail type second and a cargo box matched to the bar rating and spread third, then add a trailer hitch with a harness for your model year.",
  "body": "The first-generation Telluride is easy to accessorize once five facts are written down: seven seats or "
          "eight, console or walkway, flush rails or raised, receiver under the bumper or not, and model year. "
          "Floor liners need the first two and cost the least, so they go first. A roof rack needs only the rail "
          "type and costs about $90–$190 from the Amazon sets in the guide. The cargo box follows, because it "
          "mounts to those bars, and 165 lb of bar rating, less the box, decides what goes inside.\n\n"
          "The trailer hitch is last for most owners, since it takes the most work and its wiring splits at 2023. "
          "If your loads are heavy, put it second: the receiver carries what the roof shouldn't. X-Pro owners "
          "should remember that the brand-name hitches are rated at 5,000 lb, not 5,500 lb. Owners of a 2027 "
          "Telluride should treat this page as a list of questions, not part numbers.",
 },
 "sources": [
  ["Kia Telluride: generations, skipped 2026 model year, 2023 update, seating, Palisade relation (Wikipedia)", "https://en.wikipedia.org/wiki/Kia_Telluride"],
  ["2023 Kia Telluride press kit: X-Line raised bridge-type rails, 5,000 lb and X-Pro 5,500 lb towing (Kia Media)", "https://www.kiamedia.com/us/en/models/telluride/2023"],
  ["2023 Kia Telluride specifications: towing and seating by trim (Kia Media)", "https://www.kiamedia.com/us/en/models/telluride/2023/specifications"],
  ["Kia 2024 owner's manual, roof rack: 220 lbs. (100 kg) evenly distributed (Kia)", "https://ownersmanual.kia.com/full_webhelp/ON/2024/en_US/topics/t00305.html"],
  ["Telluride roof rack recommendations and the 220 lb manual figure (etrailer)", "https://www.etrailer.com/question-481662.html"],
  ["Telluride towing capacity by year, including X-Pro (Kia of Cerritos)", "https://www.kiacerritos.com/manufacturer-information/kia-telluride-towing-capacity/"],
  ["2023 Kia Telluride roof rack systems by rail type (etrailer)", "https://www.etrailer.com/roof-2023_Kia_Telluride.htm"],
  ["Thule flush-rail rack for 2020–2025 Telluride, 165 lb / 27.5 in spread (The Rack Shop)", "https://therackshop.com/2020-2025-kia-telluride-5dr-w-flush-rails-thule-crossbar-complete-roof-rack/"],
  ["CURT 13420 Class 3 hitch for Telluride (CURT)", "https://www.curtmfg.com/part/13420"],
  ["Draw-Tite 76420 Class III hitch, Palisade and Telluride (Draw-Tite)", "https://www.draw-tite.com/product/76420_class-iii-trailer-hitch"],
  ["CURT 56420 4-way harness fitment (CURT)", "https://www.curtmfg.com/part/56420"],
  ["Tow hitch class and tongue weight thread (TellurideForum)", "https://tellurideforum.org/threads/tow-hitch-class.14398/"],
  ["Tow package availability for 2023 thread (KiaTelluride.org)", "https://www.kiatelluride.org/threads/tow-package-with-self-leveling-suspension-available-on-lx-and-s-trims.2876/"],
  ["Yakima GrandTour 16 (Yakima)", "https://yakima.com/products/grandtour-16"],
  ["Thule Motion 3 XXL (Thule)", "https://www.thule.com/en-us/cargo-carrier/car-top-carrier/thule-motion-3-xxl-_-639950"],
 ],
}
