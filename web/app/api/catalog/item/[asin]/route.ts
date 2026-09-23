import { NextResponse } from "next/server";
import { q } from "@/lib/db";

// Public read endpoint (allowed in robots.txt for AI crawlers, like rifleconfigurator's /api/catalog/item/)
export async function GET(_: Request, { params }: { params: Promise<{ asin: string }> }) {
  const { asin } = await params;
  const rows = await q(`
    SELECT p.asin, p.name, p.brand, p.price_band, p.rating, p.attrs, c.name AS category,
      COALESCE(json_agg(json_build_object('vehicle', m.name || ' ' || v.model_name || ' ' || v.gen_slug,
        'condition', f.condition, 'note', f.note, 'confidence', f.confidence)) FILTER (WHERE f.id IS NOT NULL), '[]') AS fits
    FROM products p JOIN categories c ON c.id=p.category_id
    LEFT JOIN fitments f ON f.product_id=p.id LEFT JOIN vehicles v ON v.id=f.vehicle_id LEFT JOIN makes m ON m.id=v.make_id
    WHERE p.asin=$1 AND p.active GROUP BY p.id, c.name`, [asin]);
  if (!rows[0]) return NextResponse.json({ error: "not found" }, { status: 404 });
  return NextResponse.json(rows[0], { headers: { "Cache-Control": "public, max-age=3600" } });
}
