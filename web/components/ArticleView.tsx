import Link from "next/link";
import type { Category, Fit, GuideLink, Vehicle } from "@/lib/queries";
import { vehiclePath, vehicleTitle } from "@/lib/queries";
import { money } from "@/lib/db";
import { getAuthor } from "@/lib/authors";
import { Inline, Linker, Md } from "./Md";
import { Hero } from "./Hero";
import type { Hero as HeroT } from "@/lib/queries";

type Table = { caption?: string; head: string[]; rows: string[][] };
type Pick = { asin: string; role: string; price?: string; pros: string[]; cons: string[]; body: string; who: string; specs: [string, string][] };
export type Article = {
  dek: string; author?: string; reviewed?: string; method?: string; takeaways: string[];
  top_picks: { asin: string; role: string; why: string }[];
  fit_table?: Table; look_for: { h: string; body: string }[]; look_table?: Table; types_table?: Table;
  picks: Pick[]; install?: string[]; avoid?: { h: string; body: string }[];
  verdict: { thesis: string; body: string }; sources?: [string, string][];
};

const slug = (s: string) => s.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/(^-|-$)/g, "");
const fmtDate = (d?: string) => d ? new Date(d).toLocaleDateString("en-US", { month: "long", day: "numeric", year: "numeric" }) : "";

function T({ t }: { t: Table }) {
  return (
    <div className="tbl">
      {t.caption && <div className="tbl-cap">{t.caption}</div>}
      <table>
        <thead><tr>{t.head.map(h => <th key={h}>{h}</th>)}</tr></thead>
        <tbody>{t.rows.map((r, i) => <tr key={i}>{r.map((c, j) => <td key={j}>{j === 0 ? <strong>{c}</strong> : c}</td>)}</tr>)}</tbody>
      </table>
    </div>
  );
}

function Buy({ f, path, placement, label = "Check price on Amazon" }: { f?: Fit; path: string; placement: string; label?: string }) {
  if (!f) return null;
  return <a className="btn" href={`/go/${f.product_id}?page=${encodeURIComponent(path)}&placement=${placement}`} rel="nofollow sponsored noopener" target="_blank">{label} ›</a>;
}

