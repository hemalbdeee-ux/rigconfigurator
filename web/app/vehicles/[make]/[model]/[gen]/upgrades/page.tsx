import Link from "next/link";
import { notFound } from "next/navigation";
import type { Metadata } from "next";
import { getVehicle, heroFor, vehiclePath, vehicleTitle, type Vehicle } from "@/lib/queries";
import { getUpgrades, vehicleGuideSummaries, explainersFor } from "@/lib/pillars";
import { SITE_URL } from "@/lib/db";
import { seoTitle, titleYears } from "@/lib/seo";
import { linkMap } from "@/lib/links";
import { Hero, ogImage } from "@/components/Hero";
import { Linker, Md } from "@/components/Md";
import { AuthorBox, Avoid, Byline, Faq, Method, T, Takeaways, Toc, Verdict } from "@/components/PillarParts";
import { getAuthor } from "@/lib/authors";

export const revalidate = 3600;
type P = { make: string; model: string; gen: string };

const model = (v: Vehicle) => /^\d+(\s|$)/.test(v.model_name) ? `${v.make_name} ${v.model_name}` : v.model_name;
const upgradesSeoTitle = (v: Vehicle) => seoTitle(
  `${titleYears(v)} ${v.make_name} ${v.model_name} Upgrades, Ranked`,
  `${titleYears(v)} ${model(v)} Upgrades, Ranked`,
  `${titleYears(v)} ${model(v)} Upgrades`,
);

async function load(p: P) {
  const v = await getVehicle(p.make, p.model, p.gen);
  if (!v) return null;
  const page = await getUpgrades(v.id);
  if (!page) return null;
  const [guides, hero, learn, links] = await Promise.all([vehicleGuideSummaries(v.id), heroFor(v.id), explainersFor(page.category_slugs), linkMap(v, "__upgrades__")]);
  return { v, page, guides, hero, learn, links };
}

export async function generateMetadata({ params }: { params: Promise<P> }): Promise<Metadata> {
  const d = await load(await params);
  if (!d) return {};
  const path = `${vehiclePath(d.v)}/upgrades`;
  return {
    title: upgradesSeoTitle(d.v),
    description: d.page.meta_desc ?? undefined,
    alternates: { canonical: path },
    openGraph: { title: d.page.title, description: d.page.meta_desc ?? undefined, url: path, type: "article", images: ogImage(d.hero) },
    twitter: { card: "summary_large_image", title: d.page.title },
  };
}

