"""Upgrades pillar: 2019–2024 Subaru Forester (5th gen, SK; not the redesigned 2025 Forester).
Hub page: ranks the four published Forester category guides and links to them. No product picks or ASINs here
(the site pulls each guide's #1 pick). Every price band comes from the linked guides' picks[].price fields or the
price text in those guides (the Thule WingBar Evo figure is the etrailer price quoted in the roof rack guide);
vehicle facts from db/migrations/003_vehicles.sql (SUV, years 2019–2024, raised rails, roof load 176 lb, 1,500 lb,
3,000 lb Wilderness, Wilderness 2022+, 2025 is a new generation), the four guides and their sources, and seven pages
opened for this page on 2026-10-04: Subaru's 2019 Forester trim comparison sheet (five trims; raised roof rails
optional on the base Forester and standard on Premium, Sport, Limited and Touring; no roof capacity printed as we
read it; 1,500 lb on every trim; 8.7 in; height 67.5 in without and 68.1 in with roof rails; panoramic moonroof on
every trim except the base), Subaru's 2022 and 2024 Forester trim comparison sheets (six trims; "Roof rails with
integrated tie-down points (176 lbs. maximum capacity)" optional on Base and standard on Premium, Sport, Limited
and Touring; Wilderness "Roof rails with integrated tie-down points and Anodized Copper-finish accents (220 lbs.
dynamic maximum capacity, 800 lbs. static maximum capacity)"; "Crossbar Set - Fixed" as a Base-only accessory;
1,500 lb, 3,000 lb Wilderness; 8.7 in and 9.2 in; All-Weather Floor Liners accessory not available on Wilderness),
Subaru's 2 September 2021 release on the refreshed 2022 Forester (new ladder-type roof rail design with integrated
tie-down points, 176 lb dynamic and 700 lb static, Wilderness 220 lb and 800 lb when parked, roof-top tent use,
1,500 / 3,000 lb, Trailer Stability Assist standard, option package adds alloy wheels and roof rails to the base
model), Wikipedia's Subaru Forester page (debut March 2018, Subaru Global Platform, 182 hp, 2022 facelift with a new
front end and slightly tweaked rear bumper, Wilderness 0.5 in lift, sixth generation revealed November 2023 and on
sale in the second quarter of 2024 as a 2025 model, new Wilderness for the 2026 model year), Subaru Parts Pros'
L101SSJ005 page (2 in receiver, 1,500 lb / 150 lb, Wilderness 3,000 lb / 300 lb, harness and hitch plug included,
ball mount and ball separate, fits 2022–2024 all trims and the 2025 Wilderness only) and Our Auto Expert's
Wilderness first look (176 / 220 lb dynamic, 800 lb static, attributed to Subaru; opened, not cited).
The stored roof_load_lb (176) matches Subaru's 2022 and 2024 sheets, so it is printed with Subaru's attribution.
The stored hitch_class ('2') and receiver_in (1.25) are not printed as vehicle facts: the guides show Subaru's
accessory hitch is 1-1/4 in for 2019–2021 and 2 in for 2022–2024, and no factory-fitted receiver was confirmed.
Wikipedia's Wilderness towing figure differs from Subaru's sheets and is not used.
Not verified, and worded as such in the text: Subaru's roof figures for model years other than 2022 and 2024 (the
2019 sheet prints none as we read it); a static figure for the standard rails from any source but the 2022 release;
whether the 2019–2021 rails differ in shape from the 2022–2024 rails; what differs physically on the Wilderness
rails; whether the Base trim's optional rails match the other trims' rails; the vehicle tongue weight limit for
2019–2021 (the L101SSJ001 dealer page prints 176 lb, the 2022–2024 hitch page 150 lb); whether any Forester ships
with a factory-fitted receiver; whether Subaru itself documents the 2025 Wilderness as the 2019–2024 body (Wikipedia
says only the Wilderness was offered for 2025; the dealer hitch page agrees); why Subaru's liner accessory is
not offered on the Wilderness; 2025–2026 fit of crossbar and hitch listings titled past 2024; the Wsays hitch's
ratings and Wilderness fit; crossbar weights; the SportRack Vista XL's weight; crossbar spread for the Thule boxes.
No Forester guide exists for running boards, lighting or bike racks; none are ranked.
Text fixes 2026-10-04: kept consistent with the four guides' text fixes: floor liner fit stated as one listing fit
for 2019–2024 (not one floor for every trim); 2019–2021 tongue weight shown as not confirmed (176 lb on the
L101SSJ001 dealer page, 150 lb on the 2022–2024 page); 2025 Wilderness attributed to Wikipedia and the dealer listing.
"""

