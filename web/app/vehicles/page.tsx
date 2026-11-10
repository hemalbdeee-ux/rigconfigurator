import type { Metadata } from "next";
import Link from "next/link";
import { staticOg } from "@/components/Hero";
import { allFitmentPaths, allVehicles, modelYearsText, vehiclePath, vehicleTitle } from "@/lib/queries";
import { allPillars } from "@/lib/pillars";

export const dynamic = "force-dynamic";   // see app/page.tsx
export const metadata: Metadata = {
  title: "Truck & SUV Accessories by Vehicle",
  description: "Every truck and SUV generation we cover, with the racks, hitches, tonneau covers, floor liners and steps verified to fit each one.",
  alternates: { canonical: "/vehicles" },
  openGraph: { title: "Truck & SUV Accessories by Vehicle | Rig Configurator", url: "/vehicles", siteName: "Rig Configurator", type: "website", images: staticOg("vehicles", "Truck & SUV accessories by vehicle") },
};

const BODY: Record<string, string> = { truck: "Pickup", suv: "SUV" };

export default async function Vehicles() {
  const [vs, fps, pillars] = await Promise.all([allVehicles(), allFitmentPaths(), allPillars()]);
  const byMake = vs.reduce<Record<string, typeof vs>>((acc, v) => ((acc[v.make_name] ??= []).push(v), acc), {});
  const guideCount = fps.reduce<Record<string, number>>((acc, f) => { const k = `/vehicles/${f.make_slug}/${f.model_slug}/${f.gen_slug}`; acc[k] = (acc[k] ?? 0) + 1; return acc; }, {});
  const upgrades = new Set(pillars.filter(p => p.kind === "upgrades").map(p => p.path));
  return (
    <>
      <h1>Vehicles</h1>
      <p className="dek">{vs.length} truck and SUV generations from {Object.keys(byMake).length} makes. Pick yours to see the fit facts (bed lengths, roof type, hitch class and tow rating) and only the accessories listed to fit it.</p>
      <p className="muted">Parts are matched to a generation, not just a model name, because a redesign usually changes the bed, the roof rails and the mounting points. Check the model years on each card before you open it: a 2023 and a 2024 of the same truck can need different parts.</p>
      {Object.entries(byMake).map(([make, list]) => (
        <section key={make}>
          <h2>{make}</h2>
          <div className="grid">{list.map(v => {
            const hub = vehiclePath(v), n = guideCount[hub] ?? 0, up = `${hub}/upgrades`;
            return (
              <div key={v.id} className="card">
                <h3><Link href={hub}>{vehicleTitle(v)}</Link></h3>
                <div className="muted" style={{ fontSize: 14 }}>{v.gen_name} · {BODY[v.body_style] ?? v.body_style.toUpperCase()} · model years {modelYearsText(v)}</div>
                <div style={{ fontSize: 14, marginTop: 6 }}>
                  <Link href={hub}>{n > 0 ? `${n} fit-checked ${n === 1 ? "guide" : "guides"}` : "Fit facts"}</Link>
                  {upgrades.has(up) && <> · <Link href={up}>Upgrades, ranked</Link></>}
                </div>
              </div>
            );
          })}</div>
        </section>
      ))}
    </>
  );
}
