"""v2 product shortlist (~60 pages). Same row shape and rules as fitments_v1.py.
ASINs come from Amazon listing titles that state the fitment (confidence 2); 'confirm' in the note → confidence 1.
"""
F = []
def add(make, model, gen, cat, rows):
    for i, (asin, name, brand, band, cond, note) in enumerate(rows, 1):
        F.append((asin, name, brand, cat, band, make, model, gen, cond, note, i))

# ================================================================ FLOOR MATS
add("ford","f-150","2015-2020","floor-mats",[
 ("B0955QR36Y","Motor Trend 3D Contour-Fit Floor Mats, 2015-2020 F-150 SuperCrew","Motor Trend","$80–$120",{"cab":"SuperCrew"},"SuperCrew only."),
 ("B07C5XT7CN","AKM TPE Floor Liners 1st & 2nd row, 2015-2020 F-150 SuperCrew (bucket seats)","AKM","$90–$130",{"cab":"SuperCrew"},"Bucket-seat layout; check front bench vs buckets."),
 ("B07BDNY9SF","OEDRO All-Weather TPE Floor Liners, 2015-2025 F-150 SuperCrew (not rear fold-flat storage)","OEDRO","$90–$130",{"cab":"SuperCrew","fold_flat_storage":False},"Not for rear under-seat fold-flat storage."),
 ("B0CQ21CCXQ","Broryan TPE Floor Liners 1st & 2nd row, 2015-2025 F-150 SuperCrew (w/o fold-flat storage)","Broryan","$80–$120",{"cab":"SuperCrew","fold_flat_storage":False},"Not for fold-flat storage."),
 ("B0955VCWT1","BDK Motor Trend 3D Contour Liners front & 2nd row, 2015-2022 F-150 SuperCrew","BDK","$80–$120",{"cab":"SuperCrew"},"Covers 2015-2022."),
])
_T1_MATS = [
 ("B07YTJCWN1","3W TPE All-Weather Floor Mats, 2019-2025 Silverado/Sierra 1500 Crew Cab (factory carpeted storage)","3W","$130–$170",{"cab":"Crew Cab","rear_storage":"carpeted"},"For 2nd row with factory carpeted storage."),
 ("B0DB7QQR8X","Falafa All-Weather Floor Liners, 2019-2024 Silverado/Sierra 1500 Crew Cab with rear under-seat storage box","Falafa","$100–$140",{"cab":"Crew Cab","rear_storage":"box"},"For rear under-seat storage box."),
 ("B09TZMBFJP","KUST Rubber Floor Mats, 2019-2025 Silverado/Sierra 1500 Crew Cab with rear under-seat storage box","KUST","$90–$130",{"cab":"Crew Cab","rear_storage":"box"},"For rear under-seat storage box."),
 ("B0896T2PGT","LASFIT Floor Liners, 2019-2026 Silverado/Sierra 1500 Crew Cab, bucket seats, with rear under-seat storage box","LASFIT","$130–$170",{"cab":"Crew Cab","front":"bucket"},"Bucket seats only; not 2nd-row plastic box."),
 ("B0BNB3V38Z","Floor Mats, 2020-2026 Silverado/Sierra 1500 Crew Cab without rear under-seat storage box, front bench","Generic","$100–$140",{"cab":"Crew Cab","front":"bench","rear_storage":"none"},"Front bench, no rear storage box."),
]
add("chevrolet","silverado-1500","2019-present","floor-mats",_T1_MATS)
add("gmc","sierra-1500","2019-present","floor-mats",[
 ("B088MD3P68","OMAC 3D Custom-Fit TPE Floor Liners, 2019-2025 Sierra 1500 Crew Cab","OMAC","$90–$130",{"cab":"Crew Cab"},"Sierra-specific listing."),
 ("B09KMQTS8H","TuxMat Custom Car Mats 1st & 2nd row, 2019-2026 Sierra 1500 Crew Cab","TuxMat","$200–$260",{"cab":"Crew Cab"},"Premium maximum-coverage set."),
] + _T1_MATS[:3])
add("ram","1500","2019-present","floor-mats",[
 ("B0D66T22SK","All-Weather Floor Mats Set, 2019-2025 Ram 1500 Crew Cab New Body with factory under-seat storage (not Classic)","Generic","$100–$140",{"cab":"Crew Cab","rear_storage":True},"New body (DT) only; not Classic."),
 ("B0FJL5XRZB","TPE Floor Liners Full Set 1st & 2nd row, 2019-2025 Ram 1500 Crew Cab New Body (bucket or bench, with storage)","Generic","$110–$150",{"cab":"Crew Cab"},"New body only."),
 ("B07YBKL8MQ","Mopar OEM All-Weather Mats, Ram 1500 DT Crew Cab","Mopar","$120–$180",{"cab":"Crew Cab"},"Factory accessory mats."),
])
add("toyota","tacoma","2016-2023","floor-mats",[
 ("B0CD15B35L","3W TPE All-Weather Floor Liners, 2016-2023 Tacoma Double Cab, automatic","3W","$110–$150",{"cab":"Double Cab","trans":"automatic"},"Automatic only (manual has a different floor)."),
 ("B081DQNXB2","YITAMOTOR TPE Floor Liners 1st & 2nd row, 2016-2023 Tacoma Double Cab","YITAMOTOR","$80–$120",{"cab":"Double Cab"},"Double Cab."),
 ("B0BT92YGYN","YHTAUTO TPE Floor Liners 3-piece, 2016-2023 Tacoma Double Cab automatic","YHTAUTO","$70–$110",{"cab":"Double Cab","trans":"automatic"},"Automatic only."),
 ("B07SVTV7Z1","TuxMat Custom Car Mats 1st & 2nd row, 2016-2023 Tacoma","TuxMat","$200–$260",{},"Premium coverage."),
 ("B07YNZ6B8T","Toyota Genuine TRD Pro All-Weather Floor Liners PT908-35200-02, 2016-2023 Tacoma automatic","Toyota","$150–$200",{"trans":"automatic"},"OEM TRD Pro logo liners."),
])
add("toyota","tacoma","2024-present","floor-mats",[
 ("B0D41RD1Q6","LASFIT TPE Floor Liners front & rear, 2024-2026 Tacoma Double Cab automatic (not hybrid)","LASFIT","$120–$160",{"cab":"Double Cab","hybrid":False},"Not for i-FORCE MAX hybrid."),
 ("B0DLNN5LPW","COZONY TPE Floor Liners 1st & 2nd row, 2024-2025 Tacoma Double Cab (not hybrid)","COZONY","$90–$130",{"cab":"Double Cab","hybrid":False},"Not for hybrid."),
 ("B0DF4X546T","AOMSAZTO All-Weather TPE Floor Liners, 2024-2025 Tacoma Double Cab","AOMSAZTO","$80–$120",{"cab":"Double Cab"},"Double Cab."),
 ("B0GMY3NVPV","WeatherTech FloorLiners 1st & 2nd row, 2024-2026 Tacoma Double Cab automatic","WeatherTech","$200–$260",{"cab":"Double Cab","trans":"automatic"},"Brand-name laser-measured liners."),
 ("B0CXGDDN3D","Toyota Genuine All-Weather Floor Liners PT206-35242-20, 2024+ Tacoma Double Cab","Toyota","$150–$200",{"cab":"Double Cab"},"OEM."),
])
add("toyota","tundra","2022-present","floor-mats",[
 ("B0BRCVGXCX","LASFIT TPE Floor Liners front & rear, 2022-2026 Tundra CrewMax","LASFIT","$130–$170",{"cab":"CrewMax"},"CrewMax only."),
 ("B0DYP2F168","LNZMPART All-Weather Floor Liners full set, 2022-2025 Tundra CrewMax incl. hybrid","LNZMPART","$90–$130",{"cab":"CrewMax"},"Lists i-FORCE MAX hybrid."),
 ("B0DKF8HCQR","Falafa TPE Floor Liners front & rear, 2022-2024 Tundra CrewMax","Falafa","$90–$130",{"cab":"CrewMax"},"Listed to 2024; confirm 2025 with seller."),
 ("B0FXM1998S","Priprilod TPE Floor Liners 3-piece, 2022-2025 Tundra CrewMax","Priprilod","$80–$120",{"cab":"CrewMax"},"CrewMax only."),
 ("B0F7G535N3","AOMSAZTO Floor Liners + 5.5 ft Bed Mat set, 2022-2025 Tundra / Tundra Hybrid CrewMax","AOMSAZTO","$150–$200",{"cab":"CrewMax","bed_length_in":66},"Includes a bed mat for the 5.5 ft bed."),
])
add("ford","ranger","2019-2023","floor-mats",[
 ("B09PXYWL15","LASFIT TPE Floor Liners front & rear, 2020-2023 Ranger SuperCrew","LASFIT","$110–$150",{"cab":"SuperCrew"},"Listed from 2020; confirm 2019 with seller."),
 ("B08SM45K59","3W TPE Floor Liners 1st & 2nd row, 2019-2023 Ranger SuperCrew","3W","$110–$150",{"cab":"SuperCrew"},"SuperCrew only."),
 ("B08MTZSH7K","OMAC 3D Custom-Fit TPE Floor Liners, 2019-2023 Ranger SuperCrew","OMAC","$80–$120",{"cab":"SuperCrew"},"SuperCrew only."),
 ("B0CNT13Y6V","AOMSAZTO Floor Mats 1st & 2nd row, 2019-2023 Ranger SuperCrew","AOMSAZTO","$70–$110",{"cab":"SuperCrew"},"SuperCrew only."),
 ("B0D2HNW86C","MAXPRO TPE Floor Liners 1st & 2nd row, 2019-2023 Ranger SuperCrew","MAXPRO","$80–$120",{"cab":"SuperCrew"},"SuperCrew only."),
])
add("chevrolet","colorado","2023-present","floor-mats",[
 ("B0CV27TV86","SMARTLINER 2-Row Floor Liners, 2023-2026 Colorado Crew Cab","SMARTLINER","$120–$160",{"cab":"Crew Cab"},"Crew Cab only."),
 ("B0C9SHHWDD","HAFIDI TPE Floor Liners front & 2nd row, 2023-2025 Colorado Crew Cab / GMC Canyon","HAFIDI","$80–$120",{"cab":"Crew Cab"},"Also fits Canyon."),
 ("B0CB5HBWBH","Binmotor TPE Floor Liners, 2023-2026 Colorado Crew Cab / Canyon","Binmotor","$80–$120",{"cab":"Crew Cab"},"Also fits Canyon."),
 ("B0CX946GMG","Liner Master XPE Floor Mats 3-piece, 2023-2025 Colorado Crew Cab / Canyon","Liner Master","$70–$110",{"cab":"Crew Cab"},"Lightweight XPE."),
])
add("nissan","frontier","2022-present","floor-mats",[
 ("B09XC2GFCK","Rough Country All-Weather Floor Mats front & rear, 2022-2025 Frontier Crew Cab","Rough Country","$90–$130",{"cab":"Crew Cab"},"Crew Cab."),
 ("B09PGKNFZL","SMARTLINER 2-Row Floor Liners, 2022-2026 Frontier Crew Cab","SMARTLINER","$120–$160",{"cab":"Crew Cab"},"Check under-seat storage option on listing."),
 ("B0CP7PN2DL","Powerty 3D TPE Floor Liners 1st & 2nd row, 2022-2025 Frontier Crew Cab with 2nd-row under-seat storage","Powerty","$80–$120",{"cab":"Crew Cab","rear_storage":True},"For trucks with rear under-seat storage."),
 ("B0F3HY8QZ6","LUMWAY TPE Floor Liners + door sill guards, 2022-2026 Frontier Crew Cab (not rear under-seat speaker)","LUMWAY","$90–$130",{"cab":"Crew Cab","rear_speaker":False},"Not for 2nd-row under-seat speaker (Fender audio)."),
 ("B0CYZHCXFW","Binmotor All-Weather Floor Mats, 2022-2026 Frontier Crew Cab (not rear under-seat speaker)","Binmotor","$80–$120",{"cab":"Crew Cab","rear_speaker":False},"Not for under-seat speaker."),
])
add("toyota","4runner","2010-2024","floor-mats",[
 ("B0BMXSVVZ5","TuxMat Custom Car Mats 1st & 2nd row, 2013-2024 4Runner 5-seat","TuxMat","$200–$260",{"rows":2,"year_from":2013},"5-seat, 2013+."),
 ("B0D7CMJSKL","Floor Mats + Cargo Liner, 2013-2024 4Runner 5-seat without sliding cargo tray","Generic","$110–$150",{"rows":2,"cargo_tray":False,"year_from":2013},"Not for sliding cargo deck."),
 ("B07X7JS2PW","Toyota Genuine TRD Pro All-Weather Floor Liners PT908-89200-02, 4Runner","Toyota","$150–$200",{},"OEM TRD Pro logo liners; confirm model years on listing."),
 ("B0DT6N79NN","MERXENG All-Weather Cargo Mat, 2010-2024 4Runner 5-seat","MERXENG","$50–$80",{"rows":2},"Cargo area only."),
])
add("jeep","wrangler","2018-present","floor-mats",[
 ("B07K71ZXK1","3W TPE Floor Liners 1st & 2nd row, 2018-2026 Wrangler JL Unlimited 4-door (not JK / 4xe)","3W","$110–$150",{"doors":4,"4xe":False},"Not for 4xe or 2-door."),
 ("B08975DWH2","LASFIT TPE Floor Liners 1st & 2nd row, 2018-2026 Wrangler JL Unlimited 4-door gas/MHEV (not PHEV)","LASFIT","$110–$150",{"doors":4,"4xe":False},"Not for 4xe PHEV."),
 ("B07GNCDHD6","OEDRO TPE Floor Liners full set, 2018-2025 Wrangler JL/JLU 4-door","OEDRO","$90–$130",{"doors":4},"4-door."),
 ("B089DN4CV9","3W Floor Mats + Cargo Liner, 2018-2025 Wrangler JL Unlimited 4-door with subwoofer (not 4xe)","3W","$150–$190",{"doors":4,"subwoofer":True,"4xe":False},"For cargo area with factory subwoofer."),
 ("B0823YBHKD","3W Floor Mats + Cargo Liner, 2018-2025 Wrangler JL Unlimited 4-door without subwoofer (not 4xe)","3W","$150–$190",{"doors":4,"subwoofer":False,"4xe":False},"For cargo area without subwoofer."),
 ("B0FBQW1LQJ","Falafa TPE Floor Liners 1st & 2nd row, 2018-2025 Wrangler JL Unlimited 4-door (not JK / 4xe)","Falafa","$80–$120",{"doors":4,"4xe":False},"Not 4xe."),
])
add("ford","bronco","2021-present","floor-mats",[
 ("B0BRCS7DPF","LASFIT TPE Floor Liners 1st & 2nd row, 2021-2025 Bronco 4-door (not Bronco Sport)","LASFIT","$110–$150",{"doors":4},"4-door only; not Bronco Sport."),
 ("B0BP793P92","3W Floor Mats + Cargo Liner, 2021-2026 Bronco 4-door (not Sport, not rubberized floor)","3W","$150–$200",{"doors":4,"floor":"carpet"},"Carpeted floor only — not the washable rubberized floor option."),
 ("B0DFCNK8DS","Lwope Rubber Floor Mats, 2021-2025 Bronco 4-door","Lwope","$70–$110",{"doors":4},"4-door."),
 ("B0H6FZQYR1","Floor Mats + Cargo Liner full set, 2021-2026 Bronco 4-door (not Sport / 2-door)","Generic","$120–$160",{"doors":4},"4-door only."),
])
add("toyota","highlander","2020-present","floor-mats",[
 ("B08PPJB31Z","TGBROS 3-Row Floor Liner Set, 2020-2025 Highlander (2nd-row bench or buckets with console)","TGBROS","$120–$160",{"rows":3},"Full 3-row set."),
 ("B0DM89BCFG","MAXPRO 3-Row Floor Liners, 2020-2026 Highlander (not hybrid)","MAXPRO","$120–$160",{"rows":3,"hybrid":False},"Not for Highlander Hybrid."),
 ("B0BXLGWKGW","LASFIT TPE Floor Liners front & 2nd row, 2020-2026 Highlander 8-seat (not hybrid)","LASFIT","$110–$150",{"seats":8,"hybrid":False},"8-seat (2nd-row bench), gas only."),
 ("B088C2THJV","SMARTLINER 3rd-Row Floor Liner, 2020-2026 Highlander","SMARTLINER","$40–$70",{"rows":3},"Third row only — pair with a front/2nd-row set."),
 ("B0DQ8J5FT9","Carpet-Style All-Weather Floor Mats 4-piece, 2020-2025 Highlander 7-seat incl. hybrid","Generic","$70–$110",{"seats":7},"7-seat captain's chairs; lists hybrid."),
])
add("subaru","forester","2019-2024","floor-mats",[
 ("B07N7YX7WH","Husky Liners Weatherbeater 3-piece front & 2nd row, 2019-2024 Forester (95891)","Husky Liners","$130–$170",{},"Brand-name, made in USA."),
 ("B07JCDW4LC","Subaru Genuine All-Weather Floor Liners J501SSJ030, 2019-2024 Forester (set of 4)","Subaru","$80–$120",{},"OEM."),
 ("B08M9422VV","LASFIT TPE Floor Liners 1st & 2nd row, 2019-2024 Forester","LASFIT","$100–$140",{},"Full cabin set."),
 ("B0C23ZL7JC","3W TPE Floor Liners 1st & 2nd row, 2019-2024 Forester","3W","$100–$140",{},"Full cabin set."),
 ("B0CNW1R1LQ","IKABEVEM Floor Liners + Cargo Liner full set, 2019-2024 Forester","IKABEVEM","$90–$130",{},"Includes cargo liner."),
])
add("tesla","model-3","2017-present","floor-mats",[
 ("B0BV222V54","SUPER LINER 8-Piece All-Weather Set (floor, seatback, cargo, trunk), 2024-2026 Model 3 Highland","SUPER LINER","$130–$180",{"year_from":2024},"Highland only."),
 ("B0CY8NYC44","BRYOUS 8-Piece Floor Mats + Front/Rear Cargo Liners, 2024-2025 Model 3 Highland","BRYOUS","$110–$150",{"year_from":2024},"Highland only."),
 ("B0F1Y8FBKK","FemboMAX 6-Piece TPE Floor Mats + Cargo Liners, 2024-2026 Model 3 Highland","FemboMAX","$100–$140",{"year_from":2024},"Highland only."),
 ("B0GL7W2L94","3W Full Set Floor Mats + Cargo Liner, 2024-2026 Model 3 Highland","3W","$130–$170",{"year_from":2024},"Highland only."),
])
add("ford","explorer","2020-present","floor-mats",[
 ("B09MQGKWHR","3W TPE 3-Row Floor Liners, 2020-2026 Explorer 6-passenger incl. hybrid","3W","$150–$190",{"rows":3,"seats":6},"6-passenger (2nd-row buckets)."),
 ("B0CC4YY6XR","LASFIT TPE 3-Row Floor Liners 4-piece, 2020-2025 Explorer 6-passenger","LASFIT","$140–$180",{"rows":3,"seats":6},"6-passenger only."),
 ("B0BHZB7VWP","DrCarNow 3-Row All-Weather Floor Mats, 2020-2026 Explorer 6-passenger with bucket seats","DrCarNow","$110–$150",{"rows":3,"seats":6},"6-passenger only."),
 ("B08LZH21RT","KUST Rubber Floor Liners front & 2nd row, 2020-2026 Explorer","KUST","$70–$110",{"rows":2},"Front + 2nd row; check 6- vs 7-passenger on listing."),
])
add("chevrolet","tahoe","2021-present","floor-mats",[
 ("B08VFDFCNQ","TOUGHPRO 3-Row Floor Mat Set (made in USA), 2021-2025 Tahoe with 2nd-row buckets","TOUGHPRO","$110–$150",{"rows":3,"second_row":"bucket"},"2nd-row bucket seating."),
 ("B09SNYCX4M","Mixsuper 3-Row Floor Liners, 2021-2026 Tahoe / Yukon / Escalade with 2nd-row buckets (not bench)","Mixsuper","$130–$170",{"rows":3,"second_row":"bucket"},"Not for 2nd-row bench."),
 ("B0DG53L1MG","JSLYF All-Weather TPE Floor Mats full set, 2021-2024 Tahoe","JSLYF","$120–$160",{"rows":3},"Listed to 2024; confirm 2025 with seller."),
])
add("kia","telluride","2020-present","floor-mats",[
 ("B081W2SH36","Husky Liners Weatherbeater 3-piece front & 2nd row, 2020-2025 Telluride (95691)","Husky Liners","$130–$170",{"rows":2},"Front + 2nd row; add a 3rd-row liner."),
 ("B08T6P8XG8","WeatherTech FloorLiners full set (1st-3rd row), Telluride","WeatherTech","$280–$360",{"rows":3},"Brand-name full 3-row set; confirm seating layout."),
 ("B07RN1362T","TOUGHPRO Floor Mat Set + 3rd Row (made in USA), 2020-2025 Telluride","TOUGHPRO","$110–$150",{"rows":3},"Full 3-row set."),
 ("B08258HJGQ","SMARTLINER 3-Row + Cargo Liner set, 2020-2025 Telluride","SMARTLINER","$180–$230",{"rows":3},"Includes cargo liner behind 3rd row."),
 ("B0B1ZLL74S","SUPER LINER 3-Row Liner Set, 2020-2024 Telluride with 2nd-row buckets, no center console","SUPER LINER","$130–$170",{"rows":3,"second_row":"bucket"},"Bucket seats without console only; confirm 2025."),
])
add("hyundai","palisade","2020-2025","floor-mats",[
 ("B081TP8BD4","SMARTLINER 3-Row Floor Liner Set, 2020-2025 Palisade","SMARTLINER","$150–$200",{"rows":3},"Full 3-row set."),
 ("B07WHP4DY5","TOUGHPRO Floor Mat Set + 3rd Row (made in USA), 2020-2025 Palisade with 2nd-row buckets","TOUGHPRO","$110–$150",{"rows":3,"second_row":"bucket"},"2nd-row bucket seats."),
 ("B0D22HJYD7","RILLEC 3-Row Liners + Cargo Liners, 2020-2025 Palisade 7 & 8 seat","RILLEC","$150–$200",{"rows":3},"7- and 8-seat."),
 ("B08YJF62K1","Megiteller Heavy-Duty Rubber 3-Row Floor Liners, 2020-2025 Palisade bench & bucket","Megiteller","$100–$140",{"rows":3},"Bench and bucket layouts."),
])
add("honda","pilot","2023-present","floor-mats",[
 ("B0C4QHXBDL","SMARTLINER 3-Row + Cargo Liner set, 2023-2025 Pilot","SMARTLINER","$180–$230",{"rows":3},"Full set incl. cargo."),
 ("B0DM83VB7L","MAXPRO 3-Row Complete Floor Liner Set, 2023-2025 Pilot","MAXPRO","$120–$160",{"rows":3},"Full 3-row set."),
 ("B0CP7NQJPD","Powerty 3D TPE 3-Row Floor Liners, 2023-2026 Pilot","Powerty","$110–$150",{"rows":3},"Full 3-row set."),
 ("B0D8PS5X65","Weize 5-Piece Floor Mats + Cargo Liners, 2023-2025 Pilot","Weize","$120–$160",{"rows":3},"Includes trunk mat."),
 ("B0C9ML98TG","NIKALAIKA TPE 3-Row Floor Liners, 2023-2026 Pilot","NIKALAIKA","$100–$140",{"rows":3},"Full 3-row set."),
])
add("toyota","sequoia","2023-present","floor-mats",[
 ("B0D1DJ971M","SMARTLINER 3-Row Floor Liner Set, 2023-2025 Sequoia","SMARTLINER","$170–$220",{"rows":3},"Full 3-row set; confirm 7 vs 8 passenger."),
 ("B0DHX8F9FW","HAFIDI TPE Floor Liners 1st-3rd row, 2023-2025 Sequoia","HAFIDI","$120–$160",{"rows":3},"Full 3-row set."),
 ("B0CY84JQPK","Cartist All-Weather Floor Liners, 2023-2026 Sequoia 7-passenger without center console","Cartist","$110–$150",{"rows":3,"seats":7},"7-passenger without 2nd-row console only."),
 ("B0C3CMXLGL","Auxko All-Weather TPE Floor Mats, 2023-2025 Sequoia","Auxko","$100–$140",{"rows":3},"Full set."),
 ("B0CF66XZ1S","Husky Liners Weatherbeater 3rd-Row Liner, 2023-2026 Sequoia (14281)","Husky Liners","$50–$80",{"rows":3},"Third row only."),
])
add("ford","maverick","2022-present","floor-mats",[
 ("B0B3XWRTVX","Mixsuper Custom-Fit Floor Liners 1st & 2nd row, 2022-2026 Maverick (hybrid models only)","Mixsuper","$90–$130",{"hybrid":True},"Hybrid only — the hybrid rear floor differs."),
 ("B0CX8SJ8JD","otoez TPE Floor Liners 3-piece, 2022-2025 Maverick Hybrid only","otoez","$80–$120",{"hybrid":True},"Hybrid only."),
 ("B0C6JR93SJ","SHINJEW TPE Floor Liners 1st & 2nd row, 2022-2026 Maverick Hybrid","SHINJEW","$80–$120",{"hybrid":True},"Hybrid only."),
 ("B0DJKKGJ4N","All-Weather Floor Mats + Cargo Liner, 2022-2025 Maverick (not hybrid)","Generic","$90–$130",{"hybrid":False},"EcoBoost (gas) only."),
])
add("toyota","rav4","2019-present","floor-mats",[
 ("B07V9JYMTT","WeatherTech FloorLiners 1st & 2nd row, 2019-2025 RAV4","WeatherTech","$200–$260",{},"Brand-name; confirm hybrid/Prime on listing."),
 ("B08F4M6QPY","3D Custom-Fit Liners front & 2nd row, 2019-2025 RAV4 (gas, Hybrid, Prime)","Generic","$90–$130",{},"Lists gas, Hybrid and Prime."),
 ("B07WT1MHY3","Powerty 3D Floor Liners 1st & 2nd row, 2019-2025 RAV4 (all models)","Powerty","$80–$120",{},"All models."),
 ("B0FGXYQG99","Floor Mats + Cargo Liner Set, 2019-2025 RAV4 incl. hybrid","Generic","$100–$140",{},"Lists hybrid."),
 ("B09J8M9MR4","AOMSAZTO Floor Liners 1st & 2nd row, 2019-2025 RAV4 (not hybrid)","AOMSAZTO","$70–$110",{"hybrid":False},"Gas only."),
])
add("subaru","outback","2020-present","floor-mats",[
 ("B07WRSDBSS","Subaru Genuine Heavy-Gauge All-Weather Floor Mats J501SAN100 (set of 4), 2020-2025 Outback & Legacy","Subaru","$90–$130",{},"OEM."),
 ("B0948LXFWJ","YITAMOTOR TPE Floor Liners 1st & 2nd row, 2020-2025 Outback / Legacy","YITAMOTOR","$80–$120",{},"Also fits Legacy."),
 ("B093L62R7H","OEDRO TPE Floor Liners 1st & 2nd row, 2020-2025 Outback / Legacy","OEDRO","$90–$130",{},"Also fits Legacy."),
 ("B09R1BJW74","3D Custom-Fit Liners front & 2nd row, 2020-2025 Outback / Legacy (all models)","Generic","$90–$130",{},"All models."),
 ("B0DRYQ1QMC","Auxko All-Weather TPE Floor Mats, 2020-2025 Outback / Legacy","Auxko","$80–$120",{},"Also fits Legacy."),
])
add("jeep","gladiator","2020-present","floor-mats",[
 ("B08CSZ9WLT","3W TPE Floor Liners 1st & 2nd row, 2020-2025 Gladiator","3W","$110–$150",{},"Full cabin set."),
 ("B0BPH6XP8X","LASFIT Heavy-Duty TPE Floor Liners front & rear, 2020-2026 Gladiator JT","LASFIT","$110–$150",{},"Full cabin set."),
 ("B07Z9JFN8M","Rough Country All-Weather Floor Mats, 2020-2025 Gladiator JT with lockable under-seat storage","Rough Country","$90–$130",{"rear_storage":"lockable"},"For trucks with the lockable rear under-seat bin."),
 ("B07WFVP4J2","MAXLINER 2-Row Floor Liner Set, 2020-2025 Gladiator","MAXLINER","$100–$140",{},"Check under-seat storage option on listing."),
 ("B07RST3WS2","Mopar OEM Rubber Floor Mats (set of 4), Gladiator","Mopar","$100–$150",{},"Factory accessory mats."),
])

