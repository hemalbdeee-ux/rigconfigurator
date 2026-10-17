import Link from "next/link";
import type { Metadata } from "next";
import { CONTACT_EMAIL } from "@/lib/db";

const UPDATED = "October 15, 2026";

export const metadata: Metadata = {
  title: "Privacy Policy",
  description: "What Rig Configurator records when you visit or click an Amazon link, what Amazon records, and how to contact us about your data.",
  alternates: { canonical: "/privacy" },
};

export default function Privacy() {
  return (
    <article className="art">
      <h1>Privacy Policy</h1>
      <p className="muted">Last updated {UPDATED}</p>
      <p>Rig Configurator (&ldquo;we&rdquo;, &ldquo;us&rdquo;) runs rigconfigurator.com, a site that matches truck and SUV accessories to specific vehicles. This page explains what we collect when you use the site. The short version: there are no accounts, no forms and no advertising trackers. We record basic server logs, anonymous clicks on our Amazon links, and site usage statistics through Google Analytics.</p>

      <h2>What we collect</h2>
      <h3>Server logs</h3>
      <p>Like almost every website, our web server records standard request data: IP address, browser user agent, the page requested, the referring page and the time. We use these logs to keep the site running, to debug errors and to block abuse. They are not used to profile visitors and are not shared or sold.</p>
      <h3>Clicks on Amazon links</h3>
      <p>Buttons such as &ldquo;Check price on Amazon&rdquo; go through a short redirect on our site (<code>/go/…</code>) before sending you to Amazon. When that happens we save the product, the page you were on, which button you clicked, your browser&apos;s user agent string and, if our network provider supplies it, your country. <strong>We do not save your IP address or any identifier with this click record.</strong> We use it to see which guides and products people find useful.</p>
      <h3>Google Analytics</h3>
      <p>We use Google Analytics 4 to understand how visitors use the site, for example which pages are read, how people arrive and roughly where they are. Google Analytics sets first-party cookies (such as <code>_ga</code>) and collects data such as pages viewed, device and browser type, approximate location and referring site. Google processes this data under the <a href="https://policies.google.com/privacy" rel="nofollow noopener" target="_blank">Google Privacy Policy</a>. We do not use it for advertising and do not send names, email addresses or other personal details to Google. You can opt out with the <a href="https://tools.google.com/dlpage/gaoptout" rel="nofollow noopener" target="_blank">Google Analytics opt-out browser add-on</a> or by blocking cookies.</p>
      <h3>What we do not collect</h3>
      <p>We do not use advertising pixels. We do not ask for your name, email address or payment details, and we do not sell or rent personal information.</p>

      <h2>Amazon and other third parties</h2>
      <p>Rig Configurator is a participant in the Amazon Services LLC Associates Program. When you follow one of our links to Amazon, Amazon may set cookies to record that you came from our site, so it can credit us with a commission if you buy. Once you are on Amazon, <a href="https://www.amazon.com/gp/help/customer/display.html?nodeId=GX7NJQ4ZB8MHFRNJ" rel="nofollow noopener" target="_blank">Amazon&apos;s Privacy Notice</a> applies, not this one. Amazon tells us about qualifying purchases in aggregate reports; it does not tell us who you are.</p>
      <p>Some product photos are loaded directly from Amazon&apos;s image servers, which means your browser contacts Amazon to fetch them. Links to manufacturer sites and sources in our guides open those sites under their own privacy policies.</p>
      <p>Some guides show install videos from YouTube and owner posts from Reddit through those platforms&apos; own embeds. A YouTube video loads from youtube-nocookie.com only when you press play; a Reddit post loads Reddit&apos;s embed script when the page opens. Once loaded, those services apply their own privacy policies.</p>

      <h2>How long we keep data</h2>
      <p>Server logs are kept only as long as needed for security and troubleshooting, and are then deleted or rotated. Click records contain no personal identifiers and may be kept to compare page performance over time.</p>

      <h2>Your choices and rights</h2>
      <p>You can block or delete cookies in your browser, including Amazon&apos;s, at any time. Depending on where you live, for example the EU, UK or California, you may have the right to ask what personal data we hold about you, to have it corrected or deleted, or to object to its use. Because we don&apos;t link click records or analytics data to named individuals, in most cases we will have nothing that identifies you, but we will answer every request. Write to <a href={`mailto:${CONTACT_EMAIL}`}>{CONTACT_EMAIL}</a>.</p>

      <h2>Children</h2>
      <p>The site is written for adult vehicle owners. It is not directed at children under 13, and we do not knowingly collect information from them.</p>

      <h2>Security</h2>
      <p>The site is served only over HTTPS. Logs and the database are held on a private server that is not publicly reachable.</p>

      <h2>Changes to this policy</h2>
      <p>If we change what we collect, we will update this page and the date at the top.</p>

      <h2>Contact</h2>
      <p>Questions about privacy: <a href={`mailto:${CONTACT_EMAIL}`}>{CONTACT_EMAIL}</a>. See also our <Link href="/terms">Terms of Use</Link> and <Link href="/disclosure">Affiliate Disclosure</Link>.</p>
    </article>
  );
}
