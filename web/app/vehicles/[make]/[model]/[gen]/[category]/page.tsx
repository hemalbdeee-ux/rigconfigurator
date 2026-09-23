import Link from "next/link";
import { notFound } from "next/navigation";
import type { Metadata } from "next";
import { allFitmentPaths, fitsFor, getCategory, getFitmentPage, getVehicle, vehiclePath, vehicleTitle } from "@/lib/queries";
import { ProductCard } from "@/components/ProductCard";
import { SITE_URL, amazonUrl, money } from "@/lib/db";

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
  const [fits, page] = await Promise.all([fitsFor(v.id, c.slug), getFitmentPage(v.id, c.id)]);
  return { v, c, fits, page };
}

export async function generateMetadata({ params }: { params: Promise<P> }): Promise<Metadata> {
  const d = await load(await params);
  if (!d) return {};
  const title = d.page?.title ?? `Best ${d.c.name} for ${vehicleTitle(d.v)}`;
  return {
    title,
    description: d.page?.meta_desc ?? `${d.c.name} verified to fit the ${vehicleTitle(d.v)}, with prices and fit notes.`,
    alternates: { canonical: `${vehiclePath(d.v)}/${d.c.slug}` },
    robots: d.page?.status === "published" ? undefined : { index: false },
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
  const { v, c, fits, page } = d;
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
      { "@type": "ItemList", name: title, itemListElement: fits.map((f, i) => ({
        "@type": "ListItem", position: i + 1, url: amazonUrl(f.asin), name: f.name })) },
      ...(faq.length ? [{ "@type": "FAQPage", mainEntity: faq.map(x => ({ "@type": "Question", name: x.q, acceptedAnswer: { "@type": "Answer", text: x.a } })) }] : []),
    ],
  };

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
