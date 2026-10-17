"use client";
import { useEffect, useState } from "react";

/**
 * Real-world fit: install videos and owner posts, shown through each platform's own embed so the creator keeps
 * ownership and credit (nothing is copied to this server). YouTube loads only on click (a thumbnail facade keeps the
 * page fast and sets no YouTube cookies until the visitor plays it); Reddit posts use Reddit's official embed script.
 */
export type Embed =
  | { kind: "youtube"; id: string; title: string; channel: string; note?: string }
  | { kind: "reddit"; url: string; title: string; sub: string; author?: string; note?: string };

function YouTube({ e }: { e: Extract<Embed, { kind: "youtube" }> }) {
  const [play, setPlay] = useState(false);
  return (
    <figure className="embed">
      <div className="embed-yt">
        {play
          ? <iframe src={`https://www.youtube-nocookie.com/embed/${e.id}?autoplay=1&rel=0`} title={e.title} allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowFullScreen loading="lazy" />
          : <button type="button" className="embed-yt-facade" onClick={() => setPlay(true)} aria-label={`Play video: ${e.title}`}>
              <img src={`https://i.ytimg.com/vi/${e.id}/hqdefault.jpg`} alt="" loading="lazy" width={480} height={360} />
              <span className="embed-play" aria-hidden="true">▶</span>
            </button>}
      </div>
      <figcaption><strong>{e.title}</strong> · video by {e.channel} on YouTube{e.note ? <> · {e.note}</> : null}</figcaption>
    </figure>
  );
}

function Reddit({ e }: { e: Extract<Embed, { kind: "reddit" }> }) {
  return (
    <figure className="embed">
      <blockquote className="reddit-embed-bq" data-embed-height="520">
        <a href={e.url} rel="nofollow noopener" target="_blank">{e.title}</a><br />
        by <a href={e.author ? `https://www.reddit.com/user/${e.author}/` : e.url} rel="nofollow noopener" target="_blank">{e.author ? `u/${e.author}` : "an owner"}</a> in <a href={`https://www.reddit.com/r/${e.sub}/`} rel="nofollow noopener" target="_blank">r/{e.sub}</a>
      </blockquote>
      {e.note && <figcaption>{e.note}</figcaption>}
    </figure>
  );
}

export function Embeds({ items, model }: { items: Embed[]; model: string }) {
  const hasReddit = items.some(i => i.kind === "reddit");
  useEffect(() => {
    if (!hasReddit || document.getElementById("reddit-embed-js")) return;
    const s = document.createElement("script");
    s.id = "reddit-embed-js"; s.async = true; s.src = "https://embed.reddit.com/widgets.js"; s.charset = "UTF-8";
    document.body.appendChild(s);
  }, [hasReddit]);
  if (!items.length) return null;
  return (
    <section id="real-world" className="real-world">
      <h2>Real-world fit: owner posts and install videos</h2>
      <p className="muted">How these parts look and go on in real {model}s, from owners and installers. Each is shown through the platform&apos;s own embed and stays with its creator; we picked them, we did not make them.</p>
      <div className="embed-grid">{items.map((e, i) => e.kind === "youtube" ? <YouTube key={i} e={e} /> : <Reddit key={i} e={e} />)}</div>
    </section>
  );
}
