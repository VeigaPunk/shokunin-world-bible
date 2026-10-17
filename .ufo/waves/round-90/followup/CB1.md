# CB1 — Doc-drift audit: `corpus/knowledge/holder-assessment-boundary.md` vs the r90 checker

Seat: r90 follow-up wave, world-bible lane. Delivered tree: `ca7f9ef` (`ff9fd2aa…`),
baseline `e97613c` (`e2bb9639…`), contract-copy `1b09f3f` (also `e2bb9639…`).
Proposal artifact: `.ufo/waves/round-90/followup/CB1-boundary-refresh.md` (proposal only —
nothing in `corpus/` was touched by this seat).

## Work performed

- **Axes:** (1) inventory completeness — every claim in the boundary doc checked against the
  delivered checker or the delivered tree; (2) freeze integrity — the delivered checker must be
  exactly X2+X3 composed on `e97613c` (r88-I1), any mismatch a blocking finding; (3) proposal
  precision — replacement text must describe *delivered* behavior, not any seat's intent.
- **Freeze-then-verify (r88-I1):** applied `patches/X2-c1-nullonly.patch` and
  `patches/X3-c1-tickonly.patch` to the `e97613c` checker in `/tmp` scratch, hashed the result.
  Composition equals the delivered checker byte-for-byte: **PASS** (no blocking finding).
- **Behavioral inventory of the doc's blocks:** extracted all fenced `=== case ===` output
  blocks from the doc and replayed each case through the delivered CLI; 14/14 cases match
  byte-for-byte (r85 probes ×5, r88/r89 durable fixtures ×6, multi-cause + FN-2 pair ×3).
  Pasted blocks are therefore NOT drifted; the drift is in prose, line anchors, and inventories.
- **Edge probes (scratch, in-memory memfd/`/__cb1_probe__`; no durable fixture):** a six-record
  item exercising (a) a null `from_holder` follow-on whose expected side is a genuinely
  unresolved non-null id, (b) an observed-side-unresolved chain break, (c) a tick inversion whose
  expected side is unresolved — run against both baseline `e2bb9639` and delivered `ff9fd2aa`.
  Receipts below. This pins the exact delivered semantics the refreshed doc must state.
- **Inventory re-measurement at `ca7f9ef`:** fixture directories (canonical five JSON names),
  B1 tuple replay, provenance inventory, measurement-helper absence, README round sections,
  and a scan of Q1's r90 debt for this doc (`Q89-029`, `Q89-050`).
- **Dependency check:** artifacts at `ca7f9ef` are committed and present; two timestamped
  tree/hash checks were run 60 s apart (see Handoff). No dependency gap.

## Before → after measurements

### Freeze-then-verify receipt

```sh
mkdir -p /tmp/cb1-r90 && git show e97613c:corpus/fixtures/check_bible.py > /tmp/cb1-r90/base.py \
 && cp /tmp/cb1-r90/base.py /tmp/cb1-r90/composed.py
cd /tmp/cb1-r90 \
 && patch -p1 --no-backup-if-mismatch -i .../patches/X2-c1-nullonly.patch composed.py \
 && patch -p1 --no-backup-if-mismatch -i .../patches/X3-c1-tickonly.patch composed.py
sha256sum /tmp/cb1-r90/base.py /tmp/cb1-r90/composed.py corpus/fixtures/check_bible.py
```

Observed:

```text
patching file composed.py
patching file composed.py
Hunk #1 succeeded at 321 (offset 2 lines).
e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556  base.py
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  composed.py
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
```

**Verdict: PASS.** Delivered checker (428 lines) = X2+X3 composed on `e97613c` (435 lines).
Scratch removed after the check.

### Census replay on the delivered tree

Command: run the delivered checker over every directory under `corpus/fixtures/` containing the
five canonical JSON names, comparing `(exit, sha256(stdout), violation count)` against B1's
160-directory receipt (`patches/B1-tuples.json`). Observed:

