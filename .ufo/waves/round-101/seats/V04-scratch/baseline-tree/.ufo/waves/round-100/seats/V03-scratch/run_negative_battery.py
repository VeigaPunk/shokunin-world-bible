from concurrent.futures import ThreadPoolExecutor
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import os
import shlex
import shutil
import subprocess

LANE = Path('/home/vgpnk/Projects/shokunin/lore-shokunin').resolve()
SCRATCH = (LANE / '.ufo/waves/round-100/seats/V03-scratch').resolve()
NAME = 'r99-window-lapse'
OTHER = 'r93-m2-kojiki-cluster'
SELF_BASE = 'r95-crossing-aftermath'
TOOL = Path('corpus/tools/dependency_freeze.py')
CONTRACT = Path('corpus/tools/dependency-freeze-contract.json')
FILES = ('entities.json', 'relations.json', 'timeline.json', 'sources.json',
         'contradictions.json', 'README.md', 'claim-excerpt-map.md',
         'fictional-excerpts.md', 'inspiration-note.md', 'source-excerpt.md')
assert Path.cwd().resolve() == LANE
assert SCRATCH.is_relative_to(LANE / '.ufo/waves/round-100/seats')


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def new_bytes(path, raw):
    path = path.resolve()
    assert path.is_relative_to(SCRATCH), path
    assert not path.exists(), path
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('xb') as handle:
        handle.write(raw)


def new_json(path, obj):
    new_bytes(path, (json.dumps(obj, indent=2, ensure_ascii=False) + '\n').encode())


def inventory(paths):
    return {str(path.relative_to(LANE)): sha(path.read_bytes()) for path in paths}


reports = sorted((LANE / '.ufo/waves/round-100/seats').glob('T1*.md'))
assert reports, 'T1 report absent'
contract_raw = (LANE / CONTRACT).read_bytes()
contract = json.loads(contract_raw)
assert NAME in contract['pins'], 'r99 pin absent'
assert len(contract['pins']) == 7, 'chain is not seven fixtures'
assert all((LANE / 'corpus/fixtures' / NAME / item).is_file() for item in FILES)
for rel in ('corpus/tools/README.md', 'SKILL.md'):
    text = (LANE / rel).read_text()
    assert any(marker in text for marker in ('Round-100', 'r100', 'round 100')), rel

tracked_inputs = [LANE / TOOL, LANE / CONTRACT]
tracked_inputs += [LANE / 'corpus/fixtures' / name / item
                   for name in (NAME, SELF_BASE) for item in FILES]
tracked_inputs += [p for p in (LANE / 'corpus/fixtures' / OTHER).iterdir() if p.is_file()]
before = inventory(tracked_inputs)
snapshot = SCRATCH / 'snapshot'
new_bytes(snapshot / TOOL, (LANE / TOOL).read_bytes())
new_bytes(snapshot / CONTRACT, contract_raw)
for name in (NAME, SELF_BASE, OTHER):
    source = LANE / 'corpus/fixtures' / name
    for path in source.iterdir():
        if path.is_file():
            new_bytes(snapshot / 'corpus/fixtures' / name / path.name, path.read_bytes())
fixture_bytes = {path.name: path.read_bytes()
                 for path in (snapshot / 'corpus/fixtures' / NAME).iterdir() if path.is_file()}
tool_bytes = (snapshot / TOOL).read_bytes()

cases = []


def add(case_id, exit_code, ids, mutation=None, *, mode='verify', names_file=None):
    cases.append({'case_id': case_id, 'expected_exit': exit_code,
                  'expected_ids': sorted(ids), 'mutation': mutation,
                  'mode': mode, 'names_file': names_file})


def rewrite(files, name, change):
    value = json.loads(files[name])
    changed = change(value)
    files[name] = (json.dumps(value if changed is None else changed,
                              indent=2, ensure_ascii=False) + '\n').encode()