# ================================================================ TONNEAU (v2)
add("ford","f-150","2015-2020","tonneau-covers",[
 ("B019NUGFSS","MaxMate Soft Tri-Fold Tonneau Cover TCF371041, 2015-2021 F-150 Styleside 5.5 ft","MaxMate","$150–$200",{"bed_length_in":66},"5.5 ft Styleside."),
 ("B08VRSQ8MS","CAPSER Soft Tri-Fold Tonneau Cover, 2015-2026 F-150 5.5 ft (67 in)","CAPSER","$170–$230",{"bed_length_in":66},"5.5 ft."),
 ("B0876PBTL3","MOSTPLUS Soft Tri-Fold Tonneau Cover, 2015-2025 F-150 Styleside 5.5 ft","MOSTPLUS","$120–$170",{"bed_length_in":66},"Budget soft tri-fold."),
 ("B0BXVQ85RQ","Just-V Hard Tri-Fold Tonneau Cover, 2015-2026 F-150 Crew Cab 5.5 ft (excl. Raptor)","Just-V","$300–$380",{"bed_length_in":66},"Excludes Raptor."),
 ("B0DK3928N1","OEDRO FRP Hard Tri-Fold Tonneau Cover, 2015-2025 F-150 5.5 ft","OEDRO","$300–$400",{"bed_length_in":66},"Hard FRP panels."),
 ("B0C4FWZZFV","Soft Roll-Up Tonneau Cover, 2015-2026 F-150 6.5 ft Standard Box","Generic","$150–$200",{"bed_length_in":78},"6.5 ft bed only."),
])
add("toyota","tacoma","2016-2023","tonneau-covers",[
 ("B09DWQ1HF7","ROCTRUK Hard Tri-Fold Tonneau Cover, 2016-2026 Tacoma 5 ft, deck-rail compatible","ROCTRUK","$300–$400",{"bed_length_in":61},"Works with the factory deck rail."),
 ("B0FBG4VCM3","FRP Hard Tri-Fold Tonneau Cover, 2016-2023 Tacoma 5 ft with deck rail system (excl. Trail Edition)","Generic","$300–$400",{"bed_length_in":61},"Excludes Trail Edition."),
 ("B0DDTWZJYB","Aluminum Hard Tri-Fold Tonneau Cover, 2016-2023 Tacoma 5 ft (60 in)","Generic","$300–$400",{"bed_length_in":61},"Aluminum on-top mount."),
 ("B07PGTJXQJ","OEDRO Soft Tri-Fold Tonneau Cover, 2016-2023 Tacoma 5 ft with track rail (excl. Trail)","OEDRO","$170–$230",{"bed_length_in":61},"Excludes Trail Edition."),
 ("B07SVWZMWT","YITAMOTOR Soft Tri-Fold Bed Cover, 2016-2023 Tacoma 5 ft (excl. Trail Edition)","YITAMOTOR","$150–$210",{"bed_length_in":61},"Excludes Trail Edition."),
 ("B0CZD766F8","Aurorasters Soft Tri-Fold Tonneau Cover, 2016-2026 Tacoma 5 ft, deck-rail models only","Aurorasters","$150–$210",{"bed_length_in":61},"Only for trucks with the deck rail system."),
])
add("ford","ranger","2019-2023","tonneau-covers",[
 ("B0C4G36HHZ","XTWEEX Hard Tri-Fold Tonneau Cover, 2019-2024 Ranger 5 ft (not cargo management rails)","XTWEEX","$300–$400",{"bed_length_in":61},"Not for beds with cargo management rails."),
 ("B0CQV98BFT","FASTFIT Hard Tri-Fold Tonneau Cover, 2019-2025 Ranger 5 ft (61 in)","FASTFIT","$300–$400",{"bed_length_in":61},"On-top mount."),
 ("B0CHVLRZV9","Hard Folding Tonneau Cover, 2019-2026 Ranger 5 ft Short Box","Generic","$300–$400",{"bed_length_in":61},"Hard tri-fold."),
 ("B0D4Y4M3ZY","Hard Tri-Fold Aluminum Tonneau Cover with LED, 2019-2026 Ranger 5 ft","Generic","$320–$420",{"bed_length_in":61},"Built-in LED bed light."),
])
add("chevrolet","colorado","2023-present","tonneau-covers",[
 ("B0DCFGCBQ8","XTWEEX Hard Tri-Fold FRP Tonneau Cover, 2023-2026 Colorado / Canyon 5.2 ft (w/o Multi-Flex tailgate)","XTWEEX","$300–$400",{"bed_length_in":62},"2023+ specific; not for Multi-Flex tailgate."),
 ("B0DCFQ9LVX","XTWEEX Soft Roll-Up Tonneau Cover, 2023-2026 Canyon / Colorado 5.2 ft","XTWEEX","$150–$210",{"bed_length_in":62},"2023+ specific."),
 ("B0BF8HJ2HP","TIPTOP Soft Tri-Fold Tonneau Cover TPX3, 2015-2026 Colorado / Canyon 5.2 ft (61.7 in)","TIPTOP","$150–$210",{"bed_length_in":62},"Seller lists both generations — confirm 2023+ fit."),
 ("B09MD9WGXN","ROCTRUK Hard Tri-Fold Tonneau Cover, 2015-2026 Colorado / Canyon 5 ft","ROCTRUK","$300–$400",{"bed_length_in":62},"Seller lists both generations — confirm 2023+ fit."),
])
add("nissan","frontier","2022-present","tonneau-covers",[
 ("B0CGF916K4","Soft Roll-Up Tonneau Cover, 2022-2024 Frontier 5 ft (59.5 in)","Generic","$150–$210",{"bed_length_in":60},"2022+ listing; confirm 2025."),
 ("B0DCC3DYSV","Hard Tri-Fold Tonneau Cover, 2005-2026 Frontier 5 ft (58.6 in), with or without deck rails","Generic","$300–$400",{"bed_length_in":60},"Works with or without Utili-track."),
 ("B08X4SGDQ7","OSOBAK Hard Tri-Fold FRP Tonneau Cover, 2005-2026 Frontier 5 ft, utility-track compatible","OSOBAK","$300–$400",{"bed_length_in":60},"Utili-track compatible."),
 ("B0CHVKWCFN","Hard Folding Tonneau Cover, 2005-2026 Frontier 5 ft, with or without track rail","Generic","$300–$400",{"bed_length_in":60},"Works with or without track rail."),
 ("B0BXVRY1NY","Just-V Hard Tri-Fold Tonneau Cover, 2005-2025 Frontier Crew Cab 5 ft (requires bracket)","Just-V","$300–$380",{"bed_length_in":60},"Requires an extra bracket on some trucks."),
])

