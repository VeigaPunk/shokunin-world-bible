#!/bin/sh
# V27 r99 adjacency — post-report freeze manifest. Usage: freeze.sh <outfile>
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 1
OUT="${1:-/tmp/v27-freeze.txt}"
{
  echo "FREEZE $(date '+%Y-%m-%d %H:%M:%S %z')"
  for f in PROVINCE.md SHONEN.md SKILL.md README.md l0-questions.md \
           corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json \
           corpus/tools/README.md \
           corpus/knowledge/r99-gate-blind-spot-table.md corpus/knowledge/r99-lapse-scope-note.md \
           corpus/fixtures/r99-window-lapse/README.md corpus/fixtures/r99-window-lapse/claim-excerpt-map.md \
           corpus/fixtures/r99-window-lapse/contradictions.json corpus/fixtures/r99-window-lapse/entities.json \
           corpus/fixtures/r99-window-lapse/fictional-excerpts.md corpus/fixtures/r99-window-lapse/inspiration-note.md \
           corpus/fixtures/r99-window-lapse/relations.json corpus/fixtures/r99-window-lapse/source-excerpt.md \
           corpus/fixtures/r99-window-lapse/sources.json corpus/fixtures/r99-window-lapse/timeline.json \
           LOG.md SCORECARD.md; do
    if [ -f "$f" ]; then
      h=$(sha256sum "$f" | cut -d' ' -f1)
      m=$(stat -c %y "$f" | cut -d. -f1)
      echo "SHA256 $h  $m  $f"
    else
      echo "ABSENT $f"
    fi
  done
} > "$OUT"
sha256sum "$OUT"
