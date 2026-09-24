"""Editorial for the v2 batch (59 pages). Category templates + vehicle-specific gotchas/FAQ.
Same tuple shape as pages_v1.PAGES: (make, model, gen, category, title, meta, intro, gotchas[], faq[(q,a)], verdict)
Rule: vehicle facts only where we are sure; anything seller-dependent is phrased as "confirm on the listing".
"""

PAGES = []

def P(make, model, gen, cat, name, gotchas, faq=(), spec="", verdict=None):
    """name = '2015–2020 Ford F-150'; spec = short title suffix e.g. 'SuperCrew'."""
    t = TEMPLATES[cat]
    title = t["title"].format(name=name, spec=f" ({spec})" if spec else "")
    PAGES.append((make, model, gen, cat, title, t["meta"].format(name=name), t["intro"].format(name=name),
                  list(gotchas) + t["gotchas"], list(faq) + t["faq"], verdict or t["verdict"]))

TEMPLATES = {
 "floor-mats": dict(
  title="Best Floor Mats & Liners for {name}{spec}",
  meta="Laser-fit floor liners and all-weather mats checked against the {name} by cab, seating and storage layout — plus the layout gotchas that cause returns.",
  intro="Every set below is listed for the {name}, not a 'universal trim-to-fit' mat. Liners fail for three reasons: wrong generation, wrong seating layout (bench vs buckets, 2nd-row captain's chairs vs bench) and wrong under-seat storage. Check those three against the notes on each pick and the fit is a non-issue.",
  gotchas=["**Retention hooks**: factory driver-side hooks must line up — a mat without hook holes will slide under the pedals. All picks here are cut for the factory posts.",
           "**Stacking**: never lay a liner on top of the carpet mat. Remove the factory mat first."],
  faq=[("TPE liners or rubber mats?","TPE liners (raised edges, laser-measured) hold water and snow and look OEM; rubber mats are cheaper, heavier and grip better but cover less of the footwell."),
       ("Do I need the 2nd-row piece?","Yes if anyone rides back there — mud collects on the rear floor first. Most sets here include 1st + 2nd row; 3rd-row and cargo liners are usually separate.")],
  verdict="**Budget:** a molded rubber set listed for your layout. **Best overall:** TPE laser-fit liners, 1st + 2nd row. **Premium:** maximum-coverage liners that run up the door sills."),
 "tonneau-covers": dict(
  title="Best Tonneau Covers for {name}{spec}",
  meta="Tonneau covers fit-checked for the {name} by bed length, with the rail and tailgate gotchas that decide whether a cover seals.",
  intro="A tonneau cover fits by bed length first and rail design second — brand is a distant third. Measure inside the bed from bulkhead to tailgate before you order, then match the listing to that number. Soft roll-ups are cheapest, hard tri-folds are the value pick and retractables seal best.",
  gotchas=["**Bed liners**: over-rail drop-in liners can block clamp rails; under-rail liners and spray-in are fine.",
           "**Toolboxes**: a crossover toolbox needs a toolbox-compatible (shortened) cover."],
  faq=[("Hard or soft cover?","Hard tri-folds carry snow and light loads and lock with the tailgate; soft roll-ups are lighter, cheaper and roll fully open for tall cargo."),
       ("Do I need to drill?","No — every cover here clamps to the bed rails.")],
  verdict="**Budget:** soft roll-up for your bed length. **Best overall:** hard tri-fold. **Premium:** retractable with a canister."),
 "roof-racks": dict(
  title="Best Roof Racks & Crossbars for {name}{spec}",
  meta="Crossbars matched to the {name}'s roof type — raised rails, flush rails or fixed points — with load limits and trim exceptions.",
  intro="Crossbars fit by roof type, not by vehicle name alone. The {name} ships with a specific rail style, and some trims differ; a bar kit built for raised rails will not clamp to flush rails and vice-versa. Every pick below states the roof it fits — match it to your roof, then stay under the roof's dynamic load rating (bars + cargo).",
  gotchas=["**Dynamic vs static load**: the roof rating is for driving. The bar's own rating (often 150–300 lb) does not raise the vehicle's limit.",
           "**Wind noise**: aero (wing) bars are quieter than square bars; set bars 24–32 in apart for boxes and bike trays."],
  faq=[("Can I carry a rooftop tent?","Only if the tent plus bars stays within the roof's dynamic rating while driving. Parked (static) capacity is higher, but manufacturers rarely publish it."),
       ("Do these fit without drilling?","Yes — all clamp to the factory rails or fixed points.")],
  verdict="**Budget:** lockable aluminum bars listed for your rail type. **Best overall:** aero bars with locks. **Premium:** a brand-name tower + bar system."),
 "hitches": dict(
  title="Best Trailer Hitches for {name}{spec}",
  meta="Bolt-on receiver hitches listed for the {name}, with receiver size, the vehicle's real tow limit and what the hitch rating does not change.",
  intro="A hitch is rated for what the hitch can carry; your {name} is rated for what the vehicle can pull. The lower number always wins. The picks below bolt to existing frame holes with no welding — the brand-name options come with engineering data, the budget ones are fine for bike racks and cargo carriers.",
  gotchas=["**Wiring**: lights need a vehicle-specific T-connector harness; buy it with the hitch.",
           "**Tongue weight**: e-bike racks with two bikes can exceed 150 lb on the tongue — check both hitch and rack ratings."],
  faq=[("Does a Class 3 hitch let me tow more?","No. It only means the receiver is 2 in. The vehicle's tow rating in the owner's manual is the legal and safe limit."),
       ("Do I need to cut the bumper fascia?","Some kits need a small trim of the lower fascia; the listing says so. Most on this page are fully concealed or bolt under the bumper.")],
  verdict="**Best overall:** the CURT / Draw-Tite / Reese listing for your model. **Budget:** a bolt-on 2 in receiver for bike racks. **Add:** the matching wiring harness."),
 "running-boards": dict(
  title="Best Running Boards & Side Steps for {name}{spec}",
  meta="Running boards and nerf bars listed for the {name} by cab length, with bracket, drop-step and power-step notes.",
  intro="Running boards fit by cab length and mounting brackets. The {name} has factory threaded mounting points on the rocker, so bolt-on kits need no drilling — but a Crew Cab board will not fit an extended cab. Match the cab, then pick the step style: flat boards look OE, drop steps help shorter riders, power steps hide when the doors close.",
  gotchas=["**Lift kits**: a 2 in+ lift makes flat boards less useful — drop steps suit lifted trucks better.",
           "**Power steps** need a wiring connection; budget kits vary in harness quality, so confirm install instructions before buying."],
  faq=[("Do running boards reduce ground clearance?","Slightly — boards sit a few inches below the rocker. Off-road, rock sliders or power steps are the better choice."),
       ("How much weight do they hold?","Most rate 300–550 lb per side; the listing states it.")],
  verdict="**Budget:** tube nerf bars for your cab. **Best overall:** 6 in aluminum or carbon-steel boards. **Premium:** power-deployable steps."),
}

