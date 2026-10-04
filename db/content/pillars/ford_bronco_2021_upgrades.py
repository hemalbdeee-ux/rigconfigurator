"""Upgrades pillar: 2021–2026 Ford Bronco (6th gen, U725; the body-on-frame Bronco, not the Bronco Sport).
Hub page: ranks the four published Bronco category guides and links to them. No product picks or ASINs here
(the site pulls each guide's #1 pick). Every price band comes from the linked guides' picks[].price fields;
vehicle facts from db/migrations/003_vehicles.sql (SUV, 2-door and 4-door, removable hardtop / soft top, tailgate
spare, hitch class 2 with a 2 in receiver, 3,500 lb, no stored roof load figure, Raptor / Badlands / Sasquatch
variants), the four guides and their sources, and five pages opened for this page on 2026-10-03: Wikipedia's
sixth-generation Bronco page (100.4 / 116.1 in wheelbases, rubberized flooring with drain plugs on Black Diamond,
steel front bumper on Black Diamond and Badlands, heavy-duty modular front bumper on Everglades and Raptor,
Raptor 4,500 lb, Everglades and Raptor added for 2022), Ford's 2026 Bronco page (hard top standard on the 2-door,
soft top standard on the 4-door, dual-top option, 3,500 / 4,500 lb, "Class II Trailer Tow Package", non-Raptor
models need additional equipment such as the available Trailer Tow Prep Package, Raptor tow package standard,
washout-capable rubberized flooring), The Drive's 2021 roof article (same standard-top split at launch), Ford's
accessory page for hitch assembly MB3Z19D520K (2 in receiver, no class or rating, harness sold separately) and
the Bronco6G roof-load thread (started July 2020; 110 lb dynamic / 450 lb static from a Ford spec sheet; posters
disagree on what the 110 lb covers). Ford's 2020 Bronco press release could not be opened and is not cited.
Not verified, and worded as such in the text: which trims and years ship with a factory receiver, and its class
and rating (the vehicle data and Ford's page say Class II, the guide's aftermarket hitches are Class III / Class 3,
Ford publishes no rating for its own kit); whether tow-prep wiring is on every Bronco (Bronco6G owners say standard,
Ford's 2026 page lists a Trailer Tow Prep Package as available equipment); the roof load limit from a Ford document
(110 / 450 lb is owner-cited, some threads say 100 lb); which trims and years have the rubberized floor, a steel,
modular or plastic front bumper, the upfitter switches outside the launch year, or a factory roof rack; whether
Baja's steel-bumper fog pocket kit suits a Raptor's bumper; 2-door fit of the brand-name hitches whose listings
give no door count; Rough Country's rack weight; how the soft top folds under DV8's RRBR-01; and 2026 fit of
listings whose titles stop at 2024 or 2025. No Bronco guide exists for running boards, cargo boxes or bike racks;
none are ranked.
Source fixes 2026-10-04: the vehicle data summary now gives the Raptor's 4,500 lb and describes roof rack mounting as
the roof guide does; the roof guide's Bronco Sport trim-name tip was removed.
"""

KIND = "upgrades"
KEY = ("ford", "bronco", "2021-present")
CATEGORIES = ["floor-mats", "hitches", "roof-racks", "led-light-bars"]

TITLE = "2021–2026 Ford Bronco Upgrades, Ranked: 4 Mods in Order, With Door-Count and Top-Type Fit Traps"
META = ("Four 2021–2026 Bronco upgrades in buying order: floor liners, trailer hitch, roof rack and light bar, with "
        "2-door, soft-top, tow package and Bronco Sport traps.")

