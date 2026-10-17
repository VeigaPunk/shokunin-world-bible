#!/usr/bin/env python3
"""Build identical BR-02 mutation copies of the r94 fixture + map.

BR-02 mutation: in entities.json, entity index 4 (chalk-stair) has its
`claims` key renamed to `assertions` (content preserved byte-for-byte),
and that claim's map row (`entities.json#/4/claims/0`) is removed.
"""

import hashlib
import json
import shutil
import sys
from pathlib import Path

REPO = Path("/home/vgpnk/Projects/shokunin/lore-shokunin")
SRC = REPO / "corpus/fixtures/r94-paired-crossing"
SCRATCH = REPO / ".ufo/waves/round-95/seats/V01-scratch"
TARGETS = ("br02-old", "br02-new", "br02-new-2")
CLAIM_ROW = "entities.json#/4/claims/0"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build(dest):
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    for name in ("entities.json", "relations.json", "timeline.json", "claim-excerpt-map.md"):
        shutil.copy2(SRC / name, dest / name)

    # 1. rename the claims key on entity index 4, preserving its value
    entities_path = dest / "entities.json"
    entities = json.loads(entities_path.read_text(encoding="utf-8"))
    assert "claims" in entities[4], "expected entity[4] to have a claims key"
    entities[4]["assertions"] = entities[4].pop("claims")
    entities_path.write_text(json.dumps(entities, indent=2) + "\n", encoding="utf-8")

    # 2. remove the map row for that claim
    map_path = dest / "claim-excerpt-map.md"
    lines = map_path.read_text(encoding="utf-8").splitlines(keepends=True)
    kept = [line for line in lines if CLAIM_ROW not in line]
    assert len(lines) - len(kept) == 1, f"expected to remove exactly one map row, removed {len(lines) - len(kept)}"
    map_path.write_text("".join(kept), encoding="utf-8")

    print(f"built {dest.name}:")
    for name in ("entities.json", "relations.json", "timeline.json", "claim-excerpt-map.md"):
        print(f"  {name} sha256={sha(dest / name)}")


def main():
    for name in TARGETS:
        build(SCRATCH / name)
    # byte-identity check across the three copies
    digests = {}
    for name in TARGETS:
        digests[name] = tuple(sha(SCRATCH / name / f) for f in
                              ("entities.json", "relations.json", "timeline.json", "claim-excerpt-map.md"))
    unique = set(digests.values())
    print(f"IDENTICAL={len(unique) == 1} ({len(unique)} distinct digest sets across {len(TARGETS)} copies)")
    return 0 if len(unique) == 1 else 1


if __name__ == "__main__":
    sys.exit(main())
