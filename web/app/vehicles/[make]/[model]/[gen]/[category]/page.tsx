import Link from "next/link";
import { notFound } from "next/navigation";
import type { Metadata } from "next";
import { allFitmentPaths, fitsFor, getCategory, getFitmentPage, getVehicle, heroFor, relatedGuides, vehiclePath, vehicleTitle } from "@/lib/queries";
import { linkMap } from "@/lib/links";
import { ogImage } from "@/components/Hero";
import { ArticleView, type Article } from "@/components/ArticleView";
import { getAuthor } from "@/lib/authors";
import { ProductCard } from "@/components/ProductCard";
import { SITE_URL, money } from "@/lib/db";
import { articleSeoTitle } from "@/lib/seo";

export const revalidate = 3600;
type P = { make: string; model: string; gen: string; category: string };

export async function generateStaticParams() {
  const rows = await allFitmentPaths();
  return rows.map(r => ({ make: r.make_slug, model: r.model_slug, gen: r.gen_slug, category: r.category_slug }));
}

async function load(p: P) {
  const v = await getVehicle(p.make, p.model, p.gen);
  const c = await getCategory(p.category);
  if (!v || !c) return null;
  const [fits, page, related, hero, links] = await Promise.all([fitsFor(v.id, c.slug), getFitmentPage(v.id, c.id), relatedGuides(v.id, c.id), heroFor(v.id), linkMap(v, c.slug)]);
  return { v, c, fits, page, related, hero, links };
}

export async function generateMetadata({ params }: { params: Promise<P> }): Promise<Metadata> {
  const d = await load(await params);
  if (!d) return {};
  const title = d.page?.title ?? `Best ${d.c.name} for ${vehicleTitle(d.v)}`;
  const path = `${vehiclePath(d.v)}/${d.c.slug}`;
  return {
    title: articleSeoTitle(d.v, d.c),   // ≤ 60 chars for the SERP; the full headline stays as the H1

    description: d.page?.meta_desc ?? `${d.c.name} verified to fit the ${vehicleTitle(d.v)}, with prices and fit notes.`,
    alternates: { canonical: path },
    robots: d.page?.status === "published" ? undefined : { index: false },
    openGraph: { title, description: d.page?.meta_desc ?? undefined, url: path, siteName: "Rig Configurator", type: "article", images: ogImage(d.hero) },
    twitter: { card: "summary_large_image", title },
  };
}

// minimal markdown: paragraphs + "- " bullets + **bold**
function md(s?: string | null) {
  if (!s) return null;
  const html = s.split(/\n{2,}|\n(?=- )/).map(block => {
    const b = block.trim().replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");
    return b.startsWith("- ") ? `<ul>${b.split(/\n- |^- /).filter(Boolean).map(i => `<li>${i}</li>`).join("")}</ul>` : `<p>${b}</p>`;
  }).join("");
  return <div dangerouslySetInnerHTML={{ __html: html }} />;
}

