"""Upgrades pillar: 2020–2026 Tesla Model Y (1st gen, incl. the 2025 "Juniper" refresh; an electric crossover, no bed).
Hub page: ranks the four published Model Y category guides and links to them. No product picks or ASINs here
(the site pulls each guide's #1 pick). Every price band comes from the linked guides' picks[].price fields or, where
noted as "product list", their FITS bands; vehicle facts from db/migrations/003_vehicles.sql (EV, roof type
fixed-points, roof load 165 lb, hitch class 3, 2 in receiver, 3,500 lb, optional 7-seat, Juniper 2025; and the
Model 3 row: no factory hitch in the US, aftermarket 1.25 in, 2024 Highland refresh), the four guides and their
sources, and six pages opened for this page on 2026-10-04:
Wikipedia's Tesla Model Y page (seven-seat option in the US "until the 2025 refresh"; refreshed car available in the
US from March 2025; Model Y Standard released October 2025 with no lightbar, no rear screen and a headliner covering
the glass roof; Model Y L six seats in a 2-2-2 layout, 7.0 in longer, launched in the US on July 2, 2026; about 75%
of components shared with the Model 3);
Tesla's Model Y owner's manual, Towing and Accessories (3,500 lb / 350 lb for 5-seat and Performance on every wheel
size; lower rows for 6- and 7-seat cars; 42 psi; receiver "designed to support vertical loads up to 160 lbs";
"Do not attempt to install an accessory carrier on Model Y that is not equipped with the tow package"; "Damage
caused by non Tesla-approved accessories is not covered by the warranty"; "Trailer Mode must always be active when
towing a trailer");
the Tesla Shop Model Y Tow Package page ($1,300, steel tow bar with 2 in receiver and 7-pin connector, trailer
harness, tow mode software, "Compatible with all Model Y vehicles", shipping and Service Center installation
included, out of stock);
Tesla's tow package support page (can be purchased with the car or later; 2 x 2 in square receiver, no class);
the Tesla Shop Model Y Roof Rack page ($500, 165 lb, aluminum T-slot bars, die-cast towers with integrated locks,
"Compatible with all Model Y vehicles, excluding Model Y L", installation at home, out of stock, no static figure);
and fueleconomy.gov's driving-habits page (rooftop box 2–8% city, 6–17% highway, 10–25% at 65–75 mph; rear-mount
boxes or trays 1–2% city, 1–5% highway; gas vehicles).
Not verified, and worded as such in the text: any range, efficiency or noise figure for a rack or box on a Model Y
(Tesla publishes none; the fueleconomy.gov figures are for gas vehicles); a static roof rating for a rooftop tent;
the crossbar spread on Juniper or aftermarket bars (35.5 in is one owner's measurement on a 2021 car with Tesla's
rack); the hitch class of Tesla's package (Tesla prints none; the vehicle data says Class 3; Wikipedia calls the Performance's a "class II tow bar", not used on the page); the exact 6- and
7-seat towing rows (read through a text extraction, so the page says "as we read"); how Tesla service treats a car
with an aftermarket hitch, and whether an aftermarket harness triggers Trailer Mode; published ratings for the
Draw-Tite 76430, the LOCAME hitch and the Juniper-only hitch; fit of one-listing 2020–2026 hitches across builds;
what differs inside the Model Y Standard for liners; liners, racks and aftermarket hitches for the Model Y L;
the spread range of the Thule Pulse 2 M and SportRack Horizon 2 L; the liftgate height (cited from the cargo box
guide, manual page not reopened). No Model Y guide exists for bike racks, seat covers or dash cams; none are ranked.
Source fixes 2026-10-04: dropped "our hitch guide cites 2,300–3,500 lb" (the hitch guide no longer prints a range for 6- and 7-seat cars); the Juniper identification FAQ and section now start from model year and build date instead of the lights, matching the corrected floor mat guide.
"""

KIND = "upgrades"
KEY = ("tesla", "model-y", "2020-present")
CATEGORIES = ["floor-mats", "roof-racks", "hitches", "cargo-boxes"]

