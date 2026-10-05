import type { Metadata } from "next";
import Link from "next/link";
import { staticOg } from "@/components/Hero";
import { activeDeals, trackingStats } from "@/lib/home";
import { Price } from "@/components/Price";

export const dynamic = "force-dynamic";

export const metadata: Metadata = {
  title: "Deals: Amazon Price Drops on Fit-Checked Truck & SUV Parts",
  description: "Fit-checked racks, covers, hitches, liners and steps whose Amazon price is at least 10% under their own 30-day high, from our price tracking.",
  alternates: { canonical: "/deals" },
  openGraph: { title: "Amazon Price Drops on Fit-Checked Parts | Rig Configurator", url: "/deals", type: "website", images: staticOg("vehicles", "Deals") },
};

const money = (c: number) => `$${(c / 100).toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
const fmtDate = (d: string) => new Date(d).toLocaleDateString("en-US", { month: "long", day: "numeric", year: "numeric", timeZone: "UTC" });

export default async function Deals() {
  const [deals, t] = await Promise.all([activeDeals(), trackingStats()]);
  return (
    <section className="tool-page wide">
      <h1>Deals</h1>
      <p className="dek">Products from our fit-checked guides whose Amazon price is at least 10% under their own 30-day high. The high comes from our price tracking, which records every Amazon price we fetch; nothing here is a list price or a seller&apos;s claim.</p>
      <div className="disclose">We earn a commission from qualifying Amazon purchases, at no extra cost to you. Prices labelled &ldquo;Amazon price&rdquo; come from Amazon and carry their own time stamp. <Link href="/disclosure">How we make money</Link>.</div>

      {deals.length === 0 ? (
        <div className="box">
          <strong>No qualifying drops yet.</strong>
          <p style={{ margin: "6px 0 0" }}>
            {t.since
              ? `Price tracking started on ${fmtDate(t.since)} and covers ${t.products.toLocaleString()} products. A drop is listed only once a product has at least two weeks of history and sits 10% or more under its 30-day high, so this page fills in over the first weeks.`
              : "Price tracking starts with the next price refresh. A drop is listed only once a product has at least two weeks of history and sits 10% or more under its 30-day high."}
          </p>
          <p style={{ margin: "10px 0 0" }}>Meanwhile every guide shows the live Amazon price next to each pick: <Link href="/vehicles">pick your vehicle</Link> or <Link href="/guides">browse by category</Link>.</p>
        </div>
      ) : (
        <div className="pgrid">
          {deals.map((d, i) => {
            const go = `/go/${d.product_id}?page=${encodeURIComponent("/deals")}&placement=deal-${i + 1}`;
            return (
              <div key={d.id} className="pcard-home">
                <a href={go} rel="nofollow sponsored noopener" target="_blank" className="pcard-img">
                  {d.image_url ? <img src={d.image_url} alt={d.name} loading="lazy" /> : <div className="img-ph" aria-hidden="true" />}
                </a>
                <div className="pcard-meta">
                  <div className="pcard-role">{d.drop_pct.toFixed(0)}% under its 30-day high · <Link href={d.page}>{d.vehicle} · {d.category_name}</Link></div>
                  <div className="pcard-name">{d.name.split(",")[0]}</div>
                  <div className="pcard-price-home"><Price f={d} href={go} /></div>
                  <div className="muted" style={{ fontSize: 13 }}>30-day high in our tracking: {money(d.hi_cents)}</div>
                </div>
                <div className="pcard-actions">
                  <a className="btn" href={go} rel="nofollow sponsored noopener" target="_blank">View on Amazon ›</a>
                  <Link href={d.page} className="btn-ghost">Fit notes</Link>
                </div>
              </div>
            );
          })}
        </div>
      )}
      {t.since && deals.length > 0 && <p className="muted" style={{ fontSize: 13, marginTop: 16 }}>Tracking since {fmtDate(t.since)}. The 30-day high is the highest Amazon price we recorded for that product in the last 30 days; the price on Amazon at checkout applies.</p>}
    </section>
  );
}
