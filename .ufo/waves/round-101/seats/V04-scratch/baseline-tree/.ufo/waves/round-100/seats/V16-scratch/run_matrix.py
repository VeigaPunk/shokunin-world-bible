from concurrent.futures import ThreadPoolExecutor
from copy import deepcopy
from datetime import datetime
from hashlib import sha256
from pathlib import Path
import json
import re
import shlex
import subprocess

ROOT = Path('/home/vgpnk/Projects/shokunin/lore-shokunin').resolve()
SCRATCH = Path(__file__).resolve().parent
assert Path.cwd().resolve() == ROOT
assert SCRATCH == ROOT / '.ufo/waves/round-100/seats/V16-scratch'
OUT = SCRATCH / 'matrix'
assert not OUT.exists(), 'use a fresh output directory, never overwrite evidence'

FILES = ('entities.json', 'relations.json', 'timeline.json', 'sources.json',
         'contradictions.json', 'README.md', 'claim-excerpt-map.md',
         'fictional-excerpts.md', 'inspiration-note.md', 'source-excerpt.md')
TOOLS = {
    'bible': 'corpus/fixtures/check_bible.py',
    'support': 'corpus/tools/support_check.py',
    'map': 'corpus/tools/map_obligations.py',
    'freeze': 'corpus/tools/dependency_freeze.py',
}
CONTRACT = 'corpus/tools/dependency-freeze-contract.json'
FIXTURES = {'r100': 'r100-docket-review', 'r99': 'r99-window-lapse'}
CASES = ('control', 'm1-empty-deps', 'm2-wrong-earlier', 'm3-delete-terminal',
         'm4-span-break', 'm5-source-rebind', 'm6-coherent-prose')


def write_new(path, raw):
    path = path.resolve()
    assert path.is_relative_to(SCRATCH)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('xb') as handle:
        handle.write(raw)


def digest(raw):
    return sha256(raw).hexdigest()


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode()


def relative(path):
    return str(path.relative_to(ROOT))


seats = ROOT / '.ufo/waves/round-100/seats'
reports = {f'T{i}': sorted(relative(p) for p in seats.glob(f'T{i}*.md')
                         if p.is_file() and p.stat().st_size) for i in range(1, 5)}
assert all(reports.values()), reports
artifact_paths = ('corpus/knowledge/r100-crossing-arc-synthesis.md',
                  'corpus/knowledge/r100-provenance-semantics-boundary.md')
assert all((ROOT / path).is_file() for path in artifact_paths)
input_paths = list(TOOLS.values()) + [CONTRACT]
input_paths += [f'corpus/fixtures/{name}/{filename}'
                for name in FIXTURES.values() for filename in FILES]
input_paths += list(artifact_paths)
input_paths += [path for group in reports.values() for path in group]
original = {path: (ROOT / path).read_bytes() for path in input_paths}
manifest = {path: digest(raw) for path, raw in original.items()}
contract = json.loads(original[CONTRACT])
assert 'r99-window-lapse' in contract['pins']
assert 'r100-docket-review' not in contract['pins']
r100_timeline = json.loads(original['corpus/fixtures/r100-docket-review/timeline.json'])
assert len(r100_timeline) == 9
assert r100_timeline[-1]['id'] == 'clerk-review-first-passage'
assert r100_timeline[-1]['tick'] == 16
assert r100_timeline[-1]['depends_on'] == ['clerk-lapse-recorded']

metadata = {
    'observed_at': datetime.now().astimezone().isoformat(),
    'cwd': str(ROOT),
    'producer_reports': reports,
    'input_sha256': manifest,
    'pins': sorted(contract['pins']),
}
write_new(OUT / 'inputs.json', json_bytes(metadata))


def mutate(base, case):
    result = deepcopy(base)
    timeline = json.loads(result['timeline.json'])
    if case == 'm1-empty-deps':
        timeline[-1]['depends_on'] = []
    elif case == 'm2-wrong-earlier':
        timeline[-1]['depends_on'] = [timeline[-3]['id']]
    elif case == 'm3-delete-terminal':
        timeline.pop()
    elif case == 'm5-source-rebind':
        timeline[-1]['source_id'] = timeline[-2]['source_id']
    elif case == 'm4-span-break':
        text = result['claim-excerpt-map.md'].decode()
        rows = text.splitlines(keepends=True)
        indexes = [i for i, row in enumerate(rows) if row.startswith('| J05 |')]
        assert len(indexes) == 1
        index = indexes[0]
        old = rows[index]
        cells = [cell.strip() for cell in old.strip().strip('|').split('|')]
        assert cells[5] == '17', cells
        cells[5] = '20'
        rows[index] = '| ' + ' | '.join(cells) + ' |\n'
        result['claim-excerpt-map.md'] = ''.join(rows).encode()
    elif case == 'm6-coherent-prose':
        old = 'depends on both ninth-bell entries'
        new = 'follows both ninth-bell entries'
        for filename in ('claim-excerpt-map.md', 'fictional-excerpts.md'):
            text = result[filename].decode()
            assert text.count(old) == 1, (filename, text.count(old))
            result[filename] = text.replace(old, new).encode()
    elif case != 'control':
        raise AssertionError(case)
    if case in ('m1-empty-deps', 'm2-wrong-earlier', 'm3-delete-terminal',
                'm5-source-rebind'):
        result['timeline.json'] = json_bytes(timeline)
    return result


