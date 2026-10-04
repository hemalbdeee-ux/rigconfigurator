"""Upgrades pillar: 2017–2026 Tesla Model 3 (1st gen, incl. the 2024 "Highland" refresh; an electric sedan, no bed).
Hub page: ranks the four published Model 3 category guides and links to them. No product picks or ASINs here
(the site pulls each guide's #1 pick). Every price band comes from the linked guides' picks[].price fields or, where
noted as "product list", their FITS bands; vehicle facts from db/migrations/003_vehicles.sql (EV, roof type
fixed-points, NO stored roof load and a "verify roof load" flag, hitch class 'none', no receiver, no tow rating,
glass roof with fixed points, highland_2024; and the Model Y row: 165 lb roof figure, 3,500 lb with Tesla's package),
the four guides and their sources, and nine pages opened for this page on 2026-10-04:
Tesla's current Model 3 owner's manual, Towing and Accessories ("The towing package allows you to tow a trailer or
carry an accessory"; 1,650 lb without trailer brakes, 2,200 lb with; tongue weight 200 lb; 2 x 2 in receiver
"designed to support vertical loads of up to 121 lbs (55 kg)"; "Do not attempt to install an accessory carrier on
Model 3 that is not equipped with the towing package. Doing so can cause significant damage."; "Damage caused by
non-Tesla approved accessories is not covered by the warranty."; "Trailer Mode must always be active when towing a
trailer"; 42 psi; range "can decrease significantly");
the same manual's Vehicle Loading page ("Do not use Model 3 for towing purposes. Model 3 does not currently support
towing."; "Using Model 3 for towing without Tesla-approved towing components and accessories may void the
warranty."; "Model 3 supports the use of Tesla-approved roof racks using a Tesla mounting accessory"; "only roof
rack systems that have been approved by Tesla"; no roof load figure);
the 2017–2023 Model 3 owner's manual: contents page (no towing topic), Vehicle Loading (same towing warning and
roof rack wording) and Parts and Accessories ("Any damage caused by using or installing non-approved parts, or by
performing non-approved modifications, is not covered by the warranty.");
the Tesla Shop Model 3 Tow Package page ($1,300; steel tow bar with 2 in receiver and North America 4-pin connector,
trailer harness, tow mode software; "capable of towing up to 2,200 lbs on all wheel and rear wheel drive";
"Compatible with Model 3 Rear-Wheel Drive and All-Wheel Drive vehicles produced in 2024+. Not compatible with
Model 3 Performance vehicles."; Service Center installation included; ball mounts not included; out of stock);
the Tesla Shop Model 3 Roof Rack page ($400, load rating 150 lb, static load limit 495 lb, aluminum T-slot bars,
die-cast towers with integrated locks, "Compatible with all Model 3 vehicles", out of stock);
Wikipedia's Tesla Model 3 page (refresh announced September 1, 2023; North American orders January 10, 2024; no
stalks, 8 in rear touchscreen, tail lights without the vertical break; glass roof on all trims; Cd 0.219, not used on the page);
and fueleconomy.gov's driving-habits page (rooftop box 2–8% city, 6–17% highway, 10–25% at 65–75 mph; rear-mount
boxes or trays 1–2% city, 1–5% highway; gas vehicles).
Not verified, and worded as such in the text: any range, efficiency or noise figure for a rack or box on a Model 3
(Tesla publishes none; the fueleconomy.gov figures are for gas vehicles); a roof load limit from Tesla's manual
(none printed; 150 lb is the Tesla Shop's rating for Tesla's own rack, and the vehicle data stores no figure);
whether Tesla approves any aftermarket roof bars; the crossbar spread on aftermarket or Highland bars (28 in is
etrailer's figure for the factory rack, cited from the guides, page not reopened); how Tesla service treats a car
with an aftermarket hitch, and whether the 121 lb carrier figure applies to a receiver Tesla did not fit; published
ratings for the TIOYAR and maXpeedingrods hitches; the 42 psi towing pressure (read once through a text
extraction, so the page says "as we read it"); which connector Tesla's package has (the Tesla Shop says 4-pin; one
extraction of the manual page mentioned a 7-pin connector, so the page cites the Tesla Shop only); what the
"Model 3 Standard" that TESEVO excludes is; Highland Performance trunk trim for liners; floor liner sets for
2017–2023 cars (the floor mat guide prices Highland sets only); the spread range of the Thule Pulse 2 M and
Force 3 L; the SportRack Vista XL's weight. All Tesla manual quotes were read through a text extraction of the
page, not copied from the rendered page. No Model 3 guide exists for bike racks, seat covers or dash cams; none
are ranked.
Source fixes 2026-10-04: aligned with the corrected guides and the proposed vehicle-data row (no hitch class, tow and roof figures carried as Tesla Tow Package and Tesla Shop rack facts): dropped the two statements about what the site's vehicle data stores for roof load; reworded how to tell a Highland (listings say 2024 or later; Wikipedia order date, rear touchscreen, stalk returned on US cars for 2026; door-jamb build date and the listing's fit notes); changed the Highland Performance liner cell to "fit not confirmed"; META "150 lb roof" became "150 lb rack".
Text fixes 2026-10-04 (round 2): dek and one takeaway no longer say the roof takes a rack at fixed points "only" (the roof rack guide documents a door-frame clip system from etrailer's listing); they now state the roof has fixed mounting points and no rails.
"""

