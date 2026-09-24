import type { Hero as H } from "@/lib/queries";

// Licensed vehicle photo + the attribution CC licenses require (author, license, source link).
export function Hero({ h, alt, priority = false }: { h: H | null; alt: string; priority?: boolean }) {
  if (!h) return null;
  const small = `/img/${h.file.replace(/\.webp$/, "-800.webp")}`;
  const big = `/img/${h.file}`;
  return (
    <figure className="hero">
      <img src={big} srcSet={`${small} 800w, ${big} 1600w`} sizes="(max-width: 860px) 100vw, 820px"
        width={h.width} height={h.height} alt={alt} loading={priority ? "eager" : "lazy"} fetchPriority={priority ? "high" : "auto"} />
      <figcaption>
        Photo: {h.author} · <a href={h.license_url ?? h.source_url} rel="nofollow noopener" target="_blank">{h.license}</a> · via{" "}
        <a href={h.source_url} rel="nofollow noopener" target="_blank">Wikimedia Commons</a>
      </figcaption>
    </figure>
  );
}

export const ogImage = (h: H | null) => h ? [{ url: `/img/${h.file.replace(/\.webp$/, "-og.jpg")}`, width: 1200, height: 630 }] : undefined;
