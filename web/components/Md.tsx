// Tiny markdown: paragraphs, "- " bullets, **bold**, [text](url). Content is our own (DB), not user input.
// Optional Linker turns the first mention of a mapped phrase into an internal link (contextual internal linking).

export class Linker {
  private used = new Set<string>();
  private rules: { re: RegExp; href: string; key: string }[];
  constructor(map: Record<string, string>, private max = 8) {
    this.rules = Object.entries(map)
      .sort((a, b) => b[0].length - a[0].length) // longest phrase first ("tonneau covers" before "covers")
      .map(([phrase, href]) => ({ re: new RegExp(`\\b(${phrase.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")})\\b`, "i"), href, key: href }));
  }
  apply(html: string): string {
    // only touch text outside tags and outside existing <a>…</a>
    let inA = 0;
    return html.split(/(<[^>]+>)/).map(part => {
      if (part.startsWith("<")) { if (/^<a[\s>]/i.test(part)) inA++; else if (/^<\/a>/i.test(part)) inA--; return part; }
      if (inA || this.used.size >= this.max) return part;
      for (const r of this.rules) {
        if (this.used.has(r.key) || this.used.size >= this.max) continue;
        if (r.re.test(part)) { part = part.replace(r.re, `<a class="autolink" href="${r.href}">$1</a>`); this.used.add(r.key); }
      }
      return part;
    }).join("");
  }
}

function inline(s: string, linker?: Linker) {
  const h = s.replace(/&/g, "&amp;").replace(/</g, "&lt;")
    .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
    .replace(/\[([^\]]+)\]\(([^)\s]+)\)/g, (_m, t, u) => `<a href="${u}"${u.startsWith("http") ? ' rel="nofollow noopener" target="_blank"' : ""}>${t}</a>`);
  return linker ? linker.apply(h) : h;
}
export function mdHtml(s?: string | null, linker?: Linker): string {
  if (!s) return "";
  return s.split(/\n{2,}|\n(?=- )/).map(block => {
    const b = block.trim();
    return b.startsWith("- ")
      ? `<ul>${b.split(/\n- |^- /).filter(Boolean).map(i => `<li>${inline(i, linker)}</li>`).join("")}</ul>`
      : `<p>${inline(b, linker)}</p>`;
  }).join("");
}
export function Md({ s, className, linker }: { s?: string | null; className?: string; linker?: Linker }) {
  if (!s) return null;
  return <div className={className} dangerouslySetInnerHTML={{ __html: mdHtml(s, linker) }} />;
}
export const Inline = ({ s, linker }: { s: string; linker?: Linker }) => <span dangerouslySetInnerHTML={{ __html: inline(s, linker) }} />;
