#!/usr/bin/env bash
# Round 103 counting commands (lore). Run from the lane root: bash .ufo/waves/round-103/measure.sh [rev]
# With a rev argument, C1/C2/C3 counts read that commit via git (BEFORE = 6cec83a); without, the working tree.
set -u
rev="${1:-}"
show() { if [ -n "$rev" ]; then git show "$rev:$1" 2>/dev/null; else cat "$1" 2>/dev/null; fi; }
files() { if [ -n "$rev" ]; then git ls-tree -r --name-only "$rev" -- "$1"; else git ls-files -co --exclude-standard -- "$1"; fi; }

echo "== C1 coverage"
printf 'CM rows in corpus/README.md: '; show corpus/README.md | grep -cE '^\| CM-[a-z0-9]+ '
printf 'governed (non-uncovered, non-partial) CM-a..g rows: '; show corpus/README.md | grep -E '^\| CM-[a-g] ' | grep -cE '\| governed-'
printf 'knowledge entries with coverage-row: '; n=0; for f in $(files corpus/knowledge | grep '\.md$'); do show "$f" | sed -n 4p | grep -qE '^coverage-row: CM-' && n=$((n+1)); done; echo "$n"
printf '## Frontier headings / rows: '; show corpus/README.md | grep -c '^## Frontier'
show corpus/README.md | awk '/^## Frontier/{f=1;next} /^## /{f=0} f && /^\| [a-z]/ && !/^\| area/' | wc -l
printf 'PROVINCE Core/Frontier/Adjacent: '; show PROVINCE.md | grep -cE '^### (Core|Frontier|Adjacent)$'

echo "== C2 calibration"
printf 'QUALITY Q rows: '; show corpus/QUALITY.md | grep -cE '^\| Q[0-9]{2} '
printf 'Q rows citing a lesson: '; show corpus/QUALITY.md | grep -E '^\| Q[0-9]{2} ' | grep -c 'corpus/lessons/round-103.md#mistakes M'
printf 'lesson M rows: '; show corpus/lessons/round-103.md | grep -cE '^\| M[0-9]{2} '
printf 'mistake classes captured by a criterion: '; show corpus/lessons/round-103.md | grep -E '^\| M[0-9]{2} ' | awk -F'|' '$5 ~ /Q[0-9]{2}/' | wc -l
printf 'lesson ## Gate with admitted+rejected: '; show corpus/lessons/round-103.md | grep -cE '^### (Admitted|Rejected)$'

echo "== C3 depth (SOURCES capability)"
printf 'SOURCES rows: '; show corpus/SOURCES.md | grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
printf 'admitted r103 entries whose every source id is a mined row naming the entry in used-by: '
ok=0; tot=0
for f in $(files corpus/knowledge | grep -E 'knowledge/r103-.*\.md$'); do
  tot=$((tot+1)); good=1
  for id in $(show "$f" | sed -n 1p | grep -oE '\bS[0-9]{3,}\b' | sort -u); do
    show corpus/SOURCES.md | awk -F'|' -v id="$id" -v f="$f" '{i=$2;s=$9;gsub(/[[:space:]]/,"",i);gsub(/[[:space:]]/,"",s)} i==id && s=="mined" && index($12,f){ok=1} END{exit !ok}' || good=0
  done
  [ "$good" = 1 ] && ok=$((ok+1))
done; echo "$ok/$tot"
