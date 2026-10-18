from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re
import time

ROOT = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
assert Path.cwd().resolve() == ROOT
SEATS = ROOT / '.ufo/waves/round-100/seats'
SELF = 'V30'
SCRATCH = SEATS / 'V30-scratch'
assert SCRATCH.resolve().is_relative_to(ROOT)
ARTIFACTS = [
    'corpus/tools/dependency-freeze-contract.json',
    'corpus/tools/README.md',
    'SKILL.md',
    *['corpus/fixtures/r100-docket-review/' + name for name in [
        'README.md', 'claim-excerpt-map.md', 'contradictions.json',
        'entities.json', 'fictional-excerpts.md', 'inspiration-note.md',
        'relations.json', 'source-excerpt.md', 'sources.json', 'timeline.json',
    ]],
    'corpus/knowledge/r100-crossing-arc-synthesis.md',
    'corpus/knowledge/r100-provenance-semantics-boundary.md',
    'corpus/knowledge/r99-gate-blind-spot-table.md',
]
PRODUCERS = ['T1', 'T2', 'T3', 'T4']


def snapshot():
    grouped = {}
    unexpected = []
    for path in sorted(SEATS.glob('*.md')):
        match = re.fullmatch(r'(T[1-4]|V[0-9]{2})-.+\.md', path.name)
        if not match:
            unexpected.append(path.name)
            continue
        data = path.read_bytes()
        grouped.setdefault(match[1], []).append({
            'path': str(path.relative_to(ROOT)),
            'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest(),
        })
    nonempty = sorted(seat for seat, entries in grouped.items()
                      if any(entry['bytes'] > 0 for entry in entries))
    others = [seat for seat in nonempty if seat != SELF]
    missing_artifacts = [rel for rel in ARTIFACTS
                         if not (ROOT / rel).is_file()
                         or (ROOT / rel).stat().st_size == 0]
    try:
        contract = json.loads((ROOT / ARTIFACTS[0]).read_text())
        r99_pinned = 'r99-window-lapse' in contract.get('pins', {})
        contract_error = None
    except (OSError, ValueError) as error:
        r99_pinned = False
        contract_error = str(error)
    return {
        'utc': datetime.now(timezone.utc).isoformat(),
        'reports_present': len(nonempty),
        'reports_present_excl_self': len(others),
        'present': nonempty,
        'producer_missing': [seat for seat in PRODUCERS if seat not in nonempty],
        'artifact_missing': missing_artifacts,
        'r99_pin_present': r99_pinned,
        'contract_error': contract_error,
        'self_subtracted': True,
        'duplicates': {seat: entries for seat, entries in grouped.items()
                       if len(entries) > 1},
        'empty_reports': [entry['path'] for entries in grouped.values()
                          for entry in entries if entry['bytes'] == 0],
        'unexpected_md': unexpected,
        'reports': grouped,
    }


def main():
    start = time.monotonic()
    stop = start + 1200
    artifacts_ready_try = None
    phase_40_state = None
    records = []
    try_number = 0
    with (SCRATCH / 'poll.jsonl').open('x') as log:
        while True:
            try_number += 1
            state = snapshot()
            state.update(try_number=try_number,
                         elapsed_seconds=round(time.monotonic() - start, 3))
            ready = (not state['producer_missing']
                     and not state['artifact_missing']
                     and state['r99_pin_present'])
            if ready and artifacts_ready_try is None:
                artifacts_ready_try = try_number
            if try_number == 40:
                phase_40_state = state
            records.append(state)
            log.write(json.dumps(state, sort_keys=True) + '\n')
            log.flush()
            summary = {key: state[key] for key in [
                'utc', 'try_number', 'elapsed_seconds',
                'reports_present_excl_self', 'producer_missing',
                'artifact_missing', 'r99_pin_present',
            ]}
            print(json.dumps(summary, sort_keys=True), flush=True)
            if ready and state['reports_present_excl_self'] >= 30:
                reason = 'threshold_met_30_others_and_producer_artifacts'
                break
            if time.monotonic() >= stop:
                reason = 'bounded_20_minute_stall_escape'
                break
            time.sleep(min(20, max(0, stop - time.monotonic())))
    result = {
        'cadence_seconds': 20,
        'producer_protocol_max_tries': 40,
        'endgame_limit_seconds': 1200,
        'endgame_threshold_others': 30,
        'self_subtracted': True,
        'tries_run': try_number,
        'artifacts_ready_try': artifacts_ready_try,
        'producer_protocol_exhausted_without_ready': (
            phase_40_state is not None and artifacts_ready_try is None),
        'phase_40_state': phase_40_state,
        'stopped_reason': reason,
        'elapsed_seconds': round(time.monotonic() - start, 3),
        'final': state,
    }
    with (SCRATCH / 'poll-result.json').open('x') as result_file:
        result_file.write(json.dumps(result, indent=2) + '\n')
    print(json.dumps({key: value for key, value in result.items()
                      if key not in ['phase_40_state', 'final']}, sort_keys=True),
          flush=True)


if __name__ == '__main__':
    main()
