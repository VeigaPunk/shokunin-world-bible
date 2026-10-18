# V26 — OPERABILITY verdict (2026-10-17)

Scope: one OPERABILITY verdict, not round-wide admission or independent semantic review. Axes named for this seat: documented-command executability, exit/result interpretation, scope/path safety, and regression/preservation. The baseline is r99 closure `fe1ce46`; live HEAD was `b5fe472957ab1e4e9c90f5613acc14cd24a288ae` (round-100 declaration), with producer bytes uncommitted.

All commands below ran from `/home/vgpnk/Projects/shokunin/lore-shokunin`, using `python3`. No nested agents, commits, pushes, or network. The only seat writes were this exclusive report and the declared `.ufo/waves/round-100/seats/V26-scratch/`; no producer-owned file or other seat's scratch/report was written. No all-reports poll or bounded stall escape was needed.

## Delivered-artifact wait

Checked both artifacts and actual T1–T4 producer reports, with 20-second sleeps between unsuccessful checks, maximum 40 attempts. The executed poll batches used ranges `range(1,11)`, `range(11,21)`, and `range(21,31)`; readiness arrived at poll 24. The final batch's actual command was:

```sh
python3 - <<'PY'
from pathlib import Path
import time,json
r=Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
for attempt in range(21,31):
    c=json.loads((r/'corpus/tools/dependency-freeze-contract.json').read_text())
    fixture=r/'corpus/fixtures/r100-docket-review'
    knowledge=[r/'corpus/knowledge/r100-crossing-arc-synthesis.md',r/'corpus/knowledge/r100-provenance-semantics-boundary.md']
    seats=r/'.ufo/waves/round-100/seats'
    reports={n:[p.name for p in seats.glob(n+'*.md')] if seats.is_dir() else [] for n in ['T1','T2','T3','T4']}
    ready='r99-window-lapse' in c['pins'] and all((fixture/n).is_file() for n in ['entities.json','relations.json','timeline.json','sources.json','contradictions.json','README.md','claim-excerpt-map.md','fictional-excerpts.md','inspiration-note.md','source-excerpt.md']) and all(p.is_file() for p in knowledge) and all(reports.values())
    print(f'POLL {attempt}/40 ready={ready} pin_r99={"r99-window-lapse" in c["pins"]} fixture_files={len(list(fixture.glob("*"))) if fixture.exists() else 0} knowledge={[(p.name,p.exists()) for p in knowledge]} reports={reports}',flush=True)
    if ready: break
    if attempt<30: time.sleep(20)
PY
```

Observed final line, exit 0:

```text
POLL 24/40 ready=True pin_r99=True fixture_files=10 knowledge=[('r100-crossing-arc-synthesis.md', True), ('r100-provenance-semantics-boundary.md', True)] reports={'T1': ['T1-chain-seven.md'], 'T2': ['T2-fixture-author.md'], 'T3': ['T3-fixture-docs.md'], 'T4': ['T4-knowledge-author.md']}
```

Read all four reports and the delivered fixture README, freeze registry/addendum, synthesis, semantics-boundary note, and dated blind-spot rows before issuing this verdict. The subsequent replay reasserted all producer reports, all ten fixture files, both new notes, and the exact seven-pin set before running commands. Plans and absent artifacts were not treated as delivery.

## Replay and write containment

Actual invocation:

```sh
python3 .ufo/waves/round-100/seats/V26-scratch/run_operability.py
```

Exit 0. It executed 24 real CLI calls with `ThreadPoolExecutor(max_workers=12)` and captured every argv, cwd, complete stdout/stderr, exit, and expected outcome. Complete receipts: `.ufo/waves/round-100/seats/V26-scratch/operability-transcript.txt`; structured results and before/after SHA-256 map: `operability-results.json` in the same directory. These are local receipts, not permanent gate inputs. The runner requires a fresh mirror and deliberately refuses to overwrite its existing mirror on a repeated run.

The copied dependency-freeze tool/contract and map tool/contract were byte-identical to the delivered inputs. Their respective hashes were:

```text
dependency_freeze.py fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c
dependency-freeze-contract.json ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5
map_obligations.py 86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9
map-obligations-contract.json 2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41
```

Freeze/map self-tests ran on those isolated copies because their standard implementations place transient scratch under their script-derived root. Boundary self-test ran the live command with `TMPDIR` set to the absolute `V26-scratch/tmp` directory. All child calls inherited `PYTHONDONTWRITEBYTECODE=1` and `GIT_OPTIONAL_LOCKS=0`. Live fixture/chain checks remained direct calls to delivered files. The live successful `--freeze` operation was not repeated.

Observed terminal audit:

```text
DELIVERED FILES CHANGED DURING REPLAY []
ISOLATED GUARD LEFT CONTRACT UNCHANGED True
CHECKS 24/24 expectations matched
```

## Documented new-fixture commands work end to end

The exact three commands in `corpus/fixtures/r100-docket-review/README.md:26-28` were executed, all exit 0 with empty stderr:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r100-docket-review
python3 corpus/tools/map_obligations.py corpus/fixtures/r100-docket-review
python3 corpus/tools/support_check.py corpus/fixtures/r100-docket-review
```

Observed checker output (complete):

```text
CLEAN: schema, citations, relations, timeline; 0 violations
```

Observed map output (complete):

```text
OBLIGATIONS raw=22 mapped=22
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24
RESULT PASS
```

Observed support excerpts (full per-anchor output retained in the transcript):

```text
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24; DISTINCT-ANCHORS 20/20
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
PASS J22: source-support; mode=verbatim; anchor=found; 82:> Tick 16: After my lapse record, I made the first-passage docket review at the Chalk Stair.
RECEIPT JSON-FACTS 22; EDITORIAL-ROWS 2; TOTAL-ROWS 24
SOURCE-SUPPORT 22/22; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 24/24; VALIDATED-ROWS 24/24
RESULT PASS
```

These commands exercise the delivered fixture, not imports or a plan. The support checker successfully used its real local fixed-string grep calls.

## Seven documented frozen-chain verifications work

The seven exact read-only commands in `corpus/tools/README.md:396-402` were executed independently in the concurrent replay. All exit 0, empty stderr:

```text
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r88-m3-maya-cluster
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0
DIGEST acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae
RESULT PASS
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r94-paired-crossing
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
DIGEST 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef
RESULT PASS
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710
RESULT PASS
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r96-crossing-response
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
DIGEST 43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c
RESULT PASS
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r97-crossing-acknowledgment
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1
DIGEST a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54
RESULT PASS
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r98-clerk-filing
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
DIGEST 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0
RESULT PASS
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r99-window-lapse
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
DIGEST 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e
RESULT PASS
```

## Regression suites and status interpretation

Actual commands and observed outputs (selected receipt lines, complete output in the transcript):

```text
$ python3 .ufo/waves/round-100/seats/V26-scratch/mirror/corpus/tools/dependency_freeze.py --self-test
SELF-TEST 18/18
RESULT PASS
EXIT 0; stderr empty
$ python3 .ufo/waves/round-100/seats/V26-scratch/mirror/corpus/tools/map_obligations.py --self-test
SELF-TEST CASES 25/25 pinned
SELF-TEST PASS dual_pointer exit=1 findings=['dual_pointer']
RESULT PASS
EXIT 0; stderr empty
$ python3 corpus/tools/boundary_doc_check.py
replay_receipts=3/3
replay_cases=14/14
anchors=2/2
CERTIFIED (bounded: frozen-document drift + receipts + explicit-anchor range + structure; no semantic/AST validation)
EXIT 0; stderr empty
$ python3 corpus/tools/boundary_doc_check.py --self-test
SELF-TEST PASS anchor_range_control exit=1 findings=['anchor_range'] anchors=1/2 legacy_anchor=check_bible.py:212-224@5eb9451baff217c19d5786405f9b2aa500b7c1b7 baseline_lines=330
SELF-TEST PASS committed_default exit=0 findings=none
SELF-TEST PASS
EXIT 0; stderr empty
$ python3 corpus/tools/discriminate_check.py
RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression
EXIT 0; stderr empty
$ python3 corpus/tools/discriminate_check.py --checker e97613c
REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved — pinned delivered semantics not present
EXIT 2; stderr empty; expected negative control, not a delivered regression
$ python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93
SNAPSHOT inputs=4 digests=verified
OBLIGATIONS raw=12 mapped=12
INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15
FROZEN expected=PASS/0 findings=none matched
RESULT PASS
EXIT 0; stderr empty
```

The freeze suite separately observed the expected semantic exit-1 findings, named-file digest exit-2 findings, scope/path refusals, and `SELF-TEST-MISMATCH` exit 2. These are capability checks, not semantic certification.

Additional real CLI controls:

```text
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r99-window-lapse --freeze corpus/fixtures/r99-window-lapse
FINDING INVALID-ARGUMENTS: pass either a fixture (verify) or --freeze DIR, not both
RESULT ERROR
EXIT 2; exactly one finding; no DIGEST-MISMATCH; no contract write
$ python3 corpus/tools/dependency_freeze.py .ufo/waves/round-100/seats/V26-scratch/foreign/r99-window-lapse
FINDING PATH-MISMATCH: pin r99-window-lapse names corpus/fixtures/r99-window-lapse (resolves to /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r99-window-lapse); invoked fixture resolves to /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V26-scratch/foreign/r99-window-lapse
RESULT ERROR
EXIT 2
$ python3 .ufo/waves/round-100/seats/V26-scratch/mirror/corpus/tools/dependency_freeze.py --freeze .ufo/waves/round-100/seats/V26-scratch/foreign/r99-window-lapse
FINDING SCOPE-REFUSED: --freeze refuses .ufo/waves/round-100/seats/V26-scratch/foreign/r99-window-lapse (resolves to /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V26-scratch/foreign/r99-window-lapse); the frozen scope is corpus/fixtures/** (integration-time operation only)
RESULT ERROR
EXIT 2; isolated contract unchanged
$ python3 corpus/tools/dependency_freeze.py --help
usage: dependency_freeze.py [-h] [--freeze DIR] [--self-test] [fixture]
EXIT 0; no RESULT line; help is not a clean verification
$ python3 corpus/tools/map_obligations.py
FINDING invalid_arguments: cluster directory is required
RESULT ERROR
EXIT 2
$ python3 corpus/tools/support_check.py
RESULT ERROR
EXIT 2; stderr='usage: support_check.py [-h] [--map MAP] cluster\nsupport_check.py: error: the following arguments are required: cluster\n'
```

All controls matched their expected outcomes. Non-zero controls are retained as evidence, not hidden or misclassified as clean verification.

## Preservation and final-file stability

Actual baseline comparison command:

```sh
python3 - <<'PY'
from pathlib import Path
import hashlib,json,subprocess
r=Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
base=json.loads(subprocess.check_output(['git','show','fe1ce46:corpus/tools/dependency-freeze-contract.json'],text=True))
current=json.loads((r/'corpus/tools/dependency-freeze-contract.json').read_text())
print('PIN ADDITIONS',sorted(set(current['pins'])-set(base['pins'])))
print('PRIOR PINS IDENTICAL',sum(current['pins'][k]==v for k,v in base['pins'].items()),'/',len(base['pins']))
print('CHANGED NON-PIN KEYS',[k for k in current if k!='pins' and current[k]!=base.get(k)])
for path in [r/'corpus/fixtures/check_bible.py',*sorted((r/'corpus/tools').glob('*.py'))]:
    rel=str(path.relative_to(r))
    old=subprocess.run(['git','show','fe1ce46:'+rel],capture_output=True).stdout
    print('BASELINE BYTE IDENTICAL',rel,path.read_bytes()==old,'SHA256',hashlib.sha256(path.read_bytes()).hexdigest())
PY
```

Observed exit 0: `PIN ADDITIONS ['r99-window-lapse']`, `PRIOR PINS IDENTICAL 6 / 6`, `CHANGED NON-PIN KEYS ['revision']`; all six Python files (`check_bible.py` and the five tool scripts) printed `True`. The checker hash remained `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`. The guarded writer's top-level revision refresh is disclosed in both updated freeze documents; it is not a prior-pin change.

`git diff --check` was also run directly: exit 0, empty output. This checks tracked diffs only and is not offered as a whitespace audit of the untracked new files.

The runner monitored 94 distinct delivered input files: the producer deliverables, all seven pins' ten-file fixtures, checker/tool files and contracts. Its before/after hashes matched; a later lane-root `python3 -` audit loaded `operability-results.json` and rehashed those delivered files, observing:

```text
REPLAY EXPECTATIONS 24 / 24
MONITORED DELIVERED FILES 94
REPLAY STABILITY True
POST-REPLAY STABILITY True
LOCAL EXECUTABLE python3 /usr/bin/python3
LOCAL EXECUTABLE git /usr/bin/git
LOCAL EXECUTABLE grep /usr/bin/grep
PRIOR PINS UNCHANGED 6
PIN ADDITIONS ['r99-window-lapse']
TOP-LEVEL CHANGED KEYS ['revision']
REPORT PATH VERIFIED /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V26-verdict-operability.md
```

## Bounds and exact seat-write inventory

The new review is intentionally not frozen. This actual delivered-tree command confirms the boundary rather than silently granting extra coverage:

```text
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r100-docket-review
FINDING UNPINNED-FIXTURE: no pin for 'r100-docket-review' in corpus/tools/dependency-freeze-contract.json (pinned: ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response', 'r97-crossing-acknowledgment', 'r98-clerk-filing', 'r99-window-lapse'])
RESULT ERROR
EXIT 2
```

This is consistent with C1's declared seven-fixture set and the updated documentation, not a broken advertised command. r100 tick-16 freeze coverage remains a future candidate. Other retained bounds: r88's extra `symbolism-clause-map.md` is outside the ten-file set; support/discriminator have no self-test flag; freeze/map standard self-tests create scratch under their script-derived root; byte identity is not prose entailment or dependency-semantics proof. This seat did not re-roll standing historical failures, certify all corpus fixtures, decide testimony/chronology/rights/permission/canon, or grant round-wide admission.

All written paths are under `/home/vgpnk/Projects/shokunin/lore-shokunin/`:

- `.ufo/waves/round-100/seats/V26-verdict-operability.md` (this report).
- `.ufo/waves/round-100/seats/V26-scratch/run_operability.py` (new isolated runner).
- `.ufo/waves/round-100/seats/V26-scratch/operability-transcript.txt` (complete real-call receipts).
- `.ufo/waves/round-100/seats/V26-scratch/operability-results.json` (structured receipts and input hashes).
- `.ufo/waves/round-100/seats/V26-scratch/mirror/corpus/tools/dependency_freeze.py`.
- `.ufo/waves/round-100/seats/V26-scratch/mirror/corpus/tools/dependency-freeze-contract.json`.
- `.ufo/waves/round-100/seats/V26-scratch/mirror/corpus/tools/map_obligations.py`.
- `.ufo/waves/round-100/seats/V26-scratch/mirror/corpus/tools/map-obligations-contract.json`.
- Each of the following three complete copy roots contains exactly these ten files: `README.md`, `claim-excerpt-map.md`, `contradictions.json`, `entities.json`, `fictional-excerpts.md`, `inspiration-note.md`, `relations.json`, `source-excerpt.md`, `sources.json`, `timeline.json`:
  - `.ufo/waves/round-100/seats/V26-scratch/mirror/corpus/fixtures/r95-crossing-aftermath/`.
  - `.ufo/waves/round-100/seats/V26-scratch/mirror/corpus/fixtures/r99-window-lapse/`.
  - `.ufo/waves/round-100/seats/V26-scratch/foreign/r99-window-lapse/`.

Temporary self-test descendants were created and automatically removed inside this scratch. No required background task remains; no unresolved operability blocker was found.

PASS — OPERABILITY is not harmed on the delivered revision: new-fixture replay works, frozen chain verifies 7/7, all 24 command expectations match, regression suites pass, scope/path/usage guards retain their contracts, and 94 monitored delivered inputs remain unchanged.
