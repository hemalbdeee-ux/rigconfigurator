"use client";
import { useMemo, useState } from "react";

/** One vehicle as the calculators see it: figures come from the chart pillars (lib/toolData.json), never typed here. */
export type CalcVehicle = {
  id: number; make: string; label: string; hub: string; hitchGuide?: string; roofGuide?: string;
  tow?: { max_tow_lb: number | null; max_tow: string; tongue_lb: number | null; tongue: string; carrier_lb?: number | null; receiver: string; size: string } | null;
  roof?: { roof_lb: number | null; roof: string; roof_type: string; covers: string; confirmed: boolean } | null;
};

const num = (s: string) => { const n = Number(s.replace(/,/g, "")); return Number.isFinite(n) && n > 0 ? n : 0; };
const fmt = (n: number) => Math.round(n).toLocaleString("en-US");

function VehicleSelect({ vehicles, value, onChange }: { vehicles: CalcVehicle[]; value: number; onChange: (id: number) => void }) {
  const makes = useMemo(() => [...new Set(vehicles.map(v => v.make))].sort(), [vehicles]);
  return (
    <label className="calc-field calc-wide">
      <span>Your vehicle</span>
      <select value={value || ""} onChange={e => onChange(Number(e.target.value))}>
        <option value="" disabled>Choose your truck or SUV</option>
        {makes.map(m => <optgroup key={m} label={m}>{vehicles.filter(v => v.make === m).map(v => <option key={v.id} value={v.id}>{v.label}</option>)}</optgroup>)}
      </select>
    </label>
  );
}

function Meter({ used, limit }: { used: number; limit: number }) {
  const pct = limit > 0 ? used / limit : 0;
  const cls = pct > 1 ? "over" : pct > 0.85 ? "near" : "ok";
  return (
    <div className={`meter ${cls}`} role="img" aria-label={`${Math.round(pct * 100)} percent of the limit`}>
      <div className="meter-fill" style={{ width: `${Math.min(100, pct * 100)}%` }} />
      <span className="meter-label">{fmt(used)} of {fmt(limit)} lb · {Math.round(pct * 100)}%</span>
    </div>
  );
}

