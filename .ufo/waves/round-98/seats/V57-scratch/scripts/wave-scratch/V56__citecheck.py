#!/usr/bin/env python3
"""Resolve every cited path / file:line / file#/N in a knowledge note against the
delivered tree. Bare file names resolve against the r98 fixture dir (per the r97
citation-convention). Prints one line per citation: OK / MISSING / OUT-OF-RANGE."""
import re, sys, os, json

LANE = "/home/vgpnk/Projects/shokunin/lore-shokunin"
FX = "corpus/fixtures/r98-clerk-filing"
NOTE = sys.argv[1]

def resolve(p):
    p = p.strip()
    if p.startswith("corpus/") or p.startswith(".ufo/"):
        return os.path.join(LANE, p)
    return os.path.join(LANE, FX, p)

text = open(os.path.join(LANE, NOTE), encoding="utf-8").read()
# find backticked tokens
tokens = re.findall(r"`([^`\n]+)`", text)
cite_re = re.compile(r"^([A-Za-z0-9_./#-]+\.(?:json|md|py|sh|txt))(?::(\d+)(?:-(\d+))?|#/(\d+))?$")
seen = set()
bad = 0
n = 0
for t in tokens:
    m = cite_re.match(t)
    if not m:
        continue
    if t in seen:
        continue
    seen.add(t)
    n += 1
    path, l1, l2, idx = m.group(1), m.group(2), m.group(3), m.group(4)
    full = resolve(path)
    if not os.path.exists(full):
        print(f"MISSING  {t}  -> {os.path.relpath(full, LANE)}")
        bad += 1
        continue
    if l1:
        nl = sum(1 for _ in open(full, encoding="utf-8"))
        hi = int(l2) if l2 else int(l1)
        if hi > nl:
            print(f"OUT-OF-RANGE {t}  ({full} has {nl} lines)")
            bad += 1
            continue
    if idx is not None:
        if not path.endswith(".json"):
            print(f"NOT-JSON-POINTER {t}")
            bad += 1
            continue
        try:
            d = json.load(open(full, encoding="utf-8"))
            i = int(idx)
            if not isinstance(d, list) or i >= len(d):
                print(f"POINTER-OUT-OF-RANGE {t} (len={len(d) if isinstance(d,list) else 'non-list'})")
                bad += 1
                continue
        except Exception as e:
            print(f"POINTER-ERR {t}: {e}")
            bad += 1
            continue
    print(f"OK       {t}")
print(f"--- citations checked={n} bad={bad}")
sys.exit(1 if bad else 0)
