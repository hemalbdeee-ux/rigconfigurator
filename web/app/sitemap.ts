import type { MetadataRoute } from "next";
import { SITE_URL } from "@/lib/db";
import { allFitmentPaths, allVehicles, vehiclePath } from "@/lib/queries";

export const revalidate = 3600;

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const [vs, fps] = await Promise.all([allVehicles(), allFitmentPaths()]);
  return [
    { url: SITE_URL, changeFrequency: "daily", priority: 1 },
    { url: `${SITE_URL}/vehicles`, changeFrequency: "weekly", priority: 0.9 },
    { url: `${SITE_URL}/about`, changeFrequency: "monthly", priority: 0.3 },
    { url: `${SITE_URL}/disclosure`, changeFrequency: "yearly", priority: 0.2 },
    ...vs.map(v => ({ url: `${SITE_URL}${vehiclePath(v)}`, changeFrequency: "weekly" as const, priority: 0.8 })),
    ...fps.map(f => ({ url: `${SITE_URL}/vehicles/${f.make_slug}/${f.model_slug}/${f.gen_slug}/${f.category_slug}`, lastModified: new Date(f.updated_at), changeFrequency: "weekly" as const, priority: 0.7 })),
  ];
}