# ================================================================ FLOOR MATS
P("ford","f-150","2015-2020","floor-mats","2015–2020 Ford F-150",[
  "**13th-gen only** (P552). 2021+ floors differ; don't cross-shop listings that stop at 2020 with 2021+.",
  "**Fold-flat rear storage**: some SuperCrews have the rear under-seat fold-flat load floor — several liners say 'not for fold-flat storage'. Look under the rear seat before ordering.",
  "**Front bench vs buckets** changes the front hump piece — check your console."],
  [("Do 2021+ F-150 liners fit a 2019?","No — the 14th gen changed the floor pan and console.")], spec="SuperCrew")
P("chevrolet","silverado-1500","2019-present","floor-mats","2019–2025 Chevy Silverado 1500",[
  "**Rear under-seat storage**: T1 Crew Cabs came with no box, a plastic storage box or carpeted storage. Liners are cut for one — check under the rear bench.",
  "**Front bench vs buckets**: bench trucks have a flat center; bucket-seat liners have a console cutout.",
  "**2019 LD / Limited** is the old body — these liners won't fit."], spec="Crew Cab")
P("gmc","sierra-1500","2019-present","floor-mats","2019–2025 GMC Sierra 1500",[
  "**Same floor as the Silverado** — Silverado/Sierra liners interchange; storage layout still matters.",
  "**Denali / AT4 bucket seats** need console-cut front liners.",
  "**2019 Limited** is the old body."], spec="Crew Cab")
