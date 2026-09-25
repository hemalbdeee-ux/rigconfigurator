import type { MetadataRoute } from "next";
import { SITE_URL } from "@/lib/db";

export const dynamic = "force-dynamic";

export default function robots(): MetadataRoute.Robots {
  const rules = { allow: ["/", "/api/catalog/item/"], disallow: ["/api/", "/go/"] };
  return {
    rules: ["*", "GPTBot", "ChatGPT-User", "ClaudeBot", "Claude-Web", "anthropic-ai", "PerplexityBot", "Google-Extended", "Bingbot"].map(userAgent => ({ userAgent, ...rules })),
    sitemap: `${SITE_URL}/sitemap.xml`,
    host: SITE_URL,
  };
}
