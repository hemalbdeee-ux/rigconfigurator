"""Upgrades pillar: 2025–2026 Toyota 4Runner (6th gen, N410, TNGA-F; an SUV, no bed).
Hub page: ranks the four published 4Runner category guides and links to them. No product picks or ASINs here
(the site pulls each guide's #1 pick). Every price band comes from the linked guides' picks[].price fields, plus one
price quoted in the cargo box guide's text (The Rack Shop's Thule raised-rail crossbar kit, $444.90 on sale).
Vehicle facts from db/migrations/003_vehicles.sql (SUV, roof_type raised-rails, no stored roof load, hitch class 4,
2 in receiver, 6,000 lb, "5th-gen roof racks, mats and hitches do NOT carry over", verify flags on roof load rating
and rail style by trim; the 2010–2024 row for the older generation), the four guides and their sources, and seven
pages opened for this page on 2026-10-04:
- Toyota's 2025 4Runner launch release (nine grades; i-FORCE MAX standard on Platinum, TRD Pro and Trailhunter and
  available on TRD Off-Road, TRD Off-Road Premium and Limited; i-FORCE gas on SR5, TRD Sport and TRD Sport Premium;
  6,000 lb maximum towing; TNGA-F shared with Tacoma, Tundra, Land Cruiser and Sequoia; Trailhunter ARB roof rack and
  RIGID color-selectable LED fog lamps; TRD Pro 20 in grille LED light bar and RIGID LED fog lamps; SR5 LED head and
  fog lights; power-extending running boards available on Limited).
- Wikipedia's Toyota 4Runner page (nine trims and the same powertrain split; the hybrid "uses the space beneath the
  load floor for its high-voltage battery" and "it is expected the hybrid will not include the third row").
- 4Runner6G.com roof load thread cited by the guides (the 165 lb dynamic / 770 lb static figures are one poster's
  quote of GearJunkie's first-drive review, not a Toyota document).
- 4Runner6G.com thread "TRD Off-Road Premium OEM roof rails dynamic load" (one member gives 770 / 165 lb for the OEM
  half roof rack; the original poster cites 125 lb dynamic for the factory crossbars and says a dealer could not give
  a figure for the raised rails).
- 4Runner6G.com factory crossbars and cargo box thread (a Thule box and a Yakima basket on factory bars; one owner
  moved the bars one position closer).
- A Toyota 2025 4Runner specifications sheet posted as an attachment on 4Runner6G.com (6,000 lb; seven seats
  available on i-FORCE SR5 and Limited; roof rails, running boards and rock rails by grade). It was read through a
  text extraction and its grade columns could not be matched reliably, so the page prints no trim list from it.
Not verified, and worded as such in the text: the roof load limit from a Toyota document (GearJunkie's review, the
forum's stated origin of 165 / 770 lb, was not opened) and whether one figure covers raised rails, factory crossbars and the ARB platform alike; rail style and factory crossbars for every grade;
what the TRD Pro's roof carries; which grades ship with a hitch receiver, and the receiver's class (Class IV with a
2 in receiver is our vehicle data, not a Toyota page); which grades have running boards or rock rails; why liner
makers exclude the hybrid (the makers don't say); whether a hybrid can be ordered with a third row; 2026 fit of
Husky's 96531 and Toyota's PT989-89251, whose listings name 2025; box clamp fit on the Trailhunter's or any
aftermarket platform's bars; Rough Country 88205 and Toyota/ARB rack weights; whether any grade besides TRD Pro
and Trailhunter has a grille light bar. No 4Runner guide exists for trailer hitches or running boards on this site;
none are ranked.
"""

KIND = "upgrades"
KEY = ("toyota", "4runner", "2025-present")
CATEGORIES = ["floor-mats", "roof-racks", "cargo-boxes", "led-light-bars"]

TITLE = "2025–2026 Toyota 4Runner Upgrades, Ranked: 4 Mods in Order, With 5th-Gen and Hybrid Fit Traps"
META = ("Four 2025–2026 4Runner upgrades in buying order: floor liners, roof rack, cargo box and light bar, with "
        "5th-gen, hybrid, third-row and roof-load traps.")

