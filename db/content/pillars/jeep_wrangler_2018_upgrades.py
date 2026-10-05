"""Upgrades pillar: 2018–2026 Jeep Wrangler (JL), 2-door and 4-door Unlimited.
Hub page: ranks the three published Wrangler JL category guides and links to them. No product picks or ASINs here
(the site pulls each guide's #1 pick). Every price band comes from the linked guides' picks[].price fields;
vehicle facts from db/migrations/003_vehicles.sql (SUV, 2-door and 4-door Unlimited, removable hardtop / soft top /
Sky One-Touch, tailgate spare, factory Class II 2 in receiver on the tow package, 2,000 / 3,500 / 5,000 lb by year,
door count and trim, 4xe and 392 at 3,500 lb), the three guides and their sources, and six pages opened for this page on
2026-10-04: Wikipedia's JL page (96.8 / 118.4 in wheelbases, removable roof and doors, JL production from November
2017 with the JK built until April 27, 2018, 4xe released in 2021, Rubicon 392 from the 2021 model year, EcoDiesel
from 2020 and dropped for 2024, 2024 grille with Sport and Sport S keeping the earlier one, Gladiator based on the
JL), Jeep's 2024 Wrangler press kit (5,000 lb maximum on 4-door Rubicon 2.0L and 3.6L automatic models with 33 in
tires, Dana 44 HD full-float rear axle on Rubicon, new seven-slot grille, 12.3 in touchscreen), Jeep's 2024 pricing
release (5,000 lb tied to the Rubicon's full-float axle; as read through a text extraction: Trailer Tow with
Heavy-Duty Electrical Group standard on Willys and Rubicon, auxiliary switches standard on Rubicon, steel bumpers
available on Rubicon and standard on Rubicon X and 392, 392 4-door only), the JLwranglerforums towing thread the
hitch guide cites (started June 29, 2024; factory receivers seen are Class II at 3,500 lb; 5,000 lb is a 2024-on
Unlimited Rubicon figure; one 2024 Rubicon built with a Class II receiver), and Redwater Dodge's towing page (2-door
"2,000 – 3,500 lbs", 4-door up to 5,000 lb with the automatic, undated). Stellantis' Middle East copy of the 2024
release was also opened and is not cited.
Not verified, and worded as such in the text: any 2-door rating above 2,000 lb and any non-Rubicon 4-door rating
above 3,500 lb from a Jeep page (dealer guides list 3,500 lb for 2024-on 2-doors and 5,000 lb for properly equipped
2024-on 4-doors; our vehicle data did too until the 2026-10-04 source fix); the rating of a Rubicon on 35 in tires; whether 2025 and 2026 carry the
2024 figures; which trims and years ship with a factory receiver outside the 2024 release, and what class Jeep fits
to 5,000 lb Rubicons; where the floor drain plugs sit and whether any liner leaves an opening for them; 4xe fit of
Husky's 93921 and OEDRO's set; EcoDiesel fit of the hitches other than CURT's; 392 exhaust clearance; which trims
have a steel or plastic front bumper or auxiliary switches outside the 2024 release; and 2026 fit of listings whose
titles stop at 2025 or earlier. No JL guide exists for roof racks, running boards or bike racks; none are ranked.
Source fixes 2026-10-04: factory-hitch FAQ and section now say to read the receiver label against the owner's-manual rating (a 3,500 lb Class II caps a Jeep rated higher) and name Rubicon and Rubicon X from Jeep's 2024 press kit; "ordered with" changed to "built with"; 33 in tires added to the 5,000 lb takeaway; unconfirmed 2024-on rows point to the owner's manual chart and "ceilings" became "unconfirmed", to match the corrected hitch guide and proposed vehicle data.
"""

KIND = "upgrades"
KEY = ("jeep", "wrangler", "2018-present")
CATEGORIES = ["floor-mats", "hitches", "led-light-bars", "running-boards", "roof-racks"]

TITLE = "2018–2026 Jeep Wrangler JL Upgrades, Ranked: 3 Mods in Order, With Door-Count and 4xe Fit Traps"
META = ("Three 2018–2026 Wrangler JL upgrades in buying order: floor liners, trailer hitch and light bar, with "
        "2-door, JK, 4xe, tow rating and tailgate spare traps.")

