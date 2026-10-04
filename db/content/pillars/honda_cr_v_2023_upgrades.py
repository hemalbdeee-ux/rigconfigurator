"""Upgrades pillar: 2023–2026 Honda CR-V (6th gen; gas LX, EX, EX-L and hybrid Sport, Sport-L, TrailSport, Sport Touring).
Hub page: ranks the three published CR-V category guides and links to them. No product picks or ASINs here
(the site pulls each guide's #1 pick). Every price band comes from the linked guides' picks[].price fields or the
price text in those guides (the door-frame clamp kit prices are the etrailer figures quoted in the cargo box guide,
the roof rail list price is the dealer figure quoted there, and the Honda hitch price is the MSRP quoted in the
hitch guide); vehicle facts from db/migrations/003_vehicles.sql (SUV, 2023 onward,
roof type bare, no stored roof load, 1,500 lb; the row was corrected in the same commit to Honda's tables: bare roof on gas trims, black roof rails on hybrids, 1,000 lb hybrid towing, aftermarket 2 in receivers; earlier attrs: no factory rails, accessory rails available,
door-jamb clamp crossbars, some 2 in aftermarket hitches, 2017-2022 mats and racks do not fit), the three guides and
their sources, and seven pages opened for this page on 2026-10-04: Honda's 2026 CR-V Specifications & Features
(LX, EX, EX-L gas with 1,498 cc and 190 hp; Sport, TrailSport, Sport-L, Sport Touring hybrid with 1,993 cc and 204 hp
total; towing 1,500 lb gas and 1,000 lb hybrid; "Black Roof Rails" standard on the four hybrid trims and not on the
gas trims; power tailgate on EX-L, TrailSport and Sport-L; power tailgate with hands-free access on Sport Touring;
cargo volume behind the second row 39.3 cu ft gas, 36.3 cu ft hybrid, 34.7 cu ft Sport Touring; height 66.2 in 2WD and
66.5 in AWD), Honda's 2023 CR-V Specifications & Features (LX, EX, EX-L gas; Sport and Sport Touring hybrid; 1,500 lb
petrol and 1,000 lb hybrid; black roof rails on Sport and Sport Touring only; power tailgate on EX-L; hands-free on
Sport Touring; same heights), Honda's 20 May 2025 release on the 2026 lineup (four hybrid trims and three turbo trims,
TrailSport Hybrid new with standard all-wheel drive, all-terrain tires and a power tailgate, 9-inch touchscreen
standard across the lineup), Honda's current spec page (now titled 2027 Honda CR-V; towing 1,500 and 1,000 lb),
Wikipedia's Honda CR-V page (unveiled 12 July 2022, U.S. sales from September 2022 as a 2023 model, Honda Architecture
platform of the eleventh-generation Civic), Bernardi Parts' page for Honda hitch 08L92-3A0-100 (Class I, trailers up
to 1,500 lb, draw bar, pin and clip included, harness 08L91-3A0-100 and ball separate, hands-free tailgate sensor
adapter, 2023-2026 models, no receiver size and no tongue weight) and Bernardi Parts' page for Honda roof rails
08L02-3A0-100 ("165 pounds total capacity", 2023-2027 models, list $435, crossbars 08L04-3A0-100 sold separately).
The Honda tables were read through a text extraction, so trim-level rows are worded "as we read".
The stored hitch_class value in the vehicle data (2) is not printed on this page; the dealer's Class I wording is used.
Not verified, and worded as such wherever the text touches them: roof rails on 2024 and 2025 hybrids (only the 2023 and 2026 tables were
read); the profile of the factory rails and whether flush-rail kits fit them; any roof load figure for the bare roof or
for the factory rails (the 165 lb figure is printed for Honda's accessory rails only); whether any crossbars are
factory equipment; the receiver size of Honda's accessory hitch; the CR-V's own tongue weight limit; whether any CR-V
ships with a receiver; Draw-Tite 76342 ratings; hybrid fit and ratings of the AutoBeeDen and 13397-style hitches; which
trims have the two-position cargo floor board and how the hybrid cargo floor differs; the bar spread and bar weight of
every clamp kit; clamp kit prices for 2024-2026 cars (etrailer's figures are for the 2023 CR-V); prices of rail-mount
crossbar kits; the Vista XL's weight; crossbar spread for the Pulse 2 M and Wedge Plus; Honda's tow figures for 2024
and 2025 from a Honda table; and 2027 fit of any part. No CR-V guide exists for roof racks, running boards, bike racks
or lighting; none are ranked.
Source fixes 2026-10-04 (round 2): the TrailSport FAQ no longer says the floor liner guide calls the cabin floor shared; it now matches that guide's wording (listings split by model year and powertrain, not by trim). The stored hitch_class is now 3 with a 2 in receiver, which describes the aftermarket hitches as this page already words them; the dealer's Class I wording is still used for Honda's hitch.
"""