export default async function UpgradesPage({ params }: { params: Promise<P> }) {
  const d = await load(await params);
  if (!d) notFound();
  const { v, page, guides, hero, learn, links } = d;
  const a = page.article;
  const L = new Linker(links);
  const hub = vehiclePath(v);
  const path = `${hub}/upgrades`;
  const byCat = new Map(guides.map(g => [g.category_slug, g]));
  const items = a.priority.filter(p => byCat.has(p.category));

  const toc: [string, string][] = [
    ["priority", "Upgrade priority"],
    ...(a.tier_table ? [["budget", "Cost by tier"] as [string, string]] : []),
    ...(a.sections ?? []).map((s, i) => [`s${i}`, s.h] as [string, string]),
    ...(a.avoid?.length ? [["avoid", "What to avoid"] as [string, string]] : []),
    ["faq", "FAQ"], ["verdict", "Bottom line"],
  ];

  const jsonLd = {
    "@context": "https://schema.org",
    "@graph": [
      { "@type": "BreadcrumbList", itemListElement: [
        { "@type": "ListItem", position: 1, name: "Vehicles", item: `${SITE_URL}/vehicles` },
        { "@type": "ListItem", position: 2, name: vehicleTitle(v), item: `${SITE_URL}${hub}` },
        { "@type": "ListItem", position: 3, name: "Upgrades", item: `${SITE_URL}${path}` }] },
      { "@type": "Article", headline: page.title.length <= 110 ? page.title : upgradesSeoTitle(v).absolute, description: page.meta_desc,
        mainEntityOfPage: `${SITE_URL}${path}`, datePublished: page.published_at, dateModified: a.reviewed ?? page.published_at,
        author: { "@type": "Person", name: getAuthor(a.author).name, url: `${SITE_URL}/about` },
        publisher: { "@type": "Organization", name: "Rig Configurator", url: SITE_URL },
        ...(hero ? { image: `${SITE_URL}/img/${hero.file}` } : {}) },
      { "@type": "ItemList", name: `${vehicleTitle(v)} upgrades by priority`, numberOfItems: items.length,
        itemListElement: items.map((it, i) => ({ "@type": "ListItem", position: i + 1, name: it.h, url: `${SITE_URL}${hub}/${it.category}` })) },
      ...(page.faq.length ? [{ "@type": "FAQPage", mainEntity: page.faq.map(x => ({ "@type": "Question", name: x.q, acceptedAnswer: { "@type": "Answer", text: x.a } })) }] : []),
    ],
  };

  return (
    <article className="art">
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />
      <div className="crumbs"><Link href="/vehicles">Vehicles</Link> › <Link href={hub}>{vehicleTitle(v)}</Link> › Upgrades</div>
      <h1>{page.title}</h1>
      <p className="dek">{a.dek}</p>
      <Hero h={hero} alt={`${vehicleTitle(v)} upgrades`} priority />
      <Byline author={a.author} reviewed={a.reviewed} />
      <div className="disclose">We earn a commission from qualifying Amazon purchases, at no extra cost to you. <Link href="/disclosure">How we make money</Link>.</div>

      <Takeaways items={a.takeaways} linker={L} />
      <Toc items={toc} />

      <section id="priority">
        <h2>{model(v)} upgrades in priority order</h2>
        <p className="muted" style={{ fontSize: 14 }}>Each step links to a full fit-checked guide for the {vehicleTitle(v)}.</p>
        {items.map((it, i) => {
          const g = byCat.get(it.category)!;
          return (
            <div key={it.category} className="card upg">
              <div className="upg-head"><span className="mini-rank">{i + 1}</span><h3 style={{ margin: 0 }}>{it.h.replace(/^\d+[.)]\s*/, "")}</h3></div>
              <Md s={it.why} linker={L} />
              {it.skip_if && <p className="muted" style={{ fontSize: 14 }}><strong>Skip it if:</strong> {it.skip_if}</p>}
              {g.top_name && <p style={{ fontSize: 14 }}><strong>Our {g.top_role?.toLowerCase() ?? "top pick"}:</strong> {g.top_name.split(",")[0]}{g.top_price ? ` (${g.top_price})` : ""}</p>}
              <Link className="btn" href={`${hub}/${it.category}`}>Compare all {g.picks} {g.category_name.toLowerCase()} picks →</Link>
            </div>
          );
        })}
      </section>

      {a.tier_table && (<section id="budget"><h2>What a {model(v)} build costs, by tier</h2><T t={a.tier_table} linker={L} /></section>)}

      {(a.sections ?? []).map((s, i) => (
        <section key={s.h} id={`s${i}`}><h2>{s.h}</h2><Md s={s.body} linker={L} />{s.table && <T t={s.table} />}</section>
      ))}

      <Avoid items={a.avoid} linker={L} />

      {learn.length > 0 && (<section className="next-step"><div className="lbl">Learn before you buy</div>
        <ul style={{ margin: "6px 0 0" }}>{learn.map(x => <li key={x.path}><Link href={x.path}>{x.title}</Link></li>)}</ul></section>)}

      <Faq faq={page.faq} linker={L} />
      <Verdict v={a.verdict} linker={L} />

      <section className="cta-box">
        <strong>Everything that fits your {model(v)}</strong>
        <p className="muted">Fit facts plus every guide for the {vehicleTitle(v)}.</p>
        <Link className="btn" href={hub}>Open the {model(v)} fit hub →</Link>
      </section>

      <Method method={a.method} sources={a.sources} />
      <AuthorBox author={a.author} />
    </article>
  );
}
