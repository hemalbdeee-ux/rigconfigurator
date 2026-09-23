import { q } from "./db";

export type Vehicle = {
  id: number; make_slug: string; make_name: string; model_slug: string; model_name: string;
  gen_slug: string; gen_name: string; year_from: number; year_to: number | null; body_style: string;
  bed_lengths_in: number[]; roof_type: string | null; roof_load_lb: number | null; hitch_class: string | null;
  receiver_in: number | null; tow_rating_lb: number | null; tire_size: string | null; bolt_pattern: string | null;
  rows_seating: number; attrs: Record<string, any>; summary: string | null;
};

export type Category = { id: number; slug: string; name: string; fit_rule: string | null };

export type Fit = {
  id: number; product_id: number; asin: string; name: string; brand: string | null; image_url: string | null;
  price_cents: number | null; price_band: string | null; rating: number | null; reviews: number | null;
  weight_lb: number | null; attrs: Record<string, any>; pros: string[]; cons: string[];
  condition: Record<string, any>; note: string | null; source: string | null; confidence: number; rank: number;
  category_slug: string; category_name: string;
};

const VEHICLE_SELECT = `
  SELECT v.*, m.slug AS make_slug, m.name AS make_name
  FROM vehicles v JOIN makes m ON m.id = v.make_id`;

export const yearsLabel = (v: Vehicle) => `${v.year_from}–${v.year_to ?? "present"}`;
export const vehicleTitle = (v: Vehicle) => `${yearsLabel(v)} ${v.make_name} ${v.model_name}`;
export const vehiclePath = (v: Vehicle) => `/vehicles/${v.make_slug}/${v.model_slug}/${v.gen_slug}`;

export async function allVehicles(): Promise<Vehicle[]> {
  return q<Vehicle>(`${VEHICLE_SELECT} ORDER BY m.name, v.model_name, v.year_from DESC`);
}

export async function getVehicle(make: string, model: string, gen: string): Promise<Vehicle | null> {
  const rows = await q<Vehicle>(`${VEHICLE_SELECT} WHERE m.slug=$1 AND v.model_slug=$2 AND v.gen_slug=$3`, [make, model, gen]);
  return rows[0] ?? null;
}

export async function categoriesFor(bodyStyle: string): Promise<Category[]> {
  return q<Category>(`SELECT id, slug, name, fit_rule FROM categories WHERE $1 = ANY(body_styles) ORDER BY sort`, [bodyStyle]);
}

export async function getCategory(slug: string): Promise<Category | null> {
  const rows = await q<Category>(`SELECT id, slug, name, fit_rule FROM categories WHERE slug=$1`, [slug]);
  return rows[0] ?? null;
}

export async function fitsFor(vehicleId: number, categorySlug?: string): Promise<Fit[]> {
  return q<Fit>(
    `SELECT * FROM v_fitment WHERE vehicle_id=$1 ${categorySlug ? "AND category_slug=$2" : ""} ORDER BY rank, confidence DESC`,
    categorySlug ? [vehicleId, categorySlug] : [vehicleId]
  );
}

export async function getFitmentPage(vehicleId: number, categoryId: number) {
  const rows = await q(`SELECT * FROM fitment_pages WHERE vehicle_id=$1 AND category_id=$2`, [vehicleId, categoryId]);
  return rows[0] ?? null;
}

export async function allFitmentPaths() {
  return q<{ make_slug: string; model_slug: string; gen_slug: string; category_slug: string; updated_at: string }>(`
    SELECT m.slug AS make_slug, v.model_slug, v.gen_slug, c.slug AS category_slug, fp.updated_at
    FROM fitment_pages fp
    JOIN vehicles v ON v.id = fp.vehicle_id JOIN makes m ON m.id = v.make_id
    JOIN categories c ON c.id = fp.category_id
    WHERE fp.status = 'published'`);
}

export async function pagesFor(vehicleId: number) {
  return q<{ category_id: number; category_slug: string; title: string; verified_at: string | null; status: string }>(
    `SELECT fp.category_id, c.slug AS category_slug, fp.title, fp.verified_at, fp.status
     FROM fitment_pages fp JOIN categories c ON c.id = fp.category_id WHERE fp.vehicle_id = $1`, [vehicleId]);
}

export async function siblingsOf(v: Vehicle & { make_id?: number }): Promise<Vehicle[]> {
  return q<Vehicle>(
    `${VEHICLE_SELECT} WHERE v.id <> $1 AND (v.make_id = $2 OR v.body_style = $3)
     ORDER BY (v.make_id = $2) DESC, (v.model_slug = $4) DESC, v.year_from DESC LIMIT 6`,
    [v.id, v.make_id, v.body_style, v.model_slug]);
}
