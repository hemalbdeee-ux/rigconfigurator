"""Upgrades pillar: 2016–2023 Toyota Tacoma (3rd gen, N300). Ended generation.
Hub page: ranks the four published 3rd-gen Tacoma category guides and links to them. No product picks or ASINs here
(the site pulls each guide's #1 pick). Every price band comes from the linked guides' picks[].price fields or price
text in those guides (the FITS band for Husky 13981); vehicle facts from db/migrations/003_vehicles.sql (beds 61/74
in rounded, Class III, 2 in receiver, 6,800 lb, composite SMC bed, factory deck rails with cleats), the four guides
and their sources, Wikipedia's Toyota Tacoma page (Access Cab and Double Cab only, 73.7 and 60.5 in beds, 5-speed
manual on the four-cylinder for 2016–2017, 6-speed manual on the V6, 6,800 lb under SAE J2807 with the tow package,
2017 TRD Pro with Rigid Industries LED fogs, 2020 facelift, TNGA-F for the 4th gen) and four Toyota Newsroom releases
opened for this page: 2016 (V6 Tow Package with Class IV towing receiver hitch, 4- and 7-pin connector, Trailer-Sway
Control; SMC inner bed; deck rail system with four standard cleats; available factory tri-fold hard tonneau), 2018
(TSS-P on all models, 5-speed manual discontinued, optional V6 Tow Package, TRD Pro Rigid fogs), 2021 (Tow Package
standard with V6 and available for 4-cyl; Trail Special Edition on SR5 with lockable insulated bed storage; TRD Pro
Rigid fogs) and 2023 (same tow package wording, 6,800 lb depending on grade, Trail Edition lockable bed storage, TRD
Pro Rigid fogs). Checked 2026-10-03. All pages were read through a text extraction, so the page attributes rather
than quotes.
Disagreements stated in the text rather than resolved: vehicle data says Class III hitch, Toyota says Class IV
receiver; vehicle data and the bed rack guide treat deck rails as fitted to every truck (Toyota's wording agrees),
the tonneau guide says "many" and Tyger sells for beds with or without the track; the floor liner guide mentions only
a six-speed manual while Wikipedia and Toyota list a 5-speed manual on 2016–2017 four-cylinders; listing titles vs
RealTruck pages on Trail Edition bed boxes (Gator EFX, TruXedo Lo Pro, ArmorFlex); Hooke Road's 2005–2025 listing vs
05–23 on its own site.
Not verified, and worded as such in the text: any payload figure (none printed); Tow Package availability for the
2017, 2019, 2020 and 2022 model years and by grade; TRD Pro fog lights for 2019, 2020 and 2022; the first model year
of the Trail edition (the Wikipedia extraction reads 2022, Toyota's 2021 model-year release already describes it, so
no start year is printed); why Husky splits automatic front liners at 2018; a manual-transmission liner for 2016–2017
trucks; an Access Cab rear liner; 2024 or 2025 fit on cross-generation listings (GoRack, TOUGHPRO, Husky 13981,
Hooke Road); load ratings for both Hooke Road racks and the Thule Xsporter Pro; Baja fog pocket kit fit on the Tacoma;
the RetraxPRO XR's price; rack fit around Trail Edition bed boxes. The floor mat guide's Wikipedia URL
(Toyota_Tacoma_(third_generation)) could not be fetched and is not cited.
Source fixes 2026-10-04: vehicle data hitch class changed to Class IV (Toyota's label), the tonneau guide now treats
the deck rails as standard, and the floor liner guide names the 5-speed manual, so the page no longer reports those
three as disagreements.
"""

KIND = "upgrades"
KEY = ("toyota", "tacoma", "2016-2023")
CATEGORIES = ["floor-mats", "tonneau-covers", "led-light-bars", "bed-racks", "running-boards"]

TITLE = "2016–2023 Toyota Tacoma Upgrades, Ranked: 4 Mods in Order, With Deck Rail and Transmission Fit Traps"
META = ("Four 2016–2023 Tacoma upgrades in buying order: floor liners, tonneau cover, light bar and bed rack, "
        "with transmission, deck rail, bed box and used-part notes.")

