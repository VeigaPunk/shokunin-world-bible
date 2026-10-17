#!/usr/bin/env python3
"""Independent cross-check: parse self-test stdout, compare to persisted contract."""
import json, re, subprocess, sys, hashlib, pathlib
ROOT = pathlib.Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
TOOL = ROOT / "corpus/tools/map_obligations.py"
CONTRACT = ROOT / "corpus/tools/map-obligations-contract.json"
out = sys.argv[1] if len(sys.argv) > 1 else None
stdout = pathlib.Path(out).read_text() if out else subprocess.run(
    [sys.executable, str(TOOL), "--self-test"], cwd=ROOT, capture_output=True, text=True).stdout
line_re = re.compile(r"^SELF-TEST (PASS|FAIL) (\S+) exit=(\d+) findings=(.+)$")
seen = {}
for line in stdout.splitlines():
    m = line_re.match(line)
    if m:
        verdict, cid, exit_code, findings = m.groups()
        fids = [] if findings == "none" else re.findall(r"'([^']+)'", findings)
        seen[cid] = {"verdict": verdict, "exit": int(exit_code), "finding_ids": sorted(fids)}
contract = json.loads(CONTRACT.read_text())
cases = {c["id"]: c for c in contract["self_test"]["cases"]}
print(f"contract_cases={len(cases)} printed_cases={len(seen)}")
print(f"id_sets_equal={set(cases) == set(seen)}")
mismatches = []
for cid, c in cases.items():
    if cid not in seen:
        mismatches.append(f"{cid}: missing from stdout"); continue
    s = seen[cid]
    if s["exit"] != c["exit"]:
        mismatches.append(f"{cid}: exit contract={c['exit']} printed={s['exit']}")
    if s["finding_ids"] != sorted(c["finding_ids"]):
        mismatches.append(f"{cid}: findings contract={sorted(c['finding_ids'])} printed={s['finding_ids']}")
    if s["verdict"] != "PASS":
        mismatches.append(f"{cid}: verdict {s['verdict']}")
print("MISMATCHES:", mismatches if mismatches else "NONE")
print("RESULT line:", [l for l in stdout.splitlines() if l.startswith("RESULT ")])
print("special cases:", {k: cases[k] for k in ("schema_drift", "inventory_mismatch") if k in cases})
print("contract_sha256:", hashlib.sha256(CONTRACT.read_bytes()).hexdigest())
print("tool_sha256:", hashlib.sha256(TOOL.read_bytes()).hexdigest())
