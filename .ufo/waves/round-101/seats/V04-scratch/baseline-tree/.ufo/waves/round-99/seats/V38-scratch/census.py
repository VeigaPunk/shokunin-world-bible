#!/usr/bin/env python3
"""Repo-relative check_bible census. Counts dirs that contain entities.json
(r98 V35 definition) and, separately, every fixture directory."""
import hashlib
import os
import subprocess
import sys

REPO = "/home/vgpnk/Projects/shokunin/lore-shokunin"
ROOT = os.path.join(REPO, "corpus/fixtures")
dirs = sorted(d for d in os.listdir(ROOT) if os.path.isdir(os.path.join(ROOT, d)))
clean = negative = other = vlines = 0
odd = []
with_entities = 0
for d in dirs:
    rel = "corpus/fixtures/%s" % d
    has = os.path.isfile(os.path.join(ROOT, d, "entities.json"))
    if not has:
        continue
    with_entities += 1
    p = subprocess.run(
        [sys.executable, "corpus/fixtures/check_bible.py", rel],
        cwd=REPO, capture_output=True, text=True,
    )
    out = p.stdout + p.stderr
    if p.returncode == 0:
        clean += 1
    elif p.returncode == 1:
        negative += 1
        vlines += sum(1 for line in out.splitlines() if "VIOLATION" in line)
    else:
        other += 1
        odd.append((rel, p.returncode, out.strip()[:200]))
print("CENSUS entities.json dirs=%d clean=%d negative=%d other=%d violation_lines=%d all_dirs=%d" % (
    with_entities, clean, negative, other, vlines, len(dirs)))
for item in odd:
    print("ODD", item)
