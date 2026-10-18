#!/usr/bin/env python3
"""V16 c3-dependency-probe harness (round 98): mutate one scratch copy of the delivered
fixture per probe, run corpus/fixtures/check_bible.py on the copy. Live fixture never touched."""
import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
CHECKER = REPO / 'corpus/fixtures/check_bible.py'


def run_checker(directory):
    proc = subprocess.run([sys.executable, str(CHECKER), str(directory)],
                          capture_output=True, text=True)
    return proc.returncode, proc.stdout.strip(), proc.stderr.strip()


def load_timeline(path):
    return json.loads(path.read_text(encoding='utf-8'))


def find(rows, event_id):
    for row in rows:
        if row.get('id') == event_id:
            return row
    raise SystemExit(f'event {event_id!r} not found')


def probes(event_id, dep_id):
    def p_baseline(tl):
        return None

    def p_drop_dep(tl):
        row = find(tl, event_id)
        del row['depends_on']

    def p_unknown_id(tl):
        find(tl, event_id)['depends_on'] = ['no-such-event-id']

    def p_tick13(tl):
        find(tl, event_id)['tick'] = 13

    def p_remove_ack(tl):
        tl[:] = [r for r in tl if r.get('id') != dep_id]

    def p_empty_dep(tl):
        find(tl, event_id)['depends_on'] = []

    def p_self_dep(tl):
        find(tl, event_id)['depends_on'] = [event_id]

    def p_repeat_dep(tl):
        find(tl, event_id)['depends_on'] = [dep_id, dep_id]

    def p_wrong_earlier_edge(tl):
        find(tl, event_id)['depends_on'] = ['response-evin-salt-court']

    def p_remove_clerk(tl):
        tl[:] = [r for r in tl if r.get('id') != event_id]

    def p_duplicate_clerk(tl):
        tl.append(dict(find(tl, event_id)))

    return [
        ('P0-baseline', 0, p_baseline),
        ('P1-drop-depends_on', 1, p_drop_dep),
        ('P2-unknown-id', 1, p_unknown_id),
        ('P3-tick13-inversion', 1, p_tick13),
        ('P4-remove-ack-event', 1, p_remove_ack),
        ('P5-empty-depends_on', 0, p_empty_dep),
        ('P6-self-dep', 1, p_self_dep),
        ('P7-repeated-dep', 1, p_repeat_dep),
        ('P8-wrong-earlier-edge', 0, p_wrong_earlier_edge),
        ('P9-remove-clerk-event', 0, p_remove_clerk),
        ('P10-duplicate-clerk-id', 1, p_duplicate_clerk),
    ]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('fixture', type=Path)
    ap.add_argument('--event', default='clerk-filing-open')
    ap.add_argument('--dep', default='acknowledgment-aru-records')
    ap.add_argument('--only', default=None)
    args = ap.parse_args()
    src = args.fixture.resolve()
    base = Path(tempfile.mkdtemp(prefix='v16-'))
    failures = 0
    for name, expected, mutate in probes(args.event, args.dep):
        if args.only and args.only not in name:
            continue
        copy_dir = base / name
        shutil.copytree(src, copy_dir)
        timeline_path = copy_dir / 'timeline.json'
        tl = load_timeline(timeline_path)
        mutate(tl)
        timeline_path.write_text(json.dumps(tl, indent=2) + '\n', encoding='utf-8')
        exit_code, out, err = run_checker(copy_dir)
        ok = exit_code == expected
        failures += 0 if ok else 1
        print(f'PROBE {name} exit={exit_code} expected={expected} ok={ok}')
        for line in out.splitlines():
            print(f'  OUT| {line}')
        if err:
            for line in err.splitlines():
                print(f'  ERR| {line}')
    shutil.rmtree(base, ignore_errors=True)
    print(f'RESULT {"PASS" if failures == 0 else "FAIL"} ({failures} unexpected)')
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
