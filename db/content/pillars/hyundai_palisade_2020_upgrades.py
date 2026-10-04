"""Upgrades pillar: 2020–2025 Hyundai Palisade (1st gen, LX2; three-row SUV, no bed; the 2026 Palisade is a new generation).
Hub page: ranks the four published Palisade category guides and links to them. No product picks or ASINs here
(the site pulls each guide's #1 pick). Every price band comes from the linked guides' picks[].price fields or price
text in those guides (Stealth's conversion kits at $299 and $399, the Thule system at $604.85 to $704.85);
vehicle facts from db/migrations/003_vehicles.sql (SUV, flush side rails, no stored roof load figure, hitch class 3
with a 2 in receiver, 5,000 lb, three rows, "XRT 2023+", "2026 is a new generation", "Telluride twin"; the Telluride
row's raised rails on X-Line and X-Pro from 2023), the four guides and their sources, and six pages opened for this
page on 2026-10-04: Hyundai's 2023 Palisade specification sheet (maximum trailer weight 5,000 lb with trailer brakes
and 1,650 lb without; pre-wiring and heavy-duty transmission oil cooler standard on all trims; no tow hitch listed;
Trailer Sway Control standard; self-leveling suspension on SEL Premium and up; "Roof rails load capacity (lbs.) 220";
trims SE, SEL, XRT, Limited, Calligraphy; GVWR 5,732 / 5,871 lb FWD / AWD; weights printed for 7P and 8P models;
tongue load referred to the owner's manual), Hyundai's 2020 sheet (5,000 / 1,650 lb, roof rails load capacity 220,
trims SE, SEL, Limited, same GVWR, no hitch listed), Hyundai's 2024 sheet (5,000 / 1,650 lb, roof rails load capacity
220, Trailer Sway Control standard, self-leveling standard on XRT and up, Calligraphy Night Edition added, same GVWR,
no hitch listed), Wikipedia's Hyundai Palisade page (bench for eight or optional captain's seats for seven; updated
model debuted at the New York International Auto Show on 13 April 2022 for the 2023 model year with a revised front
end and enhanced infotainment; Calligraphy since the 2021 model year; second generation unveiled 6 December 2024 and
the 2026 Palisade shown for North America on 16 April 2025), CURT's 13427 page (Class 3, 2 in, 5,000 lb / 750 lb,
6,000 lb / 750 lb with weight distribution, 2020–2025 Palisade, 39 lb, not for vertical-hanging bike racks, novice
install, limited lifetime warranty) and etrailer's Palisade answers page (32 in crossbar spread on factory crossbars,
about 71 in of hatch clearance against 55 in needed by a Thule Motion XT).
The three Hyundai sheets were read through a text extraction, so the page says "as we read" where a table layout
matters. The self-leveling, Trailer Sway Control and GVWR lines were read but are not printed on the page.
Two guides say the Palisade's roof limit is only in the owner's manual; this page prints Hyundai's 220 lb
"roof rails load capacity" line with attribution and still points to the manual.
Not verified, and worded as such in the text: Hyundai's tow and roof figures for 2021, 2022 and 2025 (sheets not
read); whether the 220 lb figure is a driving limit and whether it includes the crossbars' weight; pre-wiring and the
transmission cooler for model years other than 2023 (the line did not appear in our reading of the 2020 and 2024
sheets); whether any Palisade left the factory with a receiver; the Palisade's own tongue load limit; second-row
seating by trim for any model year; the second-row layout of the Smartliner and Husky 95711 listings; 2025 fit of Husky's 95711 (title stops at 2024) and 2024–2025 fit of Thule's
Amazon crossbar listing (title stops at 2023); Calligraphy fit of the EYOUHZ bars; fit of anything on the Calligraphy
Night Edition; the tow rating of the Stealth hitch; the part number and ratings of the Reese bundle; KUAFU's ratings;
the part number of a 2023–2025 4-way harness; crossbar weights; the spread of aftermarket bars (etrailer's 32 in is
for factory crossbars); the SkyBox NX Skinny's spread; the MasterFit 440's price and clamp fit on other brands' bars;
Telluride interchange beyond what each maker lists; and 2026 Palisade fit of any part. The Palisade Forums thread
cited by the cargo box guide (220 lb from Hyundai's accessory crossbar guide) was not opened for this page and is
not used or cited here. No Palisade guide exists for other categories; none are ranked.
"""

