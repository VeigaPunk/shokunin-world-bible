## Work performed

- Axes: **scope integrity** (the re-derivation changes only the boundary document), **fixture coverage** (all 166 directory tuples remain stable), and **calibration** (the five r85 probe receipts remain byte-stable).
- Read the round-92 wave spec, CB1's r90 section instructions, the e97613c source contract, the current boundary document, B1/B2 census receipts, and the D1/D2 re-derivation artifacts. Ran live checker calls for the full fixture census and all five r85 probes.
- No tracked file was modified, no patch was applied, no `/tmp` scratch was created, and no commit/push was made. This report and `patches/H-delta.json` are the only files written by this seat.

## Before → after measurements

**Baseline identity.**

Command:

```sh
git rev-parse HEAD && git status --porcelain --untracked-files=no && sha256sum corpus/knowledge/holder-assessment-boundary.md && wc -l corpus/knowledge/holder-assessment-boundary.md && sha256sum corpus/fixtures/check_bible.py && git diff --name-only HEAD -- corpus
```

Observed (status and corpus diff streams empty):

```text
396c568cbf86bba2c4b7a4ce8bd69fc38bb33d1f
c0c59dafc32c7fdc52f30352359b2c252e7607c76010063231b8f89d223911c9  corpus/knowledge/holder-assessment-boundary.md
549 corpus/knowledge/holder-assessment-boundary.md
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
```

The certifiable source contract at e97613c was measured in memory:

```sh
python3 - <<'PY'
import hashlib, subprocess
raw=subprocess.check_output(['git','show','e97613c:corpus/knowledge/holder-assessment-boundary.md'])
text=raw.decode()
heads=[line for line in text.splitlines() if line.startswith('#')]
print(f'e97613c_boundary_sha256={hashlib.sha256(raw).hexdigest()}')
print(f'e97613c_boundary_lines={len(text.splitlines())} h1={sum(x.startswith("# ") for x in heads)} h2={sum(x.startswith("## ") for x in heads)} heading_lines={heads}')
PY
```

```text
e97613c_boundary_sha256=a4b1b331ba96ff5d57200517cfe1d9e4c8f6030b4fd9ec2e46f38e7fbb4b3fd2
e97613c_boundary_lines=630 h1=1 h2=9 heading_lines=['# Holder-assessment boundary: reading provenance ambiguity disclosures', '## The contract (round-1 baseline paragraph, kept)', '## First-stop causes (delivered `1b09f3f`)', '## Decision table: reference state → output → next action', '## Editor checklist', '## Precise limits of the disclosure', '## Commands (self-contained, run from the lane root)', '## Evidence and citations', '## Status split', '## Measured results (parent-owned slot)']
```

**166-directory tuple census.** Each sorted direct fixture directory was run with the repo-relative invocation; current tuples were compared independently to round-92 B1 and B2.

```sh
python3 - <<'PY'
import hashlib, json, subprocess
from pathlib import Path
manifests={n:json.loads(Path(f'.ufo/waves/round-92/patches/{n}-tuples.json').read_text()) for n in ('B1','B2')}
actual={}
stderr_nonempty=[]
for d in sorted(Path('corpus/fixtures').iterdir()):
    if not d.is_dir(): continue
    p=subprocess.run(['python3','-I','corpus/fixtures/check_bible.py',str(d)],capture_output=True)
    if p.stderr: stderr_nonempty.append(str(d))
    actual[str(d)]={'exit':p.returncode,'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),'violation_count':sum(x.startswith('VIOLATION:') for x in p.stdout.decode().splitlines())}
for name,m in manifests.items():
    diffs=[path for path,row in actual.items() if path not in m or any(row[k]!=m[path][k] for k in row)]
    removed=sorted(set(m)-set(actual))
    print(f'{name}: manifest_dirs={len(m)} live_dirs={len(actual)} tuple_mismatches={len(diffs)} removed={len(removed)}')
raw1=Path('.ufo/waves/round-92/patches/B1-tuples.json').read_bytes(); raw2=Path('.ufo/waves/round-92/patches/B2-tuples.json').read_bytes()
print(f'B1_B2_bytes_equal={raw1==raw2} B1_sha256={hashlib.sha256(raw1).hexdigest()} B2_sha256={hashlib.sha256(raw2).hexdigest()}')
print(f'stderr_nonempty={stderr_nonempty}')
PY
```

```text
B1: manifest_dirs=166 live_dirs=166 tuple_mismatches=0 removed=0
B2: manifest_dirs=166 live_dirs=166 tuple_mismatches=0 removed=0
B1_B2_bytes_equal=True B1_sha256=185ce02d2e2bf80e2846dada9e864fc533d58cfd229be9e2596d4b1f2a21baaf B2_sha256=185ce02d2e2bf80e2846dada9e864fc533d58cfd229be9e2596d4b1f2a21baaf
stderr_nonempty=[]
```

**Five r85 outputs.** The same live command output was compared byte-for-byte with both the pasted receipt in the current document and the pasted receipt from e97613c.