KIND = "upgrades"
KEY = ("honda", "cr-v", "2023-present")
CATEGORIES = ["floor-mats", "hitches", "cargo-boxes"]

TITLE = "2023–2026 Honda CR-V Upgrades, Ranked: 3 Mods in Order, With Gas vs Hybrid and Roof Fit Traps"
META = ("Three 2023–2026 CR-V upgrades in buying order: floor liners, trailer hitch and cargo box, with gas vs hybrid "
        "fit, roof rails, crossbars and tow limits.")

FAQ = [
 ("What should I upgrade first on a 2023–2026 Honda CR-V?",
  "Floor liners, then a trailer hitch, then a cargo box. Liners cost the least, about $80–$240 across the sets in "
  "the floor liner guide, and the fit check is short: a 2023 or later listing, plus the cargo deck position for a cargo liner. A hitch is second at about $120–$300 from the aftermarket, and it "
  "carries bikes or a cargo tray without any roof hardware. The cargo box is last because it costs the most and "
  "needs crossbars first."),
 ("Does the 2023–2026 CR-V have roof rails, and on which trims?",
  "It depends on the powertrain. Honda's 2023 and 2026 specifications list black "
  "roof rails as standard on the hybrid trims and not on the gas LX, EX and EX-L. We read those two model years "
  "only, so look at your roof. etrailer's fit guide splits the 2023 CR-V into two roofs: no rails, and flush rails that run front to back. Honda sells its "
  "crossbars separately, so plan to buy bars either way."),
 ("How much can a 2023–2026 CR-V tow, and does an aftermarket hitch raise it?",
  "A hitch never raises it. Honda's 2023 and 2026 specifications list 1,500 lb for the gas LX, EX and EX-L and "
  "1,000 lb for every hybrid trim, and Honda's current spec page shows the same two figures. CURT's 13397 is rated "
  "at 3,500 lb and etrailer lists a B&W hitch at 4,500 lb, but the lower number always applies. We did not read a Honda table for 2024 or 2025, so your owner's manual is the authority."),
 ("Can a CR-V Hybrid carry bikes on a hitch rack?",
  "Yes, within a limit you have to look up. A bike rack loads the hitch as tongue weight, not trailer weight. CURT "
  "rates its 13397 at 525 lb of tongue weight, but that is the hitch's figure. The Honda pages we read give no "
  "tongue weight for the CR-V itself, so read your owner's manual and count the rack's own weight along with the bikes. Buy a 2 in receiver for the widest choice of racks. CURT also says the 13397 is not "
  "for vertical-hanging bike racks."),
 ("How much weight can a 2023–2026 CR-V roof carry with a cargo box?",
  "The one published figure the guides found is for Honda's accessory roof rails, which a Honda parts dealer lists at 165 lb total capacity. That total covers crossbars, box and gear. For a bare roof with a clamp kit, the "
  "cargo box guide says to use the lower of your owner's manual figure and the kit's rating. We could not confirm a figure for the black roof rails on hybrid trims. A 330 lb claim on a crossbar "
  "listing describes the bar, not the roof."),
 ("What crossbars does a CR-V need for a cargo box, and what do they cost?",
  "It depends on the roof. For a bare roof, the cargo box guide quotes etrailer's prices for three door-frame clamp "
  "kits on the 2023 CR-V: about $468 for a steel INNO Square Bar kit, about $695 for Yakima's BaseLine with "
  "JetStream bars and about $705 for Thule's WingBar Evo. Wonderdriver's budget bars name the 2023–2026 EX, LX and "
  "EX-L, and their price is on the listing. A CR-V with rails takes a flush-rail kit or Honda's own crossbars. These are pointers, not ranked picks."),
 ("Do 2017–2022 CR-V parts fit a 2023–2026 CR-V?",
  "Floor liners and roof racks don't. The 2023 CR-V is a new generation, and Wikipedia says it is based on the platform of the eleventh-generation Civic. Husky sells 99401 for 2017–2022 and 99411 for the current car. "
  "Hitches are the exception: CURT lists the 13397 for 2017–2026, and Draw-Tite's 76342 listing names the same "
  "years. A cargo box also carries over, because it clamps to crossbars and not to the car."),
 ("Does the 2026 CR-V TrailSport need different parts?",
  "Treat it as a hybrid with all-wheel drive. Honda's May 2025 release describes the TrailSport Hybrid as a new "
  "2026 trim with the two-motor hybrid system, standard all-wheel drive and a power tailgate. Honda's 2026 table "
  "lists it at 1,000 lb of towing, with black roof rails. The listings in the floor liner guide split by model year and powertrain, not by trim, so "
  "match gas or hybrid for the cargo liner. Some listings stop at "
  "2025, including AutoBeeDen's hitch and Autocessking's liners, so confirm 2026 with the seller."),
 ("Will a trailer hitch stop the CR-V's hands-free tailgate from working?",
  "It can. The kick sensor sits under the rear bumper, next to where a hitch mounts. The Amazon title for CURT's "
  "13397 warns that it may affect the hands-free liftgate. An etrailer expert says Draw-Tite's hitch keeps the "
  "feature working on a 2025 CR-V, and Honda lists a sensor adapter for its own accessory hitch. As we read Honda's "
  "2023 and 2026 specifications, the hands-free power tailgate is a Sport Touring feature. If yours opens with a kick, ask the seller before ordering."),
 ("How much does it cost to add all three upgrades to a CR-V?",
  "From the prices in the three guides, a budget build on a bare-roof gas CR-V runs about $1,118–$1,218: HAFIDI's "
  "cabin liners, AutoBeeDen's hitch, an INNO steel clamp kit and SportRack's Vista XL. A mid build runs about "
  "$1,675–$1,775 with Weize's floor and cargo set, CURT's 13397, Yakima's clamp kit and Thule's Pulse 2 M. A premium "
  "build with Husky's 99411, Draw-Tite's 76342, Thule's clamp kit and INNO's Wedge Plus runs about $1,923–$2,043. "
  "Crossbars make up about $468–$705 of each total, and trailer wiring is extra. Liners plus a hitch alone come to about $200–$300 on a budget."),
]

