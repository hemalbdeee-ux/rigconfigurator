import Link from "next/link";
import { notFound } from "next/navigation";
import type { Metadata } from "next";
import { allVehicles, categoriesFor, fitsFor, getVehicle, heroFor, pagesFor, siblingsOf, vehiclePath, vehicleTitle, yearsLabel, type Fit } from "@/lib/queries";
import { Hero, ogImage } from "@/components/Hero";
import { categoryBlurb, checkBeforeBuying } from "@/lib/hubCopy";
import { SITE_URL, money } from "@/lib/db";
import { hubSeoTitle } from "@/lib/seo";

export const revalidate = 3600;
type P = { make: string; model: string; gen: string };

export async function generateStaticParams() {
  const vs = await allVehicles();
  return vs.map(v => ({ make: v.make_slug, model: v.model_slug, gen: v.gen_slug }));
}

export async function generateMetadata({ params }: { params: Promise<P> }): Promise<Metadata> {
  const { make, model, gen } = await params;
  const v = await getVehicle(make, model, gen);
  if (!v) return {};
  const description = `Fit facts for the ${vehicleTitle(v)} (${v.gen_name}) and every accessory verified to fit it: bed, roof, hitch and interior.`;
  const title = hubSeoTitle(v);
  return {
    title,
    description,
    alternates: { canonical: vehiclePath(v) },
    openGraph: { title: title.absolute, description, url: vehiclePath(v), siteName: "Rig Configurator", type: "website", images: ogImage(await heroFor(v.id)) },
  };
}

function MiniPick({ f, rank, page }: { f: Fit; rank: number; page: string }) {
  const cond = Object.values(f.condition ?? {}).filter(x => typeof x !== "boolean").join(", ");
  return (
    <div className="mini">
      <span className="mini-rank">{rank}</span>
      <div className="mini-body">
        <div className="mini-name">{f.name}</div>
        <div className="muted" style={{ fontSize: 13 }}>
          {f.brand}{cond ? ` · fits ${cond}` : ""}{f.confidence === 3 ? " · fit verified" : ""}
        </div>
      </div>
      <div className="mini-cta">
        <div style={{ fontWeight: 700 }}>{money(f.price_cents, f.price_band)}</div>
        <a href={`/go/${f.product_id}?page=${encodeURIComponent(page)}&placement=hub-${rank}`} rel="nofollow sponsored noopener" target="_blank">Amazon ›</a>
      </div>
    </div>
  );
}

