"use client";
import { useRouter } from "next/navigation";

export function VehiclePicker({ vehicles }: { vehicles: { label: string; path: string }[] }) {
  const router = useRouter();
  return (
    <div className="select" style={{ justifyContent: "center" }}>
      <select defaultValue="" onChange={e => e.target.value && router.push(e.target.value)} aria-label="Pick your vehicle">
        <option value="" disabled>Select your vehicle…</option>
        {vehicles.map(v => <option key={v.path} value={v.path}>{v.label}</option>)}
      </select>
    </div>
  );
}
