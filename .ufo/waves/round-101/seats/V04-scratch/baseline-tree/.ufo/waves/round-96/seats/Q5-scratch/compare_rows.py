#!/usr/bin/env python3
"""Q5 scratch: compare the 15 inherited rows of r95 and r96 maps on
(pointer, span, anchor) and confirm the r96 row set adds exactly one row."""
import re
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
R95 = ROOT / "corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md"
R96 = ROOT / "corpus/fixtures/r96-crossing-response/claim-excerpt-map.md"


def fact_rows(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    rows = []
    in_facts = False
    for line in lines:
        if re.match(r"^##\s+JSON facts", line):
            in_facts = True
            continue
        if in_facts and re.match(r"^#{1,6}\s+", line):
            break
        if in_facts and line.lstrip().startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if set("".join(cells)) <= set("-: "):
                continue
            rows.append(cells)
    return rows[1:] if rows else rows  # drop header


def key(cells):
    pointer = cells[1].strip("`")
    span = cells[5]
    anchor = cells[7].strip("`")
    return (pointer, span, anchor)


def main():
    r95 = [key(c) for c in fact_rows(R95)]
    r96 = [key(c) for c in fact_rows(R96)]
    print(f"r95 fact rows={len(r95)} r96 fact rows={len(r96)}")
    ok = True
    for i, (a, b) in enumerate(zip(r95, r96), 1):
        same = a == b
        ok = ok and same
        print(f"{'SAME' if same else 'DIFF'} J{i:02d} r95={a}")
        if not same:
            print(f"          r96={b}")
    extra = r96[len(r95):]
    print(f"extra r96 rows={len(extra)}: {extra}")
    ok = ok and len(extra) == 1
    print("ROWS", "ALL-OK" if ok else "PROBLEM")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
