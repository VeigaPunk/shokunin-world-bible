#!/bin/bash
# V55 C2 probe suite (final): run against an isolated fake root built from DELIVERED tool+contract.
# Usage: bash probe-c2-final.sh  (from anywhere; paths absolute)
set -u
REPO=/home/vgpnk/Projects/shokunin/lore-shokunin
SCR=$REPO/.ufo/waves/round-97/seats/V55-scratch
FAKE=$SCR/fakeroot3
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
mkdir -p $FAKE/corpus/fixtures/samenamed
cp -r $FAKE/corpus/fixtures/r96-crossing-response $FAKE/corpus/fixtures/samenamed/
mkdir -p $FAKE/corpus/fixtures/nested
cp -r $FAKE/corpus/fixtures/r96-crossing-response $FAKE/corpus/fixtures/nested/
echo "tool sha: $(sha256sum $FAKE/corpus/tools/dependency_freeze.py | cut -d' ' -f1)"
echo "contract sha at start: $(sha256sum $FAKE/corpus/tools/dependency-freeze-contract.json | cut -d' ' -f1)"
H0=$(sha256sum $FAKE/corpus/tools/dependency-freeze-contract.json | cut -d' ' -f1)

run() { # label, then command...
  local label="$1"; shift
  echo "--- $label"
  echo "\$ $*"
  ( cd $FAKE && python3 "$@" ); local code=$?
  echo "exit=$code"
}

echo
echo "=== P1 SCOPE GUARD: out-of-scope targets must exit 2, contract unchanged ==="
run "P1a freeze foreign/ (relative, out of scope)" corpus/tools/dependency_freeze.py --freeze foreign/r96-crossing-response
run "P1b freeze absolute out-of-scope" corpus/tools/dependency_freeze.py --freeze $FAKE/outofscope/r96-crossing-response
run "P1c freeze traversal escaping scope" corpus/tools/dependency_freeze.py --freeze corpus/fixtures/../../foreign/r96-crossing-response
run "P1d freeze corpus/tools (out of scope)" corpus/tools/dependency_freeze.py --freeze corpus/tools
run "P1e freeze scope dir itself" corpus/tools/dependency_freeze.py --freeze corpus/fixtures
echo "--- contract sha after refusals (must equal start): $(sha256sum $FAKE/corpus/tools/dependency-freeze-contract.json | cut -d' ' -f1) (start $H0)"

echo
echo "=== P10 SCOPE GUARD: in-scope same-named different-path target must be refused (pin-path rewrite) ==="
run "P10a freeze corpus/fixtures/samenamed/r96-crossing-response" corpus/tools/dependency_freeze.py --freeze corpus/fixtures/samenamed/r96-crossing-response
echo "--- contract sha after P10 (must equal start): $(sha256sum $FAKE/corpus/tools/dependency-freeze-contract.json | cut -d' ' -f1)"

echo
echo "=== P2 SCOPE GUARD: in-scope same-path target accepted (pin refresh; fake root only) ==="
run "P2a freeze corpus/fixtures/r96-crossing-response (in scope, same path)" corpus/tools/dependency_freeze.py --freeze corpus/fixtures/r96-crossing-response
echo "--- pin path recorded:"
python3 -c "import json;print(json.load(open('$FAKE/corpus/tools/dependency-freeze-contract.json'))['pins']['r96-crossing-response']['fixture'])"
run "P2b freeze absolute in-scope path (r94)" corpus/tools/dependency_freeze.py --freeze $FAKE/corpus/fixtures/r94-paired-crossing

echo
echo "=== P3 PATH BINDING ==="
run "P3a verify foreign-path same-named copy (expect PATH-MISMATCH exit 2)" corpus/tools/dependency_freeze.py foreign/r96-crossing-response
run "P3b verify in-scope-but-different-path copy (expect PATH-MISMATCH exit 2)" corpus/tools/dependency_freeze.py corpus/fixtures/nested/r96-crossing-response
run "P3c verify correct path (expect 0)" corpus/tools/dependency_freeze.py corpus/fixtures/r96-crossing-response

echo
echo "=== P8 SYMLINK PROBES ==="
ln -sfn $FAKE/foreign/r96-crossing-response $FAKE/corpus/fixtures/symlink-escape
run "P8a freeze symlink inside fixtures -> foreign target (expect SCOPE-REFUSED)" corpus/tools/dependency_freeze.py --freeze corpus/fixtures/symlink-escape
run "P8b verify symlink inside fixtures -> foreign target (expect PATH-MISMATCH)" corpus/tools/dependency_freeze.py corpus/fixtures/symlink-escape

echo
echo "=== P4 DIGEST-MISMATCH NAMES THE CHANGED FILE (tamper at pinned path) ==="
python3 - <<PYEOF
p='$FAKE/corpus/fixtures/r96-crossing-response/timeline.json'
t=open(p).read()
t2=t.replace('south bell at Salt Court','South bell at Salt Court',1)
assert t2!=t, 'tamper target not found'
open(p,'w').write(t2)
print('tampered pinned-path copy timeline.json (case change, non-inventory-modeled)')
PYEOF
run "P4a verify tampered pinned path (expect DIGEST-MISMATCH naming timeline.json)" corpus/tools/dependency_freeze.py corpus/fixtures/r96-crossing-response

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
echo "=== P7 r97 (new fixture) verify status (expect UNPINNED-FIXTURE; chain is 4) ==="
( cd $REPO && python3 corpus/tools/dependency_freeze.py corpus/fixtures/r97-crossing-acknowledgment ); echo "exit=$?"

echo
echo "=== P11 REAL-TREE DENY + HASH GUARD (read-only probe on real contract) ==="
H1=$(sha256sum $REPO/corpus/tools/dependency-freeze-contract.json | cut -d' ' -f1)
echo "real contract sha before: $H1"
( cd $REPO && python3 corpus/tools/dependency_freeze.py --freeze corpus/knowledge ) ; echo "exit=$?"
echo "real contract sha after: $(sha256sum $REPO/corpus/tools/dependency-freeze-contract.json | cut -d' ' -f1)"
