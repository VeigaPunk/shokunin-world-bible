# CB-audit — Round-92 boundary reconstruction

## Work performed

- Axes: **reconstruction fidelity** (JAXIS R1; H5/CB1 doc-state findings), **closure coverage** (JAXIS R2), and **calibration/receipt integrity** (JAXIS R3, H5 F8, checker freeze).
- Audited D1's complete-document proposal and D2's unified diff as separate, unselected candidates; reconstructed D2 in memory only. Compared both to `.ufo/waves/round-91/followup/JAXIS.md` R1–R3, `H5.md` F1–F8, and `CB1.md` F1–F7.
- Ran the required T1 poll every 60 seconds through the 20-minute deadline. Exact command and terminal receipt:

  ```sh
  sh .ufo/waves/poll_wait.sh .ufo/waves/round-92/T1.md 1200
  ```

  ```text
  POLL_CHECK t=60s path=.ufo/waves/round-92/T1.md present=no
  POLL_CHECK t=120s path=.ufo/waves/round-92/T1.md present=no
  POLL_CHECK t=180s path=.ufo/waves/round-92/T1.md present=no
  POLL_CHECK t=240s path=.ufo/waves/round-92/T1.md present=no
  POLL_CHECK t=300s path=.ufo/waves/round-92/T1.md present=no
  POLL_CHECK t=360s path=.ufo/waves/round-92/T1.md present=no
  POLL_CHECK t=420s path=.ufo/waves/round-92/T1.md present=no
  POLL_CHECK t=480s path=.ufo/waves/round-92/T1.md present=no
  POLL_CHECK t=540s path=.ufo/waves/round-92/T1.md present=no
  POLL_CHECK t=600s path=.ufo/waves/round-92/T1.md present=no
  POLL_CHECK t=660s path=.ufo/waves/round-92/T1.md present=no
  POLL_CHECK t=720s path=.ufo/waves/round-92/T1.md present=no
  POLL_CHECK t=780s path=.ufo/waves/round-92/T1.md present=no
  POLL_CHECK t=840s path=.ufo/waves/round-92/T1.md present=no
  POLL_CHECK t=900s path=.ufo/waves/round-92/T1.md present=no
  POLL_CHECK t=960s path=.ufo/waves/round-92/T1.md present=no
  POLL_CHECK t=1020s path=.ufo/waves/round-92/T1.md present=no
  POLL_CHECK t=1080s path=.ufo/waves/round-92/T1.md present=no
  POLL_CHECK t=1140s path=.ufo/waves/round-92/T1.md present=no
  POLL_CHECK t=1200s path=.ufo/waves/round-92/T1.md present=no
  POLL_TERMINAL status=0 reason=deadline elapsed=1200s checks=20
  ```

- T1.md/T1-certification.json became available after that poll. Their certification outcome is `FAIL`, and they say no selected/integrated r92 document is present. T1's `D1.md absent` snapshot is now stale because D1.md subsequently appeared; its no-integration finding remains true. Neither D1 nor D2 is selected or certified.
- No tracked or staged file was changed; neither proposal was applied; no commit, push, or `/tmp` scratch was used. The only intended writes are this report and `patches/CB-audit.json`.

## Before → after measurements

**Current tree and patch applicability.** Exact command (cwd `lore-shokunin/`):

```sh
set +e
printf 'HEAD='; git rev-parse HEAD
printf 'boundary_sha='; sha256sum corpus/knowledge/holder-assessment-boundary.md | cut -d' ' -f1
printf 'checker_sha='; sha256sum corpus/fixtures/check_bible.py | cut -d' ' -f1
git diff --quiet HEAD --; printf 'tracked_worktree_diff_exit=%s\n' "$?"
git diff --cached --quiet; printf 'staged_diff_exit=%s\n' "$?"
printf 'D1_full_document_apply_check: '
git apply --check .ufo/waves/round-92/patches/D1-boundary-doc.md 2>&1; printf 'exit=%s\n' "$?"
printf 'D2_patch_apply_check: '
git apply --check .ufo/waves/round-92/patches/D2-boundary-doc.md 2>&1; printf 'exit=%s\n' "$?"
printf 'D2_numstat:\n'; git apply --numstat .ufo/waves/round-92/patches/D2-boundary-doc.md
```