P("ram","1500","2019-present","floor-mats","2019–2025 Ram 1500 DT",[
  "**DT vs Classic**: the Ram 1500 Classic (sold through 2024) has a different floor. All picks here are DT (new body).",
  "**Rear under-seat storage bins** change the 2nd-row liner — check under the rear seat.",
  "**Front bench vs buckets** changes the center piece."], spec="Crew Cab")
P("toyota","tacoma","2016-2023","floor-mats","2016–2023 Toyota Tacoma",[
  "**Access Cab vs Double Cab**: different rear floors; buy for your cab.",
  "**Manual vs automatic** changes the driver-side footwell on a few liners.",
  "**2024+ Tacoma** is a new platform — no crossover."], spec="Double Cab")
P("toyota","tacoma","2024-present","floor-mats","2024–2025 Toyota Tacoma",[
  "**New TNGA-F platform** — 2016–2023 liners do not fit.",
  "**i-FORCE MAX hybrid** has a battery under the rear seat on some trims; confirm the 2nd-row liner lists hybrid.",
  "**Double Cab vs XtraCab**: different rear layouts."], spec="Double Cab")
P("toyota","tundra","2022-present","floor-mats","2022–2025 Toyota Tundra",[
  "**CrewMax vs Double Cab**: different rear floors.",
  "**i-FORCE MAX hybrid** changes under-seat layout on some trims — check hybrid on the listing.",
  "**2014–2021 liners** don't fit the 3rd gen."], spec="CrewMax")
P("ford","ranger","2019-2023","floor-mats","2019–2023 Ford Ranger",[
  "**SuperCrew vs SuperCab**: different rear floors.",
  "**2024+ Ranger** is a new generation — no crossover.",
  "**Rear under-seat storage** varies; check the rear floor."], spec="SuperCrew")
P("chevrolet","colorado","2023-present","floor-mats","2023–2025 Chevy Colorado",[
  "**3rd gen only** — 2015–2022 liners don't fit the 2023+ floor.",
  "**Crew Cab only** in this generation, so layout is simple; confirm year range on the listing.",
  "**ZR2 / Trail Boss** share the floor."], spec="Crew Cab")
P("nissan","frontier","2022-present","floor-mats","2022–2025 Nissan Frontier",[
  "**2022+ interior is new** even though the frame carries over — many listings say 2005–2021; skip those.",
  "**Crew Cab vs King Cab**: different rear floors."], spec="Crew Cab")
P("toyota","4runner","2010-2024","floor-mats","2010–2024 Toyota 4Runner",[
  "**Sliding rear cargo deck** (optional) changes the cargo liner; floor liners are unaffected.",
  "**3rd-row option** (SR5/Limited) needs a 3rd-row piece.",
  "**Early vs late 5th gen**: a few liners split 2010–2012 and 2013+ at the driver retention post — check."])
P("jeep","wrangler","2018-present","floor-mats","2018–2025 Jeep Wrangler JL",[
  "**2-door vs 4-door** (Unlimited): different rear floors.",
  "**4xe plug-in hybrid** has a raised rear floor — needs 4xe-specific rear liners.",
  "**Drain plugs**: JL floors have drain plugs; liners with drain cut-outs are a nice-to-have."])
P("ford","bronco","2021-present","floor-mats","2021–2025 Ford Bronco",[
  "**2-door vs 4-door** rear floors differ.",
  "**Not Bronco Sport** — different vehicle entirely.",
  "**Washout interior** option already has rubber floors; liners still help with containment."])
P("toyota","highlander","2020-present","floor-mats","2020–2025 Toyota Highlander",[
  "**Captain's chairs vs 2nd-row bench** changes the 2nd-row liner.",
  "**Hybrid** has a different rear floor on some years — confirm hybrid on the listing.",
  "**Not Grand Highlander** — different vehicle."])
P("subaru","forester","2019-2024","floor-mats","2019–2024 Subaru Forester",[
  "**SK generation only**; 2025+ is new.",
  "**Wilderness** shares the floor."])
P("tesla","model-3","2017-present","floor-mats","Tesla Model 3 (2024+ Highland)",[
  "**Highland (2024+) vs pre-Highland (2017–2023)**: the refresh changed the front footwells — our picks are Highland listings. Pre-Highland owners need 2017–2023 listings.",
  "**Frunk and trunk liners** are sold separately."])
