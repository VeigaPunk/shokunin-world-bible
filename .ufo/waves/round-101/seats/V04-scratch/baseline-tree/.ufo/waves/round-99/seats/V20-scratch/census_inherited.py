#!/usr/bin/env python3
"""Null control: check_bible over fixture dirs excluding r99-window-lapse."""
import hashlib
import json
import os
import subprocess
import sys

REPO = "/home/vgpnk/Projects/shokunin/lore-shokunin"
ROOT = os.path.join(REPO, "corpus/fixtures")
skip = {"r99-window-lapse"}
dirs = sorted(
    d for d in os.listdir(ROOT)
    if os.path.isdir(os.path.join(ROOT, d)) and d not in skip
)
clean = negative = violation_lines = 0
odd = []
receipts = {}
for d in dirs:
    rel = "corpus/fixtures/%s" % d
    p = subprocess.run(
        [sys.executable, "corpus/fixtures/check_bible.py", rel],
        cwd=REPO,
        capture_output=True,
        text=True,
    )
    out = (p.stdout + p.stderr).strip()
    receipts[rel] = {
        "exit": p.returncode,
        "stdout_sha256": hashlib.sha256(out.encode()).hexdigest(),
    }
    if p.returncode == 0:
        clean += 1
    elif p.returncode == 1:
        negative += 1
        violation_lines += sum(1 for line in out.splitlines() if "VIOLATION" in line)
    else:
        odd.append([rel, p.returncode, out[:400]])
res = {
    "fixture_dirs": len(dirs),
    "clean_exit0": clean,
    "negative_exit1": negative,
    "violation_lines": violation_lines,
    "non_0_1_exits": odd,
}
print(json.dumps(res))
out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "census_inherited_receipts.json")
with open(out_path, "w") as fh:
    json.dump(receipts, fh, indent=1, sort_keys=True)
    fh.write("\n")
