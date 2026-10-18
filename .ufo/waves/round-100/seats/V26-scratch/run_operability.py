import concurrent.futures
import hashlib
import json
import os
from pathlib import Path
import shlex
import shutil
import subprocess

ROOT = Path('/home/vgpnk/Projects/shokunin/lore-shokunin').resolve()
SCRATCH = ROOT / '.ufo/waves/round-100/seats/V26-scratch'
assert Path.cwd().resolve() == ROOT
assert SCRATCH.resolve() == SCRATCH and SCRATCH.is_relative_to(ROOT)
assert Path(__file__).resolve() == SCRATCH / 'run_operability.py'
CHAIN = ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response', 'r97-crossing-acknowledgment', 'r98-clerk-filing', 'r99-window-lapse']
FILES = ['entities.json', 'relations.json', 'timeline.json', 'sources.json', 'contradictions.json', 'README.md', 'claim-excerpt-map.md', 'fictional-excerpts.md', 'inspiration-note.md', 'source-excerpt.md']
seats = ROOT / '.ufo/waves/round-100/seats'
for name in ['T1', 'T2', 'T3', 'T4']:
    reports = list(seats.glob(name + '*.md'))
    assert len(reports) == 1, (name, reports)
    assert reports[0].stat().st_size > 0
    print('PRODUCER', reports[0].relative_to(ROOT))
fixture = ROOT / 'corpus/fixtures/r100-docket-review'
for name in FILES:
    assert (fixture / name).is_file(), name
for name in ['r100-crossing-arc-synthesis.md', 'r100-provenance-semantics-boundary.md']:
    assert (ROOT / 'corpus/knowledge' / name).is_file(), name
contract = json.loads((ROOT / 'corpus/tools/dependency-freeze-contract.json').read_text())
assert set(contract['pins']) == set(CHAIN)
paths = [ROOT / 'corpus/tools/dependency-freeze-contract.json', ROOT / 'corpus/tools/README.md', ROOT / 'SKILL.md', ROOT / 'corpus/knowledge/r100-crossing-arc-synthesis.md', ROOT / 'corpus/knowledge/r100-provenance-semantics-boundary.md', ROOT / 'corpus/knowledge/r99-gate-blind-spot-table.md']
paths += [fixture / name for name in FILES]
paths += sorted((ROOT / 'corpus/tools').glob('*.py'))
paths += [ROOT / 'corpus/tools/map-obligations-contract.json', ROOT / 'corpus/tools/boundary-doc-contract.json', ROOT / 'corpus/fixtures/check_bible.py']
paths += [ROOT / 'corpus/fixtures' / name / filename for name in CHAIN for filename in FILES]
def hashes():
    return {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}
before = hashes()
mirror = SCRATCH / 'mirror'
assert not mirror.exists(), 'Use a fresh scratch mirror; do not overwrite an earlier run'
(mirror / 'corpus/tools').mkdir(parents=True)
for name in ['dependency_freeze.py', 'dependency-freeze-contract.json', 'map_obligations.py', 'map-obligations-contract.json']:
    source = ROOT / 'corpus/tools' / name
    destination = mirror / 'corpus/tools' / name
    shutil.copy2(source, destination)
    assert source.read_bytes() == destination.read_bytes()
    print('MIRROR BYTE-IDENTICAL', name, hashlib.sha256(source.read_bytes()).hexdigest())
for name in ['r95-crossing-aftermath', 'r99-window-lapse']:
    source = ROOT / 'corpus/fixtures' / name
    destination = mirror / 'corpus/fixtures' / name
    shutil.copytree(source, destination)
    for filename in FILES:
        assert (source / filename).read_bytes() == (destination / filename).read_bytes()
foreign = SCRATCH / 'foreign/r99-window-lapse'
shutil.copytree(ROOT / 'corpus/fixtures/r99-window-lapse', foreign)
(SCRATCH / 'tmp').mkdir()
mirror_rel = mirror.relative_to(ROOT)
foreign_rel = foreign.relative_to(ROOT)
environment = {**os.environ, 'TMPDIR': str(SCRATCH / 'tmp'), 'PYTHONDONTWRITEBYTECODE': '1', 'GIT_OPTIONAL_LOCKS': '0'}
specs = []
def add(label, argv, code=0, fragments=()):
    specs.append((label, ['python3', *map(str, argv)], code, fragments))
for name in CHAIN:
    add('chain-' + name, ['corpus/tools/dependency_freeze.py', 'corpus/fixtures/' + name], fragments=['RESULT PASS'])