FAQ = [
 ("What should I upgrade first on a 2025–2026 Toyota 4Runner?",
  "Floor liners, then a roof rack. Liners cost the least, about $120–$240 across the picks in our guide, and they "
  "need two facts from you: gas or i-FORCE MAX hybrid, and five seats or seven. The roof rack comes second because "
  "the cargo box and any roof light depend on it. Raised rails take clamp-on crossbars at about $100–$170, while a "
  "Trailhunter's ARB platform needs nothing. The cargo box is third and lighting is last, since some trims ship with a grille light bar. Buy only listings that name 2025 or 2026."),
 ("Do 2010–2024 4Runner parts fit the 2025–2026 4Runner?",
  "No, with one exception. Toyota moved the 2025 model to its TNGA-F platform, and our guides found a new cabin "
  "floor, roof, hood and front end. Makers sell separate parts. Husky's liners are 99571 for 2013–2024 and 96531 "
  "for 2025. Rough Country's roof platform is 88201 for the old body and 88205 for the new one. The exception is the cargo box, which clamps "
  "to crossbars and not to the vehicle, so the box carries over while the bars under it don't."),
 ("I have the i-FORCE MAX hybrid. What changes on this list?",
  "Mostly the floor and cargo liners. Toyota's launch release makes the i-FORCE MAX standard on the Platinum, TRD "
  "Pro and Trailhunter and available on the TRD Off-Road, TRD Off-Road Premium and Limited. LASFIT, TripleAliners and Vantio all exclude the hybrid. Wikipedia says the hybrid uses the "
  "space beneath the load floor for its high-voltage battery, so treat cargo liners with the same caution. Toyota's genuine liner is the low-risk route because a dealer can check it against your VIN. Racks, boxes and lights don't depend on powertrain."),
 ("Does a seven-seat 4Runner need different parts?",
  "Only the liners. A seven-seat 4Runner needs a three-row set and a cargo liner cut around the folded third row. "
  "Our guide lists two: a budget kit for seven-seat SR5 and Limited gas models at about $150–$200, and NQOQN's "
  "kit, whose listing doesn't state powertrain. Toyota's listing says its genuine liner is third-row compatible, "
  "which is not the same as third-row coverage, so ask the dealer which rows are included. LASFIT, TripleAliners "
  "and Vantio list five seats, and Husky's 96531 covers the front and second rows only."),
 ("How much weight can the 2025–2026 4Runner roof carry with a rack and a cargo box?",
  "Use the figure in your owner's manual. Owners on 4Runner6G.com cite 165 lb dynamic, meaning while driving, and "
  "770 lb static, meaning parked. We could not confirm either from a Toyota document. The rack counts first. Sherpa quotes about 50 lb "
  "for its Capitol platform, which leaves about 115 lb of 165. A 43 lb Thule Force 3 L on top leaves about 72 lb "
  "for gear. A rack's own rating, such as Rough Country's 300 lb dynamic, never raises the roof's limit."),
 ("Can I put a cargo box on the factory crossbars, or do I need a new roof rack?",
  "Factory crossbars will do if your 4Runner has them. On 4Runner6G.com, owners report mounting a "
  "Thule box and a Yakima basket on factory bars, and one had to move the bars one position closer before the "
  "clamps fit. Check the box's crossbar spread against where your bars can sit: 24 to 36 in for Yakima's GrandTour "
  "16, and three fixed positions for SportRack's Vista XL. One owner in another thread cites 125 lb dynamic for the factory crossbars, lower than the 165 lb usually quoted, so read the manual."),
 ("I have a Trailhunter or TRD Pro. Which of these upgrades do I still need?",
  "Fewer than other owners. Toyota's launch release gives the Trailhunter an ARB roof rack, RIGID color-selectable "
  "LED fog lamps and a grille with an integrated LED light bar, and the TRD Pro a 20 in grille light bar and RIGID "
  "fog lamps. A Trailhunter can skip the roof rack, and both can skip fog-pocket kits. What remains: floor liners that suit the hybrid, since both trims are hybrid-only, and a cargo box whose clamps fit the platform's bars. We could not confirm what the TRD Pro's roof carries, so look before buying crossbars."),
 ("Can I mount a light bar on the roof of a 2025–2026 4Runner?",
  "Yes, but the mount comes from the rack. Our lighting guide says a roof bar on this generation attaches to an "
  "aftermarket platform or to the Trailhunter's ARB rack, not to the roof itself. Sherpa builds its Capitol in a "
  "half-height version for a single-row light bar, and Front Runner lists a light-bar-ready kit, KSTF005T. Choose the roof rack first. A roof bar gives the most reach, the most hood glare and the most wind noise. The same guide says such lights are usually for off-road use only. Rules vary, so check your state's."),
 ("Does the 2025–2026 4Runner come with a trailer hitch, and how much can it tow?",
  "Look under the rear bumper and read the window sticker. Our vehicle data records the hitch for this generation "
  "as Class IV with a 2 in receiver and a 6,000 lb maximum tow rating, and Toyota's launch release gives the same "
  "6,000 lb maximum. We could not confirm which grades ship with a receiver. The number for your 4Runner is in the "
  "owner's manual. There is no trailer hitch guide for this generation on this site yet, so none is ranked. An aftermarket hitch never raises the tow rating."),
 ("How much does it cost to add all four upgrades to a 2025–2026 4Runner?",
  "From the prices on our four guides' picks, a budget build runs about $840–$930: LASFIT's cabin liners, clamp-on "
  "crossbars, SportRack's Vista XL and Cali Raised's ditch light kit. A mid build runs about $1,179–$1,289 with "
  "Husky's WeatherBeater set, the 330 lb adjustable crossbars, Yakima's GrandTour 16 and Cali Raised's fog kit. A "
  "premium build with Toyota's genuine liners, the Thule crossbar kit, a Thule Force 3 L or Motion 3 XL and Baja's "
  "S2 Sport fog kit runs about $2,112–$2,442. All three assume raised rails with no crossbars yet."),
]