TITLE = "2020–2026 Tesla Model Y Upgrades, Ranked: 4 Mods in Order, With Juniper and Glass-Roof Fit Traps"
META = ("Four 2020–2026 Model Y upgrades in buying order: floor liners, roof rack, trailer hitch and cargo box, with "
        "Juniper, 7-seat, 165 lb roof and tow package notes.")

FAQ = [
 ("What should I upgrade first on a 2020–2026 Tesla Model Y?",
  "Floor liners, then a roof rack. Liners cost the least, about $120–$230, and need three facts: "
  "pre-refresh or Juniper, five seats or seven, and whether the trim is the Standard. A roof rack is second at about "
  "$150–$500, bolted to four fixed points with no drilling. The trailer hitch is third "
  "because it is the biggest decision: Tesla's Tow Package at about $1,300, or an aftermarket receiver at about "
  "$120–$420. A cargo box is last, since it needs the bars first."),
 ("How do I tell a pre-refresh Model Y from a Juniper, a Standard or a Model Y L?",
  "Start with the model year and the build date on the door-jamb label, not the lights. Our guides describe the "
  "Juniper by its full-width light bar front and rear and its rear-seat touchscreen; the 2020–2024 Model Y has "
  "separate headlights. One version breaks the light test. Wikipedia says the Model Y Standard, released in October "
  "2025, has no lightbar and no rear screen. The Model Y L is the six-seat version, 7.0 in longer. A 2025 can be "
  "either body, since the refreshed Model Y reached US buyers in March 2025, so check the build date and the "
  "listing's fit notes."),
 ("Can I put a bike rack on a Model Y that doesn't have Tesla's Tow Package?",
  "Aftermarket 2 in receivers are sold for that. Tesla's position is "
  "different. Its owner's manual says the receiver is designed to support vertical loads up to 160 lb and, as we "
  "read it, says not to install an accessory carrier on a Model Y that is not equipped with the tow package. It adds "
  "that damage caused by non Tesla-approved accessories is not covered by the warranty. We could not confirm how "
  "Tesla service treats an aftermarket hitch, so ask before you buy."),
 ("How much can a Model Y tow, and does an aftermarket hitch change that?",
  "A hitch never raises it. Tesla's owner's manual gives 3,500 lb of towing and 350 lb of tongue weight for "
  "five-seat and Performance cars on every wheel size, with five or fewer people aboard. Six- and seven-seat cars have their own tables: the limit depends on wheel size and drops as the seats fill, and as we "
  "read them, a full seven-seat Model Y is limited to 2,000 lb on 19 in wheels and is marked 'Not permitted' on 20 in wheels. Tesla also asks for 42 psi cold and says "
  "Trailer Mode must be active when towing."),
 ("How much weight can the Model Y's glass roof carry?",
  "Plan around 165 lb in total. Tesla rates its Model Y Roof Rack at 165 lb, our vehicle data holds the same figure, "
  "and that total includes the bars and the carrier. TESEVO's bars weigh 12.4 lb, and the boxes in the cargo box "
  "guide weigh 30.2 lb to 57 lb. Tesla's rack page gives no "
  "static figure, so there is no official number for a rooftop tent."),
 ("How much range does a roof rack or cargo box cost on a Model Y?",
  "Tesla doesn't publish a number. It says its rack was engineered for minimal impact to range. The "
  "only figures our guides cite are from fueleconomy.gov and describe gas vehicles: a large, blunt rooftop cargo box "
  "can reduce fuel economy by around 2–8% in city driving, 6–17% on the highway and 10–25% at 65–75 mph. Rear-mount "
  "cargo boxes or trays cost 1–5% on the highway. We found no equivalent published figure for the Model Y, so use "
  "those numbers for direction only."),
 ("Do 2020–2024 Model Y accessories fit the 2025–2026 Juniper?",
  "It depends on the category. Floor liners: no, makers sell separate sets. Roof bars: Tesla says its own rack fits "
  "every Model Y except the Model Y L, while Tesstudio and EVBASE sell separate Juniper parts. Hitches: Tesla says "
  "its Tow Package is compatible with all Model Y vehicles, but Stealth Hitches sells separate parts for 2020–2022, "
  "2023–2024 and 2026, and one budget listing is for 2025 only. Cargo boxes: the box is universal, so only the bars "
  "change."),
 ("Do Model 3 floor mats, roof racks or hitches fit the Model Y?",
  "No. Wikipedia says the Model Y shares about 75% of its components with the Model 3, but not these. "
  "Our floor mat guide says the Model Y is taller, with a different floor, trunk and frunk. TESEVO "
  "and Tesstudio sell Model 3 and Model Y racks as separate versions. A title that says Highland names the Model 3's "
  "2024 refresh. Our vehicle data lists aftermarket Model 3 hitches as 1.25 in receivers, where the Model Y's are "
  "2 in."),
 ("How much does it cost to add all four upgrades to a Model Y?",
  "From the prices on our four guides' picks, a budget build on a 2020–2024 five-seat Model Y runs about "
  "$940–$1,130: 3W liners, AUXPACBO bars, a LOCAME receiver and SportRack's Horizon 2 L. With Juniper parts it runs "
  "about $990–$1,200. A mid build with a larger liner kit, TESEVO bars, a Draw-Tite or Juniper-only hitch and a "
  "DeepSpace 10 or Pulse 2 M runs about $1,248–$1,499. A premium build with 3D MAXpider mats, Tesla's rack, Tesla's "
  "Tow Package and a GrandTour 16 or Wedge 660 runs about $2,659–$2,895."),
]

