#!/usr/bin/env python3
"""Compare r96 map rows to r97 map rows modulo cluster-path re-qualification."""
import os
import re

ROOT = "/home/vgpnk/Projects/shokunin/lore-shokunin"
os.chdir(ROOT)
R96 = "corpus/fixtures/r96-crossing-response/claim-excerpt-map.md"
R97 = "corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md"


def rows(path):
    out = {}
    for line in open(path, encoding="utf-8"):
        m = re.match(r"^\|\s*(J\d+|S\d+)\s*\|", line)
        if m:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            out[m.group(1)] = cells
    return out


r96, r97 = rows(R96), rows(R97)
print("r96 row ids:", sorted(r96))
print("r97 row ids:", sorted(r97))
new = sorted(set(r97) - set(r96))
gone = sorted(set(r96) - set(r97))
print("new rows:", new, "gone rows:", gone)
diffs = 0
for rid in sorted(set(r96) & set(r97)):
    a = [c.replace("r96-crossing-response:", "r97-crossing-acknowledgment:") for c in r96[rid]]
    b = r97[rid]
    if a != b:
        diffs += 1
        print(f"DIFF {rid}:")
        for i, (x, y) in enumerate(zip(a, b)):
            if x != y:
                print(f"   cell{i}: r96={x!r}")
                print(f"          r97={y!r}")
        if len(a) != len(b):
            print(f"   cell-count r96={len(a)} r97={len(b)}")
print(f"inherited rows compared: {len(set(r96) & set(r97))}; differing: {diffs}")
for rid in new:
    print(f"new row {rid}: {r97[rid]}")
