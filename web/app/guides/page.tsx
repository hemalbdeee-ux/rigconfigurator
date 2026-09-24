import Link from "next/link";
import type { Metadata } from "next";
import { publishedGuides } from "@/lib/queries";

export const revalidate = 3600;
export const metadata: Metadata = {
  title: "Truck & SUV Accessory Guides by Category",
  description: "Every fit-checked buying guide on Rig Configurator, grouped by accessory: tonneau covers, roof racks, hitches, floor liners, running boards and more.",
  alternates: { canonical: "/guides" },
};

export default async function Guides() {
  const rows = await publishedGuides();
  const cats = new Map<string, { name: string; rows: typeof rows }>();
  for (const r of rows) { if (!cats.has(r.category_slug)) cats.set(r.category_slug, { name: r.category_name, rows: [] }); cats.get(r.category_slug)!.rows.push(r); }
  return (
    <>
      <h1>Accessory guides by category</h1>
      <p className="muted">{rows.length} fit-checked guides across {cats.size} categories. Each one is written for a single vehicle generation.</p>
      <div className="grid" style={{ marginTop: 16 }}>
        {[...cats].map(([slug, c]) => (
          <Link key={slug} href={`/guides/${slug}`} className="card"><h3>{c.name}</h3><div className="muted">{c.rows.length} vehicle guides →</div></Link>
        ))}
      </div>
    </>
  );
}
