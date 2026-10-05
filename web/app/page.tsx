import type { Metadata } from "next";
import Link from "next/link";
import { SITE_URL } from "@/lib/db";
import { DEFAULT_OG } from "@/components/Hero";
import { allVehicles, vehiclePath, vehicleTitle } from "@/lib/queries";
import { GUIDE_COPY } from "@/lib/guideCopy";
import { allPillars } from "@/lib/pillars";
import { categoryCounts, featuredVehicles, recentGuides, siteStats, topPicks } from "@/lib/home";
import { VehiclePicker } from "@/components/VehiclePicker";
import { Price } from "@/components/Price";

// Rendered per request: at `docker build` the DB is unreachable and a prerendered copy would list no vehicles.
export const dynamic = "force-dynamic";

const HOME_TITLE = "Rig Configurator: Fit-Checked Truck & SUV Accessories";
const HOME_DESC = "Pick your vehicle, see only the racks, hitches, tonneau covers and gear that actually fit. Verified against manufacturer fit guides.";
export const metadata: Metadata = {
  title: { absolute: HOME_TITLE },
  description: HOME_DESC,
  alternates: { canonical: "/" },
  openGraph: { title: HOME_TITLE, description: HOME_DESC, url: "/", siteName: "Rig Configurator", type: "website", locale: "en_US", images: DEFAULT_OG },
  twitter: { card: "summary_large_image", title: HOME_TITLE, description: HOME_DESC },
};

const homeLd = {
  "@context": "https://schema.org",
  "@graph": [
    { "@type": "WebSite", "@id": `${SITE_URL}/#website`, url: `${SITE_URL}/`, name: "Rig Configurator", publisher: { "@id": `${SITE_URL}/#org` } },
    { "@type": "Organization", "@id": `${SITE_URL}/#org`, name: "Rig Configurator", url: `${SITE_URL}/` },
  ],
};

const CATEGORY_ICON: Record<string, string> = {
  "tonneau-covers": "▭", "bed-racks": "⌸", "roof-racks": "⌶", "cargo-boxes": "▣",
  "hitches": "⊙", "floor-mats": "▤", "running-boards": "▬", "led-light-bars": "✦",
};

const fmtDate = (d: string | null) => d ? new Date(d).toLocaleDateString("en-US", { month: "short", day: "numeric", year: "numeric", timeZone: "UTC" }) : "";

