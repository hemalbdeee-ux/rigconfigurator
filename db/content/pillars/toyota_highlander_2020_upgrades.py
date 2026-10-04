"""Upgrades pillar: 2020–2026 Toyota Highlander (4th gen, XU70; three-row midsize SUV, no bed).
Hub page: ranks the four published Highlander category guides and links to them. No product picks or ASINs here
(the site pulls each guide's #1 pick). Every price band comes from the linked guides' picks[].price fields or price
text in those guides (the generic 7-seat carpet-style set's FITS band; etrailer's Thule WingBar Evo, Yakima SkyLine
and Yakima BaseLine prices in the roof rack guide); vehicle facts from db/migrations/003_vehicles.sql (SUV, flush
rails "with fixed points on railed trims (per etrailer); some base trims may be bare", no stored roof load figure,
hitch class 3 with a 2 in receiver, 5,000 lb, three rows, "Hybrid shares fit", Grand Highlander "different vehicle
(2024+)"), the four guides and their sources, and five pages opened for this page on 2026-10-04: Wikipedia's Toyota
Highlander page (fourth generation on sale December 2019 for the 2020 model year; GA-K platform; grades L, LE, XLE,
XSE, Limited, Platinum; Hybrid on all but L and XSE; XSE added for 2021; 2.4L turbo four replaced the 3.5L V6 for
the 2023 model year; L discontinued for 2024; LE discontinued for 2026; Grand Highlander introduced February 2023
as a larger alternative sharing the name and GA-K platform; fifth-generation Highlander unveiled February 10, 2026,
sales set to start in late 2026), Toyota's 2025 Highlander release (2.4L turbo models up to 5,000 lb; all Hybrid
models up to 3,500 lb; LE seating for eight; Hybrid XLE up to eight; Hybrid Platinum second-row captain's chairs;
seven seats standard with a bench optional on some grades; XSE, Limited and Platinum on 20 in wheels; XLE with
hands-free power liftgate; roof rails mentioned with no grade list we could read), Toyota's parts page for the Tow
Hitch Receiver PT228-48174 (accessory; "engineered to help accommodate your Highlander's maximum tow rating";
12-month warranty; in-store pickup only; no model years, class or rating as we read it), Toyota's 2026 Highlander
newsroom page (7- or 8-person seating; gas models add standard all-wheel drive; opened, not cited) and
toyota.com/highlander (opened, not cited; it added nothing). All were read through a text extraction, so the page
says "as we read" where a missing item matters. Not every fact read is printed (the roof rail mention, the XLE
liftgate, Hybrid XLE seating and 2026 all-wheel drive are left out; GA-K appears only in a source label). Toyota's 2023 Highlander release timed
out and is not cited. The hitch guide's dealer towing page (Beaver Toyota) was not reopened and is not cited here;
Toyota's own 2025 release carries the same 5,000 lb and 3,500 lb figures.
Not verified, and worded as such in the text: the Highlander's roof load limit from any Toyota US document (165 lb
is Toyota Canada's crossbar rating plus rack makers' ratings); which grades and years have roof rails, and whether
any L or LE is bare; the spread of Toyota's and BRIGHTLINES' bolt-in bars and of the clamp-on sets; second-row seating by grade for every
year; whether any grade ships with a factory receiver, and the class and rating of Toyota's accessory receiver; the
2020–2022 V6 tow rating from a Toyota document (the hitch guide says "commonly listed at 5,000 lb"); whether
front-wheel-drive gas models carry the same tow figure every year; the Highlander's own tongue weight limit and
whether weight distribution is allowed; which spare each grade carries; what in the Hybrid floor differs beyond
the guide's "battery under the second-row seat"; SportRack Vista XL weight and load rating; TLAPS hitch ratings;
2025–2026 fit of listings whose titles stop at 2024 or 2025; and any fit on the fifth-generation Highlander.
No Highlander guide exists for running boards or lighting; neither is ranked. Amazon URLs in the guides' source
lists are not repeated here.
"""

KIND = "upgrades"
KEY = ("toyota", "highlander", "2020-present")
CATEGORIES = ["floor-mats", "roof-racks", "hitches", "cargo-boxes"]

