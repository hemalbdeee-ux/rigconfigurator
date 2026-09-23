"""Product shortlist for the first 30 money pages. ASINs taken from Amazon listing titles that state the fitment
(source=amazon-listing, confidence 2). Promote to confidence 3 after checking the manufacturer fit guide.
Run `python db/content/build_fitments_csv.py` → pipeline/data/fitments.csv
Row: (asin, name, brand, category, price_band, make, model, gen, condition dict, note, rank)
"""
F = []
def add(make, model, gen, cat, rows):
    for i, (asin, name, brand, band, cond, note) in enumerate(rows, 1):
        F.append((asin, name, brand, cat, band, make, model, gen, cond, note, i))

# ---------------- F-150 2021+ tonneau
add("ford","f-150","2021-present","tonneau-covers",[
 ("B0B94WC2F1","Tyger Auto T3 Soft Tri-Fold Tonneau Cover, 2021-2026 F-150 & Lightning, 5.5 ft","Tyger Auto","$250–$320",{"bed_length_in":66},"Lists Lightning fitment; not for beds with utility track."),
 ("B0DK3928N1","OEDRO FRP Hard Tri-Fold Tonneau Cover, 2015-2025 F-150, 5.5 ft","OEDRO","$300–$400",{"bed_length_in":66},"Hard FRP panels; utility track must be removed."),
 ("B0C4G2H93V","XTWEEX Hard Tri-Fold Tonneau Cover, 2015-2026 F-150, 5.5 ft","XTWEEX","$300–$400",{"bed_length_in":66},"Fiberglass panels, no-drill clamps."),
 ("B0BXVQ85RQ","Just-V Hard Tri-Fold Tonneau Cover, 2015-2026 F-150 Crew Cab, 5.5 ft (excl. Raptor)","Just-V","$300–$380",{"bed_length_in":66},"Excludes Raptor."),
 ("B0C4FWZZFV","Soft Roll-Up Tonneau Cover, 2015-2026 F-150, 6.5 ft Standard Box","Generic","$150–$200",{"bed_length_in":78},"6.5 ft bed only."),
 ("B0CFXLJYBM","Soft Roll-Up Tonneau Cover, 2015-2025 F-150 Fleetside, 6.5 ft (78.9 in)","Generic","$150–$200",{"bed_length_in":78},"6.5 ft bed only."),
])

# ---------------- Silverado 1500 2019+ tonneau
_SILV = [
 ("B0DH3VK6C4","Tono King FRP Hard Folding Tonneau Cover, 2019-2026 Silverado/Sierra 1500, 5'8\" bed","Tono King","$330–$420",{"bed_length_in":70},"Hard FRP tri-fold; steel beds only."),
 ("B07V31TZT5","Xcover Low Profile Hard Folding Tonneau Cover, 2019-2025 Silverado/Sierra 1500, 5.8 ft","Xcover","$380–$480",{"bed_length_in":70},"Low-profile aluminum; check Multi-Flex/MultiPro tailgate note on listing."),
 ("B0BXVYS2ND","Just-V Hard Tri-Fold Tonneau Cover, 2019-2024 Silverado/Sierra 1500 Crew Cab, 5.8 ft","Just-V","$300–$380",{"bed_length_in":70},"Crew Cab short bed only."),
 ("B082PJFTTB","OEDRO Soft Tri-Fold Tonneau Cover, 2019-2026 Silverado/Sierra 1500, 5.8 ft (no Multi-Flex tailgate)","OEDRO","$200–$260",{"bed_length_in":70},"Not for Multi-Flex / MultiPro tailgate."),
 ("B0CPY26JVS","Logan Soft Tri-Fold Tonneau Cover, 2019-2025 Silverado/Sierra 1500, 5.8 ft","Logan","$180–$240",{"bed_length_in":70},"Soft tri-fold."),
 ("B0B1DWQPT9","CAPSER Soft Tri-Fold Tonneau Cover, 2019-2026 Silverado/Sierra 1500, 5.8 ft","CAPSER","$180–$240",{"bed_length_in":70},"Soft tri-fold."),
 ("B0CFXP1Y3X","Soft Roll-Up Tonneau Cover, 2019-2025 Silverado/Sierra 1500, 6.6 ft (79.2 in)","Generic","$150–$210",{"bed_length_in":79},"Not for CarbonPro bed or cargo bar system."),
 ("B0CFV3DHSX","Soft Roll-Up Tonneau Cover, 2019-2025 Silverado/Sierra 1500, 6.6 ft (not Multi-Flex / CarbonPro)","Generic","$150–$210",{"bed_length_in":79},"Not for Multi-Flex tailgate or CarbonPro bed."),
 ("B0BS4GK568","Soft Roll-Up Tonneau Cover, 2014-2026 Silverado/Sierra 1500, 6.5 ft","Generic","$140–$200",{"bed_length_in":79},"Long production run; confirm 2019+ new body on listing."),
]
add("chevrolet","silverado-1500","2019-present","tonneau-covers",_SILV)
add("gmc","sierra-1500","2019-present","tonneau-covers",[(a,n,b,p,c,(note+" Not for CarbonPro composite bed.") if "CarbonPro" not in note else note) for a,n,b,p,c,note in _SILV])