KIND = "upgrades"
KEY = ("subaru", "forester", "2019-2024")
CATEGORIES = ["floor-mats", "roof-racks", "hitches", "cargo-boxes"]

TITLE = "2019–2024 Subaru Forester Upgrades, Ranked: 4 Mods in Order, With Roof Rail and Tongue Weight Traps"
META = ("Four 2019–2024 Forester upgrades in buying order: floor liners, roof rack, trailer hitch and cargo box, with "
        "Base and Wilderness rails, roof load and tow limits.")

FAQ = [
 ("What should I upgrade first on a 2019–2024 Subaru Forester?",
  "Floor liners, then crossbars. Liners cost the least, about $80–$170 in the floor liner guide, and the listings "
  "cover 2019–2024 as one fit. A roof rack is second: the Amazon crossbar sets for the raised rails run about "
  "$80–$170, and Subaru's sheets give the standard roof 176 lb against 150 lb of tongue weight at the hitch. A "
  "trailer hitch is third at about $120–$280 from the aftermarket, mainly for a bike rack. The cargo box is last "
  "because it costs the most and needs the bars first."),
 ("How much weight can a 2019–2024 Forester roof carry?",
  "Subaru's 2022 and 2024 trim comparison sheets print a 176 lb maximum capacity for the standard roof rails. The "
  "same sheets give the Wilderness rails 220 lb dynamic, meaning while driving, and 800 lb static, meaning parked. "
  "Subaru's release on the refreshed 2022 Forester adds a 700 lb static limit for the standard rails. The 2019 "
  "sheet we read lists the rails without a figure, so 2019–2021 owners should check the owner's manual. Crossbars, "
  "box and cargo all count."),
 ("Does every 2019–2024 Forester have roof rails?",
  "No. Subaru's 2019, 2022 and 2024 trim comparison sheets list raised roof rails as standard on Premium, Sport, "
  "Limited and Touring and as optional on the Base trim. So a Base can have a bare roof, and etrailer's 2022 fit "
  "guide lists a Forester configuration with no rails or crossbars. Without rails, none of the clamp-on crossbars "
  "in the roof rack guide will mount, and the guide's route is a door-jamb clamp system from Thule or Yakima."),
 ("Does the Forester Wilderness need different parts?",
  "For the roof, yes. The Wilderness was sold with this body for 2022–2024, and for 2025 per Wikipedia, and the crossbar listings in the roof "
  "rack guide say \"except Wilderness\" or \"not Wilderness\". The guide found no Amazon set titled for it and "
  "points to a Thule or Yakima system entered in the fit guide as Wilderness. Subaru rates its rails at 220 lb "
  "dynamic and 800 lb static and the trim at 3,000 lb of towing. Aftermarket floor liners titled 2019–2024 carry "
  "no trim exclusion, but Subaru's sheets don't offer its own liners on this trim, so confirm the fit."),
 ("How much can a 2019–2024 Forester tow, and does an aftermarket trailer hitch raise it?",
  "A hitch never raises it. Subaru's 2019 trim comparison sheet lists 1,500 lb for every trim, and the 2022 and "
  "2024 sheets list 1,500 lb for every trim except the Wilderness, which is rated at 3,000 lb. A Subaru dealer "
  "listing for the 2022–2024 factory hitch gives tongue weights of 150 lb and 300 lb. Every aftermarket hitch with "
  "published ratings in the hitch guide is rated at 3,500 lb, so the vehicle is the limit. We read three model years only, "
  "so use your owner's manual."),
 ("Should I get a 1.25 in or a 2 in receiver on a Forester?",
  "Get 2 in if bikes are the reason for the hitch. The hitch guide notes that many larger platform bike racks are "
  "sold only in 2 in. Draw-Tite's 76271 is about $200–$280 and bolts on without drilling. A 1.25 in hitch such as "
  "Draw-Tite's 36671, about $180–$250, weighs 27.5 lb against 37 lb and is enough for a small trailer or a light "
  "rack."),
 ("Can a Forester carry two e-bikes on a hitch rack?",
  "Add it up first. A hitch bike rack is all tongue weight, and a Subaru dealer listing gives 150 lb for "
  "non-Wilderness Foresters and 300 lb for the Wilderness. The rack's own weight counts along with both bikes, and "
  "the hitch guide warns that two heavy e-bikes on a large platform rack can reach or pass 150 lb. The hitch's "
  "rating doesn't help: Draw-Tite's 76271 is rated at 525 lb, but the Forester's figure still applies."),
 ("Can I put a rooftop tent on a 2019–2024 Forester?",
  "Subaru's release on the refreshed 2022 Forester gives the standard roof rails a 176 lb dynamic capacity and a "
  "700 lb static limit and says that allows safe use of a roof-top tent. The Wilderness rails are rated at 220 lb "
  "and 800 lb. Subaru's catalog says its SOA367010 aero crossbars do not support rooftop tents, so use a rated "
  "aftermarket system. We could not confirm the static figure for 2019–2021 cars, so check the owner's manual."),
 ("Will 2019–2024 Forester parts fit a 2025 Forester, and do 2014–2018 parts fit mine?",
  "Treat floor liners and crossbars as no. The 2025 Forester is a new generation, except the Wilderness per Wikipedia, and Husky sells a separate liner "
  "set, 95381, for 2025–2026. Hitches are the grey area: Draw-Tite, CURT and Reese list their Forester hitches for "
  "2019–2026, so confirm with the maker's fit checker. Going back, 2014–2018 liners don't fit, but some clamp-on "
  "crossbars are titled 2014–2024 because they grip raised rails."),
 ("How much does it cost to add all four upgrades to a Forester?",
  "From the prices on the four guides' picks, a budget build runs about $730–$890: Subaru's or IKABEVEM's liners, "
  "EZREXPM or Snailfly crossbars, the Wsays hitch and SportRack's Vista XL. A mid build runs about $1,109–$1,269 "
  "with LASFIT or 3W liners, Tuyoung's lockable bars, Draw-Tite's 76271 and Yakima's GrandTour 16. A premium build "
  "with Husky's liners, a Thule WingBar Evo system, Subaru's hitch kit and Thule's Force 3 L runs about "
  "$1,965–$2,070. The totals assume standard raised rails. Hitch wiring and a ball mount are extra."),
]

