# CB-audit — Round 93

## Work performed

Axes audited:
- **C1 document parity:** independently re-check the r92 boundary-document repair against the r91 Q91-001/002 forensic findings, with Q91-003's boundary-related README note as adjacent debt.
- **Certification strength:** run CERT's proposed checker and test whether its result enforces B3's contract.
- **Evidence integrity:** replay the C9 fixtures and verify the delivered document/checker state without modifying tracked files.

Read the r93 wave spec, r91 Q1 debt ledger, r92 CB-audit receipt, B3 certification specification, r92 D1/D2 boundary artifacts, current boundary document, and delivered checker. The CERT artifact arrived as `.ufo/waves/round-93/patches/CERT-tool.patch`; its report and materialized `corpus/tools/boundary_doc_check.py` were absent. The helper found the actual patch path immediately:

```sh
sh .ufo/waves/poll_wait.sh .ufo/waves/round-93/patches/CERT-tool.patch 1200
```

```text
POLL_HIT path=.ufo/waves/round-93/patches/CERT-tool.patch elapsed=0s checks=0
```

Executed the Python tool source directly from the patch in memory, from the repository root; it was not applied to the worktree. No tracked file was changed. Disposable contradiction/hash probes used automatically cleaned `/tmp` directories.

## Before → after measurements

Baseline is r91 delivered `c2ab3d0`; after is r92 closure `HEAD=87779a00f25bd1855ede479e490123843e5f056e`.

```sh
python3 - <<'PY'
import subprocess
from pathlib import Path
import re
p='corpus/knowledge/holder-assessment-boundary.md'
before=subprocess.run(['git','show',f'c2ab3d0:{p}'],check=True,capture_output=True,text=True).stdout
after=Path(p).read_text()
for label, text in (('c2ab3d0',before),('HEAD',after)):
    lines=text.splitlines()
    print(f'[{label}]')
    for needle in ('435','428','e2bb9639','ff9fd2aa','`Checker at delivered 1b09f3f`','holder identity is not uniquely resolvable: {details}; provenance tick',':272',':285',':274',':287',':306',':308'):
        print(f'{needle}={text.count(needle)}')
    print('checker_lines_context='+repr([line.strip() for line in lines if '435' in line or '428' in line][:3]))
PY
```

```text
[c2ab3d0]
435=2
428=1
e2bb9639=3
ff9fd2aa=2
`Checker at delivered 1b09f3f`=0
holder identity is not uniquely resolvable: {details}; provenance tick=1
:272=1
:285=1
:274=1
:287=1
:306=1
:308=1
checker_lines_context=['- Checker at delivered `1b09f3f` (`corpus/fixtures/check_bible.py`, 435', 'lines, sha256 `e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556`):', 'FN-2 qualification `:320-352`; CLI/exit behavior `:425-435`.']
[HEAD]
435=0
428=2
e2bb9639=2
ff9fd2aa=5
`Checker at delivered 1b09f3f`=0
holder identity is not uniquely resolvable: {details}; provenance tick=0
:272=0
:285=0
:274=1
:287=1
:306=0
:308=1
checker_lines_context=['- Checker at the r90-delivered tree `ca7f9ef` (`corpus/fixtures/check_bible.py`, 428', 'behavior `:418-428`.']
```

This closes the concrete Q91-001 contradiction: the stale holder-qualified tick rule went from 1 occurrence to 0; the raw-presence citations `:272/:285/:306` were replaced by `:274/:287/:308`. The stale 435-line/e2bb checker description is gone; the current evidence block names 428 lines and `ff9fd2aa`.

```sh
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
from pathlib import Path
import re
s = Path('corpus/knowledge/holder-assessment-boundary.md').read_text()
lines = s.splitlines()
in_fence = False
headings = []
for n, line in enumerate(lines, 1):
    if line.lstrip().startswith('```'):
        in_fence = not in_fence
        continue
    if not in_fence:
        m = re.match(r'^#{1,6}\s+(.*?)\s*#*\s*$', line)
        if m:
            title = re.sub(r'[*`_~]', '', m.group(1))
            title = ' '.join(title.split()).casefold()
            headings.append((n, len(m.group(0).split()[0]), title))
