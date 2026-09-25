import type { Category, Vehicle } from "@/lib/queries";

const model = (v: Vehicle) => /^\d+(\s|$)/.test(v.model_name) ? `${v.make_name} ${v.model_name}` : v.model_name;

export const BRAND = "Rig Configurator";
const SUFFIX = ` | ${BRAND}`;
export const MAX_TITLE = 60;

/**
 * <title> for search results (≤ 60 chars), kept separate from the on-page H1.
 * Tries each candidate with the brand suffix, then without, then cuts the last one at a word boundary.
 * Returned as { absolute } so the layout's "%s | Rig Configurator" template is not applied twice.
 */
export function seoTitle(...candidates: string[]): { absolute: string } {
  for (const c of candidates) if ((c + SUFFIX).length <= MAX_TITLE) return { absolute: c + SUFFIX };
  for (const c of candidates) if (c.length <= MAX_TITLE) return { absolute: c };
  const last = candidates[candidates.length - 1];
  return { absolute: last.slice(0, MAX_TITLE + 1).replace(/\s+\S*$/, "").replace(/[\s,:;–—-]+$/, "") };
}

/** "2024–2026" instead of "2024–present" for titles; ISR keeps the current year fresh. */
export const titleYears = (v: Vehicle) => `${v.year_from}–${v.year_to ?? new Date().getFullYear()}`;

const SHORT: Record<string, string> = {
  "roof-racks": "Roof Racks",
  "hitches": "Trailer Hitches",
  "floor-mats": "Floor Mats",
  "running-boards": "Running Boards",
  "dash-cams": "Dash Cams",
  "lift-kits": "Lift Kits",
};
/** Search-style category name: "Roof Racks & Crossbars" → "Roof Racks". */
export const shortCategory = (c: Category) => SHORT[c.slug] ?? c.name.split(/ & | and /)[0];

export function articleSeoTitle(v: Vehicle, c: Category) {
  const y = titleYears(v), cat = shortCategory(c);
  return seoTitle(
    `Best ${cat} for ${y} ${v.make_name} ${v.model_name}`,
    `Best ${cat} for ${y} ${model(v)}`,
    `${y} ${model(v)} ${cat}`,
  );
}

export function hubSeoTitle(v: Vehicle) {
  const y = titleYears(v);
  return seoTitle(
    `${y} ${v.make_name} ${v.model_name} Accessories That Fit`,
    `${y} ${model(v)} Accessories That Fit`,
    `${y} ${v.make_name} ${v.model_name} Accessories`,
    `${y} ${model(v)} Accessories`,
  );
}

export function categorySeoTitle(c: Category) {
  return seoTitle(`${c.name} by Vehicle: Fit-Checked Guides`, `${shortCategory(c)} by Vehicle: Fit-Checked Guides`, `${shortCategory(c)} by Vehicle`);
}
