import Link from "next/link";
import type { Metadata } from "next";
import { allPillars } from "@/lib/pillars";
import { SITE_URL } from "@/lib/db";
import { staticOg } from "@/components/Hero";

// Rendered per request: at `docker build` the DB is unreachable and a prerendered copy would be empty.
export const dynamic = "force-dynamic";
export const metadata: Metadata = {
  title: "Learn: Truck & SUV Accessory Explainers",
  description: "Plain-English explainers for truck and SUV accessories: hard vs soft tonneau covers, hitch classes, roof rail types, and upgrade plans by vehicle.",
  alternates: { canonical: "/learn" },
  openGraph: { title: "Learn: Truck & SUV Accessory Explainers | Rig Configurator", url: "/learn", type: "website", images: staticOg("guides", "Learn") },
};

export default async function Learn() {
  const all = await allPillars();
  const explainers = all.filter(p => p.kind === "explainer");
  const upgrades = all.filter(p => p.kind === "upgrades");
  const jsonLd = { "@context": "https://schema.org", "@type": "CollectionPage", url: `${SITE_URL}/learn`, name: "Learn",
    hasPart: all.map(p => ({ "@type": "Article", headline: p.title, url: `${SITE_URL}${p.path}` })) };
  return (
    <article className="art">
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />
      <h1>Learn</h1>
      <p className="dek">The questions to settle before you pick a product: which type, which rating, which size. Each explainer links to the fit-checked guides for every vehicle we cover.</p>
      {explainers.length > 0 && (<section><h2>Explainers</h2>
        <div className="grid">{explainers.map(p => <Link key={p.path} href={p.path} className="card"><h3>{p.title}</h3>{p.dek && <div className="muted" style={{ fontSize: 14 }}>{p.dek}</div>}</Link>)}</div></section>)}
      {upgrades.length > 0 && (<section><h2>Upgrade plans by vehicle</h2>
        <div className="grid">{upgrades.map(p => <Link key={p.path} href={p.path} className="card"><h3>{p.title}</h3>{p.dek && <div className="muted" style={{ fontSize: 14 }}>{p.dek}</div>}</Link>)}</div></section>)}
      <p style={{ marginTop: 24 }}><Link href="/guides">Browse all buying guides by category →</Link></p>
    </article>
  );
}
