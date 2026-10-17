"use client";
import { useState } from "react";

/**
 * "Cite this page" box under data charts and tools. Bloggers and forum posters who reuse a figure get a ready attribution
 * line; the anchor is the page name plus the brand, never a keyword.
 */
export function CiteBox({ url, name }: { url: string; name: string }) {
  const html = `<a href="${url}">${name}</a> (Rig Configurator)`;
  const text = `${name}, Rig Configurator: ${url}`;
  const [copied, setCopied] = useState<"" | "html" | "text">("");
  const copy = async (what: "html" | "text") => {
    try { await navigator.clipboard.writeText(what === "html" ? html : text); setCopied(what); setTimeout(() => setCopied(""), 2000); } catch { /* clipboard blocked: the text stays selectable */ }
  };
  return (
    <aside className="cite-box" aria-label="Cite this page">
      <strong>Using these figures?</strong>
      <p className="muted">You are welcome to quote this page in a post, forum thread or article. Please credit it with a link:</p>
      <code className="cite-code">{html}</code>
      <div className="cite-actions">
        <button type="button" className="btn-ghost" onClick={() => copy("html")}>{copied === "html" ? "Copied" : "Copy HTML link"}</button>
        <button type="button" className="btn-ghost" onClick={() => copy("text")}>{copied === "text" ? "Copied" : "Copy plain text"}</button>
      </div>
    </aside>
  );
}
