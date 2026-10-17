#!/usr/bin/env python3
"""V39 independent r88 raw-obligation enumeration.

Standalone: imports nothing from corpus/tools. Two methods that must agree:
  method A: generic recursive walker over parsed JSON; yields a pointer for
            every dict field named source_id (claims, relations/timeline
            records) and every first_appearance field on entity records.
  method B: text-level regex cross-count of "source_id"/"first_appearance"
            occurrences per raw file, checked against parsed array lengths.
Prints the obligation set (sorted) and both counts.
"""
import json
import re
import sys
from pathlib import Path

RAW_FILES = ("entities.json", "relations.json", "timeline.json")


def walk(node, pointer, out):
    if isinstance(node, dict):
        for key, value in node.items():
            child = f"{pointer}/{key}" if pointer else key
            if key == "source_id" and isinstance(value, str):
                out.append((pointer, value))
            elif key == "first_appearance" and isinstance(value, str):
                out.append((child, value))
            walk(value, child, out)
    elif isinstance(node, list):
        for index, item in enumerate(node):
            walk(item, f"{pointer}/{index}", out)


def method_a(cluster):
    found = []
    for name in RAW_FILES:
        data = json.loads((cluster / name).read_text(encoding="utf-8"))
        assert isinstance(data, list), name
        walk(data, name, found)
    # contract positions only: top-level array records /i, entity
    # first_appearance /i/first_appearance, entity claims /i/claims/j
    kept = {}
    for pointer, value in found:
        parts = pointer.split("/")
        ok = (
            len(parts) == 2
            or (len(parts) == 3 and parts[2] == "first_appearance")
            or (len(parts) == 4 and parts[2] == "claims")
        )
        if not ok:
            raise SystemExit(f"method A: unexpected source-bearing pointer {pointer}")
        if pointer in kept:
            raise SystemExit(f"method A: repeated pointer {pointer}")
        kept[pointer] = value
    return kept


def method_b(cluster):
    total = 0
    detail = {}
    for name in RAW_FILES:
        text = (cluster / name).read_text(encoding="utf-8")
        data = json.loads(text)
        source_hits = len(re.findall(r'"source_id"\s*:', text))
        first_hits = len(re.findall(r'"first_appearance"\s*:', text))
        if name == "entities.json":
            expected = sum(1 for e in data if "first_appearance" in e) + sum(
                len(e.get("claims", [])) for e in data
            )
        else:
            expected = len(data)
        assert source_hits + first_hits == expected, (name, source_hits, first_hits, expected)
        detail[name] = (source_hits, first_hits, expected)
        total += expected
    return total, detail


def main():
    cluster = Path(sys.argv[1])
    a = method_a(cluster)
    b_total, b_detail = method_b(cluster)
    print("METHOD A obligations:")
    for pointer in sorted(a):
        print(f"  {pointer} -> {a[pointer]}")
    print(f"METHOD A count: {len(a)}")
    print("METHOD B text cross-count per file (source_id, first_appearance, expected):")
    for name, row in b_detail.items():
        print(f"  {name}: {row}")
    print(f"METHOD B count: {b_total}")
    print("AGREE" if len(a) == b_total else "DISAGREE")
    return 0 if len(a) == b_total else 1


if __name__ == "__main__":
    raise SystemExit(main())
