## Work performed

Axis: **C1 DEPTH** — deliver the boundary-document certifier. Added a patch-only proposal for `corpus/tools/boundary_doc_check.py` and its `corpus/tools/README.md` usage section in `.ufo/waves/round-93/patches/CERT-tool.patch`. The tool pairs receipt fences with immediately preceding checker command fences, accepts only literal fixture paths and a small no-shell command grammar, executes each expanded checker call, and compares stdout plus recorded return codes. It also verifies every explicit `check_bible.py:NNN[-MMM]` range against the delivered checker's line count, and checks H1 count, normalized duplicate headings, and instruction markers. It is read-only; success prints `CERTIFIED` / exits 0, any failed check lists its failure / exits 1. Anchor checks are line-existence only, as permitted by the seat mission; they do not verify source-content signatures.

No tracked files were edited, no sibling files were modified, and no commit or push was made. Patch and this seat report are the only files written by this seat.

## Before → after measurements

**Baseline tool availability and tracked-tree guard.** Exact command (cwd `lore-shokunin/`):

```sh
if [ -e corpus/tools/boundary_doc_check.py ]; then printf 'baseline_tool=present\n'; else printf 'baseline_tool=absent\n'; fi; git diff --quiet HEAD --; tracked=$?; git diff --cached --quiet; staged=$?; printf 'tracked_diff_exit=%s\nstaged_diff_exit=%s\n' "$tracked" "$staged"
```

Observed:

```text
baseline_tool=absent
tracked_diff_exit=0
staged_diff_exit=0
```

**Candidate certifier against the delivered boundary document.** The tool stays patch-only per the write boundary, so the exact added Python source was extracted in memory from the proposed patch and run as the CLI; it executed the actual `check_bible.py` calls with repository-root cwd. Exact command:

```sh
python3 - <<'PY'
from pathlib import Path
import subprocess, sys
patch = Path('.ufo/waves/round-93/patches/CERT-tool.patch').read_text()
start = patch.index('+++ b/corpus/tools/boundary_doc_check.py\n') + len('+++ b/corpus/tools/boundary_doc_check.py\n')
end = patch.index('\ndiff --git a/corpus/tools/README.md', start)
source = '\n'.join(line[1:] for line in patch[start:end].splitlines() if line.startswith('+')) + '\n'
runner = "import sys; exec(compile(sys.stdin.read(), 'corpus/tools/boundary_doc_check.py', 'exec'))"
result = subprocess.run([sys.executable, '-c', runner], input=source, text=True, capture_output=True)
print('COMMAND: python3 -c <CERT-tool.patch source>')
print(result.stdout, end='')
if result.stderr: print('STDERR:', result.stderr, file=sys.stderr)
print(f'EXIT: {result.returncode}')
raise SystemExit(result.returncode)
PY
```

Observed:

```text
COMMAND: python3 -c <CERT-tool.patch source>
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
EXIT: 0
```

All three recognized checker receipt blocks replayed, covering 14 cases; each replay had matching stdout/return code and empty stderr. Both explicit checker line citations resolve in the 428-line delivered checker.

**Fail-closed scratch perturbations.** Each temporary document was written alone under `/tmp` and removed immediately. Exact command:

```sh
python3 - <<'PY'
from pathlib import Path
import os, subprocess, sys, tempfile
patch = Path('.ufo/waves/round-93/patches/CERT-tool.patch').read_text()
start = patch.index('+++ b/corpus/tools/boundary_doc_check.py\n') + len('+++ b/corpus/tools/boundary_doc_check.py\n')
end = patch.index('\ndiff --git a/corpus/tools/README.md', start)
source = '\n'.join(line[1:] for line in patch[start:end].splitlines() if line.startswith('+')) + '\n'
runner = "import sys; exec(compile(sys.stdin.read(), 'corpus/tools/boundary_doc_check.py', 'exec'))"
doc = Path('corpus/knowledge/holder-assessment-boundary.md').read_bytes()
old = b'CLEAN: schema, citations, relations, timeline; 0 violations'
receipt_at = doc.index(b'```text', doc.index(b'## Commands'))
position = doc.index(old, receipt_at)
receipt_mutation = doc[:position] + b'CLEAN: intentionally changed receipt' + doc[position + len(old):]
probes = [
    ('duplicate_heading', doc + b'\n## Editor checklist\n'),
    ('unresolved_anchor', doc.replace(b'check_bible.py:212-224', b'check_bible.py:9999', 1)),
    ('receipt_drift', receipt_mutation),
]
for name, payload in probes:
    with tempfile.NamedTemporaryFile(mode='wb', suffix='.md', dir='/tmp', delete=False) as scratch:
        scratch.write(payload)
        scratch_path = scratch.name
    try:
        result = subprocess.run([sys.executable, '-c', runner, '--doc', scratch_path], input=source, capture_output=True, text=True)
        failures = [line for line in result.stdout.splitlines() if line.startswith('FAIL:')]
        print(f'PROBE {name}: exit={result.returncode} expected=1; ' + (failures[0] if failures else 'no failure detail'))
        if result.returncode != 1 or not failures:
            print(result.stdout, end='')
            raise SystemExit(f'{name} did not fail closed')
    finally:
        os.unlink(scratch_path)
