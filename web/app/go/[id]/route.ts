import { NextRequest, NextResponse } from "next/server";
import { q, amazonUrl } from "@/lib/db";

// /go/123?page=/vehicles/...&placement=card-1  → logs click → 302 to Amazon with tag
export async function GET(req: NextRequest, { params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const pid = Number(id);
  if (!Number.isInteger(pid)) return NextResponse.json({ error: "bad id" }, { status: 400 });
  const rows = await q<{ asin: string }>(`SELECT asin FROM products WHERE id=$1 AND active`, [pid]);
  if (!rows[0]) return NextResponse.json({ error: "not found" }, { status: 404 });

  const sp = req.nextUrl.searchParams;
  q(`INSERT INTO clicks (product_id, page, placement, ua, country) VALUES ($1,$2,$3,$4,$5)`,
    [pid, sp.get("page"), sp.get("placement"), req.headers.get("user-agent")?.slice(0, 200), req.headers.get("cf-ipcountry") ?? req.headers.get("x-country")])
    .catch(() => {});

  return NextResponse.redirect(amazonUrl(rows[0].asin), { status: 302 });
}