P("ford","explorer","2020-present","floor-mats","2020–2025 Ford Explorer",[
  "**Captain's chairs vs 2nd-row bench** changes the 2nd-row liner.",
  "**3rd row** needs a 3-row set.",
  "**Hybrid / ST** share the floor on most listings — confirm."])
P("chevrolet","tahoe","2021-present","floor-mats","2021–2025 Chevy Tahoe",[
  "**Captain's chairs vs bench** in the 2nd row.",
  "**Tahoe vs Suburban**: same front, different cargo — floor sets usually interchange, cargo liners do not.",
  "**Yukon** shares the floor."])
P("kia","telluride","2020-present","floor-mats","2020–2025 Kia Telluride",[
  "**Captain's chairs (7-seat) vs bench (8-seat)** changes the 2nd-row liner.",
  "**2026 is a new generation** — check year ranges."])
P("hyundai","palisade","2020-2025","floor-mats","2020–2025 Hyundai Palisade",[
  "**Captain's chairs vs bench** in the 2nd row.",
  "**2026 Palisade is a new generation** — these liners stop at 2025."])
P("honda","pilot","2023-present","floor-mats","2023–2025 Honda Pilot",[
  "**4th gen only**; 2016–2022 liners don't fit.",
  "**Removable 2nd-row middle seat** — liners cover both configurations; confirm on listing.",
  "**TrailSport** shares the floor."])
P("toyota","sequoia","2023-present","floor-mats","2023–2025 Toyota Sequoia",[
  "**3rd gen (TNGA-F)** — no crossover with 2008–2022.",
  "**Captain's chairs vs bench** in the 2nd row.",
  "**Sliding 3rd row / cargo shelf** changes the cargo liner."])
P("ford","maverick","2022-present","floor-mats","2022–2025 Ford Maverick",[
  "**Hybrid vs EcoBoost**: the rear under-seat floor differs — hybrid liners won't fit an EcoBoost and vice-versa. Check your powertrain.",
  "**AWD EcoBoost** shares the EcoBoost floor."])
P("toyota","rav4","2019-present","floor-mats","2019–2025 Toyota RAV4",[
  "**Hybrid / Prime** have different rear floors on some listings — confirm.",
  "**Cargo liner** varies with the adjustable cargo floor height."])
P("subaru","outback","2020-present","floor-mats","2020–2025 Subaru Outback",[
  "**6th gen (BT) only**.",
  "**Wilderness** shares the floor.",
  "**Not Legacy** — similar but different rear."])
P("jeep","gladiator","2020-present","floor-mats","2020–2025 Jeep Gladiator",[
  "**Different from Wrangler JL** in the rear — use Gladiator listings.",
  "**Rear under-seat storage** changes the 2nd-row liner — lift the seat."])

# ================================================================ TONNEAU
P("ford","f-150","2015-2020","tonneau-covers","2015–2020 Ford F-150",[
  "**Beds**: 5.5 ft (67.1 in), 6.5 ft (78.9 in), 8 ft (97.6 in). Measure.",
  "**BoxLink cleats** can interfere with some rails — remove them.",
  "**Covers listed 2015–2025** fit both 13th and 14th gen beds by the same length; the bed box carried over."],
  [("Do 2021+ F-150 covers fit a 2018?","Usually yes when the listing covers 2015–2025 — the bed dimensions carried over. Match bed length.")])
P("toyota","tacoma","2016-2023","tonneau-covers","2016–2023 Toyota Tacoma",[
  "**Beds**: 5 ft (60.5 in) and 6 ft (73.7 in).",
  "**Deck rail system** (factory side-rail tracks) blocks clamp rails on some covers — look for 'with deck rail'.",
  "**Bed-side storage box** (driver side, 2016+ some trims) can foul low-profile rails."])
P("ford","ranger","2019-2023","tonneau-covers","2019–2023 Ford Ranger",[
  "**Beds**: 5 ft (SuperCrew) and 6 ft (SuperCab).",
  "**2024+ Ranger** bed differs — check the year range stops at 2023 or explicitly spans both."])