# ================================================================ ROOF RACKS (v2)
add("toyota","highlander","2020-present","roof-racks",[
 ("B08H5LH7BF","HEKA Cross Bars, 2020-2025 Highlander XLE/XSE/Limited/Platinum/Hybrid (factory side rails)","HEKA","$80–$120",{"roof_type":"raised-rails"},"Trims with factory side rails."),
 ("B0C2PF9P84","Richeer 220 lb Cross Bars, 2020-2025 Highlander with raised side rails","Richeer","$80–$120",{"roof_type":"raised-rails"},"Raised rails only."),
 ("B08KW6ZVWR","Snailfly Cross Bars, 2020-2026 Highlander XLE/XSE/Limited/Platinum (side rails)","Snailfly","$90–$130",{"roof_type":"raised-rails"},"Side-rail trims."),
 ("B0FCC3VV88","260 lb Lockable Cross Bars, 2020-2025 Highlander XLE/Limited/Platinum","Generic","$100–$140",{"roof_type":"raised-rails"},"Anti-theft locks."),
])
add("subaru","forester","2019-2024","roof-racks",[
 ("B07TWL2VJN","Snailfly Cross Bars, 2014-2024 Forester (except Wilderness)","Snailfly","$90–$130",{"roof_type":"raised-rails"},"Not Wilderness."),
 ("B0D12MDLS1","Tuyoung 300 lb Lockable Cross Bars, 2014-2026 Forester with raised rails (not Wilderness)","Tuyoung","$100–$140",{"roof_type":"raised-rails"},"Not Wilderness."),
 ("B099HSLM2M","EZREXPM Cross Bars, 2014-2024 Forester / Crosstrek with raised side rails","EZREXPM","$80–$120",{"roof_type":"raised-rails"},"Multi-fit Subaru bars."),
 ("B0GX94PB8J","300 lb Adjustable Lockable Cross Bars, 2019-2025 Forester","Generic","$90–$130",{"roof_type":"raised-rails"},"Confirm trim on listing."),
])
add("tesla","model-3","2017-present","roof-racks",[
 ("B0FX44TW2R","WheelX Lockable Cross Bars, 2017-2026 Model 3, 176 lb","WheelX","$150–$220",{"roof_type":"fixed-points"},"Lists Highland; fixed-point mount."),
 ("B09T3LXFL3","AUPACBO Cross Bars, 2017-2025 Model 3","AUPACBO","$140–$200",{"roof_type":"fixed-points"},"Fixed-point mount."),
 ("B0BN1N2QX4","AUXPACBO Lockable Roof Rack, 2017-2023 Model 3","AUXPACBO","$150–$220",{"roof_type":"fixed-points","year_to":2023},"Pre-Highland only."),
 ("B0GV1CCG1Y","220 lb Aero Cross Bars, 2017-2024 Model 3","Generic","$130–$190",{"roof_type":"fixed-points"},"Confirm Highland (2024+) with seller."),
])
add("hyundai","palisade","2020-2025","roof-racks",[
 ("B0DDH72T81","Tuyoung 300 lb Lockable Cross Bars, 2019-2025 Palisade SE/SEL/XRT/Limited/Calligraphy","Tuyoung","$100–$140",{"roof_type":"raised-rails"},"All trims with side rails."),
 ("B0CJPS7RJL","HmmtyRack 300 lb Lockable Cross Bars, 2019-2025 Palisade","HmmtyRack","$100–$140",{"roof_type":"raised-rails"},"All trims with side rails."),
 ("B08CSVZML6","Snailfly Lockable Cross Bars, 2019-2025 Palisade with flush side rails","Snailfly","$90–$130",{"roof_type":"raised-rails"},"Seller describes the rails as flush — match your roof."),
 ("B0CKP9QYP7","EYOUHZ 300 lb Lockable Cross Bars, 2019-2025 Palisade with side rails","EYOUHZ","$100–$140",{"roof_type":"raised-rails"},"Side-rail trims."),
])
add("jeep","grand-cherokee","2022-present","roof-racks",[
 ("B0CW1GPQD1","260 lb Cross Bars, 2022-2025 Grand Cherokee & 2021-2025 Grand Cherokee L (factory flush side rails only)","Generic","$100–$140",{"roof_type":"flush-rails"},"Flush-rail roofs only."),
 ("B0C3BVJBJB","Wonderdriver 300 lb Cross Bars, 2021-2026 Grand Cherokee L & Grand Cherokee","Wonderdriver","$100–$150",{"roof_type":"flush-rails"},"Heavy duty."),
 ("B0DJY2P54T","300 lb Low-Noise Cross Bars, 2022-2026 Grand Cherokee / 2021-2026 Grand Cherokee L","Generic","$100–$150",{"roof_type":"flush-rails"},"Low wind noise."),
 ("B0D3TBG2NW","FLYCLE 220 lb Lockable Cross Bars, 2022-2025 Grand Cherokee WL / 2021-2025 Grand Cherokee L","FLYCLE","$90–$130",{"roof_type":"flush-rails"},"Anti-theft lock."),
])
add("toyota","rav4","2019-present","roof-racks",[
 ("B081J9P2KY","Autekcomma 260 lb Lockable Cross Bars, 2019-2025 RAV4 (not LE / Adventure / TRD Off-Road / Woodland)","Autekcomma","$90–$130",{"roof_type":"raised-rails"},"Standard raised rails only."),
 ("B08LG42HL8","FLYCLE Lockable Cross Bars, 2019-2025 RAV4 (not Adventure / TRD Off-Road)","FLYCLE","$80–$120",{"roof_type":"raised-rails"},"Standard rails only."),
 ("B07WGHX1K5","ROKIOTOEX Cross Bars, 2019-2024 RAV4 Adventure / TRD factory raised rails","ROKIOTOEX","$100–$150",{"roof_type":"raised-rails","trim":"Adventure/TRD Off-Road"},"Adventure / TRD rails only."),
 ("B0GDYBR15P","Aluminum Cross Bars, 2019-2025 RAV4, no-drill","Generic","$70–$110",{"roof_type":"raised-rails"},"Confirm trim on listing."),
 ("B0CGRJFWDV","VEVOR 160 lb Lockable Cross Bars, 2020-2023 RAV4 (not Adventure / TRD Off-Road)","VEVOR","$60–$90",{"roof_type":"raised-rails"},"Listed 2020-2023; confirm other years."),
])
add("kia","telluride","2020-present","roof-racks",[
 ("B0DXPZDL1P","Lockable Aluminum Cross Bars, 2020-2025 Telluride","Generic","$90–$130",{"roof_type":"raised-rails"},"Standard trims."),
 ("B09TW15M9N","Snailfly Lockable Cross Bars, 2019-2025 Telluride EX / S / SX / SX-P (except LE, X-Line, X-Pro)","Snailfly","$90–$130",{"roof_type":"raised-rails"},"Not for X-Line / X-Pro rails."),
 ("B0CZZWTQNH","Tuyoung 300 lb Cross Bars, 2023-2025 Telluride X-Pro & X-Line raised rails","Tuyoung","$100–$140",{"roof_type":"raised-rails","trim":"X-Line/X-Pro"},"X-Line / X-Pro only."),
 ("B0BM9ZMDTC","Snailfly 165 lb Cross Bars, 2023-2025 Telluride X-Pro / X-Line","Snailfly","$90–$130",{"roof_type":"raised-rails","trim":"X-Line/X-Pro"},"X-Line / X-Pro only."),
])
add("ford","explorer","2020-present","roof-racks",[
 ("B0CSVZHTXH","KINGGERI 330 lb Cross Bars, 2020-2026 Explorer with factory raised side rails","KINGGERI","$100–$150",{"roof_type":"raised-rails"},"Raised rails only; not flush-rail trims."),
 ("B0GJSW8FP5","Powerty 300 lb Lockable Cross Bars, 2020-2026 Explorer","Powerty","$90–$140",{"roof_type":"raised-rails"},"Raised side rails."),
 ("B0F4X7FN9V","OBNAUX 300 lb Cross Bars, 2020-2025 Explorer raised rails","OBNAUX","$90–$130",{"roof_type":"raised-rails"},"Raised side rails."),
 ("B0BQJ76YR6","KitsPro 260 lb Cross Bars, 2020-2025 Explorer (raised side rails only)","KitsPro","$80–$120",{"roof_type":"raised-rails"},"Raised rails only."),
 ("B0BX46Q12R","PARTOL Lockable Cross Bars, 2020-2024 Explorer raised rails","PARTOL","$80–$120",{"roof_type":"raised-rails"},"Listed 2020-2024; confirm 2025+."),
])