```sh
python3 - <<'PY'
import hashlib, re, subprocess
from pathlib import Path
cases=['r85-control','r85-unique-break-control','r85-masked-ambiguous','r85-isolated-ambiguous','r85-harbor-repro']
source=subprocess.check_output(['git','show','e97613c:corpus/knowledge/holder-assessment-boundary.md'],text=True)
e976=next(b+'\n' for b in re.findall(r'```text\n(.*?)\n```',source,re.S) if b.startswith('=== r85-control ==='))
doc=Path('corpus/knowledge/holder-assessment-boundary.md').read_text()
marker='Observed output (verbatim; stderr empty in all five; byte-identical to the\nr88 replay, so this block did not change with the r89 amendments):\n\n```text\n'
current=doc.split(marker,1)[1].split('\n```',1)[0]+'\n'
live=''; bad_stderr=[]
for case in cases:
    live+=f'=== {case} ===\n'
    p=subprocess.run(['python3','corpus/fixtures/check_bible.py',f'corpus/live/runs/round-85/probe-inputs/{case}'],capture_output=True)
    live+=p.stdout.decode()+f'[rc={p.returncode}]\n'
    if p.stderr: bad_stderr.append(case)
    print(f'{case}: exit={p.returncode} stdout_sha256={hashlib.sha256(p.stdout).hexdigest()} stderr_bytes={len(p.stderr)}')
print(f'live_equals_e97613c_pasted_block={live==e976}')
print(f'live_equals_current_pasted_block={live==current}')
print(f'nonempty_stderr_cases={bad_stderr}')
PY
```

```text
r85-control: exit=0 stdout_sha256=afe570fcebf45fe3913b8b87c65a2e0408e99e9c69854757a2498d5be420c07e stderr_bytes=0
r85-unique-break-control: exit=1 stdout_sha256=1a218a9a71a13d2772b7ef3d739f3949c10b12f126463af40e4656988c9c9094 stderr_bytes=0
r85-masked-ambiguous: exit=1 stdout_sha256=757cc1308914ffe5968464c3e9b3fbffef70b040ba89e5f3b0aa1a4186d489c1 stderr_bytes=0
r85-isolated-ambiguous: exit=1 stdout_sha256=3e50866af53011ee465ac9126f37ce098420ba64360a1f5283f13340eb4904ad stderr_bytes=0
r85-harbor-repro: exit=1 stdout_sha256=5c5b5955d87f87797c2389ee1ef7dc67f04392fa407521aa0a77b79c6bb6e54d stderr_bytes=0
live_equals_e97613c_pasted_block=True
live_equals_current_pasted_block=True
nonempty_stderr_cases=[]
```

The five probe input trees were unchanged from e97613c:

```sh
git diff --quiet e97613c HEAD -- corpus/live/runs/round-85/probe-inputs/r85-control corpus/live/runs/round-85/probe-inputs/r85-unique-break-control corpus/live/runs/round-85/probe-inputs/r85-masked-ambiguous corpus/live/runs/round-85/probe-inputs/r85-isolated-ambiguous corpus/live/runs/round-85/probe-inputs/r85-harbor-repro; rc=$?; printf 'five_r85_input_diff_e97613c_to_HEAD=%s\n' "$rc"; git status --porcelain --untracked-files=no
```

```text
five_r85_input_diff_e97613c_to_HEAD=0
```

**Candidate/patch scope.** D2's unified diff is applyable but was not applied. Its final receipt:

```sh
sha256sum .ufo/waves/round-92/patches/D2-boundary-doc.md && git apply --stat .ufo/waves/round-92/patches/D2-boundary-doc.md && git apply --numstat .ufo/waves/round-92/patches/D2-boundary-doc.md && git apply --check .ufo/waves/round-92/patches/D2-boundary-doc.md && printf 'D2_apply_check=PASS\n' && printf 'tracked_corpus_diff_names=' && git diff --name-only HEAD -- corpus
```

```text
55495d1002baa2776abf93c8bd0df26bd39493ba8cbe4b2dddac77aaf6c8d428  .ufo/waves/round-92/patches/D2-boundary-doc.md
 corpus/knowledge/holder-assessment-boundary.md |  458 +++++++++++++++---------
1 file changed, 290 insertions(+), 168 deletions(-)
290	168	corpus/knowledge/holder-assessment-boundary.md
D2_apply_check=PASS
tracked_corpus_diff_names=
```

A content search for the five `=== r85-... ===` wrappers in the D2 diff found no matches; its hunks do not rewrite those receipt lines.

D1's whole-document candidate arrived after the dependency deadline. Its structural and receipt check was:

```sh
python3 - <<'PY'
import re, subprocess
from pathlib import Path
p=Path('.ufo/waves/round-92/patches/D1-boundary-doc.md')
text=p.read_text()
inside=False; heads=[]
for line in text.splitlines():
    if line.startswith('```'):
        inside=not inside; continue
    if not inside:
        m=re.match(r'^(#{1,6})\s+(.+?)\s*#*$',line)
        if m: heads.append((len(m.group(1)),m.group(2).strip()))
