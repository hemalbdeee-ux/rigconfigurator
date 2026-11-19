import { notFound } from "next/navigation";
import type { Metadata } from "next";
import { allSpecs, getSpec, specPath } from "@/lib/specs";
import { SpecView } from "@/components/SpecView";
import { staticOg } from "@/components/Hero";

export const revalidate = 3600;
type P = { make: string; model: string; topic: string };

export async function generateStaticParams() {
  return (await allSpecs()).map(s => ({ make: s.make_slug, model: s.model_slug, topic: s.topic }));
}

export async function generateMetadata({ params }: { params: Promise<P> }): Promise<Metadata> {
  const { make, model, topic } = await params;
  const s = await getSpec(make, model, topic);
  if (!s) return {};
  const path = specPath(s);
  return {
    title: { absolute: s.seo_title }, description: s.meta_desc, alternates: { canonical: path },
    openGraph: { title: s.title, description: s.meta_desc, url: path, type: "article", images: staticOg("vehicles", s.title) },
  };
}

export default async function SpecPageView({ params }: { params: Promise<P> }) {
  const { make, model, topic } = await params;
  const s = await getSpec(make, model, topic);
  if (!s) notFound();
  return <SpecView s={s} />;
}