export default async function Home() {
  const [vehicles, stats, featured, picks, cats, recent, pillars] = await Promise.all([
    allVehicles(), siteStats(), featuredVehicles(), topPicks(6), categoryCounts(), recentGuides(6), allPillars(),
  ]);
  const explainers = pillars.filter(p => p.kind === "explainer").slice(0, 6);
  const pickerRows = vehicles.map(v => ({ make: v.make_name, label: vehicleTitle(v), path: vehiclePath(v) }));

  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(homeLd) }} />

      {/* 1. Hero: one job, get the visitor to their vehicle hub in one click */}
      <section className="home-hero">
        <div className="home-hero-copy">
          <div className="eyebrow">Fit-checked accessories for {stats.vehicles} trucks and SUVs</div>
          <h1>Parts that actually fit your rig.</h1>
          <p className="home-sub">Pick your vehicle. See only the tonneau covers, racks, hitches, liners and steps listed for that exact generation, with the live Amazon price next to each one.</p>
          <VehiclePicker vehicles={pickerRows} />
          <ul className="trust">
            <li><strong>{stats.guides}</strong> buying guides</li>
            <li><strong>{stats.products.toLocaleString()}</strong> fit-checked products</li>
            <li><strong>{stats.vehicles}</strong> vehicle generations</li>
            <li>Rankings never sold</li>
          </ul>
        </div>
      </section>

      {/* 2. Popular vehicles with photos: the second-fastest route to a hub */}
      <section className="home-sec">
        <div className="sec-head">
          <h2>Start with your vehicle</h2>
          <Link href="/vehicles">All {stats.vehicles} vehicles →</Link>
        </div>
        <div className="vgrid">
          {featured.map(v => (
            <Link key={v.id} href={vehiclePath(v)} className="vcard">
              {v.hero
                ? <img src={`/img/${v.hero.file.replace(/\.webp$/, "-800.webp")}`} alt={vehicleTitle(v)} loading="lazy" width={800} height={450} />
                : <div className="vcard-ph" aria-hidden="true">{v.body_style === "truck" ? "Truck" : "SUV"}</div>}
              <div className="vcard-body">
                <div className="vcard-title">{vehicleTitle(v)}</div>
                <div className="muted">{v.gen_name} · {v.guides} guide{v.guides === 1 ? "" : "s"}</div>
              </div>
            </Link>
          ))}
        </div>
      </section>

      {/* 3. Top picks: live Amazon price + direct link, the shortest path to a purchase */}
      {picks.length > 0 && (
        <section className="home-sec">
          <div className="sec-head">
            <h2>Top picks right now</h2>
            <span className="muted">Rank #1 in its guide · live Amazon price</span>
          </div>
          <div className="disclose">We earn a commission from qualifying Amazon purchases, at no extra cost to you. Prices labelled &ldquo;Amazon price&rdquo; come from Amazon and carry their own time stamp. <Link href="/disclosure">How we make money</Link>.</div>
          <div className="pgrid">
            {picks.map((p, i) => {
              const go = `/go/${p.product_id}?page=${encodeURIComponent("/")}&placement=home-pick-${i + 1}`;
              return (
                <div key={p.id} className="pcard-home">
                  <a href={go} rel="nofollow sponsored noopener" target="_blank" className="pcard-img">
                    {p.image_url ? <img src={p.image_url} alt={p.name} loading="lazy" /> : <div className="img-ph" aria-hidden="true" />}
                  </a>
                  <div className="pcard-meta">
                    <div className="pcard-role">{p.role ?? "Top pick"} · <Link href={p.page}>{p.vehicle} · {p.category_name}</Link></div>
                    <div className="pcard-name">{p.name.split(",")[0]}</div>
                    <div className="pcard-price-home"><Price f={p} href={go} /></div>
                  </div>
                  <div className="pcard-actions">
                    <a className="btn" href={go} rel="nofollow sponsored noopener" target="_blank">View on Amazon ›</a>
                    <Link href={p.page} className="btn-ghost">Why it ranks #1</Link>
                  </div>
                </div>
              );
            })}
          </div>
        </section>
      )}

      {/* 4. Shop by category */}
      <section className="home-sec">
        <div className="sec-head"><h2>Shop by category</h2><Link href="/guides">All guides →</Link></div>
        <div className="cgrid">
          {cats.map(c => (
            <Link key={c.slug} href={`/guides/${c.slug}`} className="ccard">
              <span className="cicon" aria-hidden="true">{CATEGORY_ICON[c.slug] ?? "•"}</span>
              <span className="ccard-body">
                <span className="ccard-title">{c.name}</span>
                <span className="muted">{GUIDE_COPY[c.slug]?.blurb ?? `${c.guides} vehicle guides`}</span>
                <span className="ccard-count">{c.guides} vehicle guide{c.guides === 1 ? "" : "s"}</span>
              </span>
            </Link>
          ))}
        </div>
      </section>

      {/* 5. How it works + why trust it */}
      <section className="home-sec how">
        <h2>How every guide is built</h2>
        <div className="how-grid">
          <div><span className="how-n">1</span><strong>One vehicle, one generation.</strong><p>Every guide covers one truck or SUV generation, because a redesign changes the bed, roof rails and hitch mounts. Nothing is matched by model name alone.</p></div>
          <div><span className="how-n">2</span><strong>Fit from the makers, not the badge.</strong><p>Bed lengths, roof types and tow ratings come from manufacturer fit guides and spec sheets. Where a maker publishes no figure, the guide says so and sends you to the owner&apos;s manual.</p></div>
          <div><span className="how-n">3</span><strong>Ranked on specs, priced live.</strong><p>Picks are ranked on published ratings, coverage, warranty and fit notes. Amazon prices refresh several times a day with a time stamp. A product&apos;s commission is never a ranking factor.</p></div>
        </div>
      </section>

      {/* 6. Recent guides + explainers */}
      <section className="home-sec two-col">
        <div>
          <div className="sec-head"><h2>Recently reviewed</h2></div>
          <ul className="list-plain">
            {recent.map(r => (
              <li key={r.path}>
                <Link href={r.path}>{r.title}</Link>
                <div className="muted">{r.vehicle} · {r.category}{r.reviewed ? ` · reviewed ${fmtDate(r.reviewed)}` : ""}</div>
              </li>
            ))}
          </ul>
        </div>
        <div>
          <div className="sec-head"><h2>Settle the basics first</h2><Link href="/learn">All explainers →</Link></div>
          <ul className="list-plain">
            {explainers.map(p => (
              <li key={p.path}><Link href={p.path}>{p.title}</Link>{p.dek && <div className="muted">{p.dek}</div>}</li>
            ))}
          </ul>
        </div>
      </section>

      {/* 7. Closing CTA */}
      <section className="home-cta">
        <h2>Ready when you are.</h2>
        <p className="muted">Pick your vehicle and see only what fits.</p>
        <VehiclePicker vehicles={pickerRows} compact />
      </section>
    </>
  );
}
