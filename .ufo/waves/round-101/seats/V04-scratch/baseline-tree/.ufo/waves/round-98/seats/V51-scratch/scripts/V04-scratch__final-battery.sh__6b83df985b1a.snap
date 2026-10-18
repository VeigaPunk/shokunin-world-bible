#!/bin/bash
# V04 c1-regression final battery — runs from the lane repo root.
set -u
S=".ufo/waves/round-98/seats/V04-scratch"
M="$S/mirror-final"
rm -rf "$M"
mkdir -p "$M/corpus/tools" "$M/corpus/fixtures"
cp corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json "$M/corpus/tools/"
for f in r95-crossing-aftermath r97-crossing-acknowledgment r98-clerk-filing; do cp -r "corpus/fixtures/$f" "$M/corpus/fixtures/"; done
T="$M/corpus/tools/dependency_freeze.py"
C="$M/corpus/tools/dependency-freeze-contract.json"

echo "### revision under test"
sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json
C0=$(sha256sum corpus/tools/dependency-freeze-contract.json | cut -d' ' -f1)

echo "### 1 self-test (real tree)"
python3 corpus/tools/dependency_freeze.py --self-test | tail -2
echo "SELFTEST_EXIT=${PIPESTATUS[0]}"

echo "### 2 chain 6/6 (real tree)"
for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response r97-crossing-acknowledgment r98-clerk-filing; do
  out=$(python3 corpus/tools/dependency_freeze.py "corpus/fixtures/$f"); rc=$?
  echo "$f exit=$rc $(echo "$out" | tr '\n' ' | ')"
done

echo "### 3 SCOPE-REFUSED (real tool, --freeze outside scope)"
python3 corpus/tools/dependency_freeze.py --freeze "$PWD/$S/target" | tail -2
echo "EXIT=${PIPESTATUS[0]}"

echo "### 4 PATH-MISMATCH (real tool, foreign same-name copies)"
for f in r95-crossing-aftermath r98-clerk-filing; do
  rm -rf "$S/foreign/$f"; cp -r "corpus/fixtures/$f" "$S/foreign/$f"
  python3 corpus/tools/dependency_freeze.py "$PWD/$S/foreign/$f" | head -1
  echo "$f EXIT=${PIPESTATUS[0]}"
done

echo "### 5 in-scope same-named --freeze refusal (mirror), r95 and r98"
mkdir -p "$M/corpus/fixtures/nested"
for f in r95-crossing-aftermath r98-clerk-filing; do
  rm -rf "$M/corpus/fixtures/nested/$f"; cp -r "corpus/fixtures/$f" "$M/corpus/fixtures/nested/$f"
  python3 "$T" --freeze "$M/corpus/fixtures/nested/$f" | head -1
  echo "$f EXIT=${PIPESTATUS[0]}"
done

echo "### 6 tamper classes (mirror r95)"
python3 -c "
import json
p='$M/corpus/fixtures/r95-crossing-aftermath/timeline.json'
d=json.load(open(p))
for r in d:
    if r['id']=='aftermath-missing-evin': r['depends_on']=[]
json.dump(d,open(p,'w'),indent=2); open(p,'a').write('\n')
"
python3 "$T" "$M/corpus/fixtures/r95-crossing-aftermath" | tail -2
echo "SEMANTIC_TAMPER_EXIT=${PIPESTATUS[0]}"
cp corpus/fixtures/r95-crossing-aftermath/timeline.json "$M/corpus/fixtures/r95-crossing-aftermath/timeline.json"
printf '\n' >> "$M/corpus/fixtures/r95-crossing-aftermath/timeline.json"
python3 "$T" "$M/corpus/fixtures/r95-crossing-aftermath" | tail -2
echo "COSMETIC_TAMPER_EXIT=${PIPESTATUS[0]}"
cp corpus/fixtures/r95-crossing-aftermath/timeline.json "$M/corpus/fixtures/r95-crossing-aftermath/timeline.json"

echo "### 7 path-less legacy pin migration (mirror)"
python3 -c "
import json
p='$C'; c=json.load(open(p)); del c['pins']['r95-crossing-aftermath']['fixture']
json.dump(c,open(p,'w'),indent=2); open(p,'a').write('\n')
"
python3 "$T" --freeze "$M/corpus/fixtures/r95-crossing-aftermath" | head -1
echo "MIGRATE_EXIT=${PIPESTATUS[0]}"
python3 -c "import json;c=json.load(open('$C'));print('pin path after migration:',repr(c['pins']['r95-crossing-aftermath'].get('fixture')))"
python3 "$T" "$M/corpus/fixtures/r95-crossing-aftermath" | tail -1
echo "REVERIFY_EXIT=${PIPESTATUS[0]}"

echo "### 8 guard precedes migration (path-less pin + out-of-scope copy)"
python3 -c "
import json
p='$C'; c=json.load(open(p)); del c['pins']['r95-crossing-aftermath']['fixture']
json.dump(c,open(p,'w'),indent=2); open(p,'a').write('\n')
"
G0=$(sha256sum "$C" | cut -d' ' -f1)
python3 "$T" --freeze "$S/foreign/r95-crossing-aftermath" | head -1
echo "EXIT=${PIPESTATUS[0]}"
G1=$(sha256sum "$C" | cut -d' ' -f1); [ "$G0" = "$G1" ] && echo MIRROR_CONTRACT_UNCHANGED=yes || echo MIRROR_CONTRACT_UNCHANGED=NO

echo "### 9 strict loader fails closed on a dropped pinned case"
python3 -c "
import json
p='$C'; c=json.load(open(p)); del c['self_test']['expected']['clean']
json.dump(c,open(p,'w'),indent=2); open(p,'a').write('\n')
"
python3 "$T" --self-test | tail -2
echo "EXIT=${PIPESTATUS[0]}"

echo "### 10 marker-env sensitivity of the new recursion guard (real tree)"
DEPENDENCY_FREEZE_SELF_TEST_CHILD=1 python3 corpus/tools/dependency_freeze.py --self-test | tail -2
echo "EXIT=${PIPESTATUS[0]}"

echo "### 11 real contract untouched by the battery"
C1=$(sha256sum corpus/tools/dependency-freeze-contract.json | cut -d' ' -f1)
echo "BEFORE=$C0"
echo "AFTER=$C1"
[ "$C0" = "$C1" ] && echo CONTRACT_UNCHANGED=yes || echo CONTRACT_UNCHANGED=NO

echo "### 12 residue"
ls -d *-self-test-*/ 2>/dev/null || echo "no repo-root self-test scratch residue"
