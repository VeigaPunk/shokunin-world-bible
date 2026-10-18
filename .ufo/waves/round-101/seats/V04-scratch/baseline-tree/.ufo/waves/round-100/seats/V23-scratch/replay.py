from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import hashlib
import json
import shlex
import shutil
import subprocess

ROOT = Path('/home/vgpnk/Projects/shokunin/lore-shokunin').resolve()
SCRATCH = ROOT / '.ufo/waves/round-100/seats/V23-scratch'
assert Path.cwd().resolve() == ROOT
assert Path(__file__).resolve().parent == SCRATCH.resolve()
CHAIN = (
    'r88-m3-maya-cluster',
    'r94-paired-crossing',
    'r95-crossing-aftermath',
    'r96-crossing-response',
    'r97-crossing-acknowledgment',
    'r98-clerk-filing',
    'r99-window-lapse',
)
CONTRACT = 'corpus/tools/dependency-freeze-contract.json'
TOOL = 'corpus/tools/dependency_freeze.py'
producer_reports = sorted(p for p in (SCRATCH.parent).glob('T1*.md') if p.is_file())
assert producer_reports, 'C1 producer report absent; no replay allowed'
print('PRODUCER_REPORTS', [p.name for p in producer_reports])
contract_bytes = (ROOT / CONTRACT).read_bytes()
contract = json.loads(contract_bytes)
assert set(contract['pins']) == set(CHAIN)


def fingerprint():
    paths = [ROOT / CONTRACT, ROOT / TOOL]
    for name in CHAIN:
        paths.extend(ROOT / 'corpus/fixtures' / name / filename for filename in contract['pinned_files'])
    return {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}


def run(argv):
    result = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True)
    return {'command': shlex.join(argv), 'exit': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr}


def show(result):
    print('$', result['command'])
    print(result['stdout'], end='')
    if result['stderr']:
        print('STDERR:', result['stderr'], end='')
    print('EXIT', result['exit'])


before = fingerprint()
baseline_bytes = subprocess.check_output(['git', 'show', f'fe1ce46:{CONTRACT}'], cwd=ROOT)
baseline = json.loads(baseline_bytes)
comparison = {
    'baseline_pin_names': sorted(baseline['pins']),
    'delivered_pin_names': sorted(contract['pins']),
    'unchanged_prior_pins': {name: contract['pins'].get(name) == pin for name, pin in baseline['pins'].items()},
    'new_pin_names': sorted(set(contract['pins']) - set(baseline['pins'])),
    'removed_pin_names': sorted(set(baseline['pins']) - set(contract['pins'])),
    'other_top_level_changes': sorted(key for key in set(contract) | set(baseline) if key not in {'pins', 'revision'} and contract.get(key) != baseline.get(key)),
    'tool_unchanged_from_fe1ce46': subprocess.check_output(['git', 'show', f'fe1ce46:{TOOL}'], cwd=ROOT) == (ROOT / TOOL).read_bytes(),
}
print('COMPARISON', json.dumps(comparison, sort_keys=True))
with ThreadPoolExecutor(max_workers=7) as pool:
    chain_results = list(pool.map(run, (['python3', TOOL, f'corpus/fixtures/{name}'] for name in CHAIN)))
for result in chain_results:
    show(result)
print('CHAIN', f"{sum(result['exit'] == 0 and result['stdout'].endswith('RESULT PASS\n') for result in chain_results)}/7")

mirror = SCRATCH / 'guarded-reconstruction'
assert not mirror.exists(), 'scratch reconstruction already exists'
(mirror / 'corpus/tools').mkdir(parents=True)
shutil.copy2(ROOT / TOOL, mirror / TOOL)
(mirror / CONTRACT).write_bytes(baseline_bytes)
for name in ('r99-window-lapse', 'r95-crossing-aftermath'):
    shutil.copytree(ROOT / 'corpus/fixtures' / name, mirror / 'corpus/fixtures' / name)
reconstruction = run(['python3', str(mirror / TOOL), '--freeze', str(mirror / 'corpus/fixtures/r99-window-lapse')])
show(reconstruction)
reconstruction_equal = (mirror / CONTRACT).read_bytes() == contract_bytes
print('GUARDED_RECONSTRUCTION_BYTE_IDENTICAL', reconstruction_equal)
self_test = run(['python3', str(mirror / TOOL), '--self-test'])
show(self_test)

r99_pin = contract['pins']['r99-window-lapse']
print('R99_PIN', json.dumps({key: r99_pin[key] for key in ('fixture', 'revision', 'payload_schema_version', 'pinned_files', 'counts', 'content_sha256')}, sort_keys=True))
print('R99_TERMINAL_EDGE', json.dumps(r99_pin['events']['clerk-lapse-recorded'], sort_keys=True))
after = fingerprint()
stable = before == after
print('LIVE_INPUTS_STABLE', stable)
print('CONTRACT_SHA256', before[CONTRACT])
print('TOOL_SHA256', before[TOOL])
record = {
    'head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
    'comparison': comparison,
    'chain_results': chain_results,
    'reconstruction': reconstruction,
    'reconstruction_byte_identical': reconstruction_equal,
    'self_test_in_owned_scratch': self_test,
    'live_inputs_stable': stable,
    'input_fingerprints': before,
}
(SCRATCH / 'replay.json').write_text(json.dumps(record, indent=2) + '\n')
assert all(comparison['unchanged_prior_pins'].values())
assert comparison['new_pin_names'] == ['r99-window-lapse']
assert not comparison['removed_pin_names'] and not comparison['other_top_level_changes']
assert comparison['tool_unchanged_from_fe1ce46']
assert all(result['exit'] == 0 and result['stdout'].endswith('RESULT PASS\n') for result in chain_results)
assert reconstruction['exit'] == 0 and reconstruction_equal
assert self_test['exit'] == 0 and 'SELF-TEST 18/18\nRESULT PASS\n' in self_test['stdout']
assert stable
print('V23_INDEPENDENT_REPLAY PASS')
