#!/bin/bash
# V59 independent C1b demo: path-less legacy pin migrated by --freeze (not SCOPE-REFUSED).
set -u
R=/home/vgpnk/Projects/shokunin/lore-shokunin
W=$(mktemp -d /tmp/v59-legacy-XXXX)
mkdir -p "$W/corpus/tools" "$W/corpus/fixtures"
cp "$R/corpus/tools/dependency_freeze.py" "$R/corpus/tools/dependency-freeze-contract.json" "$W/corpus/tools/"
cp -r "$R/corpus/fixtures/r95-crossing-aftermath" "$W/corpus/fixtures/"
python3 - "$W" <<'PY'
import json,sys
p=sys.argv[1]+"/corpus/tools/dependency-freeze-contract.json"
c=json.load(open(p))
pin=c["pins"]["r95-crossing-aftermath"]
pin.pop("fixture",None)          # legacy: path-less pin
c["pins"]["r95-crossing-aftermath"]=pin
json.dump(c,open(p,"w"),indent=2); open(p,"a").write("\n")
print("legacy pin now has keys:", list(pin.keys())[:3])
PY
echo "== verify with legacy pin (expect PATH-MISMATCH or migration?) =="
python3 "$W/corpus/tools/dependency_freeze.py" "$W/corpus/fixtures/r95-crossing-aftermath" | tail -2; echo "EXIT=${PIPESTATUS[0]}"
echo "== --freeze with legacy pin (expect FROZEN, exit 0; was SCOPE-REFUSED before C1b) =="
python3 "$W/corpus/tools/dependency_freeze.py" --freeze "$W/corpus/fixtures/r95-crossing-aftermath" | tail -3; echo "EXIT=${PIPESTATUS[0]}"
python3 - "$W" <<'PY'
import json,sys
c=json.load(open(sys.argv[1]+"/corpus/tools/dependency-freeze-contract.json"))
print("after freeze, pin.fixture =", c["pins"]["r95-crossing-aftermath"].get("fixture"))
PY
echo "== baseline control: same mutation against 9a3d648 tool =="
mkdir -p "$W/base/corpus/tools" "$W/base/corpus/fixtures"
git -C "$R" show 9a3d648:corpus/tools/dependency_freeze.py > "$W/base/corpus/tools/dependency_freeze.py"
git -C "$R" show 9a3d648:corpus/tools/dependency-freeze-contract.json > "$W/base/corpus/tools/dependency-freeze-contract.json"
cp -r "$R/corpus/fixtures/r95-crossing-aftermath" "$W/base/corpus/fixtures/"
python3 - "$W" <<'PY'
import json,sys
p=sys.argv[1]+"/base/corpus/tools/dependency-freeze-contract.json"
c=json.load(open(p)); c["pins"]["r95-crossing-aftermath"].pop("fixture",None)
json.dump(c,open(p,"w"),indent=2); open(p,"a").write("\n")
PY
python3 "$W/base/corpus/tools/dependency_freeze.py" --freeze "$W/base/corpus/fixtures/r95-crossing-aftermath" | tail -2; echo "EXIT=${PIPESTATUS[0]}"
echo "MIRROR=$W"