KIND = "upgrades"
KEY = ("hyundai", "palisade", "2020-2025")
CATEGORIES = ["floor-mats", "hitches", "roof-racks", "cargo-boxes"]

TITLE = "2020–2025 Hyundai Palisade Upgrades, Ranked: 4 Mods in Order, With Seat-Count and Flush-Rail Traps"
META = ("Four 2020–2025 Palisade upgrades in buying order: floor liners, trailer hitch, roof rack and cargo box, with "
        "7- vs 8-seat, flush rail and 2023 wiring checks.")

FAQ = [
 ("What should I upgrade first on a 2020–2025 Hyundai Palisade?",
  "Floor liners, then a trailer hitch. Liners cost the least, from about $100–$140 for a three-row rubber set, and "
  "need one fact from you: seven seats or eight. A hitch is second because Hyundai's spec sheets list no receiver "
  "and one part covers 2020–2025, at about $120–$300. Crossbars for the flush side rails come third, at about "
  "$90–$170 for an Amazon set. A cargo box is last, since it mounts to those bars and costs the most."),
 ("Does the 2020–2025 Palisade come with a trailer hitch from the factory?",
  "Not as listed equipment in the Hyundai documents we read. Hyundai's 2020, 2023 and 2024 Palisade specification "
  "sheets list no tow hitch. The 2023 sheet does list trailer pre-wiring and a heavy-duty transmission oil cooler as "
  "standard on every trim. We could not confirm that equipment for other model years, so check the window sticker. "
  "Look under the rear bumper before you order a hitch."),
 ("How much can a 2020–2025 Palisade tow, and does an aftermarket hitch raise it?",
  "A hitch never raises it. Hyundai's 2020, 2023 and 2024 specification sheets list a maximum trailer weight of "
  "5,000 lb with trailer brakes and 1,650 lb without, and our vehicle data records 5,000 lb. CURT's 13427 is rated "
  "at 5,000 lb, so it matches the vehicle. Draw-Tite's 76420 reaches 6,000 lb with weight distribution, but the "
  "Palisade's 5,000 lb still applies. We did not read the sheets for 2021, 2022 or 2025, so use your owner's manual "
  "for those years."),
 ("How much weight can a Palisade roof carry with crossbars and a cargo box?",
  "Use the lowest of three numbers. Hyundai's 2020, 2023 and 2024 specification sheets list a roof rails load "
  "capacity of 220 lb. Thule rates its Evo Flush Rail system for the Palisade at 165 lb, and Amazon crossbar sets "
  "print 165 to 300 lb. Some boxes have their own cargo limit, such as 100 lb for Yakima's DeepSpace 10. Bars, box "
  "and cargo all count. On the Thule system, a 47 lb Yakima SkyBox 16 Carbonite leaves 118 lb for gear."),
 ("Which floor liners fit a 7-seat Palisade, and which fit an 8-seat?",
  "Seven-seat Palisades have two captain's chairs in the second row, and eight-seat Palisades have a bench. In the "
  "floor liner guide, TOUGHPRO's three-row rubber set is for second-row buckets only. RILLEC lists 7- and 8-seat "
  "and Megiteller lists bench and bucket, so ask which second-row piece ships. WeatherTech splits its parts by "
  "layout in its fit program. The Smartliner and Husky 95711 listings name no layout in the guide, so confirm "
  "before ordering."),
 ("Did the 2023 refresh change which Palisade accessories fit?",
  "For wiring and hidden-hitch kits, yes. For the rest, the guides found no split. Wikipedia says the updated "
  "Palisade debuted in April 2022 for the 2023 model year with a revised front end. CURT's 56420 4-way harness "
  "lists 2020–2022 only, and Stealth Hitches sells separate towing conversion kits for 2020–2022 and 2023–2025. The "
  "CURT 13427 and Draw-Tite 76420 hitches cover 2020–2025 with one part. Husky's 95711 liner title stops at 2024 "
  "and Thule's Amazon crossbar listing at 2023, so confirm later years."),
 ("Do 2020–2025 Palisade parts fit the redesigned 2026 Palisade?",
  "Assume not, with one exception. The 2026 model is a new generation; Wikipedia says it was unveiled in December "
  "2024. Husky sells a separate liner set for it, 96381, against 95711 for 2020–2024. The roof rack guide notes "
  "that some sellers now print separate 2026 crossbar listings, and nothing in the hitch guide is listed for 2026. "
  "The exception is a cargo box, which clamps to crossbars, not to the vehicle."),
 ("Do Kia Telluride liners, hitches or crossbars fit the Palisade?",
  "Only where a maker lists both. The Kia is a related but different vehicle. In the hitch guide, Draw-Tite's 76420 "
  "and KUAFU's budget hitch name both, while CURT sells separate parts: 13427 for the Palisade and 13420 for the "
  "Kia. The floor liner guide says most makers sell separate liner sets because the cabins differ. Our vehicle data "
  "records raised rails on the Kia's X-Line and X-Pro from 2023, while every Palisade trim in the listings we found "
  "has flush rails."),
 ("Do the XRT and Calligraphy trims need different parts?",
  "Not in the listings the guides found. The floor liner guide says trims change seats and finishes, not the floor. "
  "Snailfly's and Tuyoung's crossbar listings name the SE, SEL, XRT, Limited and Calligraphy with the same flush "
  "side rails. EYOUHZ's title leaves out the Calligraphy, so ask that seller. CURT lists the 13427 hitch for every "
  "2020–2025 trim. Hyundai's 2024 sheet adds a Calligraphy Night Edition, which no listing in the guides names, so "
  "we could not confirm its fit."),
 ("How much does it cost to add all four upgrades to a Palisade?",
  "From the prices on the four guides' picks, a budget build runs about $450–$600: Megiteller rubber liners, KUAFU's "
  "hitch, OMAC crossbars and Rightline Gear's soft carrier. A mid build runs about $1,059–$1,249 with Smartliner "
  "liners, CURT's 13427, ERKUL bars and Yakima's SkyBox 16 Carbonite. A premium build with WeatherTech's full set, "
  "Draw-Tite's 76420, Thule's Evo Flush Rail system and the Thule Motion 3 XXL runs about $2,355–$2,615. A wiring "
  "harness is extra in every column."),
]

