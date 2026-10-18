from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re
import shlex
import subprocess

ROOT = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
assert Path.cwd().resolve() == ROOT
BASELINE = 'fe1ce46'
OWNED_DOCS = [
    'SKILL.md',
    'corpus/tools/README.md',
    'corpus/knowledge/r99-gate-blind-spot-table.md',
    'corpus/knowledge/r100-crossing-arc-synthesis.md',
    'corpus/knowledge/r100-provenance-semantics-boundary.md',
]
FIXTURE = 'corpus/fixtures/r100-docket-review'
FIXTURE_FILES = [
    'entities.json', 'relations.json', 'timeline.json', 'sources.json',
    'contradictions.json', 'README.md', 'claim-excerpt-map.md',
    'fictional-excerpts.md', 'inspiration-note.md', 'source-excerpt.md',
]
ARTIFACTS = OWNED_DOCS + [FIXTURE + '/' + name for name in FIXTURE_FILES]
SEATS = ROOT / '.ufo/waves/round-100/seats'


def git(*args):
    return subprocess.run(['git', *args], cwd=ROOT, capture_output=True, check=True).stdout


def sha(data):
    return hashlib.sha256(data).hexdigest()


def run(command):
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    return command, result


print('AUDIT_AT', datetime.now(timezone.utc).isoformat())
print('ROOT', ROOT)
print('BASELINE', git('rev-parse', BASELINE).decode().strip())
print('HEAD', git('rev-parse', 'HEAD').decode().strip())
for prefix in ('T1', 'T2', 'T3', 'T4'):
    reports = [p for p in sorted(SEATS.glob(prefix + '*.md')) if p.is_file() and p.stat().st_size]
    print('PRODUCER_REPORT', prefix, [(p.name, sha(p.read_bytes())) for p in reports])
    assert reports, 'ABSENT producer report ' + prefix
for rel in ARTIFACTS:
    assert (ROOT / rel).is_file() and (ROOT / rel).stat().st_size, 'ABSENT artifact ' + rel

contract_rel = 'corpus/tools/dependency-freeze-contract.json'
contract_bytes = (ROOT / contract_rel).read_bytes()
contract = json.loads(contract_bytes)
before = json.loads(git('show', BASELINE + ':' + contract_rel))
print('CONTRACT_SHA256', sha(contract_bytes))
print('PIN_COUNT', len(contract['pins']))
print('PINS_ADDED', sorted(set(contract['pins']) - set(before['pins'])))
print('PINS_REMOVED', sorted(set(before['pins']) - set(contract['pins'])))
print('PREEXISTING_PIN_FIELDS_UNCHANGED', all(contract['pins'][name] == old for name, old in before['pins'].items()))
print('SELF_TEST_EXPECTATION_COUNT', len(contract['self_test']['expected']))
file_checks = 0
bad_files = []
for name, pin in sorted(contract['pins'].items()):
    observed = {file: sha((ROOT / pin['fixture'] / file).read_bytes()) for file in pin['files']}
    mismatches = [file for file, digest in observed.items() if digest != pin['files'][file]]
    payload = json.dumps(observed, sort_keys=True, separators=(',', ':')).encode()
    content_ok = sha(payload) == pin['content_sha256']
    print('PIN_CURRENT', name, 'files=' + str(len(observed)), 'mismatches=' + repr(mismatches), 'content_match=' + str(content_ok), 'digest=' + pin['content_sha256'], 'revision=' + pin['revision'])
    file_checks += len(observed)
    bad_files.extend(name + '/' + file for file in mismatches)
print('PIN_FILE_DIGEST_CHECKS', file_checks, 'mismatches=' + repr(bad_files))

hash_paths = [
    'corpus/tools/dependency_freeze.py', contract_rel,
    'corpus/tools/support_check.py', 'corpus/tools/map_obligations.py',
    'corpus/fixtures/check_bible.py', 'corpus/tools/boundary-doc-contract.json',
    'corpus/tools/map-obligations-contract.json',
] + ARTIFACTS
hashes = {rel: sha((ROOT / rel).read_bytes()) for rel in dict.fromkeys(hash_paths)}
for rel, digest in hashes.items():
    print('CURRENT_SHA256', rel, digest)

known = {digest: rel for rel, digest in hashes.items()}
known.update({pin['content_sha256']: 'PIN-CONTENT:' + name for name, pin in contract['pins'].items()})
known.update({digest: 'PIN-FILE:' + name + '/' + file for name, pin in contract['pins'].items() for file, digest in pin['files'].items()})
freshness = re.compile(r'sha.?256|digest|revision|6/6|7/7|173|174|17/17|18/18|unpinned|six chain|six-fixture|six frozen|seven|next.?re.?check', re.I)
for rel in OWNED_DOCS + [FIXTURE + '/' + name for name in FIXTURE_FILES if name.endswith('.md')]:
    current = (ROOT / rel).read_text().splitlines()
    original_result = subprocess.run(['git', 'show', BASELINE + ':' + rel], cwd=ROOT, capture_output=True, text=True)
    original = original_result.stdout.splitlines() if original_result.returncode == 0 else []
    if original == current:
        print('DOC_BASELINE_EQUAL', rel)
        continue
    prefix = 0
    while prefix < min(len(original), len(current)) and original[prefix] == current[prefix]:
        prefix += 1
    print('NEW_BYTE_SWEEP', rel, 'first_changed_line=' + str(prefix + 1), 'lines=' + str(len(current)))
    for number, line in enumerate(current, 1):
        if number <= prefix:
            continue
        if freshness.search(line):
            print('FRESHNESS_LINE', rel + ':' + str(number), line)
        for value in re.findall(r'(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])', line):
            print('DIGEST_REFERENCE', rel + ':' + str(number), value, 'CURRENT=' + known.get(value, 'UNCLASSIFIED-HISTORICAL-OR-MUTANT'))

