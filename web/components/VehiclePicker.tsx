"use client";
import { useMemo, useState } from "react";
import { useRouter } from "next/navigation";

export type PickerVehicle = { make: string; label: string; path: string };

// Two-step picker: make, then generation. One click to the vehicle hub, where every product is fit-checked.
export function VehiclePicker({ vehicles, compact = false, cta = "Show parts that fit →" }: { vehicles: PickerVehicle[]; compact?: boolean; cta?: string }) {
  const router = useRouter();
  const makes = useMemo(() => [...new Set(vehicles.map(v => v.make))].sort(), [vehicles]);
  const [make, setMake] = useState("");
  const [path, setPath] = useState("");
  const models = useMemo(() => vehicles.filter(v => v.make === make), [vehicles, make]);
  const go = () => { if (path) router.push(path); };
  return (
    <form className={`picker${compact ? " picker-compact" : ""}`} onSubmit={e => { e.preventDefault(); go(); }} aria-label="Find parts for your vehicle">
      <label className="picker-field">
        <span>Make</span>
        <select value={make} onChange={e => { setMake(e.target.value); setPath(""); }} aria-label="Make">
          <option value="" disabled>Choose a make</option>
          {makes.map(m => <option key={m} value={m}>{m}</option>)}
        </select>
      </label>
      <label className="picker-field">
        <span>Model and years</span>
        <select value={path} onChange={e => setPath(e.target.value)} disabled={!make} aria-label="Model and years">
          <option value="" disabled>{make ? "Choose your model" : "Pick a make first"}</option>
          {models.map(v => <option key={v.path} value={v.path}>{v.label.replace(`${v.make} `, "")}</option>)}
        </select>
      </label>
      <button type="submit" className="btn btn-lg" disabled={!path}>{cta}</button>
    </form>
  );
}
