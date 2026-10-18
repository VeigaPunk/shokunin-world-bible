from datetime import datetime
from pathlib import Path
import hashlib
import json
import time

ROOT = Path('/home/vgpnk/Projects/shokunin/lore-shokunin').resolve()
SCRATCH = ROOT / '.ufo/waves/round-100/seats/V27-scratch'
SEATS = ROOT / '.ufo/waves/round-100/seats'
assert Path.cwd() == ROOT
assert SCRATCH.resolve().is_relative_to(ROOT)
files = [
    'corpus/tools/dependency-freeze-contract.json',
    'corpus/tools/README.md',
    'SKILL.md',
    'corpus/knowledge/r100-crossing-arc-synthesis.md',
    'corpus/knowledge/r100-provenance-semantics-boundary.md',
    'corpus/knowledge/r99-gate-blind-spot-table.md',
]
files += [f'corpus/fixtures/r100-docket-review/{name}' for name in (
    'entities.json', 'relations.json', 'timeline.json', 'sources.json',
    'contradictions.json', 'README.md', 'claim-excerpt-map.md',
    'fictional-excerpts.md', 'inspiration-note.md', 'source-excerpt.md',
)]
for attempt in range(1, 41):
    missing = [name for name in files if not (ROOT / name).is_file() or not (ROOT / name).stat().st_size]
    reports = {prefix: [str(p.relative_to(ROOT)) for p in sorted(SEATS.glob(prefix + '-*.md')) if p.is_file() and p.stat().st_size] for prefix in ('T1', 'T2', 'T3', 'T4')}
    missing_reports = [prefix for prefix, paths in reports.items() if not paths]
    entry = {
        'attempt': attempt,
        'at': datetime.now().astimezone().isoformat(),
        'missing_artifacts': missing,
        'missing_producer_reports': missing_reports,
        'producer_reports': reports,
    }
    print(json.dumps(entry, sort_keys=True), flush=True)
    if not missing and not missing_reports:
        hashes = {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in files}
        for paths in reports.values():
            hashes.update({name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in paths})
        (SCRATCH / 'ready-manifest.json').write_text(json.dumps({'ready': entry, 'sha256': hashes}, indent=2) + '\n')
        print('READY artifacts=16 producer-prefixes=4', flush=True)
        break
    if attempt < 40:
        time.sleep(20)
else:
    print('ABSENT producer/artifact poll exhausted after 40 tries', flush=True)
    raise SystemExit(3)
