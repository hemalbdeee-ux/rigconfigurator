import type { Metadata } from "next";
import { notFound } from "next/navigation";

// Placeholder for silos not built yet. Replace each with its own route folder as you build it.
const SECTIONS: Record<string, string> = {
  build: "Builder — pick a vehicle, fill slots with fit-checked parts, see a running total.",
  tools: "Tools — hitch class finder, bed-length checker, tow capacity calculator.",
  deals: "Deals — Amazon price drops on racks, covers and hitches.",
  laws: "Laws by state — window tint, lift height, light bar rules.",
};

export async function generateMetadata({ params }: { params: Promise<{ section: string }> }): Promise<Metadata> {
  const { section } = await params;
  const name = section.charAt(0).toUpperCase() + section.slice(1);
  return { title: `${name}: Coming Soon`, robots: { index: false, follow: true } };
}
export function generateStaticParams() { return Object.keys(SECTIONS).map(section => ({ section })); }

export default async function Section({ params }: { params: Promise<{ section: string }> }) {
  const { section } = await params;
  const text = SECTIONS[section];
  if (!text) notFound();
  return (<><h1 style={{ textTransform: "capitalize" }}>{section}</h1><p className="muted">{text}</p><p className="muted">Coming soon.</p></>);
}
