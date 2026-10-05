"""Long-form article — Best Roof Racks / Crossbars for the 2023–2026 Honda CR-V (6th gen).
Mirrors the approved pilot (ford_f150_2021_tonneau.py) and the RAV4 / Highlander / Forester roof-rack pages.
No invented hands-on testing: vehicle facts come from Honda's 2024 and 2026 Specifications & Features releases
(hondanews.com), Wikipedia, etrailer's 2024 CR-V roof page and an etrailer expert answer, and Bernardi Parts' page for
Honda's accessory roof rails; product facts come from the Amazon listing titles recorded in FITS (found by amazon.com
search on 2026-10-05; amazon.com pages cannot be opened) plus the etrailer pages in SOURCES (read 2026-10-05).
Rail type: etrailer lists the railed 2024 CR-V as "Flush mounted rails that run front to back", so FITS uses
{"roof_type": "flush-rails"} for rail-mounted sets and {"roof_type": "bare"} for door-frame clamp sets.
No Thule, Yakima, INNO or Honda-genuine listing whose Amazon title names the 2023+ CR-V was found, so those systems
appear only as etrailer / dealer options in the text, not as picks.
Not verified, and worded as such: any Honda roof load figure for the bare roof or the hybrid trims' factory rails
(the 165 lb figure is printed for Honda's accessory rails only); bar ratings, materials, locks, weights, spread and
warranty for every Amazon set beyond what its title says; 2027 fit of any part.
"""

KEY = ("honda", "cr-v", "2023-present", "roof-racks")

TITLE = "Best Roof Racks & Crossbars for 2023–2026 Honda CR-V: 6 Picks for Bare Roofs and Hybrid Rails"
META = ("Six crossbar sets for the 6th-gen CR-V by roof: door-frame clamp bars for the gas LX, EX and EX-L, rail bars "
        "for the hybrids' flush rails, with load and fit notes.")

FAQ = [
 ("Does the 2023–2026 Honda CR-V have roof rails?",
  "Only the hybrid trims. Honda's 2024 and 2026 Specifications & Features tables list Black Roof Rails as standard on the Sport, Sport-L and Sport Touring (2024) and on the Sport, TrailSport, Sport-L and Sport Touring (2026), and not on the gas LX, EX and EX-L. Our cargo box guide read the 2023 table, which lists the rails on the Sport and Sport Touring, the two hybrids sold that year. We did not read the 2025 table. Look at your roof before you shop: a smooth roof needs door-frame clamp bars, and a roof with rails needs bars made for those rails."),
 ("Are the CR-V's roof rails raised or flush?",
  "Flush, according to etrailer. Its 2024 CR-V roof page lists the railed configuration as \"Flush mounted rails that run front to back,\" and an etrailer expert answering a 2024 CR-V owner whose rails \"sit flat\" recommended Yakima's SightLine towers, which are made for flush side rails. A flush rail has no gap underneath, so bars that wrap a clamp around a raised rail will not work. The budget Amazon sets here are titled for the CR-V's side rails; one title says \"Flush Side Rails\" outright. Check the foot in each listing's photos against your rail before you order."),
 ("What crossbars fit a gas CR-V LX, EX or EX-L with no rails?",
  "A door-frame clamp system. Its feet sit on the roof edge on rubber pads and hook into the door openings, with a fit kit shaped for the CR-V. etrailer lists the Thule WingBar Evo with Evo Clamp feet for the bare-roof 2024 CR-V at $704.85, the Yakima BaseLine with JetStream bars at $694.80 and an INNO Square Bar kit at $469.12. On Amazon, the Wonderdriver set is titled for the 2023–2026 CR-V EX, LX and EX-L, and the BRIGHTLINES set for the CR-V without roof rails. Honda's accessory roof rails, part 08L02-3A0-100, are the other route."),
 ("How much weight can the CR-V roof carry?",
  "We could not find a roof load figure in Honda's 2024 or 2026 specification tables, so your owner's manual is the authority. Two figures we did read: Bernardi Parts prints \"165 pounds total capacity DO NOT EXCEED!\" for Honda's accessory roof rails, and etrailer lists 165 lb for the Thule WingBar Evo and Yakima BaseLine kits. Both cover the crossbars, the accessory and the cargo together while driving. A 220 lb or 330 lb figure in an Amazon title is the seller's bar claim and does not raise the roof's limit. Load to the lowest number you can confirm."),
 ("Do the hybrid trims take the same crossbars as the gas trims?",
  "No. The roof differs by powertrain on this generation. Honda's tables put black roof rails on the hybrid Sport, Sport-L, Sport Touring and 2026 TrailSport, and none on the gas LX, EX and EX-L. So a hybrid takes rail-mounted bars such as the ANTS PART, HEKA or Snailfly sets, and a gas CR-V takes door-frame clamp bars such as the Wonderdriver set or a Thule or Yakima clamp kit. Several Amazon titles name \"CR-V Sport Hybrid\" for that reason. The one exception is a gas CR-V fitted with Honda's accessory rails, which then takes rail bars."),
 ("Do 2017–2022 CR-V crossbars fit the 2023 CR-V?",
  "Don't count on it. The sixth-generation CR-V, unveiled in July 2022 and sold in the U.S. from September 2022 as a 2023 model, has a new body on the Honda Architecture platform, and our fitment data flags that 2017–2022 racks do not carry over. Door-frame clamp kits use a vehicle-specific fit kit, so a 2017–2022 kit will not match the 2023+ door openings. Some Amazon listings stretch across generations; the BRIGHTLINES set here is titled 2012–2026, so confirm the 2023+ fit with the seller before you buy it."),
 ("Can I buy Honda's own crossbars for the CR-V?",
  "Yes, through a Honda dealer. Bernardi Parts lists Honda Crossbars, part 08L04-3A0-100, for the 2023–2027 CR-V at $250, sold separately from the roof rails (08L02-3A0-100, $435 list, $369.75 sale at the same dealer). The rails page prints a 165 lb total capacity. We could not find a listing on Amazon whose title names the 2023+ CR-V for the genuine crossbars, so they are not a pick here. If you own a hybrid with factory rails, ask the dealer to confirm by VIN that the accessory crossbars fit the factory rails before ordering."),
 ("Can I open the sunroof with crossbars installed?",
  "etrailer attaches the same note to every Thule kit it lists for the railed 2024 CR-V: \"The sunroof should not be opened while the rack is installed.\" A crossbar or an accessory can sit in the path of the glass panel as it slides back. Treat that as the rule for any rack on a CR-V with a moonroof, not only Thule's. Set the bars, close the glass, and leave it closed until the bars come off."),
 ("Which crossbars are quietest on a CR-V?",
  "Aero (teardrop) aluminum bars are quieter than square or round steel bars. etrailer's Thule WingBar Evo and Yakima JetStream bars are that shape, and so are most of the Amazon aluminum sets here, going by their titles. On the railed trims, a flush-rail kit sits inside the rails and keeps overhang short. Honda's own crossbars give the factory look. Whatever you buy, keep the end caps on, keep the bars inside the rails, and take them off between trips if the whistle bothers you."),
 ("How far apart should CR-V crossbars be?",
  "On the railed trims, bars slide along the rail, so set the spread to what your box, tent or carrier needs; cargo boxes publish a minimum and maximum, and our CR-V cargo box guide lists them. On a bare roof, a door-frame clamp kit fixes the spread at the door openings, so pick an accessory with a wide range. Keep the rear bar forward of the liftgate's swing, open the liftgate slowly the first time, and re-tighten after the first drive."),
]

