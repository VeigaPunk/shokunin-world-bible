# JCAL5 — method-varied census (python3 -I, shuffled seed 9101, regenerated baseline)

Seat: JCAL5 (round-91 follow-up wave). Delivered tree: `c2ab3d0` (HEAD at run time; `git status --short` clean apart from the follow-up artifacts). Baseline: `a7c6a17`; old checker commit: `e97613c`.
Receipt: `.ufo/waves/round-91/followup/JCAL5-delta.json` (135,197 bytes, SHA-256 `303457ab61475bf2e689c813cdd7d23f9a7f9290d85c6a01c1060d41b4f1c097`).

## Work performed

Axes: **reproducibility of the C1 census claim**, **evidence integrity**, **no-harm** (baseline receipts untouched, no tracked writes outside the follow-up directory).

Method variation from B1/B2: driver and every checker subprocess run under `python3 -I`; baseline **regenerated** from `a7c6a17` blobs via `git archive` (not read from B1/B2 receipts — those were used only as an after-the-fact cross-check); iteration order = union of baseline+delivered fixture names shuffled with `random.Random(9101)`; then a replicate with seed 4242. Three censuses were run over the same seeded order:

- **A (regenerated baseline):** per fixture, `tar -xf base.tar -C work corpus/fixtures/<name>`, then `python3 -I corpus/fixtures/check_bible.py corpus/fixtures/<name>` with cwd=`work` (baseline checker extracted from the same archive), then `rm -rf` the extracted dir — one fixture materialized at a time, file-frugal under inode pressure (`/tmp` at 100% inode use, IFree≈1.7k; peak scratch ≈12 inodes: 1 tar + 1 checker + 1 fixture dir + receipt).
- **B (delivered):** `python3 -I corpus/fixtures/check_bible.py corpus/fixtures/<name>` with cwd at repo root, over the delivered tree on disk.
- **C (discrimination recheck):** `git show e97613c:corpus/fixtures/check_bible.py > $scratch/old_checker.py`; `python3 -I $scratch/old_checker.py corpus/fixtures/<name>` with cwd at repo root, over the delivered fixtures.
- **Replicate:** delivered census again with `random.Random(4242)`; compared tuple-wise to run B.

Acceptance criteria (from the seat mandate): reproduce the **0 changed + 2 new of 166** delta and the C1 discrimination claim, with receipts. The checker hash pin in `corpus/knowledge/r91-c9-watch.md` was also string-checked.

Exactly run, exact outputs:

```sh
git archive --format=tar -o $scratch/base.tar a7c6a1773d5994246a76e4eff30d645f161920e0 corpus/fixtures
# git_archive_exit=0 tar_bytes=1525760
sha256sum corpus/fixtures/check_bible.py
# ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
git show a7c6a17:corpus/fixtures/check_bible.py | sha256sum
# ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  -
git show e97613c:corpus/fixtures/check_bible.py | sha256sum
# e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556  -
```

Driver (`python3 -I`, heredoc; full script logic and all rows in `JCAL5-delta.json`):

```text
names_baseline=164 names_delivered=166 union=166
shuffle_seed=9101 first8=['r20-negative-prereq', 'r23-note-class', 'r22-unknown-mixed', 'r21-malformed',
  'r35-bell7-conflict', 'r34-tarin-hearsay', 'r62-independent', 'r9-dup-low-high']
baseline_only=[] delivered_only=['r91-c1-null-chain', 'r91-c1-tick-unresolved']
BASELINE   dirs=164 exits={0: 32, 1: 132} violations=417 stderr_nonempty=0
DELIVERED  dirs=166 exits={0: 32, 1: 134} violations=421 stderr_nonempty=0
OLD-CHECKER dirs=166 exits={0: 32, 1: 134} violations=421 stderr_nonempty=0
DELTA shared=164 changed_shared=[] added=['corpus/fixtures/r91-c1-null-chain','corpus/fixtures/r91-c1-tick-unresolved'] removed=[]
DISCRIMINATION changed_under_old=['corpus/fixtures/r91-c1-null-chain','corpus/fixtures/r91-c1-tick-unresolved']
  exit_changes=[] stderr_changes=[]
CROSS_CHECK B1 mismatches=0 rows=164; B2 mismatches=0 rows=164
FILE_DELTA added=12 modified=['r87-myth-cluster/claim-excerpt-map.md','r88-m3-maya-cluster/claim-excerpt-map.md',
  'r89-inspiration-paraphrase/claim-to-excerpt-map.md'] deleted=[]
C9_WATCH_PIN=True
replicate_seed=4242 dirs=166 mismatches_vs_seed9101=[]
README blocks: r91-c1-null-chain {block0==e97613c: True, block1==delivered: True}
              r91-c1-tick-unresolved {block0==e97613c: True, block1==delivered: True}
```

Tuple = `(exit, stdout_sha256, violation_count, stderr empties)`. B1/B2 cross-check used their stored `(exit, stdout_sha256, violation_count)` triples for the 164 shared fixture paths.

## Before → after measurements

**The 0+2 delta is reproduced exactly.** Regenerated baseline (census A): 164 fixture dirs, exits {0:32, 1:132}, 417 `VIOLATION:` lines total, stderr empty for all 164. Delivered (census B): 166 dirs, exits {0:32, 1:134}, 421 violations, stderr empty. Delta by fixture path: `shared=164`, `changed_shared=[]` → **0 changed**; `added` = `r91-c1-null-chain`, `r91-c1-tick-unresolved` → **+2 new** of **166**; `removed=[]`.

