#!/bin/bash
# V01 harness: snapshot delivered bytes, run self-test, perturb in scratch
set -u
REPO=/home/vgpnk/Projects/shokunin/lore-shokunin
SC=$REPO/.ufo/waves/round-97/seats/V01-scratch
echo "=== 0. delivered byte digests ==="
sha256sum "$REPO/corpus/tools/map_obligations.py" "$REPO/corpus/tools/map-obligations-contract.json"
echo
echo "=== 1. contract case count + dual_pointer entry ==="
python3 - <<'PY'
import json
d=json.load(open('/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/map-obligations-contract.json'))
c=d['self_test']['cases']
print("cases:",len(c))
print("ids:",",".join(x['id'] for x in c))
print("dual_pointer entry:",json.dumps([x for x in c if x['id']=='dual_pointer']))
PY
echo
echo "=== 2. delivered --self-test ==="
cd "$REPO" && python3 corpus/tools/map_obligations.py --self-test; echo "exit=$?"
echo
echo "=== 3. PERTURBATION A: neutralize dual_pointer emission (scratch tool copy) ==="
A=$SC/pertA/corpus/tools; mkdir -p "$A"
cp "$REPO/corpus/tools/map_obligations.py" "$A/"; cp "$REPO/corpus/tools/map-obligations-contract.json" "$A/"
python3 - "$A/map_obligations.py" <<'PY'
import sys,re
p=sys.argv[1]; s=open(p).read()
old="            if mention is not None:"
assert s.count(old)==1, ("anchor count",s.count(old))
s=s.replace(old,"            if False:  # V01 perturbation: neutralize dual_pointer emission")
open(p,"w").write(s)
print("perturbed:",p)
PY
cd "$SC/pertA" && python3 corpus/tools/map_obligations.py --self-test; echo "exit=$?"
