import Link from "next/link";
import data from "@/lib/toolData.json";
import type { Vehicle } from "@/lib/queries";

type Roof = { roof_type: string; roof_lb: number | null; roof: string; covers: string; source: string; confirmed: boolean };
type Tow = { receiver: string; size: string; max_tow: string; tongue: string; source: string };
const D = data as unknown as { roof: Record<string, Roof>; tow: Record<string, Tow> };

/** Which chart a guide category draws its vehicle figures from. */
const KIND: Record<string, "roof" | "tow"> = { "roof-racks": "roof", "cargo-boxes": "roof", "hitches": "tow" };

/**
 * The vehicle's own figures from the chart pillars (lib/toolData.json), shown on roof rack, cargo box and hitch guides.
 * Every value is the chart row as written, with its source line; nothing is typed here.
 */
export function VehicleNumbers({ v, category }: { v: Vehicle; category: string }) {
  const kind = KIND[category];
  if (!kind) return null;
  const k = `${v.make_name} ${v.model_name} ${v.year_from}`.toLowerCase();
  const name = /^\d/.test(v.model_name) ? `${v.make_name} ${v.model_name}` : v.model_name;
  if (kind === "roof") {
    const r = D.roof[k];
    if (!r) return null;
    return (
      <section className="vnum" aria-label={`${name} roof figures`}>
        <h2 id="vehicle-numbers">{name} roof figures</h2>
        <table><tbody>
          <tr><th>Roof</th><td>{r.roof_type}</td></tr>
          <tr><th>Roof load (lb)</th><td>{r.roof}{r.roof_lb && !r.confirmed ? " · not confirmed by the maker" : ""}</td></tr>
          {r.covers && <tr><th>What the figure covers</th><td>{r.covers}</td></tr>}
          <tr><th>Source</th><td className="muted">{r.source}</td></tr>
        </tbody></table>
        <p className="vnum-links"><Link href="/tools/roof-load-calculator">Roof load calculator →</Link> <Link href="/learn/roof-load-limits-by-vehicle">All 32 vehicles compared →</Link></p>
      </section>
    );
  }
  const t = D.tow[k];
  if (!t) return null;
  return (
    <section className="vnum" aria-label={`${name} towing figures`}>
      <h2 id="vehicle-numbers">{name} hitch and towing figures</h2>
      <table><tbody>
        <tr><th>Factory receiver</th><td>{t.receiver}</td></tr>
        <tr><th>Receiver size and class</th><td>{t.size}</td></tr>
        <tr><th>Max tow (lb)</th><td>{t.max_tow}</td></tr>
        <tr><th>Tongue weight (lb)</th><td>{t.tongue}</td></tr>
        <tr><th>Source</th><td className="muted">{t.source}</td></tr>
      </tbody></table>
      <p className="vnum-links"><Link href="/tools/tongue-weight-calculator">Tongue weight calculator →</Link> <Link href="/learn/factory-tow-hitch-by-vehicle">All 32 vehicles compared →</Link></p>
    </section>
  );
}