KIND = "upgrades"
KEY = ("tesla", "model-3", "2017-present")
CATEGORIES = ["floor-mats", "roof-racks", "cargo-boxes", "hitches"]

TITLE = "2017–2026 Tesla Model 3 Upgrades, Ranked: 4 Mods in Order, With Highland and Glass-Roof Fit Traps"
META = ("Four 2017–2026 Model 3 upgrades in buying order: floor liners, roof rack, cargo box and trailer hitch, with "
        "Highland, 150 lb rack and Tesla tow package notes.")

FAQ = [
 ("What should I upgrade first on a 2017–2026 Tesla Model 3?",
  "Floor liners, then a roof rack. Liners cost the least, about $100–$230, and need one fact: 2017–2023 or Highland. "
  "The floor mat guide prices Highland sets only. "
  "A roof rack is second at about $130–$400, bolted to fixed points with no drilling. A cargo box is third, since it "
  "needs the bars. The trailer hitch is last: Tesla's Tow Package, about $1,300, covers only 2024 and later "
  "Rear-Wheel Drive and All-Wheel Drive cars, and Tesla's manual says not to fit a carrier without it."),
 ("How do I tell a 2017–2023 Model 3 from a 2024 Highland?",
  "Start with the model year on the registration. Every liner set the floor mat guide prices is listed for 2024 or later. "
  "Wikipedia says North American orders opened on January 10, 2024, and describes the refreshed car with an 8 in rear "
  "touchscreen and, at launch, no turn signal or gear selector stalks. It also says the turn signal stalk returned on "
  "US cars for the 2026 model year. Rack makers go by build: Tesstudio sells one rack "
  "for builds to October 2023 and another from November 2023, and TESEVO lists the Highland separately, so read "
  "the build date on the door-jamb label and the listing's fit notes."),
 ("Do 2017–2023 Model 3 accessories fit the 2024–2026 Highland?",
  "It depends on the category. Floor liners: no. Makers sell separate sets, and all five sets the floor mat guide "
  "prices are Highland only. Roof bars: Tesla says its own rack is compatible with all Model 3 vehicles, while "
  "Tesstudio and TESEVO sell separate Highland versions. Hitches: CURT lists its 13431, 13449 and 11581 for "
  "2017–2023 only, Stealth lists its SHR09001 for 2017–2025, and Tesla's Tow Package is for cars produced in 2024 "
  "or later."),
 ("How much weight can the Model 3's glass roof carry?",
  "Plan around 150 lb in total. That is the load rating the Tesla Shop gives for the Model 3 Roof Rack, with a "
  "495 lb static load limit. The Tesla manual pages "
  "we opened print no roof load, so 150 lb is the rack's rating, not a separate roof figure. It covers the bars, the "
  "carrier and the cargo. Aftermarket bars listed at 176 lb or 220 lb do not raise the limit."),
 ("Can a Tesla Model 3 tow a trailer in the US?",
  "Only some can, going by Tesla's documents. The Tesla Shop lists a Model 3 Tow Package for Rear-Wheel Drive and "
  "All-Wheel Drive cars produced in 2024 or later, not the Performance. With it, the owner's manual gives 1,650 lb "
  "without trailer brakes, 2,200 lb with them and 200 lb of tongue weight. The 2017–2023 manual says: \"Do not use "
  "Model 3 for towing purposes. Model 3 does not currently support towing.\" An aftermarket hitch rated at 2,000 lb "
  "or 3,500 lb changes neither statement, so ask Tesla first."),
 ("Can I put a hitch bike rack on a Model 3 that doesn't have Tesla's Tow Package?",
  "Aftermarket hitches are sold for that, at about $120–$600 in the hitch guide. Tesla's position is "
  "different. Its owner's manual says: \"Do not attempt to install an accessory carrier on Model 3 that is not "
  "equipped with the towing package. Doing so can cause significant damage.\" It adds that damage caused by "
  "non-Tesla approved accessories is not covered by the warranty. With the package, the receiver is designed for "
  "vertical loads of up to 121 lb. We could not confirm how Tesla service treats an "
  "aftermarket hitch, so ask a Service Center before buying one."),
 ("How much range does a roof rack or cargo box cost on a Model 3?",
  "Tesla doesn't publish a number. The only figures "
  "the guides cite are from fueleconomy.gov and describe gas vehicles: a large, blunt rooftop cargo box can reduce "
  "fuel economy by around 2–8% in city driving, 6–17% on the highway and 10–25% at 65–75 mph. We found no "
  "equivalent published figure for the Model 3, so use those numbers for direction only. A lower box helps: the "
  "INNO Wedge 660 is 11 in tall against 19 in for the SportRack Vista XL."),
 ("Do Model Y floor mats, roof racks or hitches fit the Model 3?",
  "No. The floor mat guide says the two share many parts, but the Model Y is taller, with a different floor, trunk "
  "and frunk shape. TESEVO and Tesstudio put both cars on one product page and sell them as separate versions, so "
  "choose the Model 3 option for your build. The roof figures differ too: the cargo box guide notes a 165 lb rating "
  "and a wider crossbar spread on the crossover, against 150 lb and about 28 in here. Tesla sells a separate Tow "
  "Package for each car."),
 ("How much does it cost to add all four upgrades to a Model 3?",
  "On the four guides' prices, a budget build on a 2024–2026 Highland runs about $820–$1,010: "
  "FemboMAX liners, WheelX bars, SportRack's Vista XL and TIOYAR's receiver. A mid build with SUPER LINER's kit, "
  "the same bars, a SkyBox 16 or Pulse 2 M and Stealth's hidden rack package runs about $1,329–$1,700. A premium "
  "build with 3D MAXpider mats, Tesla's rack, a Wedge 660 or Force 3 L and Tesla's Tow Package runs about "
  "$2,715–$2,810. The floor mat guide prices no 2017–2023 set, so there is no total for those cars. Ask Tesla "
  "before buying an aftermarket hitch."),
]