FAQ = [
 ("What should I upgrade first on a 2021–2026 Ford Bronco?",
  "Floor liners, then a trailer hitch. Liners cost the least, about $70–$210 across the cabin sets in our guide, and "
  "with the doors and roof off, weather lands in the footwells. A hitch comes second: about "
  "$130–$352, and it carries bikes or a cargo tray without touching the Bronco's small roof limit. The "
  "roof rack is third because the right one depends on door count and top type. Lighting is last, since most of it "
  "is off-road light. First confirm every listing says Bronco, not Bronco Sport."),
 ("Does every Ford Bronco come with a trailer hitch from the factory?",
  "No. Owners on Bronco6G report that the receiver comes only when the Trailer Tow Package was ordered, and one "
  "Badlands with the Sasquatch package in that thread had no hitch. Ford's 2026 Bronco page says most models need "
  "additional equipment to hitch up a trailer and that the Raptor includes an upgraded tow package. Look "
  "under the rear bumper for a square 2 in opening. If a receiver is there, you need only a ball mount and perhaps a "
  "wiring harness."),
 ("How much can a 2021–2026 Bronco tow, and does an aftermarket hitch raise it?",
  "A hitch never raises it. Our vehicle data lists a 3,500 lb maximum, and Ford's 2026 page says most Broncos can tow "
  "up to 3,500 lb and the Raptor up to 4,500 lb. Our hitch guide found lower figures for some builds: 3,460 lb on "
  "some 2.7L Broncos in dealer charts, and 3,080 lb for a 2024 Everglades in an etrailer expert answer. The maximum "
  "varies with engine, trim, package and model year, so use the towing chart in your owner's manual. The lower of "
  "vehicle and hitch rating applies."),
 ("Can I put a roof rack on a Bronco with the soft top?",
  "Yes, but only a rack built for it. A soft top can't carry load, so the rack has to bolt to the factory attachment "
  "points and bridge over the fabric. The one pick in our roof rack guide that does this is DV8's RRBR-01, about "
  "$1,200, listed for 4-door Broncos with the factory soft top. DV8 rates it at 200 lb evenly distributed while "
  "driving, lists it at about 31 lb and excludes the Raptor and Everglades. Its pages don't say how the top folds "
  "with the rack fitted, so ask the seller."),
 ("How much weight can a Bronco roof carry with a rack or a rooftop tent?",
  "Less than the rack's rating suggests. Owners on Bronco6G quote Ford's figures as 110 lb dynamic (driving) "
  "and 450 lb static (parked). Some threads mention 100 lb, and posters disagree on whether the "
  "110 lb covers the roof panels or the whole roof, so confirm it in your owner's manual. The rack's own weight "
  "counts against the driving figure. Hooke Road's 4-door rack is about 67 lb, which leaves about 43 lb. One owner "
  "notes a Yakima rooftop tent at 101.4 lb."),
 ("Will 4-door Bronco accessories fit a 2-door Bronco?",
  "It depends on the category. Floor liners: no. Every set in our guide is cut for the 4-door, and the 2-door's "
  "shorter rear area needs its own rear piece. Roof racks: mostly no. Full platforms fit one hardtop length, so "
  "Hooke Road sells a separate 2-door rack at about $450, though the Wonderdriver crossbar kit is listed for both. "
  "Hitches: the Snailfly listing names both, but most listings give "
  "no door count, so ask. Lights: our guide lists the A-pillar mount for 2-door and 4-door Broncos."),
 ("Do Bronco Sport floor mats, hitches, racks or lights fit the Bronco?",
  "No, in all four categories. The Bronco Sport is a smaller unibody crossover on a different platform with a fixed "
  "roof, and makers sell separate parts for it. Husky's liners are "
  "95301 for the Bronco 4-door and 95341 for the Sport. Draw-Tite's hitch is 76436 for the Sport and 76527 or 76605 "
  "for the Bronco. Rigid's Bronco Sport roof light kit carries the code CX430 in its title. Buy only listings that "
  "name the Bronco with a door count or say \"not Bronco Sport\"."),
 ("Does the washout rubberized floor change which Bronco floor liners fit?",
  "Yes. Some Broncos have washable rubberized flooring with drain plugs in place of carpet. Wikipedia lists it on the "
  "Black Diamond trim, and Ford's 2026 page describes washout-capable rubberized flooring. We could "
  "not confirm a full list of trims and years, so look at your own floor. 3W's floor-and-cargo kit is listed as not "
  "for the rubberized floor. Husky's StayPut nibs are designed for carpet. "
  "Our guide points these owners to heavy rubber mats such as Lwope's."),
 ("Are LED light bars street legal on a Ford Bronco?",
  "Usually not while driving on public roads, and it depends on your state. Our lighting guide relies on KC HiLiTES' "
  "guidance: off-road-only lights must be off on the roadway, many states also require an opaque cover, and states "
  "commonly limit how many auxiliary lamps you can run and how high they sit. "
  "SAE-marked fog lamps, such as the Squadron SAE lights in Baja's fog pocket "
  "kit, are designed for road use. This is not legal advice. Check your own state's rules first."),
 ("How much does it cost to add all four upgrades to a Bronco?",
  "From the prices on our four guides' picks, a budget build runs about $870–$1,050: Lwope rubber mats, a Snailfly or "
  "Rough Country receiver, a Wonderdriver crossbar kit and Baja's Squadron Pro A-pillar kit. "
  "A mid build runs about $1,697–$1,857 with LASFIT liners, CURT's 13493, a Hooke Road "
  "platform and Baja's XL80 kit. A premium build with Husky's WeatherBeater set, a Draw-Tite hitch or Ford's kit, a "
  "DV8 rack and Rigid's roof kit or Baja's fog pocket kit runs about $2,430–$2,929. Wiring and a cargo liner are "
  "extra."),
]