# ---------------- Ram 1500 DT 2019+ tonneau (standard bed; RamBox covers are scarce on Amazon — list none rather than guess)
add("ram","1500","2019-present","tonneau-covers",[
 ("B0CJNN5QBN","Hard Tri-Fold Tonneau Cover, 2019-2025 Ram 1500 New Body & Classic, 5.7 ft, without RamBox","Generic","$300–$400",{"bed_length_in":67,"rambox":False},"Without RamBox only."),
 ("B07V1LCY6Q","Xcover Low Profile Hard Folding Tonneau Cover, 2019-2025 Ram 1500 New Body, 5.7 ft","Xcover","$380–$480",{"bed_length_in":67,"rambox":False},"Not for Classic body, track system, roll bar or multifunction tailgate."),
 ("B0C4G44H67","XTWEEX Hard Tri-Fold Tonneau Cover, 2009-2026 Ram 1500, 5.7 ft, without RamBox","XTWEEX","$300–$400",{"bed_length_in":67,"rambox":False},"Without RamBox only."),
 ("B0D2D3MPHY","ZTOP Hard Rolling Tonneau Cover, 2019-2026 Ram 1500 New Body, 5.7 ft, w/o RamBox","ZTOP","$450–$600",{"bed_length_in":67,"rambox":False},"Hard rolling (retractable-style)."),
 ("B0B14JJFC2","Retractable Hard Tonneau Cover, 2009-2024 Ram 1500 (Classic & New), 5.7 ft, w/o RamBox","Generic","$500–$700",{"bed_length_in":67,"rambox":False},"Aluminum retractable; verify 2025 on listing."),
 ("B09ZQDY22J","Xcover Soft Roll-Up Tonneau Cover, 2019-2026 Ram 1500 New Body, 5.7 ft","Xcover","$150–$210",{"bed_length_in":67,"rambox":False},"Soft roll-up."),
 ("B0F5H2L1V4","Soft Tri-Fold Tonneau Cover, 2009-2026 Ram 1500 (Classic & New), 5.7 ft, without RamBox","Generic","$170–$230",{"bed_length_in":67,"rambox":False},"Soft tri-fold."),
])

# ---------------- Tundra 2022+ tonneau
add("toyota","tundra","2022-present","tonneau-covers",[
 ("B0D49R24LT","Hard Folding Tonneau Cover, 2022-2026 Tundra, 5.5 ft Short Box","Generic","$300–$400",{"bed_length_in":66},"Hard tri-fold."),
 ("B0DCBZXMNQ","Hard Tri-Fold Tonneau Cover, 2022-2026 Tundra 5.5 ft, with or without deck rails","Generic","$300–$400",{"bed_length_in":66},"Works with the factory deck-rail system."),
 ("B0B4ZLRTYB","FeeTUO FRP Hard Tri-Fold Tonneau Cover, 2022-2026 Tundra 5.5 ft w/ OE rail system","FeeTUO","$320–$420",{"bed_length_in":66},"FRP panels; OE deck rails compatible."),
 ("B0G5PSKF6C","Soft Tri-Fold Tonneau Cover, 2022-2026 Tundra 5.5 ft with deck rail system (excl. Trail Edition)","Generic","$180–$240",{"bed_length_in":66},"Excludes Trail Edition."),
 ("B0D49QWMTR","Hard Folding Tonneau Cover, 2022-2026 Tundra, 6.5 ft Standard Box","Generic","$320–$420",{"bed_length_in":79},"6.5 ft bed."),
 ("B0D49TCXQW","Soft Quad-Fold Tonneau Cover, 2022-2026 Tundra, 6.5 ft Standard Box","Generic","$170–$230",{"bed_length_in":79},"6.5 ft bed."),
])

# ---------------- Gladiator tonneau
add("jeep","gladiator","2020-present","tonneau-covers",[
 ("B096KZ9CBP","UnderCover ArmorFlex Hard Folding Tonneau Cover AX32010, 2020-2025 Gladiator 5 ft","UnderCover","$900–$1,100",{"bed_length_in":60},"Premium armored hard fold; brand-name warranty."),
 ("B07WDYCKF8","UnderCover Flex Hard Folding Tonneau Cover FX31010, 2020-2025 Gladiator 5 ft","UnderCover","$800–$1,000",{"bed_length_in":60},"Premium hard fold."),
 ("B081S4JMG1","Gator EFX Hard Tri-Fold Tonneau Cover GC34010, 2020-2025 Gladiator 5 ft","Gator","$600–$800",{"bed_length_in":60},"Aluminum low-profile tri-fold."),
 ("B0CHVMX3VJ","Hard Folding Tonneau Cover, 2020-2026 Gladiator JT 5 ft, with or without Trail Rail","Generic","$300–$400",{"bed_length_in":60},"Trail Rail compatible."),
 ("B08X4SR8J2","OSOBAK Hard Tri-Fold Tonneau Cover, 2020-2026 Gladiator, compatible with factory utility track","OSOBAK","$300–$400",{"bed_length_in":60},"Trail Rail / utility track compatible."),
 ("B0CQV7GPJC","FASTFIT Hard Tri-Fold Tonneau Cover, 2020-2026 Gladiator 5 ft with track system","FASTFIT","$300–$400",{"bed_length_in":60},"Sits on top of the bed rails."),
 ("B0FHKL9D3X","Retractable Hard Tonneau Cover, 2020-2025 Gladiator 5 ft with deck rail, 600 lb","Generic","$500–$700",{"bed_length_in":60},"Aluminum slat retractable; no-drill."),
 ("B0BPQ6WLXZ","Toptiny Soft Folding Tonneau Cover TSTF031, 2020-2026 Gladiator 5 ft","Toptiny","$160–$220",{"bed_length_in":60},"Budget soft tri-fold."),
])

