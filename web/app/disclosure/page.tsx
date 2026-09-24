import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Affiliate Disclosure",
  description: "How Rig Configurator earns money from Amazon affiliate links, and how that does and doesn't affect our recommendations.",
  alternates: { canonical: "/disclosure" },
};

export default function Disclosure() {
  return (
    <article className="art">
      <h1>Affiliate Disclosure</h1>
      <p><strong>Rig Configurator is a participant in the Amazon Services LLC Associates Program, an affiliate advertising program designed to provide a means for sites to earn advertising fees by advertising and linking to Amazon.com.</strong> As an Amazon Associate we earn from qualifying purchases.</p>
      <p>When you click a &ldquo;Check price on Amazon&rdquo; or similar button and buy, we may receive a commission. The price you pay is the same.</p>
      <h2>What commissions do not change</h2>
      <p>Products are ranked on fitment, published specifications, warranty and owner reports. A product&apos;s commission rate is not a ranking factor, and we list products that fit even when they are sold elsewhere.</p>
      <h2>Prices</h2>
      <p>Prices shown are checked at the date on each page and change often. The price on Amazon at the time of purchase applies.</p>
      <p className="muted">Product names, logos and brands are property of their respective owners. Rig Configurator is not affiliated with or endorsed by any vehicle or accessory manufacturer.</p>
    </article>
  );
}
