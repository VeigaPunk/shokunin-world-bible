import ast
import concurrent.futures
import datetime
import hashlib
import importlib.util
import json
import os
import shlex
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path('/home/vgpnk/Projects/shokunin/lore-shokunin').resolve()
SCRATCH = ROOT / '.ufo/waves/round-100/seats/V17-scratch'
BASELINE = 'fe1ce46'
PHASE = sys.argv[1]
OUTPUT = SCRATCH / PHASE
assert OUTPUT.resolve().is_relative_to(SCRATCH)
OUTPUT.mkdir(parents=True, exist_ok=True)
ENV = os.environ.copy()
ENV['TMPDIR'] = str(SCRATCH / 'tmp')
ENV['PYTHONDONTWRITEBYTECODE'] = '1'


def git(*args):
    result = subprocess.run(['git', *args], cwd=ROOT, capture_output=True, check=True)
    return result.stdout


def digest(data):
    return hashlib.sha256(data).hexdigest()


def constants(path):
    tree = ast.parse(path.read_text())
    return {node.targets[0].id: ast.literal_eval(node.value) for node in tree.body
            if isinstance(node, ast.Assign) and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name) and node.targets[0].id in ('PIN', 'BASELINE', 'FIXTURES')}


spec = importlib.util.spec_from_file_location('v17_boundary', ROOT / 'corpus/tools/boundary_doc_check.py')
boundary = importlib.util.module_from_spec(spec)
spec.loader.exec_module(boundary)
contract = json.loads((ROOT / boundary.CONTRACT_PATH).read_text())
disc = constants(ROOT / 'corpus/tools/discriminate_check.py')
fixture_dirs = boundary.checker_fixture_paths((ROOT / boundary.DEFAULT_DOC).read_text())
disc_dirs = ['corpus/fixtures/' + name for name in disc['FIXTURES']]
fixed_paths = [boundary.CONTRACT_PATH, boundary.CHECKER_PATH, boundary.DEFAULT_DOC,
               'corpus/tools/boundary_doc_check.py', 'corpus/tools/discriminate_check.py']
scopes = fixed_paths + fixture_dirs + disc_dirs


def pin_audit(label):
    tracked = git('ls-tree', '-r', '-z', '--name-only', BASELINE, '--', *scopes).decode().split('\0')
    names = {name for name in tracked if name}
    for directory in fixture_dirs + disc_dirs:
        names.update(str(path.relative_to(ROOT)) for path in (ROOT / directory).rglob('*') if path.is_file())
    records = []
    for name in sorted(names):
        path = ROOT / name
        live = digest(path.read_bytes()) if path.is_file() else None
        try:
            baseline = digest(git('show', BASELINE + ':' + name))
        except subprocess.CalledProcessError:
            baseline = None
        try:
            head = digest(git('show', 'HEAD:' + name))
        except subprocess.CalledProcessError:
            head = None
        records.append({'path': name, 'live_sha256': live, 'baseline_sha256': baseline,
                        'head_sha256': head, 'same_baseline': live is not None and live == baseline,
                        'same_head': live is not None and live == head})
    pins = {}
    for key in ('document', 'checker'):
        pin = contract[key]
        live = digest((ROOT / pin['path']).read_bytes())
        committed = digest(git('show', pin['revision'] + ':' + pin['path']))
        pins[key] = {'pin_sha256': pin['sha256'], 'live_sha256': live, 'committed_sha256': committed,
                     'all_match': pin['sha256'] == live == committed}
    legacy = contract['checker']
    legacy_sha = digest(git('show', legacy['legacy_baseline_revision'] + ':' + boundary.CHECKER_PATH))
    control_sha = digest(git('show', disc['BASELINE'] + ':' + boundary.CHECKER_PATH))
    result = {
        'time': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'head': git('rev-parse', 'HEAD').decode().strip(),
        'baseline': git('rev-parse', BASELINE).decode().strip(),
        'baseline_is_ancestor': subprocess.run(['git', 'merge-base', '--is-ancestor', BASELINE, 'HEAD'], cwd=ROOT).returncode == 0,
        'pins': pins,
        'discriminator_PIN': disc['PIN'],
        'three_way_checker_match': disc['PIN'] == contract['checker']['sha256'] == pins['checker']['live_sha256'],
        'legacy_pin_sha256': legacy['legacy_baseline_sha256'],
        'legacy_blob_sha256': legacy_sha,
        'legacy_match': legacy_sha == legacy['legacy_baseline_sha256'],
        'regression_control_revision': disc['BASELINE'],
        'regression_control_sha256': control_sha,
        'control_is_distinct': control_sha != pins['checker']['live_sha256'],
        'receipt_fixture_dirs': fixture_dirs,
        'discriminator_fixture_dirs': disc_dirs,
        'path_count': len(records),
        'bad_paths': [row for row in records if not row['same_baseline'] or not row['same_head']],
        'records': records,
        'scoped_git_status': git('status', '--porcelain', '--', *scopes).decode(),
        'scoped_diff_baseline': git('diff', BASELINE, '--name-status', '--', *scopes).decode(),
    }
    (OUTPUT / (label + '-pins.json')).write_text(json.dumps(result, indent=2) + '\n')
    brief = {key: value for key, value in result.items() if key not in ('records', 'receipt_fixture_dirs', 'discriminator_fixture_dirs')}
    print(label + ' ' + json.dumps(brief, sort_keys=True), flush=True)
    return result


