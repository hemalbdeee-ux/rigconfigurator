import Link from "next/link";
import { getAuthor } from "@/lib/authors";
import type { Table } from "@/lib/pillars";
import { Inline, Linker, Md } from "./Md";

export const fmtDate = (d?: string | null) => d ? new Date(d).toLocaleDateString("en-US", { month: "long", day: "numeric", year: "numeric", timeZone: "UTC" }) : "";

export function T({ t, linker }: { t: Table; linker?: Linker }) {
  return (
    <div className="tbl">
      {t.caption && <div className="tbl-cap">{t.caption}</div>}
      <table>
        <thead><tr>{t.head.map(h => <th key={h}>{h}</th>)}</tr></thead>
        <tbody>{t.rows.map((r, i) => <tr key={i}>{r.map((c, j) => <td key={j}>{j === 0 ? <strong><Inline s={c} /></strong> : <Inline s={c} linker={linker} />}</td>)}</tr>)}</tbody>
      </table>
    </div>
  );
}

export function Byline({ author, reviewed }: { author?: string; reviewed?: string }) {
  const a = getAuthor(author);
  return (
    <div className="byline">
      By <Link href="/about">{a.name}</Link> · {a.role}{reviewed && <> · Last reviewed {fmtDate(reviewed)}</>}
    </div>
  );
}

export function Takeaways({ items, linker }: { items: string[]; linker?: Linker }) {
  return (
    <section className="box takeaways">
      <strong>Key takeaways</strong>
      <ol>{items.map(t => <li key={t}><Inline s={t} linker={linker} /></li>)}</ol>
    </section>
  );
}

export function Toc({ items }: { items: [string, string][] }) {
  return <nav className="toc-box"><strong>On this page</strong><ol>{items.map(([id, label]) => <li key={id}><a href={`#${id}`}>{label}</a></li>)}</ol></nav>;
}

export function Avoid({ items, linker }: { items?: { h: string; body: string }[]; linker?: Linker }) {
  if (!items?.length) return null;
  return (<section id="avoid"><h2>What to avoid</h2>
    <div className="box warnbox">{items.map(x => <p key={x.h}><strong>{x.h}.</strong> <Inline s={x.body} linker={linker} /></p>)}</div></section>);
}

export function Faq({ faq, linker }: { faq: { q: string; a: string }[]; linker?: Linker }) {
  if (!faq.length) return null;
  return (<section id="faq"><h2>Frequently asked questions</h2>
    {faq.map(x => <details key={x.q} className="faq"><summary>{x.q}</summary><p><Inline s={x.a} linker={linker} /></p></details>)}</section>);
}

export function Verdict({ v, linker }: { v: { thesis: string; body: string }; linker?: Linker }) {
  return (
    <section id="verdict" className="verdict">
      <div className="muted" style={{ fontSize: 12, letterSpacing: ".08em" }}>BOTTOM LINE</div>
      <h2 style={{ marginTop: 6 }}>{v.thesis}</h2>
      <Md s={v.body} linker={linker} />
    </section>
  );
}

export function Method({ method, sources }: { method?: string; sources?: [string, string][] }) {
  if (!method && !sources?.length) return null;
  return (
    <section className="method"><h3>How we wrote this</h3>{method && <p>{method}</p>}
      {sources?.length ? (<><strong style={{ fontSize: 14 }}>Sources</strong><ul className="sources">{sources.map(([l, u]) => <li key={u}><a href={u} rel="nofollow noopener" target="_blank">{l}</a></li>)}</ul></>) : null}
    </section>
  );
}

export function AuthorBox({ author }: { author?: string }) {
  const a = getAuthor(author);
  return (
    <section className="author">
      <div className="avatar">{a.name.split(" ").map(w => w[0]).join("")}</div>
      <div><strong><Link href="/about">{a.name}</Link></strong> <span className="muted">· {a.role}</span>
        <p style={{ margin: "4px 0" }}>{a.bio}</p>
        <div>{a.facts.map(x => <span key={x} className="pill">{x}</span>)}</div></div>
    </section>
  );
}
