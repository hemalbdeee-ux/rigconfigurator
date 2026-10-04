"""Upgrades pillar: 2020–2025 Subaru Outback (6th gen, BT; the wagon, not the Legacy sedan and not the 2026 redesign).
Hub page: ranks the four published Outback category guides and links to them. No product picks or ASINs here
(the site pulls each guide's #1 pick). Every price band comes from the linked guides' picks[].price fields;
vehicle facts from db/migrations/003_vehicles.sql (SUV body style, raised rails with integrated swing-out crossbars
on most trims, fixed ladder-style rack on the Wilderness, factory hitch L101SAN000 Class II with a 2 in receiver and
harness, 2,700 lb standard / 3,500 lb XT and Wilderness, 2026 is a new generation, year_to 2025), the four guides and
their sources, and seven pages opened for this page on 2026-10-04: Subaru's 2025 Outback trim comparison sheet (nine
trims; 2,700 lb on Base, Premium, Onyx Edition, Limited and Touring, 3,500 lb on Onyx Edition XT, Wilderness, Limited
XT and Touring XT; "Roof rails with integrated and retractable cross bars (150 pounds maximum capacity)" on every
trim except the Wilderness; Wilderness rails with integrated tie-down points, 200 lb dynamic / 700 lb static; 8.7 in
and 9.5 in ground clearance), Subaru's 2022 Outback trim comparison sheet (same tow split, same 150 lb and
200 / 700 lb roof wording), Subaru's 2022 Outback Wilderness press release (fixed ladder-type roof rack system,
700 lb static limit for roof-top tent use, no dynamic figure, 3,500 lb, 9.5 in, standard all-weather floor mats),
Wikipedia's Subaru Outback page (182 hp 2.5 L and 260 hp 2.4 L turbo, Wilderness released May 2021 as a 2022 model,
2023 refresh: new front fascia, headlights and front cladding except on the Wilderness, third EyeSight camera on
Touring, Onyx trim with the non-turbo engine; 2026 seventh generation), Subaru Parts Pros' L101SAN000 page (Class II,
2 in, 2,700 lb / 270 lb on 2.5L, 3,500 lb / 350 lb on 2.4L, harness included, mount and ball not included,
Wilderness fascia panel and cutting template required and sold separately, not compatible with the rear bumper
underguard), The Rack Shop's Yakima SkyLine kit page ("WEIGHT LIMIT: 165 lbs", replaces the factory stowable
crossbars) and Autoblog's driveway test of the factory crossbars (round sockets, narrower than aftermarket bars).
The stored roof_load_lb value in the vehicle data (176) is not printed on this page; Subaru's own sheets are used.
AHG Auto Service's roof capacity page (a source in two of the guides) was also opened; it gives 150, 176, 200 and
220 lb for different Outbacks without a Subaru document, so none of its figures are used or cited here.
Not verified, and worded as such in the text: Subaru's roof figures for model years other than 2022 and 2025;
whether the 150 lb figure is a driving limit only and whether it applies with aftermarket crossbars (retailers quote
165 lb for their kits); any parked (static) figure for the standard roof; the center-to-center spread of the factory
crossbars; tow and tongue weight figures for model years we did not read; whether any Outback ships with a
factory-installed receiver; whether the 2023 refresh changed anything at the rear bumper; the weight of the Amazon
crossbar sets and of the SportRack Vista XL; 2024–2025 fit of the Thule kit titled 2010–2023; the rail type of the
OMAC bars; the TUZILLA hitch's ratings and Wilderness fit; whether all-weather mats stayed standard on the
Wilderness after 2022; and whether each box's clamps suit each crossbar profile. No Outback guide exists for running
boards, lighting or bike racks; none are ranked.
Source fixes 2026-10-04: "fixed sockets" reworded to "round sockets in the rails" to match Autoblog and the corrected guides; Autoblog source label no longer says swing-in; the guides now also cite Subaru's 2023 sheet; the stored roof_load_lb was changed from 176 to 150 in the same commit, and the rails, tow and fit_note attrs and the summary were rewritten to match Subaru's sheets.
"""

KIND = "upgrades"
KEY = ("subaru", "outback", "2020-present")
CATEGORIES = ["floor-mats", "hitches", "roof-racks", "cargo-boxes"]

