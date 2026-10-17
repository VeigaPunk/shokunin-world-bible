#!/usr/bin/env python3
"""V39: independently verify r88 map anchor/span/mode against the fixture files.

Checks (no import of corpus/tools):
  A. the dialect-pointer row set equals my standalone enumeration one-to-one
     (same pointers, same source IDs);
  B. each JSON-fact row's span `file:line` resolves and contains its exact anchor;
  C. each row's declared R9 mode matches the delivered file's declared mode;
  D. the two editorial rows resolve to source-excerpt.md and their anchors occur there.
"""
import importlib.util
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CLUSTER = Path(sys.argv[1] if len(sys.argv) > 1 else "corpus/fixtures/r88-m3-maya-cluster")


def load(name):
    spec = importlib.util.spec_from_file_location(name, HERE / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


enum = load("enumerate_r88")
parser = load("parse_r88_map")

text = (CLUSTER / "claim-excerpt-map.md").read_text(encoding="utf-8")
rows = []
for title, raw_rows in parser.section_rows(text):
    table = [parser.cells(r) for r in raw_rows]
    table = [r for r in table if not all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in r)]
    if not table or "Excerpt path:line" not in "|".join(table[0]):
        continue
    header = table[0]
    for row in table[1:]:
        record = dict(zip(header, row))
        pointer, token = parser.to_pointer(record.get("JSON fact and fields", ""))
        source = record.get("`source_id`", record.get("source_id", ""))
        match = re.search(r"`([^`]+)`", source)
        rows.append({
            "id": record.get("ID"),
            "pointer": pointer,
            "source_id": match.group(1) if match else source.strip(),
            "span": record.get("Excerpt path:line", "").strip("`"),
            "mode": record.get("R9 mode", "").strip("`"),
            "anchor": record.get("Exact anchor", "").strip("`"),
        })

problems = []
expected = enum.method_a(CLUSTER)
fact_rows = [r for r in rows if r["pointer"]]
editorial_rows = [r for r in rows if not r["pointer"]]


def canonical(pointer):
    return pointer.replace(".json/", ".json#/", 1)


# R9 excerpt declarations table: filename -> declared delivery mode
declared_modes = {}
for title, raw_rows in parser.section_rows(text):
    table = [parser.cells(r) for r in raw_rows]
    table = [r for r in table if not all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in r)]
    if not table or "Delivery mode" not in "|".join(table[0]):
        continue
    header = table[0]
    for row in table[1:]:
        record = dict(zip(header, row))
        excerpt = re.search(r"`([A-Za-z0-9_.-]+\.md):[0-9–-]+`", record.get("Excerpt", ""))
        if excerpt:
            declared_modes[excerpt.group(1)] = record.get("Delivery mode", "").strip("`")

# A. one-to-one against enumeration
enum_set = {canonical(p) for p in expected}
row_set = {r["pointer"] for r in fact_rows}
if enum_set != row_set:
    problems.append(f"A: pointer sets differ: enum-only={sorted(enum_set - row_set)} row-only={sorted(row_set - enum_set)}")
for r in fact_rows:
    if expected.get(r["pointer"].replace(".json#/", ".json/", 1)) != r["source_id"]:
        problems.append(f"A: {r['pointer']} source {r['source_id']!r} != raw "
                        f"{expected.get(r['pointer'].replace('.json#/', '.json/', 1))!r}")
if len(fact_rows) != len(row_set):
    problems.append("A: duplicate pointers among fact rows")

# B/C. span + anchor + mode per row
for r in rows:
    if not r["span"]:
        problems.append(f"{r['id']}: empty span")
        continue
    match = re.fullmatch(r"([A-Za-z0-9_.-]+\.md):([0-9]+)", r["span"])
    if not match:
        problems.append(f"{r['id']}: span {r['span']!r} not file:line")
        continue
    filename, line_no = match.group(1), int(match.group(2))
    target = CLUSTER / filename
    if not target.is_file():
        problems.append(f"{r['id']}: span target {filename} missing")
        continue
    lines = target.read_text(encoding="utf-8").splitlines()
    if line_no < 1 or line_no > len(lines):
        problems.append(f"{r['id']}: span line {line_no} out of range ({len(lines)} lines)")
        continue
    if r["anchor"] not in lines[line_no - 1]:
        problems.append(f"{r['id']}: anchor {r['anchor']!r} not on {r['span']}")
    if declared_modes.get(filename) != r["mode"]:
        problems.append(f"{r['id']}: row mode {r['mode']!r} != declarations-table mode "
                        f"{declared_modes.get(filename)!r} for {filename}")
    if filename == "fictional-excerpts.md" and "`verbatim`" not in lines[2]:
        problems.append(f"{r['id']}: fictional-excerpts.md line 3 does not declare `verbatim`")

# D. editorial shape
if len(editorial_rows) != 2:
    problems.append(f"D: expected 2 editorial rows, saw {len(editorial_rows)}")
for r in editorial_rows:
    if not r["span"].startswith("source-excerpt.md:"):
        problems.append(f"D: {r['id']} span {r['span']!r} not in source-excerpt.md")

print(f"rows total={len(rows)} fact={len(fact_rows)} editorial={len(editorial_rows)}")
print(f"enumeration count={len(expected)} fact-row count={len(fact_rows)}")
for r in fact_rows:
    print(f"  {r['id']:>3} {r['pointer']:<40} {r['span']:<28} {r['mode']:<9} anchor-ok")
print("ANCHOR/SPAN/MODE " + ("AGREE" if not problems else "PROBLEMS"))
for p in problems:
    print("PROBLEM:", p)
raise SystemExit(0 if not problems else 1)
