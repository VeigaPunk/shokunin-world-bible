#!/usr/bin/env python3
import argparse
import concurrent.futures
import hashlib
import json
from pathlib import Path
import shlex
import shutil
import subprocess

ROOT = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
SCRATCH = ROOT / '.ufo/waves/round-100/seats/T4-scratch'
WORK = SCRATCH / 'replays'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare():
    cases = {
        'pre-r99-anchor': ('r95-crossing-aftermath', '4265df5'),
        'delivered-anchor': ('r95-crossing-aftermath', None),
        'delivered-precedence': ('r98-clerk-filing', None),
        'delivered-prose-control': ('r98-clerk-filing', None),
        'delivered-self-test': ('r95-crossing-aftermath', None),
    }
    for name, (fixture, revision) in cases.items():
        mirror = WORK / name
        assert mirror.resolve().is_relative_to(SCRATCH.resolve())
        if mirror.exists():
            raise SystemExit(f'refusing existing replay mirror: {mirror}')
        (mirror / 'corpus/tools').mkdir(parents=True)
        (mirror / 'corpus/fixtures').mkdir(parents=True)
        shutil.copytree(ROOT / 'corpus/fixtures' / fixture,
                        mirror / 'corpus/fixtures' / fixture)
        for rel in ('corpus/tools/dependency_freeze.py',
                    'corpus/tools/dependency-freeze-contract.json',
                    'corpus/tools/support_check.py'):
            target = mirror / rel
            if revision:
                result = subprocess.run(['git', 'show', f'{revision}:{rel}'],
                                        cwd=ROOT, capture_output=True, check=True)
                target.write_bytes(result.stdout)
            else:
                shutil.copy2(ROOT / rel, target)
        print(f'PREPARED {mirror.relative_to(ROOT)} fixture={fixture} revision={revision or "delivered"}')


def run():
    current_contract = ROOT / 'corpus/tools/dependency-freeze-contract.json'
    for name in ('delivered-anchor', 'delivered-precedence', 'delivered-prose-control', 'delivered-self-test'):
        mirror = WORK / name
        for rel in ('corpus/tools/dependency_freeze.py', 'corpus/tools/dependency-freeze-contract.json', 'corpus/tools/support_check.py'):
            shutil.copy2(ROOT / rel, mirror / rel)
    baseline = WORK / 'pre-r99-anchor'
    anchor = WORK / 'delivered-anchor'
    precedent = WORK / 'delivered-precedence'
    prose = WORK / 'delivered-prose-control'
    isolated = WORK / 'delivered-self-test'
    r95 = 'corpus/fixtures/r95-crossing-aftermath'
    r98 = 'corpus/fixtures/r98-clerk-filing'
    command_specs = [
        ('A1-pre-r99-support', ['python3', baseline / 'corpus/tools/support_check.py', baseline / r95], 1),
        ('A2-pre-r99-freeze', ['python3', baseline / 'corpus/tools/dependency_freeze.py', baseline / r95], 0),
        ('A3-delivered-support', ['python3', ROOT / 'corpus/tools/support_check.py', anchor / r95], 1),
        ('A4-delivered-freeze', ['python3', anchor / 'corpus/tools/dependency_freeze.py', anchor / r95], 2),
        ('A5-delivered-check-bible', ['python3', ROOT / 'corpus/fixtures/check_bible.py', anchor / r95], 0),
        ('A6-delivered-map', ['python3', ROOT / 'corpus/tools/map_obligations.py', anchor / r95], 0),
        ('B1-semantic-precedence', ['python3', precedent / 'corpus/tools/dependency_freeze.py', precedent / r98], 1),
        ('B2-prose-control', ['python3', prose / 'corpus/tools/dependency_freeze.py', prose / r98], 2),
        ('C1-combined-invalid', ['python3', ROOT / 'corpus/tools/dependency_freeze.py', ROOT / r98, '--freeze', ROOT / r98], 2),
        ('SELF-delivered-freeze', ['python3', isolated / 'corpus/tools/dependency_freeze.py', '--self-test'], 0),
    ]
    before = sha(current_contract)
    def execute(spec):
        label, argv, expected = spec
        argv = [str(part.relative_to(ROOT)) if isinstance(part, Path) else str(part) for part in argv]
        result = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True)
        return label, argv, expected, result
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
        results = list(pool.map(execute, command_specs))
    transcript = []
    structured = []
    failures = []
    for label, argv, expected, result in results:
        command = shlex.join(argv)
        transcript.append(f'## {label}\n$ {command}\n{result.stdout}{result.stderr}exit={result.returncode}\n')
        structured.append({'label': label, 'command': command, 'stdout': result.stdout,
                           'stderr': result.stderr, 'exit': result.returncode, 'expected': expected})
        print(f'{label}: exit={result.returncode} expected={expected}')
        for line in result.stdout.splitlines():
            if line.startswith(('FAIL:', 'FINDING ', 'RESULT ', 'SELF-TEST ', 'SOURCE-SUPPORT ', 'CLEAN:', 'OBLIGATIONS ')):
                print(line)
        if result.returncode != expected:
            failures.append(label)
    after = sha(current_contract)
    semantic = next(item for item in structured if item['label'] == 'B1-semantic-precedence')
    if 'REDUCTION-DETECTED' not in semantic['stdout'] or 'DIGEST-MISMATCH' in semantic['stdout']:
        failures.append('semantic-finding-set')
    combined = next(item for item in structured if item['label'] == 'C1-combined-invalid')
    finding_ids = [line.split(':', 1)[0] for line in combined['stdout'].splitlines() if line.startswith('FINDING ')]
    if finding_ids != ['FINDING INVALID-ARGUMENTS']:
        failures.append('combined-finding-set')
    if before != after:
        failures.append('concurrent-contract-change-replay-required')
    metadata = {
        'root': str(ROOT), 'contract_sha256_before': before, 'contract_sha256_after': after,
        'tool_sha256': sha(ROOT / 'corpus/tools/dependency_freeze.py'),
        'support_sha256': sha(ROOT / 'corpus/tools/support_check.py'),
        'baseline_support_sha256': sha(baseline / 'corpus/tools/support_check.py'),
        'baseline_freeze_sha256': sha(baseline / 'corpus/tools/dependency_freeze.py'),
        'baseline_contract_sha256': sha(baseline / 'corpus/tools/dependency-freeze-contract.json'),
        'commands': structured, 'failures': failures,
    }
    (SCRATCH / 'replay-output.txt').write_text('\n'.join(transcript), encoding='utf-8')
    (SCRATCH / 'replay-results.json').write_text(json.dumps(metadata, indent=2) + '\n', encoding='utf-8')
    print(f'CONTRACT before={before} after={after} unchanged={before == after}')
    print(f'REPLAY failures={failures}')
    raise SystemExit(bool(failures))


if __name__ == '__main__':
    assert Path.cwd().resolve() == ROOT.resolve()
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['prepare', 'run'])
    args = parser.parse_args()
    prepare() if args.mode == 'prepare' else run()
