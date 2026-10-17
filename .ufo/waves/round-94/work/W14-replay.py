#!/usr/bin/env python3
"""Derive W14 comparison-boundary cases from the committed r93 canonical input."""

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
CLUSTER = ROOT / "corpus/fixtures/r93-m2-kojiki-cluster"
MAP = CLUSTER / "claim-excerpt-map.md"


def load_json(name):
    return json.loads((CLUSTER / name).read_text(encoding="utf-8"))


def obligations():
    result = set()
    for index, entity in enumerate(load_json("entities.json")):
        if entity.get("first_appearance"):
            result.add(f"entities.json#/{index}/first_appearance")
        for claim_index, claim in enumerate(entity.get("claims", [])):
            if claim.get("source_id"):
                result.add(f"entities.json#/{index}/claims/{claim_index}")
    for filename in ("relations.json", "timeline.json"):
        for index, record in enumerate(load_json(filename)):
            if record.get("source_id"):
                result.add(f"{filename}#/{index}")
    return result


def mapped_rows():
    rows = []
    pattern = re.compile(r"^\|\s*(E\d+)\s*\|\s*`([^`]+)`")
    for line in MAP.read_text(encoding="utf-8").splitlines():
        match = pattern.match(line)
        if match:
            rows.append((match.group(1), match.group(2)))
    return rows


def resolve(pointer):
    filename, marker, fragment = pointer.partition("#")
    if not marker or filename not in {"entities.json", "relations.json", "timeline.json"}:
        raise ValueError("unsupported pointer file/grammar")
    if not fragment.startswith("/") or re.search(r"~(?![01])", fragment):
        raise ValueError("unsupported JSON-pointer grammar")
    value = load_json(filename)
    for token in fragment[1:].split("/"):
        token = token.replace("~1", "/").replace("~0", "~")
        if isinstance(value, list) and token.isdecimal():
            index = int(token)
            if index >= len(value):
                return False
            value = value[index]
        elif isinstance(value, dict) and token in value:
            value = value[token]
        else:
            return False
    return True


def compare(rows, expected):
    pointers = [pointer for _, pointer in rows]
    counts = Counter(pointers)
    missing = sorted(expected - set(pointers))
    extras = sorted(set(pointers) - expected)
    duplicates = sorted(pointer for pointer, count in counts.items() if count > 1)
    extra_detail = [
        {"pointer": pointer, "target_exists": resolve(pointer)} for pointer in extras
    ]
    return {
        "mapped_rows": len(pointers),
        "missing_obligations": missing,
        "extra_pointers": extra_detail,
        "duplicate_pointers": duplicates,
        "expected_class": "comparison FAIL (exit 1)"
        if missing or extras or duplicates
        else "clean (exit 0)",
    }


def main():
    expected = obligations()
    rows = mapped_rows()
    baseline = compare(rows, expected)
    if baseline["missing_obligations"] or baseline["extra_pointers"] or baseline["duplicate_pointers"]:
        raise SystemExit("r93 canonical map does not match derived obligation inventory")

    missing_pointer = "entities.json#/0/first_appearance"
    phantom_pointer = "entities.json#/999/first_appearance"
    existing_non_obligation = "entities.json#/0/id"
    cases = [
        ("W14-MISSING-FIRST-APPEARANCE", [row for row in rows if row[1] != missing_pointer]),
        ("W14-DUPLICATE-FIRST-APPEARANCE", rows + [("W14-DUP", missing_pointer)]),
        ("W14-PHANTOM-OUT-OF-RANGE", rows + [("W14-PHANTOM", phantom_pointer)]),
        ("W14-EXISTING-NON-OBLIGATION", rows + [("W14-NONOBLIGATION", existing_non_obligation)]),
    ]
    result = {
        "input": "corpus/fixtures/r93-m2-kojiki-cluster",
        "canonical_obligations": len(expected),
        "canonical_map_rows": len(rows),
        "baseline_oracle": baseline,
        "cases": [
            {"case": label, **compare(mutated, expected)} for label, mutated in cases
        ],
        "parse_error_control": {
            "pointer": "entities.json#0/first_appearance",
            "reason": "missing slash after #; unsupported JSON-pointer grammar",
            "expected_class": "could-not-evaluate / parse ERROR (exit 2)",
        },
        "target_cli": {
            "path": "corpus/tools/map_obligations.py",
            "present": (ROOT / "corpus/tools/map_obligations.py").is_file(),
            "finding_ids": "unavailable; target CLI is not present",
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
