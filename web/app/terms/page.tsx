import Link from "next/link";
import type { Metadata } from "next";
import { CONTACT_EMAIL } from "@/lib/db";

const UPDATED = "September 25, 2026";

export const metadata: Metadata = {
  title: "Terms of Use",
  description: "The terms for using Rig Configurator: fitment information is a guide, confirm on the retailer listing, and how affiliate links and content use work.",
  alternates: { canonical: "/terms" },
};

export default function Terms() {
  return (
    <article className="art">
      <h1>Terms of Use</h1>
      <p className="muted">Last updated {UPDATED}</p>
      <p>These terms apply to rigconfigurator.com (&ldquo;the site&rdquo;), run by Rig Configurator (&ldquo;we&rdquo;, &ldquo;us&rdquo;). By using the site you agree to them. If you don&apos;t agree, please don&apos;t use the site.</p>

      <h2>Fitment information is a guide</h2>
      <p>We match products to vehicles using manufacturer fit guides, part-number listings, retailer listings and owner reports. Manufacturers change parts between model years, trims, cabs, bed lengths and option packages, and listings change without notice. <strong>Always confirm fitment on the retailer&apos;s or manufacturer&apos;s page for your exact vehicle before you buy.</strong> Where we are unsure, the page says &ldquo;confirm fit on listing&rdquo;.</p>
      <p>Tow ratings, roof loads, receiver classes and similar figures on the site are summaries. The limits in your vehicle&apos;s owner&apos;s manual and on the product&apos;s label or instructions always take priority. Follow the manufacturer&apos;s installation instructions and torque specs, and use a professional installer if you are not sure.</p>

      <h2>No warranty</h2>
      <p>The site is provided &ldquo;as is&rdquo; and &ldquo;as available&rdquo;. We work to keep it accurate, but we do not warrant that any information, price or availability is complete, current or error-free. Prices and availability are set by the retailer and may differ from what we show.</p>

      <h2>Limitation of liability</h2>
      <p>To the fullest extent the law allows, Rig Configurator is not liable for any indirect, incidental or consequential loss, or for damage to vehicles or property, arising from use of the site or from products bought through it. Products are sold by third-party retailers, and their terms, returns and warranties apply to your purchase. Nothing in these terms limits rights you have under consumer law that cannot be excluded.</p>

      <h2>Affiliate links</h2>
      <p>Many links to Amazon on the site are affiliate links, and we may earn a commission on qualifying purchases at no extra cost to you. Details are in our <Link href="/disclosure">Affiliate Disclosure</Link>. Product names, logos and trademarks belong to their owners. We are not affiliated with or endorsed by any vehicle or accessory manufacturer.</p>

      <h2>Using our content</h2>
      <p>The guides, tables and fitment data on the site are our work and are protected by copyright. You may read, print and share links to pages for personal, non-commercial use. You may not copy, republish or scrape the content or fitment data in bulk, or use it to build a competing database, without written permission.</p>

      <h2>Acceptable use</h2>
      <p>Don&apos;t try to disrupt the site, get around its security, or overload it with automated requests. We may block access that looks abusive.</p>

      <h2>Links to other sites</h2>
      <p>We link to retailers, manufacturers and sources we cite. We don&apos;t control those sites and aren&apos;t responsible for their content, prices or policies.</p>

      <h2>Privacy</h2>
      <p>How we handle data is covered in our <Link href="/privacy">Privacy Policy</Link>.</p>

      <h2>Changes</h2>
      <p>We may update these terms. The date at the top shows when they last changed. If you keep using the site after a change, the new terms apply.</p>

      <h2>Contact</h2>
      <p>Found a fitment error or have a question about these terms? Email <a href={`mailto:${CONTACT_EMAIL}`}>{CONTACT_EMAIL}</a> with the year, trim and part number if it&apos;s about a product.</p>
    </article>
  );
}
