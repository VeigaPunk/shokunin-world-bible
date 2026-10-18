#!/usr/bin/env python3
"""Compare JSON-facts rows (pointer/anchor/span) between two maps."""
import re, sys
from pathlib import Path

def rows(path):
    out = []
    for line in Path(path).read_text().splitlines():
        if not line.startswith('| J'):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        rid, pointer, source, ns, epath, span, mode, anchor = cells[:8]
        out.append((rid, pointer, anchor.strip('`'), span, mode))
    return out

a, b = sys.argv[1], sys.argv[2]
ra, rb = rows(a), rows(b)
print(f"rows_a={len(ra)} rows_b={len(rb)}")
da = {r[1]: r for r in ra}
db = {r[1]: r for r in rb}
inherited = [r for r in rb if r[0] in {x[0] for x in ra}]
print(f"same-ID rows in b: {len(inherited)}")
bad = 0
for r in ra:
    other = db.get(r[1])
    if other is None:
        print(f"NEW-IN-B: {r[0]} {r[1]}")
        continue
    if (r[2], r[3], r[4]) != (other[2], other[3], other[4]):
        bad += 1
        print(f"CHANGED: {r[0]} {r[1]}\n  a={(r[2],r[3],r[4])}\n  b={(other[2],other[3],other[4])}")
print(f"changed_inherited={bad}")
