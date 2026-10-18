#!/bin/bash
# V46 poll v2: 20s cadence, max 40 tries.
# Ready when S1-S5 reports exist, both r99 knowledge files exist, r99 fixture
# has >=10 files, inherited tools + pre-r99 fixtures have zero drift vs 4265df5,
# and the signature is stable across two consecutive samples.
set -u
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
SCR=$ROOT/.ufo/waves/round-99/seats/V46-scratch
cd "$ROOT"
LOG=$SCR/poll.log
echo "POLL-V2-START $(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$LOG"
prev=""
for i in $(seq 1 40); do
  ts=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  names=$(ls -1 .ufo/waves/round-99/seats/S*.md 2>/dev/null | xargs -n1 basename 2>/dev/null | tr '\n' ',' )
  reports=0
  for s in S1-freeze-hygiene.md S2-tools-docs.md S3-fixture-author.md S4-fixture-docs.md S5-knowledge-notes.md; do
    if [ -f ".ufo/waves/round-99/seats/$s" ]; then reports=$((reports+1)); fi
  done
  # also count any other S*.md
  extra=$(ls -1 .ufo/waves/round-99/seats/S*.md 2>/dev/null | wc -l)
  know=0
  [ -f corpus/knowledge/r99-gate-blind-spot-table.md ] && know=$((know+1))
  [ -f corpus/knowledge/r99-lapse-scope-note.md ] && know=$((know+1))
  tools_sig=""
  for f in corpus/fixtures/check_bible.py corpus/tools/support_check.py corpus/tools/boundary_doc_check.py corpus/tools/discriminate_check.py corpus/tools/map_obligations.py corpus/live/rejected-r4/check_bible.py; do
    tools_sig+="$(git hash-object "$f"):"
  done
  move_sig=""
  for f in corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json corpus/tools/README.md SKILL.md; do
    move_sig+="$(git hash-object "$f"):"
  done
  r99_n=$(find corpus/fixtures/r99-window-lapse -type f 2>/dev/null | wc -l)
  r99_sig=$(find corpus/fixtures/r99-window-lapse -type f -printf '%P %s\n' 2>/dev/null | sort | sha256sum | awk '{print $1}')
  know_sig=""
  for f in corpus/knowledge/r99-gate-blind-spot-table.md corpus/knowledge/r99-lapse-scope-note.md; do
    if [ -f "$f" ]; then know_sig+="$(git hash-object "$f"):"; else know_sig+="ABSENT:"; fi
  done
  drift=$(git diff --name-only 4265df5 -- \
      corpus/fixtures/check_bible.py \
      corpus/tools/support_check.py \
      corpus/tools/boundary_doc_check.py \
      corpus/tools/discriminate_check.py \
      corpus/tools/map_obligations.py \
      corpus/live \
      corpus/fixtures \
      corpus/tools/boundary-doc-contract.json \
      corpus/tools/map-obligations-contract.json \
    | grep -v '^corpus/fixtures/r99-window-lapse/' | wc -l)
  # unexpected corpus writes: porcelain excluding declared producer paths and pycache
  stray=$(git status --porcelain --untracked-files=all -- corpus SKILL.md \
    | grep -v '__pycache__' \
    | grep -v 'corpus/fixtures/r99-window-lapse/' \
    | grep -v 'corpus/tools/dependency_freeze.py' \
    | grep -v 'corpus/tools/dependency-freeze-contract.json' \
    | grep -v 'corpus/tools/README.md' \
    | grep -v ' SKILL.md' \
    | grep -v 'corpus/knowledge/r99-' \
    | wc -l)
  line="try=$i ts=$ts named_reports=$reports extra_Smd=$extra names=${names:-none} know=$know r99_files=$r99_n drift=$drift stray=$stray"
  echo "$line tools=$tools_sig move=$move_sig knowsig=$know_sig r99sig=$r99_sig" >> "$LOG"
  sig="$reports|$know|$tools_sig|$move_sig|$know_sig|$r99_sig|$drift|$stray"
  if [ "$reports" -ge 5 ] && [ "$know" -eq 2 ] && [ "$r99_n" -ge 10 ] && [ "$drift" -eq 0 ] && [ "$stray" -eq 0 ] && [ "$sig" = "$prev" ]; then
    echo "POLL-STABLE try=$i $ts" >> "$LOG"
    echo "$line" > "$SCR/poll-stable.txt"
    echo "tools=$tools_sig" >> "$SCR/poll-stable.txt"
    echo "move=$move_sig" >> "$SCR/poll-stable.txt"
    echo "knowsig=$know_sig" >> "$SCR/poll-stable.txt"
    echo "r99sig=$r99_sig" >> "$SCR/poll-stable.txt"
    exit 0
  fi
  prev="$sig"
  sleep 20
done
echo "POLL-EXHAUSTED $(date -u +%Y-%m-%dT%H:%M:%SZ) last_sig=$sig" >> "$LOG"
exit 2