FAQ = [
 ("What should I upgrade first on a 2018–2026 Jeep Wrangler JL?",
  "Floor liners, then a trailer hitch. Liners cost about $90–$210 across the picks in our guide, and with the doors "
  "and top off, weather lands in the footwells. You need three facts to order them: two doors or four, gas or 4xe, "
  "and whether there is a subwoofer in the cargo area. A hitch comes second. CURT's 13392 is about $126 at etrailer, "
  "and a 2 in receiver carries bikes or a cargo tray on a Jeep with a small cargo area. Lighting is last, because "
  "most of it is off-road light and the mounts carry the most trim exclusions."),
 ("Will 4-door Unlimited accessories fit a 2-door Wrangler JL?",
  "It depends on the category. Floor liners: the front pair yes, the rear no. Husky sells the 93991 for the 2-door's "
  "short rear area, about $140–$200, and the budget sets in our guide are Unlimited only. Hitches: CURT's 13392, Draw-Tite's 76382, Mopar's 82215209 and the Xprite receiver are listed for 2-door "
  "and 4-door JLs, but the 2-door's tow rating is lower. Lights: our guide lists windshield-frame and A-pillar "
  "mounts for both bodies. The 4xe and the Rubicon 392 are 4-door only."),
 ("Do JK Wrangler parts fit a JL?",
  "Some hitches do. Most other parts don't. Wikipedia says the two generations overlapped: JL production began in "
  "November 2017 and the JK was built until April 27, 2018, so a 2018 Wrangler can be either. Full liner sets are generation-specific. Husky's 93971 is the 2007–2018 JK Unlimited set "
  "and the 93921 the JL Unlimited set, though its 13021 front pair is listed for both. CURT's 13392 and Draw-Tite's "
  "76382 are listed for the JK and the JL. Light brackets should name the JL and your model year."),
 ("How much can a Wrangler JL tow, and does a Class III hitch raise it?",
  "A hitch never raises it. Dealer towing guides and our vehicle data list 2,000 lb for 2018–2023 2-doors and "
  "3,500 lb for 2018–2023 4-doors, the 4xe and the Rubicon 392. Jeep's 2024 press kit gives a 5,000 lb maximum on "
  "4-door Rubicon automatics with 33 in tires. Dealer guides also list up to 3,500 lb for 2024-on 2-doors and "
  "5,000 lb for other properly equipped 4-doors; we could not confirm those from a Jeep page. Use the towing chart "
  "in your owner's manual."),
 ("Does every Wrangler JL come with a factory hitch?",
  "No. Our hitch guide says a JL has a factory receiver only if it was built with the Trailer Tow package. Jeep's "
  "2024 press kit lists it as standard on the Rubicon and Rubicon X, and as we read the 2024 pricing release, on "
  "the Willys too; we could not confirm other trims or years. Look under the rear bumper for a square 2 in "
  "opening. Owners on JLwranglerforums report the factory receiver they have seen is a Class II rated 3,500 lb. If "
  "one is fitted, read its label and compare it with the tow rating in your owner's manual. A 3,500 lb Class II "
  "receiver caps a Jeep rated higher. If the label covers what you tow, you need only a ball mount and wiring. If "
  "no receiver is fitted, Mopar sells the factory part as kit 82215209 for about $275–$312."),
 ("What changes if I have a Wrangler 4xe or a Rubicon 392?",
  "The 4xe changes the most. Its battery sits under the rear seat, so 3W, LASFIT and Falafa list their liner sets as "
  "not for the 4xe. Our guide's route is Husky's 13021 front pair, about $90–$130, with a rear piece that names the "
  "4xe. Quadratec's Q&A confirms Mopar's hitch on the 4xe, and the rating stays at 3,500 lb. Quadratec excludes the "
  "4xe from KC's 91336 light kit, and KC sells bracket set 7331 for it. The 392 takes Unlimited liners, is also "
  "listed at 3,500 lb, and has a taller cowl: Baja's A-pillar kit needs M6 x 80 mm bolts, and KC's bracket set for "
  "it is 7328."),
 ("Will a hitch bike rack or cargo carrier clear the JL's tailgate spare?",
  "Not always, so measure first. The spare hangs on the tailgate directly above the receiver, and our hitch guide "
  "calls it the main reason hitch racks fail to fit a JL. Measure from the receiver pin hole to the back of the tire "
  "and compare that with the rack's clearance spec. CURT's 13392 has a 9 in tube, which "
  "etrailer notes is meant to help bike racks clear the spare. A hitch extender is the other fix, but it adds "
  "leverage, so stay well under the tongue weight rating."),
 ("Did the 2024 refresh change which accessories fit the JL?",
  "For most parts, no, but check three things. First, year ranges: Nilight's windshield bracket lists 2018–2023 and "
  "several liner and hitch titles stop at 2025. Second, the grille. Jeep's 2024 press "
  "kit describes a new seven-slot grille, and Wikipedia says the Sport and Sport S kept the earlier one, so "
  "grille-mounted lights must match yours. Third, towing. Jeep gives the 2024 Rubicon a Dana 44 HD full-float rear "
  "axle and a 5,000 lb maximum on 4-door automatics with 33 in tires."),
 ("Are LED light bars street legal on a Jeep Wrangler?",
  "Usually only off-road, and it depends on your state. CJ Pony Parts "
  "quotes California as requiring off-road lights to be off and covered with an opaque cover on the highway, "
  "Pennsylvania as requiring them off and covered, and North Carolina as requiring light bars off on public roads. "
  "KC HiLiTES says most states restrict mounting to 12–42 in above the ground, and a 50 in windshield bar sits "
  "above that range. This is not legal advice. Check your own state's code before driving with a light uncovered."),
 ("How much does it cost to add all three upgrades to a Wrangler JL?",
  "From the prices on our three guides' picks, a budget 4-door build runs about $210–$300 for an OEDRO liner set and "
  "an Xprite or CURT receiver. Hawkley's or Nilight's light brackets and a bar are priced on their listings and "
  "come on top. A mid build runs from about $659–$859 with LASFIT liners or 3W's floor-and-cargo "
  "kit, a WeiSen or Draw-Tite hitch and Baja's Squadron Sport A-pillar kit. A premium build with a Husky "
  "WeatherBeater set, Mopar's receiver and Baja's LP6 Pro bumper kit runs about $1,575–$1,682. All figures are "
  "approximate."),
]