# ---------------- Maverick tonneau
add("ford","maverick","2022-present","tonneau-covers",[
 ("B0BNMKS29M","TIPTOP Hard Tri-Fold FRP Tonneau Cover TPM3, 2022-2026 Maverick 4.5 ft","TIPTOP","$300–$380",{"bed_length_in":54},"FRP hard tri-fold, on-top mount."),
 ("B0DWSHP5X9","Hard Tri-Fold Tonneau Cover, 2022-2026 Maverick 4.5 ft (54.4 in)","Generic","$280–$360",{"bed_length_in":54},"Hard tri-fold."),
 ("B0CG1M386H","PENSUN Hard Tri-Fold Tonneau Cover with LED lights, 2022-2025 Maverick 4.5 ft","PENSUN","$300–$400",{"bed_length_in":54},"Includes LED bed lights; no-drill."),
 ("B0F9WDPKR5","Soft Tri-Fold Tonneau Cover, 2022-2026 Maverick 4.5 ft","Generic","$150–$200",{"bed_length_in":54},"Soft tri-fold."),
 ("B0GFMF7Q37","Soft Tri-Fold Tonneau Cover, 2022-2025 Maverick Fleetside 4.6 ft (54.4 in)","Generic","$150–$200",{"bed_length_in":54},"Soft tri-fold."),
 ("B0C4G93K2C","Soft Tri-Fold Tonneau Cover, 2022-2025 Maverick 4.6 ft box","Generic","$150–$200",{"bed_length_in":54},"Soft tri-fold."),
])

# ---------------- Ranger 2024+ tonneau — sellers list 2019-2026 on one SKU; the 2024 bed differs, so confidence stays 1 until confirmed
add("ford","ranger","2024-present","tonneau-covers",[
 ("B0CHVLRZV9","Hard Folding Tonneau Cover, 2019-2026 Ranger 5 ft Short Box (seller lists both generations)","Generic","$300–$400",{"bed_length_in":60},"Seller claims 2019-2026; 2024+ bed differs — confirm with seller before buying."),
 ("B0D4Y4M3ZY","Hard Tri-Fold Aluminum Tonneau Cover with LED, 2019-2026 Ranger 5 ft (seller lists both generations)","Generic","$320–$420",{"bed_length_in":60},"Seller claims 2019-2026; confirm 2024+ fit."),
 ("B0CQV98BFT","FASTFIT Hard Tri-Fold Tonneau Cover, 2019-2025 Ranger 5 ft (61 in)","FASTFIT","$300–$400",{"bed_length_in":60},"Listed to 2025; confirm 2024+ fit with seller."),
])

# ---------------- Tacoma 2024+ tonneau (retractables confirmed; tri-folds added as listings appear)
add("toyota","tacoma","2024-present","tonneau-covers",[
 ("B0GTM1XFPB","Retractable Hard Aluminum Tonneau Cover, 2024-2026 Tacoma 5 ft (60 in)","Generic","$500–$700",{"bed_length_in":60},"Lockable, no-drill; confirmed 2024+ listing."),
 ("B0GV3XPK7S","Heavy-Duty Retractable Tonneau Cover, 2024-2025 Tacoma 4th Gen, 5 ft","Generic","$500–$700",{"bed_length_in":60},"Mechanical lock; confirmed 4th-gen listing."),
])

# Tacoma 2024+ hard tri-folds (appended)
add("toyota","tacoma","2024-present","tonneau-covers",[
 ("B0F24DTVS1","DNYKER Hard Tri-Fold Tonneau Cover, 2024-2026 Tacoma 5 ft with OE track system (excl. Trail Edition)","DNYKER","$300–$400",{"bed_length_in":60},"Confirmed 2024+ listing; excludes Trail Edition."),
 ("B0D9PT8T9F","YITAMOTOR FRP Hard Tri-Fold Tonneau Cover, 2024-2026 Tacoma 5 ft with deck rail system","YITAMOTOR","$300–$400",{"bed_length_in":60},"Confirmed 2024+ listing; excludes Trail Edition."),
])

