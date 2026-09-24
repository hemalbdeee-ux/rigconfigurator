import Link from "next/link";
import type { Metadata } from "next";
import { AUTHORS } from "@/lib/authors";

export const metadata: Metadata = {
  title: "About Rig Configurator — How We Check Fitment",
  description: "Who runs Rig Configurator, how products are matched to each truck and SUV generation, and how the site makes money.",
  alternates: { canonical: "/about" },
};

export default function About() {
  const a = AUTHORS["md-hanzala"];
  return (
    <article className="art">
      <h1>About Rig Configurator</h1>
      <p className="dek">Rig Configurator answers one question before you buy a truck or SUV accessory: <strong>does it fit my exact vehicle?</strong></p>
      <h2>How we check fitment</h2>
      <p>Every product on the site is linked to a specific vehicle generation — for example the 2021–2026 Ford F-150 — and, where it matters, a bed length, cab, roof-rail type or trim. We build those links from the manufacturer&apos;s own fit guide and part-number listing, cross-checked against the retailer listing and owner reports on model-specific forums. When a listing is ambiguous we say so on the page (&ldquo;confirm on the listing&rdquo;) instead of guessing.</p>
      <h2>What we do not claim</h2>
      <p>Unless an article says it was installed and used by us, our picks are based on published specifications, fitment data and owner reports — not our own hands-on testing. Each long-form guide lists its sources and a &ldquo;How we chose&rdquo; note.</p>
      <h2>Who runs the site</h2>
      <section className="author">
        <div className="avatar">MH</div>
        <div><strong>{a.name}</strong> <span className="muted">· {a.role}</span><p style={{ margin: "4px 0" }}>{a.bio}</p>
          <div>{a.facts.map(x => <span key={x} className="pill">{x}</span>)}</div></div>
      </section>
      <h2>How the site makes money</h2>
      <p>We earn a commission when you buy through our Amazon links, at no extra cost to you. Commissions never change which product ranks where. Read the <Link href="/disclosure">affiliate disclosure</Link>.</p>
      <h2>Found a fitment error?</h2>
      <p>Fit data changes with model-year updates. If a product we list doesn&apos;t fit your vehicle, tell us the year, trim and part number and we&apos;ll correct the page.</p>
    </article>
  );
}
