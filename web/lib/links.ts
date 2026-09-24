// Internal-link map for contextual links inside article bodies.
// Same vehicle, other categories → category synonyms; same model, other generations, same category → "2015–2020 F-150".
import { q } from "./db";
import { vehiclePath, type Vehicle } from "./queries";

export const CURRENT_MODEL_YEAR = 2026;

export const CATEGORY_PHRASES: Record<string, string[]> = {
  "tonneau-covers": ["tonneau covers", "tonneau cover", "bed cover"],
  "bed-racks": ["bed racks", "bed rack"],
  "roof-racks": ["roof racks", "roof rack", "crossbars"],
  "cargo-boxes": ["cargo boxes", "cargo box"],
  "hitches": ["trailer hitches", "trailer hitch", "receiver hitch"],
  "bike-racks": ["bike racks", "bike rack"],
  "floor-mats": ["floor liners", "floor mats", "floor liner"],
  "seat-covers": ["seat covers"],
  "running-boards": ["running boards", "side steps", "nerf bars"],
  "led-light-bars": ["light bars", "light bar"],
  "dash-cams": ["dash cams", "dash cam"],
  "lift-kits": ["leveling kit", "lift kit"],
};

export async function linkMap(v: Vehicle, currentCategory: string): Promise<Record<string, string>> {
  const rows = await q<{ path: string; category_slug: string; same: boolean; year_from: number; year_to: number | null; model_name: string }>(`
    SELECT '/vehicles/'||m.slug||'/'||v.model_slug||'/'||v.gen_slug||'/'||c.slug AS path, c.slug AS category_slug,
           (v.id=$1) AS same, v.year_from, v.year_to, v.model_name
    FROM fitment_pages fp JOIN vehicles v ON v.id=fp.vehicle_id JOIN makes m ON m.id=v.make_id JOIN categories c ON c.id=fp.category_id
    WHERE fp.status='published' AND ((v.id=$1 AND c.slug<>$2) OR (v.id<>$1 AND v.make_id=(SELECT make_id FROM vehicles WHERE id=$1)
          AND v.model_slug=(SELECT model_slug FROM vehicles WHERE id=$1) AND c.slug=$2))`, [v.id, currentCategory]);
  const map: Record<string, string> = { "vehicle hub": vehiclePath(v), [`${v.model_name} fit hub`]: vehiclePath(v) };
  for (const r of rows) {
    if (r.same) for (const p of CATEGORY_PHRASES[r.category_slug] ?? []) map[p] = r.path;
    else {
      const to = r.year_to ?? CURRENT_MODEL_YEAR; // "-present" generations are written as "2025–2026 4Runner"
      map[`${r.year_from}–${to} ${r.model_name}`] = r.path; map[`${r.year_from}-${to} ${r.model_name}`] = r.path;
    }
  }
  return map;
}