export default async function FitmentPage({ params }: { params: Promise<P> }) {
  const p = await params;
  const d = await load(p);
  if (!d) notFound();
  const { v, c, fits, page, related, hero, links } = d;
  const article: Article | null = page?.article ?? null;
  const path = `${vehiclePath(v)}/${c.slug}`;
  const title = page?.title ?? `Best ${c.name} for ${vehicleTitle(v)}`;
  const faq: { q: string; a: string }[] = page?.faq ?? [];

  const jsonLd = {
    "@context": "https://schema.org",
    "@graph": [
      { "@type": "BreadcrumbList", itemListElement: [
        { "@type": "ListItem", position: 1, name: "Vehicles", item: `${SITE_URL}/vehicles` },
        { "@type": "ListItem", position: 2, name: vehicleTitle(v), item: `${SITE_URL}${vehiclePath(v)}` },
        { "@type": "ListItem", position: 3, name: c.name, item: `${SITE_URL}${path}` }] },
      // Names only: ListItem.url must point at pages on this site, never at Amazon.
      { "@type": "ItemList", name: title, numberOfItems: fits.length, itemListElement: fits.map((f, i) => ({
        "@type": "ListItem", position: i + 1, name: f.name })) },
      ...(article ? [{ "@type": "Article", headline: title.length <= 110 ? title : articleSeoTitle(v, c).absolute, description: page?.meta_desc, mainEntityOfPage: `${SITE_URL}${path}`,
        author: { "@type": "Person", name: getAuthor(article.author).name, url: `${SITE_URL}/about` },
        publisher: { "@type": "Organization", name: "Rig Configurator", url: SITE_URL },
        datePublished: page?.published_at ?? article.reviewed, dateModified: article.reviewed ?? page?.updated_at,
        ...(hero ? { image: `${SITE_URL}/img/${hero.file}` } : {}) }] : []),
      ...(faq.length ? [{ "@type": "FAQPage", mainEntity: faq.map(x => ({ "@type": "Question", name: x.q, acceptedAnswer: { "@type": "Answer", text: x.a } })) }] : []),
    ],
  };

  if (article) return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />
      <ArticleView v={v} c={c} fits={fits} a={article} title={title} faq={faq} related={related} path={path} verifiedAt={page?.verified_at} hero={hero} links={links} />
    </>
  );

  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />
      <div className="crumbs"><Link href="/vehicles">Vehicles</Link> › <Link href={vehiclePath(v)}>{vehicleTitle(v)}</Link> › {c.name}</div>
      <h1>{title}</h1>
      {page?.verified_at && <div className="muted">Fit data verified {new Date(page.verified_at).toLocaleDateString("en-US", { month: "long", year: "numeric" })} · affiliate links, no extra cost to you</div>}
      <div className="box">{md(page?.intro_md) ?? <p>Every product below is matched to this exact generation. Check the fit pill and note on each card.</p>}</div>

      {fits.length > 0 && (<>
        <h2>Fit-verified comparison</h2>
        <table>
          <thead><tr><th>#</th><th>Product</th><th>Fits</th><th>Type</th><th>Weight</th><th>Price</th><th></th></tr></thead>
          <tbody>
            {fits.map((f, i) => (
              <tr key={f.id}>
                <td>{i + 1}</td>
                <td><a href={`#${f.asin}`}>{f.name}</a></td>
                <td>{Object.values(f.condition ?? {}).join(", ") || "All"}</td>
                <td>{f.attrs?.type ?? "—"}</td>
                <td>{f.weight_lb ? `${f.weight_lb} lb` : "—"}</td>
                <td>{money(f.price_cents, f.price_band)}</td>
                <td><a href={`/go/${f.product_id}?page=${encodeURIComponent(path)}&placement=table-${i + 1}`} rel="nofollow sponsored" target="_blank">Buy</a></td>
              </tr>))}
          </tbody>
        </table>
        <h2>Top picks, ranked</h2>
        <div style={{ display: "grid", gap: 16 }}>
          {fits.map((f, i) => <ProductCard key={f.id} f={f} rank={i + 1} page={path} />)}
        </div>
      </>)}

      {page?.gotchas_md && (<><h2>Fit gotchas for the {vehicleTitle(v)}</h2>{md(page.gotchas_md)}</>)}
      {page?.install_md && (<><h2>Install notes</h2>{md(page.install_md)}</>)}
      {faq.length > 0 && (<><h2>FAQ</h2>{faq.map(x => <div key={x.q} className="card" style={{ marginBottom: 8 }}><strong>{x.q}</strong><p style={{ margin: "6px 0 0" }}>{x.a}</p></div>)}</>)}
      {page?.verdict_md && (<><h2>Verdict</h2>{md(page.verdict_md)}</>)}

      <p style={{ marginTop: 32 }}><Link className="btn" href={`/build?vehicle=${v.id}`}>Build your full {v.model_name} setup →</Link></p>
    </>
  );
}
