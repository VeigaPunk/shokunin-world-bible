# JCAL2 — Calibration judge #2 (adversarial), round-89 FOLLOW-UP

Seat: **JCAL2**. Judge target: the delivered tree at `1b09f3f` (work commit; baseline `51b286b`), C1 only.
Delivered-tree evidence unless a command says otherwise; all probes and baseline archives lived in `/tmp`.

## Work performed

- Confirmed the delivered checker is the reviewed candidate byte-for-byte:
  `sha256sum corpus/fixtures/check_bible.py` → `e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556`
  (identical to C5's post-`X1-c1.patch` hash, `.ufo/waves/round-89/C5.md`), and the pinned baseline checker is
  `dcacffd6981e1af5f60b31bed20c6eccce25970444088e4ee2e30e3249411911`. `git rev-parse HEAD` → `1b09f3ff8016b26a2259e086f673d0112f4f54e5`.
- Read the wave evidence from the delivered tree: `X1.md` (implementation), `C5.md`, `C6.md` (adversarial reviews), `F1/F2/F3.md`
  (fixture seats), and the twelve sibling follow-up reports in `.ufo/waves/round-89/followup/` (JCAL1, JCAL3, JCOV1, JCOV3,
  JCOV4, JDEP2, JDEP4, H1, H2, H5, P4, V2) — cited below where they overlap my measurements.
- **Dependency check (no wait needed).** The brief's two 60s wait-checks were moot on arrival: `.ufo/waves/round-89/patches/X1-c1.patch`
  mtime `2026-10-17 03:52:46 -0300`, `C5.md` 03:58, `C6.md` 04:02, the sibling follow-up reports 04:19–04:20, work commit 04:15:31;
  my first measurement was 04:29. Nothing was pending; no gap to note beyond the one recorded in “Findings”.
- Built 22 generated probe directories (two batches) under `/tmp/lore-r89-JCAL2.mk/probes{,2}` covering: the four FN-1 branch
  combinations (holder/source × raw-present/truly-absent) plus an over-a-broken-table control; four FN-2 controls; C5 and C6 debt
  reproductions plus an extension; and C1 summary controls. Ran each against the delivered checker and the pinned baseline checker.
- Ran an independent 160-directory census with both checkers. Repository writes: this report and `JCAL2-probes.json` only.
- Environment note for sibling seats: `/tmp` tmpfs is at **100% inodes** (`df -i /tmp`: 1 042 000/1 048 576 used) with 9.7G space free.
  New scratch must be file-frugal; I kept every probe to 5 small JSON files and did not extract full trees.

## Before → after measurements

### Delivered-tree identity and census (independent)

```sh
cd /home/vgpnk/Projects/shokunin/lore-shokunin
for d in corpus/fixtures/*/; do n=${d#corpus/fixtures/}; n=${n%/}; [ "$n" = "check_bible.py" ] && continue; \
  o=$(python3 corpus/fixtures/check_bible.py "$d" 2>&1); printf '%s\texit=%s\n' "$n" "$?" >> /tmp/lore-r89-JCAL2.mk/census160.txt; done
```

Observed: `dirs=160 clean=32 dirty=128`. Same loop with the pinned baseline checker
(`/tmp/lore-r89-JCAL2.mk/base-check_bible.py`, `dcacffd6…`) gave `32 exit=0`, `128 exit=1`, and
`diff` of the two `(directory, exit)` lists was **empty** — 0 exit flips, matching the commit's “0 exit changes” and the sibling
delta seats (JCAL1: “4 changed + 11 new of 160, 0 exit flips, 145 unchanged tuples”).

### (a) `r89-c1-multi-cause-valid` — does the disclosure name BOTH latching causes?

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r89-c1-multi-cause-valid
```

```text
VIOLATION: entities[1].id: duplicate entities id 'r89-c1-multi-cause-valid-ambiguous-holder'
VIOLATION: entities[2].provenance[0].tick: required nonnegative integer
VIOLATION: entities[2].provenance[0].to_holder: ambiguous entity 'r89-c1-multi-cause-valid-ambiguous-holder'
VIOLATION: entities[2].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: malformed record (invalid tick); ambiguous holder identity to_holder 'r89-c1-multi-cause-valid-ambiguous-holder' at entities[2].provenance[0]
4 violation(s); no canon changed
exit=1
```

**Yes — both latching causes** (`invalid tick`, `ambiguous holder identity`), in validation order, with no other cause claimed.
Four probes fixed the boundary of the claim:

| probe | delivered output (cause clause) | reading |
|---|---|---|
| `c1-multi-three-causes` | `first stop: malformed record (invalid tick); holder reference to_holder 'ghost' absent from raw entities and absent from the resolved index; source reference 'ghostsrc' absent from raw sources and absent from the resolved index` | all three latching causes join; baseline named only the tick |
| `c1-multi-record-tail` | same two-cause clause on `provenance[1]` **and** `provenance[2]` | joined summary propagates to tail disclosures with the right origin |
| `c1-nonlatch-ambiguous-source` | `first stop: malformed record (invalid tick) at entities[2].provenance[0]` (a local `ambiguous in-world source 'srcc'` line is emitted) | a non-latching cause is NOT promoted into the summary — “all **and only** latching” holds |
| `c1-shape-plus-source` | `first stop: malformed record (unexpected field set)` (no local source finding) | the shape branch stays single-cause but remains consistent with its own local findings |

### (b) FN-2 — unresolvable vs resolved identity, and four false-qualification controls

Fixture pair on the delivered tree:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r89-fn2-unresolved-chain-break
python3 corpus/fixtures/check_bible.py corpus/fixtures/r89-fn2-control
```

```text
r89-fn2-unresolved-chain-break:
VIOLATION: entities[4].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'

r89-fn2-control:
VIOLATION: entities[3].provenance[1]: provenance chain break; expected from_holder 'f3-dup', got 'mira'
```

Controls (scratch dirs; same command shape `python3 <checker> /tmp/lore-r89-JCAL2.mk/probes/<name>`):

| control | construction | delivered cause | verdict |
|---|---|---|---|
| `fn2-resolved-unrelated-invalid` | expected holder unique; an **unrelated** schema-invalid entity row present | `provenance chain break; expected from_holder 'dup', got 'mira'` (unqualified) | no “any invalid row” false trigger |
| `fn2-observed-unresolved` | expected `'mira'` resolved; observed `'dup'` raw-duplicated, uniquely indexed | `possible provenance chain break, not a definite identity mismatch: expected from_holder 'mira'; got 'dup'; from_holder 'dup' is not uniquely resolvable …` | names only the unresolved side; no false claim about `'mira'` |
| `fn2-ambiguous-both-valid` | `'dup'` twice, both schema-valid (ambiguous index) | `first stop: ambiguous holder identity to_holder 'dup' …` — no “possible chain break” line | genuinely ambiguous identity takes the ambiguous path, not the qualified comparison |
| `r89-fn2-control` (delivered fixture) | resolved pair, no extra rows | unqualified | matched control is a real control |

The claim “FN-2 qualifies comparison findings under unresolvable holder identity, without false qualification on resolved
identities” holds on all six cases. Baseline comparison: every control was unqualified *and* correctly unqualified before, so no
control regressed.

### (c) FN-1 — is the resolved-index wording accurate in both branches?

```sh
D=/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/check_bible.py
for p in /tmp/lore-r89-JCAL2.mk/probes/fn1-*; do python3 "$D" "$p"; done
```

```text
fn1-holder-raw-present:        first stop: holder reference to_holder 'ghost' present in raw entities but absent from the resolved index
fn1-holder-absent:             first stop: holder reference to_holder 'ghost' absent from raw entities and absent from the resolved index
fn1-from-holder-raw-present:   first stop: holder reference from_holder 'ghost' present in raw entities but absent from the resolved index
fn1-holder-raw-present-twice:  first stop: holder reference to_holder 'ghost' present in raw entities but absent from the resolved index   (two raw rows, both schema-rejected)
fn1-source-raw-present:        first stop: source reference 'ghostsrc' present in raw sources but absent from the resolved index
fn1-source-absent:             first stop: source reference 'ghostsrc' absent from raw sources and absent from the resolved index
fn1-source-empty-id:           first stop: malformed record (invalid source_id)
fn1-entities-missing:          VIOLATION: entities.json: cannot load JSON: [Errno 2] … ; no holder-absence clause at all
```

Readings: both branches are worded accurately for holders **and** sources, for one and for multiple rejected raw rows; the
`malformed`/`unknown` split is real (`fn1-source-empty-id` → `malformed record (invalid source_id)`; the parent-authored
`corpus/fixtures/r89-c1-malformed-source-id` pins that branch durably, closing X1's named gap); and the “raw-present” wording
cannot be emitted against a table that never loaded, because provenance checks need an item row from that table (control
`fn1-entities-missing`). The F2 fixtures themselves are accurate but worded differently — see Finding 3.

Branch coverage on the delivered tree (my own run over the full stdout of all 160 directories):

```sh
grep -c 'present in raw' /tmp/lore-r89-JCAL2.mk/census160-full.txt        # -> 0
grep -o 'absent from raw entities and absent from the resolved index' … | wc -l   # -> 6
grep -o 'absent from raw sources and absent from the resolved index' … | wc -l    # -> 15
```

**The raw-present half of the FN-1 wording is exercised by zero delivered fixtures** (independently reproducing JCAL1's and
JCAL3's Debt 3); only the truly-absent half is pinned (21 occurrences across the corpus).

### (d) Debt reproductions — C5 (tick scope) and C6 (nullable `from_holder`)

```sh
python3 "$D" /tmp/lore-r89-JCAL2.mk/probes/c5-tick-unresolved-observed   # raw-duplicated observed holder, ticks 2 then 1
python3 "$D" /tmp/lore-r89-JCAL2.mk/probes/c5-tick-resolved-control      # same ticks, all holders unique
python3 /tmp/lore-r89-JCAL2.mk/base-check_bible.py <same dirs>           # baseline
```

```text
c5-tick-resolved-control (after == before):
VIOLATION: entities[2].provenance[1].tick: provenance tick 1 must be greater than previous tick 2
VIOLATION: entities[2].provenance[1]: provenance chain break; expected from_holder 'mira', got 'dup'

c5-tick-unresolved-observed (after):
VIOLATION: entities[2].provenance[1].tick: input-structural finding, not sourced-canon; holder identity is not uniquely resolvable: from_holder 'dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); provenance tick 1 must be greater than previous tick 2
VIOLATION: entities[2].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'mira'; got 'dup'; from_holder 'dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index)
```

```text
c6-null-from-later (after):
VIOLATION: entities[2].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'mira'; got None; from_holder None is not uniquely resolvable (0 raw entity rows carry this id, but only 0 is in the resolved index)
c6-null-from-later (baseline):
VIOLATION: entities[2].provenance[1]: provenance chain break; expected from_holder 'mira', got None
c6-null-from-later-tick (after): the tick finding is qualified the same way.
```

Extension of the same root cause, not covered by either C5 or C6 as measured (C6's scope note predicted it):

```text
fn2-first-record-unresolved (after):
VIOLATION: entities[2].provenance[0]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: from_holder 'dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); first record must have from_holder null
fn2-first-record-unresolved (baseline):
VIOLATION: entities[2].provenance[0]: provenance chain break; first record must have from_holder null
```

A record that is not the first-holder-origin form violates a **definite** structural rule; identity resolvability is irrelevant, yet
the delivered tree hedges it as “possible … not a definite identity mismatch”.

### Exit-code and count invariance

Machine receipt (`.ufo/waves/round-89/followup/JCAL2-probes.json`), from `python3 /tmp/lore-r89-JCAL2.mk/receipt.py`:
`probes=22 exit_flips=0 count_changes=0 stdout_changed=14`, delivered `e2bb9639…`, baseline `dcacffd6…`, stderr empty on every
delivered run. So all 22 probes (including both debt reproductions) preserve exits, violation counts, and stderr — the harms below
are diagnostic-wording only, and the same holds for all 160 fixture directories.

## Findings & named debt

**(a) Valid-key combined cause summary — PASS.** All simultaneously latching causes are named, in validation order, on the stop
record and on tail disclosures; a non-latching ambiguous source is not promoted; the shape-invalid branch is unchanged and stays
self-consistent (it also emits no local findings it then omits). Scope note, agreeing with JCAL1: the `'; '`-joined form already
existed for the shape-invalid branch (`r87-probe-shape-ambiguous`, `r88-shape-ambiguous-armed`), so the *new* mechanism is the
valid-key path only — the commit's phrasing (“valid-key combined cause summary”) is correctly scoped.

**(b) FN-2 qualification — PASS as claimed.** Unresolved expected/observed holder ⇒ qualified; resolved identities stay definite
under four controls, including one with an unrelated schema-invalid row and one where an actually ambiguous id takes the ambiguous
path. No false qualification on a resolved identity was found.

**(c) FN-1 resolved-index wording — PASS as to accuracy, with a coverage gap.** Both branches are factually accurate for both
field kinds and for multi-row raw tables; unavailable tables are kept separate (`source table unavailable`); the raw-present
branch is unreachable against a table that failed to load. Bounded vocabulary tension: the local field line still says
`dangling entity 'ghost'` when the same id is `present in raw entities` (index-relative meaning of “dangling”; pre-existing
wording, told in the same output). Same observation as C5.

**Finding 1 — C5 debt reproduced: tick-order findings are qualified though position-decidable. Classification: behavior defect
(over-broad predicate), bounded and disclosed.** Object of the qualifier is the tick comparison, which depends only on the record
position and the two `tick` integers, never on holder identity; the baseline was definite here. The qualification downgrades the
finding’s stated strength without improving calibration. Disclosed in the delivered work-commit message (“tick-order findings also
carry the qualification (conservative superset)”) and flagged by C5. Message-only: no exit, count, or stderr change.

**Finding 2 — C6 debt reproduced: the nullable sentinel is treated as an unresolvable identity. Classification: behavior defect
(over-broad predicate), bounded and disclosed.** `holder_identity_detail(None, …)` yields `from_holder None is not uniquely
resolvable (0 raw entity rows carry this id, but only 0 is in the resolved index)`; every clause is literally true but vacuous, and
the sentence is offered as the *reason* a **definite** first-record/chain rule violation is “possible … not a definite identity
mismatch”. Disclosed in the work-commit message (“nullable from_holder misclassification debt (C6)”). Message-only.

**Finding 3 — third site of the same root cause: the first-record rule (`fn2-first-record-unresolved`).** Not separately disclosed
in the commit; predicted by C6's scope note (“leave tick ordering and the first-record null requirement definite”) and measured
here. Same classification: behavior defect, bounded, message-only.

*Root cause for Findings 1–3 is one predicate:* `transition_holder_details` / `holder_identity_detail` drive (i) chain-continuity
qualification (correct, intended), (ii) tick-order qualification (not identity-dependent), and (iii) the first-record null rule
(definite, not identity-dependent); plus the sentinel case (`None`). A two-part narrowing — non-null ids only, and identity-dependent
comparisons only — closes all three without touching the FN-2 half.

**Finding 4 — FN-1's raw-present branch has no durable fixture. Classification: coverage gap (named debt), corroborating
JCAL1/JCAL3.** `present in raw` occurs 0 times across all 160 delivered directories; the branch is demonstrated only by scratch
probes (mine and JCAL1's). The delivered code implements it; the delivered fixtures do not pin it.

**Finding 5 — declared-expectation drift (carried; also JCAL3 Debt 1, V2, H2 F3).** `r89-f2-dangling-to/README.md:9`,
`r89-f2-dangling-from/README.md:9` and `r89-f2-invalid-source-id/README.md:9` declare the retired strings
`dangling holder …` / `unknown source '…'`, which the delivered checker no longer emits; the delivered outputs are the
`holder reference … absent from raw entities and absent from the resolved index` / `source reference … absent from raw sources …`
forms quoted above. Substance (cause class, origin `entities[3].provenance[1]`, `[1]`–`[3]` range) is right, so this is
documentation parity, not behavior — but r88 closure repaired exactly this class, and JDEP4 (F7, citing the r88 precedent) rules
that documentation-parity debt counts as harm at closure, so it is closure-blocking under that precedent.
Related and likewise owed at closure: `corpus/knowledge/holder-assessment-boundary.md` still declares the pre-r89 precedence rule
(JCAL3 Debt 2) and `corpus/fixtures/README.md` has no Round 89 section (JCAL3 Debt 5).

### Verdict recommendation

**Calibration: improved (bounded).** All three C1 claim halves are verified on the delivered tree by independent measurement — the
valid-key combined summary names all and only latching causes; FN-2 qualifies unresolvable-identity comparisons with four clean
false-qualification controls; the FN-1 wording distinguishes raw-present from truly-absent accurately for holders and sources. No
exit, violation-count, stderr, or clean/dirty change anywhere I measured (22 probes + 160 directories). The bound is Findings 1–5:
one root-cause predicate over-reach at three sites, a raw-present branch with no durable fixture, and carried documentation drift.

Rider for the L1, stated plainly: Findings 1–3 are *new* losses of definiteness relative to the baseline at those three sites — at
the null-sentinel site the delivered output also offers a vacuous reason for the hedge. They are disclosed, message-only, and do
not touch any behavior surface, so I do not rule the axis harmed; but if the fleet's “a trade anywhere is not an improvement” rule
is applied to disclosure definiteness, those three sites must be recorded as a bounded harm and repaired in r90 before closure
calls the axis cleanly improved. Recommended r90 fix: gate the qualifier on non-null ids and identity-dependent comparisons only;
keep tick ordering and the first-record null requirement definite. No other calibration trade was found.

## Handoff

- Deliverables: `.ufo/waves/round-89/followup/JCAL2.md` (this report) and `.ufo/waves/round-89/followup/JCAL2-probes.json`
  (machine receipt: per-probe before/after stdout, exits, counts, checker hashes).
- Repo writes were limited to those two files. No commit, no push. `l0-questions.md` shows `M` in the worktree from another seat
  (K1's authorized append); I did not touch it. Sibling repos were not read or written.
- Scratch: `/tmp/lore-r89-JCAL2.mk/` — `gen.py`, `gen2.py`, `probes/` (18 dirs), `probes2/` (4 dirs), `probe-runs.txt`
  (full before/after dumps), `census160.txt`, `census160-full.txt`, `census160-baseline.txt`, `receipt.py`,
  `probes-receipt.json`, `base-check_bible.py` (pinned baseline checker).
- Follow-ups for r90 (owners for the L1 to assign): (1) narrow the identity qualifier per the recommendation above and add a
  fixture for the null-sentinel and tick sites; (2) add a durable raw-present fixture (schema-rejected entity row referenced as a
  provenance holder, and the source analogue); (3) update the three F2 READMEs, `holder-assessment-boundary.md`, and add the
  Round 89 fixture-registry section (JCAL3 Debts 1/2/5).
- Note for sibling seats: `/tmp` is at 100% inodes — keep scratch file-frugal.