ARTICLE = {
 "dek": "Four upgrades for the sixth-generation 4Runner, in buying order. Fit on this SUV turns on a short list of "
        "facts: the 2025 redesign, which leaves older parts behind; gas or i-FORCE MAX hybrid; five seats or seven; "
        "what is already on the roof; and a trim list that puts a rack, a grille light bar or RIGID fog lamps on some models.",
 "author": "jake-morrison",
 "reviewed": "2026-10-04",
 "method": "We did not install any of these parts ourselves. The order comes from our four fit-checked 2025–2026 "
           "4Runner guides, weighing how many owners each upgrade suits, what it costs, which upgrades depend on another, and how much of the fit is confirmed. Price bands are the prices "
           "listed on those guides' picks, checked at maker and retailer stores in September 2026, and are "
           "approximate. Vehicle facts come from our vehicle data, the guides' sources, Toyota's 2025 launch "
           "release, Wikipedia's 4Runner page and three 4Runner6G.com owner threads. Where we couldn't confirm a "
           "factory detail, the text says so.",
 "takeaways": [
  "**Buy 2025+ parts.** The 4Runner moved to TNGA-F for 2025, and Husky, Rough Country and Front Runner sell separate part numbers for the older generation.",
  "**Gas or hybrid, five seats or seven.** Several liner sets exclude the i-FORCE MAX, and a third row needs a three-row set.",
  "**Look at the roof first.** Raised rails take clamp-on crossbars; a Trailhunter already has an ARB platform that rail clamps can't grip.",
  "**One roof limit covers rack, box and gear.** Owners cite 165 lb while driving. We could not confirm it from Toyota, so check your manual.",
  "**Check the trim before buying lights.** Toyota fits the TRD Pro and Trailhunter with a grille light bar and RIGID fog lamps.",
 ],
 "priority": [
  {"category": "floor-mats",
   "h": "1. Floor liners first: the lowest price, and two questions before you order",
   "why": "Floor liners lead because they cost the least on this page and get used on every drive. The 2025 model has a new cabin floor, so buy listings that name 2025 or later. Husky shows "
          "the split in its catalog: 96531 for the 2025 4Runner and 99571 for 2013–2024. Two questions decide the "
          "rest. First, gas or i-FORCE MAX hybrid. LASFIT, TripleAliners, Vantio and the budget seven-seat set in "
          "our guide all say they are not for the hybrid. Second, five seats or seven. A third row needs a "
          "three-row set and a cargo liner cut around it. Prices in our guide run about $120–$160 for LASFIT's "
          "cabin set, about $150–$200 for TripleAliners' kit with cargo and seatback pieces or for the three-row "
          "set, about $150–$210 for Husky's WeatherBeater and about $180–$240 for Toyota's genuine liners, which a "
          "dealer can check against your VIN. The trade-off is documentation against coverage: Husky publishes a "
          "lifetime warranty against cracks and breaks but covers the cabin only, and its listing names 2025 "
          "without stating powertrain or seating.",
   "skip_if": "You drive in a dry climate, keep the cabin clean and are content with the factory mats."},
  {"category": "roof-racks",
   "h": "2. Roof rack second: the base for the cargo box and any roof light",
   "why": "A roof rack ranks second because two later upgrades stand on it. A cargo box clamps to crossbars or a "
          "platform, and a roof light bar mounts to the rack, not to the roof. Raised side rails take clamp-on crossbars, about $100–$150 for the 260 lb set in our guide or about "
          "$120–$170 for the 330 lb adjustable set; those ratings are the sellers' own. A Trailhunter already has "
          "an ARB platform, and rail-clamp bars have nothing to grip on it. Platforms bolt to the factory mounting "
          "points with no drilling: Rough Country's 88205 at about $700 with a 40 x 56 in deck, Toyota's ARB-built "
          "PT989-89251 at about $1,200–$1,600, and Sherpa's full-length Capitol at about $1,559 and about 50 lb. "
          "The roof itself is the limit. Owners on 4Runner6G.com cite 165 lb while driving, and the rack's weight "
          "comes out of that first. Racks and crossbars from the older generation don't fit. The trade-off: a platform gives a flat deck with T-slots, while crossbars weigh far less.",
   "skip_if": "Your roof already carries factory crossbars or the Trailhunter's platform, or nothing you carry needs to go up there."},
  {"category": "cargo-boxes",
   "h": "3. Cargo box third: a universal box, fitted to this roof by weight, spread and hatch gap",
   "why": "A cargo box comes third because it can't be chosen until the rack question is settled. The box is universal; the math is not. Bars or platform, box and gear all share the "
          "roof's driving limit, which owners cite at 165 lb. The boxes in our guide weigh from 38.6 lb for "
          "Rhino-Rack's MasterFit 440L to 57 lb for Yakima's CBX 16. Three checks decide fit. Crossbar spread: "
          "Yakima's GrandTour 16 accepts 24 to 36 in, and one owner on 4Runner6G.com had to move the factory "
          "crossbars one position closer before a Thule box's clamps fit. Hatch clearance: Thule lists more than "
          "50 5/8 in of front clearance for its Force 3 L. Clamp size, if the box sits on a platform. Prices run "
          "about $450 for SportRack's Vista XL, about $699 for the CBX 16, about $709 for the GrandTour 16, about "
          "$880 for the Force 3 L and about $1,150 for Thule's Motion 3 XL; Rhino-Rack publishes no price. The trade-off is volume against weight: an 18 cu ft box holds more dense gear than the roof can carry.",
   "skip_if": "Your gear fits behind the second row, or it is heavy enough to belong on a hitch-mounted carrier."},
  {"category": "led-light-bars",
   "h": "4. Lighting last: a thin market, and your trim may already have it",
   "why": "Lighting ranks last for three reasons. Some trims already have it: Toyota's launch release gives the "
          "TRD Pro a 20 in LED light bar in the grille and RIGID fog lamps, and the Trailhunter a grille light bar "
          "and RIGID color-selectable fog lamps. The 6th-gen market is still thin, so our guide lists fog-pocket "
          "kits and hood-hinge ditch lights, not a wide choice of bars. And most auxiliary light is off-road light. Baja Designs' S2 Sport kit, about $607, puts four lights in the fog pockets and "
          "runs from the stock fog switch, but Baja says it will not work on the TRD Pro. Cali Raised's hood-hinge "
          "ditch kit, from about $170, bolts to factory points and is not for 2024 or older 4Runners. Its two-bar "
          "fog kit is about $200. A true light bar means the grille on a TRD Pro or Trailhunter, where Diode "
          "Dynamics sells an SS20 kit maker-direct, or the roof, where the mount comes from the rack. Check your state's rules before switching any of it on.",
   "skip_if": "You own a TRD Pro or Trailhunter and the factory grille bar and RIGID fogs are enough, or you never drive unlit trails."},
 ],
 "tier_table": {
  "caption": "Approximate price bands from the picks in our 2025–2026 4Runner guides (September 2026; Amazon prices move daily). Each column assumes raised rails; the box sits on that column's crossbars",
  "head": ["Upgrade", "Budget", "Mid", "Premium"],
  "rows": [
   ["Floor liners", "About $120–$160 (LASFIT cabin set; gas, five-seat only)", "About $150–$210 (Husky WeatherBeater 96531; confirm 2026, powertrain and seating)", "About $180–$240 (Toyota genuine liners, checked by VIN)"],
   ["Roof rack", "About $100–$150 (260 lb clamp-on crossbars)", "About $120–$170 (330 lb adjustable clamp-on crossbars)", "About $445 (Thule raised-rail crossbar kit, rated 165 lb; The Rack Shop's sale price)"],
   ["Cargo box", "About $450 (SportRack Vista XL; three fixed bar positions)", "About $709 (Yakima GrandTour 16, 24–36 in spread)", "About $880 (Thule Force 3 L) to $1,150 (Thule Motion 3 XL); confirm the spread with Thule"],
   ["Lighting", "About $170 (Cali Raised ditch light kit, no switch)", "About $200 (Cali Raised two-bar fog kit)", "About $607 (Baja Designs S2 Sport fog kit; not for TRD Pro)"],
   ["Total", "About $840–$930", "About $1,179–$1,289", "About $2,112–$2,442"],
  ],
 },
 "sections": [
  {"h": "What the 4Runner may already have: roof, grille, fog lamps, steps and hitch",
   "body": "Three of the four upgrades change with what Toyota fitted at the factory. The table is not a full equipment list, and we could not confirm rail style or factory crossbars for every grade.\n\n"
           "**Hitch and towing.** There is no trailer hitch guide for this generation on this site, so none is "
           "ranked. Our vehicle data records the hitch as **Class IV with a 2 in receiver** and the maximum tow "
           "rating as **6,000 lb**, and Toyota's launch release gives the same maximum. We could not confirm which "
           "grades ship with a receiver. Look under the rear bumper before shopping for a trailer hitch.\n\n"
           "**Steps.** There is no running boards guide for this generation either. Toyota's launch release lists "
           "power-extending running boards as available on the Limited. A Toyota 2025 specification sheet posted "
           "on 4Runner6G.com lists running boards on several grades and steel rock rails on the TRD Pro, but we "
           "could not match every line to a grade with confidence, so we print no trim list.",
   "table": {"caption": "2025–2026 4Runner grades: powertrain and factory equipment per Toyota's launch release",
             "head": ["Grade", "Powertrain", "Factory equipment we could confirm", "What changes"],
             "rows": [
              ["SR5", "i-FORCE gas", "LED head and fog lights; optional third row per our liner guide", "Count the seats before ordering liners"],
              ["TRD Sport, TRD Sport Premium", "i-FORCE gas", "Nothing we could confirm that changes fit", "Gas five-seat liner sets apply"],
              ["TRD Off-Road, TRD Off-Road Premium", "Gas, or i-FORCE MAX", "Owners report factory crossbars on SR5 and TRD Off-Road Premium", "Check powertrain; a box may fit the bars you have"],
              ["Limited", "Gas, or i-FORCE MAX", "Power-extending running boards available; optional third row per our liner guide", "Check powertrain and seating"],
              ["Platinum", "i-FORCE MAX", "Nothing further we could confirm", "Hybrid liner rule applies"],
              ["TRD Pro", "i-FORCE MAX", "20 in LED light bar in the grille; RIGID LED fog lamps", "Skip fog-pocket kits; roof equipment not confirmed"],
              ["Trailhunter", "i-FORCE MAX", "ARB roof rack; RIGID color-selectable LED fog lamps; grille LED light bar", "Skip the roof rack and fog kits; a box clamps to the platform's bars"],
             ]}},
  {"h": "Older parts, Tacoma parts and listings with no year",
   "body": "The 2025 redesign is the first fit trap in every category. Toyota's launch release puts the 4Runner "
           "on the TNGA-F platform shared with the Tacoma, Tundra, Land Cruiser and Sequoia. Our vehicle data says "
           "roof racks, mats and hitches from the older generation do not carry over.\n\n"
           "The older generation ran for 15 years, so its parts are plentiful, and our roof rack and lighting guides both note sellers who title them simply \"4Runner\". Look for 2025 or 2026 in the title, and check the part number on a used part.\n\n"
           "Ditch brackets and fog kits are often titled for the 2024+ "
           "Tacoma, the 2022+ Tundra and the 2025+ 4Runner together, because the parts are shared. Floor liners "
           "are the opposite. Our floor liner guide says the 4Runner's cabin, second row and cargo area are its "
           "own, so a Tacoma set does not fit.\n\n"
           "Husky's 96531 and Toyota's PT989-89251 rack are both listed for 2025, so ask about a 2026.",
   "table": {"caption": "What the parts in our 4Runner guides say about generation",
             "head": ["Part", "2010–2024 generation", "2025–2026 4Runner", "What to do"],
             "rows": [
              ["Husky WeatherBeater liners", "99571 (2013–2024)", "96531 (listing names 2025)", "Confirm 2026 with Husky"],
              ["Rough Country roof platform", "88201", "88205 (2025–2026)", "Check the part number on a used rack"],
              ["Front Runner Slimsport", "KSTF003T", "KSTF004T", "Buy from Dometic or a Front Runner dealer"],
              ["Clamp-on crossbars", "Different clamps", "Listings titled 2025–2026, raised rails", "Don't reuse old bars"],
              ["Cali Raised ditch light kit", "Not designed for 2024 or older", "2025+ 4Runner and 2024+ Tacoma", "A shared Tacoma title is expected"],
              ["Rooftop cargo box", "Carries over", "Carries over", "Keep the box, buy 2025–2026 crossbars"],
             ]}},
  {"h": "Gas or hybrid, five seats or seven: the two liner questions",
   "body": "Floor liners are the one category here where the powertrain matters. Toyota's launch release makes "
           "the i-FORCE MAX hybrid standard on the Platinum, TRD Pro and Trailhunter and available on the TRD "
           "Off-Road, TRD Off-Road Premium and Limited. The SR5, TRD Sport and TRD Sport Premium are gas.\n\n"
           "The liner makers don't say why they exclude the hybrid. Wikipedia says the hybrid uses the space "
           "beneath the load floor for its high-voltage battery, a reason to be as careful with cargo liners. It also says the hybrid is expected not to include the third row, which we could not confirm.\n\n"
           "What each set in our guide states:\n\n"
           "- **Husky WeatherBeater 96531:** front and second row. The listing names 2025 and does not state "
           "powertrain or seating, so check Husky's fit tool.\n"
           "- **Toyota genuine liners:** 2025+, third-row compatible per the listing. A dealer can confirm hybrid "
           "and seating by VIN.\n"
           "- **LASFIT:** five-seat, gas, not hybrid. A cabin set, or a full set with cargo and backrest mats.\n"
           "- **TripleAliners:** five-seat, gas, not hybrid. Front, second row, cargo and seatback.\n"
           "- **Vantio:** five-seat, not hybrid.\n"
           "- **Budget three-row set:** seven-seat SR5 and Limited, not hybrid, with a cargo liner.\n"
           "- **NQOQN:** seven-seat. Powertrain not stated, so ask the seller.\n\n"
           "For a hybrid, that leaves Toyota's liner or a seller's written confirmation."},
  {"h": "One roof limit for the rack, the box and the lights",
   "body": "Everything on the roof shares one number, the least certain fact on this page. Our guides use **165 lb dynamic and 770 lb static**, as cited by owners on 4Runner6G.com. The poster in that "
           "thread attributes the figures to GearJunkie's first-drive review. In a second thread, a member quotes "
           "the same pair for the OEM half roof rack, another owner cites 125 lb dynamic for the factory "
           "crossbars, and a dealer could not give a figure for the raised rails. Our vehicle data holds no figure, and we could not confirm one from Toyota. Your owner's manual is the authority.\n\n"
           "Taking 165 lb as the working number, subtract in this order:\n\n"
           "- **The rack.** Sherpa quotes about 50 lb for the Capitol, which leaves about 115 lb. Rough Country "
           "doesn't publish the 88205's weight and Toyota doesn't publish the ARB-built rack's, so ask.\n"
           "- **The box.** 38.6 lb for the MasterFit 440L, 43 lb for the Force 3 L, 51 lb for the Motion 3 XL, "
           "51.5 lb for the GrandTour 16 and 57 lb for the CBX 16. SportRack doesn't publish the Vista XL's "
           "weight.\n"
           "- **The gear.** On crossbars, our cargo box guide puts it at roughly 100 lb. On the Capitol under a Force 3 L, 72 lb is left.\n\n"
           "Ratings on the parts don't change this. Rough Country and Sherpa list 300 lb dynamic, and the crossbar sellers 260 lb and 330 lb. The lowest figure in the stack applies on the road.\n\n"
           "Two more measurements matter. Thule lists front clearance of more than 50 5/8 in for the Force "
           "3 L and more than 52 3/32 in for the Motion 3 XL, to keep the box off the rear hatch. And the boxes "
           "add 15 to 19 in of height, so measure the garage door."},
  {"h": "Decide the roof as one job, then fit in this order",
   "body": "The roof rack, cargo box and roof light bar are one decision.\n\n"
           "- **Box only:** keep the raised rails and use crossbars. They cost and weigh the least.\n"
           "- **Box on a platform:** check the box maker's maximum bar size against the platform's bars. Our cargo "
           "box guide points platform owners to the 38.6 lb MasterFit 440L.\n"
           "- **Roof light bar:** pick a rack with a light mount first, such as Sherpa's half-height Capitol.\n"
           "- **Platform in place of rails:** owners fitting Toyota's ARB-built rack report removing the factory "
           "rails with a 12 mm socket and a pry tool. Keep the rails and bolts.\n\n"
           "Then fit in this order.\n\n"
           "1. **Floor liners.** No tools. Remove the factory mats, hook the driver liner onto the retention posts "
           "and press the pedals to the floor.\n"
           "2. **Roof rack.** Set crossbars to the spacing the box maker specifies and tighten the clamps evenly. "
           "For a platform, torque to the kit's figure.\n"
           "3. **Cargo box.** Fit the clamps loosely, measure from the front bar to the hatch seam, open the hatch "
           "slowly, then tighten.\n"
           "4. **Lights.** Fog-pocket kits plug into the factory fog connectors. Ditch pods need a relay, a fuse and a switch."},
 ],
 "avoid": [
  {"h": "An older-generation part, or a listing with no year", "body": "The cabin floor, roof, hood and front end changed for 2025. Husky's 99571 and Rough Country's 88201 are parts for the older body."},
  {"h": "A gas-only liner set in a hybrid, or a five-seat kit with a third row", "body": "LASFIT, TripleAliners and Vantio exclude the i-FORCE MAX and list five seats."},
  {"h": "Loading the roof to the rack's rating", "body": "A 600 lb static rating or a 330 lb crossbar rating doesn't raise the roof's limit. Rack, box and gear all count against the driving figure in your manual."},
  {"h": "Fog kits or clamp-on bars bought before checking the trim", "body": "Baja's S2 Sport kit will not work on a TRD Pro, and rail clamps have nothing to grip on the Trailhunter's ARB platform."},
 ],
 "verdict": {
  "thesis": "On the 2025–2026 4Runner, buy floor liners matched to powertrain and seating first, choose a roof rack by the roof you already have, add a cargo box that fits the bars and the weight budget, and leave lighting for last.",
  "body": "The sixth-generation 4Runner is easy to accessorize once five facts are written down: model year, gas "
          "or hybrid, five seats or seven, what is on the roof, and which trim it is. Floor liners need the first "
          "three and cost the least, so they go first. Crossbars at about $100–$170 are enough for a box, and a platform is worth its weight only for flat gear or a roof light.\n\n"
          "The cargo box is third because it is bought to fit the rack and the roof limit, which owners cite at "
          "165 lb and which we could not confirm from Toyota. A light bar or fog kit is fourth because the market is thin and most of it is off-road light. "
          "Before shopping for a trailer hitch, look under the rear bumper. Owners of a 2010–2024 4Runner should "
          "treat this page as a list of questions, not part numbers. Each linked guide covers the fit details for "
          "its category.",
 },
 "sources": [
  ["The All-New 2025 Toyota 4Runner: TNGA-F, grades, powertrains, towing, TRD Pro and Trailhunter equipment (Toyota Newsroom)", "https://pressroom.toyota.com/the-all-new-2025-toyota-4runner-the-icon-that-inspires-exploration/"],
  ["Toyota 4Runner, sixth generation: trims, hybrid battery location, third row (Wikipedia)", "https://en.wikipedia.org/wiki/Toyota_4Runner"],
  ["Roof load figures cited by owners, Trailhunter rack on another trim (4Runner6G.com)", "https://www.4runner6g.com/forum/threads/installing-trailhunter-roof-rack-on-another-trim-same-weight-load-capacity.2248/"],
  ["TRD Off-Road Premium OEM roof rails dynamic load (4Runner6G.com)", "https://www.4runner6g.com/forum/threads/trd-off-road-premium-oem-roof-rails-dynamic-load.5655/"],
  ["Factory crossbars and a rooftop cargo box, 2025 4Runner (4Runner6G.com)", "https://www.4runner6g.com/forum/threads/help-with-factory-crossbars-measurement-will-my-rooftop-cargo-box-fit.5075/"],
  ["2025 4Runner specifications and product information sheet, as posted by an owner (4Runner6G.com)", "https://4runner6g.com/forum/attachments/2025-4runner-specs-product-info-pdf.5259"],
  ["Husky Liners: WeatherBeater vs X-act Contour (Husky Liners)", "https://huskyliners.com/blog/husky-liners-weatherbeater-vs-xact-contour/"],
  ["Rough Country roof rack 88205, 2025–2026 4Runner (Rough Country)", "https://www.roughcountry.com/product/toyota-4runner-roof-rack-88205"],
  ["Sherpa Equipment Co. The Capitol, 2025–2026 4Runner (Sherpa)", "https://sherpaec.com/products/capitol"],
  ["Toyota Roof Rack by ARB PT989-89251 (Toyota Auto Parts)", "https://autoparts.toyota.com/products/product/roof-rack-pt98989251"],
  ["Front Runner Slimsport KSTF004T, 6th-gen 4Runner (Dometic)", "https://www.dometic.com/en-us/product/toyota-4runner-6th-gen-roofrack-slimsport-kstf004t"],
  ["Thule crossbar kit for 2025–2026 4Runner raised rails (The Rack Shop)", "https://therackshop.com/2025-2026-toyota-4runner-w-raised-rails-thule-53-crossbar-complete-roof-rack/"],
  ["Thule Force 3 L: weight, load rating, front clearance (Thule)", "https://www.thule.com/en-us/cargo-carrier/car-top-carrier/thule-force-3-l-_-645750"],
  ["S2 Sport OEM Fog Light Replacement Kit, 2025–2026 4Runner, non-TRD Pro (Baja Designs)", "https://www.bajadesigns.com/products/s2-sport-oem-fog-light-replacement-kit-2025-on-toyota-4runner-note-non-trd-pro/"],
  ["Ditch Light Bracket Kit for 2025+ 4Runner (Cali Raised LED)", "https://caliraisedled.com/products/ditch-light-bracket-kit-for-2025-4runner"],
 ],
}