ARTICLE = {
 "dek": "Three upgrades for the JL Wrangler, in buying order. Fit turns on a short list of facts: two doors or four, "
        "JL or the older JK, gas, 4xe or 392, the tow rating for your year and body, and a spare tire that hangs on "
        "the tailgate right above the receiver.",
 "author": "jake-morrison",
 "reviewed": "2026-10-04",
 "method": "We did not install any of these parts ourselves. The order comes from our three fit-checked 2018–2026 "
           "Wrangler JL guides, weighing how many Jeeps each upgrade suits, what it costs and how much can go wrong "
           "with fit. Price bands are the prices "
           "listed on those guides' picks, checked at maker and retailer stores in September 2026, and are "
           "approximate. Vehicle facts come from our vehicle data, the guides' sources, Wikipedia's JL page and "
           "Jeep's 2024 Wrangler press kit and pricing release. Where we couldn't confirm a factory detail, the text "
           "says so.",
 "takeaways": [
  "**Count the doors first.** Husky's 93991 is the 2-door liner set and the 93921 the Unlimited set. The budget sets in our guide are Unlimited only.",
  "**JL, not JK.** Both were built as 2018 models. Full liner sets are generation-specific, while CURT's and Draw-Tite's hitches are listed for both.",
  "**The Jeep's tow rating beats the hitch's.** Listed figures run from 2,000 lb on 2018–2023 2-doors to 5,000 lb on 2024 4-door Rubicon automatics with 33 in tires.",
  "**The 4xe and 392 carry their own fit notes.** The 4xe's battery changes the rear floor, and both are excluded from some light kits.",
  "**The spare sits above the receiver, and lights go last.** Measure before buying a hitch rack. Most light bars are off-road only, so check your state's rules.",
 ],
 "priority": [
  {"category": "floor-mats",
   "h": "1. Floor liners first: the cabin that gets rained in, bought by doors and powertrain",
   "why": "Floor liners lead on the JL because the doors and roof come off, so rain, dust and trail mud land in the "
          "footwells. Three facts decide fit. First, doors. The 2-door has a short area behind the front seats and the 4-door "
          "Unlimited has a full rear footwell, so Husky sells the WeatherBeater 93991 for the 2-door and the 93921 "
          "for the Unlimited. The budget sets in our guide are Unlimited only. Second, powertrain. The 4xe plug-in "
          "hybrid carries its battery under the rear seat, and 3W, LASFIT and Falafa list their sets as not for the "
          "4xe. Third, the cargo floor. JLs with the premium Alpine audio have a subwoofer there, and 3W sells its "
          "floor-and-cargo kit with and without the cut for it. Prices in our guide run about $90–$130 for "
          "OEDRO's set, about $110–$150 for LASFIT's recycled TPE, about $150–$190 for 3W's kit and about $140–$210 "
          "for Husky's two WeatherBeater sets, which Husky says are made in the USA with a lifetime warranty against "
          "cracks and breaks. The trade-off is firm, tall walls against softer TPE.",
   "skip_if": "You run the Jeep with the carpet out, rinse the tub after every trip and are content to rely on the drain plugs."},
  {"category": "hitches",
   "h": "2. Trailer hitch second: about $126 for a 2 in receiver, capped by the Jeep's own rating",
   "why": "A trailer hitch ranks second because it costs little and suits every JL. The "
          "cargo area is small, so a 2 in receiver is where bikes and a cargo tray go. Check first whether you need "
          "one. Our hitch guide says a factory receiver comes only with the Trailer Tow package, so look under the "
          "rear bumper. Then read the Jeep's rating, which is usually lower than the hitch's. Dealer towing guides list 2,000 lb for 2018–2023 2-doors and 3,500 lb for 4-doors of those "
          "years, and Jeep puts its 5,000 lb maximum on 2024 4-door Rubicon automatics. CURT's 13392 is a Class III "
          "rated 5,000 lb with 500 lb of tongue weight, and etrailer lists it at about $126. Draw-Tite's 76382, "
          "about $200–$270, is rated 4,500 lb and 675 lb. Mopar's 82215209, about $275–$312, is a Class 2 rated "
          "3,500 lb and 350 lb. The Xprite and WeiSen receivers run about $120–$210, with ratings to confirm on the "
          "listing. The trade-off is the spare. It hangs on the tailgate above the receiver, so a hitch rack has to "
          "reach past it.",
   "skip_if": "A square 2 in receiver is already bolted to the frame under your rear bumper, and its label covers what you tow."},
  {"category": "led-light-bars",
   "h": "3. Lighting last: mostly off-road light, and the mount and trim decide fit",
   "why": "Lighting comes last for three reasons. Most of it is off-road light. The first kit our guide prices "
          "starts at about $399, well above a liner set or a hitch. And it has the most trim exclusions. The light "
          "bar itself is mostly universal. What has to match the Jeep is the mount. Baja Designs lists its Squadron Sport A-pillar kit for the 2018–2026 JL "
          "at factory mounting points with no trimming, from about $399. Its LP6 Pro bumper kit, about $1,160, is "
          "sold in separate versions for the factory steel and plastic bumpers. KC's 50 in Gravity Pro6 windshield "
          "kit, 160 W and 18,400 raw lumens, is priced on the listing, and retailers list it as excluding the 4xe or "
          "the Rubicon 392. Hawkley's bracket kit and Nilight's 52 in bracket are also priced on their listings. "
          "CJ Pony Parts quotes California as "
          "requiring off-road lights off and covered on the highway, and rules differ by state, so check yours "
          "before driving with one uncovered.",
   "skip_if": "Your night driving is on public roads, where an off-road light has to stay off."},
 ],
 "tier_table": {
  "caption": "Approximate price bands from the picks in our 2018–2026 Wrangler JL guides (September 2026; Amazon prices move daily). The budget and mid liner sets are 4-door parts; the 2-door set is Husky's 93991",
  "head": ["Upgrade", "Budget", "Mid", "Premium"],
  "rows": [
   ["Floor liners", "About $90–$130 (OEDRO TPE set, 4-door; confirm 4xe)", "About $110–$150 (LASFIT TPE, gas or eTorque 4-door) or $150–$190 (3W floor-and-cargo kit, not 4xe)", "About $150–$210 (Husky WeatherBeater 93921, 4-door) or $140–$200 (93991, 2-door)"],
   ["Trailer hitch", "About $120–$170 (Xprite, ratings on the listing) or about $126 (CURT 13392, 5,000 lb / 500 lb, etrailer's price)", "About $150–$210 (WeiSen with 4-pin harness, listed to 2025) or $200–$270 (Draw-Tite 76382, 4,500 lb / 675 lb)", "About $275–$312 (Mopar 82215209, Class 2, 3,500 lb / 350 lb)"],
   ["Lighting", "Priced on the listing: Hawkley's bracket kit with two 4 in spots (not 4xe) or Nilight's 52 in bracket (to 2023). Bar extra", "From about $399 (Baja Squadron Sport A-pillar kit)", "About $1,160 (Baja LP6 Pro bumper kit; buy the version for your bumper)"],
   ["Total", "About $210–$300 plus the light brackets and a bar", "From about $659–$859", "About $1,575–$1,682; hitch wiring extra"],
  ],
 },
 "sections": [
  {"h": "Two doors or four, JL or JK: settle this before anything else",
   "body": "The JL is sold as a 2-door and a 4-door Unlimited. Wikipedia lists their wheelbases at 96.8 in and "
           "118.4 in, and that gap shows up behind the front seats.\n\n"
           "- **Floor liners.** The front footwells are shared, which is why Husky's 13021 front pair covers both "
           "bodies. The rear is not: Husky's 93991 is the 2-door set, its 93921 the Unlimited set, and the budget "
           "sets in our guide are cut for the Unlimited only.\n"
           "- **Trailer hitch.** The brand-name hitches in our guide and the Xprite are listed for both bodies. "
           "What changes with door count is the tow rating, covered in the next section.\n"
           "- **Lighting.** Our guide lists windshield-frame and A-pillar mounts for all JLs. Trim and powertrain "
           "matter there, not doors.\n\n"
           "The second question is generation. Wikipedia says JL production began in November 2017 and the JK was "
           "built until April 27, 2018, so a 2018 Wrangler can be either, and listings mix the two. Full liner sets "
           "are generation-specific: Husky's 93971 is the 2007–2018 JK Unlimited set. Hitches are the exception. "
           "CURT lists the 13392 for the 2007–2018 JK and the 2018–2026 JL, and Draw-Tite lists the 76382 for "
           "2007–2026 Wranglers, so a 2007 start year is normal on those two. Light brackets should name the JL and "
           "your model year. If you aren't sure which 2018 you own, ask a Jeep dealer to check the VIN."},
  {"h": "Tow ratings by year, doors and powertrain: the number a hitch can't change",
   "body": "A hitch rating is only the hitch's limit. The Wrangler's own limit varies widely inside this one "
           "generation, and the lower of the two always applies.\n\n"
           "Through 2023, our vehicle data and the dealer towing guides our hitch guide cites "
           "list **2,000 lb** for the 2-door and **3,500 lb** for the 4-door. The 4xe and the Rubicon 392 are listed "
           "at **3,500 lb** in every year they are offered.\n\n"
           "From 2024 the top figure rises to **5,000 lb**, and this is where to read carefully. Jeep's 2024 press "
           "kit gives that maximum on 4-door Rubicon models with the 2.0L or 3.6L engine, the automatic and 33 in "
           "tires. Its pricing release ties the figure to the Rubicon's new Dana 44 HD full-float rear axle, and "
           "owners on JLwranglerforums describe it as a 2024-on Unlimited Rubicon figure. Dealer guides extend "
           "5,000 lb to any properly equipped 4-door with the 8-speed automatic and list 2024-on 2-doors at up to "
           "3,500 lb. We could not confirm from a Jeep page that a 4-door "
           "Sport or Sahara, a Rubicon on 35 in tires or any 2-door reaches those figures. Treat them as unconfirmed "
           "and use the towing chart in your owner's manual.",
   "table": {"caption": "2018–2026 Wrangler JL tow ratings as listed (the lower of vehicle and hitch applies)",
             "head": ["Configuration", "Years", "Listed maximum", "Hitch that matches"],
             "rows": [
              ["2-door", "2018–2023", "2,000 lb (vehicle data, dealer guides)", "Any. Every hitch in our guide is rated above the Jeep"],
              ["2-door", "2024 on", "Up to 3,500 lb in dealer guides; not confirmed from a Jeep page. Use the owner's manual chart", "Mopar 82215209 (3,500 lb) or any Class III"],
              ["4-door Unlimited", "2018–2023", "3,500 lb (vehicle data, dealer guides)", "Mopar 82215209 matches; CURT 13392 or Draw-Tite 76382 add tongue weight"],
              ["4-door Rubicon, 2.0L or 3.6L, automatic, 33 in tires", "2024 on", "5,000 lb (Jeep's 2024 press kit)", "CURT 13392 (5,000 lb / 500 lb). Draw-Tite's 4,500 lb or Mopar's 3,500 lb becomes the limit"],
              ["Other 4-doors", "2024 on", "Up to 5,000 lb in dealer guides; not confirmed from Jeep for non-Rubicon trims. Use the owner's manual chart", "CURT 13392 covers either figure"],
              ["4xe plug-in hybrid", "2021 on", "3,500 lb", "Mopar 82215209, confirmed for the 4xe in Quadratec's Q&A"],
              ["Rubicon 392", "Years offered", "3,500 lb", "Ask the seller about exhaust clearance"],
             ]}},
  {"h": "The factory receiver, the tailgate spare and the wiring",
   "body": "**Look first.** Our hitch guide says a JL has a factory receiver only if it was built with the Trailer "
           "Tow package. Jeep's 2024 press kit lists Trailer Tow as standard on the Rubicon and Rubicon X. As we "
           "read Jeep's 2024 pricing release, Trailer Tow with the Heavy-Duty Electrical Group is "
           "standard on the Willys and Rubicon. We could not confirm other trims or years, so look under the rear "
           "bumper for a square 2 in opening and check the window sticker.\n\n"
           "**Read its label.** Our vehicle data records the factory hitch as Class II with a 2 in receiver, and "
           "Mopar describes its 82215209 kit as a Class 2 receiver rated 3,500 lb with 350 lb of tongue weight. "
           "Owners on JLwranglerforums say every factory JL receiver they have seen is Class II. One reports a 2024 "
           "Rubicon whose manual shows 5,000 lb with a Class III hitch, while the Jeep was built with a Class II "
           "receiver. We could not confirm what Jeep fits to 5,000 lb Rubicons, so the label decides whether you "
           "need a second hitch. Compare it with the tow rating in your owner's manual: a 3,500 lb Class II "
           "receiver caps a Jeep rated higher.\n\n"
           "**The spare.** It hangs on the tailgate directly above the receiver, and our hitch guide calls it the "
           "main reason hitch racks fail to fit. CURT's 13392 uses a 9 in receiver tube to help racks clear it. Measure "
           "from the receiver pin hole to the back of the tire and compare that with the rack's clearance spec.\n\n"
           "**The bumper.** These hitches bolt to the frame behind the factory rear bumper. Many aftermarket steel "
           "bumpers have their own receiver or cover those frame points.\n\n"
           "**The wiring.** A 4-way flat harness covers tail, brake and turn lights. Electric trailer brakes need a "
           "7-way connector and a brake controller. Only the WeiSen bundle includes a harness, a 4-pin."},
  {"h": "4xe, Rubicon 392 and the 2024 refresh: the variants that change the plan",
   "body": "Trim changes little about liners or hitches on the JL. Our floor liner guide says trims don't change "
           "the floor, and the hitches in our guide are listed by body, not by trim. Powertrain, the 392's taller "
           "cowl, the front bumper and the model year are what move parts in or out. Mojave, which appears in "
           "several JL light listings, is a Gladiator trim.",
   "table": {"caption": "2018–2026 Wrangler JL variants that change the upgrade plan",
             "head": ["Jeep", "What it has", "What changes"],
             "rows": [
              ["4xe plug-in hybrid (2021 on)", "4-door only; battery under the rear seat; listed at 3,500 lb", "3W, LASFIT and Falafa liners, KC's 91336 kit and Hawkley's brackets exclude it; KC's 7331 brackets are the 4xe set"],
              ["Rubicon 392", "4-door only; listed at 3,500 lb; taller cowl (Baja)", "Unlimited liner sets fit. ExtremeTerrain excludes it from KC's 91336; KC's 7328 brackets are the 392 set; Baja's A-pillar kit needs M6 x 80 mm bolts"],
              ["EcoDiesel", "Offered from 2020 and dropped for 2024 (Wikipedia)", "CURT's 13392 excludes it. The other hitch listings don't say, so ask"],
              ["2024 refresh", "New seven-slot grille (Jeep); Wikipedia says Sport and Sport S kept the earlier grille", "Grille-mount lights must match your grille. Nilight's bracket lists 2018–2023"],
              ["Factory auxiliary switches", "Standard on Rubicon for 2024, as we read Jeep's release", "Baja's upfitter harness versions suit a factory switch bank. Other Jeeps use the toggle harness"],
              ["Steel or plastic front bumper", "Steel bumpers available on Rubicon and standard on Rubicon X and 392 for 2024, as we read Jeep's release", "Baja sells separate LP6 Pro kits for the factory steel and plastic bumpers. Look at yours"],
              ["2025–2026 model years", "Several listings stop at 2025 or earlier", "Confirm Husky's 93921, 3W's kit, OEDRO, WeiSen, KC's 91336 and Baja's LP6 Pro kit. LASFIT, Husky's 93991, CURT, Mopar and Hawkley name 2026. Baja's A-pillar kit and Draw-Tite's hitch list 2026 on the makers' pages, but their Amazon titles don't"],
             ]}},
  {"h": "Drain plugs and an open top, what isn't ranked, and the order to fit",
   "body": "Wikipedia describes both JL bodies as convertibles with a removable roof and doors, and our vehicle data "
           "lists a hardtop, a soft top and the Sky One-Touch power top. Our floor "
           "liner guide notes that the JL tub has drain plugs so the interior can be washed out, and that "
           "tall-walled liners keep most water and mud off the carpet, so you use the plugs less. We could not "
           "confirm from a Jeep page where the plugs sit, and our guide doesn't record how any of its liners sits "
           "over them, so ask the seller if you plan to rinse the cabin with the liners in. If you pull "
           "the carpet, our guide says a nibbed liner grips the bare floor less well, so rely on the retention "
           "posts.\n\n"
           "Running boards now have their own JL guide on this site, split by door count, so they are not ranked "
           "again here. Roof racks now have their own JL guide, sorted by hardtop, soft top and door count, so they are "
           "not ranked here either. Bike racks have no JL guide yet, so no products are named for them.\n\n"
           "Fit the three in this order.\n\n"
           "1. **Floor liners.** No tools. Remove the factory mats, check that the drain plugs are seated, hook the "
           "driver liner onto the retention posts and press every pedal to the floor.\n"
           "2. **Trailer hitch.** Draw-Tite quotes 20 minutes with no drilling for the 76382, and Quadratec puts the "
           "Mopar receiver at under an hour. CURT's instructions call for lowering the exhaust temporarily.\n"
           "3. **Lights.** Our lighting guide's rule is a harness with a relay, a fuse and a switch, and the "
           "upfitter version only if your Jeep has factory auxiliary switches. Aim the lights at night on level "
           "ground, then fit the covers."},
 ],
 "avoid": [
  {"h": "An Unlimited liner set in a 2-door, or a gas rear in a 4xe", "body": "The rear floors differ. Husky's 93991 is the 2-door set, and 3W, LASFIT and Falafa list their sets as not for the 4xe."},
  {"h": "JK listings on a JL", "body": "Husky's 93971 is a JK Unlimited set. A hitch listed for 2007–2026 can be correct, but a JK-only hitch or bracket is not."},
  {"h": "Reading the hitch rating as the tow rating", "body": "A 5,000 lb hitch on a 2018–2023 2-door still leaves you at 2,000 lb, and a 3,500 lb Class 2 receiver caps a Rubicon rated at 5,000 lb."},
  {"h": "A light mount bought before checking trim and bumper", "body": "KC's 50 in kit is listed as excluding the 4xe or the 392, Hawkley excludes the 4xe, and Baja's bumper kit comes in steel and plastic bumper versions."},
 ],
 "verdict": {
  "thesis": "On the 2018–2026 Wrangler JL, buy floor liners by door count and powertrain first, add a trailer hitch rated for your Jeep if no receiver is fitted, and leave lighting for last, bought by mount, trim and bumper.",
  "body": "The JL is easy to accessorize once six facts are written down: JL or JK, two doors or four, gas, 4xe or "
          "392, subwoofer or not, receiver or no receiver, and the tow figure in your owner's manual. Floor liners "
          "need the first four and cost about $90–$210, so they go first. A trailer hitch needs one look under the "
          "bumper and one rating check. It starts at about $126 for CURT's 13392 and carries bikes or a tray, "
          "provided the rack clears the tailgate spare.\n\n"
          "A light bar or pod kit is third because most of it is off-road light, and because the mount, the trim "
          "and the front bumper all have to match before the first wire is run. Roof racks, running boards and bike "
          "racks aren't ranked, since the site has no JL guide for them yet. Owners who also have a 2020–2026 "
          "Gladiator can share Husky's 13021 front liner pair and Baja's A-pillar kit, but the rear floor is the "
          "truck's own. Each linked guide covers the fit details for its category.",
 },
 "sources": [
  ["Jeep Wrangler (JL): body styles, wheelbases, JK overlap, 4xe, 392, EcoDiesel, 2024 update (Wikipedia)", "https://en.wikipedia.org/wiki/Jeep_Wrangler_(JL)"],
  ["Press Kit: 2024 Jeep Wrangler, towing, Rubicon axle, grille (Stellantis Media)", "https://media.stellantisnorthamerica.com/newsrelease.do?id=24889&mid=4"],
  ["Jeep Brand Announces Starting Prices for 2024 Wrangler Lineup (Stellantis Media)", "https://media.stellantisnorthamerica.com/newsrelease.do?id=24902&mid=52"],
  ["JL towing capacity and factory Class II hitch thread (JLwranglerforums)", "https://www.jlwranglerforums.com/forum/threads/5-000-lbs-towing-capacity.132594/"],
  ["Jeep Wrangler towing guide, 2-door vs 4-door (Redwater Dodge)", "https://www.redwaterdodge.com/jeep-wrangler-towing"],
  ["CURT 13392 Class 3 Trailer Hitch (CURT)", "https://www.curtmfg.com/part/13392"],
  ["CURT 13392 on 2022 Wrangler (etrailer)", "https://www.etrailer.com/Trailer-Hitch/Jeep/Wrangler/2022/C13392.html"],
  ["Draw-Tite 76382 Class III Trailer Hitch (Draw-Tite)", "https://www.draw-tite.com/product/76382_class-iii-trailer-hitch"],
  ["Mopar 82215209 Receiver Hitch Kit (Quadratec)", "https://www.quadratec.com/p/mopar/82215209-receiver-hitch-wrangler-jl"],
  ["Husky Liners: WeatherBeater vs X-act Contour (Husky Liners)", "https://huskyliners.com/blog/husky-liners-weatherbeater-vs-xact-contour/"],
  ["Baja Designs LP6 Pro Bumper Kit 447671UP (RealTruck)", "https://realtruck.com/p/baja-designs-jeep-lights-bumper-kits/bdi-447671up/"],
  ["Baja Designs Squadron Sport A-Pillar Light Kit, JL/JT (Baja Designs)", "https://www.bajadesigns.com/products/2018-Jeep-JL-A-Pillar-Sportsmen-Kit.asp"],
  ["KC HiLiTES Gravity Pro6 50 in JL/JT kit 91336 (Quadratec)", "https://www.quadratec.com/p/kc-hilites/gravity-pro6-led-light-bar-jeep-wrangler-jl-gladiator-jt-91336"],
  ["Are LED light bars and auxiliary lights street legal? (KC HiLiTES)", "https://www.kchilites.com/campfire/post/are-led-light-bars-and-auxiliary-lights-street-legal"],
  ["Are light bars legal? Light bar laws by state (CJ Pony Parts)", "https://www.cjponyparts.com/resources/are-light-bars-legal"],
 ],
}
