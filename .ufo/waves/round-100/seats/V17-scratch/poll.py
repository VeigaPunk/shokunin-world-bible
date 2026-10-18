import datetime
import json
import time
from pathlib import Path

ROOT = Path('/home/vgpnk/Projects/shokunin/lore-shokunin').resolve()
SCRATCH = ROOT / '.ufo/waves/round-100/seats/V17-scratch'
SEATS = ROOT / '.ufo/waves/round-100/seats'
FIXTURE = ROOT / 'corpus/fixtures/r100-docket-review'
FILES = (
    'entities.json', 'relations.json', 'timeline.json', 'sources.json',
    'contradictions.json', 'README.md', 'claim-excerpt-map.md',
    'fictional-excerpts.md', 'inspiration-note.md', 'source-excerpt.md',
)
KNOWLEDGE = (
    'corpus/knowledge/r100-crossing-arc-synthesis.md',
    'corpus/knowledge/r100-provenance-semantics-boundary.md',
    'corpus/knowledge/r99-gate-blind-spot-table.md',
)
start = 1
if (SCRATCH / 'poll-status.json').is_file():
    previous = json.loads((SCRATCH / 'poll-status.json').read_text())
    start = previous['try'] + 1
    elapsed = datetime.datetime.now(datetime.timezone.utc).timestamp() - datetime.datetime.fromisoformat(previous['time']).timestamp()
    time.sleep(max(0, 20 - elapsed))
    print('POLL-RESUME after local schema correction; next_try=' + str(start), flush=True)
for attempt in range(start, 41):
    missing = [str((FIXTURE / name).relative_to(ROOT)) for name in FILES if not (FIXTURE / name).is_file()]
    missing += [name for name in KNOWLEDGE if not (ROOT / name).is_file()]
    reports = {seat: sorted(str(p.relative_to(ROOT)) for p in SEATS.glob(seat + '*.md') if p.is_file()) for seat in ('T1', 'T2', 'T3', 'T4')}
    missing_reports = [seat for seat, paths in reports.items() if not paths]
    try:
        contract = json.loads((ROOT / 'corpus/tools/dependency-freeze-contract.json').read_text())
        pin_present = 'r99-window-lapse' in contract.get('pins', {})
        contract_keys = list(contract)
    except (OSError, ValueError) as error:
        pin_present = False
        contract_keys = [str(error)]
    if not pin_present:
        missing.append('dependency-freeze-contract.json: r99-window-lapse fixture pin')
    state = {
        'try': attempt,
        'time': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'missing_artifacts': missing,
        'missing_reports': missing_reports,
        'reports': reports,
        'contract_keys': contract_keys,
        'ready': not missing and not missing_reports,
    }
    print(json.dumps(state, sort_keys=True), flush=True)
    (SCRATCH / 'poll-status.json').write_text(json.dumps(state, indent=2) + '\n')
    if state['ready']:
        print('POLL-READY try=' + str(attempt), flush=True)
        raise SystemExit(0)
    if attempt < 40:
        time.sleep(20)
print('POLL-EXHAUSTED try=40', flush=True)
raise SystemExit(3)
