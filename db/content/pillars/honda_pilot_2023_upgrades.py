"""Upgrades pillar: 2023–2026 Honda Pilot (4th gen; three-row midsize SUV, no bed).
Hub page: ranks the three published Pilot category guides and links to them. No product picks or ASINs here
(the site pulls each guide's #1 pick). Every price band comes from the linked guides' picks[].price fields or price
text in those guides (the Yakima TimberLine crossbar kit at The Rack Shop, $503.90 on sale, from the cargo box
guide); vehicle facts from db/migrations/003_vehicles.sql (SUV, roof_type raised-rails, roof load 165 lb and rails-by-trim attrs corrected to Honda's Info Center in the same commit,
hitch class 3 with a 2 in receiver, 5,000 lb, three rows, "5,000 lb AWD; 3,500 lb FWD", TrailSport variant), the
three guides and their sources, and six pages opened for this page on 2026-10-04: Honda Info Center's 2023 towing
page (3,500 lb 2WD, 5,000 lb AWD, TrailSport standard integrated Class III trailer hitch, premium unleaded
recommended above 3,500 lb, towing accessories installed at dealerships), Honda Info Center's 2023 roof rails page
(standard on Sport, TrailSport, Touring and Elite; up to 165 lb using accessory crossbars), Honda's 2023 Pilot press
kit (all-new chassis, wheelbase 2.8 in longer, length 3.4 in longer; removable middle seat on Touring and Elite
stored under the rear cargo floor; TrailSport with second-row captain's chairs, tow hitch, full-size spare, +1.0 in
ride height and all-season floor mats; captain's chairs available on EX-L; hands-free tailgate on Touring and
Elite), Honda's 2024 Pilot specifications sheet (8 seats on LX, Sport, EX-L, Touring, Elite; 7 seats with captain's
chairs on TrailSport and EX-L 7P; full-size spare on TrailSport only; 3,500 lb 2WD and 5,000 lb AWD; height 71.0 in,
72.0 in TrailSport), Honda's current Pilot page (shows the 2026 model, so the guides' 2023–2026 span is current;
trims Sport, EX-L, TrailSport, Touring, Touring Blackout, Elite, Black Edition; TrailSport with 2nd-row captain's
chairs, roof rails and an integrated Class III trailer hitch; stowable 2nd-row center seat on EX-L, Touring, Touring
Blackout, Elite and Black Edition) and Wikipedia's Honda Pilot page (LX dropped and Black Edition reintroduced for
2025; 2026 refresh). The Honda pages were read through a text extraction, so trim lists taken from the 2026 page are
worded "as we read".
Not verified, and worded as such in the text: Honda's tongue weight limit for the Pilot (no Honda page we read
states one); a roof load figure for bare-roof trims with a clamp kit (Honda's 165 lb is stated for the rails);
roof rails by trim for 2025–2026 beyond the Sport, TrailSport and Touring cards on Honda's 2026 page (two readings
of the Elite and Black Edition cards disagreed, so no claim is printed for them); whether the stowable middle seat
is on the Sport or LX; whether any liner set's second-row piece suits captain's chairs (no listing in the guide
names a layout); whether the floor pan is unchanged for 2026 from a Honda document; bar weight, spread and price of
the budget crossbars; a specific bare-roof clamp kit, its price and rating; SportRack Vista XL weight and load
rating; Rhino-Rack MasterFit 440L price; Honda's dealer hitch part number and price; whether Honda's height figure
includes the roof rails; hands-free tailgate trims after 2023; and 2026 fit of listings whose titles stop at 2025.
No Pilot guide exists for roof racks, running boards or lighting; none is ranked.
"""

KIND = "upgrades"
KEY = ("honda", "pilot", "2023-present")
CATEGORIES = ["floor-mats", "hitches", "cargo-boxes"]

TITLE = "2023–2026 Honda Pilot Upgrades, Ranked: 3 Mods in Order, With Roof Rail and Tow Rating Fit Traps"
META = ("Three 2023–2026 Honda Pilot upgrades in buying order: floor liners, trailer hitch and cargo box, with roof "
        "rail, second-row, 165 lb roof and tow rating checks.")

