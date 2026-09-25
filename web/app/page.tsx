import type { Metadata } from "next";
import Link from "next/link";
import { SITE_URL } from "@/lib/db";
import { allVehicles, vehiclePath, vehicleTitle } from "@/lib/queries";
import { VehiclePicker } from "@/components/VehiclePicker";

export const revalidate = 60;

const HOME_TITLE = "Rig Configurator: Fit-Checked Truck & SUV Accessories";
const HOME_DESC = "Pick your vehicle, see only the racks, hitches, tonneau covers and gear that actually fit. Verified against manufacturer fit guides.";
export const metadata: Metadata = {
  title: { absolute: HOME_TITLE },
  description: HOME_DESC,
  alternates: { canonical: "/" },
  openGraph: { title: HOME_TITLE, description: HOME_DESC, url: "/", siteName: "Rig Configurator", type: "website", locale: "en_US" },
  twitter: { card: "summary", title: HOME_TITLE, description: HOME_DESC },
};

const homeLd = {
  "@context": "https://schema.org",
  "@graph": [
    { "@type": "WebSite", "@id": `${SITE_URL}/#website`, url: `${SITE_URL}/`, name: "Rig Configurator", publisher: { "@id": `${SITE_URL}/#org` } },
    { "@type": "Organization", "@id": `${SITE_URL}/#org`, name: "Rig Configurator", url: `${SITE_URL}/` },
  ],
};

export default async function Home() {
  const vehicles = await allVehicles();
  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(homeLd) }} />
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
