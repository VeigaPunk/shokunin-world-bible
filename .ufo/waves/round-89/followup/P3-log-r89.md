# P3 — LOG r89 entry proposal

Seat P3 (round-89 follow-up wave, world-bible lane). Judged tree: `lore-shokunin`
at `1b09f3ff8016b26a2259e086f673d0112f4f54e5` (`1b09f3f`), baseline
`51b286b5a1e503e6e6ace1f8da0bd606a3c10d94` (`51b286b`). Tree clean at judgement
start and end (`git status --porcelain` → only `?? .ufo/waves/round-89/followup/`,
the judging wave's own untracked directory).

Every number below is either my own replay on the delivered tree (marked "P3
replay") or is attributed in-line to the follow-up seat that produced it. Scratch
lives under `/tmp/P3-*` and `/tmp/P3-probes/` and is not a deliverable.

Deliverable: an append-ready `LOG.md` round-89 entry (under **Handoff** below),
plus the motivating evidence, measurements, and honest debt that entry must carry.
This is a proposal for the integrating owner; it is not appended here.

## Work performed

- Confirmed the tree under judgement: `git log --oneline -3` → HEAD `1b09f3f` on
  top of `51b286b`; `git status --porcelain` clean except the follow-up dir. Work
  commit `git show --stat HEAD` → 136 files, +12330/−15.
- **Own census of the delivered tree.** Loop over every direct fixture directory
  running `python3 corpus/fixtures/check_bible.py corpus/fixtures/<dir>` from the
  repo root — the *same relative-path invocation* the baseline census used (the
  r88 method trap: absolute paths make the path-embedding "missing-file" fixtures
  report false deltas). Recorded exit, violation-line count, and stderr per dir.
- **Own baseline-vs-delivered delta.** Extracted `51b286b:corpus/fixtures/check_bible.py`
  (SHA-256 `dcacffd6…`, 395 lines) to `/tmp/P3-base/`, then ran both checkers over
  all 149 baseline dirs and diffed `(returncode, stdout)` per dir.
- **C1 fixture replays** (all 10 C1 dirs) and the C3 R9 demo, from the lane root.
- **C2 anchor verification:** `grep -cF` for each of the 14 anchors in
  `patches/S2-fact-map.json` against its delivered excerpt; recomputed the r87
  cluster's D1 fact composition from `entities/relations/timeline/sources.json`.
- **Two 60 s wait-checks** on `followup/` (log `/tmp/P3-polls.txt`), per the seat
  block. Both found the directory empty (04:17:38, 04:18:38 `-03:00`). The judging
  artifacts landed at 04:18–04:20, i.e. within ~30 s of my second check; I read
  them after the fact and attribute their receipts in-line. Nothing in my verdicts
  depends on an absent seat.
- **Two scratch probes** (`/tmp/P3-probes/`) reproducing the two named C1
  semantics debts on the delivered checker: nullable-`from_holder`
  misclassification and the tick-order qualification superset.

## Before → after measurements

### Census and delta (P3 replay)

```sh
for d in corpus/fixtures/*/; do python3 corpus/fixtures/check_bible.py "$d"; done
```

```text
TOTAL=160 zero=32 one=128 other=0 stderr_cases=0
TOTAL_VIOLATION_LINES=399
```

Baseline for the same harness over the 149 baseline dirs: `0=31 / 1=118`, 367
violation lines, 0 stderr (matches `patches/B1-tuples.json` and `H2-delta.json`).

Delta, delivered checker vs baseline checker over the 149 shared dirs:

```text
=== corpus/fixtures/r87-probe-multi-invalid (baseline_rc=1 delivered_rc=1)
=== corpus/fixtures/r87-probe-record-and-chain (baseline_rc=1 delivered_rc=1)
=== corpus/fixtures/r88-mixed-stop (baseline_rc=1 delivered_rc=1)
=== corpus/fixtures/r88-nonholder-stop (baseline_rc=1 delivered_rc=1)
=== CHANGED DIRS ===
4
```

New dirs (`comm -13` of the two `git ls-tree -d` listings): **11** — 5
`r89-c1-*` (`invalid-tick`, `invalid-from-holder`, `invalid-to-holder`,
`malformed-source-id`, `multi-cause-valid`), 3 `r89-f2-*` (`dangling-to`,
`dangling-from`, `invalid-source-id`), 2 `r89-fn2-*` (`unresolved-chain-break`,
`control`), and `r89-inspiration-paraphrase`. So the claim "**4 changed + 11 new
of 160 dirs, 0 exit changes**" reproduces exactly. The arithmetic closes:
4+3+3+3+4+4+4+4+2+1+0 = 32 added violation lines; 367 + 32 = 399; clean dirs
31 + 1 (`r89-inspiration-paraphrase`) = 32.

Checker: delivered `corpus/fixtures/check_bible.py` SHA-256
`e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556`, 435 lines;
`git diff --numstat 51b286b 1b09f3f -- corpus/fixtures/check_bible.py` → `54 14`.
`V2` confirms the stronger freeze property: **the delivered file is X1's patch
applied to `51b286b`, byte-for-byte — no integrator amendment this round** (the
r88 process gap is not repeated). `H2` independently reproduces the delta and adds
the stronger property that **no shared path changed its violation count**, and the
4 changed paths are pure FN-1 disclosure-wording substitutions (no added/removed
findings).

### C1 fixture behaviour (P3 replay, lane root)

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/<case>   # each exit 1, empty stderr
```

```text
r89-c1-invalid-tick            4 findings; first stop malformed record (invalid tick) at entities[3].provenance[1]
r89-c1-invalid-from-holder     3; first stop malformed record (invalid from_holder)
r89-c1-invalid-to-holder       3; first stop malformed record (invalid to_holder)
r89-c1-malformed-source-id     3; first stop malformed record (invalid source_id) at entities[2].provenance[1]
r89-c1-multi-cause-valid       4; first stop: malformed record (invalid tick); ambiguous holder identity to_holder '…' at entities[2].provenance[0]
r89-f2-dangling-to             4; first stop holder reference to_holder 'r89-f2-missing-to' absent from raw entities and absent from the resolved index
r89-f2-dangling-from           4; same for from_holder
r89-f2-invalid-source-id       4; first stop source reference 'r89-f2-unknown-source' absent from raw sources and absent from the resolved index
r89-fn2-unresolved-chain-break 2; qualified — possible provenance chain break, not a definite identity mismatch (2 raw entity rows, 1 indexed)
r89-fn2-control                1; unqualified — provenance chain break; expected from_holder 'f3-dup', got 'mira'
r89-inspiration-paraphrase     CLEAN, exit 0
```

The combined-cause summary names **both** simultaneous latching causes on a
valid-key record, matching `E1`'s proposed form; each of the six named
first-cause branches names that cause first; FN-1 distinguishes raw absence from
index absence; FN-2 qualifies without suppressing, and its control stays
unqualified. This is the wave's "8 cause-branch fixtures (5 `r89-c1-*` + 3
`r89-f2-*`) + FN-2 pair + paraphrase demo" set, which `V2` replayed
independently.

### C2 anchors and support (P3 replay)

```sh
cd corpus/fixtures/r87-myth-cluster
while IFS='|' read -r f a; do echo "$(grep -cF "$a" "$f")  $f  :: $a"; done <<'EOF'
… 14 rows from patches/S2-fact-map.json …
EOF
```

All 14 rows → `1`. The delivered shell-charter excerpt carries the
pledge-framed R3 phrase (`Watch clause: Under this charter's pledge, Shellweavers
keep watch with the Reed Bell.`), which matches the current S2 map anchor — the
R3 mismatch C7 measured against M3/M4 is reconciled on the delivered tree.

Fact composition (recomputed from the cluster JSON): 7 `first_appearance`
pointers + 7 entity claims + 4 relation edges + 4 timeline events = **22**. The
baseline-supported 8 = 7 resolvable pointers + the `lowwater-hymn` claim; the 14
newly supported facts are exactly the 6 remaining entity claims + 4 relations + 4
events, each with a delivered anchor. `JCOV1` independently replayed the whole
cluster under the D1 rule → **8 → 22 supported, 14/14 anchors, 7/7 pointers**;
`JDEP4` → **32/32 source-attributed facts across two clusters** (r87 22 + r88 10).

**Receipt caveat (JCOV1-D1).** The probe command stored in
`patches/M4-verify.json` (`before.d1_support.command`) prints
`facts=22 OK=8 not-OK=14` on the delivered tree — I reproduced exactly that. It
counts claim support as literal `statement in prose[source]`, which no delivered
excerpt contains, so it cannot print 22. `M4-verify.json`'s `after.facts_supported:
22` is a hand-composed `8 + 14`. The number is true; the receipt for it is not one
reproducible command. The round record should cite the composition or a per-fact
anchor map, not that `after` block alone.

### C3 rows and demo (P3 replay / diff)

- `corpus/knowledge/r88-sourced-inspiration-decision-table.md` gains R8
  (rights-blocked element disposition), R9 (excerpt delivery-mode), R10
  (cross-cluster contradiction register) as **three rows × 6 columns**, plus an
  Integration-boundary section and r89 integration notes that scope R8–R10 as
  **prospective** (R9 applies to clusters landed from r89 onward; r87/r88 annotate
  at their next content touch; R10's register is created on first real conflict).
  `V2` confirms the append preserves the six-column shape and header with no
  existing row modified.
- `corpus/knowledge/r89-cross-cluster-contradiction.md` — the R10 worked example
  (32 lines), honest that the second cluster is hypothetical and absent, and that
  the live register destination `corpus/knowledge/cross-cluster-contradictions.md`
  does not exist yet.
- `corpus/fixtures/r89-inspiration-paraphrase/` — the durable R9 **negative** demo:
  delivery mode declared in both the excerpt (`**Delivery mode:** paraphrase`) and
  the map entry, the anchor hits (`moved to the west stair` → 1), and the mapped
  claim **fails** R9 support because the underlying text is `not delivered /
  unverified`. `JDEP4` credits it as the reason the support rule returns a negative
  verdict, not just a positive one.
- `corpus/knowledge/reference-ledger.md` — the ETCSL row now carries
  `external-only / text not delivered at lore; citation is a research lead with
  verified line locators, not delivered support.` (1-line change).

### Named-debt probes on the delivered checker (P3, `/tmp/P3-probes/`)

Both debts the commit message records as bounds reproduce:

```sh
python3 corpus/fixtures/check_bible.py /tmp/P3-probes/null-from-holder
# 1 finding: "…possible provenance chain break, not a definite identity mismatch:
#   expected from_holder 'keeper'; got None; from_holder None is not uniquely
#   resolvable (0 raw entity rows carry this id, but only 0 is in the resolved index)"
```

A schema-valid `from_holder: null` on a later record is a **definite** chain break
(`None` ≠ previous holder), yet it is qualified as an uncertain identity mismatch:
`holder_identity_detail(None, …)` returns a detail for the 0-raw/0-indexed case
(`check_bible.py:168-173`). Restricting the predicate to non-null IDs is the
correction C6 filed.

```sh
python3 corpus/fixtures/check_bible.py /tmp/P3-probes/tick-null-transition
# 2 findings; the tick inversion reads:
# "…tick: input-structural finding, not sourced-canon; holder identity is not
#  uniquely resolvable: from_holder None is not uniquely resolvable (0 raw … 0 …);
#  provenance tick 5 must be greater than previous tick 10"
```

A definite tick-order violation carries an identity note that has nothing to do
with tick ordering — the "conservative superset" bound. Holder resolution is not a
cause of `tick <= previous_tick`.

## Findings & named debt

### Per-axis verdicts on the delivered tree

| axis | proposed verdict | receipt | bound |
|---|---|---|---|
| calibration | **improved (bounded)** | P3 census: 160 dirs, `0=32/1=128`, 399 lines, 0 stderr; delta exactly 4 changed + 11 new, 0 exit changes; 10 C1 fixtures replay with the claimed causes/summary. `V2`: delivered checker == X1's patch byte-for-byte, no amendment; all 8 cause-branch fixtures + FN-2 pair replay with claimed exits. `H2`: 4 changed paths are pure FN-1 disclosure text, 0 violation-count changes on shared paths. | Three semantics/documentation bounds: (1) the tick-order qualification superset; (2) nullable-`from_holder` over-qualification; (3) three F2 READMEs quote pre-FN-1 cause strings (`V2` 8/11 READMEs match). The last is an expectation-layer trade, so calibration is not a clean improvement. |
| coverage | **improved (bounded)** | P3: 14/14 anchors `grep -cF` → 1; 8 → 22 D1 facts; ETCSL `external-only / text not delivered` marker present; r87 cluster `CLEAN` exit 0. `JCOV1`: 0/14 → 14/14 anchors, 1/7 → 7/7 pointers, 8 → 22 supported, 0 exit changes over 149 dirs → "improved (bounded)". `JCOV3` (R9/R10 demo sub-scope) and `JCOV4` also rule **improved (bounded)**; `JDEP4` 32/32. | `JCOV1`-D1 (22/22 receipt not one reproducible command); D2 (`r87-myth-cluster/README.md` not updated at its r89 content touch); D3 (decision-table row-5 evidence cell stale); D4 (no R9 delivery-mode declaration on the r87/r88 excerpts — the deferral must be re-stated in the r89 ledger or discharged); one delivered page-level locator set, `CLEAN` is structural not prose support. |
| depth | **improved (bounded) on the artifact surface; a documentation harm is recorded, not netted** | P3: R8/R9/R10 integrated with owners + prospective scoping; R9 negative demo present and mode-declared in excerpt and map; R10 worked example present; ledger marker present. `JDEP4`: depth **improved (bounded)**, and recommends a second capabilities row `in-world excerpt support verification`. `JCOV3`: R9/R10 demo sub-scope improved (bounded). | `H5`/`H2`: the **expectation layer did not keep up**. `corpus/knowledge/holder-assessment-boundary.md` — the doc `corpus/fixtures/README.md` names as "the current contract" — is stale on every surface the r89 wording touched (cause-table rows 9/10/13, the precedence paragraph falsified by `r89-c1-multi-cause-valid`, the "names only the FIRST check" row, a replay block that no longer reproduces, code lines stale by +14…+18). `corpus/fixtures/README.md` has no Round 89 section; `r87-probe-source-prefix/README.md` cites three stale code lines. `H2` states explicitly that this trade must be counted against the move, not netted out. |

No axis is `unchanged` on my reading (`JDEP4`'s "calibration unchanged" refers to
*self-assessment artifacts* in the work commit, not the checker). No
`unprovable-but-better`. **No L1 verdict artifact existed at draft time**, and
`followup/` held only the seats listed in Handoff — so admission is L1's call and
the round record must not present the boundary-doc drift as closed.

### Named debt (all carried into the proposed entry)

1. **Tick-order qualification superset** (P3 probe, `C6`, commit bound): a definite
   `tick <= previous_tick` finding carries `input-structural finding, not
   sourced-canon` plus a holder-identity note whenever a transition holder is
   unresolved — including when that holder is a schema-valid `None`. Holder
   resolution is not a cause of tick ordering.
2. **Nullable `from_holder` over-qualification** (P3 probe, `C6` finding B): a
   definite chain break where the observed `from_holder` is `None` is qualified as
   a *possible* identity mismatch, with the misleading detail `0 raw entity rows
   … 0 is in the resolved index`. Restrict the predicate to non-null IDs and to
   identity-dependent continuity.
3. **Poll protocol gaps — the 25-minute deadline was still missed.** `W1`'s
   cutoff at 03:52:53 found **21 of 31** non-clerk seats with artifacts; ten seats
   landed their reports **2–19 minutes after** the deadline (`C5` 03:58, `C6` 04:02,
   `C7` 04:11, `C8` 03:59, `D3` 03:55, `K1` 04:01, `M2` 04:01, `M4` 03:59, `R1`
   03:58, `T1` 04:03) — including the largest report and the round's decisive
   discipline critic (`C7`, 25 KB). `X1`'s patch arrived at 03:52:46, seconds
   before several seats' cutoffs (`M2` deadline 03:52:34, `M4` final Glob 03:52:48,
   `C7` final snapshot 03:52:49, `W1` 03:52:53), so their "X1 absent" observations
   raced the arrival and are not facts. Two first-pollers hit the 600 s shell-task
   timeout and left gaps (`M2` 03:37:34–03:40:55; `X1` after 03:37:30, resumed
   03:40:24). The "proceed at deadline with what exists" rule would have discarded
   roughly a third of the wave; wait-checks are advisory, not a gate.
4. **M2's stale-map late replay.** `M2`'s combined M1+M2 scratch replay reports
   22/22, but against the current S2 anchor map it matches only **3/14**
   (`C7.md:365`: ids `E3`, `T1`, `T2`), because it ran against an earlier map
   snapshot. `M4-verify.json`'s R3 anchor is likewise pre-pledge (the delivered
   excerpt happens to satisfy both strings). Neither 22/22 claim can be adopted as
   current-map verification; the delivered-tree 14/14 is the P3/`JCOV1` result.
5. **r87/r88 R9-annotation debt.** Neither the four new r87 excerpts nor
   `r88-m3-maya-cluster/source-excerpt.md` declares an R9 delivery mode
   (`grep -rn "Delivery mode"` finds only the r89 demo). The table's integration
   note defers r87/r88 to "their next content touch"; r89 *is* such a touch, so the
   deferral must be re-stated in the r89 closure record or discharged (`JCOV1`-D4,
   `H5` item 5).
6. **Expectation/documentation parity** (`V2`, `H5`, `JCOV1`-D2/D3): three F2
   READMEs quote pre-FN-1 cause strings; `r87-myth-cluster/README.md` lists neither
   the four new excerpts nor the `keeps_watch_with` edge; the decision table's row-5
   evidence cell is stale; `corpus/fixtures/README.md` has no Round 89 section;
   `r87-probe-source-prefix/README.md` cites three stale code lines; the two FN-2
   READMEs still say "integration verification pending".
7. **FN-1 raw-present branch has no durable fixture** (`H5` item 6): the
   `present in raw … but absent from the resolved index` wording is scratch-verified
   only (`C6`'s raw-present probe). `r89-c1-malformed-source-id` closes `X1`'s
   malformed-`source_id` gap, not this one.
8. **Unlanded alternatives** (patches only, absent from the tree): `X2-c1-summary-only.patch`,
   `X3-c1-qualify-only.patch`, `M1-excerpts.patch`, `M2-excerpts.patch`,
   `M3-excerpts.patch` (M3 was the selected basis, delivered via M4's synthesis),
   `D1-rows.md`, `S3-r8-r10-sketches.md`, `W2-*` proposals. `T1`/`R1`/`D1` work-wave
   drafts were not integrated as artifacts; their material is reflected in the
   delivered rows.
9. **Spence row placement** (`JDEP4`): the r88 Spence ledger row sits at line 13,
   after the table's closing paragraph, so it renders outside the table; the ETCSL
   row is correctly in-table. Repair before admission.
10. **Process / hygiene.** `V2` reports **no integrator amendment** this round —
    a real improvement over r88's unlogged amendment. `corpus/fixtures/__pycache__/`
    was observed untracked by `SE1` and is absent from the delivered commit;
    `.gitignore` still does not name it (only `.ufo/interactive-sessions/`). The
    `capabilities` table is still empty in the delivered `SCORECARD.md` (r88's
    "provenance stop-cause assessment" row is not in the file on disk), so
    `JDEP4`'s proposed second row cannot be entered until that is repaired — the
    honest alternative is to defer it one round. No saturation, no retirement, no
    `[x]`; `SHONEN.md` byte-unchanged (`git diff --stat 51b286b 1b09f3f -- SHONEN.md`
    → empty).

### Follow-up wave status at draft time

`followup/` was empty at both of my 60 s checks (04:17:38, 04:18:38). By 04:20 it
held `V2`, `H2`, `H5`, `JCOV1`, `JCOV3`, `JCOV4`, `JDEP4` (+ `H1-census.json`,
`H2-delta.json`, `JCOV1-probes.json`, `JCOV3-probes.json`, `JDEP2-probes.json`).
**No `P1`, `P2`, `K1`, `SE2`, `JDEP1/2/3/5`, or L1 verdict artifact** exists yet, so
no province verdict and no scorecard re-cut for r89 exist at draft time. The round
report at `/home/vgpnk/Projects/shokunin/.ufo/reports/round-89/` does not exist
(P1's authorized write, not mine).

## Handoff

### Proposed `LOG.md` append (append-ready text; not for direct append before L1 adjudication)

> ## Round 89 — 2026-10-17 (cause-branch fixtures + combined-cause summary + FN-1/2; r87 support completion; R8–R10 governance; luna-max work wave; work commit `1b09f3f`)
>
> - Baseline before this round is `51b286b5a1e503e6e6ace1f8da0bd606a3c10d94`
>   (r88 closure; lane tree clean). The round ran as a world-bible work wave
>   recorded under `.ufo/waves/round-89/` — 32 seat reports plus prefixed patch
>   artifacts, landed as `1b09f3f` (136 files, +12330/−15) — followed by a
>   judging/integration wave under `.ufo/waves/round-89/followup/`. No push and no
>   merge this round.
>
> - **Motivating evidence — C1 (calibration).** r88 admitted (bounded) three gaps:
>   six first-cause branches had no durable fixture; the combined same-record
>   summary existed only on the shape-invalid branch, so a valid-key multi-defect
>   record named only the first defect in field order; and FN-1/FN-2 input shapes
>   were corpus-uncovered. Measured at `51b286b`: the valid-key multi-cause case
>   disclosed only the invalid tick, and a chain break against a non-uniquely
>   resolvable holder was reported as a definite mismatch.
>
> - **C1 landed — `1b09f3f`.** `corpus/fixtures/check_bible.py` (+54/−14; 395 →
>   435 lines; SHA-256 `e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556`):
>   valid-key records retain and join **every** latching first-stop cause with
>   `'; '`; raw entity/source ID counts are tracked alongside the resolved indexes
>   and a distinct `present in raw … but absent from the resolved index` wording is
>   emitted (FN-1); a chain-break comparison whose expected holder is not uniquely
>   resolvable is qualified as an input-structural *possible* break rather than a
>   definite mismatch (FN-2). Eight cause-branch fixtures (5 `r89-c1-*` + 3
>   `r89-f2-*`), the FN-2 pair, and the R9 demo land with it — 11 new fixture dirs.
>   Counting from the lane root: `r89-c1-multi-cause-valid` → 4 findings, exit 1,
>   first stop `malformed record (invalid tick); ambiguous holder identity
>   to_holder '…' at entities[2].provenance[0]`; `r89-fn2-control` → 1 finding,
>   unqualified. Closure census: **160 fixture dirs** (was 149), exits `0=32 / 1=128`,
>   **399 violation lines** (baseline-149 subset 367), 0 stderr cases; deltas
>   enumerable — **4 changed tuples + 11 new, 0 exit changes, 0 violation-count
>   changes on shared paths**; the 4 changed paths are pure FN-1 disclosure-wording
>   substitutions.
>   Corroboration: `V2` (**delivered checker == X1's patch applied to `51b286b`,
>   byte-for-byte — no integrator amendment this round**; all 11 new dirs replay
>   with the claimed exits; 8/11 READMEs match line-by-line), `H2` (independent
>   census and per-path diff), `C6` (per-amendment isolation: A changes 1 path, B 0,
>   C 3), `F1`/`F2`/`F3`.
>   Bounds: (a) **tick-order qualification superset** — a definite
>   `tick <= previous_tick` finding carries the qualifier plus a holder-identity
>   note whenever a transition holder is unresolved, though holder resolution is not
>   a cause of tick ordering; (b) **nullable-`from_holder` misclassification** — a
>   schema-valid `None` observed holder is treated as a 0-raw/0-indexed unresolved
>   identity, so a definite chain break is labelled possible; both reproduced on the
>   delivered tree by probe; (c) three F2 READMEs still quote the pre-FN-1 cause
>   strings (`V2`).
>
> - **C2 landed — `1b09f3f` (coverage).** Four delivered in-world excerpts —
>   `gate-witness`, `dune-register`, `shell-charter`, `tide-bell-tally` — make the
>   r87 cluster **14/14 anchored** under the D1 rule (`grep -nF` anchor + whole-claim
>   review), i.e. **8 → 22 of 22** source-attributed facts supported (7 pointers +
>   7 entity claims + 4 relation edges + 4 timeline events; the R3 anchor is the
>   pledge-framed delivered phrase, so the pledge-vs-performance boundary holds). The
>   ETCSL ledger row gains `external-only / text not delivered at lore`. Counting:
>   r87 cluster `CLEAN: schema, citations, relations, timeline; 0 violations`, exit 0;
>   census 149 → 160 dirs. Corroboration: `JCOV1` (**coverage improved (bounded)**:
>   0/14 → 14/14 anchors, 1/7 → 7/7 pointers, 8 → 22 supported, 0 exit changes over
>   the 149 baseline dirs), `JCOV3`/`JCOV4` (**improved (bounded)**), `JDEP4` (32/32
>   across two clusters), `C7`/`S2`/`M4`.
>   Bounds: `M4-verify.json`'s `after.facts_supported: 22` is a hand-composed `8 + 14`
>   — its own stored probe command prints `OK=8` and must not be cited as the receipt
>   (`JCOV1`-D1); `r87-myth-cluster/README.md` is unchanged and lists none of the four
>   new excerpts (`JCOV1`-D2, `JCOV4`); the decision-table row-5 evidence cell is stale
>   (`JCOV1`-D3); `M2`'s combined M1+M2 replay claimed 22/22 but matches only 3/14 of
>   the current S2 anchors (`C7`), and `M4`'s verify JSON carries a pre-pledge R3
>   anchor.
>
> - **C3 landed — `1b09f3f` (depth).**
>   `corpus/knowledge/r88-sourced-inspiration-decision-table.md` gains **R8**
>   (rights-blocked element disposition: materiality screen + disposition, no rights
>   finding), **R9** (excerpt delivery-mode — verbatim/translation/paraphrase/summary,
>   declared in both excerpt and claim map; a paraphrase is not the source's own text
>   and cannot carry source-text support), and **R10** (cross-cluster contradiction
>   register procedure with claim pointers and `unresolved` status), each with an
>   owner and **prospective** scoping. `corpus/knowledge/r89-cross-cluster-contradiction.md`
>   is the R10 worked example (second cluster explicitly hypothetical);
>   `corpus/fixtures/r89-inspiration-paraphrase/` is the durable R9 **negative** demo
>   (mode declared in excerpt and map; the anchor hits; support is withheld). `V2`
>   confirms the append preserves the six-column row shape with no existing row
>   modified. Corroboration: `JDEP4` (**depth improved (bounded)**; recommends a second
>   capabilities row `in-world excerpt support verification`), `JCOV3` (R9/R10 demo
>   sub-scope improved (bounded)), `D2`/`D3`/`T1`/`R1`.
>   Bounds: R8–R10 are governance rows, not checker or schema changes; R10's register
>   file does not exist yet; the Spence ledger row sits after the table's closing
>   paragraph (`JDEP4` F7).
>
> - **Documentation harm recorded, not netted.** `H5` and `H2` measured that the
>   expectation layer around the delivered checker did not keep up. The
>   `corpus/knowledge/holder-assessment-boundary.md` — the doc `corpus/fixtures/README.md`
>   names as "the current contract" — is stale on every surface the r89 wording
>   touched: its cause-table rows 9/10/13, the precedence paragraph whose "only the
>   shape-invalid branch combines two cause phrases" claim is falsified by
>   `r89-c1-multi-cause-valid`, the "names only the FIRST check in precedence order"
>   decision row, a replay block that no longer reproduces, and code lines stale by
>   +14…+18. This is the same condition r88 recorded as `depth: harmed (bounded)` and
>   repaired inside that round. `corpus/fixtures/README.md` has no Round 89 section;
>   `r87-probe-source-prefix/README.md` cites three stale code lines. `H2` states the
>   documentation-parity cost must be counted against the move, not netted out; `H5`
>   puts the ruling to L1.
>
> - **Per-axis verdicts (proposed; L1 adjudication pending).** calibration
>   **improved (bounded)**; coverage **improved (bounded)**; depth **improved
>   (bounded) on the artifact surface, with a documentation harm recorded and
>   unresolved**. No axis unchanged; no `unprovable-but-better`; the round is **not
>   admitted** here — no L1 verdict artifact existed at record-drafting time.
>
> - **Carried debt.** (1) Tick-order qualification superset. (2) Nullable-`from_holder`
>   over-qualification. (3) Poll protocol: the 25-minute deadline was still missed by
>   ten seats (2–19 min late) and two first-pollers hit the 600 s timeout, leaving
>   gaps; `X1`'s patch arrival raced four seats' cutoffs, so their "X1 absent" lines
>   are not facts. (4) `M2`'s stale-map 3/14 late replay; `M4`'s pre-pledge R3 anchor.
>   (5) r87/r88 R9 delivery-mode annotation deferred to "next content touch" — r89 is
>   that touch, so re-state or discharge it. (6) Expectation parity: three F2 READMEs,
>   the r87 cluster README, the decision-table row-5 cell, `corpus/fixtures/README.md`,
>   `r87-probe-source-prefix/README.md`. (7) FN-1 raw-present branch has no durable
>   fixture. (8) Unlanded alternatives (`X2`/`X3`, `M1`/`M2`/`M3`, `D1`, `S3`, `W2`).
>   (9) Spence row renders outside the ledger table. (10) `capabilities` table still
>   empty in `SCORECARD.md`; `__pycache__` unnamed in `.gitignore`.
>
> - **Process.** The author→verifier barrier held: work-wave seats produced patches
>   and reports only, and patch-level verification happened in the follow-up wave
>   against the delivered tree. **The delivered checker is exactly `X1-c1.patch`
>   applied to `51b286b` — no integrator amendment this round**, closing r88's
>   unlogged-amendment gap (`V2`). Census invocations must use the baseline's
>   relative fixture paths. The wait protocol is advisory, not a gate: the deadline
>   discarded nothing only because the parent proceeded on late material.
>
> - **Province.** No follow-up province verdict existed at draft time. Work-wave
>   `K1`: the excerpts are lore-side record craft — no chousa artifact, citation, or
>   setting text appears in M1/M3/M4, and no lore setting text appears in the
>   sibling lanes (bounded literal scan); kotodama is rejected as the authoring lane,
>   and its integration-contract draft remains untracked with acknowledgement
>   pending. The r87 and r88 L0 lines stand unamended; `l0-questions.md` is unchanged
>   this round (4 lines).
>
> - **SHONEN.** No promotion, no push, no merge. `SHONEN.md` is unchanged this round
>   (`git diff --stat 51b286b 1b09f3f -- SHONEN.md` → empty); all four boxes stay
>   `[~]`/`[ ]` with no `[x]` claimed. Box 2's "logged in LOG.md" clause is satisfied
>   only once this entry is appended. No saturation or retirement is declared — the
>   `capabilities` table is empty and no rubric exists.

### Notes for the integrating owner (not part of the LOG text)

- Append under a new `## Round 89 — …` section at the end of `LOG.md`. No tracked
  file was written by P3; this proposal is the only P3 write.
- Figures sourced from follow-up seats rather than re-measured by me are attributed
  in-line (`V2`, `H2`, `H5`, `JCOV1`, `JCOV3`, `JCOV4`, `JDEP4`, and the work-wave
  `C6`/`C7`/`X1`/`M2`/`M4`/`SE1`/`W1`). P3's own re-measurements: the 160-dir census
  and 399-line count; the 149-dir baseline-vs-delivered tuple delta and the 4 changed
  paths; the 11 new dirs and the added-line arithmetic; the checker SHA-256s and
  numstat; the 10 C1 fixture replays; the 14 C2 anchor greps and the 22-fact
  composition; the M4 probe-command replay (`OK=8`); the R9 demo and R10 worked
  example; the ledger marker; and the two named-debt probes.
- **Decide before appending:** (a) whether to repair the boundary doc and the
  expectation layer inside the round (then depth reads as a clean bounded improvement
  and the harm paragraph is replaced by the repair receipt) or to record the harm as
  `depth: harmed (bounded)` per the r88 precedent; (b) whether to repair the three F2
  READMEs and the `r87-probe-source-prefix` line refs; (c) whether to enter
  `JDEP4`'s second capabilities row (blocked until the r88 row is actually present in
  `SCORECARD.md`); (d) whether to re-state the r87/r88 R9 annotation deferral in the
  r89 closure record or discharge it.
- Working-tree state at draft time (04:20 `-03:00`): `l0-questions.md` unchanged;
  `.ufo/waves/round-89/followup/` untracked (12 files). Nothing else.
- Scratch probes used by P3 lived under `/tmp/P3-*` and `/tmp/P3-probes/` and are not
  deliverables.

---

## Finalization addendum (04:32 `-03:00`) — supersedes the drafting pass's entry text

This seat ran a second pass after the remaining siblings landed (final two 60 s polls
04:28:07 / 04:29:07: 36 artifacts, unchanged; no L1 verdict artifact exists; drafting-pass
polls 04:17:38 / 04:18:38 had found the directory empty). Own re-verification reproduced
every headline figure in this file exactly — `TOTAL=160 zero=32 one=128`, **399 VIOLATION
lines** (raw 559 stdout lines = 399 findings + 128 trailers + 32 `CLEAN:` lines), 0 stderr;
`4 changed + 11 new`, 0 exit and 0 shared-path count changes, the 4 changed dirs being
`r87-probe-multi-invalid`, `r87-probe-record-and-chain`, `r88-mixed-stop`,
`r88-nonholder-stop`; 14/14 anchors → 1 each; composition 22; both clusters `CLEAN`; both
debt probes reproduce. New since the draft: **JDEP1's measured rendering defect** (the
R8–R10 rows render as a paragraph of literal pipe text — P3 re-verified 8 `<tr>` and
`<p>| R8` in the marked render), Q2's process figures (19/32 first artifacts ≤ deadline but
23/32 wrote after it; 10 seats hit the 600 s cap), K1's one-line `l0-questions.md` append
(now 5 lines, uncommitted), CB1's and E1's unlanded boundary-doc refresh proposals, P4's
SHONEN box proposal, and the full sibling consensus (JCAL1/JCAL3 calibration; JCOV1–JCOV5,
JDEP4 coverage; JDEP1–JDEP4, P4 depth — every judge ruling **improved (bounded)** or a
scoped sub-verdict, none unqualified). The full seat narrative and roll-up table are in
`followup/P3.md`; the append-ready entry follows.