# ================================================================ HITCHES
add("jeep","wrangler","2018-present","hitches",[
 ("B07CC2TLB6","CURT 13392 Class 3 Trailer Hitch 2 in, 2018-2026 Wrangler JL (also fits JK)","CURT","$200–$270",{},"Brand-name; bolt-on under rear bumper."),
 ("B07CGV7SHR","Mopar Class 2 Receiver Hitch, 2018+ Wrangler JL","Mopar","$250–$350",{},"OEM part; confirm bumper style (steel vs plastic)."),
 ("B0CFF2SVB6","WeiSen Class 3 Hitch 2 in + 4-pin wiring harness, 2018-2025 Wrangler JL","WeiSen","$150–$210",{},"Hitch + harness bundle."),
 ("B07Z7YYM54","Xprite Class 3 Rear Receiver Hitch 2 in, 2018+ Wrangler JL 2-door & 4-door","Xprite","$120–$170",{},"Budget; 2- and 4-door."),
 ("B0H6Y15PL9","Bolt-On Class 3 Hitch 2 in, 6,000 lb, 2018-2026 Wrangler JL","Generic","$130–$190",{},"Vehicle tow rating still applies."),
])
add("ford","explorer","2020-present","hitches",[
 ("B08448PCYS","CURT 13438 Class 3 Trailer Hitch 2 in, 2020+ Explorer","CURT","$200–$270",{},"Brand-name; skip if factory Class 3/4 receiver fitted."),
 ("B0CF5J19JR","KUAFU Class 3 Trailer Hitch 2 in, 2020-2026 Explorer","KUAFU","$120–$170",{},"Budget; bike rack / carrier."),
 ("B0DQ3T4NYK","TLAPS Class 3 Trailer Hitch 2 in, 2020-2026 Explorer","TLAPS","$130–$190",{},"Budget."),
 ("B0H93PJXMS","D Solutions Class 3 Trailer Hitch 2 in, 2020-2024 Explorer","D Solutions","$130–$190",{"year_to":2024},"Listed 2020-2024; confirm 2025+."),
])
add("honda","pilot","2023-present","hitches",[
 ("B0GX1489FJ","Class 3 Trailer Hitch 2 in (13472-style), 2023-2026 Pilot","Generic","$150–$220",{},"Lists 2023-2026; all trims incl. TrailSport."),
 ("B0GN2F4ZTF","maXpeedingrods Class 3 Trailer Hitch 2 in, 2023+ Pilot","maXpeedingrods","$120–$180",{},"Budget; confirm TrailSport fit with seller."),
 ("B0H3TH6CLP","AutoBeeDen Class 3 Trailer Hitch 2 in, 2023+ Pilot","AutoBeeDen","$120–$180",{},"Budget."),
])
add("honda","cr-v","2023-present","hitches",[
 ("B08YPB3MV9","Draw-Tite 76342 Class 3 Trailer Hitch 2 in, 2017-2026 CR-V","Draw-Tite","$200–$270",{},"Brand-name; listing covers 2017-2026."),
 ("B0GCCRDQ9G","Class 3 Trailer Hitch 2 in (13397-style), 2017-2026 CR-V","Generic","$130–$190",{},"Budget."),
 ("B0H836JYYY","AutoBeeDen Class 3 Trailer Hitch 2 in, 2023+ CR-V","AutoBeeDen","$120–$180",{},"Budget; confirm hybrid fit with seller."),
])
add("jeep","grand-cherokee","2022-present","hitches",[
 ("B07NWF6VBS","CURT 13525 Class 3 Trailer Hitch 2 in, 2022-2026 Grand Cherokee & 2021-2026 Grand Cherokee L","CURT","$220–$300",{},"Brand-name; 7,500 lb GTW hitch rating — your vehicle rating still rules."),
 ("B0FRRSRSJ4","Autekcomma Class 3 Trailer Hitch 2 in (13525-style), 2022-2026 Grand Cherokee / Grand Cherokee L","Autekcomma","$130–$190",{},"Budget."),
 ("B0H48MF8BF","Class 3 Trailer Hitch 2 in, 2022-2024 Grand Cherokee & 2021-2024 Grand Cherokee L","Generic","$130–$190",{"year_to":2024},"Listed through 2024; confirm 2025+."),
])
add("ford","bronco","2021-present","hitches",[
 ("B0B9NPWBQH","CURT 13493 Class 3 Trailer Hitch 2 in, 2021-2026 Bronco without factory receiver","CURT","$200–$270",{},"Brand-name; only for trucks without the factory hitch. Not Bronco Sport."),
 ("B09Q5V2LNC","Snailfly Class 3 Trailer Hitch 2 in, 2021-2026 Bronco (not Bronco Sport)","Snailfly","$130–$190",{},"Budget; 2- and 4-door."),
 ("B0BNH665PQ","Upgraded Class 3 Trailer Hitch 2 in, 2021-2026 Bronco (not Bronco Sport)","Generic","$120–$180",{},"Budget."),
 ("B0CP8YGJKS","YZONA Hitch Receiver Kit with cover, 2021-2025 Bronco 2-door & 4-door","YZONA","$120–$180",{},"Includes receiver cover."),
])
add("subaru","outback","2020-present","hitches",[
 ("B0FWC1VHNS","TUZILLA Class 3 Trailer Hitch 2 in, 2020-2026 Outback (all) / 2020-2025 Legacy","TUZILLA","$130–$190",{},"Subaru rates the Outback 2,700–3,500 lb by engine; hitch rating does not raise it."),
 ("B0G24ZSLKC","WOLFSTORM Class 3 Trailer Hitch 2 in, 2020-2025 Outback & Legacy","WOLFSTORM","$120–$180",{},"Budget."),
 ("B0G12TJSRT","AUTOFREE Class III Tow Hitch 2 in, 2020-2025 Outback & Legacy","AUTOFREE","$120–$180",{},"Budget."),
 ("B0FGY1SKY5","Class 3 Trailer Hitch 2 in, 2020-2026 Outback (all trims)","Generic","$120–$180",{},"Confirm Wilderness fit with seller."),
])
add("kia","telluride","2020-present","hitches",[
 ("B07VMNPFQH","CURT 13420 Class 3 Trailer Hitch 2 in, concealed body, select 2020+ Telluride","CURT","$220–$300",{},"Brand-name; confirm 2025 on listing."),
 ("B07TW9M782","Kia Genuine OEM Telluride Tow Hitch with Harness","Kia","$450–$650",{},"OEM kit incl. harness."),
 ("B0FZG3J9GH","Wsays Class 3 Trailer Hitch 2 in, 2020-2025 Telluride","Wsays","$130–$190",{},"Budget."),
 ("B0CT5GF8W5","Class 3 Trailer Hitch 2 in, 2020-2025 Telluride & Palisade, 5,000 lb GTW","Generic","$130–$190",{},"Budget."),
])
add("hyundai","palisade","2020-2025","hitches",[
 ("B07XYN395W","CURT 13427 Class 3 Trailer Hitch 2 in, select 2020+ Palisade","CURT","$200–$280",{},"Brand-name."),
 ("B0CQSY7JPC","KUAFU Class 3 Trailer Hitch 2 in (13427-style), 2020-2025 Palisade & Telluride","KUAFU","$120–$180",{},"Budget."),
 ("B0FS55TN7X","Class 3 Trailer Hitch 2 in, 2020-2025 Palisade / Telluride","Generic","$120–$180",{},"Budget."),
])

