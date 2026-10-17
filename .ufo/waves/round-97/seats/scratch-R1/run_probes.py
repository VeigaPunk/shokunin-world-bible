#!/usr/bin/env python3
"""R1 scratch probe: loader strictness + load-bearing pin demonstrations.

Builds isolated tool+contract roots under scratch (each copy's ROOT is scratch-local,
so its self-test temp trees stay in scratch) and runs --self-test in each.
Usage: run_probes.py <outfile>
"""
import json
import pathlib
import subprocess
import sys

REPO = pathlib.Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SC = REPO / ".ufo/waves/round-97/seats/scratch-R1"
TOOL = REPO / "corpus/tools/map_obligations.py"
CONTRACT = REPO / "corpus/tools/map-obligations-contract.json"
OUT = SC / "probes"

delivered = TOOL.read_text(encoding="utf-8")
baseline = subprocess.run(
    ["git", "-C", str(REPO), "show", "f3e09f9:corpus/tools/map_obligations.py"],
    capture_output=True, text=True, check=True,
).stdout
live = json.loads(CONTRACT.read_text(encoding="utf-8"))
cases = live["self_test"]["cases"]
ids = [case["id"] for case in cases]


def without(*dropped):
    return [case for case in cases if case["id"] not in dropped]


neutralized = delivered.replace("            if mention is not None:\n", "            if False:\n")
assert neutralized != delivered, "neutralization did not apply"
assert "dual_pointer" in ids, "live contract does not pin dual_pointer"

VARIANTS = {
    "delivered-live25": (delivered, cases, "25-case live contract, delivered tool"),
    "delivered-drop-dual": (delivered, without("dual_pointer"), "24 cases: dual_pointer pin dropped"),
    "delivered-drop-schema": (delivered, without("schema_drift"), "24 cases: schema_drift pin dropped"),
    "delivered-drop-inventory": (delivered, without("inventory_mismatch"), "24 cases: inventory_mismatch pin dropped"),
    "baseline-drop-dual": (baseline, without("dual_pointer"), "24 cases: dual_pointer dropped, r96 tool"),
    "baseline-drop-schema": (baseline, without("schema_drift"), "24 cases: schema_drift dropped, r96 tool"),
    "neutralized-live25": (neutralized, cases, "25-case contract, dual_pointer emission neutralized"),
}

lines = [
    f"live contract: {len(cases)} cases, dual_pointer pinned={'dual_pointer' in ids}",
    f"delivered tool sha256: {__import__('hashlib').sha256(delivered.encode()).hexdigest()}",
    f"baseline (f3e09f9) tool sha256: {__import__('hashlib').sha256(baseline.encode()).hexdigest()}",
    "",
]
for name, (text, variant_cases, note) in VARIANTS.items():
    root = OUT / name
    (root / "corpus/tools").mkdir(parents=True, exist_ok=True)
    (root / "corpus/tools/map_obligations.py").write_text(text, encoding="utf-8")
    contract = json.loads(json.dumps(live))
    contract["self_test"]["cases"] = variant_cases
    (root / "corpus/tools/map-obligations-contract.json").write_text(
        json.dumps(contract, indent=2) + "\n", encoding="utf-8")
    result = subprocess.run(
        [sys.executable, str(root / "corpus/tools/map_obligations.py"), "--self-test"],
        cwd=str(REPO), capture_output=True, text=True, check=False,
    )
    lines.append(f"=== {name} — {note} — exit={result.returncode} ===")
    body = [line for line in result.stdout.splitlines() if line.strip()]
    if len(body) > 8:
        shown = [*body[:3], "…", *body[-3:]]
    else:
        shown = body
    lines.extend(shown)
    if result.stderr:
        lines.append("STDERR " + result.stderr.strip())
    lines.append("")

report = "\n".join(lines)
print(report)
if len(sys.argv) > 1:
    pathlib.Path(sys.argv[1]).write_text(report, encoding="utf-8")
