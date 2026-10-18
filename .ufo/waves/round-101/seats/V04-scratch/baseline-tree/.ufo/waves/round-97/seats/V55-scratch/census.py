#!/usr/bin/env python3
"""V55 independent census: run check_bible.py on every directory under corpus/fixtures.

Counts: directories, exit-0 clean, exit-1 negative, other exits, VIOLATION lines.
Repo-relative invocation from the lane root, matching corpus/fixtures/README.md.
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
FIXTURES = ROOT / "corpus/fixtures"

def main():
    dirs = sorted(p for p in FIXTURES.iterdir() if p.is_dir())
    clean = negative = other = 0
    violations = 0
    other_list = []
    for d in dirs:
        rel = "corpus/fixtures/" + d.name
        r = subprocess.run([sys.executable, "corpus/fixtures/check_bible.py", rel],
                           cwd=ROOT, capture_output=True, text=True)
        out = r.stdout + r.stderr
        violations += sum(1 for line in r.stdout.splitlines() if line.startswith("VIOLATION"))
        if r.returncode == 0:
            clean += 1
        elif r.returncode == 1:
            negative += 1
        else:
            other += 1
            other_list.append((rel, r.returncode))
    print(f"DIRS {len(dirs)}; CLEAN {clean}; NEGATIVE {negative}; OTHER {other}; VIOLATION-LINES {violations}")
    for rel, code in other_list:
        print(f"OTHER-EXIT {code}: {rel}")

if __name__ == "__main__":
    main()
