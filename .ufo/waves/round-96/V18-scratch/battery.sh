#!/bin/bash
# V18 seat battery — c3-addition-endpoint, run against the frozen revision.
# All mutations on scratch copies under V18-scratch; corpus is read-only here.
set -u
cd /home/vgpnk/Projects/shokunin/lore-shokunin
S=.ufo/waves/round-96/V18-scratch
P=python3

echo "=== REVISION (before) ==="
sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json

echo "=== B1 baseline 4/4 chain (real corpus) ==="
for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response; do
  printf "%-28s " "$f"; $P corpus/tools/dependency_freeze.py corpus/fixtures/$f >"$S/logs/b1-$f.out" 2>&1
  echo "exit=$? $(grep -c FINDING "$S/logs/b1-$f.out") findings $(grep RESULT "$S/logs/b1-$f.out")"
done

echo "=== B2 clean scratch copy (x2) ==="
$P $S/probe.py clean r95-crossing-aftermath 2>&1 | grep -E "^--- run|^=== SUMMARY|FREEZE|RESULT"

echo "=== B3 phantom depends_on addition, r96 response-evin-salt-court += phantom-tick-13 (x2) ==="
$P $S/probe.py mutate r96-crossing-response phantom response-evin-salt-court phantom-tick-13 2>&1 | grep -E "^MUTATED|^--- run|FINDING|RESULT|^=== SUMMARY"

echo "=== B4 relation from/to flip, r96 (x2) ==="
$P $S/probe.py mutate r96-crossing-response flip 2>&1 | grep -E "^MUTATED|^--- run|FINDING|RESULT|^=== SUMMARY"

echo "=== B5 relation endpoint change aru->jorin, r95 (x2) ==="
$P $S/probe.py mutate r95-crossing-aftermath endpoint aru jorin 2>&1 | grep -E "^MUTATED|^--- run|FINDING|RESULT|^=== SUMMARY"

echo "=== B6 event row deletion with its edges, r96 aftermath-missing-evin (x2) ==="
$P $S/probe.py mutate r96-crossing-response delete aftermath-missing-evin 2>&1 | grep -E "^MUTATED|^--- run|FINDING|RESULT|^=== SUMMARY"

echo "=== B7 BR-01 reduction: r94 tick-10 loses evin-ninth-bell (x2) ==="
$P $S/probe.py mutate r94-paired-crossing reduce paired-crossing-decision evin-ninth-bell 2>&1 | grep -E "^MUTATED|^--- run|FINDING|RESULT|^=== SUMMARY"

echo "=== B8 digest-only text tamper (inventory-neutral), r95 (x2) ==="
$P $S/probe.py mutate r95-crossing-aftermath texttamper aftermath-missing-evin 2>&1 | grep -E "^MUTATED|^--- run|FINDING|RESULT|^=== SUMMARY"

echo "=== B9 self-test (x2) ==="
for i in 1 2; do
  $P corpus/tools/dependency_freeze.py --self-test >"$S/logs/b9-selftest-$i.out" 2>&1
  echo "run$i exit=$? $(grep -E '^SELF-TEST|^RESULT' "$S/logs/b9-selftest-$i.out" | tr '\n' ' ')"
done

echo "=== B10 exit-2 surfaces (unpinned / missing dir / bad args / self-test+fixture) ==="
rm -rf "$S/scratch-root/not-a-pinned-name"; cp -r corpus/fixtures/r95-crossing-aftermath "$S/scratch-root/not-a-pinned-name"
$P corpus/tools/dependency_freeze.py "$S/scratch-root/not-a-pinned-name" 2>&1 | head -2; echo "unpinned exit=$?"
$P corpus/tools/dependency_freeze.py "$S/scratch-root/does-not-exist" 2>&1 | head -2
$P corpus/tools/dependency_freeze.py 2>&1 | head -2
$P corpus/tools/dependency_freeze.py --self-test corpus/fixtures/r95-crossing-aftermath 2>&1 | head -2

echo "=== B11 independent pin-vs-oracle cross-check ==="
$P $S/pincheck.py; echo "exit=$?"

echo "=== B12 corpus write audit + REVISION (after) ==="
git status --porcelain corpus/
sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json
