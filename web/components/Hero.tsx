import type { Hero as H } from "@/lib/queries";

// Licensed vehicle photo + the attribution CC licenses require (author, license, source link).
export function Hero({ h, alt, priority = false }: { h: H | null; alt: string; priority?: boolean }) {
  if (!h) return null;
  const small = `/img/${h.file.replace(/\.webp$/, "-800.webp")}`;
  const big = `/img/${h.file}`;
  return (
    <figure className="hero">
      <picture>
        {/* Phones get the 800w file regardless of DPR: the 1600w webp (125–240 KB) put mobile LCP at the 2.5 s line. */}
        <source media="(max-width: 860px)" srcSet={small} />
        <img src={big} srcSet={`${small} 800w, ${big} 1600w`} sizes="820px"
          width={h.width} height={h.height} alt={alt} loading={priority ? "eager" : "lazy"} fetchPriority={priority ? "high" : "auto"} />
      </picture>
      <figcaption>
        Photo: {h.author} · <a href={h.license_url ?? h.source_url} rel="nofollow noopener" target="_blank">{h.license}</a> · via{" "}
        <a href={h.source_url} rel="nofollow noopener" target="_blank">Wikimedia Commons</a>
      </figcaption>
    </figure>
  );
}

export const DEFAULT_OG = [{ url: "/og/default.jpg", width: 1200, height: 630, alt: "Rig Configurator" }];
export const staticOg = (name: string, alt: string) => [{ url: `/og/${name}.jpg`, width: 1200, height: 630, alt }];
export const ogImage = (h: H | null, alt?: string) => h ? [{ url: `/img/${h.file.replace(/\.webp$/, "-og.jpg")}`, width: 1200, height: 630, alt: alt ?? h.title }] : DEFAULT_OG;
