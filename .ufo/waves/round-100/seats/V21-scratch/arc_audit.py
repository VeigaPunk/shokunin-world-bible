#!/usr/bin/env python3
import concurrent.futures
import hashlib
import json
from pathlib import Path
import re
import shlex
import subprocess

ROOT = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
SCRATCH = ROOT / '.ufo/waves/round-100/seats/V21-scratch'
FIXTURES = [
    'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response',
    'r97-crossing-acknowledgment', 'r98-clerk-filing', 'r99-window-lapse',
    'r100-docket-review',
]
EXPECTED = [(5, 1, 3, 3, 14), (5, 1, 4, 4, 15), (5, 1, 5, 5, 16),
            (5, 1, 6, 6, 17), (6, 1, 7, 7, 20), (6, 1, 8, 8, 21),
            (6, 1, 9, 9, 22)]


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))


def map_rows(path):
    rows = []
    for line in path.read_text(encoding='utf-8').splitlines():
        if re.match(r'^\| J\d+ \|', line):
            cells = [cell.strip() for cell in line.strip('|').split('|')]
            cells[3] = re.sub(r'`r(?:94-paired-crossing|95-crossing-aftermath|96-crossing-response|97-crossing-acknowledgment|98-clerk-filing|99-window-lapse|100-docket-review):', '`CLUSTER:', cells[3])
            rows.append(cells)
    return rows


def main():
    assert Path.cwd().resolve() == ROOT.resolve()
    failures = []
    records = []
    previous = None
    previous_fixture = None
    for name, expected in zip(FIXTURES, EXPECTED):
        fixture = ROOT / 'corpus/fixtures' / name
        tables = {key: read_json(fixture / f'{key}.json')
                  for key in ('entities', 'relations', 'timeline', 'sources', 'contradictions')}
        obligations = len(tables['entities']) + sum(len(row.get('claims', [])) for row in tables['entities']) + len(tables['relations']) + len(tables['timeline'])
        counts = tuple(len(tables[key]) for key in ('entities', 'relations', 'timeline', 'sources')) + (obligations,)
        assert counts == expected, (name, counts, expected)
        assert tables['contradictions'] == [], name
        last = tables['timeline'][-1]
        record = {'fixture': name, 'counts_entities_relations_events_sources_obligations': counts,
                  'last_event': last, 'last_source': tables['sources'][-1]}
        if previous is not None:
            preserving = {
                'entities_prefix': tables['entities'][:len(previous['entities'])] == previous['entities'],
                'relations': tables['relations'] == previous['relations'],
                'timeline_prefix': tables['timeline'][:-1] == previous['timeline'],
                'sources_prefix': tables['sources'][:-1] == previous['sources'],
                'excerpt_byte_prefix': (fixture / 'fictional-excerpts.md').read_bytes().startswith((previous_fixture / 'fictional-excerpts.md').read_bytes()),
                'inspiration_bytes': (fixture / 'inspiration-note.md').read_bytes() == (previous_fixture / 'inspiration-note.md').read_bytes(),
                'external_excerpt_bytes': (fixture / 'source-excerpt.md').read_bytes() == (previous_fixture / 'source-excerpt.md').read_bytes(),
                'inherited_map_rows': map_rows(fixture / 'claim-excerpt-map.md')[:len(map_rows(previous_fixture / 'claim-excerpt-map.md'))] == map_rows(previous_fixture / 'claim-excerpt-map.md'),
            }
            record['preserving_vs_previous'] = preserving
            if not all(preserving.values()):
                failures.append(f'{name}:preserving:{preserving}')
        records.append(record)
        previous, previous_fixture = tables, fixture
        print(f'ARC {name}: entities/relations/events/sources/obligations={"/".join(map(str, counts))}; event={last["id"]}; source={last["source_id"]}; tick={last["tick"]}')
        if 'preserving_vs_previous' in record:
            print(f'PRESERVING {name}: {record["preserving_vs_previous"]}')
    commands = []
    for name in FIXTURES:
        fixture = f'corpus/fixtures/{name}'
        for tool in ['corpus/fixtures/check_bible.py', 'corpus/tools/support_check.py', 'corpus/tools/map_obligations.py']:
            commands.append(['python3', tool, fixture])
    def execute(argv):
        result = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True)
        return {'command': shlex.join(argv), 'exit': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr}
    with concurrent.futures.ThreadPoolExecutor(max_workers=14) as pool:
        receipts = list(pool.map(execute, commands))
    transcript = []
    for item in receipts:
        transcript.append(f'$ {item["command"]}\n{item["stdout"]}{item["stderr"]}exit={item["exit"]}\n')
        print(f'$ {item["command"]} exit={item["exit"]}')
        for line in item['stdout'].splitlines():
            if line.startswith(('CLEAN:', 'INVENTORY ', 'SOURCE-SUPPORT ', 'OBLIGATIONS ', 'RESULT ', 'FINDING ')):
                print(line)
        if item['exit'] != 0:
            failures.append(item['command'])
    census = len([p for p in (ROOT / 'corpus/fixtures').iterdir() if p.is_dir()])
    print(f'CENSUS {census}')
    if census != 174:
        failures.append(f'census={census}')
    data = {'records': records, 'receipts': receipts, 'fixture_directory_census': census,
            'failures': failures, 'r100_files_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in (ROOT / 'corpus/fixtures/r100-docket-review').iterdir() if p.is_file()}}
    (SCRATCH / 'arc-results.json').write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')
    (SCRATCH / 'arc-output.txt').write_text('\n'.join(transcript), encoding='utf-8')
    print(f'ARC-AUDIT failures={failures}')
    raise SystemExit(bool(failures))


if __name__ == '__main__':
    main()
