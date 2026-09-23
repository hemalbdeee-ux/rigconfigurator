import type { Metadata } from "next";
import Link from "next/link";
import "./globals.css";
import { SITE_URL } from "@/lib/db";

export const metadata: Metadata = {
  metadataBase: new URL(SITE_URL),
  title: { default: "Rig Configurator — Fit-checked parts for your truck, SUV & overland rig", template: "%s | Rig Configurator" },
  description: "Pick your vehicle, see only the racks, hitches, tonneau covers and gear that actually fit. Verified against manufacturer fit guides.",
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
            <Link href="/tools">Tools</Link>
            <Link href="/deals">Deals</Link>
            <Link href="/laws">Laws</Link>
          </nav>
        </header>
        <main className="wrap">{children}</main>
        <footer className="foot">
          <p>As an Amazon Associate we earn from qualifying purchases. Fit data is verified against manufacturer fit guides; always confirm on the retailer page before buying.</p>
          <p><Link href="/about">About</Link> · <Link href="/disclosure">Affiliate disclosure</Link> · <Link href="/privacy">Privacy</Link> · <Link href="/terms">Terms</Link></p>
        </footer>
      </body>
    </html>
  );
}
