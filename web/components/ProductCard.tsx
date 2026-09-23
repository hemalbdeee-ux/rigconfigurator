import type { Fit } from "@/lib/queries";
import { money } from "@/lib/db";

export function ProductCard({ f, rank, page }: { f: Fit; rank: number; page: string }) {
  const conf = f.confidence === 3 ? ["ok", "Fit verified"] : f.confidence === 2 ? ["", "Fit per listing"] : ["warn", "Fit unverified"];
  const cond = Object.entries(f.condition ?? {}).map(([k, v]) => `${k.replace(/_/g, " ")}: ${v}`).join(" · ");
  const go = `/go/${f.product_id}?page=${encodeURIComponent(page)}&placement=card-${rank}`;
  return (
    <div className="card product" id={f.asin}>
      {f.image_url ? <img src={f.image_url} alt={f.name} loading="lazy" /> : <div style={{ width: 120, height: 120, background: "#222", borderRadius: 8 }} />}
      <div>
        <h3>#{rank} {f.name}</h3>
        <div className="muted">{f.brand} {f.rating ? `· ★ ${f.rating} (${f.reviews?.toLocaleString()} reviews)` : ""}</div>
        <div style={{ margin: "6px 0" }}>
          <span className={`pill ${conf[0]}`}>{conf[1]}</span>
          {cond && <span className="pill">{cond}</span>}
          {f.attrs?.type && <span className="pill">{f.attrs.type}</span>}
        </div>
        {f.note && <div className="muted" style={{ fontSize: 14 }}>⚠ {f.note}</div>}
        <ul>{f.pros?.map(p => <li key={p}>✔ {p}</li>)}{f.cons?.map(c => <li key={c}>✘ {c}</li>)}</ul>
      </div>
      <div className="cta" style={{ textAlign: "right" }}>
        <div style={{ fontSize: 20, fontWeight: 700 }}>{money(f.price_cents, f.price_band)}</div>
        <a className="btn" href={go} rel="nofollow sponsored noopener" target="_blank">View on Amazon</a>
      </div>
    </div>
  );
}