TITLE = "2020–2025 Subaru Outback Upgrades, Ranked: 4 Mods in Order, With Roof-Rail and Tow-Rating Fit Traps"
META = ("Four 2020–2025 Outback upgrades in buying order: floor liners, trailer hitch, roof rack and cargo box, with "
        "Wilderness rails, roof load and 2.5L vs turbo towing.")

FAQ = [
 ("What should I upgrade first on a 2020–2025 Subaru Outback?",
  "Floor liners, then a trailer hitch. Liners cost the least, about $80–$180 across the full sets in the floor "
  "guide, and every trim shares one floor, so the only fit check is the model year. A hitch comes second: about "
  "$130–$320 from the aftermarket, and it carries bikes or a cargo tray without using the roof allowance. Crossbars "
  "are third, because every trim except the Wilderness already has retractable bars in the rails. A cargo box is "
  "last, since it costs the most and depends on the bar spread."),
 ("How much can a 2020–2025 Outback tow, and does an aftermarket hitch raise it?",
  "A hitch never raises it. Subaru's 2022 and 2025 spec sheets list 2,700 lb for the 2.5-liter trims and 3,500 lb "
  "for the 2.4-liter turbo in the XT trims and the Wilderness. A Subaru dealer listing for the factory hitch gives "
  "tongue weights of 270 lb and 350 lb. CURT's and Draw-Tite's hitches are rated at 3,500 lb or more, so the "
  "vehicle is the limit. We read Subaru's sheets for two model years only, so use the towing section of your owner's manual "
  "for your trim and year."),
 ("How much weight can a 2020–2025 Outback roof carry?",
  "It depends on the roof. Subaru's 2022 and 2025 spec sheets list the roof rails with integrated, retractable "
  "crossbars at a 150 lb maximum capacity. The same sheets list the Wilderness rails at 200 lb dynamic, meaning "
  "while driving, and 700 lb static, meaning parked. We did not read the sheets for other model years, so check "
  "your owner's manual. The box or carrier, any added crossbars and the cargo all count against the figure. A "
  "crossbar rated at 300 or 330 lb doesn't change it."),
 ("Does the Outback Wilderness need different parts?",
  "For the roof and the factory hitch, yes. The Wilderness, sold for 2022–2025, has fixed ladder-type rails with no "
  "crossbars, so it takes bars titled for the Wilderness, such as Tuyoung's 330 lb set at about $100–$140. Subaru's "
  "own hitch needs a Wilderness-specific fascia panel and a cutting template on this trim. Floor liners don't "
  "change, because the cabin floor is shared, and Subaru's 2022 release lists all-weather mats as standard on the "
  "Wilderness. It has the turbo engine, so Subaru rates it at 3,500 lb."),
 ("Can I mount a cargo box on the Outback's factory crossbars?",
  "Usually, on trims that have them. The box clamps to the deployed bars, provided the distance between them falls "
  "inside the box's range. Deploy the bars and measure center to center. Yakima lists 24–34.5 in for the SkyBox 16 "
  "Carbonite and 24–36 in for the GrandTour 16; etrailer lists 21-13/16 to 36-9/16 in for the Thule Motion 3 XL. "
  "We don't have a published spread for the factory bars, so the tape measure decides. If it doesn't match, "
  "clamp-on aftermarket bars let you set the spread."),
 ("Can I put a rooftop tent on a 2020–2025 Outback?",
  "The Wilderness is the trim built for it. Subaru's 2022 release gives its ladder-type rails a 700 lb static limit "
  "and says that allows a roof-top tent on the trail. On the road, the tent and the crossbars have to fit under the "
  "200 lb dynamic figure in Subaru's spec sheets. Standard trims are the harder case: the "
  "sheets we read give their roof a 150 lb maximum and no parked figure. Ask the tent maker whether it approves "
  "your Outback, and treat the owner's manual as the authority."),
 ("Can a 2.5-liter Outback carry bikes on a hitch rack?",
  "Yes. Every hitch in the guide has a 2 in receiver, which takes most platform bike racks without an adapter. The "
  "limit is tongue weight. Subaru's dealer listing gives 270 lb for the 2.5-liter Outback and 350 lb for the turbo, "
  "and the rack's own weight counts along with the bikes. The hitch's rating doesn't help: Draw-Tite's 76597 "
  "is rated at 675 lb, but on a 2.5-liter the Outback's 270 lb still applies."),
 ("Did the 2023 refresh change which Outback accessories fit?",
  "Not in any part the four guides cover. Wikipedia describes the 2023 update as a new front fascia, new headlights "
  "and additional front cladding on every model except the Wilderness, plus an Onyx trim with the non-turbo engine. "
  "Husky lists its 95541 liners for 2020–2025, CURT lists the 13494 hitch for 2020–2026 and ERKUL's crossbars are "
  "titled 2020–2025. The refresh adds one towing trap. An Onyx Edition without XT has the 2.5-liter engine and a "
  "2,700 lb rating in Subaru's 2025 sheet; the Onyx Edition XT is rated at 3,500 lb."),
 ("Do 2015–2019 or 2026 Outback parts fit a 2020–2025 Outback?",
  "Assume not. The 2020 Outback moved to a new platform with a new cabin floor, and Husky sells 99671 for 2015–2019 "
  "and 95541 for 2020–2025. The 2026 Outback is another new generation: Subaru sells separate factory hitches for "
  "it, L101SAR000 and L101SAR001, and several Wilderness crossbar listings say NOT for 2026. Two things do cross "
  "over. A cargo box clamps to crossbars, not to the vehicle. And CURT and Draw-Tite list the 13494 and 76597 for "
  "2020–2026, though for a 2026 you should confirm with the maker's fit checker."),
 ("How much does it cost to add all four upgrades to an Outback?",
  "From the prices on the four guides' picks, a budget build on a standard trim runs about $660–$760: a YITAMOTOR "
  "or Auxko liner set, the TUZILLA hitch, the factory crossbars and SportRack's Vista XL. A Wilderness adds about "
  "$90–$130 for bars. A mid build runs about $969–$1,139 with Subaru's mats or OEDRO liners, CURT's 13494, ERKUL's "
  "bars and Yakima's SkyBox 16 Carbonite. A premium build with Husky's WeatherBeater set, Draw-Tite's 76597, a "
  "Thule crossbar kit and the Thule Motion 3 XL runs about $2,010–$2,400. Wiring for an aftermarket hitch is extra."),
]