from collections import defaultdict
by_title = defaultdict(list)
for n, level, title in headings: by_title[title].append(n)
duplicates = {k:v for k,v in by_title.items() if len(v)>1}
markers = ('TODO','TBD','FIXME','REPLACE:','INSERT HERE','PASTE HERE','APPLY ORDER','OLD TEXT','NEW TEXT','INSTRUCTION SHEET','SECTION-REPLACEMENT INSTRUCTIONS','SKIPPED AS NAMED DEBT')
found = [(n, marker) for n,line in enumerate(lines,1) for marker in markers if marker.casefold() in line.casefold()]
print(f'h1_count={sum(level == 1 for _,level,_ in headings)}')
print(f'headings={len(headings)}')
print(f'duplicate_headings={duplicates}')
print(f'instruction_markers={found}')
print(f'verified_at_count={sum(line.lower().startswith("verified-at:") for line in lines)}')
print(f'stale_tick_claim_count={s.count("holder identity is not uniquely resolvable: {details}; provenance tick")}')
print(f'old_cli_claim_count={s.count("435 lines")}')
print(f'old_delivered_checker_label_count={s.count("Checker at delivered `1b09f3f`")}')
PY
```

```text
h1_count=1
headings=10
duplicate_headings={}
instruction_markers=[]
verified_at_count=1
stale_tick_claim_count=0
old_cli_claim_count=0
old_delivered_checker_label_count=0
```

The delivered checker remains the pinned 428-line source:

```sh
sha256sum corpus/fixtures/check_bible.py; wc -l corpus/fixtures/check_bible.py
```

```text
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
428 corpus/fixtures/check_bible.py
```

Replayed the two r91 C9 fixtures:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-null-chain; printf '[rc=%s]\n' "$?"; python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-tick-unresolved; printf '[rc=%s]\n' "$?"
```

```text
VIOLATION: entities[3].provenance[1]: provenance chain break; expected from_holder 'mira', got None
1 violation(s); no canon changed
[rc=1]
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[4].provenance[1].tick: provenance tick 1 must be greater than previous tick 3
VIOLATION: entities[4].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'
3 violation(s); no canon changed
[rc=1]
```

Ran CERT's added Python source from the patch, without applying it:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
from pathlib import Path
patch = Path('.ufo/waves/round-93/patches/CERT-tool.patch').read_text().splitlines()
start = patch.index('+++ b/corpus/tools/boundary_doc_check.py') + 1
source = []
for line in patch[start:]:
    if line.startswith('diff --git '):
        break
    if line.startswith('+'):
        source.append(line[1:])
    elif line.startswith('\\'):
        continue
exec(compile('\n'.join(source) + '\n', 'CERT-tool.patch:corpus/tools/boundary_doc_check.py', 'exec'), {'__name__': '__main__'})
PY
```

```text
CHECK receipt replay: PASS
CHECK code anchors: PASS
CHECK document structure: PASS
replay_receipts=3/3
replay_cases=14/14
anchors=2/2
h1_count=1
duplicate_headings=0
instruction_markers=0
CERTIFIED
```

Then tested the candidate's fail-closed behavior with a contradictory temporary document and a checker changed only by a harmless leading comment. The following runs the same patch source in three modes (baseline, injected C9 contradiction, byte-changed checker):

```sh
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
from contextlib import redirect_stdout
from hashlib import sha256
from io import StringIO
from pathlib import Path
import sys, tempfile
patch = Path('.ufo/waves/round-93/patches/CERT-tool.patch').read_text().splitlines()
start = patch.index('+++ b/corpus/tools/boundary_doc_check.py') + 1
source=[]
for line in patch[start:]:
    if line.startswith('diff --git '): break
    if line.startswith('+'): source.append(line[1:])
code='\n'.join(source)+'\n'
def run(args):
    previous=sys.argv
    sys.argv=['boundary_doc_check.py', *args]
    output=StringIO()
    try:
        with redirect_stdout(output):
            try: exec(compile(code,'CERT-tool.patch:corpus/tools/boundary_doc_check.py','exec'),{'__name__':'__main__'})
            except SystemExit as error: rc=error.code
    finally: sys.argv=previous
    text=output.getvalue()
    print(f'exit={rc}; final={text.strip().splitlines()[-1]}; anchors={next(line for line in text.splitlines() if line.startswith("anchors="))}; replays={next(line for line in text.splitlines() if line.startswith("replay_cases="))}')
original=Path('corpus/knowledge/holder-assessment-boundary.md').read_text()
checker=Path('corpus/fixtures/check_bible.py').read_bytes()
with tempfile.TemporaryDirectory(prefix='cb-audit-') as directory:
    root=Path(directory)
    contradictory=root/'contradictory.md'
    contradictory.write_text(original+'\nLegacy rule: holder identity is not uniquely resolvable: {details}; provenance tick findings are qualified.\n')
    changed=root/'check_bible.py'
    changed.write_bytes(b'# harmless byte change; semantics unchanged\n'+checker)
    print('baseline_document:')
    run([])
    print('injected_contradiction:')
    run(['--doc',str(contradictory)])
    print(f'changed_checker_sha256={sha256(changed.read_bytes()).hexdigest()}')
    print('changed_checker_bytes:')
    run(['--checker',str(changed)])
