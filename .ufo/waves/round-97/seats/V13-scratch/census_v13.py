#!/usr/bin/env python3
"""V13 (round 97) independent census: repo-relative check_bible run over every
fixture directory. Counts directories, exit-0 clean, exit-1 negative, violation
lines, and any non-0/1 exit. Fresh implementation, repo-relative argv."""
import json
import os
import subprocess
import sys

REPO = "/home/vgpnk/Projects/shokunin/lore-shokunin"
ROOT = os.path.join(REPO, "corpus/fixtures")

dirs = sorted(
    d for d in os.listdir(ROOT)
    if os.path.isdir(os.path.join(ROOT, d))
)

clean = negative = 0
violation_lines = 0
odd = []
receipts = {}
for d in dirs:
    rel = "corpus/fixtures/%s" % d
    p = subprocess.run(
        [sys.executable, "corpus/fixtures/check_bible.py", rel],
        cwd=REPO, capture_output=True, text=True,
    )
    out = (p.stdout + p.stderr).strip()
    receipts[rel] = {"exit": p.returncode, "stdout": out}
    if p.returncode == 0:
        clean += 1
    elif p.returncode == 1:
        negative += 1
        for line in out.splitlines():
            if line.strip().startswith("VIOLATION"):
                violation_lines += 1
    else:
        odd.append((rel, p.returncode, out))

result = {
    "fixture_dirs": len(dirs),
    "clean_exit0": clean,
    "negative_exit1": negative,
    "violation_lines": violation_lines,
    "non_0_1_exits": odd,
    "clean_dirs": sorted(k for k, v in receipts.items() if v["exit"] == 0),
}
print(json.dumps(result, indent=2))
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "census_v13_receipts.json"), "w") as fh:
    json.dump(receipts, fh, indent=2, sort_keys=True)
