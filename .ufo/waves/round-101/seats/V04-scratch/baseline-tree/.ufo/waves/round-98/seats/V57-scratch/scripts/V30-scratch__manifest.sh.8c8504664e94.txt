#!/bin/sh
cd /home/vgpnk/Projects/shokunin/lore-shokunin || exit 1
FILES="PROVINCE.md SHONEN.md SKILL.md README.md l0-questions.md
corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json corpus/tools/README.md
corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md
corpus/knowledge/r95-aftermath-scope-note.md corpus/knowledge/r96-response-scope-note.md corpus/knowledge/r97-acknowledgment-scope-note.md"
for f in corpus/fixtures/r98-clerk-filing/*; do FILES="$FILES $f"; done
if [ -f corpus/knowledge/r98-clerk-scope-note.md ]; then FILES="$FILES corpus/knowledge/r98-clerk-scope-note.md"; fi
sha256sum $FILES | sort -k2 | tee "$1"
echo "MANIFEST-DIGEST $(sha256sum "$1" | cut -d' ' -f1)"
