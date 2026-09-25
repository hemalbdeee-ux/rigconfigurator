import { Pool, types } from "pg";

// DATE columns come back as "YYYY-MM-DD" strings, not Date objects at local midnight (which shifted JSON-LD dates by a day).
types.setTypeParser(1082, (v: string) => v);

declare global {
  // eslint-disable-next-line no-var
  var __pgPool: Pool | undefined;
}

export const pool =
  global.__pgPool ??
  new Pool({
    connectionString: process.env.DATABASE_URL,
    max: 10,
    idleTimeoutMillis: 30_000,
  });
if (process.env.NODE_ENV !== "production") global.__pgPool = pool;

export async function q<T = any>(text: string, params: any[] = []): Promise<T[]> {
  try {
    const { rows } = await pool.query(text, params);
    return rows as T[];
  } catch (err: any) {
    // During `next build` inside Docker the DB is not reachable: render nothing now, ISR fills pages at runtime.
    if (process.env.NEXT_PHASE === "phase-production-build" && ["ECONNREFUSED", "ENOTFOUND", "EAI_AGAIN"].includes(err?.code)) return [];
    throw err;
  }
}

// Production default; override with SITE_URL (build arg + runtime env) for staging/local.
export const SITE_URL = (process.env.SITE_URL || "https://rigconfigurator.com").replace(/\/+$/, "");
export const AMAZON_TAG = process.env.AMAZON_TAG ?? "rigconfig-20";

export function amazonUrl(asin: string) {
  return `https://www.amazon.com/dp/${asin}?tag=${AMAZON_TAG}`;
}

export function money(cents: number | null, band: string | null) {
  if (cents) return `$${(cents / 100).toFixed(2)}`;
  return band ?? "See price";
}
