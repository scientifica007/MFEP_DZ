#!/usr/bin/env python3
"""Resolve brittle JORADP PDF URLs from stable issue identity.

JORADP direct PDF URLs are historically inconsistent in path casing and may
behave differently depending on the client. This resolver treats
(year, issue, language) as the stable source identity and tries:

1. recorded URLs supplied by the repository;
2. deterministic case/extension variants;
3. the official JORADP yearly issue index (ZAyyyy/ZFyyyy) and links found there.

It never stores a PDF in the repository.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable

BASE = "https://www.joradp.dz"
PDF_RE = re.compile(r"(?P<prefix>[AF])(?P<year>\d{4})(?P<issue>\d{3})\.(?P<ext>pdf)", re.I)


@dataclass
class Probe:
    url: str
    method: str
    ok: bool
    http_status: int | None = None
    content_type: str | None = None
    error: str | None = None


@dataclass
class Resolution:
    year: int
    issue: int
    language: str
    resolved_url: str | None
    method: str | None
    issue_index_url: str
    attempts: list[Probe]


class LinkCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hrefs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        for key, value in attrs:
            if key.lower() == "href" and value:
                self.hrefs.append(value)


def user_agent() -> str:
    return "MFEP_DZ-JORADP-resolver/1.0 (+https://github.com/scientifica007/MFEP_DZ)"


def normalize_language(language: str) -> str:
    value = language.lower().strip()
    aliases = {"ar": "ar", "arabic": "ar", "a": "ar", "fr": "fr", "french": "fr", "f": "fr"}
    if value not in aliases:
        raise ValueError(f"unsupported language: {language!r}")
    return aliases[value]


def filename(year: int, issue: int, language: str, ext: str = "pdf") -> str:
    prefix = "A" if language == "ar" else "F"
    return f"{prefix}{year}{issue:03d}.{ext}"


def issue_index_url(year: int, language: str) -> str:
    code = "ZA" if language == "ar" else "ZF"
    return f"{BASE}/JRN/{code}{year}.htm"


def infer_identity_from_urls(urls: Iterable[str]) -> tuple[int | None, int | None, str | None]:
    for url in urls:
        match = PDF_RE.search(url)
        if not match:
            continue
        year = int(match.group("year"))
        issue = int(match.group("issue"))
        language = "ar" if match.group("prefix").upper() == "A" else "fr"
        return year, issue, language
    return None, None, None


def parse_manifest_urls(path: Path) -> dict[str, list[str]]:
    """Read URLs under top-level ar:/fr: sections without a YAML dependency."""
    result = {"ar": [], "fr": []}
    current: str | None = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        if raw == "ar:":
            current = "ar"
            continue
        if raw == "fr:":
            current = "fr"
            continue
        if raw and not raw.startswith(" "):
            current = None
            continue
        if not current:
            continue
        for candidate in re.findall(r'https?://[^"\s]+', raw):
            candidate = candidate.rstrip("',]")
            if candidate not in result[current]:
                result[current].append(candidate)
    return result


def deterministic_candidates(year: int, issue: int, language: str) -> list[str]:
    if language == "ar":
        dirs = ["jo-arabe", "JO-ARABE", "JO-Arabe", "jo-Arabe"]
    else:
        dirs = ["jo-francais", "JO-FRANCAIS", "JO-Francais", "jo-Francais"]

    candidates: list[str] = []
    for ftp in ("FTP", "ftp"):
        for directory in dirs:
            for ext in ("pdf", "PDF"):
                candidates.append(
                    f"{BASE}/{ftp}/{directory}/{year}/{filename(year, issue, language, ext)}"
                )
    return candidates


def probe(url: str, method: str, timeout: int = 20) -> Probe:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": user_agent(),
            "Accept": "application/pdf,text/html;q=0.8,*/*;q=0.5",
            "Range": "bytes=0-8191",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            status = getattr(response, "status", None)
            content_type = response.headers.get_content_type()
            prefix = response.read(8192)
            ok = content_type == "application/pdf" or prefix.startswith(b"%PDF")
            return Probe(
                url=url,
                method=method,
                ok=ok,
                http_status=status,
                content_type=content_type,
                error=None if ok else "response is not a PDF",
            )
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as exc:
        return Probe(url=url, method=method, ok=False, error=str(exc))


def links_from_issue_index(year: int, issue: int, language: str, timeout: int = 20) -> list[str]:
    index = issue_index_url(year, language)
    request = urllib.request.Request(index, headers={"User-Agent": user_agent()})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            html = response.read().decode("utf-8", errors="replace")
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError):
        return []

    collector = LinkCollector()
    collector.feed(html)
    target_stem = filename(year, issue, language).rsplit(".", 1)[0].lower()
    results: list[str] = []
    for href in collector.hrefs:
        absolute = urllib.parse.urljoin(index, href)
        if target_stem in absolute.lower() and absolute.lower().endswith(".pdf"):
            if absolute not in results:
                results.append(absolute)
    return results


def unique(items: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item and item not in seen:
            seen.add(item)
            result.append(item)
    return result


def resolve_issue(
    year: int,
    issue: int,
    language: str,
    recorded_urls: Iterable[str] = (),
    timeout: int = 20,
) -> Resolution:
    language = normalize_language(language)
    attempts: list[Probe] = []

    candidates = unique([*recorded_urls, *deterministic_candidates(year, issue, language)])
    for url in candidates:
        result = probe(url, "recorded_or_deterministic_variant", timeout=timeout)
        attempts.append(result)
        if result.ok:
            return Resolution(
                year=year,
                issue=issue,
                language=language,
                resolved_url=url,
                method=result.method,
                issue_index_url=issue_index_url(year, language),
                attempts=attempts,
            )

    for url in links_from_issue_index(year, issue, language, timeout=timeout):
        if url in candidates:
            continue
        result = probe(url, "official_year_index", timeout=timeout)
        attempts.append(result)
        if result.ok:
            return Resolution(
                year=year,
                issue=issue,
                language=language,
                resolved_url=url,
                method=result.method,
                issue_index_url=issue_index_url(year, language),
                attempts=attempts,
            )

    return Resolution(
        year=year,
        issue=issue,
        language=language,
        resolved_url=None,
        method=None,
        issue_index_url=issue_index_url(year, language),
        attempts=attempts,
    )


def resolve_from_source(
    source: str,
    language: str | None = None,
    year: int | None = None,
    issue: int | None = None,
    timeout: int = 20,
) -> Resolution:
    path = Path(source)
    recorded_urls: list[str] = []

    if path.is_file():
        manifest = parse_manifest_urls(path)
        if language:
            lang = normalize_language(language)
            recorded_urls.extend(manifest[lang])
        else:
            lang = ""
        all_urls = manifest["ar"] + manifest["fr"]
        inferred_year, inferred_issue, inferred_lang = infer_identity_from_urls(all_urls)
        year = year or inferred_year
        issue = issue or inferred_issue
        if not language:
            if inferred_lang is None:
                raise ValueError("--lang is required when language cannot be inferred")
            lang = inferred_lang
        if not recorded_urls:
            recorded_urls.extend(manifest[lang])
    else:
        recorded_urls = [source]
        inferred_year, inferred_issue, inferred_lang = infer_identity_from_urls(recorded_urls)
        year = year or inferred_year
        issue = issue or inferred_issue
        if language:
            lang = normalize_language(language)
        elif inferred_lang:
            lang = inferred_lang
        else:
            raise ValueError("--lang is required when language cannot be inferred")

    if year is None or issue is None:
        raise ValueError("year/issue could not be inferred; pass --year and --issue")

    return resolve_issue(year, issue, lang, recorded_urls, timeout=timeout)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Resolve a JORADP PDF from stable issue identity with fallbacks."
    )
    parser.add_argument("source", help="recorded PDF URL or sources.yml path")
    parser.add_argument("--lang", choices=["ar", "fr"], help="target language")
    parser.add_argument("--year", type=int, help="gazette year (normally inferred)")
    parser.add_argument("--issue", type=int, help="gazette issue number (normally inferred)")
    parser.add_argument("--timeout", type=int, default=20)
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    args = parser.parse_args()

    resolution = resolve_from_source(
        args.source,
        language=args.lang,
        year=args.year,
        issue=args.issue,
        timeout=args.timeout,
    )
    payload = asdict(resolution)

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"JORADP {resolution.year} issue {resolution.issue} ({resolution.language})")
        print(f"Issue index: {resolution.issue_index_url}")
        if resolution.resolved_url:
            print(f"Resolved: {resolution.resolved_url}")
            print(f"Method: {resolution.method}")
        else:
            print("Resolved: NONE")
        print(f"Attempts: {len(resolution.attempts)}")

    return 0 if resolution.resolved_url else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
