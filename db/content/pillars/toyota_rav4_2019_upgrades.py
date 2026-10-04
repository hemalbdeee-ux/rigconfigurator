"""Upgrades pillar: 2019–2025 Toyota RAV4 (5th gen, XA50; gas, Hybrid and Prime / Plug-in Hybrid).
Hub page: ranks the four published RAV4 category guides and links to them. No product picks or ASINs here
(the site pulls each guide's #1 pick). Every price band comes from the linked guides' picks[].price fields or the
price text in those guides (the Thule crossbar kit prices are the etrailer figures quoted in the roof rack guide);
vehicle facts from db/migrations/003_vehicles.sql (SUV, years 2019–2025, raised rails, roof load 165 lb, hitch
class 2, receiver 1.25 in, 3,500 lb maximum, attrs: raised rails on XLE and up, LE bare roof, 1,500 lb standard and
3,500 lb Adventure / TRD Off-Road, 2026 is a new generation), the four guides and their sources, and six pages
opened for this page on 2026-10-04: Wikipedia's XA50 page (TNGA-K platform, TRD Off-Road added for 2020, Woodland
Edition added for 2023 as a hybrid, Adventure and TRD Off-Road discontinued for 2025, Prime renamed Plug-in Hybrid
for 2025, sixth generation revealed 20–21 May 2025 for the 2026 model year), Toyota Vallejo's 2024 towing page
(1,500 / 3,500 / 1,750 / 2,500 lb; Tow Prep standard on Adventure and TRD Off-Road with a built-in receiver and
wiring harness; other versions need an optional receiver), Toyota's parts page for hitch PK960-42K10 (2 in receiver
tube, hitch cover, the two grade exclusions, kick sensor note; no model years and no price), etrailer's 2021 RAV4
roof page (three roof configurations: raised rails, flush rails, no rails; sunroof note), RAV4Resource's roof limit
page (176.4 lb / 80 kg for 2019–2024, found in the owner's manual under Cargo and Luggage) and Toyota's 2024 RAV4
release (gas and hybrid grade lists; Woodland Edition has high profile black roof rails and standard cross bars).
Toyota's support article on Adventure towing did not load and is not cited.
Not verified, and worded as such in the text: which grades and years have standard raised rails, flush rails or a
bare roof (the LE bare roof is from the vehicle data; etrailer names no trims; Toyota's release mentions only the
Woodland's rails); the Woodland's rail profile and whether its factory cross bars are on every year; the roof limit
from a Toyota document (165 lb in the vehicle data, 176.4 lb on RAV4Resource, nothing for 2025, no static figure);
the size and class of the factory Tow Prep receiver; tow ratings for years other than 2024 and for the 2025 Plug-in
Hybrid; the vehicle's tongue weight limit; what exactly differs in the hybrid floor; B&W fit on 2019–2022 Hybrids
and other makers' Hybrid and Prime years; ratings of the Rigid Hitch and the CURT bundle; crossbar weights; the
Vista XL's weight; crossbar spread for the Force 3 L and SkyBox NX Skinny; whether RAV4 rails allow a 32 in spread;
and any 2026 fit. No RAV4 guide exists for running boards or lighting; neither is ranked.
"""

KIND = "upgrades"
KEY = ("toyota", "rav4", "2019-present")
CATEGORIES = ["floor-mats", "roof-racks", "hitches", "cargo-boxes"]

TITLE = "2019–2025 Toyota RAV4 Upgrades, Ranked: 4 Mods in Order, With Powertrain and Roof Rail Fit Traps"
META = ("Four 2019–2025 RAV4 upgrades in buying order: floor liners, roof rack, trailer hitch and cargo box, with "
        "gas, Hybrid and Prime fit, rail types and tow limits.")