ARTICLE = {
 "dek": "Four upgrades for the first-generation Model 3, in the order most owners should buy them. On this sedan the "
        "order is shaped by a 2024 refresh that split liners, roof bars and hitches into separate parts, by a glass "
        "roof with fixed mounting points and bars about 28 in apart, and by what Tesla's own manual "
        "says about towing and hitch carriers.",
 "author": "jake-morrison",
 "reviewed": "2026-10-04",
 "method": "We did not install any of these parts ourselves. The order comes from the four fit-checked 2017–2026 "
           "Model 3 guides on this site, weighing how many Model 3s each upgrade suits, what it costs and what "
           "Tesla's own documents say about it. Price bands are the prices listed on those "
           "guides' picks, checked in September 2026, and are approximate. Vehicle facts come from the site's "
           "vehicle data, the guides' sources, Wikipedia's Model 3 page, Tesla's owner's manuals for the 2017–2023 "
           "and the current Model 3 and the Tesla Shop, opened on October 4, 2026. Efficiency figures are "
           "fueleconomy.gov's and describe gas vehicles. Where we couldn't confirm a detail, the text says so.",
 "takeaways": [
  "**Name the car before the part.** Makers split liners, roof bars and hitches at the 2024 Highland refresh.",
  "**The glass roof has fixed mounting points and no rails.** Tesla rates its Model 3 Roof Rack at 150 lb, which covers the bars, the carrier and the cargo.",
  "**Tesla's bars sit about 28 in apart.** A cargo box needs a spread range that includes 28 in, and a long box overhangs the trunk lid.",
  "**Tesla ties towing and carriers to its own package.** It lists one only for 2024 and later Rear-Wheel Drive and All-Wheel Drive cars, and its manual says not to fit a carrier without it.",
  "**Aftermarket hitches are sold anyway.** We could not confirm how Tesla service treats them, so ask Tesla before buying one.",
 ],
 "priority": [
  {"category": "floor-mats",
   "h": "1. Floor liners first: the lowest price on the page, once you know which Model 3 you have",
   "why": "Floor liners lead because they cost the least, need no tools and suit every Model 3. One fact decides fit: "
          "Highland or not. The floor mat guide says the 2024 refresh changed the interior and trunk trim enough "
          "that makers sell separate sets, and every set it prices is listed for 2024 and later cars. For a "
          "2017–2023 Model 3 it gives one instruction: buy a set that names those years. After generation, choose "
          "coverage across the footwells, rear floor, frunk, trunk floor, lower trunk well and seatbacks; kits run "
          "from six to eight pieces. Prices run about $100–$140 for FemboMAX's 6-piece set, "
          "about $130–$180 for SUPER LINER's 8-piece kit with seatback pieces and about "
          "$150–$230 for 3D MAXpider's Kagu cabin set. The trade-off is documentation against coverage: retailers "
          "describe the Kagu's three-layer construction, but its frunk liner is sold separately.",
   "skip_if": "The cabin, frunk and trunk stay dry and clean, and the factory carpet mats are enough for you."},
  {"category": "roof-racks",
   "h": "2. Roof rack second: no drilling, off in minutes, and rated at 150 lb",
   "why": "A roof rack ranks second because it adds the most carrying capacity for the money and comes off again. "
          "Racks bolt into fixed mounting points under the glass roof's "
          "trim, with no drilling, and the towers rest on the body, not the glass. Tesla's Model 3 Roof Rack, "
          "about $400, is the reference: Tesla says it is compatible with all Model 3 vehicles and rates it at "
          "150 lb, which covers bars, carrier and cargo. Aftermarket bars cost about $130–$220, and makers that "
          "publish fitment split them at the refresh. WheelX's lockable set, about $150–$220, is the one listing "
          "in the roof rack guide that spans 2017–2026. The trade-offs are drag, wind noise and a line in Tesla's "
          "manual, which says to use only roof rack systems approved by Tesla.",
   "skip_if": "Everything you carry fits in the trunk, the lower trunk well and the frunk."},
  {"category": "cargo-boxes",
   "h": "3. Cargo box third: it needs the bars, a range that includes 28 in, and a light shell",
   "why": "A cargo box ranks third because it can't be used without crossbars and costs more than any set of bars, "
          "about $450–$880 in the cargo box guide. It ranks ahead of the hitch because Tesla provides for it: the "
          "Tesla Shop says the rack's T-slots take cargo boxes. Spread: "
          "etrailer's experts give the factory rack about 28 in between bars, so the box's range must include it. "
          "The Yakima SkyBox 16 (about $599 on sale, 24–34.5 in) and the INNO Wedge 660 (about $865, 24–39 in) do. "
          "Weight: the box counts against Tesla's 150 lb, and the Thule Pulse 2 M, about $700, weighs 31 lb "
          "against 47 lb for the SkyBox 16. Length: a long box on bars 28 in apart overhangs the windshield and "
          "the trunk lid. The trade-off is drag, and Tesla publishes no figure for it on this car.",
   "skip_if": "You take one or two road trips a year and the luggage fits in the trunk and the frunk."},
  {"category": "hitches",
   "h": "4. Trailer hitch last: Tesla's package covers some 2024 and later cars, and its manual warns off the rest",
   "why": "A trailer hitch ranks last because it is the one upgrade here that Tesla's own documents restrict. The "
          "Tesla Shop lists a Model 3 Tow Package at about $1,300 installed, rated up to 2,200 lb, for Rear-Wheel "
          "Drive and All-Wheel Drive cars produced in 2024 or later. It is not compatible with the Performance. "
          "For every other Model 3, Tesla's manual says not to install an accessory carrier on a car that is not "
          "equipped with the towing package, and the 2017–2023 manual says the car does not support towing. "
          "Aftermarket hitches are sold anyway: about $120–$200 for TIOYAR's 2024–2026 receiver, about $300–$360 "
          "for CURT's 13431 for 2017–2023 cars and about $450–$600 for Stealth's hidden rack package, listed "
          "2017–2025. We could not confirm how Tesla service treats a "
          "car with one, so ask Tesla before you buy.",
   "skip_if": "Your bikes fit on the roof bars or inside the car, or you want to stay inside what Tesla's manual provides for."},
 ],
 "tier_table": {
  "caption": "Approximate price bands from the 2017–2026 Model 3 guides' picks (September 2026; Amazon prices move daily). Every column is a parts list for a Highland car, since the floor mat guide prices Highland sets only, and includes the crossbars its cargo box needs",
  "head": ["Upgrade", "Budget", "Mid", "Premium"],
  "rows": [
   ["Floor liners", "About $100–$140 (FemboMAX 6-piece, 2024–2026)", "About $130–$180 (SUPER LINER 8-piece, 2024–2026)", "About $150–$230 (3D MAXpider Kagu cabin set, 2024–2026)"],
   ["Roof rack", "About $150–$220 (WheelX lockable bars, listed 2017–2026)", "About $150–$220 (the same WheelX bars)", "About $400 (Tesla Model 3 Roof Rack; out of stock when checked)"],
   ["Cargo box", "About $450 (SportRack Vista XL)", "About $599 (Yakima SkyBox 16, sale price) to $700 (Thule Pulse 2 M)", "About $865 (INNO Wedge 660) to $880 (Thule Force 3 L)"],
   ["Trailer hitch", "About $120–$200 (TIOYAR, 2024–2026; ask Tesla first)", "About $450–$600 (Stealth hidden rack package, 2017–2025; ask Tesla first)", "About $1,300 (Tesla Tow Package, installed; not for the Performance)"],
   ["Total", "About $820–$1,010 on a 2024–2026 Highland", "About $1,329–$1,700 on a 2024–2025 Highland", "About $2,715–$2,810 on a 2024 or later Rear-Wheel Drive or All-Wheel Drive car"],
  ],
 },
 "sections": [
  {"h": "2017–2023 or Highland: identify the Model 3 before the part",
   "body": "One name covers two sets of parts. Tesla refreshed the Model 3, and listings call the refreshed car "
           "Highland and date it from 2024.\n\n"
           "**How to tell.** Start with the model year on the registration: every liner set the floor mat guide "
           "prices is listed for 2024 or later. Wikipedia says North American orders opened on January 10, "
           "2024, and describes the refreshed car with an 8 in touchscreen for rear passengers, tail lights with "
           "no vertical break between the trunk and the side and, at launch, no turn signal or gear selector "
           "stalks. It also says the turn signal stalk returned on US cars for the 2026 model year.\n\n"
           "**Why the build month matters.** Tesstudio sells one roof rack for builds to October 2023 and another "
           "from November 2023, and TESEVO lists builds to October 2023 and the Highland separately. The build "
           "month is on the door-jamb label, so go by that and the listing's fit notes. A title that "
           "ends at 2024 or 2025 without the word Highland could mean either body, so ask the seller which parts "
           "ship.\n\n"
           "**Performance and Standard.** Tesla says its Tow Package is not compatible with the Model 3 "
           "Performance. The roof rack guide notes that TESEVO excludes a version it calls the Model 3 Standard. "
           "We could not confirm what differs on it, so ask the seller.",
   "table": {"caption": "Model 3 versions and what the four guides list for each",
             "head": ["Model 3", "Floor liners", "Roof bars", "Hitch"],
             "rows": [
              ["2017–2023 (builds to October 2023)", "No priced pick; buy a set that names 2017–2023", "Tesla's rack; AUXPACBO lockable set, about $150–$220; WheelX", "No Tesla tow option. CURT 13431, 13449 and 11581, maXpeedingrods; Stealth SHR09001 (2017–2025)"],
              ["2024–2025 Highland", "All five sets in the guide", "Tesla's rack; WheelX; confirm Highland fit on other sets", "Tesla Tow Package; Stealth SHR09001; TIOYAR (2024–2026)"],
              ["2026", "All but BRYOUS, which is listed 2024–2025", "Tesla's rack; WheelX", "Tesla Tow Package; TIOYAR; Stealth lists to 2025, so confirm"],
              ["Highland Performance", "Fit not confirmed in the guide; ask the seller", "Tesla says its rack fits all Model 3", "Tesla Tow Package not compatible"],
             ]}},
  {"h": "The glass roof: fixed points, Tesla's 150 lb rating, and Tesla's rule on racks",
   "body": "The Model 3's roof is glass, with no rails, no gutters and no opening panel. A rack attaches at fixed "
           "mounting points hidden under the roof trim, and the towers rest on the body at those points, not on "
           "the glass.\n\n"
           "**The figure.** "
           "The 150 lb in the guides is Tesla's rating for its own Model 3 Roof Rack: the Tesla Shop page gives a "
           "150 lb load rating and a 495 lb static load limit. Neither Tesla manual page we opened prints a roof "
           "load, so treat 150 lb as the working limit for bars, carrier and cargo together.\n\n"
           "**What Tesla's manual says.** The Vehicle Loading page, in both the 2017–2023 manual and the current "
           "one, says the Model 3 \"supports the use of Tesla-approved roof racks using a Tesla mounting "
           "accessory\" and that owners must use \"only roof rack systems that have been approved by Tesla\". "
           "Tesla's own rack, about $400, meets that, and it was out of stock on October 4, 2026. Aftermarket bars "
           "are sold for the same fixed points at about $130–$220. We could not confirm whether Tesla approves any "
           "of them, and the 2017–2023 manual says damage caused by \"installing non-approved parts\" is not "
           "covered by the warranty, so ask Tesla first. Their listed ratings of 176 lb or 220 lb describe the "
           "bars, not the roof."},
  {"h": "A 28 in spread on a sedan roof: sizing a cargo box",
   "body": "A cargo box is universal. What is specific to the Model 3 is the short distance between the bars and "
           "the trunk lid behind them.\n\n"
           "**The spread.** The guides cite etrailer's product experts for about 28 in between the bars of Tesla's "
           "rack. We could not confirm the spread of aftermarket or Highland-specific bars, so measure yours "
           "center to center before choosing a box.\n\n"
           "**The overhang.** On bars 28 in apart, most of the box hangs past them. Too far forward and the nose "
           "sits over the windshield. Too far back and the tail sits over the rear glass, where the trunk lid "
           "rises. Center the box and open the trunk slowly the first time.",
   "table": {"caption": "Cargo boxes against a 28 in spread and Tesla's 150 lb rating (specs from the cargo box guide; the bars' weight comes off too)",
             "head": ["Cargo box", "Box weight", "Left of 150 lb before bars", "Length, and overhang on 28 in bars", "Crossbar spread range"],
             "rows": [
              ["Thule Pulse 2 M", "31 lb", "About 119 lb", "68.9 in; about 41 in", "Not published; confirm with Thule"],
              ["Rhino-Rack MasterFit 440", "38.6 lb", "About 111 lb", "76 in; about 48 in", "About 24.4–36.6 in"],
              ["INNO Wedge 660", "42 lb", "About 108 lb", "80 in; about 52 in", "24–39 in"],
              ["Thule Force 3 L", "43 lb", "About 107 lb", "76.8 in; about 49 in", "Not published; confirm with Thule"],
              ["Yakima SkyBox 16", "47 lb", "About 103 lb", "81 in; about 53 in", "24–34.5 in"],
              ["SportRack Vista XL", "Not published", "Confirm on the listing", "63 in; about 35 in", "Fixed at 25-7/8, 27-7/8 or 29-7/8 in"],
             ]}},
  {"h": "Towing and hitch carriers: what Tesla sells, what its manual says, and where an aftermarket hitch stands",
   "body": "**What Tesla sells.** The Tesla Shop lists a Model 3 Tow Package at about $1,300: a steel tow bar with "
           "a 2 in hitch receiver and a 4-pin connector, a trailer harness and tow mode software, with Service "
           "Center installation included. Tesla says it is \"capable of towing up to 2,200 lbs\" and \"compatible "
           "with Model 3 Rear-Wheel Drive and All-Wheel Drive vehicles produced in 2024+. Not compatible with "
           "Model 3 Performance vehicles.\" The shop showed it out of stock on October 4, 2026.\n\n"
           "**What the manual gives a car with that package.** The current manual's Towing and Accessories page "
           "lists 1,650 lb without trailer brakes, 2,200 lb with them and a maximum tongue weight of 200 lb. It "
           "says \"Trailer Mode must always be active when towing a trailer\" and, as we read it, asks for 42 psi "
           "in the tires. For carriers, the receiver is \"designed to support vertical loads of up to 121 lbs "
           "(55 kg)\", rack and bikes together.\n\n"
           "**What the manual says about every other Model 3.** The same page carries this caution: \"Do not "
           "attempt to install an accessory carrier on Model 3 that is not equipped with the towing package. Doing "
           "so can cause significant damage.\" It adds: \"Damage caused by non-Tesla approved accessories is not "
           "covered by the warranty.\" The 2017–2023 manual's Vehicle Loading page says: "
           "\"Do not use Model 3 for towing purposes. Model 3 does not currently support towing.\" The current "
           "manual's Vehicle Loading page carries the same warning, so the only towing figures Tesla publishes are "
           "for a car fitted with its own package.\n\n"
           "**Where that leaves an aftermarket hitch.** Aftermarket hitches are sold for both bodies, and the "
           "hitch guide lists six. They are not Tesla's towing package, and nothing we read from Tesla approves "
           "them for a trailer or a carrier. Their ratings describe the steel, not the car: 2,000 lb and 300 lb "
           "of tongue weight on CURT's 13431, or 3,500 lb and 350 lb on Stealth's tow package. We could not "
           "confirm how Tesla service treats a Model 3 with one fitted, or whether Tesla's 121 lb figure can be "
           "applied to a receiver Tesla did not install. Ask a Tesla Service Center before buying, and get the "
           "answer in writing.\n\n"
           "**If you still buy one.** Match the listing to the body, and expect the rear fascia to come off. "
           "CURT rates its 13431 as a professional-level install."},
  {"h": "Range, combined Tesla listings, and the order to fit the four",
   "body": "**Range.** Tesla publishes no range figure for a rack or a box on the Model 3. The Tesla Shop says the "
           "rack was engineered for \"maximum aerodynamic efficiency, minimal interior noise and impact to "
           "range\", with no number. The figures the guides cite are fueleconomy.gov's, and they "
           "describe fuel economy on gas vehicles: around 2–8% in city driving, 6–17% on the highway and 10–25% "
           "at 65–75 mph for a large, blunt rooftop cargo box, and 1–5% on the highway for rear-mount cargo boxes "
           "or trays. We found no equivalent published figure for the Model 3, so read those as direction, not a "
           "range forecast. For towing, Tesla's manual says only that driving range \"can decrease "
           "significantly\".\n\n"
           "**Combined listings.** Many sellers put the Model 3 and the Model Y in one title. They are different "
           "vehicles. The floor mat guide says the crossover's mats do not fit, and TESEVO's and Tesstudio's rack "
           "pages sell the two as separate versions. The site's vehicle data gives the crossover a 165 lb roof "
           "figure and a 3,500 lb tow rating with its own Tesla package. Neither number applies to a Model 3.\n\n"
           "**The order to fit them.** Floor liners go in first and need no tools. The bars bolt into the fixed "
           "points next, with no pad touching the glass. The box goes on centered, with bars, box and gear under "
           "150 lb. A hitch comes last."},
 ],
 "avoid": [
  {"h": "A 2017–2023 part on a Highland, or a Highland part on a 2017–2023 car", "body": "Liner sets, aftermarket roof bars and most hitches are split at the refresh. Every liner set the floor mat guide prices is Highland only, and CURT's hitches stop at 2023."},
  {"h": "Loading the roof to the bar's or the box's rating", "body": "Bars listed at 176 lb or 220 lb and boxes rated at 165 lb don't raise Tesla's 150 lb rack rating, which covers the bars, the box and the gear."},
  {"h": "A cargo box that can't reach 28 in, or a long one pushed back", "body": "The Yakima DeepSpace 10 needs at least 32 in between bars. An 80 in box overhangs 28 in bars by about 52 in, and sliding it rearward puts the tail over the trunk lid."},
  {"h": "Treating a hitch's rating as Tesla's approval", "body": "A 2,000 lb or 3,500 lb hitch rating does not change Tesla's manual, which says not to fit an accessory carrier to a Model 3 without the towing package. Ask Tesla first."},
 ],
 "verdict": {
  "thesis": "On the 2017–2026 Model 3, buy floor liners matched to the body first, add fixed-point roof bars second and a cargo box that fits a 28 in spread third, and treat a trailer hitch as a question for Tesla before it is a purchase.",
  "body": "The Model 3 is easy to accessorize once four facts are written down: 2017–2023 or Highland, the build "
          "month, the drivetrain, and the spread of the bars on the roof. Floor liners need only the first and cost "
          "the least. A roof rack needs the build month, bolts on at home and comes off again. A cargo box follows "
          "the bars and has to suit a 28 in spread.\n\n"
          "The trailer hitch sits last because it is the one choice with consequences beyond fit. Tesla lists a Tow "
          "Package only for 2024 and later Rear-Wheel Drive and All-Wheel Drive cars, and its manual says not to "
          "fit an accessory carrier to any Model 3 without it. Aftermarket hitches cost far less and sit outside "
          "what Tesla's manual provides for, so ask Tesla first. Each linked guide covers the fit details for its "
          "category.",
 },
 "sources": [
  ["Model 3 Owner's Manual: Towing and Accessories (Tesla)", "https://www.tesla.com/ownersmanual/model3/en_us/GUID-BD9A38D5-4410-45A3-8337-BDF7342750F3.html"],
  ["Model 3 Owner's Manual: Vehicle Loading, towing warning and roof racks (Tesla)", "https://www.tesla.com/ownersmanual/model3/en_us/GUID-877ACE2D-B62F-4596-A6AD-A74F7905741C.html"],
  ["2017–2023 Model 3 Owner's Manual: Vehicle Loading (Tesla)", "https://www.tesla.com/ownersmanual/2017_2023_model3/en_us/GUID-877ACE2D-B62F-4596-A6AD-A74F7905741C.html"],
  ["2017–2023 Model 3 Owner's Manual: Parts and Accessories (Tesla)", "https://www.tesla.com/ownersmanual/2017_2023_model3/en_us/GUID-ECA7C07B-7944-496B-8FC5-12762BF061F1.html"],
  ["Model 3 Tow Package: price, contents, compatibility (Tesla Shop)", "https://shop.tesla.com/product/model-3-tow-package"],
  ["Tesla Model 3 Roof Rack: 150 lb rating, 495 lb static limit, fitment (Tesla Shop)", "https://shop.tesla.com/product/model-3-roof-rack"],
  ["Tesla Model 3: 2024 refresh dates and changes, glass roof (Wikipedia)", "https://en.wikipedia.org/wiki/Tesla_Model_3"],
  ["Cargo box and rear carrier fuel economy impact (fueleconomy.gov)", "https://www.fueleconomy.gov/feg/driveHabits.jsp"],
  ["Model 3 28 in crossbar spread and Yakima box fit (etrailer expert answers)", "https://www.etrailer.com/answers.aspx?AnswerMake=Tesla&Manufacturer=Yakima&Filter=fit"],
  ["Tesstudio roof rack variants, Model 3 and Highland (Tesstudio)", "https://www.tesstudio.com/products/tesstudio-roof-rack-for-tesla-model-3-highland-model-y-model-y-juniper-set-of-2"],
  ["TESEVO lockable aluminum roof rack, Model 3/Y (TESEVO)", "https://www.tesevo.com/products/tesla-model-3-highland-y-juniper-aluminum-lockable-roof-rack"],
  ["Stealth Hitches SHR09001, 2017–2025 Model 3 (Stealth Hitches)", "https://stealthhitches.com/products/tesla-hitch-shr09001"],
  ["CURT 13431 Model 3 hitch (etrailer)", "https://www.etrailer.com/Trailer-Hitch/CURT/C13431.html"],
  ["Thule Pulse 2 M (Thule)", "https://www.thule.com/en-us/cargo-carrier/car-top-carrier/thule-pulse-2-m-_-610250"],
  ["3D Maxpider Kagu floor liners (AutoAccessoriesGarage)", "https://www.autoaccessoriesgarage.com/Floor-Mats-Liners/3D-Maxpider-Kagu-Floor-Liners"],
 ],
}
