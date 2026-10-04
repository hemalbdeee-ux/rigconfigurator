"""Upgrades pillar: 2010–2024 Toyota 4Runner (5th gen, N280). Ended generation.
Hub page: ranks the four published 5th-gen 4Runner category guides and links to them. No product picks or ASINs here
(the site pulls each guide's #1 pick). Every price band comes from the linked guides' picks[].price fields or price
text in those guides (the $544.99 maker-page price for Cali Raised's roof kit);
vehicle facts from db/migrations/003_vehicles.sql (SUV, raised rails, roof load 120 lb, hitch class 3 with a 2 in
receiver, 5,000 lb, third row optional on Limited/SR5, power roll-down rear window, TRD Pro basket rack), the four
guides and their sources, and five pages opened for this page on 2026-10-04: Wikipedia's Toyota 4Runner (N280) page
(SR5, Limited and Trail at launch; 4.0 L V6 with 5-speed automatic; 2.7 L four-cylinder on 2WD for 2010 only; 2014
facelift with revised fascias, projector headlamps, revised dashboard and center stack; Trail renamed TRD Off-Road
for the 2017 model year; Nightshade based on the Limited; TRD Sport for 2022; TSS-P standard for 2020), three Toyota
Newsroom releases: 2013 (5,000 lb, standard integrated tow hitch receiver and wiring harness, sliding rear cargo deck
up to 440 lb mentioned with the Limited, optional third row for seven, a roof rack standard), 2017 (5,000 lb with 500 lb tongue weight, receiver and wiring harness standard on all grades, pull-out
cargo deck 440 lb, third row on SR5 and Limited, Trail renamed TRD Off-Road) and 2020 (same towing figures, receiver
standard on all models, TSS-P standard on all grades, third row on SR5 and Limited, TRD roof rack exclusive to the
TRD Pro), and Trail4Runner's roof rack roundup (the 120 lb figure is in a reader comment citing a 2016 SR5 owner's
manual, not in the article; "the TRD Pro comes with that roof basket"). Toyota's 2022 release returned a 403 and is
not cited. All pages were read through a text extraction, so the page attributes rather than quotes.
Not verified, and worded as such in the text: the 120 lb roof limit from a Toyota document, and whether it differs by
year; the hitch class (vehicle data says Class III, Toyota's releases name none); a factory receiver for model years
other than 2013, 2017 and 2020; why liner makers split at 2013; a cabin liner for 2010–2012; a cargo liner cut for
the sliding deck; which TRD Pro years and special editions have the basket rack; whether Cali Raised's hidden grille
brackets suit the TRD Pro grille; whether a box's clamps fit a given platform's slats; whether Cali Raised's roof
light brackets and a platform can share the factory roof points; the weights of the Rough Country 88201, the
Slimsport and the SportRack Vista XL; 2019–2024 fit of Rhino-Rack's RT4B1 backbone; 2024 fit of listings titled to
2023; the model years for Toyota's PT908-89200-02 liners. No 4Runner guide exists for trailer hitches or running
boards; neither is ranked.
Source conflicts, attributed in the text and not presented as disagreements (fix at the source): vehicle data summary
and the cargo box guide put the Class III receiver on "tow-package trucks", while Toyota's 2013, 2017 and 2020
releases call the receiver and wiring harness standard; vehicle data says the basket rack replaces the rails on the
TRD Pro, the guides say "some TRD Pro years and special editions"; vehicle data and the roof and cargo guides credit
the 120 lb figure to Trail4Runner, where it is a reader comment; the three guides cite three different Wikipedia
URLs, and only the (N280) one was opened.
Source fixes 2026-10-04: TRD Pro roof statements now follow Toyota's 2019, 2020 and 2021 releases (TRD roof rack new for 2019 and exclusive to the TRD Pro; Yakima baskets on the Trail and Venture Special Editions in the 2021 release; 2022–2024 not confirmed); the 120 lb FAQ names the Trail4Runner reader comment; etrailer's 24–42 in spread and 57 in hatch figure are tied to the Yakima SkyBox 12; the Cali Raised roof kit maker-page price is given as about $525–$545 by option; the Squadron Sport street-use line now says the retailer page makes no SAE or DOT claim; the guide-level conflicts listed above were corrected in the four guides the same day.
Text fixes 2026-10-04 (round 2): the dek, the roof takeaway and the cargo box heading no longer state 120 lb as the roof's limit; they name it as the reader-cited figure, matching the retitled cargo box guide. META now says "a low roof load" in place of "a 120 lb roof".
"""

