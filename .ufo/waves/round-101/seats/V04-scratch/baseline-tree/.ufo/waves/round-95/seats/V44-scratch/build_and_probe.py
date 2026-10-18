#!/usr/bin/env python3
"""V44 exit-contract-c2: transplant r13/r16/r17/r19/r20 edge classes onto
scratch copies of the delivered corpus/fixtures/r95-crossing-aftermath fixture
and check the prior calibration semantics reproduce.

Read-only wrt the corpus: copies go under V44-scratch/probes/.
"""
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
SRC = Path(os.environ.get('V44_SRC', str(REPO / 'corpus/fixtures/r95-crossing-aftermath')))
SCR = REPO / '.ufo/waves/round-95/seats/V44-scratch'
PROBES = SCR / os.environ.get('V44_PROBEDIR', 'probes')
LOGS = SCR / os.environ.get('V44_LOGDIR', 'logs')
CHECKER = REPO / 'corpus/fixtures/check_bible.py'


def event(eid, tick, entity, place, deps, source='paired-clock'):
    return {
        'id': eid, 'tick': tick, 'entity_id': entity, 'place_id': place,
        'depends_on': deps,
        'description': f'V44 exit-contract probe row {eid}; input-structural only, no canon assertion.',
        'source_id': source,
    }


# name -> (appended timeline rows, class label)
MUTATIONS = {
    'neg-tick': ([
        event('v44-neg-a', -1, 'aru', 'quiet-rise', []),
        event('v44-neg-b', -1, 'aru', 'salt-court', []),
    ], 'r19-negative-tick: same unique actor, two valid places, tick -1'),
    'neg-dep': ([
        event('v44-neg-prereq', -2, 'aru', 'quiet-rise', []),
        event('v44-neg-dependent', -1, 'aru', 'salt-court', ['v44-neg-prereq']),
    ], 'r20-both-negative: dependent tick -1 depends_on prereq tick -2'),
    'missing-actor': ([
        event('v44-ghost-a', 12, 'unlisted', 'quiet-rise', []),
        event('v44-ghost-b', 12, 'unlisted', 'salt-court', []),
    ], 'r13-missing-actor: absent actor id at one tick, two valid places'),
    'missing-place': ([
        event('v44-noplace-a', 14, 'aru', 'unlisted-place', []),
        event('v44-noplace-b', 14, 'aru', 'quiet-rise', []),
    ], 'r16-missing-place: absent place id plus one valid place, same tick/actor'),
    'wrong-kind': ([
        event('v44-wrong-a', 13, 'aru', 'evin', []),
        event('v44-wrong-b', 13, 'aru', 'quiet-rise', []),
        event('v44-wrong-c', 13, 'aru', 'salt-court', []),
    ], "r17-wrong-first: place_id 'evin' is a character, then two valid places at the same tick"),
}


def run_checker(directory):
    proc = subprocess.run(
        [sys.executable, str(CHECKER), str(directory)],
        capture_output=True, text=True, cwd=str(REPO),
    )
    return proc.stdout, proc.stderr, proc.returncode


def violation_lines(stdout):
    return [ln for ln in stdout.splitlines() if ln.startswith('VIOLATION:')]


def check_expectations(name, lines):
    """Return list of (ok, note) for the class expectations."""
    checks = []
    if name == 'neg-tick':
        checks.append((len(lines) == 2 and all('must be nonnegative' in ln for ln in lines),
                       'exactly 2 must-be-nonnegative lines'))
        checks.append((not any('double-booked' in ln for ln in lines),
                       'no double-booked for tick -1 occupancy'))
    elif name == 'neg-dep':
        checks.append((len(lines) == 2 and all('must be nonnegative' in ln for ln in lines),
                       'exactly 2 must-be-nonnegative lines'))
        checks.append((not any('inversion' in ln for ln in lines),
                       'no timeline inversion across negative ticks'))
    elif name == 'missing-actor':
        checks.append((len(lines) == 2 and all("dangling entity 'unlisted'" in ln for ln in lines),
                       'exactly 2 dangling-actor lines'))
        checks.append((not any('double-booked' in ln for ln in lines),
                       'no double-booked for missing actor'))
    elif name == 'missing-place':
        checks.append((len(lines) == 1 and "dangling entity 'unlisted-place'" in lines[0],
                       'exactly 1 dangling-place line'))
        checks.append((not any('double-booked' in ln for ln in lines),
                       'no double-booked when a place id is missing'))
    elif name == 'wrong-kind':
        checks.append((sum("not a place 'evin'" in ln for ln in lines) == 1,
                       "one not-a-place line for 'evin'"))
        db = [ln for ln in lines if 'double-booked' in ln]
        checks.append((len(db) == 1 and "'aru'" in db[0] and 'tick 13' in db[0]
                       and "'quiet-rise'" in db[0] and "'salt-court'" in db[0]
                       and 'evin' not in db[0],
                       'one double-booked between the two valid places, wrong-kind excluded'))
        checks.append((len(lines) == 2, 'exactly 2 violation lines total'))
    return checks


def main():
    LOGS.mkdir(parents=True, exist_ok=True)
    PROBES.mkdir(parents=True, exist_ok=True)
    summary = []
    # Control: unmutated copy of the delivered fixture.
    control = PROBES / 'control'
    if control.exists():
        shutil.rmtree(control)
    shutil.copytree(SRC, control)
    out, err, code = run_checker(control)
    (LOGS / 'control.stdout.txt').write_text(out)
    (LOGS / 'control.stderr.txt').write_text(err)
    summary.append({'probe': 'control', 'exit': code, 'lines': violation_lines(out),
                    'checks': [(code == 0 and 'CLEAN' in out, 'unmutated delivered fixture is CLEAN exit 0')]})
    for name, (rows, label) in MUTATIONS.items():
        dest = PROBES / name
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(SRC, dest)
        timeline_path = dest / 'timeline.json'
        rows_json = json.loads(timeline_path.read_text(encoding='utf-8'))
        rows_json.extend(rows)
        timeline_path.write_text(json.dumps(rows_json, indent=2) + '\n', encoding='utf-8')
        out, err, code = run_checker(dest)
        (LOGS / f'{name}.stdout.txt').write_text(out)
        (LOGS / f'{name}.stderr.txt').write_text(err)
        lines = violation_lines(out)
        checks = check_expectations(name, lines)
        summary.append({'probe': name, 'class': label, 'exit': code, 'lines': lines,
                        'checks': checks})
    (LOGS / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    all_ok = True
    for item in summary:
        ok = all(c[0] for c in item['checks'])
        all_ok = all_ok and ok
        print(f"== {item['probe']} exit={item['exit']} {'PASS' if ok else 'FAIL'}")
        for ln in item['lines']:
            print('   ', ln)
        for c_ok, note in item['checks']:
            print(f"    check {'ok' if c_ok else 'FAILED'}: {note}")
    print('ALL_OK' if all_ok else 'SOME_FAILED')
    return 0 if all_ok else 1


if __name__ == '__main__':
    raise SystemExit(main())