ARTICLE = {
 "dek": "Four upgrades for the first-generation Palisade, in the order most owners should buy them. Fit on this "
        "three-row SUV turns on a short list of facts: seven seats or eight, side rails that sit flush to the roof, "
        "a 5,000 lb tow rating with no receiver in Hyundai's spec sheets, wiring that splits at the 2023 refresh, "
        "and listings that stretch into the redesigned 2026 Palisade.",
 "author": "jake-morrison",
 "reviewed": "2026-10-04",
 "method": "We did not install any of these parts ourselves. The order comes from the four fit-checked 2020–2025 "
           "Palisade guides on this site, weighing how many Palisades each upgrade suits, what it costs, what it "
           "depends on and how much doubt sits in the fit. Price bands are the prices on those guides' picks, checked in September 2026, and are approximate. Vehicle facts come from "
           "our vehicle data, the guides' sources, Hyundai's 2020, 2023 and 2024 Palisade specification sheets, "
           "CURT, etrailer and Wikipedia. We read Hyundai's sheets for three model years only. Where we couldn't "
           "confirm a factory detail, the text says so.",
 "takeaways": [
  "**Count the second-row seats.** Captain's chairs make a 7-seat Palisade and a bench makes an 8-seat one, and the second-row floor liner is shaped for one or the other.",
  "**The receiver is the missing piece.** Hyundai's 2023 spec sheet lists trailer pre-wiring and a heavy-duty transmission cooler as standard, and no tow hitch.",
  "**5,000 lb braked, 1,650 lb unbraked.** Hyundai's 2020, 2023 and 2024 sheets print both figures, and no hitch raises either.",
  "**Flush rails, and 220 lb on them at most.** Hyundai's sheets list a 220 lb roof rails load capacity; Thule rates its Palisade system at 165 lb.",
  "**Read the years on every listing.** Wiring and hidden-hitch kits split at 2023, and the 2026 redesign is a new generation.",
 ],
 "priority": [
  {"category": "floor-mats",
   "h": "1. Floor liners first: count the second-row seats, then read the years",
   "why": "Floor liners lead on the Palisade because they cost the least and every Palisade can use them. Two facts "
          "decide fit. The first is the second row: a bench for eight or captain's chairs for seven, each with its "
          "own second-row liner. In the floor liner "
          "guide, TOUGHPRO's rubber set is for buckets only, RILLEC lists 7- and 8-seat, Megiteller lists bench and "
          "bucket, and WeatherTech splits its parts by layout. The second is the generation: Husky sells 95711 for "
          "2020–2024 and a separate 96381 for the 2026 model. Prices run about $100–$140 for Megiteller's three-row "
          "rubber, about $110–$150 for TOUGHPRO's, about $130–$170 for Husky's 95711 front and second row, about "
          "$150–$200 for Smartliner's three rows or RILLEC's three rows plus cargo liners, and about $280–$360 for "
          "WeatherTech's full set. The trade-off is walls against price: the rubber sets have lower edges than a "
          "molded liner, and Husky's set stops at the second row.",
   "skip_if": "You live somewhere dry, the carpet mats are still clean and the third row rarely carries anyone."},
  {"category": "hitches",
   "h": "2. Trailer hitch second: Hyundai lists the wiring and the cooler, not the receiver",
   "why": "A trailer hitch ranks second because it is the one part of the tow setup that the Hyundai documents we "
          "read leave out, and its fit is the simplest on this page. Hyundai's 2023 specification sheet lists "
          "trailer pre-wiring and a heavy-duty transmission oil cooler as standard on every trim, and no tow hitch. "
          "One part covers 2020–2025. CURT's 13427 is a Class 3 hitch rated at 5,000 lb with 750 lb of tongue "
          "weight, about $200–$280. Draw-Tite's 76420, about $220–$300, is rated at 5,000 lb and 500 lb, or "
          "6,000 lb and 750 lb with weight distribution. "
          "KUAFU's copy runs about $120–$180 with seller-supplied ratings. A 2 in receiver also takes a bike rack "
          "or a cargo carrier, which keeps weight off the roof. The trade-offs: no hitch raises Hyundai's 5,000 lb "
          "braked and 1,650 lb unbraked limits, and CURT says the 13427 isn't compatible with vertical-hanging "
          "bike racks.",
   "skip_if": "A 2 in receiver is already bolted under the rear bumper, or you never tow and carry nothing behind the liftgate."},
  {"category": "roof-racks",
   "h": "3. Roof rack third: flush rails take flush-rail feet, and the bars are the base for a box",
   "why": "A roof rack ranks third because fewer owners need one than need a receiver, and because it is the base "
          "for the cargo box in slot four. Our vehicle data lists flush side rails, and the listings in the roof "
          "rack guide name the SE, SEL, XRT, Limited and Calligraphy with the same rail. A flush rail has no gap "
          "underneath, so the foot has to grip it from the side; raised-rail towers won't hold. Thule's fit is the "
          "Evo Flush Rail foot 710601 with kit 6008 and 50 in WingBar Evo bars, rated at 165 lb, about $605–$705. "
          "Amazon sets clamp to the same rails for less: about $90–$140 for OMAC's 165 lb lockable bars, about "
          "$90–$130 for Snailfly's, about $110–$170 for ERKUL's 220 lb set with metal mounts and about $100–$140 "
          "for the 300 lb Tuyoung and EYOUHZ sets. The trade-off is proof. The printed ratings on the Amazon sets "
          "are the sellers' own, and none changes the 220 lb roof rails load capacity in Hyundai's sheets.",
   "skip_if": "Hyundai's accessory crossbars are already on the rails, or everything you carry fits behind the third row or on a hitch carrier."},
  {"category": "cargo-boxes",
   "h": "4. Cargo box last: it clamps to the bars, and the bars set the limit",
   "why": "A cargo box comes last because it costs the most, needs the crossbars from slot three and is used on the "
          "fewest days. It clamps to the bars, not to the Palisade, so the vehicle-specific part is the numbers. An "
          "etrailer expert gives the Palisade about 32 in of spread on its factory crossbars and about 71 in of "
          "rear hatch clearance, room enough for long boxes mounted forward. Weight is the tighter limit. The "
          "hard boxes in the cargo box guide weigh 30.2 to 57.2 lb, so Thule's 165 lb system has roughly 108 to "
          "135 lb left for gear. Prices run about $140 for Rightline Gear's Sport 3 soft carrier, about $599 for "
          "Yakima's SkyBox 16 Carbonite, about $649 for the DeepSpace 10, about $799 for the SkyBox NX Skinny, "
          "about $865 for the INNO Wedge 660 and about $1,250 for the Thule Motion 3 XXL without the duffel bundle. "
          "The trade-offs are height at the garage door and width: a 36 in box fills most of Thule's 50 in bars.",
   "skip_if": "The luggage fits with the third row folded, or the extra load is heavy more than bulky and belongs on a hitch carrier."},
 ],
 "tier_table": {
  "caption": "Approximate price bands from the picks in the 2020–2025 Palisade guides (September 2026; Amazon prices move daily). The cargo box sits on the same column's crossbars",
  "head": ["Upgrade", "Budget", "Mid", "Premium"],
  "rows": [
   ["Floor liners", "About $100–$140 (Megiteller rubber, three rows, bench or bucket)", "About $150–$200 (Smartliner three-row TPE, or RILLEC three rows plus cargo)", "About $280–$360 (WeatherTech full set, three rows)"],
   ["Trailer hitch", "About $120–$180 (KUAFU Class 3; confirm ratings on the listing)", "About $200–$280 (CURT 13427, 5,000 lb / 750 lb)", "About $220–$300 (Draw-Tite 76420; 5,000 lb / 500 lb, or 6,000 lb / 750 lb with weight distribution)"],
   ["Roof rack", "About $90–$140 (OMAC lockable flush-rail bars, 165 lb printed)", "About $110–$170 (ERKUL bars with metal mounts, 220 lb printed)", "About $605–$705 (Thule Evo Flush Rail system with kit 6008, 165 lb)"],
   ["Cargo box", "About $140 (Rightline Gear Sport 3 soft carrier, on the OMAC bars)", "About $599 (Yakima SkyBox 16 Carbonite, on the ERKUL bars)", "About $1,250 (Thule Motion 3 XXL, box alone, on the Thule bars)"],
   ["Total", "About $450–$600", "About $1,059–$1,249", "About $2,355–$2,615; wiring extra in every column"],
  ],
 },
 "sections": [
  {"h": "Seven seats or eight: the second row decides the liner set",
   "body": "The first-generation Palisade's second row comes two ways. Wikipedia describes seating for up to eight "
           "with a second-row bench, or seven with the optional captain's chairs. Each layout takes a different "
           "second-row liner, and the floor liner guide notes that the third-row piece sometimes changes too.\n\n"
           "Don't go by trim. Hyundai's specification sheets print weights for 7-passenger and 8-passenger models "
           "but, as we read them, don't say which trims get which layout. We could not confirm seating by trim for "
           "any model year, so open the rear door and count.\n\n"
           "Then decide how many zones to cover. If the third row is mostly folded flat, a cargo liner earns its "
           "place. Husky's 22711, about $100–$150, is listed for 2020–2025 and runs to the back of the second row "
           "over the folded third row. Rows are separate pieces, so brands can be mixed, as long as every piece "
           "names the 2020–2025 Palisade and your layout.",
   "table": {"caption": "2020–2025 Palisade liner sets in the floor liner guide, by second-row layout and coverage",
             "head": ["Set", "Second row it lists", "Rows covered", "Years listed", "Check before ordering"],
             "rows": [
              ["WeatherTech FloorLiners full set", "Split by layout in WeatherTech's fit program", "Three rows", "First-generation Palisade", "Confirm the layout in WeatherTech's fit checker"],
              ["Husky WeatherBeater 95711", "Not stated", "Front and second row", "2020–2024", "Confirm a 2025; Husky's 15261 front and 12731 second-row pieces list 2020–2025"],
              ["Smartliner three-row set", "Not stated", "Three rows", "2020–2025", "Confirm the layout with the seller"],
              ["RILLEC three rows plus cargo", "7- and 8-seat", "Three rows and cargo", "2020–2025", "Which second-row piece ships"],
              ["TOUGHPRO rubber", "Captain's chairs (buckets) only", "Three rows", "2020–2025", "Not for an 8-seat Palisade"],
              ["Megiteller rubber", "Bench and bucket", "Three rows", "2020–2025", "Which second-row piece ships"],
             ]}},
  {"h": "Towing: what Hyundai lists, what you add and the numbers a hitch can't change",
   "body": "**The receiver.** Our vehicle data records a Class III hitch with a 2 in receiver for this generation, "
           "the size of the CURT and Draw-Tite hitches in the hitch guide. Hyundai's 2020, 2023 and 2024 "
           "specification sheets list no tow hitch, and we could not confirm that any Palisade left the factory "
           "with one. Look under the rear bumper before ordering.\n\n"
           "**What Hyundai does list.** The 2023 sheet shows trailer pre-wiring and a heavy-duty transmission oil "
           "cooler as standard on all trims. We did not find that line for other years, so check the window "
           "sticker.\n\n"
           "**The rating.** All three sheets list **5,000 lb with trailer brakes and 1,650 lb without**. The lower "
           "of hitch and vehicle applies. A small utility trailer with a mower or a load of firewood can pass "
           "1,650 lb, and past that point Hyundai expects the trailer to have its own brakes.\n\n"
           "**Tongue weight.** CURT rates the 13427 at 750 lb. Draw-Tite rates the 76420 at 500 lb, or 750 lb with "
           "weight distribution. Those are hitch ratings. Hyundai's 2023 sheet prints no tongue load figure and "
           "points to the owner's manual, so we could not confirm the Palisade's own limit.\n\n"
           "**Wiring.** This is the year-specific part. CURT's 56420 4-way harness lists 2020–2022. A 2023–2025 "
           "Palisade needs a harness that names those years; the Reese bundle in the hitch guide includes one, "
           "though its title gives no part number or rating. For a braked trailer, add a 7-way connector and a "
           "brake controller. CURT lists its 51529 quick-plug harness for 2021–2025."},
  {"h": "Flush rails, 220 lb and 165 lb: the math under a cargo box",
   "body": "**The rails.** Rack makers treat the Palisade's side rails as flush: the rail is attached to the roof "
           "along its whole length, with no gap underneath. Thule's fit guide pairs the 2020–2025 Palisade with the "
           "Evo Flush Rail foot and kit 6008, and etrailer's Palisade list has no raised-rail towers. etrailer also "
           "shows Thule's WingBar Edge as not fitting the 2022 Palisade.\n\n"
           "**The roof figure.** Hyundai's 2020, 2023 and 2024 specification sheets list a **roof rails load "
           "capacity of 220 lb**. We did not read the sheets "
           "for 2021, 2022 or 2025, and they don't say whether the figure is for driving only, so your owner's "
           "manual is the authority.\n\n"
           "**The bar rating.** Thule rates its Palisade system at **165 lb**. Amazon sets print 165 lb (OMAC), "
           "220 lb (ERKUL) and 300 lb (Tuyoung, EYOUHZ), which are the sellers' figures. The lowest number applies, "
           "and the roof rack guide counts bars, carrier and cargo toward the total.\n\n"
           "On the 165 lb Thule system, the box's weight comes off first:\n\n"
           "- **Yakima DeepSpace 10:** 30.2 lb, leaving about 135 lb. Yakima caps the box at 100 lb of cargo, so "
           "100 lb applies.\n"
           "- **Rhino-Rack MasterFit 440:** 38.6 lb, leaving about 126 lb.\n"
           "- **INNO Wedge 660:** 42 lb, leaving 123 lb. Its own limit is 110 lb.\n"
           "- **Yakima SkyBox NX Skinny:** 43 lb, leaving 122 lb.\n"
           "- **Yakima SkyBox 16 Carbonite:** 47 lb, leaving 118 lb.\n"
           "- **Thule Motion 3 XXL:** 57.2 lb, leaving about 108 lb.\n\n"
           "**Spread and width.** The etrailer figure of about 32 in is for factory crossbars, so measure your own. "
           "It is the exact minimum for the DeepSpace 10 (32–46 in), and Yakima publishes no spread for the NX "
           "Skinny. On Thule's 50 in bars, a 36 in SkyBox 16 leaves about 14 in, and the 26.5 in NX Skinny leaves "
           "about 23.5 in for a bike mount."},
  {"h": "The 2023 refresh, the 2026 Palisade and Telluride listings: read the years and the name",
   "body": "Our vehicle data and all four guides treat 2020–2025 as one generation. Four kinds of listing blur "
           "that.\n\n"
           "**The 2023 refresh.** Wikipedia says the updated Palisade debuted at the New York International Auto "
           "Show in April 2022 for the 2023 model year, with a revised front end and an enhanced infotainment "
           "system. Our vehicle data adds the XRT from 2023, and Wikipedia dates the Calligraphy to the 2021 model "
           "year. The guides found one group of parts that splits at 2023: wiring and hidden-hitch kits.\n\n"
           "**The redesign.** Wikipedia says the second generation was unveiled in December 2024 and shown for "
           "North America in April 2025. Nothing in the four guides is listed for it except the cargo boxes.\n\n"
           "**Telluride listings.** The Kia Telluride is a related but different vehicle. Draw-Tite's 76420, "
           "KUAFU's hitch and Stealth's 2020–2022 kit are listed for both. CURT sells 13427 for the Palisade at "
           "39 lb and 13420 for the Kia at 33 lb, and most liner makers sell separate sets. Buy the listing that "
           "names the Palisade.\n\n"
           "**A 2019 in the title.** Several crossbar titles read 2019–2025. The first US model year was 2020, so "
           "the roof rack guide reads those as full first-generation coverage.",
   "table": {"caption": "What changes by model year, as the four Palisade guides found it",
             "head": ["Part", "2020–2022 vs 2023–2025", "2026 model"],
             "rows": [
              ["Floor liners", "No split found; most sets are listed 2020–2025. Husky's 95711 title stops at 2024", "Different floor; Husky sells 96381 for it"],
              ["Trailer hitch", "Same part: CURT 13427 and Draw-Tite 76420 cover 2020–2025", "None in the hitch guide is listed for it"],
              ["Wiring and hidden-hitch kits", "Split: CURT 56420 is 2020–2022; Stealth sells SHT25031 for 2020–2022 and SHT25031A for 2023–2025; the Reese bundle is 2023–2025", "Not listed"],
              ["Crossbars", "No split found; Thule's Amazon title stops at 2023 while The Rack Shop lists kit 6008 for 2020–2025", "New body and roof; some sellers print separate 2026 listings"],
              ["Cargo box", "Universal; no split", "Carries over once 2026 bars are fitted"],
             ]}},
  {"h": "Roof or hitch: where the weight goes, and the order to fit things",
   "body": "The Palisade has no bed, so cargo that won't fit inside goes on the roof or behind the bumper.\n\n"
           "- **The roof takes bulky, light loads.** A hard box on 165 lb bars has roughly 108 to 135 lb left for "
           "gear.\n"
           "- **The hitch takes heavy loads.** The cargo box guide points coolers and water jugs to a hitch cargo "
           "carrier. The hitch's tongue rating and the figure in the Palisade's owner's manual both apply, and the "
           "lower one wins.\n"
           "- **A hidden receiver is a rack mount first.** The Stealth Hitches listing in the hitch guide is a "
           "rack package for bikes and carriers. Towing needs Stealth's conversion kit, about $299 for 2020–2022 "
           "or about $399 for 2023–2025, and the pages the guide read gave no tow rating.\n\n"
           "Fit the four in this order.\n\n"
           "1. **Floor liners.** No tools. Lift out the factory mats in every row, seat the driver liner on "
           "Hyundai's retention posts and press both pedals to the floor.\n"
           "2. **Trailer hitch.** The CURT and Draw-Tite bolt to existing frame points with no drilling. Draw-Tite "
           "quotes 30 minutes and CURT calls the job novice-level. Then plug in a harness that names your model "
           "year.\n"
           "3. **Crossbars.** Wash the rails, mark the spread the box needs and tighten the clamps side to side in "
           "steps. Check them again after the first week.\n"
           "4. **Cargo box.** With a helper, center it, slide it forward clear of the sunroof opening and open the "
           "power liftgate slowly before tightening to spec. Keep the sunroof closed on the road."},
 ],
 "avoid": [
  {"h": "A liner set ordered before counting the second-row seats", "body": "Captain's chairs and a bench take different second-row pieces. TOUGHPRO's set is for buckets only, and RILLEC and Megiteller list both layouts, so ask which piece ships."},
  {"h": "Raised-rail towers, or a roof loaded to the bar's printed rating", "body": "The Palisade's rails have no gap to wrap a tower around. A 300 lb bar doesn't change Thule's 165 lb system rating or the 220 lb roof rails figure in Hyundai's spec sheets."},
  {"h": "Towing to the hitch rating, or with the wrong year's harness", "body": "A 6,000 lb weight-distribution rating doesn't lift Hyundai's 5,000 lb limit, and past 1,650 lb the trailer needs its own brakes. CURT's 56420 harness lists 2020–2022 only."},
  {"h": "Listings that reach into 2026 or name only the Telluride", "body": "The 2026 Palisade is a new generation with its own liners and crossbars, and CURT sells a different hitch for the Kia. Buy listings that name the 2020–2025 Palisade."},
 ],
 "verdict": {
  "thesis": "On the 2020–2025 Palisade, buy floor liners by seat count first, bolt on a 2 in trailer hitch with a harness for your model year second, add flush-rail crossbars third, and choose a cargo box last around the bar rating and Hyundai's 220 lb roof rails figure.",
  "body": "The first-generation Palisade is easy to accessorize once four facts are written down: seven seats or "
          "eight, model year, whether a receiver is already under the bumper, and which crossbars are on the rails. "
          "Floor liners need the first two and cost the least, so they go first. The trailer hitch is second "
          "because one part fits 2020–2025, Hyundai's 2023 sheet shows the pre-wiring and cooling in place, and a "
          "receiver carries what the roof can't.\n\n"
          "The roof rack is third and the cargo box fourth, because the box mounts to the bars, and the bar rating "
          "less the box decides what goes inside. Plan around 165 lb on Thule's system and never more than the "
          "220 lb Hyundai prints for the rails. Owners of a 2026 Palisade should treat this page as a list of "
          "questions, not part numbers.",
 },
 "sources": [
  ["2023 Palisade specifications: towing, pre-wiring, transmission cooler, roof rails load capacity, trims (Hyundai)", "https://www.hyundainews.com/assets/documents/original/50303-2023PalisadeProductSpecs20220630.pdf"],
  ["2020 Palisade specifications: towing, roof rails load capacity, trims (Hyundai)", "https://www.hyundainews.com/assets/documents/original/40272-2020PalisadeSpecifications.pdf"],
  ["2024 Palisade specifications: towing, roof rails load capacity, self-leveling, trims (Hyundai)", "https://www.hyundainews.com/assets/documents/original/56241-2024PalisadeSpecs020323.pdf"],
  ["Hyundai Palisade: seating, 2023 update, second generation (Wikipedia)", "https://en.wikipedia.org/wiki/Hyundai_Palisade"],
  ["CURT 13427 Class 3 hitch for Palisade (CURT)", "https://www.curtmfg.com/part/13427"],
  ["Draw-Tite 76420 Class III hitch, Palisade and Telluride (Draw-Tite)", "https://www.draw-tite.com/product/76420_class-iii-trailer-hitch"],
  ["CURT 56420 4-way harness fitment (CURT)", "https://www.curtmfg.com/part/56420"],
  ["CURT 51529 brake controller harness (CURT)", "https://www.curtmfg.com/part/51529"],
  ["Stealth towing conversion kit, 2023–2025 Palisade (Stealth Hitches)", "https://stealthhitches.com/products/towing-conversion-kit-sht25031a"],
  ["Stealth towing conversion kit, 2020–2022 Palisade and Telluride (Stealth Hitches)", "https://stealthhitches.com/products/towing-conversion-kit-sht25031"],
  ["Palisade crossbar spread and hatch clearance for a Thule box (etrailer)", "https://www.etrailer.com/answers.aspx?AnswerModel=Palisade&Manufacturer=Thule&Filter=fit&AnswerMake=Hyundai"],
  ["2022 Hyundai Palisade roof rack systems (etrailer)", "https://www.etrailer.com/roof-2022_Hyundai_Palisade.htm"],
  ["2020–2025 Palisade Thule complete rack, kit 6008 (The Rack Shop)", "https://therackshop.com/2020-2025-hyundai-palisade-w-flush-rails-thule-crossbar-complete-roof-rack/"],
  ["Thule Motion 3 XXL (Thule)", "https://www.thule.com/en-us/cargo-carrier/car-top-carrier/thule-motion-3-xxl-_-639950"],
  ["Husky Liners: WeatherBeater vs X-act Contour (Husky Liners)", "https://huskyliners.com/blog/husky-liners-weatherbeater-vs-xact-contour/"],
 ],
}
