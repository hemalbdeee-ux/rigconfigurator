"""Long-form article — Best LED Light Bars & Light Kits for 2021–2026 Ford F-150 (14th gen).
Mirrors the approved pilot (ford_f150_2021_tonneau.py) and the JL / Bronco light-bar pages. No invented hands-on
testing: every spec comes from maker/retailer pages listed in sources (checked 2026-09-27). Bars are mostly
universal; what is F-150-specific is the mount (fog pockets, lower grille/bumper opening, Raptor bumper, A-pillar
ditch brackets), the DRL vs non-DRL fog pocket split, the 2024 front-end refresh and the Raptor/Tremor variants.
Upfitter switch availability is reported by owners only (F150gen14), so it is phrased as such. No 2021+ roof-mount
bracket listing from a verifiable brand was found, so roof bars are covered as a "confirm" option, not a pick.
"""

KEY = ("ford", "f-150", "2021-present", "led-light-bars")

TITLE = "Best LED Light Bars for 2021–2026 Ford F-150: 5 Kits for Fog Pockets, Grille, Raptor and A-Pillar"
META = ("Five F-150 light kits and mounts, from fog pocket pods to a Raptor bumper bar, with lumens, amp draw, "
        "DRL and Raptor fit notes, upfitter wiring and road-use rules.")

FAQ = [
 ("What is the best LED light kit for a 2021–2026 F-150?",
  "For a standard F-150 with DRL headlights, the Baja Designs Squadron SAE/Pro fog pocket kit. Baja lists two Squadron SAE fog lights at 2,420 lumens and two Squadron Pro driving/combo lights at 4,095 lumens each, all rated IP69K, with a toggle or upfitter harness, from $1,032.95. The SAE pair is built to the J583 fog standard and connects to the factory fog light switch, so you get road-friendly fogs and off-road reach in the factory pockets. Baja lists it for 2021–2023 trucks with DRL only."),
 ("Does my F-150 have factory upfitter switches?",
  "Only some do. Owners on the F150gen14 forum report that the Tremor has upfitter switches in the overhead console, and some believe the Raptor has them too, while posters say they aren't offered in the build-and-price tool for standard F-150 trims. Look at your overhead console. If there's a bank of AUX switches, an upfitter harness such as Baja's 640093 is the clean way to wire lights. If not, buy the toggle-switch version of the kit, which includes its own switch and harness."),
 ("Will a Raptor light kit fit a regular F-150?",
  "No. The Raptor has its own front bumper and fog pockets, and Baja sells separate Raptor kits, such as the S2 SAE/S2 Pro fog pocket kit and the XL linkable bumper kit, listed only for the 2021–2026 F-150 Raptor (and the 2024–2026 Raptor 37 and Raptor R). Wikipedia notes the Raptor is only sold as a SuperCrew with a 5.5 ft box and is wider than other F-150s. Buy Raptor kits only for a Raptor, and standard F-150 kits for everything else."),
 ("What does \"with DRL\" or \"without DRL\" mean on F-150 fog pocket kits?",
  "It is a front-end split that decides which fog pocket kit fits. Baja lists its Squadron SAE/Pro fog pocket kit for the 2021–2023 F-150 with daytime running lights only and says it is not compatible with non-DRL trucks. Baja also sells a Squadron SAE Sport kit whose Amazon title reads F-150 2021+ without daytime running lights. Check your headlights and your window sticker, then buy the version that matches. If you're not sure, ask the seller with your VIN."),
 ("Are LED light bars legal to use on the road in an F-150?",
  "Usually not while driving. KC HiLiTES says it's illegal to have off-road-only lights turned on while on the roadway, and that many states also require them covered, with California and Pennsylvania requiring opaque covers. States also limit the number of auxiliary lamps and their mounting height. SAE J583 fog lamps, like the Squadron SAE and S2 SAE lights in Baja's fog pocket kits, are the road-friendly option. Grille bars, bumper bars and ditch lights are off-road lighting in most states. Check your own state's rules."),
 ("Do light kits from the 2021–2023 F-150 fit the 2024 refresh?",
  "Not automatically. Wikipedia says the 2024 update brought revised grilles and headlights, and that's where most light mounts live. Baja's Squadron SAE/Pro fog pocket kit is listed for 2021–2023, the Diode Dynamics fog pocket and SS5 bumper listings stop at 2023, while Diode's A-pillar ditch light listing reads 2021–2026 and Baja's Raptor kits list 2021–2026. Buy a listing that names your model year, and ask the seller if your year isn't named."),
 ("How much current do F-150 light kits draw?",
  "Check the per-light amps and add them up. Baja lists each Squadron SAE fog at 2.1 amps and each Squadron Pro at 3 amps, so a four-light pocket kit is about 10 amps. Baja's XL linkable Raptor bumper kit is listed at 156 watts and 12 amps. Budget grille bars often list watts only; divide by roughly 12 to 14 volts to estimate amps. Every bar or pair of pods needs a relay, an inline fuse sized for the load and a switch, or a factory upfitter circuit rated for it."),
 ("Can I mount a light bar on an F-150 roof?",
  "You can, but choose carefully. ZROADZ sells front roof brackets for 50 and 52 in curved bars that are listed for the 2015–2020 F-150, and several budget roof-bracket listings name 2004–2018 trucks. We didn't find a roof bracket from a brand with a verifiable spec page whose listing names the 2021+ truck, so confirm with the seller that any roof mount names your year and cab. A roof bar is the highest-glare, most-regulated mount, and a big bar needs a heavy relay circuit."),
 ("Do I need to drill to add fog pocket or bumper lights?",
  "Usually not. Fog pocket kits use the factory fog light openings with vehicle-specific brackets, and Baja says its XL linkable Raptor bumper kit needs no drilling or cutting. Bumper-opening grille bars and A-pillar ditch brackets are designed to bolt to existing points, though the listing is the only source for budget kits. The wiring is where you may need to pass a harness through the firewall, so plan a grommet route and read the install sheet before you start."),
 ("Should I buy an SAE fog kit or a spot/driving kit?",
  "If you want lights you can use on the road, SAE fog. Baja's Squadron SAE and S2 SAE lights are built to the J583 fog lamp standard, with a sharp cutoff that keeps light low. Spot and driving combo pods reach much farther but are off-road lights. The best F-150 fog pocket kits combine both: Baja's standard F-150 kit pairs two SAE fogs with two Squadron Pro driving/combo lights, and its Raptor kit pairs two S2 SAE fogs with two S2 Pro pods."),
]