ARTICLE = {
 "dek": "Four upgrades for the sixth-generation Outback, in buying order. Fit on this wagon turns on a short list of "
        "facts: retractable factory crossbars or the Wilderness's fixed ladder rails, the 2.5-liter engine or the "
        "turbo, and the model years printed on the listing. The roof carries less than most crossbar ratings "
        "suggest, which is why the hitch ranks above the rack.",
 "author": "jake-morrison",
 "reviewed": "2026-10-04",
 "method": "We did not install any of these parts ourselves. The order comes from the four fit-checked 2020–2025 "
           "Outback guides on this site, weighing how many Outbacks each upgrade suits, what it costs and how much "
           "can go wrong with fit (roof rail type, engine, trim, model year). Price bands are the prices listed on "
           "those guides' picks, checked at maker and retailer stores in September 2026, and are approximate. "
           "Vehicle facts come from our vehicle data, the guides' sources, Subaru's 2022 and 2025 Outback trim "
           "comparison sheets, Subaru's 2022 Outback Wilderness press release, a Subaru dealer parts page and "
           "Wikipedia. Where we couldn't confirm a factory detail for every model year, the text says so.",
 "takeaways": [
  "**Look at the roof first.** Most trims have rails with retractable crossbars built in; the 2022–2025 Wilderness has fixed ladder rails and no crossbars.",
  "**The roof carries less than the bars claim.** Subaru's 2022 and 2025 spec sheets print 150 lb for the retractable-crossbar roof, and 200 lb driving and 700 lb parked for the Wilderness.",
  "**The engine sets the tow rating.** Subaru lists 2,700 lb for the 2.5-liter and 3,500 lb for the turbo XT trims and the Wilderness. No hitch raises either.",
  "**Tongue weight limits a bike rack.** Subaru's dealer listing gives 270 lb on the 2.5-liter and 350 lb on the turbo, and the rack's own weight counts.",
  "**Read the years on every listing.** The 2015–2019 Outback has a different floor, and the 2026 Outback is a new generation.",
 ],
 "priority": [
  {"category": "floor-mats",
   "h": "1. Floor liners first: one floor across every trim, and the lowest price on the page",
   "why": "Floor liners lead on the Outback because they cost the least, every drive uses them and their fit is the "
          "simplest of the four. The floor guide found one cabin floor across the 2020–2025 generation, so 2.5-liter, "
          "XT turbo and Wilderness trims all take the same liners. Two checks decide fit. First, the years. The 2020 "
          "Outback moved to the Subaru Global Platform with a new floor, and Husky's catalog shows the split: 99671 "
          "for 2015–2019 and 95541 for 2020–2025. Second, the vehicle named. Most listings also name the 2020–2025 "
          "Legacy, which shares the cabin floor, but a Legacy cargo liner won't fit the wagon. Prices in the guide "
          "run about $80–$120 for YITAMOTOR's or Auxko's TPE sets, about $90–$130 for OEDRO's set and for Subaru's "
          "J501SAN100 heavy-gauge mats, and about $130–$180 for Husky's WeatherBeater 95541, which Husky says is "
          "made in the USA with a lifetime warranty against cracks and breaks. The trade-off is walls against "
          "price: Subaru's mats lift out easily but hold less snowmelt than a deep liner.",
   "skip_if": "You have a Wilderness, which Subaru's 2022 release lists with all-weather floor mats as standard, and they are still in good shape."},
  {"category": "hitches",
   "h": "2. Trailer hitch second: it carries more than the roof can, on every trim",
   "why": "A trailer hitch ranks second because it suits every Outback and gives the wagon a place to carry weight "
          "that the roof can't. Subaru's dealer listing for the factory hitch gives a tongue weight of 270 lb on the "
          "2.5-liter and 350 lb on the 2.4-liter turbo, against Subaru's 150 lb roof figure on most trims. Engine "
          "decides the tow rating Subaru gives: 2,700 lb for the 2.5-liter, 3,500 lb for XT trims and the Wilderness, and no hitch raises "
          "either. Prices in the hitch guide run about $130–$190 for the budget TUZILLA, about $200–$280 for CURT's "
          "concealed 13494, about $230–$320 for Draw-Tite's 76597 and about $460–$530 for Subaru's own L101SAN000. "
          "The Subaru kit is a Class II hitch with the wiring harness included; the aftermarket hitches are Class 3 "
          "and need a plug-in harness bought separately. All have a 2 in receiver. The Wilderness is the fit "
          "exception: Subaru's kit needs a Wilderness-specific fascia panel and a cutting template on that trim. "
          "The trade-off with any hitch rack or carrier is that its own weight counts against tongue weight.",
   "skip_if": "A 2 in receiver is already bolted under the rear bumper, as it may be on a used Outback with the dealer-fitted hitch."},
  {"category": "roof-racks",
   "h": "3. Roof rack third: most trims already have crossbars, and the Wilderness has none",
   "why": "The roof rack ranks third because most Outbacks don't need one bought. Subaru's 2025 spec sheet lists "
          "roof rails with integrated, retractable crossbars on every trim except the Wilderness, and the roof rack "
          "guide says those bars handle a cargo bag, one bike or skis. The Wilderness, sold for 2022–2025, has fixed "
          "ladder-type rails with no crossbars, so it always needs a set. Rail type decides fit: bars titled \"Only "
          "Fit Wilderness\" don't suit the standard rails, and standard-rail bars aren't listed for the ladder "
          "rails. Prices in the guide run about $80–$130 for ERKUL's lockable bars for standard rails, about "
          "$90–$130 for the BougeRV and 300 lb lockable Wilderness sets, about $100–$140 for Tuyoung's 330 lb "
          "Wilderness bars and about $500–$750 for a Thule kit built for the stowable factory rack. The trade-off "
          "is that a bar's rating is not the roof's. Subaru's 2022 and 2025 sheets print 150 lb for the "
          "retractable-crossbar roof and 200 lb while driving for the Wilderness, well under the 220 to 330 lb on "
          "the budget listings.",
   "skip_if": "Your Outback has the retractable crossbars and they are wide enough for what you carry."},
  {"category": "cargo-boxes",
   "h": "4. Cargo box last: the costliest part here, limited by bar spread and the roof figure",
   "why": "The cargo box comes last because it costs the most, gets used on the fewest days and depends on the "
          "crossbar decision above. On standard trims the factory crossbars plug into round sockets in the rails, so deploy them, measure center to center "
          "and compare with the box's range: 24–34.5 in for Yakima's SkyBox 16 Carbonite, 24–36 in for the "
          "GrandTour 16, 21-13/16 to 36-9/16 in for the Thule Motion 3 XL per etrailer, and 32–46 in for the "
          "DeepSpace 10. A Wilderness needs crossbars before any box. Then the weight. The box and the gear inside "
          "share Subaru's roof figure, and the boxes in the guide weigh 30.2 to 51.5 lb. Prices run about $350 for "
          "the archived RocketBox 16, about $450 for SportRack's Vista XL, about $599 for the SkyBox 16, about $649 "
          "for the DeepSpace 10, about $709 for the GrandTour 16, about $799 for the SkyBox NX Skinny and about "
          "$1,150 for the Motion 3 XL. Test the rear gate with any box over 80 in.",
   "skip_if": "Your gear fits behind the seats, or it is heavy enough that a hitch carrier is the better place for it."},
 ],
 "tier_table": {
  "caption": "Approximate price bands from the picks in the 2020–2025 Outback guides (September 2026; Amazon prices move daily). Totals are for a standard trim with retractable crossbars",
  "head": ["Upgrade", "Budget", "Mid", "Premium"],
  "rows": [
   ["Floor liners", "About $80–$120 (YITAMOTOR or Auxko TPE)", "About $90–$130 (Subaru J501SAN100 mats or OEDRO TPE)", "About $130–$180 (Husky WeatherBeater 95541)"],
   ["Trailer hitch", "About $130–$190 (TUZILLA Class 3; confirm ratings on the listing)", "About $200–$280 (CURT 13494, 3,500 lb / 350 lb)", "About $230–$320 (Draw-Tite 76597, 4,500 lb / 675 lb)"],
   ["Roof rack", "Nothing to buy on standard trims: the factory crossbars. Wilderness: about $90–$130 (BougeRV bars)", "About $80–$130 (ERKUL lockable bars, standard rails). Wilderness: about $100–$140 (Tuyoung)", "About $500–$750 (Thule kit for the stowable factory rack; not for the Wilderness)"],
   ["Cargo box", "About $450 (SportRack Vista XL, on the factory bars if a fixed mounting position matches)", "About $599 (Yakima SkyBox 16 Carbonite, on the ERKUL bars)", "About $1,150 (Thule Motion 3 XL, on the Thule bars)"],
   ["Total", "About $660–$760; a Wilderness adds about $90–$130 for bars", "About $969–$1,139", "About $2,010–$2,400; wiring extra in every column"],
  ],
 },
 "sections": [
  {"h": "Two roofs: retractable crossbars or Wilderness ladder rails",
   "body": "The sixth-generation Outback was built with two roofs, and nearly every crossbar listing is written for "
           "one of them.\n\n"
           "**Standard trims.** Subaru's 2025 spec sheet describes the roof on every trim except the Wilderness as "
           "roof rails with integrated and retractable cross bars. Autoblog describes how they work: lift a tab, "
           "pull the bar out of its round socket, swing it across and plug it into the socket on the other side. "
           "Autoblog also notes that the bars aren't as wide as aftermarket bars.\n\n"
           "**Wilderness.** Subaru's 2022 press release calls it a fixed ladder-type roof rack system, and the spec "
           "sheets list roof rails with integrated tie-down points and anodized copper-finish accents. Neither "
           "mentions crossbars, so budget for a set. If you're unsure which roof you have, look for the "
           "copper-finish tie-down points.",
   "table": {"caption": "2020–2025 Outback roofs, and what each means for a rack, a box and a tent",
             "head": ["Roof", "Trims and years", "Subaru's roof figure", "Crossbars", "Cargo box", "Rooftop tent"],
             "rows": [
              ["Rails with retractable crossbars", "Every trim except the Wilderness, 2020–2025", "150 lb maximum (2022 and 2025 spec sheets)", "Built in; ERKUL's set or a Thule kit for wider bars", "Clamps to the factory bars if their spread suits the box", "No parked figure in the sheets we read"],
              ["Fixed ladder-type rails", "Wilderness, 2022–2025", "200 lb driving, 700 lb parked (2022 and 2025 spec sheets)", "None from the factory; buy bars titled for the Wilderness", "Needs crossbars first", "Subaru ties the 700 lb figure to roof-top tent use"],
             ]}},
  {"h": "150, 200 and 700 lb: read the roof figure before the bar rating",
   "body": "Three numbers matter on this roof, and each belongs to one configuration.\n\n"
           "- **150 lb.** Subaru's 2022 and 2025 trim comparison sheets list the roof rails with integrated, "
           "retractable crossbars at a 150 lb maximum capacity. The sheets don't split it into driving and parked "
           "figures.\n"
           "- **200 lb.** The same sheets list the Wilderness rails at a 200 lb dynamic maximum, meaning while "
           "driving.\n"
           "- **700 lb.** The Wilderness static maximum, meaning parked.\n\n"
           "We read those sheets for 2022 and 2025 only. The Rack Shop lists a 165 lb weight limit for its Yakima "
           "SkyLine kit on this Outback, and the Thule listing in the roof rack guide states 165 lb. We could not "
           "confirm that aftermarket bars raise Subaru's figure, so plan around 150 lb on a standard trim. Your "
           "owner's manual is the authority for your model year. The 220, 300 or 330 lb on a crossbar listing is "
           "the bar's own strength, and the lower number always wins.\n\n"
           "Here is what a box leaves under 150 lb on the factory bars, before anything else rides on the roof:\n\n"
           "- **Yakima SkyBox 16 Carbonite, 47 lb:** about 103 lb for gear.\n"
           "- **Thule Motion 3 XL, 51 lb:** about 99 lb, well under the 165 lb Thule rates the box for.\n"
           "- **Yakima DeepSpace 10, 30.2 lb:** about 120 lb of roof allowance, but Yakima caps the box at 100 lb "
           "of cargo.\n\n"
           "On a Wilderness, start from 200 lb. Subtract the weight of any aftermarket crossbars first; the Amazon "
           "sets in the roof rack guide don't publish theirs, so weigh them or ask the seller."},
  {"h": "Towing: the engine sets the number, the hitch doesn't",
   "body": "**The rating.** Subaru's 2022 and 2025 spec sheets list **2,700 lb** for every 2.5-liter trim and "
           "**3,500 lb** for the 2.4-liter turbo trims, and our vehicle data records the same split. The lower of "
           "vehicle and hitch applies. Your owner's manual is the authority for your trim and year.\n\n"
           "**The badge trap.** XT and Wilderness badges mean the turbo. Onyx is the name to read twice: "
           "Subaru's 2025 sheet lists an Onyx Edition at 2,700 lb and an Onyx Edition XT at 3,500 lb.\n\n"
           "**The receiver.** Subaru sells the hitch as an accessory, L101SAN000. The spec sheets we read don't "
           "list a receiver as equipment on any trim, so we could not confirm that any Outback leaves the factory "
           "with one. Look under the rear bumper. Our vehicle data records the factory part as Class II with a 2 in "
           "receiver. The dealer listing includes a wiring harness, but not the hitch mount or ball.\n\n"
           "**Tongue weight.** This is the limit for a bike rack or cargo carrier: 270 lb on the 2.5-liter and "
           "350 lb on the turbo, per the dealer listing. CURT's and Draw-Tite's hitches are rated at 350 lb or "
           "more, so the limit is the Outback's.\n\n"
           "**Wilderness.** The dealer listing says a Wilderness-specific bumper fascia panel and a cutting "
           "template are required, both sold separately, and that the hitch is not compatible with the rear bumper "
           "underguard.",
   "table": {"caption": "2020–2025 Outback towing by engine (Subaru's figures; your owner's manual is the authority)",
             "head": ["Outback", "Engine", "Max tow", "Max tongue weight", "Hitch notes"],
             "rows": [
              ["Base, Premium, Limited, Touring; Onyx Edition from 2023", "2.5 L, 182 hp", "2,700 lb", "270 lb", "CURT's and Draw-Tite's ratings exceed the vehicle's"],
              ["Onyx Edition XT, Limited XT, Touring XT", "2.4 L turbo, 260 hp", "3,500 lb", "350 lb", "CURT's 13494 and 13570 match it; Draw-Tite's 76597 exceeds it"],
              ["Wilderness (2022–2025)", "2.4 L turbo, 260 hp", "3,500 lb", "350 lb", "Own rear fascia; Subaru's kit needs a panel and a cutting template"],
             ]}},
  {"h": "Model years: the 2023 refresh, the 2015–2019 Outback, the Legacy and the 2026 redesign",
   "body": "Our vehicle data and all four guides treat 2020–2025 as one generation. Four kinds of listing blur "
           "that.\n\n"
           "**The 2023 refresh.** Wikipedia describes it as a new front fascia, new headlights and additional front "
           "cladding on every model except the Wilderness. None of the four guides found a part that splits at "
           "2023: Husky lists 95541 for 2020–2025 and CURT lists the 13494 for 2020–2026.\n\n"
           "**The 2015–2019 generation.** Liners don't carry over, and Husky's Outback cargo liner 28801 is listed "
           "for 2015–2019, not this generation. The Thule crossbar kit in the roof rack guide is titled 2010–2023, which reaches "
           "back past this generation and stops short of 2024, so confirm 2024 and 2025 with the seller. The Amazon "
           "listing for Subaru's hitch names 2020–2024; confirm a 2025 by VIN.\n\n"
           "**The 2026 Outback.** It is a new generation with new rails and its own factory hitches, L101SAR000 and "
           "L101SAR001. CURT's 13494, Draw-Tite's 76597 and the TUZILLA hitch are listed through 2026, while several "
           "Wilderness crossbar listings say NOT for 2026.\n\n"
           "**The Legacy.** The 2020–2025 sedan shares the Outback's platform. Most liner sets and CURT's two "
           "hitches name both. The sedan's tow rating is its own."},
  {"h": "Roof or hitch: where the weight goes, what isn't ranked and the order to fit things",
   "body": "The Outback is a wagon with no bed, so cargo that won't fit inside goes on the roof or behind the "
           "bumper. Subaru's numbers favor the hitch for heavy things. A 2.5-liter Outback allows 270 lb on the "
           "receiver against 150 lb on the roof, and a turbo allows 350 lb. The cargo box guide makes the same call and "
           "points owners to a hitch carrier for coolers and other heavy items.\n\n"
           "Height is the other roof cost. Subaru lists 8.7 in of ground clearance on standard trims and 9.5 in on "
           "the Wilderness, and the boxes in the guide stand 15 to 19 in tall on top of the bars. Measure before "
           "driving into a garage.\n\n"
           "This page ranks the four categories that have a fit-checked Outback guide on this site. Running boards, "
           "lighting and bike racks have none for this vehicle, so they aren't ranked and no products are named for "
           "them.\n\n"
           "Fit the four in this order.\n\n"
           "1. **Floor liners.** No tools. Remove the factory mat, hook the driver liner onto Subaru's retention "
           "hooks and press both pedals to the floor.\n"
           "2. **Trailer hitch.** Draw-Tite quotes about 60 minutes with no drilling for the 76597. Fit the plug-in "
           "wiring harness the same day.\n"
           "3. **Crossbars.** On a standard trim, stow the factory bars along the rails first. Set the spread to "
           "suit the box and recheck the clamps after the first drive.\n"
           "4. **Cargo box.** Mount it forward, clear of the sunroof, and open the rear gate slowly the first time."},
 ],
 "avoid": [
  {"h": "Wilderness crossbars on a standard Outback, or the reverse", "body": "The rails are different shapes. Buy bars titled for raised rails on standard trims and bars titled \"Only Fit Wilderness\" for the ladder rails."},
  {"h": "Loading the roof to the bar or box rating", "body": "A 330 lb bar or a 165 lb box rating doesn't change Subaru's 150 lb figure for the retractable-crossbar roof or the Wilderness's 200 lb driving figure. The 700 lb number is for a parked Wilderness."},
  {"h": "Towing to the hitch rating", "body": "A 4,500 lb hitch on a 2.5-liter Outback is still a 2,700 lb, 270 lb setup. Read the badge: an Onyx Edition without XT has the 2.5-liter."},
  {"h": "Listings for the wrong years", "body": "2015–2019 liners don't fit the 2020 floor, the 2026 Outback has new rails and its own factory hitches, and some titles stop at 2023 or 2024."},
 ],
 "verdict": {
  "thesis": "On the 2020–2025 Outback, buy floor liners by generation first, add a 2 in trailer hitch and plan loads around your engine's rating, buy crossbars only as the roof type requires, and leave the cargo box for last.",
  "body": "The sixth-generation Outback is easy to accessorize once four facts are written down: model year, "
          "engine, Wilderness or not, and whether a receiver is already fitted. Floor liners need only the year, "
          "since every trim shares one floor, and they cost the least. A trailer hitch needs the engine and the "
          "trim, costs about $130–$320 from the aftermarket and gives the wagon a 270 or 350 lb carrying point that "
          "the roof can't match.\n\n"
          "The roof rack is third because most trims carry their own crossbars, and the Wilderness, which carries "
          "none, needs bars made for its ladder rails. The cargo box is last because it costs the most and has to "
          "fit both the bar spread and a roof figure of 150 lb on standard trims or 200 lb while driving on the "
          "Wilderness, per Subaru's 2022 and 2025 spec sheets. Each linked guide covers the fit details for its own "
          "category.",
 },
 "sources": [
  ["2025 Outback trim comparison: engines, towing, roof rails and roof capacity by trim (Subaru)", "https://www.subaru.com/services/vehicles/pdf/trimComparison/2025/OBK"],
  ["2022 Outback trim comparison: towing and roof capacity by trim (Subaru)", "https://www.subaru.com/services/vehicles/pdf/trimComparison/2022/OBK"],
  ["Subaru debuts 2022 Outback Wilderness: ladder-type roof rack, 700 lb static limit (Subaru U.S. Media Center)", "https://media.subaru.com/newsrelease.do?fIId=1724&id=1762&mid="],
  ["Subaru Outback: sixth generation, Wilderness, 2023 refresh, 2026 seventh generation (Wikipedia)", "https://en.wikipedia.org/wiki/Subaru_Outback"],
  ["Subaru L101SAN000 trailer hitch: class, ratings by engine, Wilderness notes (Subaru Parts Pros)", "https://www.subarupartspros.com/sku/l101san000.html"],
  ["CURT 13494 Class 3 hitch (CURT)", "https://www.curtmfg.com/part/13494"],
  ["CURT 13570 Class 3 hitch (CURT)", "https://www.curtmfg.com/part/13570"],
  ["Draw-Tite 76597 Class III hitch (Draw-Tite)", "https://www.draw-tite.com/product/76597_class-3-trailer-hitch"],
  ["Outback roof rack driveway test (Autoblog)", "https://www.autoblog.com/2020/10/15/subaru-outback-roof-rack-driveway-test/"],
  ["2020–2025 Outback Yakima SkyLine kit (The Rack Shop)", "https://therackshop.com/2020-2025-subaru-outback-w-raised-rails-yakima-crossbar-complete-roof-rack-1/"],
  ["Yakima SkyBox 16 Carbonite (Yakima)", "https://yakima.com/collections/roof-boxes/products/skybox-16-carbonite-2014-2023"],
  ["Yakima DeepSpace 10 (Yakima)", "https://yakima.com/collections/roof-boxes/products/deepspace-10"],
  ["Thule Motion 3 XL (Thule)", "https://www.thule.com/en-us/cargo-carrier/car-top-carrier/thule-motion-3-xl-_-639850"],
  ["SportRack Vista XL mounting positions (etrailer)", "https://www.etrailer.com/question-156482.html"],
  ["Husky Liners: WeatherBeater vs X-act Contour (Husky Liners)", "https://huskyliners.com/blog/husky-liners-weatherbeater-vs-xact-contour/"],
 ],
}
