import { q } from "./db";

/** Spec lookup pages (/specs/<make>/<model>/<topic>). Content: db/content/specs/*.py → 014_spec_pages.sql. */
export type SpecRow = (string | number | number[])[];   // cells…, then the source number(s) of the row
export type SpecSection = { id: string; h: string; intro?: string; table: { head: string[]; rows: SpecRow[] }; notes?: string[] };
export type SpecPage = {
  id: number; make_slug: string; model_slug: string; topic: string; make_name: string; model_name: string; topic_label: string;
  title: string; seo_title: string; meta_desc: string; faq: { q: string; a: string }[]; published_at: string | null;
  page: { answer: string; reviewed: string; covers: string; not_covered?: string; sections: SpecSection[]; check: string[]; related?: string[]; sources: [string, string][] };
};
export const specPath = (p: { make_slug: string; model_slug: string; topic: string }) => `/specs/${p.make_slug}/${p.model_slug}/${p.topic}`;

// The table is created by migration 014. Until that has run on a database, behave as "no spec pages" instead of failing the page.
// A page is live when it is published and its scheduled release time (publish_at, if any) has passed.
const LIVE = `status='published' AND (publish_at IS NULL OR publish_at <= now())`;
async function safe<T>(sql: string, params: any[] = []): Promise<T[]> {
  try { return await q<T>(sql, params); } catch (e: any) { if (e?.code === "42P01" || e?.code === "42703") return []; throw e; }
}

export async function getSpec(make: string, model: string, topic: string): Promise<SpecPage | null> {
  const r = await safe<SpecPage>(`SELECT * FROM spec_pages WHERE ${LIVE} AND make_slug=$1 AND model_slug=$2 AND topic=$3`, [make, model, topic]);
  return r[0] ?? null;
}

export type SpecLink = { make_slug: string; model_slug: string; topic: string; make_name: string; model_name: string; topic_label: string; title: string; updated: string };
export async function allSpecs(): Promise<SpecLink[]> {
  return safe<SpecLink>(`SELECT make_slug, model_slug, topic, make_name, model_name, topic_label, title, (page->>'reviewed') AS updated
    FROM spec_pages WHERE ${LIVE} ORDER BY make_name, model_name, topic_label`);
}
/** The same spec for other models (same make first), for cross-links between spec pages. */
export async function sameTopicElsewhere(s: { make_slug: string; model_slug: string; topic: string }, max = 10): Promise<SpecLink[]> {
  const all = (await allSpecs()).filter(x => x.topic === s.topic && !(x.make_slug === s.make_slug && x.model_slug === s.model_slug));
  return [...all.filter(x => x.make_slug === s.make_slug), ...all.filter(x => x.make_slug !== s.make_slug)].slice(0, max);
}
export async function specsForModel(make: string, model: string): Promise<SpecLink[]> {
  return (await allSpecs()).filter(s => s.make_slug === make && s.model_slug === model);
}

/** Published accessory guides of this model in the given categories (newest generation first), for the "parts that depend on this" block. */
export type SpecGuide = { path: string; title: string; vehicle: string; category_name: string };
export async function guidesForModel(make: string, model: string, categories: string[]): Promise<SpecGuide[]> {
  if (!categories.length) return [];
  return q<SpecGuide>(`
    SELECT '/vehicles/'||m.slug||'/'||v.model_slug||'/'||v.gen_slug||'/'||c.slug AS path, fp.title, c.name AS category_name,
           v.year_from||'–'||COALESCE(v.year_to, EXTRACT(YEAR FROM CURRENT_DATE)::int)::text||' '||m.name||' '||v.model_name AS vehicle
    FROM fitment_pages fp JOIN vehicles v ON v.id=fp.vehicle_id JOIN makes m ON m.id=v.make_id JOIN categories c ON c.id=fp.category_id
    WHERE fp.status='published' AND m.slug=$1 AND v.model_slug=$2 AND c.slug = ANY($3)
    ORDER BY array_position($3, c.slug), v.year_from DESC`, [make, model, categories]);
}
export async function hubsForModel(make: string, model: string): Promise<{ path: string; label: string }[]> {
  return q(`SELECT '/vehicles/'||m.slug||'/'||v.model_slug||'/'||v.gen_slug AS path,
      v.year_from||'–'||COALESCE(v.year_to, EXTRACT(YEAR FROM CURRENT_DATE)::int)::text||' '||m.name||' '||v.model_name AS label
    FROM vehicles v JOIN makes m ON m.id=v.make_id WHERE m.slug=$1 AND v.model_slug=$2 ORDER BY v.year_from DESC`, [make, model]);
}
