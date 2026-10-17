#!/bin/bash
set -u
REPO=/home/vgpnk/Projects/shokunin/lore-shokunin
SC=$REPO/.ufo/waves/round-97/seats/V01-scratch
rm -rf "$SC/pertA" "$SC/pertA0" "$SC/pertB" "$SC/pertC" "$SC/cluster" "$SC/r96"
echo "=== delivered digests (re-check) ==="
sha256sum "$REPO/corpus/tools/map_obligations.py" "$REPO/corpus/tools/map-obligations-contract.json"
echo
echo "=== cluster: hand-built legacy dual-pointer cluster (same shape as prepare_test_case) ==="
python3 - "$SC/cluster" <<'PY'
import json,sys,pathlib
c=pathlib.Path(sys.argv[1]); c.mkdir(parents=True,exist_ok=True)
files={"entities.json":[{"id":"test-entity","first_appearance":"fixture-source","claims":[{"statement":"test claim","source_id":"fixture-source"}]}],
"relations.json":[{"from":"test-entity","to":"other","type":"linked","source_id":"fixture-source"}],
"timeline.json":[{"id":"test-event","source_id":"fixture-source"}]}
for n,v in files.items(): (c/n).write_text(json.dumps(v,indent=2)+"\n")
lines=["# Isolated mapping fixture","","## JSON facts","",
"| ID | JSON fact and fields | In-world source ID |","|---|---|---|",
"| E1 | `entities[0].first_appearance` (also named `entities[1].first_appearance`) | `fixture-source` |",
"| E2 | `entities[0].claims[0]` | `fixture-source` |",
"| R1 | `relations[0]` | `fixture-source` |",
"| T1 | `timeline[0]` | `fixture-source` |"]
(c/"claim-excerpt-map.md").write_text("\n".join(lines)+"\n")
print("built",c)
PY
echo "--- delivered tool on the dual-pointer cluster (expect exit 1, dual_pointer) ---"
cd "$REPO" && python3 corpus/tools/map_obligations.py "$SC/cluster"; echo "exit=$?"
echo
echo "=== CONTROL A0: scratch copy UNPERTURBED -> self-test ==="
A0=$SC/pertA0/corpus/tools; mkdir -p "$A0"
cp "$REPO/corpus/tools/map_obligations.py" "$A0/"; cp "$REPO/corpus/tools/map-obligations-contract.json" "$A0/"
cd "$SC/pertA0" && python3 corpus/tools/map_obligations.py --self-test | tail -4; echo "exit=${PIPESTATUS[0]}"
cd "$SC/pertA0" && python3 corpus/tools/map_obligations.py --self-test >"$SC/A0.out" 2>&1; echo "A0 raw exit=$?"
echo
echo "=== PERTURBATION A: neutralize dual_pointer emission ==="
A=$SC/pertA/corpus/tools; mkdir -p "$A"
cp "$REPO/corpus/tools/map_obligations.py" "$A/"; cp "$REPO/corpus/tools/map-obligations-contract.json" "$A/"
python3 - "$A/map_obligations.py" <<'PY'
import sys
p=sys.argv[1]; s=open(p).read()
old="            if mention is not None:"
assert s.count(old)==1,("anchor count",s.count(old))
open(p,"w").write(s.replace(old,"            if False:  # V01 perturbation: neutralize dual_pointer emission"))
print("perturbation applied to",p)
PY
echo "--- perturbed tool on the SAME cluster (expect exit 0, no findings) ---"
cd "$SC/pertA" && python3 corpus/tools/map_obligations.py "$SC/cluster"; echo "exit=$?"
echo "--- perturbed tool --self-test (expect dual_pointer case FAIL, RESULT ERROR, exit 2) ---"
cd "$SC/pertA" && python3 corpus/tools/map_obligations.py --self-test >"$SC/A.out" 2>&1; echo "A raw exit=$?"
grep -E "SELF-TEST CASES|dual_pointer|RESULT|FINDING" "$SC/A.out"
echo
echo "=== PERTURBATION B: scratch contract drops the dual_pointer case ==="
B=$SC/pertB/corpus/tools; mkdir -p "$B"
cp "$REPO/corpus/tools/map_obligations.py" "$B/"; cp "$REPO/corpus/tools/map-obligations-contract.json" "$B/"
python3 - "$B/map-obligations-contract.json" <<'PY'
import json,sys
p=sys.argv[1]; d=json.load(open(p))
before=len(d['self_test']['cases'])
d['self_test']['cases']=[c for c in d['self_test']['cases'] if c['id']!='dual_pointer']
json.dump(d,open(p,'w'),indent=2); open(p,'a').write("\n")
print(f"cases {before} -> {len(d['self_test']['cases'])} (dropped dual_pointer)")
PY
cd "$SC/pertB" && python3 corpus/tools/map_obligations.py --self-test >"$SC/B.out" 2>&1; echo "B raw exit=$?"
cat "$SC/B.out"
echo
echo "=== PERTURBATION C: scratch contract flips dual_pointer expected exit 1->0 ==="
C=$SC/pertC/corpus/tools; mkdir -p "$C"
cp "$REPO/corpus/tools/map_obligations.py" "$C/"; cp "$REPO/corpus/tools/map-obligations-contract.json" "$C/"
python3 - "$C/map-obligations-contract.json" <<'PY'
import json,sys
p=sys.argv[1]; d=json.load(open(p))
for c in d['self_test']['cases']:
    if c['id']=='dual_pointer':
        c['exit']=0; c['finding_ids']=[]
json.dump(d,open(p,'w'),indent=2); open(p,'a').write("\n")
print("dual_pointer expectation flipped to exit 0 / no findings")
PY
cd "$SC/pertC" && python3 corpus/tools/map_obligations.py --self-test >"$SC/C.out" 2>&1; echo "C raw exit=$?"
grep -E "dual_pointer|RESULT|FINDING" "$SC/C.out"
