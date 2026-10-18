#!/bin/bash
# V41 C2 verification (run from lane root)
set -u
S=.ufo/waves/round-96/seats/V41-scratch
F=corpus/fixtures/r96-crossing-response
R95=corpus/fixtures/r95-crossing-aftermath

echo "=== C2 counts: r95 vs r96 ==="
python3 - <<'EOF'
import json
for name,path in [('r95','corpus/fixtures/r95-crossing-aftermath'),('r96','corpus/fixtures/r96-crossing-response')]:
    row=[]
    for f in ['entities','relations','contradictions','sources','timeline']:
        d=json.load(open(f'{path}/{f}.json')); row.append(f'{f}={len(d)}')
    print(name, ' '.join(row))
r96=json.load(open('corpus/fixtures/r96-crossing-response/timeline.json'))
for ev in r96:
    print('  event:', json.dumps({k:ev.get(k) for k in ('event_id','tick','entity_id','place_id','depends_on','source_id')}))
EOF

echo "=== C2 byte-copy check (5 files) ==="
for f in entities.json relations.json contradictions.json inspiration-note.md source-excerpt.md; do
  if cmp -s "$R95/$f" "$F/$f"; then echo "BYTE-IDENTICAL $f"; else echo "DIFFERS $f"; fi
done
echo "=== C2 changed files ==="
for f in sources.json timeline.json fictional-excerpts.md; do
  if cmp -s "$R95/$f" "$F/$f"; then echo "unchanged $f"; else echo "CHANGED $f"; fi
done

echo "=== C2 inherited r95 map rows parsed-value identical (namespace column normalized) ==="
python3 - <<'EOF'
import re,pathlib
def rows(p):
    t=pathlib.Path(p).read_text().split('\n')
    out={}
    for l in t:
        m=re.match(r'^\|\s*(J\d+|P\d+)\s*\|(.*)$', l)
        if m: out[m.group(1)]=[c.strip() for c in m.group(2).split('|')]
    return out
def norm(cells):
    return [c for i,c in enumerate(cells) if i!=2]  # drop path-qualified namespace column (idx2 of split body)
r95=rows('corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md')
r96=rows('corpus/fixtures/r96-crossing-response/claim-excerpt-map.md')
print('r95 rows:',len(r95),'r96 rows:',len(r96))
common=[k for k in r95 if k in r96]
mism=[k for k in common if norm(r95[k])!=norm(r96[k])]
raw_mism=[k for k in common if r95[k]!=r96[k]]
print('common:',len(common),'normalized-mismatched:',mism,'raw-mismatched:',len(raw_mism))
print('new in r96:',[k for k in r96 if k not in r95])
print('J16 row:', r96.get('J16'))
EOF
echo "--- r96 declared inventory line ---"
grep -n "Expected inventory" corpus/fixtures/r96-crossing-response/claim-excerpt-map.md

echo "=== C2 map_obligations on r96 fixture ==="
python3 corpus/tools/map_obligations.py "$F"; echo "EXIT=$?"

echo "=== C2 check_bible ==="
python3 corpus/fixtures/check_bible.py "$F"; echo "EXIT=$?"

echo "=== C2 census ==="
echo "worktree dirs: $(find corpus/fixtures -mindepth 1 -maxdepth 1 -type d | wc -l)"
echo "HEAD dirs: $(git ls-tree -d --name-only HEAD:corpus/fixtures | wc -l)"

echo "=== C2 support_check on r96 fixture ==="
python3 corpus/tools/support_check.py "$F" 2>&1 | tail -8; echo "EXIT=${PIPESTATUS[0]}"

echo "=== C2 unresolved-account content check ==="
grep -n -i "accus\|winner\|blame\|contradict\|guilt" "$F/fictional-excerpts.md" "$F/README.md" "$F/claim-excerpt-map.md" 2>/dev/null | head -20
echo "--- sources ---"
python3 -c "
import json
for s in json.load(open('corpus/fixtures/r96-crossing-response/sources.json')): print(s)
"
