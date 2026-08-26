#!/usr/bin/env python3
"""Materialize text from JORADP without persisting the PDF.

The source argument may be either:
- a recorded JORADP PDF URL; or
- a repository sources.yml manifest.

The URL is resolved through joradp_resolver.py before download, so broken direct
links can fall back to path variants and the official yearly issue index.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

from joradp_resolver import resolve_from_source, user_agent


def download(url: str, destination: Path) -> None:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": user_agent(), "Accept": "application/pdf,*/*;q=0.5"},
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        destination.write_bytes(response.read())


def extract(pdf: Path, first_page: int, last_page: int) -> str:
    executable = shutil.which("pdftotext")
    if not executable:
        raise RuntimeError(
            "pdftotext was not found. Install Poppler utilities before running."
        )

    command = [
        executable,
        "-f",
        str(first_page),
        "-l",
        str(last_page),
        "-layout",
        "-enc",
        "UTF-8",
        str(pdf),
        "-",
    ]
    result = subprocess.run(
        command,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.decode("utf-8", errors="replace"))
    return result.stdout.decode("utf-8", errors="replace")


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Resolve and temporarily download a JORADP PDF, then emit text only. "
            "The PDF is never stored in the repository."
        )
    )
    parser.add_argument(
        "source",
        help="recorded JORADP PDF URL or repository sources.yml path",
    )
    parser.add_argument("output", type=Path, help="UTF-8 text output path")
    parser.add_argument("--lang", choices=["ar", "fr"], help="target language")
    parser.add_argument("--year", type=int, help="gazette year if not inferable")
    parser.add_argument("--issue", type=int, help="gazette issue number if not inferable")
    parser.add_argument("--first-page", type=int, required=True)
    parser.add_argument("--last-page", type=int, required=True)
    parser.add_argument("--timeout", type=int, default=20)
    parser.add_argument(
        "--show-resolution",
        action="store_true",
        help="print recorded/fallback resolution details before extraction",
    )
    args = parser.parse_args()

    if args.first_page < 1 or args.last_page < args.first_page:
        parser.error("invalid page range")

    resolution = resolve_from_source(
        args.source,
        language=args.lang,
        year=args.year,
        issue=args.issue,
        timeout=args.timeout,
    )
    if not resolution.resolved_url:
        raise RuntimeError(
            f"could not resolve JORADP PDF for {resolution.year} "
            f"issue {resolution.issue} ({resolution.language}); "
            f"index={resolution.issue_index_url}"
        )

    if args.show_resolution:
        print(f"Resolved URL: {resolution.resolved_url}")
        print(f"Resolution method: {resolution.method}")
        print(f"Issue index: {resolution.issue_index_url}")
        print(f"Attempts: {len(resolution.attempts)}")

    args.output.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="mfep-dz-") as temp_dir:
        pdf_path = Path(temp_dir) / "source.pdf"
        download(resolution.resolved_url, pdf_path)
        text = extract(pdf_path, args.first_page, args.last_page)
        args.output.write_text(text, encoding="utf-8")

    print(f"Wrote text to {args.output}")
    print("Temporary PDF removed.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
