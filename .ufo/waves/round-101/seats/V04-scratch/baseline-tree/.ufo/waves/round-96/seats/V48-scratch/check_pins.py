#!/usr/bin/env python3
"""V48 independent pin cross-check: recompute sha256 of the actual fixture
bytes and compare against dependency-freeze-contract.json pins."""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
contract = json.loads((ROOT / "corpus/tools/dependency-freeze-contract.json").read_text())


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


bad = 0
for name, pin in sorted(contract["pins"].items()):
    fx = ROOT / pin["fixture"]
    print(f"== {name} ==")
    files = {}
    for fname, pinned in sorted(pin["files"].items()):
        actual = sha(fx / fname)
        status = "OK" if actual == pinned else "MISMATCH"
        if actual != pinned:
            bad += 1
        print(f"  {fname}: pinned={pinned[:16]}… actual={actual[:16]}… {status}")
        files[fname] = actual
    payload = json.dumps({n: files[n] for n in sorted(files)}, sort_keys=True, separators=(",", ":"))
    content = hashlib.sha256(payload.encode()).hexdigest()
    cstatus = "OK" if content == pin["content_sha256"] else "MISMATCH"
    if content != pin["content_sha256"]:
        bad += 1
    print(f"  content_sha256: pinned={pin['content_sha256'][:16]}… recomputed={content[:16]}… {cstatus}")
    tl = json.loads((fx / "timeline.json").read_text())
    rel = json.loads((fx / "relations.json").read_text())
    ent = json.loads((fx / "entities.json").read_text()) if (fx / "entities.json").is_file() else None
    src = json.loads((fx / "sources.json").read_text()) if (fx / "sources.json").is_file() else None
    edges = sum(len(e.get("depends_on", [])) for e in tl)
    obs = {"events": len(tl), "dependency_edges": edges, "relations": len(rel),
           "entities": len(ent) if ent is not None else None,
           "sources": len(src) if src is not None else None}
    pin_counts = pin["counts"]
    for k, v in obs.items():
        if k in pin_counts and pin_counts[k] != v:
            bad += 1
            print(f"  counts.{k}: pinned={pin_counts[k]} observed={v} MISMATCH")
    print(f"  counts observed: {obs}")

print(f"\nTOTAL mismatches: {bad}")
sys.exit(1 if bad else 0)
