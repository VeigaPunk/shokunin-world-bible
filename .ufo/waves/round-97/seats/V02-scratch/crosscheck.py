#!/usr/bin/env python3
"""Independent cross-check: contract expectations vs printed --self-test behavior.

Usage: crosscheck.py <selftest_stdout> [contract_path]
No contract-writing code here; read-only parser.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
contract_path = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "corpus/tools/map-obligations-contract.json"
out = Path(sys.argv[1]).read_text(encoding="utf-8")

contract = json.loads(contract_path.read_text(encoding="utf-8"))
cases = contract.get("self_test", {}).get("cases")
if not isinstance(cases, list):
    print("contract self_test.cases not a list")
    sys.exit(3)
persisted = {c["id"]: (c["exit"], sorted(c["finding_ids"])) for c in cases}

printed = {}
pinned_line = None
for line in out.splitlines():
    m = re.match(r"^SELF-TEST CASES (\d+)/(\d+) pinned$", line)
    if m:
        pinned_line = (int(m.group(1)), int(m.group(2)))
        continue
    m = re.match(r"^SELF-TEST (PASS|FAIL) (\S+) exit=(\d+) findings=(.+)$", line)
    if m:
        status, cid, ex, fnd = m.groups()
        flist = [] if fnd == "none" else re.findall(r"'([^']+)'", fnd)
        printed[cid] = (int(ex), sorted(flist), status)

print(f"contract_cases={len(persisted)} printed_cases={len(printed)} pinned_line={pinned_line}")
print(f"id_sets_equal={set(persisted) == set(printed)}")
mismatches = []
for cid in sorted(set(persisted) | set(printed)):
    if cid not in persisted:
        mismatches.append((cid, "printed but not persisted", printed[cid]))
    elif cid not in printed:
        mismatches.append((cid, "persisted but not printed", persisted[cid]))
    else:
        pex, pfind, status = printed[cid]
        cex, cfind = persisted[cid]
        if pex != cex or pfind != cfind:
            mismatches.append((cid, f"persisted {cex}/{cfind} != printed {pex}/{pfind}", status))
        if status != "PASS":
            mismatches.append((cid, f"status {status}", ""))
print("MISMATCHES: NONE" if not mismatches else "MISMATCHES:")
for row in mismatches:
    print("  ", row)
result_lines = [l for l in out.splitlines() if l.startswith("RESULT ")]
print("RESULT line:", result_lines)
sys.exit(0 if not mismatches and result_lines == ["RESULT PASS"] else 1)