```text
fixture_dirs_canonical=164
b1_receipt_dirs=160
mismatches_vs_b1=0 stderr_nonempty=0
new_dirs=4 ['corpus/fixtures/r90-c1-rawpresent-from', 'corpus/fixtures/r90-c1-rawpresent-source',
            'corpus/fixtures/r90-c1-rawpresent-to', 'corpus/fixtures/r90-c1-three-causes']
```

Scope note: the doc's "165-directory two-revision census" (r89) = 160 fixture dirs + 5 live
probe dirs (`r89 CB1.md` receipt: `"total_dirs": 165, "fixture_dirs": 160, "live_dirs": 5`;
git ls-tree count at `e97613c` and `1b09f3f`: 160 fixture dirs; `corpus/live/runs/round-85/
probe-inputs` holds 5). The r90 delta (X2/C8/C1) is fixture-only: **160 → 164 dirs, 0 changed
tuples of the 160, 4 all-new dirs, 0 exit changes, 0 stderr**. The refresh must keep the two
scopes explicit or the numbers read as inconsistent.

### Pasted-block parity (14/14)

Command: parse the doc's `=== case ===` blocks, replay each through the delivered CLI, compare
body + `[rc=]`. Observed:

```text
parsed_blocks=4 cases=14
MATCH r85-control, r85-harbor-repro, r85-isolated-ambiguous, r85-masked-ambiguous,
      r85-unique-break-control, r88-mixed-stop, r88-nonholder-stop, r88-shape-ambiguous-armed,
      r89-c1-multi-cause-valid, r89-f2-dangling-from, r89-f2-dangling-to,
      r89-f2-invalid-source-id, r89-fn2-control, r89-fn2-unresolved-chain-break
drifting_cases=0
```

### Edge probes: baseline `e2bb9639` → delivered `ff9fd2aa`

One fixture (in-memory, source `src`; `f3-dup` = 2 raw entity rows / 1 resolved; records
`[0] (0,None,'harbor') [1] (2,'harbor','f3-dup') [2] (3,None,'mira') [3] (4,'f3-dup','mira')
[4] (5,'mira','f3-dup') [5] (1,'mira','harbor')` on item `relic`; both checkers exit 1, stderr
empty, same violation count 5):

```text
BEFORE [2]: … possible provenance chain break …: expected from_holder 'f3-dup' is not uniquely
            resolvable (…); got None; from_holder None is not uniquely resolvable (0 raw … 0 …)
AFTER  [2]: … possible provenance chain break …: expected from_holder 'f3-dup' is not uniquely
            resolvable (…); got None
BEFORE [5].tick: input-structural finding, not sourced-canon; holder identity is not uniquely
            resolvable: expected from_holder 'f3-dup' is not uniquely resolvable (…);
            provenance tick 1 must be greater than previous tick 5
AFTER  [5].tick: provenance tick 1 must be greater than previous tick 5
[3] unchanged both sides: expected from_holder 'mira'; got 'f3-dup'; from_holder 'f3-dup' is not
            uniquely resolvable (…)
```

Two semantics the refreshed doc must state exactly:

- The vacuous `None` clause is gone (null contributes no identity clause, `:168-170`), but a
  null-observed chain break **stays qualified when the expected side is a genuinely unresolved
  non-null id** — the delivered composition follows X2's narrower bound, not E1's fuller
  "definite even if the preceding id is unresolved" panel wording. This is a
  wording-panel-vs-delivered divergence worth a judging-wave ruling (not doc-only).
- The tick line never carries a holder-identity note (integer-only, `:324-326`); only an
  independently ambiguous **source** adds the prefix.

### Delivered-tree inventory re-measured

```text
provenance_dirs=33  duplicated_holder_records=13  dup_dirs=10 (identical ten to the doc's list)
measure_helper_exists=False
corpus/fixtures/*.py = check_bible.py only
README: '## Round 89: cause branches + support completion' present at :1012 (added by the r89
closure commit e97613c; the doc's "no Round 89 section at 1b09f3f" was true only for 1b09f3f);
no '## Round 90' section at ca7f9ef.
```

## Findings & named debt

**Drift inventory** (doc line numbers as delivered at `ca7f9ef`; full replacement text in
`CB1-boundary-refresh.md`):

