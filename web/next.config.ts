import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: "standalone",
  poweredByHeader: false,   // drop "x-powered-by: Next.js"
  async headers() {
    return [{
      source: "/:path*",
      headers: [
        // HTTPS-only site behind Traefik; no includeSubDomains/preload so other subdomains are unaffected.
        { key: "Strict-Transport-Security", value: "max-age=31536000" },
        { key: "X-Content-Type-Options", value: "nosniff" },
        { key: "Referrer-Policy", value: "strict-origin-when-cross-origin" },
        { key: "X-Frame-Options", value: "SAMEORIGIN" },
        { key: "Permissions-Policy", value: "camera=(), microphone=(), geolocation=()" },
      ],
    }];
  },
  images: {
    remotePatterns: [{ protocol: "https", hostname: "m.media-amazon.com" }],
  },
  async redirects() {
    return [];
  },
};

export default nextConfig;
