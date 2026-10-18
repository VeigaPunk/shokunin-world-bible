#!/bin/bash
cd /home/vgpnk/Projects/shokunin/lore-shokunin
S=.ufo/waves/round-95/seats
echo "=== REPORT COUNT (maxdepth 1 .md) ==="
find $S -maxdepth 1 -name '*.md' -type f | wc -l
echo "=== REPORTS ==="
find $S -maxdepth 1 -name '*.md' -type f | sort | sed 's|.*/||'
echo "=== NON-MD ENTRIES ==="
find $S -maxdepth 1 ! -name '*.md' | sort | sed 's|.*/||'
echo "=== PRODUCER ARTIFACTS ==="
for p in corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json corpus/tools/README.md corpus/fixtures/r95-crossing-aftermath corpus/knowledge/r95-aftermath-scope-note.md; do
  if [ -e "$p" ]; then echo "PRESENT $p"; else echo "ABSENT  $p"; fi
done
echo "=== r95 fixture files ==="
ls corpus/fixtures/r95-crossing-aftermath/ 2>&1
