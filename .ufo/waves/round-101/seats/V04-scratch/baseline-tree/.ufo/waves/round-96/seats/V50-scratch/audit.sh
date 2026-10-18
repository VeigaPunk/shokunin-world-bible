#!/bin/bash
# V50 receipt-wording audit harness — run from lane repo root
cd /home/vgpnk/Projects/shokunin/lore-shokunin
S=.ufo/waves/round-96/seats/V50-scratch
echo "=== T0 digests of delivered r96 artifacts ==="
sha256sum corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json \
  corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json 2>&1
echo "=== M1 map_obligations on r96-crossing-response ==="
python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response; echo "EXIT=$?"
echo "=== M2 self-test ==="
python3 corpus/tools/map_obligations.py --self-test > $S/selftest.out 2>&1; echo "EXIT=$?"
grep -c "SELF-TEST PASS" $S/selftest.out; tail -1 $S/selftest.out
echo "=== M3 contract case count ==="
python3 - <<'PY'
import json
c=json.load(open('corpus/tools/map-obligations-contract.json'))
print('cases:', len(c['self_test']['cases']))
print('ids:', [x['id'] for x in c['self_test']['cases']])
PY
echo "=== M4 dependency_freeze chain ==="
for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response; do
  python3 corpus/tools/dependency_freeze.py corpus/fixtures/$f > $S/freeze-$f.out 2>&1; echo "$f EXIT=$? :: $(tail -1 $S/freeze-$f.out)"
done
echo "=== M5 dependency_freeze self-test ==="
python3 corpus/tools/dependency_freeze.py --self-test > $S/freeze-selftest.out 2>&1; echo "EXIT=$?"; tail -2 $S/freeze-selftest.out
echo "=== M6 r96 map rows vs r95 (parsed-value) ==="
python3 $S/compare_maps.py
