#!/bin/bash
# V55 C2 probe suite: run against an isolated fake root built from DELIVERED tool+contract.
# Usage: bash probe-c2.sh  (from anywhere; paths absolute)
set -u
REPO=/home/vgpnk/Projects/shokunin/lore-shokunin
SCR=$REPO/.ufo/waves/round-97/seats/V55-scratch
FAKE=$SCR/fakeroot2
export TMPDIR=$SCR/tmp
mkdir -p $TMPDIR

echo "=== REBUILD FAKE ROOT (delivered tool + delivered contract) ==="
rm -rf $FAKE
mkdir -p $FAKE/corpus/tools $FAKE/corpus/fixtures $FAKE/foreign $FAKE/outofscope
cp $REPO/corpus/tools/dependency_freeze.py $FAKE/corpus/tools/
cp $REPO/corpus/tools/dependency-freeze-contract.json $FAKE/corpus/tools/
cp -r $REPO/corpus/fixtures/r96-crossing-response $FAKE/corpus/fixtures/
cp -r $REPO/corpus/fixtures/r95-crossing-aftermath $FAKE/corpus/fixtures/
cp -r $REPO/corpus/fixtures/r94-paired-crossing $FAKE/corpus/fixtures/
cp -r $REPO/corpus/fixtures/r88-m3-maya-cluster $FAKE/corpus/fixtures/
cp -r $REPO/corpus/fixtures/r96-crossing-response $FAKE/foreign/
cp -r $REPO/corpus/fixtures/r96-crossing-response $FAKE/outofscope/r96-crossing-response
cp $REPO/corpus/tools/dependency-freeze-contract.json $SCR/delivered-contract-snapshot.json
sha256sum $FAKE/corpus/tools/dependency-freeze-contract.json
echo "FAKE ROOT READY at $FAKE"

run() { # label, then command...
  local label="$1"; shift
  echo "--- $label"
  echo "\$ $*"
  ( cd $FAKE && python3 "$@" ); local code=$?
  echo "exit=$code"
}

echo
echo "=== P1 SCOPE GUARD: out-of-scope targets must exit 2 ==="
run "P1a freeze foreign/ (relative, out of scope)" corpus/tools/dependency_freeze.py --freeze foreign/r96-crossing-response
run "P1b freeze /abs out-of-scope" corpus/tools/dependency_freeze.py --freeze $FAKE/outofscope/r96-crossing-response
run "P1c freeze traversal escaping scope" corpus/tools/dependency_freeze.py --freeze corpus/fixtures/../../foreign/r96-crossing-response
run "P1d freeze corpus/knowledge-style dir (out of scope)" corpus/tools/dependency_freeze.py --freeze corpus/tools
echo "--- contract bytes after out-of-scope attempts (must be unchanged):"
sha256sum $FAKE/corpus/tools/dependency-freeze-contract.json

echo
echo "=== P2 SCOPE GUARD: in-scope target accepted (fake root only) ==="
run "P2a freeze corpus/fixtures/r96-crossing-response (in scope)" corpus/tools/dependency_freeze.py --freeze corpus/fixtures/r96-crossing-response
echo "--- pin path recorded:"
python3 -c "import json;print(json.load(open('$FAKE/corpus/tools/dependency-freeze-contract.json'))['pins']['r96-crossing-response']['fixture'])"

echo
echo "=== P3 PATH BINDING ==="
run "P3a verify foreign-path same-named copy (expect PATH-MISMATCH exit 2)" corpus/tools/dependency_freeze.py foreign/r96-crossing-response
mkdir -p $FAKE/corpus/fixtures/nested
cp -r $FAKE/corpus/fixtures/r96-crossing-response $FAKE/corpus/fixtures/nested/
run "P3b verify in-scope-but-different-path copy (expect PATH-MISMATCH exit 2)" corpus/tools/dependency_freeze.py corpus/fixtures/nested/r96-crossing-response
run "P3c verify correct path (expect 0)" corpus/tools/dependency_freeze.py corpus/fixtures/r96-crossing-response

echo
echo "=== P4 DIGEST-MISMATCH NAMES THE CHANGED FILE ==="
python3 - <<PYEOF
p='$FAKE/foreign/r96-crossing-response/timeline.json'
t=open(p).read()
t2=t.replace('south bell at Salt Court','South bell at Salt Court',1)
assert t2!=t, 'tamper target not found'
open(p,'w').write(t2)
print('tampered foreign copy timeline.json (case change, non-inventory-modeled)')
PYEOF
run "P4a verify tampered copy (expect DIGEST-MISMATCH naming timeline.json)" corpus/tools/dependency_freeze.py foreign/r96-crossing-response

echo
echo "=== P5 SELF-TEST (real delivered tool, real contract) ==="
( cd $REPO && python3 corpus/tools/dependency_freeze.py --self-test ); echo "exit=$?"
echo "--- contract expected case count:"
python3 -c "import json;c=json.load(open('$REPO/corpus/tools/dependency-freeze-contract.json'));print(len(c['self_test']['expected']), sorted(c['self_test']['expected']))"

echo
echo "=== P6 CHAIN 4/4 (real repo, read-only verify) ==="
for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response; do
  ( cd $REPO && python3 corpus/tools/dependency_freeze.py corpus/fixtures/$f >/dev/null 2>&1; echo "$f exit=$?" )
done

echo
echo "=== P7 r97 (new fixture) verify status ==="
( cd $REPO && python3 corpus/tools/dependency_freeze.py corpus/fixtures/r97-crossing-acknowledgment ); echo "exit=$?"
