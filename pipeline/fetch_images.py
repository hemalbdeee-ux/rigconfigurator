"""Hero photos for every vehicle generation from Wikimedia Commons — licensed, attributed, quality-gated.

Why Commons (not Bing/Google Images): search-engine results are mostly copyrighted press/dealer photos with
no reuse right. Commons files carry an explicit free license (CC BY / CC BY-SA / CC0 / PD) plus author
metadata, so we can publish them with a credit line.

Quality gates (all must pass): JPEG · ≥1600×900 px · landscape 1.3–2.1 · free license · file title names the
model · no interior/detail/toy/damaged shots. Survivors are scored (year match, "front"/3-4 view, size).
Best score ≥ AUTO_APPROVE with a model year inside the generation is approved automatically; the rest wait in data/img/review.html.

Run inside the pipeline container:
  python fetch_images.py                 # all vehicles without an approved image
  python fetch_images.py --redo ford/f-150/2021-present
  python fetch_images.py --approve 123   # approve candidate id 123 (see review.html)
"""
import html, io, json, os, re, sys, time
import requests
from PIL import Image
from common import conn, revalidate

API = "https://commons.wikimedia.org/w/api.php"
UA = {"User-Agent": "RigConfiguratorBot/1.0 (https://rigconfigurator.com/about)"}
IMG_DIR = os.environ.get("IMG_DIR", "/app/data/img")
AUTO_APPROVE = 6.0
FREE = re.compile(r"^(cc0|public domain|pd|cc by(-sa)? ?\d(\.\d)?)", re.I)
BAD = re.compile(r"\b(interior|dashboard|cockpit|engine|motor|badge|logo|emblem|wheels?|rims?|seats?|tail ?lights?|headlights?|"
                 r"details?|crash|wreck|damaged|burnt?|police|sheriff|fire|ambulance|toys?|lego|diecast|model car|"
                 r"drawing|diagram|sketch|render|concept|prototype|patent|bed|trunk|cargo area|steering)\b", re.I)  # word-bounded: "toy" must not hit "Toyota"


def model_tokens(model_name):
    # "Silverado 1500" -> ["silverado"], "F-150" -> ["f-150","f150"], "4Runner" -> ["4runner"], "Model Y" -> ["model y"]
    m = model_name.lower()
    base = m.split(" 1500")[0].strip()
    toks = {base, base.replace("-", ""), base.replace("-", " ")}
    return [t for t in toks if t]


def search(q, limit=40):
    r = requests.get(API, headers=UA, timeout=30, params={
        "action": "query", "format": "json", "generator": "search", "gsrsearch": f"{q} filetype:bitmap",
        "gsrnamespace": 6, "gsrlimit": limit, "prop": "imageinfo",
        "iiprop": "url|size|mime|extmetadata", "iiurlwidth": 1600})
    r.raise_for_status()
    return list((r.json().get("query") or {}).get("pages", {}).values())


def meta(ii, key):
    v = (ii.get("extmetadata") or {}).get(key, {}).get("value", "")
    return html.unescape(re.sub(r"<[^>]+>", "", str(v))).strip()


def score(page, v, toks):
    ii = (page.get("imageinfo") or [{}])[0]
    title = page.get("title", "")
    t = title.lower()
    w, h = ii.get("width", 0), ii.get("height", 0)
    lic = meta(ii, "LicenseShortName")
    if ii.get("mime") != "image/jpeg" or w < 1600 or h < 900: return None
    if not (1.3 <= w / max(h, 1) <= 2.1): return None
    if not FREE.match(lic): return None
    if not any(tok in t for tok in toks): return None
    if BAD.search(t): return None
    if v["make_name"].lower() not in t and v["make_slug"] not in t: return None
    s = 3.0
    yrs = [int(y) for y in re.findall(r"\b((?:19|20)\d\d)\b", title)]
    y_to = v["year_to"] or 2026
    if yrs:
        s += 3.0 if any(v["year_from"] <= y <= y_to for y in yrs) else -4.0
    if re.search(r"front|3/4|three.quarter|\bfr\b", t): s += 1.5
    if re.search(r"\brear\b|\bback\b|\bside\b", t): s -= 1.0
    s += min(w / 1600, 3) * 0.5
    if any(x in t for x in (v["gen_name"] or "").lower().split() if len(x) > 3): s += 0.5
    year_ok = bool(yrs) and any(v["year_from"] <= y <= y_to for y in yrs)
    return {"title": title, "score": round(s, 2), "year_ok": year_ok, "w": w, "h": h, "thumb": ii.get("thumburl"), "desc": ii.get("descriptionurl"),
            "author": meta(ii, "Artist")[:200] or "Unknown", "license": lic, "license_url": meta(ii, "LicenseUrl")}


