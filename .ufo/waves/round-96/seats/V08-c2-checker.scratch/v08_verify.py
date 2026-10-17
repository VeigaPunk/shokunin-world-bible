#!/usr/bin/env python3
"""V08 c2-checker: independent re-derivation of the C2 claims for r96-crossing-response."""
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
FIX = ROOT / 'corpus/fixtures/r96-crossing-response'
R95 = ROOT / 'corpus/fixtures/r95-crossing-aftermath'
CB = ROOT / 'corpus/fixtures/check_bible.py'

fail = []


def load(p):
    return json.loads(Path(p).read_text(encoding='utf-8'))


def say(tag, msg):
    print(f'[{tag}] {msg}')


print('=== A. check_bible r96 ===')
proc = subprocess.run([sys.executable, str(CB), str(FIX)], capture_output=True, text=True)
print(f'$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response')
print(proc.stdout.strip())
print(proc.stderr.strip())
print(f'EXIT={proc.returncode}')
if proc.returncode != 0:
    fail.append(f'check_bible r96 exit {proc.returncode}')
if 'CLEAN' not in proc.stdout:
    fail.append('check_bible r96 not CLEAN')

print('=== B. check_bible r95 ===')
proc95 = subprocess.run([sys.executable, str(CB), str(R95)], capture_output=True, text=True)
print(proc95.stdout.strip())
print(f'EXIT={proc95.returncode}')
if proc95.returncode != 0:
    fail.append(f'check_bible r95 exit {proc95.returncode}')

print('=== C. table counts (json.load) ===')
ents = load(FIX / 'entities.json')
rels = load(FIX / 'relations.json')
tl = load(FIX / 'timeline.json')
srcs = load(FIX / 'sources.json')
contras = load(FIX / 'contradictions.json')
counts = {'entities': len(ents), 'relations': len(rels), 'events': len(tl),
          'sources': len(srcs), 'contradictions': len(contras)}
print(json.dumps(counts, indent=2))
want = {'entities': 5, 'relations': 1, 'events': 5, 'sources': 5}
for k, v in want.items():
    if counts[k] != v:
        fail.append(f'{k} count {counts[k]} != {v}')
print('entity ids:', [e['id'] for e in ents])
print('source ids:', [s['id'] for s in srcs])
print('event ids:', [t['id'] for t in tl])

print('=== D. new tick-12 response event ===')
by_id = {t['id']: t for t in tl}
ev = by_id.get('response-evin-salt-court')
if ev is None:
    fail.append('missing event response-evin-salt-court')
    print('MISSING response-evin-salt-court')
else:
    print(json.dumps(ev, indent=2, ensure_ascii=False))
    if ev.get('tick') != 12:
        fail.append(f"tick {ev.get('tick')} != 12")
    if ev.get('entity_id') != 'evin':
        fail.append(f"entity_id {ev.get('entity_id')} != evin")
    if ev.get('place_id') != 'salt-court':
        fail.append(f"place_id {ev.get('place_id')} != salt-court")
    if ev.get('depends_on') != ['aftermath-missing-evin']:
        fail.append(f"depends_on {ev.get('depends_on')} != ['aftermath-missing-evin']")

print('=== E. dangling / duplicate id sweep ===')
ent_ids = [e['id'] for e in ents]
src_ids = [s['id'] for s in srcs]
ev_ids = [t['id'] for t in tl]
for name, seq in (('entity', ent_ids), ('source', src_ids), ('event', ev_ids)):
    dups = [k for k, c in Counter(seq).items() if c > 1]
    if dups:
        fail.append(f'duplicate {name} ids: {dups}')
    print(f'{name} ids: {len(seq)} total, duplicates={dups}')
rel_ids = [f"{r['from']}->{r['to']}" for r in rels]
print('relation endpoints:', rel_ids)
for r in rels:
    for side in ('from', 'to'):
        if r[side] not in ent_ids:
            fail.append(f"relation {side} {r[side]!r} dangling")
    if r['source_id'] not in src_ids:
        fail.append(f"relation source_id {r['source_id']!r} dangling")
for e in ents:
    if e['first_appearance'] not in src_ids:
        fail.append(f"entity {e['id']} first_appearance {e['first_appearance']!r} dangling")
    for c in e['claims']:
        if c['source_id'] not in src_ids:
            fail.append(f"entity {e['id']} claim source_id {c['source_id']!r} dangling")
for t in tl:
    if t['entity_id'] not in ent_ids:
        fail.append(f"event {t['id']} entity_id {t['entity_id']!r} dangling")
    if t['place_id'] not in ent_ids:
        fail.append(f"event {t['id']} place_id {t['place_id']!r} dangling")
    if t['source_id'] not in src_ids:
        fail.append(f"event {t['id']} source_id {t['source_id']!r} dangling")
    for d in t['depends_on']:
        if d not in ev_ids:
            fail.append(f"event {t['id']} depends_on {d!r} dangling")
for c in contras:
    print('contradiction:', c.get('id'))
print('dangling sweep complete')

print('=== F. byte-copy fidelity vs r95 (5 declared copies) ===')
for name in ('entities.json', 'relations.json', 'contradictions.json',
             'inspiration-note.md', 'source-excerpt.md'):
    a = (R95 / name).read_bytes()
    b = (FIX / name).read_bytes()
    same = a == b
    print(f'{name}: identical={same} bytes {len(a)}/{len(b)}')
    if not same:
        fail.append(f'{name} is not a byte copy of r95')

print('=== G. r95 inherited rows parsed-value identical (sources 4 + events 4) ===')
src95 = {s['id']: s for s in load(R95 / 'sources.json')}
for sid, row in src95.items():
    if sid not in src_ids:
        fail.append(f'r95 source {sid} missing in r96')
    else:
        new = next(s for s in srcs if s['id'] == sid)
        if new != row:
            fail.append(f'r95 source {sid} parsed value changed')
tl95 = {t['id']: t for t in load(R95 / 'timeline.json')}
for tid, row in tl95.items():
    if tid not in by_id:
        fail.append(f'r95 event {tid} missing in r96')
    else:
        if by_id[tid] != row:
            fail.append(f'r95 event {tid} parsed value changed')
print(f'r95 sources present: {sorted(set(src95) & set(src_ids))}')
print(f'r95 events present: {sorted(set(tl95) & set(by_id))}')
print(f'sources added: {sorted(set(src_ids) - set(src95))}')
print(f'events added: {sorted(set(by_id) - set(tl95))}')

print('=== H. unresolved framing (no contradiction asserted) ===')
print(f'contradictions.json: {json.dumps(contras)}')
if contras:
    fail.append('contradictions not empty (C2 declares unresolved/no contradiction)')

print()
if fail:
    print('FAILURES:')
    for f in fail:
        print(' -', f)
    print(f'VERDICT: FAIL ({len(fail)} failure(s))')
    sys.exit(1)
print('VERDICT: PASS (all C2 checks)')
