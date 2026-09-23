import Link from "next/link";
import { notFound } from "next/navigation";
import type { Metadata } from "next";
import { allVehicles, categoriesFor, fitsFor, getVehicle, vehiclePath, vehicleTitle, yearsLabel } from "@/lib/queries";

export const revalidate = 3600;
type P = { make: string; model: string; gen: string };

export async function generateStaticParams() {
  const vs = await allVehicles();
  return vs.map(v => ({ make: v.make_slug, model: v.model_slug, gen: v.gen_slug }));
}

export async function generateMetadata({ params }: { params: Promise<P> }): Promise<Metadata> {
  const { make, model, gen } = await params;
  const v = await getVehicle(make, model, gen);
  if (!v) return {};
  return {
    title: `${vehicleTitle(v)} Accessories That Fit — Racks, Hitches, Covers & Mats`,
    description: `Fit facts for the ${vehicleTitle(v)} (${v.gen_name}) and every accessory verified to fit it.`,
    alternates: { canonical: vehiclePath(v) },
  };
}

export default async function VehicleHub({ params }: { params: Promise<P> }) {
  const { make, model, gen } = await params;
  const v = await getVehicle(make, model, gen);
  if (!v) notFound();
  const [cats, fits] = await Promise.all([categoriesFor(v.body_style), fitsFor(v.id)]);
  const countBy = Object.fromEntries(cats.map(c => [c.slug, fits.filter(f => f.category_slug === c.slug).length]));

  const facts: [string, string | null][] = [
    ["Generation", v.gen_name], ["Years", yearsLabel(v)], ["Body", v.body_style],
    ["Bed lengths", v.bed_lengths_in?.length ? v.bed_lengths_in.map(b => `${b} in (${(b / 12).toFixed(1)} ft)`).join(", ") : null],
    ["Roof type", v.roof_type], ["Roof load", v.roof_load_lb ? `${v.roof_load_lb} lb` : null],
    ["Hitch class", v.hitch_class ? `Class ${v.hitch_class} (${v.receiver_in} in receiver)` : null],
    ["Tow rating", v.tow_rating_lb ? `${v.tow_rating_lb.toLocaleString()} lb` : null],
    ["Tire size", v.tire_size], ["Bolt pattern", v.bolt_pattern], ["Seating rows", String(v.rows_seating)],
  ];

  return (
    <>
      <div className="crumbs"><Link href="/vehicles">Vehicles</Link> › {v.make_name} › {v.model_name}</div>
      <h1>{vehicleTitle(v)} Accessories That Fit</h1>
      <p className="muted">{v.summary}</p>
      <p><Link className="btn" href={`/build?vehicle=${v.id}`}>Build your {v.model_name} setup</Link></p>

      <h2>Fit facts</h2>
      <table><tbody>
        {facts.filter(([, val]) => val).map(([k, val]) => <tr key={k}><th>{k}</th><td>{val}</td></tr>)}
      </tbody></table>

      <h2>Accessories by category</h2>
      <div className="grid">
        {cats.map(c => (
          <Link key={c.slug} href={`${vehiclePath(v)}/${c.slug}`} className="card">
            <h3>{c.name}</h3>
            <div className="muted">{countBy[c.slug] ? `${countBy[c.slug]} fit-checked picks` : "Coming soon"}</div>
          </Link>
        ))}
      </div>
    </>
  );
}
