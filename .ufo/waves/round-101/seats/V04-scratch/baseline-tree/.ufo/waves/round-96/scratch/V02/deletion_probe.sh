#!/bin/bash
# Supplementary C1(a) probe: deletion class on a SCRATCH copy of r95-crossing-aftermath.
set -u
REPO=/home/vgpnk/Projects/shokunin/lore-shokunin
S=$REPO/.ufo/waves/round-96/scratch/V02/deletion
rm -rf "$S"; mkdir -p "$S"
cp -r "$REPO/corpus/fixtures/r95-crossing-aftermath" "$S/control"
cp -r "$REPO/corpus/fixtures/r95-crossing-aftermath" "$S/mutated"
python3 - "$S/mutated" <<'PY'
import json, sys, pathlib
d = pathlib.Path(sys.argv[1])
ent = json.loads((d/"entities.json").read_text())
del ent[1]["claims"][0]          # drop Evin's claims key  -> entities.json#/1/claims/0 disappears
(d/"entities.json").write_text(json.dumps(ent, indent=2) + "\n")
m = (d/"claim-excerpt-map.md").read_text().splitlines(keepends=True)
out = [l for l in m if not l.startswith("| J07 |")]   # drop its map row
(d/"claim-excerpt-map.md").write_text("".join(out))
print("mutated: claims entries now", sum(len(e.get("claims",[])) for e in ent), "| J07 row present:", any(l.startswith("| J07 |") for l in out))
PY
echo "=== control (unmutated copy) ==="
python3 "$REPO/corpus/tools/map_obligations.py" "$S/control"; echo "EXIT=$?"
echo "=== deletion-class mutation (claims key + J07 row removed) ==="
python3 "$REPO/corpus/tools/map_obligations.py" "$S/mutated"; echo "EXIT=$?"