# ---------------- Bed racks
add("toyota","tacoma","2016-2023","bed-racks",[
 ("B0DJ5ST21T","YZONA 13.3 in Overland Bed Rack with LED lights, 2016-2025 Tacoma with bed rails, 1,000 lb","YZONA","$350–$450",{},"Clamps to factory deck rails; low/mid height for tents."),
 ("B0BPHJTYD9","u-Box 19 in Full-Height Overland Bed Rack, Tacoma 5 ft bed / Gladiator / Ranger / Colorado","u-Box","$450–$600",{"bed_length_in":61},"Full height; 5 ft bed only."),
 ("B0BPM8R6GQ","Hooke Road 12.3 in Overland Bed Rack, Tacoma 5 ft / Gladiator / Ranger / Colorado","Hooke Road","$350–$450",{"bed_length_in":61},"Low-profile steel; 5 ft bed only."),
 ("B0DS2BHPLF","JOYTUTUS 14.96 in Overland Bed Rack with MOLLE panels, 900 lb, Tacoma / Gladiator / Ranger / Colorado","JOYTUTUS","$400–$500",{},"Adjustable width; check bed length on listing."),
])
add("jeep","gladiator","2020-present","bed-racks",[
 ("B0DF7LHZD2","SUORTO Overland Bed Rack with 2 LED light bars, 2020-2025 Gladiator JT, 500 lb","SUORTO","$350–$450",{},"Gladiator-specific clamp rack."),
 ("B0D3GJZGHF","OTHOWE 22 in High Overland Bed Rack, Gladiator JT (without tonneau cover)","OTHOWE","$400–$500",{},"Full height; not compatible with a tonneau."),
 ("B0DS2BHPLF","JOYTUTUS 14.96 in Overland Bed Rack with MOLLE panels, 900 lb, 2020-2025 Gladiator","JOYTUTUS","$400–$500",{},"Mid height; tent-rated per listing."),
 ("B0BPHJTYD9","u-Box 19 in Full-Height Overland Bed Rack, Gladiator JT","u-Box","$450–$600",{},"Full height."),
 ("B0BPM8R6GQ","Hooke Road 12.3 in Overland Bed Rack, Gladiator JT","Hooke Road","$350–$450",{},"Low profile."),
])
add("ford","ranger","2024-present","bed-racks",[
 ("B0DS2BHPLF","JOYTUTUS 14.96 in Adjustable Overland Bed Rack, lists 2019-2025 Ranger","JOYTUTUS","$400–$500",{},"Adjustable clamp rack; seller lists to 2025 — confirm 2024+ bed width."),
 ("B0DDKJ37N4","OBNAUX Overland Bed Rack with LED bars, lists 2004-2025 Ranger","OBNAUX","$300–$400",{},"Universal clamp rack; confirm 2024+ with seller."),
])

