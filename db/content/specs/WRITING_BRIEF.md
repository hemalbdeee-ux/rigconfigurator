# Spec pages: writing brief

A spec page answers one lookup question for one model ("Toyota Tacoma towing capacity") or one generation.
URL: `/specs/<make>/<model>/<topic>`. One file per page in this folder → `build_specs_sql.py` → `014_spec_pages.sql`.

Rules (the validator enforces the first four):
1. Every table row ends with a source number. No source, no row. No source at all, no page.
2. Sources are the maker's own documents: owner's manual, brochure spec table, press spec sheet, towing guide.
   A dealer page, forum or retailer is not a source for a spec figure.
3. Write the figure exactly as the source prints it, with its condition (engine, cab, drivetrain, package).
   Never fill a blank cell from memory or from another model year. Leave the model year out and say so on the page.
4. `PUBLISH = False` until every model year the title promises is covered and the owner has approved the page.
5. One page per answer. When every year of a generation shares a figure, that is one section, not one page per year.
6. 300–700 words outside the tables. Answer first, then tables, then how to check your own vehicle. No filler.
7. Safety figures (towing, tongue weight, payload, lug nut torque, roof load): add the line telling the reader that the
   label on their own vehicle and its owner's manual override this page.
8. No invented testing, no "we measured". The page reports what the maker published and says where.

Module fields: KEY=(make_slug, model_slug, topic), MAKE, MODEL, TOPIC_LABEL, PUBLISH, TITLE (H1), SEO_TITLE (≤60),
META (≤155), FAQ [(q, a)], PAGE {answer, reviewed, covers, not_covered?, sections[{id, h, intro?, table{head, rows}, notes?}],
check[], related[category slugs], sources[(label, url)]}.
