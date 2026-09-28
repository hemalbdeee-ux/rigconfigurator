# Pillar pages brief (Upgrades hubs + Explainers)

Read `db/content/articles/WRITING_BRIEF.md` first: the honesty, sourcing, voice and no-invented-testing rules there apply here unchanged.
Pillar pages are HUBS: they explain, rank and decide, then send the reader to the fit-checked vehicle × category guides.
They do NOT carry their own product picks or ASINs (the site pulls each linked guide's #1 pick from the DB).

## Upgrades module — `<make>_<model>_<genstart>_upgrades.py`
```
KIND = "upgrades"
KEY = ("ford", "f-150", "2021-present")          # DB slugs
CATEGORIES = [...]                                # ONLY categories that have a published guide for this vehicle (you are told which)
TITLE = "2021–2026 Ford F-150 Upgrades, Ranked: ..."   # ≤100 chars
META = "..."                                      # 110–165 chars
FAQ = [(q, a), ...]                               # 8–12, real long-tail questions, 60–130-word answers
ARTICLE = {
  "dek": "...", "author": "jake-morrison", "reviewed": "YYYY-MM-DD",
  "method": "How the order was decided (fitment data, maker specs, the guides' sources). No hands-on claims.",
  "takeaways": [5 short bold-led lines],
  "priority": [ {"category": "<slug in CATEGORIES>", "h": "1. Floor liners first: ...",
                 "why": "120–220 words, vehicle-specific: why this upgrade ranks here, what decides fit on THIS vehicle (bed length, cab, trim, rails...), the trade-off, rough cost band from the linked guide",
                 "skip_if": "one line"} , ... ],       # every CATEGORY once, in recommended order
  "tier_table": {"caption": "...", "head": ["Upgrade", "Budget", "Mid", "Premium"], "rows": [[...], ..., ["Total", "...", "...", "..."]]},
                 # price bands must come from the linked guides (read their picks' "price" fields) — say "about"
  "sections": [{"h": "...", "body": "markdown"}...],  # 3–5: e.g. things this vehicle does NOT need (factory receiver? say so), order-of-install/compatibility (rack + tonneau), trims that change fit, what to buy first on a budget
  "avoid": [{"h": "...", "body": "..."} x4],
  "verdict": {"thesis": "one bold sentence", "body": "2 paragraphs"},
  "sources": [[label, url], ...]                   # ≥4; reuse sources from the vehicle's guides + maker pages
}
```
Get the facts from the vehicle's existing guides: `db/content/articles/<make>_<model>_<genstart>_*.py` (top_picks, picks[].price, fit_table, look_for, FAQ). Stay consistent with them.
Mention category phrases naturally ("tonneau cover", "bed rack", "floor liners", "running boards", "light bar", "trailer hitch") — the page autolinks them.
Minimum 2,800 words (ARTICLE + FAQ). Aim 3,200–4,000.

## Explainer module — `<slug_with_underscores>.py`
```
KIND = "explainer"
SLUG = "hard-vs-soft-tonneau-covers"
CATEGORIES = ["tonneau-covers"]                  # the category guides this explainer feeds
TITLE = "Hard vs Soft Tonneau Covers: ..."       # text before ":" becomes the SEO title, keep it ≤ 41 chars
META, FAQ (8–12) as above
ARTICLE = {
  "dek", "author", "reviewed", "method", "takeaways": [5],
  "compare_table": {"caption", "head", "rows"},   # the core X-vs-Y matrix
  "sections": [{"h", "body", "table"?}] ≥5,       # mechanism, security, weather, access, cost, install, weight/MPG claims (only if sourced)...
  "decision": [{"if": "...", "then": "..."} ≥3],  # "If you haul tall loads weekly: ..."
  "avoid": [4], "verdict", "sources": ≥4
}
```
Minimum 2,500 words. Aim 2,800–3,600. Numbers (SAE/ratings/weights/prices) only from pages you actually read; cite them in sources.

## Finish
`python3 db/content/validate_pillars.py db/content/pillars/<files>` → fix until PASS.
