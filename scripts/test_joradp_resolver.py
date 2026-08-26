#!/usr/bin/env python3
"""Offline deterministic tests for joradp_resolver.py."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import joradp_resolver as resolver


class JoradpResolverTests(unittest.TestCase):
    def test_issue_index_urls(self) -> None:
        self.assertEqual(
            resolver.issue_index_url(2018, "ar"),
            "https://www.joradp.dz/JRN/ZA2018.htm",
        )
        self.assertEqual(
            resolver.issue_index_url(2018, "fr"),
            "https://www.joradp.dz/JRN/ZF2018.htm",
        )

    def test_identity_inference(self) -> None:
        year, issue, language = resolver.infer_identity_from_urls(
            ["https://www.joradp.dz/FTP/jo-francais/2018/F2018036.pdf"]
        )
        self.assertEqual((year, issue, language), (2018, 36, "fr"))

    def test_case_variants_include_known_pattern(self) -> None:
        candidates = resolver.deterministic_candidates(2018, 36, "fr")
        self.assertIn(
            "https://www.joradp.dz/FTP/JO-FRANCAIS/2018/F2018036.pdf",
            candidates,
        )
        self.assertIn(
            "https://www.joradp.dz/FTP/jo-francais/2018/F2018036.PDF",
            candidates,
        )

    def test_manifest_keeps_pdf_urls_and_ignores_issue_index(self) -> None:
        content = '''text_id: EXAMPLE
ar:
  url: "https://www.joradp.dz/FTP/jo-arabe/2018/A2018036.PDF"
  access:
    issue_index_url: "https://www.joradp.dz/JRN/ZA2018.htm"
fr:
  url: "https://www.joradp.dz/FTP/jo-francais/2018/F2018036.pdf"
  access:
    issue_index_url: "https://www.joradp.dz/JRN/ZF2018.htm"
    resolved_url: "https://www.joradp.dz/FTP/JO-FRANCAIS/2018/F2018036.pdf"
'''
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sources.yml"
            path.write_text(content, encoding="utf-8")
            urls = resolver.parse_manifest_urls(path)

        self.assertEqual(
            urls["ar"],
            ["https://www.joradp.dz/FTP/jo-arabe/2018/A2018036.PDF"],
        )
        self.assertEqual(
            urls["fr"],
            [
                "https://www.joradp.dz/FTP/jo-francais/2018/F2018036.pdf",
                "https://www.joradp.dz/FTP/JO-FRANCAIS/2018/F2018036.pdf",
            ],
        )


if __name__ == "__main__":
    unittest.main()
