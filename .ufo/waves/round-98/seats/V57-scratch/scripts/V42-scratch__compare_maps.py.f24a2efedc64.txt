#!/usr/bin/env python3
"""V42 comparator: parse the JSON-facts tables of the r97 and r98 maps and
compare inherited rows (J01..J17) parsed-value; report the new rows and the
declared inventory line vs parsed counts. Read-only."""
import re, sys, json

def parse_map(path):
    text = open(path, encoding="utf-8").read()
    inv = None
    m = re.search(r"\*\*Expected inventory:\*\*\s*(.+)", text)
    if m:
        inv = m.group(1).strip()
    rows = {}
    for line in text.splitlines():
        if not line.startswith("| J"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        # ID | pointer | source | namespace | excerpt | span | mode | anchor
        if len(cells) < 8:
            continue
        rid = cells[0]
        rows[rid] = {
            "pointer": cells[1],
            "source_id": cells[2],
            "namespace": cells[3],
            "excerpt": cells[4],
            "span": cells[5],
            "mode": cells[6],
            "anchor": cells[7],
        }
    # editorial rows S01/S02 for completeness
    for line in text.splitlines():
        if not line.startswith("| S"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 7:
            rows[cells[0]] = {"editorial": cells[1:7]}
    return inv, rows

a_inv, a = parse_map(sys.argv[1])
b_inv, b = parse_map(sys.argv[2])
print("A inventory:", a_inv)
print("B inventory:", b_inv)
print("A rows:", len(a), "B rows:", len(b))
new = sorted(set(b) - set(a))
missing = sorted(set(a) - set(b))
print("new rows in B:", new)
print("missing rows in B:", missing)
diffs = []
for rid in sorted(set(a) & set(b)):
    if a[rid] != b[rid]:
        diffs.append(rid)
print("changed inherited rows:", diffs)
for rid in diffs:
    for k in a[rid]:
        if a[rid][k] != b[rid].get(k):
            print(f"  {rid}.{k}:\n    A: {a[rid][k]}\n    B: {b[rid].get(k)}")
for rid in new:
    print(f"  {rid}: {json.dumps(b[rid], ensure_ascii=False)}")