ARTICLE = {
 "dek": "Three upgrades for the sixth-generation CR-V, in buying order. Fit on this compact SUV turns on a short "
        "list of facts: a 2023 redesign that left older liners and racks behind, gas or hybrid, a roof that is bare "
        "on gas trims in Honda's tables, and a tow rating of 1,500 or 1,000 lb.",
 "author": "jake-morrison",
 "reviewed": "2026-10-04",
 "method": "We did not install any of these parts ourselves. The order comes from the three fit-checked 2023–2026 "
           "CR-V guides on this site, weighing how many CR-Vs each upgrade suits, what it costs, what it depends on and how much can go wrong with fit. Price bands are "
           "the prices on those guides' picks and the retailer prices the guides quote, checked in September 2026, "
           "and are approximate. Vehicle facts come from this site's vehicle data, the guides' sources, Honda's 2023 "
           "and 2026 specification tables, Honda's May 2025 release, two Honda dealer parts pages and Wikipedia. "
           "The Honda tables reached us as extracted text, so trim-level details carry an \"as we read\" note. "
           "Where we couldn't confirm a factory detail, the text says so.",
 "takeaways": [
  "**Buy 2023+ liners and racks.** Husky sells 99401 for 2017–2022 and 99411 for the current CR-V. Hitches are the exception: CURT lists the 13397 for 2017–2026.",
  "**Read the badge.** LX, EX and EX-L are gas; Sport, Sport-L, TrailSport and Sport Touring are hybrids. Honda rates the gas trims at 1,500 lb and the hybrids at 1,000 lb.",
  "**Look at the roof before any box.** Honda's 2023 and 2026 tables list black roof rails on hybrid trims only. A bare roof needs a door-frame clamp kit.",
  "**Plan the roof around 165 lb.** That is the total printed for Honda's accessory rails, and crossbars, box and gear all count against it.",
  "**Buy the hitch for racks, not ratings.** A 2 in Class 3 receiver takes most bike racks and cargo trays, and Honda's tow figure still applies.",
 ],
 "priority": [
  {"category": "floor-mats",
   "h": "1. Floor liners first: the lowest price, with one look at the cargo floor",
   "why": "Floor liners lead on the CR-V because they cost the least, every drive uses them and no other part on "
          "this page depends on them. The 2023 CR-V is a new generation with a new floor, and "
          "Husky's catalog shows the split: 99401 for 2017–2022 and 99411 for the current car. The cabin is the easy "
          "half, since most sets in the floor liner guide name both gas and hybrid. The cargo area is the harder "
          "half. Many CR-Vs have a cargo floor board that sits in an upper or a lower position, and a cargo liner "
          "is cut for one of them. Weize's, TTX's and Husky's 24411 cargo liners are cut for the upper position, "
          "and Autocessking's kit is listed for the hybrid only. Prices in the guide run about $80–$120 for "
          "HAFIDI's cabin set, about $110–$150 for Weize's floor and cargo set, about $130–$180 for Husky's "
          "WeatherBeater 99411 and about $180–$240 for Husky's 4-piece bundle with cargo. Husky says WeatherBeater "
          "is made in the USA with a lifetime warranty against cracks and breaks; the TPE sets publish no warranty "
          "terms the guide could check. One trap: the 99411 listing names 2024–2026, so a 2023 owner should order "
          "the bundle or Husky's separate pieces.",
   "skip_if": "You already have raised-edge liners cut for the 2023 or later floor."},
  {"category": "hitches",
   "h": "2. Trailer hitch second: a carrying point for every CR-V, capped at 1,500 or 1,000 lb",
   "why": "A trailer hitch ranks second because every CR-V can use one and it adds a carrying point without "
          "touching the roof. On this SUV the hitch is mostly for a bike rack or a cargo tray. Honda rates the gas "
          "trims at 1,500 lb and the hybrid trims at 1,000 lb, and no hitch raises either figure. Three facts "
          "decide the purchase. First, powertrain: an etrailer expert says CURT's 13397 fits every CR-V, hybrids "
          "included, while Amazon's listing for Draw-Tite's older 76128 says Except Hybrid. Second, receiver size: "
          "every aftermarket hitch in the hitch guide is a Class 3 with a 2 in receiver, the size most bike racks "
          "and carriers use, while a Honda parts dealer describes Honda's accessory hitch as Class I. Third, the "
          "tailgate: CURT's listing warns the hitch may affect the hands-free liftgate. Prices in the guide run "
          "about $120–$180 for AutoBeeDen's hitch, about $170–$230 for CURT's 13397, about $200–$270 for "
          "Draw-Tite's 76342 and about $220–$300 for CURT's kit with a 4-way harness. Honda's hitch lists at about "
          "$412 before the harness and ball. The trade-off is the install: CURT says the fascia must be trimmed "
          "and the exhaust lowered temporarily.",
   "skip_if": "A receiver is already under the rear bumper, as it may be on a used CR-V with the dealer-fitted Honda hitch."},
  {"category": "cargo-boxes",
   "h": "3. Cargo box last: the costliest step, and it can't go on without crossbars",
   "why": "The cargo box comes last because it costs the most, gets used on the fewest days and can't go on until "
          "crossbars are fitted. Honda's 2023 and 2026 specifications list black roof rails on the hybrid trims "
          "only, and the vehicle data on this site follows them. "
          "So a gas CR-V needs a door-frame clamp kit, and a CR-V with rails needs bars made for them. The "
          "cargo box guide quotes etrailer prices of about $468 to $705 for brand-name clamp kits on the bare-roof "
          "2023 CR-V, which can cost as much as the box. Three numbers then pick the box: length, because the "
          "liftgate swings up behind a short roof; weight, because bars, box and gear share one roof figure; and "
          "crossbar spread, because a clamp kit fixes it. Prices run about $450 for SportRack's Vista XL, 63 in "
          "long; about $599 on sale for Yakima's SkyBox 16 Carbonite, 81 in and 47 lb; about $700 for Thule's "
          "Pulse 2 M, 68.9 in and 31 lb; and about $888 for INNO's Wedge Plus, 13-3/4 in tall. The trade-off is "
          "drag: the guide notes lower mpg with any box.",
   "skip_if": "Your heavy items are coolers and bins, which the cargo box guide sends to a hitch carrier."},
 ],
 "tier_table": {
  "caption": "Approximate price bands from the 2023–2026 CR-V guides (September 2026; Amazon prices move daily). Totals are for a gas trim with a bare roof; the guides give no price for rail-mount crossbars",
  "head": ["Upgrade", "Budget", "Mid", "Premium"],
  "rows": [
   ["Floor liners", "About $80–$120 (HAFIDI cabin TPE)", "About $110–$150 (Weize floor set with an upper-deck cargo liner)", "About $130–$180 (Husky WeatherBeater 99411, titled 2024–2026)"],
   ["Trailer hitch", "About $120–$180 (AutoBeeDen Class 3, 2 in; titled 2017–2025, hybrid fit not stated)", "About $170–$230 (CURT 13397, 2 in, 3,500 lb / 525 lb)", "About $200–$270 (Draw-Tite 76342, 2 in; confirm ratings on the listing)"],
   ["Crossbars for the box (a cost line, not a ranked upgrade)", "About $468 (INNO Square Bar steel clamp kit, etrailer price for the 2023 CR-V)", "About $695 (Yakima BaseLine with JetStream bars, etrailer price)", "About $705 (Thule WingBar Evo clamp kit, etrailer price)"],
   ["Cargo box", "About $450 (SportRack Vista XL, 18 cu ft, 63 in; three fixed mounting positions)", "About $700 (Thule Pulse 2 M, 14 cu ft, 68.9 in, 31 lb)", "About $888 (INNO Wedge Plus, 13 cu ft, 13-3/4 in tall)"],
   ["Total", "About $1,118–$1,218", "About $1,675–$1,775", "About $1,923–$2,043; trailer wiring extra in every column"],
  ],
 },
 "sections": [
  {"h": "Gas or hybrid: the badge sets the tow rating, the roof and the cargo floor",
   "body": "Honda sells the sixth-generation CR-V with two powertrains, and the trim name tells you which one you "
           "have. Honda's 2026 specifications list the LX, EX and EX-L with a 1.5-liter turbo engine of 190 hp, and "
           "the Sport, TrailSport, Sport-L and Sport Touring with a 2.0-liter two-motor hybrid system of 204 hp in "
           "total. The 2023 table lists the LX, EX and EX-L as gas and the Sport and Sport Touring as hybrids. The "
           "TrailSport Hybrid is new for 2026, per Honda's May 2025 release.\n\n"
           "**Tow rating and roof.** Both tables give 1,500 lb for the gas trims and 1,000 lb for the hybrids, and "
           "both list black roof rails on the hybrid trims only. We read two model years, and the tables reached "
           "us as extracted text, so trust your eyes over the table.\n\n"
           "**Cargo floor.** The floor liner guide warns that the hybrid's cargo floor can differ from the gas "
           "car's. Honda's 2026 table points the same way, with less cargo volume behind the second row on hybrid "
           "trims. Match the powertrain on any cargo liner, and check whether the floor board sits in the upper or "
           "lower position.",
   "table": {"caption": "2023–2026 CR-V by trim group (Honda's 2023 and 2026 specifications, as we read them)",
             "head": ["Trims", "Powertrain", "Honda tow rating", "Roof in Honda's tables", "Cargo behind the second row (2026 table)", "Fit note"],
             "rows": [
              ["LX, EX, EX-L", "1.5 L turbo gas, 190 hp", "1,500 lb", "No roof rails listed", "39.3 cu ft", "Wonderdriver's bare-roof crossbars name these trims"],
              ["Sport, Sport-L", "2.0 L hybrid, 204 hp total", "1,000 lb", "Black roof rails", "36.3 cu ft", "Buy a hitch that names the hybrid"],
              ["TrailSport (new for 2026)", "2.0 L hybrid, all-wheel drive standard", "1,000 lb", "Black roof rails", "36.3 cu ft", "Confirm 2026 on listings that stop at 2025"],
              ["Sport Touring", "2.0 L hybrid, 204 hp total", "1,000 lb", "Black roof rails", "34.7 cu ft", "Hands-free power tailgate; see the hitch section"],
             ]}},
  {"h": "The roof: no roof rack guide here, so this is what to know about crossbars",
   "body": "There is no roof rack guide for the 2023–2026 CR-V on this site, so this page ranks no crossbars. A cargo box still needs them, so here is what the sources say.\n\n"
           "**What is overhead.** The vehicle data on this site lists a bare roof on gas trims and black roof rails on hybrids. etrailer's "
           "fit guide splits the 2023 CR-V into two roofs: no rails, and flush rails that run front to back. "
           "Honda's 2023 and 2026 specifications list black roof rails on the hybrid trims and not on the LX, EX or "
           "EX-L. The listings in the guide line up with that: Wonderdriver's bare-roof bars name the EX, LX and "
           "EX-L, and the ANTS PART bars in the guide's product list, titled for the CR-V and CR-V Sport Hybrid, need roof rails. We could not confirm the profile of the factory rails, or that every hybrid of every year has "
           "them.\n\n"
           "**Bare roof.** The route is a kit whose feet clamp into the door openings, with a fit kit listed for "
           "the 2023 or later CR-V. The clamp points are fixed, so the kit sets the distance between the bars.\n\n"
           "**Rails.** A CR-V with rails takes a flush-rail kit; the guide names Yakima's SightLine without a "
           "price. Honda's accessory rails, 08L02-3A0-100, list at about $435 at one Honda parts dealer, and bars "
           "on rails can slide to suit a box.\n\n"
           "Racks for the 2017–2022 CR-V don't fit.",
   "table": {"caption": "2023–2026 CR-V roofs and the crossbars each takes (prices are the etrailer and dealer figures quoted in the cargo box guide)",
             "head": ["Roof", "Where it is found", "Crossbars", "Price in the guide"],
             "rows": [
              ["Bare roof", "LX, EX and EX-L in Honda's 2023 and 2026 tables", "Door-frame clamp kit: INNO Square Bar (steel), Yakima BaseLine with JetStream bars or Thule WingBar Evo", "About $468, $695 and $705 at etrailer for the 2023 CR-V"],
              ["Bare roof, budget route", "Same trims", "Wonderdriver lockable aluminum bars", "On the listing; spread and bar weight not published"],
              ["Black roof rails", "Hybrid trims in Honda's 2023 and 2026 tables", "A flush-rail kit, the ANTS PART bars or Honda crossbars 08L04-3A0-100; confirm the rail profile in a fit guide", "No price in the guides"],
             ]}},
  {"h": "165 lb, box weight and length: the roof math before a cargo box",
   "body": "**The figure.** A Honda parts dealer lists the accessory roof rails at 165 lb total capacity. The "
           "total covers everything above the rails: crossbars, box and gear. For a bare roof with a clamp kit, the "
           "cargo box guide says to use the lower of your owner's manual figure and the kit's rating. The vehicle "
           "data on this site stores no roof load figure for this CR-V, and we could not confirm one for the black "
           "roof rails on hybrid trims.\n\n"
           "Starting from 165 lb, the makers' box weights leave this much before the crossbars' own weight comes "
           "off:\n\n"
           "- **Thule Pulse 2 M, 31 lb:** 134 lb.\n"
           "- **Rhino-Rack MasterFit 440L, 38.6 lb:** 126.4 lb.\n"
           "- **INNO Wedge Plus, 44 lb:** 121 lb, but etrailer lists a 110 lb cargo limit for the box.\n"
           "- **Yakima SkyBox 16 Carbonite, 47 lb:** 118 lb.\n"
           "- **SportRack Vista XL:** weight not published.\n\n"
           "The guide's working figure after a set of bars is roughly 100 to 120 lb, which suits soft bags and skis, not a full cooler.\n\n"
           "**Length.** The liftgate swings up behind a short roof. The boxes run from 63 in for the Vista XL and "
           "68.9 in for the Pulse 2 M to 80 in for the Wedge Plus and 81 in for the SkyBox 16. Mount any box "
           "forward and open the liftgate slowly the first time.\n\n"
           "**Spread.** A clamp kit fixes it. Rhino-Rack gives about 24.4 to 36.6 in for the MasterFit 440L and "
           "Yakima gives 24–34.5 in for the SkyBox 16. The Vista XL mounts only at 25-7/8, 27-7/8 or 29-7/8 in."},
  {"h": "Towing and the hitch: 1,500 or 1,000 lb, receiver size and tongue weight",
   "body": "**The rating.** Honda lists 1,500 lb for the LX, EX and EX-L and 1,000 lb for the hybrid trims. The hitch guide puts that in terms of a small utility trailer, a jet ski or a teardrop camper.\n\n"
           "**The receiver.** Honda sells its hitch as an accessory, 08L92-3A0-100. A Honda parts dealer describes "
           "it as a Class I hitch for trailers up to 1,500 lb. The dealer "
           "page doesn't state the receiver size, and the hitch "
           "guide notes that Class I receivers are normally 1-1/4 in. Every aftermarket hitch in the guide is a "
           "Class 3 with a 2 in receiver, which gives the wider choice of racks. We could not confirm that any "
           "CR-V leaves the factory with a receiver, so look under the rear bumper of a used one.\n\n"
           "**Tongue weight.** This is the number that limits a rack or a carrier. CURT rates the 13397 at 525 lb, "
           "but the Honda pages we read give no tongue weight for the CR-V itself. Read your owner's manual, and "
           "count the rack's own weight.\n\n"
           "**The install.** CURT says the 13397 needs the fascia trimmed and the exhaust lowered temporarily, and "
           "etrailer rates the job 6 out of 10. An etrailer expert says the Draw-Tite needs only the lower fascia "
           "trimmed, and that it keeps the hands-free tailgate working on a 2025 CR-V.\n\n"
           "**Wiring.** A bike rack needs none. A trailer needs a 4-way flat harness and a ball mount. Honda's "
           "harness is 08L91-3A0-100, and an etrailer expert suggests CURT's 56370 for all-wheel-drive CR-Vs."},
  {"h": "Model years, what isn't ranked and the order to fit things",
   "body": "**2023.** Wikipedia says the sixth generation went on sale in the U.S. in September 2022 as a 2023 "
           "model. Liners and roof racks for the 2017–2022 CR-V don't fit it. Hitches cross the line, since CURT "
           "lists the 13397 for 2017–2026.\n\n"
           "**Inside the generation.** Year ranges vary by part. Husky's 99411 set names 2024–2026, its 4-piece "
           "bundle 2023–2024 and its 24411 cargo liner 2023–2025. Sunsdrew's and Autocessking's liners and "
           "AutoBeeDen's hitch stop at 2025.\n\n"
           "**2026.** Honda's May 2025 release adds the TrailSport Hybrid. etrailer says the 2026 changes around "
           "the hitch area are cosmetic, so hitches that fit a 2025 carry over.\n\n"
           "**2027.** Honda's site now shows a 2027 CR-V with the same 1,500 and 1,000 lb tow figures. The guides "
           "checked 2023–2026, and we have not checked 2027 fit for any part.\n\n"
           "This page ranks the three categories that have a fit-checked CR-V guide on this site. Roof racks, "
           "running boards, bike racks and lighting have none, so they aren't ranked.\n\n"
           "Fit the three in the ranked order. Liners need no tools, the hitch means trimming the lower fascia, "
           "and crossbars go on before the box."},
 ],
 "avoid": [
  {"h": "2017–2022 liners or racks on a 2023 or later CR-V", "body": "The 2023 CR-V has a new floor. Husky's 99401 is the old part and 99411 the new one, and the vehicle data on this site flags that older mats and racks do not fit."},
  {"h": "Ordering crossbars before looking at the roof", "body": "A door-frame clamp kit is for a bare roof, and a flush-rail kit is for rails. Honda's 2023 and 2026 tables list black roof rails on hybrid trims only, so read the listing against your own roof."},
  {"h": "Loading or towing to the part's rating", "body": "A 330 lb crossbar claim doesn't change the 165 lb printed for Honda's accessory rails, and a 3,500 lb hitch doesn't change Honda's 1,500 lb gas or 1,000 lb hybrid limit. The lower number wins."},
  {"h": "Gas-only or wrong-deck parts on a hybrid", "body": "Amazon's listing for Draw-Tite's 76128 hitch says Except Hybrid. Cargo liners are cut for the upper or the lower deck position, and Autocessking's kit is for the hybrid."},
 ],
 "verdict": {
  "thesis": "On the 2023–2026 CR-V, buy floor liners by model year and cargo deck first, add a 2 in trailer hitch that names your powertrain second, and leave the cargo box for last, after crossbars that match your roof.",
  "body": "The sixth-generation CR-V is easy to accessorize once four facts are written down: model year, gas or "
          "hybrid, what is on the roof and where the cargo floor board sits. Floor liners need the year and, for a "
          "cargo liner, the deck position and the powertrain. They cost about $80–$240 in the guide, so they go first. A trailer hitch needs the powertrain and a look at the tailgate. It costs about $120–$300 from the aftermarket and gives every CR-V a place for bikes or a cargo tray.\n\n"
          "The cargo box is last because the roof takes the most planning. Crossbars come first, and on a "
          "bare-roof gas trim a brand-name clamp kit runs about $468 to $705 at etrailer. This site has no roof "
          "rack guide for the CR-V yet, so confirm the kit in the maker's fit guide. Then choose the box by length, "
          "weight and spread, and plan the load around the 165 lb printed for Honda's accessory rails or the figure "
          "in your owner's manual.",
 },
 "sources": [
  ["2026 Honda CR-V Specifications & Features: trims, towing, roof rails, tailgate, cargo volume (Honda Newsroom)", "https://hondanews.com/en-US/honda-automobiles/releases/release-2ecca7d29f72bf212c56033cca000993-2026-honda-cr-v-specifications-features-updated"],
  ["2023 Honda CR-V Specifications & Features: trims, towing, roof rails, tailgate (Honda Newsroom)", "https://hondanews.com/en-US/honda-automobiles/releases/release-74895511bca6e7abc42504d7581990ac-2023-honda-cr-v-specifications-features"],
  ["2026 CR-V lineup and TrailSport Hybrid release, 20 May 2025 (Honda Newsroom)", "https://hondanews.com/en-US/honda-automobiles/releases/release-0d29cf91ab5515b985a1c286910cc6fb-rugged-electrified-and-refreshed-best-selling-honda-cr-v-gains-new-trailsport-hybrid-trim-and-more-standard-tech-as-2026-lineup-arriving-in-dealers-now"],
  ["CR-V specs and towing by trim, now showing the 2027 model (Honda)", "https://automobiles.honda.com/cr-v/specs-features-trim-comparison"],
  ["Honda CR-V, sixth generation (Wikipedia)", "https://en.wikipedia.org/wiki/Honda_CR-V"],
  ["Honda Trailer Hitch 08L92-3A0-100: Class I, 1,500 lb, harness and adapter (Bernardi Parts)", "https://www.bernardiparts.com/Products/Honda-Trailer-Hitch-(CRV-2023-2025)__08L92-3A0-100.aspx"],
  ["Honda CR-V accessory roof rails 08L02-3A0-100, 165 lb total (Bernardi Parts)", "https://www.bernardiparts.com/Products/Honda-Roof-Rails-(CRV-2023-2026)__08L02-3A0-100.aspx"],
  ["2023 Honda CR-V roof types and crossbar kits (etrailer)", "https://www.etrailer.com/roof-2023_honda_cr-v.htm"],
  ["CURT 13397 Class 3 hitch, CR-V (CURT)", "https://www.curtmfg.com/part/13397"],
  ["Recommended hitch for a 2023 CR-V Hybrid (etrailer Q&A)", "https://www.etrailer.com/question-695796.html"],
  ["Draw-Tite on a 2025 CR-V: bumper trimming (etrailer Q&A)", "https://www.etrailer.com/question-791484.html"],
  ["Hitch for a 2026 CR-V Hybrid (etrailer Q&A)", "https://www.etrailer.com/question-836313.html"],
  ["Husky Liners: WeatherBeater vs X-act Contour (Husky Liners)", "https://huskyliners.com/blog/husky-liners-weatherbeater-vs-xact-contour/"],
  ["Thule Pulse 2 M (Thule)", "https://www.thule.com/en-us/cargo-carrier/car-top-carrier/thule-pulse-2-m-_-610250"],
  ["SportRack Vista XL mounting positions (etrailer)", "https://www.etrailer.com/question-156482.html"],
 ],
}
