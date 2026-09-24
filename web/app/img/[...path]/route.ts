// Serves licensed images written by pipeline/fetch_images.py into the shared volume (./pipeline/data/img → /app/img).
// Next only serves /public files that exist at build time, so runtime images go through this handler.
import { readFile } from "node:fs/promises";
import path from "node:path";

const ROOT = process.env.IMG_DIR ?? "/app/img";
const TYPES: Record<string, string> = { ".webp": "image/webp", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png" };

export async function GET(_req: Request, { params }: { params: Promise<{ path: string[] }> }) {
  const { path: parts } = await params;
  const rel = parts.join("/");
  const ext = path.extname(rel).toLowerCase();
  if (!TYPES[ext] || rel.includes("..")) return new Response("Not found", { status: 404 });
  try {
    const buf = await readFile(path.join(ROOT, rel));
    return new Response(new Uint8Array(buf), { headers: { "Content-Type": TYPES[ext], "Cache-Control": "public, max-age=604800, stale-while-revalidate=86400" } });
  } catch {
    return new Response("Not found", { status: 404 });
  }
}
