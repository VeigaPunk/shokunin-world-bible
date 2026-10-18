from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json
import re
import subprocess

ROOT = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
assert Path.cwd().resolve() == ROOT
WAVE = ROOT / '.ufo/waves/round-100'
SEATS = WAVE / 'seats'
SCRATCH = SEATS / 'V30-scratch'
SELF = 'V30'
BASELINE = 'fe1ce46'
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
PROTECTED = [
    'PROVINCE.md', 'SHONEN.md', 'README.md', 'l0-questions.md',
    'corpus/fixtures/check_bible.py', 'corpus/tools/dependency_freeze.py',
    'corpus/tools/support_check.py', 'corpus/tools/map_obligations.py',
    'corpus/tools/boundary_doc_check.py',
]


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT).decode().rstrip('\n')


def file_meta(path):
    data = path.read_bytes()
    stat = path.stat()
    return {
        'sha256': hashlib.sha256(data).hexdigest(),
        'bytes': len(data),
        'mtime_utc': datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat(),
    }


def seat_key(seat):
    return (seat[0], int(seat[1:]))


def audit():
    snapshot_utc = datetime.now(timezone.utc).isoformat()
    report_map = {}
    unexpected = []
    header_mismatches = []
    header_token_misses = []
    empty = []
    tiny = []
    conclusions = {}
    for path in sorted(SEATS.glob('*.md')):
        match = re.fullmatch(r'(T[1-4]|V[0-9]{2})-.+\.md', path.name)
        if not match:
            unexpected.append(path.name)
            continue
        seat = match[1]
        meta = file_meta(path)
        meta['path'] = str(path.relative_to(ROOT))
        report_map.setdefault(seat, []).append(meta)
        text = path.read_text(errors='replace')
        lines = text.splitlines()
        first_heading = next((line for line in lines[:20] if line.startswith('#')), '')
        meta['first_heading'] = first_heading
        header_seats = re.findall(r'\b(T[1-4]|V[0-9]{2})\b', first_heading)
        if header_seats and seat not in header_seats:
            header_mismatches.append({'seat': seat, 'path': meta['path'],
                                      'heading': first_heading})
        if not re.search(r'\b' + re.escape(seat) + r'\b', '\n'.join(lines[:20])):
            header_token_misses.append(meta['path'])
        meta['last_nonempty_line'] = next((line for line in reversed(lines) if line.strip()), '')
        conclusions.setdefault(seat, []).append(meta['last_nonempty_line'])
        if meta['bytes'] == 0:
            empty.append(meta['path'])
        elif meta['bytes'] < 200:
            tiny.append(meta['path'])
    present = sorted((seat for seat, rows in report_map.items()
                      if any(row['bytes'] for row in rows)), key=seat_key)
    others = [seat for seat in present if seat != SELF]
    duplicates = {seat: [row['path'] for row in rows]
                  for seat, rows in report_map.items() if len(rows) > 1}
    candidate = {}
    missing = []
    for rel in ARTIFACTS:
        path = ROOT / rel
        if path.is_file() and path.stat().st_size:
            candidate[rel] = file_meta(path)
        else:
            missing.append(rel)
    protected = {}
    for rel in PROTECTED:
        path = ROOT / rel
        live = file_meta(path)
        old = subprocess.check_output(['git', 'show', BASELINE + ':' + rel], cwd=ROOT)
        live['baseline_sha256'] = hashlib.sha256(old).hexdigest()
        live['same_as_baseline'] = live['sha256'] == live['baseline_sha256']
        protected[rel] = live
    contract_path = ROOT / ARTIFACTS[0]
    contract = json.loads(contract_path.read_text())
    old_contract = json.loads(subprocess.check_output(
        ['git', 'show', BASELINE + ':' + ARTIFACTS[0]], cwd=ROOT))
    pin_names = list(contract['pins'])
    inherited_changed = [name for name, pin in old_contract['pins'].items()
                         if contract['pins'].get(name) != pin]
    new_pins = sorted(set(contract['pins']) - set(old_contract['pins']))
    removed_pins = sorted(set(old_contract['pins']) - set(contract['pins']))
    top_changed = sorted(key for key in set(old_contract) | set(contract)
                         if key != 'pins' and old_contract.get(key) != contract.get(key))
    changed_tracked = git('diff', '--name-only', BASELINE, '--').splitlines()
    fixture = ROOT / 'corpus/fixtures/r100-docket-review'
    actual_fixture_files = sorted(path.name for path in fixture.iterdir() if path.is_file()) if fixture.exists() else []
    parent_wave = Path('/home/vgpnk/Projects/shokunin/.ufo/waves/round-100')
    parent_files = sorted(str(path) for path in parent_wave.rglob('*') if path.is_file()) if parent_wave.exists() else []
    poll_path = SCRATCH / 'poll-result.json'
    poll = json.loads(poll_path.read_text()) if poll_path.exists() else None
    result = {
        'snapshot_utc': snapshot_utc,
        'root': str(ROOT),
        'baseline_commit': git('rev-parse', BASELINE),
        'baseline_is_ancestor_of_head': subprocess.run(
            ['git', 'merge-base', '--is-ancestor', BASELINE, 'HEAD'], cwd=ROOT).returncode == 0,
        'head_at_snapshot': git('rev-parse', 'HEAD'),
        'git_status_short': git('status', '--short').splitlines(),
        'changed_tracked_since_baseline': changed_tracked,
        'collection': {
            'reports_expected': 32,
            'reports_present': len(present),
            'reports_present_excl_self': len(others),
            'reports_missing_count': max(0, 32 - len(present)),
            'reports_excess_count': max(0, len(present) - 32),
            'producer_count': sum(seat.startswith('T') for seat in present),
            'verifier_count': sum(seat.startswith('V') for seat in present),
            'present': present,
            'expected_roster_provided_by_dispatch': None,
            'missing_seat_ids_not_inferred': True,
            'scratch_directories_without_report_not_credited': sorted(
                path.name for path in SEATS.iterdir()
                if path.is_dir()
                and re.fullmatch(r'(T[1-4]|V[0-9]{2})-scratch', path.name)
                and path.name.split('-')[0] not in present),
            'producer_present': [seat for seat in ['T1', 'T2', 'T3', 'T4'] if seat in present],
            'producer_absent': [seat for seat in ['T1', 'T2', 'T3', 'T4'] if seat not in present],
            'duplicate_report_prefixes': duplicates,
            'header_seat_mismatches': header_mismatches,
            'header_token_misses_first20': header_token_misses,
            'empty_reports': empty,
            'tiny_reports_under_200_bytes': tiny,
            'unexpected_md_in_seats_dir': unexpected,
            'non_report_top_level': sorted(path.name for path in SEATS.iterdir()
                                           if not path.is_file() or path.suffix != '.md'),
            'parent_tree_files': parent_files,
            'conclusions_observed_not_adjudicated': conclusions,
        },
        'report_map': report_map,
        'candidate_revision_meta': candidate,
        'missing_candidate_paths': missing,
        'fixture_files': actual_fixture_files,
        'protected_files': protected,
        'pin_inventory': {
            'count': len(pin_names), 'names': pin_names,
            'new_pins': new_pins, 'removed_pins': removed_pins,
            'inherited_changed': inherited_changed,
            'top_level_changed_fields': top_changed,
            'r99_pin': contract['pins'].get('r99-window-lapse'),
        },
        'poll': poll,
    }
    return result


