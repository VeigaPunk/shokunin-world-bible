# V21 — documented-command operability (2026-10-17)

Seat scope: commands in T3's delivered fixture README, T4's three corpus knowledge notes (only the dated r100 additions in the inherited r99 table), and the tools README Round-100 addendum. Axes: command reproducibility, exact-output agreement, ownership/read-only safety. This is not round-wide admission or semantic certification.

Baseline: r99 closure `fe1ce46`; observed live HEAD `b5fe472957ab1e4e9c90f5613acc14cd24a288ae`, the declaration revision. All commands ran from `/home/vgpnk/Projects/shokunin/lore-shokunin`; Python commands used `python3`.

## Result and strict bound

- **21/21 ownership-safe literal commands matched**: 20 Python commands plus the documented contract `git diff`. Expected negative controls returned their documented non-zero exits; these are positive reproductions, not unexpected failures. Every stderr was empty.
- **Two relocated harness copies passed**: the arc audit made 21 real gate calls, all exit 0; the correction replay made 10 real calls, all expected exits, including `SELF-TEST 18/18`. Only each copy's `SCRATCH` assignment changed from T4 to V21.
- **Universal “every command runs as written” remains unproved by this seat**: T4's two documented logging harness invocations were not executed literally because they overwrite T4-owned scratch. Their underlying read-only commands were executed literally, and their relocated harness copies passed. This is a verification-ownership bound, not an observed failing command.
- The historical integration-time `--freeze` example is explicitly **not a verification command** (`corpus/tools/README.md:371`); it was not rerun against the delivered contract. T1's actual producer receipt was read, and its resulting pin/verification command was independently exercised.

Complete literal commands, stdout, stderr, expected/observed exits and assertion results: `.ufo/waves/round-100/seats/V21-scratch/command-output.txt` and `results.json`. Relocated harness receipts: `arc-output.txt`, `arc-results.json`, `replay-output.txt`, `replay-results.json` in the same V21 scratch directory.

## Artifact/report wait

The initial `pwd && ls -la && ls -la .ufo/waves/round-100/seats` observed the correct lane cwd, then `ls: cannot access '.ufo/waves/round-100/seats': No such file or directory`, exit 2. This was pre-delivery absence, not a delivered-command failure.

Polled artifact presence **and** T1–T4 report presence at 20-second spacing, maximum 40 polls; readiness occurred at poll 23. The final actual polling call was:

```sh
python3 - <<'PY'
from pathlib import Path
from time import sleep
root=Path('/home/vgpnk/Projects/shokunin/lore-shokunin').resolve()
for attempt in range(23,29):
    sleep(20)
    seats=root/'.ufo/waves/round-100/seats'
    reports=sorted(p.name for p in seats.glob('T*.md')) if seats.exists() else []
    artifacts=[root/'corpus/fixtures/r100-docket-review/README.md',root/'corpus/fixtures/r100-docket-review/claim-excerpt-map.md',root/'corpus/knowledge/r100-crossing-arc-synthesis.md',root/'corpus/knowledge/r100-provenance-semantics-boundary.md']
    print(f'POLL {attempt}/40: reports={reports}; artifacts='+str({p.name:p.is_file() for p in artifacts}),flush=True)
    if all(p.is_file() for p in artifacts) and all(any(p.startswith(f'T{i}-') for p in reports) for i in (1,2,3,4)):
        print('READY',flush=True); break
PY
```

Observed exit 0:

```text
POLL 23/40: reports=['T1-chain-seven.md', 'T2-fixture-author.md', 'T3-fixture-docs.md', 'T4-knowledge-author.md']; artifacts={'README.md': True, 'claim-excerpt-map.md': True, 'r100-crossing-arc-synthesis.md': True, 'r100-provenance-semantics-boundary.md': True}
READY
```

T1, T3, and T4 producer reports were read. No producer plan was verified as an implementation. No all-reports poll, self-inclusive endgame wait, stall escape, or background task was needed.

## T3 README: all three literal commands

