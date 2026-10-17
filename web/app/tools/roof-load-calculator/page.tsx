import type { Metadata } from "next";
import Link from "next/link";
import { SITE_URL } from "@/lib/db";
import { staticOg } from "@/components/Hero";
import { RoofCalc } from "@/components/Calculators";
import { CiteBox } from "@/components/CiteBox";
import { calcVehicles } from "@/lib/toolVehicles";

export const dynamic = "force-dynamic";
const PATH = "/tools/roof-load-calculator";
const TITLE = "Roof Load Calculator for Racks, Boxes and Tents";
const DESC = "Add up crossbars, a cargo box or rooftop tent and the cargo, then check the total against your SUV's roof figure and the rack rating.";

export const metadata: Metadata = {
  title: { absolute: `${TITLE} | Rig Configurator` },
  description: DESC,
  alternates: { canonical: PATH },
  openGraph: { title: TITLE, description: DESC, url: PATH, type: "website", images: staticOg("guide-roof-racks", TITLE) },
};

const FAQ: [string, string][] = [
  ["What counts toward the roof load limit?", "Everything above the roof while you drive: the crossbars and feet or the platform, the cargo box, tent or bike mounts, and whatever is in or on them. A 15 lb set of bars and a 45 lb box leave only about 105 lb for cargo on a 165 lb roof."],
  ["Which limit applies, the vehicle or the rack?", "The lower one. A 300 lb crossbar on a roof rated 165 lb carries 165 lb, bars included. A 165 lb rack system on a roof rated 220 lb carries 165 lb."],
  ["What is the difference between dynamic and static roof load?", "Dynamic is the limit while moving, and it is the one that governs a cargo box or a tent on the road. Static is the parked limit, which matters for a rooftop tent with people inside. Only a few makers print a static figure; Subaru does for the Wilderness models."],
  ["Why do so many limits say 165 lb?", "165 lb is 75 kg, the standard rating Thule, Yakima and many rack makers print for a complete system. When a vehicle maker publishes no roof figure, that rack rating is often the only number available, which is why the calculator asks for the rack rating separately."],
  ["Where do the vehicle figures come from?", "From our roof load limits chart, which lists the source behind every figure and marks the ones the maker has not confirmed. The calculator shows that chart note under each result."],
];

export default async function Page() {
  const vehicles = (await calcVehicles()).filter(v => !/bare cab roof/i.test(v.roof?.roof_type ?? ""));
  const jsonLd = { "@context": "https://schema.org", "@graph": [
    { "@type": "BreadcrumbList", itemListElement: [
      { "@type": "ListItem", position: 1, name: "Tools", item: `${SITE_URL}/tools` },
      { "@type": "ListItem", position: 2, name: TITLE, item: `${SITE_URL}${PATH}` }] },
    { "@type": "WebApplication", name: TITLE, url: `${SITE_URL}${PATH}`, applicationCategory: "UtilitiesApplication", operatingSystem: "Any", offers: { "@type": "Offer", price: "0", priceCurrency: "USD" } },
    { "@type": "FAQPage", mainEntity: FAQ.map(([q, a]) => ({ "@type": "Question", name: q, acceptedAnswer: { "@type": "Answer", text: a } })) },
  ] };
  return (
    <article className="art tool-page">
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />
      <div className="crumbs"><Link href="/tools">Tools</Link> › Roof load calculator</div>
      <h1>{TITLE}</h1>
      <p className="dek">Pick your SUV, enter the weight of the bars, the box or tent and the cargo, and see how much of the limit you use. Vehicle figures come from our <Link href="/learn/roof-load-limits-by-vehicle">roof load limits chart</Link>; pickups are left out because their cab roofs have no published figure and the load belongs in the bed.</p>
      <RoofCalc vehicles={vehicles} />
      <h2>How the check works</h2>
      <p>The calculator adds the three weights and compares the total with the lower of two limits: the vehicle&apos;s roof figure and the rating of the rack system. Both limits apply at once, so the smaller one is the real ceiling. If our chart has no maker figure for your vehicle, it uses the rack rating alone and says so.</p>
      <p>Weights to expect: crossbars about 10 to 20 lb, a platform 40 to 60 lb, a cargo box 35 to 60 lb empty, and a hard-shell rooftop tent 100 lb or more. Check the listing of the exact product you own.</p>
      <h2>Frequently asked questions</h2>
      {FAQ.map(([q, a]) => <details key={q} className="faq"><summary>{q}</summary><p>{a}</p></details>)}
      <p className="muted" style={{ fontSize: 13 }}>This calculator is a planning aid, not a safety certification. Your owner&apos;s manual and the rack maker&apos;s instructions are the authority for your exact vehicle.</p>
      <p><Link href="/learn/roof-rail-types-explained">Roof rail types explained →</Link> · <Link href="/guides/roof-racks">Roof racks by vehicle →</Link> · <Link href="/tools/tongue-weight-calculator">Tongue weight calculator →</Link></p>
      <CiteBox url={`${SITE_URL}${PATH}`} name={TITLE} />
    </article>
  );
}
