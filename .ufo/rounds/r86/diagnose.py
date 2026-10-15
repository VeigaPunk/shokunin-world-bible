#!/usr/bin/env python3
"""Measure inherited, unadmitted lore work; not a round-admission authority."""
import copy
import hashlib
import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tarfile
import tempfile

ROOT = Path(__file__).resolve().parents[3]
BASELINE = '5eb9451baff217c19d5786405f9b2aa500b7c1b7'
CHECKER = Path('corpus/fixtures/check_bible.py')
PROBES = Path('corpus/live/runs/round-85/probe-inputs')
NOTICE = ('provenance continuity and tick-order comparisons unassessed at this '
          'and all later records because holder identity is ambiguous')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(root, target):
    command = [sys.executable, str(CHECKER), str(target)]
    result = subprocess.run(command, cwd=root, capture_output=True, text=True)
    return {'command': command, 'returncode': result.returncode,
            'stdout': result.stdout, 'stderr': result.stderr}


def triple(row):
    return row['returncode'], row['stdout'], row['stderr']


def main():
    candidate_sha = sha(ROOT / CHECKER)
    archive = subprocess.run(['git', 'archive', BASELINE, 'corpus'], cwd=ROOT,
                             check=True, capture_output=True).stdout
    with tempfile.TemporaryDirectory(prefix='lore-r86-diagnostic-') as temporary:
        scratch = Path(temporary)
        before = scratch / 'baseline'
        before.mkdir()
        with tarfile.open(fileobj=io.BytesIO(archive)) as bundle:
            bundle.extractall(before, filter='data')
        inputs = sorted(path for path in (before / 'corpus').rglob('*.json'))
        changed_inputs = [str(path.relative_to(before)) for path in inputs
                          if not (ROOT / path.relative_to(before)).is_file()
                          or path.read_bytes() != (ROOT / path.relative_to(before)).read_bytes()]
        replay = []
        for path in sorted((before / 'corpus/fixtures').iterdir()):
            if path.is_dir():
                target = path.relative_to(before)
                old, new = run(before, target), run(ROOT, target)
                replay.append({'case': path.name, 'same': triple(old) == triple(new),
                               'before': old, 'candidate': new})
        probes = []
        for name in ('r85-control', 'r85-unique-break-control', 'r85-masked-ambiguous',
                     'r85-isolated-ambiguous', 'r85-harbor-repro'):
            probes.append({'case': name, 'before': run(before, PROBES / name),
                           'candidate': run(ROOT, PROBES / name)})

        control = json.loads((before / PROBES / 'r85-control/entities.json').read_text())
        masked = json.loads((before / PROBES / 'r85-masked-ambiguous/entities.json').read_text())
        scenarios = {}
        destination = copy.deepcopy(masked)
        destination[3]['provenance'].append({'tick': 4, 'from_holder': 'mira',
                                           'to_holder': 'harbor', 'source_id': 'archive-ledger'})
        scenarios['ambiguous-to-with-late-break-and-tick'] = destination
        origin = copy.deepcopy(control)
        vault = {'id': 'vault', 'kind': 'place', 'name': 'Vault',
                 'first_appearance': 'archive-ledger', 'claims': []}
        origin.extend([copy.deepcopy(vault), copy.deepcopy(vault)])
        origin[3]['provenance'][1].update(from_holder='vault', to_holder='tower')
        origin[3]['provenance'][2].update(from_holder='tower', to_holder='harbor')
        origin[3]['provenance'].append({'tick': 4, 'from_holder': 'mira',
                                      'to_holder': 'tower', 'source_id': 'archive-ledger'})
        scenarios['ambiguous-from-with-late-break-and-tick'] = origin
        prior_invalid = copy.deepcopy(destination)
        prior_invalid[3]['provenance'][0]['extra'] = 'scratch-only malformed record'
        scenarios['earlier-invalid-then-ambiguity'] = prior_invalid
        both = copy.deepcopy(destination)
        both[3]['provenance'][1]['from_holder'] = 'vault'
        scenarios['both-holder-fields-ambiguous'] = both
        independent = copy.deepcopy(destination)
        second = copy.deepcopy(independent[3])
        second.update(id='second-item', name='Second item')
        independent.append(second)
        third = copy.deepcopy(control[3])
        third.update(id='unique-broken-item', name='Unique broken item')
        third['provenance'][2]['from_holder'] = 'mira'
        independent.append(third)
        scenarios['per-item-reset-and-independent-break'] = independent
        prefix = copy.deepcopy(destination)
        prefix[3]['provenance'][0]['from_holder'] = 'tower'
        scenarios['definite-prefix-before-ambiguity'] = prefix
        dangling = copy.deepcopy(control)
        dangling[3]['provenance'][1]['to_holder'] = 'missing-to'
        dangling[3]['provenance'][2]['from_holder'] = 'missing-from'
        scenarios['dangling-both-directions'] = dangling
        matrix = []
        for name, entities in scenarios.items():
            target = scratch / name
            shutil.copytree(before / PROBES / 'r85-control', target)
            (target / 'entities.json').write_text(json.dumps(entities, indent=2) + '\n')
            matrix.append({'case': name, 'candidate': run(ROOT, target)})

        by_probe = {row['case']: row for row in probes}
        by_case = {row['case']: row['candidate'] for row in matrix}
        flags = {
            'inherited_input_json_unchanged': not changed_inputs,
            'all_inherited_fixture_tuples_unchanged': all(row['same'] for row in replay),
            'unique_clean_control_unchanged': triple(by_probe['r85-control']['before']) == triple(by_probe['r85-control']['candidate']),
            'unique_break_control_unchanged': triple(by_probe['r85-unique-break-control']['before']) == triple(by_probe['r85-unique-break-control']['candidate']),
            'baseline_mask_has_no_holder_disclosure': '.to_holder: ambiguous entity' not in by_probe['r85-masked-ambiguous']['before']['stdout'] and NOTICE not in by_probe['r85-masked-ambiguous']['before']['stdout'],
        }
        for name, field in (('ambiguous-to-with-late-break-and-tick', 'to_holder'),
                            ('ambiguous-from-with-late-break-and-tick', 'from_holder')):
            row = by_case[name]
            text = row['stdout']
            flags[name] = (row['returncode'] == 1 and row['stderr'] == ''
                           and f"entities[3].provenance[1].{field}: ambiguous entity 'vault'" in text
                           and text.count(NOTICE) == 1
                           and 'provenance chain break' not in text
                           and 'must be greater than previous tick' not in text)
        flags['notice_after_earlier_invalidity'] = (by_case['earlier-invalid-then-ambiguity']['stdout'].count(NOTICE) == 1
                                                    and 'expected exactly tick, from_holder, to_holder, source_id' in by_case['earlier-invalid-then-ambiguity']['stdout'])
        text = by_case['both-holder-fields-ambiguous']['stdout']
        flags['both_fields_and_one_notice'] = ("provenance[1].from_holder: ambiguous entity 'vault'" in text
                                               and "provenance[1].to_holder: ambiguous entity 'vault'" in text
                                               and text.count(NOTICE) == 1)
        text = by_case['per-item-reset-and-independent-break']['stdout']
        flags['per_item_reset_and_independent_break'] = (text.count(NOTICE) == 2
                                                        and 'entities[7].provenance[2]: provenance chain break' in text)
        flags['prefix_break_retained'] = ('entities[3].provenance[0]: provenance chain break; first record must have from_holder null'
                                          in by_case['definite-prefix-before-ambiguity']['stdout'])
        text = by_case['dangling-both-directions']['stdout']
        flags['dangling_not_reclassified'] = ("to_holder: dangling entity 'missing-to'" in text
                                               and "from_holder: dangling entity 'missing-from'" in text
                                               and NOTICE not in text and 'ambiguous entity' not in text)
        flags['checker_unchanged_during_measurement'] = sha(ROOT / CHECKER) == candidate_sha
        verdict = 'PASS' if all(flags.values()) else 'FAIL'
        summary = {
            'fixture_count': len(replay),
            'same_fixture_tuples': sum(row['same'] for row in replay),
            'baseline_exit_counts': {str(code): sum(row['before']['returncode'] == code for row in replay) for code in (0, 1)},
            'changed_fixture_cases': [row['case'] for row in replay if not row['same']],
            'inherited_json_count': len(inputs),
            'changed_inherited_json': changed_inputs,
            'probe_count': len(probes), 'scratch_scenarios': len(matrix),
            'empty_stderr_all': all(not row[side]['stderr'] for row in replay + probes for side in ('before', 'candidate')) and all(not row['candidate']['stderr'] for row in matrix),
        }
        output = {'schema': 'lore-r86-inherited-diagnostic-v1',
                  'baseline_commit': BASELINE,
                  'baseline_checker_sha256': sha(before / CHECKER),
                  'candidate_checker_sha256': candidate_sha,
                  'candidate_status': 'dirty inherited unadmitted worktree; not a committed implementation',
                  'summary': summary, 'observations': flags,
                  'verdict_lines': [f'INHERITED_CANDIDATE_DIAGNOSTIC: {verdict}',
                                    'ROUND_ADMISSION: BLOCKED required_alias_bindings_missing; native_task_batches=0; no_native_judgment',
                                    'PROTOCOL_GATE_CONFORMANCE: COULD_NOT_EVALUATE missing_SKILL_registry_and_selftest'],
                  'fixture_runs': replay, 'probe_runs': probes, 'scratch_runs': matrix}
        print(json.dumps(output, indent=2))
        return 0 if verdict == 'PASS' else 1


if __name__ == '__main__':
    raise SystemExit(main())
