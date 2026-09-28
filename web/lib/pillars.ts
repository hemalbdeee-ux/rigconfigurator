import { q } from "./db";
import type { Vehicle } from "./queries";

export type Table = { caption?: string; head: string[]; rows: string[][] };
export type Section = { h: string; body: string; table?: Table };

export type UpgradesArticle = {
  dek: string; author?: string; reviewed?: string; method?: string; takeaways: string[];
  /** Ranked upgrade list; each item points at one of the vehicle's category guides. */
  priority: { category: string; h: string; why: string; skip_if?: string }[];
  tier_table?: Table;
  sections?: Section[];
  avoid?: { h: string; body: string }[];
  verdict: { thesis: string; body: string };
  sources?: [string, string][];
};

export type ExplainerArticle = {
  dek: string; author?: string; reviewed?: string; method?: string; takeaways: string[];
  compare_table?: Table;
  sections: Section[];
  decision?: { if: string; then: string }[];
  avoid?: { h: string; body: string }[];
  verdict: { thesis: string; body: string };
  sources?: [string, string][];
};

export type PillarRow<A> = {
  id: number; kind: "upgrades" | "explainer"; slug: string; vehicle_id: number | null; category_slugs: string[];
  title: string; meta_desc: string | null; faq: { q: string; a: string }[]; article: A;
  published_at: string; updated_at: string;
};

export async function getUpgrades(vehicleId: number) {
  const rows = await q<PillarRow<UpgradesArticle>>(
    `SELECT * FROM pillar_pages WHERE kind='upgrades' AND status='published' AND vehicle_id=$1`, [vehicleId]);
  return rows[0] ?? null;
}

export async function getExplainer(slug: string) {
  const rows = await q<PillarRow<ExplainerArticle>>(
    `SELECT * FROM pillar_pages WHERE kind='explainer' AND status='published' AND slug=$1`, [slug]);
  return rows[0] ?? null;
}

export type PillarLink = { kind: "upgrades" | "explainer"; slug: string; title: string; path: string; category_slugs: string[]; dek: string | null; updated: string };

/** All published pillar pages with their URL path. */
export async function allPillars(): Promise<PillarLink[]> {
  return q<PillarLink>(`
    SELECT p.kind, p.slug, p.title, p.category_slugs, p.article->>'dek' AS dek,
           COALESCE((p.article->>'reviewed')::date, p.published_at)::text AS updated,
           CASE WHEN p.kind='upgrades' THEN '/vehicles/'||p.slug||'/upgrades' ELSE '/learn/'||p.slug END AS path
    FROM pillar_pages p WHERE p.status='published' ORDER BY p.kind, p.title`);
}

/** Explainers that cover any of these categories (for "Learn first" boxes on guides). */
export async function explainersFor(categorySlugs: string[]): Promise<PillarLink[]> {
  return (await allPillars()).filter(p => p.kind === "explainer" && p.category_slugs.some(c => categorySlugs.includes(c)));
}

/** Path of the vehicle's upgrades page, if one is published. */
export async function upgradesPathFor(v: Vehicle): Promise<string | null> {
  const rows = await q<{ id: number }>(`SELECT id FROM pillar_pages WHERE kind='upgrades' AND status='published' AND vehicle_id=$1`, [v.id]);
  return rows.length ? `/vehicles/${v.make_slug}/${v.model_slug}/${v.gen_slug}/upgrades` : null;
}

/** For an upgrades page: each published category guide of the vehicle with its #1 pick (name, price, role). */
export type GuideSummary = { category_slug: string; category_name: string; title: string; top_role: string | null; top_name: string | null; top_price: string | null; top_asin: string | null; picks: number };
export async function vehicleGuideSummaries(vehicleId: number): Promise<GuideSummary[]> {
  return q<GuideSummary>(`
    SELECT c.slug AS category_slug, c.name AS category_name, fp.title,
           fp.article->'top_picks'->0->>'role' AS top_role,
           fp.article->'top_picks'->0->>'asin' AS top_asin,
           (SELECT p.name FROM products p WHERE p.asin = fp.article->'top_picks'->0->>'asin' LIMIT 1) AS top_name,
           (SELECT x->>'price' FROM jsonb_array_elements(fp.article->'picks') x WHERE x->>'asin' = fp.article->'top_picks'->0->>'asin' LIMIT 1) AS top_price,
           jsonb_array_length(COALESCE(fp.article->'picks','[]'::jsonb)) AS picks
    FROM fitment_pages fp JOIN categories c ON c.id = fp.category_id
    WHERE fp.vehicle_id = $1 AND fp.status = 'published' AND fp.article IS NOT NULL
    ORDER BY c.sort`, [vehicleId]);
}
