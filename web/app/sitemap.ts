import type { MetadataRoute } from "next";
import { SITE_URL } from "@/lib/db";
import { allFitmentPaths, allVehicles, vehiclePath } from "@/lib/queries";
import { allPillars } from "@/lib/pillars";

// Rendered per request: the DB is not reachable during `docker build`, so a build-time sitemap would be empty.
export const dynamic = "force-dynamic";

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const [vs, fps, pillars] = await Promise.all([allVehicles(), allFitmentPaths(), allPillars()]);
  return [
    { url: SITE_URL, changeFrequency: "daily", priority: 1 },
    { url: `${SITE_URL}/vehicles`, changeFrequency: "weekly", priority: 0.9 },
    { url: `${SITE_URL}/guides`, changeFrequency: "weekly", priority: 0.8 },
    { url: `${SITE_URL}/build`, changeFrequency: "weekly", priority: 0.6 },
    { url: `${SITE_URL}/tools`, changeFrequency: "monthly", priority: 0.6 },
    { url: `${SITE_URL}/deals`, changeFrequency: "daily", priority: 0.6 },
    ...[...new Set(fps.map(f => f.category_slug))].map(c => ({ url: `${SITE_URL}/guides/${c}`, changeFrequency: "weekly" as const, priority: 0.7 })),
    ...(pillars.length ? [{ url: `${SITE_URL}/learn`, changeFrequency: "weekly" as const, priority: 0.7 }] : []),
    ...pillars.map(p => ({ url: `${SITE_URL}${p.path}`, lastModified: new Date(p.updated), changeFrequency: "monthly" as const, priority: 0.8 })),
    { url: `${SITE_URL}/about`, changeFrequency: "monthly", priority: 0.3 },
    { url: `${SITE_URL}/disclosure`, changeFrequency: "yearly", priority: 0.2 },
    { url: `${SITE_URL}/privacy`, changeFrequency: "yearly", priority: 0.2 },
    { url: `${SITE_URL}/terms`, changeFrequency: "yearly", priority: 0.2 },
    ...vs.map(v => ({ url: `${SITE_URL}${vehiclePath(v)}`, changeFrequency: "weekly" as const, priority: 0.8 })),
    ...fps.map(f => ({ url: `${SITE_URL}/vehicles/${f.make_slug}/${f.model_slug}/${f.gen_slug}/${f.category_slug}`, lastModified: new Date(f.updated_at), changeFrequency: "weekly" as const, priority: 0.7 })),
  ];
}
