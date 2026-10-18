#!/bin/sh
# V24 r98 adjacency — post-report freeze manifest. Usage: freeze.sh <outfile>
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 1
OUT="${1:-/tmp/v24-freeze.txt}"
{
  echo "FREEZE $(date '+%Y-%m-%d %H:%M:%S %z')"
  for f in PROVINCE.md SHONEN.md SKILL.md README.md l0-questions.md \
           corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json \
           corpus/tools/README.md corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md \
           corpus/knowledge/r95-aftermath-scope-note.md corpus/knowledge/r96-response-scope-note.md \
           corpus/knowledge/r98-clerk-scope-note.md \
           corpus/fixtures/r98-clerk-filing/README.md corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md \
           corpus/fixtures/r98-clerk-filing/contradictions.json corpus/fixtures/r98-clerk-filing/entities.json \
           corpus/fixtures/r98-clerk-filing/fictional-excerpts.md corpus/fixtures/r98-clerk-filing/inspiration-note.md \
           corpus/fixtures/r98-clerk-filing/relations.json corpus/fixtures/r98-clerk-filing/source-excerpt.md \
           corpus/fixtures/r98-clerk-filing/sources.json corpus/fixtures/r98-clerk-filing/timeline.json; do
    if [ -f "$f" ]; then
      h=$(sha256sum "$f" | cut -d' ' -f1)
      m=$(stat -c %y "$f" | cut -d. -f1)
      echo "SHA256 $h  $m  $f"
    else
      echo "ABSENT $f"
    fi
  done
  echo "MANIFEST-DIGEST $(sha256sum $OUT 2>/dev/null | cut -d' ' -f1)"
} > "$OUT"
sha256sum "$OUT" | cut -d' ' -f1