FAQ = [
 ("What should I upgrade first on a 2016–2023 Tacoma?",
  "Floor liners, then a tonneau cover. Liners cost the least, about $70–$260 across our guide's picks, and they are "
  "the easiest part to order wrong here: the automatic and the manual have different front floors, and Husky "
  "splits its automatic front liners at the 2018 model year. The cover comes second and a light bar third, with "
  "brackets from about $65. The bed rack is last, but decide on it before you pay for the cover. A budget start, "
  "YHTAUTO liners and Tyger's T3 cover, comes to about $291–$331."),
 ("Do I need to buy a trailer hitch for a 2016–2023 Tacoma?",
  "Often not. Look under the rear bumper first. Our vehicle data lists a Class IV hitch with a 2 in receiver and a 6,800 lb maximum. Toyota's releases put that Class IV towing receiver hitch in the Tow Package with a 4- and 7-pin connector. The 2018 release calls that package optional on the V6. The 2021 and 2023 "
  "releases say it is standard with the V6 and available for the four-cylinder. We did not read every model year. If "
  "a receiver is there, an aftermarket trailer hitch adds nothing, and no hitch raises Toyota's rating."),
 ("Do 2016–2023 Tacoma parts fit the 2024–2026 Tacoma, or the other way around?",
  "Mostly no, in both directions. Wikipedia says the newer truck moved to the TNGA-F platform, and maker catalogs "
  "show the split: BAK's MX4 is 448426 for this truck and 448446 for the new one, Rough Country sells the 73109 rack "
  "for 2005–2023 and the 73119 and 73141 for 2024–2026, and Cali Raised says its 2024 ditch brackets don't fit 2023 "
  "or older trucks. What moves across is universal hardware: light bars and pods themselves, and some universal "
  "clamp racks."),
 ("I bought a used 3rd-gen Tacoma. What should I check before ordering parts?",
  "Seven things. Count the pedals: three means a manual, and most liner sets are "
  "automatic only. Read the model year on the door-jamb label. Note the cab. Measure the bed inside at the rail: "
  "about 60.5 in or about 73.7 in. Look for the deck rail cleats; Toyota describes four as standard, and installing "
  "a cover such as the UnderCover ArmorFlex removes them for good. Look for storage boxes in the bed sides, which "
  "mark a Trail Edition. Last, look under the rear bumper for a receiver."),
 ("I have a manual-transmission Tacoma. What changes on this list?",
  "Only the front floor liner. Our floor liner guide says the manual truck's floor differs around the clutch pedal "
  "and shifter, and that 3W, YHTAUTO, Husky's 93941 and Toyota's TRD Pro liners are automatic only. The one manual "
  "part it names is Husky's 13981 front pair, about $90–$130, listed for 2018–2024 trucks; pair it with Husky's 14951 "
  "Double Cab rear. Our guide names no manual liner for 2016–2017 trucks, so ask the seller. No cover, rack or "
  "light listing in our guides is split by transmission."),
 ("I have an Access Cab. What changes on this list?",
  "The Access Cab has the 6 ft bed only, so order 6 ft covers: our guide names the BAKFlip MX4 448427, "
  "RetraxPRO MX 80852, TruXedo Lo Pro 557001 and Tyger T3 TG-BC3T1631. Rough Country's "
  "73109 rack is out because it fits the 5 ft bed only; Hooke Road's 18.8 in rack is listed for the 6 ft bed. Every "
  "full liner set in our guide is cut for the Double Cab. Husky's 13951 and 13961 front pairs list both cabs for "
  "2016–2017 automatics, and the Access Cab needs its own rear piece, which our guide doesn't name."),
 ("Can I run a tonneau cover and a bed rack together on a 3rd-gen Tacoma?",
  "Yes, with the right pair. The RetraxPRO XR, part T-80851 for the 5 ft bed, has T-slot rails along its sides, and "
  "RealTruck says the GoRack mounts to any bed cover with a T-slot style rail system. Yakima sells a Tonneau Kit 1 "
  "adapter for its OverHaul HD and OutPost HD towers that names the Retrax XR. Most folding covers take up the rail "
  "tops, and Rough Country says its 73109 does not fit trucks with tri-fold or retractable covers."),
 ("How much does it cost to add all four upgrades to a 2016–2023 Tacoma?",
  "From the prices on our guides' picks, a budget build runs about $836–$886: YHTAUTO or TOUGHPRO floor "
  "protection, Tyger's T3 cover, Cali Raised's lower bumper brackets and Rough Country's 73109 rack, before a bar and "
  "harness. A mid build runs about $1,465–$1,574 with 3W liners, a TruXedo Lo Pro or Gator EFX, Cali Raised's "
  "complete lower bumper kit and the same rack. A premium build runs about $2,877–$3,970 with a hard cover from the "
  "ArmorFlex to the RetraxPRO MX and the GoRack. These totals compare spending levels, not parts lists: "
  "the 73109 fits the 5 ft bed only and excludes tri-fold and retractable covers."),
 ("Do TRD Pro and Trail Edition trucks need different parts?",
  "Mostly no for the TRD Pro, yes for the Trail Edition. Cali Raised lists its lower bumper kit for all trims and "
  "names the TRD Pro grille. Wikipedia says the "
  "2017 TRD Pro launched with Rigid Industries LED fog lights, and Toyota's 2018, 2021 and 2023 releases list them "
  "too, so a fog pocket kit adds less there. On the Trail Edition, Toyota describes lockable storage in the bed, and "
  "RealTruck says the BAKFlip MX4, Gator EFX and RetraxPRO MX won't work with those boxes. Rack makers don't address "
  "them."),
]

