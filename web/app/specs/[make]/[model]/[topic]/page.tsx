import Link from "next/link";
import { notFound } from "next/navigation";
import type { Metadata } from "next";
import { CONTACT_EMAIL, SITE_URL } from "@/lib/db";
import { allSpecs, getSpec, guidesForModel, hubsForModel, sameTopicElsewhere, specPath, specsForModel, type SpecRow } from "@/lib/specs";
import { getAuthor } from "@/lib/authors";
import { AuthorBox, fmtDate } from "@/components/PillarParts";
import { staticOg } from "@/components/Hero";

export const revalidate = 3600;
type P = { make: string; model: string; topic: string };

export async function generateStaticParams() {
  return (await allSpecs()).map(s => ({ make: s.make_slug, model: s.model_slug, topic: s.topic }));
}

export async function generateMetadata({ params }: { params: Promise<P> }): Promise<Metadata> {
  const { make, model, topic } = await params;
  const s = await getSpec(make, model, topic);
  if (!s) return {};
  const path = specPath(s);
  return {
    title: { absolute: s.seo_title }, description: s.meta_desc, alternates: { canonical: path },
    openGraph: { title: s.title, description: s.meta_desc, url: path, type: "article", images: staticOg("vehicles", s.title) },
  };
}

const srcList = (r: SpecRow): number[] => { const x = r[r.length - 1]; return Array.isArray(x) ? x : [x as number]; };