ARTICLE = {
 "dek": "Five F-150 light setups, from a budget grille bar to Baja's fog pocket kits and a 39 in Raptor bumper bar. Bars are mostly universal, so we focus on what is specific to the 2021–2026 F-150: fog pockets and the DRL split, the 2024 front-end refresh, Raptor-only mounts, upfitter switches on some trims, amp draw, and the road rules that decide when you can switch them on.",
 "author": "jake-morrison",
 "reviewed": "2026-09-27",
 "method": "We did not install these lights ourselves. We ranked them on published specs (lumens, watts, amps, sealing, harness, warranty), on the fitment each maker or Amazon listing gives for the 2021–2026 F-150 and its Raptor variants, on owner reports about upfitter switches from the F150gen14 forum, and on KC HiLiTES' general guidance on auxiliary lighting. Truck facts come from Wikipedia. Prices were checked at Baja Designs in September 2026. Amazon prices change daily, so the button shows the live price.",
 "takeaways": [
  "**Fog pockets are the best first mount.** They're low, factory-looking and can hold SAE fog lamps you can legally use on the road.",
  "**Match the front end.** Baja's standard kit fits 2021–2023 trucks with DRL only; non-DRL, 2024+ and Raptor trucks need other kits.",
  "**Raptor parts are Raptor-only.** The Raptor bumper and fog pockets differ; Baja lists separate kits for the 2021–2026 Raptor.",
  "**Upfitter switches aren't universal.** Owners report them on the Tremor (and possibly Raptor); most trucks need a toggle harness with relay and fuse.",
  "**Bars and spots are off-road lights.** Keep them off, and covered where required, on public roads.",
 ],
 "top_picks": [
  {"asin": "B0CD9JH1KS", "role": "Best overall (standard F-150)", "why": "Two SAE fogs plus two 4,095 lm Squadron Pros in the factory pockets, IP69K"},
  {"asin": "B0CM75CNCT", "role": "Best Raptor fog kit", "why": "Two S2 SAE fogs and two S2 Pro pods for the Raptor pockets, $735.95"},
  {"asin": "B0FXHBGFD2", "role": "Best Raptor bumper bar", "why": "39.16 in linkable 6XL bar, no drilling, rock guards and harness included"},
  {"asin": "B0DK2DPY78", "role": "Best budget grille bar", "why": "96 W bar with lower bumper-opening brackets and switch wiring, 2021+ and Lightning"},
  {"asin": "B0B8PHDZHP", "role": "Best A-pillar ditch brackets", "why": "Diode Dynamics brackets listed for 2021–2026 F-150, pick your own pods"},
 ],
 "fit_table": {
  "caption": "2021–2026 F-150 details that affect light mounting",
  "head": ["Item", "Applies to", "What it means for lights"],
  "rows": [
   ["Fog pockets, DRL vs non-DRL", "Standard F-150 trims", "Baja's Squadron SAE/Pro kit fits 2021–2023 with DRL only; a separate non-DRL kit exists."],
   ["2024 refresh", "2024–2026", "Revised grilles and headlights (Wikipedia). 2021–2023 grille, bumper and fog kits need a listing that names 2024+."],
   ["Raptor / Raptor 37 / Raptor R", "SuperCrew, 5.5 ft box only", "Own bumper and fog pockets. Baja lists Raptor kits for 2021–2026 (Raptor R and 37 from 2024)."],
   ["Tremor", "SuperCrew, 5.5 ft box", "Owners report overhead upfitter switches. Use upfitter harnesses where present."],
   ["Lightning (2022–2025)", "Electric", "Some grille kits name it; confirm before buying."],
  ],
 },
 "look_for": [
  {"h": "Mount location: fog pockets, grille, bumper, A-pillar or roof",
   "body": "On an F-150, most useful mounts sit low. Fog pocket kits replace the factory fog lights with vehicle-specific brackets and pods. Lower grille or bumper-opening kits hide a single bar behind the lower fascia. Raptor owners can add a linkable bar across the bumper. A-pillar ditch brackets put two pods beside the windshield for trail edges and corners. Roof bars are the least common on this generation: we found roof brackets listed for the 2015–2020 F-150 but none from a verifiable brand naming the 2021+ truck. Pick the location first, then a kit whose listing names your year, trim and front end."},
  {"h": "Front end: DRL, non-DRL, the 2024 refresh and Raptor",
   "body": "The F-150's fog pockets aren't all the same. Baja lists its Squadron SAE/Pro fog pocket kit for the 2021–2023 F-150 with daytime running lights only and says it doesn't fit non-DRL trucks, and it sells a separate Squadron SAE Sport kit whose Amazon title reads 2021+ without DRL. Wikipedia says the 2024 refresh brought revised grilles and headlights, so kits that stop at 2023 need a check before they go on a 2024–2026 truck. The Raptor has its own bumper and fog pockets, and Baja sells Raptor-only kits for them. Wikipedia notes the Raptor is a 5.5 ft SuperCrew and wider than other F-150s. Know which front end you have before you order."},
  {"h": "Upfitter switches and wiring",
   "body": "A proper light install needs a relay, an inline fuse sized for the load and a switch you can reach. Some F-150s already have the switches. Owners on the F150gen14 forum report that the Tremor has upfitter switches in the overhead console, and some believe the Raptor does too, while they say standard trims don't offer them in Ford's build-and-price tool. Baja sells its F-150 fog pocket kit with either a toggle-switch harness (640139) or an upfitter harness (640093) that uses the factory switches, and on both versions one pair of lights connects to the OEM fog light switch. If your overhead console has no AUX bank, buy the toggle version."},
  {"h": "Output, beam pattern and amp draw",
   "body": "Big numbers aren't the whole story. Baja lists its Squadron Pro driving/combo lights at 4,095 lumens, 41.4 watts and 3 amps each, and its Squadron SAE fogs at 2,420 lumens and 2.1 amps. On the Raptor, the S2 Pro pods are 2,245 lumens and the S2 SAE fogs 1,210 lumens each at 12.42 watts. Baja's XL linkable Raptor bumper kit lists 156 watts and 12 amps. Spot and driving beams reach down the trail; wide and SAE fog beams light the road edge and near ground. Add up the amps on each switch and fuse, and remember a big roof bar can draw far more than a pair of pods."},
  {"h": "Road rules, SAE fogs, sealing and glare",
   "body": "Nearly every bar and spot pod is an off-road light. KC HiLiTES says off-road-only lights must be off on the roadway and that many states also require them covered, with California and Pennsylvania requiring opaque covers. KC adds that states commonly limit driving lights to about 16–42 in above the ground and fog lamps to about 12–30 in, and that mounting in line with or below the headlights avoids most problems. SAE J583 fog lamps, like Baja's Squadron SAE and S2 SAE, are the road-friendly choice. Low fog pocket and grille lights cause the least hood glare and wind noise. For sealing, Baja rates its Squadron and XL lights IP69K."},
 ],
 "look_table": {
  "head": ["Feature", "Look for", "Avoid"],
  "rows": [
   ["Fitment", "Listing names the 2021+ F-150 and your model year", "2015–2020 or \"universal F-150\" listings"],
   ["Front end", "DRL / non-DRL and Raptor stated", "Fog pocket kits for the wrong front end"],
   ["Wiring", "Toggle harness with relay and fuse, or an upfitter harness if you have switches", "Bare lights with no relay or fuse"],
   ["Output", "Published lumens, watts and amps", "\"Super bright\" with no figures"],
   ["Road use", "SAE J583 fog lamps for street driving", "Spot pods marketed as fog lights"],
   ["Sealing", "IP69K or IP68 stated", "\"Waterproof\" with no rating"],
  ],
 },
 "types_table": {
  "caption": "F-150 light mount locations compared",
  "head": ["Mount", "Example on this page", "Beam use", "Glare", "Road use", "Trade-off"],
  "rows": [
   ["Fog pockets", "Baja Squadron SAE/Pro kit", "SAE fog plus driving fill", "Least", "SAE fogs usable on road", "DRL / year / Raptor specific"],
   ["Lower grille / bumper opening", "iJDMTOY 96 W bar kit", "Mid-range fill", "Low", "Off-road only in most states", "Limited published specs"],
   ["Raptor bumper bar", "Baja 6XL linkable kit", "Long-range and spread", "Low", "Off-road only in most states", "Raptor only, premium price"],
   ["A-pillar ditch lights", "Diode Dynamics brackets", "Wide, trail edges and corners", "Some", "Usually off-road only", "Pods and wiring extra"],
   ["Roof line", "No verified 2021+ bracket", "Long-range distance", "Most (off hood)", "Off-road only in most states", "Wind noise, height rules"],
  ],
 },
 "picks": [
  {"asin": "B0CD9JH1KS", "role": "Best overall (standard F-150)", "price": "From $1,033",
   "pros": ["Two Squadron SAE fogs meet SAE J583", "Two Squadron Pro driving/combo lights at 4,095 lm each", "One pair runs off the factory fog light switch", "Toggle or upfitter harness versions", "IP69K, IK10, limited lifetime warranty"],
   "cons": ["Baja lists 2021–2023 with DRL only", "This listing is the upfitter, amber version; toggle sold separately", "Not for the Raptor"],
   "body": "Baja's Squadron SAE/Pro fog pocket kit turns the F-150's factory fog pockets into a four-light setup that covers both road and trail. Baja lists two Squadron SAE lights at 2,420 lumens, 29 watts and 2.1 amps each, built to the SAE J583 fog standard, and two Squadron Pro driving/combo lights at 4,095 lumens, 41.4 watts and 3 amps each. The kit includes the mounting brackets and stainless hardware, and the lights are rated IP69K (pressure washable, waterproof to 9 ft) and IK10 for impact. One pair connects to the factory fog light switch, so the road-legal fogs work like the originals. Baja lists it from $1,032.95 with a limited lifetime warranty and 30-day money-back guarantee.\n\nFit is the catch. Baja lists the kit for the 2021–2023 F-150 with daytime running lights only and says it isn't compatible with non-DRL trucks; the Amazon title reads 2021+, so check your front end and year against Baja's page. This listing is the amber, upfitter-harness version (Baja harness 640093), which suits trucks with the overhead switches owners report on the Tremor. Without them, buy the toggle version (harness 640139). At about 10 amps for all four lights, it's a modest load for a fused relay circuit.",
   "who": "Owners of 2021–2023 DRL-equipped F-150s who want road-legal fogs and off-road fill in the factory pockets.",
   "specs": [["Type", "Fog pocket kit (4 lights)"], ["Part #", "490003 kit (Baja)"], ["Fits", "2021–2023 F-150 with DRL only (Baja)"], ["Fogs", "2x Squadron SAE, 2,420 lm, 2.1 A each"], ["Driving", "2x Squadron Pro, 4,095 lm, 3 A each"], ["Standard", "SAE J583 (SAE lights)"], ["Harness", "Upfitter 640093 (this listing) or toggle 640139"], ["Sealing", "IP69K, IK10"], ["Price", "From $1,032.95 (Baja)"]]},
  {"asin": "B0CM75CNCT", "role": "Best Raptor fog kit", "price": "$736",
   "pros": ["Two S2 SAE fogs built to J583", "Two S2 Pro driving combo pods at 2,245 lm", "Brackets, harness adaptors and rock guards included", "Listed for 2021–2026 Raptor and 2024–2026 Raptor 37 / R", "Limited lifetime warranty"],
   "cons": ["Raptor only", "Lower output than Squadron-size pods", "Baja recommends professional installation"],
   "body": "The Raptor's fog pockets take their own kits, and Baja's S2 SAE/S2 Pro kit is the value pick for them. Baja lists two S2 SAE lights at 1,210 raw lumens and 12.42 watts each, designed to meet J583 fog lamp requirements, and two S2 Pro driving combo lights at 2,245 raw lumens and 23.4 watts each. The kit comes with four harness adaptors, four black rock guards, the mounting brackets and all hardware, and the SAE lights are offered in clear or Baja amber. Baja lists it at $735.95 with a 30-day satisfaction guarantee and a limited lifetime warranty.\n\nFit is Raptor-specific. Baja lists the 2021–2026 F-150 Raptor, the 2024–2026 Raptor 37 and Raptor R, and the 2023–2026 Bronco Raptor, and none of the standard F-150 trims. This Amazon listing is the clear version and its title reads F-150 Raptor 2021-on. The SAE fogs are the road-friendly pair; the S2 Pro pods add reach for trail use and should be off on public roads. Baja recommends professional installation. If you want more output, Baja also sells a Squadron-size Raptor pocket kit, but at a much higher price.",
   "who": "Raptor owners who want road-legal fogs plus trail fill in the factory pockets at a moderate price.",
   "specs": [["Type", "Fog pocket kit (4 lights)"], ["Part #", "448182 / 448183 (Baja)"], ["Fits", "2021–2026 Raptor, 2024–2026 Raptor 37/R (Baja)"], ["Fogs", "2x S2 SAE, 1,210 lm, 12.42 W each"], ["Driving", "2x S2 Pro, 2,245 lm, 23.4 W each"], ["Standard", "SAE J583 (SAE lights)"], ["Included", "Brackets, 4 harness adaptors, 4 rock guards"], ["Warranty", "Limited lifetime"], ["Price", "$735.95 (Baja)"]]},
  {"asin": "B0FXHBGFD2", "role": "Best Raptor bumper bar", "price": "From $1,853",
   "pros": ["39.16 in linkable bar, up to 24,570 lm (6XL Pro)", "No drilling or cutting (Baja)", "Straight or arc setup, 45 degree pitch adjustment", "Harness 640163 and six rock guards included", "IP69K, IK10, limited lifetime warranty"],
   "cons": ["Raptor only; Amazon title reads Raptor R/37 2024+", "Most expensive kit here", "Off-road lighting in most states"],
   "body": "For Raptor owners who want a bar rather than pods, Baja's XL linkable bumper kit mounts six XL lights across the front bumper. Baja lists a 39.16 in overall length, with 18,900 lumens for the 6XL Sport version and 24,570 lumens for the 6XL Pro, and a rating of 156 watts and 12 amps with built-in overvoltage protection. Each light adjusts horizontally, so the row can be set straight or in an arc, and there's 45 degrees of vertical pitch adjustment. Baja includes a pre-crimped, pre-trimmed harness (640163) and six black rock guards, and says the bumper mount needs no drilling or cutting.\n\nBaja's page lists the kit for the 2021–2026 F-150 Raptor and starts it at $1,852.95 with a limited lifetime warranty and 30-day money-back guarantee. This Amazon listing is the 6XL Pro clear version, and its title names the Raptor R and Raptor 37 for 2024+, so owners of earlier Raptors should confirm fit against Baja's page or with the seller. A bumper-height bar throws less hood glare than a roof bar, but at this output it's still an off-road light, so keep it off on public roads and add up its 12 amps with anything else on the circuit.",
   "who": "Raptor owners who want a single long bar with the most output and a factory-looking mount.",
   "specs": [["Type", "Linkable bumper light bar kit (6 lights)"], ["Part #", "740004 (Baja SKU)"], ["Fits", "2021–2026 F-150 Raptor (Baja); listing names Raptor R/37 2024+"], ["Length", "39.16 in"], ["Output", "18,900 lm (Sport) / 24,570 lm (Pro)"], ["Rating", "156 W, 12 A"], ["Sealing", "IP69K, IK10"], ["Mounting", "No drilling or cutting"], ["Price", "From $1,852.95 (Baja)"]]},
  {"asin": "B0DK2DPY78", "role": "Best budget grille bar", "price": "Check listing",
   "pros": ["Complete kit: bar, brackets and on/off switch wiring", "96 W bar in the lower bumper opening", "Listing names 2021-up F-150 and Lightning", "Hidden, low mount with little hood glare", "A fraction of a Baja kit's price"],
   "cons": ["No maker spec page we could read; listing only", "No published lumens, IP rating or amp figure", "Confirm 2024+ front-end fit"],
   "body": "iJDMTOY's lower grille kit is the budget way to add a bar without changing the look of the truck. The Amazon listing includes one 96 W LED bar, brackets that mount it in the lower bumper opening, and on/off switch wiring, and names the 2021-up F-150 and the Lightning. A bar in the lower opening sits well below the hood line, so it throws little glare back at the driver and sits closer to the mounting heights KC says most states use than a roof bar would. At 96 watts, expect roughly 7 to 8 amps at typical charging voltage, well within a single fused relay circuit.\n\nThe limits are data and fit. The listing is the only source we could read, and it doesn't publish lumens, beam pattern or a sealing rating, so treat it as a fill light and check the harness for a relay and inline fuse before you connect it. Wikipedia says the 2024 refresh brought revised grilles, so 2024–2026 owners should confirm that the brackets match their lower opening; Tremor and Raptor fronts differ as well. iJDMTOY sells a separate kit for the 2015–2020 F-150, so make sure you're on the 2021-up listing.",
   "who": "Budget-minded owners who want a hidden bar for back roads and job sites.",
   "specs": [["Type", "Lower grille / bumper-opening bar kit"], ["Bar", "96 W LED (per listing)"], ["Fits", "2021-up F-150 and Lightning (per listing)"], ["Included", "Bar, brackets, switch wiring"], ["Output", "Not published"], ["Price", "Check listing"]]},
  {"asin": "B0B8PHDZHP", "role": "Best A-pillar ditch brackets", "price": "Check listing",
   "pros": ["Listing names 2021–2026 F-150", "Brand-name vehicle-specific brackets", "Pods at the A-pillar light trail edges and corners", "Choose your own pod size and beam", "Also sold as complete kits with SS3 or C2 pods"],
   "cons": ["Bracket-only listing: pods and harness extra", "Diode's spec pages blocked our fetch; listing only", "Off-road lighting in most states"],
   "body": "Ditch lights, pods at the base of the A-pillars, fill the gap between fog lights and a long-range bar by lighting the trail edges and corners. Diode Dynamics' Stage Series backlit ditch light kit is the most useful F-150 listing for them because its title names the 2021–2026 F-150, a wider range than many fog and bumper kits. This listing is the bracket-only version, so you choose the pods; Diode sells the same kit on Amazon with its SS3 and C2 pods in white or yellow combo patterns if you'd rather buy it complete.\n\nDiode Dynamics' own site blocked our page fetch, so the listing is our only spec source. Check the bracket material, the hardware and the pod size the brackets take before ordering, and budget for a relay harness with an inline fuse and a switch, or connect to the upfitter switches if your truck has them. A-pillar pods sit higher than fog lights and throw some glare off the hood, and in most states they're off-road lights, so keep them off on public roads.",
   "who": "Owners who want trail-edge lighting on any 2021–2026 F-150 and prefer to pick their own pods.",
   "specs": [["Type", "A-pillar ditch light brackets"], ["Fits", "2021–2026 F-150 (per listing)"], ["Included", "Brackets only (this listing)"], ["Pods", "Not included; SS3 / C2 kits sold separately"], ["Wiring", "Not included"], ["Price", "Check listing"]]},
 ],
 "install": [
  "Identify your front end: standard F-150 with or without DRL, 2021–2023 or 2024+, Tremor, Raptor or Lightning. Buy only a kit that names it.",
  "Check the overhead console for AUX switches. If you have them, order the upfitter harness; if not, the toggle version with relay and fuse.",
  "Disconnect the negative battery terminal, then remove the factory fog lights or trim pieces the instructions call for.",
  "Fit the brackets and lights at the factory points, leaving them loose for aiming. Route the harness away from heat and moving parts, using an existing firewall grommet where possible.",
  "Reconnect the battery, test every circuit, aim the lights at night on level ground and tighten all bolts.",
  "Keep off-road lights off, and covered where required, on public roads. Re-check bolts after the first rough road.",
 ],
 "avoid": [
  {"h": "A fog pocket kit for the wrong front end", "body": "Baja's standard kit is DRL-only for 2021–2023; non-DRL, 2024+ and Raptor trucks need different kits."},
  {"h": "Buying 2015–2020 F-150 parts", "body": "Grille, roof and fog kits for the previous generation look similar in search results. Check the year range on the title."},
  {"h": "Assuming you have upfitter switches", "body": "Owners report them on the Tremor, not on most trims. Without them, use a toggle harness with a relay and fuse."},
  {"h": "Driving with spot pods on", "body": "Spot and driving pods are off-road lights. Use SAE fog lamps for road driving and keep the rest off."},
 ],
 "verdict": {
  "thesis": "Start in the fog pockets: Baja's Squadron SAE/Pro kit for DRL-equipped 2021–2023 trucks, the S2 SAE/S2 Pro kit for a Raptor, and add a bumper bar or A-pillar pods only if you need more reach.",
  "body": "On a 2021–2026 F-150, the front end decides fit more than the light does. Baja's Squadron SAE/Pro fog pocket kit is the best all-round choice for standard trucks it fits, with SAE fogs for the road and Squadron Pro reach for the trail. Raptor owners get a well-priced four-light setup from the S2 SAE/S2 Pro kit, and the 6XL linkable bumper bar if they want maximum output. iJDMTOY's grille bar and Diode Dynamics' ditch brackets cover the budget end, with the caveat that their listings carry the only specs. Match the kit to your DRL, model year and trim, and wire it with a relay and fuse unless you have factory upfitter switches.\n\nIf you're fitting a bed rack for a rooftop tent, rear-facing scene lights can mount there instead of on the cab, and a tonneau cover or roof rack choice may affect where you route wiring. Owners of the 2015–2020 F-150 need different grille and fog kits. For the rest of the truck, see our fit-checked trailer hitch, running boards and floor liners pages.",
 },
 "sources": [
  ["Ford Squadron SAE/Pro Fog Pocket Light Kit, 2021–2023 F-150 (Baja Designs)", "https://www.bajadesigns.com/products/ford-squadron-sae-pro-fog-pocket-light-kit-ford-2021-2022-f-150/"],
  ["S2 SAE/S2 Pro Fog Pocket Kit, 2021–2026 F-150 Raptor (Baja Designs)", "https://www.bajadesigns.com/products/s2-sae-s2-pro-fog-pocket-kit-ford-f-150-raptor-2021-on-bronco-raptor-2022-on/"],
  ["Ford Raptor S2 SAE Dual Fog Pocket Kit (Baja Designs)", "https://www.bajadesigns.com/products/s2-sae-dual-fog-pocket-kit-ford-f-150-raptor-21-23-bronco-raptor-22-on/"],
  ["XL Linkable Bumper Light Kit, 2021–2026 F-150 Raptor (Baja Designs)", "https://www.bajadesigns.com/products/ford-xl-linkable-bumper-light-kit-ford-2021-2024-f-150-raptor/"],
  ["Where are the upfitter switches? (F150gen14 forum)", "https://www.f150gen14.com/forum/threads/where-are-the-upfitter-switches.1054/"],
  ["Auxiliary switch locations (F150gen14 forum)", "https://www.f150gen14.com/forum/threads/auxiliary-switch-locations.6037/"],
  ["Are LED light bars and auxiliary lights street legal? (KC HiLiTES)", "https://www.kchilites.com/campfire/post/are-led-light-bars-and-auxiliary-lights-street-legal"],
  ["Ford F-Series fourteenth generation — trims, 2024 refresh, Raptor, Tremor (Wikipedia)", "https://en.wikipedia.org/wiki/Ford_F-Series_(fourteenth_generation)"],
 ],
}

