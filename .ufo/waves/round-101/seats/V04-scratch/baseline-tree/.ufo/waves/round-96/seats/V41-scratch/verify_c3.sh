#!/bin/bash
# V41 C3 verification (run from lane root). Mutated copies keep the pinned basename
# (r94-paired-crossing) inside a scratch parent so pin_for() resolves them.
set -u
S=.ufo/waves/round-96/seats/V41-scratch
T=corpus/tools/dependency_freeze.py

echo "=== C3 revision pins ==="
sha256sum $T corpus/tools/dependency-freeze-contract.json

echo "=== C3 self-test ==="
python3 $T --self-test > "$S/c3-selftest.out" 2>&1; echo "EXIT=$?"
echo "CASE ok lines: $(grep -c ' ok$' "$S/c3-selftest.out")  MISMATCH lines: $(grep -c 'MISMATCH' "$S/c3-selftest.out")"
grep -E "^SELF-TEST|^RESULT" "$S/c3-selftest.out"

echo "=== C3 clean chain (4 pinned fixtures) ==="
for d in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response; do
  echo "-- $d"; python3 $T "corpus/fixtures/$d"; echo "EXIT=$?"
done

mkvariant() { # $1=variant name, $2=python mutation snippet
  rm -rf "$S/mut/$1"; mkdir -p "$S/mut/$1"
  cp -r corpus/fixtures/r94-paired-crossing "$S/mut/$1/r94-paired-crossing"
  python3 - "$S/mut/$1/r94-paired-crossing/timeline.json" "$S/mut/$1/r94-paired-crossing/relations.json" <<EOF
import json,pathlib,sys
tl=pathlib.Path(sys.argv[1]); rel=pathlib.Path(sys.argv[2])
$2
EOF
}

echo "=== C3 BR-01 reduction (drop evin-ninth-bell from r94 tick-10 depends_on) ==="
mkvariant red "
d=json.loads(tl.read_text())
for ev in d:
    if ev['id']=='paired-crossing-decision': ev['depends_on']=[x for x in ev['depends_on'] if x!='evin-ninth-bell']
tl.write_text(json.dumps(d,indent=2)+'\n'); print('depends_on ->',[ev['depends_on'] for ev in d if ev['id']=='paired-crossing-decision'])"
python3 $T "$S/mut/red/r94-paired-crossing"; echo "EXIT=$?"

echo "=== C3 addition (phantom edge on evin-ninth-bell) ==="
mkvariant add "
d=json.loads(tl.read_text())
for ev in d:
    if ev['id']=='evin-ninth-bell': ev['depends_on']=['aru-ninth-bell']
tl.write_text(json.dumps(d,indent=2)+'\n'); print('added edge evin-ninth-bell -> aru-ninth-bell')"
python3 $T "$S/mut/add/r94-paired-crossing"; echo "EXIT=$?"

echo "=== C3 event endpoint change (place_id) ==="
mkvariant end "
d=json.loads(tl.read_text())
for ev in d:
    if ev['id']=='paired-crossing-decision': ev['place_id']='quiet-rise'
tl.write_text(json.dumps(d,indent=2)+'\n'); print('place_id chalk-stair -> quiet-rise')"
python3 $T "$S/mut/end/r94-paired-crossing"; echo "EXIT=$?"

echo "=== C3 relation endpoint flip ==="
mkvariant rel "
d=json.loads(rel.read_text()); d[0]['from'],d[0]['to']=d[0]['to'],d[0]['from']
rel.write_text(json.dumps(d,indent=2)+'\n'); print('relation flipped:',d[0])"
python3 $T "$S/mut/rel/r94-paired-crossing"; echo "EXIT=$?"

echo "=== C3 digest tamper (description edit, inventory-neutral) ==="
mkvariant dig "
d=json.loads(tl.read_text()); d[0]['description']=d[0]['description']+' (edited)'
tl.write_text(json.dumps(d,indent=2)+'\n'); print('description edited')"
python3 $T "$S/mut/dig/r94-paired-crossing"; echo "EXIT=$?"

echo "=== C3 event removed ==="
mkvariant evrm "
d=[ev for ev in json.loads(tl.read_text()) if ev['id']!='evin-ninth-bell']
tl.write_text(json.dumps(d,indent=2)+'\n'); print('event evin-ninth-bell removed')"
python3 $T "$S/mut/evrm/r94-paired-crossing"; echo "EXIT=$?"

echo "=== C3 could-not-evaluate: unpinned fixture / missing dir / bad args ==="
python3 $T corpus/fixtures/r93-m2-kojiki-cluster; echo "unpinned EXIT=$?"
python3 $T "$S/does-not-exist"; echo "missing EXIT=$?"
python3 $T; echo "no-arg EXIT=$?"
python3 $T --self-test corpus/fixtures/r94-paired-crossing; echo "self-test+fixture EXIT=$?"

echo "=== C3 --freeze exists (not used in admitted path) ==="
grep -n "\-\-freeze" $T | head -3

echo "=== C3 corpus untouched check ==="
git status --porcelain