print('scratch_perturbations=3/3 exit_1')
PY
```

Observed:

```text
PROBE duplicate_heading: exit=1 expected=1; FAIL: duplicate heading 'editor checklist' at lines [210, 650]
PROBE unresolved_anchor: exit=1 expected=1; FAIL: unresolved anchor check_bible.py:9999: checker has 428 lines
PROBE receipt_drift: exit=1 expected=1; FAIL: stdout mismatch for r85-control (receipt line 355)
scratch_perturbations=3/3 exit_1
```

**Patch validation.** Exact command:

```sh
git apply --check --verbose .ufo/waves/round-93/patches/CERT-tool.patch; rc=$?; printf 'git_apply_check_exit=%s\n' "$rc"; exit "$rc"
```

Observed:

```text
Checking patch corpus/tools/boundary_doc_check.py...
Checking patch corpus/tools/README.md...
Hunk #1 succeeded at 25 (offset -1 lines).
git_apply_check_exit=0
```

**R8 dossier dependency poll.** Exact command: `sh .ufo/waves/poll_wait.sh .ufo/waves/round-93/D2.md 1200`.

Observed poll receipt:

```text
POLL_CHECK t=60s path=.ufo/waves/round-93/D2.md present=no
POLL_CHECK t=120s path=.ufo/waves/round-93/D2.md present=no
POLL_CHECK t=180s path=.ufo/waves/round-93/D2.md present=no
POLL_CHECK t=240s path=.ufo/waves/round-93/D2.md present=no
POLL_CHECK t=300s path=.ufo/waves/round-93/D2.md present=no
POLL_HIT path=.ufo/waves/round-93/D2.md elapsed=300s checks=5
```

D2's report and patch arrived; neither was modified or applied by this seat.

**R9 venue dependency poll, first helper invocation.** Exact command: `sh .ufo/waves/poll_wait.sh .ufo/waves/round-93/D1.md 1200`. The background-command limit interrupted the helper during its 600-second sleep cap; its trap reported the partial poll:

```text
POLL_CHECK t=60s path=.ufo/waves/round-93/D1.md present=no
POLL_CHECK t=120s path=.ufo/waves/round-93/D1.md present=no
POLL_CHECK t=180s path=.ufo/waves/round-93/D1.md present=no
POLL_CHECK t=240s path=.ufo/waves/round-93/D1.md present=no
POLL_CHECK t=300s path=.ufo/waves/round-93/D1.md present=no
POLL_CHECK t=360s path=.ufo/waves/round-93/D1.md present=no
POLL_CHECK t=420s path=.ufo/waves/round-93/D1.md present=no
POLL_CHECK t=480s path=.ufo/waves/round-93/D1.md present=no
POLL_CHECK t=540s path=.ufo/waves/round-93/D1.md present=no
Terminated                 sleep 60
POLL_TERMINAL status=1 reason=trap elapsed=540s checks=9
```

**R9 venue dependency poll, continuation.** Exact command: `sh .ufo/waves/poll_wait.sh .ufo/waves/round-93/D1.md 600`.

```text
POLL_CHECK t=60s path=.ufo/waves/round-93/D1.md present=no
POLL_CHECK t=120s path=.ufo/waves/round-93/D1.md present=no
POLL_CHECK t=180s path=.ufo/waves/round-93/D1.md present=no
POLL_HIT path=.ufo/waves/round-93/D1.md elapsed=180s checks=3
```

The D1 report arrived on the continuation before the 20-minute deadline; its patch had already appeared. Final presence command:

```sh
if [ -f .ufo/waves/round-93/D1.md ]; then printf 'D1_report=present\n'; else printf 'D1_report=absent\n'; fi; if [ -f .ufo/waves/round-93/D2.md ]; then printf 'D2_report=present\n'; else printf 'D2_report=absent\n'; fi; if [ -f .ufo/waves/round-93/patches/D1-venue.patch ]; then printf 'D1_patch=present\n'; else printf 'D1_patch=absent\n'; fi; if [ -f .ufo/waves/round-93/patches/D2-dossier.patch ]; then printf 'D2_patch=present\n'; else printf 'D2_patch=absent\n'; fi
```

Observed:

```text
D1_report=present
D2_report=present
D1_patch=present
D2_patch=present
```

Neither dependency artifact was modified or applied by this seat.

## Findings & named debt

- The current r92 boundary document is certified by the proposed tool, and the three gates each fail closed under an isolated mutation.
- The certification tool itself remains a proposal until the integrator applies `CERT-tool.patch`; the post-landing one-command invocation is therefore not yet verified on an installed tracked tool.
- The line-anchor gate establishes only that cited numbers fall within the delivered checker. It does not implement B3's broader AST/content-signature or C9 semantic review; the current seat mission explicitly asks for line-existence validation (content sniff optional).
- Both C1 dependencies (D1 R9 venue repair and D2 R8 dossier) have reports and patches available; no dependency gap remains for this seat.

## Handoff

- `.ufo/waves/round-93/patches/CERT-tool.patch` — new certifier plus `corpus/tools/README.md` section.
- `.ufo/waves/round-93/CERT.md` — this seat receipt, including replay, negative probes, and D1/D2 poll receipts.
- Integration must apply the patch and run `python3 corpus/tools/boundary_doc_check.py` from the repo root; no tracked change was applied in this seat.
