import { notFound } from "next/navigation";

// Placeholder for silos not built yet. Replace each with its own route folder as you build it.
const SECTIONS: Record<string, string> = {
  build: "Builder — pick a vehicle, fill slots with fit-checked parts, see a running total.",
  guides: "Guides — cross-vehicle buying guides and install how-tos.",
  tools: "Tools — hitch class finder, bed-length checker, tow capacity calculator.",
  deals: "Deals — Amazon price drops on racks, covers and hitches.",
  laws: "Laws by state — window tint, lift height, light bar rules.",
  about: "About Rig Configurator.",
  disclosure: "Affiliate disclosure: As an Amazon Associate we earn from qualifying purchases.",
  privacy: "Privacy policy.",
  terms: "Terms of use.",
};

export const metadata = { robots: { index: false } };
export function generateStaticParams() { return Object.keys(SECTIONS).map(section => ({ section })); }

export default async function Section({ params }: { params: Promise<{ section: string }> }) {
  const { section } = await params;
  const text = SECTIONS[section];
  if (!text) notFound();
  return (<><h1 style={{ textTransform: "capitalize" }}>{section}</h1><p className="muted">{text}</p><p className="muted">Coming soon.</p></>);
}
