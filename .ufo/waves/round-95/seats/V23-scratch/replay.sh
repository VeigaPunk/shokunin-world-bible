#!/bin/bash
# V23 spot replays on r95-crossing-aftermath
cd /home/vgpnk/Projects/shokunin/lore-shokunin
echo "=== SPOT REPLAY 1: check_bible ==="
python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath; echo "exit=$?"
echo "=== SPOT REPLAY 2: map_obligations ==="
python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath; echo "exit=$?"
echo "=== counts ==="
python3 - <<'PY'
import json, pathlib
d = pathlib.Path('corpus/fixtures/r95-crossing-aftermath')
ents = json.loads((d/'entities.json').read_text()); rels = json.loads((d/'relations.json').read_text())
tl = json.loads((d/'timeline.json').read_text()); srcs = json.loads((d/'sources.json').read_text())
print('entities', len(ents), 'relations', len(rels), 'events', len(tl), 'sources', len(srcs))
print('timeline ids', [e['id'] for e in tl]); print('source ids', [s['id'] for s in srcs])
new = [e for e in tl if e['id']=='aftermath-missing-evin']
print('new event:', json.dumps(new))
PY
echo "=== inherited byte-copy check ==="
for f in entities.json relations.json contradictions.json inspiration-note.md source-excerpt.md; do
  if diff -q corpus/fixtures/r94-paired-crossing/$f corpus/fixtures/r95-crossing-aftermath/$f >/dev/null; then echo "$f BYTE_IDENTICAL"; else echo "$f DIFFERS"; fi
done
echo "=== inherited parsed-value check (timeline/sources) ==="
python3 - <<'PY'
import json, pathlib
a = pathlib.Path('corpus/fixtures/r94-paired-crossing'); b = pathlib.Path('corpus/fixtures/r95-crossing-aftermath')
for f, k in [('timeline.json',3),('sources.json',3)]:
    ja = json.loads((a/f).read_text()); jb = json.loads((b/f).read_text())
    same = ja == jb[:k]
    print(f, 'inherited_prefix_identical=', same, 'new_tail=', json.dumps(jb[k:])[:400])
PY
