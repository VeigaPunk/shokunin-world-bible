#!/bin/bash
# V14 c2-dependency-probe driver: poll for Q4 fixture, then run probes on scratch copies.
ROOT=/home/vgpnk/Projects/shokunin/lore-shokunin
FIX=$ROOT/corpus/fixtures/r96-crossing-response
SEATS=$ROOT/.ufo/waves/round-96/seats
SCRATCH=$SEATS/V14-scratch
CHECK=$ROOT/corpus/fixtures/check_bible.py
LOG=$SCRATCH/driver.log
: > "$LOG"

need_files=(entities.json relations.json contradictions.json inspiration-note.md source-excerpt.md sources.json timeline.json fictional-excerpts.md)

found=0
for i in $(seq 1 40); do
  ok=1
  for f in "${need_files[@]}"; do
    [ -f "$FIX/$f" ] || { ok=0; break; }
  done
  q4report=$(ls "$SEATS"/Q4*.md 2>/dev/null | head -1)
  if [ "$ok" = 1 ] && [ -n "$q4report" ]; then
    echo "FOUND at try $i ($(date -u +%FT%TZ)); Q4 report: $q4report" >> "$LOG"
    found=1; break
  fi
  echo "try $i: absent (ok=$ok q4report=${q4report:-none}) $(date -u +%FT%TZ)" >> "$LOG"
  sleep 20
done
if [ "$found" != 1 ]; then
  echo "ABSENT after 40 tries" >> "$LOG"
  exit 3
fi

# provenance digests of the delivered fixture
echo "== provenance: sha256 of delivered fixture files ==" >> "$LOG"
( cd "$FIX" && sha256sum "${need_files[@]}" ) >> "$LOG" 2>&1

# counts
echo "== counts ==" >> "$LOG"
python3 - "$FIX" >> "$LOG" 2>&1 <<'PY'
import json,sys,pathlib
d=pathlib.Path(sys.argv[1])
for sec in ("entities","relations","timeline","sources","contradictions"):
    rows=json.loads((d/f"{sec}.json").read_text())
    print(f"{sec}: {len(rows)} rows")
PY

# control: pristine copy
CTRL=$SCRATCH/ctrl-pristine
rm -rf "$CTRL"; cp -r "$FIX" "$CTRL"
echo "+ python3 corpus/fixtures/check_bible.py $CTRL" >> "$LOG"
python3 "$CHECK" "$CTRL" >> "$LOG" 2>&1
echo "exit=$?" >> "$LOG"

mutate() { # $1=mode $2=destname
  local mode=$1 dest=$SCRATCH/$2
  rm -rf "$dest"; cp -r "$FIX" "$dest"
  python3 - "$dest/timeline.json" "$mode" >> "$LOG" 2>&1 <<'PY'
import json,sys,pathlib
p=pathlib.Path(sys.argv[1]); mode=sys.argv[2]
rows=json.loads(p.read_text())
resp=[r for r in rows if isinstance(r,dict) and r.get('id')=='response-evin-salt-court']
if len(resp)!=1:
    print(f"MUTATION-SETUP-FAIL: expected exactly 1 'response-evin-salt-court', found {len(resp)}")
    sys.exit(9)
r=resp[0]
if mode=='drop_key':
    r.pop('depends_on',None)
elif mode=='empty_deps':
    r['depends_on']=[]
elif mode=='unknown_dep':
    r['depends_on']=['aftermath-missing-evin-missing']
elif mode=='tick11':
    r['tick']=11
elif mode=='remove_aftermath':
    rows=[x for x in rows if x.get('id')!='aftermath-missing-evin']
else:
    print("MUTATION-SETUP-FAIL: unknown mode", mode); sys.exit(9)
p.write_text(json.dumps(rows,indent=2,ensure_ascii=False)+"\n")
print(f"MUTATION-OK mode={mode}")
PY
}

for m in drop_key empty_deps unknown_dep tick11 remove_aftermath; do
  mutate "$m" "probe-$m"
  echo "+ python3 corpus/fixtures/check_bible.py $SCRATCH/probe-$m" >> "$LOG"
  python3 "$CHECK" "$SCRATCH/probe-$m" >> "$LOG" 2>&1
  echo "exit=$?" >> "$LOG"
done
echo "DONE" >> "$LOG"
