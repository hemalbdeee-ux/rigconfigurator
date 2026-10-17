import data from "./toolData.json";
import { allVehicles, publishedGuides, vehiclePath, vehicleTitle } from "./queries";
import type { CalcVehicle } from "@/components/Calculators";

type ToolData = { tow: Record<string, any>; roof: Record<string, any> };
const D = data as ToolData;
const key = (make: string, model: string, yearFrom: number) => `${make} ${model} ${yearFrom}`.toLowerCase();

/** Every covered vehicle with its chart figures (lib/toolData.json, built from the chart pillars) and its guide links. */
export async function calcVehicles(): Promise<CalcVehicle[]> {
  const [vs, hitches, roofs] = await Promise.all([allVehicles(), publishedGuides("hitches"), publishedGuides("roof-racks")]);
  const guideFor = (rows: { path: string }[], hub: string) => rows.find(r => r.path.startsWith(hub + "/"))?.path;
  return vs.map(v => {
    const k = key(v.make_name, v.model_name, v.year_from);
    const hub = vehiclePath(v);
    return {
      id: v.id, make: v.make_name, label: vehicleTitle(v), hub,
      hitchGuide: guideFor(hitches, hub), roofGuide: guideFor(roofs, hub),
      tow: D.tow[k] ?? null, roof: D.roof[k] ?? null,
    };
  }).sort((a, b) => a.label.localeCompare(b.label));
}