# ================================================================ RUNNING BOARDS
add("ford","f-150","2021-present","running-boards",[
 ("B0CTK467CG","Nilight 6 in Aluminum Running Boards, 2015-2026 F-150 SuperCrew","Nilight","$150–$220",{"cab":"SuperCrew"},"SuperCrew only; bolts to factory rocker holes."),
 ("B08DD4WMLQ","YITAMOTOR 6 in Running Boards, 2015-2025 F-150 SuperCrew","YITAMOTOR","$150–$220",{"cab":"SuperCrew"},"SuperCrew only."),
 ("B0CT5H96YH","Just-V 4 in Drop-Down Running Boards, 2015-2025 F-150 SuperCrew","Just-V","$180–$260",{"cab":"SuperCrew"},"Drop steps; SuperCrew only."),
 ("B0D3XG4Y5L","6 in 2-Step Side Rails, 2015-2026 F-150 SuperCrew","Generic","$140–$200",{"cab":"SuperCrew"},"Budget."),
])
_T1_BOARDS = [
 ("B0DG8QB7RY","3STONZ 6 in Aluminum Running Boards, 2019-2025 Silverado/Sierra 1500 Crew Cab","3STONZ","$160–$230",{"cab":"Crew Cab"},"Crew Cab only."),
 ("B0BHWGXLHC","OEDRO 6 in Running Boards, 2019-2025 Silverado/Sierra 1500 Crew Cab","OEDRO","$150–$220",{"cab":"Crew Cab"},"Paintable step plates."),
 ("B07MCDNK9S","TAC 5 in Oval Side Steps, 2019-2025 Silverado/Sierra 1500 Crew Cab","TAC","$130–$190",{"cab":"Crew Cab"},"Budget tube steps."),
 ("B0CW3NM48D","2-Step Running Boards, 2019-2025 Silverado/Sierra 1500 Crew Cab (excl. 2019 LD)","Generic","$140–$200",{"cab":"Crew Cab"},"Not 2019 Limited/LD (old body)."),
]
add("chevrolet","silverado-1500","2019-present","running-boards",_T1_BOARDS)
add("gmc","sierra-1500","2019-present","running-boards",_T1_BOARDS[:2] + [
 ("B0CLZJ2QC7","RHOBRA 6 in Running Boards, 2019-2026 Silverado/Sierra 1500 Crew Cab","RHOBRA","$150–$220",{"cab":"Crew Cab"},"OE-style."),
])
add("ram","1500","2019-present","running-boards",[
 ("B0C4SCZR2C","PZ 6 in Aluminum Running Boards, 2019-2025 Ram 1500 Crew Cab New Body (not Classic)","PZ","$150–$220",{"cab":"Crew Cab"},"DT only; not Classic."),
 ("B0DCDQ23BJ","BINARY STAR 6 in Running Boards, 2019-2025 Ram 1500 Crew Cab New Body","BINARY STAR","$140–$200",{"cab":"Crew Cab"},"DT only."),
 ("B09QYWN42V","SMANOW Drop-Down Side Steps, 2019-2026 Ram 1500 Crew Cab New Body","SMANOW","$160–$230",{"cab":"Crew Cab"},"Drop steps; DT only."),
 ("B0GCDN7ZCB","Running Boards, 2019-2025 Ram 1500 Crew Cab (excl. Classic)","Generic","$130–$190",{"cab":"Crew Cab"},"Budget."),
])
add("toyota","tundra","2022-present","running-boards",[
 ("B0B97VX42F","Rough Country BA2 5 in Running Boards, 2022-2025 Tundra CrewMax","Rough Country","$200–$280",{"cab":"CrewMax"},"Brand-name; CrewMax only."),
 ("B09Z6KMM4V","OTHOWE Flat Oval Running Boards, 2022-2026 Tundra CrewMax","OTHOWE","$150–$220",{"cab":"CrewMax"},"CrewMax only."),
 ("B0DL5NGNXV","TIEZFUL Drop-Down Side Steps, 2022-2026 Tundra CrewMax","TIEZFUL","$180–$260",{"cab":"CrewMax"},"Drop steps."),
 ("B0D3X95ZRT","6 in 2-Step Side Rails, 2022-2026 Tundra CrewMax","Generic","$140–$200",{"cab":"CrewMax"},"Budget."),
])
add("chevrolet","tahoe","2021-present","running-boards",[
 ("B09J4W1JRW","HD Ridez 5 in Running Boards, 2021-2025 Tahoe & Yukon (not Yukon XL / Suburban)","HD Ridez","$150–$220",{},"Tahoe/Yukon wheelbase only."),
 ("B0CF8GH8T9","Aluminum Side Steps, 2021-2025 Tahoe","Generic","$180–$260",{},"OE-style board."),
 ("B0F9F7SV4J","Deployable Electric Power Running Boards, 2021-2025 Tahoe","Generic","$600–$900",{},"Power steps; wiring required — confirm harness with seller."),
])
add("toyota","sequoia","2023-present","running-boards",[
 ("B0G6Z9PMB7","POFENZE Running Boards, 2023-2026 Sequoia","POFENZE","$150–$220",{},"Carbon steel, wide step."),
 ("B0G6YH3VXJ","2-Step Running Boards, 2023-2026 Sequoia","Generic","$150–$220",{},"Budget."),
 ("B0DF6KZP3X","2-Pc Running Boards with brackets, 2023-2025 Sequoia","Generic","$180–$260",{},"OE-style."),
 ("B0F5H7M2PV","Deployable Electric Power Running Boards, 2023-2026 Sequoia","Generic","$700–$1,000",{},"Power steps; confirm install kit with seller."),
])
add("toyota","tacoma","2024-present","running-boards",[
 ("B0DPHXYSGS","TAC Gen5 4 in Drop Side Steps, 2024-2025 Tacoma Double Cab (incl. Hybrid)","TAC","$180–$260",{"cab":"Double Cab"},"Double Cab only; lists i-FORCE MAX hybrid."),
 ("B0DBHWJ4X4","BINARY STAR Wheel-to-Wheel Running Boards, 2024-2026 Tacoma Double Cab","BINARY STAR","$170–$240",{"cab":"Double Cab"},"Wheel-to-wheel coverage."),
 ("B0CY1ZW3QN","OTHOWE 5.5 in Step Bars, 2024-2026 Tacoma Double Cab","OTHOWE","$140–$200",{"cab":"Double Cab"},"No drilling."),
 ("B0D91Y7XN9","CLAMBER 7.5 in Nerf Bars / Rock Sliders, 2024-2025 Tacoma Double Cab","CLAMBER","$200–$280",{"cab":"Double Cab"},"Slider-style step."),
])
add("nissan","frontier","2022-present","running-boards",[
 ("B09NRWB49Y","TAC Sidewinder 4 in Drop Side Steps, 2005-2026 Frontier Crew Cab","TAC","$170–$240",{"cab":"Crew Cab"},"Crew Cab only; listing spans both generations — confirm bracket fit for 2022+ with seller."),
 ("B0FG32L3H3","TIEZFUL 2-Step Running Boards, 2005-2025 Frontier Crew Cab","TIEZFUL","$150–$220",{"cab":"Crew Cab"},"Crew Cab; confirm 2022+ with seller."),
 ("B0G336DBYZ","TIEZFUL 5.1 in Drop-Down Side Steps, 2005-2025 Frontier Crew Cab","TIEZFUL","$160–$230",{"cab":"Crew Cab"},"Crew Cab; confirm 2022+ with seller."),
])
add("subaru","forester","2019-2024","hitches",[
 ("B089T7SGQ4","Draw-Tite 36671 Class 2 Trailer Hitch 1.25 in, 2019-2026 Forester","Draw-Tite","$180–$250",{"receiver_in":1.25},"Brand-name; 1.25 in receiver."),
 ("B0876X7Y23","Reese Towpower 06191 Class 2 Trailer Hitch 1.25 in, 2019-2026 Forester","Reese","$170–$240",{"receiver_in":1.25},"Brand-name; 1.25 in."),
 ("B07PDHHSST","CURT 13409 Class 3 Trailer Hitch 2 in, select Forester","CURT","$200–$270",{"receiver_in":2},"2 in for bike racks; Forester tow rating stays 1,500 lb. Confirm years on listing."),
 ("B0F9L6DMRT","Wsays Class 3 Trailer Hitch 2 in, 2019-2026 Forester","Wsays","$120–$180",{"receiver_in":2},"Budget."),
])
add("tesla","model-3","2017-present","hitches",[
 ("B07YXHNHHW","CURT 13431 Class 3 Trailer Hitch 2 in, select Model 3","CURT","$200–$280",{},"Brand-name; confirm your model year (pre-Highland vs 2024+ Highland) on listing."),
 ("B09DGB75RL","Stealth Hitches Hidden Receiver Hitch (rack package), 2017-2025 Model 3","Stealth Hitches","$350–$500",{},"Hidden receiver; bike racks."),
 ("B0FXGN3CF9","maXpeedingrods Class II Hitch 2 in, 2017-2023 Model 3","maXpeedingrods","$120–$180",{"year_to":2023},"Pre-Highland only."),
])