ARTICLE = {
 "dek": "Four upgrades for the first-generation Model Y, in the order most owners should buy them. On this crossover "
        "the order is shaped by a 2025 refresh that split liners, roof bars and hitches into separate parts, by a "
        "glass roof that takes a rack only at four fixed points and carries 165 lb, and by Tesla's own rules on what "
        "may hang from the hitch.",
 "author": "jake-morrison",
 "reviewed": "2026-10-04",
 "method": "We did not install any of these parts ourselves. The order comes from our four fit-checked 2020–2026 "
           "Model Y guides, weighing how many Model Ys each upgrade suits, what it costs, how easily it comes off "
           "again and how much can go wrong with fit. Price bands are the prices listed on those guides' picks, "
           "checked at maker and retailer stores in September 2026, and are approximate. Vehicle facts come from our "
           "vehicle data, the guides' sources, Wikipedia's Model Y page, Tesla's owner's manual and the Tesla Shop, "
           "opened on October 4, 2026. Efficiency figures are fueleconomy.gov's and describe gas vehicles. Where we "
           "couldn't confirm a detail, the text says so.",
 "takeaways": [
  "**Name the body before the part.** Pre-refresh 2020–2024, Juniper, Standard and Model Y L take different liners, and makers split roof bars and hitches too.",
  "**The roof takes a rack at four fixed points only.** Tesla rates its rack at 165 lb, and that covers the bars, the carrier and the cargo.",
  "**Tesla's limits cap every hitch.** The manual gives 3,500 lb of towing, 350 lb of tongue weight and 160 lb of vertical load for a carrier.",
  "**The manual ties carriers to the Tow Package.** As we read it, Tesla says not to fit an accessory carrier to a Model Y without that package.",
  "**A cargo box needs bars and the right spread.** Tesla's bars were measured at about 35.5 in apart on a 2021 Model Y, which rules some boxes out.",
 ],
 "priority": [
  {"category": "floor-mats",
   "h": "1. Floor liners first: the lowest price on the page, once generation and seats are settled",
   "why": "Floor liners lead because they cost the least and every Model Y benefits. Three facts decide fit. "
          "Generation: makers sell separate sets for the 2020–2024 Model Y and the Juniper, and several listings say "
          "\"not Juniper\" or \"Juniper only\". Seats: most sets are cut for five, and the seven-seat version offered "
          "before the refresh needs a set that names it. Trim: the Juniper kits from Foronetry, TripleAliners and "
          "Autocessking exclude the Standard. Then choose coverage, since kits run from six to eleven pieces across "
          "the cabin, frunk, trunk floor and lower trunk well. Prices in our guide run about $120–$160 for 3W's "
          "6-piece set for 2020–2024 five-seat cars, about $140–$190 for Foronetry's 8-piece Juniper set, about "
          "$150–$200 for TripleAliners' 10-piece or Autocessking's 11-piece Juniper kits and about $150–$230 for "
          "3D MAXpider's Kagu cabin set. The trade-off is documentation against coverage: retailers describe the "
          "Kagu's three-layer construction, but it covers the cabin only.",
   "skip_if": "The cabin and trunk stay dry and clean, and the factory carpet mats are enough for you."},
  {"category": "roof-racks",
   "h": "2. Roof rack second: no drilling, off in minutes, and capped at 165 lb",
   "why": "A roof rack ranks second because it is the cheapest way to add carrying capacity and the easiest "
          "load-carrying upgrade to undo. The Model Y has a glass roof with no rails. Every rack bolts into four "
          "metal mounting points hidden under the trim along the roof edges, with no drilling, and our roof rack "
          "guide says the bars come off in a few minutes. Tesla says its own rack, about "
          "$500, fits every Model Y except the Model Y L. Tesstudio and EVBASE sell separate 2020–2024 and Juniper "
          "versions, and TESEVO excludes the Standard and the L. Prices run about $150–$220 for AUXPACBO's lockable "
          "bars for the original body, about $180–$260 for the RuiHui set whose listing names the Juniper and about "
          "$269 for TESEVO's. Tesla rates its rack at 165 lb, and that covers bars, carrier and cargo. The trade-off "
          "is drag and wind noise, and Tesla publishes no figure for either.",
   "skip_if": "Everything you carry fits in the trunk, the lower well and the frunk, or bikes are the only load and a hitch will carry them."},
  {"category": "hitches",
   "h": "3. Trailer hitch third: Tesla's Tow Package or an aftermarket receiver, and they are not equivalent",
   "why": "A trailer hitch ranks third because it has the most to decide and is the hardest to reverse. One route "
          "is Tesla's Model Y Tow Package, about $1,300 with Service Center installation: a steel tow bar with a "
          "2 in receiver, a 7-pin connector, a trailer harness and tow mode software. "
          "The other route is an aftermarket Class 3 receiver: about $120–$200 for "
          "LOCAME's, about $250–$350 for Draw-Tite's 76430 and about $300–$420 for CURT's kit with a 4-way harness. "
          "Those are split by build year. Tesla's limits cap all of them: 3,500 lb of trailer and 350 lb of tongue "
          "weight on five-seat cars, and 160 lb of vertical load for a carrier. The trade-offs are structural and "
          "contractual. etrailer notes that CURT's hitch replaces the rear impact structure, and Tesla's manual says "
          "not to fit a carrier without the tow package. If bikes are your main load, move this slot up to second.",
   "skip_if": "Your Model Y was ordered with the Tow Package, which already includes the 2 in receiver and the 7-pin connector."},
  {"category": "cargo-boxes",
   "h": "4. Cargo box last: it needs the bars first, and it has the largest drag cost",
   "why": "A cargo box comes last for three reasons. It can't be used without crossbars. It costs about $550–$865 "
          "in our guide, more than any set of bars. And it is the one upgrade here with a sourced efficiency cost: "
          "fueleconomy.gov says a large, blunt rooftop box can cut fuel economy by 6–17% on the highway and 10–25% "
          "at 65–75 mph. Those figures are for gas vehicles and Tesla publishes none for the Model Y, so read them "
          "as direction, not a range forecast. What is specific to the Model Y is the "
          "crossbar spread, which an owner on etrailer measured at about 35.5 in on Tesla's bars on a 2021 Model Y. "
          "The Yakima GrandTour 16 (about $709, 24–36 in), the DeepSpace 10 (about $649, 32–46 in) and the INNO "
          "Wedge 660 (about $865, 24–39 in) reach it. Box weight counts against "
          "the 165 lb limit, from 30.2 lb for the DeepSpace 10 to 57 lb for the CBX 16.",
   "skip_if": "You take one or two road trips a year and the luggage fits in the trunk wells and frunk."},
 ],
 "tier_table": {
  "caption": "Approximate price bands from our 2020–2026 Model Y guides' picks and product lists (September 2026; Amazon prices move daily). Each column includes the crossbars its cargo box needs",
  "head": ["Upgrade", "Budget", "Mid", "Premium"],
  "rows": [
   ["Floor liners", "About $120–$160 (3W 6-piece, 2020–2024 five-seat) or $140–$190 (Foronetry 8-piece, Juniper five-seat)", "About $130–$180 (Foronetry 9-piece, 2021–2024 five-seat) or $150–$200 (TripleAliners 10-piece, Juniper)", "About $150–$230 (3D MAXpider Kagu cabin set for your generation)"],
   ["Roof rack", "About $150–$220 (AUXPACBO lockable bars, original body) or $180–$260 (RuiHui, listing names Juniper)", "About $269 (TESEVO lockable bars; buy the version for your body)", "About $500 (Tesla Model Y Roof Rack; all Model Y except the L; out of stock when checked)"],
   ["Trailer hitch", "About $120–$200 (LOCAME Class 3, listed 2020–2026; confirm your build year)", "About $250–$350 (Draw-Tite 76430, 2020–2024) or $180–$260 (Juniper-only Class 3, 2025 not 2026)", "About $1,300 (Tesla Tow Package, installed)"],
   ["Cargo box", "About $550 (SportRack Horizon 2 L)", "About $649 (Yakima DeepSpace 10) to $700 (Thule Pulse 2 M)", "About $709 (Yakima GrandTour 16) to $865 (INNO Wedge 660)"],
   ["Total", "About $940–$1,130 on a 2020–2024 Model Y; about $990–$1,200 with the Juniper parts", "About $1,298–$1,499 on a 2021–2024 Model Y; about $1,248–$1,429 on a 2025 Juniper", "About $2,659–$2,895; frunk and trunk liners extra"],
  ],
 },
 "sections": [
  {"h": "Pre-refresh, Juniper, Standard or L: identify the Model Y before the part",
   "body": "One name covers four sets of parts. Our guides split the Model Y at the 2025 refresh, which listings "
           "call Juniper, and note two more versions that makers exclude by name.\n\n"
           "**The refresh.** Wikipedia says the refreshed Model Y became available in the US in March 2025. Our "
           "guides describe it with a full-width light bar front and rear and a rear-seat touchscreen. A Model Y "
           "built early in 2025 can still be the older body, so go by the model year and the build date on the "
           "door-jamb label, not the lights alone.\n\n"
           "**The Standard.** Wikipedia says Tesla released the lower-priced Model Y Standard in October 2025 "
           "without the lightbar or the rear screen, and with a headliner covering the glass roof. So a 2026 "
           "Model Y with no light bar is not a pre-refresh car. We could not confirm what differs for liners.\n\n"
           "**The Model Y L.** Wikipedia describes a six-seat version with a 2-2-2 layout, 7.0 in longer than the "
           "regular Model Y, launched in the US in July 2026. Tesla excludes it from its Roof Rack.",
   "table": {"caption": "Model Y versions and what our guides list for each",
             "head": ["Model Y", "Floor liners", "Roof bars", "Hitch"],
             "rows": [
              ["2020–2024, five seats", "3W (2020–2024), 3D MAXpider Kagu (2021–2025, with a separate 2020 set)", "Tesla's rack; aftermarket sets listed 2020–2024 or 2020–2025", "Tesla Tow Package; CURT 13598 (2020–2023); Draw-Tite 76430 (2020–2024)"],
              ["Pre-refresh, seven seats", "A set that names seven seats; 3D MAXpider third-row mat", "Tesla's rack, which excludes only the L", "Same hitches; the manual lowers the tow limit as seats fill"],
              ["2025–2026 Juniper", "TripleAliners, Autocessking, Foronetry 8-piece; 3D MAXpider's Juniper set is titled 2026", "Tesla's rack; bars that name Juniper, such as RuiHui's", "Tesla Tow Package; a Juniper-only Class 3 listing for 2025; Stealth SHR09004 for 2026 only"],
              ["Model Y Standard", "Three Juniper kits exclude it; ask the seller", "TESEVO excludes it; EVBASE lists a separate part", "Tesla Tow Package; no aftermarket listing in our guide names it"],
              ["Model Y L", "No set in our guide names it", "Excluded from Tesla's rack; no confirmed rack", "No aftermarket listing in our guide names it; ask Tesla"],
             ]}},
  {"h": "The glass roof: four fixed points, 165 lb, and what bars and a box cost",
   "body": "The Model Y's roof is glass with no side rails. A rack attaches to four metal mounting points hidden "
           "under the rubber trim along the roof edges, and the towers sit on the steel frame so the glass carries "
           "no load.\n\n"
           "**The limit.** Tesla rates its Model Y Roof Rack at 165 lb, and our vehicle data holds the same figure. "
           "It covers the bars, the carrier and the cargo. TESEVO publishes 12.4 lb for its bars. Tesla publishes "
           "no weight for its own, and no static figure for a rooftop tent.\n\n"
           "**The spread.** An owner on etrailer measured Tesla's bars on a 2021 Model Y at about 35.5 in center to "
           "center. That is one measurement on one body, so measure Juniper and aftermarket bars before choosing a "
           "box.\n\n"
           "**Range and noise.** Tesla says its rack was engineered for maximum aerodynamic efficiency, minimal "
           "interior noise and impact to range, and publishes no number for any of them. The figures our guides "
           "cite are fueleconomy.gov's, for gas vehicles: 6–17% on the highway for a large, blunt rooftop box, "
           "against 1–5% for rear-mount boxes or trays. We found no published "
           "equivalent for the Model Y. Height is the part a buyer controls: the INNO Wedge 660 is 11 in tall and "
           "the GrandTour 16 is 18 in.\n\n"
           "**The liftgate.** The cargo box guide cites Tesla's manual for a liftgate that opens up to about 7.5 ft "
           "high. Set the box forward and save a lower opening height if the gap is tight.",
   "table": {"caption": "Box weight against Tesla's 165 lb rating (specs as listed in the cargo box guide; the bars' weight comes off as well)",
             "head": ["Cargo box", "Box weight", "Left of 165 lb before bars", "Box's own load limit", "Crossbar spread range"],
             "rows": [
              ["Yakima DeepSpace 10", "30.2 lb", "About 135 lb", "100 lb", "32–46 in"],
              ["Thule Pulse 2 M", "31 lb", "About 134 lb", "165 lb (75 kg)", "Not published; confirm with Thule"],
              ["SportRack Horizon 2 L", "37 lb", "About 128 lb", "110 lb", "Not published; confirm on the listing"],
              ["Rhino-Rack MasterFit 440", "38.6 lb", "About 126 lb", "75 kg (165 lb)", "About 24.4–36.6 in"],
              ["INNO Wedge 660", "42 lb", "About 123 lb", "110 lb", "24–39 in"],
              ["Yakima GrandTour 16", "51.5 lb", "About 113 lb", "Not given in the guide", "24–36 in"],
              ["Yakima CBX 16", "57 lb", "About 108 lb", "Not given in the guide", "24–35.5 in; at the limit, so measure"],
             ]}},
  {"h": "Tow Package or aftermarket hitch: what Tesla sells, and what Tesla allows",
   "body": "**What Tesla sells.** The Tesla Shop lists the Model Y Tow Package at about $1,300: a steel tow bar "
           "with a 2 in receiver and a 7-pin connector, a trailer harness and tow mode software, with Service "
           "Center installation in the price. Tesla says it is compatible with all Model Y "
           "vehicles. The shop showed it out of stock on October 4, 2026.\n\n"
           "**What Tesla allows.** The manual gives 3,500 lb and 350 lb of tongue weight for five-seat and "
           "Performance cars. Six- and seven-seat cars lose capacity as seats fill. "
           "As we read the manual's tables, a seven-seat Model Y with every seat taken is limited "
           "to 2,000 lb on 19 in wheels and is marked 'Not permitted' on 20 in wheels, so read the row for your "
           "wheels and passenger count; the manual's table is the authority. For carriers, the receiver is designed for vertical loads up to 160 lb, rack and bikes "
           "together. As we read it, the same section says not to install an accessory carrier on a Model Y "
           "without the tow package, and that damage caused by non Tesla-approved accessories is not covered by "
           "the warranty.\n\n"
           "**Where that leaves an aftermarket hitch.** They are sold by build year and they bolt on, but Tesla's "
           "manual makes no provision for them. We could not confirm how Tesla service treats one, so ask first. "
           "CURT does not claim that its 56532 4-way harness, about $40–$70 and listed "
           "for 2020–2022 only, turns on Tesla's Trailer Mode.\n\n"
           "**Class and structure.** Tesla's pages describe a 2 x 2 in square receiver and print no hitch class. "
           "Our vehicle data records Class 3, and the aftermarket hitches are sold as Class 3. Our guide found no published "
           "ratings for the Draw-Tite 76430. etrailer notes that CURT's hitch requires permanent removal of the rear impact structure, and an "
           "etrailer expert says the Draw-Tite also replaces the bumper beam. EcoHitch sits lower and keeps it."},
  {"h": "Five seats or seven, frunk and trunk wells: sizing a liner kit",
   "body": "Our floor mat guide counts seven zones in a Model Y: the front footwells, a large rear floor, the frunk, "
           "the main trunk floor, the lower trunk well beneath it, the seatbacks when folded and the rear bumper "
           "sill. Kits run from six to eleven pieces.\n\n"
           "**Five seats or seven.** Wikipedia says the US Model Y offered optional third-row seats until the 2025 "
           "refresh. The second-row floor and cargo area differ on that version, and most sets in our guide are "
           "listed for five seats. 3D MAXpider sells a third-row mat for the seven-seat 2021–2025 Model Y, about "
           "$50–$80 in our guide's product list.\n\n"
           "**Cabin set or whole-car kit.** 3D MAXpider's Kagu full set covers the cabin, with frunk and trunk "
           "pieces bought separately. 3W's 6-piece set adds cargo and frunk liners for 2020–2024 five-seat cars. "
           "TripleAliners' 10-piece Juniper kit adds the rear lower well, backrest pieces and a bumper guard.\n\n"
           "**The lower trunk well.** Our guide calls it deep and notes that it collects water from wet gear. Look "
           "for a well liner with an edge, and dry it after wet trips."},
  {"h": "Model 3 listings, and the order to fit the four",
   "body": "The Model Y is based on the Model 3, and Wikipedia says the two share about 75% of their components. "
           "The parts on this page do not interchange.\n\n"
           "- **Floor liners.** Our floor mat guide says Model 3 mats don't fit: the Model Y is taller, with a "
           "different floor, trunk and frunk.\n"
           "- **Roof rack.** TESEVO's and Tesstudio's rack pages name both the Model 3 and the Model Y, sold as "
           "separate versions. Highland is the Model 3's 2024 refresh, per our vehicle data, and Juniper is the "
           "Model Y's.\n"
           "- **Cargo box.** The cargo box guide puts the 2017–2026 Model 3 at a 28 in spread and a 150 lb rating, "
           "against about 35.5 in and 165 lb here.\n"
           "- **Trailer hitch.** Our vehicle data lists no factory hitch for the US Model 3 and aftermarket 1.25 in "
           "receivers for bike racks only. Model Y hitches use a 2 in receiver.\n\n"
           "Fit the four in the ranked order. Liners need no tools. The bars bolt into the four mounting points at "
           "home, and no pad should touch the glass. Tesla fits its Tow Package at a Service Center, while an "
           "aftermarket hitch means removing the rear fascia. The box goes on last, set forward of the liftgate, "
           "with bars, box and gear under 165 lb."},
 ],
 "avoid": [
  {"h": "A 2020–2024 part on a Juniper, or a Juniper part on a Standard", "body": "Liners, aftermarket roof bars and aftermarket hitches are split at the refresh, and three Juniper liner kits exclude the Standard. A 2025 can be either body."},
  {"h": "Treating a hitch's rating as the Model Y's", "body": "CURT's 525 lb tongue-weight rating doesn't raise Tesla's 3,500 lb, 350 lb and 160 lb limits. Tesla's manual also says not to fit a carrier without the tow package."},
  {"h": "Loading the roof to the box's rating", "body": "Tesla's 165 lb covers the bars and the box too. A 51.5 lb GrandTour 16 leaves about 113 lb before the bars come off the total."},
  {"h": "Model 3 and combined Model 3/Y listings", "body": "Model 3 mats don't fit, Model 3 hitches are 1.25 in, and rack makers sell the two as separate versions. Buy the listing that names the Model Y and your body."},
 ],
 "verdict": {
  "thesis": "On the 2020–2026 Model Y, buy floor liners matched to generation and seats first, add fixed-point roof bars for your body second, choose between Tesla's Tow Package and an aftermarket trailer hitch with the manual open, and buy a cargo box only once the bars are measured.",
  "body": "The Model Y is easy to accessorize once five facts are written down: pre-refresh, Juniper, Standard or L; "
          "the build date; five seats or seven; whether the Tow Package was ordered; and the spread of the bars on "
          "the roof. Floor liners need the first three and cost the least. A roof rack needs only the body, bolts "
          "on at home and comes off again, and Tesla's own rack removes the fit question for every version but the "
          "L.\n\n"
          "The trailer hitch sits third because it is the one choice with consequences beyond fit: Tesla's package "
          "brings the 7-pin connector and Trailer Mode, while an aftermarket receiver costs far less and sits "
          "outside what Tesla's manual provides for. The cargo box is last because it needs the bars and has the "
          "largest drag cost. Each "
          "linked guide covers the fit details for its category.",
 },
 "sources": [
  ["Tesla Model Y: seating, 2025 refresh, Model Y Standard, Model Y L, Model 3 parts sharing (Wikipedia)", "https://en.wikipedia.org/wiki/Tesla_Model_Y"],
  ["Model Y Owner's Manual: Towing and Accessories (Tesla)", "https://www.tesla.com/ownersmanual/modely/en_us/GUID-F5C80FF5-8DE3-4750-8BAF-0DCC0CFA0C5C.html"],
  ["Model Y Tow Package: price, contents, compatibility (Tesla Shop)", "https://shop.tesla.com/product/model-y-tow-package"],
  ["Model Y Tow Package support page: receiver, Trailer Mode, carriers (Tesla)", "https://www.tesla.com/support/shop/model-y-tow-package"],
  ["Tesla Model Y Roof Rack: 165 lb rating, fitment (Tesla Shop)", "https://shop.tesla.com/product/model-y-roof-rack"],
  ["Model Y owner's manual: liftgate opening height (Tesla)", "https://www.tesla.com/ownersmanual/modely/en_us/GUID-3667D28B-5B3B-49CE-A1C1-3D70AC60D9F6.html"],
  ["Cargo box and rear carrier fuel economy impact (fueleconomy.gov)", "https://www.fueleconomy.gov/feg/driveHabits.jsp"],
  ["Model Y factory rack crossbar spread (etrailer Q&A)", "https://www.etrailer.com/question-591977.html"],
  ["Tesstudio roof rack variants, Model 3/Y/Juniper (Tesstudio)", "https://www.tesstudio.com/products/tesstudio-roof-rack-for-tesla-model-3-highland-model-y-model-y-juniper-set-of-2"],
  ["CURT 13598 Class 3 hitch, Model Y (CURT)", "https://www.curtmfg.com/part/13598"],
  ["2021 Tesla Model Y trailer hitches (etrailer)", "https://www.etrailer.com/Trailer-Hitch/Tesla/Model+Y/2021/DT58MR.html?vehicleid=202120216003159"],
  ["Draw-Tite vs EcoHitch for a 2023 Model Y (etrailer Q&A)", "https://www.etrailer.com/question-710375.html"],
  ["Stealth Hitches 2026 Model Y SHR09004 (Stealth Hitches)", "https://stealthhitches.com/products/tesla-hitch-shr09004"],
  ["TESEVO lockable aluminum roof rack, Model 3/Y (TESEVO)", "https://www.tesevo.com/products/tesla-model-3-highland-y-juniper-aluminum-lockable-roof-rack"],
  ["3D Maxpider Kagu floor liners (AutoAccessoriesGarage)", "https://www.autoaccessoriesgarage.com/Floor-Mats-Liners/3D-Maxpider-Kagu-Floor-Liners"],
 ],
}
