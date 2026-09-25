import Link from "next/link";
import { notFound } from "next/navigation";
import type { Metadata } from "next";
import { categorySeoTitle } from "@/lib/seo";
import { SITE_URL } from "@/lib/db";
import { GUIDE_COPY } from "@/lib/guideCopy";
import { staticOg } from "@/components/Hero";
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
  const title = categorySeoTitle(c);
  const description = GUIDE_COPY[c.slug]?.blurb
    ? `${c.name} by vehicle generation. ${GUIDE_COPY[c.slug].blurb}`
    : `${c.name} matched to your exact truck or SUV generation, with prices and fit notes.`;
  return {
    title, description,
    alternates: { canonical: `/guides/${c.slug}` },
    openGraph: { title: title.absolute, description, url: `/guides/${c.slug}`, type: "website", images: staticOg(`guide-${c.slug}`, `${c.name} by vehicle`) },
  };
}

export default async function CategoryIndex({ params }: { params: Promise<P> }) {
  const { category } = await params;
  const [c, rows] = await Promise.all([getCategory(category), publishedGuides(category)]);
  if (!c || rows.length === 0) notFound();
  const copy = GUIDE_COPY[c.slug];
  const byMake = new Map<string, typeof rows>();
  for (const r of rows) { if (!byMake.has(r.make_name)) byMake.set(r.make_name, []); byMake.get(r.make_name)!.push(r); }
  const url = `${SITE_URL}/guides/${c.slug}`;
  const jsonLd = {
    "@context": "https://schema.org",
    "@graph": [
      { "@type": "CollectionPage", "@id": url, url, name: `${c.name} by vehicle`, description: copy?.intro,
        isPartOf: { "@id": `${SITE_URL}/#website` },
        mainEntity: { "@type": "ItemList", numberOfItems: rows.length,
          itemListElement: rows.map((r, i) => ({ "@type": "ListItem", position: i + 1, url: `${SITE_URL}${r.path}`, name: r.title })) } },
      { "@type": "BreadcrumbList", itemListElement: [
        { "@type": "ListItem", position: 1, name: "Guides", item: `${SITE_URL}/guides` },
        { "@type": "ListItem", position: 2, name: c.name, item: url }] },
      ...(copy ? [{ "@type": "FAQPage", mainEntity: copy.faq.map(([q, a]) => ({ "@type": "Question", name: q, acceptedAnswer: { "@type": "Answer", text: a } })) }] : []),
    ],
  };
  return (
    <article className="art">
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />
      <div className="crumbs"><Link href="/guides">Guides</Link> › {c.name}</div>
      <h1>{c.name} by vehicle</h1>
      <p className="dek">{copy?.intro ?? `Pick your truck or SUV. Each guide lists only the ${c.name.toLowerCase()} listed for that generation, with the fit gotchas for it.`}</p>

      <nav className="toc-box"><strong>{rows.length} {rows.length === 1 ? "guide" : "guides"}, one per vehicle generation</strong>
        <ul className="cat-list">{[...byMake].map(([make, list]) => list.map(r => <li key={r.path}><Link href={r.path}>{r.vehicle}</Link></li>))}</ul>
      </nav>

      {copy && (<section>
        <h2>What decides whether {c.name.toLowerCase()} fit</h2>
        {copy.fit.map(([h, b]) => <div key={h}><h3>{h}</h3><p>{b}</p></div>)}
      </section>)}

      <section>
        <h2>Guides by make</h2>
        {[...byMake].map(([make, list]) => (
          <div key={make} className="cat-group">
            <h3>{make}</h3>
            <div className="grid">{list.map(r => (
              <Link key={r.path} href={r.path} className="card">
                <div className="muted" style={{ fontSize: 12 }}>{r.vehicle}</div>
                <h3 style={{ marginTop: 4 }}>{r.title}</h3>
                {r.meta_desc && <div className="muted" style={{ fontSize: 14 }}>{r.meta_desc}</div>}
              </Link>))}
            </div>
          </div>
        ))}
      </section>

      {copy && (<section>
        <h2>Common mistakes</h2>
        <div className="box warnbox">{copy.mistakes.map(([h, b]) => <p key={h}><strong>{h}.</strong> {b}</p>)}</div>
      </section>)}

      {copy && (<section id="faq">
        <h2>Frequently asked questions</h2>
        {copy.faq.map(([q, a]) => <details key={q} className="faq"><summary>{q}</summary><p>{a}</p></details>)}
      </section>)}

      <p className="muted" style={{ fontSize: 14 }}>Fit is checked against manufacturer fit guides and retailer listings for each generation. Always confirm on the listing for your exact trim. <Link href="/about">How we check fitment</Link>.</p>
      <p style={{ marginTop: 24 }}><Link href="/guides">← All categories</Link></p>
    </article>
  );
}