**Cross-check (independent receipts).** Every one of my 164 regenerated-baseline rows equals the corresponding B1 row (0 mismatches) and the B2 row (0 mismatches). Together with my two shuffled orders (9101, 4242 — replicate had 0 mismatches), the census is now stable under three distinct iteration orders: sorted (B1), reverse (B2), shuffled (this seat).

**Discrimination reproduced (C1).** Running the `e97613c` checker over the 166 delivered fixtures changes stdout for exactly the two new fixtures and nothing else; exits and stderr are unchanged on all 166 (`changed_under_old` = the two added paths; `exit_changes=[]`, `stderr_changes=[]`). The diffs are exactly the declared repaired lines, one line each:

```text
r91-c1-null-chain (old → delivered):
- VIOLATION: entities[3].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'mira'; got None; from_holder None is not uniquely resolvable (0 raw entity rows carry this id, but only 0 is in the resolved index)
+ VIOLATION: entities[3].provenance[1]: provenance chain break; expected from_holder 'mira', got None

r91-c1-tick-unresolved (line 2 of 3, old → delivered):
- VIOLATION: entities[4].provenance[1].tick: input-structural finding, not sourced-canon; holder identity is not uniquely resolvable: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); provenance tick 1 must be greater than previous tick 3
+ VIOLATION: entities[4].provenance[1].tick: provenance tick 1 must be greater than previous tick 3
```

The tick fixture's separately qualified chain-break line is byte-identical under both checkers. Each new fixture's README `text` blocks both match reality byte-for-byte: block 0 = `e97613c` stdout, block 1 = delivered stdout.

**Checker pin.** Delivered file SHA-256 == `a7c6a17` blob SHA-256 == `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`; the string is present in `corpus/knowledge/r91-c9-watch.md`. So the baseline and delivered runs are checker-comparable, and "r91 does not touch the checker" holds at blob level (the checker does not appear in `git diff --raw a7c6a17 c2ab3d0 -- corpus/fixtures`).

**File-level vs tuple-level delta (explicit separation).** `git diff --raw a7c6a17 c2ab3d0 -- corpus/fixtures`: 12 added files (the two new fixture dirs), 0 deleted, 3 modified — all three are map markdown (the paths above), none is a checker input. No shared fixture JSON changed, which together with the pinned checker and stderr/stdout determinism fully explains the 0 changed tuples.

## Findings & named debt

- Verdict for the seat's axes: **reproduced exactly, evidence improved, nothing harmed.** The "0 changed + 2 new of 166" census delta and the C1 discrimination claim both hold under a third independent census method (regenerated `git archive` baseline, `python3 -I`, seeded shuffle) and under a replicate order; the two stored baseline receipts agree row-for-row with the regenerated one.
- The census is a **tuple-level** instrument (exit, stdout hash, violation count, stderr). It is deliberately blind to the 3 modified map `.md` files (r91 C2's wording fixes) — the "0 changed" statement is output-level, not byte-level. Named so nobody reads it as "no file changed". Also, README inner consistency was byte-checked only for the 2 new fixtures, not for the 164 legacy ones.
- Method honesty: two of my scratch driver iterations failed before writing anything to the repo (first: `git ls-tree <commit> corpus/fixtures` returns the tree itself, so baseline names parsed as 1; second: a copy of the replicate script double-prefixed paths → KeyError). Neither aborted run wrote the receipt or touched tracked files; the receipt on disk is from the corrected driver, and the replicate figures come from the corrected rerun.
- Scratch: one tar (1,525,760 bytes) + per-fixture extract-run-delete under `/tmp/lore-r91-JCAL5`; directory removed at exit; other seats' `/tmp` dirs (C10, H2, JCAL2, JCOV3, jcov4) were left untouched; `/tmp` inode usage was 100% throughout (IFree ~1.7–1.8k), which is why no full baseline extraction was done.

## Handoff

- Artifacts: `.ufo/waves/round-91/followup/JCAL5.md` (this file) and `.ufo/waves/round-91/followup/JCAL5-delta.json` — full rows for census A (164), B (166), C (166), the delta, discrimination lines, B1/B2 cross-check, file-level delta, seed receipts, replicate, and README byte-exactness. JSON parses (`python3 -I -m json.tool`-equivalent load OK).
- No other tracked writes; no commit/push. `git status --short` shows only `?? .ufo/waves/round-91/followup/`.
- For the parent/verifier: the seat's mandate is discharged — the 0+2 delta reproduces exactly and the discriminating pair is the only output-level change in the delivered fixture census. Nothing left unverified within the mandate; the named debt (tuple-level scope; legacy READMEs unchecked; sibling scratch dirs left in place) is as above.

**Cross-seat consistency (post-handoff check, read-only).** Sibling `followup/H4-census.json` (independent `python3 -I` census) reports the same headline numbers: baseline 164 dirs / exits {0:32, 1:132} / 417 violations; delivered 166 / {0:32, 1:134} / 421; changed=0, added=2 (`r91-c1-null-chain`, `r91-c1-tick-unresolved`), removed=0, delivered stderr non-empty=0. Row-level: H4's 166 rows vs my baseline rows, 0 tuple mismatches. So the 0+2 delta now stands under four independent runs by three seats (B1 sorted, B2 reverse, H4, and this seat shuffled 9101 + replicate 4242).