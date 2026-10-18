#!/usr/bin/env python3
"""V04: compare observed r95-tool runs against the r94 F11 baseline table.

Baseline IDs quoted from .ufo/waves/round-94/followup/F11-c2-negative.md
(its section 3 table, corroborated by its section 4 self-test dump):
  base -> PASS exit 0 no findings
  a    -> FAIL exit 1 missing_obligation
  b    -> FAIL exit 1 duplicate_mapping
  c    -> FAIL exit 1 phantom_obligation
  d    -> FAIL exit 1 source_id_mismatch
  e    -> ERROR exit 2 malformed_json
  f1   -> ERROR exit 2 map_missing   (nonexistent map file)
  f2   -> ERROR exit 2 foreign_path  (map outside cluster)
  f3   -> ERROR exit 2 unsafe_path   (traversal in --map)
  f4   -> ERROR exit 2 map_missing   (map path is a directory; F11's extra variant)
"""
import re
import sys
from pathlib import Path

RUNS = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent / "runs-new"

EXPECTED = {
    "base": ("PASS", 0, []),
    "a": ("FAIL", 1, ["missing_obligation"]),
    "b": ("FAIL", 1, ["duplicate_mapping"]),
    "c": ("FAIL", 1, ["phantom_obligation"]),
    "d": ("FAIL", 1, ["source_id_mismatch"]),
    "e": ("ERROR", 2, ["malformed_json"]),
    "f1": ("ERROR", 2, ["map_missing"]),
    "f2": ("ERROR", 2, ["foreign_path"]),
    "f3": ("ERROR", 2, ["unsafe_path"]),
    "f4": ("ERROR", 2, ["map_missing"]),
}

def parse(path):
    text = path.read_text(encoding="utf-8")
    ids = re.findall(r"^FINDING ([a-z_]+):", text, re.M)
    res = re.search(r"^RESULT ([A-Z]+)$", text, re.M)
    code = re.search(r"^EXIT=(\d+)$", text, re.M)
    return (res.group(1) if res else None, int(code.group(1)) if code else None, ids)

ok = True
for case, (eres, ecode, eids) in EXPECTED.items():
    for passn in (1, 2):
        p = RUNS / f"{case}-run{passn}.out"
        if not p.exists():
            print(f"{case} pass{passn}: MISSING FILE {p}"); ok = False; continue
        res, code, ids = parse(p)
        same = (res == eres and code == ecode and ids == eids)
        status = "MATCH" if same else "CHANGED"
        if not same:
            ok = False
        print(f"{case} pass{passn}: {status} observed=({res},{code},{ids}) expected=({eres},{ecode},{eids})")

# byte stability between passes
for case in EXPECTED:
    p1, p2 = RUNS / f"{case}-run1.out", RUNS / f"{case}-run2.out"
    if p1.exists() and p2.exists():
        same = p1.read_bytes() == p2.read_bytes()
        print(f"{case} stability: {'IDENTICAL' if same else 'DIFFERS'}")
        if not same:
            ok = False

print("VERDICT:", "ALL-MATCH" if ok else "DELTA-FOUND")