KIND = "upgrades"
KEY = ("toyota", "4runner", "2010-2024")
CATEGORIES = ["floor-mats", "roof-racks", "cargo-boxes", "led-light-bars"]

TITLE = "2010–2024 Toyota 4Runner Upgrades, Ranked: 4 Mods in Order, With Model-Year and Roof Load Fit Traps"
META = ("Four 2010–2024 4Runner upgrades in buying order: floor liners, roof rack, cargo box and light bar, with "
        "2013 and 2014 year splits, a low roof load and TRD Pro notes.")

FAQ = [
 ("What should I upgrade first on a 2010–2024 4Runner?",
  "Floor liners, then the roof. Liners cost the least, about $110–$260 across the cabin sets in our guide, and fit by "
  "model year, seat count and cargo floor. The roof comes second because it is the base for the third upgrade. Look "
  "up first. If raised rails and crossbars are there, a cargo box can clamp straight on. If the bars are missing, "
  "clamp-on crossbars cost about $90–$150. A light bar comes last, since most of it is off-road light."),
 ("Do I need to buy a trailer hitch for a 2010–2024 4Runner?",
  "Probably not. Toyota's releases for the 2013, 2017 and 2020 model years describe an integrated tow-hitch receiver "
  "and wiring harness as standard, with a 5,000 lb maximum. Our vehicle data records a Class III hitch with a 2 in "
  "receiver and the same 5,000 lb. Toyota's releases don't name a class, and we did not read one for every model "
  "year, so look under the rear bumper. If a receiver is there, an aftermarket trailer hitch adds nothing, and no "
  "hitch raises Toyota's rating."),
 ("How much weight can a 5th-gen 4Runner roof carry with a cargo box?",
  "Our vehicle data lists 120 lb. A reader comment on Trail4Runner cites it from the owner's manual of a 2016 SR5, and we "
  "could not confirm it from a Toyota document, so read the manual for your own year. The guides treat it as a "
  "driving limit that covers the crossbars or platform, the box and the gear inside. A 36 lb Thule Pulse L leaves 84 "
  "lb before the bars, which the cargo box guide turns into roughly 60 to 75 lb of gear."),
 ("Why do so many 4Runner floor liners start at 2013 and not 2010?",
  "We could not confirm the reason. Husky's WeatherBeater 99571, TuxMat's set and the budget floor-plus-cargo kit are "
  "all listed for 2013–2024, and our floor liner guide found no explanation on the listings. Wikipedia dates the "
  "facelift, with its revised dashboard and center stack, to 2014, a year later. If you own a 2010–2012, buy a cabin "
  "set that names your year or ask the seller. Husky's cargo liners are listed for 2010–2024."),
 ("I have a 2010–2013 4Runner. Which parts on this list change?",
  "Two categories. Most cabin liner sets start at 2013, so a 2010–2012 needs a listing that names its year. Cali "
  "Raised lists its 32 in hidden grille brackets for 2014–2024 only, because the 2014 facelift changed the front "
  "fascia. Our lighting guide names iJDMTOY's 20 in lower-grille kit, titled for 2010–2013, and three mounts that "
  "span the facelift: fog pockets, hood hinges and the roof. The roof parts don't change. The crossbars and Rough "
  "Country's 88201 platform are listed for 2010–2024."),
 ("Do 2010–2024 4Runner parts fit the 2025–2026 4Runner?",
  "Mostly no. Our vehicle data records a new platform, roof and rail geometry for the new generation, and makers "
  "sell separate parts. Rough Country's platform is 88201 for this generation and 88205 for the new one. Front "
  "Runner's Slimsport is KSTF003T against KSTF004T. Husky sells a separate 96531 liner set for the 2025 model. A "
  "cargo box does move across, because it clamps to crossbars. For lights, our guide says very little carries over."),
 ("Does a 4Runner TRD Pro need different parts?",
  "On the roof and possibly at the grille. Toyota's 2019 release introduced a TRD roof rack found only on the TRD "
  "Pro, and its 2020 and 2021 releases call the rack exclusive to that grade. We could not confirm 2022–2024. "
  "Clamp-on crossbars won't grip a rack or basket, and box clamps aren't made for basket tubing. Our lighting guide notes a "
  "unique TRD Pro grille and doesn't record whether Cali Raised's hidden grille brackets suit it, so ask. The cabin "
  "floor is shared with the other trims."),
 ("My 4Runner has the third row or the sliding cargo deck. What changes?",
  "Only the cargo liner, and which full kits you can buy. Our floor liner guide says the first and second row liners "
  "are the same either way. The third-row seat folds into the cargo floor, so it takes Husky's 25741 cargo liner, "
  "while the 25722 is for the standard floor only. TuxMat's set and the budget kit are listed for five seats. No pick "
  "in our guide is cut for the sliding deck; it suggests a deck-specific mat or a rubber mat laid on the deck."),
 ("Are LED light bars street legal on a 4Runner?",
  "Usually only off-road, and it depends on your state. Our lighting guide says many states treat light bars and "
  "auxiliary lights with off-road beams as equipment that must be switched off on public roads, and that some also "
  "require an opaque cover or limit how many auxiliary lamps you run and how high they sit. Replacement fog lights "
  "are the easiest to keep street-friendly, though the retailer page for the Squadron Sport kit makes no SAE or DOT claim. This is not legal "
  "advice. Check your own state's vehicle code."),
 ("How much does it cost to add all four upgrades to a 4Runner?",
  "From the prices on our four guides' picks, a budget build runs about $715–$795: a floor-plus-cargo liner kit, "
  "InTimesAuto crossbars, SportRack's Vista XL and Cali Raised's grille brackets, before a bar and harness. A mid "
  "build runs about $1,119–$1,492 with Husky's 99571 liners, ERKUL's locking bars, a Yakima SkyBox 16 or Thule Pulse "
  "L and a ditch or grille light kit. A premium build runs about $2,485–$2,814 with TuxMat, Front Runner's 3/4 "
  "platform, a DeepSpace 10 or Wedge 660 and Baja's fog pocket kit."),
]

