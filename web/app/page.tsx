import Link from "next/link";
import { allVehicles, vehiclePath, vehicleTitle } from "@/lib/queries";
import { VehiclePicker } from "@/components/VehiclePicker";

export const revalidate = 60;

export default async function Home() {
  const vehicles = await allVehicles();
  return (
    <>
      <section style={{ textAlign: "center", padding: "32px 0" }}>
        <h1>Parts that actually fit your rig.</h1>
        <p className="muted">Pick your vehicle. See only the racks, hitches, covers and gear verified to fit — then buy on Amazon.</p>
        <VehiclePicker vehicles={vehicles.map(v => ({ label: vehicleTitle(v), path: vehiclePath(v) }))} />
      </section>

      <h2>Start with your vehicle</h2>
      <div className="grid">
        {vehicles.map(v => (
          <Link key={v.id} href={vehiclePath(v)} className="card">
            <h3>{vehicleTitle(v)}</h3>
            <div className="muted">{v.gen_name} · {v.body_style.toUpperCase()}</div>
          </Link>
        ))}
      </div>

      <h2>Toolkit</h2>
      <div className="grid">
        {[["/build","Build","Configure a full setup with fit-checked parts and a running total"],
          ["/tools","Tools","Hitch class finder, bed-length checker, tow capacity calculator"],
          ["/deals","Deals","Amazon price drops on racks, covers and hitches"],
          ["/laws","Laws by state","Window tint, lift height and light bar rules"],
          ["/guides","Guides","Hard vs soft tonneau, Class 3 vs 4 hitch, install how-tos"]].map(([h,t,d]) => (
          <Link key={h} href={h} className="card"><h3>{t}</h3><div className="muted">{d}</div></Link>
        ))}
      </div>
    </>
  );
}
