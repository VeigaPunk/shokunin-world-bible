from datetime import datetime
from pathlib import Path
import re
import time

root = Path('/home/vgpnk/Projects/shokunin/lore-shokunin').resolve()
seats = root / '.ufo/waves/round-100/seats'
self_id = 'V29'
required = [
    root / 'corpus/knowledge/r100-crossing-arc-synthesis.md',
    root / 'corpus/knowledge/r100-provenance-semantics-boundary.md',
]
required.extend(root / 'corpus/fixtures/r100-docket-review' / name for name in (
    'entities.json', 'relations.json', 'timeline.json', 'sources.json',
    'contradictions.json', 'README.md', 'claim-excerpt-map.md',
    'fictional-excerpts.md', 'inspiration-note.md', 'source-excerpt.md',
))
for attempt in range(1, 41):
    reports = {}
    for path in seats.iterdir():
        match = re.fullmatch(r'([TV])(\d+)-.*\.md', path.name)
        if match and path.is_file() and path.stat().st_size:
            seat_id = match[1] + str(int(match[2]))
            if seat_id != self_id:
                reports.setdefault(seat_id, []).append(path.name)
    absent = [str(path.relative_to(root)) for path in required if not path.is_file() or not path.stat().st_size]
    producer_absent = [f'T{i}' for i in range(1, 5) if f'T{i}' not in reports]
    duplicates = {key: names for key, names in reports.items() if len(names) != 1}
    print(f'{datetime.now().astimezone().isoformat()} attempt={attempt}/40 other_unique_reports={len(reports)}/31 self_excluded={self_id} missing_producers={producer_absent} missing_artifacts={absent} duplicates={duplicates}', flush=True)
    print('reports=' + repr(sorted(name for names in reports.values() for name in names)), flush=True)
    if len(reports) >= 31 and not producer_absent and not absent and not duplicates:
        print('ALL-OTHERS-PRESENT; producer artifacts present; poll complete', flush=True)
        break
    if attempt < 40:
        time.sleep(20)
else:
    print('ABSENT: bounded 40-attempt poll exhausted; no absent report or artifact verified', flush=True)
