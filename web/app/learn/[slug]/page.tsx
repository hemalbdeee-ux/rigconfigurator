import Link from "next/link";
import { notFound } from "next/navigation";
import type { Metadata } from "next";
import { getExplainer } from "@/lib/pillars";
import { publishedGuides } from "@/lib/queries";
import { SITE_URL } from "@/lib/db";
import { seoTitle } from "@/lib/seo";
import { CATEGORY_PHRASES } from "@/lib/links";
import { staticOg } from "@/components/Hero";
import { Linker, Md } from "@/components/Md";
import { AuthorBox, Avoid, Byline, Faq, Method, T, Takeaways, Toc, Verdict } from "@/components/PillarParts";
import { getAuthor } from "@/lib/authors";

export const revalidate = 3600;
type P = { slug: string };

export async function generateMetadata({ params }: { params: Promise<P> }): Promise<Metadata> {
  const page = await getExplainer((await params).slug);
  if (!page) return {};
  const path = `/learn/${page.slug}`;
  const cat = page.category_slugs[0];
  return {
    title: seoTitle(page.title.split(":")[0], page.title.split(":")[0].slice(0, 58)),
    description: page.meta_desc ?? undefined,
    alternates: { canonical: path },
    openGraph: { title: page.title, description: page.meta_desc ?? undefined, url: path, type: "article",
      images: cat ? staticOg(`guide-${cat}`, page.title) : undefined },
    twitter: { card: "summary_large_image", title: page.title },
  };
}

export default async function Explainer({ params }: { params: Promise<P> }) {
  const page = await getExplainer((await params).slug);
  if (!page) notFound();
  const a = page.article;
  const path = `/learn/${page.slug}`;
  const guides = (await Promise.all(page.category_slugs.map(c => publishedGuides(c)))).flat();

  // Link the first mention of each covered category to its /guides index.
  const map: Record<string, string> = {};
  for (const c of page.category_slugs) for (const p of CATEGORY_PHRASES[c] ?? []) map[p] = `/guides/${c}`;
  const L = new Linker(map, 4);

  const toc: [string, string][] = [
    ...(a.compare_table ? [["compare", "Side-by-side"] as [string, string]] : []),
    ...a.sections.map((s, i) => [`s${i}`, s.h] as [string, string]),
    ...(a.decision?.length ? [["decide", "Which one to buy"] as [string, string]] : []),
    ...(guides.length ? [["by-vehicle", "Guides by vehicle"] as [string, string]] : []),
    ...(a.avoid?.length ? [["avoid", "What to avoid"] as [string, string]] : []),
    ["faq", "FAQ"], ["verdict", "Bottom line"],
  ];

  const jsonLd = {
    "@context": "https://schema.org",
    "@graph": [
      { "@type": "BreadcrumbList", itemListElement: [
        { "@type": "ListItem", position: 1, name: "Learn", item: `${SITE_URL}/learn` },
        { "@type": "ListItem", position: 2, name: page.title, item: `${SITE_URL}${path}` }] },
      { "@type": "Article", headline: page.title.length <= 110 ? page.title : page.title.split(":")[0], description: page.meta_desc,
        mainEntityOfPage: `${SITE_URL}${path}`, datePublished: page.published_at, dateModified: a.reviewed ?? page.published_at,
        author: { "@type": "Person", name: getAuthor(a.author).name, url: `${SITE_URL}/about` },
        publisher: { "@type": "Organization", name: "Rig Configurator", url: SITE_URL } },
      ...(page.faq.length ? [{ "@type": "FAQPage", mainEntity: page.faq.map(x => ({ "@type": "Question", name: x.q, acceptedAnswer: { "@type": "Answer", text: x.a } })) }] : []),
    ],
  };

  return (
    <article className="art">
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />
      <div className="crumbs"><Link href="/learn">Learn</Link> › {page.title.split(":")[0]}</div>
      <h1>{page.title}</h1>
      <p className="dek">{a.dek}</p>
      <Byline author={a.author} reviewed={a.reviewed} />

      <Takeaways items={a.takeaways} linker={L} />
      <Toc items={toc} />

      {a.compare_table && (<section id="compare"><h2>Side-by-side</h2><T t={a.compare_table} /></section>)}

      {a.sections.map((s, i) => (
        <section key={s.h} id={`s${i}`}><h2>{s.h}</h2><Md s={s.body} linker={L} />{s.table && <T t={s.table} />}</section>
      ))}

      {a.decision?.length ? (<section id="decide"><h2>Which one to buy</h2>
        <div className="box">{a.decision.map(x => <p key={x.if}><strong>If {x.if}:</strong> {x.then}</p>)}</div></section>) : null}

      {guides.length > 0 && (<section id="by-vehicle"><h2>Find the right one for your vehicle</h2>
        <p className="muted" style={{ fontSize: 14 }}>Each guide lists only the parts sold for that generation, with its fit gotchas.</p>
        <ul className="cat-list">{guides.map(g => <li key={g.path}><Link href={g.path}>{g.vehicle} {g.category_name.toLowerCase()}</Link></li>)}</ul>
        <p style={{ fontSize: 14 }}>{page.category_slugs.map(c => <Link key={c} href={`/guides/${c}`} style={{ marginRight: 12 }}>All {c.replace(/-/g, " ")} guides →</Link>)}</p>
      </section>)}

      <Avoid items={a.avoid} />
      <Faq faq={page.faq} />
      <Verdict v={a.verdict} />
      <Method method={a.method} sources={a.sources} />
      <AuthorBox author={a.author} />
    </article>
  );
}