TITLE = "2020–2026 Toyota Highlander Upgrades, Ranked: 4 Mods in Order, With Hybrid and XSE Fit Traps"
META = ("Four 2020–2026 Highlander upgrades in buying order: floor liners, roof rack, trailer hitch and cargo box, "
        "with Hybrid, XSE, roof rail and Grand Highlander checks.")

FAQ = [
 ("What should I upgrade first on a 2020–2026 Toyota Highlander?",
  "Floor liners, then crossbars. Liners cost the least, about $110–$160 for a two-row or three-row set in the "
  "floor liner guide, and they need two facts from you: captain's chairs or a bench in the second row, and gas "
  "or Hybrid. Crossbars are second at about $80–$140 for clamp-on sets, provided the roof has side rails. A "
  "trailer hitch is third, at about $244–$257 for a brand-name receiver. A cargo box is last because it costs "
  "the most and needs the bars first."),
 ("Do Grand Highlander parts fit the regular Highlander?",
  "No, with two exceptions. Wikipedia says the Grand Highlander was introduced in February 2023 as a larger alternative, and the guides treat it as a separate vehicle from "
  "the 2024 model year. It uses its own liners, crossbars and hitches, such as Draw-Tite's 76639. The "
  "exceptions: a cargo box clamps to crossbars, so the box can move between the two while the bars can't, and "
  "Tekonsha's 118827 harness is listed for both the 2020–2025 Highlander and the 2024–2025 Grand Highlander."),
 ("Which floor liners fit a 7-seat, 8-seat or Hybrid Highlander?",
  "Match the second row and the powertrain. A 7-seat Highlander has two captain's chairs and an 8-seat one has "
  "a bench, and the floor liner guide says the Hybrid's battery sits under the second-row seat. LASFIT's set is "
  "for 8-seat gas models. MAXPRO's is not for the Hybrid and doesn't state seating. TGBROS lists a bench or "
  "buckets with a console and doesn't mention the Hybrid. A generic carpet-style set, about $70–$110, is listed "
  "for 7-seat models including the Hybrid. Husky's titles carry no Hybrid exclusion and don't state seating, so "
  "use Husky's fit tool."),
 ("Does my Highlander have roof rails, and what if the roof is bare?",
  "The crossbar listings in the roof rack guide name the XLE, XSE, Limited and "
  "Platinum, gas and Hybrid, as having factory side rails. None names the L or LE, and etrailer lists naked-roof "
  "racks for the 2023 Highlander, which suggests some left the factory bare. On a bare roof, rail bars have nothing to hold. You need a door-frame system such "
  "as Yakima's BaseLine, which etrailer lists at about $605–$774."),
 ("How much weight can the Highlander's roof carry with crossbars and a cargo box?",
  "Plan around 165 lb for bars, box and gear together. That is the evenly distributed figure Toyota Canada lists "
  "for Toyota's Highlander crossbars, and the rating etrailer and The Rack Shop give for Thule and Yakima "
  "systems. Two clamp-on sets print 220 and 260 lb, which are sellers' bar "
  "ratings. The guides found no separate roof figure published for this generation, so the owner's manual "
  "decides. On 165 lb bars a 47 lb Yakima SkyBox 16 leaves 118 lb before the bars' own weight."),
 ("Does the Highlander come with a trailer hitch from the factory?",
  "We could not confirm that any grade does. Toyota's parts site sells a Tow Hitch Receiver, part PT228-48174, "
  "as a Highlander accessory, for in-store pickup only. As we read that page, it names no model years, class or "
  "rating. Look under the rear bumper for a square "
  "2 in opening and read the window sticker. If one is there, you need a ball mount or a rack, not a trailer hitch."),
 ("How much can a 2020–2026 Highlander tow, and does a 6,000 lb hitch raise it?",
  "No hitch raises it. Toyota's 2025 release says the 2.4L turbo models can tow up to 5,000 lb and all Hybrid "
  "models up to 3,500 lb, and the site's vehicle data lists 5,000 lb as the maximum. The 2020–2022 V6 is also "
  "commonly listed at 5,000 lb; we did not confirm that from a Toyota document, so read the owner's manual. The "
  "lower of hitch and vehicle applies. A 6,000 lb CURT 13460 on a Hybrid is still a 3,500 lb setup."),
 ("Did the 2023 switch from the V6 to the turbo four change which accessories fit?",
  "Not in any of the four guides. Wikipedia says the 2.4L turbocharged four-cylinder replaced the 3.5L V6 for "
  "the 2023 model year. etrailer lists the same Thule fit kit, TH22RE, for 2020 "
  "through 2023 and for 2025. CURT lists one hitch, the 13460, for 2020–2026. Titles differ in how far they run: Husky's X-act Contour kit stops at 2024, and the TGBROS set, the Tekonsha harness and several crossbar listings stop at 2025."),
 ("How much does it cost to add all four upgrades to a Highlander?",
  "From the prices on the four guides' picks, a budget build runs about $780–$920: LASFIT liners, Richeer "
  "crossbars, a TLAPS receiver and SportRack's Vista XL. A mid build runs about $1,053–$1,146 with a TGBROS or "
  "MAXPRO three-row set, Snailfly bars, a B&W or CURT hitch and Yakima's SkyBox 16 Carbonite. A premium build with Husky's kit and cargo liner, a Thule WingBar Evo system, a hitch with Tekonsha's harness "
  "and a Thule Pulse L or Motion 3 XXL runs about $2,095–$2,732. Subtract the hitch if a receiver is fitted."),
]

