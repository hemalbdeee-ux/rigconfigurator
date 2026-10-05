import { q } from "./db";
import type { Fit, Hero, Vehicle } from "./queries";

// Data for the home page. Everything here is read live (the page is force-dynamic), so counts, prices and
// review dates are never stale.

export type SiteStats = { vehicles: number; guides: number; products: number; makes: number };

export async function siteStats(): Promise<SiteStats> {
  const r = await q<SiteStats>(`
    SELECT (SELECT count(*)::int FROM vehicles) AS vehicles,
           (SELECT count(*)::int FROM fitment_pages WHERE status='published') AS guides,
           (SELECT count(DISTINCT product_id)::int FROM fitments) AS products,
           (SELECT count(*)::int FROM makes) AS makes`);
  return r[0];
}

// The vehicles featured on the home page, in order. Big-parc trucks and SUVs first; the rest live on /vehicles.
export const FEATURED: [string, string, string][] = [
  ["ford", "f-150", "2021-present"], ["chevrolet", "silverado-1500", "2019-present"], ["ram", "1500", "2019-present"],
  ["toyota", "tacoma", "2024-present"], ["jeep", "wrangler", "2018-present"], ["toyota", "4runner", "2025-present"],
  ["toyota", "rav4", "2019-present"], ["tesla", "model-y", "2020-present"],
];

export type FeaturedVehicle = Vehicle & { guides: number; hero: Hero | null };

export async function featuredVehicles(): Promise<FeaturedVehicle[]> {
  const rows = await q<Vehicle & { guides: number; hero_file: string | null; hero_w: number | null; hero_h: number | null }>(`
    SELECT v.*, m.slug AS make_slug, m.name AS make_name,
           (SELECT count(*)::int FROM fitment_pages fp WHERE fp.vehicle_id=v.id AND fp.status='published') AS guides,
           vi.file AS hero_file, vi.width AS hero_w, vi.height AS hero_h
    FROM vehicles v JOIN makes m ON m.id=v.make_id
    LEFT JOIN vehicle_images vi ON vi.vehicle_id=v.id AND vi.status='approved'`);
  const byKey = new Map(rows.map(r => [`${r.make_slug}/${r.model_slug}/${r.gen_slug}`, r]));
  const out: FeaturedVehicle[] = [];
  for (const [mk, md, gen] of FEATURED) {
    const r = byKey.get(`${mk}/${md}/${gen}`);
    if (!r || r.guides === 0) continue;
    const { hero_file, hero_w, hero_h, ...v } = r;
    out.push({ ...v, hero: hero_file ? { file: hero_file, width: hero_w ?? 1600, height: hero_h ?? 900, title: "", author: "", license: "", license_url: null, source_url: "" } : null });
  }
  return out;
}

// Rank-1 product of a hand-picked set of high-traffic guides: the fastest honest path from the home page to Amazon.
const TOP_PICK_PAGES: [string, string, string, string][] = [
  ["ford", "f-150", "2021-present", "tonneau-covers"], ["toyota", "tacoma", "2024-present", "bed-racks"],
  ["jeep", "wrangler", "2018-present", "floor-mats"], ["chevrolet", "silverado-1500", "2019-present", "running-boards"],
  ["toyota", "rav4", "2019-present", "roof-racks"], ["ram", "1500", "2019-present", "tonneau-covers"],
  ["toyota", "4runner", "2025-present", "led-light-bars"], ["subaru", "outback", "2020-present", "cargo-boxes"],
];

export type TopPick = Fit & { vehicle: string; page: string; role: string | null };

export async function topPicks(limit = 6): Promise<TopPick[]> {
  const rows = await q<TopPick>(`
    SELECT f.*, v.year_from||'–'||COALESCE(v.year_to, EXTRACT(YEAR FROM CURRENT_DATE)::int)::text||' '||m.name||' '||v.model_name AS vehicle,
           '/vehicles/'||m.slug||'/'||v.model_slug||'/'||v.gen_slug||'/'||f.category_slug AS page,
           fp.article->'top_picks'->0->>'role' AS role
    FROM v_fitment f JOIN vehicles v ON v.id=f.vehicle_id JOIN makes m ON m.id=v.make_id
    JOIN fitment_pages fp ON fp.vehicle_id=v.id AND fp.category_id=(SELECT id FROM categories WHERE slug=f.category_slug)
    WHERE fp.status='published' AND f.rank=1
      AND (m.slug, v.model_slug, v.gen_slug, f.category_slug) IN (${TOP_PICK_PAGES.map((_, i) => `($${i * 4 + 1},$${i * 4 + 2},$${i * 4 + 3},$${i * 4 + 4})`).join(",")})`,
    TOP_PICK_PAGES.flat());
  const order = new Map(TOP_PICK_PAGES.map((p, i) => [p.join("/"), i]));
  rows.sort((a, b) => (order.get(a.page.replace("/vehicles/", "")) ?? 99) - (order.get(b.page.replace("/vehicles/", "")) ?? 99));
  return rows.slice(0, limit);
}

export type RecentGuide = { path: string; title: string; vehicle: string; category: string; reviewed: string | null };

export async function recentGuides(limit = 6): Promise<RecentGuide[]> {
  return q<RecentGuide>(`
    SELECT '/vehicles/'||m.slug||'/'||v.model_slug||'/'||v.gen_slug||'/'||c.slug AS path, fp.title, c.name AS category,
           v.year_from||'–'||COALESCE(v.year_to, EXTRACT(YEAR FROM CURRENT_DATE)::int)::text||' '||m.name||' '||v.model_name AS vehicle,
           (fp.article->>'reviewed') AS reviewed
    FROM fitment_pages fp JOIN vehicles v ON v.id=fp.vehicle_id JOIN makes m ON m.id=v.make_id JOIN categories c ON c.id=fp.category_id
    WHERE fp.status='published' AND fp.article IS NOT NULL
    ORDER BY (fp.article->>'reviewed') DESC NULLS LAST, fp.published_at DESC NULLS LAST, fp.id DESC
    LIMIT $1`, [limit]);
}

export type CategoryCount = { slug: string; name: string; guides: number };

export async function categoryCounts(): Promise<CategoryCount[]> {
  return q<CategoryCount>(`
    SELECT c.slug, c.name, count(fp.id)::int AS guides
    FROM categories c JOIN fitment_pages fp ON fp.category_id=c.id AND fp.status='published'
    GROUP BY c.id ORDER BY c.sort`);
}
