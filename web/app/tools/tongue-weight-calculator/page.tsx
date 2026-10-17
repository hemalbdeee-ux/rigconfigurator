import type { Metadata } from "next";
import Link from "next/link";
import { SITE_URL } from "@/lib/db";
import { staticOg } from "@/components/Hero";
import { TongueCalc } from "@/components/Calculators";
import { CiteBox } from "@/components/CiteBox";
import { calcVehicles } from "@/lib/toolVehicles";

export const dynamic = "force-dynamic";
const PATH = "/tools/tongue-weight-calculator";
const TITLE = "Tongue Weight Calculator by Vehicle";
const DESC = "Work out the right tongue weight for a trailer, or the load a hitch bike rack puts on your receiver, and check it against your truck or SUV's published limits.";

export const metadata: Metadata = {
  title: { absolute: `${TITLE} | Rig Configurator` },
  description: DESC,
  alternates: { canonical: PATH },
  openGraph: { title: TITLE, description: DESC, url: PATH, type: "website", images: staticOg("guide-hitches", TITLE) },
};

const FAQ: [string, string][] = [
  ["How do you calculate tongue weight?", "Multiply the loaded trailer weight by 0.10 and by 0.15. A 5,000 lb trailer should put about 500 to 750 lb on the ball. The range keeps a conventional trailer stable: under 10 percent tends to sway, over 15 percent loads the rear axle and the hitch too much. Weigh it to be sure; a tongue scale or a truck-stop scale gives the real figure."],
  ["Does a hitch bike rack count as tongue weight?", "Yes, all of it. A platform rack and the bikes on it press straight down on the receiver, and because the load sits well behind the bumper it adds leverage too. Two e-bikes on a heavy platform rack can pass 150 lb, which is the whole tongue limit on some small SUVs."],
  ["Where do I find my vehicle's tongue weight limit?", "In the towing section of the owner's manual and on the label of the hitch receiver. Use the lower of the two. Many makers print a tow rating but no separate tongue figure on their websites, which is why this calculator lets you type the figure from your manual."],
  ["Is the hitch class the same as my vehicle's limit?", "No. The class describes what the receiver can carry; the vehicle has its own rating, and the lower one is your limit. A Class IV receiver on a vehicle rated for 5,000 lb is still a 5,000 lb setup."],
  ["Where do the vehicle figures come from?", "From our factory tow hitch chart, which lists the maker or dealer page behind every figure and says when a figure could not be confirmed. The calculator shows that chart note next to each result."],
];

export default async function Page() {
  const vehicles = await calcVehicles();
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
      <div className="crumbs"><Link href="/tools">Tools</Link> › Tongue weight calculator</div>
      <h1>{TITLE}</h1>
      <p className="dek">Pick your truck or SUV, then enter a trailer weight or a hitch carrier load. The calculator gives the tongue weight to aim for and checks it against the figures in our <Link href="/learn/factory-tow-hitch-by-vehicle">factory tow hitch chart</Link>.</p>
      <TongueCalc vehicles={vehicles} />
      <h2>How the numbers work</h2>
      <p><strong>Trailers.</strong> Tongue weight is the downward push of the trailer coupler on the ball. The usual target is 10 to 15 percent of the loaded trailer, so load heavy items slightly ahead of the trailer axle. Check two limits: the vehicle&apos;s tow rating for the trailer, and the tongue limit for the coupler load. The lowest rating in the chain wins: vehicle, receiver, ball mount, ball and coupler.</p>
      <p><strong>Hitch carriers.</strong> A bike rack or cargo carrier puts its entire weight, plus the load, on the receiver. Makers that publish a separate carrier limit, such as Tesla for the Model Y and Model 3, set it below the trailer tongue figure; our chart quotes those figures where we found them.</p>
      <p><strong>When there is no figure.</strong> For most vehicles in our chart the maker prints no tongue limit on its public pages. That is not a zero; it means the number is in the owner&apos;s manual or on the hitch label. Type it into the optional field and the check runs on your figure.</p>
      <h2>Frequently asked questions</h2>
      {FAQ.map(([q, a]) => <details key={q} className="faq"><summary>{q}</summary><p>{a}</p></details>)}
      <p className="muted" style={{ fontSize: 13 }}>This calculator is a planning aid, not a safety certification. Your owner&apos;s manual and the labels on the hitch and trailer are the authority for your exact build.</p>
      <p><Link href="/learn/trailer-hitch-classes-explained">Trailer hitch classes explained →</Link> · <Link href="/guides/hitches">Hitches by vehicle →</Link> · <Link href="/tools/roof-load-calculator">Roof load calculator →</Link></p>
      <CiteBox url={`${SITE_URL}${PATH}`} name={TITLE} />
    </article>
  );
}
