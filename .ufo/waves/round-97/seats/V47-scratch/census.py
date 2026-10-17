#!/usr/bin/env python3
"""V47 census harness: repo-relative check_bible.py run over corpus/fixtures/* dirs."""
import subprocess
import sys
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
FIX = ROOT / "corpus/fixtures"
CHECKER = "corpus/fixtures/check_bible.py"


def main():
    dirs = sorted(p for p in FIX.iterdir() if p.is_dir())
    clean = negative = other = 0
    violation_lines = 0
    changed = []
    for d in dirs:
        rel = f"corpus/fixtures/{d.name}"
        r = subprocess.run(
            ["python3", CHECKER, rel], cwd=ROOT, capture_output=True, text=True
        )
        if r.returncode == 0:
            clean += 1
        elif r.returncode == 1:
            negative += 1
            violation_lines += len([l for l in r.stdout.splitlines() if l.strip()])
        else:
            other += 1
            changed.append((rel, r.returncode))
    print(f"CENSUS dirs={len(dirs)} clean={clean} negative={negative} other={other} violation_lines={violation_lines}")
    for rel, rc in changed:
        print(f"  NON-0/1 EXIT {rel} -> {rc}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