Actual command (`README.md:26`), exit 0:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r100-docket-review
```

Complete stdout:

```text
CLEAN: schema, citations, relations, timeline; 0 violations
```

Actual command (`README.md:27`), exit 0:

```sh
python3 corpus/tools/support_check.py corpus/fixtures/r100-docket-review
```

Selected observed stdout (complete per-anchor output is in the V21 transcript):

```text
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24; DISTINCT-ANCHORS 20/20
PASS J22: source-support; mode=verbatim; anchor=found; 82:> Tick 16: After my lapse record, I made the first-passage docket review at the Chalk Stair.
SOURCE-SUPPORT 22/22; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 24/24; VALIDATED-ROWS 24/24
RESULT PASS
```

Actual command (`README.md:28`), exit 0:

```sh
python3 corpus/tools/map_obligations.py corpus/fixtures/r100-docket-review
```

Complete stdout:

```text
OBLIGATIONS raw=22 mapped=22
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24
RESULT PASS
```

These same commands also occur in T4's synthesis and were deduplicated in the literal-command count.

## Tools README addendum: seven live pins and the negative control

The seven commands at `corpus/tools/README.md:396-402` were executed independently and concurrently, exactly as written:

```sh
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r88-m3-maya-cluster
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r94-paired-crossing
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r96-crossing-response
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r97-crossing-acknowledgment
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r98-clerk-filing
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r99-window-lapse
```

Every command exited 0 and printed `RESULT PASS`. Observed receipts and digests:

```text
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0
DIGEST acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
DIGEST 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
DIGEST 43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1
DIGEST a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
DIGEST 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0
FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1
DIGEST 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e
```

Actual negative-control command (`corpus/tools/README.md:410`):

```sh
python3 .ufo/waves/round-100/seats/T1-scratch/corpus/tools/dependency_freeze.py .ufo/waves/round-100/seats/T1-scratch/corpus/fixtures/r99-window-lapse
```

Observed complete stdout, expected exit 1:

```text
FREEZE r99-window-lapse: events 8/8; dependency-edges 6/7; relations 1/1
FINDING REDUCTION-DETECTED: event clerk-lapse-recorded lost depends_on ['clerk-filing-open']
RESULT FAIL
```

Actual inline command (`corpus/tools/README.md:389`):

```sh
git diff fe1ce46 -- corpus/tools/dependency-freeze-contract.json
```

Observed exit 0. Diff hunks `@@ -32,7 +32,7 @@` and `@@ -554,6 +554,129 @@` show the top-level revision changing `337f0fa52b02626b7687eedbb2d99fab30446fe4` → `b5fe472957ab1e4e9c90f5613acc14cd24a288ae`, and the new r99 pin. The exact diff is in the V21 transcript; the documentation's metadata qualification is accurate.

The displayed `python3 corpus/tools/dependency_freeze.py --freeze corpus/fixtures/r99-window-lapse` at line 374 is a historical integration receipt explicitly prohibited from being rerun for verification. I did not execute it or hand-edit the contract.

## T4 dated rows: every read-only individual command reproduced

Row 10, historical support command (`r99-gate-blind-spot-table.md:287`):

```sh
python3 .ufo/waves/round-100/seats/T4-scratch/replays/pre-r99-anchor/corpus/tools/support_check.py .ufo/waves/round-100/seats/T4-scratch/replays/pre-r99-anchor/corpus/fixtures/r95-crossing-aftermath
```

Row 10, delivered support command (line 288):

```sh
python3 corpus/tools/support_check.py .ufo/waves/round-100/seats/T4-scratch/replays/delivered-anchor/corpus/fixtures/r95-crossing-aftermath
```

Both observed expected exit 1, including:

```text
FAIL J14: source-support; mode=verbatim; anchor=not-found
SOURCE-SUPPORT 14/15; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 17/17; VALIDATED-ROWS 16/17
FAIL: J14: source-support anchor missing
RESULT FAIL
```

Historical freeze control (line 303):

```sh
python3 .ufo/waves/round-100/seats/T4-scratch/replays/pre-r99-anchor/corpus/tools/dependency_freeze.py .ufo/waves/round-100/seats/T4-scratch/replays/pre-r99-anchor/corpus/fixtures/r95-crossing-aftermath
```

Observed complete stdout, exit 0:

```text
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
RESULT PASS
```

Delivered freeze control (line 315):

```sh
python3 .ufo/waves/round-100/seats/T4-scratch/replays/delivered-anchor/corpus/tools/dependency_freeze.py .ufo/waves/round-100/seats/T4-scratch/replays/delivered-anchor/corpus/fixtures/r95-crossing-aftermath
```

Observed expected exit 2, `FINDING DIGEST-MISMATCH` naming `fictional-excerpts.md`, `RESULT ERROR`; content digest `b97a3b80df29110f6f369c7bd52ee09cd733e46f3f7d84420563c931744f7dca` versus pin `97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710`. Complete digest finding matches the note and is in the V21 transcript.

The two inline commands at line 324:

```sh
python3 corpus/fixtures/check_bible.py .ufo/waves/round-100/seats/T4-scratch/replays/delivered-anchor/corpus/fixtures/r95-crossing-aftermath
python3 corpus/tools/map_obligations.py .ufo/waves/round-100/seats/T4-scratch/replays/delivered-anchor/corpus/fixtures/r95-crossing-aftermath
```

Both exited 0. Checker stdout was `CLEAN: schema, citations, relations, timeline; 0 violations`; map stdout was:

```text
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
RESULT PASS
```

Row 11 edge-plus-prose command (line 331):

```sh
python3 .ufo/waves/round-100/seats/T4-scratch/replays/delivered-precedence/corpus/tools/dependency_freeze.py .ufo/waves/round-100/seats/T4-scratch/replays/delivered-precedence/corpus/fixtures/r98-clerk-filing
```

Observed complete stdout, expected exit 1:

```text
FREEZE r98-clerk-filing: events 7/7; dependency-edges 5/6; relations 1/1
FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']
RESULT FAIL
```

No `DIGEST-MISMATCH`. This entire stdout was also compared for exact equality with the note's output block and matched.

Row 11 prose-only command (line 345):

```sh
python3 .ufo/waves/round-100/seats/T4-scratch/replays/delivered-prose-control/corpus/tools/dependency_freeze.py .ufo/waves/round-100/seats/T4-scratch/replays/delivered-prose-control/corpus/fixtures/r98-clerk-filing
```

Observed complete stdout, expected exit 2:

```text
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
FINDING DIGEST-MISMATCH: content digest c811669ea2534d48122939e270599376160b8f5936eecb2e766c141464b6808b != pin 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0; changed: fictional-excerpts.md (sha256 29e384bf2eb2ab80858ace9423f29088a552553f87da7f6a9b694cbb050666de -> dbcd5f11f4260f0e85c3271698afe1bac79ace52c31e9b651187371fb79e4b26); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
```

The entire stdout exactly matched the note's output block.

Row 12 command (line 361; also provenance boundary line 50):

```sh
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r98-clerk-filing --freeze corpus/fixtures/r98-clerk-filing
```

Observed complete stdout, expected exit 2:

```text
FINDING INVALID-ARGUMENTS: pass either a fixture (verify) or --freeze DIR, not both
RESULT ERROR
```

Exactly one finding, no verification receipt, no digest finding, no contract write. The entire stdout exactly matched the note's output block. Contract SHA-256 stayed `ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5`.

Before accepting mirror-based receipts, a lane-root `python3 -` check compared all 12 delivered mirror tool/contract/support files byte-for-byte to live inputs and all 3 historical mirror inputs to actual `git show 4265df5:<path>` output. Observed exit 0: `T4 DELIVERED MIRROR INPUTS 12/12 byte-identical to live` and `T4 HISTORICAL MIRROR INPUTS 3/3 byte-identical to 4265df5`.

## T4 convenience harnesses: safe relocated execution, not literal execution

These two documented commands were **not** run literally:

```sh
python3 .ufo/waves/round-100/seats/T4-scratch/arc_audit.py
python3 .ufo/waves/round-100/seats/T4-scratch/replay.py run
```

Reason: `T4-scratch/arc_audit.py:98-99` writes T4's `arc-results.json` and `arc-output.txt`. `T4-scratch/replay.py:52-55` overwrites T4 mirror tools/contracts/support scripts; line 73 invokes a self-test that writes temporary files within T4 scratch; lines 116-117 overwrite T4 replay receipts. This verifier owns none of those paths. No attempted forbidden write was made.

I copied both scripts and the existing replay mirrors into V21 scratch, verified pre-relocation script bytes were identical, then used Read→Edit to change only:

```text
SCRATCH = ROOT / '.ufo/waves/round-100/seats/T4-scratch'
```

to:

```text
SCRATCH = ROOT / '.ufo/waves/round-100/seats/V21-scratch'
```

The live lane `ROOT` and all gate logic remained unchanged. A subsequent byte comparison confirmed this was the only delta in each script. Actual safe commands, run concurrently from the lane root:

```sh
python3 .ufo/waves/round-100/seats/V21-scratch/arc_audit.py
python3 .ufo/waves/round-100/seats/V21-scratch/replay.py run
```

Arc command observed exit 0: all 21 real checker/support/map calls against r94–r100 exited 0; map obligation counts `14,15,16,17,20,21,22`; every step's eight preservation booleans was `True`; `CENSUS 174`; `ARC-AUDIT failures=[]`. Exact child commands and full stdout are in V21 `arc-output.txt`; this is actual execution, not an import-only check.

Replay command observed exit 0:

```text
A1-pre-r99-support: exit=1 expected=1
A2-pre-r99-freeze: exit=0 expected=0
A3-delivered-support: exit=1 expected=1
A4-delivered-freeze: exit=2 expected=2
A5-delivered-check-bible: exit=0 expected=0
A6-delivered-map: exit=0 expected=0
B1-semantic-precedence: exit=1 expected=1
B2-prose-control: exit=2 expected=2
C1-combined-invalid: exit=2 expected=2
SELF-delivered-freeze: exit=0 expected=0
SELF-TEST 18/18
RESULT PASS
CONTRACT before=ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5 after=ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5 unchanged=True
REPLAY failures=[]
```

These relocated successes establish useful capability evidence but are **not** silently counted as exact execution of the two T4-owned harness commands. If the parent requires the universal literal-replay condition, those two invocations still need an authorized owner or an authorized configurable output-root interface. No producer-code change was made by V21.

## Snapshot, ownership, and handoff

The following inputs were hashed before literal replay and checked again after both relocated harnesses; no input changed:

```text
corpus/fixtures/r100-docket-review/README.md a312a364d4d9476e98c0fae3f62b23bf72e73a06c508aac04ffe48cf9cf4c5fa
corpus/tools/README.md c99217cd0663125214cee7007951a1b9ae98f466f7081344c03ad0f45f87f399
corpus/knowledge/r100-crossing-arc-synthesis.md 6fcffc8154a11419adbcaefba6d728ee544af831cb5e1b999429404c3b243acc
corpus/knowledge/r100-provenance-semantics-boundary.md 29cc7d856b2600bbb03dec577487bc0f09525ab444a3e3109ef0040ab7edeb36
corpus/knowledge/r99-gate-blind-spot-table.md f1b3719a3954bbae44562f9e01b99434327ff50fba0c3a0755634dc9d76830ff
corpus/tools/dependency-freeze-contract.json ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5
```

Final lane-root `python3 -` assertions observed exit 0:

```text
LITERAL 21/21 matched; RELOCATED ARC 21/21 exit 0; RELOCATED REPLAY 10/10 expected exits
CENSUS 174
FINAL delivered documents and contract unchanged
SCRATCH FILES 77 total bytes 701712
VERIFIED REPORT BEFORE WRITE /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V21-operability.md
```

Writes were confined to this exclusive absolute report path and declared `.ufo/waves/round-100/seats/V21-scratch/`. The exhaustive 77-file scratch path list is `V21-scratch/file-manifest.json`; it includes the two relocated scripts, copied five replay mirrors, and generated JSON/text receipts. Temporary self-test subtrees were created and removed only inside V21 scratch. No live fixture/tool/contract/document edit, nested agent, commit, push, network call, or other-seat write was made. No needed background task remains.

No actual documented command replay failed its expected result. Operability of the ownership-safe surface is demonstrated; whole-claim semantics, testimony truth, chronology authentication, rights, permission, and canon remain outside these receipts.

INCONCLUSIVE — 21/21 ownership-safe literal commands matched and both relocated harnesses passed, but the universal literal-command requirement is not fully verified because T4's two logging harness commands would overwrite T4-owned scratch; the explicitly historical guarded freeze was not rerun.
