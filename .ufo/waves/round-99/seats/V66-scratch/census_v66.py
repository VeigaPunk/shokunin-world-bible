#!/usr/bin/env python3
"""V66 independent corpus census. Repo-relative check_bible over direct fixture dirs."""
import json
import os
import subprocess
import sys

REPO = "/home/vgpnk/Projects/shokunin/lore-shokunin"
ROOT = os.path.join(REPO, "corpus/fixtures")
OUT = os.path.join(REPO, ".ufo/waves/round-99/seats/V66-scratch")

dirs = sorted(d for d in os.listdir(ROOT) if os.path.isdir(os.path.join(ROOT, d)))
clean = negative = 0
violation_lines = 0
odd = []
per = []
for d in dirs:
    rel = "corpus/fixtures/%s" % d
    p = subprocess.run(
        [sys.executable, "corpus/fixtures/check_bible.py", rel],
        cwd=REPO, capture_output=True, text=True,
    )
    out = (p.stdout + p.stderr).strip()
    vcount = sum(1 for line in out.splitlines() if line.strip().startswith("VIOLATION"))
    per.append({"path": rel, "exit": p.returncode, "violations": vcount, "head": out.splitlines()[:2]})
    if p.returncode == 0:
        clean += 1
    elif p.returncode == 1:
        negative += 1
        violation_lines += vcount
    else:
        odd.append({"path": rel, "exit": p.returncode, "out": out[:500]})

result = {
    "dirs": len(dirs),
    "clean": clean,
    "negative": negative,
    "violation_lines": violation_lines,
    "non01": odd,
    "has_r99": "r99-window-lapse" in dirs,
    "r99_exit": next((x["exit"] for x in per if x["path"].endswith("r99-window-lapse")), None),
}
with open(os.path.join(OUT, "census.json"), "w") as f:
    json.dump({"summary": result, "per": per}, f, indent=2)
print(json.dumps(result, sort_keys=True))
