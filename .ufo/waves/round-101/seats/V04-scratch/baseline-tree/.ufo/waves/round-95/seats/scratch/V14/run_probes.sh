#!/usr/bin/env bash
# V14 c2-dependency-probe: four scratch-copy mutations of r95-crossing-aftermath.
# Live tree is never touched: every probe works on a copy under this scratch dir.
set -u
cd "$(dirname "$0")/../../../.."   # repo root
S=.ufo/waves/round-95/seats/scratch/V14
SRC=corpus/fixtures/r95-crossing-aftermath

echo "### baseline: live fixture check_bible"
python3 corpus/fixtures/check_bible.py "$SRC"; echo "exit=$?"

for p in a b c d; do
  rm -rf "$S/probe-$p"
  cp -r "$SRC" "$S/probe-$p"
done

python3 - <<'EOF'
import json, pathlib
S = pathlib.Path('.ufo/waves/round-95/seats/scratch/V14')
TARGET = 'aftermath-missing-evin'
DEP = 'paired-crossing-decision'

def load(p):
    return json.loads(p.read_text(encoding='utf-8'))

def save(p, rows):
    p.write_text(json.dumps(rows, indent=2) + '\n', encoding='utf-8')

# (a) drop paired-crossing-decision from the tick-11 event's depends_on
p = S / 'probe-a' / 'timeline.json'
rows = load(p)
hit = [r for r in rows if r['id'] == TARGET]
assert len(hit) == 1, hit
hit[0]['depends_on'] = [d for d in hit[0]['depends_on'] if d != DEP]
print('(a) aftermath depends_on ->', hit[0]['depends_on'])
save(p, rows)

# (b) point depends_on at an unknown id
p = S / 'probe-b' / 'timeline.json'
rows = load(p)
hit = [r for r in rows if r['id'] == TARGET]
hit[0]['depends_on'] = ['ghost-event-r95']
print('(b) aftermath depends_on ->', hit[0]['depends_on'])
save(p, rows)

# (c) set tick 9 on the aftermath event
p = S / 'probe-c' / 'timeline.json'
rows = load(p)
hit = [r for r in rows if r['id'] == TARGET]
hit[0]['tick'] = 9
print('(c) aftermath tick ->', hit[0]['tick'])
save(p, rows)

# (d) remove the tick-10 row
p = S / 'probe-d' / 'timeline.json'
rows = load(p)
before = [r['id'] for r in rows]
rows = [r for r in rows if r['id'] != DEP]
print('(d) removed', DEP, 'timeline ids', before, '->', [r['id'] for r in rows])
save(p, rows)
EOF

for p in a b c d; do
  echo "### probe-$p check_bible"
  python3 corpus/fixtures/check_bible.py "$S/probe-$p"
  echo "exit=$?"
done
