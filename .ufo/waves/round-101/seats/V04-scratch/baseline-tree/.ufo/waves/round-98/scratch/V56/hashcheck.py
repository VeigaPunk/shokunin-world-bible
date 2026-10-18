#!/usr/bin/env python3
"""Extract `sha256 \`xxxxxxxx…\`` hash pins from a file and compare the 8-hex prefix
against the actual sha256 of the named tool file (nearest preceding path mention)."""
import re, sys, os, hashlib
LANE = "/home/vgpnk/Projects/shokunin/lore-shokunin"
path = sys.argv[1]
text = open(path, encoding="utf-8").read()
# pairs of (toolfile mention, hash) within the same sentence/line
for line in text.splitlines():
    hashes = re.findall(r"`([0-9a-f]{8})…`", line)
    if not hashes:
        continue
    files = re.findall(r"`([A-Za-z0-9_.-]+\.(?:py|json))`", line)
    for h in hashes:
        # find the file whose name appears closest before this hash
        pos = line.index(h)
        best, bestpos = None, -1
        for f in files:
            fp = line.rfind(f, 0, pos)
            if fp > bestpos:
                best, bestpos = f, fp
        if best is None:
            print(f"UNBOUND hash {h} in: {line.strip()[:120]}")
            continue
        full = None
        for cand in ["corpus/tools/"+best, "corpus/fixtures/"+best, "corpus/"+best]:
            if os.path.exists(os.path.join(LANE, cand)):
                full = os.path.join(LANE, cand); break
        if full is None:
            print(f"NOFILE hash {h} bound to {best}")
            continue
        actual = hashlib.sha256(open(full,'rb').read()).hexdigest()
        verdict = "MATCH" if actual.startswith(h) else "STALE"
        print(f"{verdict} {best} cited={h} actual={actual[:8]}  <- {line.strip()[:100]}")
