import { NextRequest, NextResponse } from "next/server";
import { revalidatePath } from "next/cache";

// Pipeline calls: POST /api/revalidate?secret=...  body: {"paths":["/vehicles/ford/f-150/2021-2025/tonneau-covers"]}
export async function POST(req: NextRequest) {
  if (req.nextUrl.searchParams.get("secret") !== process.env.REVALIDATE_SECRET) return NextResponse.json({ ok: false }, { status: 401 });
  const { paths = [] } = await req.json().catch(() => ({ paths: [] }));
  for (const p of paths as string[]) revalidatePath(p);
  return NextResponse.json({ ok: true, revalidated: paths.length });
}