commands = [['python3', 'corpus/tools/dependency_freeze.py', pin['fixture']] for pin in contract['pins'].values()]
commands += [
    ['python3', 'corpus/fixtures/check_bible.py', FIXTURE],
    ['python3', 'corpus/tools/map_obligations.py', FIXTURE],
    ['python3', 'corpus/tools/support_check.py', FIXTURE],
    ['python3', 'corpus/tools/discriminate_check.py'],
    ['python3', 'corpus/tools/discriminate_check.py', '--checker', 'e97613c'],
    ['python3', 'corpus/tools/boundary_doc_check.py'],
]
with ThreadPoolExecutor(max_workers=len(commands)) as pool:
    for command, result in pool.map(run, commands):
        print('$', shlex.join(command))
        print(result.stdout, end='')
        print('STDERR', repr(result.stderr))
        print('EXIT', result.returncode)

watch = (ROOT / 'corpus/knowledge/r91-c9-watch.md').read_text()
rows = [(n, line) for n, line in enumerate(watch.splitlines(), 1) if line.startswith('| 2026-')]
print('C9_DATED_ROWS', len(rows))
print('C9_LATEST_ROW', rows[-1])
print('C9_R100_SECTION_PRESENT', 'r100 re-check' in watch)
print('C9_BASELINE_EQUAL', (ROOT / 'corpus/knowledge/r91-c9-watch.md').read_bytes() == git('show', BASELINE + ':corpus/knowledge/r91-c9-watch.md'))
spot_checks = [
    ('corpus/tools/dependency_freeze.py', 'corpus/knowledge/r99-gate-blind-spot-table.md', 274),
    (contract_rel, 'corpus/knowledge/r100-provenance-semantics-boundary.md', 40),
    ('corpus/fixtures/check_bible.py', 'corpus/knowledge/r100-crossing-arc-synthesis.md', 111),
    ('corpus/tools/support_check.py', 'corpus/knowledge/r99-gate-blind-spot-table.md', 284),
]
for rel, doc, number in spot_checks:
    digest = hashes[rel]
    assert digest in (ROOT / doc).read_text().splitlines()[number - 1]
    print('SPOT-PASS', rel, digest, doc + ':' + str(number))
print('REQUIRED_DIGEST_SPOTS 4/4 current')
table_rel = 'corpus/knowledge/r99-gate-blind-spot-table.md'
old_table = git('show', BASELINE + ':' + table_rel)
new_table = (ROOT / table_rel).read_bytes()
assert new_table.startswith(old_table)
addendum = new_table[len(old_table):].decode()
assert addendum.count('| 2026-10-17 / r100 |') == 3
assert '8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628' not in addendum
print('TABLE_APPEND_ONLY', 'historical_bytes=' + str(len(old_table)), 'dated_rows=3', 'old_contract_pin_not_carried_into_addendum=True')
for rel in ('corpus/README.md', 'corpus/fixtures/README.md', 'corpus/knowledge/r91-c9-watch.md'):
    print('CARRIED_DOCUMENT_BASELINE_EQUAL', rel, (ROOT / rel).read_bytes() == git('show', BASELINE + ':' + rel))
sequence = ROOT / 'corpus/fixtures/r91-c1-tick-unresolved'
print('C9_SEQUENCE_SCOPE_EXCERPT_FILES', sorted(path.name for path in sequence.glob('*excerpt*')))
print('C9_SEQUENCE_SCOPE_README_LINE3', (sequence / 'README.md').read_text().splitlines()[2])
producer_report = SEATS / 'T2-fixture-author.md'
for number, line in enumerate(producer_report.read_text().splitlines(), 1):
    for token in re.findall(r'sha256=([0-9a-f]{32,})', line):
        if len(token) != 64:
            print('PRODUCER_REPORT_MALFORMED_DIGEST', producer_report.name + ':' + str(number), 'length=' + str(len(token)), token)
print('ACTUAL_R100_RELATIONS_SHA256', hashes[FIXTURE + '/relations.json'])
fixtures = sorted(path for path in (ROOT / 'corpus/fixtures').iterdir() if path.is_dir() and not path.name.startswith(('.', '__')))
census_commands = [['python3', 'corpus/fixtures/check_bible.py', str(path.relative_to(ROOT))] for path in fixtures]
with ThreadPoolExecutor(max_workers=16) as pool:
    census = list(pool.map(run, census_commands))
exit_counts = {code: sum(result.returncode == code for _, result in census) for code in sorted({result.returncode for _, result in census})}
print('CENSUS', 'directories=' + str(len(census)), 'exit_counts=' + repr(exit_counts))
print('CENSUS', 'violations=' + str(sum(sum(line.startswith('VIOLATION:') for line in result.stdout.splitlines()) for _, result in census)))
print('CENSUS', 'stderr_nonempty=' + repr([command[-1] for command, result in census if result.stderr]))
print('SNAPSHOT_STABLE', all(sha((ROOT / rel).read_bytes()) == digest for rel, digest in hashes.items()))
print('CONTRACT_STABLE', sha((ROOT / contract_rel).read_bytes()) == sha(contract_bytes))
