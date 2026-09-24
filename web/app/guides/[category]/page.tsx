import Link from "next/link";
import { notFound } from "next/navigation";
import type { Metadata } from "next";
import { getCategory, publishedGuides } from "@/lib/queries";

export const revalidate = 3600;
type P = { category: string };

export async function generateStaticParams() {
  const rows = await publishedGuides();
  return [...new Set(rows.map(r => r.category_slug))].map(category => ({ category }));
}

export async function generateMetadata({ params }: { params: Promise<P> }): Promise<Metadata> {
  const c = await getCategory((await params).category);
  if (!c) return {};
  return {
    title: `${c.name} by Vehicle — Fit-Checked Guides`,
    description: `${c.name} matched to your exact truck or SUV generation. Pick your vehicle to see what fits, with prices and fit notes.`,
    alternates: { canonical: `/guides/${c.slug}` },
  };
}

export default async function CategoryIndex({ params }: { params: Promise<P> }) {
  const { category } = await params;
  const [c, rows] = await Promise.all([getCategory(category), publishedGuides(category)]);
  if (!c || rows.length === 0) notFound();
  const byMake = new Map<string, typeof rows>();
  for (const r of rows) { if (!byMake.has(r.make_name)) byMake.set(r.make_name, []); byMake.get(r.make_name)!.push(r); }
  const jsonLd = { "@context": "https://schema.org", "@type": "CollectionPage", name: `${c.name} by vehicle`,
    hasPart: rows.map(r => ({ "@type": "Article", headline: r.title, url: r.path })) };
  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />
      <div className="crumbs"><Link href="/guides">Guides</Link> › {c.name}</div>
      <h1>{c.name} by vehicle</h1>
      <p className="muted">Pick your truck or SUV. Each guide lists only the {c.name.toLowerCase()} listed for that generation, with the fit gotchas for it.</p>
      {[...byMake].map(([make, list]) => (
        <section key={make} className="cat-group">
          <h2>{make}</h2>
          <ul className="cat-list">{list.map(r => <li key={r.path}><Link href={r.path}>{r.vehicle}</Link></li>)}</ul>
        </section>
      ))}
      <p style={{ marginTop: 32 }}><Link href="/guides">← All categories</Link></p>
    </>
  );
}
