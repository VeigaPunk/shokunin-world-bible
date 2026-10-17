#!/usr/bin/env python3
"""V18 scratch: compare r96 (post-repair) and r97 map rows cell-by-cell.

Usage: python3 rows.py <r96-map> <r97-map>
Prints per-row cell comparisons for the JSON-facts table (J*) and
editorial table (S*), ignoring only the path-qualification cell (col index 3
in the J table) which is expected to change namespace per fixture.
"""
import sys


def rows(path):
    out = {}
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if all(set(c) <= set("-: ") and c for c in cells):
            continue
        if cells[0] in ("ID",):
            continue
        out[cells[0]] = cells
    return out


a, b = rows(sys.argv[1]), rows(sys.argv[2])
print("rows in r96:", len(a), "rows in r97:", len(b))
print("ids only-r96:", sorted(set(a) - set(b)), "ids only-r97:", sorted(set(b) - set(a)))
changed_any = False
for rid in [f"J{i:02d}" for i in range(1, 30)] + ["S01", "S02"]:
    if rid not in a or rid not in b:
        continue
    ca, cb = a[rid], b[rid]
    if len(ca) != len(cb):
        print(f"{rid}: CELL-COUNT DIFF {len(ca)} vs {len(cb)}")
        changed_any = True
        continue
    diffs = [i for i, (x, y) in enumerate(zip(ca, cb)) if x != y]
    # path-qualification column is index 3 in both tables
    non_pq = [i for i in diffs if i != 3]
    if non_pq:
        print(f"{rid}: NON-PQ CELL DIFF at cols {non_pq}")
        for i in non_pq:
            print(f"    col{i}: r96={ca[i]!r}")
            print(f"    col{i}: r97={cb[i]!r}")
        changed_any = True
    elif diffs:
        print(f"{rid}: only path-qualification cell differs")
print("VERDICT:", "NON-PQ-DIFFS-FOUND" if changed_any else "ALL-SHARED-ROWS-NON-PQ-IDENTICAL")