| # | Doc location | Drift | Class |
|---|---|---|---|
| D1 | `:188` decision-table row 3 | Claims every finding involving an unresolved id is qualified, incl. `{record_label}.tick: … holder identity is not uniquely resolvable: {details}; …` (`:327-333`, `:334-344`, `:345-350`). Delivered tick branch emits no identity note; qualification covers chain-continuity and first-record forms only. | behavioral |
| D2 | `:266-276` limits bullet "Comparison findings can be non-definite" | Tick clause false; "both sides tested, either can trigger it" now chain-only; missing the delivered rules: null side contributes nothing; tick = integer-only with source-prefix only; first-record guard qualified when that id is unresolved. | behavioral |
| D3 | `:23-28` revision history | Lists three revisions, ending at r89/`1b09f3f`. r90 adds the fourth: X2 null-guard + X3 integer-only tick (C9 ruling), integrated `ca7f9ef`, checker `ff9fd2aa`. | provenance |
| D4 | `:2-6`, `:8-10`, `:35-44` banner/verified-at | All pinned to `1b09f3f`/`e2bb9639`; delivered is `ca7f9ef`/`ff9fd2aa`. Header claims a "delivered tree" refresh that no longer matches. | provenance |
| D5 | `:46-60` recheck | Its triggers fired (provenance branch and comparison wording changed); trigger list does not yet name the tick comparison or the null guard. | process |
| D6 | `:148`, `:153-154` cause section heading + `{raw_presence}` refs | "delivered `1b09f3f`"; `:272`, `:285`, `:306` → `:274`, `:287`, `:308`. | anchors |
| D7 | cause-table Code column (`:158-171`) and `:173-180` join refs | Behavior unchanged, refs shift +2 up to the tick edit (`:198-203→:200-205`, `:206-208→:208-210`, `:212-214→:214-216`, `:215-221→:217-223`, `:222-248→:224-250`, `:249-312→:251-314`, `:256→:258`, `:313-316→:315-318`, `:313-319→:315-321`). | anchors |
| D8 | `:187`, `:191-195`, `:234-241`, `:277-280`, `:300-312` | Mixed stale refs; see remap table in the proposal. `:320`→`:322`; `:322-326` (tick/identity) superseded by `:324-326`/`:327-329`; `:327-333`→`:330-335`; `:334-344`→`:339-341`; `:345-350` **deleted behavior**; definite forms `:333/:343-344/:349-350`→`:326/:337/:343`; emission `:220/:247/:317-318`→`:222/:249/:319-320`; CLI `:425-435`→`:418-428`. | anchors |
| D9 | `:508-520` evidence block | Whole delivered-ref list at `1b09f3f`; needs `ca7f9ef`/`ff9fd2aa` + remap. Unchanged landmarks: `:38-39`, `:72-76`, `:82-97` (pre-shift), loop now `:187-345`, `holder_identity_detail` `:168-175`, relation-endpoint precedent `:184`. | anchors |
| D10 | `:543-553` provenance inventory | Re-measured: 29 → 33 dirs carry provenance; 13 duplicated-holder records across the same ten dirs (unchanged). The four new r90 fixtures carry provenance but no duplicated holder refs. | inventory |
| D11 | `:460-478` "remaining branches" paragraph | Says the two `present in raw … but absent from the resolved index` wordings and the three-cause record have "no durable fixture yet" — three new durable fixtures now exist (`r90-c1-rawpresent-to/-from/-source`, `r90-c1-three-causes`), replayed above. FN-2 sub-branch list also needs restating (below). | inventory |
| D12 | `:565-574` README paragraph | "no `## Round 89` section at `1b09f3f`" is stale at delivery: README has `## Round 89: cause branches + support completion` at `:1012` (r89 closure `e97613c`) pointing at this doc; no `## Round 90` section exists, so the r90 change is currently stated nowhere in `corpus/`. | inventory |
| D13 | `:578-620` status split | OBSERVED lists predate r90; census wording needs the scope split (165 = 160+5 r89; 164 fixture-only at r90); r90 receipts to add (14/14 block parity, 0-delta census, new fixture outputs, edge probes). | inventory |
| D14 | `:622-630` measured-results slot | Revision label stale; "helper absent" still true at `ca7f9ef` (verified); no five-gate score exists. | provenance |

