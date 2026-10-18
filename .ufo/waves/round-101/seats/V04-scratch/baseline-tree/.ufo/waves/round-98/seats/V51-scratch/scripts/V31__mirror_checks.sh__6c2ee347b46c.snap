#!/bin/bash
# V31 adjudicator mirror checks: C1(a) exit-2 self-test mismatch, C1(b) path-less
# legacy pin migration (delivered vs baseline), C2 V46 discharge (r97 tick-13 edge).
# Usage: mirror_checks.sh <label>   (label: pre|post — post requires S1 landed)
R=/home/vgpnk/Projects/shokunin/lore-shokunin
TOOL=$R/corpus/tools/dependency_freeze.py
CONTRACT=$R/corpus/tools/dependency-freeze-contract.json
BASE_TOOL=$R/.ufo/waves/round-98/scratch/V31/baseline_dependency_freeze.py
W=$R/.ufo/waves/round-98/scratch/V31/work
rm -rf "$W"; mkdir -p "$W"

# extract baseline tool + contract (9a3d648) once
[ -f "$BASE_TOOL" ] || git -C "$R" show 9a3d648:corpus/tools/dependency_freeze.py > "$BASE_TOOL"
BASE_CONTRACT=$R/.ufo/waves/round-98/scratch/V31/baseline_contract.json
[ -f "$BASE_CONTRACT" ] || git -C "$R" show 9a3d648:corpus/tools/dependency-freeze-contract.json > "$BASE_CONTRACT"

mk_mirror() { # $1=dir  $2=tool source  [$3=contract source]
  mkdir -p "$1/corpus/tools" "$1/corpus/fixtures"
  cp "$2" "$1/corpus/tools/dependency_freeze.py"
  cp "${3:-$CONTRACT}" "$1/corpus/tools/dependency-freeze-contract.json"
  mkdir -p "$1/corpus/fixtures/r95-crossing-aftermath"
  cp -r "$R/corpus/fixtures/r95-crossing-aftermath/." "$1/corpus/fixtures/r95-crossing-aftermath/"
}

echo "########## TEST A: SELF-TEST-MISMATCH exit contract (delivered tool) ##########"
A=$W/self_test_mismatch
mk_mirror "$A" "$TOOL"
python3 - "$A" <<'PY'
import json,sys
p=sys.argv[1]+"/corpus/tools/dependency-freeze-contract.json"
c=json.load(open(p))
c["self_test"]["expected"]["clean"]["exit"]=1   # deliberately wrong expectation
json.dump(c,open(p,"w"),indent=2,ensure_ascii=False)
PY
python3 "$A/corpus/tools/dependency_freeze.py" --self-test > "$A/out.txt" 2>&1
echo "delivered-tool rc=$? (want 2)"
grep -E "CASE clean|SELF-TEST|FINDING|RESULT" "$A/out.txt" | head -6
echo "--- baseline tool + baseline contract, same mutation ---"
A2=$W/self_test_mismatch_base
mk_mirror "$A2" "$BASE_TOOL" "$BASE_CONTRACT"
python3 - "$A2" <<'PY'
import json,sys
p=sys.argv[1]+"/corpus/tools/dependency-freeze-contract.json"
c=json.load(open(p))
c["self_test"]["expected"]["clean"]["exit"]=1
json.dump(c,open(p,"w"),indent=2,ensure_ascii=False)
PY
python3 "$A2/corpus/tools/dependency_freeze.py" --self-test > "$A2/out.txt" 2>&1
echo "baseline-tool rc=$? (was 1 pre-C1)"
grep -E "CASE clean|SELF-TEST|FINDING|RESULT" "$A2/out.txt" | head -6

echo "########## TEST B: path-less legacy pin migrated by --freeze ##########"
B=$W/legacy_pin
mk_mirror "$B" "$TOOL"
mkdir -p "$B/corpus/fixtures/r95-crossing-aftermath"
cp -r "$R/corpus/fixtures/r95-crossing-aftermath/." "$B/corpus/fixtures/r95-crossing-aftermath/"
python3 - "$B" <<'PY'
import json,sys
p=sys.argv[1]+"/corpus/tools/dependency-freeze-contract.json"
c=json.load(open(p))
del c["pins"]["r95-crossing-aftermath"]["fixture"]   # path-less legacy pin
json.dump(c,open(p,"w"),indent=2,ensure_ascii=False)
PY
python3 "$B/corpus/tools/dependency_freeze.py" --freeze "$B/corpus/fixtures/r95-crossing-aftermath" > "$B/out.txt" 2>&1
echo "delivered-tool rc=$?"
grep -E "FROZEN|FINDING|RESULT|DIGEST" "$B/out.txt" | head -5
echo "pin fixture field after: $(python3 -c "import json;print(json.load(open('$B/corpus/tools/dependency-freeze-contract.json'))['pins']['r95-crossing-aftermath'].get('fixture'))")"
echo "--- baseline tool same mutation ---"
B2=$W/legacy_pin_base
mk_mirror "$B2" "$BASE_TOOL"
cp "$B/corpus/tools/dependency-freeze-contract.json" "$B2/corpus/tools/dependency-freeze-contract.json"
python3 - "$B2" <<'PY'
import json,sys
p=sys.argv[1]+"/corpus/tools/dependency-freeze-contract.json"
c=json.load(open(p))
del c["pins"]["r95-crossing-aftermath"]["fixture"]
json.dump(c,open(p,"w"),indent=2,ensure_ascii=False)
PY
mkdir -p "$B2/corpus/fixtures/r95-crossing-aftermath"
cp -r "$R/corpus/fixtures/r95-crossing-aftermath/." "$B2/corpus/fixtures/r95-crossing-aftermath/"
python3 "$B2/corpus/tools/dependency_freeze.py" --freeze "$B2/corpus/fixtures/r95-crossing-aftermath" > "$B2/out.txt" 2>&1
echo "baseline-tool rc=$? (expect 2 SCOPE-REFUSED)"
grep -E "FINDING|RESULT" "$B2/out.txt" | head -3

echo "########## TEST C: V46 discharge — r97 tick-13 edge drop (delivered) ##########"
C=$W/v46
mk_mirror "$C" "$TOOL"
mkdir -p "$C/corpus/fixtures/r97-crossing-acknowledgment"
cp -r "$R/corpus/fixtures/r97-crossing-acknowledgment/." "$C/corpus/fixtures/r97-crossing-acknowledgment/"
python3 "$C/corpus/tools/dependency_freeze.py" "$C/corpus/fixtures/r97-crossing-acknowledgment" > "$C/out_control.txt" 2>&1
echo "control (no mutation) rc=$? (want 0)"
tail -2 "$C/out_control.txt"
python3 - "$C" <<'PY'
import json,sys
p=sys.argv[1]+"/corpus/fixtures/r97-crossing-acknowledgment/timeline.json"
t=json.load(open(p))
for rec in t:
    if rec["id"]=="acknowledgment-aru-records":
        rec["depends_on"]=[d for d in rec["depends_on"] if d!="response-evin-salt-court"]
json.dump(t,open(p,"w"),indent=2)
PY
python3 "$C/corpus/tools/dependency_freeze.py" "$C/corpus/fixtures/r97-crossing-acknowledgment" > "$C/out_mutated.txt" 2>&1
echo "mutated (edge dropped) rc=$? (want 1)"
grep -E "FINDING|RESULT|FREEZE" "$C/out_mutated.txt" | head -4
echo "=== DONE ==="
