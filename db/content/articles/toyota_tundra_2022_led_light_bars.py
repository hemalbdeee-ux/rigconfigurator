"""Long-form article — Best LED Light Bars & Light Kits for 2022–2026 Toyota Tundra (3rd gen, XK70).
Mirrors the approved pilot (ford_f150_2021_tonneau.py) and the 5th-gen 4Runner / Bronco light-bar pages. No invented
hands-on testing: every spec comes from the maker/retailer pages listed in sources (checked 2026-09-27). Bars are
mostly universal; what is Tundra-specific is the mount (TRD Pro-style grille, lower bumper opening, fog pockets,
hood hinge, roof), the factory grille bar and the 2007–2021 vs 2022+ split, so picks are kits and brackets whose
Amazon titles name the 2022+ Tundra.
"""

KEY = ("toyota", "tundra", "2022-present", "led-light-bars")

TITLE = "Best LED Light Bars for 2022–2026 Toyota Tundra: 5 Kits Checked by Mount Location"
META = ("Five 3rd-gen Tundra light kits, from a TRD Pro grille bar to SAE fog pods and ditch lights, with lumens, "
        "amp draw, wiring, drilling and road-use notes.")

FAQ = [
 ("What is the best LED light bar for a 2022–2026 Tundra?",
  "If your truck has the TRD Pro-style grille, Diode Dynamics' SS20 grille light bar kit. Yota Xpedition lists it for all 2022+ Tundras with the OEM TRD Pro grille, hybrid and non-hybrid, at 7,376 lumens and 76.5 watts in Sport form or 25,088 lumens and 105 watts in Pro form, IP69K sealed, from $499.95. It sits inside the grille, so it looks factory and keeps glare off the hood. Without that grille, iJDMTOY's 20 in lower-opening kit is the budget bar that names the 2022+ truck."),
 ("Do 2007–2021 Tundra light bar brackets fit a 2022 Tundra?",
  "No. The third-generation Tundra started production in December 2021 with a new body, front end and hood, and brackets for the old truck are listed by year. Cali Raised, for example, sells separate 2014–2021 and 2022+ ditch brackets, and its 32 in lower bumper and 52 in roof kits are listed only for 2007–2021 or 2014–2021 trucks. Used-parts listings often just say \"Tundra,\" so look for 2022 or later in the title before you buy."),
 ("Does the 2022+ Tundra have a factory light bar?",
  "Some trucks do. Toyota's 2027 Tundra announcement says the grille-mounted LED light bar has been upgraded for brighter output, which confirms a factory grille bar on the current generation. The aftermarket builds its grille kits around the TRD Pro grille, and Yota Xpedition notes that on a TRD Pro, Diode's SS20 kit runs on its own harness and a new switch. We couldn't open a Toyota page listing which 2022–2026 trims carry the factory bar, so check your window sticker or grille."),
 ("Are LED light bars legal to use on the road in a Tundra?",
  "Usually not while driving. Rules vary by state, but many treat light bars, ditch pods and other auxiliary lights with off-road beams as off-road equipment that must be switched off on public roads, and some require an opaque cover or limit how many auxiliary lamps you can run and how high they sit. Fog lights built to the SAE J583 fog standard, such as Baja's S2 SAE kit, are the street-friendly option. Check your own state's rules before switching anything on in traffic."),
 ("Do I need to drill to add a light bar to a Tundra?",
  "Most kits don't, but one popular location does. Diode's grille kit uses a bracket kit in the TRD Pro grille, Cali Raised's ditch kit bolts on at existing factory mounting points, and Baja's S2 SAE fog kit is listed as no-drill. Baja's 9XL linkable roof bar kit for the 2022–2026 Tundra is different: Baja says it requires drilling for the front mounting bolts and won't work with a roof rack. Read the install sheet before you order."),
 ("How many amps does a Tundra light bar draw?",
  "Divide watts by system voltage. Diode lists the SS20 Pro at 105 W, roughly 7.6 A at 13.8 V, and the Sport at 76.5 W, roughly 5.5 A. iJDMTOY's 100 W bar is roughly 7.2 A. Baja's S2 SAE fog lights are 12.42 W each, so four draw about 3.6 A. Baja's 9XL roof bar is listed at 234 W and 18.0 A. Fuse and relay each light on its own circuit rather than stacking several on one switch."),
 ("Will a roof light bar cause wind noise on a Tundra?",
  "It can. A long bar at the front of the roof sits in the airflow at highway speed, and bare bars and brackets are a common source of whistling or humming. None of the maker pages here publish a noise figure. A grille bar, fog-pocket lights or ditch pods stay out of the worst airflow, which is one reason the picks on this page are low mounts. If you do want a roof bar, a fairing or a bar mounted behind a rack's wind deflector usually helps."),
 ("Will Baja's S2 SAE fog kit fit my TRD Pro Tundra?",
  "Check first. Baja lists the S2 SAE OEM fog light replacement kit for the 2022–2026 Tundra and flags a non-TRD Pro fitment note on the product page, so TRD Pro owners should confirm with Baja or the seller before ordering. The kit uses four lights, two per side, with a custom harness, adapter harness and brackets. Cali Raised's plug-in fog kit is listed for the 2022+ Tundra without a trim note, so confirm that too if your truck has factory upgraded fogs."),
 ("Will 2022–2026 Tundra light kits fit the 2027 Tundra?",
  "Don't assume so. Toyota's 2027 announcement describes new, square front styling, rectangular fog lights integrated into the bumper, new hexagonal grille designs and an upgraded grille light bar. Fog-pocket kits and grille brackets are the parts most likely to change. Toyota says full 2027 details are due in fall 2026, so wait for makers to publish 2027 fitment. Hood-hinge ditch brackets are the most likely to carry over, but confirm that too."),
 ("Should I choose amber or white lights for a Tundra?",
  "Amber for dust, rain and snow; white for maximum visible output. Amber scatters less off particles in the air, so it throws less glare back at you in bad weather. Diode offers the SS20 in white (6000K) or yellow (3000K), Baja offers the S2 SAE kit in clear or amber, and Cali Raised's fog and ditch kits come in white or amber. A common setup is amber in the fog pockets and white in the grille."),
]

