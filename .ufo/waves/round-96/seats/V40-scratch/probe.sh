#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
W=.ufo/waves/round-96/seats/V40-scratch/probe
rm -rf "$W"; mkdir -p "$W"
echo "== pins =="
sha256sum corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json
git show dcb2d92:corpus/tools/map_obligations.py > "$W/baseline_tool.py"
sha256sum "$W/baseline_tool.py"

echo; echo "== C1a deletion class: baseline =="
cp -r corpus/fixtures/r95-crossing-aftermath "$W/del"
python3 - "$W/del" <<'PY'
import json,sys
p=sys.argv[1]+'/entities.json'
d=json.load(open(p)); del d[0]['claims']
open(p,'w').write(json.dumps(d,indent=2)+'\n')
PY
grep -v '| J06 |' "$W/del/claim-excerpt-map.md" > "$W/del/map.tmp" && mv "$W/del/map.tmp" "$W/del/claim-excerpt-map.md"
python3 "$W/baseline_tool.py" "$W/del"; echo "baseline_exit=$?"
echo "== C1a deletion class: delivered =="
python3 corpus/tools/map_obligations.py "$W/del"; echo "delivered_exit=$?"

echo; echo "== C1c dual_pointer: baseline =="
cp -r corpus/fixtures/r88-m3-maya-cluster "$W/dual"
python3 - "$W/dual/claim-excerpt-map.md" <<'PY'
import sys
p=sys.argv[1]; t=open(p).read()
old='| P1 | `entities[0].first_appearance` (Aru) |'
new='| P1 | `entities[0].first_appearance` (also `relations.json#/0`) (Aru) |'
assert old in t, 'P1 cell not found'
open(p,'w').write(t.replace(old,new,1))
PY
python3 "$W/baseline_tool.py" "$W/dual"; echo "baseline_exit=$?"
echo "== C1c dual_pointer: delivered =="
python3 corpus/tools/map_obligations.py "$W/dual"; echo "delivered_exit=$?"

echo; echo "== C1b self-test delivered =="
python3 corpus/tools/map_obligations.py --self-test | tail -4; echo "selftest_exit=${PIPESTATUS[0]}"

echo; echo "== battery: delivered clean fixtures =="
for d in r88-m3-maya-cluster r93-m2-kojiki-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response; do
  echo "-- $d"; python3 corpus/tools/map_obligations.py corpus/fixtures/$d; echo "exit=$?"
done
echo "-- r87 (expect 2)"; python3 corpus/tools/map_obligations.py corpus/fixtures/r87-myth-cluster; echo "exit=$?"
echo "-- r89 (expect 2)"; python3 corpus/tools/map_obligations.py corpus/fixtures/r89-inspiration-paraphrase; echo "exit=$?"
echo "-- frozen r93 (expect 0)"; python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93; echo "exit=$?"

echo; echo "== C3 chain 4/4 =="
for d in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response; do
  echo "-- $d"; python3 corpus/tools/dependency_freeze.py corpus/fixtures/$d; echo "exit=$?"
done
echo; echo "== C3 BR-01 reduction mutation =="
mkdir -p "$W/br01"; cp -r corpus/fixtures/r94-paired-crossing "$W/br01/r94-paired-crossing"
python3 - "$W/br01/r94-paired-crossing/timeline.json" <<'PY'
import json,sys
p=sys.argv[1]; d=json.load(open(p))
d[2]['depends_on']=[x for x in d[2]['depends_on'] if x!='evin-ninth-bell']
open(p,'w').write(json.dumps(d,indent=2)+'\n')
PY
python3 corpus/tools/dependency_freeze.py "$W/br01/r94-paired-crossing"; echo "exit=$?"
echo; echo "== C3 addition mutation =="
mkdir -p "$W/add"; cp -r corpus/fixtures/r96-crossing-response "$W/add/r96-crossing-response"
python3 - "$W/add/r96-crossing-response/timeline.json" <<'PY'
import json,sys
p=sys.argv[1]; d=json.load(open(p))
d[4]['depends_on']=sorted(d[4]['depends_on']+['aru-ninth-bell'])
open(p,'w').write(json.dumps(d,indent=2)+'\n')
PY
python3 corpus/tools/dependency_freeze.py "$W/add/r96-crossing-response"; echo "exit=$?"
echo; echo "== C3 self-test =="
python3 corpus/tools/dependency_freeze.py --self-test | tail -3; echo "selftest_exit=${PIPESTATUS[0]}"

echo; echo "== C2 =="
python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response; echo "exit=$?"
echo "census: $(ls -d corpus/fixtures/*/ | wc -l)"
echo; echo "== git status =="
git status --porcelain | head -20
