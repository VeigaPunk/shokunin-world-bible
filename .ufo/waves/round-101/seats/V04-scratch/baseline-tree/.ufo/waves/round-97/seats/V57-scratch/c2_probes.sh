#!/bin/bash
# V57 C2 probes — runs entirely inside V57-scratch (never writes producer-owned paths)
set -u
R=/home/vgpnk/Projects/shokunin/lore-shokunin
S=$R/.ufo/waves/round-97/seats/V57-scratch
P=$S/probe-r3
rm -rf $P
mkdir -p $P/corpus/tools $P/corpus/fixtures $P/foreign
cp $R/corpus/tools/dependency_freeze.py $P/corpus/tools/
cp $R/corpus/tools/dependency-freeze-contract.json $P/corpus/tools/
cp -r $R/corpus/fixtures/r96-crossing-response $P/corpus/fixtures/r96-crossing-response
cp -r $R/corpus/fixtures/r96-crossing-response $P/foreign/r96-crossing-response
T="$P/corpus/tools/dependency_freeze.py"
echo "== a) freeze ACCEPT under corpus/fixtures (scratch root) =="
python3 "$T" --freeze "$P/corpus/fixtures/r96-crossing-response"; echo "exit=$?"
echo "== b) verify pinned copy =="
python3 "$T" "$P/corpus/fixtures/r96-crossing-response"; echo "exit=$?"
echo "== c) tamper timeline.json -> DIGEST-MISMATCH naming file =="
python3 - <<'PY'
import pathlib
p=pathlib.Path('/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-97/seats/V57-scratch/probe-r3/corpus/fixtures/r96-crossing-response/timeline.json')
t=p.read_text(encoding='utf-8')
t=t.replace('Tick 11', 'Tick 1X', 1)
p.write_text(t, encoding='utf-8')
print('tampered timeline.json byte changed')
PY
python3 "$T" "$P/corpus/fixtures/r96-crossing-response"; echo "exit=$?"
echo "== d) scope guard: freeze a FOREIGN path (outside corpus/fixtures) =="
python3 "$T" --freeze "$P/foreign/r96-crossing-response"; echo "exit=$?"
echo "== e) path binding: verify foreign same-named copy =="
python3 "$T" "$P/foreign/r96-crossing-response"; echo "exit=$?"
echo "== f) pin label recorded by the guarded freeze =="
python3 -c "
import json
d=json.load(open('$P/corpus/tools/dependency-freeze-contract.json'))
p=d['pins']['r96-crossing-response']
print('fixture label:', p['fixture']); print('revision:', p['revision'])
"