Observed:

```text
HEAD=396c568cbf86bba2c4b7a4ce8bd69fc38bb33d1f
boundary_sha=c0c59dafc32c7fdc52f30352359b2c252e7607c76010063231b8f89d223911c9
checker_sha=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
tracked_worktree_diff_exit=0
staged_diff_exit=0
D1_full_document_apply_check: error: No valid patches in input (allow with "--allow-empty")
exit=128
D2_patch_apply_check: exit=0
D2_numstat:
290	168	corpus/knowledge/holder-assessment-boundary.md
```

D1 is a complete Markdown document, not a unified diff; the `git apply` error is a format observation, not a content verdict. D2 is applicable as a check only. Neither was applied; the tracked target remains the 549-line r91 baseline.

**Candidate structure, preserved blocks, and replay.** D2 was applied to the HEAD document in memory with context/deletion assertions; the script ran the checker directly for each embedded case and compared stdout bytes, exit code, and stderr. Exact command:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
from collections import Counter
from pathlib import Path
import hashlib, re, subprocess, sys
base_path='corpus/knowledge/holder-assessment-boundary.md'
base=subprocess.check_output(['git','show',f'HEAD:{base_path}']).decode().splitlines(keepends=True)
patch=Path('.ufo/waves/round-92/patches/D2-boundary-doc.md').read_text()
out=[]; cur=0; active=False; old_i=old_n=old_start=0
for line in patch.splitlines(keepends=True):
    m=re.match(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@',line)
    if m:
        if active: assert old_i-(old_start-1)==old_n
        old_start=int(m.group(1)); old_n=int(m.group(2) or 1); old_i=old_start-1
        assert old_i>=cur
        out.extend(base[cur:old_i]); cur=old_i; active=True; continue
    if not active: continue
    if line.startswith(' '):
        assert base[old_i]==line[1:],(old_i+1,base[old_i],line[1:])
        out.append(line[1:]); old_i+=1; cur=old_i
    elif line.startswith('-'):
        assert base[old_i]==line[1:],(old_i+1,base[old_i],line[1:])
        old_i+=1; cur=old_i
    elif line.startswith('+'): out.append(line[1:])
    elif line.startswith('\\'): pass
    else: raise AssertionError(repr(line))
if active: assert old_i-(old_start-1)==old_n
candidate2=''.join(out)+''.join(base[cur:])
candidates={'D1':Path('.ufo/waves/round-92/patches/D1-boundary-doc.md').read_text(),'D2':candidate2}
source=subprocess.check_output(['git','show',f'e97613c:{base_path}']).decode()
get_fences=lambda text:list(re.finditer(r'^```([^\n]*)\n(.*?)^```[ \t]*$',text,re.M|re.S))
source_fences=get_fences(source)
limit_markers=('Scope: exactly two assessments stop','One form, one boundary','Causes are collected, not selected','Cause wording separates','Emission order is asymmetric','A duplicated item id arms a separate stop','Everything else continues','Three states, not two','No truth claims','Ambiguous SOURCE is not a stop cause','Chain eligibility is no longer orthogonal','Measurement ceiling','The two r89 hedged shapes are repaired')
for name,text in candidates.items():
    lines=text.splitlines(); in_fence=False; headings=[]; markers=[]
    mark_re=re.compile(r'\b(?:TODO|TBD|FIXME)\b|REPLACE:|INSERT HERE|PASTE HERE|APPLY ORDER|OLD TEXT|NEW TEXT|INSTRUCTION SHEET|SECTION-REPLACEMENT INSTRUCTIONS|SKIPPED AS NAMED DEBT\b',re.I)
    for n,line in enumerate(lines,1):
        if re.match(r'^\s*```',line): in_fence=not in_fence; continue
        if in_fence: continue
        h=re.match(r'^(#{1,6})\s+(.+?)\s*#*\s*$',line)
        if h: headings.append((len(h.group(1)),re.sub(r'\s+',' ',re.sub(r'[`*_]','',h.group(2))).strip().casefold(),n))
        markers.extend((n,m.group(0)) for m in mark_re.finditer(line))
    counts=Counter(t for _,t,_ in headings); dup=[t for t,c in counts.items() if c>1]
    fences=get_fences(text)
    source_blocks=Counter(hashlib.sha256(m.group(2).encode()).hexdigest() for m in source_fences)
    candidate_blocks=Counter(hashlib.sha256(m.group(2).encode()).hexdigest() for m in fences)
    shared=sum((source_blocks & candidate_blocks).values())
    replay=[m.group(2) for m in fences if m.group(1).strip().lower() not in ('sh','bash') and re.search(r'(?m)^=== .+ ===$',m.group(2)) and re.search(r'(?m)^\[rc=\d+\]$',m.group(2))]
    cases=mis=err=0
    for body in replay:
        parts=re.split(r'(?m)^=== (.+) ===\n',body)
        for i in range(1,len(parts),2):
            case=parts[i]; expected=parts[i+1]; m=re.search(r'(?m)^\[rc=(\d+)\]$',expected); assert m,case
            fixture=(Path('corpus/live/runs/round-85/probe-inputs')/case if case.startswith('r85-') else Path('corpus/fixtures')/case)
            p=subprocess.run([sys.executable,'corpus/fixtures/check_bible.py',str(fixture)],capture_output=True)
            cases+=1; err+=bool(p.stderr); mis+=not(p.returncode==int(m.group(1)) and p.stdout==expected[:m.start()].encode())
    limit=sum(x.casefold() in text.casefold() for x in limit_markers)
    print(f'{name}: sha256={hashlib.sha256(text.encode()).hexdigest()} lines={len(lines)} h1={sum(l==1 for l,_,_ in headings)} h2={sum(l==2 for l,_,_ in headings)} duplicate_headings={dup!r} verified_at={sum(x.startswith("verified-at:") for x in lines)} instruction_markers={markers!r}')
    print(f'{name}: r91_fixture_mentions={{"null-chain":{text.count("r91-c1-null-chain")},"tick-unresolved":{text.count("r91-c1-tick-unresolved")}}} limits={limit}/{len(limit_markers)} code_fences={len(fences)} source_fence_hashes_shared={shared}')
    print(f'{name}: replay_blocks={len(replay)} replay_cases={cases} mismatches={mis} stderr_nonempty={err}')
    print(f'{name}: delivered_old_checker_label={text.count("Checker at delivered `1b09f3f`")} e2bb9639={text.count("e2bb9639")} stale_round90_sentence={text.count("There is no `## Round 90` section at `ca7f9ef`")} r87_table_phrase={text.count("The r87 decision table")} row3_current_phrase={text.count("Tick findings are NOT qualified")}')
PY
```

Observed:

```text
D1: sha256=92c9baf71c70b3fe845c8f2d7309934fe64523e0963072f484f259ef0ac462f9 lines=524 h1=1 h2=9 duplicate_headings=[] verified_at=1 instruction_markers=[]
D1: r91_fixture_mentions={"null-chain":0,"tick-unresolved":0} limits=13/13 code_fences=7 source_fence_hashes_shared=7
D1: replay_blocks=3 replay_cases=14 mismatches=0 stderr_nonempty=0
D1: delivered_old_checker_label=1 e2bb9639=2 stale_round90_sentence=1 r87_table_phrase=1 row3_current_phrase=1
D2: sha256=8e1fe8774a70f06c31efd783b4313a1639c1da4bcfd830be92134e8964536728 lines=671 h1=1 h2=9 duplicate_headings=[] verified_at=1 instruction_markers=[]
D2: r91_fixture_mentions={"null-chain":4,"tick-unresolved":4} limits=13/13 code_fences=7 source_fence_hashes_shared=7
D2: replay_blocks=3 replay_cases=14 mismatches=0 stderr_nonempty=0
D2: delivered_old_checker_label=0 e2bb9639=3 stale_round90_sentence=0 r87_table_phrase=2 row3_current_phrase=1
```

Thus both candidate texts pass the narrow structure, embedded replay, and preserved-block checks; those checks do not certify a selected/delivered document. D1's exact stale claims and D2's residual seam are detailed below.

**The two r91 fixture README blocks under both checker versions.** Exact command:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
from pathlib import Path
import subprocess, sys
old=subprocess.check_output(['git','show','e97613c:corpus/fixtures/check_bible.py'],text=True)
for name in ('r91-c1-null-chain','r91-c1-tick-unresolved'):
    fixture=f'corpus/fixtures/{name}'; readme=Path(fixture,'README.md').read_text()
    expected={}
    for rev,heading in (('e97613c','e97613c'),('delivered','the delivered checker')):
        start=readme.index(f'## Expected output with {heading}')
        fence=readme.index('```text\n',start)+len('```text\n')
        end=readme.index('\n```',fence)
        expected[rev]=readme[fence:end]+'\n'
    for rev,argv in (('e97613c',[sys.executable,'-c',old,fixture]),('delivered',[sys.executable,'corpus/fixtures/check_bible.py',fixture])):
        p=subprocess.run(argv,capture_output=True,text=True)
        ok=p.stdout==expected[rev] and p.returncode==1 and not p.stderr
        print(f'{name} {rev}: {"MATCH" if ok else "MISMATCH"} exit={p.returncode} stderr_bytes={len(p.stderr.encode())}')
PY
```

Observed:

```text
r91-c1-null-chain e97613c: MATCH exit=1 stderr_bytes=0
r91-c1-null-chain delivered: MATCH exit=1 stderr_bytes=0
r91-c1-tick-unresolved e97613c: MATCH exit=1 stderr_bytes=0
r91-c1-tick-unresolved delivered: MATCH exit=1 stderr_bytes=0
```

**README, decision-table, watch, and composition state.** Exact read-only command:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
from pathlib import Path
import subprocess
readme=Path('corpus/fixtures/README.md').read_text().splitlines()
rounds=[x for x in readme if x.startswith('## Round')]
text='\n'.join(readme)
print(f'README last_round_heading={rounds[-1]} round91_headings={sum(x.startswith("## Round 91") for x in rounds)} round92_headings={sum(x.startswith("## Round 92") for x in rounds)} r91_fixture_mentions={text.count("r91-c1-null-chain")}/{text.count("r91-c1-tick-unresolved")}')
table=Path('corpus/knowledge/r88-sourced-inspiration-decision-table.md').read_text()
r8=table.split('### R8 appendix',1)[1].split('### R9 appendix',1)[0]
r9=table.split('### R9 appendix',1)[1].split('### R10 appendix',1)[0]
r10=table.split('### R10 appendix',1)[1]
checks={
 'R8_inseparable_whole_element':'inseparable' in r8.lower() and 'whole element' in r8.lower(),
 'R8_failed_gate_not_proof':'not proof' in r8.lower() or 'does not prove source use' in r8.lower(),
 'R9_manual_review':'manual r9 gate' in r9.lower() or 'manual review' in r9.lower(),
 'R9_lexical_receipt_boundary':'lexical preflight' in r9.lower() and 'not that receipt' in r9.lower()}
for k,v in checks.items(): print(f'{k}={v}')
print(f'R8_R9_checks={sum(checks.values())}/{len(checks)} R10_Owner={"Owner:" in r10} R10_Trigger={"Trigger:" in r10} R10_Worked_example={"Worked example:" in r10}')
watch=Path('corpus/knowledge/r91-c9-watch.md').read_text()
tick=Path('corpus/fixtures/r91-c1-tick-unresolved/README.md').read_text()
print(f'watch_e97613c_sha_pinned={"e97613c" in watch and "a4b1b331" in watch} watch_ambiguous_source_wording={"ambiguous source" in watch.lower() or "ambiguous-source" in watch.lower()} watch_successor_named={any(x in watch for x in ("C10","C11","r93"))} tick_parent_or_composition_note={"parent" in tick.lower() or "compos" in tick.lower()}')
files={'R2':'.ufo/waves/round-92/patches/R2-readme.patch','E3':'.ufo/waves/round-92/patches/E3-c3-wording.patch','X1':'.ufo/waves/round-92/patches/X1-recheck.patch','X2':'.ufo/waves/round-92/patches/X2-note.patch'}
for name,path in files.items():
 p=subprocess.run(['git','apply','--check',path],capture_output=True,text=True)
 print(f'patch_{name}_exit={p.returncode}')
for names in (('R2','E3'),('X1','E3')):
 data=b''.join(Path(files[n]).read_bytes() for n in names)
 p=subprocess.run(['git','apply','--check','-'],input=data,capture_output=True)
 print(f'patch_{"+".join(names)}_exit={p.returncode} stderr={p.stderr.decode().strip()!r}')
PY
```

Observed:

```text
README last_round_heading=## Round 90: hedged-shapes repair + support machinery round91_headings=0 round92_headings=0 r91_fixture_mentions=0/0
R8_inseparable_whole_element=False
R8_failed_gate_not_proof=False
R9_manual_review=False
R9_lexical_receipt_boundary=False
R8_R9_checks=0/4 R10_Owner=True R10_Trigger=False R10_Worked_example=False
watch_e97613c_sha_pinned=False watch_ambiguous_source_wording=False watch_successor_named=False tick_parent_or_composition_note=False
patch_R2_exit=0
patch_E3_exit=0
patch_X1_exit=0
patch_X2_exit=0
patch_R2+E3_exit=1 stderr='error: patch failed: corpus/fixtures/README.md:1016\nerror: corpus/fixtures/README.md: patch does not apply'
patch_X1+E3_exit=1 stderr='<stdin>:167: new blank line at EOF.\n+\nerror: patch failed: corpus/knowledge/r91-c9-watch.md:41\nerror: patch does not apply'
```

## Findings & named debt

**JAXIS recommendations** (source: `.ufo/waves/round-91/followup/JAXIS.md:293-306`):

- **R1 — boundary re-derivation: D1 partial; D2 partial.** Both candidates have one H1, nine H2s, one `verified-at`, zero duplicate headings/instruction markers, 13/13 scanned limit markers, seven of seven source fence hashes, and 14/14 pasted-case replays. D1 still says the null-chain fixture is “scratch-only” at `patches/D1-boundary-doc.md:408` and says Round 90 has not landed at `:486`; the candidate contains no `r91-c1-*` fixture names and retains the `Checker at delivered 1b09f3f` label at `:439`. Its header names that D9 evidence block as historical (`:3-5`) but does not correct the contradictory body label; D12 also still lists the Round-90 README insertion as an outside action although that section exists. D2 corrects the r91 fixture and Round-90 history text (`patches/D2-boundary-doc.md:378-382, 441-442, 478-481`) but leaves an orphaned e2bb9639 checker paragraph (`:411-423`), duplicates the r87 README paragraph (`:516` plus the old continuation), and keeps an r90 “Landed” provenance header rather than an r92 re-derivation header (`:21-27`). Neither is a delivered B3 target.
- **R2 — README and governance closure: unaddressed in both candidates.** Tracked README ends at Round 90; no Round 91 section or r91 fixture reference exists. The delivered table is 0/4 for the R8/R9 residual checks; R10 has Owner but no Trigger or Worked example. `R2-readme.patch` proposes a Round 92 section, not the owed Round 91 section; E1 is proposal wording only, and no R10 transfer or R9 probe re-point is integrated (`.ufo/waves/round-92/R2.md:174-184`, `D2.md:284-294`).
- **R3 — watch/census calibration: partial, proposals only.** X1 supplies a first periodic re-check proposal and X2/R2 supply the repo-relative census note, but the tracked watch still lacks the `e97613c` hash, explicit ambiguous-SOURCE wording, and named successor; the tick fixture README still lacks a parent/composition note. The four patches pass individual `git apply --check`; R2+E3 and X1+E3 conflict at README:1016 and watch:41 respectively. Do not represent R3 as landed.

**H5 findings** (source: `.ufo/waves/round-91/followup/H5.md:79-95`):

- **F1 — D9 second range honesty:** D1 `named_debt, still contradictory` (header names the historical block, but body still calls 1b09f3f “delivered”); D2 `partial` (the updated ca7f9ef block is followed by the orphaned e2bb9639 fragment).
- **F2 — row-2 references:** D1 `addressed`; D2 `addressed` (the current row is re-anchored; the single-row test is part of the D1/D2 table replacement).
- **F3 — D6/D7 anchors:** D1 `addressed`; D2 `addressed` (both re-derived candidates use the delivered-checker content anchors; see D1.md and D2.md anchor audits).
- **F4 — D13 status and D2 limits bullet:** D1 `addressed`; D2 `addressed` (both contain the limits set and restored status material; D2 also adds the two r91 fixture references). The separate D2 orphan is tracked under F1/CB1 F4.
- **F5 — lost headings/limits:** D1 `addressed`; D2 `addressed` (the contract, Commands, and Status split sections are present; both retain the 13 checked limits).
- **F6 — stale Round-90/inventory claims:** D1 `unaddressed`; D2 `addressed for H5’s two claims` (it says Round 90 landed at a7c6a17 and updates the inventory with both r91 fixtures). D1 still says “until a Round 90 section lands” and omits both fixture names.
- **F7 — fixtures README Round-91 closure:** both `unaddressed`; tracked README still has no Round 91 section and names neither fixture.
- **F8 — sound replay/freeze items:** both `addressed` for candidate evidence: seven source fenced blocks match, 14/14 embedded cases replay with zero mismatch/empty stderr, and both fixture READMEs match both checker versions (commands/results above). This does not override the unselected status.

**CB1 findings** (source: `.ufo/waves/round-91/followup/CB1.md:222-259`):

- **F1 — assembly defect:** D1 `partial` (structure is repaired, but stale fixture/README claims and checker label remain); D2 `partial` (corrects those claims but leaves the checker seam, duplicated README paragraph, and non-r92 header).
- **F2 — contradictory decision row:** both `addressed` (one current row-3 marker each; no duplicate heading or duplicate row remains in the audited text).
- **F3 — skipped-item accounting:** D1 `partial` (it explicitly lists D8/D9/D12, but the D12 Round-90 README action is stale and the D9 “historical” body remains contradictory); D2 `unaddressed` in the candidate text (no r92 applied/skipped receipt/header is included). S1’s anchor plan records three skips, but that does not repair the candidate's own provenance/accounting.
- **F4 — r89 checker called delivered:** both `partial`; D1 retains the old label, D2 leaves the orphaned e2bb9639 hash/citation fragment after inserting the current checker inventory.
- **F5 — lost contract limits:** both `addressed` (13/13 marker scan and all relevant sections present).
- **F6 — stale delivered-state claims:** D1 `unaddressed`; D2 `addressed` as scoped by CB1 F6 (Round 90 and inventory claims corrected). D1’s old scratch-only null-chain statement is separately retained as R1/F1 debt.
- **F7 — sound parts:** both `addressed` for the measured replay/frozen-checker evidence; no checker modification or regression is claimed.

**Named debt / disposition:** (1) T1 did not select either proposal and its B3 report is fail-closed; (2) D1 needs the r91 fixture/D11, Round-90 README, and historical checker-label contradictions resolved; (3) D2 needs the orphan e2bb9639 block, duplicated README continuation, and explicit r92 provenance/skip receipt reconciled; (4) Round-91 README closure, R8/R9/R10 governance, and remaining watch/fixture notes are still unlanded. R1–R3 must not be described as wholly closed, and positive replay results must not be promoted to document certification.

## Handoff

- Deliverables written by this seat: `.ufo/waves/round-92/CB.md` and `.ufo/waves/round-92/patches/CB-audit.json` only.
- Selection remains **absent**. D1 is a complete proposed document; D2 is an applicable proposed patch; neither was applied, integrated, or certified. T1's current certification outcome is `FAIL` because the required delivered-target candidate is absent. Do not infer selection from D1/D2 availability or from the replay passes.
- Parent integration should first record an explicit candidate selection, resolve that candidate’s named residuals and cross-file patch conflicts, then freeze the exact tracked document and rerun B3 against that delivered tree. No code build/test applies to this audit-only deliverable; its validation is the exact read-only checks recorded above.
- No tracked/staged change, patch application, commit, push, or `/tmp` artifact was made.
