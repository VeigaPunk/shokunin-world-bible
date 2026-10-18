#!/usr/bin/env python3
"""V29 census replica (fresh, r96 doc-parity).

Counts, over top-level directories of a fixtures root, using repo-relative
argv exactly as the r95 closure census did:
  - fixture directory count
  - exit-0 (clean) count
  - exit-1 (intentional negative) count
  - any other exits (listed)
  - VIOLATION line count in stdout

Usage: census_r96.py [fixtures-root]   (run from the repo root)
"""
import json
import os
import subprocess
import sys

root = sys.argv[1] if len(sys.argv) > 1 else "corpus/fixtures"
dirs = sorted(d for d in os.listdir(root) if os.path.isdir(os.path.join(root, d)))
clean = neg = other = viol = 0
others = []
for d in dirs:
    p = subprocess.run(
        ["python3", "corpus/fixtures/check_bible.py", f"{root}/{d}"],
        capture_output=True, text=True,
    )
    if p.returncode == 0:
        clean += 1
    elif p.returncode == 1:
        neg += 1
    else:
        other += 1
        others.append((d, p.returncode))
    viol += sum(1 for line in p.stdout.splitlines() if "VIOLATION" in line)
print(json.dumps({
    "dirs": len(dirs), "clean": clean, "negative": neg, "other": other,
    "violation_lines": viol, "other_dirs": others,
}, indent=1))
