// Category-level buying copy for /guides and /guides/[category].
// Rules only: no product claims, no invented test results. Vehicle-specific detail lives in each guide.

export type GuideCopy = {
  blurb: string;                 // one line for the /guides card
  intro: string;                 // opening paragraph
  fit: [string, string][];       // "What decides fit"
  mistakes: [string, string][];  // "Common mistakes"
  faq: [string, string][];
};

export const GUIDE_COPY: Record<string, GuideCopy> = {
  "tonneau-covers": {
    blurb: "Matched to your bed length, rail system and tailgate, not just the badge.",
    intro: "A tonneau cover fits a truck bed, not a truck name. The same model can come with two or three bed lengths, and a new generation often brings a new bed, with different rails, a different tailgate and a different part number. Every guide below is written for one generation and lists which bed and option packages each cover is sold for.",
    fit: [
      ["Bed length", "Measure inside the bed along the top of the rail, from the bulkhead to the closed tailgate. Covers are sold by nominal bed size (5.5 ft, 6.5 ft, 8 ft and so on). A cover for the wrong length won't seal or latch."],
      ["Generation and model year", "When a truck is redesigned, the bed usually changes too, so covers rarely carry over to the next generation. Check the model years in the listing, not just the model name."],
      ["Factory bed options", "Rail and storage systems such as deck rails, cargo-management tracks, RamBox bins and composite or multi-function tailgates can each need a dedicated kit or rule a cover out altogether. Each guide lists the options that matter for that truck."],
      ["Cover style", "Soft roll-ups are the cheapest and give full bed access. Hard tri-folds and quad-folds add security and fold toward the cab. Retractables roll into a canister, which takes some bed space. One-piece hinged covers look clean but lift as one panel."],
    ],
    mistakes: [
      ["Ordering by cab instead of bed", "Crew-cab and extended-cab trucks often share a bed length, and the same cab can come with a longer bed. The bed length is what decides fit."],
      ["Expecting a waterproof bed", "Most covers are water-resistant, not waterproof. Seals keep most rain out, and retractables usually need their drain tubes connected. Don't leave electronics in the bed and assume they'll stay dry."],
      ["Forgetting the rest of the setup", "Bed racks, toolboxes, bed caps and some bed liners can clash with the cover's rails. If you plan to add a rack, check that the cover and the rack are listed as compatible."],
    ],
    faq: [
      ["Will a tonneau cover from my old truck fit my new one?", "Only if the new truck has the same bed. Within a generation it often will. Across generations it usually won't, because the bed rails, the length or the tailgate change."],
      ["Which tonneau cover type is most secure?", "Hard covers that lock with the tailgate (folding, retractable or one-piece) are harder to get into than soft roll-ups, which can be cut. None are as secure as a locked cab."],
      ["Can I run a bed rack with a tonneau cover?", "Yes, but only with parts made to work together. Some racks mount to the cover's rails or to the bed's rail system. Check both listings for compatibility before buying either."],
    ],
  },
  "bed-racks": {
    blurb: "Rack height, mounting method and load ratings matched to your bed.",
    intro: "A bed rack turns a pickup bed into a platform for a rooftop tent, fuel cans or recovery gear. Fit depends on the bed's length and rails, and on what else you want in the bed: a tonneau cover, a bed cap or a drawer system. Each guide below covers one generation and notes which racks clamp on and which bolt to factory rail points.",
    fit: [
      ["Bed length and rails", "Racks are sized to the bed, and many use factory rail systems or stake pockets to mount. A rack for the short bed won't reach the mounting points on a long bed."],
      ["Mounting method", "Clamp-on racks don't need drilling and come off easily. Rail-mounted racks use factory deck rails or tracks. Drill-in racks are the stiffest but make permanent holes."],
      ["Height", "Low racks sit near cab height to cut wind noise and drag. Mid-height racks leave room to reach the bed under a tent. Full-height racks give the most storage underneath."],
      ["Load ratings", "Makers usually give a dynamic rating (while driving) and a higher static rating (parked, e.g. with people sleeping in a tent). Keep the tent, gear and rack inside the dynamic figure on the road."],
    ],
    mistakes: [
      ["Ignoring the dynamic rating", "The larger static number is for a parked truck. A heavy tent plus gear can exceed the dynamic rating, especially on washboard roads."],
      ["Buying the rack before the cover", "Not every rack works with every tonneau cover. Decide on both, or buy a rack that's listed for your cover."],
      ["Blocking the tailgate or third brake light", "Check the rack's clearance and whether it covers the cab-mounted brake light, which many states require to be visible."],
    ],
    faq: [
      ["Can I put a rooftop tent on a bed rack?", "Yes, if the rack's dynamic rating covers the tent's weight while driving and its static rating covers the tent plus the people in it when parked."],
      ["Do bed racks cause wind noise?", "Some do, mainly when the crossbars sit above the cab. Lower racks and fairings reduce it."],
      ["Will a bed rack fit with a tonneau cover?", "Many do when mounted to the bed rails or a compatible cover rail. Check that the rack maker lists your cover."],
    ],
  },
  "roof-racks": {
    blurb: "Crossbars matched to your roof type: bare, raised rails, flush rails or fixed points.",
    intro: "A roof rack starts with the roof, not the brand. Bare roofs, raised side rails, flush rails and fixed mounting points each need a different foot or clamp, and trims of the same model can come with different roofs. Each guide below is written for one generation and lists which roof each crossbar kit fits.",
    fit: [
      ["Roof type", "Raised rails have a gap under the rail for clamp-on feet. Flush rails sit tight to the roof and need flush-rail kits. Fixed points are hidden mounts under covers. Bare roofs need door-jamb clips. A kit for one roof type won't fit another."],
      ["Trim and body", "Base trims may ship with a bare roof while higher trims get rails. Three-row, long-wheelbase and removable-top versions can need different kits."],
      ["Roof load limit", "The owner's manual lists a dynamic roof limit. It includes the rack itself, so subtract the bars and feet before adding boxes, bikes or a tent."],
      ["Crossbar spread and length", "Factory mounting points fix the spread on many vehicles. Bar length and position affect what fits: a cargo box, bikes and kayaks side by side, or clearance for a sunroof or rear hatch."],
    ],
    mistakes: [
      ["Using raised-rail bars on flush rails", "Clamp feet made for raised rails can't grip a flush rail. Check which rail type you have before ordering."],
      ["Forgetting the rack's own weight", "A 150 lb roof limit isn't 150 lb of gear once 15–25 lb of bars and feet are on the roof."],
      ["Not checking the rear hatch", "Long bars or loads mounted far back can hit the open liftgate. Test before loading."],
    ],
    faq: [
      ["Can I use factory crossbars and aftermarket accessories?", "Usually, if the accessory's mount fits the bar profile (square, round, aero or factory shape). Check the accessory's bar compatibility list."],
      ["Do roof racks hurt fuel economy?", "Yes, some, especially with loads on them. Aero bars cause less drag than square bars, and taking bars off when you don't need them helps most."],
      ["Is the roof rating for the rack or the roof?", "Both apply. Stay under the lower of the vehicle's dynamic roof limit and the rack's rating."],
    ],
  },
  "cargo-boxes": {
    blurb: "The box is universal; the bars, spread and hatch clearance decide fit.",
    intro: "Most cargo boxes fit most crossbars, so the real fit questions are about your vehicle: which bars its roof takes, how far apart they sit, how much weight the roof is rated for, and whether the liftgate still opens with the box on. Each guide below works through those for one generation.",
    fit: [
      ["Crossbars first", "A box clamps to crossbars, and the bars have to match the roof type. If you don't have bars yet, start with the roof rack guide for your vehicle."],
      ["Bar spread", "Box mounting hardware only reaches a certain range of spreads. Vehicles with fixed mounting points set the spread for you, so check it against the box's range."],
      ["Weight", "Box weight, bar weight and cargo together must stay under the roof's dynamic limit. A large box can take up half of a small SUV's roof limit before anything goes in it."],
      ["Liftgate and antenna clearance", "Slide the box forward far enough that the open liftgate clears it, and check sunroof and shark-fin antenna clearance up front."],
    ],
    mistakes: [
      ["Picking by volume alone", "A long box can hit the liftgate on a short roof. Length matters more than liters on compact SUVs."],
      ["Overloading", "Pack light, bulky items in the box and keep heavy gear inside the vehicle."],
      ["Skipping the side-opening check", "Dual-side opening boxes are easier to reach in parking lots, but only if the box sits where you can reach both sides."],
    ],
    faq: [
      ["Do I need special crossbars for a cargo box?", "No, most boxes fit round, square and aero bars with their standard clamps. Very thick factory bars can need a different mounting kit."],
      ["How big a cargo box can my SUV take?", "Check the roof length between the windshield and the open liftgate, the bar spread and the roof load limit. Each guide gives these for its vehicle."],
      ["Can I leave a cargo box on all year?", "You can, but it adds drag and wind noise. Many owners take it off between trips."],
    ],
  },
  "hitches": {
    blurb: "Receiver size, hitch class and your vehicle's own tow rating, which always wins.",
    intro: "A hitch never increases what your vehicle can tow. The usable rating is the lower of the hitch's rating and the vehicle's own tow and tongue-weight limits, which change with engine, drivetrain and tow package. Each guide below lists the factory ratings for one generation and the receiver hitches listed for it.",
    fit: [
      ["Receiver size", "1.25 in receivers suit bike racks and light loads. 2 in is the common size for towing and most hitch accessories. 2.5 in is for heavy-duty towing. Match the receiver to what you plan to put in it."],
      ["Hitch class", "Classes I–V rate the hitch for gross trailer weight and tongue weight. The class is the hitch's limit, not your vehicle's."],
      ["Vehicle tow rating", "Your owner's manual or the maker's towing guide gives the rating for your exact configuration. The lower of vehicle and hitch applies."],
      ["Wiring and brakes", "Trailers need working lights, usually through a 4-pin or 7-pin connector. Heavier trailers need electric brakes and a brake controller. Check your vehicle's harness options."],
    ],
    mistakes: [
      ["Assuming a Class IV hitch means Class IV towing", "A 10,000 lb hitch on a 3,500 lb-rated SUV is still limited to 3,500 lb."],
      ["Forgetting tongue weight", "Tongue weight should typically be around 10–15% of trailer weight, and it has to fit inside both the hitch's and the vehicle's tongue-weight limits."],
      ["Buying a hitch when one is already there", "Many trucks and tow-package vehicles have a factory receiver. Check under the rear bumper first."],
    ],
    faq: [
      ["Can I put a bike rack on any hitch?", "Check the rack's required receiver size and the hitch's tongue-weight rating. Heavy e-bike racks often need a 2 in receiver."],
      ["Do I need to drill to install a hitch?", "Most custom-fit hitches bolt to existing frame holes. Some vehicles need a bumper trim or heat-shield cut. Each guide notes this where the listing says so."],
      ["What wiring do I need?", "A vehicle-specific T-connector harness is the simplest for 4-pin lights. Towing heavier trailers usually means a 7-pin connector and a brake controller."],
    ],
  },
  "floor-mats": {
    blurb: "Liners matched to your model year, seating layout and console.",
    intro: "Floor liners are cut to one vehicle's floor pan, so they are generation-specific and often layout-specific too. Bench versus bucket seats, the number of rows, underseat storage and hybrid versions can each change the part number. Each guide below covers one generation and shows which layout each set fits.",
    fit: [
      ["Generation and model year", "Floors change with redesigns and sometimes mid-generation. The listing's model years matter more than the model name."],
      ["Seating layout", "Front bench versus buckets, second-row bench versus captain's chairs, and whether there is a third row all change the rear liner and sometimes the front."],
      ["Storage and console", "Underseat bins, fold-flat floors and console shapes need matching cutouts, or the liner won't lie flat."],
      ["Retention hooks", "Driver-side liners should lock onto the factory retention posts or hooks so the mat can't slide under the pedals."],
    ],
    mistakes: [
      ["Stacking mats", "Never put a liner on top of the factory carpet mat. Stacked mats can bunch up and catch the pedals."],
      ["Buying trim-to-fit for the driver side", "Universal mats may not reach the retention posts and can slide forward. Use a custom-fit liner for the driver's side."],
      ["Choosing the wrong rear row", "Captain's-chair and bench versions use different second-row liners. Check your seats before ordering."],
    ],
    faq: [
      ["What's the difference between floor mats and floor liners?", "Mats are mostly flat. Liners have raised edges that run up the sides of the footwell to hold water, mud and snow."],
      ["Are TPE liners better than rubber?", "TPE is lighter, stiffer and has little odor. Rubber is heavier and more flexible in the cold. Both work, so fit and coverage matter more."],
      ["Do I need all three rows?", "Only if you use the third row. Many owners buy front and second-row sets first and add a cargo liner."],
    ],
  },
  "running-boards": {
    blurb: "Cab length, mounting points and step style for your truck or SUV.",
    intro: "Running boards, nerf bars and drop steps all bolt to the vehicle's rocker or body mounts, so the cab length and generation decide which kit fits. Each guide below covers one generation and notes which cab each board is sold for.",
    fit: [
      ["Cab length", "Crew, double, extended and regular cabs need different board lengths. A crew-cab board won't fit an extended cab."],
      ["Mounting points", "Most kits use existing body mounts with no drilling. Some trims have factory rock rails or rocker covers that need removing first."],
      ["Step style", "Flat boards run the full cab length. Nerf bars are tubes with step pads. Drop steps sit lower for lifted trucks. Power steps deploy when the door opens and need wiring."],
      ["Ground clearance", "Anything hanging below the rocker reduces side clearance off-road. Slim boards or slider-style steps suit trail use."],
    ],
    mistakes: [
      ["Ordering for the wrong cab", "Check the cab name on your truck, not only the bed length, before you order."],
      ["Using running boards as rock sliders", "Most boards are built for stepping, not for taking the truck's weight on rocks. Use sliders made for that."],
      ["Ignoring the height", "On lifted or tall trucks, a flush board may still leave a big step. A drop step or wider pad helps."],
    ],
    faq: [
      ["Do running boards need drilling?", "Most custom-fit kits bolt to existing mounting points. Check the listing for your trim."],
      ["What's the difference between nerf bars and running boards?", "Nerf bars are round or oval tubes with small step pads. Running boards are wider, flat platforms along the whole cab."],
      ["Are power running boards worth it?", "They tuck away for clearance and look clean, but they cost more, need wiring and have motors that can fail in mud or salt."],
    ],
  },
  "led-light-bars": {
    blurb: "Mounting brackets are vehicle-specific; the light bars aren't. Check your state's rules.",
    intro: "Light bars are mostly universal, so fit comes down to brackets that match your vehicle's bumper, hood, A-pillar or windshield frame, and a harness that wires in safely. Each guide below covers mounting spots and bracket kits for one generation.",
    fit: [
      ["Mounting location", "Bumper, grille, hood, A-pillar and windshield-frame mounts each take different brackets and bar lengths."],
      ["Bar length and curve", "Windshield and roof mounts usually need a curved bar of a set length, and bumper openings limit the size."],
      ["Wiring", "Use a harness with a relay, a fuse and a switch. Tapping into existing circuits without a relay can overload them."],
      ["Beam pattern", "Spot beams reach far, flood beams light wide, and combo bars do both. Choose for the kind of driving you do."],
    ],
    mistakes: [
      ["Using off-road lights on public roads", "Many states restrict auxiliary off-road lights on public roads and may require them to be covered or off. Check your state's rules."],
      ["Drilling when a bracket exists", "Vehicle-specific brackets often use factory bolts. Check before drilling."],
      ["Skipping the relay", "High-draw bars without a relay can burn out switches and wiring."],
    ],
    faq: [
      ["Are LED light bars street legal?", "Rules vary by state. Many treat them as off-road lights that must be off, and sometimes covered, on public roads."],
      ["Where should I mount a light bar?", "Bumper and grille mounts cause less glare off the hood. Roof and windshield mounts light farther but can glare and add wind noise."],
      ["Do I need a wiring harness?", "Yes. A harness with a relay, fuse and switch is the safe way to wire a high-draw light bar."],
    ],
  },
};
