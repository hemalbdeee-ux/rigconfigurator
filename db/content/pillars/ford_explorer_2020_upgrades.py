"""Upgrades pillar: 2020–2026 Ford Explorer (6th gen, U625; three-row SUV, no bed).
Hub page: ranks the four published Explorer category guides and links to them. No product picks or ASINs here
(the site pulls each guide's #1 pick). Every price band comes from the linked guides' picks[].price fields or price
text in those guides (Malone AirFlow2 and Yakima BaseLine on etrailer, the Husky third-row bundle's FITS band);
vehicle facts from db/migrations/003_vehicles.sql (SUV, raised rails standard, no stored roof load figure, hitch
class 3 with a 2 in receiver, 5,600 lb with tow package, three rows, hybrid note, "2025 facelift keeps roof/hitch
fit"), the four guides and their sources, and five pages opened for this page on 2026-10-04: Wikipedia's
sixth-generation Explorer page (rear-wheel-drive-based CD6 platform shared with the Aviator; 5,300 lb on the 2.3L
and 5,600 lb on the 3.0L; Timberline added for 2021; 2025 facelift with a redesigned front fascia and revised
interior; trims cut to Active, ST-Line, ST, Platinum; Tremor, replacing the Timberline, and Active 100A for 2026),
Ford's Explorer page, which now shows the 2027 model (5,000 lb on any model; standard Class III Trailer Tow
Package with a Class III hitch receiver, seven-wire harness, four- and seven-pin connectors; second-row captain's
chairs standard and a bench available on all but the Tremor; Slick Roof Conversion deletes the roof rails on
Active, ST-Line, Platinum and ST), Ford Authority's October 2023 report (2024 lineup drops the 3.3L hybrid and the
Limited Hybrid and Platinum Hybrid trims; Police Interceptor Utility keeps it), Ford's accessory page for the
Yakima crossbar kit VLB5Z7855100A (2020–2027 Explorer, up to 165 lb depending on vehicle and bar rating) and
Draw-Tite's 76320 page (Class IV, 6,000 / 900 lb, not for weight distribution). Ford's support page on roof rack
weight opened without its article text and is not cited.
Not verified, and worded as such in the text: the Explorer's roof load limit from any Ford document; whether the
Class III package is standard on 2025 and 2026 from a Ford document (dealer and reference pages say so, Ford's
page shows 2027, and CURT still lists a 2025+ fit for Explorers without a receiver); which hitch class the 2020–2024
factory package used with each engine; what an Explorer built without the package is rated to tow; the hybrid's
tow rating; the Explorer's own tongue weight limit; second-row seating by trim for 2020–2026 (Ford's page is 2027);
whether the Slick Roof option existed before 2027; the hybrid's last retail model year (2023 is our reading of
Ford Authority); liner fit around the 2025 console; fit of any part on the Timberline, Tremor or Police
Interceptor Utility beyond what the guides say; SportRack Vista XL weight and load rating; and 2025–2026 fit of
listings whose titles stop at 2023, 2024 or 2025. No Explorer guide exists for running boards or lighting; neither
is ranked.
"""

KIND = "upgrades"
KEY = ("ford", "explorer", "2020-present")
CATEGORIES = ["floor-mats", "roof-racks", "cargo-boxes", "hitches"]

TITLE = "2020–2026 Ford Explorer Upgrades, Ranked: 4 Mods in Order, With Second-Row and Tow Package Fit Traps"
META = ("Four 2020–2026 Explorer upgrades in buying order: floor liners, roof rack, cargo box and trailer hitch, with "
        "second-row, roof limit and tow package checks.")

