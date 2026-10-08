// IndexNow key file: https://rigconfigurator.com/indexnow-key.txt must return the key as plain text.
// The pipeline sends keyLocation pointing here, so the key can live in .env instead of a committed file.
export const dynamic = "force-dynamic";

export function GET() {
  const key = process.env.INDEXNOW_KEY;
  if (!key) return new Response("Not found", { status: 404 });
  return new Response(key, { headers: { "Content-Type": "text/plain; charset=utf-8", "Cache-Control": "public, max-age=3600" } });
}
