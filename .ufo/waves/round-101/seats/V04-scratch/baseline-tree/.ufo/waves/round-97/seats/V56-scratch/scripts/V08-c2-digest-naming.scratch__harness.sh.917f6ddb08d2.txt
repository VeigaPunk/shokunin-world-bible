#!/bin/bash
# V08 c2-digest-naming harness — runs on the frozen R3 revision
cd /home/vgpnk/Projects/shokunin/lore-shokunin
SC=.ufo/waves/round-97/seats/V08-c2-digest-naming.scratch
TOOL=corpus/tools/dependency_freeze.py
CONTR=corpus/tools/dependency-freeze-contract.json
REAL_FIX=corpus/fixtures/r95-crossing-aftermath
set -u

echo "########## 0. frozen hashes"
sha256sum $TOOL $CONTR | tee $SC/logs/frozen-hashes.txt
stat -c "%y %s %n" $TOOL $CONTR | tee -a $SC/logs/frozen-hashes.txt

echo "########## 1. self-test on frozen revision"
python3 $TOOL --self-test 2>&1 | tee $SC/logs/selftest.log; echo "EXIT=${PIPESTATUS[0]}"

echo "########## 2. four pins name paths"
python3 $SC/check_pins.py 2>&1 | tee $SC/logs/pins.log

echo "########## 3. real chain 4/4 clean"
for d in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response; do
  python3 $TOOL corpus/fixtures/$d; echo "EXIT=$?"
done | tee $SC/logs/chain.log

echo "########## 4. foreign-path pristine copy on REAL tool"
python3 $TOOL $SC/foreign/r95-crossing-aftermath 2>&1 | tee $SC/logs/foreign.log; echo "EXIT=${PIPESTATUS[0]}"

echo "########## 5. mirror workspace: build"
WS=$SC/ws
rm -rf $WS; mkdir -p $WS/corpus/tools $WS/corpus/fixtures
cp $TOOL $CONTR $WS/corpus/tools/
cp -r $REAL_FIX $WS/corpus/fixtures/
MIRROR_FIX=$WS/corpus/fixtures/r95-crossing-aftermath

echo "########## 5a. mirror clean control"
python3 $WS/corpus/tools/dependency_freeze.py $MIRROR_FIX 2>&1 | tee $SC/logs/mirror-clean.log; echo "EXIT=${PIPESTATUS[0]}"

echo "########## 6. T1: tamper sources.json (one char) -> expect DIGEST-MISMATCH naming sources.json"
python3 - <<'PY'
from pathlib import Path
p = Path(".ufo/waves/round-97/seats/V08-c2-digest-naming.scratch/ws/corpus/fixtures/r95-crossing-aftermath/sources.json")
t = p.read_text(); t2 = t.replace("note", "Note", 1); assert t2 != t; p.write_text(t2)
print("tampered: sources.json first 'note' -> 'Note'")
PY
python3 $WS/corpus/tools/dependency_freeze.py $MIRROR_FIX 2>&1 | tee $SC/logs/T1-sources.log; echo "EXIT=${PIPESTATUS[0]}"

echo "########## 7. T2: fresh mirror; tamper timeline.json description only -> names timeline.json"
rm -rf $MIRROR_FIX && cp -r $REAL_FIX $MIRROR_FIX
python3 - <<'PY'
from pathlib import Path
p = Path(".ufo/waves/round-97/seats/V08-c2-digest-naming.scratch/ws/corpus/fixtures/r95-crossing-aftermath/timeline.json")
t = p.read_text(); t2 = t.replace("south bell at Salt Court", "South bell at Salt Court", 1); assert t2 != t; p.write_text(t2)
print("tampered: timeline.json 'south bell at Salt Court' -> 'South ...'")
PY
python3 $WS/corpus/tools/dependency_freeze.py $MIRROR_FIX 2>&1 | tee $SC/logs/T2-timeline.log; echo "EXIT=${PIPESTATUS[0]}"

echo "########## 8. T3: fresh mirror; tamper TWO files -> names both"
rm -rf $MIRROR_FIX && cp -r $REAL_FIX $MIRROR_FIX
python3 - <<'PY'
from pathlib import Path
d = Path(".ufo/waves/round-97/seats/V08-c2-digest-naming.scratch/ws/corpus/fixtures/r95-crossing-aftermath")
t = (d/"sources.json").read_text(); (d/"sources.json").write_text(t.replace("note","Note",1))
t = (d/"entities.json").read_text(); (d/"entities.json").write_text(t.replace("north lantern","North lantern",1))
print("tampered: sources.json + entities.json")
PY
python3 $WS/corpus/tools/dependency_freeze.py $MIRROR_FIX 2>&1 | tee $SC/logs/T3-two.log; echo "EXIT=${PIPESTATUS[0]}"

echo "########## 9. real fixture untouched (real tool on real path)"
python3 $TOOL $REAL_FIX 2>&1 | tee $SC/logs/real-r95-after.log; echo "EXIT=${PIPESTATUS[0]}"
