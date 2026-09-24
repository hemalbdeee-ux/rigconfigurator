# RigConfigurator long-form article brief (for writers / agents)

You are writing ONE Python module per page in `db/content/articles/`, in exactly the same shape as the
approved pilot: `db/content/articles/ford_f150_2021_tonneau.py` — READ IT FIRST and mirror its structure,
depth, tone and field names. The owner approved that page; match it.

## File
- Name: `<make>_<model>_<genstart>_<category>.py`, lowercase, dashes → underscores
  (e.g. `chevrolet_silverado_1500_2019_tonneau.py`, `toyota_tacoma_2024_tonneau.py`).
- Module constants: `KEY`, `TITLE`, `META`, `FAQ`, `ARTICLE`, `FITS` (see pilot).
- `KEY` = (make_slug, model_slug, gen_slug, category_slug) exactly as in the DB
  (see `db/migrations/003_vehicles.sql` for vehicles; category slugs: tonneau-covers, bed-racks, roof-racks,
  cargo-boxes, hitches, floor-mats, running-boards, led-light-bars).
- `ARTICLE["author"] = "jake-morrison"`, `ARTICLE["reviewed"] = "2026-09-24"`.
- Titles: current generations use "YYYY–2026" (e.g. "2019–2026 Chevy Silverado 1500"); ended generations use their real span.
- META 120–165 chars. TITLE ≤ 100 chars, includes the vehicle + a number/qualifier.

## Research rules (non-negotiable)
1. Vehicle facts (bed lengths in inches, cabs, trims, special beds/tailgates, roof type, tow rating, generation
   changes) — read `db/migrations/003_vehicles.sql` for our stored facts, then confirm/extend from the
   manufacturer or a reliable reference (Wikipedia generation page, manufacturer spec sheet).
2. Products: 5–7 picks spanning budget → premium, prefer real brands (for tonneau: BAK/BAKFlip, Gator,
   RetraxPRO, TruXedo, Tyger, UnderCover, Extang, Rough Country, Worksport, Peragon, etc.).
   Each pick MUST have an Amazon ASIN found via WebSearch restricted to amazon.com whose listing TITLE names
   this vehicle/generation and the right size (bed length / cab / trim). Record that title as the FITS name.
   If you can't find an ASIN for a brand, drop that brand — never invent an ASIN.
3. Specs (load rating, material, warranty, weight, install time, price) come from the maker's page or
   RealTruck/etrailer/official store (WebFetch works on realtruck.com, etrailer.com, maker sites; amazon.com
   pages are blocked). Quote prices as "RealTruck lists it at $X" or a price band; if unverified say "about $X"
   or use the FITS band. Never state a number you did not read.
4. NO invented hands-on testing. Never write "we tested", "our testing", "we installed", "hands-on",
   "after N miles", "our truck". Authority = fitment data + maker specs + cited owner reports.
   Owner reports: only cite a forum thread you actually opened/searched ("owners on TacomaWorld report…").
5. Anything unverified → "confirm on the listing" / "ask the seller" (and the word "confirm" in the FITS note
   lowers confidence automatically).
6. 6–9 `sources` entries: every maker/retailer page you used + reference pages.

## Content requirements (validator enforces)
- ≥3,000 words total (ARTICLE + FAQ). Aim 3,300–4,200.
- takeaways 5 · top_picks 4–5 · look_for 4–5 sections (100–150 words each, vehicle-specific) ·
  look_table 5–6 rows · types_table (category-appropriate) · picks 5–7 (each: 5 pros, 3 cons, 2 paragraphs
  body 180–280 words with the specific facts, "who" line, 6–9 spec rows) · install 5–7 steps ·
  avoid 4 items · FAQ 9–10 real long-tail questions (60–130-word answers) · verdict thesis + 2 paragraphs.
- fit_table where it helps (bed lengths / cab / trim / rail type).
- Vehicle-specific gotchas are the unique value: special tailgates (MultiPro, Pro Access, RamBox, CarbonPro,
  deck rail / utility track, Utili-track, factory bed rails, hybrid batteries, etc.). Explain what they mean
  for fit.
- Verdict body: mention 1–2 related categories naturally (e.g. "floor liners", "running boards", "bed rack",
  "roof rack", "trailer hitch") — the site auto-links those phrases to sibling pages. If an older/newer
  generation exists in the DB, mention it as "YYYY–YYYY <Model>" (e.g. "2016–2023 Tacoma") so it autolinks.
- Voice: declarative expert, concrete numbers, benefit then trade-off. No fluff, no emojis, American English.
- Text must not contain the strings `$a$`, `$t$`, `$f$`, `$m$`.

## FITS
`(asin, amazon_listing_title_shortened, brand, price_band, cond_dict, note)` — picks first in pick order,
then optional size variants (e.g. other bed length versions of the same product). cond_dict uses the
vehicle facts, e.g. `{"bed_length_in": 67}`, `{"cab": "Crew Cab"}`, `{"roof_type": "raised-rails"}`.

## Before you finish
Run `python3 db/content/validate_articles.py db/content/articles/<your files>` from the repo root
(`/home/claude/rigconfigurator`) and fix every ✗ until PASS. Report: file names, word counts, picks+ASINs,
and any fact you could not verify.