def event(files, event_id, change):
    def apply(rows):
        change(next(row for row in rows if row['id'] == event_id))
    rewrite(files, 'timeline.json', apply)


def modify_event(event_id, key, value):
    return lambda files, pin: event(files, event_id, lambda row: row.__setitem__(key, value))


def relation(files, index, change):
    def apply(rows):
        change(rows[index])
    rewrite(files, 'relations.json', apply)


add('clean_r99', 0, [])
add('semantic_drop_tick15_edge', 1, ['REDUCTION-DETECTED'],
    modify_event('clerk-lapse-recorded', 'depends_on', []))
add('semantic_add_tick15_edge', 1, ['ADDITION-DETECTED'],
    modify_event('clerk-lapse-recorded', 'depends_on', ['clerk-filing-open', 'v03-phantom']))
add('semantic_remove_tick15_event', 1, ['REDUCTION-DETECTED'],
    lambda f, c: rewrite(f, 'timeline.json', lambda rows: [r for r in rows if r['id'] != 'clerk-lapse-recorded']))
add('semantic_add_event_with_dependency', 1, ['ADDITION-DETECTED'],
    lambda f, c: rewrite(f, 'timeline.json', lambda rows: rows.append({
        'id': 'v03-added-event', 'tick': 16, 'entity_id': 'clerk-maren',
        'place_id': 'chalk-stair', 'depends_on': ['clerk-lapse-recorded']})))
for key, value in (('tick', 150), ('entity_id', 'aru'), ('place_id', 'salt-court')):
    add('semantic_event_endpoint_' + key, 1, ['ENDPOINT-CHANGE'],
        modify_event('clerk-lapse-recorded', key, value))
add('semantic_relation_endpoint_flip', 1, ['ENDPOINT-CHANGE'],
    lambda f, c: relation(f, 0, lambda row: row.update({'from': 'evin', 'to': 'aru'})))
add('semantic_relation_remove', 1, ['REDUCTION-DETECTED'],
    lambda f, c: rewrite(f, 'relations.json', lambda rows: []))
add('semantic_relation_add', 1, ['ADDITION-DETECTED'],
    lambda f, c: rewrite(f, 'relations.json', lambda rows: rows.append({
        'from': 'aru', 'to': 'clerk-maren', 'type': 'v03-unpinned'})))


def mixed(files, pin):
    event(files, 'clerk-lapse-recorded', lambda row: row.__setitem__('depends_on', []))
    files['fictional-excerpts.md'] += b'\nV03 byte-change probe.\n'


add('semantic_precedes_digest', 1, ['REDUCTION-DETECTED'], mixed)
for filename in FILES:
    add('digest_newline_' + filename, 2, ['DIGEST-MISMATCH'],
        lambda f, c, name=filename: f.__setitem__(name, f[name] + b'\n'), names_file=filename)
for filename in FILES:
    required = filename in ('timeline.json', 'relations.json')
    add('missing_' + filename, 2, ['FILE-MISSING' if required else 'DIGEST-MISMATCH'],
        lambda f, c, name=filename: f.pop(name), names_file=filename)
for case_id, filename, raw in (
        ('malformed_json_syntax', 'timeline.json', b'[{\n'),
        ('malformed_json_utf8', 'timeline.json', b'\xff'),
        ('malformed_json_sources', 'sources.json', b'{v03-invalid\n')):
    add(case_id, 2, ['MALFORMED-JSON'], lambda f, c, n=filename, r=raw: f.__setitem__(n, r))
for name in ('timeline.json', 'relations.json'):
    add('malformed_model_object_' + name, 2, ['MALFORMED-MODEL'],
        lambda f, c, n=name: f.__setitem__(n, b'{}\n'))
add('malformed_model_empty_event_id', 2, ['MALFORMED-MODEL'],
    modify_event('clerk-lapse-recorded', 'id', ''))
add('malformed_model_duplicate_event_id', 2, ['MALFORMED-MODEL'],
    modify_event('clerk-lapse-recorded', 'id', 'clerk-filing-open'))