add('new-schema', ['corpus/fixtures/check_bible.py', 'corpus/fixtures/r100-docket-review'], fragments=['CLEAN: schema, citations, relations, timeline; 0 violations'])
add('new-map', ['corpus/tools/map_obligations.py', 'corpus/fixtures/r100-docket-review'], fragments=['OBLIGATIONS raw=22 mapped=22', 'TOTAL-ROWS 24/24', 'RESULT PASS'])
add('new-support', ['corpus/tools/support_check.py', 'corpus/fixtures/r100-docket-review'], fragments=['SOURCE-SUPPORT 22/22', 'VALIDATED-ROWS 24/24', 'RESULT PASS'])
add('new-freeze-bound', ['corpus/tools/dependency_freeze.py', 'corpus/fixtures/r100-docket-review'], 2, ['FINDING UNPINNED-FIXTURE:', 'RESULT ERROR'])
add('freeze-self-test-isolated', [mirror_rel / 'corpus/tools/dependency_freeze.py', '--self-test'], fragments=['SELF-TEST 18/18', 'RESULT PASS'])
add('map-self-test-isolated', [mirror_rel / 'corpus/tools/map_obligations.py', '--self-test'], fragments=['SELF-TEST CASES 25/25 pinned', 'SELF-TEST PASS dual_pointer', 'RESULT PASS'])
add('boundary-default', ['corpus/tools/boundary_doc_check.py'], fragments=['replay_cases=14/14', 'CERTIFIED (bounded:'])
add('boundary-self-test', ['corpus/tools/boundary_doc_check.py', '--self-test'], fragments=['SELF-TEST PASS committed_default', 'SELF-TEST PASS anchor_range_control', '\nSELF-TEST PASS\n'])
add('discriminator-default', ['corpus/tools/discriminate_check.py'], fragments=['RESULT: DISCRIMINATION HELD'])
add('discriminator-negative', ['corpus/tools/discriminate_check.py', '--checker', 'e97613c'], 2, ['REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved'])
add('map-frozen-r93', ['corpus/tools/map_obligations.py', '--frozen', '.ufo/waves/round-94/frozen/map-obligations-r93'], fragments=['SNAPSHOT inputs=4 digests=verified', 'FROZEN expected=PASS/0', 'RESULT PASS'])
add('freeze-invalid-combined', ['corpus/tools/dependency_freeze.py', 'corpus/fixtures/r99-window-lapse', '--freeze', 'corpus/fixtures/r99-window-lapse'], 2, ['FINDING INVALID-ARGUMENTS:', 'RESULT ERROR'])
add('freeze-foreign-path', ['corpus/tools/dependency_freeze.py', foreign_rel], 2, ['FINDING PATH-MISMATCH:', 'RESULT ERROR'])
add('freeze-foreign-scope-isolated', [mirror_rel / 'corpus/tools/dependency_freeze.py', '--freeze', foreign_rel], 2, ['FINDING SCOPE-REFUSED:', 'RESULT ERROR'])
add('freeze-help', ['corpus/tools/dependency_freeze.py', '--help'], fragments=['usage: dependency_freeze.py'])
add('map-invalid-missing', ['corpus/tools/map_obligations.py'], 2, ['FINDING invalid_arguments:', 'RESULT ERROR'])
add('support-invalid-missing', ['corpus/tools/support_check.py'], 2, ['usage: support_check.py'])

def execute(spec):
    label, argv, code, fragments = spec
    result = subprocess.run(argv, cwd=ROOT, env=environment, capture_output=True, text=True, timeout=120)
    output = result.stdout + result.stderr
    ok = result.returncode == code and all(fragment in output for fragment in fragments) and 'Traceback' not in output
    if label == 'freeze-invalid-combined':
        ok = ok and output.count('FINDING ') == 1 and 'DIGEST-MISMATCH' not in output
    if label == 'freeze-help':
        ok = ok and not any(line.startswith('RESULT ') for line in result.stdout.splitlines())
    return {'label': label, 'command': shlex.join(argv), 'cwd': str(ROOT), 'exit': result.returncode, 'expected_exit': code, 'stdout': result.stdout, 'stderr': result.stderr, 'ok': ok}
with concurrent.futures.ThreadPoolExecutor(max_workers=12) as pool:
    results = list(pool.map(execute, specs))
log = []
for result in results:
    log.extend(['## ' + result['label'], '$ ' + result['command'], 'CWD ' + result['cwd'], result['stdout'].rstrip(), 'STDERR ' + repr(result['stderr']), f"EXIT {result['exit']} EXPECTED {result['expected_exit']} MATCH {result['ok']}", ''])
after = hashes()
changed = [name for name in before if before[name] != after[name]]
mirror_contract_unchanged = (mirror / 'corpus/tools/dependency-freeze-contract.json').read_bytes() == (ROOT / 'corpus/tools/dependency-freeze-contract.json').read_bytes()
log += ['DELIVERED FILES CHANGED DURING REPLAY ' + repr(changed), 'ISOLATED GUARD LEFT CONTRACT UNCHANGED ' + str(mirror_contract_unchanged), f"CHECKS {sum(r['ok'] for r in results)}/{len(results)} expectations matched"]
(SCRATCH / 'operability-transcript.txt').write_text('\n'.join(log) + '\n')
(SCRATCH / 'operability-results.json').write_text(json.dumps({'results': results, 'before': before, 'after': after, 'changed': changed, 'mirror_contract_unchanged': mirror_contract_unchanged}, indent=2) + '\n')
print('\n'.join(log))
assert not changed, changed
assert mirror_contract_unchanged
assert all(result['ok'] for result in results), [r['label'] for r in results if not r['ok']]
