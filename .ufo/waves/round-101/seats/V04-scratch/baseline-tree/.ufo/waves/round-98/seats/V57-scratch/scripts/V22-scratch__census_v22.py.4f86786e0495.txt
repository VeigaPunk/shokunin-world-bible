#!/usr/bin/env python3
"""V22 (round 98) independent corpus census, fresh implementation.

Repo-relative check_bible.py run over every direct fixture directory.
Counts: directories, exit-0 clean, exit-1 intentional negative, VIOLATION
lines, any non-0/1 exit. Writes a JSON receipt and a per-dir log.
"""
import json
import os
import subprocess
import sys

REPO = "/home/vgpnk/Projects/shokunin/lore-shokunin"
ROOT = os.path.join(REPO, "corpus/fixtures")
OUT = os.path.join(REPO, ".ufo/waves/round-98/seats/V22-scratch")

dirs = sorted(d for d in os.listdir(ROOT) if os.path.isdir(os.path.join(ROOT, d)))
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
        odd.append({"path": rel, "exit": p.returncode, "out": out})

result = {
    "dirs": len(dirs),
    "clean": clean,
    "negative": negative,
    "violation_lines": violation_lines,
    "non01": odd,
    "dir_list": dirs,
}
with open(os.path.join(OUT, "census.json"), "w") as f:
    json.dump(result, f, indent=2, sort_keys=True)
print(json.dumps({k: v for k, v in result.items() if k != "dir_list"}, sort_keys=True))
