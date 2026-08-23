#!/usr/bin/env python3
"""Validate h4ckd4d Detection Engineering repository consistency.

This tool performs local/static checks only. It does not generate traffic,
contact external systems, or execute detection engines.
"""

from __future__ import annotations

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
CATALOG = ROOT / "metadata" / "rule-catalog.json"
COVERAGE = ROOT / "metadata" / "coverage-matrix.json"

REQUIRED = {
    "id",
    "engine",
    "path",
    "native_id",
    "title",
    "status",
    "severity",
    "confidence",
    "data_source",
    "description",
    "false_positives",
    "attack",
    "revision",
}

ALLOWED_ENGINES = {"snort3", "suricata", "sigma"}
ALLOWED_STATUS = {"experimental", "test", "stable", "deprecated"}
ALLOWED_SEVERITY = {"informational", "low", "medium", "high", "critical"}
ALLOWED_CONFIDENCE = {"low", "medium", "high"}
ALLOWED_DOMAINS = {"network", "dns", "http", "tls", "windows", "linux", "identity", "cloud", "endpoint"}
ALLOWED_TEST_COVERAGE = {"static-validation", "synthetic-fixture", "engine-validation", "analyst-review"}
ATTACK_RE = re.compile(r"^T\d{4}(?:\.\d{3})?$")
SID_RE = re.compile(r"\bsid\s*:\s*(\d+)\s*;")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def main() -> int:
    errors: list[str] = []
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    rules = data.get("rules", [])

    if not rules:
        fail(errors, "catalog contains no rules")

    seen_ids: set[str] = set()
    seen_native: set[tuple[str, str]] = set()

    for index, rule in enumerate(rules, start=1):
        missing = REQUIRED - set(rule)
        if missing:
            fail(errors, f"rule #{index} missing fields: {sorted(missing)}")
            continue

        rule_id = str(rule["id"])
        engine = str(rule["engine"])
        native_id = str(rule["native_id"])
        path = ROOT / str(rule["path"])

        if rule_id in seen_ids:
            fail(errors, f"duplicate project rule id: {rule_id}")
        seen_ids.add(rule_id)

        native_key = (engine, native_id)
        if native_key in seen_native:
            fail(errors, f"duplicate native id for {engine}: {native_id}")
        seen_native.add(native_key)

        if engine not in ALLOWED_ENGINES:
            fail(errors, f"{rule_id}: unsupported engine {engine}")
        if rule["status"] not in ALLOWED_STATUS:
            fail(errors, f"{rule_id}: invalid status {rule['status']}")
        if rule["severity"] not in ALLOWED_SEVERITY:
            fail(errors, f"{rule_id}: invalid severity {rule['severity']}")
        if rule["confidence"] not in ALLOWED_CONFIDENCE:
            fail(errors, f"{rule_id}: invalid confidence {rule['confidence']}")
        if not isinstance(rule["revision"], int) or rule["revision"] < 1:
            fail(errors, f"{rule_id}: revision must be a positive integer")
        if not isinstance(rule["false_positives"], list):
            fail(errors, f"{rule_id}: false_positives must be a list")
        if not isinstance(rule["attack"], list):
            fail(errors, f"{rule_id}: attack must be a list")
        else:
            for technique in rule["attack"]:
                if not ATTACK_RE.match(str(technique)):
                    fail(errors, f"{rule_id}: invalid ATT&CK technique id {technique}")

        if not path.is_file():
            fail(errors, f"{rule_id}: missing rule file {rule['path']}")
            continue

        text = path.read_text(encoding="utf-8")

        if engine in {"snort3", "suricata"}:
            sids = set(SID_RE.findall(text))
            if native_id not in sids:
                fail(errors, f"{rule_id}: native sid {native_id} not found in {rule['path']}")
            if rule_id not in text:
                fail(errors, f"{rule_id}: project id not embedded in {rule['path']}")

        if engine == "sigma":
            required_sigma_markers = ["title:", "id:", "logsource:", "detection:", "condition:"]
            for marker in required_sigma_markers:
                if marker not in text:
                    fail(errors, f"{rule_id}: Sigma file missing {marker}")
            if f"id: {native_id}" not in text:
                fail(errors, f"{rule_id}: Sigma UUID does not match catalog")

    coverage_data = json.loads(COVERAGE.read_text(encoding="utf-8"))
    coverage_rows = coverage_data.get("coverage", [])
    coverage_ids: set[str] = set()

    for index, row in enumerate(coverage_rows, start=1):
        row_id = str(row.get("id", ""))
        if not row_id:
            fail(errors, f"coverage row #{index}: missing id")
            continue
        if row_id in coverage_ids:
            fail(errors, f"duplicate coverage id: {row_id}")
        coverage_ids.add(row_id)
        if row.get("domain") not in ALLOWED_DOMAINS:
            fail(errors, f"{row_id}: invalid coverage domain {row.get('domain')}")
        tests = row.get("test_coverage")
        if not isinstance(tests, list) or not tests:
            fail(errors, f"{row_id}: test_coverage must be a non-empty list")
        else:
            unknown = set(tests) - ALLOWED_TEST_COVERAGE
            if unknown:
                fail(errors, f"{row_id}: unsupported test coverage values {sorted(unknown)}")
        if not isinstance(row.get("tuning_required"), bool):
            fail(errors, f"{row_id}: tuning_required must be boolean")

    missing_coverage = seen_ids - coverage_ids
    unknown_coverage = coverage_ids - seen_ids
    if missing_coverage:
        fail(errors, f"catalog rules missing coverage rows: {sorted(missing_coverage)}")
    if unknown_coverage:
        fail(errors, f"coverage rows reference unknown rules: {sorted(unknown_coverage)}")

    fixture = ROOT / "tests" / "fixtures" / "windows_4625_synthetic.json"
    try:
        fixture_data = json.loads(fixture.read_text(encoding="utf-8"))
        if fixture_data.get("fixture") is not True:
            fail(errors, "synthetic fixture must explicitly set fixture=true")
    except (OSError, json.JSONDecodeError) as exc:
        fail(errors, f"invalid synthetic fixture: {exc}")

    if errors:
        print("Detection repository validation failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Detection repository validation passed: {len(rules)} cataloged rules with coverage metadata.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