FAQ = [
 ("What should I upgrade first on a 2019–2025 Toyota RAV4?",
  "Floor liners, then crossbars. Liners cost the least, about $70–$260 in the floor liner guide, and the one fit "
  "question is the liftgate badge: gas, Hybrid or Prime. A roof rack is second because clamp-on crossbars for "
  "standard raised rails run about $60–$130 and the cargo box depends on them. A trailer hitch is third at about "
  "$150–$220, and the cargo box is last because it costs the most. On an LE with a bare roof, move the hitch up to "
  "second."),
 ("Do the RAV4 Hybrid and Prime need different parts than the gas RAV4?",
  "For the floor and the hitch, sometimes. For the roof, no. Husky's 95501 set and 13231 front pair are listed as "
  "not fitting hybrid models, and AOMSAZTO's set is gas only, while the generic 3D set names gas, Hybrid and Prime. "
  "Hitch makers list powertrains by year: B&W's RH670118BW covers the 2023–2025 Hybrid and the Prime through 2024. "
  "Crossbars and boxes go by rail type, because the Hybrid and Prime share the roof with the gas RAV4 of the same "
  "grade."),
 ("How much can my RAV4 tow, and does an aftermarket trailer hitch raise it?",
  "A hitch never raises it. The hitch guide uses Toyota dealer figures, and the Toyota Vallejo page for the 2024 "
  "model matches them: 1,500 lb for the gas LE, XLE, XLE Premium and Limited, 3,500 lb for the Adventure and TRD "
  "Off-Road, 1,750 lb for every Hybrid and 2,500 lb for the Prime. We could not confirm other model years or the "
  "2025 Plug-in Hybrid, so read the owner's manual."),
 ("Does my RAV4 Adventure or TRD Off-Road already have a hitch receiver?",
  "Probably. Both trims had Toyota's Tow Prep Package as standard, and the Toyota Vallejo towing page describes them "
  "as having built-in trailer hitch receivers and wiring harnesses. Look under the rear bumper. "
  "If a receiver is there, you need only a ball mount or a rack that matches the opening. We could not "
  "confirm from Toyota whether that receiver is 1.25 in or 2 in, so measure it. Wikipedia says both trims were "
  "discontinued for 2025."),
 ("Should I get a 1.25 in or a 2 in receiver for a bike rack on a RAV4?",
  "Get 2 in unless you already own 1.25 in gear. The hitch guide notes that most hitch bike racks and cargo carriers "
  "are built for 2 in, and that a 1.25 in receiver rules out many heavier platform racks. B&W's 2 in hitch is about "
  "$212 with 675 lb of tongue weight. Reese's 1.25 in 06192 is about $150–$220 with 350 lb and isn't rated for "
  "weight distribution. Toyota's parts page lists its own PK960-42K10 hitch with a 2 in receiver tube."),
 ("How much weight can a RAV4 roof carry with crossbars and a cargo box?",
  "The vehicle data on this site lists 165 lb for the 2019–2025 RAV4. RAV4Resource gives 176.4 lb (80 kg) for "
  "2019–2024 models and points to the Cargo and Luggage section of the owner's manual. Plan around the lower figure. "
  "The limit covers crossbars, box and gear together. A 47 lb SkyBox 16 leaves 118 lb "
  "before the bars are counted. A 260 lb rating on a crossbar listing describes the bar, not the roof."),
 ("My RAV4 LE has no roof rails. What are my options?",
  "The vehicle data lists the LE with a bare roof, so look at yours first. With no rails, none of the clamp-on "
  "crossbars in the roof rack guide will mount. The guide's route is a door-jamb clamp system: etrailer prices "
  "Thule's SquareBar Evo for the RAV4's naked roof at about $605 and the WingBar Evo at about $705. A trailer hitch "
  "at about $150–$220 costs far less, so on an LE it makes sense to fit the hitch first."),
 ("Is a roof box or a hitch cargo carrier better on a RAV4?",
  "The cargo box guide's rule is soft bags and skis on the roof, coolers and heavy bins on a "
  "hitch carrier. A roof box locks, keeps gear dry and leaves the rear clear, but it uses the roof limit and adds "
  "drag, which on a Prime means fewer electric miles. A hitch carrier holds heavier items low, but it blocks the "
  "liftgate unless it tilts, and its weight counts as tongue weight. Check that figure in your owner's manual."),
 ("Will 2019–2025 RAV4 parts fit a 2026 RAV4, and do 2013–2018 parts fit mine?",
  "Treat both as no. The 2019 RAV4 moved to the TNGA-K platform, so 2013–2018 liners don't fit, and hitch makers use "
  "separate part numbers: CURT's 13406 is listed for 2013–2018 and Draw-Tite's 75235 for 2006–2018. The 2026 RAV4 "
  "is a new sixth generation, and CURT sells a separate hitch, 13652, for 2026–2027. The one part that carries over "
  "is the cargo box, because it clamps to crossbars."),
 ("How much does it cost to add all four upgrades to a RAV4?",
  "From the prices on the four guides' picks, a budget build runs about $730–$880: budget TPE liners, VEVOR "
  "crossbars, Reese's 1.25 in hitch and SportRack's Vista XL. A mid build runs about $1,001–$1,191 with a "
  "floor-and-cargo liner set, Autekcomma bars, B&W's hitch and a Yakima 16 cu ft box. A premium build with "
  "WeatherTech liners, Thule bars, the B&W hitch with CURT's harness and Thule's Force 3 L runs about $1,787–$2,012. "
  "The totals assume standard raised rails and are approximate."),
]