ARTICLE = {
 "dek": "Five 3rd-gen Tundra lighting setups, from a Diode Dynamics bar inside the TRD Pro grille to Baja SAE fog pods and bolt-on ditch lights. Bars are mostly universal, so we focus on what is specific to the 2022+ Tundra: the mount, the factory grille bar, the 2007–2021 split, wiring and amp draw, and the road-use rules that decide when you can switch them on.",
 "author": "jake-morrison",
 "reviewed": "2026-09-27",
 "method": "We did not install these lights ourselves. We ranked them on published specs (lumens, watts, sealing, harness, warranty), on the fitment each maker, retailer or Amazon listing gives for the 2022–2026 Tundra and its trims, and on Toyota's own announcements for factory lighting. Prices were checked at the maker or a Toyota specialist retailer in September 2026. Where a spec comes only from an Amazon listing title, we say so. Amazon prices move daily, so the button shows the live price.",
 "takeaways": [
  "**Buy the mount, then the bar.** Bars are mostly universal; the grille bracket, fog-pocket kit or ditch bracket must name the 2022+ Tundra.",
  "**2007–2021 parts don't fit.** The 3rd gen has a new body and front; makers sell separate 2022+ brackets.",
  "**Check what your grille already has.** Toyota confirms a factory grille-mounted light bar on the current generation; grille kits target the TRD Pro grille.",
  "**Use a relay, fuse and switch.** A 105 W grille bar pulls roughly 7.6 A; a 9XL roof bar 18 A.",
  "**Most bars are off-road only.** SAE J583 fog kits are the street-friendly exception.",
 ],
 "top_picks": [
  {"asin": "B0BHKSJQ1C", "role": "Best grille light bar", "why": "Diode SS20 inside the TRD Pro grille, up to 25,088 lm, IP69K, from $499.95"},
  {"asin": "B0CDQV7P7V", "role": "Best street-friendly fog upgrade", "why": "Four Baja S2 SAE J583 fog lights, 1,210 lm each, no drilling"},
  {"asin": "B0CQN4YK9H", "role": "Best ditch light kit", "why": "Bolt-on 2022+ hood-hinge brackets with pods and harness, made in the USA"},
  {"asin": "B0BHBT4N66", "role": "Best budget light bar", "why": "20 in, 100 W bar in the lower bumper opening, brackets and switch wiring included"},
  {"asin": "B0DK485C8Z", "role": "Best budget fog upgrade", "why": "Two 6 in, 3,500 lm bars in the fog pockets, plug-and-play, $199.99"},
 ],
 "fit_table": {
  "caption": "2022–2026 Tundra details that affect light mounting",
  "head": ["Item", "Applies to", "What it means for lights"],
  "rows": [
   ["New 3rd-gen body and front", "2022–2026", "2007–2021 grille, bumper, ditch and roof brackets don't fit. Buy 2022+ listings."],
   ["TRD Pro-style grille", "TRD Pro, or trucks converted to that grille", "Diode SS20 and Baja S8 20 in grille kits mount here."],
   ["Factory grille-mounted light bar", "Current generation (per Toyota's 2027 release)", "Confirm what your truck has; on TRD Pro, Diode's kit uses its own harness and switch."],
   ["Fog pockets", "2022–2026", "Baja S2 SAE and Cali Raised kits replace the factory fogs; check trim notes."],
   ["Cabs and beds", "Double Cab, CrewMax; 5.5, 6.5, 8.1 ft beds", "Don't affect front lights, but decide where bed rack or roof lights go."],
   ["2027 refresh", "2027 Tundra", "New front, fog lights and grille; don't assume 2022–2026 kits carry over."],
  ],
 },
 "look_for": [
  {"h": "Generation first — 2007–2021 parts won't fit",
   "body": "The third-generation Tundra entered production in December 2021 with a new body, frame, front end and hood, and the lighting aftermarket split with it. Cali Raised, for example, sells its 2022+ ditch brackets as a separate part from its 2014–2021 brackets, and its 32 in hidden lower bumper and 52 in curved roof kits are listed only for the older trucks. The old truck ran from 2007 to 2021, so used brackets are everywhere and often listed simply as \"Tundra.\" Look for 2022 or later in the title, and be wary of kits whose year range stops at 2021. For 2027, Toyota has announced a new front again."},
  {"h": "Know what your grille already has",
   "body": "Toyota's 2027 Tundra announcement says the grille-mounted LED light bar has been upgraded for brighter output and that RIGID fog lights are available, which confirms the current truck already offers a factory grille bar. Aftermarket grille kits are built around the TRD Pro grille. Yota Xpedition lists Diode's SS20 kit for all 2022+ Tundras with the OEM TRD Pro grille, and Baja's S8 20 in kit for SR through Capstone trucks fitted with a TRD Pro grille as well as TRD Pros. On a TRD Pro, Diode's kit runs on its own harness and a new switch. Check your grille before ordering; a standard-grille truck needs a different mount, such as the lower bumper opening."},
  {"h": "Mount location sets the beam, glare and noise",
   "body": "A 3rd-gen Tundra has five common homes for extra light. The grille takes a 20 in-class bar behind the TRD Pro-style mesh, low enough to keep glare off the hood. The lower bumper opening takes a bar on non-TRD Pro trucks. The fog pockets take replacement pods, the most street-friendly option. The hood hinges take two ditch pods for trail edges. The roof takes a long bar for maximum reach, but it's the loudest, the most glare-prone and off-road only almost everywhere. Baja also sells Squadron 2.0 kits for the headlight vents on 2022–2026 trucks, at 3,200 lumens per Sport light."},
  {"h": "Wiring, relay, fuse and amp draw",
   "body": "Every add-on light needs a relay, a fuse sized for its draw and a switch you can reach. Divide watts by voltage to size it. Diode lists the SS20 at 76.5 W in Sport form and 105 W in Pro form, roughly 5.5 A and 7.6 A at 13.8 V. iJDMTOY's 100 W bar is roughly 7.2 A. Baja's S2 SAE lights are 12.42 W each, about 3.6 A for four. Baja lists its 9XL roof bar at 234 W and 18.0 A, which needs heavy wire and its own relay. If you plan several circuits, a switch panel or power-distribution module is tidier than a string of toggles."},
  {"h": "Sealing, color and drilling",
   "body": "Look for a published IP rating. Diode lists the SS20 as IP69K with sealed Deutsch DT connectors, and Baja describes its S8 as waterproof and submersible; Cali Raised and iJDMTOY don't publish an IP figure for these kits, so ask if you ford water often. Amber reduces back-glare in dust and rain; white gives the most visible output, and Diode offers 6000K white or 3000K yellow. Most Tundra kits are no-drill. The exception worth knowing is the roof: Baja says its 9XL roof kit needs drilling for the front bolts and won't work with a roof rack."},
 ],
 "look_table": {
  "head": ["Feature", "Look for", "Avoid"],
  "rows": [
   ["Fitment", "Listing names the 2022+ Tundra (and your grille type for grille kits)", "\"Fits Tundra\" with no year, or 2007–2021 kits"],
   ["Grille", "TRD Pro grille stated, factory bar and sensors addressed", "Grille kits that ignore what's already behind the mesh"],
   ["Wiring", "Harness with relay, fuse and switch, or plug-in fog adaptors", "Bars spliced into a headlight circuit"],
   ["Output", "Published lumens and watts", "\"Super bright\" with no figures"],
   ["Sealing", "IP67–IP69K or submersible stated", "No waterproof rating"],
   ["Mounting", "Bolt-on at factory points", "Roof kits that need drilling unless you accept it"],
  ],
 },
 "types_table": {
  "caption": "2022–2026 Tundra light mount locations compared",
  "head": ["Mount", "Example on this page", "Beam use", "Glare", "Road use", "Trade-off"],
  "rows": [
   ["TRD Pro grille", "Diode SS20 kit", "Driving / combo", "Low", "Usually off-road only", "Needs the TRD Pro-style grille"],
   ["Lower bumper opening", "iJDMTOY 20 in kit", "Fill / driving", "Low", "Usually off-road only", "Specs only from the listing"],
   ["Fog pocket", "Baja S2 SAE, Cali Raised", "Fog / near field", "Lowest", "SAE J583 version street-friendly", "Least reach"],
   ["Hood hinge (ditch)", "Cali Raised kit", "Trail edges", "Some off hood", "Usually off-road only", "Pods in view from cabin"],
   ["Roof", "Baja 9XL (maker-direct)", "Long-range reach", "Most", "Off-road only in most states", "Drilling, wind noise, 18 A"],
  ],
 },
 "picks": [
  {"asin": "B0BHKSJQ1C", "role": "Best grille light bar", "price": "From $500",
   "pros": ["Mounts inside the TRD Pro grille for a factory look", "Up to 25,088 lm (Pro) or 7,376 lm (Sport)", "IP69K with sealed Deutsch DT connectors", "SAE Driving or Combo beam, white or yellow", "Fits hybrid and non-hybrid 2022+ trucks"],
   "cons": ["Needs the OEM TRD Pro grille", "On a TRD Pro, runs on its own harness and new switch", "Amazon title lists 2022–2025; confirm 2026"],
   "body": "If your Tundra wears the TRD Pro-style grille, Diode Dynamics' SS20 grille light bar kit is the most complete bar built for it. Yota Xpedition lists it for all 2022+ Tundras with the OEM TRD Pro grille, hybrid and non-hybrid, and the kit includes one SS20 bar, a heavy-duty wiring harness, a Pro grille bracket kit and mounting hardware. The Sport version is listed at 76.5 watts and 7,376 lumens, and the Pro at 105 watts and 25,088 lumens, both IP69K with passive heat-sink cooling and sealed Deutsch DT connectors. Beam choices are SAE Driving or Combo/Driving, in 6000K white or 3000K yellow.\n\nYota Xpedition prices it from $499.95. Because the bar sits behind the grille mesh, it keeps a stock look when off and throws far less glare off the hood than a roof bar. Two details matter. On a TRD Pro, the retailer says you use the kit's harness with a new switch rather than a factory control, and Toyota's 2027 release confirms the current truck already offers a factory grille-mounted bar, so check what's behind your grille first. This Amazon listing is the white driving-beam version titled for 2022–2025; confirm 2026 and which power level it ships. At 105 W, the Pro draws roughly 7.6 A, so fuse it accordingly.",
   "who": "Owners of TRD Pro or TRD Pro-grille Tundras who want a real bar with a factory look.",
   "specs": [["Type", "Grille light bar kit"], ["Bar", "Diode SS20 Stage Series"], ["Output", "7,376 lm Sport / 25,088 lm Pro"], ["Power", "76.5 W Sport / 105 W Pro"], ["Sealing", "IP69K"], ["Fits", "2022+ Tundra with OEM TRD Pro grille"], ["Beam", "SAE Driving or Combo, white or yellow"], ["Price", "From $499.95 (Yota Xpedition)"]]},
  {"asin": "B0CDQV7P7V", "role": "Best street-friendly fog upgrade", "price": "From $680",
   "pros": ["Designed to meet SAE J583 fog lamp requirements", "Four lights, 1,210 lm and 5,712 cd each", "Only 12.42 W per light", "No drilling; brackets and harnesses included", "Lifetime limited warranty, 30-day guarantee"],
   "cons": ["Expensive for fog lights", "Trim note on Baja's page; TRD Pro owners must confirm", "Fog beam, not long-range reach"],
   "body": "Most of what you bolt to a Tundra is off-road lighting, but fog lights built to a road standard are the exception, and Baja Designs' S2 SAE OEM fog light replacement kit is the one that names the 2022+ Tundra. Baja says the lights are designed to meet SAE J583 fog lamp requirements, with a sharp cutoff for dust and fog. The kit uses four S2 SAE lights, two per side, each listed at 1,210 lumens, 5,712 candela and 12.42 watts, so the set draws only about 3.6 A. It includes two mounting brackets, a wiring harness, splitter harnesses, an adapter harness and hardware, and Baja describes it as a quick, no-drill install.\n\nBaja lists it from $679.95 as SKU 448162 in clear or 448167 in amber, with a 30-day satisfaction guarantee and a lifetime limited warranty. Baja's page lists 2022–2026 fitment with a non-TRD Pro note, so TRD Pro owners should confirm before ordering. It is a fog light, so it lights the road close to the truck and below the glare line rather than far down the trail. If you want more output and don't need the SAE rating, Baja's S2 Sport version for the 2022+ Tundra is also on Amazon, but it's an off-road light.",
   "who": "Owners who drive at night in rain, fog or dust on public roads and want a legal-minded upgrade.",
   "specs": [["Type", "Fog pocket replacement (4 lights)"], ["Standard", "Designed to SAE J583 fog"], ["Output", "1,210 lm / 5,712 cd per light"], ["Power", "12.42 W per light"], ["Fits", "2022–2026 Tundra (non-TRD Pro note)"], ["Mounting", "No drilling"], ["Warranty", "Lifetime limited"], ["Price", "From $679.95 (Baja Designs)"]]},
  {"asin": "B0CQN4YK9H", "role": "Best ditch light kit", "price": "From $170",
   "pros": ["Made for the 2022+ Tundra hood hinges", "Bolt-on at existing factory points; no drilling", "Pods and wiring harness included", "Laser-cut, CNC-bent steel, made in the USA", "2-year warranty on brackets"],
   "cons": ["No switch on this listing", "No IP rating or lumens on the maker page", "Pods visible from the cabin"],
   "body": "Ditch lights mount at the hood hinges and light the ditches and corners a grille bar can't reach, and Cali Raised LED's low-profile kit is built for the 2022+ Tundra. Cali Raised describes the brackets as laser-cut and CNC-bent steel, powder-coated in black semi-gloss and made in the USA, with a bolt-on install at existing factory mounting points in about one to two hours with basic hand tools. The kit includes brackets, a pair of pods, a wiring harness and hardware; on the maker's site, pod choices are 3x2 18 W white or amber, or 27 W side-projecting pods. This Amazon listing ships 3.5 in round cannon pods with a harness and no switch.\n\nCali Raised lists the kit at $169.99, or $189.99 with its OEM-style square switch, and gives a 2-year warranty on the mounting brackets. Two 18 W pods draw roughly 2.6 A at 13.8 V, so a small relay and fuse cover them. Cali Raised doesn't publish lumens or an IP rating for the pods, so confirm output and sealing on the listing. Ditch pods sit in the driver's line of sight and reflect some light off the hood, and they're off-road lighting in most states, so keep them off on public roads. Brackets-only versions exist if you already own pods.",
   "who": "Trail drivers who want to see edges and corners on any 2022–2026 Tundra.",
   "specs": [["Type", "Hood-hinge ditch light kit (2 pods)"], ["Pods", "3.5 in round cannon (this listing)"], ["Fits", "2022+ Tundra"], ["Mounting", "Factory points, no drilling"], ["Material", "Laser-cut steel, powder-coated, USA"], ["Warranty", "2 years on brackets"], ["Price", "$169.99 / $189.99 with switch (Cali Raised)"]]},
  {"asin": "B0BHBT4N66", "role": "Best budget light bar", "price": "Check listing",
   "pros": ["Titled for the 2022-up Tundra", "Complete kit: 20 in bar, brackets, switch wiring", "Lower bumper opening keeps glare low", "Works without the TRD Pro grille (per title)", "Lowest-cost bar on this page"],
   "cons": ["Specs only from the listing title", "No published IP rating or lumens", "Single-row 20 in bar: modest reach"],
   "body": "If your Tundra doesn't have the TRD Pro grille, the lower bumper opening is the next-lowest place for a bar, and iJDMTOY's kit is a budget option titled for the 2022-up Tundra. According to the listing title, it includes a 100 W single-row 20 in LED bar, brackets for the lower bumper opening and an on/off switch wiring kit, so you get a complete setup rather than brackets alone. A bar mounted low in the bumper keeps light off the hood and out of the driver's eyes, and a single-row bar is slim enough to sit mostly out of sight.\n\nThe weak point is verification. The listing title is the only source we could check; we found no maker page with a lumen figure, IP rating or warranty, so confirm those on the listing and read recent owner questions. At 100 W, the bar draws roughly 7.2 A at 13.8 V, so make sure the included harness has a relay and a fuse sized for it. Check with the seller that the bar and brackets stay clear of any front sensors or camera on your trim, and whether it works with your bumper and grille style. Like every bar on this page, it's off-road lighting in most states.",
   "who": "Budget buyers with a standard-grille 2022+ Tundra who want a hidden-ish bar.",
   "specs": [["Type", "Lower bumper opening bar kit"], ["Bar", "20 in single row, 100 W (per title)"], ["Fits", "2022-up Tundra (per title)"], ["Included", "Bar, brackets, switch wiring"], ["Current", "About 7.2 A at 13.8 V (calculated)"], ["Price", "Check listing"]]},
  {"asin": "B0DK485C8Z", "role": "Best budget fog upgrade", "price": "$200",
   "pros": ["Two 6 in bars, 30 W and 3,500 lm each", "OEM plug-and-play, pre-wired", "No cutting or drilling (Cali Raised)", "Amber or white", "Same part fits 2024+ Tacoma and 2025+ 4Runner"],
   "cons": ["No IP rating, beam pattern or warranty on the product page", "Not sold as an SAE fog light", "Amber has a longer lead time"],
   "body": "For a quarter of Baja's price, Cali Raised LED's fog light replacement kit puts two 6 in LED bars in the factory fog pockets. Cali Raised lists it for the 2022+ Tundra, 2024+ Tacoma and 2025+ 4Runner, which is why the Amazon title names all three, and says each bar is 30 watts and 3,500 lumens, 7,000 lumens for the pair. The kit is pre-wired and described as OEM plug-and-play, using existing mounting points with no cutting or drilling, and the steel brackets are CAD-designed for an OEM-like look. Cali Raised prices it at $199.99 in white or amber, with a three-to-four-week lead time on amber.\n\nOn paper it out-lumens Baja's SAE kit, but it isn't sold as an SAE fog light, and Cali Raised's product page doesn't publish a beam pattern, IP rating or warranty term. Treat it as auxiliary lighting for road-use purposes unless the listing shows an SAE fog marking. Two 30 W bars draw roughly 4.3 A at 13.8 V. The page gives no trim notes, so if your truck has upgraded factory fogs, confirm with the seller that the connector and pocket match. It's the simplest way on this page to add serious near-field light to a 2022+ Tundra.",
   "who": "Budget-minded owners who want a plug-in fog upgrade and mostly drive off-pavement at night.",
   "specs": [["Type", "Fog pocket replacement (2 bars)"], ["Bar", "6 in, 30 W"], ["Output", "3,500 lm each, 7,000 total (Cali Raised)"], ["Fits", "2022+ Tundra, 2024+ Tacoma, 2025+ 4Runner"], ["Wiring", "OEM plug-and-play"], ["Mounting", "Existing points, no drilling"], ["Price", "$199.99 (Cali Raised)"]]},
 ],
 "install": [
  "Choose the location, then confirm your model year (2022+), your grille (TRD Pro-style or standard) and whether a factory grille bar is already fitted.",
  "Disconnect the negative battery terminal before any wiring work.",
  "Fit the brackets at the factory points the instructions show (grille, lower bumper opening, fog pocket or hood hinge), leaving bolts loose for aiming.",
  "Route the harness away from exhaust heat and moving parts, mount the relay and fuse near the battery, and put the switch within reach. Fog kits plug into the factory fog connectors instead.",
  "Reconnect the battery, test every light, and check the dash for driver-assist or camera warnings.",
  "Aim the lights at night on level ground, tighten every bolt, and keep off-road lights off, and covered where required, on public roads.",
 ],
 "avoid": [
  {"h": "Buying 2007–2021 brackets for a 2022+ truck", "body": "The 3rd gen has a new body and front. Lower bumper, ditch and roof brackets for the old truck don't fit; buy 2022+ listings."},
  {"h": "Ordering a grille kit without the TRD Pro grille", "body": "Diode and Baja grille kits are built for the TRD Pro-style grille. Standard-grille trucks need a lower bumper, fog-pocket or ditch mount."},
  {"h": "Under-wiring a big bar", "body": "A 105 W grille bar pulls about 7.6 A and Baja's roof bar 18 A. Use a relay, a correctly sized fuse and adequate wire gauge."},
  {"h": "Running off-road lights on the road", "body": "Grille, ditch and roof bars are off-road lighting in most states. Keep them off, and covered where required; use SAE fog lights for road driving."},
 ],
 "verdict": {
  "thesis": "Match the light to your grille and your driving: Diode's SS20 for TRD Pro-grille trucks, Baja's S2 SAE fogs for road use, Cali Raised ditch pods for trail edges, and iJDMTOY's 20 in kit as the budget bar.",
  "body": "On a 3rd-gen Tundra the mount decides everything. Diode Dynamics' SS20 grille kit is the best bar for trucks with the TRD Pro grille, with published output, IP69K sealing and a stock look, though you should check what factory bar your grille already has. Baja's S2 SAE kit is the best choice if most of your night driving is on public roads, Cali Raised's ditch kit lights the trail edges on any 2022+ truck, and its $199.99 fog kit and iJDMTOY's 20 in lower-bumper kit are the budget routes. A roof bar gives the most reach, but Baja's 9XL roof kit needs drilling and won't work with a roof rack, so decide between roof lights and a roof rack before you buy either. If you're shopping for a 2027 Tundra, wait for fitment: the front end changes again.\n\nMany Tundra owners also mount lights on a bed rack, which keeps glare off the hood and the roof free. After lighting, running boards help with the climb into a lifted truck, and floor liners protect the carpet from mud. The vehicle hub lists every fit-checked accessory for your Tundra.",
 },
 "sources": [
  ["Diode Dynamics SS20 TRD Pro Grille Lightbar Kit, Tundra 2022+ (Yota Xpedition)", "https://yotaxpedition.com/products/ss20-trd-pro-grille-lightbar-kit-tundra-2022"],
  ["Baja Designs S8 20 in TRD Grille Light Bar Kit, Tundra 2022+ (Yota Xpedition)", "https://yotaxpedition.com/products/s8-20-inch-trd-grille-light-bar-kit-tundra-2022-2024"],
  ["Toyota S2 SAE OEM Fog Light Replacement Kit, 2022+ Tundra (Baja Designs)", "https://www.bajadesigns.com/products/toyota-s2-sae-oem-fog-light-replacement-kit-toyota-2022-on-tundra/"],
  ["9XL Linkable Roof Bar Kit, Toyota Tundra 2022+ (Baja Designs)", "https://www.bajadesigns.com/products/9xl-linkable-roof-bar-kit-toyota-tundra-2022-on/"],
  ["2022+ Toyota Tundra lighting kits (Baja Designs)", "https://www.bajadesigns.com/vehicle/2022-toyota-tundra/"],
  ["Low Profile Ditch Light Brackets Kit for 2022+ Tundra (Cali Raised LED)", "https://caliraisedled.com/products/low-profile-ditch-light-brackets-kit-for-2022-toyota-tundra"],
  ["Fog Light Replacement Kit for 2025+ 4Runner / 2022+ Tundra (Cali Raised LED)", "https://caliraisedled.com/products/fog-light-replacement-kit-for-2025-4runner"],
  ["New 2027 Toyota Tundra: grille light bar, fog lights, front styling (Toyota Newsroom)", "https://pressroom.toyota.com/new-2027-toyota-tundra-brings-rugged-updated-styling-advanced-technology-and-new-trailhunter-package/"],
  ["Toyota Tundra, third generation (Wikipedia)", "https://en.wikipedia.org/wiki/Toyota_Tundra"],
 ],
}

