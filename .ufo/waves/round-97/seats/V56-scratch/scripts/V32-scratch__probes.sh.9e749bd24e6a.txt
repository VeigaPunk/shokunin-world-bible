#!/bin/bash
# V32 r97 probe battery: copied-tree probes for C1 drop protection / pin load-bearing,
# C2 scope guard / path binding / digest naming. Never mutates live artifacts.
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 9
S=$PWD/.ufo/waves/round-97/seats/V32-scratch/after
P=$S/probes
rm -rf "$P"; mkdir -p "$P"

echo "### C1: copied map tree (tool+contract copies, ROOT=copy root)"
MT=$P/map-tree
mkdir -p $MT/corpus/tools
cp corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json $MT/corpus/tools/
python3 - "$MT" <<'EOF'
import json, subprocess, sys
MT = sys.argv[1]
cp = MT + '/corpus/tools/map-obligations-contract.json'
tool = MT + '/corpus/tools/map_obligations.py'
def run(label):
    r = subprocess.run([sys.executable, tool, '--self-test'], capture_output=True, text=True, cwd=MT)
    head = [l for l in r.stdout.splitlines() if l.startswith('SELF-TEST CASES')]
    tail = [l for l in r.stdout.splitlines() if l.startswith('RESULT') or l.startswith('FINDING')]
    print(f'{label}: exit={r.returncode} {head} {tail}')
c = json.load(open(cp))
print('contract cases:', len(c['self_test']['cases']))
for drop in [x['id'] for x in c['self_test']['cases']]:
    cc = json.loads(json.dumps(c))
    cc['self_test']['cases'] = [x for x in cc['self_test']['cases'] if x['id'] != drop]
    json.dump(cc, open(cp, 'w'), indent=2)
    r = subprocess.run([sys.executable, tool, '--self-test'], capture_output=True, text=True, cwd=MT)
    head = [l for l in r.stdout.splitlines() if l.startswith('SELF-TEST CASES')]
    tail = [l for l in r.stdout.splitlines() if l.startswith('RESULT') or l.startswith('FINDING')]
    print(f'drop {drop}: exit={r.returncode} {head} {tail}')
json.dump(c, open(cp, 'w'), indent=2)
EOF

echo; echo "### C1: pin load-bearing (neutralize dual_pointer emission in a copy)"
NT=$P/neutralize
mkdir -p $NT/corpus/tools
cp corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json $NT/corpus/tools/
python3 - "$NT" <<'EOF'
import re, subprocess, sys
NT = sys.argv[1]
tool = NT + '/corpus/tools/map_obligations.py'
src = open(tool).read()
# neutralize: make the dual_pointer finding a no-op by replacing the finding id string in the emission
print('occurrences of dual_pointer in tool source:', src.count('dual_pointer'))
open(tool, 'w').write(src.replace('"dual_pointer"', '"dual_pointer_disabled"'))
r = subprocess.run([sys.executable, tool, '--self-test'], capture_output=True, text=True, cwd=NT)
head = [l for l in r.stdout.splitlines() if l.startswith('SELF-TEST CASES')]
tail = [l for l in r.stdout.splitlines() if l.startswith('RESULT') or l.startswith('FINDING') or 'dual' in l.lower()]
print('neutralized run:', r.returncode, head, tail[:6])
EOF

echo; echo "### C2: copied dep tree (tool+contract copies, ROOT=copy root)"
DT=$P/dep-tree
mkdir -p $DT/corpus/tools $DT/corpus/fixtures $DT/outside
cp corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json $DT/corpus/tools/
cp -r corpus/fixtures/r95-crossing-aftermath $DT/corpus/fixtures/
cp -r corpus/fixtures/r95-crossing-aftermath $DT/outside/probe-fixture
echo "-- --freeze on an out-of-scope target (copy tree)"
python3 $DT/corpus/tools/dependency_freeze.py --freeze $DT/outside/probe-fixture; echo "exit=$?"
echo "-- copy contract pins after out-of-scope attempt:"
python3 -c "import json;print(list(json.load(open('$DT/corpus/tools/dependency-freeze-contract.json'))['pins']))"
echo "-- --freeze on an in-scope target (copy tree, corpus/fixtures/...)"
cp -r corpus/fixtures/r95-crossing-aftermath $DT/corpus/fixtures/v32-in-scope
python3 $DT/corpus/tools/dependency_freeze.py --freeze $DT/corpus/fixtures/v32-in-scope; echo "exit=$?"
echo "-- copy contract pins after in-scope freeze:"
python3 -c "import json;print(list(json.load(open('$DT/corpus/tools/dependency-freeze-contract.json'))['pins']))"
echo "-- digest naming: mutate a pinned copy inside the copy tree"
python3 - <<'EOF'
import pathlib
p = pathlib.Path('.ufo/waves/round-97/seats/V32-scratch/after/probes/dep-tree/corpus/fixtures/r95-crossing-aftermath/timeline.json')
p.write_text(p.read_text() + '\n')
EOF
python3 $DT/corpus/tools/dependency_freeze.py $DT/corpus/fixtures/r95-crossing-aftermath; echo "exit=$?"

echo; echo "### C2 LIVE: path binding (same-named copy at a foreign path, live tool, read-only)"
python3 corpus/tools/dependency_freeze.py .ufo/waves/round-97/seats/V32-scratch/foreign/r94-paired-crossing; echo "exit=$?"

echo; echo "### C2 LIVE: --freeze scope guard on an out-of-scope existing fixture (safe if the guard fires before any write)"
BEFORE=$(sha256sum corpus/tools/dependency-freeze-contract.json | awk '{print $1}')
python3 corpus/tools/dependency_freeze.py --freeze .ufo/waves/round-97/seats/V32-scratch/foreign/r95-crossing-aftermath; echo "exit=$?"
AFTER=$(sha256sum corpus/tools/dependency-freeze-contract.json | awk '{print $1}')
echo "live contract sha before=$BEFORE after=$AFTER same=$([ "$BEFORE" = "$AFTER" ] && echo YES || echo NO)"
