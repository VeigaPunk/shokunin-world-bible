#!/usr/bin/env python3
import concurrent.futures
import hashlib
import json
from pathlib import Path
import re
import shlex
import subprocess

ROOT = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
SCRATCH = ROOT / '.ufo/waves/round-100/seats/T4-scratch'
DOCS = ['corpus/knowledge/r100-crossing-arc-synthesis.md',
        'corpus/knowledge/r100-provenance-semantics-boundary.md',
        'corpus/knowledge/r99-gate-blind-spot-table.md']
TOOLS = {'dependency_freeze.py': 'corpus/tools/dependency_freeze.py',
         'support_check.py': 'corpus/tools/support_check.py',
         'map_obligations.py': 'corpus/tools/map_obligations.py',
         'check_bible.py': 'corpus/fixtures/check_bible.py'}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    assert Path.cwd().resolve() == ROOT.resolve()
    checked = set()
    ranges = set()
    output = []
    def emit(line):
        output.append(line)
        print(line)
    def check(candidate):
        match = re.match(r'^(.*?)(?::(\d+)(?:-(\d+))?)?$', candidate)
        name, start, end = match.groups()
        if '<' in name or name.endswith('/**'):
            return
        if name in TOOLS:
            name = TOOLS[name]
        if not name.startswith(('corpus/', '.ufo/', 'LOG.md')):
            return
        target = (ROOT / name).resolve()
        assert target.is_relative_to(ROOT), candidate
        assert target.exists(), candidate
        checked.add(name)
        if start:
            assert target.is_file(), candidate
            count = len(target.read_text(encoding='utf-8').splitlines())
            assert 1 <= int(start) <= int(end or start) <= count, (candidate, count)
            ranges.add(candidate)
    for rel in DOCS:
        path = ROOT / rel
        text = path.read_text(encoding='utf-8')
        assert text.endswith('\n'), rel
        assert all(line == line.rstrip() for line in text.splitlines()), rel
        assert sum(line.startswith('```') for line in text.splitlines()) % 2 == 0, rel
        for field in ('source:', 'verified-at:', 'recheck:'):
            assert any(line.startswith(field) for line in text.splitlines()), (rel, field)
        if rel.endswith('r99-gate-blind-spot-table.md'):
            text = text.split('## Dated addendum — 2026-10-17, round 100', 1)[1]
        for token in re.findall(r'`([^`\n]+)`', text):
            if token.startswith('python3 '):
                for part in shlex.split(token)[1:]:
                    check(part)
            elif ' ' not in token:
                match = re.search(r'\{([^{}]+)\}', token)
                if match:
                    for part in match.group(1).split(','):
                        check(token[:match.start()] + part + token[match.end():])
                else:
                    check(token)
        for line in text.splitlines():
            if line.startswith('python3 '):
                for part in shlex.split(line)[1:]:
                    check(part)
        for match in re.finditer(r'`(dependency_freeze\.py):(\d+)(?:-(\d+))?`', text):
            check(match.group(0).strip('`'))
        emit(f'DOC {rel}: bytes={path.stat().st_size} sha256={sha(path)} style=PASS')
    baseline = subprocess.check_output(['git', 'show', 'fe1ce46:corpus/knowledge/r99-gate-blind-spot-table.md'], cwd=ROOT)
    table = (ROOT / DOCS[-1]).read_bytes()
    assert table.startswith(baseline)
    emit(f'TABLE historical_prefix={len(baseline)} bytes preserved; added_bytes={len(table)-len(baseline)}')
    table_text = table.decode('utf-8')
    for number in (10, 11, 12):
        assert len(re.findall(rf'^\| {number} \| 2026-10-17 / r100 \|', table_text, re.M)) == 1
    emit('TABLE dated_rows=3 exact; historical_rows_unmodified=PASS')
    arc = json.loads((SCRATCH / 'arc-results.json').read_text())
    assert arc['failures'] == []
    assert len(arc['receipts']) == 21 and all(item['exit'] == 0 for item in arc['receipts'])
    for name, digest in arc['r100_files_sha256'].items():
        assert sha(ROOT / 'corpus/fixtures/r100-docket-review' / name) == digest, name
    emit('ARC saved_real_gate_receipts=21/21 clean; delivered_r100_file_stability=10/10')
    replay = json.loads((SCRATCH / 'replay-results.json').read_text())
    assert replay['failures'] == []
    contract_path = ROOT / 'corpus/tools/dependency-freeze-contract.json'
    assert sha(contract_path) == replay['contract_sha256_before'] == replay['contract_sha256_after']
    assert sha(ROOT / TOOLS['dependency_freeze.py']) == replay['tool_sha256']
    emit(f'REPLAY all_expected_outcomes=PASS; contract_stable={sha(contract_path)}')
    contract = json.loads(contract_path.read_text())
    assert len(contract['pins']) == 7
    assert 'r100-docket-review' not in contract['pins']
    base_contract = json.loads(subprocess.check_output(['git', 'show', 'fe1ce46:corpus/tools/dependency-freeze-contract.json'], cwd=ROOT))
    assert all(contract['pins'][name] == pin for name, pin in base_contract['pins'].items())
    def run(name):
        argv = ['python3', 'corpus/tools/dependency_freeze.py', f'corpus/fixtures/{name}']
        result = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True)
        return argv, result
    with concurrent.futures.ThreadPoolExecutor(max_workers=7) as pool:
        for argv, result in pool.map(run, contract['pins']):
            assert result.returncode == 0 and 'RESULT PASS' in result.stdout, (argv, result.stdout)
            emit(f'$ {shlex.join(argv)}\n{result.stdout.rstrip()}\nexit={result.returncode}')
    emit('CHAIN 7/7 clean; six inherited pins unchanged; r100 explicitly unpinned')
    result = subprocess.run(['git', 'diff', '--check', '--', *DOCS], cwd=ROOT, capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr
    emit('GIT-DIFF-CHECK PASS (new-file whitespace independently checked above)')
    emit(f'CITED_PATHS {len(checked)}; EXPLICIT_RANGES {len(ranges)}; MISSING 0')
    emit('FINAL-AUDIT PASS')
    (SCRATCH / 'final-audit-output.txt').write_text('\n'.join(output) + '\n', encoding='utf-8')
    manifest = sorted(str(path.relative_to(ROOT)) for path in SCRATCH.rglob('*') if path.is_file())
    manifest_path = SCRATCH / 'file-manifest.json'
    if str(manifest_path.relative_to(ROOT)) not in manifest:
        manifest.append(str(manifest_path.relative_to(ROOT)))
    manifest_path.write_text(json.dumps(sorted(manifest), indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
