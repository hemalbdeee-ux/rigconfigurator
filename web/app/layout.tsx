import type { Metadata } from "next";
import Link from "next/link";
import Script from "next/script";
import "./globals.css";
import { SITE_URL } from "@/lib/db";
import { DEFAULT_OG } from "@/components/Hero";

const GA_ID = "G-ETSZ9MSTVN";

export const metadata: Metadata = {
  metadataBase: new URL(SITE_URL),
  title: { default: "Rig Configurator: Fit-Checked Truck & SUV Accessories", template: "%s | Rig Configurator" },
  description: "Pick your vehicle, see only the racks, hitches, tonneau covers and gear that actually fit. Verified against manufacturer fit guides.",
  openGraph: { siteName: "Rig Configurator", type: "website", locale: "en_US", images: DEFAULT_OG },
  twitter: { card: "summary_large_image" },
  // Pinterest domain claim (social plan): renders <meta name="p:domain_verify" ...> in every page head.
  other: { "p:domain_verify": "7cb436579f1a8cd3c2a593f2d4711aa6" },
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <header className="nav">
          <Link href="/" className="brand">Rig<span>Configurator</span></Link>
          <nav>
            <Link href="/build">Build</Link>
            <Link href="/vehicles">Vehicles</Link>
            <Link href="/guides">Guides</Link>
            <Link href="/learn">Learn</Link>
            <Link href="/tools">Tools</Link>
            <Link href="/deals">Deals</Link>
          </nav>
        </header>
        <main className="wrap">{children}</main>
        <footer className="foot">
          <p>As an Amazon Associate we earn from qualifying purchases. Fit data is verified against manufacturer fit guides; always confirm on the retailer page before buying.</p>
          <p style={{ fontSize: 12 }}>CERTAIN CONTENT THAT APPEARS ON THIS SITE COMES FROM AMAZON. THIS CONTENT IS PROVIDED &lsquo;AS IS&rsquo; AND IS SUBJECT TO CHANGE OR REMOVAL AT ANY TIME.</p>
          <p><Link href="/about">About</Link> · <Link href="/disclosure">Affiliate disclosure</Link> · <Link href="/privacy">Privacy</Link> · <Link href="/terms">Terms</Link></p>
        </footer>
        {/* GA4 loads after the page is idle: it was the largest script and its <head> preload competed with the hero image and CSS. */}
        <Script src={`https://www.googletagmanager.com/gtag/js?id=${GA_ID}`} strategy="lazyOnload" />
        <Script id="ga4" strategy="lazyOnload">
          {`window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', '${GA_ID}');`}
        </Script>
        {/* Field Web Vitals (LCP, INP, CLS) as GA4 events, so INP has data before CrUX does. */}
        <Script id="web-vitals" strategy="lazyOnload">
          {`import('https://unpkg.com/web-vitals@4.2.4/dist/web-vitals.attribution.js').then(function(m){function s(x){if(window.gtag)gtag('event',x.name,{value:Math.round(x.name==='CLS'?x.delta*1000:x.delta),metric_id:x.id,metric_value:x.value,metric_rating:x.rating,non_interaction:true});}m.onLCP(s);m.onINP(s);m.onCLS(s);}).catch(function(){});`}
        </Script>
      </body>
    </html>
  );
}