# ---------------- Roof racks
add("toyota","4runner","2010-2024","roof-racks",[
 ("B0CQ1VSKTN","KitsPro 260 lb Roof Rack Cross Bars, 2010-2024 4Runner (factory raised side rails only)","KitsPro","$90–$130",{"roof_type":"raised-rails"},"Clamp-on aluminum; not for TRD Pro basket."),
 ("B0D12M8BTZ","Tuyoung 300 lb Lockable Cross Bars, 2010-2024 4Runner with side rails","Tuyoung","$100–$140",{"roof_type":"raised-rails"},"Lockable; raised rails only."),
 ("B0FZST5M5K","300 lb Lockable Aluminum Cross Bars, 2010-2024 4Runner","Generic","$90–$130",{"roof_type":"raised-rails"},"Anti-theft locks."),
 ("B0FG7NBC6W","260 lb Aluminum Cross Bars, 2010-2024 4Runner","Generic","$80–$120",{"roof_type":"raised-rails"},"Budget clamp-on bars."),
 ("B0BTLXZV3T","Aluminum Rail Cross Bars, 2010-2024 4Runner","Generic","$70–$110",{"roof_type":"raised-rails"},"Budget."),
 ("B08NXB5H29","Roof Rack Side Rails (replacement raised rails), 2010-2024 4Runner","Generic","$150–$220",{},"For trucks missing factory rails; needed before crossbars."),
])
add("toyota","4runner","2025-present","roof-racks",[
 ("B0FNVH28DX","260 lb Lockable Roof Rack Cross Bars, 2025-2026 4Runner, wide-grip clamps, no drilling","Generic","$100–$150",{"roof_type":"raised-rails"},"Confirmed 2025+ listing."),
 ("B0G3THM11J","Upgraded Lockable Aluminum Cross Bars, 2025-2026 4Runner","Generic","$100–$150",{"roof_type":"raised-rails"},"Confirmed 2025+ listing."),
])
add("ford","bronco","2021-present","roof-racks",[
 ("B0BW821W8X","Wonderdriver 5-Piece Roof Rack Cross Bars, 2021-2026 Bronco hardtop 2-door & 4-door","Wonderdriver","$150–$220",{"roof_type":"removable"},"Hardtop only; not Bronco Sport."),
 ("B0FXM1DYRK","Wonderdriver 330 lb 5-Piece Cross Bars, 2021-2026 Bronco hardtop 2-door & 4-door","Wonderdriver","$170–$240",{"roof_type":"removable"},"Higher load rating version."),
 ("B0DP4MVP7Z","ANTS PART 5-Piece Extended Roof Rack Kit (2 rails + 3 bars), 2021-2026 Bronco 4-door hardtop","ANTS PART","$180–$260",{"roof_type":"removable","doors":4},"4-door only; no-drill."),
 ("B0C9CJK487","ROSY PIXEL Roof Rack Kit, side rails + cross bars, 2021-2026 Bronco hardtop","ROSY PIXEL","$150–$220",{"roof_type":"removable"},"Hardtop only."),
 ("B0D6QW62SB","Broaddict Half Roof Rack, 2021-2026 Bronco 4-door hardtop","Broaddict","$200–$300",{"roof_type":"removable","doors":4},"Rear-half platform; keeps front panels removable."),
 ("B0D179TWJ6","Extended Cross Bars + Side Ladder, 2021-2025 Bronco 4-door hardtop","Generic","$250–$350",{"roof_type":"removable","doors":4},"Includes side ladder."),
])
add("subaru","outback","2020-present","roof-racks",[
 ("B0BPY41QBK","BougeRV Lockable Cross Bars, 2020-2025 Outback Wilderness only","BougeRV","$90–$130",{"roof_type":"raised-rails","trim":"Wilderness"},"Wilderness ladder rack only."),
 ("B0CSW5W542","Soruci 300 lb Cross Bars, 2022-2025 Outback Wilderness only","Soruci","$90–$130",{"roof_type":"raised-rails","trim":"Wilderness"},"Wilderness only."),
 ("B0C1B1M96H","300 lb Lockable Cross Bars, 2022-2025 Outback Wilderness","Generic","$90–$130",{"roof_type":"raised-rails","trim":"Wilderness"},"Wilderness only."),
 ("B099HSLM2M","EZREXPM Cross Bars for raised side rails (Forester / Crosstrek / 2022-2025 Outback Wilderness)","EZREXPM","$80–$120",{"roof_type":"raised-rails","trim":"Wilderness"},"Multi-fit; confirm Outback trim on listing."),
])
add("tesla","model-y","2020-present","roof-racks",[
 ("B0H93M98FJ","RuiHui Roof Rack Cross Bars, 2020-2026 Model Y incl. Juniper, 165 lb, lockable","RuiHui","$180–$260",{"roof_type":"fixed-points"},"Lists Juniper; fixed-point mount."),
 ("B0FS1X1KX4","Cross Bars for 2020-2026 Model Y incl. Juniper, quiet aero design","Generic","$180–$260",{"roof_type":"fixed-points"},"Lists Juniper; not for S/3/X."),
 ("B0DHZJMV4S","Noiseless Lockable Aluminum Roof Rack, 2020-2025 Model Y","Generic","$170–$250",{"roof_type":"fixed-points"},"2020-2025 only; confirm Juniper separately."),
 ("B0D3ZVKCXM","AUXPACBO Upgraded Noiseless Lockable Roof Rack, 2020-2025 Model Y","AUXPACBO","$170–$250",{"roof_type":"fixed-points"},"2020-2025."),
 ("B09VJZ3JWH","AUXPACBO Lockable Cross Bars, 2020-2025 Model Y","AUXPACBO","$150–$220",{"roof_type":"fixed-points"},"2020-2025."),
])

# ---------------- Cargo boxes (boxes are universal — the crossbars carry the vehicle fit)
_BOXES = [
 ("B001PUZXGK","Yakima SkyBox 16 Rooftop Cargo Box, 16 cu ft","Yakima","$550–$700",{},"Universal T-slot/clamp mount; needs crossbars first."),
 ("B083KP48XC","Yakima GrandTour 16 Premium Cargo Box, dual-side opening","Yakima","$800–$1,000",{},"Premium 16 cu ft; needs crossbars."),
 ("B0DYWCZSD8","Yakima SkyBox NX Skinny 12 cu ft Cargo Box","Yakima","$450–$600",{},"Narrow — leaves room for a bike or kayak beside it."),
 ("B001PUZ24I","Yakima RocketBox 16 Cargo Box","Yakima","$450–$600",{},"Budget Yakima 16 cu ft."),
 ("B09HC2LWX8","Yakima DeepSpace 10 Hard Shell Cargo Box","Yakima","$350–$450",{},"Compact 10 cu ft."),
]
add("toyota","rav4","2019-present","cargo-boxes",[
 ("B081J9P2KY","Autekcomma 260 lb Lockable Cross Bars, 2019-2025 RAV4 (not LE / Adventure / TRD Off-Road / Woodland)","Autekcomma","$90–$130",{"roof_type":"raised-rails"},"Standard raised rails only — buy first, then a box."),
 ("B08LG42HL8","FLYCLE Lockable Cross Bars, 2019-2025 RAV4 (not Adventure / TRD Off-Road)","FLYCLE","$80–$120",{"roof_type":"raised-rails"},"Standard rails only."),
 ("B07WGHX1K5","ROKIOTOEX Cross Bars, 2019-2024 RAV4 Adventure / TRD factory raised rails","ROKIOTOEX","$100–$150",{"roof_type":"raised-rails","trim":"Adventure/TRD Off-Road"},"Adventure / TRD rails only."),
 ("B0GDYBR15P","Aluminum Cross Bars, 2019-2025 RAV4, no-drill","Generic","$70–$110",{"roof_type":"raised-rails"},"Confirm trim on listing."),
] + _BOXES)
add("subaru","outback","2020-present","cargo-boxes",_BOXES)
add("kia","telluride","2020-present","cargo-boxes",[
 ("B0DXPZDL1P","Lockable Aluminum Cross Bars, 2020-2025 Telluride","Generic","$90–$130",{"roof_type":"raised-rails"},"Buy first, then a box."),
 ("B09TW15M9N","Snailfly Lockable Cross Bars, 2019-2025 Telluride EX / S / SX / SX-P (except LE, X-Line, X-Pro)","Snailfly","$90–$130",{"roof_type":"raised-rails"},"Not for X-Line / X-Pro rails."),
 ("B0CZZWTQNH","Tuyoung 300 lb Cross Bars, 2023-2025 Telluride X-Pro & X-Line raised rails","Tuyoung","$100–$140",{"roof_type":"raised-rails","trim":"X-Line/X-Pro"},"X-Line / X-Pro only."),
 ("B0BM9ZMDTC","Snailfly 165 lb Cross Bars, 2023-2025 Telluride X-Pro / X-Line","Snailfly","$90–$130",{"roof_type":"raised-rails","trim":"X-Line/X-Pro"},"X-Line / X-Pro only."),
] + _BOXES)

