#!/bin/bash
# V30 content-gated poll v2. 20s cadence, max 40 tries.
# READY when:
#   - timeline has clerk-lapse-recorded AND sources has clerk-lapse-note
#   - S3 report nonempty
#   - contract has >=1 pin whose files dict has >=10 entries (full-file pinning)
#     OR S1 report nonempty AND schema_version changed / md tamper case present
#   - r99-gate-blind-spot-table.md nonempty AND S5 report nonempty
# Producer reports required for the surfaces this seat covers.
set -u
LANE=/home/vgpnk/Projects/shokunin/lore-shokunin
SEATS=$LANE/.ufo/waves/round-99/seats
LOG=$SEATS/V30-scratch/poll.log
FIX=$LANE/corpus/fixtures/r99-window-lapse
CONTRACT=$LANE/corpus/tools/dependency-freeze-contract.json
TABLE=$LANE/corpus/knowledge/r99-gate-blind-spot-table.md
NOTE=$LANE/corpus/knowledge/r99-lapse-scope-note.md
: > "$LOG"
i=0
while [ "$i" -lt 40 ]; do
  i=$((i + 1))
  ts=$(date '+%Y-%m-%d %H:%M:%S %z')
  ev=0; srcnote=0
  s1=no; s3=no; s4=no; s5=no
  table=no; scope=no
  pins10=0; npins=0; schema=?; mdcase=no
  if [ -f "$FIX/timeline.json" ]; then ev=$(grep -c 'clerk-lapse-recorded' "$FIX/timeline.json" 2>/dev/null || true); fi
  if [ -f "$FIX/sources.json" ]; then srcnote=$(grep -c 'clerk-lapse-note' "$FIX/sources.json" 2>/dev/null || true); fi
  if [ -f "$CONTRACT" ]; then
    read -r schema npins pins10 mdcase < <(python3 - << 'PY'
import json
c=json.load(open("/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/tools/dependency-freeze-contract.json"))
pins=c.get("pins") or {}
n10=0
if isinstance(pins, dict):
    for v in pins.values():
        files=v.get("files") if isinstance(v, dict) else None
        if isinstance(files, dict) and len(files) >= 10:
            n10 += 1
        elif isinstance(files, list) and len(files) >= 10:
            n10 += 1
exp=c.get("self_test", {}).get("expected")
blob=json.dumps(exp).lower() if exp is not None else ""
md="yes" if ("markdown" in blob or "md_tamper" in blob or "readme" in blob and "tamper" in blob) else "no"
# also scan case ids
if isinstance(exp, dict):
    ids=" ".join(exp.keys()).lower()
    if any(x in ids for x in ("markdown", "md_tamper", "prose", "readme_tamper")):
        md="yes"
print(c.get("schema_version"), len(pins) if isinstance(pins, dict) else -1, n10, md)
PY
)
  fi
  nonempty() { local f; f=$(ls $SEATS/$1 2>/dev/null | head -1); [ -n "$f" ] && [ -s "$f" ]; }
  nonempty 'S1-*.md' && s1=yes
  nonempty 'S3-*.md' && s3=yes
  nonempty 'S4-*.md' && s4=yes
  nonempty 'S5-*.md' && s5=yes
  [ -s "$TABLE" ] && table=yes
  [ -s "$NOTE" ] && scope=yes
  seats_n=$(find "$SEATS" -maxdepth 1 -name '*.md' -type f | wc -l)
  echo "try=$i ts=$ts ev=$ev note=$srcnote schema=$schema npins=$npins pins10=$pins10 mdcase=$mdcase table=$table scope=$scope s1=$s1 s3=$s3 s4=$s4 s5=$s5 seats_md=$seats_n" | tee -a "$LOG"
  # content delivery of the surfaces this coverage seat must see
  if [ "$ev" -ge 1 ] && [ "$srcnote" -ge 1 ] && [ "$s3" = yes ] && [ "$pins10" -ge 1 ] && [ "$s1" = yes ] && [ "$table" = yes ] && [ "$s5" = yes ]; then
    echo "HIT try=$i ts=$ts" | tee -a "$LOG"
    exit 0
  fi
  if [ "$i" -ge 40 ]; then break; fi
  sleep 20
done
echo "ABSENT after $i tries ts=$(date '+%Y-%m-%d %H:%M:%S %z')" | tee -a "$LOG"
exit 1