**FN-2 sub-branch status after r90** (for the refresh, replacing the doc's scratch-only list):
expected-side chain — durable (`r89-fn2-unresolved-chain-break`, replayed); observed-side and
first-record — still scratch-only; **tick-under-unresolved-holder — the branch no longer exists**
(C9 ruling; texture removed at `:324-326`); null-chain-definite and the mixed
null-observed/unresolved-expected case — pinned only by wave receipts (B3/C9 probes; CB1's probe
above). Any future fixture seat should pin observed-side + first-record and the null-chain
definite shape.

**No blocking findings.** Freeze hash matches; the delivered tree's contract-relevant behavior is
exactly the composition C9 ruled, and every pasted block in the doc still reproduces.

**Adjacent debt (outside this seat's file scope, reported for the integrator):**

- `corpus/fixtures/r87-probe-source-prefix/README.md:1` cites `:350`/`:333`/`:344` — r89 checker
  lines; at `ff9fd2aa` the same diagnostics live at `:343`/`:326`/`:337` (tick `:325-326`, chain
  `:337`, first-record `:343`). Already tracked as Q89-032.
- Q1's `Q89-029` ("did not replay every pasted receipt or re-anchor every code reference") is now
  resolved in both directions: 14/14 receipts replay; the re-anchoring is exactly what the
  refresh proposal carries.
- Q1's `Q89-050` residue ("historical shape-valid bound and fixture-family list not explicitly
  retired", evidence cites this doc) grows by D1–D14 until the refresh lands.
- E1's wording panel vs delivered composition (mixed null/unresolved-expected chain) — a decision
  for the judging wave: either the doc describes delivered behavior (as proposed) or an r91
  calibration move adopts E1's definite template.

## Handoff

- **Deliverables:**
  `.ufo/waves/round-90/followup/CB1.md` (this audit) and
  `.ufo/waves/round-90/followup/CB1-boundary-refresh.md` (proposal only — ready-to-paste
  replacement text for D1–D14 plus the anchor-remap table; *not applied*, per seat scope).
- **What the closure integrator should do:** apply the refresh to
  `corpus/knowledge/holder-assessment-boundary.md` with the r90 re-verification stamps
  (`ca7f9ef`, `ff9fd2aa`, census receipt above); add a `## Round 90` section to
  `corpus/fixtures/README.md` (the r89 closure added the Round 89 section the same way); re-anchor
  `r87-probe-source-prefix/README.md` (Q89-032). No other tracked file is implied.
- **Freeze state:** delivered checker `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`
  (428 lines) = X2+X3 composed on `e97613c` (`e2bb9639…`, 435 lines). No mismatch.
- **Dependency receipts (two checks, 60 s apart, delivered tree):**

  ```text
  check=1 2026-10-17T06:59:02-03:00
  ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
  HEAD = ca7f9ef; worktree shows only untracked follow-up artifacts (sibling seats H2/H3/H4, Q1…)
  check=2 2026-10-17T07:00:02-03:00
  ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
  HEAD = ca7f9ef; Q1-r90-debt.json modified by the Q1 seat; CB1* files present
  dependency_checks_done
  ```

  The checker hash was stable across both checks. The worktree is *not* clean at the file level
  because sibling follow-up seats are writing their own `followup/<SEAT>*` artifacts
  concurrently; this seat wrote only `.ufo/waves/round-90/followup/CB1.md` and
  `.ufo/waves/round-90/followup/CB1-boundary-refresh.md`. No tracked corpus file changed after
  `ca7f9ef`.
- **Scratch:** `/tmp/cb1-r90` and the two probe output files were removed; `/tmp` inode pressure
  noted (248 free inodes at start, 100% in use) — probes used memfd where possible.
- **No commit, no push; no sibling-repo access.**