# Product list for this page. (asin, name, brand, band, cond, note)
FITS = [
 ("B0CD9JH1KS","Baja Designs Squadron SAE Pro Fog Pocket LED Light Kit fits Ford F-150 2021+ with Upfitter Wiring Harness (Multi-Pattern; Amber)","Baja Designs","$1,000–$1,150",{"mount":"fog-pocket","drl":True,"upfitter":True},"Baja lists 2021-2023 with DRL only, not Raptor — confirm year and DRL; toggle version for trucks without upfitter switches."),
 ("B0CM75CNCT","Baja Designs S2 SAE Pro Fog Pocket LED Light Kit for Ford F-150 Raptor 2021-on; Bronco Raptor 2022-on (Clear)","Baja Designs","$700–$780",{"mount":"fog-pocket","trim":"Raptor"},"Raptor only."),
 ("B0FXHBGFD2","Baja Designs 6XL Pro Linkable LED Front Bumper Light Bar Kit for Ford F-150 Raptor R/37 2024+ (Clear)","Baja Designs","$1,800–$2,000",{"mount":"bumper","trim":"Raptor"},"Raptor only; title names 2024+ Raptor R/37 — confirm fit on 2021-2023 Raptor."),
 ("B0DK2DPY78","iJDMTOY Lower Grille Mount LED Light Bar, 2021-up Ford F150 & Lightning, 96W bar, lower bumper opening brackets & on/off switch wiring","iJDMTOY","Check listing",{"mount":"grille"},"Listing-only specs; confirm 2024+ grille, Tremor and Raptor fit."),
 ("B0B8PHDZHP","Diode Dynamics Stage Series Backlit Ditch Light Kit compatible with Ford F-150 2021-2026, Bracket Only","Diode Dynamics","Check listing",{"mount":"a-pillar"},"Brackets only; confirm pod size and wiring."),
 ("B0CDNQS4GC","Baja Designs Squadron SAE Sport Fog Pocket LED Light Kit fits Ford F-150 2021+ Without Daytime Running Lights (Multi-Pattern; Clear; Toggle Wiring)","Baja Designs","Check listing",{"mount":"fog-pocket","drl":False},"Non-DRL trucks; confirm year."),
 ("B0CM7553WG","Baja Designs S2 SAE Sport Fog Pocket LED Light Kit for Ford F-150 Raptor 2021-on; Bronco Raptor 2022-on (Clear)","Baja Designs","Check listing",{"mount":"fog-pocket","trim":"Raptor"},"Raptor only; Sport version."),
 ("B0CM75GJMM","Baja Designs S2 SAE Pro Fog Pocket LED Light Kit for Ford F-150 Raptor 2021-on; Bronco Raptor 2022-on (Amber)","Baja Designs","$700–$780",{"mount":"fog-pocket","trim":"Raptor"},"Amber version of #2."),
 ("B09TXKDVH3","Baja Designs S2 Pro LED Dual Fog Pocket Light Kit for Ford F-150 Raptor 2021-22 (Multi-Pattern; Clear)","Baja Designs","Check listing",{"mount":"fog-pocket","trim":"Raptor","year_to":2022},"Raptor 2021-22 listing; confirm later years."),
 ("B0B8Q17MHM","Diode Dynamics Stage Series Backlit Ditch Light Kit compatible with Ford F-150 2021-2026, SS3 Sport White Combo","Diode Dynamics","Check listing",{"mount":"a-pillar"},"Complete kit with SS3 Sport pods; confirm contents."),
 ("B0B8PHBVC5","Diode Dynamics Stage Series Backlit Ditch Light Kit compatible with Ford F-150 2021-2026, C2 1.0 Pro White Combo","Diode Dynamics","Check listing",{"mount":"a-pillar"},"Complete kit with C2 Pro pods; confirm contents."),
 ("B0B8PLJ7KK","Diode Dynamics Stage Series Fog Pocket Kit compatible with Ford F-150 2021-2023, White Sport","Diode Dynamics","Check listing",{"mount":"fog-pocket","year_to":2023},"Listed 2021-2023; confirm DRL / trim fit."),
 ("B0B8QDXMVP","Diode Dynamics SS5 Bumper LED Pod Light Kit compatible with Ford F-150 2021-2023, Bracket Only","Diode Dynamics","Check listing",{"mount":"bumper","year_to":2023},"Brackets only; listed 2021-2023 — confirm."),
]
