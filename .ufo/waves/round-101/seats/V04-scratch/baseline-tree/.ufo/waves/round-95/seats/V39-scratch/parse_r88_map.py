#!/usr/bin/env python3
"""V39: parse the r88 map with my own table reader; emit expected dialect rows.

Extracts both tables of corpus/fixtures/r88-m3-maya-cluster/claim-excerpt-map.md
as (section, id, pointer_cell, source_cell, span, mode, anchor) and transforms
the bracket/dot pointer dialect into canonical JSON Pointers, independently of
corpus/tools/map_obligations.py. Also verifies each row's anchor/span/mode
against the fixture excerpt files.
"""
import json
import re
import sys
from pathlib import Path

CLUSTER = Path(sys.argv[1] if len(sys.argv) > 1 else "corpus/fixtures/r88-m3-maya-cluster")
MAP = CLUSTER / "claim-excerpt-map.md"

DIALECT = re.compile(r"^(entities|relations|timeline)\[([0-9]+)\](?:\.(claims)\[([0-9]+)\]|\.(first_appearance))?$")


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def to_pointer(cell):
    """`entities[0].first_appearance` (possibly with backticks/notes) -> pointer."""
    match = re.search(r"`([^`]+)`", cell)
    token = match.group(1) if match else cell.strip()
    m = DIALECT.fullmatch(token)
    if not m:
        return None, token
    file, index, _claims, claim_index, field = m.groups()
    if field == "first_appearance":
        return f"{file}.json#/{index}/first_appearance", token
    if claim_index is not None:
        return f"{file}.json#/{index}/claims/{claim_index}", token
    return f"{file}.json#/{index}", token


def section_rows(text):
    lines = text.splitlines()
    sections = []
    current = None
    for line in lines:
        heading = re.match(r"^##\s+(.*)$", line)
        if heading:
            current = heading.group(1).strip()
            sections.append((current, []))
            continue
        if current is not None and line.lstrip().startswith("|"):
            sections[-1][1].append(line)
    return sections


def main():
    text = MAP.read_text(encoding="utf-8")
    out = []
    for title, raw_rows in section_rows(text):
        rows = [cells(r) for r in raw_rows]
        rows = [r for r in rows if not all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in r)]
        if not rows:
            continue
        header = rows[0]
        if "Excerpt path:line" not in "|".join(header):
            continue
        for row in rows[1:]:
            record = dict(zip(header, row))
            row_id = record.get("ID")
            pointer_cell = record.get("JSON fact and fields", "")
            source_cell = record.get("`source_id`", record.get("source_id", ""))
            span = record.get("Excerpt path:line", "")
            mode = record.get("R9 mode", "").strip("`")
            anchor = record.get("Exact anchor", "").strip("`")
            pointer, token = to_pointer(pointer_cell)
            src = re.search(r"`([^`]+)`", source_cell)
            src = src.group(1) if src else source_cell.strip()
            out.append({
                "section": title.split("(")[0].strip(),
                "id": row_id,
                "token": token,
                "pointer": pointer,
                "source_id": src,
                "span": span,
                "mode": mode,
                "anchor": anchor,
            })
    for row in out:
        print(json.dumps(row, ensure_ascii=False))
    dialect_rows = [r for r in out if r["pointer"]]
    print(f"TOTAL rows={len(out)} dialect_pointer_rows={len(dialect_rows)} nonpointer_rows={len(out) - len(dialect_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
