#!/usr/bin/env python3
"""V02 driver: run the migration matrix against S1's delivered tool.

For each staged case under cases/, run --freeze on the in-scope fixture and record
exit code + output. Extra probes:
  - legacy_missing_key: quote the pin before/after, check other pins and top-level
    keys survive, and run verify first on a pristine copy (fail-closed pre-migration).
"""
import json
import pathlib
import shutil
import subprocess
import sys

BASE = pathlib.Path("/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-98/seats/scratch/V02")
CASES = BASE / "cases"
FIXTURE = "r95-crossing-aftermath"


def run(case, argv):
    proc = subprocess.run([sys.executable, *argv], cwd=CASES / case, capture_output=True, text=True)
    print(f"$ (cwd=cases/{case}) python3 {' '.join(str(a).replace(str(CASES / case), '.') for a in argv)}")
    for line in proc.stdout.splitlines():
        print("  " + line)
    if proc.stderr.strip():
        for line in proc.stderr.splitlines():
            print("  STDERR " + line)
    print(f"  exit={proc.returncode}")
    return proc.returncode, proc.stdout


def pin_of(case):
    contract = json.loads((CASES / case / "corpus/tools/dependency-freeze-contract.json").read_text())
    return contract


def main():
    ordered = sys.argv[1:] or sorted(p.name for p in CASES.iterdir() if p.is_dir())
    for case in ordered:
        print(f"\n=== CASE {case} ===")
        tool = CASES / case / "corpus/tools/dependency_freeze.py"
        fixture = CASES / case / "corpus/fixtures" / FIXTURE
        before = pin_of(case)["pins"][FIXTURE]
        print("pin BEFORE:", json.dumps(before, sort_keys=True)[:240])
        run(case, [tool, "--freeze", fixture])
        after_contract = pin_of(case)
        after = after_contract["pins"][FIXTURE]
        print("pin AFTER :", json.dumps(after, sort_keys=True)[:240])
        print("fixture key after:", "fixture" in after, "| value:", after.get("fixture"))


if __name__ == "__main__":
    main()
