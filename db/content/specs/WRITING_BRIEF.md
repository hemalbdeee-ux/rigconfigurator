# Spec pages: writing brief

A spec page answers one lookup question for one model ("Toyota Tacoma towing capacity") or one generation.
URL: `/specs/<make>/<model>/<topic>`. One file per page in this folder → `build_specs_sql.py` → `014_spec_pages.sql`.

Rules (the validator enforces the first four):
1. Every table row ends with a source number. No source, no row. No source at all, no page.
2. Sources are the maker's own documents: owner's manual, brochure spec table, press spec sheet, towing guide.
   A dealer page, forum or retailer is not a source for a spec figure.
3. Write the figure exactly as the source prints it, with its condition (engine, cab, drivetrain, package).
   Never fill a blank cell from memory or from another model year. Leave the model year out and say so on the page.
4. Publish only what is sourced. The `covers` line names exactly the model years on the page and `not_covered` names the rest;
   the title promises no years the page does not have. (Owner approved the page format on 19 Nov 2026.)
5. One page per answer. When every year of a generation shares a figure, that is one section, not one page per year.
6. 300–700 words outside the tables. Answer first, then tables, then how to check your own vehicle. No filler.
7. Safety figures (towing, tongue weight, payload, lug nut torque, roof load): add the line telling the reader that the
   label on their own vehicle and its owner's manual override this page.
8. No invented testing, no "we measured". The page reports what the maker published and says where.

Module fields: KEY=(make_slug, model_slug, topic), MAKE, MODEL, TOPIC_LABEL, PUBLISH, TITLE (H1), SEO_TITLE (≤60),
META (≤155), FAQ [(q, a)], PAGE {answer, reviewed, covers, not_covered?, sections[{id, h, intro?, table{head, rows}, notes?}],
check[], related[category slugs], sources[(label, url)]}.

## Sequence and release (owner's rule, 19 Nov 2026: 10–15 pages a day, in order)
- `QUEUE.csv` is the order of work: one model at a time, every topic of that model, then the next model. Take the next `todo`
  rows in `seq` order; a row whose maker source cannot be found gets status `blocked` and a note, never an invented figure.
- Every figure is read from the maker document twice (two separate reads); a value the two reads disagree on, or whose column
  mapping is unclear, is left out.
- `PUBLISH = True` plus `PUBLISH_AT = "YYYY-MM-DD"`: the page goes live at 10:00 Asia/Dhaka on that day (column `publish_at`).
  At most 12 pages per day. After writing, set the QUEUE row to `scheduled` with the date, file name and covered years.
- Internal links are automatic: other specs of the same model, the same spec of other models, the model's guides and hubs.
  Put the matching accessory categories in `related`.
- Maker documents that work: fromtheroad.ford.com spec PDFs (Ford), toyota.com eBrochures and pressroom.toyota.com (Toyota).
