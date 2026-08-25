#!/usr/bin/env python3
"""Materialize text from an official JORADP PDF without persisting the PDF.

The PDF is downloaded to a temporary file, processed with the `pdftotext`
command (Poppler), and deleted automatically when the process exits.

This tool intentionally does not commit or cache binary source documents.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path


def download(url: str, destination: Path) -> None:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "MFEP_DZ-text-materializer/1.0"},
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
            "Download a JORADP PDF temporarily and emit text only. "
            "The PDF is never stored in the repository."
        )
    )
    parser.add_argument("url", help="official JORADP PDF URL")
    parser.add_argument("output", type=Path, help="UTF-8 text output path")
    parser.add_argument("--first-page", type=int, required=True)
    parser.add_argument("--last-page", type=int, required=True)
    args = parser.parse_args()

    if args.first_page < 1 or args.last_page < args.first_page:
        parser.error("invalid page range")

    args.output.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="mfep-dz-") as temp_dir:
        pdf_path = Path(temp_dir) / "source.pdf"
        download(args.url, pdf_path)
        text = extract(pdf_path, args.first_page, args.last_page)
        args.output.write_text(text, encoding="utf-8")

    print(f"Wrote text to {args.output}")
    print("Temporary PDF removed.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # deterministic CLI boundary
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