export function TongueCalc({ vehicles }: { vehicles: CalcVehicle[] }) {
  const [id, setId] = useState(0);
  const [mode, setMode] = useState<"trailer" | "carrier">("trailer");
  const [trailer, setTrailer] = useState("3500");
  const [carrier, setCarrier] = useState("55");
  const [cargo, setCargo] = useState("110");
  const [manual, setManual] = useState("");
  const v = vehicles.find(x => x.id === id);
  const t = v?.tow ?? null;
  // A hitch carrier is held to the maker's carrier figure where one exists (Tesla prints one below the trailer tongue figure).
  const tongueLimit = num(manual) || (mode === "carrier" && t?.carrier_lb) || t?.tongue_lb || 0;
  const tw = num(trailer), lo = tw * 0.10, hi = tw * 0.15;
  const vertical = num(carrier) + num(cargo);

  return (
    <div className="calc">
      <div className="calc-row">
        <VehicleSelect vehicles={vehicles} value={id} onChange={i => { setId(i); setManual(""); }} />
        <div className="calc-field">
          <span>What goes on the hitch?</span>
          <div className="seg">
            <button type="button" className={mode === "trailer" ? "on" : ""} onClick={() => setMode("trailer")}>A trailer</button>
            <button type="button" className={mode === "carrier" ? "on" : ""} onClick={() => setMode("carrier")}>Bike rack / cargo carrier</button>
          </div>
        </div>
      </div>

      {mode === "trailer" ? (
        <div className="calc-row">
          <label className="calc-field"><span>Loaded trailer weight (lb)</span><input inputMode="numeric" value={trailer} onChange={e => setTrailer(e.target.value)} /></label>
          <label className="calc-field"><span>Tongue limit from your manual or hitch label (lb, optional)</span><input inputMode="numeric" placeholder={t?.tongue_lb ? String(t.tongue_lb) : "e.g. 500"} value={manual} onChange={e => setManual(e.target.value)} /></label>
        </div>
      ) : (
        <div className="calc-row">
          <label className="calc-field"><span>Carrier or rack weight (lb)</span><input inputMode="numeric" value={carrier} onChange={e => setCarrier(e.target.value)} /></label>
          <label className="calc-field"><span>Bikes or cargo on it (lb)</span><input inputMode="numeric" value={cargo} onChange={e => setCargo(e.target.value)} /></label>
          <label className="calc-field"><span>Tongue limit from your manual or hitch label (lb, optional)</span><input inputMode="numeric" placeholder={t?.tongue_lb ? String(t.tongue_lb) : "e.g. 350"} value={manual} onChange={e => setManual(e.target.value)} /></label>
        </div>
      )}

      <div className="calc-out" aria-live="polite">
        {mode === "trailer" ? (<>
          <div className="calc-big">Target tongue weight: <strong>{fmt(lo)}–{fmt(hi)} lb</strong></div>
          <p className="muted">10 to 15 percent of a {fmt(tw)} lb loaded trailer, the range most trailer and hitch makers give for a stable conventional trailer. Less than 10 percent tends to sway; more overloads the rear axle and the hitch.</p>
          {v && t?.max_tow_lb ? (
            <p>{tw > t.max_tow_lb
              ? <><strong className="bad">Over the tow rating.</strong> {fmt(tw)} lb is above the {fmt(t.max_tow_lb)} lb maximum in our chart for the {v.label}.</>
              : <><strong className="good">Under the tow rating.</strong> {fmt(tw)} lb is {Math.round(tw / t.max_tow_lb * 100)}% of the {fmt(t.max_tow_lb)} lb maximum in our chart for the {v.label}.</>}
              {" "}<span className="muted">Chart note: {t.max_tow}</span></p>
          ) : v ? <p className="muted">Our chart has no single tow figure for this vehicle: {t?.max_tow ?? "not stored"}. Use the owner&apos;s manual.</p> : null}
          {v && tongueLimit > 0 && <><Meter used={hi} limit={tongueLimit} /><p className="muted">Upper end of the target range against a {fmt(tongueLimit)} lb tongue limit{num(manual) ? " (the figure you entered)" : ` (chart: ${t?.tongue})`}.</p></>}
        </>) : (<>
          <div className="calc-big">Load on the hitch: <strong>{fmt(vertical)} lb</strong></div>
          <p className="muted">A hitch-mounted carrier puts its whole weight on the receiver: the carrier plus everything on it, and it sits further back than a trailer coupler, which adds leverage.</p>
          {v && tongueLimit > 0 && <><Meter used={vertical} limit={tongueLimit} /><p className="muted">Against {num(manual) ? "the figure you entered" : t?.carrier_lb ? `the maker's ${fmt(t.carrier_lb)} lb carrier limit` : `the ${fmt(tongueLimit)} lb tongue figure in our chart`}.</p></>}
          {v && tongueLimit > 0 && <p>{vertical > tongueLimit
            ? <><strong className="bad">Over the limit.</strong> Lighten the load or use a lighter carrier.</>
            : <><strong className="good">Within the limit</strong>, with {fmt(tongueLimit - vertical)} lb to spare.</>}</p>}
        </>)}
        {v && (
          <div className="calc-src">
            <div><strong>Hitch on the {v.label}:</strong> {t ? t.receiver : "not in our chart"}</div>
            {t && <div><strong>Receiver:</strong> {t.size}</div>}
            <div><strong>Tongue figure in our chart:</strong> {t?.tongue ?? "not in our chart"}</div>
            {!t?.tongue_lb && !num(manual) && <div className="muted">No maker tongue figure on the pages we read. Enter the figure from your manual or the hitch label above to check your load.</div>}
            <div className="calc-links">{v.hitchGuide && <a href={v.hitchGuide}>Hitches that fit the {v.label} →</a>} <a href={v.hub}>All {v.label} fit facts →</a></div>
          </div>
        )}
      </div>
    </div>
  );
}

