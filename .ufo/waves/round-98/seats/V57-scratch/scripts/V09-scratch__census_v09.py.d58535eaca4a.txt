#!/usr/bin/env python3
"""V09 (round 98) independent census: fresh implementation, repo-relative
check_bible run over every fixture directory. Counts dirs, exit-0 clean,
exit-1 negative, VIOLATION lines, non-0/1 exits. Writes receipts JSON next
to this script (name given as argv[1] suffix)."""
import json
import os
import subprocess
import sys

REPO = "/home/vgpnk/Projects/shokunin/lore-shokunin"
ROOT = os.path.join(REPO, "corpus/fixtures")

exclude = set(sys.argv[2:])
dirs = sorted(
    d for d in os.listdir(ROOT)
    if os.path.isdir(os.path.join(ROOT, d)) and d not in exclude
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
tag = sys.argv[1] if len(sys.argv) > 1 else "run"
here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "census_v09_%s.json" % tag), "w") as fh:
    json.dump(receipts, fh, indent=2, sort_keys=True)
print(json.dumps({k: v for k, v in result.items() if k != "clean_dirs"},
                 indent=2))
print("clean_dirs_count", len(result["clean_dirs"]))
