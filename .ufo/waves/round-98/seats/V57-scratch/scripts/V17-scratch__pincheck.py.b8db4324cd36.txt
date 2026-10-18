#!/usr/bin/env python3
"""V17 W05 pin integrity: recompute sha256 for every pinned path, report
mismatch/missing. Usage: pincheck.py <pinfile> [pinfile2 ...]"""
import hashlib, os, sys
REPO = "/home/vgpnk/Projects/shokunin/lore-shokunin"
for pf in sys.argv[1:]:
    pf = pf if os.path.isabs(pf) else os.path.join(REPO, pf)
    rows = [l.split() for l in open(pf) if l.strip()]
    mism, missing, ok = [], [], 0
    for h, p in rows:
        fp = os.path.join(REPO, p)
        if not os.path.exists(fp):
            missing.append(p); continue
        d = hashlib.sha256(open(fp, "rb").read()).hexdigest()
        if d == h: ok += 1
        else: mism.append((p, h, d))
    print("%s: rows=%d ok=%d mismatch=%d missing=%d" % (pf, len(rows), ok, len(mism), len(missing)))
    for p, h, d in mism:
        print("  MISMATCH %s pinned=%s worktree=%s" % (p, h, d))
    for p in missing:
        print("  MISSING %s" % p)