ARTICLE = {
 "dek": "Four upgrades for the fifth-generation 4Runner, in buying order. The generation ended with the 2024 model "
        "year, so most owners are fitting parts to a used SUV that someone else specified. Fit turns on a few facts: "
        "the model year, five seats or seven, the cargo floor, what the roof carries from the factory, and a roof "
        "figure of 120 lb, cited by a reader from an owner's manual, that has to cover the bars, the box and the gear.",
 "author": "jake-morrison",
 "reviewed": "2026-10-04",
 "method": "We did not install any of these parts ourselves. The order comes from our four fit-checked 2010–2024 "
           "4Runner guides, weighing how many 4Runners each upgrade suits, what it costs, what it depends on and how "
           "much of its fit is confirmed across fifteen model years. Price bands are the prices listed on those "
           "guides' picks, checked at maker and retailer stores in September 2026, and are approximate. Vehicle facts "
           "come from our vehicle data, the guides' sources, Wikipedia's fifth-generation 4Runner page, Toyota's "
           "press releases for the 2013, 2017 and 2020 model years and Trail4Runner's roof rack roundup. Where we "
           "couldn't confirm a factory detail, the text says so.",
 "takeaways": [
  "**Read the model year first.** Most cabin liner sets start at 2013, hidden grille light brackets start at 2014, and the 2020–2024 radar limits a grille mount to one bar.",
  "**Count the seats and look at the cargo floor.** A standard floor, a sliding deck and a third row each take a different cargo liner.",
  "**Look up before buying anything for the roof.** Most trims have raised rails with crossbars. The TRD Pro got a TRD roof rack for 2019, and the Trail and Venture Special Editions carry a Yakima basket.",
  "**The roof figure we use is 120 lb, and everything counts.** It comes from a reader comment, not a Toyota document. Bars or platform, box and gear share it. Confirm the figure in your owner's manual.",
  "**Look under the bumper before shopping for a hitch.** Toyota's 2013, 2017 and 2020 releases list a tow-hitch receiver and wiring harness as standard.",
 ],
 "priority": [
  {"category": "floor-mats",
   "h": "1. Floor liners first: model year, seat count and cargo floor",
   "why": "Floor liners lead because they cost the least and suit every 4Runner. Three facts decide fit. The first is "
          "model year: Husky's WeatherBeater 99571, TuxMat's set and the budget floor-plus-cargo kit are all listed "
          "for 2013–2024, so a 2010–2012 owner needs a listing that names the year. The second is seating: TuxMat and "
          "the budget kit are listed for five seats. The third is the cargo floor. Husky's 25722 cargo liner covers "
          "the standard floor only and its 25741 is for the third row; both are listed for 2010–2024. Prices in our "
          "guide run about $110–$150 for the budget kit with its cargo liner, about $150–$210 for the Husky 99571, "
          "about $150–$200 for Toyota's TRD Pro liners (PT908-89200-02; confirm the years on the listing) and about "
          "$200–$260 for TuxMat. A Husky cargo liner adds about $100–$150. The trade-off is walls against coverage: "
          "Husky's firm tray holds more slush, while TuxMat covers more carpet and holds less standing water.",
   "skip_if": "The 4Runner came with liners that match its year and cargo floor, or it lives on dry pavement and the carpet mats are enough."},
  {"category": "roof-racks",
   "h": "2. Roof rack second: look up before you spend anything",
   "why": "The roof ranks second because it is the base for the cargo box in slot three, and because the first step "
          "costs nothing. Our roof rack guide finds raised side rails with factory crossbars on most trims, a TRD roof "
          "rack on the TRD Pro from 2019 and a Yakima basket on the Trail and Venture Special Editions. If the rails are there and the bars are gone, "
          "clamp-on crossbars cost about $90–$130 from InTimesAuto or about $100–$150 from ERKUL with locks. Both are "
          "listed for raised rails only. A platform is the bigger step. It bolts to the roof's factory mounting "
          "points with no drilling, and the factory rails usually come off. Prices run about $700 for Rough Country's "
          "full-length 88201, about $1,049 for Front Runner's Slimsport, about $1,199 for the Slimline II 3/4 kit and "
          "about $1,000–$1,300 for Rhino-Rack's Pioneer tray before its mounting backbone. The trade-off is weight. "
          "Our vehicle data lists a 120 lb roof limit, and the 3/4 kit installs at about 59 lb, which leaves about 61 "
          "lb.",
   "skip_if": "Raised rails and factory crossbars are already on the roof and all you want up there is a box, bikes or skis."},
  {"category": "cargo-boxes",
   "h": "3. Cargo box third: buy by weight, because the roof figure is low",
   "why": "A cargo box ranks third because it needs crossbars under it. The box itself is universal. What is specific "
          "here is the reader-cited 120 lb roof figure, which has to cover the bars, the box and the gear. The cargo box guide "
          "therefore ranks by box weight: 36 lb for Thule's 16 cu ft Pulse L, 38.6 lb for Rhino-Rack's MasterFit "
          "440L, 30.2 lb for Yakima's DeepSpace 10, 42 lb for the 11 in tall INNO Wedge 660 and 47 lb for Yakima's "
          "SkyBox 16 Carbonite. Prices in the guide run about $450 for SportRack's Vista XL, whose weight isn't "
          "published, about $599 for the SkyBox 16 on sale, about $649 for the DeepSpace 10, about $786 for the Pulse "
          "L and about $918 for the Wedge 660. The MasterFit is priced on the listing. Two measurements finish the "
          "job: the crossbar spread against the box's range, and the distance from the front bar to the hatch seam. "
          "The trade-off is height: these boxes add 11 to 19 in above the bars.",
   "skip_if": "The gear is heavy, not bulky. Coolers, fuel and recovery gear belong on a hitch carrier in the factory receiver."},
  {"category": "led-light-bars",
   "h": "4. Light bar last: the mount follows the model year, and most of it is off-road light",
   "why": "Lighting comes last because most of it is off-road light, and because its fit splits into three year "
          "groups. The bar is mostly universal. The mount has to match. Cali Raised lists its 32 in hidden grille "
          "brackets for 2014–2024 only, since the 2014 facelift changed the front fascia. From 2020, Toyota Safety "
          "Sense P is standard, with a radar at the grille, and Cali Raised says those models can mount one bar "
          "there, not two. Three mounts span every year: the fog pockets, the hood hinges and the roof. Prices in our "
          "guide run about $65 for Cali Raised's grille brackets alone, from about $270 for Diode Dynamics' ditch "
          "light kit, from about $346 for Cali Raised's grille kit with a bar, and about $437 for Baja Designs' "
          "Squadron Sport fog pocket kit, which plugs into the factory fog switch. Cali Raised's 52 in roof kit is "
          "priced on the listing; its own page showed about $525–$545 by option. A roof bar gives the most reach and the most glare. "
          "Check your state's rules before switching any of these on.",
   "skip_if": "You don't drive unlit trails or dirt roads at night, where an off-road light is allowed to be on."},
 ],
 "tier_table": {
  "caption": "Approximate price bands from the picks in our 2010–2024 4Runner guides (September 2026; Amazon prices move daily). Each column mounts together: the box sits on that column's bars or platform. If factory crossbars are in place, leave out the bars",
  "head": ["Upgrade", "Budget", "Mid", "Premium"],
  "rows": [
   ["Floor liners", "About $110–$150 (floor-plus-cargo kit; 2013–2024, five seats, no sliding deck)", "About $150–$210 (Husky WeatherBeater 99571, 2013–2024)", "About $200–$260 (TuxMat, 2013–2024, five seats)"],
   ["Roof rack", "About $90–$130 (InTimesAuto clamp-on crossbars, raised rails only)", "About $100–$150 (ERKUL locking crossbars, raised rails only)", "About $1,199 (Front Runner Slimline II 3/4 platform, about 59 lb)"],
   ["Cargo box", "About $450 (SportRack Vista XL; confirm its weight)", "About $599 (Yakima SkyBox 16 Carbonite, sale price) to $786 (Thule Pulse L, sale price)", "About $649 (Yakima DeepSpace 10, 30.2 lb) to $918 (INNO Wedge 660, 42 lb); confirm the clamps fit the platform"],
   ["Light bar", "About $65 (Cali Raised hidden grille brackets, 2014–2024; bar and harness extra)", "About $270 (Diode Dynamics ditch light kit) to $346 (Cali Raised 32 in hidden grille kit, 2014–2024)", "About $437 (Baja Designs Squadron Sport fog pocket kit, 2010–2024)"],
   ["Total", "About $715–$795, plus a bar and harness", "About $1,119–$1,492", "About $2,485–$2,814; platform and box leave about 19–31 lb of a 120 lb roof"],
  ],
 },
 "sections": [
  {"h": "Towing: the receiver is probably already under the bumper",
   "body": "There is no trailer hitch guide for the 2010–2024 4Runner on this site, so the hitch isn't ranked. Here "
           "is what the SUV may already have.\n\n"
           "**The receiver.** Toyota's releases for the 2013, 2017 and 2020 model years each describe an integrated "
           "tow-hitch receiver and wiring harness as standard. We did not read a release for every model year, and a "
           "used 4Runner may have had parts changed, so look under the rear bumper for a square 2 in opening and "
           "check the wiring connector. If both are there, an aftermarket trailer hitch adds nothing.\n\n"
           "**The class.** Our vehicle data records a **Class III hitch with a 2 in receiver**. The Toyota releases "
           "we read don't name a class, so read the label on the hitch itself.\n\n"
           "**The rating.** Our vehicle data lists a maximum of **5,000 lb**. Toyota's 2013 release gives the same "
           "figure, and its 2017 and 2020 releases add a maximum tongue weight of **500 lb**. Your own figures are in "
           "the owner's manual, and no receiver raises them.\n\n"
           "The receiver matters on this page because the roof figure is small. The cargo box guide sends coolers, "
           "fuel and recovery gear to a hitch cargo carrier and keeps the roof for sleeping bags, jackets and "
           "duffels.\n\n"
           "Running boards have no guide for this vehicle either, so they aren't ranked."},
  {"h": "Fifteen model years: the lines that fall inside the generation",
   "body": "The drivetrain barely changed. Wikipedia lists a 4.0-liter V6 with a 5-speed automatic, plus a 2.7-liter "
           "four-cylinder on 2WD models for 2010 only, and no listing in our guides is split by engine or drivetrain. "
           "What changed for parts is the front end, in 2014 and again in 2020, and how liner makers list the early years.\n\n"
           "Wikipedia dates the facelift to 2014: revised front and rear fascias, projector headlamps and a revised "
           "dashboard and center stack. It dates Toyota Safety Sense P to the 2020 model year, and Toyota's 2020 "
           "release says the system is standard on all grades. Liner makers draw their line a year before the "
           "facelift, at 2013, and we found nothing that explains it.\n\n"
           "Listing titles add a line of their own: several stop at 2023.",
   "table": {"caption": "2010–2024 4Runner model-year lines that change which part fits",
             "head": ["Model years", "What changed, or where listings split", "What to do"],
             "rows": [
              ["2010–2012", "Husky's 99571, TuxMat's set and the budget full kit all start at 2013", "Buy cabin liners that name your year, or ask the seller. Husky's cargo liners and MERXENG's cargo mat are listed for 2010–2024"],
              ["2010–2013", "Pre-facelift front fascia and lower grille", "Skip 2014–2024 grille brackets. iJDMTOY's 20 in kit is titled 2010–2013; fog pocket, hood hinge and roof mounts span the change"],
              ["2020–2024", "Toyota Safety Sense P standard, with a radar at the grille", "One bar behind the grille (Cali Raised). Check the dash for radar warnings after fitting any front light"],
              ["2019–2024", "Rhino-Rack's RT4B1 backbone listing names 2010–2018", "Confirm with the seller before buying the Pioneer tray and backbone"],
              ["2024", "Amazon titles for Diode Dynamics' ditch kit and Cali Raised's grille kit stop at 2023", "Ask the seller to confirm 2024; Cali Raised's own page lists 2014–2024"],
              ["2025–2026", "New generation with a new roof and cabin", "Liners, crossbars, platforms and light brackets don't carry over; a cargo box does"],
             ]}},
  {"h": "What is on the roof, and what a 120 lb figure leaves",
   "body": "Our vehicle data records raised rails and a roof load of **120 lb** for this generation. The figure is "
           "quoted on Trail4Runner's roof rack roundup, where a reader cites the owner's manual of a 2016 SR5. We "
           "could not confirm it from a Toyota document, and it may differ by year, so read your own manual. The "
           "guides treat it as a driving limit that covers everything above the roof.\n\n"
           "Start with what the roof has. Our roof rack guide finds raised side rails with factory crossbars on most "
           "SR5, TRD Off-Road, TRD Sport, Limited and Nightshade models. Toyota's 2019 release calls the TRD roof rack "
           "new and found only on the TRD Pro, and its 2020 and 2021 releases call it exclusive to that grade. The "
           "2021 release adds Yakima cargo baskets on the Trail and Venture Special Editions. We could not confirm "
           "the TRD Pro roof for 2022–2024, so look. Clamp-on crossbars need raised rails, and box clamps are "
           "made for crossbars, not basket tubing.\n\n"
           "Factory bars usually take a box. An etrailer expert answer about a 2015 Limited says the Yakima SkyBox 12 fits "
           "bars no larger than 3-1/2 in wide by 1-11/16 in tall, spread 24 to 42 in. Each box has its own range, "
           "such as 23-5/8 to 34-3/8 in on the Pulse L and 32 to 46 in on the DeepSpace 10. The same expert gives 57 "
           "in from the center of the front crossbar to the hatch seam for that SkyBox 12, so measure both before "
           "ordering.",
   "table": {"caption": "What is left of a 120 lb roof figure, using the weights published in our guides",
             "head": ["On the roof", "Published weight", "Left of 120 lb"],
             "rows": [
              ["Yakima DeepSpace 10", "30.2 lb", "89.8 lb, less the bars"],
              ["Thule Pulse L", "36 lb", "84 lb, less the bars; the guide plans on 60 to 75 lb of gear"],
              ["Rhino-Rack MasterFit 440L", "38.6 lb", "81.4 lb, less the bars"],
              ["INNO Wedge 660", "42 lb", "78 lb, less the bars"],
              ["Yakima SkyBox 16 Carbonite", "47 lb", "73 lb, less the bars"],
              ["Front Runner Slimline II 3/4 platform", "About 59 lb installed", "About 61 lb"],
              ["Front Runner Slimline II full platform", "About 91 lb installed", "About 29 lb"],
              ["3/4 platform plus Pulse L", "About 95 lb", "About 25 lb"],
              ["Rough Country 88201, Front Runner Slimsport, SportRack Vista XL", "Not published", "Ask the seller before planning a load"],
             ]}},
  {"h": "Seats, cargo floor and trim: which 4Runner do you have?",
   "body": "Trim names changed over fifteen years, and most of them don't change fit. What matters is a short list of "
           "equipment.\n\n"
           "- **Third row.** Our vehicle data lists it as an option on the SR5 and Limited, and Toyota's 2017 and "
           "2020 releases say the same. The seat folds into the cargo floor, so the cargo liner is Husky's 25741. "
           "TuxMat and the budget kit name five seats.\n"
           "- **Sliding cargo deck.** Toyota's releases describe a pull-out deck that supports up to 440 lb, and the "
           "2013 release mentions it with the Limited. Husky's 25722 and the budget kit exclude it.\n"
           "- **Trail and TRD Off-Road.** These are one grade under two names. Toyota's 2017 release says the Trail "
           "and Trail Premium became the TRD Off-Road and TRD Off-Road Premium that year.\n"
           "- **TRD Pro.** Our lighting guide dates it to 2015–2024 and notes its own grille, updated for the radar "
           "in 2020. Look for the TRD roof rack on 2019 and later models, and ask Cali Raised whether its hidden grille brackets "
           "suit that grille.\n\n"
           "Our floor liner guide's rule covers all of it: buy cabin liners by model year and cargo liners by cargo "
           "floor, not by trim name."},
  {"h": "Buying for a used 4Runner: six checks, then the order to fit things",
   "body": "A used 4Runner arrives with someone else's choices. Write down six things before ordering.\n\n"
           "1. **Model year**: 2010–2012, 2013, 2014–2019 or 2020–2024.\n"
           "2. **Seats and cargo floor**: five or seven; standard, sliding deck or third row.\n"
           "3. **Roof**: raised rails with crossbars, rails without bars, a basket, or bare mounting points left by a "
           "platform.\n"
           "4. **Crossbar spread**, center to center, and the distance from the front bar to the hatch seam.\n"
           "5. **Front end**: whether a previous owner already fitted lights or brackets.\n"
           "6. **Receiver**: present, with its wiring connector.\n\n"
           "Fit the four in this order.\n\n"
           "1. **Floor liners.** No tools. Remove the factory mat, hook the driver liner onto Toyota's retention "
           "posts and press the pedals to the floor.\n"
           "2. **Crossbars or platform.** Set clamp-on bars at the spread the box maker specifies. For a platform, "
           "our guide says to remove the factory rails and keep the hardware.\n"
           "3. **Cargo box.** Mount it forward and open the hatch slowly to check the gap before tightening the "
           "clamps.\n"
           "4. **Lights.** They go last because a roof light kit and a platform both use the roof's factory mounting "
           "points. We could not confirm that Cali Raised's roof brackets and a platform can share them, so ask both "
           "makers. Use a harness with a relay, a fuse and a switch."},
 ],
 "avoid": [
  {"h": "A 2013–2024 liner set or a 2014–2024 grille kit on an early 4Runner", "body": "Most cabin sets start at 2013, and Cali Raised's hidden grille brackets start at 2014. Earlier models need a listing that names their year."},
  {"h": "A cargo liner ordered before looking at the cargo floor", "body": "Husky's 25722 fits the standard floor only, the 25741 is for the third row, and neither is for the sliding deck."},
  {"h": "Loading the roof to the rack's or the box's rating", "body": "A 300 lb platform or a 110 lb box doesn't change the 120 lb roof figure. Bars or platform, box and gear have to fit under the number in your owner's manual."},
  {"h": "2025–2026 part numbers on a 2010–2024 roof or floor", "body": "Rough Country's 88205, Front Runner's KSTF004T and Husky's 96531 are parts for the new generation. Buy the number listed for your model year."},
 ],
 "verdict": {
  "thesis": "On the 2010–2024 4Runner, buy floor liners by model year, seat count and cargo floor first, sort out the roof second, add a light cargo box third, and leave lighting for last, matched to the front end your model year has.",
  "body": "Most fit mistakes on the fifth-generation 4Runner come from three lines inside its fifteen years: 2013 for "
          "cabin liners, 2014 for the front fascia and 2020 for the radar. Floor liners need the year, the seat count "
          "and the cargo floor, and they cost the least, so they go first. The roof rack decision is second because "
          "it starts with a look, not a purchase: factory crossbars are enough for a box, and even a 3/4 platform "
          "spends about half of a 120 lb roof figure before anything is loaded.\n\n"
          "The cargo box is third and should be the lightest one that holds your gear. The light bar is fourth "
          "because the mount depends on the year and most of the light is for off-road use. Skip the trailer hitch "
          "shopping until you have looked under the bumper, since Toyota's releases list a receiver as standard. If "
          "you have moved on to a 2025–2026 4Runner, shop from that generation's guides. A box can come with you, "
          "while liners, crossbars, platforms and brackets can't.",
 },
 "sources": [
  ["Toyota 4Runner (N280): grades, engines, 2014 facelift, TRD Off-Road name, 2020 TSS-P (Wikipedia)", "https://en.wikipedia.org/wiki/Toyota_4Runner_(N280)"],
  ["2013 Toyota 4Runner: towing, hitch receiver, sliding rear cargo deck, third row, roof rack (Toyota Newsroom)", "https://pressroom.toyota.com/2013-toyota-4runner-true-suv-capaability/"],
  ["2017 Toyota 4Runner: towing and tongue weight, receiver on all grades, TRD Off-Road name (Toyota Newsroom)", "https://pressroom.toyota.com/2017-toyota-4runner-everday-suv-explore-where-when-you-want/"],
  ["2020 Toyota 4Runner: Toyota Safety Sense P on all grades, towing, TRD Pro roof rack (Toyota Newsroom)", "https://pressroom.toyota.com/the-adventurer-toyota-4runner-gains-new-safety-and-multimedia-tech-for-2020/"],
  ["2019 Toyota 4Runner: new TRD roof rack on the TRD Pro only (Toyota Newsroom)", "https://pressroom.toyota.com/2019-toyota-4runner-strengthens-legacy-35-year/"],
  ["2021 Toyota 4Runner: Yakima cargo baskets on the Trail and Venture Special Editions (Toyota Newsroom, PDF view)", "https://pressroom.toyota.com/?generate_pdf=64905"],
  ["Top 5th Gen 4Runner Roof Racks, with the 120 lb owner's manual figure in a reader comment (Trail4Runner)", "https://trail4runner.com/2017/12/04/5th-gen-4runner-roof-racks/"],
  ["Husky Liners: WeatherBeater vs X-act Contour (Husky Liners)", "https://huskyliners.com/blog/husky-liners-weatherbeater-vs-xact-contour/"],
  ["TuxMat home page (TuxMat)", "https://tuxmat.com/"],
  ["Rough Country roof rack 88201, 2010–2024 4Runner (Rough Country)", "https://www.roughcountry.com/product/toyota-4runner-roof-rack-88201"],
  ["Front Runner Slimline II 3/4 kit KRTF050T (4Runner Lifestyle)", "https://www.4runnerlifestyle.com/products/front-runner-4runner-2010-present-3-4-slimeline-ii-roof-rack-kit"],
  ["Front Runner Slimsport KSTF003T (Dometic)", "https://www.dometic.com/en-us/product/toyota-4runner-roofrack-slimsport-kstf003t"],
  ["Thule Pulse L TH615 specs (etrailer)", "https://www.etrailer.com/Roof-Box/Thule/TH615.html"],
  ["Cargo box on 2015 4Runner Limited factory crossbars (etrailer expert answer)", "https://www.etrailer.com/question-239020.html"],
  ["Yakima DeepSpace 10 (Yakima)", "https://yakima.com/collections/roof-boxes/products/deepspace-10"],
  ["32 in Hidden Grille LED Light Bar Brackets Kit, 2014–2024 4Runner (Cali Raised LED)", "https://caliraisedled.com/products/32-hidden-grille-led-light-bar-brackets-kit-for-2014-2024-toyota-4runner"],
  ["52 in Curved LED Light Bar Roof Brackets Kit, 2003–2024 4Runner (Cali Raised LED)", "https://caliraisedled.com/products/52-curved-led-light-bar-roof-brackets-kit-for-2003-2024-toyota-4runner"],
  ["Baja Designs Squadron Sport Fog Pocket Kit, 4Runner 2010–2024 (4Runner Lifestyle)", "https://www.4runnerlifestyle.com/products/baja-designs-squadron-r-2-0-sport-fog-pocket-light-kit-for-4runner-2010-2024"],
 ],
}