FAQ = [
 ("What should I upgrade first on a 2020–2026 Ford Explorer?",
  "Floor liners, then crossbars. Liners cost the least, from about $70–$110 for a front and second-row rubber set, "
  "and need one fact from you: captain's chairs or a bench in the second row. A roof rack is second because "
  "clamp-on bars for the raised rails cost about $80–$150 and need no fit kit. A cargo box is third, since it mounts "
  "to those bars. A trailer hitch is last because many Explorers already have a receiver."),
 ("Does every 2020–2026 Explorer come with a trailer hitch from the factory?",
  "No. On 2020–2024 Explorers the Trailer Tow Package was optional, so many were built with no receiver. Dealer and "
  "reference pages in our hitch guide report that Ford made the Class III package standard on every 2025 trim, and "
  "Ford's current Explorer page, which now shows the 2027 model, lists it as standard. We could not confirm 2025 and "
  "2026 from a Ford document. Look under the rear bumper for a square 2 in opening."),
 ("How much can a 2020–2026 Explorer tow, and does an aftermarket hitch raise it?",
  "A hitch never raises it. Our vehicle data lists a maximum of 5,600 lb with the tow package, which is the 3.0L "
  "EcoBoost V6 figure for 2020–2024. The 2.3L EcoBoost is rated at 5,300 lb with the package, and the hybrid lower. "
  "Dealer pages and TowingSpecs list 5,000 lb for every 2025 and 2026 Explorer. The lower of hitch and vehicle "
  "applies, so a 6,000 lb CURT 13438 adds no capacity and a 3,500 lb Draw-Tite 76910 reduces it."),
 ("How much weight can an Explorer carry on the roof with crossbars and a cargo box?",
  "Use the lowest of three numbers. Brand-name raised-rail systems for the Explorer are rated at 165 lb. The box may "
  "have its own cargo limit, such as 110 lb for Thule's Pulse L. The Explorer's roof limit is in the owner's manual; "
  "we could not confirm that figure from Ford. On 165 lb bars, a 51.5 lb Yakima GrandTour 16 leaves 113.5 lb for "
  "gear at most."),
 ("Do I need crossbars before a cargo box, or do the factory rails do the job?",
  "You need crossbars. The factory rails run front to back, and a box clamps to bars that run across the roof. "
  "Raised rails have a gap underneath, so any raised-rail crossbar that names the Explorer clamps on without a "
  "vehicle-specific fit kit. Our roof rack guide lists Amazon sets at about $80–$150. The exception is Rightline "
  "Gear's Sport 3 soft carrier, about $140, which RealTruck lists for vehicles with or without a roof rack."),
 ("Which floor liners fit a 6-passenger Explorer, and which fit a 7-passenger?",
  "Six-passenger Explorers have two captain's chairs in the second row; seven-passenger Explorers have a bench. In "
  "our floor liner guide, the 3W, LASFIT and DrCarNow three-row sets are listed for 6-passenger models only. Husky's "
  "6-piece WeatherBeater kit is listed for a bench or buckets with a center console. Husky's 99321 is listed for "
  "2020–2026 without naming a layout, so check Husky's fit tool, and KUST's listing asks you to check 6- versus "
  "7-passenger."),
 ("Do parts from a 2011–2019 Explorer fit the 2020 and newer Explorer?",
  "No. Wikipedia says the 2020 Explorer moved to the rear-wheel-drive-based CD6 platform shared with the Lincoln "
  "Aviator. Husky sells front liners 13761 for 2015–2019 and 99321 for 2020–2026. Our hitch guide says "
  "fifth-generation hitches such as Draw-Tite's 76034 won't bolt up, and our roof rack guide says 2011–2019 bars "
  "were made for a different roof. Buy listings whose year range starts at 2020."),
 ("Did the 2025 facelift change which Explorer accessories fit?",
  "Only in part. Our vehicle data notes that the 2025 facelift keeps roof and hitch fit, and etrailer's 2025 "
  "Explorer list carries the same raised-rail part numbers as earlier years. Two things changed for buyers. The "
  "Class III tow package is reported standard from 2025, so a hitch is rarely needed. And our floor liner guide says "
  "the console was revised, so confirm the second-row liner with the seller."),
 ("Do these upgrades fit the Explorer Hybrid, ST, Timberline and Police Interceptor Utility?",
  "Our guides treat the Hybrid, ST and Timberline as sharing the sixth-generation floor and raised rails, and 3W's "
  "liner listing names the hybrid. The hybrid's tow rating is lower. Listings rarely name the Timberline or the 2026 "
  "Tremor, so check for a gap under the rail and ask the seller. The Police Interceptor Utility has a fleet-specific "
  "interior, often with vinyl flooring, and retail liners aren't listed for it."),
 ("How much does it cost to add all four upgrades to an Explorer?",
  "From the prices on our four guides' picks, a budget build runs about $410–$560: KUST rubber mats, budget "
  "crossbars, Rightline Gear's soft carrier and a budget hitch. A mid build runs about $925–$1,045 with Husky's "
  "99321 or 3W liners, KINGGERI or Powerty bars, SportRack's Vista XL and CURT's 13438. A premium build with "
  "Husky's 6-piece kit, Malone's AirFlow2, a Yakima or Thule box and Draw-Tite's Hidden Hitch runs about "
  "$1,525–$2,211. Subtract the hitch if a receiver is fitted."),
]