ARTICLE = {
 "dek": "Four upgrades for the sixth-generation Bronco, in buying order. Fit on this "
        "SUV turns on a handful of facts: two doors or four, soft top or hardtop, carpet or a washout floor, whether "
        "the tow package was ordered, and which front bumper is fitted. Every category also has Bronco Sport parts "
        "mixed into its search results.",
 "author": "jake-morrison",
 "reviewed": "2026-10-03",
 "method": "We did not install any of these parts ourselves. The order comes from our four fit-checked 2021–2026 "
           "Bronco guides, weighing how many Broncos each upgrade suits, what it costs and how "
           "much can go wrong with fit (door count, top, floor, bumper, tow package, model year). Price bands are the "
           "prices listed on those guides' picks, checked at maker and retailer stores in September 2026, and are "
           "approximate. Vehicle facts come from our vehicle data, the guides' sources, Wikipedia's sixth-generation "
           "Bronco page, Ford's 2026 Bronco page and Ford's accessory store. Where the sources disagree, or where we "
           "couldn't confirm a factory detail, the text says so.",
 "takeaways": [
  "**Bronco, not Bronco Sport.** The Sport is a different vehicle, and its liners, hitches, racks and light kits don't fit.",
  "**Count the doors and look at the top.** Every liner set in our guide is 4-door, and a roof rack fits one door count and one top type.",
  "**Look under the rear bumper before hitch shopping.** Owners report the receiver comes only with the Trailer Tow Package.",
  "**The roof carries little.** Owners cite Ford's limits as 110 lb while driving and 450 lb parked, and the rack's own weight counts.",
  "**Lights go last.** Roof kits depend on the rack and bumper kits on the bumper. Most of it is off-road light, so check your state's rules.",
 ],
 "priority": [
  {"category": "floor-mats",
   "h": "1. Floor liners first: the cabin that gets rained in",
   "why": "Floor liners lead on the Bronco because they cost the least and because the doors and the roof come "
          "off. With the doors off, rain, dust and trail spray land straight in the footwells. Three facts decide fit. First, the listing must name the Bronco and "
          "not the Bronco Sport; Husky sells 95301 for the Bronco 4-door and 95341 for the Sport. Second, door count. "
          "Every set in our guide is cut for the 4-door, and the 2-door's shorter rear area needs its own rear piece. "
          "Third, the floor. Some Broncos have washable rubberized flooring with drain plugs instead of carpet, and "
          "3W's floor-and-cargo kit is listed as not for that floor. Prices in our guide run about $70–$110 for "
          "Lwope's rubber mats, about $110–$150 for LASFIT's TPE set, about $150–$200 for 3W's kit with a cargo liner "
          "and about $150–$210 for Husky's WeatherBeater 95301, which Husky says is made in the USA with a lifetime "
          "warranty against cracks and breaks. The trade-off is firm, tall walls against softer TPE with a lower lip.",
   "skip_if": "You have the washout floor, hose the cabin out after every trip and are content to rely on the drain plugs."},
  {"category": "hitches",
   "h": "2. Trailer hitch second: cheap, simple to fit, and it keeps weight off the roof",
   "why": "A trailer hitch ranks second because it costs little, suits nearly every Bronco and moves weight off a "
          "roof that can carry very little. Most hitches in our guide are listed for the 2021–2026 Bronco, and the "
          "budget Snailfly listing names both the 2-door and the 4-door. The first check is whether you need one. "
          "Owners on Bronco6G report the factory receiver comes only with the Trailer Tow Package, whatever the trim, "
          "so look under the rear bumper. The second check is the rating. Most Broncos are rated at up to 3,500 lb and the Raptor at "
          "4,500 lb, so a Raptor needs Draw-Tite's 76527 or 76605, rated 4,500 lb with 675 lb of tongue weight. "
          "CURT's 13493 is rated 3,500 lb and 350 lb. Prices run about $130–$200 for the Snailfly and Rough Country "
          "receivers, about $200–$270 for the CURT, about $200–$280 for the Draw-Tite and about $352 for Ford's own "
          "kit. The trade-off is the spare, which hangs on the swing-out tailgate above the receiver, so a loaded hitch "
          "rack can block the gate.",
   "skip_if": "A square 2 in receiver is already bolted under your rear bumper."},
  {"category": "roof-racks",
   "h": "3. Roof rack third: bought by door count and top, limited by the roof",
   "why": "A roof rack ranks third because it is the hardest of the four to buy right. Two facts pick the rack before brand does: two doors or four, and hardtop or "
          "soft top. Full platforms are cut for one hardtop length. Rough Country's 88202, Hooke Road's Discovery and "
          "DV8's RRBR-02 are 4-door hardtop parts, Hooke Road sells a separate 2-door rack, and a soft top needs a "
          "bridging rack such as DV8's RRBR-01. Ford lists the soft top as the 4-door's standard top, so look up "
          "before shopping. Owners on Bronco6G quote Ford's roof figures as 110 lb while driving "
          "and 450 lb parked, and the rack's weight counts against the first number. Prices in our guide run about "
          "$150–$220 for a Wonderdriver crossbar kit, about $450–$500 for Hooke Road's platforms, from about $500 for "
          "Rough Country's half rack, about $1,000 for DV8's hardtop rack and about $1,200 for its soft-top rack. The "
          "other trade-off is the open roof: a platform bolted across the front panels ties them down.",
   "skip_if": "Everything you carry fits behind the rear seat or on a hitch carrier, or you take the top off most weekends."},
  {"category": "led-light-bars",
   "h": "4. Lighting last: mostly off-road light, and the mount decides fit",
   "why": "Lighting comes last for three reasons. Most of it is off-road light. It has the highest entry price in our guides, from "
          "about $520. And the roof-mounted options depend on the rack decision above: Rigid sells its 40 in SR kit "
          "as a roof-line version, 46724, and a version for the factory roof rack, 46726, while DV8's racks accept "
          "40 in and 50 in light bar mounts. We could not confirm which Broncos have that factory rack. The light bar itself is mostly universal; the mount is what has to match the "
          "Bronco. Baja Designs lists its A-pillar kits for the 2021–2026 Bronco and the 2022–2026 Bronco "
          "Raptor with no cutting or drilling. Its six-light fog pocket kit is for the OE steel bumper only. "
          "Prices run from about $520 for Baja's Squadron Pro A-pillar kit, "
          "from about $937 for the XL80 A-pillar kit, about $1,080 for Rigid's 40 in roof kit and from about $1,167 "
          "for the fog pocket kit; Hooke Road's 50 in windshield brackets are priced on the listing. KC HiLiTES says "
          "off-road lights must be off on the roadway, and that many states also require covers.",
   "skip_if": "You don't drive unlit trails or dirt roads at night, where an off-road light is allowed to be on."},
 ],
 "tier_table": {
  "caption": "Approximate price bands from the picks in our 2021–2026 Bronco guides (September 2026; Amazon prices move daily)",
  "head": ["Upgrade", "Budget", "Mid", "Premium"],
  "rows": [
   ["Floor liners", "About $70–$110 (Lwope rubber mats, 4-door)", "About $110–$150 (LASFIT TPE, 4-door)", "About $150–$210 (Husky WeatherBeater 95301, 4-door); the 23321 cargo liner is about $100–$150 more"],
   ["Trailer hitch", "About $130–$190 (Snailfly) or $130–$200 (Rough Country, 3,500 lb)", "About $200–$270 (CURT 13493, 3,500 lb)", "About $200–$280 (Draw-Tite 76527, 4,500 lb) or about $352 (Ford receiver kit)"],
   ["Roof rack", "About $150–$220 (Wonderdriver crossbar kit, hardtop)", "About $450 (Hooke Road 2-door rack) or about $500 (Hooke Road 4-door Discovery)", "About $1,000 (DV8 RRBR-02, hardtop) to $1,200 (DV8 RRBR-01, soft top)"],
   ["Lighting", "About $520 (Baja Squadron Pro A-pillar kit); Hooke Road's 50 in brackets are priced on the listing", "About $937 (Baja XL80 A-pillar kit)", "About $1,080 (Rigid 40 in SR roof kit) to $1,167 (Baja six-light fog pocket kit, steel bumper)"],
   ["Total", "About $870–$1,050", "About $1,697–$1,857", "About $2,430–$2,929; wiring and cargo liner extra"],
  ],
 },
 "sections": [
  {"h": "Two doors or four, soft top or hardtop: settle this before anything else",
   "body": "The Bronco is sold as a 2-door and a 4-door, and Wikipedia lists their wheelbases at 100.4 in and "
           "116.1 in. That gap is why few parts fit both. Hooke Road's 2-door platform is 86.5 in long and its 4-door "
           "Discovery about 102.1 in.\n\n"
           "The top is the second variable, and the trim badge won't tell you which one you have. Ford's 2026 Bronco "
           "page says 2-door models come with a standard hard top and 4-door models with a standard soft top, with a "
           "dual-top option for any model. The Drive reported the same split at the 2021 launch. Look at the roof "
           "itself.\n\n"
           "Six of the seven picks in our roof rack guide need a hardtop, and the seventh, DV8's soft-top rack, is "
           "4-door only. Floor liners follow door count only. "
           "Hitches and A-pillar lights are the least affected.",
   "table": {"caption": "2021–2026 Bronco body and top combinations, and what our guides list for each",
             "head": ["Bronco", "Floor liners", "Roof rack", "Hitch and lights"],
             "rows": [
              ["4-door, hardtop", "Every set in our guide", "Full or half platforms and crossbar kits", "Any hitch matched to the rating; A-pillar, roof-line and bumper kits"],
              ["4-door, soft top (Ford's standard 4-door top)", "Same 4-door sets", "DV8 RRBR-01 bridging rack only; not Raptor or Everglades", "Same hitches; A-pillar or bumper lights, since roof-line kits are listed for hardtops"],
              ["2-door, hardtop (Ford's standard 2-door top)", "None of our picks; buy a 2-door set", "Hooke Road 2-door rack, or a crossbar kit that names the 2-door", "Snailfly names the 2-door; ask other sellers"],
              ["Painted body-color hardtop", "By door count", "Hooke Road says the 4-door Discovery works with it; ask other makers", "No change"],
             ]}},
  {"h": "The hitch: look for a factory receiver, then read the right rating",
   "body": "**The receiver.** Owners on Bronco6G report that the hitch comes only when the Trailer Tow Package was "
           "ordered. Ford's 2026 Bronco page says its non-Raptor models need additional equipment to hitch "
           "up a trailer, and that the Raptor includes an upgraded tow package as standard. Look under "
           "the rear bumper.\n\n"
           "**The class.** Our sources label the same 2 in opening differently. Our vehicle data records the Bronco's "
           "hitch as Class II with a 2 in receiver, and Ford's 2026 page, as we read it, calls the factory option a "
           "Class II Trailer Tow Package. The aftermarket hitches in our guide are sold as Class III or Class 3. "
           "Ford's accessory page for its own kit, MB3Z19D520K, gives a 2 in receiver and no class or rating. An "
           "etrailer expert answer puts the factory hitch at 3,500 lb with 350 lb of tongue weight; we could not "
           "confirm that from Ford. Read the label on the hitch itself.\n\n"
           "**The rating.** Our vehicle data lists a maximum of **3,500 lb** for most models. Ford's page and Wikipedia put the Raptor at **4,500 lb**. Our hitch guide also found 3,460 lb on some 2.7L "
           "builds and 3,080 lb for a 2024 Everglades. The maximum varies by engine, trim, package and model year, "
           "and the lower of vehicle and hitch applies. Tongue weight differs most: 675 lb on the Draw-Tite, 350 lb "
           "on the CURT and Rough Country.\n\n"
           "**The wiring.** Bronco6G owners report that tow-prep wiring is standard, while Ford's 2026 page lists a "
           "Trailer Tow Prep Package as available equipment, so we could not confirm what every Bronco has. Ford says "
           "its hitch kit requires a wiring harness sold separately, and owners note that a hitch added later doesn't "
           "bring the factory trailer brake controller.\n\n"
           "**The spare.** It hangs on the side-hinged tailgate above the receiver. Draw-Tite's 76527 is the extended "
           "length and the 76605 the standard length, at the same rating. CURT says its 13493 isn't compatible with "
           "vertical-hanging bike racks."},
  {"h": "A 110 lb roof: why the hitch outranks the rack",
   "body": "The roof limit is the main reason the trailer hitch sits above the roof rack on this page. Owners on "
           "Bronco6G quote Ford's figures as **110 lb dynamic and 450 lb static**. The "
           "thread our roof rack guide cites dates from July 2020 and quotes a Ford spec sheet, and posters in it "
           "disagree on whether the 110 lb covers the roof panels only or the whole roof. Other threads mention "
           "100 lb. Our vehicle data holds no roof load figure for the Bronco, and we could not confirm one from a "
           "Ford page. Your owner's manual is the authority.\n\n"
           "Taking 110 lb as the working number, the rack's own weight comes off it first:\n\n"
           "- **Hooke Road 4-door Discovery:** about 67 lb, which leaves about 43 lb for cargo.\n"
           "- **Hooke Road 2-door rack:** about 62 lb, leaving about 48 lb.\n"
           "- **DV8 RRBR-02 hardtop rack:** about 53 lb, leaving about 57 lb.\n"
           "- **DV8 RRBR-01 soft-top rack:** about 31 lb, leaving about 79 lb.\n"
           "- **Rough Country 88202, full or half:** weight not published. Ask before planning a load.\n\n"
           "A rack's own rating, from 200 lb while driving on DV8's racks to 800 lb evenly distributed on Hooke "
           "Road's Discovery, doesn't change this. The lower number wins.\n\n"
           "So crossbars or a half rack make more sense here than on most SUVs, and a rooftop tent is a parked load. "
           "Our roof rack guide itself points owners to a hitch-mounted cargo carrier for heavy items.\n\n"
           "The roof also comes apart, and a rack can end that. Rough Country lists its rear-section half rack as "
           "Freedom Top compatible. Hooke Road says its 4-door Discovery lets you remove the front and middle "
           "panels and that its 2-door rack keeps the front panels removable. Ask other makers."},
  {"h": "Bumper, switches and badge: the variants that change the plan",
   "body": "Trim changes little about liners or hitches. It matters for lights, for one roof rack and "
           "for the tow rating. Bumper type is the detail we could pin down least. Wikipedia lists a powder-coated "
           "steel front bumper on the Black Diamond and Badlands and a heavy-duty modular front bumper on the "
           "Everglades and Raptor. "
           "Baja Designs lists its fog pocket kit for the Bronco and the Bronco Raptor, but for the "
           "OE steel bumper only, not plastic or modular bumpers. Those statements don't line up for the "
           "Raptor, so go by the bumper on your Bronco and ask Baja before ordering.",
   "table": {"caption": "2021–2026 Bronco variants that change the upgrade plan",
             "head": ["Bronco", "What it has", "What changes"],
             "rows": [
              ["Bronco Raptor (2022 on)", "4-door; rated 4,500 lb; tow package standard per Ford's 2026 page; modular front bumper per Wikipedia", "A 4,500 lb hitch if one is added; DV8's soft-top rack excludes it; confirm fog pocket kit and liner fit"],
              ["Everglades (added for 2022)", "Modular front bumper per Wikipedia; 3,080 lb cited for a 2024", "DV8's soft-top rack excludes it; the fog pocket kit is not for modular bumpers"],
              ["Black Diamond, Badlands", "Steel front bumper per Wikipedia; rubberized floor with drain plugs on Black Diamond", "Candidates for Baja's fog pocket kit; 3W's liner kit is not for the rubberized floor"],
              ["Sasquatch package", "Mild lift and 35 in tires; not a tow package", "Larger tailgate spare, so measure hitch-rack clearance; the hardtop is unchanged"],
              ["Overhead upfitter switches", "One 30 A, one 15 A and four 10 A circuits; standard on Black Diamond, Wildtrak and Badlands at launch, optional on Base and Outer Banks (Ford Authority)", "Buy upfitter harness versions; Rigid's 18.5 A bar needs the 30 A circuit or its own relay"],
              ["2025–2026 model years", "Several titles stop at 2024 or 2025", "Confirm Husky 95301 and 23321, LASFIT, Lwope and Rough Country's hitch; Baja's own pages list 2021–2026"],
             ]}},
  {"h": "What isn't ranked, and the order to fit the four that are",
   "body": "This page ranks the four categories that have a fit-checked Bronco guide on this site. Running "
           "boards, cargo boxes and bike racks have none yet, so they aren't ranked and no products are named for "
           "them.\n\n"
           "Fit the four in this order.\n\n"
           "1. **Floor liners.** No tools. Hook the driver liner onto the retention posts and press every pedal to "
           "the floor.\n"
           "2. **Trailer hitch.** The TrailBronco write-up of a Rough Country install removed two 13 mm body-mount "
           "bolts and four 18 mm bolts under the bumper. Draw-Tite quotes 20 minutes with no drilling; CURT's "
           "documentation says drilling and trimming may be required.\n"
           "3. **Roof rack.** Our guide puts hardtop racks at 1 to 1.5 hours and DV8's soft-top rack at about 3 hours "
           "with two people.\n"
           "4. **Lights.** They go last because the rack can be the mount. Our lighting guide's rule is a relay, a "
           "fuse and a switch, or an upfitter harness matched to the circuit."},
 ],
 "avoid": [
  {"h": "Bronco Sport listings", "body": "The Sport is a different vehicle in all four categories. Husky's 95341 liners, Draw-Tite's 76436 hitch and Rigid's CX430 light kit are Sport parts."},
  {"h": "A 4-door hardtop part on a 2-door or a soft top", "body": "Every liner set in our guide is 4-door, full platforms fit one hardtop length, and a soft top can't carry crossbars or cargo."},
  {"h": "Loading the roof to the rack's rating", "body": "An 800 lb rack doesn't change the 110 lb driving limit owners cite. Rack weight plus cargo has to fit under the figure in your owner's manual."},
  {"h": "A hitch bought before looking under the bumper", "body": "Tow-package Broncos already have a receiver. On a Raptor, a 3,500 lb hitch becomes the limit."},
 ],
 "verdict": {
  "thesis": "On the 2021–2026 Bronco, buy floor liners by door count and floor type first, add a trailer hitch rated for your build if no receiver is fitted, choose a roof rack by doors and top, and leave lighting for last.",
  "body": "The Bronco is easy to accessorize once six facts are written down: Bronco or Bronco Sport, two doors or "
          "four, soft top or hardtop, carpet or rubberized floor, receiver or no receiver, and which front bumper is "
          "fitted. Floor liners need three of those and cost the least, so they go first. A trailer hitch needs one "
          "look under the bumper and one rating check, costs about $130–$352, and gives the Bronco a place to carry "
          "weight that the roof can't.\n\n"
          "The roof rack is third because it has the most ways to go wrong: door count, top type, panel removal and "
          "a driving limit that owners cite at 110 lb. A light bar or pod kit is fourth because most of it is "
          "off-road light, and because roof mounts should follow the rack decision. Each linked guide covers the "
          "fit details for its own category.",
 },
 "sources": [
  ["Ford Bronco (sixth generation): body styles, wheelbases, doors, trims, bumpers, towing (Wikipedia)", "https://en.wikipedia.org/wiki/Ford_Bronco_(sixth_generation)"],
  ["2026 Ford Bronco: standard tops, towing, Trailer Tow equipment, flooring, upfitter switches (Ford)", "https://www.ford.com/suvs/bronco/"],
  ["This Is How You Take the 2021 Ford Bronco's Doors and Roof Off (The Drive)", "https://www.thedrive.com/new-cars/41301/this-is-how-you-take-the-2021-ford-broncos-doors-and-roof-off"],
  ["Do all 2025 Broncos come with a hitch? (Bronco6G)", "https://www.bronco6g.com/forum/threads/do-all-2025-broncos-come-with-a-hitch.129087/"],
  ["Bronco 2021-2026 Trailer Hitch Assembly MB3Z19D520K (Ford Accessories)", "https://www.ford.com/product/trailer-hitch-assembly-p2844192355"],
  ["OEM vs Draw-Tite Bronco hitch rating (etrailer expert answer)", "https://www.etrailer.com/question-796075.html"],
  ["Draw-Tite 76527 Class III Trailer Hitch (Draw-Tite)", "https://www.draw-tite.com/product/76527_class-iii-trailer-hitch"],
  ["CURT 13493 Class 3 Trailer Hitch (CURT)", "https://www.curtmfg.com/part/13493"],
  ["Dynamic roof load limit of 110 lbs (Bronco6G)", "https://www.bronco6g.com/forum/threads/dynamic-roof-load-limit-of-110-lbs.1840/"],
  ["Rough Country Ford Bronco roof rack 88202 (Rough Country)", "https://www.roughcountry.com/product/configurable/ford-bronco-roof-rack-88202"],
  ["Hooke Road Discovery roof rack, 2021–2026 Bronco 4-door hardtop (Hooke Road)", "https://www.hookeroad.com/products/bronco-discovery-roof-rack-ford-21-23-4-door-hardtop-b8906s"],
  ["DV8 Offroad soft top roof rack RRBR-01 (ExtremeTerrain)", "https://www.extremeterrain.com/dv8-offroad-bronco-soft-top-roof-rack-rrbr-01.html"],
  ["Squadron SAE / Dual S2 Sport Steel Bumper Fog Pocket Kit, Bronco (Baja Designs)", "https://www.bajadesigns.com/products/ford-squadron-sae-dual-s2-sport-fog-pocket-light-kit-ford-2021-on-bronco-bronco-raptor-2022-on-note-steel-bumper/"],
  ["2021 Ford Bronco pre-wired upfitter switch details (Ford Authority)", "https://fordauthority.com/2021/05/2021-ford-bronco-pre-wired-upfitter-switch-details-revealed/"],
  ["Are LED light bars and auxiliary lights street legal? (KC HiLiTES)", "https://www.kchilites.com/campfire/post/are-led-light-bars-and-auxiliary-lights-street-legal"],
 ],
}
