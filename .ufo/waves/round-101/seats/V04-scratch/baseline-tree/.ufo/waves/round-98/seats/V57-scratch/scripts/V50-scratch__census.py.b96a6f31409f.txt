#!/usr/bin/env python3
"""V50 census (round 98): check_bible over every fixture dir; violation lines = lines containing VIOLATION."""
import hashlib, json, os, subprocess, sys
REPO = "/home/vgpnk/Projects/shokunin/lore-shokunin"
ROOT = os.path.join(REPO, "corpus/fixtures")
dirs = sorted(d for d in os.listdir(ROOT) if os.path.isdir(os.path.join(ROOT, d)))
clean = negative = violation_lines = 0
odd = []
for d in dirs:
    rel = "corpus/fixtures/%s" % d
    p = subprocess.run([sys.executable, "corpus/fixtures/check_bible.py", rel], cwd=REPO, capture_output=True, text=True)
    out = (p.stdout + p.stderr).strip()
    if p.returncode == 0: clean += 1
    elif p.returncode == 1:
        negative += 1
        violation_lines += sum(1 for line in out.splitlines() if "VIOLATION" in line)
    else: odd.append((rel, p.returncode))
print(json.dumps({"fixture_dirs": len(dirs), "clean_exit0": clean, "negative_exit1": negative, "violation_lines": violation_lines, "non_0_1_exits": odd}))
