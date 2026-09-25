import type { Metadata } from "next";
import Link from "next/link";
import { staticOg } from "@/components/Hero";
import { allVehicles, vehiclePath, vehicleTitle } from "@/lib/queries";

export const dynamic = "force-dynamic";   // see app/page.tsx
export const metadata: Metadata = {
  title: "Truck & SUV Accessories by Vehicle",
  description: "Every truck and SUV generation we cover, with the racks, hitches, tonneau covers, floor liners and steps verified to fit each one.",
  alternates: { canonical: "/vehicles" },
  openGraph: { title: "Truck & SUV Accessories by Vehicle | Rig Configurator", url: "/vehicles", siteName: "Rig Configurator", type: "website", images: staticOg("vehicles", "Truck & SUV accessories by vehicle") },
};

export default async function Vehicles() {
  const vs = await allVehicles();
  const byMake = vs.reduce<Record<string, typeof vs>>((acc, v) => ((acc[v.make_name] ??= []).push(v), acc), {});
  return (
    <>
      <h1>Vehicles</h1>
      <p className="dek">{vs.length} truck and SUV generations from {Object.keys(byMake).length} makes. Pick yours to see the fit facts (bed lengths, roof type, hitch class and tow rating) and only the accessories listed to fit it.</p>
      {Object.entries(byMake).map(([make, list]) => (
        <section key={make}>
          <h2>{make}</h2>
          <div className="grid">{list.map(v => <Link key={v.id} href={vehiclePath(v)} className="card"><h3>{vehicleTitle(v)}</h3><div className="muted">{v.gen_name}</div></Link>)}</div>
        </section>
      ))}
    </>
  );
}
