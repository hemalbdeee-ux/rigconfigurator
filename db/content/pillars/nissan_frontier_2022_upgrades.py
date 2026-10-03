"""Upgrades pillar — 2022–2026 Nissan Frontier (3rd gen, D41).
Hub page: ranks the four published Frontier category guides and links to them. No product picks or ASINs here
(the site pulls each guide's #1 pick). Every price band comes from the linked guides' picks[].price fields;
vehicle facts from db/migrations/003_vehicles.sql (beds 60/73 in, Class III, 2 in receiver, 6,720 lb, Utili-track
optional, PRO-4X), the four guides and their sources, Wikipedia's Frontier (North America) page (1,610 lb payload and
6,720 lb towing at launch, 7,150 lb and the wider long-bed Crew Cab offer for 2025) and Nissan's 2025 Frontier press
kit (7,150 lb on a King Cab 4x2, a "Class IV receiver hitch member" that is not standard on every grade, and
Utili-track availability by grade). Checked 2026-10-03. The receiver-by-grade table could not be read reliably, so
the page prints no trim list for the hitch.
Not verified, and worded as such in the text: receiver and Utili-track availability for model years other than 2025
(the 2025 tables were read through a text extraction, so the page says "as we read"), which exact configurations sit
at which tow and payload figure, bracket fit of cross-generation running board listings on the 2022+ body, and
whether the universal racks' track kits match Utili-track. Nissan's brochure URL cited in the guides now shows the
2027 Frontier and no longer mentions Utili-track, so it is not cited here.
"""

KIND = "upgrades"
KEY = ("nissan", "frontier", "2022-present")
CATEGORIES = ["floor-mats", "tonneau-covers", "running-boards", "bed-racks"]

TITLE = "2022–2026 Nissan Frontier Upgrades, Ranked: 4 Mods in Order, With Utili-track and Cab Fit Traps"
META = ("Four 2022+ Frontier upgrades in buying order: floor liners, tonneau cover, running boards and bed rack, "
        "with Utili-track, King Cab, bed length and price notes.")

