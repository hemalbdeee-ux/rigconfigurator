import Link from "next/link";
import type { Metadata } from "next";
import { publishedGuides } from "@/lib/queries";
import { GUIDE_COPY } from "@/lib/guideCopy";
import { SITE_URL } from "@/lib/db";
import { staticOg } from "@/components/Hero";

// Rendered per request: a build-time copy (no DB during `docker build`) showed "0 guides across 0 categories".
export const dynamic = "force-dynamic";
export const metadata: Metadata = {
  title: "Truck & SUV Accessory Guides by Category",
  description: "Every fit-checked buying guide on Rig Configurator, grouped by accessory: tonneau covers, roof racks, hitches, floor liners, running boards and more.",
  alternates: { canonical: "/guides" },
  openGraph: { title: "Truck & SUV Accessory Guides by Category | Rig Configurator", url: "/guides", type: "website", images: staticOg("guides", "Accessory guides by category") },
};

export default async function Guides() {
  const rows = await publishedGuides();
  const cats = new Map<string, { name: string; rows: typeof rows }>();
  for (const r of rows) { if (!cats.has(r.category_slug)) cats.set(r.category_slug, { name: r.category_name, rows: [] }); cats.get(r.category_slug)!.rows.push(r); }
  const vehicles = new Set(rows.map(r => r.vehicle)).size;
  const jsonLd = { "@context": "https://schema.org", "@type": "CollectionPage", url: `${SITE_URL}/guides`, name: "Accessory guides by category",
    hasPart: [...cats].map(([slug, c]) => ({ "@type": "CollectionPage", name: `${c.name} by vehicle`, url: `${SITE_URL}/guides/${slug}` })) };
  return (
    <article className="art">
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />
      <h1>Accessory guides by category</h1>
      <p className="dek">{rows.length} fit-checked buying guides across {cats.size} categories and {vehicles} vehicle generations. Each guide is written for one generation, so it only lists parts sold for that truck or SUV, and it notes the trims, beds, roofs or seat layouts that change the part number.</p>
      <p>Start with the category, then pick your vehicle. If you don&apos;t know your generation, the <Link href="/vehicles">vehicle list</Link> shows the years each one covers.</p>

      {[...cats].map(([slug, c]) => (
        <section key={slug} className="cat-group">
          <h2><Link href={`/guides/${slug}`}>{c.name}</Link></h2>
          {GUIDE_COPY[slug] && <p className="muted">{GUIDE_COPY[slug].blurb}</p>}
          <ul className="cat-list">{c.rows.map(r => <li key={r.path}><Link href={r.path}>{r.vehicle}</Link></li>)}</ul>
          <p style={{ fontSize: 14 }}><Link href={`/guides/${slug}`}>What decides fit, common mistakes and all {c.rows.length} {c.name.toLowerCase()} {c.rows.length === 1 ? "guide" : "guides"} →</Link></p>
        </section>
      ))}

      <h2>How the guides are made</h2>
      <p>Each product is linked to a vehicle generation using the maker&apos;s fit guide and part-number listing, checked against the retailer listing. Where a listing is unclear, the guide says to confirm fit rather than guess. Picks are based on fitment, published specs and owner reports, and each guide lists its sources. Read more on the <Link href="/about">about page</Link> and in our <Link href="/disclosure">affiliate disclosure</Link>.</p>
    </article>
  );
}
