import type { Metadata } from "next";
import Link from "next/link";
import { staticOg } from "@/components/Hero";
import { allVehicles, getVehicleById, vehiclePath, vehicleTitle, yearsLabel, type Vehicle } from "@/lib/queries";
import { checkBeforeBuying } from "@/lib/hubCopy";
import { VehiclePicker } from "@/components/VehiclePicker";

export const dynamic = "force-dynamic";

export const metadata: Metadata = {
  title: "Fit Tools: Hitch Class, Bed Length and Tow Rating by Vehicle",
  description: "Look up the hitch class and receiver size, bed lengths in inches and feet, tow rating and roof type for every truck and SUV generation we cover, with a bed length chart.",
  alternates: { canonical: "/tools" },
  openGraph: { title: "Fit Tools by Vehicle | Rig Configurator", url: "/tools", type: "website", images: staticOg("vehicles", "Fit tools") },
};

// attrs.<key>_fact overrides the generated text where the stored column would mislead (same rule as the vehicle hub).
const fact = (v: Vehicle, key: string, fallback: string | null) => {
  const o = v.attrs?.[key];
  return typeof o === "string" ? o.charAt(0).toUpperCase() + o.slice(1) : fallback;
};
const ft = (inches: number) => `${(inches / 12).toFixed(1)} ft`;

export default async function Tools({ searchParams }: { searchParams: Promise<{ vehicle?: string }> }) {
  const [{ vehicle }, vehicles] = await Promise.all([searchParams, allVehicles()]);
  const v = await getVehicleById(Number(vehicle));
  const trucks = vehicles.filter(x => x.bed_lengths_in?.length);
  return (
    <section className="tool-page">
      <h1>Fit tools</h1>
      <p className="dek">The four numbers that decide whether an accessory fits: hitch class and receiver size, bed length, tow rating and roof type. Pick a vehicle to see its figures and what to check before buying.</p>
      <VehiclePicker vehicles={vehicles.map(x => ({ make: x.make_name, label: vehicleTitle(x), path: `/tools?vehicle=${x.id}` }))} compact cta="Show fit facts →" />

      {v && (
        <div className="tool-result" id="result">
          <h2>{vehicleTitle(v)} <span className="muted" style={{ fontWeight: 400, fontSize: 16 }}>· {v.gen_name}</span></h2>
          <table>
            <tbody>
              <tr><th>Hitch</th><td>{fact(v, "hitch_fact", v.hitch_class && v.hitch_class !== "none" ? `Class ${v.hitch_class}, ${v.receiver_in} in receiver` : "No factory receiver")}</td></tr>
              <tr><th>Tow rating</th><td>{fact(v, "tow_fact", v.tow_rating_lb ? `${v.tow_rating_lb.toLocaleString()} lb maximum, with the tow package; the figure for your build is in the owner's manual` : "Not stored; see the owner's manual")}</td></tr>
              {v.bed_lengths_in?.length ? <tr><th>Bed lengths</th><td>{v.bed_lengths_in.map(b => `${b} in (${ft(b)})`).join(" · ")}</td></tr> : null}
              <tr><th>Roof</th><td>{fact(v, "roof_type_fact", v.roof_type ? v.roof_type.replace("-", " ") : null) ?? "Not stored"}{" "}{fact(v, "roof_fact", v.roof_load_lb ? `· ${v.roof_load_lb} lb dynamic` : null) ? <span className="muted">· {fact(v, "roof_fact", v.roof_load_lb ? `${v.roof_load_lb} lb dynamic` : null)}</span> : null}</td></tr>
              <tr><th>Seating rows</th><td>{v.rows_seating}</td></tr>
              {v.tire_size && <tr><th>Stock tire</th><td>{v.tire_size}{v.bolt_pattern ? ` · bolt pattern ${v.bolt_pattern}` : ""}</td></tr>}
              <tr><th>Years</th><td>{v.year_to ? yearsLabel(v) : `${v.year_from}–present`}</td></tr>
            </tbody>
          </table>
          {checkBeforeBuying(v).length > 0 && (<>
            <h3>Check before you buy</h3>
            <ul>{checkBeforeBuying(v).map(s => <li key={s}>{s}</li>)}</ul>
          </>)}
          <p><Link className="btn" href={vehiclePath(v)}>See fit-checked parts for this {v.body_style === "truck" ? "truck" : "SUV"} →</Link> <Link href={`/build?vehicle=${v.id}`} className="btn-ghost">Build a full setup</Link></p>
          <p className="muted" style={{ fontSize: 13 }}>Figures come from manufacturer spec sheets and fit guides as read on the review date of each vehicle&apos;s guides; where a maker publishes no figure the row says so. The owner&apos;s manual is the authority for your exact build.</p>
        </div>
      )}

      <h2>Bed length chart</h2>
      <p className="muted">Covers and racks fit inches, not names. Inside length at the rail, bulkhead to closed tailgate.</p>
      <div className="tbl">
        <table>
          <thead><tr><th>Truck</th><th>Beds (in)</th><th>Beds (ft)</th><th>Hitch</th><th>Max tow</th></tr></thead>
          <tbody>
            {trucks.map(t => (
              <tr key={t.id}>
                <td><Link href={vehiclePath(t)}>{vehicleTitle(t)}</Link></td>
                <td>{t.bed_lengths_in.join(" / ")}</td>
                <td>{t.bed_lengths_in.map(ft).join(" / ")}</td>
                <td>{t.hitch_class && t.hitch_class !== "none" ? `Class ${t.hitch_class}, ${t.receiver_in} in` : "None"}</td>
                <td>{t.tow_rating_lb ? `${t.tow_rating_lb.toLocaleString()} lb` : "—"}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <p className="muted" style={{ fontSize: 13 }}>Hitch class and tow figures are the maximum with the factory tow package where one exists; many trims ship without a receiver. The explainers on <Link href="/learn">Learn</Link> cover hitch classes and bed names in detail.</p>
    </section>
  );
}
