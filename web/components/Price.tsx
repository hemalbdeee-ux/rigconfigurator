import Link from "next/link";
import type { Fit } from "@/lib/queries";

// Amazon Associates Program Policies: a price that comes from the Creators API is labelled as Amazon's price, and one that and is refreshed less often than
// hourly needs a date/time stamp next to it, plus the price disclaimer (here via the "Details" link), and has to
// link to the Amazon page. v_fitment only returns price_cents while it is under 23 hours old.
function stamp(at: string | Date) {
  const d = new Date(at), p = (n: number) => String(n).padStart(2, "0");
  return `${p(d.getUTCMonth() + 1)}/${p(d.getUTCDate())}/${d.getUTCFullYear()} ${p(d.getUTCHours())}:${p(d.getUTCMinutes())} UTC`;
}

export function Price({ f, href }: { f: Fit; href: string }) {
  if (!f.price_cents || !f.price_checked_at) return <>{f.price_band ?? "See price on Amazon"}</>;
  return (
    <>
      <a href={href} rel="nofollow sponsored noopener" target="_blank" className="price-live"><span className="price-src">Amazon price</span> ${(f.price_cents / 100).toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</a>
      <span className="price-asof"> (as of {stamp(f.price_checked_at)} · <Link href="/disclosure#prices">Details</Link>)</span>
    </>
  );
}
