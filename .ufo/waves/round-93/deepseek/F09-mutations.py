#!/usr/bin/env python3
"""F09 mutation controls, v2: full-cell edits through the embedded replay (stdlib only)."""
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
OUT = ROOT / '.ufo/waves/round-93/deepseek/F09-mutations.json'
DOSSIER_REL = 'corpus/knowledge/r93-r8-worked-example.md'
os.chdir(ROOT)
dossier = Path(DOSSIER_REL).read_text(encoding='utf-8')
py_blocks = re.findall(r"<<'PY'\n(.*?)\nPY\n", dossier, re.S)
replay = py_blocks[-1]

start = dossier.index('### Corrected illustrative R8 review record')
end = dossier.index('\n### Corrected replay')
head, corr, tail = dossier[:start], dossier[start:end], dossier[end:]


def full_cell(field, new):
    pat = re.compile(r'(?m)^\| ' + re.escape(field) + r' \| .*\|$')
    text, n = pat.subn('| ' + field + ' | ' + new + ' |', corr, count=1)
    assert n == 1, field
    return text


cases = {
    'blank_cell_full': full_cell('Gate result', ''),
    'dash_cell': full_cell('Gate result', '-'),
    'filler_cell': full_cell('Owner', 'TODO placeholder'),
    'scope_inversion': full_cell('Scope / disposition',
        corr.split('| Scope / disposition | ', 1)[1].split(' |', 1)[0]
            .replace('Withhold the whole element from supported canon',
                     'Keep the whole element in supported canon')),
    'scope_appended_contradiction': full_cell('Scope / disposition',
        corr.split('| Scope / disposition | ', 1)[1].split(' |', 1)[0]
            + ' The whole element should remain in supported canon with an uncertainty notice.'),
    'trigger_inverted': full_cell('Trigger',
        corr.split('| Trigger | ', 1)[1].split(' |', 1)[0]
            .replace('Both conjuncts are required', 'Only one conjunct is required')),
}

report = {'cases': []}
with tempfile.TemporaryDirectory(dir=str(OUT.parent)) as td:
    td = Path(td)
    script = td / 'F09-replay.py'
    script.write_text(replay, encoding='utf-8')
    for label, section in cases.items():
        cand = td / f'F09-candidate-{label}.md'
        cand.write_text(head + section + tail, encoding='utf-8')
        proc = subprocess.run([sys.executable, str(script)], capture_output=True, text=True,
                              env=dict(os.environ, D2_DOSSIER=str(cand)), cwd=ROOT)
        report['cases'].append({'case': label, 'exit': proc.returncode,
                                'stdout': proc.stdout, 'stderr': proc.stderr})

# sanity: baseline unmutated still passes through the extracted replay
with tempfile.TemporaryDirectory(dir=str(OUT.parent)) as td2:
    script = Path(td2) / 'F09-replay.py'
    script.write_text(replay, encoding='utf-8')
    proc = subprocess.run([sys.executable, str(script)], capture_output=True, text=True,
                          env=dict(os.environ, D2_DOSSIER=DOSSIER_REL), cwd=ROOT)
    report['baseline_control'] = {'exit': proc.returncode, 'stdout': proc.stdout, 'stderr': proc.stderr}

OUT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
for c in report['cases']:
    print(f"{c['case']}: exit={c['exit']} :: {c['stdout'].strip().splitlines()[:2]}")
print('baseline_control:', report['baseline_control']['exit'], report['baseline_control']['stdout'].strip().splitlines()[:2])
print('wrote', OUT)
