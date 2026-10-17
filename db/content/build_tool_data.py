"""Generate web/lib/toolData.json for the tongue weight and roof load calculators from the two chart pillars
(factory_tow_hitch_by_vehicle.py, roof_load_limits_by_vehicle.py), so the calculators and the charts never disagree.
A number is extracted only where the chart cell starts with one; every row also carries the cell text, which the
calculators show verbatim as the source note. Run after editing either pillar."""
import importlib.util, json, os, re
here = os.path.dirname(__file__)

def load(name):
    p = os.path.join(here, "pillars", name)
    s = importlib.util.spec_from_file_location(name[:-3], p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.ARTICLE["compare_table"]

def key(vehicle: str, year_from: int) -> str:
    v = vehicle.replace("Chevy ", "Chevrolet ")
    v = re.sub(r"^\d{4}–\d{4}\s+", "", v)
    v = re.sub(r"\s+(JL|WL|JT)$", "", v)
    return f"{v.lower()} {year_from}"

def first_int(cell: str):
    if re.match(r"\s*\d{4}[–-]\d{4}", cell): return None   # a model-year range, not a figure ("2018–2023: 2,000 ...")
    m = re.match(r"\s*(?:Up to\s+)?([\d,]+)", cell)
    return int(m.group(1).replace(",", "")) if m else None

tow, roof = {}, {}
t = load("factory_tow_hitch_by_vehicle.py")
for r in t["rows"]:
    vehicle, gen, receiver, size, max_tow, tongue, source = r[0], r[1], r[2], r[3], r[4], r[5], r[6]
    y = int(re.match(r"(\d{4})", gen).group(1))
    tow[key(vehicle, y)] = {"receiver": receiver, "size": size, "max_tow_lb": first_int(max_tow), "max_tow": max_tow,
                            "tongue_lb": None if tongue.lower().startswith(("not published", "in the owner")) else first_int(tongue),
                            "tongue": tongue, "carrier_lb": (int(m.group(1)) if (m := re.search(r"carriers? up to (\d+)", tongue)) else None), "source": source}
t = load("roof_load_limits_by_vehicle.py")
for r in t["rows"]:
    vehicle, roof_type, load_, covers, source = r[0], r[2], r[3], r[4], r[5]
    y = int(re.match(r"(\d{4})", vehicle).group(1))
    roof[key(vehicle, y)] = {"roof_type": roof_type, "roof_lb": first_int(load_), "roof": load_, "covers": covers, "source": source,
                             "confirmed": first_int(load_) is not None and not source.lower().startswith("not confirmed")}
out = os.path.join(here, "..", "..", "web", "lib", "toolData.json")
json.dump({"tow": tow, "roof": roof}, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"wrote toolData.json: {len(tow)} tow rows, {len(roof)} roof rows")