add('malformed_model_dep_not_list', 2, ['MALFORMED-MODEL'],
    modify_event('clerk-lapse-recorded', 'depends_on', 'clerk-filing-open'))
add('malformed_model_empty_dep', 2, ['MALFORMED-MODEL'],
    modify_event('clerk-lapse-recorded', 'depends_on', ['']))
add('malformed_model_nonscalar_endpoint', 2, ['MALFORMED-MODEL'],
    modify_event('clerk-lapse-recorded', 'tick', [15]))
add('malformed_model_relation_from_missing', 2, ['MALFORMED-MODEL'],
    lambda f, c: relation(f, 0, lambda row: row.pop('from')))
add('unpinned_real_nonchain_r93', 2, ['UNPINNED-FIXTURE'], mode='unpinned')
add('missing_known_fixture', 2, ['FIXTURE-MISSING'], mode='fixture_missing')
add('same_name_foreign_path', 2, ['PATH-MISMATCH'], mode='foreign')
add('contract_absent', 2, ['CONTRACT-INVALID'], mode='contract_absent')
add('contract_malformed_json', 2, ['CONTRACT-INVALID'], mode='contract_malformed')
add('contract_root_not_object', 2, ['CONTRACT-INVALID'], mode='contract_list')
for case_id, mutation in (
        ('contract_pin_not_object', lambda c: c['pins'].__setitem__(NAME, [])),
        ('contract_pin_fixture_absent', lambda c: c['pins'][NAME].pop('fixture')),
        ('contract_pin_fixture_absolute', lambda c: c['pins'][NAME].__setitem__('fixture', '/v03/invalid')),
        ('contract_pin_fixture_outside_scope', lambda c: c['pins'][NAME].__setitem__('fixture', 'corpus/tools/v03')),
        ('contract_pin_payload_schema_1', lambda c: c['pins'][NAME].__setitem__('payload_schema_version', 1)),
        ('contract_pin_pinned_files_short', lambda c: c['pins'][NAME]['pinned_files'].pop()),
        ('contract_pin_content_digest_bad', lambda c: c['pins'][NAME].__setitem__('content_sha256', 'bad')),
        ('contract_pin_file_digest_absent', lambda c: c['pins'][NAME]['files'].pop('README.md')),
        ('contract_pin_events_not_object', lambda c: c['pins'][NAME].__setitem__('events', [])),
        ('contract_pin_event_entry_invalid', lambda c: c['pins'][NAME]['events'].__setitem__('v03', {})),
        ('contract_pin_relations_invalid', lambda c: c['pins'][NAME].__setitem__('relations', [['aru']]))):
    add(case_id, 2, ['CONTRACT-INVALID'], lambda f, c, mutate=mutation: mutate(c))
add('freeze_foreign_scope', 2, ['SCOPE-REFUSED'], mode='freeze_foreign')
add('freeze_scope_root', 2, ['SCOPE-REFUSED'], mode='freeze_scope_root')
add('freeze_same_name_other_in_scope', 2, ['SCOPE-REFUSED'], mode='freeze_collision')
add('freeze_missing_pinned_markdown', 2, ['FILE-MISSING'],
    lambda f, c: f.pop('README.md'), mode='freeze', names_file='README.md')
for mode in ('args_none', 'args_combined_verify_freeze', 'args_selftest_fixture',
             'args_selftest_freeze', 'args_unknown_flag'):
    add(mode, 2, ['INVALID-ARGUMENTS'], mode=mode)
add('selftest_clean_control', 0, [], mode='selftest')
add('selftest_expectation_flip', 2, ['SELF-TEST-MISMATCH'],
    lambda f, c: c['self_test']['expected']['clean'].__setitem__('exit', 1), mode='selftest')
add('selftest_expected_case_missing', 2, ['CONTRACT-INVALID'],
    lambda f, c: c['self_test']['expected'].pop('markdown_tamper'), mode='selftest')
