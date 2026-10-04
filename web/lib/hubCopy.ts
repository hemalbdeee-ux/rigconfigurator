import type { Vehicle } from "./queries";

// Per-category blurb for the vehicle hub (Template B). Vehicle facts are woven in so no two hubs read the same.
export function categoryBlurb(slug: string, v: Vehicle): string {
  const beds = v.bed_lengths_in?.length ? v.bed_lengths_in.map(b => `${(b / 12).toFixed(1)} ft`).join(" / ") : "";
  const gen = v.gen_name;
  const roof = v.roof_type ?? "unknown";
  // attrs.roof_phrase (optional) replaces "a <roof type> roof" where the roof differs by trim.
  const roofPhrase = typeof v.attrs?.roof_phrase === "string" ? v.attrs.roof_phrase : `a ${roof.replace("-", " ")} roof`;
  // attrs.hitch_fact (optional) replaces the generated "Class N, X in receiver" text where it would mislead.
  const hitch = typeof v.attrs?.hitch_fact === "string" ? v.attrs.hitch_fact
    : v.hitch_class && v.hitch_class !== "none" ? `Class ${v.hitch_class}, ${v.receiver_in} in receiver` : "no factory receiver";
  const tow = v.tow_rating_lb ? `${v.tow_rating_lb.toLocaleString()} lb` : "";
  // attrs.roof_fact (optional) means the stored roof load is caveated on the hub, so the blurbs do not print it as a rating.
  const roofLoad = typeof v.attrs?.roof_fact === "string" ? null : v.roof_load_lb;
  const rows = v.rows_seating;
  switch (slug) {
    case "tonneau-covers":
      return `Covers are matched to the ${v.model_name}'s bed length${beds ? ` (${beds})` : ""} — the one spec that beats brand or style. Soft roll-ups are cheapest, hard tri-folds are the sweet spot, retractables seal best.`;
    case "bed-racks":
      return `Bed racks turn the ${v.model_name} into an overland platform for rooftop tents and cargo. Height decides everything: low-profile for MPG, mid-height for tent + tailgate access, full-height for max storage.`;
    case "roof-racks":
      return `The ${gen} ${v.model_name} has ${roofPhrase}${roofLoad ? ` rated ${roofLoad} lb dynamic` : ""}, which dictates the crossbar style. Every kit here matches that roof type — no drilling, no guessing.`;
    case "cargo-boxes":
      return `Boxes are universal; the crossbars are what fit the ${v.model_name}. Pick bars for ${roofPhrase} first, then a box under your roof-load limit${roofLoad ? ` (${roofLoad} lb incl. bars)` : ""}.`;
    case "hitches": {
      // attrs.hitch_blurb (optional) replaces the generic sentence on vehicles where it would be wrong or unsafe.
      const note = typeof v.attrs?.hitch_blurb === "string" ? v.attrs.hitch_blurb : "Aftermarket hitches bolt to existing frame holes for bike racks, carriers and light towing — the vehicle rating never rises.";
      return `${v.model_name} hitch facts: ${hitch}${tow ? `, factory max tow ${tow}` : ""}. ${note}`;
    }
    case "bike-racks":
      return `Hitch-mount racks need a receiver (${hitch}); roof racks need crossbars. For e-bikes, hitch mounts only.`;
    case "floor-mats":
      return `Laser-fit liners for the ${gen} ${v.model_name}, ${rows}-row. Previous-generation mats do not fit — every set here is listed for these model years.`;
    case "seat-covers":
      return `Custom-fit covers for the ${gen} ${v.model_name} seats, with airbag-compatible seams and headrest cutouts matched to this generation.`;
    case "running-boards":
      return `Boards and steps bolt to the ${v.model_name}'s factory rocker mounts — no drilling on most kits. Cab length decides the board length.`;
    case "led-light-bars":
      return `Light bars for the ${v.model_name} are a bracket question, not a bar question: hood, bumper or windshield mounts are vehicle-specific; the bars are universal. Check your state's aux-light rules before wiring.`;
    case "dash-cams":
      return `Dash cams are universal; the hardwire kit must match the ${v.model_name}'s fuse type. Parking mode needs a constant-power fuse tap.`;
    case "lift-kits":
      return `Leveling and lift kits for the ${gen} ${v.model_name}${v.tire_size ? ` (stock ${v.tire_size})` : ""} — check tire clearance and alignment needs before buying.`;
    default:
      return `Accessories verified to fit the ${gen} ${v.model_name}.`;
  }
}

export function checkBeforeBuying(v: Vehicle): string[] {
  const out: string[] = [];
  if (v.bed_lengths_in?.length > 1) out.push(`Measure your bed inside, bulkhead to tailgate: ${v.bed_lengths_in.map(b => `${b} in = ${(b / 12).toFixed(1)} ft`).join(", ")}.`);
  const a = v.attrs ?? {};
  // attrs.roof_check (optional) replaces the generic roof-type line where it would contradict the guides.
  if (typeof a.roof_check === "string") out.push(a.roof_check);
  else if (v.roof_type === "raised-rails") out.push("Confirm your trim has the raised side rails — base trims sometimes ship bare-roof and need a different crossbar kit.");
  else if (v.roof_type === "removable") out.push("Roof is removable: racks mount to the hardtop or the body, and soft tops take no rack at all.");
  else if (v.roof_type === "flush-rails") out.push("Flush side rails (no gap under the rail): only flush-rail crossbar kits fit — raised-rail clamp bars will not grip.");
  else if (v.roof_type === "fixed-points") out.push("Glass roof with fixed mounting points — only fixed-point crossbar kits, never clamp or door-jamb bars.");
  // attrs.hitch_check (optional) replaces the generic receiver line.
  if (typeof a.hitch_check === "string") out.push(a.hitch_check);
  else if (v.hitch_class && v.hitch_class !== "none") out.push(`Check for a factory receiver under the rear bumper before buying a hitch (${v.receiver_in} in on tow-package vehicles).`);
  if (v.rows_seating === 3) out.push("Three-row: buy 3-row mat sets; 2-row sets leave the third row bare.");
  if (a.rambox) out.push("RamBox trucks need RamBox-specific covers and racks.");
  if (a.bed_utility_track) out.push("Optional bed utility track blocks most clamp-on cover rails.");
  if (a.carbonpro_fit_warning) out.push("CarbonPro composite beds need CarbonPro-listed covers.");
  if (a.trail_rail) out.push("Trail Rail cargo system changes cover and rack fit.");
  if (a.hybrid) out.push(`Hybrid variant: ${a.hybrid} — cargo-area fitments can differ.`);
  if (a.fit_note) out.push(String(a.fit_note));
  return out;
}
