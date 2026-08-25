#!/usr/bin/env python3
"""Deterministic repository checks for MFEP_DZ staging data.

No third-party dependencies are required.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


def read_jsonl(path: Path, errors: list[str]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"{path}: cannot read file: {exc}")
        return rows

    for lineno, raw in enumerate(text.splitlines(), start=1):
        line = raw.strip()
        if not line:
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(
                f"{path}:{lineno}: invalid JSON: {exc.msg} "
                f"(column {exc.colno})"
            )
            continue
        if not isinstance(value, dict):
            errors.append(f"{path}:{lineno}: JSONL row must be an object")
            continue
        value["_validator_line"] = lineno
        rows.append(value)
    return rows


def ontology_keys(path: Path, section: str, errors: list[str]) -> set[str]:
    """Read keys from one two-space-indented top-level YAML mapping section.

    ontology/core.yml intentionally uses a simple mapping layout. This avoids
    introducing a YAML dependency before the project has frozen its schema.
    """
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        errors.append(f"{path}: cannot read ontology: {exc}")
        return set()

    marker = f"{section}:"
    inside = False
    keys: set[str] = set()
    for line in lines:
        if not inside:
            if line == marker:
                inside = True
            continue

        if line and not line.startswith(" "):
            break

        if line.startswith("  ") and not line.startswith("    "):
            stripped = line.strip()
            if stripped.endswith(":"):
                keys.add(stripped[:-1])
    if not keys:
        errors.append(f"{path}: ontology section {section!r} is missing or empty")
    return keys


def require_fields(
    row: dict[str, Any],
    fields: Iterable[str],
    path: Path,
    errors: list[str],
) -> None:
    lineno = row.get("_validator_line", "?")
    for field in fields:
        if field not in row:
            errors.append(f"{path}:{lineno}: missing required field {field!r}")


def duplicates(values: Iterable[str]) -> list[str]:
    counts = Counter(values)
    return sorted(value for value, count in counts.items() if count > 1)


def validate(root: Path) -> tuple[list[str], list[str], dict[str, int]]:
    errors: list[str] = []
    warnings: list[str] = []
    counts: Counter[str] = Counter()

    ontology = root / "ontology" / "core.yml"
    legal_forms = ontology_keys(ontology, "legal_form", errors)
    relation_types = ontology_keys(ontology, "relation_type", errors)
    legal_statuses = ontology_keys(ontology, "legal_status", errors)

    metadata_files = sorted((root / "metadata" / "staging").glob("*.jsonl"))
    if not metadata_files:
        errors.append("metadata/staging: no JSONL indexes found")

    metadata_rows: list[tuple[Path, dict[str, Any]]] = []
    for path in metadata_files:
        for row in read_jsonl(path, errors):
            metadata_rows.append((path, row))

    ids: list[str] = []
    for path, row in metadata_rows:
        require_fields(
            row,
            ("id", "record_status", "legal_form", "record_path"),
            path,
            errors,
        )
        record_id = row.get("id")
        if isinstance(record_id, str):
            ids.append(record_id)
        else:
            errors.append(
                f"{path}:{row.get('_validator_line', '?')}: id must be a string"
            )

        if row.get("record_status") != "staging":
            warnings.append(
                f"{path}:{row.get('_validator_line', '?')}: "
                f"unexpected record_status={row.get('record_status')!r}"
            )

        legal_form = row.get("legal_form")
        if isinstance(legal_form, str) and legal_form not in legal_forms:
            errors.append(
                f"{path}:{row.get('_validator_line', '?')}: "
                f"unknown legal_form {legal_form!r}"
            )

        status = row.get("status")
        if isinstance(status, str) and status not in legal_statuses:
            errors.append(
                f"{path}:{row.get('_validator_line', '?')}: "
                f"unknown legal status {status!r}"
            )

        record_path = row.get("record_path")
        if isinstance(record_path, str):
            if not (root / record_path).is_file():
                errors.append(
                    f"{path}:{row.get('_validator_line', '?')}: "
                    f"record_path does not exist: {record_path}"
                )
        else:
            errors.append(
                f"{path}:{row.get('_validator_line', '?')}: "
                "record_path must be a string"
            )

    for record_id in duplicates(ids):
        errors.append(f"duplicate legal-text id in metadata indexes: {record_id}")

    known_ids = set(ids)
    counts["metadata_records"] = len(metadata_rows)

    graph_files = sorted((root / "graph" / "staging").glob("*.jsonl"))
    graph_rows: list[tuple[Path, dict[str, Any]]] = []
    edge_ids: list[str] = []
    for path in graph_files:
        for row in read_jsonl(path, errors):
            graph_rows.append((path, row))
            require_fields(row, ("id", "type", "source", "target"), path, errors)

            edge_id = row.get("id")
            if isinstance(edge_id, str):
                edge_ids.append(edge_id)

            rel_type = row.get("type")
            if isinstance(rel_type, str) and rel_type not in relation_types:
                errors.append(
                    f"{path}:{row.get('_validator_line', '?')}: "
                    f"unknown relation type {rel_type!r}"
                )

            source = row.get("source")
            if (
                isinstance(source, str)
                and source.startswith("DZ-")
                and source not in known_ids
                and not row.get("source_status")
            ):
                errors.append(
                    f"{path}:{row.get('_validator_line', '?')}: "
                    f"unresolved source {source!r} lacks source_status"
                )

            target = row.get("target")
            if (
                isinstance(target, str)
                and target.startswith("DZ-")
                and target not in known_ids
                and not row.get("target_status")
            ):
                errors.append(
                    f"{path}:{row.get('_validator_line', '?')}: "
                    f"unresolved target {target!r} lacks target_status"
                )

    for edge_id in duplicates(edge_ids):
        errors.append(f"duplicate graph edge id: {edge_id}")

    counts["graph_edges"] = len(graph_rows)

    queue_path = root / "metadata" / "discovery-queue.jsonl"
    queue_rows = read_jsonl(queue_path, errors) if queue_path.is_file() else []
    queue_ids: list[str] = []
    for row in queue_rows:
        require_fields(
            row,
            ("candidate_id", "state", "priority", "next_action"),
            queue_path,
            errors,
        )
        candidate_id = row.get("candidate_id")
        if isinstance(candidate_id, str):
            queue_ids.append(candidate_id)
        state = row.get("state")
        if state not in {"pending", "ingested_staging", "resolved", "deferred"}:
            errors.append(
                f"{queue_path}:{row.get('_validator_line', '?')}: "
                f"unknown queue state {state!r}"
            )
        priority = row.get("priority")
        if priority not in {"high", "medium", "low"}:
            errors.append(
                f"{queue_path}:{row.get('_validator_line', '?')}: "
                f"unknown priority {priority!r}"
            )

    for candidate_id in duplicates(queue_ids):
        errors.append(f"duplicate discovery candidate_id: {candidate_id}")
    counts["discovery_queue"] = len(queue_rows)

    cases_dir = root / "ai" / "evals" / "cases"
    expected_dir = root / "ai" / "evals" / "expected"
    case_rows: list[dict[str, Any]] = []
    expected_rows: list[dict[str, Any]] = []

    for path in sorted(cases_dir.glob("*.jsonl")):
        case_rows.extend(read_jsonl(path, errors))
    for path in sorted(expected_dir.glob("*.jsonl")):
        expected_rows.extend(read_jsonl(path, errors))

    case_ids = [
        row["case_id"]
        for row in case_rows
        if isinstance(row.get("case_id"), str)
    ]
    expected_ids = [
        row["case_id"]
        for row in expected_rows
        if isinstance(row.get("case_id"), str)
    ]
    for case_id in duplicates(case_ids):
        errors.append(f"duplicate eval case_id: {case_id}")
    for case_id in duplicates(expected_ids):
        errors.append(f"duplicate eval expected case_id: {case_id}")

    missing_expected = sorted(set(case_ids) - set(expected_ids))
    orphan_expected = sorted(set(expected_ids) - set(case_ids))
    for case_id in missing_expected:
        errors.append(f"eval case has no expected output: {case_id}")
    for case_id in orphan_expected:
        errors.append(f"eval expected output has no case: {case_id}")

    counts["eval_cases"] = len(case_rows)
    counts["eval_expected"] = len(expected_rows)

    return errors, warnings, dict(counts)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run deterministic structural checks on MFEP_DZ staging data."
    )
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        help="repository root (default: current directory)",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    errors, warnings, counts = validate(root)

    print("MFEP_DZ deterministic validation")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]}")

    if warnings:
        print(f"\nWarnings ({len(warnings)}):")
        for item in warnings:
            print(f"  - {item}")

    if errors:
        print(f"\nErrors ({len(errors)}):", file=sys.stderr)
        for item in errors:
            print(f"  - {item}", file=sys.stderr)
        return 1

    print("\nOK: no deterministic validation errors found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