add('selftest_expected_case_extra', 2, ['CONTRACT-INVALID'],
    lambda f, c: c['self_test']['expected'].__setitem__('v03-extra', {'exit': 0}), mode='selftest')

manifest = {
    'timestamp_utc': datetime.now(timezone.utc).isoformat(),
    'head': subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=LANE, text=True, capture_output=True, check=True).stdout.strip(),
    'producer_reports': {str(p.relative_to(LANE)): sha(p.read_bytes()) for p in reports},
    'documentation': {rel: sha((LANE / rel).read_bytes()) for rel in ('corpus/tools/README.md', 'SKILL.md')},
    'input_sha256': before,
    'pins': sorted(contract['pins']),
    'case_count': len(cases),
    'repeat_count': 2,
    'workers': 8,
    'scope': 'all subprocesses have cwd=lane root; tools, contracts, and fixtures are isolated scratch mirrors',
}
new_json(SCRATCH / 'manifest.json', manifest)


def create_case(spec):
    case_root = SCRATCH / 'cases' / spec['case_id']
    files = deepcopy(fixture_bytes)
    pin = deepcopy(contract)
    if spec['mutation']:
        spec['mutation'](files, pin)
    mode = spec['mode']
    fixture = case_root / 'corpus/fixtures' / NAME
    new_bytes(case_root / TOOL, tool_bytes)
    if mode != 'contract_absent':
        raw = b'{\n' if mode == 'contract_malformed' else b'[]\n' if mode == 'contract_list' else (
            json.dumps(pin, indent=2, ensure_ascii=False) + '\n').encode()
        new_bytes(case_root / CONTRACT, raw)
    if mode in ('foreign', 'freeze_foreign'):
        fixture = case_root / 'foreign' / NAME
    elif mode == 'freeze_collision':
        fixture = case_root / 'corpus/fixtures/nested' / NAME
    if mode != 'fixture_missing':
        for name, raw in files.items():
            new_bytes(fixture / name, raw)
    if mode == 'unpinned':
        fixture = case_root / 'corpus/fixtures' / OTHER
        for source in (snapshot / 'corpus/fixtures' / OTHER).iterdir():
            if source.is_file():
                new_bytes(fixture / source.name, source.read_bytes())
    if mode == 'selftest':
        for source in (snapshot / 'corpus/fixtures' / SELF_BASE).iterdir():
            if source.is_file():
                new_bytes(case_root / 'corpus/fixtures' / SELF_BASE / source.name, source.read_bytes())
    command = ['python3', str(case_root / TOOL)]
    if mode.startswith('freeze'):
        target = case_root / 'corpus/fixtures' if mode == 'freeze_scope_root' else fixture
        command += ['--freeze', str(target)]
    elif mode == 'selftest':
        command += ['--self-test']
    elif mode == 'args_none':
        pass
    elif mode == 'args_combined_verify_freeze':
        command += [str(fixture), '--freeze', str(fixture)]
    elif mode == 'args_selftest_fixture':
        command += ['--self-test', str(fixture)]
    elif mode == 'args_selftest_freeze':
        command += ['--self-test', '--freeze', str(fixture)]
    elif mode == 'args_unknown_flag':
        command += ['--v03-unknown-option']
    else:
        command += [str(fixture)]
    return case_root, command


prepared = [(spec, *create_case(spec)) for spec in cases]


