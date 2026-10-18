#!/bin/bash
# V107 adjacency battery. Run only after the producer gate is met.
# Writes only under V107-scratch/. Quotes are the script's own stdout files.
set -u
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
OUT="$ROOT/.ufo/waves/round-99/seats/V107-scratch"
cd "$ROOT" || exit 1
STAMP=$(date '+%Y%m%dT%H%M%S')
EV="$OUT/ev-$STAMP"
mkdir -p "$EV"
exec > >(tee "$EV/measure.log") 2>&1
echo "MEASURE_START $(date '+%Y-%m-%d %H:%M:%S %z') stamp=$STAMP"
echo "HEAD $(git rev-parse HEAD)"
echo "BASE 4265df5 $(git rev-parse 4265df5)"

echo "===== A1 charter ====="
sha256sum PROVINCE.md
git show 4265df5:PROVINCE.md | sha256sum
echo -n "hash-object "; git hash-object PROVINCE.md
echo -n "rev-parse  "; git rev-parse 4265df5:PROVINCE.md
echo -n "diff-bytes "; git diff 4265df5 -- PROVINCE.md | wc -c
for f in PROVINCE.md SHONEN.md SKILL.md README.md l0-questions.md SCORECARD.md; do
  wb=$(git hash-object "$f")
  bb=$(git rev-parse "4265df5:$f")
  hb=$(git rev-parse "HEAD:$f")
  if [ "$wb" = "$bb" ]; then rel=IDENTICAL-BASE; else rel=DIFF-BASE; fi
  if [ "$wb" = "$hb" ]; then hrel=IDENTICAL-HEAD; else hrel=DIFF-HEAD; fi
  echo "$rel $hrel $f work=$wb base=$bb head=$hb"
done
echo "SCORECARD-log $(git log -1 --format='%h %ci %s' -- SCORECARD.md)"
echo "LOG-vs-HEAD-bytes $(git diff HEAD -- LOG.md | wc -c)"
echo "LOG-numstat-vs-4265"
git diff --numstat 4265df5 -- LOG.md

echo "===== A2 tracked name-status ====="
echo "-- vs 4265df5 --"
git diff --name-status 4265df5
echo "-- vs HEAD --"
git diff --name-status HEAD
echo "-- numstat vs HEAD --"
git diff --numstat HEAD

echo "===== A2 blob audit ====="
python3 "$OUT/audit_tree.py" | tee "$EV/audit.txt"

echo "===== A2 untracked outside wave (filtered) ====="
git status --porcelain -uall | grep '^??' | grep -v 'round-99/' | tee "$EV/untracked-outside-r99.txt" || true
echo "===== A2 parent stray ====="
ls -d /home/vgpnk/Projects/shokunin/.ufo/waves/round-99 2>&1 || true
echo "===== A2 reflog ====="
git reflog -5

echo "===== A2 census ====="
echo -n "fixture-dirs "; ls -d corpus/fixtures/*/ | wc -l
echo "===== A2 modes/symlinks r99 fixture ====="
find corpus/fixtures/r99-window-lapse -type l | wc -l
find corpus/fixtures/r99-window-lapse -type f ! -perm 644 | wc -l
find corpus/knowledge -name 'r99-*' -type f -printf '%m %p\n'

echo "===== A2 chain fixtures vs 4265df5 ====="
for d in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response r97-crossing-acknowledgment r98-clerk-filing; do
  n=$(git diff --name-only 4265df5 -- "corpus/fixtures/$d" | wc -l)
  echo "chain-diff-files $d $n"
done

echo "===== hashes ====="
sha256sum \
  corpus/tools/dependency_freeze.py \
  corpus/tools/dependency-freeze-contract.json \
  corpus/tools/README.md \
  SKILL.md \
  corpus/fixtures/r99-window-lapse/* \
  corpus/knowledge/r99-gate-blind-spot-table.md \
  corpus/knowledge/r99-lapse-scope-note.md \
  | tee "$EV/freeze.sha256"

echo "===== producer mtimes ====="
stat -c '%y %n' \
  corpus/tools/dependency_freeze.py \
  corpus/tools/dependency-freeze-contract.json \
  corpus/tools/README.md \
  SKILL.md \
  corpus/fixtures/r99-window-lapse/* \
  corpus/knowledge/r99-gate-blind-spot-table.md \
  corpus/knowledge/r99-lapse-scope-note.md \
  .ufo/waves/round-99/seats/S*-*.md \
  | tee "$EV/mtimes.txt"

echo "MEASURE_END $(date '+%Y-%m-%d %H:%M:%S %z')"
