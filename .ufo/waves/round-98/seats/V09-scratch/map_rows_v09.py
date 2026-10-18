#!/usr/bin/env python3
"""V09 r98: compare inherited J rows of the r98 map against the r97 map.

Extracts rows from the '## JSON facts' section (lines starting with '| J'),
splits cells, and reports per-row equality (full cells) and equality with the
path-qualification column (index 3) excluded.
"""
import json
import re
import sys

R97 = "corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md"
R98 = "corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md"


def rows(path):
    out = {}
    in_section = False
    for line in open(path):
        if line.startswith("## JSON facts"):
            in_section = True
            continue
        if in_section and line.startswith("## "):
            break
        if in_section and line.startswith("| J"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            out[cells[0]] = cells
    return out


a, b = rows(R97), rows(R98)
report = {"r97_rows": sorted(a), "r98_rows": sorted(b)}
diffs = []
diffs_no_ns = []
for jid in sorted(a):
    if jid not in b:
        diffs.append({"row": jid, "reason": "missing in r98"})
        continue
    if a[jid] != b[jid]:
        cols = [i for i, (x, y) in enumerate(zip(a[jid], b[jid])) if x != y]
        entry = {"row": jid, "diff_cols": cols}
        for i in cols:
            entry["col%d" % i] = {"r97": a[jid][i], "r98": b[jid][i]}
        diffs.append(entry)
    ax = [c for i, c in enumerate(a[jid]) if i != 3]
    bx = [c for i, c in enumerate(b[jid]) if i != 3]
    if ax != bx:
        diffs_no_ns.append(jid)
report["rows_compared"] = len(a)
report["full_cell_diffs"] = diffs
report["diffs_ignoring_namespace_col"] = diffs_no_ns
print(json.dumps(report, indent=2))
