import type { MetadataRoute } from "next";
import { SITE_URL } from "@/lib/db";

export const dynamic = "force-dynamic";

export default function robots(): MetadataRoute.Robots {
  // `?_rsc=` = Next.js client-navigation payloads (not pages). Crawl stats showed 53% of Googlebot requests going to them.
  const rules = { allow: ["/", "/api/catalog/item/"], disallow: ["/api/", "/go/", "/*?_rsc=", "/*&_rsc="] };
  return {
    rules: ["*", "GPTBot", "ChatGPT-User", "ClaudeBot", "Claude-Web", "anthropic-ai", "PerplexityBot", "Google-Extended", "Bingbot"].map(userAgent => ({ userAgent, ...rules })),
    sitemap: `${SITE_URL}/sitemap.xml`,
    host: SITE_URL,
  };
}
