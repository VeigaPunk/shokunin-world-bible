#!/usr/bin/env python3
"""Classify every 8-hex sha256 pin in a note: CURRENT-MATCH (equals a working-tree
tool file) / HISTORICAL (equals a committed revision of some tool file) / UNVERIFIED."""
import re, sys, os, hashlib, subprocess
LANE = "/home/vgpnk/Projects/shokunin/lore-shokunin"
CAND = ["corpus/tools/map_obligations.py", "corpus/tools/dependency_freeze.py",
        "corpus/tools/support_check.py", "corpus/fixtures/check_bible.py",
        "corpus/tools/map-obligations-contract.json", "corpus/tools/dependency-freeze-contract.json"]
cur = {}
for c in CAND:
    p = os.path.join(LANE, c)
    if os.path.exists(p):
        cur[hashlib.sha256(open(p,'rb').read()).hexdigest()[:8]] = c
hist = {}
for c in CAND:
    out = subprocess.run(["git","log","--format=%H %h %s","--",c], cwd=LANE, capture_output=True, text=True).stdout
    for line in out.splitlines():
        full, short, subj = line.split(" ", 2)
        blob = subprocess.run(["git","show",f"{full}:{c}"], cwd=LANE, capture_output=True).stdout
        h = hashlib.sha256(blob).hexdigest()[:8]
        hist.setdefault(h, f"{c}@{short}")
        hist.setdefault(h, f"{c}@{short}")
text = open(sys.argv[1], encoding="utf-8").read()
pins = re.findall(r"`([0-9a-f]{8})…`", text)
uniq = sorted(set(pins))
for h in uniq:
    if h in cur:
        print(f"CURRENT-MATCH {h} = working tree {cur[h]}")
    elif h in hist:
        print(f"HISTORICAL    {h} = committed revision {hist[h]}")
    else:
        print(f"UNVERIFIED    {h}  <-- not a current tool hash nor a committed tool revision")
print(f"--- distinct pins={len(uniq)}")
