#!/bin/bash
# V59 independent C2 discharge demo: drop the r97 tick-13 edge in a mirror root.
set -u
R=/home/vgpnk/Projects/shokunin/lore-shokunin
W=$(mktemp -d /tmp/v59-mirror-XXXX)
mkdir -p "$W/corpus/tools" "$W/corpus/fixtures"
cp "$R/corpus/tools/dependency_freeze.py" "$R/corpus/tools/dependency-freeze-contract.json" "$W/corpus/tools/"
for fx in r97-crossing-acknowledgment r98-clerk-filing; do cp -r "$R/corpus/fixtures/$fx" "$W/corpus/fixtures/"; done
echo "== clean control =="
python3 "$W/corpus/tools/dependency_freeze.py" "$W/corpus/fixtures/r97-crossing-acknowledgment" | tail -2; echo "EXIT=${PIPESTATUS[0]}"
echo "== drop tick-13 edge (r97) =="
python3 - "$W" <<'PY'
import json,sys
p=sys.argv[1]+"/corpus/fixtures/r97-crossing-acknowledgment/timeline.json"
tl=json.load(open(p))
for e in tl:
    if e["id"]=="acknowledgment-aru-records": e["depends_on"]=[]
json.dump(tl,open(p,"w"),indent=2); open(p,"a").write("\n")
print("patched", p)
PY
python3 "$W/corpus/tools/dependency_freeze.py" "$W/corpus/fixtures/r97-crossing-acknowledgment" | tail -3; echo "EXIT=${PIPESTATUS[0]}"
echo "MIRROR=$W"