def save(cand, slug):
    raw = requests.get(cand["thumb"], headers=UA, timeout=60).content
    im = Image.open(io.BytesIO(raw)).convert("RGB")
    os.makedirs(os.path.join(IMG_DIR, "vehicles"), exist_ok=True)
    rel = f"vehicles/{slug}.webp"
    im.thumbnail((1600, 1600)); im.save(os.path.join(IMG_DIR, rel), "WEBP", quality=82, method=6)
    small = im.copy(); small.thumbnail((800, 800)); small.save(os.path.join(IMG_DIR, f"vehicles/{slug}-800.webp"), "WEBP", quality=80, method=6)
    # 1200x630 social crop (center)
    W, H = im.size; tw = min(W, int(H * 1200 / 630)); th = int(tw * 630 / 1200)
    og = im.crop(((W - tw) // 2, (H - th) // 2, (W + tw) // 2, (H + th) // 2)).resize((1200, 630))
    og.save(os.path.join(IMG_DIR, f"vehicles/{slug}-og.jpg"), "JPEG", quality=85)
    return rel, im.size


def vehicles(c, only=None):
    rows = c.execute("""SELECT v.id, m.slug make_slug, m.name make_name, v.model_slug, v.model_name, v.gen_slug, v.gen_name, v.year_from, v.year_to
                        FROM vehicles v JOIN makes m ON m.id=v.make_id ORDER BY m.slug, v.model_slug, v.year_from""").fetchall()
    cols = ["id", "make_slug", "make_name", "model_slug", "model_name", "gen_slug", "gen_name", "year_from", "year_to"]
    out = [dict(zip(cols, r)) for r in rows]
    if only: out = [v for v in out if f"{v['make_slug']}/{v['model_slug']}/{v['gen_slug']}" == only]
    return out


def run(only=None):
    touched = set()
    with conn() as c:
        for v in vehicles(c, only):
            if not only and c.execute("SELECT 1 FROM vehicle_images WHERE vehicle_id=%s AND status='approved'", (v["id"],)).fetchone():
                continue
            if only: c.execute("UPDATE vehicle_images SET status='candidate' WHERE vehicle_id=%s AND status='approved'", (v["id"],))
            toks = model_tokens(v["model_name"])
            y_to = v["year_to"] or 2025
            queries = [f"{v['make_name']} {v['model_name']} {y}" for y in sorted({v['year_from'], min(v['year_from'] + 1, y_to), y_to})]
            queries.append(f"{v['make_name']} {v['model_name']} {v['gen_name']}")
            seen, cands = set(), []
            for q in queries:
                try: pages = search(q)
                except Exception as e: print("search failed", q, e); continue
                for p in pages:
                    if p.get("title") in seen: continue
                    seen.add(p.get("title")); s = score(p, v, toks)
                    if s: cands.append(s)
                time.sleep(0.5)
            cands.sort(key=lambda x: -x["score"])
            slug = f"{v['make_slug']}-{v['model_slug']}-{v['gen_slug']}"
            for i, cd in enumerate(cands[:3]):
                c.execute("""INSERT INTO vehicle_images (vehicle_id, file, width, height, source_url, title, author, license, license_url, score, status)
                             VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'candidate') ON CONFLICT (vehicle_id, source_url) DO UPDATE SET score=EXCLUDED.score""",
                          (v["id"], cd["thumb"], cd["w"], cd["h"], cd["desc"], cd["title"], cd["author"], cd["license"], cd["license_url"], cd["score"]))
            best = cands[0] if cands else None
            if best and best["score"] >= AUTO_APPROVE and best["year_ok"]:  # never auto-approve an undated photo (could be another generation)
                rel, (w, h) = save(best, slug)
                c.execute("UPDATE vehicle_images SET status='approved', file=%s, width=%s, height=%s WHERE vehicle_id=%s AND source_url=%s",
                          (rel, w, h, v["id"], best["desc"]))
                touched.add(f"/vehicles/{v['make_slug']}/{v['model_slug']}/{v['gen_slug']}")
                print(f"✔ {slug}: {best['title']} ({best['license']}, score {best['score']})")
            else:
                print(f"… {slug}: {len(cands)} candidate(s), best {best['score'] if best else '-'} — review needed")
        review(c)
    revalidate(touched)


def approve(img_id):
    with conn() as c:
        r = c.execute("""SELECT vi.vehicle_id, vi.file, vi.source_url, vi.title, vi.author, vi.license, vi.license_url, vi.score,
                                m.slug, v.model_slug, v.gen_slug
                         FROM vehicle_images vi JOIN vehicles v ON v.id=vi.vehicle_id JOIN makes m ON m.id=v.make_id WHERE vi.id=%s""", (img_id,)).fetchone()
        if not r: sys.exit(f"no image {img_id}")
        vid, thumb, desc, title, author, lic, lic_url, sc, mk, md, gn = r
        if not thumb.startswith("http"): sys.exit("already saved locally; use --redo to refetch candidates")
        rel, (w, h) = save({"thumb": thumb}, f"{mk}-{md}-{gn}")
        c.execute("UPDATE vehicle_images SET status='candidate' WHERE vehicle_id=%s AND status='approved'", (vid,))
        c.execute("UPDATE vehicle_images SET status='approved', file=%s, width=%s, height=%s WHERE id=%s", (rel, w, h, img_id))
        print(f"approved {img_id} for {mk}/{md}/{gn}")
        review(c)
    revalidate({f"/vehicles/{mk}/{md}/{gn}"})


def review(c):
    """Contact sheet: every vehicle, approved image + candidates, with the id to pass to --approve."""
    rows = c.execute("""SELECT vi.id, m.name||' '||v.model_name||' '||v.gen_slug, vi.file, vi.title, vi.license, vi.author, vi.score, vi.status, vi.source_url
                        FROM vehicle_images vi JOIN vehicles v ON v.id=vi.vehicle_id JOIN makes m ON m.id=v.make_id
                        ORDER BY m.name, v.model_name, v.year_from, vi.status='approved' DESC, vi.score DESC""").fetchall()
    missing = c.execute("""SELECT m.name||' '||v.model_name||' '||v.gen_slug FROM vehicles v JOIN makes m ON m.id=v.make_id
                           WHERE NOT EXISTS (SELECT 1 FROM vehicle_images vi WHERE vi.vehicle_id=v.id AND vi.status='approved')""").fetchall()
    cards = []
    for i, name, f, title, lic, author, sc, st, src in rows:
        img = f"vehicles/{os.path.basename(f)}" if not f.startswith("http") else f
        cards.append(f'<div class="c {st}"><img src="{html.escape(img)}" loading="lazy"><b>{html.escape(name)}</b><br>#{i} · {st} · score {sc}<br>'
                     f'<small>{html.escape(title)}<br>{html.escape(lic)} · {html.escape(author)}</small><br><a href="{src}">source</a></div>')
    page = ("<meta charset=utf-8><title>Image review</title><style>body{font:14px system-ui;background:#111;color:#eee}"
            ".g{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:12px}.c{background:#1b1b1b;padding:8px;border-radius:8px}"
            ".c img{width:100%;aspect-ratio:16/9;object-fit:cover}.approved{outline:3px solid #3ecf8e}a{color:#f5a524}</style>"
            f"<h1>Vehicle hero images</h1><p>Missing approved image: {html.escape(', '.join(m[0] for m in missing)) or 'none'}</p>"
            "<p>Approve a candidate: <code>docker exec rigconfigurator-pipeline python fetch_images.py --approve ID</code></p>"
            f"<div class=g>{''.join(cards)}</div>")
    os.makedirs(IMG_DIR, exist_ok=True)
    open(os.path.join(IMG_DIR, "review.html"), "w", encoding="utf-8").write(page)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["--approve"]: approve(int(a[1]))
    elif a[:1] == ["--redo"]: run(a[1])
    else: run()