FAQ = [
 ("What should I upgrade first on a 2023–2026 Honda Pilot?",
  "Floor liners, then a trailer hitch, then a cargo box. Liners cost the least, about $100–$160 for the three-row "
  "sets in the floor liner guide, and need a 2023 or later listing and a full-width second-row piece. A hitch is "
  "second because a bolt-on receiver costs about $120–$300 and needs no other part first, unless you own a "
  "TrailSport, which already has one. The cargo box is last. It costs the most and needs crossbars first."),
 ("Do parts from a 2016–2022 Pilot fit the 2023 and newer Pilot?",
  "No. Honda's 2023 press kit calls the chassis all-new, with a wheelbase 2.8 in longer and a body 3.4 in longer "
  "than before. Part makers split their catalogs the same way. Husky's 18411 front liners are for the 2016–2022 "
  "Pilot, while its 12821 and 14821 rear liners start at 2023. CURT's 13146 hitch is for 2016–2022 and its 13472 "
  "is for 2023–2026."),
 ("Which 2023–2026 Pilot trims have roof rails, and can a cargo box go on an LX or EX-L?",
  "Honda's Info Center lists roof rails as standard on the Sport, TrailSport, Touring and Elite for 2023 and 2024. "
  "The LX and EX-L have a bare roof. A box goes on either roof once crossbars are fitted. Railed trims take a "
  "raised-rail kit. Bare-roof trims need a clamp kit that hooks into the door openings and is listed for the Pilot "
  "without rails; raised-rail bars will not mount."),
 ("How much weight can a 2023–2026 Pilot carry on the roof with a cargo box?",
  "Honda says up to 165 lb of cargo can be carried on the roof rails using accessory crossbars. That covers the "
  "bars, the box and the gear together. The boxes in the cargo box guide weigh 38.6 lb (Rhino-Rack MasterFit 440L) "
  "to 57.2 lb (Thule Motion 3 XXL), and the guide estimates roughly 90 to 120 lb left for gear once bars are on. Your owner's manual has the figure for your Pilot, and it "
  "wins over a crossbar listing that prints 300 lb."),
 ("Does my Honda Pilot already have a trailer hitch?",
  "Only the TrailSport has one from the factory. Honda's Info Center says the TrailSport comes standard with an "
  "integrated Class III trailer hitch. On the other trims, towing parts are dealer-installed accessories, so a used "
  "Pilot may or may not have a receiver. Look under the rear bumper for a square 2 in opening. If a receiver is there, an aftermarket trailer hitch adds nothing; buy a ball mount "
  "and check the wiring."),
 ("How much can a 2023–2026 Pilot tow, and does an aftermarket hitch raise it?",
  "A hitch never raises it. Honda rates the Pilot at 5,000 lb with all-wheel drive and 3,500 lb with two-wheel "
  "drive, and recommends premium unleaded fuel when towing more than 3,500 lb. Draw-Tite's 76453 and CURT's 13472 "
  "are both rated at 6,000 lb with 900 lb of tongue weight, so the vehicle is the limit. We could not confirm "
  "Honda's tongue weight limit for the Pilot from the Honda pages we read, so take that number from the owner's "
  "manual."),
 ("Which floor liners fit a Pilot with the removable middle seat or captain's chairs?",
  "The floor liner guide treats the cabin floor as the same across trims, so the question is coverage. With the "
  "stowable middle seat out, third-row passengers walk across the center of the second-row floor, so choose a "
  "second-row piece that runs the full width. Honda lists captain's chairs on the TrailSport and, in its 2024 "
  "specification sheet, on a seven-passenger EX-L. No listing recorded in the guide names a bench or captain's "
  "chairs, and we could not confirm the fit around captain's chairs, so ask the seller."),
 ("Will a hitch interfere with the hands-free power tailgate or the spare tire?",
  "It can. CURT's fit notes for its 13472 say Pilots with the hands-free liftgate need a factory sensor relocation "
  "kit. Honda's 2023 press kit lists that tailgate on the Touring and Elite. Draw-Tite lists its 76453 for the "
  "2023–2026 Pilot except with a full-size spare tire. Honda's 2024 specification sheet shows a full-size spare on "
  "the TrailSport only, and that trim already has a factory hitch."),
 ("Did the 2026 refresh change which Pilot accessories fit?",
  "The guides found no maker that split its parts at 2026. Wikipedia describes the 2026 update as a redesigned "
  "front fascia with a larger grille, a 10.2 in digital instrument cluster and a 12.3 in touchscreen. The hitch "
  "guide notes that the Draw-Tite and CURT hitches cover 2026 without a change. Other titles stop at 2025, including Smartliner's, MAXPRO's and Weize's liner "
  "sets and Husky's 14821."),
 ("How much does it cost to add all three upgrades to a Pilot?",
  "From the prices on the three guides' picks, a budget build runs about $670–$780: NIKALAIKA or Powerty liners, a "
  "maXpeedingrods hitch and SportRack's Vista XL. A mid build runs about $969–$1,089 with MAXPRO or Weize liners, "
  "an Autekcomma or DBXB-RV hitch and a Yakima CBX 16 or GrandTour 16. A premium build with Smartliner liners, "
  "Draw-Tite's 76453 and an INNO Wedge Plus or Thule Motion 3 XXL runs about $1,298–$1,780. All totals are before "
  "crossbars and wiring. TrailSport owners can subtract the hitch."),
]