ARTICLE = {
 "dek": "Four upgrades for the fifth-generation RAV4, in buying order. Fit on this compact SUV turns on a few "
        "facts: gas, Hybrid or Prime, which roof is overhead, which tow rating the version carries, and whether "
        "the listing covers the right years. Searches also return parts for the 2013–2018 and 2026 RAV4, "
        "which don't fit.",
 "author": "jake-morrison",
 "reviewed": "2026-10-04",
 "method": "We did not install any of these parts ourselves. The order comes from the four fit-checked 2019–2025 "
           "RAV4 guides on this site, weighing how many RAV4s each upgrade suits, what it costs, what it depends on "
           "and how much can go wrong with fit (powertrain, rail type, tow rating, model year). Price bands are the "
           "prices listed on those guides' picks, checked at maker and retailer stores in September 2026, and are "
           "approximate. Vehicle facts come from this site's vehicle data, the guides' sources, Wikipedia's XA50 "
           "page and Toyota's own pages. Where we couldn't confirm a factory detail, the text says so.",
 "takeaways": [
  "**Read the liftgate badge first.** Gas, Hybrid and Prime don't always share floor liners: Husky's and AOMSAZTO's sets are for gas models only.",
  "**Look at the roof before the listing.** Standard raised rails, Adventure and TRD Off-Road rails, flush rails and a bare roof each take different crossbars.",
  "**The tow rating belongs to the version, not the hitch.** Dealer figures give 1,500 lb gas, 1,750 lb Hybrid, 2,500 lb Prime and 3,500 lb Adventure and TRD Off-Road.",
  "**The roof carries about 165 lb, bars and box included.** One reference lists 176.4 lb for 2019–2024, so read the owner's manual.",
  "**Buy 2019–2025 parts only.** 2013–2018 liners and hitches don't fit, and the 2026 RAV4 is a new generation.",
 ],
 "priority": [
  {"category": "floor-mats",
   "h": "1. Floor liners first: the lowest price, and one look at the badge",
   "why": "Floor liners lead on the RAV4 because every version can use them, they cost the least and the fit check "
          "is one look at the liftgate badge. The floor liner guide says the Hybrid and Prime carry a battery under "
          "the rear seat, and some makers cut the rear and cargo pieces differently for them. Husky goes further: "
          "its WeatherBeater 95501 set and 13231 front pair are both listed as not fitting hybrid models, and "
          "AOMSAZTO's set is gas only. The generic 3D set names gas, Hybrid and Prime, Powerty says all models, and "
          "WeatherTech asks you to confirm Hybrid or Prime. Prices run about $70–$110 for AOMSAZTO, about $80–$120 "
          "for Powerty, about $90–$130 for the generic 3D set, about $100–$140 for a floor-and-cargo set that lists "
          "the hybrid, about $130–$180 for Husky's 95501 and about $200–$260 for WeatherTech's FloorLiners. "
          "WeatherTech says its liners are laser-measured with a lifetime limited warranty. The trade-off is "
          "price: WeatherTech costs about twice as much as the budget sets, which publish no warranty terms the "
          "guide could check.",
   "skip_if": "You already have raised-edge liners that hook onto the driver-side retention posts."},
  {"category": "roof-racks",
   "h": "2. Roof rack second: cheap on standard rails, and the base for everything overhead",
   "why": "A roof rack ranks second because on most RAV4s it is the cheapest way to add carrying room, and the "
          "cargo box in slot four can't go on without it. Crossbars for the standard raised rails run about "
          "$60–$130 in the roof rack guide and clamp on without drilling. Fit goes by rail, not by year or "
          "powertrain. The guide and the vehicle data put standard raised rails on the XLE and up, a different "
          "rail profile on the Adventure and TRD Off-Road, and a bare roof on the LE. Autekcomma's lockable set, "
          "about $90–$130 with a 260 lb bar rating, names every trim it excludes. FLYCLE's is about $80–$120, "
          "VEVOR's 160 lb set about $60–$90 and titled 2020–2023 only, and ROKIOTOEX's set for the Adventure and "
          "TRD rails about $100–$150. The trade-off is the roof itself: the vehicle data lists 165 lb, bars "
          "included, and no bar rating raises that. On a bare-roof LE the cheapest route in the guide is a Thule "
          "clamp kit at about $605, so LE owners should move the trailer hitch up to second.",
   "skip_if": "Your Woodland Edition already has the cross bars Toyota's 2024 release lists as standard, or nothing you carry has to go on the roof."},
  {"category": "hitches",
   "h": "3. Trailer hitch third: the place for heavy loads, capped by the version you own",
   "why": "A trailer hitch ranks third. It costs more than crossbars and takes more work, since cargo-area trim "
          "panels come off and the hands-free liftgate sensor may need adjusting. In return it carries what the "
          "roof can't: the published tongue weight ratings in the hitch guide run from 350 lb to 675 lb, against "
          "165 lb for the roof. The guide's first pick is B&W's RH670118BW, a Class III hitch with a 2 in receiver rated "
          "4,500 lb and 675 lb, at about $212 from etrailer. Reese's 06192 is the 1.25 in Class II option at about "
          "$150–$220, rated 3,500 lb and 350 lb. CURT's 56434 plug-in harness adds about $50–$80. Two facts decide "
          "the purchase: listing coverage by powertrain and year, and the version's own tow rating. Dealer figures "
          "give 1,500 lb for the gas LE through Limited, 1,750 lb for the Hybrid, 2,500 lb for the Prime and 3,500 "
          "lb for the Adventure and TRD Off-Road, which had the Tow Prep Package as standard. No hitch raises "
          "those numbers.",
   "skip_if": "A receiver is already under the bumper, as on an Adventure or TRD Off-Road with Tow Prep, or you never carry bikes or pull a trailer."},
  {"category": "cargo-boxes",
   "h": "4. Cargo box last: the largest single cost, and it needs the bars first",
   "why": "The cargo box comes last because it is the largest single purchase, about $450–$880 in the cargo box "
          "guide, and it depends on slot two. A box clamps to crossbars, so the box itself is "
          "universal. Three numbers decide which one suits this SUV: length, because the liftgate swings up toward "
          "the back of a short roof; box weight, because bars, box and gear share the roof limit; and crossbar "
          "spread. SportRack's Vista XL is about $450 for 18 cu ft in 63 in, with a rear-opening lid and fixed "
          "mounting positions. Yakima's SkyBox 16 Carbonite was about $599 on sale, at 81 in and 47 lb. The "
          "DeepSpace 10 is about $649, 60 in and 30.2 lb, but needs a 32–46 in spread. The GrandTour 16 is about "
          "$709, 79 in and 51.5 lb. Thule's Force 3 L is about $880, 76.8 in and 43 lb. The trade-offs are roof "
          "load and drag: the guide puts the room left for gear at roughly 100–120 lb, and says drag cuts into "
          "the Prime's EPA-rated 42-mile electric range.",
   "skip_if": "Your heavy items are coolers and bins, which the guide sends to a hitch carrier."},
 ],
 "tier_table": {
  "caption": "Approximate price bands from the picks in the 2019–2025 RAV4 guides (September 2026; Amazon prices move daily). Each column assumes standard raised rails; the box mounts on that column's crossbars",
  "head": ["Upgrade", "Budget", "Mid", "Premium"],
  "rows": [
   ["Floor liners", "About $70–$120 (AOMSAZTO, gas only, or Powerty, all models)", "About $100–$140 (floor-and-cargo set that lists the hybrid)", "About $200–$260 (WeatherTech FloorLiners, front and second row)"],
   ["Roof rack", "About $60–$90 (VEVOR lockable bars, 160 lb, titled 2020–2023)", "About $90–$130 (Autekcomma lockable bars, 260 lb)", "About $445–$580 (Thule SquareBar or WingBar Evo for raised rails, etrailer prices)"],
   ["Trailer hitch", "About $150–$220 (Reese 06192, 1.25 in, 3,500 lb / 350 lb)", "About $212 (B&W RH670118BW, 2 in, 4,500 lb / 675 lb)", "About $262–$292 (the B&W at about $212 plus CURT's 56434 harness at about $50–$80)"],
   ["Cargo box", "About $450 (SportRack Vista XL, 18 cu ft, 63 in)", "About $599 (Yakima SkyBox 16 Carbonite on sale) to $709 (GrandTour 16)", "About $880 (Thule Force 3 L, 16 cu ft, 76.8 in)"],
   ["Total", "About $730–$880", "About $1,001–$1,191", "About $1,787–$2,012"],
  ],
 },
 "sections": [
  {"h": "Gas, Hybrid or Prime: what the badge changes and what it leaves alone",
   "body": "The badge on the liftgate changes three things on this list and leaves one alone.\n\n"
           "**Floor and cargo liners.** The floor liner guide says the Hybrid and Prime carry a battery under the "
           "rear seat, and that some makers cut the rear and cargo liners differently for them. Husky's exclusions "
           "reach the front row too. Its 25501 cargo liner, about $90–$140, names no powertrain in its title, so confirm it with the "
           "maker.\n\n"
           "**The hitch.** The body is shared, but the listings name powertrains year by year. B&W lists its "
           "RH670118BW for the 2019–2025 RAV4, the 2023–2025 Hybrid, the Prime through 2024 and the 2025 plug-in "
           "hybrid. CURT's 56434 harness covers the 2019–2025 RAV4 and Prime in all styles. If your powertrain and "
           "year aren't named, ask the seller.\n\n"
           "**The tow rating.** The figures below are Toyota dealer figures for the 2024 model year.\n\n"
           "**The roof.** The Hybrid and Prime share the roof with the gas RAV4 of the same grade, so crossbars "
           "and a cargo box go by rail type alone.",
   "table": {"caption": "2019–2025 RAV4 by version: liners, hitch listings and tow rating",
             "head": ["Version", "Floor and cargo liners", "Hitch listings", "Max trailer (dealer figures)"],
             "rows": [
              ["Gas LE, XLE, XLE Premium, Limited", "Every set in the guide, including the gas-only Husky 95501 and AOMSAZTO", "Most name the 2019–2025 RAV4; Rigid Hitch's R3-0523 is titled 2019–2024", "1,500 lb"],
              ["Gas Adventure, TRD Off-Road (through 2024)", "Same gas sets; trim doesn't change the floor", "Tow Prep standard, with a receiver and harness per a Toyota dealer", "3,500 lb"],
              ["Hybrid, every grade, Woodland Edition included", "Generic 3D set, Powerty or the floor-and-cargo set; not Husky 95501 or AOMSAZTO", "B&W lists the 2023–2025 Hybrid; confirm 2019–2022", "1,750 lb"],
              ["Prime (2021–2024)", "The generic 3D set names the Prime; confirm any other", "B&W through 2024, Draw-Tite 2021–2023, Reese 2024 only, CURT's bundle 2021–2024", "2,500 lb"],
              ["2025 Plug-in Hybrid (the renamed Prime)", "Listings may use either name; confirm", "B&W lists the 2025 plug-in hybrid", "Check the owner's manual"],
             ]}},
  {"h": "Which roof is overhead: rails decide the crossbars, and crossbars decide the box",
   "body": "The RAV4's roof changes by trim. The vehicle data on this site lists raised rails as standard on the "
           "XLE and up and a bare roof on the LE. The roof rack guide adds a different rail profile on the Adventure and TRD "
           "Off-Road. The etrailer fit guide for the 2021 RAV4 shows three configurations: raised rails, flush "
           "mounted rails and no rails. It doesn't say which trims have which, and we could not confirm a "
           "trim-by-trim list from Toyota. Go by what you can see. A gap under the rail means raised rails, no "
           "gap means flush rails, and no rail means a clamp kit.\n\n"
           "The Woodland Edition is its own case. Autekcomma's standard-rail listing excludes it, and ROKIOTOEX's "
           "Adventure and TRD title doesn't name it. Toyota's 2024 RAV4 release says the Woodland Edition has "
           "high profile black roof rails and standard cross bars, so a Woodland may need no crossbars at all.\n\n"
           "The box follows the bars. Before paying for a box, check that the bar listing names your rail, that "
           "the two bars can be set as far apart as the box needs, and that the rear bar clears the liftgate. "
           "etrailer also advises against opening a sunroof while a rack is installed.",
   "table": {"caption": "2019–2025 RAV4 roofs and the crossbars each one takes",
             "head": ["Roof", "Where it is found", "Crossbars", "Price in the guide"],
             "rows": [
              ["Standard raised rails", "XLE, XLE Premium, XSE and Limited in gas, Hybrid and Prime form, per the roof rack guide", "Autekcomma, FLYCLE, VEVOR or the generic aluminum set; Thule SquareBar or WingBar Evo", "About $60–$130; Thule about $445–$580 at etrailer"],
              ["Adventure-style raised rails", "Adventure and TRD Off-Road, both dropped for 2025", "ROKIOTOEX, titled for the 2019–2024 Adventure and TRD factory rails", "About $100–$150"],
              ["Woodland Edition rails", "Hybrid grade added for 2023", "Toyota's 2024 release lists standard cross bars; Autekcomma's set excludes this trim", "Check the roof before buying"],
              ["Flush rails", "Listed by etrailer for the 2021 RAV4; trims not stated", "A flush-rail kit from a fit guide; none of the clamp-on sets", "Priced in etrailer's fit guide"],
              ["Bare roof", "LE, per the vehicle data", "Door-jamb clamp kit: Thule SquareBar Evo or WingBar Evo for a naked roof", "About $605–$705 at etrailer"],
             ]}},
  {"h": "Roof or hitch: where the weight should go on a compact SUV",
   "body": "The RAV4 has two places to carry what won't fit inside, and their limits differ.\n\n"
           "**The roof.** The vehicle data on this site lists a roof load of **165 lb** for this generation. "
           "RAV4Resource lists 176.4 lb (80 kg) for 2019–2024 models and says the figure is in the owner's manual "
           "under Cargo and Luggage. We did not read a Toyota manual for this page, so plan on the lower number. "
           "Starting from 165 lb, the makers' box weights leave this much before the "
           "crossbars' own weight comes off:\n\n"
           "- **Yakima DeepSpace 10, 30.2 lb:** 134.8 lb, but Yakima limits the box to 100 lb of cargo.\n"
           "- **Thule Force 3 L and Yakima SkyBox NX Skinny, 43 lb each:** 122 lb.\n"
           "- **Yakima SkyBox 16 Carbonite, 47 lb:** 118 lb.\n"
           "- **Yakima GrandTour 16, 51.5 lb:** 113.5 lb.\n"
           "- **SportRack Vista XL:** weight not published.\n\n"
           "The crossbar titles in the roof rack guide give no bar weights, so read the listing. The cargo box "
           "guide's working figure is roughly 100–120 lb for gear, which suits duffels and skis, not a cooler "
           "full of ice.\n\n"
           "**The hitch.** Tongue weight ratings in the hitch guide run from 350 lb on Reese's 06192 to 675 lb on "
           "B&W's RH670118BW. A bike rack or a cargo carrier is tongue weight, not trailer weight, so even a "
           "1,500 lb RAV4 can carry one. The limits are the rack's own rating, the tongue weight figure in your "
           "owner's manual, which we could not confirm and don't print, and liftgate clearance.\n\n"
           "**Receiver size.** A 2 in receiver takes more racks and carriers without an adapter. Toyota's "
           "parts page lists its PK960-42K10 accessory hitch with a 2 in receiver tube, and Reese's 06192 is a "
           "1.25 in part. We could not confirm the size of the Tow Prep receiver on an Adventure or TRD Off-Road. "
           "If your RAV4 already has a receiver, measure the opening before buying a rack."},
  {"h": "Model years: the 2019 start, the 2025 changes and the 2026 cutoff",
   "body": "This generation runs from 2019 through 2025, and parts for the RAV4s on either side show up in "
           "the same searches.\n\n"
           "- **2019.** The RAV4 moved to the TNGA-K platform. 2013–2018 liners don't fit, and hitch makers "
           "changed part numbers: CURT's 13406 is listed for 2013–2018 and Draw-Tite's 75235 for 2006–2018.\n"
           "- **2020 to 2023.** Wikipedia lists the TRD Off-Road as added for 2020 and the hybrid Woodland Edition "
           "for 2023. The guides date the Prime from the 2021 model year.\n"
           "- **2025.** Wikipedia says the Adventure and TRD Off-Road were discontinued and the Prime was renamed "
           "Plug-in Hybrid. The hitch guide reads a 2025 gas RAV4 as a 1,500 lb vehicle.\n"
           "- **2026.** A new sixth generation, revealed on 20–21 May 2025 per Wikipedia. CURT sells a separate "
           "hitch, 13652, for 2026–2027.\n\n"
           "Inside the generation, the liner and crossbar listings in the guides mostly run 2019–2025 as one "
           "part. Some titles stop short: VEVOR's crossbars are titled 2020–2023, and Rigid Hitch's R3-0523, "
           "about $259, and ROKIOTOEX's crossbars are titled 2019–2024.\n\n"
           "The opposite problem is a title stretched to 2019–2026: the roof rack guide warns that some Amazon "
           "listings extend their year range as models change. The cargo box is the exception, because it "
           "clamps to crossbars."},
  {"h": "What isn't ranked, and the order to fit the four that are",
   "body": "This page ranks the four categories that have a fit-checked RAV4 guide on this site. Running boards "
           "and lighting have none for this vehicle, so they aren't ranked.\n\n"
           "Fit the four in this order.\n\n"
           "1. **Floor liners.** No tools. Remove the factory mats, hook the driver liner onto Toyota's retention "
           "posts and press both pedals to the floor.\n"
           "2. **Crossbars.** Space the bars to the accessory's range, tighten the clamps evenly and open the "
           "liftgate fully to check the rear bar.\n"
           "3. **Trailer hitch.** B&W's hitch bolts to factory attachment points in three pieces with no drilling. "
           "etrailer quotes 30–45 minutes for an experienced installer and 1–2 hours for a first-timer without a "
           "lift. CURT rates its 56434 plug-in harness as professional difficulty, mostly for the wire run to "
           "the battery.\n"
           "4. **Cargo box.** Lift it on with a helper, slide it as far forward as the windshield allows and open "
           "the liftgate slowly the first time.\n\n"
           "The hitch also sits near the kick sensor. etrailer's notes say the hands-free liftgate may need "
           "adjustment with several RAV4 hitches, and Toyota's parts page says fitting its own receiver may "
           "require disabling or removing the sensor. Toyota also says that hitch is not available on Limited "
           "grades with the Advanced Technology Package or on the Prime XSE with the Premium package."},
 ],
 "avoid": [
  {"h": "A gas-only liner set on a Hybrid or Prime", "body": "Husky's 95501 and 13231 and AOMSAZTO's set exclude the hybrid. Buy a set that names your powertrain."},
  {"h": "Standard-rail crossbars on an Adventure, TRD Off-Road or LE", "body": "The Adventure and TRD rails have a different profile, and the LE's bare roof has nothing to clamp to. Read the title's exclusions against your badge and your roof."},
  {"h": "Loading or towing to the part's rating", "body": "A 260 lb crossbar doesn't change a 165 lb roof, and a 4,500 lb hitch doesn't change a 1,500 lb RAV4. The lower number wins."},
  {"h": "Parts from the generation before or after", "body": "2013–2018 liners and hitches don't fit, and the 2026 RAV4 has its own parts, such as CURT's 13652 hitch. Only the cargo box moves between generations."},
 ],
 "verdict": {
  "thesis": "On the 2019–2025 RAV4, buy floor liners by powertrain first, crossbars by rail type second, a trailer hitch sized to your version's tow rating third, and a cargo box last, once the bars and the roof load math are settled.",
  "body": "The fifth-generation RAV4 is easy to accessorize once five facts are written down: gas, Hybrid or "
          "Prime, the roof overhead, the version's tow rating, whether a receiver is already fitted, and the model "
          "year. Floor liners need only the first and cost the least, so they go first. A roof rack needs the "
          "second. On standard raised rails it costs about $60–$130, which puts it ahead of the trailer hitch. On "
          "a bare-roof LE it costs about $605 or more, so LE owners should swap the two.\n\n"
          "The hitch is third because it takes more work and brings the kick sensor into play, but it is where "
          "heavy loads belong on a roof that carries about 165 lb. The cargo box is last because it costs the most "
          "and depends on the bars, the roof limit and the liftgate.",
 },
 "sources": [
  ["Toyota RAV4 (XA50): platform, trims by year, Prime renaming, 2026 successor (Wikipedia)", "https://en.wikipedia.org/wiki/Toyota_RAV4_(XA50)"],
  ["2024 Toyota RAV4 towing capacity by trim (Toyota Vallejo)", "https://www.toyotavallejo.com/blogs/5095/2024-toyota-rav4-towing-capacity"],
  ["Toyota hitch receiver PK960-42K10: receiver tube, exclusions, kick sensor (Toyota Auto Parts)", "https://autoparts.toyota.com/products/product/hitch-receiver-pk96042k10"],
  ["2024 Toyota RAV4: Go Wild in Style, grades and Woodland Edition roof rails and cross bars (Toyota Newsroom)", "https://pressroom.toyota.com/?generate_pdf=87387"],
  ["2021 RAV4 roof rack systems by roof type (etrailer)", "https://www.etrailer.com/roof-2021_Toyota_RAV4.htm"],
  ["RAV4 roof rack weight limit by model year (RAV4Resource)", "https://rav4resource.com/toyota-rav4-roof-rack-weight-limit/"],
  ["B&W BW47BR RAV4 hitch (etrailer)", "https://www.etrailer.com/Trailer-Hitch/B-and-W/BW47BR.html"],
  ["Reese 06192 Class II hitch (Reese)", "https://www.reeseprod.com/product/06192_class-ii-trailer-hitch"],
  ["CURT 56434 custom wiring harness (CURT)", "https://www.curtmfg.com/part/56434"],
  ["2022 RAV4 hitch comparison and install notes (etrailer)", "https://www.etrailer.com/hitch-2022_Toyota_RAV4.htm"],
  ["WeatherTech FloorLiner HP buying guide (WeatherTech)", "https://www.weathertech.com/blog/product-spotlight/new-weathertech-floorliner-hp.html"],
  ["Yakima GrandTour 16 (Yakima)", "https://yakima.com/products/grandtour-16"],
  ["Yakima DeepSpace 10 (Yakima)", "https://yakima.com/collections/roof-boxes/products/deepspace-10"],
  ["Thule Force 3 L (Thule)", "https://www.thule.com/en-us/cargo-carrier/car-top-carrier/thule-force-3-l-_-645750"],
  ["SportRack Vista XL (SportRack)", "https://www.sportrack.com/product/vista-xl-cargo-box/"],
 ],
}
