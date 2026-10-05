"""Command line: python -m wayback example.com [options]"""
from __future__ import annotations

import argparse
import sys

from .archive import Archive, ArchiveError
from .restore import Options, Restorer
from .urls import parse_target


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog="wayback",
        description="Download and restore a complete website from the Wayback Machine.",
    )
    p.add_argument("url", help="domain (example.com) or Wayback URL (https://web.archive.org/web/2019.../example.com)")
    p.add_argument("-o", "--out", help="output folder (default: ./restored/<domain>)")
    p.add_argument("-t", "--timestamp", help="restore as of this date, e.g. 2019 or 20190615 (default: latest)")
    p.add_argument("--from", dest="from_ts", help="ignore captures before this date")
    p.add_argument("--to", dest="to_ts", help="ignore captures after this date")
    p.add_argument("--subdomains", action="store_true", help="also restore blog.example.com, cdn.example.com, ...")
    p.add_argument("--no-missing", action="store_true", help="don't chase links missing from the index")
    p.add_argument("--max-files", type=int, help="stop after this many files")
    p.add_argument("--workers", type=int, default=4, help="parallel downloads (default 4; archive.org throttles above ~5)")
    p.add_argument("--delay", type=float, default=0.25, help="seconds between requests (default 0.25)")
    p.add_argument("--no-zip", action="store_true", help="only write the folder, no ZIP")
    p.add_argument("--skip-media", action="store_true", help="skip video and audio files")
    args = p.parse_args(argv)

    try:
        target = parse_target(args.url)
    except ValueError as e:
        p.error(str(e))
    opts = Options(
        timestamp=args.timestamp,
        from_ts=args.from_ts,
        to_ts=args.to_ts,
        include_subdomains=args.subdomains,
        fetch_missing=not args.no_missing,
        max_files=args.max_files,
        workers=args.workers,
        min_interval=args.delay,
        make_zip=not args.no_zip,
        exclude_mimes=("video/", "audio/") if args.skip_media else (),
    )
    out = args.out or f"restored/{target.host}"

    last = [""]

    def show(pr):
        line = (
            f"\r[{pr.stage:<11}] found {pr.found}  downloaded {pr.downloaded}  "
            f"failed {pr.failed}  {pr.bytes / 1e6:.1f} MB"
        )
        if pr.message != last[0]:
            last[0] = pr.message
            sys.stderr.write("\r" + " " * 100 + "\r" + pr.log[-1] + "\n")
        sys.stderr.write(line)
        sys.stderr.flush()

    restorer = Restorer(target, out, opts, Archive(min_interval=args.delay), on_progress=show)
    try:
        restorer.run()
    except KeyboardInterrupt:
        sys.stderr.write("\nStopped. Run the same command again to resume.\n")
        return 130
    except ArchiveError as e:
        sys.stderr.write(f"\n{e}\n")
        return 1
    sys.stderr.write(f"\n\nSite folder: {restorer.site_dir}/index.html\n")
    if opts.make_zip:
        sys.stderr.write(f"ZIP:         {restorer.zip_path}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
