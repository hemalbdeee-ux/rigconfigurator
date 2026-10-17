"""Real-world fit embeds per guide: install videos (YouTube) and owner posts (Reddit), shown through each platform's own
embed. Keyed by "make/model/gen/category" (same as an article module's KEY). build_articles_sql.py merges each list into
that article's JSON as "embeds". Rules: only public posts and videos; never download or re-host the media; the
note says what the reader should look at; every entry was checked by a person before it was added.

Entry shapes:
  {"kind": "youtube", "id": "<11-char video id>", "title": "...", "channel": "...", "note": "..."}
  {"kind": "reddit", "url": "https://www.reddit.com/r/<sub>/comments/<id>/<slug>/", "title": "...", "sub": "<sub>", "author": "<user>", "note": "..."}
"""

EMBEDS: dict[str, list[dict]] = {
 "toyota/4runner/2025-present/roof-racks": [
  {"kind": "youtube", "id": "Xo4XvFauqoI", "title": "SHERPA Roof Rack for 6th Gen Toyota 4Runner: How to Install", "channel": "Alldogs Offroad Coop", "note": "the Sherpa Capitol going on a 2025 4Runner"}],
 "chevrolet/silverado-1500/2019-present/floor-mats": [
  {"kind": "youtube", "id": "EWRCvo_4dfg", "title": "2019-2026 Chevy Silverado 1500 Floor Mats: LASFIT Installation & Fit Review", "channel": "Lasfit Auto Lighting", "note": "the maker's own video; watch how the liner meets the door sill"}],
 "ford/f-150/2021-present/running-boards": [
  {"kind": "youtube", "id": "B0qxIYjjLHQ", "title": "2021-2023 F-150 AMP Research PowerStep Running Boards Review & Install", "channel": "AmericanTrucks Ford", "note": "power steps on the 14th-gen F-150; the video covers 2021-2023 trucks"}],
 "gmc/sierra-1500/2019-present/running-boards": [
  {"kind": "youtube", "id": "-U3Hh-CBxe4", "title": "2019-2023 Sierra 1500 RB20 Running Boards Review & Install", "channel": "AmericanTrucks Chevy & GMC", "note": "Go Rhino RB20 on a 2019-2023 Sierra"}],
 "ford/f-150/2021-present/tonneau-covers": [
  {"kind": "youtube", "id": "J7D9xZzWqNI", "title": "2021-2025 F-150 Rough Country Hard Low Profile Tri-Fold Tonneau Cover Review & Install", "channel": "AmericanTrucks Ford", "note": "a hard tri-fold on the 14th-gen bed"}],
 "kia/telluride/2020-present/hitches": [
  {"kind": "youtube", "id": "rbaX_cV_720", "title": "DIY Install: etrailer Trailer Hitch Receiver on a 2023 Kia Telluride", "channel": "etrailer", "note": "a bolt-on 2 in receiver, step by step"}],
 "ford/ranger/2024-present/tonneau-covers": [
  {"kind": "youtube", "id": "-p_u-VtiRN4", "title": "How to Install BAKFlip MX4 Hard Folding Tonneau Cover on a 2024 Ford Ranger", "channel": "RealTruck.com", "note": "install on the new-generation Ranger bed"}],
 "toyota/highlander/2020-present/hitches": [
  {"kind": "youtube", "id": "4bVktWwsAGQ", "title": "2020-2025 Toyota Highlander Trailer Hitch Installation (AP3002A)", "channel": "U-Haul Trailer Hitches And Towing", "note": "an installer fitting a receiver to the 4th-gen Highlander"}],
 "toyota/tacoma/2024-present/running-boards": [
  {"kind": "youtube", "id": "dwRFiq3Tgp0", "title": "2024-2025 Tacoma RedRock 4-Inch Drop TC1 Running Boards Review & Install", "channel": "ExtremeTerrain Toyota", "note": "drop-step boards on the 4th-gen Tacoma (the retailer's own brand)"}],
 "toyota/tacoma/2016-2023/tonneau-covers": [
  {"kind": "youtube", "id": "z6h58bzgujQ", "title": "2016-2023 Tacoma RedRock Soft Roll-Up Tonneau Cover Review & Install", "channel": "ExtremeTerrain Toyota", "note": "a soft roll-up on the 3rd-gen bed and deck rails (the retailer's own brand)"}],
 "ford/explorer/2020-present/roof-racks": [
  {"kind": "youtube", "id": "Qxq31fSadFM", "title": "2020+ Ford Explorer with Thule Rapid Crossroad WingBar Evo Roof Rack", "channel": "Rack Attack", "note": "Thule bars on the factory raised rails"}],
}