def build_receipt(data):
    rows = []
    for seat in sorted(data['report_map'], key=seat_key):
        reports = data['report_map'][seat]
        row = {
            'seat': seat,
            'agent_id': None,
            'outcome': None,
            'report_status': 'present' if any(report['bytes'] for report in reports) else 'empty',
            'report_path': reports[0]['path'] if len(reports) == 1 else None,
            'report_sha256': reports[0]['sha256'] if len(reports) == 1 else None,
            'reports': {Path(report['path']).name: report['sha256'] for report in reports},
            'bytes': sum(report['bytes'] for report in reports),
            'mtime_utc': max(report['mtime_utc'] for report in reports),
        }
        rows.append(row)
    collection = dict(data['collection'])
    collection.update({
        'snapshot_utc': data['snapshot_utc'],
        'snapshot_owner': 'V30-receipt-presence',
        'self_subtracted': True,
        'poll': data['poll'],
        'declared_producer_count': 4,
        'declared_verifier_count': 28,
        'declared_roster_status': 'MISMATCH' if len(rows) != 32 else 'UNRECONCILED_WITH_DISPATCH',
        'followup_evidence': {
            name: {'path': str((SCRATCH / name).relative_to(ROOT)),
                   'sha256': file_meta(SCRATCH / name)['sha256']}
            for name in ['followup-poll.json', 'roster-poll.json',
                         'stability.json', 'stability-final.json']
            if (SCRATCH / name).exists()
        },
        'snapshot_note': (
            'Presence and bytes only, not proof of report truth or completed dispatch. '
            'agent_id, outcome, dispatch metadata and served backend echo stay null for L1. '
            'The task declares 32 seats but all observed report rows are retained even when '
            'that count disagrees; no report is dropped to fit the declaration. '
            'Absent identifiers are not invented. SHA-256 rows are this snapshot only.'),
    })
    return {
        'record_type': 'round-100-receipt',
        'round': 100,
        'phase': 'single-wave-32-seat',
        'requested_model': 'openai-codex/gpt-6.1-sol',
        'dispatch_model_alias_declared': 'openai-codex/gpt-6.1-sol-max',
        'requested_effort': 'max',
        'requested_seats': 32,
        'dispatch_tool_call_id': None,
        'returned_summary': None,
        'served_backend_echo': None,
        'baseline_commit': data['baseline_commit'],
        'baseline_is_ancestor_of_head': data['baseline_is_ancestor_of_head'],
        'head_at_snapshot': data['head_at_snapshot'],
        'receipt_snapshot_utc': data['snapshot_utc'],
        'git_status_short': data['git_status_short'],
        'candidate_revision_pinned': {rel: meta['sha256'] for rel, meta in data['candidate_revision_meta'].items()},
        'candidate_revision_meta': data['candidate_revision_meta'],
        'missing_candidate_paths': data['missing_candidate_paths'],
        'fixture_files': data['fixture_files'],
        'pin_inventory': data['pin_inventory'],
        'protected_files': data['protected_files'],
        'collection_snapshot': collection,
        'known_seat_output_defects': [
            {'type': key, 'observed': collection[key]}
            for key in [
                'reports_excess_count', 'duplicate_report_prefixes',
                'header_seat_mismatches', 'header_token_misses_first20',
                'empty_reports', 'tiny_reports_under_200_bytes',
                'unexpected_md_in_seats_dir', 'parent_tree_files',
            ] if collection[key]
        ],
        'seats': rows,
        'state': 'skeleton — L1 must fill real dispatch metadata and agent IDs; no IDs invented',
        'l1_follow_up': [
            'Fill agent_id and outcome from the actual dispatch result, never from report existence.',
            'Fill dispatch_tool_call_id and returned_summary from the real single-wave dispatch.',
            'Reconcile the declared seat total against every observed report identifier; explain excess or missing outputs without dropping reports.',
            'Refresh report and candidate hashes after final report landings or closure edits.',
            'Adjudicate claims from verifier evidence; receipt presence does not admit the round.',
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--build-receipt', action='store_true')
    parser.add_argument('--label', default='snapshot')
    args = parser.parse_args()
    assert re.fullmatch(r'[a-z0-9-]+', args.label)
    data = audit()
    output = SCRATCH / (args.label + '-audit.json')
    assert output.resolve().is_relative_to(SCRATCH.resolve())
    with output.open('x') as handle:
        handle.write(json.dumps(data, indent=2) + '\n')
    if args.build_receipt:
        receipt_path = WAVE / 'receipt.json'
        assert receipt_path.resolve() == ROOT / '.ufo/waves/round-100/receipt.json'
        assert receipt_path.resolve().is_relative_to(ROOT)
        with receipt_path.open('x') as handle:
            handle.write(json.dumps(build_receipt(data), indent=2) + '\n')
    print(json.dumps({
        'snapshot_utc': data['snapshot_utc'],
        'reports_present': data['collection']['reports_present'],
        'reports_present_excl_self': data['collection']['reports_present_excl_self'],
        'reports_missing_count': data['collection']['reports_missing_count'],
        'present': data['collection']['present'],
        'producer_absent': data['collection']['producer_absent'],
        'candidate_paths_present': len(data['candidate_revision_meta']),
        'missing_candidate_paths': data['missing_candidate_paths'],
        'duplicates': data['collection']['duplicate_report_prefixes'],
        'empty_reports': data['collection']['empty_reports'],
        'header_seat_mismatches': data['collection']['header_seat_mismatches'],
        'header_token_misses': data['collection']['header_token_misses_first20'],
        'unexpected_md': data['collection']['unexpected_md_in_seats_dir'],
        'parent_tree_files': data['collection']['parent_tree_files'],
        'pin_count': data['pin_inventory']['count'],
        'new_pins': data['pin_inventory']['new_pins'],
        'inherited_pins_changed': data['pin_inventory']['inherited_changed'],
        'protected_files_changed': [rel for rel, meta in data['protected_files'].items() if not meta['same_as_baseline']],
        'audit_path': str(output.relative_to(ROOT)),
        'receipt_written': args.build_receipt,
    }, indent=2))


if __name__ == '__main__':
    main()
