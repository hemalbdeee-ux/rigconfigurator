import Link from "next/link";
import { allVehicles, vehiclePath, vehicleTitle } from "@/lib/queries";

export const revalidate = 60;
export const metadata = { title: "All Vehicles — Fit-checked accessories by make, model and generation" };

export default async function Vehicles() {
  const vs = await allVehicles();
  const byMake = vs.reduce<Record<string, typeof vs>>((acc, v) => ((acc[v.make_name] ??= []).push(v), acc), {});
  return (
    <>
      <h1>Vehicles</h1>
      {Object.entries(byMake).map(([make, list]) => (
        <section key={make}>
          <h2>{make}</h2>
          <div className="grid">{list.map(v => <Link key={v.id} href={vehiclePath(v)} className="card"><h3>{vehicleTitle(v)}</h3><div className="muted">{v.gen_name}</div></Link>)}</div>
        </section>
      ))}
    </>
  );
}