print(f'D1_candidate_lines={len(text.splitlines())} h1={sum(n==1 for n,_ in heads)} h2={sum(n==2 for n,_ in heads)} duplicate_titles={len(heads)-len({title.casefold() for _,title in heads})}')
source=subprocess.check_output(['git','show','e97613c:corpus/knowledge/holder-assessment-boundary.md'],text=True)
blocks=re.findall(r'```text\n(.*?)\n```',source,re.S)
expected=next(b+'\n' for b in blocks if b.startswith('=== r85-control ==='))
newblocks=re.findall(r'```text\n(.*?)\n```',text,re.S)
candidate=next((b+'\n' for b in newblocks if b.startswith('=== r85-control ===')),None)
print(f'D1_candidate_r85_block_found={candidate is not None}')
print(f'D1_candidate_r85_equals_e97613c_receipt={candidate==expected}')
print(f'D1_candidate_has_proposal_banner={"not landed" in text[:500]}')
PY
```

```text
D1_candidate_lines=524 h1=1 h2=9 duplicate_titles=0
D1_candidate_r85_block_found=True
D1_candidate_r85_equals_e97613c_receipt=True
D1_candidate_has_proposal_banner=True
```

The D1 file begins “Round-92 re-derivation proposal; not landed”; it is full candidate Markdown, not a unified diff (`git apply --check` reports “No valid patches in input”). Its mtime is 09:20:17, after the 09:18 dependency cutoff. `D1.md` remained absent at the final check.

**Dependency poll receipts.** D2 was already present:

```sh
sh .ufo/waves/poll_wait.sh .ufo/waves/round-92/patches/D2-boundary-doc.md 1200
```

```text
POLL_HIT path=.ufo/waves/round-92/patches/D2-boundary-doc.md elapsed=0s checks=0
```

The D1 patch poll covered the remaining eight minutes of the 20-minute window:

```sh
sh .ufo/waves/poll_wait.sh .ufo/waves/round-92/patches/D1-boundary-doc.md 480
```

```text
POLL_CHECK t=60s path=.ufo/waves/round-92/patches/D1-boundary-doc.md present=no
POLL_CHECK t=120s path=.ufo/waves/round-92/patches/D1-boundary-doc.md present=no
POLL_CHECK t=180s path=.ufo/waves/round-92/patches/D1-boundary-doc.md present=no
POLL_CHECK t=240s path=.ufo/waves/round-92/patches/D1-boundary-doc.md present=no
POLL_CHECK t=300s path=.ufo/waves/round-92/patches/D1-boundary-doc.md present=no
POLL_CHECK t=360s path=.ufo/waves/round-92/patches/D1-boundary-doc.md present=no
POLL_CHECK t=420s path=.ufo/waves/round-92/patches/D1-boundary-doc.md present=no
POLL_CHECK t=480s path=.ufo/waves/round-92/patches/D1-boundary-doc.md present=no
POLL_TERMINAL status=0 reason=deadline elapsed=480s checks=8
```

The initial D1 report poll had a 1,200-second helper deadline, but the outer process timeout interrupted its final sleep; it ended at 1,140 seconds / 19 checks and its trap emitted:

```text
POLL_TERMINAL status=1 reason=trap elapsed=1140s checks=19
```

At the 09:18:42 final-window snapshot, both D1 paths were absent. At 09:26:40, the candidate path was present and `D1.md` remained absent. The late candidate was inspected, but the expired dependency window was not restarted.

## Findings & named debt

- **Doc-only delta prediction: supported, conditionally.** D2 is a real unified diff whose sole target is `corpus/knowledge/holder-assessment-boundary.md`; `git apply --check` passes. D1 independently supplies a whole-document candidate with the same target title and the expected single-H1 / nine-H2 shape. The D1 candidate appeared after the 20-minute deadline and has no accompanying `D1.md` report.
- **Fixture invariants: confirmed on the pre-integration tree.** All 166 live tuples match both byte-identical B1/B2 receipts; no checker run emitted stderr. All five live r85 outputs match the e97613c and current-document receipts byte-for-byte, and the five probe input trees are identical to e97613c. D1's pasted r85 block also matches the e97613c receipt; D2's diff does not touch the r85 case wrappers.
- **Bounded verification only.** Neither proposal was applied, as required by the seat's write boundary. Therefore the actual post-integration tree was not measured; this is a patch/candidate-scope verification, not a certification of the delivered document or its anchors. D1's candidate is not directly applyable as a unified diff, and the late artifact lacks its report.

## Handoff

- Wrote only `.ufo/waves/round-92/H-delta.md` and `.ufo/waves/round-92/patches/H-delta.json`. No tracked file changes, commit, push, sibling-repo access, or scratch files.
- Parent integration should choose/apply the boundary-document reconstruction, then run the round-92 B3/T1 certifier on the integrated tree and recheck the fixture census/probe receipts. Do not treat this seat's prediction as proof of the yet-unseen integrated after-state.
