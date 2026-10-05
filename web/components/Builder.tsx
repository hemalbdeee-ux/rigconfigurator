"use client";
import { useMemo, useState } from "react";
import Link from "next/link";

// A trimmed Fit for the client bundle: only what the builder renders.
export type BuildItem = {
  product_id: number; asin: string; name: string; brand: string | null; image_url: string | null;
  price_cents: number | null; price_band: string | null; price_checked_at: string | null; rank: number; note: string | null;
};
export type BuildSlot = { slug: string; name: string; guide: string | null; items: BuildItem[] };

const money = (c: number) => `$${(c / 100).toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
const stamp = (at: string) => {
  const d = new Date(at), p = (n: number) => String(n).padStart(2, "0");
  return `${p(d.getUTCMonth() + 1)}/${p(d.getUTCDate())}/${d.getUTCFullYear()} ${p(d.getUTCHours())}:${p(d.getUTCMinutes())} UTC`;
};

export function Builder({ slots, hub, vehicleLabel }: { slots: BuildSlot[]; hub: string; vehicleLabel: string }) {
  // slot slug -> chosen product_id, or 0 when the slot is skipped
  const [choice, setChoice] = useState<Record<string, number>>(() => Object.fromEntries(slots.map(s => [s.slug, s.items[0]?.product_id ?? 0])));
  const chosen = useMemo(() => slots.map(s => ({ s, it: s.items.find(i => i.product_id === choice[s.slug]) ?? null })), [slots, choice]);
  const priced = chosen.filter(x => x.it?.price_cents);
  const unpriced = chosen.filter(x => x.it && !x.it.price_cents);
  const total = priced.reduce((n, x) => n + (x.it!.price_cents ?? 0), 0);
  const go = (it: BuildItem, slug: string) => `/go/${it.product_id}?page=${encodeURIComponent(`/build`)}&placement=build-${slug}`;

  return (
    <div className="builder">
      <div className="build-list">
        {slots.map(s => {
          const it = s.items.find(i => i.product_id === choice[s.slug]) ?? null;
          return (
            <section key={s.slug} className={`build-slot${it ? "" : " skipped"}`}>
              <div className="build-head">
                <label className="build-toggle">
                  <input type="checkbox" checked={!!it} onChange={e => setChoice(c => ({ ...c, [s.slug]: e.target.checked ? (s.items[0]?.product_id ?? 0) : 0 }))} />
                  <span>{s.name}</span>
                </label>
                {s.guide && <Link href={s.guide} className="muted" style={{ fontSize: 13 }}>Full guide →</Link>}
              </div>
              {it && (
                <div className="build-row">
                  <a href={go(it, s.slug)} rel="nofollow sponsored noopener" target="_blank" className="build-img">
                    {it.image_url ? <img src={it.image_url} alt={it.name} loading="lazy" /> : <div className="img-ph" aria-hidden="true" />}
                  </a>
                  <div className="build-body">
                    <select value={it.product_id} onChange={e => setChoice(c => ({ ...c, [s.slug]: Number(e.target.value) }))} aria-label={`${s.name} pick`}>
                      {s.items.map(o => <option key={o.product_id} value={o.product_id}>#{o.rank} {o.name.split(",")[0]}</option>)}
                    </select>
                    <div className="muted" style={{ fontSize: 13, marginTop: 6 }}>{it.brand}{it.note ? ` · ${it.note}` : ""}</div>
                  </div>
                  <div className="build-cta">
                    <div className="build-price">
                      {it.price_cents && it.price_checked_at
                        ? <><span className="price-src">Amazon price</span> {money(it.price_cents)}<span className="price-asof">as of {stamp(it.price_checked_at)} · <Link href="/disclosure#prices">Details</Link></span></>
                        : <span className="muted">{it.price_band ?? "See price on Amazon"}</span>}
                    </div>
                    <a className="btn" href={go(it, s.slug)} rel="nofollow sponsored noopener" target="_blank">View on Amazon ›</a>
                  </div>
                </div>
              )}
            </section>
          );
        })}
      </div>

      <aside className="build-total">
        <div className="eyebrow">Your {vehicleLabel} build</div>
        <ul className="list-plain">
          {chosen.filter(x => x.it).map(({ s, it }) => (
            <li key={s.slug}><span>{s.name}</span><strong>{it!.price_cents ? money(it!.price_cents) : (it!.price_band ?? "see Amazon")}</strong></li>
          ))}
        </ul>
        <div className="build-sum">
          <span>Amazon total ({priced.length} item{priced.length === 1 ? "" : "s"})</span>
          <strong>{money(total)}</strong>
        </div>
        {unpriced.length > 0 && <p className="muted" style={{ fontSize: 13 }}>{unpriced.length} item{unpriced.length === 1 ? " has" : "s have"} no live Amazon price right now and {unpriced.length === 1 ? "is" : "are"} not in the total.</p>}
        <p className="muted" style={{ fontSize: 12 }}>Amazon prices are as of the time stamp on each item and change often; the price on Amazon at checkout applies. Each button opens that product on Amazon.</p>
        <Link href={hub} className="btn-ghost">Back to the vehicle hub</Link>
      </aside>
    </div>
  );
}