FAQ = [
 ("What should I upgrade first on a 2022–2026 Frontier?",
  "Floor liners, then a tonneau cover. Liners cost the least, about $80–$160 in our guide, and they need two facts "
  "from you: Crew Cab or King Cab, and what sits under the rear seat cushion, which can be a Fender speaker "
  "enclosure, a storage bin or plain carpet. The cover comes second because a 5 ft or 6 ft bed is small enough that "
  "keeping it dry and out of sight matters every day. Running boards follow for the step-in height. The bed rack "
  "comes last, but decide on it before you pay for the cover, since only some covers accept crossbars. On a tight "
  "budget, a budget TPE liner set and Tyger's T3 soft cover at about $223 come to about $300–$345."),
 ("Do I need to buy a trailer hitch for a 2022+ Frontier?",
  "Maybe not. Look under the rear bumper and read the window sticker first. Our vehicle data lists a Class III hitch "
  "with a 2 in receiver for this generation. Nissan's 2025 specifications call the factory part a Class IV receiver "
  "hitch and list it as standard on some grades and optional or not offered on others. We could not map that table "
  "to every cab and drivetrain with confidence, so we don't print a trim list. Some trucks have a receiver and some "
  "don't. If yours has one, an aftermarket trailer hitch adds nothing."),
 ("How much can the Frontier tow, and do these upgrades change it?",
  "Our vehicle data lists a maximum of 6,720 lb when properly equipped, the figure Wikipedia says Nissan gave the "
  "truck at launch. Our guides and Nissan's 2025 release put the maximum at up to 7,150 lb from the 2025 model year. "
  "Both are ceilings. Nissan's 2025 specifications show the top figure on a King Cab 4x2, with Crew Cab and 4x4 "
  "trucks rated lower, so the maximum varies by cab, drivetrain and model year. Your number is on the door-jamb "
  "label and in the owner's manual. None of the four upgrades changes it, but a rack, a tent and a hard cover count "
  "against payload, as does tongue weight."),
 ("What is Utili-track, and how do I tell if my Frontier has it?",
  "Utili-track is Nissan's bed channel system for sliding tie-down cleats. Look in the bed for metal channels with "
  "cleats that slide and lock along them. As we read Nissan's 2025 equipment tables, the system comes with two "
  "adjustable cleats and is standard on the Crew Cab SL, optional on the SV and PRO grades and not offered on the S. "
  "Other years and packages may differ, so check the bed, not the badge. It matters twice: the channels sit where "
  "clamp-on covers attach, and they run where most clamp racks grip."),
 ("Can I run a tonneau cover and a bed rack together on a Frontier?",
  "Yes, if you plan them as a pair. Our guides document three routes. A cover with T-slot rails takes crossbars "
  "directly: the RetraxPRO XR, about $2,000, and BAK's MX4 TS are both sold for the 2022+ Frontier. Yakima's "
  "OverHaul HD and OutPost HD towers need Yakima's Tonneau Kit 1 for select covers. The BackRack Original combo "
  "pairs frame 15034 with the 50500 tonneau hardware kit for the 2022–2025 Frontier, though that is a headache rack "
  "and won't carry a tent. Many budget clamp racks say nothing about covers, so ask the seller before buying both."),
 ("Do parts from a 2005–2021 Frontier fit the 2022+ truck?",
  "Don't assume it. The 2022 truck kept a revised version of the old frame but got a new body, interior and bed. "
  "Cover makers show the change in their catalogs: Retrax, BAK and Tyger list the old bed at 4 ft 11 in (58.6 in) "
  "and the new one at 5 ft, with separate part numbers such as BAK's 448506 and 448538. Floor liners must start at "
  "2022 because the interior is new. Running boards are the grey area. Most listings span 2005 to 2025 as one part, "
  "but Westin sells a separate mount kit, 27-2435, for the 2022 truck, which suggests the mounting changed."),
 ("I have a King Cab. What changes on this list?",
  "Three of the four upgrades. The King Cab has the 6 ft bed only, so order 6 ft covers: our guide names the BAKFlip "
  "MX4 448539, the RetraxPRO MX 80732 and the Tyger T3 TG-BC3N1058. For floor liners, every full set in our guide "
  "is cut for the Crew Cab; Husky's X-act Contour 51901 front pair is listed for both cabs, and the rear needs a "
  "King Cab-specific piece. Every running board pick is a Crew Cab part, and the King Cab's small rear-hinged doors "
  "need shorter boards. The bed rack changes least, because clamp towers such as Yakima's fit either bed."),
 ("How much does it cost to add all four upgrades to a Frontier?",
  "From the prices on our four guides' picks, a budget build runs about $660–$800: a budget TPE liner set, Tyger's "
  "T3 soft cover, two-step rails or a basic board, and a BackRack headache rack frame before its hardware kit. A "
  "mid build runs about $1,400–$1,840 with Rough Country or WeatherTech mats, a TruXedo Pro X15 or UnderCover "
  "Select cover, drop steps and Thule's Xsporter Pro Low. A premium build with Smartliner liners, a hard cover from "
  "the BAKFlip MX4 to the RetraxPRO XR, Go Rhino's RB30 Slim and Yakima towers runs about $2,370–$3,880 before "
  "crossbars. All figures are approximate."),
 ("Does a PRO-4X need different parts?",
  "Mostly no. Our tonneau guide notes that covers are listed by model year and bed length, not by S, SV, SL or "
  "PRO-4X, and our running board guide notes the PRO-4X shares the Crew Cab body. Three things do change the "
  "choices. Fender premium audio is common on the PRO-4X and SL, and its under-seat speaker rules out some rear "
  "liners. Clearance matters on the off-road trim, so slim boards or rock sliders suit it better than drop steps. "
  "And Utili-track is optional on the PRO grades in Nissan's 2025 tables, so look in the bed before ordering a "
  "cover or a rack."),
 ("Did the 2025 refresh change which accessories fit?",
  "Our guides found no maker that split its parts at 2025. RealTruck lists the cover part numbers in our tonneau "
  "guide for 2022–2026, and Smartliner's and Binmotor's liner sets are listed for 2022–2026 too. Wikipedia "
  "describes the 2025 update as a revised front fascia, a 12.3 in touchscreen, a telescoping steering wheel, a "
  "7,150 lb maximum tow rating and a long-bed Crew Cab offered on SV, PRO-4X and SL. More Crew Cabs now have the "
  "6 ft bed, so measure before ordering a cover. Several Amazon titles stop at 2024 or 2025, including Go Rhino's "
  "RB30 Slim and the TruXedo Pro X15, so confirm later years with the seller."),
]