ARTICLE = {
 "dek": "Four upgrades for the third-generation Tacoma, in buying order. This generation "
        "ended with the 2023 model year, so many owners are fitting parts to a truck someone else specified. That "
        "shapes the order: two transmissions and a mid-run change in the front liners, a composite bed whose "
        "deck rails and bed boxes decide which covers and racks fit, and listings that stretch one year range across "
        "two or three generations.",
 "author": "jake-morrison",
 "reviewed": "2026-10-03",
 "method": "We did not install any of these parts ourselves. The order comes from our four fit-checked 2016–2023 "
           "Tacoma guides, weighing how many trucks each upgrade suits, what it costs, how often it's used and how "
           "much of its fit is confirmed for this generation. Price bands are the prices listed on those guides' "
           "picks, checked at maker and retailer "
           "stores in September 2026, and are approximate. Vehicle facts come from our vehicle data, the guides' "
           "sources, Wikipedia's Tacoma page and Toyota's press releases for the 2016, 2018, 2021 and 2023 model "
           "years. Where we couldn't confirm a factory detail, or where two of our sources disagree, the text says so.",
 "takeaways": [
  "**Count the pedals and read the model year.** Most liner sets are automatic only, and Husky splits its automatic front liners between 2016–2017 and 2018–2023.",
  "**The cab narrows the bed, a tape measure settles it.** Access Cabs have the 73.7 in bed only; Double Cabs have the 60.5 in bed or, as an option, the 73.7 in bed.",
  "**Look in the bed before any bed purchase.** Check for the deck rail cleats and for Trail Edition storage boxes, which rule out most hard covers.",
  "**Treat a wide year range as a question.** Titles that run 2005–2023, 2016–2024 or 2005–2025 cross a generation line, and little that bolts on is shared with the 2024–2026 Tacoma.",
  "**Look under the bumper before shopping for a hitch.** Toyota's Tow Package includes a Class IV receiver, and its 2021 and 2023 releases call it standard with the V6.",
 ],
 "priority": [
  {"category": "floor-mats",
   "h": "1. Floor liners first: transmission, model year and cab, in that order",
   "why": "Floor liners lead on this Tacoma because they cost the least and offer the most ways to order wrong. Three "
          "facts decide fit. The first is transmission: our guide says the manual truck's floor differs around the "
          "clutch pedal and shifter, and that 3W, YHTAUTO, Husky's 93941 and Toyota's TRD Pro liners are automatic "
          "only. The second is model year. Husky sells automatic front pairs for 2016–2017 (13951 and 13961) and a "
          "full set, 93941, for 2018–2023, while the rear floor stays the same. The third is cab, and every full set "
          "in our guide is cut for the Double Cab. Prices run about $70–$110 for YHTAUTO's TPE set, about $80–$120 "
          "for TOUGHPRO's rubber mats, about $110–$150 for 3W, about $150–$210 for Husky's WeatherBeater 93941, "
          "about $150–$200 for Toyota's PT908-35200-02 TRD Pro liners and about $200–$260 for TuxMat. Husky backs "
          "WeatherBeater with a lifetime warranty against cracks and breaks. The trade-off is feel: a firm, "
          "tall-walled liner holds the most slush, while rubber or TuxMat is more pleasant underfoot.",
   "skip_if": "The truck came with liners that match its transmission and year, or it lives on dry pavement and the carpet mats are enough."},
  {"category": "tonneau-covers",
   "h": "2. Tonneau cover second: one part number for eight model years, two bed checks first",
   "why": "A tonneau cover ranks second because the short bed is only 60.5 in long, so keeping it dry and out of "
          "sight matters. This generation is easy in one way: our guide found each cover sold as one "
          "part number per bed for all eight model years, so a used cover is simple to match. "
          "Measure the bed first, since a Double Cab can have either length. Buy a 2016–2023 part, because makers "
          "list the 2005–2015 short bed at 60.3 in under separate numbers. Then look in the bed. RealTruck says "
          "Trail Edition storage boxes rule out the BAKFlip MX4, Gator EFX and RetraxPRO MX, and the UnderCover "
          "ArmorFlex install removes the deck rail cleats for good. Prices run about $221 for the Tyger T3, about "
          "$490 for the TruXedo Lo Pro, about $549 for the Gator EFX, about $1,200 for the ArmorFlex, about $1,250 "
          "for the BAKFlip MX4 and about $1,850 for the RetraxPRO MX. Hard covers carry 300–500 lb spread evenly "
          "and lock when the tailgate is locked. Soft covers do neither.",
   "skip_if": "The truck already wears a sound cover (Toyota's 2016 release lists an available factory tri-fold hard cover), or you haul tall loads most days."},
  {"category": "led-light-bars",
   "h": "3. Light bar third: the best-documented fit on the truck, from about $65",
   "why": "Lighting ranks third, ahead of the bed rack, because the entry price is low, the fit is the best "
          "documented of the four categories and nothing about it competes with the bed. The bar itself is "
          "universal. What must match is the mount. Cali Raised lists its 32 in lower bumper hidden kit for all "
          "2016–2023 trims, grilles and sensors, names the TRD Pro grille and factory camera mounts, and says it "
          "needs no cutting or drilling. Prices run about $65 for the brackets alone, about $385 for "
          "the complete lower bumper or upper grille kit, about $395 with Cali Raised's OEM-style switch, and about "
          "$437 for Baja Designs' fog pocket kit, whose Tacoma fit needs confirming. Check the fog "
          "pockets on a TRD Pro before buying fog pods, because Toyota's releases list Rigid Industries LED fogs on "
          "that trim. Our guide treats bars and ditch pods as off-road lighting in most "
          "states, so keep them off on public roads and check your own state's rules. A low mount leaves the "
          "bar exposed to mud and rocks.",
   "skip_if": "You don't drive unlit dirt roads, or your state's rules leave you nowhere to switch the lights on."},
  {"category": "bed-racks",
   "h": "4. Bed rack last: decide it before the cover, buy it when the load calls for it",
   "why": "The bed rack comes last because the fewest owners need one, it costs the most and it limits the cover "
          "choice. Fit starts with bed length. The two beds differ by 13.2 in, Rough Country's 73109 fits the 5 ft "
          "bed only and Hooke Road's 18.8 in rack is listed for the 6 ft bed. Thule's XK4 kit, "
          "about $120, slides clamps into the factory deck rail tracks with no drilling, but the Xsporter Pro rack "
          "is sold separately. Rough Country's rack, about $480, installs with nutserts, which sit in holes. "
          "RealTruck's GoRack, about $1,090, mounts to the stake pockets, the utility rail or a T-slot cover. "
          "Ratings separate the picks: 1,000 lb static and 600 lb dynamic for the GoRack, 750 lb and 400 lb for the "
          "Rough Country, and no published split for either Hooke Road rack, both priced on the listing. If you "
          "camp from the truck, move this slot up to second and choose the cover around the rack.",
   "skip_if": "Your loads fit under a cover and you don't carry a tent, boats or ladders."},
 ],
 "tier_table": {
  "caption": "Approximate price bands from the picks in our 2016–2023 Tacoma guides (September 2026; Amazon prices move daily). Totals add one part per row; check the rack and cover pairing before buying both",
  "head": ["Upgrade", "Budget", "Mid", "Premium"],
  "rows": [
   ["Floor liners", "About $70–$120 (YHTAUTO TPE set or TOUGHPRO rubber mats)", "About $110–$150 (3W TPE liners)", "About $150–$260 (Husky WeatherBeater 93941, Toyota TRD Pro liners or TuxMat)"],
   ["Tonneau cover", "About $221 (Tyger T3 soft tri-fold)", "About $490 (TruXedo Lo Pro soft roll-up) to $549 (Gator EFX hard tri-fold)", "About $1,200 (UnderCover ArmorFlex), $1,250 (BAKFlip MX4) or $1,850 (RetraxPRO MX)"],
   ["Light bar", "About $65 (Cali Raised lower bumper brackets; bar and harness extra)", "About $385–$395 (Cali Raised lower bumper kit, without or with its switch)", "About $437 (Baja Designs fog pocket kit; confirm Tacoma fit) to $770 (two Cali Raised kits at about $385 each)"],
   ["Bed rack", "About $480 (Rough Country 73109, 5 ft bed only)", "About $480 (same rack; no priced pick in between)", "About $1,090 (RealTruck GoRack)"],
   ["Total", "About $836–$886, plus a bar and harness", "About $1,465–$1,574", "About $2,877–$3,970"],
  ],
 },
 "sections": [
  {"h": "Towing: look for the factory receiver before you shop for a hitch",
   "body": "There is no trailer hitch guide for the 2016–2023 Tacoma on this site, so here is what the truck may "
           "already have.\n\n"
           "**The receiver.** Our vehicle data lists a **Class IV hitch with a 2 in receiver**. That is Toyota's own label: its press releases name the factory part a **Class IV towing receiver hitch**, supplied in the Tow Package with a 4- and 7-pin connector. Toyota's 2018 release calls the V6 Tow Package optional. Its 2021 and 2023 releases say the "
           "package is standard with the V6 and available for the four-cylinder. We did not read the releases for "
           "2017, 2019, 2020 or 2022, so look under the rear bumper instead of going by year or trim. If a receiver "
           "is there, an aftermarket trailer hitch adds nothing.\n\n"
           "**The rating.** Our vehicle data lists a maximum of **6,800 lb** with the factory tow package. Wikipedia "
           "and Toyota give the same figure under the SAE J2807 standard, and Toyota's 2023 release adds that it "
           "depends on the model grade. Your figure is in the owner's manual and on the door-jamb labels, and a "
           "receiver never raises it.\n\n"
           "**Payload.** We could not confirm a payload figure for this generation, so this "
           "page prints none. Tongue weight, a rack, a tent and passengers all count against the number on your "
           "door-jamb label."},
  {"h": "The composite bed, its deck rails and the Trail Edition boxes",
   "body": "Toyota's releases describe the inner bed as a sheet-molded composite deck with an integrated deck rail "
           "utility system and four standard adjustable tie-down cleats. The rails are both a mount and an obstacle: "
           "racks made for this truck clamp into the tracks, while cover clamps have to work around the rails and "
           "their cleats.\n\n"
           "Toyota's wording makes the rails part of every bed in this generation, and our guides treat them that way. Tyger still sells its T3 for beds with or without the factory track, so on a used truck, look. A "
           "previous cover install may also have cost the truck its cleats.\n\n"
           "The second check is the Trail Edition. Toyota's 2021 release describes the Trail Special Edition, built "
           "on the SR5, with lockable, insulated bed storage, and its 2023 release lists lockable bed storage on the "
           "Trail Edition. Those boxes are where most hard covers stop fitting, and listing titles and retailer "
           "pages don't always agree.",
   "table": {"caption": "What the parts in our guides say about the deck rails and the bed boxes",
             "head": ["Part", "Deck rails and cleats", "Trail Edition bed boxes"],
             "rows": [
              ["BAKFlip MX4 448426 / 448427", "Amazon listing names trucks with the OE track system", "Will not work with the boxes (RealTruck)"],
              ["UnderCover ArmorFlex AX42014 / AX42015", "Install removes the cleats, and they can't be reused (RealTruck)", "Amazon title says with or without; RealTruck doesn't repeat it. Confirm"],
              ["Gator EFX GC44014", "Clamps to the bed rails, no drilling", "Amazon listing says with or without; RealTruck says it will not work. Confirm"],
              ["RetraxPRO MX 80851 / 80852", "Clamps to the bed rails, no drilling", "Not compatible (RealTruck)"],
              ["TruXedo Lo Pro 556001 / 557001", "Mounts inside the rails, no drilling", "RealTruck says it works; the Amazon title excludes the boxes. Confirm"],
              ["Tyger T3 TG-BC3T1630 / TG-BC3T1631", "Fits with or without the factory track; over-rail bedliners need holes cut", "Not for Trail Special Edition trucks with boxes (Tyger)"],
              ["Thule XK4 kit for the Xsporter Pro", "8 clamps and 8 screws slide into the factory tracks; no drilling (etrailer)", "Not addressed"],
              ["Rough Country 73109", "Installs with nutserts; Rough Country recommends its 10583 tool", "Not addressed"],
              ["RealTruck GoRack", "Stake pockets, utility rail or a T-slot cover; Tacoma hardware isn't detailed", "Not addressed"],
             ]}},
  {"h": "Cab, bed, transmission and trim: which Tacoma do you have?",
   "body": "Wikipedia and Toyota agree on the layout: two cabs, the Access Cab and the Double Cab, and no Regular "
           "Cab. The Access Cab comes with the 73.7 in bed only. The Double Cab has the 60.5 in bed as standard and "
           "the 73.7 in bed as an option. Our vehicle data rounds those to 61 and 74 in, retailers print 5' 1\" and "
           "6' 2\", and Tyger's titles print 60 and 74 in. They are the same two beds.\n\n"
           "There are two manual gearboxes to know about. Wikipedia lists a 6-speed manual with the V6 and a 5-speed manual with the four-cylinder for 2016–2017. "
           "Either one means a manual-specific front liner.",
   "table": {"caption": "2016–2023 Tacoma configurations that change the upgrade plan",
             "head": ["Truck", "What it has", "What changes"],
             "rows": [
              ["Double Cab", "60.5 in bed as standard, 73.7 in bed as an option", "Every full liner set in our guide is cut for it; order the cover and rack by bed. Rough Country's 73109 is 5 ft only"],
              ["Access Cab", "73.7 in bed only; small rear-hinged doors and a short rear area with jump seats", "6 ft covers (MX4 448427, RetraxPRO MX 80852, Lo Pro 557001) and racks; a rear liner that names the Access Cab"],
              ["Manual transmission", "6-speed with the V6; 5-speed with the four-cylinder in 2016–2017 (Wikipedia)", "Manual-specific front liners; Husky 13981 is listed for 2018–2024, so ask about earlier trucks"],
              ["TRD Pro (2017–2023)", "Heritage 'TOYOTA' grille and Rigid Industries LED fog lights (Wikipedia, Toyota)", "Cali Raised's bumper kit names its grille; a fog pocket kit adds less"],
              ["Trail Edition / Trail Special Edition", "Lockable bed storage (Toyota)", "Rules out most hard covers; rack makers don't address the boxes"],
             ]}},
  {"h": "Buying for an ended generation: year ranges, used parts and what crosses over",
   "body": "The 2016–2023 run is closed, which helps in one way: our tonneau guide found one part number per bed for "
           "all eight model years. The risk is in how listings describe the years.\n\n"
           "- **Ranges that reach back to 2005.** Rough Country's 73109 rack and Hooke Road's 11.5 in rack are "
           "listed for 2005–2023. Cover makers split there: BAK's MX4 is 448406 for the 2005–2015 bed and 448426 for "
           "this one.\n"
           "- **Ranges that run past 2023.** The GoRack's Amazon listing names the 2016–2024 Tacoma, TOUGHPRO's mats "
           "run to 2024, Husky's 13981 manual pair is listed for 2018–2024, and Hooke Road's 18.8 in rack is titled "
           "2005–2025 while Hooke Road's own site says 05–23. Our guides treat the 2024 truck as a different fit, so "
           "ask the seller.\n"
           "- **Splits inside the generation.** Husky divides automatic front liners at 2018, the year Toyota says "
           "Toyota Safety Sense P became standard and the 5-speed manual was dropped. We found nothing that ties "
           "either change to the liner split. Wikipedia dates a facelift to 2020, and no cover, rack or light "
           "listing in our guides is split there.\n"
           "- **Used parts.** Match a used cover by its part number sticker, and check the clamps and seals. "
           "The warranties on the RetraxPRO, TruXedo Lo Pro and BAKFlip MX4 are non-transferable "
           "or tied to the original buyer.\n\n"
           "What moves to or from the 2024–2026 Tacoma is a short list: light bars and pods themselves, and some "
           "universal clamp racks."},
  {"h": "Choose the cover and the rack together, and fit the cover first",
   "body": "The bed rack is last on the buying list and first on the deciding list, because most covers and most "
           "racks want the same strip of bed rail. The pairings our guides could document:\n\n"
           "- **Railed cover plus rack:** the RetraxPRO XR (T-80851 for the 5 ft bed) adds T-slot rails along its "
           "sides, and RealTruck says the GoRack mounts to any bed cover with a T-slot style rail system. Our guides "
           "list no price for the XR.\n"
           "- **Tower rack over a cover:** Yakima's Tonneau Kit 1 adapter lets the OverHaul HD and OutPost HD towers "
           "mount to covers including the Retrax XR.\n"
           "- **Rack that excludes covers:** Rough Country says the 73109 does not fit trucks with tri-fold or "
           "retractable bed covers.\n\n"
           "Tent plus cargo has to stay under the dynamic rating on the road: 600 lb on the "
           "GoRack and 400 lb on the Rough Country. The hardware counts against payload too. Yakima lists the "
           "OverHaul HD towers at 59.52 lb before crossbars, and Tyger lists the T3 cover at 30.4 lb.\n\n"
           "Fit the cover before the rack, with the deck rail cleats slid clear of the clamps, because a rack that "
           "mounts to a cover's T-slot rails needs the cover in place."},
 ],
 "avoid": [
  {"h": "Trusting a year range that crosses a generation", "body": "Titles that span 2005–2023, 2016–2024 or 2005–2025 cover two or three different trucks. Covers, liners and light brackets are generation-specific, so get 2016–2023 fit confirmed in writing."},
  {"h": "Automatic liners in a manual, or 2018+ fronts in a 2016–2017 truck", "body": "The clutch area differs, and Husky splits its automatic front liners at 2018. Count the pedals and read the door-jamb label before ordering."},
  {"h": "A hard cover ordered before looking in the bed", "body": "RealTruck says Trail Edition storage boxes rule out the BAKFlip MX4, Gator EFX and RetraxPRO MX, and the ArmorFlex install removes the deck rail cleats for good."},
  {"h": "A folding cover and a rack bought separately", "body": "Rough Country's 73109 excludes tri-fold and retractable covers. If you want both, start from a T-slot cover such as the RetraxPRO XR and a rack that mounts to it."},
 ],
 "verdict": {
  "thesis": "On the 2016–2023 Tacoma, buy floor liners matched to transmission, model year and cab first and a tonneau cover matched to bed length and bed contents second, add a light bar on 3rd-gen brackets third, and buy a bed rack only after choosing the cover around it.",
  "body": "The third-generation Tacoma is a settled truck. Eight model years share the same two beds, and our guides "
          "found the covers and Cali Raised's light kits each sold under one listing for the whole run. What varies "
          "is the individual truck: automatic or manual, 2016–2017 or 2018 and later, Access Cab or Double Cab, 60.5 "
          "or 73.7 in bed, bed boxes or not, cleats present or missing. Floor liners need the first three answers "
          "and cost the least. The tonneau cover needs the bed "
          "answers. Lighting needs only a bracket titled for this generation.\n\n"
          "The bed rack sits last because few owners need one, but its decision comes early, since most folding "
          "covers and most racks can't share a bed. Skip the hitch shopping until you have looked under the bumper, "
          "because Toyota's Tow Package brings a factory receiver. If you have moved on to a 2024–2026 Tacoma, shop "
          "from that generation's guides: bars and pods can come with you, while brackets, covers and liners can't.",
 },
 "sources": [
  ["Toyota Tacoma: third generation cabs, beds, transmissions, towing, TRD Pro, 2020 facelift; fourth generation platform (Wikipedia)", "https://en.wikipedia.org/wiki/Toyota_Tacoma"],
  ["The All-New 2016 Toyota Tacoma: V6 Tow Package, composite bed, deck rail system (Toyota Newsroom)", "https://pressroom.toyota.com/2016-toyota-tacoma-debut-aug17/"],
  ["2018 Tacoma adds Toyota Safety Sense P across lineup: transmissions, tow package, TRD Pro (Toyota Newsroom)", "https://pressroom.toyota.com/2018-tacoma-ready-adventure-toyota-safety-sense-p-across-lineup/"],
  ["2021 Toyota Tacoma and its special editions: Trail Special Edition bed storage, Tow Package (Toyota Newsroom)", "https://pressroom.toyota.com/2021-toyota-tacoma-poised-to-keep-leadership-role-while-rolling-out-new-special-editions/"],
  ["2023 Toyota Tacoma: Tow Package, bed, Trail Edition (Toyota Newsroom)", "https://pressroom.toyota.com/2023-toyota-tacoma-adds-new-sr5-sx-and-chrome-packages/"],
  ["Husky Liners: WeatherBeater vs X-act Contour (Husky Liners)", "https://huskyliners.com/blog/husky-liners-weatherbeater-vs-xact-contour/"],
  ["BAKFlip MX4 448426 (RealTruck)", "https://realtruck.com/p/bakflip-mx4-tonneau-cover/bak-448426/"],
  ["UnderCover ArmorFlex AX42014 (RealTruck)", "https://realtruck.com/p/undercover-armor-flex-tonneau-cover/udc-ax42014/"],
  ["Gator EFX GC44014 (RealTruck)", "https://realtruck.com/p/gator-efx-hard-fold-tonneau-cover/guc-gc44014/"],
  ["Tyger T3 TG-BC3T1630 (Tyger Auto)", "https://www.tygerauto.com/tonneau-cover/tyger-t3-soft-trifold/tg-bc3t1630/tyger-t3-soft-tri-fold-fit-2016-2023-toyota-tacoma-5-bed.html"],
  ["RealTruck GoRack (RealTruck)", "https://realtruck.com/p/realtruck-gorack/"],
  ["Rough Country Bed Rack 73109, Tacoma 2005-2023 (Rough Country)", "https://www.roughcountry.com/product/configurable/toyota-bed-rack-73109c"],
  ["Thule XK4 Xsporter Pro adapter kit for 2016-2023 Tacoma (etrailer)", "https://www.etrailer.com/Accessories-and-Parts/Thule/THXK4.html"],
  ["Yakima OverHaul HD towers (Yakima)", "https://yakima.com/products/overhaul-hd"],
  ["2016–2023 Toyota Tacoma 32 in Hidden LED Light Bar Kit (Cali Raised LED)", "https://caliraisedled.com/products/2016-2020-toyota-tacoma-32-lower-bumper-hidden-led-light-bar-kit"],
 ],
}