### Append-ready `LOG.md` text (consolidated)

> ## Round 89 — 2026-10-17 (cause-branch fixtures + combined same-record cause summary +
> FN-1/FN-2 wording; r87 support completion; R8–R10 governance; luna-max work wave; work
> commit `1b09f3f`)
>
> - Baseline before this round is `51b286b` (r88 closure; lane tree clean). Work wave
>   `.ufo/waves/round-89/` (32 declared / 32 enumerated / 32 delivered seats) landed
>   `1b09f3f` (136 files, +12330/−15); judging/integration wave
>   `.ufo/waves/round-89/followup/` (36 artifacts). No push and no merge this round.
>
> - **Motivating evidence — C1 (calibration).** r88 admitted (bounded): six first-cause
>   branches had no durable fixture; the combined same-record cause summary existed only on
>   the shape-invalid branch, so a valid-key multi-defect record named only the first defect
>   in field order; FN-1/FN-2 input shapes were corpus-uncovered. Measured at `51b286b`: the
>   valid-key multi-cause case disclosed only the invalid tick, and a chain break against a
>   non-uniquely resolvable holder was reported as a definite mismatch.
>
> - **C1 landed — `1b09f3f`.** `corpus/fixtures/check_bible.py` (+54/−14; 395 → 435 lines;
>   sha256 `e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556`): valid-key
>   records retain and join **every** latching first-stop cause with `'; '`; raw entity/source
>   ID counts are tracked alongside the resolved indexes (FN-1, `absent from the raw table and
>   resolved index` wording); a comparison whose expected holder is not uniquely resolvable is
>   qualified as an input-structural *possible* break (FN-2). Eight cause-branch fixtures
>   (5 `r89-c1-*` + 3 `r89-f2-*`), the FN-2 pair, and the R9 demo land with it — 11 new dirs.
>   Counting from the lane root (relative paths; the r88 method trap): **160 dirs**, exits
>   `0=32 / 1=128`, **399 VIOLATION lines** (baseline-149 subset 367), 0 stderr; delta
>   **4 changed tuples + 11 new, 0 exit changes, 0 shared-path violation-count changes**; the
>   4 changed paths are pure FN-1 disclosure-wording substitutions (`r87-probe-multi-invalid`,
>   `r87-probe-record-and-chain`, `r88-mixed-stop`, `r88-nonholder-stop`).
>   `r89-c1-multi-cause-valid` → 4 findings, exit 1, first stop `malformed record (invalid
>   tick); ambiguous holder identity …`; `r89-fn2-control` → 1 finding, unqualified.
>   Corroboration: `V2` (**delivered checker == `X1-c1.patch` on `51b286b` byte-for-byte — no
>   integrator amendment this round**), `JCAL1` (145 unchanged / 4 changed; every changed line
>   inside a `first stop:` disclosure), `JCAL3` (9-mutation discrimination matrix; **improved
>   (bounded)**), `H1` (`145 unchanged, 4 changed, 0 exit flips`), `H2`, `H3` (12 replayed + 4
>   new mutations: 0 lost findings, 0 silent passes), `P1`.
>   Bounds: (a) **tick-order qualification superset** — a definite `tick <= previous_tick`
>   finding carries the qualifier plus a holder-identity note whenever a transition holder is
>   unresolved, though holder resolution is not a cause of tick ordering; (b) **nullable
>   `from_holder` misclassification** — a schema-valid `None` observed holder is scored as a
>   0-raw/0-indexed unresolved identity, so a definite chain break is labelled possible; both
>   reproduced by probe on the delivered tree (`C6`; P3 re-run); (c) three F2 READMEs still
>   quote pre-FN-1 cause strings (`V2`); (d) `S2-fact-map.json`'s `anchor_basis` still names
>   `M3-excerpts.patch` while the delivered bytes are M4's (`Q2` — provenance defect, anchors
>   resolve).
>
> - **C2 landed — `1b09f3f` (coverage).** Four delivered in-world excerpts (`gate-witness`,
>   `dune-register`, `shell-charter`, `tide-bell-tally`) make the r87 cluster **14/14 anchored**
>   (`grep -cF` → 1 each; P3 replay), i.e. **8 → 22 of 22** source-attributed facts (7 entity
>   claims + 7 pointers + 4 relation edges + 4 timeline events; R3's anchor is the
>   pledge-framed delivered phrase, so the pledge-vs-performance boundary holds). The ETCSL
>   ledger row gains `external-only / text not delivered at lore`. Both landed clusters replay
>   `CLEAN: schema, citations, relations, timeline; 0 violations`, exit 0. Corroboration:
>   `JCOV1` (**improved (bounded)**: 0/14 → 14/14 anchors, 1/7 → 7/7 pointers, 0 exit changes
>   over the 149 baseline dirs), `JCOV2` (**improved (bounded)**: excerpt discipline + ledger,
>   contradiction preserved unresolved), `JCOV3`/`JCOV4` (**improved (bounded)**), `JCOV5`
>   (**improved (bounded)**; excerpt footers track `reliability_note` one-for-one), `JDEP4`
>   (32/32 across two clusters), `H1`.
>   Bounds: `M4-verify.json`'s stored probe command replayed on the delivered tree prints
>   `facts=22 OK=8` — its `after.facts_supported: 22` is a hand-composed `8 + 14` and must not
>   be cited as the receipt (`JCOV1`-D1, `JCOV5` F2); `r87-myth-cluster/README.md` is unchanged
>   and lists none of the four excerpts; the decision-table row-5 evidence cell is stale
>   (`JCOV1`-D3); `M2`'s combined replay claimed 22/22 but matches only 3/14 of the current S2
>   anchors (`C7`); the 22/22 is reproducible under the anchor rule from `.ufo` scratch, not
>   yet certifiable from the delivered corpus alone (no in-corpus claim-to-excerpt map, P1).
>
> - **C3 landed — `1b09f3f` (depth).** `corpus/knowledge/r88-sourced-inspiration-decision-table.md`
>   gains **R8** (rights-blocked element disposition), **R9** (excerpt delivery-mode;
>   paraphrase is retelling support only), **R10** (cross-cluster contradiction register with
>   claim pointers and `unresolved` status), each with an owner and prospective scoping;
>   `corpus/knowledge/r89-cross-cluster-contradiction.md` is the R10 worked example (second
>   cluster explicitly hypothetical); `corpus/fixtures/r89-inspiration-paraphrase/` is the
>   durable R9 **negative** demo (mode declared in excerpt and map; anchor hits; support
>   withheld). Corroboration: `JDEP1`/`JDEP2`/`JDEP3`/`JDEP4` — **improved (bounded)**;
>   `JCOV3` (demo sub-scope improved (bounded)); `P4` (box-3 evidence improved). Bounds:
>   **JDEP1-D1 (measured)** — the three appended rows have no header/delimiter row, so a GFM
>   renderer emits them as a paragraph of literal pipe text (the file parses as 1 table / 8
>   rows, identical to baseline); D2 (R10's evidence cell quotes a superseded registry scan);
>   D3 (R8's element marker occurs nowhere outside the row); D4 (sixth-column label still
>   `r87 / round-88`); D5 (`(named debt, r89 ledger)` points at the not-yet-appended entry);
>   `JDEP2` files six governance debts (R8 detection gap, marker-string proliferation, R8
>   unexercised, R9 single-mode/unknown-version gap, R10 record-and-identity test, row-set
>   provenance); `JDEP3` rules register operability **unprovable-but-better** (no shared
>   referent between the two landed clusters).
>
> - **Documentation harm recorded, not netted.** `H2`/`H5`/`E1`/`CB1` measured that the
>   expectation layer did not keep up: `corpus/knowledge/holder-assessment-boundary.md` — the
>   doc `corpus/fixtures/README.md` names as "the current contract" — is stale on every
>   surface the r89 wording touched (cause-table rows, the precedence paragraph falsified by
>   `r89-c1-multi-cause-valid`, the decision row, a replay block that no longer reproduces,
>   code line refs), and it is **unrepaired on the delivered tree**; CB1's full refresh and
>   E1's update exist as follow-up proposals only (E1's named
>   `E1-boundary-update-proposal.md` is absent from the tree). `corpus/fixtures/README.md` has
>   no Round 89 section; `r87-probe-source-prefix/README.md` cites stale line refs. Per the
>   round rule a trade is not an improvement, so depth is not a clean improvement.
>
> - **Per-axis verdicts (proposed; L1 adjudication pending — the round is NOT admitted here).**
>   calibration **improved (bounded)**; coverage **improved (bounded)**; depth **improved
>   (bounded) on the artifact surface, with a documentation harm recorded and unresolved**.
>   No axis `unchanged`; no `unprovable-but-better` at axis scope. Every axis seat recommends
>   bounded-improved and none unscoped. P1's round report (`.ufo/reports/round-89/lore.md`)
>   rules nothing; **no L1 verdict artifact existed at 04:29**.
>
> - **Carried debt.** (1) Tick-order qualification superset. (2) Nullable-`from_holder`
>   over-qualification. (3) Poll protocol (Q2): 19/32 seats' first artifact ≤ deadline but
>   23/32 wrote after it; clerk inventory 21/31 at the cutoff; 10 seats hit the 600 s
>   foreground cap; per-seat deadlines spread 03:52:19–03:53:09; fixes I1 (≤9-check loops or
>   background with 1800 s) / I2 (`landing-<ts>.json` hash-stamped freeze) / I3
>   (`wave-spec.json` + `wave-validation.json`, amendments[]). (4) `M2`'s stale-map 3/14 late
>   replay; `M4`'s pre-pledge R3 anchor. (5) r87/r88 R9 delivery-mode annotation deferred to
>   "next content touch" — r89 is that touch; re-state or discharge. (6) Expectation parity
>   (three F2 READMEs, r87 cluster README, row-5 cell, `corpus/fixtures/README.md`, source-prefix
>   README, FN-2 READMEs). (7) FN-1 raw-present branch has no durable fixture. (8) Unlanded
>   alternatives (`X2`/`X3`, `M1`/`M2`/`M3`, `D1-rows.md`, `S3`, `W2`). (9) Spence ledger row
>   renders outside its table (pre-existing). (10) `capabilities` table still `— none yet —`;
>   `__pycache__` unnamed in `.gitignore`; `SHONEN.md` unchanged with stale evidence lines.
>   (11) JDEP1-D1 rendering defect plus D2–D5. (12) Q2 process debts: three integrator edits
>   (new `r89-c1-malformed-source-id` fixture, composed table, `S2-fact-map.json` R3 anchor
>   rewrite) unverified before commit and disclosed only in-artifact/in the commit message;
>   `C7`'s M3 preference overridden with the reason only in the commit message; the landing
>   record is an mtime snapshot (19/32 seats' cutoff state survives). (13) E1's and P1's
>   named-but-absent artifacts (`E1-boundary-update-proposal.md`, `followup/P1.md`,
>   `followup/P1-measurements.json`). (14) K1's `l0-questions.md` line is uncommitted at
>   record time.
>
> - **Process.** The author→verifier barrier held: work-wave seats produced patches and
>   reports only; patch-level verification happened in the follow-up wave against the
>   delivered tree. **The delivered checker is exactly `X1-c1.patch` applied to `51b286b` —
>   no integrator amendment this round** (`V2`), closing r88's unlogged-amendment gap. Roster
>   reconciles 32/32/32 as a count but is still Markdown (Q2 §3); one integrator-authored
>   fixture has no seat or landing row. Census invocations must use the baseline's relative
>   fixture paths.
>
> - **Province.** `JCOV5`: no chousa or kotodama bleed in the four excerpts, the R9/R10
>   artifacts, or the ETCSL marker; coverage **improved (bounded)**. `K1`: the r89 delta
>   produces no unresolved rights-blocked dispute and no other escalation trigger; the one
>   authorized `l0-questions.md` append lands as line 5 (uncommitted at record time),
>   correcting the r88 kotodama line's obsolete premise (contract now tracked in
>   kotodama-shokunin, `49ac1a5`, sha256 `e834f503…`; lore holds no acknowledgement record).
>   `PROVINCE.md` bytes unchanged; every changed path is under `corpus/` (76) or `.ufo/` (60);
>   the r87 L0 line stands unamended.
>
> - **SHONEN.** No promotion, no push, no merge. `SHONEN.md` is unchanged this round
>   (`git diff --stat 51b286b 1b09f3f -- SHONEN.md` → empty); boxes stay `[~]`/`[ ]` with no
>   `[x]`. `P4` proposes `[ ]` → `[~]` for box 3 (the D1 rule now has two demonstrated
>   applications); box 1 unchanged (no `SKILL.md`); box 2's "logged in LOG.md" clause is
>   satisfied only once this entry is appended. Capabilities table still `— none yet —`; no
>   saturation or retirement is declared.
>
> - **Round record.** `LOG.md` and `SCORECARD.md` are unchanged at `1b09f3f`; this entry is
>   the round's LOG record and the target of JDEP1-D5's pointer. Scorecard draft:
>   `patches/W2-scorecard-r89.proposal.md`.

### Delta vs the drafting pass's entry text (for the integrating owner)

- Added: JDEP1-D1 rendering defect + D2–D5; Q2's I1–I3 and process debts (including the
  `S2-fact-map.json` misnaming and the silent override of C7's preference); K1's L0 append
  and JCOV5's province verdict; P4's SHONEN box-3 proposal; the sibling-artifact gaps
  (E1/P1); the confirmed `capabilities`-table state; the anchor-rule caveat on 22/22.
- Corrected: the process bullet now cites Q2's measured poll figures (19/32 first artifacts
  ≤ deadline; 23/32 wrote after; 21/31 at the cutoff) instead of the drafting pass's
  narrower W1-only reading; the verdicts bullet now records the full judge consensus and
  states explicitly that no L1 verdict exists.
- Unchanged: every census/delta/fixture/anchor/debt-probe figure — re-verified in the
  finalization pass.
