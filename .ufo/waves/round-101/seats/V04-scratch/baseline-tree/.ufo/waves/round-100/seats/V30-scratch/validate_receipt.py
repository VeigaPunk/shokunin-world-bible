from pathlib import Path
import hashlib
import json
import re
import sys

ROOT = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
assert Path.cwd().resolve() == ROOT
path = ROOT / '.ufo/waves/round-100/receipt.json'
assert path.resolve().is_relative_to(ROOT)
receipt = json.loads(path.read_text())
collection = receipt['collection_snapshot']
rows = receipt['seats']
errors = []


def check(ok, message):
    if not ok:
        errors.append(message)


check(receipt['round'] == 100, 'wrong round')
check(receipt['requested_seats'] == 32, 'wrong declared seat count')
check(receipt['requested_model'] == 'openai-codex/gpt-6.1-sol', 'wrong requested model')
check(receipt['requested_effort'] == 'max', 'wrong effort')
check(receipt['baseline_is_ancestor_of_head'], 'baseline is not an ancestor')
check(receipt['dispatch_tool_call_id'] is None, 'dispatch ID must remain null for L1')
check(receipt['returned_summary'] is None, 'dispatch summary must remain null for L1')
check(receipt['served_backend_echo'] is None, 'served backend must not be inferred')
check(all(row['agent_id'] is None and row['outcome'] is None for row in rows),
      'agent IDs or outcomes were invented')
ids = [row['seat'] for row in rows]
check(len(ids) == len(set(ids)), 'duplicate seat rows')
check(set(ids) == set(collection['present']), 'collection and seat rows disagree')
check(len(rows) == collection['reports_present'], 'row and report counts disagree')
check(collection['reports_present_excl_self'] == len(set(ids) - {'V30'}),
      'self-subtracted count is wrong')
check(collection['self_subtracted'] is True, 'self-subtracted marker missing')
check(collection['producer_present'] == ['T1', 'T2', 'T3', 'T4'], 'producer report absent')
check(not collection['producer_absent'], 'missing producer was hidden')
check(not receipt['missing_candidate_paths'], 'candidate artifact absent')
check(len(receipt['candidate_revision_pinned']) == 16, 'candidate path count is not 16')
check(receipt['pin_inventory']['count'] == 7, 'pin count is not 7')
check(receipt['pin_inventory']['new_pins'] == ['r99-window-lapse'], 'wrong new pin')
check(not receipt['pin_inventory']['removed_pins'], 'inherited pin removed')
check(not receipt['pin_inventory']['inherited_changed'], 'inherited pin altered')
check(receipt['pin_inventory']['top_level_changed_fields'] == ['revision'],
      'unexpected non-pin contract change')
check(all(meta['same_as_baseline'] for meta in receipt['protected_files'].values()),
      'protected file changed')
for key in ['duplicate_report_prefixes', 'header_seat_mismatches',
            'header_token_misses_first20', 'empty_reports',
            'tiny_reports_under_200_bytes', 'unexpected_md_in_seats_dir',
            'parent_tree_files']:
    check(not collection[key], key + ' is nonempty')
report_hashes_checked = 0
for row in rows:
    check(row['report_status'] == 'present', row['seat'] + ' is not present')
    check(bool(row['report_path']), row['seat'] + ' lacks one report path')
    if not row['report_path']:
        continue
    report_path = ROOT / row['report_path']
    check(report_path.resolve().is_relative_to(ROOT / '.ufo/waves/round-100/seats'),
          row['seat'] + ' report escaped seats directory')
    data = report_path.read_bytes()
    check(hashlib.sha256(data).hexdigest() == row['report_sha256'],
          row['seat'] + ' report hash changed after snapshot')
    check(len(data) == row['bytes'], row['seat'] + ' report size changed')
    check(re.fullmatch(r'[0-9a-f]{64}', row['report_sha256']) is not None,
          row['seat'] + ' hash is malformed')
    report_hashes_checked += 1
artifact_hashes_checked = 0
for rel, digest in receipt['candidate_revision_pinned'].items():
    artifact_path = ROOT / rel
    check(artifact_path.resolve().is_relative_to(ROOT), rel + ' escaped lane')
    data = artifact_path.read_bytes()
    check(hashlib.sha256(data).hexdigest() == digest, rel + ' artifact hash changed')
    check(len(data) == receipt['candidate_revision_meta'][rel]['bytes'],
          rel + ' artifact size changed')
    artifact_hashes_checked += 1
live = {}
for report_path in (ROOT / '.ufo/waves/round-100/seats').glob('*.md'):
    match = re.fullmatch(r'(T[1-4]|V[0-9]{2})-.+\.md', report_path.name)
    if match and report_path.stat().st_size:
        live.setdefault(match[1], []).append(report_path.name)
check(set(live) == set(ids), 'live report set changed after receipt snapshot')
poll = collection['poll']
check(poll is not None, 'bounded poll record missing')
if poll:
    check(poll['self_subtracted'] is True, 'poll counted self')
    check(poll['cadence_seconds'] == 20, 'poll cadence changed')
    check(poll['endgame_limit_seconds'] == 1200, 'poll bound changed')
    check(poll['elapsed_seconds'] <= 1202, 'poll exceeded the bounded stall escape')
    check(poll['stopped_reason'] in [
        'threshold_met_30_others_and_producer_artifacts',
        'bounded_20_minute_stall_escape'], 'unknown poll stop reason')
summary = {
    'receipt': str(path.relative_to(ROOT)),
    'receipt_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
    'declared_reports': 32,
    'observed_reports': len(rows),
    'report_hashes_checked': report_hashes_checked,
    'artifact_hashes_checked': artifact_hashes_checked,
    'agent_ids_null': all(row['agent_id'] is None for row in rows),
    'outcomes_null': all(row['outcome'] is None for row in rows),
    'self_subtracted': collection['self_subtracted'],
    'errors': errors,
    'structural_result': 'PASS' if not errors else 'FAIL',
    'full_declared_presence': len(rows) == 32,
}
print(json.dumps(summary, indent=2))
if errors:
    sys.exit(1)
if len(rows) != 32:
    sys.exit(2)
