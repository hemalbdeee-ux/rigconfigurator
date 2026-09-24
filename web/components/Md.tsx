// Tiny markdown: paragraphs, "- " bullets, **bold**, [text](url). Content is our own (DB), not user input.
function inline(s: string) {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;")
    .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
    .replace(/\[([^\]]+)\]\(([^)\s]+)\)/g, (_m, t, u) => `<a href="${u}"${u.startsWith("http") ? ' rel="nofollow noopener" target="_blank"' : ""}>${t}</a>`);
}
export function mdHtml(s?: string | null): string {
  if (!s) return "";
  return s.split(/\n{2,}|\n(?=- )/).map(block => {
    const b = block.trim();
    return b.startsWith("- ")
      ? `<ul>${b.split(/\n- |^- /).filter(Boolean).map(i => `<li>${inline(i)}</li>`).join("")}</ul>`
      : `<p>${inline(b)}</p>`;
  }).join("");
}
export function Md({ s, className }: { s?: string | null; className?: string }) {
  if (!s) return null;
  return <div className={className} dangerouslySetInnerHTML={{ __html: mdHtml(s) }} />;
}
export const Inline = ({ s }: { s: string }) => <span dangerouslySetInnerHTML={{ __html: inline(s) }} />;
