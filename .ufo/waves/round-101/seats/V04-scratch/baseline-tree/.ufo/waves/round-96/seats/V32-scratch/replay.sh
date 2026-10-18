#!/bin/bash
# V32 verdict-depth spot replays — run from lane root
set -u
echo "=== date ==="; date +%H:%M:%S
echo "=== sha256 of tools (revisions sampled) ==="
sha256sum corpus/fixtures/check_bible.py corpus/tools/map_obligations.py corpus/tools/support_check.py
echo "=== spot replay 1: check_bible r96 ==="
python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response; echo "exit=$?"
echo "=== spot replay 2: map_obligations r96 ==="
python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response; echo "exit=$?"
echo "=== companions: support_check r96 ==="
python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response; echo "exit=$?"
echo "=== r95 still CLEAN (untouched?) ==="
python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath; echo "exit=$?"
python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath; echo "exit=$?"
echo "=== counts r96 ==="
python3 - <<'PY'
import json
d='corpus/fixtures/r96-crossing-response/'
e=json.load(open(d+'entities.json')); r=json.load(open(d+'relations.json'))
c=json.load(open(d+'contradictions.json')); t=json.load(open(d+'timeline.json')); s=json.load(open(d+'sources.json'))
print('counts: entities %d relations %d events %d sources %d contradictions %d'%(len(e),len(r),len(t),len(s),len(c)))
print('timeline ids',[x['id'] for x in t])
print('source ids',[x['id'] for x in s])
PY
echo "=== preservation vs r95 ==="
cd corpus/fixtures
for f in entities.json relations.json contradictions.json inspiration-note.md source-excerpt.md; do
  if cmp -s r95-crossing-aftermath/$f r96-crossing-response/$f; then echo "IDENTICAL: $f"; else echo "DIFFER: $f"; fi
done
python3 - <<'PY'
import json
def load(p): return json.load(open(p))
a='r95-crossing-aftermath/'; b='r96-crossing-response/'
t95=load(a+'timeline.json'); t96=load(b+'timeline.json')
s95=load(a+'sources.json'); s96=load(b+'sources.json')
print('timeline r95 prefix == r96 prefix:', t96[:len(t95)]==t95)
print('sources  r95 prefix == r96 prefix:', s96[:len(s95)]==s95)
print('new event:', json.dumps(t96[-1], ensure_ascii=False))
print('new source:', json.dumps(s96[-1], ensure_ascii=False))
PY
echo "=== excerpt prefix ==="
python3 - <<'PY'
a=open('r95-crossing-aftermath/fictional-excerpts.md','rb').read()
b=open('r96-crossing-response/fictional-excerpts.md','rb').read()
print('r95 bytes',len(a),'r96 bytes',len(b),'prefix identical:', b[:len(a)]==a)
PY
echo "=== r95 dir git-clean vs baseline? ==="
cd ../..
git status --porcelain -- corpus/fixtures/r95-crossing-aftermath corpus/fixtures/r94-paired-crossing corpus/fixtures/r88-m3-maya-cluster | sed 's/^/  /'
echo "(empty above = untouched)"
echo "=== corpus-wide git status ==="
git status --porcelain | head -30