ARTICLE = {
 "dek": "Four upgrades for the fifth-generation Forester, in buying order. Fit on this compact SUV turns on a few "
        "facts: whether the roof has rails at all, whether they are the Wilderness rails, the 150 lb of tongue "
        "weight that limits a bike rack, and the years on the listing. Subaru's own sheets give the standard roof "
        "more than the hitch, which is why the roof rack ranks above the trailer hitch here.",
 "author": "jake-morrison",
 "reviewed": "2026-10-04",
 "method": "We did not install any of these parts ourselves. The order comes from the four fit-checked 2019–2024 "
           "Forester guides on this site, weighing how many Foresters each upgrade suits, what it costs and how much "
           "can go wrong with fit (roof rails, trim, receiver size, model year). Price bands are the prices listed "
           "on those guides' picks, checked at maker and retailer stores in September 2026, and are approximate. "
           "Vehicle facts come from this site's vehicle data, the guides' sources, Subaru's 2019, 2022 and 2024 "
           "trim comparison sheets, Subaru's 2022 Forester release, a Subaru dealer parts page and Wikipedia. "
           "Where we couldn't confirm a factory detail, the text says so.",
 "takeaways": [
  "**Look at the roof first.** Subaru lists raised rails as standard on Premium, Sport, Limited and Touring and optional on the Base; the 2022–2024 Wilderness has its own.",
  "**The roof figure is Subaru's, not the bar's.** Its 2022 and 2024 sheets print 176 lb for standard rails, and 220 lb dynamic and 800 lb static for the Wilderness.",
  "**The hitch is for bikes and a small trailer.** Subaru lists 1,500 lb, or 3,000 lb for the Wilderness, and a dealer listing gives 150 lb and 300 lb of tongue weight.",
  "**Choose 2 in for bike racks.** Many larger platform racks are sold only in 2 in.",
  "**Read the years on every listing.** The 2025 Forester is a new generation, except the Wilderness per Wikipedia, yet some titles run to 2025 or 2026.",
 ],
 "priority": [
  {"category": "floor-mats",
   "h": "1. Floor liners first: one fit for six model years, and the lowest price on the page",
   "why": "Floor liners lead on the Forester because they cost the least and their fit is the simplest of the "
          "four. The liner listings in the floor liner guide cover 2019–2024 as one fit, so the main "
          "check is the year range in the title. Husky sells a separate 95381 set for the 2025 Forester. Prices in "
          "the guide run about $80–$120 for Subaru's J501SSJ030 set of four, about $90–$130 for IKABEVEM's set "
          "with a cargo liner, about $100–$140 for LASFIT's or 3W's TPE sets and about $130–$170 for Husky's "
          "WeatherBeater 95891, which Husky says is made in the USA with a lifetime warranty against cracks and "
          "breaks. The trade-off is walls "
          "against price: Subaru's liners cost less but sit lower than Husky's. One Wilderness note: Subaru's 2022 "
          "and 2024 sheets don't offer its All-Weather Floor Liners accessory on that trim, so have a dealer check "
          "the part against your VIN.",
   "skip_if": "Raised-edge liners are already hooked onto the driver-side retention hooks and the cargo carpet stays clean."},
  {"category": "roof-racks",
   "h": "2. Roof rack second: low-cost clamp-on bars, on a roof Subaru rates above the hitch",
   "why": "A roof rack ranks second because clamp-on crossbars cost little, Subaru's sheets list rails but not "
          "crossbars as standard equipment, and the cargo box in slot four can't go on without them. The 2022 and "
          "2024 sheets print 176 lb for the standard rails, more than the 150 lb of tongue weight a non-Wilderness "
          "Forester allows at the hitch. Rail type decides fit: raised rails are standard on Premium, Sport, "
          "Limited and Touring and optional on the Base, and most listings exclude the 2022–2024 Wilderness. Prices "
          "in the roof rack guide run about $80–$120 for EZREXPM's bars, about $90–$130 for Snailfly's set or the "
          "lockable adjustable set, about $100–$140 for Tuyoung's lockable 300 lb bars, about $120–$170 for "
          "BRIGHTLINES' aero bars and about $260–$350 for Subaru's SOA367010 aero set, which Subaru's catalog "
          "excludes from the base model and the Wilderness. The trade-off is that a bar's rating is not the "
          "roof's: a 300 lb bar still sits on a 176 lb roof, and the bars count toward it.",
   "skip_if": "Nothing you carry has to go on the roof, or your Base has no rails, in which case move the trailer hitch up to second."},
  {"category": "hitches",
   "h": "3. Trailer hitch third: a bike rack mount first and a tow point second",
   "why": "A trailer hitch ranks third because on most Foresters it is an accessory mount more than a tow point. "
          "Subaru's sheets list 1,500 lb for every trim except the Wilderness, which is rated at 3,000 lb, and a "
          "Subaru dealer listing gives 150 lb and 300 lb of tongue weight. Every aftermarket hitch with published "
          "ratings in the hitch guide is rated at 3,500 lb, so the choice comes down to the receiver. A 2 in receiver takes "
          "the widest range of platform bike racks and cargo carriers; a 1.25 in receiver is lighter and suits a "
          "small trailer. Prices run about $120–$180 for the budget Wsays 2 in hitch, about $170–$250 for the "
          "1.25 in Reese 06191 and Draw-Tite 36671, about $200–$280 for the 2 in CURT 13409 and Draw-Tite 76271 "
          "and about $410–$475 for Subaru's own kits. The trade-off is the tongue limit: rack and bikes together "
          "must stay under 150 lb on a standard trim. Aftermarket hitches also need a plug-in wiring harness, "
          "bought separately.",
   "skip_if": "A receiver is already under the bumper, as on a used Forester with the dealer-fitted kit, or you never carry bikes or pull a trailer."},
  {"category": "cargo-boxes",
   "h": "4. Cargo box last: the costliest part here, after the bars and the roof math",
   "why": "The cargo box comes last because it is the largest single purchase, about $450–$880 in the cargo box "
          "guide, and it depends on slot two. A box clamps to crossbars, so the box "
          "itself is universal. Two numbers decide which one suits this SUV. Length comes first, because the "
          "liftgate swings up toward the back of a compact roof: the boxes run from 63 in for SportRack's Vista XL "
          "to 83 in for Yakima's CBX 16. Weight is second, because bars, box and gear share Subaru's 176 lb figure, "
          "or 220 lb on a Wilderness, and the boxes weigh 31 to 57 lb. Prices run about $450 for the Vista XL, about "
          "$699 for the CBX 16, about $700 for Thule's Pulse 2 M, about $709 for Yakima's GrandTour 16, about $865 "
          "for the INNO Wedge 660 and about $880 for Thule's Force 3 L. The trade-off is drag: fueleconomy.gov "
          "puts the highway cost of a large rooftop box at 6–17%.",
   "skip_if": "Your gear fits behind the seats, or the heavy items are bikes, which belong on a hitch rack."},
 ],
 "tier_table": {
  "caption": "Approximate price bands from the picks in the 2019–2024 Forester guides (September 2026; Amazon prices move daily). Each column assumes standard raised rails, and the box mounts on that column's crossbars",
  "head": ["Upgrade", "Budget", "Mid", "Premium"],
  "rows": [
   ["Floor liners", "About $80–$130 (Subaru J501SSJ030 set of four, or IKABEVEM with a cargo liner)", "About $100–$140 (LASFIT or 3W TPE, first and second row)", "About $130–$170 (Husky WeatherBeater 95891)"],
   ["Roof rack", "About $80–$130 (EZREXPM or Snailfly clamp-on bars)", "About $100–$140 (Tuyoung lockable bars, 300 lb bar rating)", "About $545 (Thule WingBar Evo system, etrailer price)"],
   ["Trailer hitch", "About $120–$180 (Wsays 2 in Class 3; confirm ratings on the listing)", "About $200–$280 (Draw-Tite 76271, 2 in, 3,500 lb / 525 lb)", "About $410–$475 (Subaru L101SSJ005 for 2022–2024, 2 in, harness included)"],
   ["Cargo box", "About $450 (SportRack Vista XL, 18 cu ft, 63 in)", "About $709 (Yakima GrandTour 16, 79 in, 51.5 lb)", "About $880 (Thule Force 3 L, 76.8 in, 43 lb)"],
   ["Total", "About $730–$890; wiring harness extra", "About $1,109–$1,269; wiring harness extra", "About $1,965–$2,070; ball mount extra"],
  ],
 },
 "sections": [
  {"h": "Which roof is overhead: no rails, standard raised rails or the Wilderness rails",
   "body": "The fifth-generation Forester was built with three roofs, and each crossbar listing is written for one "
           "of them.\n\n"
           "**Premium, Sport, Limited and Touring.** Subaru's 2019, 2022 and 2024 trim comparison sheets list "
           "raised roof rails as standard. A gap under the rail is what clamp-on crossbars grip.\n\n"
           "**Base.** The same sheets list raised roof rails as optional, and Subaru's 2022 release says an option "
           "package adds alloy wheels and roof rails to the base model. A Base can therefore have a bare roof. "
           "Subaru's catalog excludes the base model from its SOA367010 aero crossbars. We could not confirm "
           "whether the optional rails match the rails on other trims, so Base owners should send the seller a "
           "photo of the roof before ordering.\n\n"
           "**Wilderness.** For 2022–2024 the sheets give the Wilderness roof rails with integrated tie-down "
           "points, anodized copper-finish accents and higher ratings. The crossbar listings in the roof rack "
           "guide say \"except Wilderness\" or \"not Wilderness\", and etrailer treats the trim as its own roof "
           "configuration. We could not confirm from Subaru what differs in the rail's shape, so go by the "
           "listing.\n\n"
           "Subaru's release also describes the refreshed 2022 Forester's rails as a new ladder-type design. The "
           "listings in the guide still treat the 2019–2024 standard rails as one fit.",
   "table": {"caption": "2019–2024 Forester roofs, Subaru's figures and what each roof takes",
             "head": ["Roof", "Trims and years", "Subaru's roof figure", "Crossbars"],
             "rows": [
              ["Raised rails, standard", "Premium, Sport, Limited, Touring, 2019–2024", "176 lb maximum (2022 and 2024 sheets); 700 lb static (2022 release)", "Clamp-on bars titled for Forester raised rails, about $80–$170; Subaru SOA367010, about $260–$350"],
              ["Raised rails, optional", "Base, when the option was ordered", "176 lb maximum (2022 and 2024 sheets)", "Confirm with the seller; Subaru's aero set excludes the base model"],
              ["No rails", "Base without the option", "Not listed; see the owner's manual", "Door-jamb clamp system from Thule or Yakima; none of the clamp-on sets"],
              ["Wilderness rails", "Wilderness, 2022–2024", "220 lb dynamic, 800 lb static (2022 and 2024 sheets)", "A Thule or Yakima system entered in the fit guide as Wilderness, or a set titled for it"],
             ]}},
  {"h": "176, 700, 220 and 800 lb: what Subaru prints for the roof, and what a box leaves",
   "body": "Four numbers describe this roof.\n\n"
           "- **176 lb.** Subaru's 2022 and 2024 trim comparison sheets list the standard roof rails at a 176 lb "
           "maximum capacity. Subaru's release on the refreshed 2022 Forester calls the same figure a dynamic load "
           "capacity, meaning while driving.\n"
           "- **700 lb.** The static, or parked, limit that the 2022 release gives the standard rails. The sheets "
           "don't print it.\n"
           "- **220 lb and 800 lb.** The Wilderness rails' dynamic and static maximums in the 2022 and 2024 "
           "sheets.\n\n"
           "We could not confirm the figure for 2019–2021: the 2019 sheet we read lists the rails without a "
           "capacity, so use the owner's manual. The 300 lb on a crossbar listing and the 165 lb "
           "on a Thule box describe the bar and the box. The lower number wins.\n\n"
           "Here is what each box in the cargo box guide leaves under 176 lb, before the crossbars' own weight "
           "comes off:\n\n"
           "- **Thule Pulse 2 M, 31 lb:** 145 lb.\n"
           "- **Rhino-Rack MasterFit 440, 38.6 lb:** 137.4 lb.\n"
           "- **INNO Wedge 660, 42 lb:** 134 lb, but etrailer lists the box at a 110 lb capacity.\n"
           "- **Thule Force 3 L, 43 lb:** 133 lb.\n"
           "- **Yakima GrandTour 16, 51.5 lb:** 124.5 lb.\n"
           "- **Yakima CBX 16, 57 lb:** 119 lb.\n"
           "- **SportRack Vista XL:** weight not published.\n\n"
           "The crossbar titles in the roof rack guide give no bar weights. The cargo box guide allows around "
           "15 lb for a set and puts the room left for gear at about 100–130 lb. On a Wilderness, start from "
           "220 lb, which adds 44 lb to every line above."},
  {"h": "Towing: 1,500 lb, 150 lb on the tongue, and why receiver size is the real choice",
   "body": "**The rating.** Subaru's 2019 trim comparison sheet lists a maximum towing capacity of **1,500 lb** on "
           "every trim. The 2022 and 2024 sheets list 1,500 lb on every trim except the Wilderness, at "
           "**3,000 lb**. The 2024 sheet notes that trailer brakes may be needed.\n\n"
           "**Tongue weight.** This is the limit for a bike rack or cargo carrier. A Subaru dealer listing for the "
           "2022–2024 factory hitch gives 150 lb for non-Wilderness trims and 300 lb for the Wilderness. The dealer "
           "page for the 2019–2021 kit, L101SSJ001, prints 176 lb. We could not confirm which figure Subaru "
           "applies to a 2019–2021 car, so check the owner's manual and plan on 150 lb until you have.\n\n"
           "**1.25 in or 2 in.** Every aftermarket hitch with published ratings in the guide is rated at 3,500 lb, "
           "so receiver size is the real choice. The guide notes that many larger platform bike "
           "racks are sold only in 2 in. The 1.25 in Draw-Tite 36671 and Reese 06191 weigh 27.5 lb, against 34 lb "
           "for CURT's 13409 and 37 lb for Draw-Tite's 76271.\n\n"
           "**The receiver.** Subaru sells the hitch as an accessory. The sheets we read list no receiver as "
           "equipment, so we could not confirm that any Forester leaves the factory with one. Look under the rear "
           "bumper.",
   "table": {"caption": "2019–2024 Forester towing by version (Subaru's figures; your owner's manual is the authority)",
             "head": ["Version", "Max tow", "Max tongue weight", "Subaru's accessory hitch"],
             "rows": [
              ["2019–2021, every trim", "1,500 lb (2019 sheet)", "Not confirmed: the dealer page for L101SSJ001 prints 176 lb; use the owner's manual", "L101SSJ001, 1-1/4 in, listed as Class One"],
              ["2022–2024 Base, Premium, Sport, Limited, Touring", "1,500 lb", "150 lb", "L101SSJ005, 2 in; harness and hitch plug included, ball mount separate"],
              ["2022–2024 Wilderness", "3,000 lb", "300 lb", "L101SSJ005, 2 in"],
              ["2025 Wilderness (older body per Wikipedia)", "3,000 lb per the dealer listing", "300 lb per the dealer listing", "A dealer lists L101SSJ005 for this 2025 trim only"],
             ]}},
  {"h": "Model years: the 2022 refresh, the 2014–2018 Forester and the 2025 Forester",
   "body": "This site's vehicle data and all four guides treat 2019–2024 as one generation. Four kinds of listing "
           "blur the edges.\n\n"
           "**The 2022 refresh.** Wikipedia describes it as a new front end and a slightly tweaked rear bumper, "
           "with the Wilderness introduced alongside. Two things in the guides split at 2022: Subaru's own hitch "
           "went from the 1-1/4 in L101SSJ001 to the 2 in L101SSJ005, and the Wilderness roof arrived. The "
           "aftermarket hitches and the floor liners run 2019–2024 as one part.\n\n"
           "**The 2014–2018 Forester.** Liners don't carry over, but Snailfly's and EZREXPM's clamp-on crossbars "
           "are titled 2014–2024.\n\n"
           "**The 2025 Forester.** Wikipedia says the sixth generation went on sale in the second quarter of 2024 "
           "as a 2025 model. Husky sells a separate liner set, 95381, for 2025–2026. Titles that reach past 2024 "
           "need a question to the seller: Tuyoung's crossbars are titled 2014–2026 and the adjustable set "
           "2019–2025. Hitch makers are the exception, since Draw-Tite, CURT and Reese list their "
           "Forester hitches for 2019–2026.\n\n"
           "**The 2025 Wilderness.** A Subaru dealer lists the 2022–2024 factory hitch for the 2025 Forester "
           "Wilderness and no other 2025 trim. Wikipedia says the outgoing Forester ended after the 2024 model "
           "year except for the Wilderness, which was offered for 2025, and that the redesigned Wilderness went on "
           "sale as a 2026 model. So treat a 2025 Wilderness as the older body. We could not confirm it from "
           "Subaru, so 2025 Wilderness owners should check every part by VIN."},
  {"h": "Roof or hitch: where the weight goes, what isn't ranked and the order to fit things",
   "body": "The Forester is a two-row SUV with no bed, so cargo that won't fit inside goes on the roof or behind "
           "the bumper. On standard trims Subaru's numbers are close: 176 lb on the roof against 150 lb on the "
           "tongue. The roof takes bulky, light gear in a cargo box, and the cargo box guide sends bikes to a "
           "hitch rack. On a Wilderness the hitch pulls ahead, at 300 lb against 220 lb.\n\n"
           "Height is the roof's other cost. The 2019 sheet gives an overall height of 68.1 in with roof rails, "
           "and the boxes in the guide stand 11 to 19 in tall on top of the bars, so measure before driving into "
           "a garage. Subaru's sheets also list a panoramic moonroof on every trim except the Base, and etrailer "
           "advises against opening it with a rack installed.\n\n"
           "This page ranks the four categories that have a fit-checked Forester guide on this site. Running "
           "boards, lighting and bike racks have none for this vehicle, so they aren't ranked.\n\n"
           "Fit the four in this order.\n\n"
           "1. **Floor liners.** Remove the factory mat and hook the driver liner onto Subaru's retention hooks.\n"
           "2. **Crossbars.** Set the spread to suit the box and keep the rear bar ahead of the point where the "
           "rail curves down toward the liftgate.\n"
           "3. **Trailer hitch.** Draw-Tite quotes about 30 minutes with no drilling for the 76271; CURT says its "
           "13409 needs a hole enlarged. Fit the plug-in 4-flat harness the same day.\n"
           "4. **Cargo box.** Slide it as far forward as the windshield and antenna allow and open the liftgate "
           "slowly the first time."},
 ],
 "avoid": [
  {"h": "Clamp-on crossbars for the wrong roof", "body": "Standard-rail bars are titled \"except Wilderness\" or \"not Wilderness\", and a Base without the rail option has nothing to clamp to."},
  {"h": "Loading the roof to the bar or box rating", "body": "A 300 lb crossbar or a 165 lb box rating doesn't change Subaru's 176 lb figure for the standard rails or the Wilderness's 220 lb dynamic figure. The 700 lb and 800 lb numbers are for a parked Forester."},
  {"h": "Planning a bike rack around the hitch rating", "body": "A 3,500 lb, 525 lb hitch on a standard Forester is still a 1,500 lb, 150 lb setup. Add the rack's weight to the bikes before buying."},
  {"h": "Trusting a year range that crosses a generation", "body": "The 2025 Forester has its own liners, such as Husky's 95381, and crossbar titles that run to 2025 or 2026 need the seller's confirmation."},
 ],
 "verdict": {
  "thesis": "On the 2019–2024 Forester, buy floor liners by generation first, crossbars by rail type second, a 2 in trailer hitch planned around 150 lb of tongue weight third, and a cargo box last, once the bars and the 176 lb roof math are settled.",
  "body": "The fifth-generation Forester is easy to accessorize once four facts are written down: model year, "
          "whether the roof has rails, Wilderness or not, and whether a receiver is already fitted. Floor liners "
          "need the year first, since the listings cover 2019–2024 as one fit, and they cost the least. A roof rack needs the "
          "rail answer. On standard raised rails an Amazon set costs about $80–$170, and Subaru's 2022 and 2024 "
          "sheets give that roof 176 lb, which is why it goes ahead of the trailer hitch. On a Base with no rails, "
          "swap the two.\n\n"
          "The hitch is third because Subaru rates most Foresters at 1,500 lb and a dealer listing gives 150 lb of "
          "tongue weight, so it is a bike rack mount first. The cargo box is last because it costs the most and has "
          "to fit the bars, the liftgate and the roof figure. Owners of a 2025 Forester should treat this page as "
          "a list of questions, not part numbers.",
 },
 "sources": [
  ["2024 Forester trim comparison: roof rails and capacity, towing by trim (Subaru)", "https://www.subaru.com/services/vehicles/pdf/trimComparison/2024/FOR"],
  ["2022 Forester trim comparison: roof rails and capacity, towing by trim (Subaru)", "https://www.subaru.com/services/vehicles/pdf/trimComparison/2022/FOR"],
  ["2019 Forester trim comparison: roof rails by trim, towing, height (Subaru)", "https://www.subaru.com/services/vehicles/pdf/trimComparison/2019/FOR"],
  ["Subaru announces pricing on refreshed 2022 Forester: roof rail design and load limits, Wilderness (Subaru U.S. Media Center)", "https://media.subaru.com/pressrelease/1789/1/subaru-announces-pricing-refreshed-2022-forester-suv"],
  ["Subaru Forester: fifth generation, 2022 facelift, sixth generation (Wikipedia)", "https://en.wikipedia.org/wiki/Subaru_Forester"],
  ["Subaru L101SSJ005 trailer hitch, 2022–2024: ratings by trim, contents, 2025 Wilderness note (Subaru Parts Pros)", "https://www.subarupartspros.com/sku/l101ssj005.html"],
  ["Subaru L101SSJ001 trailer hitch, 2019–2021 (Subaru Parts Pros)", "https://www.subarupartspros.com/sku/l101ssj001.html"],
  ["Subaru Aero Crossbar Set SOA367010: fit notes and MSRP (Subaru Parts Pros)", "https://www.subarupartspros.com/sku/soa367010.html"],
  ["2022 Forester roof rack systems by rail type and moonroof note (etrailer)", "https://www.etrailer.com/roof-2022_Subaru_Forester.htm"],
  ["Draw-Tite 76271 Class III hitch (Draw-Tite)", "https://www.draw-tite.com/product/76271"],
  ["CURT 13409 Class 3 hitch (CURT)", "https://www.curtmfg.com/part/13409"],
  ["Yakima GrandTour 16 (Yakima)", "https://yakima.com/products/grandtour-16"],
  ["Thule Force 3 L (Thule)", "https://www.thule.com/en-us/cargo-carrier/car-top-carrier/thule-force-3-l-_-645750"],
  ["Cargo box fuel economy impact (fueleconomy.gov)", "https://www.fueleconomy.gov/feg/driveHabits.jsp"],
  ["Husky Liners: WeatherBeater vs X-act Contour (Husky Liners)", "https://huskyliners.com/blog/husky-liners-weatherbeater-vs-xact-contour/"],
 ],
}