def run_one(name, command):
    start = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result = subprocess.run(command, cwd=ROOT, capture_output=True, env=ENV, timeout=180)
    (OUTPUT / (name + '.stdout')).write_bytes(result.stdout)
    (OUTPUT / (name + '.stderr')).write_bytes(result.stderr)
    meta = {'command': shlex.join(command), 'cwd': str(ROOT), 'start': start,
            'end': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'exit': result.returncode,
            'stderr_bytes': len(result.stderr)}
    (OUTPUT / (name + '.json')).write_text(json.dumps(meta, indent=2) + '\n')
    return name, meta, result.stdout.decode(), result.stderr.decode()


before = pin_audit('before')
commands = [
    ('boundary-default', ['python3', 'corpus/tools/boundary_doc_check.py']),
    ('boundary-self-test', ['python3', 'corpus/tools/boundary_doc_check.py', '--self-test']),
    ('discriminate-held', ['python3', 'corpus/tools/discriminate_check.py']),
    ('discriminate-control', ['python3', 'corpus/tools/discriminate_check.py', '--checker', 'e97613c']),
]
results = {}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    for name, meta, stdout, stderr in pool.map(lambda item: run_one(*item), commands):
        results[name] = meta
        print('\n$ ' + meta['command'] + '\n' + stdout + '[rc=' + str(meta['exit']) + '; stderr_bytes=' + str(meta['stderr_bytes']) + ']', flush=True)
        if stderr:
            print(stderr, flush=True)
after = pin_audit('after')
expected_exits = {'boundary-default': 0, 'boundary-self-test': 0, 'discriminate-held': 0, 'discriminate-control': 2}
checks = {name: results[name]['exit'] == value and results[name]['stderr_bytes'] == 0 for name, value in expected_exits.items()}
checks['held_text'] = 'RESULT: DISCRIMINATION HELD' in (OUTPUT / 'discriminate-held.stdout').read_text()
checks['control_text'] = 'REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved' in (OUTPUT / 'discriminate-control.stdout').read_text()
checks['boundary_text'] = 'CERTIFIED (bounded:' in (OUTPUT / 'boundary-default.stdout').read_text()
checks['self_test_text'] = (OUTPUT / 'boundary-self-test.stdout').read_text().count('SELF-TEST PASS ') == 8
for label, audit in (('before', before), ('after', after)):
    checks[label + '_pins'] = not audit['bad_paths'] and all(value['all_match'] for value in audit['pins'].values()) and audit['three_way_checker_match'] and audit['legacy_match'] and audit['control_is_distinct'] and not audit['scoped_git_status'] and not audit['scoped_diff_baseline']
checks['stable_during_run'] = before['records'] == after['records']
summary = {'phase': PHASE, 'checks': checks, 'pass': all(checks.values()), 'path_count': after['path_count']}
(OUTPUT / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
print('V17-SUMMARY ' + json.dumps(summary, sort_keys=True), flush=True)
raise SystemExit(0 if summary['pass'] else 1)
