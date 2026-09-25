"""Generate static 1200x630 Open Graph cards for pages without a vehicle photo.
Run: python3 tools/make_og.py  → web/public/og/*.jpg (commit the output)."""
from PIL import Image, ImageDraw, ImageFont
import os
F = "/usr/share/fonts/truetype/google-fonts/Poppins-{}.ttf"
BG, CARD, LINE, FG, MUTED, ACC = "#0f1115", "#171a21", "#262b35", "#e8eaf0", "#9aa3b2", "#f5a524"
OUT = os.path.join(os.path.dirname(__file__), "..", "web", "public", "og")

def wrap(d, text, font, width):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= width: cur = t
        else: lines.append(cur); cur = w
    return lines + [cur]

def card(name, title, sub):
    im = Image.new("RGB", (1200, 630), BG); d = ImageDraw.Draw(im)
    d.rounded_rectangle((40, 40, 1160, 590), 28, fill=CARD, outline=LINE, width=2)
    d.rectangle((40, 40, 56, 590), fill=ACC)
    brand = ImageFont.truetype(F.format("Bold"), 38)
    d.text((96, 84), "Rig", font=brand, fill=FG); d.text((96 + d.textlength("Rig", font=brand), 84), "Configurator", font=brand, fill=ACC)
    size = 76
    while True:
        tf = ImageFont.truetype(F.format("Bold"), size); lines = wrap(d, title, tf, 1000)
        if len(lines) <= 3 or size <= 52: break
        size -= 6
    y = 190
    for l in lines: d.text((96, y), l, font=tf, fill=FG); y += int(size * 1.18)
    sf = ImageFont.truetype(F.format("Regular"), 32)
    for l in wrap(d, sub, sf, 1000)[:2]: d.text((96, y + 20), l, font=sf, fill=MUTED); y += 44
    d.text((96, 520), "rigconfigurator.com", font=ImageFont.truetype(F.format("Medium"), 28), fill=MUTED)
    im.save(os.path.join(OUT, f"{name}.jpg"), quality=86, optimize=True, progressive=True)

card("default", "Parts that actually fit your rig", "Fit-checked racks, hitches, tonneau covers, floor liners and steps for your exact truck or SUV generation.")
card("guides", "Accessory guides by category", "Every guide is written for one vehicle generation, with the fit gotchas for it.")
card("vehicles", "Truck & SUV accessories by vehicle", "Pick your generation to see only the parts listed to fit it.")
for slug, t in {"tonneau-covers": "Tonneau Covers", "bed-racks": "Bed Racks", "roof-racks": "Roof Racks & Crossbars", "cargo-boxes": "Cargo Boxes",
                "hitches": "Trailer Hitches", "floor-mats": "Floor Mats & Liners", "running-boards": "Running Boards & Steps", "led-light-bars": "LED Light Bars"}.items():
    card(f"guide-{slug}", f"{t} by vehicle", "Matched to your exact generation: fit rules, common mistakes and fit-checked picks.")
print(sorted(os.listdir(OUT)))
