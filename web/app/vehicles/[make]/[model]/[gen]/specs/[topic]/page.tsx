import { notFound } from "next/navigation";
import type { Metadata } from "next";
import { everySpec, getSpec, specPath } from "@/lib/specs";
import { SpecView } from "@/components/SpecView";
import { staticOg } from "@/components/Hero";

export const revalidate = 3600;
// Generation-level spec page: one generation, answered model year by model year.
type P = { make: string; model: string; gen: string; topic: string };

export async function generateStaticParams() {
  return (await everySpec()).filter(s => s.kind === "generation").map(s => ({ make: s.make_slug, model: s.model_slug, gen: s.gen_slug, topic: s.topic }));
}

export async function generateMetadata({ params }: { params: Promise<P> }): Promise<Metadata> {
  const { make, model, gen, topic } = await params;
  const s = await getSpec(make, model, topic, gen);
  if (!s) return {};
  const path = specPath(s);
  return {
    title: { absolute: s.seo_title }, description: s.meta_desc, alternates: { canonical: path },
    openGraph: { title: s.title, description: s.meta_desc, url: path, type: "article", images: staticOg("vehicles", s.title) },
  };
}

export default async function GenSpecPageView({ params }: { params: Promise<P> }) {
  const { make, model, gen, topic } = await params;
  const s = await getSpec(make, model, topic, gen);
  if (!s) notFound();
  return <SpecView s={s} />;
}