ARTICLE = {
 "dek": "Four upgrades for the third-generation Frontier, in the order most owners should buy them. On this truck the "
        "order is shaped by two cabs and two beds, by Utili-track channels that give racks a place to mount and give "
        "clamp-on covers something to work around, and by listings that still blur the 2005–2021 truck with the 2022 "
        "redesign.",
 "author": "jake-morrison",
 "reviewed": "2026-10-03",
 "method": "We did not install any of these parts ourselves. The order comes from our four fit-checked 2022–2026 "
           "Frontier guides, weighing how many trucks each upgrade suits, what it costs, how often it's used and how "
           "much of its fit is confirmed for this generation (cab, bed length, Utili-track, model year). Price bands "
           "are the prices listed on those guides' picks, checked at maker and retailer stores in September 2026, and "
           "are approximate. Vehicle facts come from our vehicle data, the guides' sources, Wikipedia's Frontier page "
           "and Nissan's 2025 press kit. Where we couldn't confirm a factory detail, the text says so.",
 "takeaways": [
  "**Buy 2022+ parts.** Cover makers list the old bed at 4 ft 11 in and the new one at 5 ft, and most running board listings span both generations.",
  "**Cab decides the cabin parts, bed decides the bed parts.** Crew Cab has the 5 ft or 6 ft bed; King Cab has the 6 ft bed only.",
  "**Look for Utili-track before any bed purchase.** Its channels sit where clamp-on covers attach and where clamp racks grip.",
  "**Lift the rear seat cushion.** A Fender speaker box, a storage bin or plain carpet decides which rear floor liner sits flat.",
  "**Check for a receiver before shopping for a hitch.** Our data lists a 2 in receiver, but Nissan's 2025 specs show it isn't on every grade.",
 ],
 "priority": [
  {"category": "floor-mats",
   "h": "1. Floor liners first: one look under the rear seat, and the lowest price on the page",
   "why": "Floor liners lead on the Frontier because they cost the least and protect the part of the truck you use on "
          "every drive. The 2022 redesign brought a new body and interior, so buy listings that start at 2022. Two "
          "facts decide fit. The first is cab. Every full set in our guide is cut for the Crew Cab; the King Cab's "
          "short rear area takes its own rear piece, and Husky's X-act Contour 51901 front pair is the one part "
          "listed for both cabs. The second is what sits under the rear seat cushion: a Fender audio speaker "
          "enclosure, a storage bin or plain carpet. LUMWAY and Binmotor say their sets are not for the under-seat "
          "speaker, and Powerty cuts its set for trucks with the storage bin. Prices in our guide run about $80–$120 "
          "for Binmotor's or Powerty's budget TPE, about $90–$130 for Rough Country's mats, about $100–$150 for "
          "WeatherTech's W608 and W610 all-weather mats and about $120–$160 for Smartliner's one-piece TPE set, "
          "which carries a limited lifetime warranty. The trade-off is mats against liners: mats lift out easily but "
          "hold less slush. There's no clutch-pedal version to match, since the 2022+ US Frontier is automatic only.",
   "skip_if": "You drive in a dry climate, keep the cab clean and are content with the factory mats."},
  {"category": "tonneau-covers",
   "h": "2. Tonneau cover second: buy by bed length, then by what the listing says about Utili-track",
   "why": "A tonneau cover ranks second because the Frontier's bed is small, so keeping all of it dry and out of "
          "sight matters more than on a full-size truck. Three checks decide fit. First, "
          "buy a 2022+ part: Retrax, BAK and Tyger list the 2005–2021 bed at 4 ft 11 in (58.6 in) and the new one "
          "at 5 ft, under separate part numbers. Second, bed length. Crew Cabs have the 5 ft bed or the 6 ft long "
          "bed, the King Cab has the 6 ft bed, and the 5 ft bed has the most choice. Third, Utili-track. Its "
          "channels sit where clamp-on covers attach, so pick a listing that says it fits with or without the "
          "system. The UnderCover Select, Extang Endure ALX, RetraxPRO XR and Tyger T3 all say so; BAK's 5 ft MX4 "
          "listings disagree, so confirm that one. Prices in our guide run about $223 for the Tyger T3, about $550 "
          "for the TruXedo Pro X15, about $850 for the UnderCover Select, about $1,050 for the BAKFlip MX4, about "
          "$1,350 for the Endure ALX and about $2,000 for the RetraxPRO XR. Hard covers carry 300–500 lb spread "
          "evenly and lock under a locked tailgate; soft covers do neither. If a rack is likely, read slot four "
          "before paying.",
   "skip_if": "You haul tall loads most days and would spend more time removing the cover than using it."},
  {"category": "running-boards",
   "h": "3. Running boards third: a useful step, once the seller confirms the brackets",
   "why": "Running boards rank third because the Frontier's step-in height is noticeable, most of all on the "
          "PRO-4X, and a step helps every passenger on every trip. They don't rank higher because this is the "
          "category with the weakest fit data. Almost every Frontier board on Amazon lists 2005 through 2025 or 2026 "
          "as one part. The 2022 truck got a new body, and Westin sells a separate mount kit, 27-2435, for the 2022 "
          "Crew Cab and King Cab, which suggests the mounting changed. So the first job is a message to the seller, "
          "asking whether the included brackets fit the 2022+ body without drilling. Every pick in our guide is a "
          "Crew Cab part; the King Cab's small rear-hinged doors need shorter boards. Prices run about $120–$220 for "
          "two-step rails, a 3 in stainless tube or a 6 in board, about $160–$240 for drop steps from TAC, TIEZFUL "
          "and SMANOW, and about $400–$520 for Go Rhino's RB30 Slim. RealTruck describes the RB30 line as galvanized "
          "16-gauge steel rated at 600 lb per side with a limited lifetime structural warranty, the only published "
          "load and warranty figures in the group. The cost of any board is side clearance, and drop steps hang "
          "lowest.",
   "skip_if": "Your PRO-4X sees rocks, where sliders protect the rocker better than any board, or nobody struggles to climb in."},
  {"category": "bed-racks",
   "h": "4. Bed rack last: decide it early, buy it when you need it",
   "why": "The bed rack comes last because the fewest owners need one, it costs the most and it uses the most "
          "payload. Few brand-name overland racks name the 2022+ Frontier, so the strongest picks in our guide are "
          "Yakima's universal clamp towers, which carry a confirm note. The OutPost HD is fixed at 13 in and costs "
          "about $799 for the towers; the OverHaul HD adjusts from 19 to 30 in and costs about $1,200. Yakima rates "
          "both at 500 lb on-road and 300 lb off-road, and crossbars are extra. Thule's Xsporter Pro Low, about "
          "$600, carries 220 lb below the cab, which suits boats and bikes but not a tent with people in it. The "
          "BackRack Original, from about $240 for the frame, is a headache rack listed for the 2022–2025 Frontier. "
          "Two things on this truck decide fit. Clamp towers fit either bed, while fixed frames need the 5 ft or 6 "
          "ft version. And Utili-track runs along the rails where clamps grip, so a rack either mounts into the "
          "track with the right hardware or clamps clear of it; Yakima says tracked beds need its Track Kit 1 or 2. "
          "If you camp from the truck, move this slot up to second and choose the cover around the rack.",
   "skip_if": "Your loads fit under a cover and you don't carry boats, ladders or a tent."},
 ],
 "tier_table": {
  "caption": "Approximate price bands from the picks in our 2022–2026 Frontier guides (September 2026; Amazon prices move daily)",
  "head": ["Upgrade", "Budget", "Mid", "Premium"],
  "rows": [
   ["Floor liners", "About $80–$120 (Binmotor or Powerty TPE)", "About $90–$150 (Rough Country mats, WeatherTech W608/W610 mats)", "About $120–$160 (Smartliner one-piece TPE)"],
   ["Tonneau cover", "About $223 (Tyger T3 soft tri-fold)", "About $550 (TruXedo Pro X15) to $850 (UnderCover Select hard fold)", "About $1,050 (BAKFlip MX4), $1,350 (Extang Endure ALX) or $2,000 (RetraxPRO XR)"],
   ["Running boards", "About $120–$220 (two-step rails, 3 in stainless tube, 6 in board)", "About $160–$240 (TAC, TIEZFUL or SMANOW drop steps)", "About $400–$520 (Go Rhino RB30 Slim)"],
   ["Bed rack", "From about $240 (BackRack Original frame, hardware kit extra; headache rack). YZONA's clamp rack is priced on the listing", "About $600 (Thule Xsporter Pro Low, 220 lb)", "About $799 (Yakima OutPost HD towers) to $1,200 (OverHaul HD towers); crossbars extra"],
   ["Total", "About $660–$800", "About $1,400–$1,840", "About $2,370–$3,880 before crossbars"],
  ],
 },
 "sections": [
  {"h": "Towing: check for a receiver before you shop for a hitch",
   "body": "There is no trailer hitch guide for the 2022+ Frontier on this site, so here is what the truck may "
           "already have.\n\n"
           "**The receiver.** Our vehicle data lists a **Class III hitch with a 2 in receiver** for this generation. "
           "Nissan's 2025 specifications name the factory part a Class IV receiver hitch and list it as standard on "
           "some grades and optional or not offered on others. We could not map that equipment table to every cab "
           "and drivetrain with confidence, and we haven't read it for every model year, so don't go by trim name. "
           "Look under the rear bumper and check your window sticker. If a receiver is there, an aftermarket "
           "trailer hitch adds nothing.\n\n"
           "**The rating.** Our vehicle data lists a maximum of **6,720 lb when properly equipped**, which is the "
           "figure Wikipedia says Nissan gave the truck at launch. Our guides and Nissan's 2025 release put the "
           "maximum at up to 7,150 lb from the 2025 model year. The maximum varies by cab, drivetrain and model "
           "year. Nissan's 2025 tables show the top figure on a King Cab 4x2, with Crew Cab and 4x4 trucks rated "
           "lower. Your figure is on the door-jamb label and in the owner's manual, and a receiver never raises it.\n\n"
           "If your truck has no receiver and only a ball mount hole in the bumper, read the owner's manual for what that bumper is rated "
           "to pull before you use it. Tongue weight counts against payload along with everything else on this "
           "page, which is the subject of the last section."},
  {"h": "Utili-track: what it gives a rack and what it asks of a cover",
   "body": "Utili-track is the Frontier's bed channel system. Our guides cite Nissan describing three available "
           "channels on the current truck, and Nissan's 2025 specifications list the system with two adjustable "
           "tie-down cleats. As we read those 2025 tables, it is standard on the Crew Cab SL, optional on the SV "
           "and PRO grades, optional on the King Cab SV and not offered on the S. Our vehicle data calls it optional. "
           "Look in your own bed and note where the cleats sit.\n\n"
           "For a bed rack, the channels can be an advantage. Our bed rack guide describes two routes: a rack can "
           "mount into the track with the right hardware, which spreads the load along the channel, or it can clamp "
           "where the track isn't in the way. For a clamp-on tonneau cover, the channels are something the fitment "
           "has to account for, because they sit where the clamps attach.",
   "table": {"caption": "What the parts in our Frontier guides say about Utili-track",
             "head": ["Part", "What the listing or maker says", "What to do"],
             "rows": [
              ["UnderCover Select SL54020", "Fits with or without Utili-track", "Order by bed length"],
              ["Extang Endure ALX 80961", "Works with or without the Utili-track system (RealTruck)", "Order by bed length"],
              ["RetraxPRO XR T-80731", "Crew Cab 5 ft bed, with or without Utilitrack", "Order by bed length"],
              ["Tyger T3 TG-BC3N1057", "Fits models with or without the utility track system", "Order; over-rail bedliners need holes cut for the clamps"],
              ["BAKFlip MX4 448538 (5 ft)", "Amazon listings have appeared both ways", "Confirm with the seller; the 6 ft 448539 and MX4 TS 449538TS are titled with or without"],
              ["TruXedo Pro X15 1492501", "RealTruck's summary doesn't mention it", "Ask before ordering"],
              ["Yakima OverHaul HD and OutPost HD", "Tracked beds need Track Kit 1 or 2; the page doesn't name Utili-track", "Confirm the kit in Yakima's fit lookup"],
              ["Thule Xsporter Pro Low", "Universal brackets grip the rails, where the channels run", "Check Thule's fit guide"],
              ["YZONA clamp rack", "Utili-track and cover fit not stated", "Ask the seller how the clamps sit"],
             ]}},
  {"h": "King Cab or Crew Cab, 5 ft or 6 ft bed",
   "body": "Cab decides floor liners and running boards. Bed length decides the cover and, for fixed-frame racks, "
           "the rack. The cab doesn't always tell you the bed. The King Cab has the 6 ft bed only, but a Crew Cab can have either, and "
           "Wikipedia says the 2025 update made the long-wheelbase Crew Cab with the 6 ft bed available on SV, "
           "PRO-4X and SL trims. Our vehicle data rounds the beds to 60 and 73 in. Cover listings print the short "
           "bed as 59.5 or 60 in and the long bed as 72.25 to 73.3 in, depending on where the maker measures. If "
           "you're unsure, measure inside the bed at the rail from the bulkhead to the closed tailgate.",
   "table": {"caption": "2022–2026 Frontier cab and bed combinations",
             "head": ["Cab / bed", "Covers and racks", "Liners and boards", "Notes"],
             "rows": [
              ["Crew Cab, 5 ft (listed as 59.5–60 in)", "Most cover choices; the RetraxPRO XR in our guide is this bed only", "Every full liner set and every running board pick in our guides", "The 2005–2021 bed is listed at 4 ft 11 in (58.6 in)"],
              ["Crew Cab, 6 ft long bed (72.25–73.3 in)", "6 ft parts: BAKFlip MX4 448539, RetraxPRO MX 80732, Tyger T3 TG-BC3N1058", "Same Crew Cab liners and boards", "On more grades from 2025 (Wikipedia); order the cover by bed, not cab"],
              ["King Cab, 6 ft", "Same 6 ft covers; clamp towers fit, fixed-frame racks need the 6 ft version", "Husky 51901 front pair plus a King Cab rear; boards must name the King Cab, and none in our guide do", "Small rear-hinged doors and a short rear area"],
             ]}},
  {"h": "Choose the cover and the rack together, then install in this order",
   "body": "The bed rack is last on the buying list and first on the deciding list, because the rack you want can "
           "rule out the tonneau cover you were about to buy. The pairings our guides could document:\n\n"
           "- **Railed cover:** the RetraxPRO XR (T-80731, about $2,000) has integrated T-slot rails and a 500 lb "
           "rating. BAK's MX4 TS (449538TS) adds T-slot rails to the MX4; our tonneau guide found it at $1,249.99 "
           "on RealTruck. Crossbars are sold separately for both.\n"
           "- **Tower rack over a cover:** Yakima says its OverHaul HD and OutPost HD towers need Tonneau Kit 1 for "
           "select covers.\n"
           "- **Headache rack with a cover:** BackRack's combo pairs the 15034 frame with the 50500 tonneau hardware "
           "kit for the 2022–2025 Frontier. For an open bed the frame takes the 30500 kit instead.\n"
           "- **Occasional rack use:** a soft tri-fold such as the Tyger T3, about $223, lifts off quickly when the "
           "rack has to go on.\n\n"
           "Utili-track changes both halves of the pair. The cover has to state that it fits with the channels, and "
           "the rack needs the maker's track kit or clamps that sit clear of them. A cover's clamps and a rack's "
           "feet work along the same strip of bed rail, so ask both makers before you buy the second part.\n\n"
           "Then fit things in this order. Floor liners go in first. The cover goes on next, since our bed rack "
           "guide says to fit the cover before the rack. Slide the Utili-track cleats clear of the clamp points, or "
           "fit the track kit the rack maker specifies, then square the rack and torque it to spec. Running boards "
           "can go on whenever the seller has confirmed the 2022+ brackets."},
  {"h": "Payload: the mid-size limit on racks, rooftop tents and trailers",
   "body": "A mid-size truck runs out of payload before a good rack runs out of capacity. Wikipedia says Nissan rated the Frontier at up to **1,610 lb** of payload at launch. That is a "
           "best-case number. Nissan's 2025 tables put the highest payload on a King Cab 4x2 and rate Crew Cab and "
           "4x4 trucks lower, so the figure that counts is the one printed on your door-jamb label.\n\n"
           "Everything comes out of that one figure:\n\n"
           "- **The rack itself.** Yakima lists the OverHaul HD towers at 59.52 lb and the OutPost HD towers at "
           "44.09 lb, before crossbars.\n"
           "- **The tent, bedding and gear.** Use the weights on their own labels.\n"
           "- **The cover.** Tyger lists the soft T3 at 30.73 lb; check the maker's page for a hard cover.\n"
           "- **Passengers, and tongue weight** if a trailer is hooked up.\n\n"
           "Then read the rack's rating the right way. Yakima's towers are rated at **500 lb on-road and 300 lb "
           "off-road**, and the moving figure is the one that limits a tent, not the parked one. Thule's Xsporter "
           "Pro Low is rated at 220 lb. Treat a budget listing with no published rating, such as the YZONA rack in "
           "our guide, as a rack for lights and light gear until the seller gives you a number.\n\n"
           "Cover ratings are a separate matter. The 500 lb on the Extang Endure ALX and RetraxPRO XR, 400 lb on the "
           "BAKFlip MX4 and 300 lb on the UnderCover Select are for flat, evenly spread loads. A tent or a bike "
           "mount needs a cover with T-slot rails and crossbars."},
 ],
 "avoid": [
  {"h": "Trusting a 2005–2025 year range", "body": "Cover makers sell separate parts for the old 4 ft 11 in bed and the new 5 ft bed, and most running board listings span both generations. Get 2022+ fit confirmed in writing."},
  {"h": "Ordering bed gear before looking for Utili-track", "body": "The channels sit where clamp-on covers attach and where clamp racks grip. Buy a cover listed with or without Utili-track, and ask the rack maker which track kit applies."},
  {"h": "Crew Cab parts on a King Cab, or a 5 ft cover on a 6 ft bed", "body": "Rear liners and running boards are cab-specific, and only Husky's 51901 front pair is listed for both cabs. Covers go by bed length, and a Crew Cab can have either bed."},
  {"h": "A tent on a rack or cover that isn't rated for it", "body": "Thule's Xsporter Pro Low is rated at 220 lb, soft covers have no rating, and hard cover ratings are for flat, evenly spread loads. Count everything against payload."},
 ],
 "verdict": {
  "thesis": "On the 2022–2026 Frontier, buy floor liners matched to cab and rear seat first and a tonneau cover matched to bed length and Utili-track second, add running boards once a seller confirms 2022+ brackets, and buy a bed rack only after choosing the cover around it.",
  "body": "The third-generation Frontier is an easy truck to accessorize once five facts are written down: cab, bed "
          "length, Utili-track or not, what sits under the rear seat, and model year. Floor liners need the cab and "
          "the rear seat answer and cost the least, so they go first. The tonneau cover needs the bed length and the "
          "Utili-track answer. Running "
          "boards earn third place on step-in height, with the caveat that our guide's picks are Crew Cab parts on "
          "cross-generation listings, so the seller's reply matters more than the title.\n\n"
          "The bed rack sits last because few owners need one and a mid-size payload limits what it can carry, but "
          "the rack decision still has to be made before the cover is paid for. Skip the hitch shopping until you "
          "have looked under the bumper. Owners of a 2005–2021 Frontier should treat this page as a list of "
          "questions, not part numbers, since cover makers split their catalogs at 2022. Each linked guide covers "
          "the fit details for its category.",
 },
 "sources": [
  ["Nissan Frontier (North America), third generation D41: cabs, beds, payload, towing, 2025 update (Wikipedia)", "https://en.wikipedia.org/wiki/Nissan_Frontier_(North_America)"],
  ["2025 Nissan Frontier press kit: specifications, towing, receiver hitch and Utili-track by grade (Nissan Newsroom)", "https://usa.nissannews.com/en-US/releases/2025-nissan-frontier-press-kit"],
  ["BAKFlip MX4 448538, 2022–2026 Frontier 5 ft bed (RealTruck)", "https://realtruck.com/p/bakflip-mx4-tonneau-cover/bak-448538/"],
  ["BAK MX4 TS 449538TS, T-slot rails (RealTruck)", "https://realtruck.com/p/bak-mx4-ts-tonneau-cover/bak-449538ts/"],
  ["Extang Endure ALX 80961, with or without Utili-track (RealTruck)", "https://realtruck.com/p/extang-endure-alx-tonneau-cover/ext-80961/"],
  ["UnderCover Select SL54020 (RealTruck)", "https://realtruck.com/p/undercover-select-tonneau-cover/udc-sl54020/"],
  ["RetraxPRO XR T-80731 for 2022+ Frontier (RealTruck)", "https://realtruck.com/p/retraxpro-xr-tonneau-cover/rtx-t-80731/"],
  ["Tyger T3 TG-BC3N1057, 2022–2026 Frontier 5 ft bed (Tyger Auto)", "https://www.tygerauto.com/tonneau-cover/tyger-t3-soft-trifold/tg-bc3n1057/tyger-t3-soft-tri-fold-fit-2022-2026-nissan-frontier-5-bed.html"],
  ["Yakima OverHaul HD towers (Yakima)", "https://yakima.com/products/overhaul-hd"],
  ["Yakima OutPost HD towers (Yakima)", "https://yakima.com/products/outpost-hd"],
  ["Thule Xsporter Pro Low Truck Rack (RealTruck)", "https://realtruck.com/p/thule-xsporter-pro-low-truck-rack/"],
  ["BackRack Original Headache Rack (RealTruck)", "https://realtruck.com/p/backrack-original-headache-rack/"],
  ["Go Rhino RB30 running boards (RealTruck)", "https://realtruck.com/p/go-rhino-rb30-running-boards/"],
  ["Husky Liners: WeatherBeater vs X-act Contour (Husky Liners)", "https://huskyliners.com/blog/husky-liners-weatherbeater-vs-xact-contour/"],
  ["SMARTLINER home page (SMARTLINER)", "https://www.smartliner-usa.com/"],
 ],
}
