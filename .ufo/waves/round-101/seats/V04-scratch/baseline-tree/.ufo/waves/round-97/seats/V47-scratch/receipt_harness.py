#!/usr/bin/env python3
"""V47 receipt harness: measure every declared ratio and print machine-checkable receipts."""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
FIX = ROOT / "corpus/fixtures"


def run(args):
    r = subprocess.run(args, cwd=ROOT, capture_output=True, text=True)
    return r.returncode, r.stdout, r.stderr


def main():
    out = {}

    # --- 25/25: map_obligations self-test ---
    rc, so, se = run(["python3", "corpus/tools/map_obligations.py", "--self-test"])
    passes = [l for l in so.splitlines() if l.startswith("SELF-TEST PASS")]
    fails = [l for l in so.splitlines() if l.startswith("SELF-TEST FAIL")]
    out["map_selftest"] = {"exit": rc, "pass": len(passes), "fail": len(fails),
                           "result": [l for l in so.splitlines() if l.startswith("RESULT")]}
    contract = json.load(open(ROOT / "corpus/tools/map-obligations-contract.json"))
    cases = contract["self_test"]["cases"]
    ids = [c["id"] for c in cases]
    out["map_contract_cases"] = len(cases)
    out["map_contract_has_dual_pointer"] = "dual_pointer" in ids
    out["map_contract_ids_tail"] = ids[-6:]

    # --- 17/17 obligations + TOTAL 19/19: r97 fixture map run ---
    r97 = FIX / "r97-crossing-acknowledgment"
    if r97.is_dir():
        rc, so, se = run(["python3", "corpus/tools/map_obligations.py",
                          "corpus/fixtures/r97-crossing-acknowledgment"])
        out["r97_map"] = {"exit": rc, "stdout": so.strip().splitlines(), "stderr": se.strip()}
        # also r96 post-repair run (receipts must be unchanged by cosmetic repair)
        rc, so, se = run(["python3", "corpus/tools/map_obligations.py",
                          "corpus/fixtures/r96-crossing-response"])
        out["r96_map_postrepair"] = {"exit": rc, "stdout": so.strip().splitlines()}
    else:
        out["r97_map"] = None

    # --- 16/16: dependency_freeze self-test ---
    rc, so, se = run(["python3", "corpus/tools/dependency_freeze.py", "--self-test"])
    m = re.search(r"SELF-TEST (\d+)/(\d+)", so)
    out["freeze_selftest"] = {"exit": rc, "ratio": m.group(0) if m else None,
                              "lines": so.strip().splitlines()}
    fc = json.load(open(ROOT / "corpus/tools/dependency-freeze-contract.json"))
    out["freeze_contract_pins"] = sorted(fc["pins"].keys())
    out["freeze_contract_expected_cases"] = sorted(fc["self_test"]["expected"].keys())
    out["freeze_contract_expected_n"] = len(fc["self_test"]["expected"])

    # --- chain: verify each pinned fixture ---
    chain = []
    for name, pin in sorted(fc["pins"].items()):
        path = pin.get("fixture", f"corpus/fixtures/{name}")
        rc, so, se = run(["python3", "corpus/tools/dependency_freeze.py", path])
        chain.append({"fixture": path, "exit": rc, "stdout": so.strip().splitlines(),
                      "stderr": se.strip()})
    out["freeze_chain"] = chain
    out["freeze_chain_clean"] = sum(1 for c in chain if c["exit"] == 0)

    # --- census ---
    dirs = sorted(p for p in FIX.iterdir() if p.is_dir())
    clean = negative = other = vlines = 0
    odd = []
    for d in dirs:
        rel = f"corpus/fixtures/{d.name}"
        rc, so, se = run(["python3", "corpus/fixtures/check_bible.py", rel])
        if rc == 0:
            clean += 1
        elif rc == 1:
            negative += 1
            vlines += sum(1 for l in so.splitlines() if l.startswith("VIOLATION"))
        else:
            other += 1
            odd.append((rel, rc))
    out["census"] = {"dirs": len(dirs), "clean": clean, "negative": negative,
                     "other": other, "violation_lines": vlines, "odd": odd}

    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    sys.exit(main())