def run_case(item):
    spec, case_root, command = item
    runs = []
    contract_path = case_root / CONTRACT
    before_contract = sha(contract_path.read_bytes()) if contract_path.exists() else None
    for repeat in (1, 2):
        env = {**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'}
        env.pop('DEPENDENCY_FREEZE_SELF_TEST_CHILD', None)
        completed = subprocess.run(command, cwd=LANE, capture_output=True, text=True, env=env, timeout=120)
        ids = sorted(line.split(':', 1)[0].split(' ', 1)[1]
                     for line in completed.stdout.splitlines() if line.startswith('FINDING '))
        results = [line for line in completed.stdout.splitlines() if line.startswith('RESULT ')]
        wanted_result = {0: 'RESULT PASS', 1: 'RESULT FAIL', 2: 'RESULT ERROR'}[spec['expected_exit']]
        expected_matches = (completed.returncode == spec['expected_exit']
                            and ids == spec['expected_ids'] and results == [wanted_result]
                            and 'Traceback' not in completed.stdout + completed.stderr
                            and not completed.stderr
                            and (not spec['names_file'] or spec['names_file'] in completed.stdout))
        after_contract = sha(contract_path.read_bytes()) if contract_path.exists() else None
        runs.append({'repeat': repeat, 'command': shlex.join(command), 'cwd': str(LANE),
                     'exit': completed.returncode, 'finding_ids': ids, 'results': results,
                     'stdout': completed.stdout, 'stderr': completed.stderr,
                     'expected_matches': expected_matches,
                     'contract_unchanged': before_contract == after_contract})
    ids_stable = runs[0]['finding_ids'] == runs[1]['finding_ids']
    output_stable = (runs[0]['stdout'], runs[0]['stderr']) == (runs[1]['stdout'], runs[1]['stderr'])
    result = {key: value for key, value in spec.items() if key != 'mutation'}
    result.update({'runs': runs, 'ids_stable': ids_stable, 'output_byte_stable': output_stable,
                   'ok': ids_stable and all(r['expected_matches'] and r['contract_unchanged'] for r in runs)})
    new_json(case_root / 'observed.json', result)
    return result


with ThreadPoolExecutor(max_workers=8) as pool:
    results = list(pool.map(run_case, prepared))
after = inventory(tracked_inputs)
source_unchanged = before == after
summary = {
    'cases': len(results), 'runs': sum(len(item['runs']) for item in results),
    'matching_cases': sum(item['ok'] for item in results),
    'stable_ids': sum(item['ids_stable'] for item in results),
    'stable_full_output': sum(item['output_byte_stable'] for item in results),
    'contracts_unchanged': all(run['contract_unchanged'] for item in results for run in item['runs']),
    'live_inputs_unchanged': source_unchanged,
    'exit1_ids': sorted({finding for item in results if item['expected_exit'] == 1
                         for run in item['runs'] for finding in run['finding_ids']}),
    'exit2_ids': sorted({finding for item in results if item['expected_exit'] == 2
                         for run in item['runs'] for finding in run['finding_ids']}),
    'failed_case_ids': [item['case_id'] for item in results if not item['ok']],
}
new_json(SCRATCH / 'results.json', {'summary': summary, 'cases': results, 'live_input_sha256_after': after})
transcript = []
for item in results:
    transcript += [f"## {item['case_id']}",
                   f"Expected exit={item['expected_exit']} IDs={item['expected_ids']}",
                   f"IDs stable={item['ids_stable']} full-output stable={item['output_byte_stable']} status={'PASS' if item['ok'] else 'FAIL'}"]
    for run in item['runs']:
        transcript += [f"### Repeat {run['repeat']}", '```sh', f"$ {run['command']}", '```',
                       '```text', run['stdout'].rstrip(),
                       f"observed_exit={run['exit']} stderr={run['stderr']!r}", '```']
new_bytes(SCRATCH / 'full-transcript.md', ('\n'.join(transcript) + '\n').encode())
print(json.dumps(summary, indent=2))
for item in results:
    run = item['runs'][0]
    print(f"CASE {item['case_id']}: repeats=2 exit={run['exit']} ids={run['finding_ids']} "
          f"stable={item['ids_stable']} {'PASS' if item['ok'] else 'FAIL'}")
print('MANIFEST', SCRATCH / 'manifest.json')
print('RESULTS', SCRATCH / 'results.json')
print('TRANSCRIPT', SCRATCH / 'full-transcript.md')
raise SystemExit(0 if summary['matching_cases'] == summary['cases'] and source_unchanged else 1)
