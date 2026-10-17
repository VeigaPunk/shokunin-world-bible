#!/bin/bash
# V27 r96 final scope sweep: raw evidence capture + producer-artifact stability.
R=/home/vgpnk/Projects/shokunin/lore-shokunin
S=$R/.ufo/waves/round-96/seats/V27-scratch
mkdir -p $S/snap
cd $R
date '+%F %T %z' | tee $S/snap/sweep-time.txt
git log --oneline -1 > $S/snap/head.txt
git status --porcelain -uall > $S/snap/porcelain.txt
git diff --name-status > $S/snap/diff-name-status.txt
git diff --cached --name-status > $S/snap/diff-cached.txt
git diff --stat > $S/snap/diff-stat.txt
echo "--- diff-name-status ---"; cat $S/snap/diff-name-status.txt
echo "--- diff-cached ---"; cat $S/snap/diff-cached.txt
echo "--- porcelain count ---"; wc -l < $S/snap/porcelain.txt
echo "--- diff stat ---"; cat $S/snap/diff-stat.txt
echo "--- __pycache__ under corpus ---"
find corpus -name __pycache__ -o -name "*.pyc" | tee $S/snap/pycache.txt
ls -la corpus/tools/__pycache__ 2>&1 | tee $S/snap/pycache-ls.txt
echo "--- fixture dir listing ---"
ls -la corpus/fixtures/r96-crossing-response/ | tee $S/snap/fixture-ls.txt
echo "--- root transients ---"
ls -d map-obligations-self-test-* dependency-freeze-* depfreeze-* dependency_freeze-* 2>/dev/null | tee $S/snap/root-transients.txt || echo "(none)"
echo "--- producer artifact stability snapshot 1 ---"
find corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json corpus/tools/README.md corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json corpus/fixtures/r96-crossing-response corpus/knowledge/r96-response-scope-note.md -printf '%T@ %s %p\n' 2>/dev/null | sort | tee $S/snap/artifacts-1.txt
sleep 75
echo "--- producer artifact stability snapshot 2 (75s later) ---"
find corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json corpus/tools/README.md corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json corpus/fixtures/r96-crossing-response corpus/knowledge/r96-response-scope-note.md -printf '%T@ %s %p\n' 2>/dev/null | sort | tee $S/snap/artifacts-2.txt
if diff -q $S/snap/artifacts-1.txt $S/snap/artifacts-2.txt >/dev/null; then
  echo "PRODUCER ARTIFACTS STABLE across 75s"
else
  echo "PRODUCER ARTIFACTS CHANGED across 75s:"
  diff $S/snap/artifacts-1.txt $S/snap/artifacts-2.txt
fi
echo "--- post-sleep porcelain re-count (churn check) ---"
git status --porcelain -uall | wc -l
date '+%F %T %z'
