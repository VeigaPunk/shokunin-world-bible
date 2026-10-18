#!/bin/bash
# V28 rights/mechanics/adjacency language scan over r97 new/changed bytes
L=/home/vgpnk/Projects/shokunin/lore-shokunin
cd "$L" || exit 1
PAT='rights|licen[cs]e|copyright|permission|canon|mechanic|gameplay|ruleset|damage|stats|balancing|public domain|training|attribut'
echo "== A4.1 language scan: r97 fixture (all files) =="
grep -n -i -E "$PAT" corpus/fixtures/r97-crossing-acknowledgment/* 2>/dev/null
echo "== A4.2 language scan: r97 knowledge note =="
grep -n -i -E "$PAT" corpus/knowledge/r97-acknowledgment-scope-note.md 2>/dev/null
echo "== A4.3 sibling-lane / cross-province strings in new bytes =="
grep -n -i -E "kotodama|game-dev|art-east-asian|kengaku|mado|tabi|sibling|\.\./" corpus/fixtures/r97-crossing-acknowledgment/* corpus/knowledge/r97-acknowledgment-scope-note.md 2>/dev/null
echo "== A4.4 tool diffs vs baseline (language + scope) =="
git diff f3e09f9 -- corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json corpus/tools/README.md | grep -n -i -E "^\+.*($PAT|mechanic|gameplay)"
echo "== A4.5 r96 map repair diff (language) =="
git diff f3e09f9 -- corpus/fixtures/r96-crossing-response/claim-excerpt-map.md | grep -n -i -E "^\+.*($PAT)"
echo "== A4.6 external comparator bound in r97 JSON? =="
python3 - <<'PY'
import json, pathlib
d = pathlib.Path('/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r97-crossing-acknowledgment')
srcs = json.loads((d/'sources.json').read_text())
ids = [s.get('source_id') for s in (srcs if isinstance(srcs, list) else srcs.get('sources', []))]
print("declared source ids:", ids)
bound=set()
for name in ('entities.json','relations.json','timeline.json'):
    txt=(d/name).read_text()
    import re
    bound |= set(re.findall(r'"source_id"\s*:\s*"([^"]+)"', txt))
print("bound source ids  :", sorted(bound))
print("all bound in declared set:", bound <= set(ids))
for name in ('entities.json','relations.json','contradictions.json','sources.json','timeline.json'):
    txt=(d/name).read_text()
    hits=[w for w in ('Spence','Kojiki','Chamberlain','Gutenberg','ETCSL','Inana','Ovid','Maya','Kiche','K\'iche') if w.lower() in txt.lower()]
    if hits: print("EXTERNAL-NAME HIT", name, hits)
print("external-name scan done")
PY
