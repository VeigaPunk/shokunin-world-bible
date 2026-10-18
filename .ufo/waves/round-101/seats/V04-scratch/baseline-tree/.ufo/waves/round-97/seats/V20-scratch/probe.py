#!/usr/bin/env python3
"""V20 c3 dependency probes on a scratch copy of the r97 fixture.

Usage: python3 probe.py <scratch-fixture-dir>
Runs the delivered checker on mutated copies of timeline.json and prints
each mutation's exit code and checker output verbatim.
"""
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
CHECKER = REPO / 'corpus' / 'fixtures' / 'check_bible.py'
SRC = Path(sys.argv[1])

ACK = sys.argv[2] if len(sys.argv) > 2 else 'acknowledgment-aru-records'
RESP = sys.argv[3] if len(sys.argv) > 3 else 'response-evin-salt-court'


def run(tag, mutate):
    with tempfile.TemporaryDirectory() as td:
        dst = Path(td) / 'fixture'
        shutil.copytree(SRC, dst)
        tl_path = dst / 'timeline.json'
        rows = json.loads(tl_path.read_text(encoding='utf-8'))
        note = mutate(rows)
        tl_path.write_text(json.dumps(rows, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
        proc = subprocess.run([sys.executable, str(CHECKER), str(dst)],
                              capture_output=True, text=True)
        print(f'=== {tag} ===')
        print(f'mutation: {note}')
        print(f'exit={proc.returncode}')
        print(proc.stdout.rstrip())
        if proc.stderr.strip():
            print('STDERR:', proc.stderr.rstrip())
        print()


def find(rows, event_id):
    return next(r for r in rows if r['id'] == event_id)


def baseline(rows):
    return 'no mutation (baseline)'


def drop_dep(rows):
    ev = find(rows, ACK)
    del ev['depends_on']
    return f'dropped depends_on key from {ACK}'


def empty_dep(rows):
    find(rows, ACK)['depends_on'] = []
    return f'set {ACK}.depends_on = []'


def unknown_dep(rows):
    find(rows, ACK)['depends_on'] = ['no-such-event-id']
    return f'set {ACK}.depends_on = ["no-such-event-id"]'


def tick11(rows):
    ev = find(rows, ACK)
    ev['tick'] = 11
    return f'set {ACK}.tick = 11 (dependency {RESP} stays at tick 12)'


def remove_response(rows):
    rows[:] = [r for r in rows if r['id'] != RESP]
    return f'removed event {RESP}'


def self_dep(rows):
    find(rows, ACK)['depends_on'] = [ACK]
    return f'set {ACK}.depends_on = ["{ACK}"] (self dependency)'


def repeat_dep(rows):
    find(rows, ACK)['depends_on'] = [RESP, RESP]
    return f'set {ACK}.depends_on = ["{RESP}", "{RESP}"] (repeated dependency)'


def equal_tick(rows):
    ev = find(rows, ACK)
    ev['tick'] = find(rows, RESP)['tick']
    return f'set {ACK}.tick = {find(rows, RESP)["tick"]} (equal to dependency tick)'


run('P0 baseline', baseline)
run('P1 drop depends_on key', drop_dep)
run('P1b empty depends_on list (boundary control)', empty_dep)
run('P2 unknown dependency id', unknown_dep)
run('P3 tick 11 inversion', tick11)
run('P4 remove response event (dangling)', remove_response)
def wrong_earlier_dep(rows):
    find(rows, ACK)['depends_on'] = ['paired-crossing-decision']
    return f'set {ACK}.depends_on = ["paired-crossing-decision"] (earlier but semantically wrong edge)'


run('P5 self dependency', self_dep)
run('P6 repeated dependency', repeat_dep)
run('P7 equal tick (strict-order boundary)', equal_tick)
run('P8 earlier-but-wrong dependency edge (discrimination boundary)', wrong_earlier_dep)