export function ArticleView({ v, c, fits, a, title, faq, related, path, verifiedAt, hero, links }: {
  v: Vehicle; c: Category; fits: Fit[]; a: Article; title: string; faq: { q: string; a: string }[];
  related: GuideLink[]; path: string; verifiedAt?: string | null; hero: HeroT | null; links: Record<string, string>;
}) {
  const L = new Linker(links);
  const next = related.find(r => r.vehicle === vehicleTitle(v));
  const byAsin = new Map(fits.map(f => [f.asin, f]));
  const author = getAuthor(a.author);
  const picked = new Set(a.picks.map(p => p.asin));
  const others = fits.filter(f => !picked.has(f.asin));
  const toc: [string, string][] = [
    ...(a.fit_table ? [["fit-check", "Which bed do you have?"] as [string, string]] : []),
    ["what-to-look-for", "What to look for"],
    ...(a.types_table ? [["types", "Cover types compared"] as [string, string]] : []),
    ...a.picks.map((p, i) => [slug(`pick-${i + 1}`), `#${i + 1}: ${byAsin.get(p.asin)?.brand ?? ""} — ${p.role}`] as [string, string]),
    ...(a.install?.length ? [["install", "How to install"] as [string, string]] : []),
    ...(a.avoid?.length ? [["avoid", "What to avoid"] as [string, string]] : []),
    ["faq", "FAQ"], ["verdict", "Verdict"],
  ];

  return (
    <article className="art">
      <div className="crumbs"><Link href="/vehicles">Vehicles</Link> › <Link href={vehiclePath(v)}>{vehicleTitle(v)}</Link> › {c.name}</div>
      <h1>{title}</h1>
      <p className="dek">{a.dek}</p>
      <Hero h={hero} alt={`${vehicleTitle(v)} — ${c.name.toLowerCase()} guide`} priority />
      <div className="byline">
        By <Link href="/about">{author.name}</Link> · {author.role}
        {a.reviewed && <> · Last reviewed {fmtDate(a.reviewed)}</>}
        {verifiedAt && <> · Fit data verified {fmtDate(verifiedAt)}</>}
      </div>
      <div className="disclose">We earn a commission from qualifying Amazon purchases, at no extra cost to you. <Link href="/disclosure">How we make money</Link>.</div>

      <section className="picks-box">
        <div className="picks-h">Our top picks</div>
        {a.top_picks.map((t, i) => {
          const f = byAsin.get(t.asin);
          if (!f) return null;
          return (
            <div key={t.asin} className="pick-row">
              <span className="mini-rank">{i + 1}</span>
              <div><a href={`#pick-${a.picks.findIndex(p => p.asin === t.asin) + 1}`} className="pick-name">{f.name.split(",")[0]}</a>
                <div className="muted" style={{ fontSize: 13 }}><strong>{t.role}</strong> — {t.why}</div></div>
              <div className="mini-cta"><div style={{ fontWeight: 700 }}>{a.picks.find(p => p.asin === t.asin)?.price ?? money(f.price_cents, f.price_band)}</div>
                <a href={`/go/${f.product_id}?page=${encodeURIComponent(path)}&placement=top-${i + 1}`} rel="nofollow sponsored noopener" target="_blank">Amazon ›</a></div>
            </div>
          );
        })}
      </section>

      <section className="box takeaways">
        <strong>Key takeaways</strong>
        <ol>{a.takeaways.map(t => <li key={t}><Inline s={t} linker={L} /></li>)}</ol>
      </section>

      <nav className="toc-box"><strong>On this page</strong><ol>{toc.map(([id, label]) => <li key={id}><a href={`#${id}`}>{label}</a></li>)}</ol></nav>

      {a.fit_table && (<section id="fit-check"><h2>Which {v.model_name} bed do you have?</h2><T t={a.fit_table} /></section>)}

      <section id="what-to-look-for">
        <h2>What to look for in a {v.model_name} {c.name.toLowerCase().replace(/s$/, "")}</h2>
        {a.look_for.map(x => <div key={x.h}><h3>{x.h}</h3><Md s={x.body} linker={L} /></div>)}
        {a.look_table && <T t={a.look_table} />}
      </section>

      {a.types_table && (<section id="types"><h2>{c.name} types compared</h2><T t={a.types_table} /></section>)}

      {a.picks.map((p, i) => {
        const f = byAsin.get(p.asin);
        if (!f) return null;
        return (
          <section key={p.asin} id={`pick-${i + 1}`} className="pick">
            <h2>#{i + 1}: {f.name.split(",")[0]} — {p.role} ({p.price ?? money(f.price_cents, f.price_band)})</h2>
            <div className="card pcard">
              <div className="pcard-top">
                {f.image_url ? <img src={f.image_url} alt={f.name} loading="lazy" /> : null}
                <div>
                  <div className="muted" style={{ fontSize: 13, textTransform: "uppercase", letterSpacing: ".05em" }}>{f.brand}</div>
                  <h3 style={{ margin: "2px 0 6px" }}>{f.name}</h3>
                  <span className={`pill ${f.confidence === 1 ? "warn" : "ok"}`}>{f.confidence === 1 ? "Confirm fit on listing" : "Listed for this truck"}</span>
                  {f.note && <span className="pill">{f.note}</span>}
                </div>
                <div className="pcard-price"><div className="price">{p.price ?? money(f.price_cents, f.price_band)}</div><Buy f={f} path={path} placement={`pick-${i + 1}`} /></div>
              </div>
              <div className="proscons">
                <div><div className="pc-h ok">Pros</div><ul>{p.pros.map(x => <li key={x}>{x}</li>)}</ul></div>
                <div><div className="pc-h bad">Cons</div><ul>{p.cons.map(x => <li key={x}>{x}</li>)}</ul></div>
              </div>
            </div>
            <Md s={p.body} linker={L} />
            <p><strong>Who it's for:</strong> {p.who}</p>
            <T t={{ caption: `${f.brand} specifications`, head: ["Spec", "Value"], rows: p.specs }} />
          </section>
        );
      })}

      {others.length > 0 && (<section>
        <h3>Also fit-checked for the {vehicleTitle(v)}</h3>
        <ul>{others.map((f, i) => <li key={f.asin}>{f.name} — {money(f.price_cents, f.price_band)} · <a href={`/go/${f.product_id}?page=${encodeURIComponent(path)}&placement=also-${i + 1}`} rel="nofollow sponsored noopener" target="_blank">Amazon</a></li>)}</ul>
      </section>)}

      {a.install?.length ? (<section id="install"><h2>How to install a {c.name.toLowerCase().replace(/s$/, "")} on the {v.model_name}</h2><ol>{a.install.map(s => <li key={s}><Inline s={s} linker={L} /></li>)}</ol></section>) : null}

      {a.avoid?.length ? (<section id="avoid"><h2>What to avoid</h2><div className="box warnbox">{a.avoid.map(x => <p key={x.h}><strong>{x.h}.</strong> <Inline s={x.body} linker={L} /></p>)}</div></section>) : null}

      <section className="cta-box">
        <strong>See everything that fits your {v.model_name}</strong>
        <p className="muted">Bed, roof, hitch and interior, filtered to the {vehicleTitle(v)}.</p>
        <Link className="btn" href={vehiclePath(v)}>Open the {v.model_name} fit hub →</Link>
      </section>

      {faq.length > 0 && (<section id="faq"><h2>Frequently asked questions</h2>
        {faq.map(x => <details key={x.q} className="faq"><summary>{x.q}</summary><p><Inline s={x.a} linker={L} /></p></details>)}</section>)}

      <section id="verdict" className="verdict">
        <div className="muted" style={{ fontSize: 12, letterSpacing: ".08em" }}>FINAL VERDICT</div>
        <h2 style={{ marginTop: 6 }}>{a.verdict.thesis}</h2>
        <Md s={a.verdict.body} linker={L} />
      </section>

      {next && (<Link href={next.path} className="next-step" style={{ display: "block" }}>
        <div className="lbl">Next step for your {v.model_name}</div>
        <strong style={{ color: "var(--fg)" }}>{next.title}</strong> <span>→</span>
      </Link>)}

      {a.method && (<section className="method"><h3>How we chose</h3><p>{a.method}</p>
        {a.sources?.length ? (<><strong style={{ fontSize: 14 }}>Sources</strong><ul className="sources">{a.sources.map(([l, u]) => <li key={u}><a href={u} rel="nofollow noopener" target="_blank">{l}</a></li>)}</ul></>) : null}
      </section>)}

      <section className="author">
        <div className="avatar">{author.name.split(" ").map(w => w[0]).join("")}</div>
        <div><strong><Link href="/about">{author.name}</Link></strong> <span className="muted">· {author.role}</span>
          <p style={{ margin: "4px 0" }}>{author.bio}</p>
          <div>{author.facts.map(x => <span key={x} className="pill">{x}</span>)}</div></div>
      </section>

      {related.length > 0 && (<section><h2>Related guides</h2>
        <p className="muted" style={{ fontSize: 14 }}><Link href={`/guides/${c.slug}`}>All {c.name.toLowerCase()} guides by vehicle →</Link> · <Link href={vehiclePath(v)}>Everything that fits the {vehicleTitle(v)} →</Link></p>
        <div className="grid">{related.map(r => <Link key={r.path} href={r.path} className="card"><div className="muted" style={{ fontSize: 12 }}>{r.category} · {r.vehicle}</div><h3 style={{ marginTop: 4 }}>{r.title}</h3></Link>)}</div></section>)}
    </article>
  );
}