ARTICLE = {
 "dek": "The sixth-generation CR-V has two roofs. Honda's tables put black roof rails on the hybrid Sport, Sport-L, Sport Touring and 2026 TrailSport, and none on the gas LX, EX and EX-L. Here are six crossbar sets matched to each: door-frame clamp bars for the bare gas roof, rail-mounted bars for the hybrids' flush rails, plus the Thule, Yakima and Honda options etrailer and a Honda dealer list, with the load, spread and sunroof details that decide which set you buy.",
 "author": "jake-morrison",
 "reviewed": "2026-10-05",
 "method": "We did not install these crossbars ourselves. We matched each set to the CR-V roof named in its Amazon listing title (bare roof or side rails) and checked the vehicle facts against Honda's 2024 and 2026 Specifications & Features releases, Wikipedia, etrailer's 2024 CR-V roof page and an etrailer expert answer, and a Honda parts dealer's page for the accessory roof rails. Amazon product pages cannot be opened by our tools, so where the only spec source is the listing title, we say so. Thule and Yakima specs and prices were read on etrailer in October 2026; Amazon prices move daily, so the button shows the live price.",
 "takeaways": [
  "**Roof type follows the powertrain.** Honda's 2024 and 2026 tables list black roof rails on the hybrid trims only; the gas LX, EX and EX-L have a bare roof. Look before you buy.",
  "**The rails are flush, not raised.** etrailer calls them flush mounted rails that run front to back. Raised-rail clamp bars do not fit; buy bars sold for the CR-V's side rails or a flush-rail kit.",
  "**A bare roof needs a door-frame clamp kit.** The Wonderdriver set is titled for the 2023–2026 EX, LX and EX-L; etrailer lists Thule and Yakima clamp kits at about $695–$705.",
  "**No Honda roof figure in the spec tables.** A Honda dealer prints 165 lb total for Honda's accessory rails, and etrailer rates the Thule and Yakima kits at 165 lb. Read your owner's manual; bars count toward the limit.",
  "**2017–2022 racks do not carry over.** Buy a listing that names 2023 or later, and confirm 2026 and 2027 if the title stops short.",
 ],
 "top_picks": [
  {"asin": "B0BX692P1F", "role": "Best overall (hybrid rails)", "why": "Titled for the 2023–2026 CR-V and CR-V Sport Hybrid with roof rails, covering the full generation"},
  {"asin": "B0CRR2R73W", "role": "Best for the bare roof (gas trims)", "why": "Titled for the 2023–2026 CR-V EX, LX and EX-L, the three trims without rails"},
  {"asin": "B0C58CT63V", "role": "Best stated rating", "why": "220 lb bar rating in the title, 2023–2026 with side rails"},
  {"asin": "B0HBB9N6RY", "role": "Best lockable (rails)", "why": "Anti-theft lock named in a title that says Flush Side Rails and 2023–2026 Hybrid"},
  {"asin": "B0BYSF7LBT", "role": "Best budget (rails)", "why": "Snailfly bars titled for the 2023–2025 CR-V Sport Hybrid with side rails"},
 ],
 "fit_table": {
  "caption": "2023–2026 CR-V roofs (the crossbar must match the roof, not the model year)",
  "head": ["Roof", "Trims", "Crossbars on this page", "Notes"],
  "rows": [
   ["Bare roof", "Gas LX, EX, EX-L (Honda 2024 and 2026 tables)", "Wonderdriver, BRIGHTLINES (door-frame clamp)", "Or Thule WingBar Evo clamp kit $704.85, Yakima BaseLine $694.80, INNO Square Bar $469.12 at etrailer"],
   ["Black roof rails (flush)", "Hybrid Sport, Sport Touring (2023), plus Sport-L (2024 on) and TrailSport (2026)", "ANTS PART, HEKA, Snailfly, lockable flush-rail set", "etrailer: flush mounted rails; Thule flush-rail kits $604.85–$809.80"],
   ["Honda accessory rails 08L02-3A0-100", "Any 2023–2027 CR-V, dealer-fitted", "Honda crossbars 08L04-3A0-100 ($250 at Bernardi) or rail bars", "Rails marked 165 lb total; $435 list"],
   ["2017–2022 CR-V", "Previous generation", "None", "Racks do not carry over"],
   ["2027 CR-V", "Honda's spec page now shows a 2027", "Confirm with the seller", "Not checked for the bars on this page"],
  ],
 },
 "look_for": [
  {"h": "Bare roof or flush rails: check the badge, then the roof",
   "body": "Honda split the sixth-generation CR-V's roof by powertrain. Its 2024 table lists Black Roof Rails as standard on the hybrid Sport, Sport-L and Sport Touring and not on the gas LX, EX and EX-L; the 2026 table adds the TrailSport Hybrid to the railed list. The 2023 table, read for our cargo box guide, puts the rails on that year's two hybrids, the Sport and Sport Touring. We did not read the 2025 table, so look at the roof: a smooth roof takes door-frame clamp bars, and rails take rail-mounted bars. The rails themselves are flush. etrailer's 2024 CR-V page calls them flush mounted rails that run front to back, with no gap underneath. That rules out the raised-rail clamp bars sold for a Forester or RAV4; the sets here are titled for the CR-V's side rails specifically."},
  {"h": "The roof limit, and why 220 lb bars don't change it",
   "body": "Neither the 2024 nor the 2026 Honda specification table prints a roof load figure, so the owner's manual is the authority. The numbers we could read are for hardware, not the roof: Bernardi Parts prints 165 lb total capacity for Honda's accessory roof rails, and etrailer lists 165 lb for the Thule WingBar Evo and Yakima BaseLine kits, with a note to follow the vehicle's own roof limit. Those figures cover the bars, the accessory and the cargo together while driving. Amazon titles here claim 200 lb, 220 lb and, on the Wonderdriver set, 330 lb. Those are bar strength claims. A stiffer bar flexes less under a cargo box; it does not let the CR-V carry more. Load to the lowest figure you can confirm, and weigh the bars and the box against it."},
  {"h": "Fixed spread on clamp kits, sliding spread on rails",
   "body": "The two roofs behave differently once the bars are on. A door-frame clamp kit on a gas CR-V puts its feet at the door openings, so the distance between the bars is set by the kit and the car, not by you. That makes the spread range of your cargo box or tent the thing to check before buying either part; the cargo box guide lists the ranges for the boxes we cover. On a hybrid with rails, the bars slide along the rail, so you set the spread to suit the accessory. On both roofs the rear limit is the liftgate: keep the rear bar forward of its swing, open it slowly the first time with the accessory mounted, and mark the rail with tape so the bars go back in the same place."},
  {"h": "Locks, noise and the sunroof",
   "body": "Only some sets lock. The Wonderdriver and BRIGHTLINES titles say anti-theft, and the flush-rail set from an unnamed seller names an anti-theft lock; the ANTS PART, HEKA and Snailfly titles do not mention locks, so check their listings. If the CR-V sits on the street or at trailheads, locks are worth the small difference, and lock the accessory too. For noise, aero aluminum bars beat square steel, and short overhang beats long. One more rule from etrailer's Thule fit data for the railed 2024 CR-V: the sunroof should not be opened while the rack is installed. Treat that as the rule for any rack on a CR-V with a moonroof."},
  {"h": "Name-brand kits and Honda's own parts",
   "body": "If you want a published fit guide and a lifetime warranty, etrailer lists complete kits for both CR-V roofs. For the bare roof: Thule WingBar Evo with Evo Clamp feet, two 53 in aluminum bars rated 165 lb, $704.85; Yakima BaseLine with 50 in JetStream bars, 165 lb, $694.80; INNO Square Bar, $469.12. For the flush rails: Thule WingBar Evo with Evo Flush Rail feet, 50 in bars, 165 lb, $704.85; SquareBar Evo $604.85; WingBar Edge $809.80. An etrailer expert priced a Yakima SightLine flush-rail setup at $694.85. Honda's route is accessory rails 08L02-3A0-100 ($435 list, $369.75 sale at Bernardi Parts) and crossbars 08L04-3A0-100 ($250). None of these has an Amazon listing titled for the 2023+ CR-V, so they are options, not picks."},
 ],
 "look_table": {
  "head": ["Feature", "Look for", "Avoid"],
  "rows": [
   ["Fitment", "Title naming the 2023+ CR-V and your roof: \"EX, LX, EX-L\" or \"without roof rails\" for gas, \"Sport Hybrid\" or \"with side rails\" for hybrids", "\"Universal\" bars, or a title that doesn't say which roof"],
   ["Rail type", "Feet made for flush side rails, or a flush-rail fit kit", "Raised-rail wrap-around clamps"],
   ["Load", "A stated bar rating, and your load under the owner's manual figure with the bars counted", "Loading to a 220 or 330 lb bar claim"],
   ["Security", "Anti-theft locks named in the title or listing", "Hex-key-only feet if you park in public"],
   ["Profile", "Aero aluminum bars, short overhang", "Long square steel bars on a daily driver"],
   ["Year range", "2023–2026, or the year you own", "Assuming 2026 fit from a title that stops at 2024 or 2025"],
  ],
 },
 "types_table": {
  "caption": "Roof-rack options on the 2023–2026 CR-V (etrailer and dealer prices read October 2026)",
  "head": ["Option", "Price guide", "Roof", "Rating (per maker/listing)", "Noise", "Best for"],
  "rows": [
   ["Budget door-frame clamp bars (Amazon)", "Check listing", "Bare roof (gas trims)", "330 lb bar claim (Wonderdriver title)", "Low to medium", "Gas LX, EX, EX-L owners on a budget"],
   ["Budget rail-mounted bars (Amazon)", "Check listing", "Flush rails (hybrid trims)", "200–220 lb bar claims", "Low to medium", "Hybrid owners carrying bags, bikes, kayaks"],
   ["Thule WingBar Evo clamp kit", "$704.85 (etrailer)", "Bare roof", "165 lb", "Low (aero)", "Fit guide, lifetime warranty, T-slot accessories"],
   ["Yakima BaseLine + JetStream", "$694.80 (etrailer)", "Bare roof", "165 lb", "Low (aero)", "Same, with Yakima accessories"],
   ["INNO Square Bar kit", "$469.12 (etrailer)", "Bare roof", "See etrailer", "Higher (square steel)", "Cheapest name-brand clamp kit"],
   ["Thule flush-rail kits (SquareBar Evo, WingBar Evo, WingBar Edge)", "$604.85–$809.80 (etrailer)", "Flush rails", "165 lb (WingBar Evo)", "Lowest (Edge)", "Hybrid owners who want the fit guide"],
   ["Honda rails 08L02-3A0-100 + crossbars 08L04-3A0-100", "$435 list rails, $250 crossbars (Bernardi Parts)", "Bare roof, dealer-fitted rails", "165 lb total (rails)", "Low", "Factory look on a gas CR-V"],
  ],
 },
 "picks": [
  {"asin": "B0BX692P1F", "role": "Best overall (hybrid rails)", "price": "Check listing",
   "pros": ["Title names the 2023–2026 CR-V and the CR-V Sport Hybrid", "Covers the whole generation so far", "Made for the roof rails the hybrid trims carry", "Lets a hybrid owner use standard clamp-style box and bike mounts", "Established Amazon seller for several Honda models"],
   "cons": ["Only for a CR-V with rails; a gas LX, EX or EX-L cannot use it", "Bar rating, locks and warranty are not in the title; read the listing", "No maker spec sheet we could open"],
   "body": "ANTS PART's set is the default for the railed CR-V because its title answers the two questions that matter: it names the 2023–2026 CR-V and the CR-V Sport Hybrid, and it is sold for the roof rails. That lines up with Honda's tables, which list black roof rails on the hybrid Sport, Sport-L, Sport Touring and 2026 TrailSport. Our cargo box guide carries the same listing with the note that it needs roof rails, so it is the natural match for any hybrid owner who wants bars before a box.\n\nWhat the title does not say, the listing must. There is no bar rating, no mention of locks and no warranty in the title, and Amazon pages cannot be opened by our tools, so read those three before ordering. The rails are flush per etrailer, with no gap underneath, so compare the foot in the listing photos with your rail. Whatever rating the seller claims, the CR-V's own roof limit applies and includes the bars; Honda prints no figure in its 2024 or 2026 tables, so take it from the owner's manual. Set the spread to your accessory, keep the rear bar clear of the liftgate, and re-tighten after the first drive.",
   "who": "Owners of hybrid Sport, Sport-L, Sport Touring and TrailSport CR-Vs who want bars titled for the whole generation.",
   "specs": [["Type", "Rail-mounted crossbars"], ["Fits (per title)", "2023–2026 CR-V and CR-V Sport Hybrid with roof rails"], ["Not for", "Bare-roof gas LX, EX, EX-L"], ["Rail type", "Flush rails (etrailer)"], ["Bar rating", "Not in title; see listing"], ["Lock", "Not in title; see listing"], ["Vehicle limit", "See owner's manual (no Honda figure in the 2024 or 2026 tables)"], ["Drilling", "None stated; confirm"]]},
  {"asin": "B0CRR2R73W", "role": "Best for the bare roof (gas trims)", "price": "Check listing",
   "pros": ["Title names the CR-V EX, LX and EX-L, the three trims without rails", "Covers 2023–2026", "Far cheaper than a Thule or Yakima clamp kit", "Listing describes aluminum bars with anti-theft locks", "The bars a gas CR-V needs before any box or bike mount"],
   "cons": ["330 lb in the listing is a bar claim, not the roof limit", "Door-frame clamp feet fix the spread; check your accessory's range", "Bar weight, spread and warranty not published on a page we could open"],
   "body": "A gas CR-V has nothing on the roof to clamp to, so it needs a kit whose feet sit on the roof edge and hook into the door openings. Wonderdriver's set is the budget version of that kit, and its title names the CR-V EX, LX and EX-L for 2023–2026, exactly the three trims Honda's tables list without roof rails. Our cargo box guide, which carries the same listing, notes that it describes heavy-duty aluminum bars with anti-theft locks and claims 330 lb. For a brand-name alternative, etrailer lists the Thule WingBar Evo clamp kit at $704.85 and the Yakima BaseLine at $694.80 for the bare-roof 2024 CR-V.\n\nTreat the numbers with care. The 330 lb figure is what the seller claims for the bars; Honda prints no roof figure in its tables, its accessory rails are marked 165 lb total, and the Thule and Yakima kits are rated 165 lb, so plan around the lowest limit you can confirm. The bigger practical point is spread. A clamp kit fixes the distance between the bars at the door openings, so measure the installed bars center to center before you buy a cargo box, and choose a box with a wide range. Confirm on the listing that you are ordering the bare-roof version, not Wonderdriver's other CR-V listing, whose title names the Sport Hybrid.",
   "who": "Gas LX, EX and EX-L owners who need bars for a bare roof and will not pay for a Thule or Yakima kit.",
   "specs": [["Type", "Door-frame clamp crossbars"], ["Fits (per title)", "2023–2026 CR-V EX, LX, EX-L"], ["Not for", "Hybrid trims with roof rails"], ["Material", "Aluminum (per listing)"], ["Lock", "Anti-theft (per listing)"], ["Listed load", "330 lb (seller's bar claim)"], ["Vehicle limit", "See owner's manual; Honda accessory rails 165 lb total"], ["Spread", "Fixed by the feet; measure before buying a box"]]},
  {"asin": "B0C58CT63V", "role": "Best stated rating", "price": "Check listing",
   "pros": ["220 lb bar rating in the title", "Title names the CR-V and CR-V Sport Hybrid, 2023–2026, with side rails", "Aluminum bars", "Covers the whole generation so far", "Title lists bikes, surfboards, kayaks and snowboards as intended loads"],
   "cons": ["220 lb is the bar's rating, not the CR-V's roof limit", "Locks not mentioned in the title", "Warranty from the seller only"],
   "body": "HEKA's set is the railed-roof pick for owners who want a number. The title states a 220 lb bar rating and names the CR-V and CR-V Sport Hybrid for 2023, 2024, 2025 and 2026 with side rails, which matches the hybrid trims Honda lists with black roof rails. It is aluminum, and the title pitches it for bikes, surfboards, kayaks and snowboards, the loads that put the most leverage on a bar. A stiffer bar flexes less under a kayak at highway speed, which is the real benefit of the rating.\n\nThe rating needs context. Honda prints no roof load figure in its 2024 or 2026 tables, its accessory rails are marked 165 lb total, and the Thule and Yakima kits etrailer lists for the CR-V are rated 165 lb. A 220 lb bar does not raise whatever your owner's manual says the roof can carry, and the bars themselves count toward it. The title does not mention locks, so check the listing if the car parks in public, and read the warranty terms there too. As with every rail set here, compare the foot with the CR-V's flush rail in the listing photos before ordering, and keep the rear bar clear of the liftgate.",
   "who": "Hybrid owners carrying kayaks or bikes who want a stated bar rating on a railed CR-V.",
   "specs": [["Type", "Rail-mounted aluminum crossbars"], ["Fits (per title)", "2023–2026 CR-V and CR-V Sport Hybrid with side rails"], ["Not for", "Bare-roof gas trims"], ["Bar rating", "220 lb (per title)"], ["Vehicle limit", "See owner's manual; 165 lb on Honda's accessory rails and the etrailer Thule/Yakima kits"], ["Lock", "Not in title; see listing"], ["Rail type", "Flush rails (etrailer)"]]},
  {"asin": "B0HBB9N6RY", "role": "Best lockable (rails)", "price": "Check listing",
   "pros": ["Anti-theft lock named in the title", "Title says Flush Side Rails, matching etrailer's description of the CR-V rail", "Title names the 2023–2026 CR-V Hybrid", "Aluminum bars", "Black finish to match the factory rails"],
   "cons": ["No brand name in the title; an unnamed seller", "Bar rating not in the title", "Warranty and return terms from the listing only"],
   "body": "This is the one rail set whose title describes the CR-V's rail the way etrailer does: Flush Side Rails. That matters because the sixth-gen CR-V's rails sit flat on the roof with no gap, and a seller who says so is more likely to have shaped the foot for it. The title also names the 2023–2026 CR-V Hybrid and an anti-theft lock, which the ANTS PART, HEKA and Snailfly titles do not. Lock cores keep the bars, and whatever is mounted to them, from leaving with a hex key at a trailhead.\n\nThe weakness is the missing brand. The title gives no seller name and no bar rating, so you are relying on the listing's own description, reviews and return terms. Read all three, and confirm that the lock is a key-lock core rather than a security screw. The roof limit does not change with the bars: Honda prints no figure in its 2024 or 2026 tables, so load to the owner's manual, bars included. If you want a named brand with a flush-rail fit guide, etrailer's Thule WingBar Evo flush-rail kit is $704.85 with a limited lifetime warranty.",
   "who": "Hybrid owners who park on the street or at trailheads and want locking bars sold for flush rails.",
   "specs": [["Type", "Lockable rail-mounted aluminum crossbars"], ["Fits (per title)", "2023–2026 CR-V Hybrid with flush side rails"], ["Not for", "Bare-roof gas trims"], ["Lock", "Anti-theft lock (per title)"], ["Bar rating", "Not in title; see listing"], ["Brand", "Not named in title"], ["Vehicle limit", "See owner's manual"]]},
  {"asin": "B0BYSF7LBT", "role": "Best budget (rails)", "price": "Check listing",
   "pros": ["Title names the 2023–2025 CR-V Sport Hybrid and says it works with side rails", "Snailfly sells rail bars for many SUVs", "Simple clamp-to-rail design", "Good enough for cargo bags, skis and a bike tray", "Usually the lowest price band among the named-brand rail sets"],
   "cons": ["Title stops at 2025; 2026 owners should confirm with the seller", "No locks or bar rating in the title", "Warranty from the seller only"],
   "body": "Snailfly's set is the basic rail bar: titled for the 2023, 2024 and 2025 CR-V and CR-V Sport Hybrid and described as working with side rails. It is the set for an owner who needs bars a few times a year for a soft cargo bag, a pair of ski carriers or one bike tray, and wants to spend as little as possible. Snailfly sells similar bars for the Forester and Highlander, which we cover in those guides, so it is a known seller rather than an anonymous listing.\n\nTwo cautions. The title stops at 2025. Honda's 2026 table lists the same black roof rails on the Sport, Sport-L and Sport Touring and adds the TrailSport, and no listing here suggests the rail changed, but that is an inference, so 2026 owners should confirm fit with the seller before ordering. And the title gives no bar rating and no locks, so read the listing for both. For a loaded cargo box on long trips, the HEKA set with its stated 220 lb rating or a Thule flush-rail kit is the stiffer choice. Keep the total load, bars included, under the roof figure in your owner's manual.",
   "who": "Budget buyers with a 2023–2025 hybrid who carry light loads a few times a year.",
   "specs": [["Type", "Rail-mounted crossbars"], ["Fits (per title)", "2023–2025 CR-V / CR-V Sport Hybrid with side rails"], ["2026", "Confirm with seller"], ["Not for", "Bare-roof gas trims"], ["Lock", "Not in title"], ["Bar rating", "Not in title; see listing"], ["Vehicle limit", "See owner's manual"]]},
  {"asin": "B07S3MC1T4", "role": "Bare-roof alternative (confirm generation)", "price": "Check listing",
   "pros": ["BRIGHTLINES is an established rack brand with spare parts sold through ASG Auto Sports", "Title says Without Roof Rails, so it is a door-frame clamp set", "Title runs to 2026", "Anti-theft hardware named in the title", "Aluminum bars"],
   "cons": ["Title spans 2012–2026, three CR-V generations; confirm the 2023+ fit kit with the seller", "Bar rating not in the title", "No page we could open gives the spread or weight"],
   "body": "BRIGHTLINES is the second bare-roof option, and the caution comes first: the title covers the 2012–2026 Honda CR-V without roof rails, which is three generations with different bodies. Door-frame clamp kits depend on a fit kit shaped for the door openings, and the 2023 CR-V is a new body on the Honda Architecture platform. A title that spans 2012 to 2026 may mean the seller ships different feet or pads by year, or it may mean a one-size claim. Ask the seller which it is, and that the kit was checked on a 2023 or later CR-V, before you order.\n\nWhy list it at all? BRIGHTLINES is a known rack brand rather than an anonymous listing; our Forester guide notes that ASG Auto Sports sells replacement end mounts and pads for its bars. The title names anti-theft hardware and aluminum bars. If the seller confirms the 2023+ fit, it is a reasonable step up from the Wonderdriver set for a gas LX, EX or EX-L. If not, the Thule WingBar Evo clamp kit or Yakima BaseLine etrailer lists for the bare-roof 2024 CR-V, both rated 165 lb with a limited lifetime warranty, is the safer buy at about $700.",
   "who": "Gas-trim owners who want a named brand on a bare roof and will confirm the 2023+ fit kit with the seller first.",
   "specs": [["Type", "Door-frame clamp crossbars"], ["Fits (per title)", "2012–2026 CR-V without roof rails"], ["2023+ fit", "Confirm with seller (multi-generation title)"], ["Not for", "Hybrid trims with roof rails"], ["Material", "Aluminum (per title)"], ["Lock", "Anti-theft (per title)"], ["Bar rating", "Not in title; see listing"], ["Vehicle limit", "See owner's manual"]]},
 ],
 "install": [
  "Identify your roof: smooth (gas LX, EX, EX-L) or black roof rails (hybrid trims). The rails are flush, so buy rail-mounted bars sold for the CR-V's side rails; a bare roof takes a door-frame clamp kit.",
  "Clean the roof edge or rails where the pads will sit so they grip paint and rail, not grit, and remove any stickers.",
  "Bare roof: set each foot at the position the kit's instructions give for the door openings, hook the clamps into the door frames with the doors open, and snug them evenly. Rails: set both bars loosely on the rails.",
  "Space the bars to your accessory's range (the rails let you slide; a clamp kit does not), keeping the rear bar forward of the liftgate's swing.",
  "Center the bars so the overhang is equal on both sides, then tighten the feet evenly, alternating sides, to the torque the instructions give.",
  "Open the liftgate fully to check clearance, and keep the sunroof closed with the rack installed, as etrailer's Thule fit notes for the CR-V say.",
  "Lock the feet, drive a short loop, re-tighten, and check again before every long trip.",
 ],
 "avoid": [
  {"h": "Rail bars on a gas LX, EX or EX-L", "body": "Those trims have nothing to clamp to. Buy a door-frame clamp set titled for the 2023+ CR-V, or have a dealer fit Honda's accessory rails first."},
  {"h": "Raised-rail clamp bars on a hybrid", "body": "etrailer lists the CR-V's rails as flush, with no gap underneath. Bars that wrap around a raised rail will not close on them."},
  {"h": "Loading to the bar claim", "body": "220 lb and 330 lb are sellers' bar ratings. Honda's accessory rails are marked 165 lb total and the Thule and Yakima kits are rated 165 lb; your owner's manual sets the roof limit, bars included."},
  {"h": "A 2017–2022 or multi-generation listing without a check", "body": "The 2023 CR-V is a new body. A kit for the old car will not match the door openings, and a 2012–2026 title needs the seller to confirm the 2023+ fit kit."},
 ],
 "verdict": {
  "thesis": "Match the roof: ANTS PART or the 220 lb HEKA set for a hybrid's flush rails, the Wonderdriver set for a gas CR-V's bare roof, and a Thule or Yakima kit from etrailer if you want a fit guide and a lifetime warranty on either.",
  "body": "The best CR-V crossbar is the one sold for your roof. Hybrid Sport, Sport-L, Sport Touring and TrailSport owners have flush rails and should buy rail bars: ANTS PART for the full-generation title, HEKA for a stated rating, the unnamed flush-rail set for locks, and Snailfly on a budget. Gas LX, EX and EX-L owners have a bare roof and need door-frame clamp bars: the Wonderdriver set, or BRIGHTLINES once the seller confirms the 2023+ fit. For either roof, etrailer's Thule WingBar Evo and Yakima BaseLine kits cost about $700 and come with a published fit kit and a 165 lb rating. Whatever you buy, the roof limit in your owner's manual includes the bars.\n\nWith bars on, a cargo box is the usual next step, and our CR-V cargo box guide lists box lengths and spread ranges for this short roof. If the roof is full, or you'd rather keep the bikes low, a trailer hitch with a bike carrier does the job within Honda's 1,500 lb gas and 1,000 lb hybrid tow ratings. The vehicle hub lists every fit-checked accessory for the 2023–2026 CR-V.",
 },
 "sources": [
  ["2024 Honda CR-V roof rack systems by roof type: flush rails and no rails, with prices and the Thule sunroof note (etrailer)", "https://www.etrailer.com/roof-2024_Honda_CR-V.htm"],
  ["How to add crossbars to a 2024 Honda CR-V with flush roof rails: Yakima SightLine answer (etrailer)", "https://etrailer.com//question/722486"],
  ["Thule WingBar Evo with Evo Clamp feet, naked roof, 165 lb, $704.85 (etrailer TH93BG)", "https://www.etrailer.com/Roof-Rack/Thule/TH93BG.html"],
  ["Thule WingBar Evo with Evo Flush Rail feet, 165 lb, $704.85 (etrailer TH24QG)", "https://www.etrailer.com/Roof-Rack/Thule/TH24QG.html"],
  ["Yakima BaseLine with JetStream bars, naked roof, 165 lb, $694.80 (etrailer Y66XD)", "https://www.etrailer.com/Roof-Rack/Yakima/Y66XD.html"],
  ["2026 Honda CR-V Specifications & Features: Black Roof Rails by trim, towing (Honda Newsroom)", "https://hondanews.com/en-US/honda-automobiles/releases/release-2ecca7d29f72bf212c56033cca000993-2026-honda-cr-v-specifications-features-updated"],
  ["2024 Honda CR-V Specifications & Features: Black Roof Rails by trim, towing (Honda Newsroom)", "https://hondanews.com/en-US/honda-automobiles/releases/release-13f25e90cfe47cd58453f1f710054868-2024-honda-cr-v-specifications-features"],
  ["Honda Roof Rails 08L02-3A0-100, 2023-2027 CR-V, 165 lb total, $435 list; crossbars 08L04-3A0-100 $250 (Bernardi Parts)", "https://www.bernardiparts.com/Products/Honda-Roof-Rails-(CRV-2023-2026)__08L02-3A0-100.aspx"],
  ["Honda CR-V sixth generation: July 2022 unveiling, 2023 model year, Honda Architecture platform (Wikipedia)", "https://en.wikipedia.org/wiki/Honda_CR-V"],
 ],
}

