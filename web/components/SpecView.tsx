import Link from "next/link";
import { CONTACT_EMAIL, SITE_URL } from "@/lib/db";
import { allCharts, allSpecs, genSpecsForModel, guidesForModel, hubsForModel, sameTopicElsewhere, specPath, specsForModel, type SpecLink, type SpecPage, type SpecRow } from "@/lib/specs";
import { getAuthor } from "@/lib/authors";
import { AuthorBox, fmtDate } from "@/components/PillarParts";

/** One renderer for the three kinds of spec page: model (/specs/…), generation (/vehicles/…/specs/…) and chart (/learn/…). */
const srcList = (r: SpecRow): number[] => { const x = r[r.length - 1]; return Array.isArray(x) ? x : [x as number]; };
const LinkList = ({ items }: { items: { path: string; label: string }[] }) => (
  <ul className="plain-links">{items.map(o => <li key={o.path}><Link href={o.path}>{o.label}</Link></li>)}</ul>);
const label = (o: SpecLink) => o.kind === "chart" ? o.title
  : `${o.kind === "generation" && o.gen_label ? o.gen_label + " " : ""}${o.make_name} ${o.model_name} ${o.topic_label.toLowerCase()}`;
const links = (list: SpecLink[]) => list.map(o => ({ path: specPath(o), label: label(o) }));