# Product list for this page. (asin, name, brand, band, cond, note)
FITS = [
 ("B0BHKSJQ1C","Diode Dynamics TRD Pro Grille Light Bar Kit compatible with Toyota Tundra 2022-2025, White Driving","Diode Dynamics","$480–$660",{"mount":"grille","grille":"TRD Pro"},"Needs OEM TRD Pro grille; listed to 2025 — confirm 2026 and Sport vs Pro."),
 ("B0CDQV7P7V","Baja Designs S2 LED SAE Fog Light Replacement Kit for Toyota Tundra 2022+","Baja Designs","$650–$720",{"mount":"fog-pocket"},"Baja page carries a non-TRD Pro note — confirm trim."),
 ("B0CQN4YK9H","Cali Raised LED Low Profile Ditch Light Brackets Kit, 2022+ Tundra (3.5 in Round Cannon Pods and Wiring Harness, No Switch)","Cali Raised LED","$165–$195",{"mount":"hood-hinge"},"No switch on this listing."),
 ("B0BHBT4N66","iJDMTOY Lower Grille Mount 20 in LED Light Bar, 2022-up Tundra, 100W single row, lower bumper opening brackets, switch wiring","iJDMTOY","Check listing",{"mount":"bumper"},"Specs from title only; confirm sensor clearance and bumper style."),
 ("B0DK485C8Z","Cali Raised LED Fog Light Replacement Kit for 2025+ 4Runner, 2024+ Tacoma and 2022+ Tundra (White)","Cali Raised LED","$190–$210",{"mount":"fog-pocket"},"Plug-and-play; confirm connector on trucks with upgraded factory fogs."),
 ("B0BHKKCPVV","Diode Dynamics TRD Pro Grille Light Bar Kit compatible with Toyota Tundra 2022-2023, Amber Combo","Diode Dynamics","$480–$660",{"mount":"grille","grille":"TRD Pro"},"Amber combo version of #1; listed to 2023 — confirm later years."),
 ("B0BHKZG99N","Diode Dynamics TRD Pro Grille Light Bar Kit compatible with Toyota Tundra 2022-2023, White Combo","Diode Dynamics","$480–$660",{"mount":"grille","grille":"TRD Pro"},"White combo version of #1; listed to 2023 — confirm later years."),
 ("B0FKQKS622","Baja Designs S2 Sport LED Fog Light Kit for 2022+ Toyota Tundra, 4 PCS, Adapter Harness, Plug and Play (Wide Cornering; Baja Amber)","Baja Designs","Check listing",{"mount":"fog-pocket"},"Off-road Sport version of #2; confirm trim."),
 ("B0CQN16T2S","Cali Raised LED 2022+ Tundra Ditch Light Brackets Lo Pro Kit, 3x2 18W Pods","Cali Raised LED","$165–$195",{"mount":"hood-hinge"},"3x2 pod version of #3."),
 ("B0CQMTSY2F","Cali Raised LED Low Profile Ditch Light Brackets Kit, 2022+ Tundra (Brackets Only)","Cali Raised LED","$55–$70",{"mount":"hood-hinge"},"Brackets only; pods universal — confirm pod size."),
 ("B0CN1LG9L5","Baja Designs S1 LED Vent Light Kit for Toyota Tundra 2022+, 6 LED Lights, Wiring Harness","Baja Designs","Check listing",{"mount":"headlight-vent"},"Vent-mount kit; confirm trim and vent style."),
 ("B0DK461BVM","Cali Raised LED Fog Light Replacement Kit for 2025+ 4Runner, 2024+ Tacoma and 2022+ Tundra (Amber)","Cali Raised LED","$190–$210",{"mount":"fog-pocket"},"Amber version of #5."),
 ("B0GSPRSBKN","Ditch Light Bracket for Tacoma 2024-2026 / 4Runner 2025-2026 / Tundra 2022-2026, heavy-duty steel","Generic","Check listing",{"mount":"hood-hinge"},"Unbranded budget brackets; confirm pod footprint and hardware."),
]