# Product list for this page. (asin, name, brand, band, cond, note)
FITS = [
 ("B0BX692P1F","ANTS PART Roof Rack Cross Bars for 2023-2026 Honda CRV & CR-V Sport Hybrid (roof rails)","ANTS PART","Check listing",{"roof_type":"flush-rails"},"Rail-mounted; hybrid trims with black roof rails. Confirm rating and locks on listing."),
 ("B0CRR2R73W","Wonderdriver Roof Rack Cross Bars for Honda CRV CR-V EX LX EX-L 2023-2026","Wonderdriver","Check listing",{"roof_type":"bare"},"Door-frame clamp set for gas trims; confirm bare-roof version, spread and bar weight."),
 ("B0C58CT63V","HEKA 220lb Roof Rack Cross Bars for Honda CR-V CRV & CRV Sport Hybrid 2023 2024 2025 2026 with Side Rails","HEKA","Check listing",{"roof_type":"flush-rails"},"220 lb is the bar claim; load to the owner's manual. Confirm locks."),
 ("B0HBB9N6RY","Roof Rack Cross Bars for Honda CR-V CRV 2023 2024 2025 2026 Hybrid, Anti-Theft Lock, Aluminum, with Flush Side Rails","Generic","Check listing",{"roof_type":"flush-rails"},"Unnamed seller; confirm rating and warranty on listing."),
 ("B0BYSF7LBT","Snailfly Cross Bars for 2023 2024 2025 Honda CR-V CRV Sport Hybrid, Work with Side Rails","Snailfly","Check listing",{"roof_type":"flush-rails"},"Title stops at 2025; confirm 2026 with seller."),
 ("B07S3MC1T4","BRIGHTLINES Anti-Theft Aluminum Roof Rack Crossbars for 2012-2026 Honda CRV Without Roof Rails","BRIGHTLINES","Check listing",{"roof_type":"bare"},"Multi-generation title; confirm the 2023+ fit kit with the seller."),
 ("B0BR5BDP42","Huray 200 LBS Roof Rack Cross Bars for Honda CRV CR-V / CRV Hybrid 2023 2024, with Side Roof Rails","Huray","Check listing",{"roof_type":"flush-rails"},"Title covers 2023-2024 only; confirm 2025 and 2026 with seller."),
 ("B0BMYSL7QZ","AOMSAZTO Roof Rack Cross Bars for 2023 2024 Honda CR-V LX, EX, Sport Hybrid, EX-L, Sport Touring Hybrid (Need Side Rails)","AOMSAZTO","Check listing",{"roof_type":"flush-rails"},"Needs side rails despite naming gas trims; confirm 2025 and 2026 with seller."),
]