export async function SpecView({ s }: { s: SpecPage }) {
  const p = s.page, path = specPath(s), url = `${SITE_URL}${path}`;
  const isGen = s.kind === "generation", isChart = s.kind === "chart";
  const model = `${s.make_name} ${s.model_name}`;
  const name = isChart ? s.topic_label : isGen ? `${p.gen_label ?? ""} ${model}`.trim() : model;
  const author = getAuthor();

  // Link blocks. Every list holds live pages only, so a page never links to something that is not published yet.
  const [guidesAll, hubsAll, modelSpecs, genSpecs, elsewhere, charts, everyModel] = await Promise.all([
    isChart ? [] : guidesForModel(s.make_slug, s.model_slug, p.related ?? []),
    isChart ? [] : hubsForModel(s.make_slug, s.model_slug),
    isChart ? [] : specsForModel(s.make_slug, s.model_slug),
    isChart ? [] : genSpecsForModel(s.make_slug, s.model_slug),
    isChart ? [] : sameTopicElsewhere(s),
    allCharts(), isChart ? allSpecs() : []]);
  const guides = isGen ? guidesAll.filter(g => g.path.includes(`/${s.gen_slug}/`)) : guidesAll;
  const hubs = isGen ? hubsAll.filter(h => h.path.endsWith(`/${s.gen_slug}`)) : hubsAll;
  const thisGen = genSpecs.filter(x => x.gen_slug === s.gen_slug && x.topic !== s.topic);                 // other specs, same generation
  const otherGens = genSpecs.filter(x => x.topic === s.topic && x.gen_slug !== s.gen_slug);               // same spec, other generations
  const allYears = modelSpecs.filter(x => x.topic === s.topic);                                           // the model-level page of this spec
  const moreModel = modelSpecs.filter(x => x.topic !== s.topic);
  const gensOfTopic = isGen ? [] : genSpecs.filter(x => x.topic === s.topic);                             // model page → its year-by-year pages
  const topicCharts = charts.filter(c => c.topic === s.topic && specPath(c) !== path);
  const live = new Set(everyModel.map(specPath));
  const years = Object.entries(p.years ?? {}).sort(([a], [b]) => Number(b) - Number(a));

  const crumbs = isChart ? [{ name: "Learn", item: "/learn" }, { name: s.title.split(":")[0] }]
    : isGen ? [{ name: "Vehicles", item: "/vehicles" }, ...(hubs[0] ? [{ name: `${p.gen_label ?? ""} ${model}`.trim(), item: hubs[0].path }] : [{ name: model }]), { name: s.topic_label }]
    : [{ name: "Specs", item: "/specs" }, { name: model }, { name: s.topic_label }];
  const jsonLd = {
    "@context": "https://schema.org",
    "@graph": [
      { "@type": "Organization", "@id": `${SITE_URL}/#organization`, name: "Rig Configurator", url: SITE_URL,
        logo: { "@type": "ImageObject", url: `${SITE_URL}/logo.png`, contentUrl: `${SITE_URL}/logo.png`, width: 600, height: 120 } },
      { "@type": "BreadcrumbList", "@id": `${url}#breadcrumb`, name: crumbs.map(c => c.name).join(" › "),
        itemListElement: crumbs.map((c, i) => ({ "@type": "ListItem", position: i + 1, name: c.name, ...("item" in c && c.item ? { item: `${SITE_URL}${c.item}` } : i === crumbs.length - 1 ? { item: url } : {}) })) },
      { "@type": "Article", "@id": `${url}#article`, headline: s.title, description: s.meta_desc, mainEntityOfPage: url,
        ...(s.published_at ? { datePublished: s.published_at } : {}), dateModified: p.reviewed,
        author: { "@type": "Person", name: author.name, url: `${SITE_URL}/about`, jobTitle: author.role },
        publisher: { "@id": `${SITE_URL}/#organization` },
        citation: p.sources.map(([l, u]) => ({ "@type": "CreativeWork", name: l, url: u })) },
      ...(s.faq.length ? [{ "@type": "FAQPage", mainEntity: s.faq.map(x => ({ "@type": "Question", name: x.q, acceptedAnswer: { "@type": "Answer", text: x.a } })) }] : []),
    ],
  };

  return (
    <article className="art spec">
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />
      <div className="crumbs">{crumbs.map((c, i) => <span key={c.name}>{i > 0 && " › "}{"item" in c && c.item ? <Link href={c.item}>{c.name}</Link> : c.name}</span>)}</div>
      <h1>{s.title}</h1>
      <section className="short-answer" aria-label="Short answer"><strong>Short answer:</strong> {p.answer}</section>
      <div className="byline">
        By <Link href="/about">{author.name}</Link> · {author.role} · Last reviewed {fmtDate(p.reviewed)} · Covers: {p.covers}
      </div>
      <p className="fit-years">Every figure below is copied from {isChart ? "each maker's" : `${s.make_name}'s`} own published specifications; the number after each row links to its source. We did not measure or test {isChart ? "these vehicles" : "the vehicle"}. Your owner&apos;s manual and the labels on your own vehicle override this page.</p>
      {p.not_covered && <p className="muted" style={{ fontSize: 14 }}><strong>Not covered yet:</strong> {p.not_covered}</p>}

      {years.length > 0 && (
        <nav className="year-pick" aria-label="Pick your model year"><strong>Your model year:</strong>
          {years.map(([y, id]) => <a key={y} href={`#${id}`}>{y}</a>)}
        </nav>
      )}

      {p.sections.length > 1 && (
        <nav className="toc-box"><strong>On this page</strong><ol>
          {p.sections.map(x => <li key={x.id}><a href={`#${x.id}`}>{x.h}</a></li>)}
          <li><a href="#check">{isChart ? "How to use this chart" : `Check your own ${s.model_name}`}</a></li>
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
                {r.slice(0, -1).map((c, j) => {
                  const to = j === 0 ? p.links?.[c as string] : undefined;      // chart rows link to the vehicle's own page once it is live
                  return <td key={j}>{j === 0 ? <strong>{to && live.has(to) ? <Link href={to}>{c as string}</Link> : (c as string)}</strong> : (c as string)}</td>;
                })}
                <td className="src-col">{srcList(r).map((n, k) => <span key={n}>{k > 0 && " "}<a href={`#src-${n}`} aria-label={`Source ${n}`}>[{n}]</a></span>)}</td>
              </tr>))}
            </tbody>
          </table></div>
          {sec.notes?.map(n => <p key={n} className="muted" style={{ fontSize: 14 }}>{n}</p>)}
        </section>
      ))}

      <section id="check">
        <h2>{isChart ? "How to use this chart" : `Check your own ${s.model_name}`}</h2>
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

      {isGen && thisGen.length > 0 && <section><h2>More {name} specs</h2><LinkList items={links(thisGen)} /></section>}
      {isGen && (otherGens.length > 0 || allYears.length > 0) && (
        <section><h2>{s.topic_label} of other {s.model_name} years</h2><LinkList items={[...links(otherGens), ...allYears.map(o => ({ path: specPath(o), label: `${model} ${o.topic_label.toLowerCase()}, all years` }))]} /></section>)}
      {!isGen && !isChart && gensOfTopic.length > 0 && <section><h2>{s.topic_label} by model year</h2><LinkList items={links(gensOfTopic)} /></section>}
      {!isChart && moreModel.length > 0 && <section><h2>{isGen ? `${model} specs, all years` : `More ${model} specs`}</h2><LinkList items={links(moreModel)} /></section>}
      {elsewhere.length > 0 && <section><h2>{s.topic_label} of other models</h2><LinkList items={links(elsewhere)} /></section>}
      {topicCharts.length > 0 && <section><h2>{isChart ? "Related charts" : "Compare with other vehicles"}</h2><LinkList items={links(topicCharts)} /></section>}

      {s.faq.length > 0 && (
        <section id="faq"><h2>Frequently asked questions</h2>
          {s.faq.map(x => <details key={x.q} className="faq"><summary>{x.q}</summary><p>{x.a}</p></details>)}
        </section>
      )}

      <section className="method" id="sources">
        <h3>Sources</h3>
        <ol className="sources">{p.sources.map(([l, u], i) => <li key={u} id={`src-${i + 1}`}><a href={u} rel="nofollow noopener" target="_blank">{l}</a></li>)}</ol>
        <p>Found a figure that does not match your owner&apos;s manual? Email <a href={`mailto:${CONTACT_EMAIL}?subject=${encodeURIComponent(`Spec correction: ${name} ${isChart ? "" : s.topic_label}`.trim())}`}>{CONTACT_EMAIL}</a> with the model year and a photo of the page or label, and we will correct it.</p>
      </section>
      <AuthorBox />
    </article>
  );
}