jobs = []
mutations = []
for fixture_label, fixture_name in FIXTURES.items():
    base = {filename: original[f'corpus/fixtures/{fixture_name}/{filename}']
            for filename in FILES}
    for case in CASES:
        mirror = OUT / fixture_label / case
        fixture = mirror / 'corpus/fixtures' / fixture_name
        mutated = mutate(base, case)
        for filename, raw in mutated.items():
            write_new(fixture / filename, raw)
        for tool_path in TOOLS.values():
            write_new(mirror / tool_path, original[tool_path])
        write_new(mirror / CONTRACT, original[CONTRACT])
        mutations.append({
            'fixture': fixture_label,
            'case': case,
            'path': relative(fixture),
            'changed_files': [name for name in FILES if base[name] != mutated[name]],
            'changed_sha256': {name: {'before': digest(base[name]), 'after': digest(mutated[name])}
                               for name in FILES if base[name] != mutated[name]},
        })
        for gate, tool_path in TOOLS.items():
            command = ['python3', relative(mirror / tool_path), relative(fixture)]
            jobs.append((fixture_label, case, gate, command))


def expected(fixture_label, case, gate):
    if gate == 'bible':
        return 0, set(), ('CLEAN: schema, citations, relations, timeline; 0 violations',)
    if gate == 'support':
        if case == 'm4-span-break':
            return 1, set(), ('FAIL: J05: anchor hit outside declared line span 20', 'RESULT FAIL')
        return 0, set(), ('RESULT PASS',)
    if gate == 'map':
        if case == 'm3-delete-terminal':
            return 1, {'phantom_obligation'}, ('RESULT FAIL',)
        if case == 'm5-source-rebind':
            return 1, {'source_id_mismatch'}, ('RESULT FAIL',)
        count = 22 if fixture_label == 'r100' else 21
        return 0, set(), (f'OBLIGATIONS raw={count} mapped={count}', 'RESULT PASS')
    if fixture_label == 'r100':
        return 2, {'UNPINNED-FIXTURE'}, ('RESULT ERROR',)
    if case == 'control':
        return 0, set(), ('FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1', 'RESULT PASS')
    if case in ('m1-empty-deps', 'm3-delete-terminal'):
        return 1, {'REDUCTION-DETECTED'}, ('RESULT FAIL',)
    if case == 'm2-wrong-earlier':
        return 1, {'ADDITION-DETECTED', 'REDUCTION-DETECTED'}, ('RESULT FAIL',)
    required_file = {'m4-span-break': 'claim-excerpt-map.md',
                     'm5-source-rebind': 'timeline.json',
                     'm6-coherent-prose': 'fictional-excerpts.md'}[case]
    return 2, {'DIGEST-MISMATCH'}, (required_file, 'RESULT ERROR')


def run(job):
    fixture_label, case, gate, command = job
    completed = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=60)
    output = completed.stdout + completed.stderr
    exit_code, finding_ids, fragments = expected(fixture_label, case, gate)
    observed_ids = set(re.findall(r'^FINDING ([A-Za-z0-9_-]+):', output, re.MULTILINE))
    match = (completed.returncode == exit_code and observed_ids == finding_ids
             and all((fragment in output.splitlines() if fragment.startswith('RESULT ')
                      else fragment in output) for fragment in fragments))
    record = {
        'fixture': fixture_label, 'case': case, 'gate': gate,
        'command': shlex.join(command), 'exit': completed.returncode,
        'finding_ids': sorted(observed_ids), 'expected_exit': exit_code,
        'expected_finding_ids': sorted(finding_ids), 'expected_fragments': fragments,
        'matches': match, 'stdout': completed.stdout, 'stderr': completed.stderr,
    }
    write_new(OUT / fixture_label / case / f'{gate}.stdout.txt', completed.stdout.encode())
    write_new(OUT / fixture_label / case / f'{gate}.stderr.txt', completed.stderr.encode())
    return record


with ThreadPoolExecutor(max_workers=8) as executor:
    results = list(executor.map(run, jobs))

remaining = {path: digest((ROOT / path).read_bytes()) for path in original}
drift = {path: {'before': manifest[path], 'after': remaining[path]}
         for path in manifest if manifest[path] != remaining[path]}
write_new(OUT / 'results.json', json_bytes({'metadata': metadata, 'mutations': mutations,
                                        'results': results, 'input_drift_during_run': drift}))
receipts = []
for result in results:
    receipts.append(f"## {result['fixture']} {result['case']} {result['gate']}\n")
    receipts.append('$ ' + result['command'] + '\n')
    receipts.append(result['stdout'])
    if result['stderr']:
        receipts.append('[stderr]\n' + result['stderr'])
    receipts.append(f"observed_exit={result['exit']} expected_match={result['matches']}\n\n")
write_new(OUT / 'commands.log', ''.join(receipts).encode())
for fixture_label in FIXTURES:
    for case in CASES:
        selected = [row for row in results if row['fixture'] == fixture_label and row['case'] == case]
        print(f"{fixture_label} {case}: " + '; '.join(
            f"{row['gate']}={row['exit']}[{','.join(row['finding_ids']) or '-'}]" for row in selected))
failed = [row for row in results if not row['matches']]
print(f'EXPECTED-MATCHES {len(results) - len(failed)}/{len(results)}')
print('INPUT-DRIFT ' + json.dumps(drift, sort_keys=True))
print('EVIDENCE ' + relative(OUT / 'results.json'))
for row in failed:
    print(json.dumps(row, ensure_ascii=False))
raise SystemExit(1 if failed or drift else 0)