export default async function VehicleHub({ params }: { params: Promise<P> }) {
  const { make, model, gen } = await params;
  const v = await getVehicle(make, model, gen);
  if (!v) notFound();
  const [cats, fits, pages, sibs, hero] = await Promise.all([categoriesFor(v.body_style), fitsFor(v.id), pagesFor(v.id), siblingsOf(v), heroFor(v.id)]);
  const path = vehiclePath(v);
  const published = new Map(pages.filter(p => p.status === "published").map(p => [p.category_slug, p]));
  const byCat = (slug: string) => fits.filter(f => f.category_slug === slug);
  const ready = cats.filter(c => published.has(c.slug) && byCat(c.slug).length > 0);
  const planned = cats.filter(c => !ready.includes(c));

  const facts: [string, string | null][] = [
    ["Generation", v.gen_name], ["Years", v.year_to ? yearsLabel(v) : `${v.year_from}–present (current generation)`], ["Body", v.body_style.toUpperCase()],
    ["Bed lengths", v.bed_lengths_in?.length ? v.bed_lengths_in.map(b => `${b} in (${(b / 12).toFixed(1)} ft)`).join(", ") : null],
    ["Roof type", v.roof_type], ["Roof load", v.roof_load_lb ? `${v.roof_load_lb} lb dynamic` : null],
    ["Hitch class", v.hitch_class && v.hitch_class !== "none" ? `Class ${v.hitch_class} (${v.receiver_in} in receiver)` : "No factory receiver"],
    ["Tow rating", v.tow_rating_lb ? `${v.tow_rating_lb.toLocaleString()} lb (max, tow package)` : null],
    ["Tire size", v.tire_size], ["Bolt pattern", v.bolt_pattern], ["Seating rows", String(v.rows_seating)],
  ];
  const checks = checkBeforeBuying(v);

  const jsonLd = {
    "@context": "https://schema.org",
    "@graph": [
      { "@type": "BreadcrumbList", itemListElement: [
        { "@type": "ListItem", position: 1, name: "Vehicles", item: `${SITE_URL}/vehicles` },
        { "@type": "ListItem", position: 2, name: vehicleTitle(v), item: `${SITE_URL}${path}` }] },
      { "@type": "ItemList", name: `${vehicleTitle(v)} accessory guides`, itemListElement: ready.map((c, i) => ({
        "@type": "ListItem", position: i + 1, url: `${SITE_URL}${path}/${c.slug}`, name: published.get(c.slug)!.title })) },
    ],
  };

  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />
      <div className="crumbs"><Link href="/vehicles">Vehicles</Link> › {v.make_name} › {v.model_name} › {v.gen_name}</div>
      <h1>{vehicleTitle(v)} Accessories That Fit</h1>
      <p className="muted">{v.summary}</p>
      <Hero h={hero} alt={`${vehicleTitle(v)} (${v.gen_name})`} priority />

      <div className="stats">
        <div><strong>{ready.length}</strong><span>fit-checked guides</span></div>
        <div><strong>{fits.length}</strong><span>products matched</span></div>
        <div><strong>{v.tow_rating_lb ? `${(v.tow_rating_lb / 1000).toFixed(1)}k` : "—"}</strong><span>lb max tow</span></div>
      </div>

      {ready.length > 0 && (
        <nav className="toc">
          <strong>Jump to:</strong> {ready.map((c, i) => <span key={c.slug}>{i > 0 && " · "}<a href={`#${c.slug}`}>{c.name}</a></span>)}
        </nav>
      )}

      <h2>Fit facts</h2>
      <table><tbody>
        {facts.filter(([, val]) => val).map(([k, val]) => <tr key={k}><th>{k}</th><td>{val}</td></tr>)}
      </tbody></table>

      {checks.length > 0 && (<>
        <h2>Check before you buy</h2>
        <ul>{checks.map(c => <li key={c}>{c}</li>)}</ul>
      </>)}

      {ready.map(c => {
        const list = byCat(c.slug);
        const p = published.get(c.slug)!;
        return (
          <section key={c.slug} id={c.slug} className="hub-sec">
            <h2>{c.name}</h2>
            <p>{categoryBlurb(c.slug, v)}</p>
            <div className="mini-list">{list.slice(0, 3).map((f, i) => <MiniPick key={f.id} f={f} rank={i + 1} page={path} />)}</div>
            <p><Link href={`${path}/${c.slug}`}>{list.length > 3 ? `See all ${list.length} fit-checked ${c.name.toLowerCase()} →` : `Full ${c.name.toLowerCase()} guide: ${p.title} →`}</Link>
              <span className="muted" style={{ fontSize: 14 }}> · <Link href={`/guides/${c.slug}`}>{c.name} for other vehicles</Link></span></p>
          </section>
        );
      })}

      {ready.length === 0 && (<>
        <h2>Accessory guides</h2>
        <p className="muted">Product lists for this {v.model_name} are still in fit verification. Use the fit facts above to shop safely in the meantime — bed length, roof type and receiver size answer most compatibility questions.</p>
      </>)}

      {planned.length > 0 && (
        <p className="muted" style={{ marginTop: 24, fontSize: 14 }}>
          In verification for the {v.model_name}: {planned.map(c => c.name).join(", ")}.
        </p>
      )}

      <p style={{ marginTop: 24 }}><Link className="btn" href={`/build?vehicle=${v.id}`}>Build your {v.model_name} setup</Link></p>

      {sibs.length > 0 && (<>
        <h2>Related vehicles</h2>
        <div className="grid">
          {sibs.map(s => (
            <Link key={s.id} href={vehiclePath(s)} className="card">
              <h3>{vehicleTitle(s)}</h3><div className="muted">{s.gen_name}</div>
            </Link>
          ))}
        </div>
      </>)}
    </>
  );
}
