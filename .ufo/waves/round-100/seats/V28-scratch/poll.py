from pathlib import Path
import datetime
import hashlib
import json
import time

ROOT = Path('/home/vgpnk/Projects/shokunin/lore-shokunin').resolve()
SCRATCH = ROOT / '.ufo/waves/round-100/seats/V28-scratch'
SEATS = SCRATCH.parent
assert Path.cwd().resolve() == ROOT
assert SCRATCH.resolve().is_relative_to(ROOT)
files = ['entities.json', 'relations.json', 'timeline.json', 'sources.json', 'contradictions.json', 'README.md', 'claim-excerpt-map.md', 'fictional-excerpts.md', 'inspiration-note.md', 'source-excerpt.md']
required = [f'corpus/fixtures/r100-docket-review/{name}' for name in files] + [
    'corpus/tools/dependency-freeze-contract.json',
    'corpus/tools/README.md',
    'SKILL.md',
    'corpus/knowledge/r100-crossing-arc-synthesis.md',
    'corpus/knowledge/r100-provenance-semantics-boundary.md',
    'corpus/knowledge/r99-gate-blind-spot-table.md',
]

with (SCRATCH / 'poll.jsonl').open('w') as log:
    for attempt in range(1, 41):
        reports = {seat: sorted(str(p.relative_to(ROOT)) for p in SEATS.glob(f'{seat}-*.md') if p.is_file() and p.stat().st_size > 0) for seat in ['T1', 'T2', 'T3', 'T4']}
        absent = [name for name in required if not (ROOT / name).is_file()]
        entry = {'attempt': attempt, 'timestamp': datetime.datetime.now().astimezone().isoformat(), 'artifacts': len(required) - len(absent), 'expected_artifacts': len(required), 'absent': absent, 'reports': reports}
        print(json.dumps(entry, sort_keys=True), flush=True)
        log.write(json.dumps(entry, sort_keys=True) + '\n')
        log.flush()
        if not absent and all(reports.values()):
            names = required + ['PROVINCE.md', 'SHONEN.md', 'README.md', 'l0-questions.md', 'LOG.md', 'SCORECARD.md', 'corpus/fixtures/check_bible.py', 'corpus/tools/dependency_freeze.py', 'corpus/tools/support_check.py', 'corpus/tools/map_obligations.py', 'corpus/tools/boundary_doc_check.py'] + [name for paths in reports.values() for name in paths]
            manifest = {name: {'sha256': hashlib.sha256((ROOT / name).read_bytes()).hexdigest(), 'size': (ROOT / name).stat().st_size, 'mtime_ns': (ROOT / name).stat().st_mtime_ns, 'ctime_ns': (ROOT / name).stat().st_ctime_ns} for name in sorted(set(names))}
            (SCRATCH / 'ready-manifest.json').write_text(json.dumps({'ready_at': entry['timestamp'], 'attempt': attempt, 'files': manifest}, indent=2) + '\n')
            print('READY artifacts=16/16 producer_reports=4/4; manifest=V28-scratch/ready-manifest.json', flush=True)
            break
        if attempt < 40:
            time.sleep(20)
    else:
        print('ABSENT: producer readiness gate not met after 40 tries', flush=True)
        raise SystemExit(2)
