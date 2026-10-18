#!/bin/bash
# V59 failsafe spot-check harness — runs only what is present; never fabricates.
R=/home/vgpnk/Projects/shokunin/lore-shokunin
cd "$R" || exit 9
echo "== git status =="; git status --porcelain | head -20
echo "== C1a: self-test exit + case count =="
python3 corpus/tools/dependency_freeze.py --self-test; echo "EXIT=$?"
echo "-- FROZEN_CASES count:"; grep -c '^    "' corpus/tools/dependency_freeze.py >/dev/null; python3 - <<'PY'
import re,pathlib
src=pathlib.Path('corpus/tools/dependency_freeze.py').read_text()
m=re.search(r'FROZEN_CASES = \((.*?)\n\)', src, re.S)
if m: print('FROZEN_CASES n=', len(re.findall(r'"([a-z_]+)"', m.group(1))))
PY
echo "== C1c: precedence text =="; python3 -c "import json;print(json.load(open('corpus/tools/dependency-freeze-contract.json'))['precedence'])"
echo "== C2: pins =="; python3 -c "import json;c=json.load(open('corpus/tools/dependency-freeze-contract.json'));print(len(c['pins']), list(c['pins'].keys()))"
for f in corpus/fixtures/r88-m3-maya-cluster corpus/fixtures/r94-paired-crossing corpus/fixtures/r95-crossing-aftermath corpus/fixtures/r96-crossing-response corpus/fixtures/r97-crossing-acknowledgment corpus/fixtures/r98-clerk-filing; do
  [ -d "$f" ] && { echo "-- verify $f"; python3 corpus/tools/dependency_freeze.py "$f" 2>&1 | tail -2; echo "EXIT=$?"; }
done
echo "== C3: fixture counts =="
python3 - <<'PY'
import json,pathlib
d=pathlib.Path('corpus/fixtures/r98-clerk-filing')
if not d.is_dir(): print('ABSENT'); raise SystemExit
for f in ('entities.json','relations.json','timeline.json','sources.json'):
    p=d/f
    if p.exists():
        v=json.loads(p.read_text())
        print(f, len(v))
print('files:', sorted(x.name for x in d.iterdir()))
PY
echo "== C3: check_bible =="; [ -d corpus/fixtures/r98-clerk-filing ] && python3 corpus/fixtures/check_bible.py corpus/fixtures/r98-clerk-filing; echo "EXIT=$?"
echo "== C3: map obligations =="; [ -f corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md ] && grep -c '^|' corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md
