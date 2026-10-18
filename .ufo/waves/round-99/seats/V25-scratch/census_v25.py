#!/usr/bin/env python3
"""V25 (round 99) independent corpus census.

Repo-relative check_bible.py over every direct fixture directory.
Counts: directories, exit-0 clean, exit-1 intentional negative, VIOLATION
lines, any non-0/1 exit.
"""
import json
import os
import subprocess
import sys

REPO = "/home/vgpnk/Projects/shokunin/lore-shokunin"
ROOT = os.path.join(REPO, "corpus/fixtures")
OUT = os.path.join(REPO, ".ufo/waves/round-99/seats/V25-scratch")

dirs = sorted(d for d in os.listdir(ROOT) if os.path.isdir(os.path.join(ROOT, d)))
clean = negative = 0
violation_lines = 0
odd = []
per = {}
for d in dirs:
    rel = "corpus/fixtures/%s" % d
    p = subprocess.run(
        [sys.executable, "corpus/fixtures/check_bible.py", rel],
        cwd=REPO, capture_output=True, text=True,
    )
    out = (p.stdout + p.stderr).strip()
    vcount = 0
    if p.returncode == 0:
        clean += 1
    elif p.returncode == 1:
        negative += 1
        for line in out.splitlines():
            if line.strip().startswith("VIOLATION"):
                violation_lines += 1
                vcount += 1
    else:
        odd.append({"path": rel, "exit": p.returncode, "out": out})
    per[d] = {"exit": p.returncode, "violations": vcount}

result = {
    "dirs": len(dirs),
    "clean": clean,
    "negative": negative,
    "violation_lines": violation_lines,
    "non01": odd,
    "r99_present": "r99-window-lapse" in dirs,
    "r99": per.get("r99-window-lapse"),
}
with open(os.path.join(OUT, "census.json"), "w") as f:
    json.dump({"summary": result, "per": per, "dir_list": dirs}, f, indent=2, sort_keys=True)
print(json.dumps(result, sort_keys=True))