P("chevrolet","colorado","2023-present","tonneau-covers","2023–2025 Chevy Colorado",[
  "**5 ft 2 in bed only** in this generation.",
  "**Many listings say 2015–2026** on one SKU even though the body changed in 2023 — buy 2023+-specific listings or confirm with the seller.",
  "**Storage bed rail / multi-pro tailgate** on some trims — confirm compatibility."])
P("nissan","frontier","2022-present","tonneau-covers","2022–2025 Nissan Frontier",[
  "**Beds**: 5 ft and 6 ft.",
  "**Utili-track** channels in the bed rails block clamp rails on some covers — look for Utili-track compatible."])

# ================================================================ ROOF RACKS
P("toyota","highlander","2020-present","roof-racks","2020–2025 Toyota Highlander",[
  "**Raised rails on most trims**; base L may ship bare — confirm your rails.",
  "**Not Grand Highlander**."])
P("subaru","forester","2019-2024","roof-racks","2019–2024 Subaru Forester",[
  "**Raised rails on every trim**, 176 lb dynamic.",
  "**Wilderness** has a different, higher-rated rail — Wilderness-specific bars."])
P("tesla","model-3","2017-present","roof-racks","Tesla Model 3",[
  "**Glass roof with fixed points** under the door seals — only fixed-point kits; never clamp-on gutter bars.",
  "**Tesla does not publish a high roof load** — keep loads light (bikes, a slim box)."])
P("hyundai","palisade","2020-2025","roof-racks","2020–2025 Hyundai Palisade",[
  "**Side rails on most trims**; some sellers describe them as flush — check whether there is a gap under your rails.",
  "**2026 is a new generation**."])
P("jeep","grand-cherokee","2022-present","roof-racks","2022–2025 Jeep Grand Cherokee",[
  "**Flush side rails** on most WL trims — raised-rail clamp bars will not fit.",
  "**Grand Cherokee L** shares the rail style; bars listed for both fit both."])
P("toyota","rav4","2019-present","roof-racks","2019–2025 Toyota RAV4",[
  "**Two rail styles**: standard raised rails vs Adventure / TRD Off-Road / Woodland rails. Bars are listed for one or the other.",
  "**Base LE** may ship without rails."])
P("kia","telluride","2020-present","roof-racks","2020–2025 Kia Telluride",[
  "**X-Line / X-Pro** have a taller rail — use X-Line/X-Pro-specific bars.",
  "**2026 is a new generation**."])
P("ford","explorer","2020-present","roof-racks","2020–2025 Ford Explorer",[
  "**Raised rails vs flush rails**: most Explorers have raised side rails; check for a gap under the rail before buying clamp bars.",
  "**ST and Timberline** share the rail style on most listings — confirm."])

# ================================================================ HITCHES
P("jeep","wrangler","2018-present","hitches","2018–2025 Jeep Wrangler JL",[
  "**Factory hitch** comes with the tow package on many JLs — check under the rear bumper first.",
  "**Tow rating** 2018–2023: 2,000 lb (2-door) / 3,500 lb (4-door). 2024+: 3,500 lb (2-door) / 5,000 lb (4-door, V6 or 2.0T, 8-speed, tow pkg). 4xe and 392: 3,500 lb.",
  "**Aftermarket steel bumpers** often have their own receiver."])
P("ford","explorer","2020-present","hitches","2020–2025 Ford Explorer",[
  "**Factory Class 3/4 receiver** is standard or packaged on many trims — check before buying.",
  "**Tow rating** varies 5,000–5,600 lb by engine and package; the owner's manual rules."])
P("honda","pilot","2023-present","hitches","2023–2025 Honda Pilot",[
  "**Honda tow package** is dealer-installed on many trucks; TrailSport often has it standard — check first.",
  "**Tow rating** 5,000 lb (AWD) — the hitch rating doesn't raise it."])
P("honda","cr-v","2023-present","hitches","2023–2025 Honda CR-V",[
  "**Tow rating** is 1,500 lb — the hitch here is mainly for bike racks and cargo carriers.",
  "**Hybrid**: confirm the listing covers hybrid; exhaust and spare layout differ."])
P("jeep","grand-cherokee","2022-present","hitches","2022–2025 Jeep Grand Cherokee",[
  "**Factory Class 4 receiver** with the tow package — check first.",
  "**4xe** has different rear packaging on some listings — confirm."])
