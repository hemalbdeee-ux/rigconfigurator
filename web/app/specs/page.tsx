import Link from "next/link";
import { notFound } from "next/navigation";
import type { Metadata } from "next";
import { allSpecs, specPath } from "@/lib/specs";
import { staticOg } from "@/components/Hero";

// ISR: empty at build (no DB during `docker build`); db/apply.sh revalidates this path after each deploy.
export const revalidate = 3600;
export const metadata: Metadata = {
  title: "Truck & SUV Specs by Model: Towing, Bed Size, Bolt Pattern",
  description: "Towing capacity, bed size, bolt pattern, tire size and other figures for trucks and SUVs, copied from each maker's own spec sheets with the source beside every row.",
  alternates: { canonical: "/specs" },
  openGraph: { title: "Truck & SUV Specs by Model | Rig Configurator", url: "/specs", type: "website", images: staticOg("vehicles", "Specs by model") },
};

export default async function Specs() {
  const all = await allSpecs();
  if (!all.length) notFound();   // no published spec page yet: no empty index page
  const byModel = all.reduce<Record<string, typeof all>>((acc, s) => ((acc[`${s.make_name} ${s.model_name}`] ??= []).push(s), acc), {});
  return (
    <article className="art">
      <h1>Specs by model</h1>
      <p className="dek">The numbers you need before you buy a part or hook up a trailer, copied from each maker&apos;s own specification sheets. Every row links to its source.</p>
      {Object.entries(byModel).map(([name, list]) => (
        <section key={name}>
          <h2>{name}</h2>
          <ul className="plain-links">{list.map(s => <li key={s.topic}><Link href={specPath(s)}>{name} {s.topic_label.toLowerCase()}</Link></li>)}</ul>
        </section>
      ))}
    </article>
  );
}
