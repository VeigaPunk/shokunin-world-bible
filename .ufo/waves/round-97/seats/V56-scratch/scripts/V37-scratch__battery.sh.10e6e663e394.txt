#!/bin/bash
# V37 grounding battery for round 97. Writes ONLY under V37-scratch.
# Run from lane root: bash .ufo/waves/round-97/seats/V37-scratch/battery.sh
set -u
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 9
S=.ufo/waves/round-97/seats/V37-scratch
T=$S/battery.txt
: > "$T"
run() { echo "\$ $*" >> "$T"; "$@" >> "$T" 2>&1; echo "exit=$?" >> "$T"; echo >> "$T"; }

echo "== V37 battery $(date +%FT%T%z) ==" >> "$T"
echo "HEAD: $(git rev-parse --short HEAD)  status:" >> "$T"
git status --porcelain >> "$T"

echo "## hashes of delivered artifacts" >> "$T"
sha256sum corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json \
  corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json \
  corpus/tools/README.md corpus/fixtures/r96-crossing-response/claim-excerpt-map.md >> "$T" 2>&1
sha256sum corpus/fixtures/r97-crossing-acknowledgment/* >> "$T" 2>&1

echo "## C1: contract case count + self-test" >> "$T"
python3 -c "import json;print('cases:',len(json.load(open('corpus/tools/map-obligations-contract.json'))['self_test']['cases']))" >> "$T" 2>&1
run python3 corpus/tools/map_obligations.py --self-test

echo "## C1: loader tightening (mirror; drop dual_pointer from contract copy)" >> "$T"
M=$S/mirror-delivered
rm -rf "$M"; mkdir -p "$M/corpus/tools"
cp corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json "$M/corpus/tools/"
python3 - "$M/corpus/tools/map-obligations-contract.json" <<'EOF' >> "$T" 2>&1
import json,sys
p=sys.argv[1]; d=json.load(open(p))
before=len(d['self_test']['cases'])
d['self_test']['cases']=[c for c in d['self_test']['cases'] if c['id']!='dual_pointer']
json.dump(d,open(p,'w'),indent=2)
print(f'dropped dual_pointer: {before} -> {len(d["self_test"]["cases"])} cases')
EOF
run python3 "$M/corpus/tools/map_obligations.py" --self-test

echo "## C1: baseline laxness control (r96 tool+contract; drop schema_drift)" >> "$T"
B=$S/mirror-baseline
rm -rf "$B"; mkdir -p "$B/corpus/tools"
git show f3e09f9:corpus/tools/map_obligations.py > "$B/corpus/tools/map_obligations.py"
git show f3e09f9:corpus/tools/map-obligations-contract.json > "$B/corpus/tools/map-obligations-contract.json"
python3 - "$B/corpus/tools/map-obligations-contract.json" <<'EOF' >> "$T" 2>&1
import json,sys
p=sys.argv[1]; d=json.load(open(p))
before=len(d['self_test']['cases'])
d['self_test']['cases']=[c for c in d['self_test']['cases'] if c['id']!='schema_drift']
json.dump(d,open(p,'w'),indent=2)
print(f'dropped schema_drift: {before} -> {len(d["self_test"]["cases"])} cases')
EOF
run python3 "$B/corpus/tools/map_obligations.py" --self-test

echo "## C1: dual_pointer pin load-bearing (neutralize emission in mirror tool)" >> "$T"
N=$S/mirror-neutralized
rm -rf "$N"; mkdir -p "$N/corpus/tools"
cp corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json "$N/corpus/tools/"
python3 - "$N/corpus/tools/map_obligations.py" <<'EOF' >> "$T" 2>&1
import sys,re
p=sys.argv[1]; s=open(p).read()
s2=re.sub(r'(def second_pointer_mention\([^)]*\):\n)', r'\1    return None\n', s, count=1)
print('patched' if s2!=s else 'PATCH FAILED'); open(p,'w').write(s2)
EOF
run python3 "$N/corpus/tools/map_obligations.py" --self-test

echo "## C1: regression battery on delivered corpus" >> "$T"
for fx in r88-m3-maya-cluster r93-m2-kojiki-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response r97-crossing-acknowledgment; do
  run python3 corpus/tools/map_obligations.py "corpus/fixtures/$fx"
done
run python3 corpus/tools/map_obligations.py corpus/fixtures/r87-myth-cluster
run python3 corpus/tools/map_obligations.py corpus/fixtures/r89-inspiration-paraphrase
run python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93

echo "## C2: freeze self-test + chain" >> "$T"
python3 -c "import json;d=json.load(open('corpus/tools/dependency-freeze-contract.json'));st=d.get('self_test');print('freeze self_test:', len(st['cases']) if isinstance(st,dict) and 'cases' in st else st);print('pins:', sorted(d['pins'].keys()))" >> "$T" 2>&1
run python3 corpus/tools/dependency_freeze.py --self-test
for fx in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response; do
  run python3 corpus/tools/dependency_freeze.py "corpus/fixtures/$fx"
done

echo "## C2: scope guard (mirror tree with git; --freeze foreign path must refuse)" >> "$T"
G=$S/mirror-freeze
rm -rf "$G"; mkdir -p "$G/corpus/tools" "$G/corpus/fixtures" "$G/foreign"
cp corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json "$G/corpus/tools/"
cp -r corpus/fixtures/r96-crossing-response "$G/corpus/fixtures/r96-x"
( cd "$G" && git init -q . && git add -A && git -c user.email=v37@scratch -c user.name=V37 commit -qm init )
run python3 "$G/corpus/tools/dependency_freeze.py" --freeze "$G/foreign/r96-x"
echo "--- foreign freeze: contract unchanged? sha:" >> "$T"
sha256sum "$G/corpus/tools/dependency-freeze-contract.json" >> "$T"
run python3 "$G/corpus/tools/dependency_freeze.py" --freeze "$G/corpus/fixtures/r96-x"
echo "--- after allowed freeze, pins:" >> "$T"
python3 -c "import json;print(sorted(json.load(open('$G/corpus/tools/dependency-freeze-contract.json'))['pins'].keys()))" >> "$T" 2>&1

echo "## C2: path binding (foreign same-named copy; delivered tool must exit 2 PATH-MISMATCH)" >> "$T"
F=$S/foreign-r96
rm -rf "$F"; mkdir -p "$F"
cp -r corpus/fixtures/r96-crossing-response "$F/"
run python3 corpus/tools/dependency_freeze.py "$F/r96-crossing-response"
echo "--- baseline tool on same foreign copy (expect exit 0):" >> "$T"
BT=$S/mirror-baseline-freeze
rm -rf "$BT"; mkdir -p "$BT/corpus/tools"
git show f3e09f9:corpus/tools/dependency_freeze.py > "$BT/corpus/tools/dependency_freeze.py"
git show f3e09f9:corpus/tools/dependency-freeze-contract.json > "$BT/corpus/tools/dependency-freeze-contract.json"
run python3 "$BT/corpus/tools/dependency_freeze.py" "$F/r96-crossing-response"

echo "## C2: DIGEST-MISMATCH names changed file (mirror pinned-path tamper)" >> "$T"
D=$S/mirror-digest
rm -rf "$D"; mkdir -p "$D/corpus/tools" "$D/corpus/fixtures"
cp corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json "$D/corpus/tools/"
cp -r corpus/fixtures/r96-crossing-response "$D/corpus/fixtures/"
printf ' \n' >> "$D/corpus/fixtures/r96-crossing-response/relations.json"
run python3 "$D/corpus/tools/dependency_freeze.py" "$D/corpus/fixtures/r96-crossing-response"

echo "## C3: r97 fixture gates" >> "$T"
run python3 corpus/fixtures/check_bible.py corpus/fixtures/r97-crossing-acknowledgment
run python3 corpus/tools/support_check.py corpus/fixtures/r97-crossing-acknowledgment
run python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response
echo "census: $(ls -d corpus/fixtures/*/ | wc -l) dirs" >> "$T"

echo "## C3: r96 receipts unchanged by repair (baseline map vs delivered map)" >> "$T"
RB=$S/r96-baseline-map
rm -rf "$RB"; mkdir -p "$RB"
cp -r corpus/fixtures/r96-crossing-response "$RB/"
git show f3e09f9:corpus/fixtures/r96-crossing-response/claim-excerpt-map.md > "$RB/r96-crossing-response/claim-excerpt-map.md"
run python3 corpus/tools/map_obligations.py "$RB/r96-crossing-response"
run python3 corpus/tools/support_check.py "$RB/r96-crossing-response"
echo "--- delivered r96 receipts:" >> "$T"
run python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response
run python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response

echo "== battery done $(date +%FT%T%z) ==" >> "$T"
echo "WROTE $T"