P("ford","bronco","2021-present","hitches","2021–2025 Ford Bronco",[
  "**Factory receiver** on many trims (and Sasquatch) — the CURT 13493 is only for trucks without one.",
  "**Not Bronco Sport** — different vehicle.",
  "**Modular steel bumper** trims may need a bumper-specific hitch."])
P("subaru","outback","2020-present","hitches","2020–2025 Subaru Outback",[
  "**Tow rating** 2,700 lb (2.5L) or 3,500 lb (XT turbo). Hitch rating does not raise it.",
  "**Legacy** shares the hitch but not the tow rating."])
P("kia","telluride","2020-present","hitches","2020–2025 Kia Telluride",[
  "**Tow rating** 5,000 lb; self-leveling rear suspension on some trims helps with tongue weight.",
  "**Palisade** shares most aftermarket hitches."])
P("hyundai","palisade","2020-2025","hitches","2020–2025 Hyundai Palisade",[
  "**Tow rating** 5,000 lb.",
  "**Telluride hitches** usually interchange — the listing names both."])
P("subaru","forester","2019-2024","hitches","2019–2024 Subaru Forester",[
  "**Tow rating** 1,500 lb (3,000 lb Wilderness) — a 2 in hitch is for bike racks, not heavier towing.",
  "**1.25 in vs 2 in**: many bike racks need 2 in; Class 2 hitches take 1.25 in racks only."])
P("tesla","model-3","2017-present","hitches","Tesla Model 3",[
  "**No US tow rating** from Tesla for most Model 3s — treat these as bike-rack / cargo-carrier hitches.",
  "**Highland (2024+) vs 2017–2023**: rear fascia differs; match the listing year."])

# ================================================================ RUNNING BOARDS
P("ford","f-150","2021-present","running-boards","2021–2025 Ford F-150",[
  "**SuperCrew vs SuperCab**: board length differs — picks here are SuperCrew.",
  "**Factory power boards** (Platinum/Limited) — remove before fitting fixed boards.",
  "**Lightning** shares the SuperCrew rocker; confirm listing."], spec="SuperCrew")
P("chevrolet","silverado-1500","2019-present","running-boards","2019–2025 Chevy Silverado 1500",[
  "**Crew Cab vs Double Cab** — picks are Crew Cab.",
  "**2019 LD** is the old body.",
  "**HD (2500/3500)** shares the Crew Cab rocker on most listings."], spec="Crew Cab")
P("gmc","sierra-1500","2019-present","running-boards","2019–2025 GMC Sierra 1500",[
  "**Same rocker as Silverado** Crew Cab.",
  "**AT4X / Denali Ultimate** may have factory power steps."], spec="Crew Cab")
P("ram","1500","2019-present","running-boards","2019–2025 Ram 1500 DT",[
  "**DT vs Classic** — picks are DT (new body).",
  "**Quad Cab vs Crew Cab** board lengths differ."], spec="Crew Cab")
P("toyota","tundra","2022-present","running-boards","2022–2025 Toyota Tundra",[
  "**CrewMax vs Double Cab** board lengths differ.",
  "**TRD Pro / Capstone** may have factory steps or sliders."], spec="CrewMax")
P("chevrolet","tahoe","2021-present","running-boards","2021–2025 Chevy Tahoe",[
  "**Tahoe vs Suburban** have different wheelbases — boards are not interchangeable.",
  "**Yukon (not XL)** shares the Tahoe length."])
P("toyota","sequoia","2023-present","running-boards","2023–2025 Toyota Sequoia",[
  "**3rd gen only**.",
  "**TRD Pro** has factory rock rails on some model years — confirm."])
P("toyota","tacoma","2024-present","running-boards","2024–2025 Toyota Tacoma",[
  "**Double Cab vs XtraCab** lengths differ.",
  "**Trailhunter / TRD Pro** have factory rock rails."], spec="Double Cab")
P("nissan","frontier","2022-present","running-boards","2022–2025 Nissan Frontier",[
  "**Crew Cab vs King Cab** lengths differ.",
  "**Listings spanning 2005–2025** fit the same frame mounts per sellers, but confirm 2022+ bracket fit before ordering."], spec="Crew Cab")
