import type { Metadata } from "next";
import Link from "next/link";
import { staticOg } from "@/components/Hero";
import { allVehicles, categoriesFor, fitsFor, getVehicleById, pagesFor, vehiclePath, vehicleTitle } from "@/lib/queries";
import { VehiclePicker } from "@/components/VehiclePicker";
import { Builder, type BuildSlot } from "@/components/Builder";

export const dynamic = "force-dynamic";

export async function generateMetadata({ searchParams }: { searchParams: Promise<{ vehicle?: string }> }): Promise<Metadata> {
  const v = await getVehicleById(Number((await searchParams).vehicle));
  const title = v ? `Build Your ${vehicleTitle(v)} Setup` : "Build Your Truck or SUV Setup";
  return {
    title,
    description: v
      ? `Pick fit-checked accessories for the ${vehicleTitle(v)} by category and see the live Amazon total.`
      : "Pick your vehicle, choose fit-checked accessories by category and see the live Amazon total.",
    alternates: { canonical: v ? `/build?vehicle=${v.id}` : "/build" },
    robots: v ? { index: false, follow: true } : undefined,   // one canonical builder page; vehicle states are tools, not landing pages
    openGraph: { title: `${title} | Rig Configurator`, url: "/build", type: "website", images: staticOg("vehicles", title) },
  };
}

export default async function Build({ searchParams }: { searchParams: Promise<{ vehicle?: string }> }) {
  const { vehicle } = await searchParams;
  const v = await getVehicleById(Number(vehicle));
  if (!v) {
    const vehicles = await allVehicles();
    return (
      <section className="tool-page">
        <h1>Build your setup</h1>
        <p className="dek">Pick a vehicle. The builder lists the top fit-checked pick in every category for that generation, lets you swap each one, and totals the live Amazon prices.</p>
        <VehiclePicker vehicles={vehicles.map(x => ({ make: x.make_name, label: vehicleTitle(x), path: `/build?vehicle=${x.id}` }))} compact cta="Start the build →" />
        <h2>How the builder works</h2>
        <ol>
          <li><strong>Pick the generation.</strong> {vehicles.length} truck and SUV generations are covered; each one has its own parts list, because a redesign changes beds, roof rails and mounting points.</li>
          <li><strong>Start from the top pick in each category.</strong> The builder opens with the first-ranked product from each of that vehicle&apos;s fit-checked guides and offers up to five alternatives per category.</li>
          <li><strong>Untick what you do not need and swap the rest.</strong> The total follows your choices.</li>
        </ol>
        <h2>What the total includes</h2>
        <p>The total adds up the Amazon prices we last fetched for the ticked products; each price carries its own time stamp, and Amazon&apos;s page is the final word. A product Amazon gave no price for shows a price band and is left out of the total, with a note saying so. Shipping, tax and installation are not included.</p>
        <p className="muted">Want the reasoning behind each pick first? <Link href="/vehicles">Open your vehicle&apos;s fit hub</Link> or <Link href="/guides">browse the guides by category</Link>.</p>
      </section>
    );
  }
  const [cats, fits, pages] = await Promise.all([categoriesFor(v.body_style), fitsFor(v.id), pagesFor(v.id)]);
  const published = new Set(pages.filter(p => p.status === "published").map(p => p.category_slug));
  const hub = vehiclePath(v);
  const slots: BuildSlot[] = cats
    .map(c => ({
      slug: c.slug, name: c.name, guide: published.has(c.slug) ? `${hub}/${c.slug}` : null,
      items: fits.filter(f => f.category_slug === c.slug).slice(0, 5).map(f => ({
        product_id: f.product_id, asin: f.asin, name: f.name, brand: f.brand, image_url: f.image_url,
        price_cents: f.price_cents, price_band: f.price_band, price_checked_at: f.price_checked_at ? new Date(f.price_checked_at).toISOString() : null,
        rank: f.rank, note: f.note,
      })),
    }))
    .filter(s => s.items.length > 0);
  return (
    <section className="tool-page wide">
      <div className="crumbs"><Link href="/build">Build</Link> › <Link href={hub}>{vehicleTitle(v)}</Link></div>
      <h1>Build your {vehicleTitle(v)}</h1>
      <p className="dek">Every product below is listed for this generation. Untick a category you do not need, swap a pick from its menu, and the Amazon total updates.</p>
      <div className="disclose">We earn a commission from qualifying Amazon purchases, at no extra cost to you. Prices labelled &ldquo;Amazon price&rdquo; come from Amazon and carry their own time stamp. <Link href="/disclosure">How we make money</Link>.</div>
      <Builder slots={slots} hub={hub} vehicleLabel={v.model_name} />
    </section>
  );
}