# ---------------- Hitches
add("ford","maverick","2022-present","hitches",[
 ("B0BHZY5GTP","CURT 13504 Class 3 Trailer Hitch, 2 in receiver, 2022-2025 Maverick (excl. factory receiver)","CURT","$180–$240",{},"Brand-name; bolt-on."),
 ("B0B6296PL4","Draw-Tite 76557 Class 3 Trailer Hitch, 2 in receiver, 2022-2026 Maverick","Draw-Tite","$180–$240",{},"Brand-name; bolt-on."),
 ("B0H2DP5QBR","Nilight Class 3 Trailer Hitch 2 in, 2022-2026 Maverick (excl. factory receiver)","Nilight","$120–$170",{},"Budget; bike rack / cargo carrier."),
 ("B0GFQH1Z61","Armordillo Class 3 Hitch with loaded ball mount, 2022-2026 Maverick","Armordillo","$150–$200",{},"Includes ball mount."),
 ("B0FWC3TNXN","TUZILLA Class 3 Trailer Hitch 2 in, 2022-2026 Maverick","TUZILLA","$110–$160",{},"Budget."),
 ("B0FXM8SX2T","APS Class 3 Rear Towing Hitch Receiver, 2022-2026 Maverick","APS","$110–$160",{},"Budget."),
])
add("toyota","rav4","2019-present","hitches",[
 ("B01K52C53W","CURT Class 3 Trailer Hitch 2 in with 4-way flat wiring harness, 2019-2025 RAV4 & 2021-2024 RAV4 Prime","CURT","$260–$340",{},"Hitch + harness bundle; lists Prime."),
 ("B0H8Z9D2FN","CURT Class 3 Trailer Hitch with 4-way custom wiring harness, 2019-2025 RAV4","CURT","$250–$330",{},"Hitch + harness."),
 ("B07V3NLKV9","Rigid Hitch R3-0523 Class 3 Trailer Hitch 2 in, 2019-2024 RAV4, made in USA","Rigid Hitch","$180–$240",{},"Hitch only; verify 2025 on listing."),
])
add("tesla","model-y","2020-present","hitches",[
 ("B0H2GPMC4N","Class 3 Trailer Hitch 2 in, 2020-2026 Model Y all trims","Generic","$180–$260",{},"For bike racks / carriers; no Trailer Mode."),
 ("B0BNVFCPRH","Class 3 Trailer Hitch 2 in, 2020-2024 Model Y","Generic","$170–$250",{"year_to":2024},"Pre-Juniper only."),
 ("B0F2MDYT6Z","Class 3 Trailer Hitch 2 in, 2025 Model Y Juniper (not 2026)","Generic","$180–$260",{"year_from":2025,"year_to":2025},"Juniper-specific."),
 ("B0G3242GBZ","Trailer Hitch 2 in receiver, 2020-2025 Model Y, alloy steel","Generic","$170–$250",{},"Bike racks / cargo carriers."),
 ("B0HB2ZQJL3","Trailer Hitch Receiver 2 in, 2020-2026 Model Y, 2,000 lb GTW, includes cover","Generic","$150–$220",{},"Light-duty; racks only."),
])
add("toyota","highlander","2020-present","hitches",[
 ("B08KH848CN","CURT 13460 Class 3 Trailer Hitch 2 in, select Highlander (2020+)","CURT","$200–$280",{},"Confirm 2020-2025 on listing; not Grand Highlander."),
 ("B0DQ3K1XVD","TLAPS Class 3 Trailer Hitch 2 in, 2020-2025 Highlander","TLAPS","$140–$200",{},"Budget; lists 2020-2025."),
])

