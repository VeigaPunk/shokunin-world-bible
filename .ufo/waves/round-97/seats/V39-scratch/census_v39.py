#!/usr/bin/env python3
"""V39 census replica (r97 integration checklist).

Replicates the r95/r96 closure census recipe: over top-level directories of a
fixtures root, repo-relative argv, count exit codes, VIOLATION lines, and
non-empty stderr. Usage: census_v39.py [fixtures-root] (run from repo root).
"""
import json
import os
import subprocess
import sys

root = sys.argv[1] if len(sys.argv) > 1 else "corpus/fixtures"
dirs = sorted(d for d in os.listdir(root) if os.path.isdir(os.path.join(root, d)))
clean = neg = other = viol = stderr_nonempty = 0
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
    if p.stderr.strip():
        stderr_nonempty += 1
print(json.dumps({
    "dirs": len(dirs), "clean": clean, "negative": neg, "other": other,
    "violation_lines": viol, "stderr_nonempty": stderr_nonempty,
    "other_dirs": others,
}, indent=1))