ARTICLE = {
 "dek": "Four upgrades for the sixth-generation Explorer, in the order most owners should buy them. Fit on this "
        "three-row SUV turns on a short list of facts: a second-row bench or captain's chairs, a console or an open "
        "walkway, whether the roof still has its raised rails, whether a tow package was ordered, and which side of "
        "2020 and 2025 the listing was written for.",
 "author": "jake-morrison",
 "reviewed": "2026-10-04",
 "method": "We did not install any of these parts ourselves. The order comes from our four fit-checked 2020–2026 "
           "Explorer guides, weighing how many Explorers each upgrade suits, what it costs, what it depends on and "
           "how much work or doubt sits in the fit. Price bands are the prices on those guides' picks, checked in "
           "September 2026, and are approximate. Vehicle facts come from our vehicle data, the guides' sources, "
           "Wikipedia, Ford Authority, Draw-Tite and Ford's Explorer and accessory pages. Ford's page now shows the "
           "2027 model, and we say so wherever we lean on it. Where we couldn't confirm a factory detail, the text "
           "says so.",
 "takeaways": [
  "**Look at the second row first.** Captain's chairs seat six and a bench seats seven, and the second-row floor liner is shaped differently for each.",
  "**Buy 2020+ parts.** The 2020 Explorer moved to a new rear-wheel-drive-based platform, so 2011–2019 liners, hitches and crossbars don't carry over.",
  "**Crossbars come before the cargo box.** Raised rails take clamp-on bars with no fit kit, and brand-name systems for the Explorer are rated at 165 lb.",
  "**Check for a receiver before hitch shopping.** The tow package was optional for 2020–2024, and dealers report it standard from 2025.",
  "**No hitch raises the tow rating.** Sources put it at 5,300 lb (2.3L) or 5,600 lb (3.0L) with the package for 2020–2024 and 5,000 lb for 2025–2026.",
 ],
 "priority": [
  {"category": "floor-mats",
   "h": "1. Floor liners first: one look at the second row decides the set",
   "why": "Floor liners lead on the Explorer because they cost the least and every Explorer can use them. One fact "
          "decides fit: the second row. Captain's chairs make a 6-passenger Explorer, with a center console or an "
          "open walkway between them, and a bench makes a 7-passenger one. In our guide, the 3W, LASFIT and "
          "DrCarNow three-row sets are 6-passenger only. Husky's 6-piece WeatherBeater kit is listed for a bench or "
          "for buckets with a center console, and Husky's 99321 names no layout, so run it through Husky's fit "
          "tool. Prices run about $70–$110 for KUST's rubber front and second-row mats, about $110–$190 for the "
          "three-row TPE sets, about $150–$210 for Husky's 99321 and about $280–$380 for the Husky kit that adds "
          "the third row and cargo area. The trade-off is coverage against price: the cheapest set stops at the "
          "second row.",
   "skip_if": "The factory mats are holding up, the cabin stays dry and nobody climbs into the third row in muddy shoes."},
  {"category": "roof-racks",
   "h": "2. Roof rack second: cheap crossbars on raised rails, and the base for the box",
   "why": "A roof rack ranks second because on this SUV it is cheap, quick to fit and the foundation for the next "
          "slot. Our vehicle data lists raised side rails as standard. The rail has a gap underneath, so a crossbar "
          "clamps around it with no vehicle-specific fit kit. Look at your own roof first, though: Ford's current "
          "Explorer page lists a Slick Roof Conversion that deletes the rails on some trims. A bar sold as \"flush\", such as Thule's WingBar Edge, still clamps to raised rails, while "
          "flush-rail feet don't fit. Prices in our guide run about $80–$120 for KitsPro's or PARTOL's bars, about "
          "$90–$140 for Powerty's lockable set and about $100–$150 for KINGGERI's. etrailer lists Malone's AirFlow2 "
          "with locks at $245.60–$260.95. Brand-name systems are rated at 165 lb and the Amazon sets print "
          "260–330 lb. The trade-off is proof: the higher printed ratings are the sellers' own, with no published "
          "test.",
   "skip_if": "Everything you carry fits behind the third row or on a hitch carrier, and no cargo box, skis or boats are planned."},
  {"category": "cargo-boxes",
   "h": "3. Cargo box third: universal fit, limited by the bars under it",
   "why": "A cargo box comes third because it needs the crossbars from slot two. It clamps to "
          "the bars, not to the Explorer, so the vehicle-specific part is the numbers. The first is weight. "
          "Brand-name Explorer bar systems are rated at 165 lb, and the hard boxes in our guide weigh 36 lb (Thule "
          "Pulse L) to 57 lb (Yakima CBX 16), which leaves about 108–129 lb for gear before the roof limit in your "
          "owner's manual is applied. The second is length: a long box set too far back sits in the arc of the "
          "power liftgate. Prices in our guide run about $140 for Rightline Gear's Sport 3 soft carrier, about $450 "
          "for SportRack's Vista XL, about $699–$865 for Yakima's CBX 16 and GrandTour 16, Thule's Pulse L and the "
          "INNO Wedge 660, and about $1,150 for Thule's Motion 3 XL. The trade-offs are height at the garage door "
          "and a panoramic roof that should stay closed.",
   "skip_if": "Your extra loads are heavy more than bulky; those belong on a hitch carrier, not on the roof."},
  {"category": "hitches",
   "h": "4. Trailer hitch last: many Explorers already have one, and the rest need trimming",
   "why": "A trailer hitch sits last because it is the upgrade the fewest owners need to buy and the one with the "
          "most work in it. On 2020–2024 Explorers the Trailer Tow Package was optional, and dealer pages report the "
          "Class III package as standard on every 2025 trim. So look under the rear bumper first. If no receiver is "
          "there, the default in our guide is CURT's 13438, a Class III hitch rated at 6,000 lb with 600 lb of "
          "tongue weight, about $235. etrailer's install notes call for trimming the underbody panel and bumper "
          "fascia, modifying the heat shield and lowering the exhaust, in 1.5 to 3.5 hours. Draw-Tite's 76910 "
          "Hidden Hitch, about $300–$420, has a removable receiver but is rated at 3,500 lb. Budget copies from "
          "KUAFU, Autekcomma and TLAPS run about $120–$190 with seller-supplied ratings. No hitch raises the "
          "Explorer's own rating. If you carry heavy bikes or coolers, move this slot up to second.",
   "skip_if": "A square 2 in receiver is already under your rear bumper; buy a ball mount and check the wiring instead."},
 ],
 "tier_table": {
  "caption": "Approximate price bands from the picks in our 2020–2026 Explorer guides (September 2026; Amazon prices move daily). The cargo box sits on the same column's crossbars",
  "head": ["Upgrade", "Budget", "Mid", "Premium"],
  "rows": [
   ["Floor liners", "About $70–$110 (KUST rubber mats, front and second row)", "About $150–$190 (3W three-row TPE, 6-passenger) or $150–$210 (Husky 99321, front and second row)", "About $280–$380 (Husky 6-piece kit: three rows and cargo)"],
   ["Roof rack", "About $80–$120 (KitsPro or PARTOL crossbars)", "About $100–$150 (KINGGERI) or $90–$140 (Powerty, lockable)", "About $246–$261 (Malone AirFlow2 on etrailer, 165 lb)"],
   ["Cargo box", "About $140 (Rightline Gear Sport 3 soft carrier, on the budget crossbars)", "About $450 (SportRack Vista XL, on the mid crossbars)", "About $699 (Yakima CBX 16) or $709 (GrandTour 16) to $1,150 (Thule Motion 3 XL), on the Malone bars"],
   ["Trailer hitch", "About $120–$170 (KUAFU) or $130–$190 (Autekcomma, TLAPS)", "About $235 (CURT 13438, 6,000 lb)", "About $300–$420 (Draw-Tite 76910 Hidden Hitch; highest price, lowest rating at 3,500 lb)"],
   ["Total", "About $410–$560", "About $925–$1,045", "About $1,525–$2,211; wiring extra"],
  ],
 },
 "sections": [
  {"h": "Bench or captain's chairs, console or walkway: read the second row before the price",
   "body": "The sixth-generation Explorer has three rows, and its second row comes two ways. Two captain's chairs "
           "make it a 6-passenger SUV, and a three-person bench makes it a 7-passenger one. The captain's chairs can "
           "have a center console between them or an open walkway to the third row. Each layout takes a different "
           "second-row liner.\n\n"
           "Don't go by trim. Ford's current Explorer page, which now shows the 2027 model, says captain's chairs "
           "are standard on every model and the bench is available on all but the Tremor. We could not confirm "
           "seating by trim for each earlier model year, so open the rear door and look.\n\n"
           "Then decide how many zones to cover: front, second row, third row and cargo. Husky's third-row liner "
           "and cargo mat bundle (22321 and 19321) folds up and down with the third row. Its title covers 2020–2023 "
           "and it runs about $130–$180, so confirm later years.",
   "table": {"caption": "2020–2026 Explorer second-row layouts and the liner sets our guide lists for each",
             "head": ["Layout", "Seats", "Sets that list it", "Check before ordering"],
             "rows": [
              ["Captain's chairs with a center console", "6", "Husky 6-piece kit (buckets with console); 3W, LASFIT and DrCarNow list 6-passenger", "The second-row piece shape in the listing photos"],
              ["Captain's chairs with an open walkway", "6", "3W, LASFIT and DrCarNow list 6-passenger", "Whether the walkway is covered; confirm the Husky kit with Husky"],
              ["Three-person bench", "7", "Husky 6-piece kit and Husky 99321; KUST asks you to check", "None of the three-row TPE sets in our guide lists the bench"],
              ["Third row and cargo area", "6 or 7", "Husky 6-piece kit covers both; 3W, LASFIT and DrCarNow cover the third row", "3W's set has no cargo liner; KUST and Husky 99321 stop at the second row"],
             ]}},
  {"h": "Towing: the factory package, the rating by engine and year, and what a bolt-on hitch can't change",
   "body": "**The receiver.** Our vehicle data records a Class III hitch with a 2 in receiver for this generation. "
           "Our hitch guide found that the Trailer Tow Package was optional on 2020–2024 Explorers, and that dealer "
           "and reference pages report the Class III package as standard on every 2025 trim. Ford's current page, "
           "which now shows the 2027 model, describes a standard Class III Trailer Tow Package with a hitch "
           "receiver, a seven-wire harness and four- and seven-pin connectors. We could not confirm 2025 and 2026 "
           "from a Ford document, and CURT still lists its 13438 for 2025–2027 Explorers that have no factory "
           "receiver.\n\n"
           "**The rating.** Our vehicle data lists a maximum of **5,600 lb with the tow package**, which is the "
           "3.0L EcoBoost V6 figure. Wikipedia gives 5,300 lb for the 2.3L EcoBoost. For 2025 and 2026, the dealer "
           "pages and TowingSpecs cited in our hitch guide list **5,000 lb** for every engine, and Ford's current "
           "page says the same. Your figure is on the door-jamb label and in the owner's guide.\n\n"
           "**What a bolt-on hitch changes.** It adds a receiver, not rating. The lower of hitch and vehicle "
           "applies. Our hitch guide adds that Ford quoted its top ratings for Explorers with the factory package, "
           "which it says also covers cooling and wiring. If you plan to tow near 5,000 lb without the package, ask "
           "a Ford dealer what your VIN is rated for.\n\n"
           "**Class and tongue weight.** We could not confirm from Ford which hitch class the 2020–2024 package "
           "used with each engine, so read the label on the receiver. Among bolt-on hitches, tongue weight is "
           "600 lb on the Class III CURT, 900 lb on Draw-Tite's Class IV 76320 and 350 lb on the 76910. Draw-Tite "
           "says neither of its two is suitable for weight distribution systems.\n\n"
           "**Wiring.** Without the factory package there is no trailer socket, so budget for a harness.",
   "table": {"caption": "2020–2026 Explorer tow ratings and factory receivers, as the sources in our hitch guide report them",
             "head": ["Model years", "Engine", "Rating with the package", "Factory receiver"],
             "rows": [
              ["2020–2024", "2.3L EcoBoost four-cylinder", "5,300 lb", "Only with the optional Trailer Tow Package"],
              ["2020–2024", "3.0L EcoBoost V6 (ST, Platinum, King Ranch)", "5,600 lb", "Only with the optional package"],
              ["Hybrid years", "3.3L V6 hybrid", "Lower; sources differ, so read the owner's guide", "Only with the optional package"],
              ["2025–2026", "2.3L or 3.0L EcoBoost", "5,000 lb", "Dealers report the Class III package standard on every trim"],
             ]}},
  {"h": "Raised rails, crossbars and the roof limit: the math under a cargo box",
   "body": "Three limits stack under a cargo box: the box's cargo rating, the bar rating and the roof limit.\n\n"
           "**The rails.** Our vehicle data lists raised side rails as standard. No rails means a naked roof, which "
           "takes a door-frame clip system; etrailer lists Yakima's BaseLine at $604.75–$773.75. Ford's current "
           "page, for the 2027 model, lists a Slick Roof Conversion that deletes the rails on the Active, ST-Line, "
           "Platinum and ST.\n\n"
           "**The bar rating.** Every brand-name raised-rail system on etrailer's Explorer lists is rated at "
           "**165 lb**. Ford's accessory store describes its Yakima crossbar kit, VLB5Z7855100A, for the 2020–2027 "
           "Explorer as supporting up to 165 lb, depending on vehicle and bar rating. The Amazon sets print "
           "260–330 lb, which are seller figures.\n\n"
           "**The roof limit.** Our vehicle data holds no roof load figure, and we could not confirm one from a "
           "Ford page. It is in your owner's manual and covers bars, box and cargo together. Use the lowest "
           "number.\n\n"
           "On 165 lb bars, the box's weight comes off first:\n\n"
           "- **Thule Pulse L:** 36 lb, leaving 129 lb. The box's own cargo limit is 110 lb, so 110 lb applies.\n"
           "- **INNO Wedge 660:** 42 lb, leaving 123 lb. Its own limit is also 110 lb.\n"
           "- **Thule Motion 3 XL:** 51 lb, leaving 114 lb. Thule rates the box for 165 lb.\n"
           "- **Yakima GrandTour 16:** 51.5 lb, leaving 113.5 lb.\n"
           "- **Yakima CBX 16:** 57 lb, leaving 108 lb.\n"
           "- **SportRack Vista XL:** weight and load rating not published; ask the seller.\n\n"
           "**Liftgate and glass.** Measure from the front crossbar to the line where the roof meets the hatch and "
           "compare it with the box maker's figure; Thule lists more than 52 3/32 in of front clearance for the "
           "84.7 in Motion 3 XL. etrailer's experts say a rack installs fine on an Explorer ST with the panoramic "
           "roof but advise keeping the glass closed with a box on."},
  {"h": "Roof or hitch: where the weight should go, and the order to fit things",
   "body": "- **The roof takes bulky, light loads.** A hard box on 165 lb bars has about 108–129 lb left for gear. "
           "In return it keeps the liftgate and rear camera clear, locks, and keeps soft bags dry.\n"
           "- **The hitch takes heavy loads.** A hitch cargo carrier or platform bike rack loads the receiver, not "
           "the roof. Tongue weight is rated at 600 lb on CURT's 13438 and 350 lb on Draw-Tite's 76910. The "
           "Explorer has its own tongue weight limit in the owner's guide, which we could not confirm for this "
           "page, and the lower figure applies.\n"
           "- **Heavy bikes go on the hitch.** Our roof rack guide notes that lifting bikes onto a tall SUV roof is "
           "hard work.\n\n"
           "Fit the four in this order.\n\n"
           "1. **Floor liners.** Pull the factory mats, hook the driver liner onto Ford's retention posts "
           "and press each pedal to the floor.\n"
           "2. **Crossbars.** Clean the rails, set the spread and tighten the clamps side to side in steps.\n"
           "3. **Cargo box.** With a helper, center it, slide it forward and open the liftgate slowly before "
           "tightening to spec.\n"
           "4. **Hitch.** etrailer estimates 1.5 to 3.5 hours for the CURT with trimming; "
           "Draw-Tite quotes 40 minutes and no drilling for the 76910. Explorers with the hands-free liftgate have "
           "a kick sensor where the hitch goes, and CURT's instructions cover it.\n\n"
           "Running boards and lighting have no Explorer guide on this site yet, so they aren't ranked."},
  {"h": "The 2020 redesign, the Hybrid, the 2025 facelift and the trims that change fit",
   "body": "**2011–2019 parts.** Wikipedia says the 2020 Explorer moved to the rear-wheel-drive-based CD6 platform "
           "it shares with the Lincoln Aviator. Husky sells front liners 13761 for 2015–2019 and 99321 for "
           "2020–2026. Our hitch guide says Draw-Tite's 76034, a fifth-generation hitch, won't bolt up, and our "
           "roof rack guide says 2011–2019 bars were made for a different roof.\n\n"
           "**Hybrid.** Ford Authority reported in October 2023 that the 2024 lineup dropped the 3.3L V6 hybrid, "
           "along with the Limited Hybrid and Platinum Hybrid trims that carried it, while the Police Interceptor "
           "Utility kept the powertrain. That makes 2023 the last retail year as we read it. Its tow rating is "
           "lower, and 3W's is the only liner listing in our guide that names the hybrid.\n\n"
           "**2025 facelift.** Wikipedia describes a redesigned front fascia, a revised interior and a lineup cut "
           "to Active, ST-Line, ST and Platinum, with the Tremor and Active 100A added for 2026. Our vehicle data "
           "notes that the facelift keeps roof and hitch fit. Our floor liner guide says the console changed, so "
           "confirm the second-row piece for a 2025 or 2026.\n\n"
           "**Listings that stop early.** Husky's 6-piece kit, LASFIT's liners and the OBNAUX and KitsPro bars are "
           "titled through 2025. PARTOL's bars stop at 2024.\n\n"
           "**ST, Timberline and Tremor.** The ST has the same raised rails; an etrailer expert recommends Thule's "
           "Evo Raised Rail foot, TH710401, with 60 in WingBar Evo bars for a 2021 ST. Wikipedia says the Tremor "
           "replaced the Timberline for 2026. Listings in our guides don't name either, so check for a gap under "
           "the rail and ask the seller.\n\n"
           "**Police Interceptor Utility.** It uses a fleet-specific interior, often with vinyl flooring, and "
           "retail liners aren't listed for it. Treat fit of the other parts as unconfirmed."},
 ],
 "avoid": [
  {"h": "A liner set bought by trim instead of by second row", "body": "Captain's chairs and a bench take different second-row liners. The 3W, LASFIT and DrCarNow sets in our guide are 6-passenger only."},
  {"h": "2011–2019 Explorer listings, and Aviator liners", "body": "The 2020 platform has a new floor and roof. Husky's 13761 liners and Draw-Tite's 76034 hitch are fifth-generation parts, and Aviator liners are cut for a different floor."},
  {"h": "Loading the roof to the printed bar rating", "body": "A 330 lb bar doesn't change the roof limit in the owner's manual, and brand-name Explorer systems are rated at 165 lb. Count bars, box and cargo."},
  {"h": "A hitch bought before looking under the bumper", "body": "Tow-package Explorers already have a receiver. A 6,000 lb hitch on a 5,000 lb Explorer still tows 5,000 lb, and a 3,500 lb hidden hitch lowers the limit."},
 ],
 "verdict": {
  "thesis": "On the 2020–2026 Explorer, buy floor liners by second-row layout first, add raised-rail crossbars second and a cargo box matched to the bar rating third, and buy a trailer hitch only after confirming there is no factory receiver.",
  "body": "The sixth-generation Explorer is easy to accessorize once five facts are written down: bench or captain's "
          "chairs, console or walkway, rails on the roof or not, receiver under the bumper or not, and model year. "
          "Floor liners need the first two and cost the least, so they go first. Crossbars come next and the "
          "cargo box after them, because the box mounts to those bars and 165 lb of bar rating, less "
          "the box, decides what goes inside.\n\n"
          "The trailer hitch is last for most owners. Dealers report a standard receiver from 2025, many earlier "
          "Explorers were ordered with one, and the rest need an afternoon of trimming to add it. If your loads are "
          "heavy, put the hitch second, since the receiver carries what the roof can't. Owners of a 2011–2019 "
          "Explorer should treat this page as a list of questions, not part numbers.",
 },
 "sources": [
  ["Ford Explorer (sixth generation): CD6 platform, engines, towing, trims, 2025 facelift (Wikipedia)", "https://en.wikipedia.org/wiki/Ford_Explorer_(sixth_generation)"],
  ["Ford Explorer, 2027 model shown: seating, Class III Trailer Tow Package, 5,000 lb, Slick Roof Conversion (Ford)", "https://www.ford.com/suvs/explorer/"],
  ["2024 Ford Explorer drops 3.3L V6 hybrid powertrain (Ford Authority)", "https://fordauthority.com/2023/10/2024-ford-explorer-drops-3-3l-v6-hybrid-powertrain/"],
  ["Explorer 2020–2027 Crossbar System Kit by Yakima, VLB5Z7855100A (Ford Accessories)", "https://ford.com/product/racks-and-carriers-by-yakima-crossbar-kit-p2819514137"],
  ["Explorer towing capacity by year (TowingSpecs)", "https://towingspecs.com/ford/explorer/towing-capacity/"],
  ["2025 Explorer towing and standard Class III package (Group 1 Ford of Shreveport)", "https://www.group1fordofshreveport.com/ford-research/ford-explorer-towing-capacity/"],
  ["CURT 13438 Class 3 hitch (CURT)", "https://www.curtmfg.com/part/13438"],
  ["CURT CU78FR install notes for 2022 Explorer (etrailer)", "https://www.etrailer.com/Trailer-Hitch/Ford/Explorer/2022/CU78FR.html"],
  ["Draw-Tite 76910 Hidden Hitch (Draw-Tite)", "https://www.draw-tite.com/product/76910_class-iii-trailer-hitch"],
  ["Draw-Tite 76320 Class IV hitch (Draw-Tite)", "https://www.draw-tite.com/product/76320_class-iii-trailer-hitch"],
  ["2023 Ford Explorer roof rack systems by rail type (etrailer)", "https://www.etrailer.com/roof-2023_Ford_Explorer.htm"],
  ["Explorer roof rack, cargo box and panoramic roof answers (etrailer)", "https://www.etrailer.com/answers.aspx?AnswerModel=Explorer&Manufacturer=Thule&Filter=fit&AnswerMake=Ford"],
  ["Yakima GrandTour 16 (Yakima)", "https://yakima.com/products/grandtour-16"],
  ["Thule Pulse Large TH615 (etrailer)", "https://www.etrailer.com/Roof-Box/Thule/TH615.html"],
  ["Husky Liners: WeatherBeater vs X-act Contour (Husky Liners)", "https://huskyliners.com/blog/husky-liners-weatherbeater-vs-xact-contour/"],
 ],
}