PY
```

```text
baseline_document:
exit=0; final=CERTIFIED; anchors=anchors=2/2; replays=replay_cases=14/14
injected_contradiction:
exit=0; final=CERTIFIED; anchors=anchors=2/2; replays=replay_cases=14/14
changed_checker_sha256=753a0e787510c09af127ee27c9f14fd7627950e8827525141580ef173fcd1e7e
changed_checker_bytes:
exit=0; final=CERTIFIED; anchors=anchors=2/2; replays=replay_cases=14/14
```

Patch applicability and delivery state:

```sh
git apply --check .ufo/waves/round-93/patches/CERT-tool.patch; printf 'apply_check_exit=%s\n' "$?"; test -e corpus/tools/boundary_doc_check.py; printf 'delivered_tool_path_exit=%s\n' "$?"
```

```text
apply_check_exit=0
delivered_tool_path_exit=1
```

The adjacent fixture-index check also remains negative:

```sh
python3 - <<'PY'
from pathlib import Path
s=Path('corpus/fixtures/README.md').read_text()
print(f'round91_heading_count={s.count("## Round 91")}')
print(f'r91_null_chain_mentions={s.count("r91-c1-null-chain")}')
print(f'r91_tick_unresolved_mentions={s.count("r91-c1-tick-unresolved")}')
PY
```

```text
round91_heading_count=0
r91_null_chain_mentions=0
r91_tick_unresolved_mentions=0
```

## Findings & named debt

- **Q91-001 — closed for the delivered boundary doc.** The duplicate/stale C9 tick row is absent (`holder-assessment-boundary.md:201`, `:287-290`); the only table row says tick findings are not qualified by unresolved holder identity. Both r91 fixtures reproduce the intended definite tick / separately qualified chain behavior.
- **Q91-002 — core findings repaired, but one provenance residue remains.** The duplicate H1, duplicated `verified-at`, stale tick row, stale raw-presence anchors, old 435-line checker block, and instruction markers are gone. Remaining `1b09f3f`/`e2bb9639` references describe historical r89 comparisons, not the current checker. However, the document still says it was “Refreshed” and “Landed” at round 90 and that “This revision was rewritten” by round-90 CB1 (`corpus/knowledge/holder-assessment-boundary.md:3-8,32`), while the r92 work commit `c4d4823` re-derived the current text. This stale provenance header was also noted by the r92 audit (`.ufo/waves/round-92/patches/CB-audit.json:101-103`); update it before calling Q91-002 wholly closed.
- **Q91-003 — still open outside this document.** The boundary doc now correctly says the Round 90 README section landed at `a7c6a17` (`:590-596`), but `corpus/fixtures/README.md` still has no Round 91 heading or either r91 fixture name. The Q91-003 index debt remains.
- **CERT tool — false-positive certification / C1 not yet supportable.** The patch returns `CERTIFIED`, but it does not encode B3's required checker hash pin (B3 `:18-22`), AST/content-based anchor catalog (B3 `:32-58`), or C9 contradiction gate (B3 `:69-71`). Its `check_anchors` only matches literal `check_bible.py:NNN` text and checks that numbers fall within the file's line count (`.ufo/waves/round-93/patches/CERT-tool.patch:266-286`); it does not verify code content. It reports only 2 anchors despite 119 colon-number references in the doc. The probe results prove it accepts both a superseded tick-qualification claim and a byte-changed checker. The patch's README claim that it “resolves every” citation (`CERT-tool.patch:405-408`) overstates this implementation.
- The CERT patch applies cleanly but remains patch-only; `corpus/tools/boundary_doc_check.py` is absent from the delivered tree. Its printed `CERTIFIED` is therefore an observed patch result, not evidence that a committed, B3-conforming certifier exists.
- No verdict is claimed here for unrelated r91 debts (Q91-004 through Q91-009) or the separate R8/R9 inspiration decision table.

## Handoff

Created only `.ufo/waves/round-93/CB-audit.md`. No tracked files were modified, no patch was applied, and no commit/push was made. Before accepting C1 certification, revise CERT's patch to implement B3's hash pin, content/AST anchor validation, and C9 contradiction check, then rerun it against the frozen delivered document/checker. Also refresh the boundary document's provenance header and land the missing Round 91 fixture README index in its proper owner lane.
