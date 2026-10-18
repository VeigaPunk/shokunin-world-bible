#!/usr/bin/env python3
"""V46 scratch: parse J##/S## rows from two claim-excerpt-map.md files, cell-by-cell diff."""
import re
import sys


def rows(path):
    out = {}
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            m = re.match(r"\|\s*(J\d+|S\d+)\s*\|", line)
            if m:
                cells = [c.strip() for c in line.rstrip("\n").strip("|").split("|")]
                out[m.group(1)] = cells
    return out


a, b = rows(sys.argv[1]), rows(sys.argv[2])
na, nb = set(a), set(b)
print(f"A rows: {len(a)}  B rows: {len(b)}")
print(f"B-only: {sorted(nb - na)}  A-only: {sorted(na - nb)}")
for k in sorted(na & nb, key=lambda x: (x[0], int(x[1:]))):
    ca, cb = a[k], b[k]
    if ca == cb:
        continue
    diffs = []
    if len(ca) != len(cb):
        diffs.append(f"CELLCOUNT {len(ca)} vs {len(cb)}")
    for i, (x, y) in enumerate(zip(ca, cb)):
        if x != y:
            diffs.append((i, x, y))
    print(f"{k}: cells={len(ca)}/{len(cb)} diffs={diffs}")
