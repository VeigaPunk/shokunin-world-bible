#!/usr/bin/env python3
"""F09 scoped evidence runner for the r93 R8 dossier (stdlib only, read-only on product files).

Runs every ```sh block embedded in corpus/knowledge/r93-r8-worked-example.md,
recomputes the canonical-record digest through a parser independent of the
dossier's own code, and re-runs the mutation controls through the embedded
replay extracted from the corrected block. Writes F09-evidence.json only.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
OUT = ROOT / '.ufo/waves/round-93/deepseek/F09-evidence.json'
DOSSIER_REL = 'corpus/knowledge/r93-r8-worked-example.md'
TABLE_REL = 'corpus/knowledge/r88-sourced-inspiration-decision-table.md'
FIELDS = (
    'Element and scope pointer', 'Creator account', 'Reviewer / record date',
    'Gate result', 'Contrary evidence', 'Separability rationale',
    'Scope / disposition', 'Next action', 'Owner', 'Trigger',
    'Inspiration note target', 'Element-map target',
)

os.chdir(ROOT)
report = {
    'revision': subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip(),
    'dossier_sha256': hashlib.sha256(Path(DOSSIER_REL).read_bytes()).hexdigest(),
    'table_sha256': hashlib.sha256(Path(TABLE_REL).read_bytes()).hexdigest(),
    'shell_blocks': [],
    'digest_check': {},
    'mutations': [],
    'markers': {},
}

dossier = Path(DOSSIER_REL).read_text(encoding='utf-8')
table = Path(TABLE_REL).read_text(encoding='utf-8')

# ---- 1. run every embedded sh block ----
blocks = re.findall(r'```sh\n(.*?)```', dossier, re.S)
env = dict(os.environ, D2_DOSSIER=DOSSIER_REL)
for i, block in enumerate(blocks, 1):
    proc = subprocess.run(['bash', '-c', block], capture_output=True, text=True, env=env, cwd=ROOT)
    report['shell_blocks'].append({
        'block': i,
        'head': block.strip().splitlines()[0][:120],
        'exit': proc.returncode,
        'stdout': proc.stdout,
        'stderr': proc.stderr,
    })

# ---- 2. independent digest recomputation (separate parser from the dossier's) ----
def slice_record(text):
    marker = '### Corrected illustrative R8 review record'
    tail = text.split(marker, 1)[1]
    tail = tail.split('\n### Corrected replay', 1)[0]
    rows = {}
    for line in tail.splitlines():
        s = line.strip()
        if not (s.startswith('|') and s.endswith('|')):
            continue
        parts = [c.strip() for c in s[1:-1].split('|')]
        if len(parts) != 2:
            continue
        if all(set(p) <= set('-: ') and p for p in parts):
            continue
        rows.setdefault(parts[0], []).append(parts[1])
    return rows

rows = slice_record(dossier)
missing = [f for f in FIELDS if f not in rows or len(rows[f]) != 1]
values = [re.sub(r'\s+', ' ', rows[f][0]).strip() for f in FIELDS] if not missing else []
payload = json.dumps(values, ensure_ascii=False, separators=(',', ':')).encode('utf-8')
independent = hashlib.sha256(payload).hexdigest()
literal = re.search(r"EXPECTED_RECORD_SHA256 = '([0-9a-f]{64})'", dossier)
assignments = re.findall(r'EXPECTED_RECORD_SHA256\s*=\s*([^\n]+)', dossier)
report['digest_check'] = {
    'record_rows_found': len(rows),
    'missing_or_duplicated': missing,
    'independent_digest': independent,
    'literal_in_dossier': literal.group(1) if literal else None,
    'match': bool(literal) and independent == literal.group(1),
    'assignment_lines': assignments,
    'payload_preview': payload.decode('utf-8')[:200],
}

# ---- 3. mutation controls through the embedded replay ----
py_blocks = re.findall(r"<<'PY'\n(.*?)\nPY\n", dossier, re.S)
report['python_payload_blocks'] = len(py_blocks)
replay_code = py_blocks[-1] if py_blocks else None

corr_start = dossier.index('### Corrected illustrative R8 review record')
corr_end = dossier.index('\n### Corrected replay')
head, corr, tail = dossier[:corr_start], dossier[corr_start:corr_end], dossier[corr_end:]

def mutate(old, new, label, section='corrected'):
    """Replace first occurrence of old inside the corrected record section."""
    assert old in corr, f'mutation anchor missing: {label}'
    text = head + corr.replace(old, new, 1) + tail
    return text, label

cases = [
    mutate('| Gate result | R2 unavailable.', '| Gate result | ', 'blank_gate_result'),
    mutate('| Owner | Normative owner:', '| Owner | TODO placeholder', 'filler_owner'),
    mutate('| Scope / disposition | Withhold the whole element',
           '| Scope / disposition | The whole element should remain in supported canon with an uncertainty notice. Withhold the whole element',
           'scope_contradiction'),
    mutate('R2 unavailable. The hypothetical creator', 'R2    unavailable. The hypothetical creator', 'whitespace_only'),
]

if replay_code:
    with tempfile.TemporaryDirectory(dir=str(OUT.parent)) as td:
        td = Path(td)
        script = td / 'F09-replay.py'
        script.write_text(replay_code, encoding='utf-8')
        for text, label in cases:
            cand = td / f'F09-candidate-{label}.md'
            cand.write_text(text, encoding='utf-8')
            penv = dict(os.environ, D2_DOSSIER=str(cand))
            proc = subprocess.run([sys.executable, str(script)], capture_output=True, text=True,
                                  env=penv, cwd=ROOT)
            report['mutations'].append({
                'case': label, 'exit': proc.returncode,
                'stdout': proc.stdout, 'stderr': proc.stderr,
            })

# ---- 4. marker/supersession census ----
for marker in ('### Corrected illustrative R8 review record', '### Corrected replay',
               '## Illustrative R8 review record', '## Replay instructions',
               '## Record-to-decision crosswalk', 'This dated correction supersedes',
               'use only this corrected record and replay below',
               '### R8 appendix', '### R9 appendix'):
    report['markers'][marker] = dossier.count(marker)

# ---- 5. delivered R8 appendix slice checks (source_checks strings) ----
r8 = table.split('### R8 appendix', 1)[1].split('### R9 appendix', 1)[0]
report['appendix_slice_lines'] = len(r8.splitlines())
report['appendix_checks'] = {t: (t in r8) for t in (
    '**Owner:** the lore integration editor records the two-part R2 gate result',
    '**Trigger:** either R2 condition fails or remains unresolved, and the reviewer cannot separate',
    'in the inspiration note and element map',
    'withhold the **whole element from supported canon**',
    'same seven threshold names in the same order as *Kesh Hymn* lines 12–19',
    'creator denies using a source',
    'no independently authored, supportable remainder survives removing that sequence',
    'does not itself prove copying or source use',
)}
report['r2_conjunct_phrases'] = {
    'BOTH_creator_account': 'requires BOTH the creator' in r8,
    'either_R2_condition_fails': 'either R2 condition fails or remains unresolved' in r8,
    'both_R2_conditions_pass': 'both R2 conditions pass' in r8,
}

OUT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print(json.dumps({k: report[k] for k in ('revision', 'dossier_sha256', 'table_sha256')}, indent=2))
for b in report['shell_blocks']:
    print(f"block {b['block']} exit={b['exit']} :: {b['head']}")
print(json.dumps(report['digest_check'], indent=2))
for m in report['mutations']:
    print(f"mutation {m['case']} exit={m['exit']} stdout={m['stdout'].strip()!r}")
print('markers:', json.dumps(report['markers']))
print('appendix checks:', json.dumps(report['appendix_checks']))
print('conjunct phrases:', json.dumps(report['r2_conjunct_phrases']))
print('wrote', OUT)
