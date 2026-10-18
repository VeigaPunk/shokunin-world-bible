#!/bin/bash
R=/home/vgpnk/Projects/shokunin/lore-shokunin
S=$R/.ufo/waves/round-96/seats/V34-scratch
cd $R
echo "########## DELIVERED HASHES ##########"
sha256sum corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json corpus/tools/README.md
echo "########## SELF-TEST ##########"
out=$(python3 corpus/tools/map_obligations.py --self-test 2>&1); code=$?
echo "$out" | grep -c "^SELF-TEST"
echo "$out" | grep -E "SELF-TEST (FAIL|PASS) (schema_drift|inventory_mismatch|dual_pointer)"
echo "$out" | tail -3
echo "SELF-TEST EXIT=$code"
echo "########## CONTRACT CASES ##########"
python3 -c "import json;c=json.load(open('corpus/tools/map-obligations-contract.json'));print('cases=',len(c['self_test']['cases']));print([x for x in c['self_test']['cases'] if x['id'] in ('schema_drift','inventory_mismatch','dual_pointer')])"
echo "########## C1a DEMOS ##########"
for c in del-demo/cluster control/cluster; do echo "--- $c ---"; python3 corpus/tools/map_obligations.py $S/$c; echo "EXIT=$?"; done
echo "########## C1c D1 DEMO ##########"
python3 corpus/tools/map_obligations.py $S/d1-demo/cluster; echo "EXIT=$?"
echo "########## DRIFT SCOPE ##########"
for c in entities_unexpected relations_unexpected entities_nonshaped; do echo "--- $c ---"; python3 corpus/tools/map_obligations.py $S/drift-demo/$c; echo "EXIT=$?"; done
echo "########## EXTRA CASES ##########"
for c in no_declared editorial_only event_delete; do echo "--- $c ---"; python3 corpus/tools/map_obligations.py $S/extra/$c; echo "EXIT=$?"; done
echo "########## FIXTURE BATTERY ##########"
for d in r87-myth-cluster r88-m3-maya-cluster r89-inspiration-paraphrase r93-m2-kojiki-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response; do echo "--- $d ---"; python3 corpus/tools/map_obligations.py corpus/fixtures/$d; echo "EXIT=$?"; done
echo "########## FROZEN r93 ##########"
python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93; echo "EXIT=$?"
echo "########## DRIFT REGION DIFF vs baseline ##########"
python3 - <<'PY'
import pathlib
src = pathlib.Path("corpus/tools/map_obligations.py").read_text()
def region(text, start, end):
    i = text.index(start); j = text.index(end, i); return text[i:j]
new = region(src, "def claim_shaped", "def raw_obligations(cluster)")
old = pathlib.Path("/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-96/seats/V34-scratch/baseline_drift_region.txt").read_text()
print("IDENTICAL" if new == old else "CHANGED")
if new != old:
    import difflib
    print("".join(difflib.unified_diff(old.splitlines(True), new.splitlines(True), "baseline", "delivered")))
PY
echo "########## NEW PIN TAMPER SENSITIVITY ##########"
rm -rf $S/tamper2 && mkdir -p $S/tamper2/corpus/tools
cp corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json $S/tamper2/corpus/tools/
python3 - <<'PY'
import json, pathlib
p = pathlib.Path("/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-96/seats/V34-scratch/tamper2/corpus/tools/map-obligations-contract.json")
c = json.loads(p.read_text())
for case in c["self_test"]["cases"]:
    if case["id"] in ("schema_drift", "inventory_mismatch"):
        case["exit"] = 0; case["finding_ids"] = []
p.write_text(json.dumps(c, indent=2) + "\n")
PY
python3 $S/tamper2/corpus/tools/map_obligations.py --self-test 2>&1 | grep -E "SELF-TEST (FAIL|PASS) (schema_drift|inventory_mismatch)|RESULT|FINDING"; echo "TAMPER2 EXIT=${PIPESTATUS[0]}"
echo "########## README DOC CONSISTENCY ##########"
grep -n "not a gate\|does not by itself change the exit code" corpus/tools/README.md || echo "stale non-gating sentence GONE"
grep -n "inventory_mismatch\|dual_pointer" corpus/tools/README.md | head -8 || echo "new IDs absent from README"
echo "########## END ##########"
