from datetime import datetime
import hashlib
import json
from pathlib import Path
import time

ROOT = Path('/home/vgpnk/Projects/shokunin/lore-shokunin').resolve()
assert Path.cwd().resolve() == ROOT
SEATS = ROOT / '.ufo/waves/round-100/seats'
SCRATCH = SEATS / 'V07-scratch'
FIXTURE = ROOT / 'corpus/fixtures/r100-docket-review'
BASE = ROOT / 'corpus/fixtures/r99-window-lapse'
FILES = (
    'entities.json', 'relations.json', 'timeline.json', 'sources.json',
    'contradictions.json', 'README.md', 'claim-excerpt-map.md',
    'fictional-excerpts.md', 'inspiration-note.md', 'source-excerpt.md',
)
BASE_HASHES = {
    name: hashlib.sha256((BASE / name).read_bytes()).hexdigest()
    for name in ('README.md', 'claim-excerpt-map.md')
}
LOG = SCRATCH / 'poll.log'
assert LOG.resolve().is_relative_to(SCRATCH.resolve())
with LOG.open('x', encoding='utf-8') as log:
    for attempt in range(1, 41):
        missing = [name for name in FILES if not (FIXTURE / name).is_file()]
        docs = {}
        for name in BASE_HASHES:
            path = FIXTURE / name
            docs[name] = (
                'absent' if not path.is_file() else
                'same-as-r99' if hashlib.sha256(path.read_bytes()).hexdigest() == BASE_HASHES[name]
                else 'moved'
            )
        reports = sorted(
            path.name for path in SEATS.iterdir()
            if path.is_file() and path.name.startswith('T3')
            and path.suffix == '.md' and path.stat().st_size > 0
        )
        ready = not missing and all(value == 'moved' for value in docs.values()) and bool(reports)
        record = {
            'time': datetime.now().astimezone().isoformat(timespec='seconds'),
            'attempt': attempt,
            'missing': missing,
            'docs': docs,
            'producer_reports': reports,
            'status': 'READY' if ready else 'WAIT',
        }
        line = json.dumps(record, sort_keys=True)
        print(line, flush=True)
        log.write(line + '\n')
        log.flush()
        if ready:
            raise SystemExit(0)
        if attempt < 40:
            time.sleep(20)
    print('ABSENT: readiness not observed within 40 tries', flush=True)
    log.write('ABSENT: readiness not observed within 40 tries\n')
    raise SystemExit(3)