ARTICLE = {
 "dek": "Three upgrades for the fourth-generation Pilot, in the order most owners should buy them. Fit on this "
        "three-row SUV turns on a short list of facts: a listing that starts at 2023, what the second row looks "
        "like, whether the roof has rails, front-wheel or all-wheel drive, and whether a receiver is already under "
        "the rear bumper.",
 "author": "jake-morrison",
 "reviewed": "2026-10-04",
 "method": "We did not install any of these parts ourselves. The order comes from the three fit-checked 2023–2026 "
           "Pilot guides on this site, weighing how many Pilots each upgrade suits, what it costs, what else it "
           "needs before it works and how much of its fit is confirmed for this generation. Price bands are the "
           "prices on those guides' picks, checked in September 2026, and are approximate. Vehicle facts come from "
           "this site's vehicle data, the guides' sources, Honda's Info Center, press kit, specification sheet and "
           "current Pilot page, which shows the 2026 model, and Wikipedia. Where we could not confirm a factory "
           "detail, the text says so.",
 "takeaways": [
  "**Buy 2023+ parts.** Honda calls the 2023 chassis all-new, and Husky and CURT sell separate part numbers for the 2016–2022 Pilot and for 2023 on.",
  "**Look at the second row.** A stowable middle seat leaves a walkway and the TrailSport has captain's chairs, so pick a second-row floor liner that runs the full width.",
  "**Look at the roof before pricing a cargo box.** Honda lists rails as standard on the Sport, TrailSport, Touring and Elite for 2023 and 2024; a bare-roof LX or EX-L needs a clamp kit.",
  "**165 lb covers bars, box and gear.** Honda quotes up to 165 lb on the rails with accessory crossbars, and the boxes in the guide weigh 38.6 to 57.2 lb.",
  "**Drivetrain sets the tow limit.** Honda rates the Pilot at 5,000 lb with AWD and 3,500 lb with 2WD, no hitch raises either, and the TrailSport already has a receiver.",
 ],
 "priority": [
  {"category": "floor-mats",
   "h": "1. Floor liners first: every Pilot can use them, and the second row is the main question",
   "why": "Floor liners lead on the Pilot because they cost the least, need no other part and suit every trim. Fit "
          "starts with the year. The 2023 Pilot has a new floor, and the floor liner guide shows Husky's 18411 "
          "front liners stopping at 2022 while its 12821, 50931 and 14821 rear pieces start at 2023. The second "
          "question is the second row. Some Pilots have a middle seat that lifts out and leaves a walkway to the "
          "third row, and the TrailSport has captain's chairs. Either way, pick a second-row piece that runs the "
          "full width. Prices in the guide run about $100–$150 for NIKALAIKA's or Powerty's three-row TPE sets, "
          "about $120–$160 for MAXPRO's three rows or Weize's five-piece set with cargo liners, and about "
          "$180–$230 for Smartliner's three rows plus cargo, which carries a limited lifetime warranty. The trade-off is "
          "documentation: the budget sets publish no warranty terms the guide could check, and several titles "
          "stop at 2025.",
   "skip_if": "The factory mats are holding up, the cabin stays dry and nobody climbs into the third row in muddy shoes."},
  {"category": "hitches",
   "h": "2. Trailer hitch second: a low-cost bolt-on receiver, unless you own a TrailSport",
   "why": "A trailer hitch ranks second because it costs less than any box on the roof, needs no other part before "
          "it carries a bike rack or a cargo carrier, and takes the heavy loads the roof can't. It is not first "
          "because one trim doesn't need it: Honda fits an integrated Class III hitch to every TrailSport. The "
          "hitch guide's default is Draw-Tite's 76453, a Class IV hitch with a 2 in receiver rated at 6,000 lb "
          "with 900 lb of tongue weight, at about $230–$300. Budget Class 3 hitches run about $150–$220 from Autekcomma and DBXB-RV, both patterned on CURT's 13472, and about $120–$180 from maXpeedingrods, with ratings that are the sellers' own. Three things decide fit: a listing that names the 2023–2026 Pilot, the hands-free "
          "tailgate sensor, which CURT says needs a factory relocation kit, and a full-size spare, which "
          "Draw-Tite excludes. The trade-off is wiring. A receiver without a harness carries bikes but lights no "
          "trailer.",
   "skip_if": "You own a TrailSport, or a square 2 in receiver is already under the rear bumper; buy a ball mount and check the wiring instead."},
  {"category": "cargo-boxes",
   "h": "3. Cargo box last: it needs crossbars first, and 165 lb has to cover everything",
   "why": "A cargo box comes last because it costs the most, can't go on until crossbars are fitted and changes "
          "where the Pilot can park. The box is universal and clamps to the bars, so the Pilot-specific part is "
          "the roof. Honda's Info Center lists roof rails as standard on the Sport, TrailSport, Touring and Elite "
          "for 2023 and 2024. The LX and EX-L have a bare roof and need a clamp kit. Honda quotes up to 165 lb on "
          "the rails with accessory crossbars, and that covers bars, box and gear. The boxes in the cargo box "
          "guide weigh 38.6 lb to 57.2 lb. Prices run about $450 for SportRack's Vista XL, about $699 for Yakima's "
          "CBX 16, about $709 for the GrandTour 16, about $888 for the INNO Wedge Plus and about $1,250 for "
          "Thule's Motion 3 XXL box alone. Crossbars are "
          "extra. The trade-offs are length against the power liftgate and height at the garage door.",
   "skip_if": "Your extra loads are heavy more than bulky, or the Pilot has to live behind a 7 ft garage door; a hitch cargo carrier suits both cases better."},
 ],
 "tier_table": {
  "caption": "Approximate price bands from the picks in the 2023–2026 Pilot guides (September 2026; Amazon prices move daily). Crossbars and trailer wiring are extra in every column",
  "head": ["Upgrade", "Budget", "Mid", "Premium"],
  "rows": [
   ["Floor liners", "About $100–$150 (NIKALAIKA or Powerty, three rows, listed for 2023–2026)", "About $120–$160 (MAXPRO three rows, or Weize five-piece with cargo liners; titles stop at 2025)", "About $180–$230 (Smartliner three rows plus cargo; title stops at 2025)"],
   ["Trailer hitch", "About $120–$180 (maXpeedingrods Class 3; rating per listing)", "About $150–$220 (Autekcomma or DBXB-RV, CURT 13472 pattern)", "About $230–$300 (Draw-Tite 76453, Class IV, 6,000 lb)"],
   ["Cargo box", "About $450 (SportRack Vista XL, rear opening)", "About $699 (Yakima CBX 16) to $709 (Yakima GrandTour 16)", "About $888 (INNO Wedge Plus) to $1,250 (Thule Motion 3 XXL, box alone)"],
   ["Crossbars (needed under any box)", "Not in the total. Budget bars for railed trims are priced on the listing", "Not in the total. Honda's accessory bars 08L04-T90-100 are not priced in the guide", "Not in the total. Yakima TimberLine kit, about $504 on sale at The Rack Shop for railed 2023–2025 Pilots"],
   ["Total", "About $670–$780 before crossbars and wiring", "About $969–$1,089 before crossbars and wiring", "About $1,298–$1,780 before crossbars and wiring"],
  ],
 },
 "sections": [
  {"h": "The second row: stowable middle seat, bench or captain's chairs",
   "body": "The fourth-generation Pilot has three rows, and its second row comes in more than one form. Honda's "
           "2023 press kit describes a removable middle seat on the Touring and Elite that stores under the rear "
           "cargo floor, so the same Pilot seats eight with it in place or seven with a walkway. Honda's 2024 "
           "specification sheet lists seven seats with captain's chairs on the TrailSport and on a "
           "seven-passenger EX-L. Don't go by the badge. Open the rear door and look.\n\n"
           "The floor liner guide treats the cabin floor as the same across trims, and says the removable seat "
           "changes how the second-row floor is used, not its shape. With the seat out, third-row passengers walk "
           "across the middle of that floor, so check the listing photos for a second-row piece that runs the "
           "full width.\n\n"
           "Captain's chairs are the open question. None of the listings recorded in the guide names a bench or "
           "captain's chairs, and we could not confirm that every set's second-row piece sits flat around them. "
           "Ask the seller before ordering for a TrailSport or a seven-passenger EX-L.",
   "table": {"caption": "2023–2026 Pilot second-row layouts and what the floor liner guide lists",
             "head": ["Layout or zone", "Where Honda lists it", "Seats", "Liner check"],
             "rows": [
              ["Bench with a removable, stowable middle seat", "Touring and Elite (2023 press kit); EX-L, Touring, Touring Blackout, Elite and Black Edition (2026 page, as we read it)", "8 with the seat in, 7 with it out", "A full-width second-row piece that covers the walkway"],
              ["Second-row bench, 40/20/40 split", "LX, Sport, EX-L, Touring and Elite (2024 specification sheet)", "8", "Any three-row set in the guide; confirm the year range"],
              ["Captain's chairs", "TrailSport (press kit, 2024 sheet, 2026 page); seven-passenger EX-L (2024 sheet)", "7", "No listing in the guide names this layout; ask the seller"],
              ["Third row and cargo area", "Every trim", "Same", "Smartliner covers both; MAXPRO, Powerty and NIKALAIKA include the third row but no cargo liner; Husky's 14821 is a third-row piece"],
             ]}},
  {"h": "Roof rails, crossbars and the 165 lb figure: what sits under a cargo box",
   "body": "There is no roof rack guide for the fourth-generation Pilot on this site, so a roof rack is not ranked "
           "here.\n\n"
           "**The rails.** Honda's Info Center lists roof rails as standard on the Sport, TrailSport, Touring and "
           "Elite for 2023 and 2024. The LX and EX-L come without them. As we read Honda's 2026 page, it lists "
           "roof rails on the Sport, TrailSport and Touring and not on the EX-L; we could not read every other "
           "trim reliably. For a Black Edition, a Touring Blackout or any 2025 or 2026 Pilot, look at the roof. "
           "Rails that run front to back take a raised-rail crossbar kit. A smooth roof takes a clamp kit that "
           "hooks into the door openings.\n\n"
           "**The crossbars.** The guide names three raised-rail "
           "routes: Honda's accessory crossbars, part 08L04-T90-100; a Yakima TimberLine kit that The Rack Shop "
           "lists for the railed 2023–2025 Pilot, rated at 165 lb, at about $504 on sale; and budget aluminum "
           "bars listed for the 2023–2026 Sport, TrailSport, Touring and Elite, priced on the listing. The guide "
           "names no specific clamp kit for bare-roof trims, so buy one listed for the Pilot without rails.\n\n"
           "**The roof figure.** Honda says up to 165 lb of cargo can be carried on the roof rails using "
           "accessory crossbars. This site's vehicle data records the same 165 lb, and the owner's manual "
           "has the number for your Pilot. The budget bars print 300 lb, which is a bar claim; the lowest number "
           "applies. We could not confirm a figure for a bare roof with a clamp kit.\n\n"
           "The table takes each box's weight off 165 lb. The guide's estimate is roughly "
           "90 to 120 lb for gear once bars are fitted.",
   "table": {"caption": "Boxes in the Pilot cargo box guide against Honda's 165 lb roof figure",
             "head": ["Box", "Volume and length", "Box weight", "Left of 165 lb before the bars", "Limit or fit note"],
             "rows": [
              ["Rhino-Rack MasterFit 440L", "15.5 cu ft, 76 in", "38.6 lb", "126.4 lb", "Box rated for 165 lb"],
              ["INNO Wedge Plus", "13 cu ft, 80 in", "44 lb", "121 lb", "Box cargo limit is 110 lb per etrailer, so 110 lb applies at most"],
              ["Yakima GrandTour 16", "16 cu ft, 79 in", "51.5 lb", "113.5 lb", "Bar spread 24–36 in"],
              ["Yakima CBX 16", "16 cu ft, 83 in", "57 lb", "108 lb", "Bar spread 24–35.5 in"],
              ["Thule Motion 3 XXL", "21 cu ft, 91.3 in", "57.2 lb", "107.8 lb", "Box rated for 165 lb; front clearance over 54 13/16 in"],
              ["SportRack Vista XL", "18 cu ft, 63 in", "Not published", "Ask the seller", "Mounts only at 25-7/8, 27-7/8 or 29-7/8 in"],
             ]}},
  {"h": "Towing: who already has a receiver, the rating by drivetrain and tongue weight",
   "body": "**The receiver.** This site's vehicle data records a Class III hitch with a 2 in receiver for this "
           "generation. That describes the TrailSport: Honda's Info Center says it comes standard with an "
           "integrated Class III trailer hitch, and the hitch guide notes that Honda mounts it behind the "
           "full-size spare. For other trims, Honda's Info Center says towing accessories are available for "
           "installation at dealerships, so a used Pilot may or may not have a receiver.\n\n"
           "**The rating.** Honda rates the Pilot at **5,000 lb with all-wheel drive and 3,500 lb with two-wheel "
           "drive**, and the vehicle data matches. Honda recommends premium unleaded fuel when towing more than "
           "3,500 lb.\n\n"
           "**What a bolt-on hitch changes.** It adds a receiver, not rating. Draw-Tite's Class IV 76453 and "
           "CURT's Class III 13472 are both rated at 6,000 lb, and the lower of hitch and vehicle applies. On a "
           "2WD Pilot that is 3,500 lb.\n\n"
           "**Tongue weight.** Both name-brand hitches are rated at 900 lb of tongue weight. We could not confirm "
           "Honda's own tongue weight limit for the Pilot from the Honda pages we read. It is in the owner's "
           "manual, and the lower figure applies.\n\n"
           "**Two fit catches.** CURT says Pilots with the hands-free liftgate need a factory sensor relocation "
           "kit with its 13472, and Honda's 2023 press kit lists that tailgate on the Touring and Elite. "
           "Draw-Tite excludes Pilots with a full-size spare; Honda's 2024 specification sheet lists one on the "
           "TrailSport only.\n\n"
           "**Wiring.** A hitch alone won't light a trailer. Plan on a 4-way flat connector at minimum, and a "
           "7-way connector with a brake controller for a trailer with electric brakes. Buy a harness that names "
           "the 2023+ Pilot."},
  {"h": "Roof or hitch: where the weight goes, the garage check and the order to fit things",
   "body": "- **The roof takes bulky, light loads.** Honda's 165 lb covers bars, box and gear, so a box suits "
           "duffels, sleeping bags and a stroller.\n"
           "- **The hitch takes heavy loads.** A hitch cargo carrier or platform bike rack loads the receiver, "
           "within the hitch's tongue rating and the limit in the owner's manual.\n\n"
           "**The garage check.** Honda's 2024 specification sheet lists the Pilot at 71.0 in tall on most trims "
           "and 72.0 in on the TrailSport. We could not confirm whether those figures include the roof rails. The "
           "boxes in the guide add 13-3/4 in (INNO Wedge Plus) to 19 in (SportRack Vista XL) above the bars. On a "
           "71 in Pilot that is 84.75 to 90 in before the crossbars are counted, and a 7 ft door opening is "
           "84 in. Measure the Pilot with bars fitted and add the box height.\n\n"
           "**The liftgate.** The boxes run from 63 in (Vista XL) to 91.3 in (Motion 3 XXL). Mount any box as far "
           "forward as the windshield allows, then open the liftgate slowly the first time.\n\n"
           "Fit the three in this order.\n\n"
           "1. **Floor liners.** Pull the factory mats, hook the driver liner onto Honda's retention posts and "
           "press each pedal to the floor.\n"
           "2. **Hitch.** Confirm there is no receiver, and get the sensor relocation kit if the Pilot has the "
           "hands-free tailgate. Draw-Tite quotes 40 minutes with no drilling for the 76453.\n"
           "3. **Crossbars, then the box.** Set the bar spread inside the box's range, lift the box on with a "
           "helper, slide it forward and check the liftgate before tightening."},
  {"h": "Model years and trims: the 2023 redesign, the 2026 refresh and where listings stop",
   "body": "**2016–2022 parts.** They don't carry over. Honda's 2023 press kit describes an all-new chassis with "
           "a wheelbase 2.8 in longer and an overall length 3.4 in longer than the old Pilot. The hitch guide "
           "says the 2023 Pilot shares its platform with the 2022 and later Acura MDX: CURT's 13472 and "
           "Draw-Tite's 76453 are listed for the 2023–2026 Pilot and the 2022–2026 MDX, while CURT's 13146 is for "
           "the 2016–2022 Pilot.\n\n"
           "**Trims that came and went.** Wikipedia says the LX was discontinued for 2025 and the Black Edition "
           "was reintroduced that year. Honda's 2026 page also shows a Touring Blackout. The budget crossbar "
           "listing in the cargo box guide names neither, so look at the roof and ask the seller.\n\n"
           "**The 2026 refresh.** Wikipedia describes a redesigned front fascia with a larger grille, a 10.2 in "
           "digital instrument cluster and a 12.3 in touchscreen. The hitch guide notes that the Draw-Tite and "
           "CURT hitches cover 2026 without a change. We could not confirm from a Honda document that the floor "
           "pan is unchanged, though Powerty and NIKALAIKA list their liners for 2023–2026 as one part.\n\n"
           "**Where listings stop.** Smartliner's, MAXPRO's and Weize's liner sets and Husky's "
           "14821 third-row liner stop at 2025. So do one budget hitch and The Rack Shop's Yakima crossbar kit. "
           "For anything short of your model year, ask the seller.\n\n"
           "**TrailSport.** Honda's 2023 press kit lists a tow hitch, a full-size spare, second-row captain's "
           "chairs, all-season floor mats and a ride height raised by 1.0 in as standard. So a TrailSport owner "
           "can skip the hitch and should check liner fit around the captain's chairs."},
 ],
 "avoid": [
  {"h": "2016–2022 Pilot listings, Passport liners and MDX-only hitch titles", "body": "Husky's 18411 liners and CURT's 13146 hitch are third-generation parts, the floor liner guide says the Passport has its own floor, and a hitch title that names only the MDX doesn't confirm Pilot fit."},
  {"h": "Raised-rail crossbars on a bare-roof LX or EX-L", "body": "A bare roof needs a clamp kit listed for the Pilot without rails. The budget bars in the cargo box guide exclude the LX and EX-L by name."},
  {"h": "Loading the roof to a bar's 300 lb claim", "body": "Honda quotes up to 165 lb on the rails with accessory crossbars, and bars, box and gear all count. A 57.2 lb Motion 3 XXL leaves 107.8 lb before the bars come off."},
  {"h": "A hitch for a TrailSport, or 5,000 lb behind a 2WD Pilot", "body": "The TrailSport already has an integrated Class III hitch. On other trims a 6,000 lb hitch doesn't change Honda's rating of 5,000 lb with AWD or 3,500 lb with 2WD."},
 ],
 "verdict": {
  "thesis": "On the 2023–2026 Pilot, buy floor liners with a full-width second-row piece first, add a trailer hitch second unless a TrailSport's factory receiver is already there, and buy a cargo box last, after crossbars matched to your roof and a load plan under 165 lb.",
  "body": "The fourth-generation Pilot is easy to accessorize once five facts are written down: model year, what "
          "the second row looks like, rails on the roof or not, AWD or 2WD, and receiver under the bumper or not. "
          "Floor liners need the first two and cost the least, so they go first. A trailer hitch needs the last "
          "two plus a look at the tailgate and the spare. It carries the heavy items "
          "that should stay off the roof.\n\n"
          "The cargo box sits last because its limits come from the Pilot and not from the box: rails on some "
          "trims and a bare roof on others, a 165 lb figure that has to cover bars, box and gear, and a body "
          "about 71 in tall before anything is added. A roof rack is not ranked here, but the right crossbars are the first purchase under any box. Owners of a 2016–2022 Pilot "
          "should treat this page as a list of questions, not part numbers.",
 },
 "sources": [
  ["Honda Pilot, 2026 model shown: trims, second-row seating, TrailSport hitch and roof rails (Honda)", "https://automobiles.honda.com/pilot"],
  ["2023 Pilot towing capacity: 3,500 lb 2WD, 5,000 lb AWD, TrailSport Class III hitch (Honda Info Center)", "https://www.hondainfocenter.com/2023/Pilot/Feature-Guide/Engine-Chassis-Features/Towing-Capacity/"],
  ["2023 Pilot roof rails: trims and 165 lb figure (Honda Info Center)", "https://www.hondainfocenter.com/2023/Pilot/Feature-Guide/Exterior-Features/Roof-Rails/"],
  ["2024 Pilot roof rails (Honda Info Center)", "https://www.hondainfocenter.com/2024/Pilot/Feature-Guide/Exterior-Features/Roof-Rails/"],
  ["2023 Honda Pilot Press Kit: all-new chassis, removable middle seat, TrailSport equipment (Honda)", "https://hondanews.com/en-US/honda-automobiles/releases/release-4e58b4e0fcd795affa5685a66a252ccf-2023-honda-pilot-press-kit"],
  ["2024 Honda Pilot Specifications & Features: seating, spare tire, towing, height (Honda)", "https://hondanews.com/en-US/honda-automobiles/releases/release-5003aaa39c009393f5d06d620f07211a-2024-honda-pilot-specifications-features"],
  ["Honda Pilot, fourth generation: trims by year, 2026 refresh (Wikipedia)", "https://en.wikipedia.org/wiki/Honda_Pilot"],
  ["Draw-Tite 76453 Class IV hitch (Draw-Tite)", "https://www.draw-tite.com/product/76453_class-iv-trailer-hitch"],
  ["CURT 13472 Class 3 hitch (CURT)", "https://www.curtmfg.com/part/13472"],
  ["Yakima TimberLine rack for 2023–2025 Pilot with raised rails (The Rack Shop)", "https://therackshop.com/2023-2025-honda-pilot-w-raised-rails-yakima-crossbar-complete-roof-rack/"],
  ["Honda Pilot cross bars 08L04-T90-100 (Honda Automotive Parts)", "https://www.hondaautomotiveparts.com/oem-parts/honda-cross-bars-8l04t90100"],
  ["Yakima GrandTour 16 (Yakima)", "https://yakima.com/products/grandtour-16"],
  ["Rhino-Rack MasterFit Roof Box 440L (Rhino-Rack)", "https://www.rhinorack.com/en-us/products/roof-racks/roof-boxes/roof-boxes/masterfit-roof-box-440l-black-_rmft440"],
  ["Thule Motion 3 XXL (Thule)", "https://www.thule.com/en-us/cargo-carrier/car-top-carrier/thule-motion-3-xxl-_-639950"],
  ["Husky Liners: WeatherBeater vs X-act Contour (Husky Liners)", "https://huskyliners.com/blog/husky-liners-weatherbeater-vs-xact-contour/"],
 ],
}
