# Wayback Restore

Download and restore a **complete website** from the Internet Archive's Wayback Machine. You get every page, image, stylesheet, script and font, with links rewritten so the site works offline or on new hosting. It comes as a folder plus a ZIP.

It has a web app (enter a domain, watch progress, preview, download the ZIP) and a command-line tool that share one engine.

## How it restores a site

1. **Index.** It queries the Wayback CDX API for every successful (HTTP 200) capture of the domain, paging with `resumeKey` so sites with millions of captures work.
2. **Pick one capture per URL.** It takes the newest by default. With a date, it takes the latest capture at or before that moment, and falls back to the first capture after it. `www.` and the bare domain are treated as the same site.
3. **Download raw files.** It uses `https://web.archive.org/web/<ts>id_/<url>`. The `id_` flag returns the original bytes without the archive toolbar or rewritten links. Downloads run in parallel with a shared rate limit, and it retries with backoff on 429/5xx, honouring `Retry-After`.
4. **Fill gaps.** The CDX index often misses files, such as fonts loaded from CSS, `srcset` images and `@import`s. It scans the downloaded HTML and CSS for links on the same site and fetches those too, for up to 3 rounds.
5. **Rewrite links.** Every `href`, `src`, `srcset`, `data-src`, `poster`, `action`, inline `style`, `<style>` block, CSS `url()` / `@import` and meta refresh that points to a restored file becomes a relative path. It unwraps any `web.archive.org/web/…` links and removes `<base>` tags and leftover toolbar code. It changes only the links: the rest of the markup stays byte-for-byte as archived, and the original encoding is kept.
6. **Package.** It writes `site/`, `report.json` (listing files that couldn't be restored), an `.htaccess` for Apache hosting, and `<domain>.zip`.

URL → file mapping: `/` → `index.html`, `/about` → `about/index.html`, `/page.php?id=3` → `page_q_id=3.php.html`, and `cdn.example.com/x.png` → `_hosts/cdn.example.com/x.png` when subdomains are included.

Jobs can resume. Progress is saved to `manifest.json`, and running the same job again only downloads what is missing.

## Command line

```bash
pip install -r requirements.txt
python -m wayback example.com                                  # latest version of every page
python -m wayback https://web.archive.org/web/20190615000000/example.com/   # as it looked on that date
python -m wayback example.com -t 2016 --subdomains --skip-media -o ./out
python -m wayback example.com/blog/                            # only a section
```

Options: `--from/--to` (limit the capture window), `--max-files`, `--workers` (default 4), `--delay` (seconds between requests), `--no-missing`, `--no-zip`. Press Ctrl+C to stop, then run the same command again to resume.

## Web app

```bash
pip install -r requirements.txt
uvicorn app.server:app --port 8000          # http://localhost:8000
# or
docker compose up -d --build
```

| Env var | Default | Meaning |
|---|---|---|
| `SITE_NAME` | `Wayback Restore` | Brand name shown in the page |
| `MAX_PARALLEL_JOBS` | `2` | Restores running at once (others queue) |
| `MAX_FILES_PER_JOB` | `0` (no limit) | Cap per restore, useful for a free tier |
| `JOB_TTL_HOURS` | `48` | Finished jobs and ZIPs are deleted after this |
| `DATA_DIR` | `data` (`/data` in Docker) | Where jobs are stored |
| `WAYBACK_BASE` | `https://web.archive.org` | Archive endpoint (tests point this at a fake) |

API: `POST /api/jobs {url, timestamp?, from_ts?, to_ts?, include_subdomains?, skip_media?}` → `{id}`; `GET /api/jobs/{id}` (progress); `POST /api/jobs/{id}/cancel`; `GET /api/jobs/{id}/download` (ZIP); `GET /api/snapshots?url=` (months with a home page capture); `/preview/{id}/…` serves the restored site, sandboxed with CSP.

Identical requests share one job, so a popular site is only downloaded once while its result is kept.

## Tests

```bash
pip install -r requirements-dev.txt
python -m pytest -q
```

The tests run against `tests/fake_archive.py`, a local imitation of the CDX API and `id_` snapshots. It covers paging, 429 retries, `www`/non-`www`, date selection, unlisted assets, `<base>` tags, latin-1 pages, `srcset`, CSS `@import`/`url()`, resume and the web API.

## Notes

- archive.org rate-limits heavily. Keep `--workers` at 4 or below. A site with 10,000 files takes roughly 30–90 minutes.
- Dynamic features (search, forms, logins, anything server-side) can't be restored. Only what the archive captured as files comes back.
- Only restore sites you own or have the rights to reuse.