# ---------------- Floor mats
add("toyota","4runner","2025-present","floor-mats",[
 ("B0F1CMKNT5","LASFIT All-Weather TPE Floor Liners, 2025-2026 4Runner 5-seat gas (not hybrid), front & rear","LASFIT","$120–$160",{"rows":2,"hybrid":False},"5-seat gas only."),
 ("B0F1CMB75T","LASFIT Floor Liners + Cargo + Backrest Mats, 2025-2026 4Runner 5-seat gas","LASFIT","$170–$220",{"rows":2,"hybrid":False},"Full set incl. cargo; gas only."),
 ("B0F23X594D","TripleAliners Heavy-Duty TPE Liners, 2025-2026 4Runner 5-seat, front/2nd row/cargo/seatback (not hybrid)","TripleAliners","$150–$200",{"rows":2,"hybrid":False},"Full set; gas only."),
 ("B0F6V4NW6B","All-Weather Floor Mats + Cargo Liner, 2025-2026 4Runner 7-seat SR5/Limited (not hybrid)","Generic","$150–$200",{"rows":3,"hybrid":False},"3-row set."),
 ("B0G3NYLLVR","NQOQN All-Weather Floor Mats + Trunk + Backrest, 2025-2026 4Runner 7-seat","NQOQN","$140–$190",{"rows":3},"3-row set."),
 ("B0DV11JW53","Toyota Genuine All-Weather Floor Liners, 2025+ 4Runner, third-row compatible","Toyota","$180–$240",{},"OEM liners."),
 ("B0GRYDX3SF","Vantio TPE Floor Liners, 2025-2026 4Runner 5-seat (not hybrid)","Vantio","$100–$140",{"rows":2,"hybrid":False},"Budget 5-seat."),
])
add("honda","cr-v","2023-present","floor-mats",[
 ("B0CSKR1WZ6","TPE All-Weather Floor Mats + Cargo Liner, 2023-2026 CR-V gas & hybrid","Generic","$110–$150",{},"Full set incl. cargo; lists hybrid."),
 ("B0CWRYCGGY","Weize Floor Mats + Cargo Liner (upper position), 2023-2026 CR-V incl. Hybrid","Weize","$110–$150",{},"Cargo liner for upper deck position."),
 ("B0BVLYJV8X","HAFIDI TPE Floor Liners 1st & 2nd row, 2023-2026 CR-V & CR-V Hybrid","HAFIDI","$80–$120",{},"Cabin set only."),
 ("B0CZ364XXB","Sunsdrew TPE Floor Liners 1st & 2nd row, 2023-2025 CR-V & Hybrid","Sunsdrew","$80–$120",{},"Cabin set only."),
 ("B0DZNG9CHB","TTX Lighting Floor Liners + Cargo Liner + Backrest Mats, 2023-2026 CR-V gas & hybrid (upper deck)","TTX Lighting","$120–$160",{},"Full set."),
 ("B0D5QNN1BD","Autocessking 4-Piece Floor Mats + Cargo Liner, 2023-2025 CR-V Hybrid (upper deck)","Autocessking","$100–$140",{"hybrid":True},"Hybrid cargo deck."),
])
add("tesla","model-y","2020-present","floor-mats",[
 ("B0GTS6R1N6","Foronetry 8-Piece All-Weather Set, 2025-2026 Model Y Juniper 5-seat (frunk, trunk, cargo, rear mats)","Foronetry","$140–$190",{"year_from":2025,"rows":2},"Juniper only; not Standard trim or 7-seat."),
 ("B0DZGGYTBC","TripleAliners 10-Piece Set, 2025-2026 Model Y Juniper (floor, frunk, trunk, rear lower, backrest, bumper guard)","TripleAliners","$150–$200",{"year_from":2025},"Juniper only; not Standard."),
 ("B0H251XWBW","Autocessking 11-Piece All-Weather Mats + Cargo Liners, 2025-2026 Model Y Juniper (not Standard)","Autocessking","$150–$200",{"year_from":2025},"Juniper only."),
 ("B0H6QQJ7GT","Front (frunk) + Rear Trunk Mats, 2025-2026 Model Y Juniper 5-seat Premium/Performance","Generic","$60–$90",{"year_from":2025},"Trunk/frunk only; Juniper."),
 ("B0BRJQ2C7V","3W 6-Piece TPE Floor Mats + Cargo + Frunk Liners, 2020-2024 Model Y 5-seat (not Juniper)","3W","$120–$160",{"year_to":2024,"rows":2},"Pre-Juniper only."),
 ("B0CBWNQYW5","Foronetry 9-Piece All-Weather Set, 2021-2024 Model Y 5-seat (not 7-seat / not Juniper)","Foronetry","$130–$180",{"year_to":2024,"rows":2},"Pre-Juniper only."),
 ("B0CPXZKX62","WEIZE 6-Piece All-Weather Mats + Trunk + Cargo Liners, 2020-2024 Model Y 5-seat","WEIZE","$100–$140",{"year_to":2024,"rows":2},"Pre-Juniper only."),
 ("B09YTGFHGG","TAPTES XPE Floor Mats Full Set + Trunk Cargo Liner, 2021-2025 Model Y 5-seat","TAPTES","$110–$150",{"rows":2},"Lists to 2025; confirm Juniper vs pre-refresh on listing."),
])
add("jeep","grand-cherokee","2022-present","floor-mats",[
 ("B0BHS6HHQ5","3W TPE Floor Mats + Cargo Liner, 2022-2026 Grand Cherokee WL incl. 4xe (not L / WK2)","3W","$130–$180",{"rows":2},"Full set incl. trunk; 4xe listed."),
 ("B0GT4Y47WY","All-Weather Floor Mats Set, 2022-2026 Grand Cherokee WL 5-seat incl. 4xe (not L)","Generic","$90–$130",{"rows":2},"Cabin set; 4xe listed."),
 ("B0CTCMD7GL","All-Weather TPE Floor Mats, 2022-2025 Grand Cherokee WL incl. 4xe, 5-seat only (not WK2 / WL75)","Generic","$90–$130",{"rows":2},"Cabin set."),
 ("B09TK59VFT","Flymotor Custom-Fit TPE Floor Liners, 2022-2024 Grand Cherokee WL 2-row full set","Flymotor","$100–$140",{"rows":2},"2022-2024; confirm 2025 on listing."),
 ("B0CKW3XNVK","Floor Liner + Cargo Mat Full Set, 2022-2026 Grand Cherokee WL incl. 4xe (not L / WK)","Generic","$120–$160",{"rows":2},"Full set incl. cargo."),
])
add("ford","f-150","2021-present","floor-mats",[
 ("B0896RQ7VT","LASFIT TPE Floor Liners 1st & 2nd row, 2015-2026 F-150 SuperCrew & 2022-2025 Lightning (rear without fold-flat storage)","LASFIT","$120–$160",{"cab":"SuperCrew","fold_flat_storage":False},"Not for rear fold-flat under-seat storage."),
 ("B0DCVH5QF5","Mixsuper TPE Floor Liners 2-row, 2015-2025 F-150 SuperCrew incl. Lightning (fits rear bench with under-seat storage)","Mixsuper","$110–$150",{"cab":"SuperCrew","fold_flat_storage":True},"Fits rear under-seat storage."),
 ("B0D7HZSBRH","KARPAL Custom-Fit TPE Front Floor Liners, 2015-2025 F-150 SuperCrew / SuperCab incl. Lightning","KARPAL","$70–$100",{},"Front row only."),
 ("B0CWRY7BVD","Weize TPE Floor Liners Front & 2nd row, 2015-2025 F-150 SuperCrew & Lightning (not rear fold-flat storage)","Weize","$100–$140",{"cab":"SuperCrew","fold_flat_storage":False},"Not for rear fold-flat storage."),
 ("B09D32CVXR","Custom-Fit Rubber All-Weather Floor Liners, 2015-2025 F-150 & 2022-2024 Lightning SuperCrew (not rear fold-flat storage)","Generic","$90–$130",{"cab":"SuperCrew","fold_flat_storage":False},"Not for rear fold-flat storage."),
 ("B0H2YGZR9G","TPE Floor Mats + Cargo Liner Full Set, 2015-2025 F-150 SuperCrew 1st & 2nd row","Generic","$110–$150",{"cab":"SuperCrew"},"Full set."),
])