export default async function SpecPageView({ params }: { params: Promise<P> }) {
  const { make, model, topic } = await params;
  const s = await getSpec(make, model, topic);
  if (!s) notFound();
  const p = s.page, path = specPath(s), url = `${SITE_URL}${path}`, name = `${s.make_name} ${s.model_name}`;
  const [guides, hubs, siblings, elsewhere] = await Promise.all([guidesForModel(make, model, p.related ?? []), hubsForModel(make, model), specsForModel(make, model), sameTopicElsewhere(s)]);
  const others = siblings.filter(x => x.topic !== s.topic);
  const author = getAuthor();
  const jsonLd = {
    "@context": "https://schema.org",
    "@graph": [
      { "@type": "Organization", "@id": `${SITE_URL}/#organization`, name: "Rig Configurator", url: SITE_URL,
        logo: { "@type": "ImageObject", url: `${SITE_URL}/logo.png`, contentUrl: `${SITE_URL}/logo.png`, width: 600, height: 120 } },
      { "@type": "BreadcrumbList", "@id": `${url}#breadcrumb`, name: `Specs › ${name} › ${s.topic_label}`, itemListElement: [
        { "@type": "ListItem", position: 1, name: "Specs", item: `${SITE_URL}/specs` },
        { "@type": "ListItem", position: 2, name },
        { "@type": "ListItem", position: 3, name: s.topic_label, item: url }] },
      { "@type": "Article", "@id": `${url}#article`, headline: s.title, description: s.meta_desc, mainEntityOfPage: url,
        ...(s.published_at ? { datePublished: s.published_at } : {}), dateModified: p.reviewed,
        author: { "@type": "Person", name: author.name, url: `${SITE_URL}/about`, jobTitle: author.role },
        publisher: { "@id": `${SITE_URL}/#organization` },
        citation: p.sources.map(([label, u]) => ({ "@type": "CreativeWork", name: label, url: u })) },
      ...(s.faq.length ? [{ "@type": "FAQPage", mainEntity: s.faq.map(x => ({ "@type": "Question", name: x.q, acceptedAnswer: { "@type": "Answer", text: x.a } })) }] : []),
    ],
  };

  return (
    <article className="art spec">
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />
      <div className="crumbs"><Link href="/specs">Specs</Link> › {name} › {s.topic_label}</div>
      <h1>{s.title}</h1>
      <section className="short-answer" aria-label="Short answer"><strong>Short answer:</strong> {p.answer}</section>
      <div className="byline">
        By <Link href="/about">{author.name}</Link> · {author.role} · Last reviewed {fmtDate(p.reviewed)} · Covers: {p.covers}
      </div>
      <p className="fit-years">Every figure below is copied from {s.make_name}&apos;s own published specifications; the number after each row links to its source. We did not measure or test the vehicle. Your owner&apos;s manual and the labels on your own vehicle override this page.</p>
      {p.not_covered && <p className="muted" style={{ fontSize: 14 }}><strong>Not covered yet:</strong> {p.not_covered}</p>}

      {p.sections.length > 1 && (
        <nav className="toc-box"><strong>On this page</strong><ol>
          {p.sections.map(x => <li key={x.id}><a href={`#${x.id}`}>{x.h}</a></li>)}
          <li><a href="#check">Check your own {s.model_name}</a></li>
          {s.faq.length > 0 && <li><a href="#faq">FAQ</a></li>}
          <li><a href="#sources">Sources</a></li>
        </ol></nav>
      )}

      {p.sections.map(sec => (
        <section key={sec.id} id={sec.id}>
          <h2>{sec.h}</h2>
          {sec.intro && <p>{sec.intro}</p>}
          <div className="tbl"><table>
            <thead><tr>{sec.table.head.map(h => <th key={h}>{h}</th>)}<th className="src-col">Source</th></tr></thead>
            <tbody>{sec.table.rows.map((r, i) => (
              <tr key={i}>
                {r.slice(0, -1).map((c, j) => <td key={j}>{j === 0 ? <strong>{c as string}</strong> : (c as string)}</td>)}
                <td className="src-col">{srcList(r).map((n, k) => <span key={n}>{k > 0 && " "}<a href={`#src-${n}`} aria-label={`Source ${n}`}>[{n}]</a></span>)}</td>
              </tr>))}
            </tbody>
          </table></div>
          {sec.notes?.map(n => <p key={n} className="muted" style={{ fontSize: 14 }}>{n}</p>)}
        </section>
      ))}

      <section id="check">
        <h2>Check your own {s.model_name}</h2>
        <ul>{p.check.map(c => <li key={c}>{c}</li>)}</ul>
      </section>

      {(guides.length > 0 || hubs.length > 0) && (
        <section id="parts">
          <h2>Parts that depend on this</h2>
          {guides.length > 0 && <div className="grid">{guides.map(g => (
            <Link key={g.path} href={g.path} className="card"><div className="muted" style={{ fontSize: 12 }}>{g.category_name} · {g.vehicle}</div><h3 style={{ marginTop: 4 }}>{g.title}</h3></Link>))}</div>}
          {hubs.length > 0 && <p style={{ fontSize: 15 }}>Everything that fits: {hubs.map((h, i) => <span key={h.path}>{i > 0 && " · "}<Link href={h.path}>{h.label}</Link></span>)}</p>}
        </section>
      )}

      {others.length > 0 && (
        <section><h2>More {name} specs</h2>
          <ul className="plain-links">{others.map(o => <li key={o.topic}><Link href={specPath(o)}>{name} {o.topic_label.toLowerCase()}</Link></li>)}</ul>
        </section>
      )}

      {elsewhere.length > 0 && (
        <section><h2>{s.topic_label} of other models</h2>
          <ul className="plain-links">{elsewhere.map(o => <li key={specPath(o)}><Link href={specPath(o)}>{o.make_name} {o.model_name} {o.topic_label.toLowerCase()}</Link></li>)}</ul>
        </section>
      )}

      {s.faq.length > 0 && (
        <section id="faq"><h2>Frequently asked questions</h2>
          {s.faq.map(x => <details key={x.q} className="faq"><summary>{x.q}</summary><p>{x.a}</p></details>)}
        </section>
      )}

      <section className="method" id="sources">
        <h3>Sources</h3>
        <ol className="sources">{p.sources.map(([label, u], i) => <li key={u} id={`src-${i + 1}`}><a href={u} rel="nofollow noopener" target="_blank">{label}</a></li>)}</ol>
        <p>Found a figure that does not match your owner&apos;s manual? Email <a href={`mailto:${CONTACT_EMAIL}?subject=${encodeURIComponent(`Spec correction: ${name} ${s.topic_label}`)}`}>{CONTACT_EMAIL}</a> with the model year and a photo of the page or label, and we will correct it.</p>
      </section>
      <AuthorBox />
    </article>
  );
}