ARTICLE = {
 "dek": "Four upgrades for the fourth-generation Highlander, in the order most owners should buy them. Fit on this "
        "three-row SUV turns on a short list of facts: captain's chairs or a bench in the second row, gas or "
        "Hybrid, rails on the roof or not, an XSE badge or not, and whether the listing was written for the "
        "Highlander or the larger Grand Highlander.",
 "author": "jake-morrison",
 "reviewed": "2026-10-04",
 "method": "We did not install any of these parts ourselves. The order comes from the four fit-checked 2020–2026 "
           "Highlander guides on this site, weighing how many owners each upgrade suits, what it costs and which "
           "purchase depends on another (a cargo box needs crossbars first). Price bands are the prices on those "
           "guides' picks, checked in September 2026, and are approximate. Vehicle facts come from the site's "
           "vehicle data, the guides' sources, Wikipedia's Highlander page, Toyota's 2025 Highlander release "
           "and Toyota's parts site. Where we couldn't confirm a factory detail, the text says so.",
 "takeaways": [
  "**Count the second-row seats and read the badge.** Captain's chairs or a bench, and gas or Hybrid, decide the floor liner set; MAXPRO and LASFIT exclude the Hybrid.",
  "**It isn't a Grand Highlander.** That is a larger vehicle sold from the 2024 model year, with its own liners, crossbars and hitches.",
  "**Look at the roof before buying bars.** Listings name the XLE, XSE, Limited and Platinum as railed; none names the L or LE.",
  "**Plan the roof around 165 lb.** That is Toyota Canada's crossbar rating, and it covers bars, cargo box and gear together.",
  "**No hitch raises the tow rating.** Toyota lists up to 5,000 lb for 2.4L turbo models and 3,500 lb for the Hybrid, and CURT's 13460 excludes the XSE.",
 ],
 "priority": [
  {"category": "floor-mats",
   "h": "1. Floor liners first: three rows to cover, and two answers every listing needs",
   "why": "Floor liners lead on the Highlander because they cost the least and every owner can use them. Two "
          "facts decide fit. The first is the second row: captain's chairs make a 7-seat Highlander and a bench "
          "makes an 8-seat one. The second is powertrain. The "
          "floor liner guide says the Hybrid's battery sits under the second-row seat, and MAXPRO and LASFIT "
          "list their sets as not for the Hybrid. Prices run about $110–$150 for LASFIT's front and second-row "
          "set (8-seat, gas), about $120–$160 for the TGBROS or MAXPRO three-row sets and about $220–$300 for "
          "Husky's X-act Contour three-row kit, which Husky says is made in the USA with a lifetime warranty "
          "against cracks and breaks. Smartliner's third-row liner adds about $40–$70 and Husky's 25791 cargo "
          "liner about $100–$150. The trade-off is paperwork: TGBROS and MAXPRO publish no warranty terms, and "
          "the Husky kit's title stops at 2024.",
   "skip_if": "The factory mats are holding up, the cabin stays dry and nobody climbs into the third row in muddy shoes."},
  {"category": "roof-racks",
   "h": "2. Roof rack second: cheap crossbars, provided the roof has rails",
   "why": "A roof rack ranks second because crossbars are cheap and nothing else goes on the roof without them. The site's vehicle data records flush side rails on most trims. The Amazon "
          "listings in the roof rack guide name the XLE, XSE, Limited and Platinum, gas and Hybrid; none names "
          "the L or LE, and etrailer also lists naked-roof systems for the 2023 Highlander. Bars attach three "
          "ways. Clamp-on sets grip the rail: about $80–$120 for Richeer's or HEKA's, about $90–$130 for "
          "Snailfly's and about $100–$140 for the lockable set. Bolt-in bars use the rail's preset points: "
          "about $130–$170 for BRIGHTLINES' and about $300–$450 for Toyota's PT767-48200. Thule and Yakima "
          "fixed-point systems run about $695–$705 on etrailer. The trade-off is proof: the cheapest sets "
          "publish the least, and no bar rating replaces the limit in the owner's manual.",
   "skip_if": "The roof is bare, or everything you carry fits inside or on a hitch carrier."},
  {"category": "hitches",
   "h": "3. Trailer hitch third: check for a receiver, then check for an XSE badge",
   "why": "A trailer hitch ranks third. It costs more than crossbars and takes real work under the vehicle, but "
          "it carries what the roof can't. Look under the rear bumper first: Toyota sells a receiver as an "
          "accessory, so a dealer may have fitted one. If there is none, the grade decides the part. CURT lists "
          "its 13460 for 2020–2026 Highlanders excluding the XSE, at 6,000 lb with 900 lb of tongue weight, "
          "about $257. B&W's RH670220BW is listed for XSE and non-XSE models at 5,000 lb and 750 lb, about "
          "$244. Reese's Class IV 84439 kit with wiring runs about $300–$400 and excludes 2020–2023 models with "
          "twin-tip exhaust. A budget TLAPS receiver runs about $140–$200, with ratings to confirm on the "
          "listing. etrailer says every 2023 Highlander hitch it sells needs the underbody panel trimmed or "
          "removed and fits with the 18 in spare only. If you tow or carry bikes most weeks, move this slot up "
          "to second.",
   "skip_if": "A square 2 in receiver already shows under the rear bumper; buy a ball mount and check the wiring instead."},
  {"category": "cargo-boxes",
   "h": "4. Cargo box last: the biggest spend, held to the bars' 165 lb and spread",
   "why": "A cargo box comes last because it is the biggest spend, it can't go on until the crossbars are, and it is a trip accessory, not a daily one. Two numbers from the bars decide the choice. The first is weight. The cargo box guide "
          "plans around 165 lb for bars, box and gear, and the picks weigh 36 lb (Thule Pulse L) to 57.2 lb "
          "(Thule Motion 3 XXL). The second is spread: The Rack Shop lists a 31 in maximum for its Thule "
          "Fixpoint kit, and all six picks mount inside that. Prices run about $450 for SportRack's Vista XL, "
          "about $599 on sale for Yakima's SkyBox 16 Carbonite, about $699 for the CBX 16, about $786 for the "
          "Pulse L, about $918 for the INNO Wedge 660 and about $1,250 for the Motion 3 XXL. The trade-offs "
          "are height and fuel: fueleconomy.gov puts a roof box at 10–25% worse at 65–75 mph. If every seat is "
          "full on every trip, move this slot up to third.",
   "skip_if": "The third row stays folded on trips, or the heavy items can ride on a hitch carrier."},
 ],
 "tier_table": {
  "caption": "Approximate price bands from the picks in the four 2020–2026 Highlander guides (September 2026; Amazon prices move daily). Each cargo box sits on the same column's crossbars",
  "head": ["Upgrade", "Budget", "Mid", "Premium"],
  "rows": [
   ["Floor liners", "About $110–$150 (LASFIT front and second row; 8-seat gas only)", "About $120–$160 (TGBROS or MAXPRO three-row set; MAXPRO is not for the Hybrid)", "About $320–$450 (Husky X-act Contour kit at about $220–$300 plus Husky 25791 cargo liner at about $100–$150)"],
   ["Roof rack", "About $80–$120 (Richeer clamp-on bars, 220 lb listed)", "About $90–$130 (Snailfly clamp-on bars, listed for 2020–2026)", "About $705 (Thule WingBar Evo fixed-point system on etrailer, 165 lb)"],
   ["Trailer hitch", "About $140–$200 (TLAPS Class 3 receiver; ratings on the listing)", "About $244 (B&W RH670220BW, lists the XSE) or $257 (CURT 13460, not the XSE)", "About $284–$327 (the B&W or CURT plus Tekonsha's 118827 harness at about $40–$70)"],
   ["Cargo box", "About $450 (SportRack Vista XL; set the bars to one of its three positions)", "About $599 (Yakima SkyBox 16 Carbonite, sale price; regular $749)", "About $786 (Thule Pulse L, sale price) to $1,250 (Thule Motion 3 XXL, box alone)"],
   ["Total", "About $780–$920", "About $1,053–$1,146", "About $2,095–$2,732"],
  ],
 },
 "sections": [
  {"h": "Seven seats or eight, gas or Hybrid: the two answers every floor liner listing needs",
   "body": "**Second row.** Two captain's chairs make a 7-seat Highlander and a three-person bench makes an "
           "8-seat one. The floor liner guide notes that some 7-seat Highlanders put a small console between "
           "the chairs and others leave an open walkway. Don't go by grade. As we read Toyota's 2025 release, "
           "the LE has seating for eight, the Hybrid Platinum has second-row captain's chairs, and on some "
           "grades seven seats are standard with a bench optional. We could not map seating to every grade and "
           "year, so open the rear door and count.\n\n"
           "**Powertrain.** The guide says the Highlander Hybrid's battery sits under the second-row seat, "
           "which changes the second-row floor. That is why two sets in the table are gas only. Wikipedia says "
           "the Hybrid is available on every grade except the L and XSE, so look for the badge on the "
           "liftgate.\n\n"
           "**Rows.** The cabin has four zones: front, second row, third row and cargo. A two-row set plus "
           "Smartliner's third-row liner, about $40–$70, covers three rows. Husky's 25791 cargo liner, about "
           "$100–$150, runs to the back of the second row and folds with the third row.",
   "table": {"caption": "What each cabin set in the floor liner guide lists for the 2020–2026 Highlander",
             "head": ["Set", "Rows covered", "Second row", "Hybrid", "Years listed"],
             "rows": [
              ["Husky X-act Contour 4-piece", "Front, second, third", "Not in the title; use Husky's fit tool", "No exclusion in the title; confirm", "2020–2024"],
              ["TGBROS 3-row set", "Front, second, third", "Bench, or buckets with a console", "Not mentioned; ask the seller", "2020–2025"],
              ["MAXPRO 3-row liners", "Front, second, third", "Not stated; ask the seller", "Not for the Hybrid", "2020–2026"],
              ["LASFIT TPE liners", "Front and second", "8-seat bench only", "Not for the Hybrid", "2020–2026"],
              ["Generic carpet-style 4-piece set", "Confirm on the listing", "7-seat captain's chairs", "Lists the Hybrid", "2020–2025"],
              ["Husky WeatherBeater 15321 and 12791", "Front; second row", "Confirm the second-row piece", "No exclusion in the titles; confirm", "2020–2026"],
             ]}},
  {"h": "Rails, fixed points and 165 lb: the roof as a base for a cargo box",
   "body": "**The rails.** The site's vehicle data records flush side rails on most trims and holds no roof "
           "load figure. etrailer classes the rails as flush-mounted with fixed mounting points. Richeer's "
           "listing says raised side rails and BRIGHTLINES' says flush side rails, so compare the mount in the "
           "listing photos with your own rail.\n\n"
           "**Three ways to mount bars.**\n\n"
           "- **Clamp-on sets** grip the rail and cost about $80–$140. Measure the spread you end up with.\n"
           "- **Bolt-in bars** use the rails' preset points: Toyota's PT767-48200 and BRIGHTLINES' "
           "replacement. They sit at fixed positions, and the guides publish no spread for either, so measure "
           "center to center before choosing a box. Toyota's US parts page lists the XLE, Limited and Platinum "
           "only; have a dealer check an XSE or a Hybrid by VIN.\n"
           "- **Fixed-point systems** from Thule and Yakima cost about $695–$705 on etrailer. The Rack Shop "
           "lists a 31 in maximum spread for its Thule Fixpoint kit.\n\n"
           "**The limit.** Toyota Canada lists 75 kg (165 lb), evenly distributed, for Toyota's crossbars. "
           "etrailer rates the Thule WingBar Evo and Yakima SkyLine systems at 165 lb, and AHG Auto Service "
           "quotes 75 kg for 2020–2023 models. BRIGHTLINES lists 154 lb. The 220 lb and 260 lb on two Amazon "
           "sets are sellers' bar ratings. The guides found no separate roof figure for this generation, so "
           "use the lowest number and check the owner's manual.\n\n"
           "**Liftgate.** A long box set too far back meets the liftgate. Thule gives a front-clearance figure "
           "of more than 54 13/16 in for the 91.7 in Motion 3 XXL.",
   "table": {"caption": "Boxes in the cargo box guide on 165 lb Highlander bars (makers' and etrailer's figures; subtraction is ours)",
             "head": ["Box", "Box weight", "Crossbar spread", "Inside a 31 in kit?", "Left of 165 lb before the bars"],
             "rows": [
              ["Thule Pulse L", "36 lb", "23-5/8 to 34-3/8 in", "Yes", "129 lb; the box's own limit is 110 lb"],
              ["INNO Wedge 660", "42 lb", "24–39 in", "Yes", "123 lb; the box's own limit is 110 lb"],
              ["Yakima SkyBox 16 Carbonite", "47 lb", "24–34.5 in", "Yes", "118 lb"],
              ["Yakima CBX 16", "57 lb", "24–35.5 in", "Yes", "108 lb"],
              ["Thule Motion 3 XXL", "57.2 lb", "21-13/16 to 36-9/16 in", "Yes", "About 108 lb"],
              ["SportRack Vista XL", "Not published", "Fixed at 25-7/8, 27-7/8 or 29-7/8 in", "Yes", "Ask the seller"],
              ["Yakima DeepSpace 10 (not a pick)", "30.2 lb", "32–46 in", "No", "Does not mount on that kit"],
             ]}},
  {"h": "Towing: gas or Hybrid, the 2023 engine change and the receiver question",
   "body": "**The rating.** The site's vehicle data lists a maximum of **5,000 lb**. Toyota's 2025 release says "
           "the 2.4L turbo models can tow up to 5,000 lb and all Hybrid models up to **3,500 lb**. Your figure is in the owner's "
           "manual.\n\n"
           "**The engine change.** Wikipedia says the 2.4L turbocharged four-cylinder replaced the 3.5L V6 for "
           "the 2023 model year. The hitch guide notes that the 2020–2022 V6 is commonly listed at 5,000 lb as "
           "well. We did not confirm that from a Toyota document.\n\n"
           "**The receiver.** The vehicle data records Class III with a 2 in receiver. Toyota's parts site "
           "sells a Tow Hitch Receiver, PT228-48174, as an accessory with a 12-month warranty. As we read that "
           "page, it gives no model years, class or rating. We could not confirm that any grade leaves the "
           "factory with a receiver, so look under the bumper.\n\n"
           "**What a bolt-on hitch changes.** It adds a receiver, not rating. The lower of hitch and vehicle "
           "applies. CURT's Class 3 13460 is rated at 6,000 lb with 900 lb of tongue weight, B&W's RH670220BW "
           "at 5,000 lb and 750 lb, and Reese's Class IV 84439 at 6,000 lb and 900 lb. We could not confirm "
           "the Highlander's own tongue weight limit, or whether Toyota allows weight distribution; both are "
           "owner's manual questions.\n\n"
           "**The XSE.** Added for 2021, it has its own rear fascia and twin-tip exhaust. CURT excludes it, "
           "Reese excludes 2020–2023 twin-tip models, and etrailer lists the B&W for it.\n\n"
           "**The spare.** etrailer's notes for every 2023 Highlander hitch it sells say the hitch fits with "
           "the 18 in spare only. Toyota's 2025 release puts the XSE, Limited and Platinum on 20 in wheels. We "
           "could not confirm which spare each grade carries, so look at yours.\n\n"
           "**Wiring.** Tekonsha's 118827, about $40–$70, is a plug-in 4-way flat harness listed for "
           "2020–2025. Some other harness listings say a factory tow "
           "package is required, so confirm the connector with the seller."},
  {"h": "Highlander or Grand Highlander, 2014–2019 or 2020 on, and listings that stop early",
   "body": "**Grand Highlander.** The guides treat it as a larger, separate vehicle from the 2024 model year, with its own liners, bars and hitches. Only a cargo box and Tekonsha's 118827 harness are listed across both. Skip any listing that names "
           "both vehicles for one liner, bar or hitch.\n\n"
           "**2014–2019 parts.** The floor liner guide says the 2020 Highlander has a new floor, and Husky's "
           "99601 set is a 2014–2019 part. Buy liners and bars whose years start at 2020. Hitches need a "
           "closer read, because Reese lists the 84439 across 2014–2023 with its twin-tip exclusion.\n\n"
           "**Inside the generation.** Per Wikipedia, the XSE arrived for 2021, the turbo four replaced the V6 "
           "for 2023, the L was dropped for 2024 and the LE for 2026. None of this splits a part number in "
           "the guides.\n\n"
           "**Listings that stop early.**\n\n"
           "- **Through 2024:** Husky's X-act Contour kit and the B&W hitch's Amazon title. etrailer lists the "
           "B&W through 2026.\n"
           "- **Through 2025:** the TGBROS liners, the Richeer, HEKA, lockable and BRIGHTLINES bars on Amazon, "
           "the TLAPS hitch, the Reese kit's Amazon title and the Tekonsha harness.\n"
           "- **Through 2026:** the MAXPRO and LASFIT liners, Husky's WeatherBeater pieces, Snailfly's bars "
           "and CURT's 13460.\n\n"
           "**The next Highlander.** Wikipedia says a fifth-generation Highlander was unveiled on February 10, "
           "2026, with sales set to start in late 2026. No part in the four guides is listed for it, and we "
           "have no fit data for it."},
  {"h": "Roof or hitch for the heavy gear, and the order to fit all four",
   "body": "- **The roof takes bulky, light gear.** With 165 lb for bars, box and contents, a hard box leaves "
           "roughly 90 to 115 lb for gear.\n"
           "- **The hitch takes heavy gear.** Tongue ratings in the hitch guide run from 500 lb on etrailer's "
           "own hitch to 900 lb on the CURT and Reese, though the Highlander's limit in the owner's manual "
           "still governs.\n"
           "- **Bikes go on the hitch.** The boxes are 33 to 38 in wide and The Rack Shop's Thule kit uses "
           "50 in bars, so a box leaves little room for a bike mount. CURT says the 13460 is not compatible "
           "with vertical hanging bike racks.\n"
           "- **Fuel.** fueleconomy.gov puts a rooftop box at 10–25% worse at 65–75 mph and a rear-mounted "
           "carrier at 1–5% on the highway. Take the box off between trips, on the Hybrid most of all.\n\n"
           "Fit the four in this order.\n\n"
           "1. **Floor liners.** Remove the factory mats, hook the driver liner onto Toyota's retention posts "
           "and press the pedals to the floor.\n"
           "2. **Crossbars.** Set the front bar, then the rear, and tighten side to side in "
           "steps.\n"
           "3. **Trailer hitch.** Lower the spare and trim or remove the underbody panel as the instructions "
           "show. etrailer's reported times for the B&W run from about 50 minutes to more than 2 hours. "
           "etrailer notes the CURT may limit the hands-free liftgate, so test it afterward.\n"
           "4. **Cargo box.** With a helper, center it, slide it forward and open the liftgate slowly before "
           "tightening the clamps.\n\n"
           "Running boards and lighting have no Highlander guide on this site yet, so they aren't ranked."},
 ],
 "avoid": [
  {"h": "A listing that says Grand Highlander, or both", "body": "The Grand Highlander is a larger vehicle with its own liners, crossbars and hitches. Only a cargo box and Tekonsha's 118827 harness are listed across both."},
  {"h": "A gas-only or wrong-layout liner set", "body": "MAXPRO and LASFIT exclude the Hybrid, LASFIT is cut for the 8-seat bench, and the generic carpet-style set is for 7-seat captain's chairs."},
  {"h": "Loading the roof to the printed bar rating", "body": "A 260 lb bar doesn't change the roof. Toyota Canada, Thule and Yakima figures are 165 lb, and bars, box and gear all count against it."},
  {"h": "A hitch bought without reading the exclusion line", "body": "CURT's 13460 excludes the XSE and Reese's 84439 excludes 2020–2023 twin-tip exhaust. A 6,000 lb hitch on a 3,500 lb Hybrid still tows 3,500 lb."},
 ],
 "verdict": {
  "thesis": "On the 2020–2026 Highlander, buy floor liners matched to second-row seating and powertrain first, add crossbars second if the roof has rails, fit a trailer hitch chosen by XSE badge third, and buy the cargo box last, sized to the bars' 165 lb and spread.",
  "body": "The fourth-generation Highlander is easy to accessorize once five facts are written down: captain's "
          "chairs or a bench, gas or Hybrid, rails or a bare roof, XSE or not, and Highlander or Grand "
          "Highlander. Floor liners need the first two and cost the least, so they go first. A roof rack is "
          "second because clamp-on bars cost about $80–$140 and everything that rides on the roof depends on "
          "them.\n\n"
          "The trailer hitch sits third. It has the most work in it, and it gives heavy gear and bikes a place "
          "the 165 lb roof can't. The cargo box is last because it is the biggest spend and has to suit the "
          "bars already on the roof. Owners of a 2014–2019 Highlander or a Grand "
          "Highlander should treat this page as a list of questions, not part numbers.",
 },
 "sources": [
  ["Toyota Highlander: fourth generation XU70, GA-K platform, grades, 2023 engine change, Grand Highlander, fifth generation (Wikipedia)", "https://en.wikipedia.org/wiki/Toyota_Highlander"],
  ["2025 Toyota Highlander release: 5,000 lb turbo and 3,500 lb Hybrid towing, seating, grades (Toyota USA Newsroom)", "https://pressroom.toyota.com/celebrate-the-best-of-toyota-highlander-with-limited-25th-edition-hybrid/"],
  ["Toyota Tow Hitch Receiver PT228-48174 (Toyota Parts)", "https://autoparts.toyota.com/products/product/tow-hitch-receiver-pt22848174"],
  ["Toyota Roof Rack Cross Bars PT767-48200 (Toyota Parts)", "https://autoparts.toyota.com/products/product/roof-rack-cross-bars-xle-limited-platinum-pt76748200"],
  ["Roof Rack Cross Bars 2020–2025 Highlander/Hybrid, 165 lb rating (Toyota Customs, Canada)", "https://toyotacustoms.com/products/roof-rack-cross-bars"],
  ["2023 Toyota Highlander roof rack systems by roof type (etrailer)", "https://www.etrailer.com/roof-2023_Toyota_Highlander.htm"],
  ["Thule crossbar kit for 2020–2026 Highlander flush rails, 165 lb / 31 in spread (The Rack Shop)", "https://therackshop.com/2020-2025-toyota-highlander-w-flush-rails-thule-crossbar-complete-roof-rack/"],
  ["Highlander roof rack weight limits by generation (AHG Auto Service)", "https://www.ahgautoservice.com/what-is-the-weight-limit-for-the-roof-rack-on-a-toyota-highlander/"],
  ["2023 Highlander hitch comparison and install notes (etrailer)", "https://www.etrailer.com/hitch-2023_Toyota_Highlander.htm"],
  ["CURT 13460 Class 3 hitch, Highlander (CURT)", "https://www.curtmfg.com/part/13460"],
  ["B&W BW62PR Highlander hitch (etrailer)", "https://www.etrailer.com/Trailer-Hitch/B-and-W/BW62PR.html"],
  ["Reese 84439 Class IV hitch (Reese)", "https://www.reeseprod.com/product/84439_class-iii-trailer-hitch"],
  ["Tekonsha T-One 118827 harness (Tekonsha)", "https://www.tekonsha.com/product/118827_t-one-connector-assembly-with-upgraded-circuit-protected-modulite-hd-module"],
  ["Husky Liners: WeatherBeater vs X-act Contour, origin and warranty (Husky Liners)", "https://huskyliners.com/blog/husky-liners-weatherbeater-vs-xact-contour/"],
  ["Cargo box and rear carrier fuel economy impact (fueleconomy.gov)", "https://www.fueleconomy.gov/feg/driveHabits.jsp"],
 ],
}