# ---------------- LED light bars (Wrangler JL) — bracket kits carry the vehicle fit; bars are universal
add("jeep","wrangler","2018-present","led-light-bars",[
 ("B07QHNYFYW","Diode Dynamics Hood Mount LED Light Bar Brackets, 2018-2025 Wrangler JL","Diode Dynamics","$70–$100",{"mount":"hood"},"Brand-name hood cowl brackets for 20 in bars."),
 ("B0B2LTBF3T","Hawkley 50-52 in A-Pillar Windshield Light Bar Brackets + 2x 4 in spot lights, 2018-2026 JL/JLU & 2019-2026 Gladiator (not 4xe / Mojave)","Hawkley","$80–$120",{"mount":"windshield"},"Not for 4xe or Mojave."),
 ("B0BMTXQZLT","Hawkley 50/52 in A-Pillar Light Bar Mounting Brackets, 2018-2026 Wrangler JL/JLU & Gladiator JT","Hawkley","$50–$80",{"mount":"windshield"},"Brackets only."),
 ("B07M5K9LMX","AUXMART 52 in Windshield Light Bar Brackets with A-pillar mounts, 2018-2022 JL / Gladiator (not Mojave)","AUXMART","$50–$80",{"mount":"windshield","year_to":2022},"Listed to 2022; confirm later years."),
 ("B083NGH9CW","Auto Dynasty 52 in Windshield LED Light Bar Steel Brackets, 2018-2020 JL","Auto Dynasty","$40–$70",{"mount":"windshield","year_to":2020},"2018-2020 only."),
 ("B07VCLXVVZ","Mopar OEM Bumper Mount Light Bracket, Wrangler JL","Mopar","$60–$100",{"mount":"bumper"},"Factory bumper bracket for cube/bar lights."),
 ("B07Y5XWXZ8","Fab Fours ViCowl 20 in Light Bar Insert, 2018+ Wrangler JL","Fab Fours","$150–$220",{"mount":"hood"},"Cowl insert for a 20 in bar."),
])