export function RoofCalc({ vehicles }: { vehicles: CalcVehicle[] }) {
  const [id, setId] = useState(0);
  const [rack, setRack] = useState("15");
  const [carrier, setCarrier] = useState("45");
  const [cargo, setCargo] = useState("60");
  const [rackRating, setRackRating] = useState("165");
  const [manual, setManual] = useState("");
  const v = vehicles.find(x => x.id === id);
  const r = v?.roof ?? null;
  const vehicleLimit = num(manual) || r?.roof_lb || 0;
  const rr = num(rackRating);
  const limit = vehicleLimit && rr ? Math.min(vehicleLimit, rr) : vehicleLimit || rr;
  const total = num(rack) + num(carrier) + num(cargo);
  const which = vehicleLimit && rr ? (rr < vehicleLimit ? "the rack rating" : "the vehicle figure") : vehicleLimit ? "the vehicle figure" : "the rack rating";

  return (
    <div className="calc">
      <div className="calc-row"><VehicleSelect vehicles={vehicles} value={id} onChange={i => { setId(i); setManual(""); }} /></div>
      <div className="calc-row">
        <label className="calc-field"><span>Crossbars or platform (lb)</span><input inputMode="numeric" value={rack} onChange={e => setRack(e.target.value)} /></label>
        <label className="calc-field"><span>Cargo box, tent or bike mounts (lb)</span><input inputMode="numeric" value={carrier} onChange={e => setCarrier(e.target.value)} /></label>
        <label className="calc-field"><span>What you put in or on it (lb)</span><input inputMode="numeric" value={cargo} onChange={e => setCargo(e.target.value)} /></label>
      </div>
      <div className="calc-row">
        <label className="calc-field"><span>Rack system rating (lb)</span><input inputMode="numeric" value={rackRating} onChange={e => setRackRating(e.target.value)} /></label>
        <label className="calc-field"><span>Roof limit from your manual (lb, optional)</span><input inputMode="numeric" placeholder={r?.roof_lb ? String(r.roof_lb) : "e.g. 165"} value={manual} onChange={e => setManual(e.target.value)} /></label>
      </div>

      <div className="calc-out" aria-live="polite">
        <div className="calc-big">Total on the roof while driving: <strong>{fmt(total)} lb</strong></div>
        {limit > 0 ? (<>
          <Meter used={total} limit={limit} />
          <p>{total > limit
            ? <><strong className="bad">Over by {fmt(total - limit)} lb.</strong> The limit here is {fmt(limit)} lb, set by {which}.</>
            : <><strong className="good">Within the limit</strong> of {fmt(limit)} lb, set by {which}, with {fmt(limit - total)} lb to spare.</>}</p>
        </>) : <p className="muted">Enter a rack rating or a roof figure to check the load.</p>}
        <p className="muted">The dynamic (driving) limit counts everything above the roof: bars, feet, platform, box or tent, and the cargo. A parked rooftop tent with people in it is a separate static figure, which only a few makers print.</p>
        {v && (
          <div className="calc-src">
            <div><strong>Roof on the {v.label}:</strong> {r?.roof_type ?? "not in our chart"}</div>
            <div><strong>Roof figure in our chart:</strong> {r ? r.roof : "not in our chart"}{r?.roof_lb && !r.confirmed ? " (not confirmed by the maker)" : ""}</div>
            {r?.covers && <div className="muted">{r.covers}</div>}
            {!r?.roof_lb && !num(manual) && <div className="muted">No maker roof figure on the pages we read. The check above uses the rack rating only; your owner&apos;s manual may set a lower limit.</div>}
            <div className="calc-links">{v.roofGuide && <a href={v.roofGuide}>Roof racks that fit the {v.label} →</a>} <a href={v.hub}>All {v.label} fit facts →</a></div>
          </div>
        )}
      </div>
    </div>
  );
}
