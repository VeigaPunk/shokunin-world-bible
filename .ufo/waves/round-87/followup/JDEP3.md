# JDEP3 — Depth judge #3 (completeness attacker)

Seat: JDEP3. Wave: round-87 follow-up (world-bible lane), fleet root
`/home/vgpnk/Projects/shokunin`, repo `lore-shokunin/`.
Measured revision: `2b48ca72033dfd1060b6f81c4cf27ad83deae57f` (`2b48ca7`).
Detached scratch worktree `/tmp/r87-JDEP3` at that revision; probes under
`/tmp/jdep3/probes/`. No tracked file was written by this seat; every output is
`followup/JDEP3.md` and `followup/JDEP3-probes.json` (21 probes).

Mission: using S1's branch map alone, construct inputs that exercise a
provenance-block branch **not covered by the landed decision table**. Each
uncovered branch demonstrated is a depth-verdict finding.

Delivered checker identity (the table's own header pins the same hash):

```sh
cd /tmp/r87-JDEP3 && sha256sum corpus/fixtures/check_bible.py
# 3ae4134d1d7d0f4b72f5ed0b344de54e886b60ab7cacd8e8ab0008521efcb237  corpus/fixtures/check_bible.py
```

All probe commands are `python3 corpus/fixtures/check_bible.py <path>` run from
`/tmp/r87-JDEP3` (absolute probe path) or from the lane root (named fixtures).

## The table under attack — I1 landed mid-run

The block designates I1's `corpus/knowledge/r87-provenance-chain-decision-table.md`,
falling back to D2's patch if absent. Two wait-checks at 60 s spacing both
returned absent:

```sh
ls -la corpus/knowledge/r87-provenance-chain-decision-table.md   # x2, 60s apart
# ls: cannot access '.../r87-provenance-chain-decision-table.md': No such file or directory
```

I therefore began against D2's patch and demonstrated 14 uncovered branches /
stale rows against it. **I1 then wrote the file (untracked) before this report
was finished**, together with two durable probe fixtures. Re-checked:

```sh
git -C /home/vgpnk/Projects/shokunin/lore-shokunin status --porcelain
#  M corpus/knowledge/holder-assessment-boundary.md     (I2)
#  M l0-questions.md                                    (K2)
# ?? .ufo/waves/round-87/followup/
# ?? corpus/fixtures/r87-probe-entry-shape/
# ?? corpus/fixtures/r87-probe-record-and-chain/
# ?? corpus/knowledge/r87-provenance-chain-decision-table.md   (I1, untracked)
```

The findings below are re-derived **against the landed I1 table** (30 rows, 262
lines). The D2-based findings that I1's table resolves are listed at the end as
"closed by the landed table" so the parent can see what the integration fixed.

## Table quality check — every cited receipt replays byte-identically

The landed table claims "Every row's observed output is pasted from a rerun on
this tree". Independently replayed all 14 cited fixtures:

```sh
cd /home/vgpnk/Projects/shokunin/lore-shokunin
for f in consistent item-chain-valid r87-chain-unique-valid item-chain-broken \
         r87-chain-unique-broken r7-item-ambiguous r87-masked-break-to-ambiguous \
         r87-masked-break-from-ambiguous r87-probe-entry-shape \
         r87-probe-record-and-chain r61-independent-empty r61-independent-unavailable; do
  python3 corpus/fixtures/check_bible.py corpus/fixtures/$f; done
for f in r85-unique-break-control r85-masked-ambiguous; do
  python3 corpus/fixtures/check_bible.py corpus/live/runs/round-85/probe-inputs/$f; done
```

**Result: 14/14 reproduce the pasted output exactly** — every `VIOLATION:` line
in order, the final `N violation(s); no canon changed` / `CLEAN:` footer, and the
exit code. Spot checks: `r87-probe-entry-shape` → 2 findings
(`entities[6].id: duplicate entities id 'rope'`, `entities[4].provenance:
expected array`), exit 1; `r87-probe-record-and-chain` → 35 findings, exit 1;
`r7-item-ambiguous` → 7 findings, exit 1; `r61-independent-unavailable` → 6
findings, exit 1. The table is durable and reproducible; no row pastes a stale
output. (This is a real improvement over D2's patch, whose 26 `r87-d2-*` commands
were not replayable at all.)

---

## Findings against the landed table

### U-1 (uncovered, severe) — a row-shape violation deletes the entire provenance block

Branch: the row-shape gate `check_bible.py:65-76` drops an entity row whose
required members are malformed, so the row never enters `data['entities']` and
the block at `:171-273` never runs. S1 records the precondition (`S1.md:10`,
"Rejected raw entity rows never reach this block"); no table row covers it —
rows 1–30 all assume the entity passed the schema gate.

Probe `P17-rowshape-rejected`: `item-chain-valid` with `seal`'s required `name`
deleted and record `[1]` given a dangling `to_holder` plus an unknown `source_id`.

```sh
python3 corpus/fixtures/check_bible.py /tmp/jdep3/probes/P17-rowshape-rejected
# VIOLATION: entities[3].name: required nonempty str
# VIOLATION: relations[0].to: dangling entity 'seal'
# 2 violation(s); no canon changed
# exit=1
```

Neither the dangling holder nor the unknown source is reported. One malformed
field on an item row removes holder resolution, tick ordering, source membership
and chain continuity for that item **with no provenance-specific disclosure** —
a silent-skip class structurally identical to the one C1 closed for ambiguous
holders, and absent from the table. Depth finding.

### U-2 (asserted but not demonstrated) — ambiguous-source prefix on the FIRST-record finding

Row 19's code-anchor column cites `:267`, `:269`, `:271`, but its only fixture is
`anvil` r2, which exercises `:269`. Row 20 (`rope` r0, first record with non-null
`from_holder`) has no ambiguous source, so `:271` under the prefix is never
exercised anywhere in the table or its receipts.

Probe `P1-prefix-first-record` (duplicated `ambig-src`, record `[0]` cites it
with non-null `from_holder`):

```sh
python3 corpus/fixtures/check_bible.py /tmp/jdep3/probes/P1-prefix-first-record
# VIOLATION: sources[3].id: duplicate sources id 'ambig-src'
# VIOLATION: entities[3].provenance[0].source_id: ambiguous in-world source 'ambig-src'
# VIOLATION: entities[3].provenance[0]: input-structural finding, not sourced-canon; provenance chain break; first record must have from_holder null
# 3 violation(s); no canon changed
# exit=1
```

Depth finding.

### U-3 (asserted but not demonstrated) — ambiguous-source prefix on the TICK finding

Row 19's anchor cites `:267`; `anvil` r2 emits only the chain-break line (`:269`),
never a prefixed tick line. Row 21/22 (equal/reversed tick) have no ambiguous
source.

Probe `P2-prefix-tick`:

```sh
python3 corpus/fixtures/check_bible.py /tmp/jdep3/probes/P2-prefix-tick
# VIOLATION: sources[3].id: duplicate sources id 'ambig-src'
# VIOLATION: entities[3].provenance[0].source_id: ambiguous in-world source 'ambig-src'
# VIOLATION: entities[3].provenance[1].tick: input-structural finding, not sourced-canon; provenance tick 0 must be greater than previous tick 0
# 3 violation(s); no canon changed
# exit=1
```

`P13-prefix-both` (both comparisons fail after an ambiguous source) emits both
prefixed lines at one `record_label` — also not demonstrated by any row:

```sh
python3 corpus/fixtures/check_bible.py /tmp/jdep3/probes/P13-prefix-both
# VIOLATION: sources[3].id: duplicate sources id 'ambig-src'
# VIOLATION: entities[3].provenance[0].source_id: ambiguous in-world source 'ambig-src'
# VIOLATION: entities[3].provenance[1].tick: input-structural finding, not sourced-canon; provenance tick 0 must be greater than previous tick 0
# VIOLATION: entities[3].provenance[1]: input-structural finding, not sourced-canon; provenance chain break; expected from_holder 'mira', got 'tower'
# 4 violation(s); no canon changed
# exit=1
```

Depth finding.

### U-4 (uncovered, the residual masked-break vector) — a shape-invalid record carrying the ambiguous holder id never arms the stop

`:196-206` (`continue` on non-object / wrong key set) precedes the holder block
`:213-241`, so `holder_ambiguity_stop` is never set from a shape-invalid record;
`can_check_chain` latches false and every later comparison is skipped with no
disclosure. Row 8 covers the wrong-key finding alone; no row combines it with an
ambiguous holder id.

Probe `P6-shape-invalid-ambiguous` (`r87-masked-break-to-ambiguous` with an extra
key on the ambiguous-holder record `[0]`):

```sh
python3 corpus/fixtures/check_bible.py /tmp/jdep3/probes/P6-shape-invalid-ambiguous
# VIOLATION: entities[5].id: duplicate entities id 'dup'
# VIOLATION: entities[3].provenance[0]: expected exactly tick, from_holder, to_holder, source_id
# 2 violation(s); no canon changed
# exit=1
```

The genuine break that rows 14/15/29 disclose for the same fixture base is here
neither reported nor disclosed. Independently found by JCAL1 (probe
`r87-jcal1-residual-wrongkeys-ambiguous`, `JCAL1.md` Part C and debt item 1);
this probe confirms it on a C1 fixture base. Depth finding.

### U-5 (row-level defect) — row 26 mis-describes its fixture; the latch is not isolated

Row 26 claims: "`rope` r7 invalid, r8 **valid-but-would-break** … no break at
r8". The shipped `r87-probe-record-and-chain` `rope` r8 is
`{"tick": 10, "from_holder": null, "to_holder": "later-ghost", "source_id": "courier-log"}`.
`later-ghost` is dangling, so r8 is **invalid on its own** and its own finding is
what row 28 pastes (`entities[4].provenance[8].to_holder: dangling entity
'later-ghost'`). A record that is invalid is skipped by the `:260-263` gate
regardless of the r7 latch, so the fixture cannot distinguish "latch suppressed
the comparison" from "the record was invalid anyway".

Replacing r8 with a genuinely valid record that *would* fire keeps the claim and
removes the dangling finding (35 → 34):

```sh
python3 corpus/fixtures/check_bible.py /tmp/jdep3/probes/P20-valid-after-latch
# ... (lamp/bell/chime/anvil lines unchanged) ...
# VIOLATION: entities[4].provenance[7].source_id: unknown in-world source 'ghost-source'
# 34 violation(s); no canon changed
# exit=1
```

No `entities[4].provenance[8]` comparison line appears even though r8 is valid
and discontinuous, which **does** demonstrate the permanent latch. Depth
finding: row 26's stated evidence is inaccurate and its claim needs the valid
post-latch record to be sound.

### U-6 (uncovered, minor) — one record carrying an ambiguous holder *and* an invalidating source

Rows 13/14/15 and 16/17 cover the two families separately; row 27 combines an
*earlier* invalid record with a later ambiguous one, not the same record.

Probe `P8b-ambiguous-plus-unknown`:

```sh
python3 corpus/fixtures/check_bible.py /tmp/jdep3/probes/P8b-ambiguous-plus-unknown
# VIOLATION: entities[5].id: duplicate entities id 'vault'
# VIOLATION: entities[3].provenance[1].from_holder: ambiguous entity 'vault'
# VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons unassessed at this and all later records because holder identity is ambiguous
# VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity from_holder 'vault' first occurred at entities[3].provenance[1]
# VIOLATION: entities[3].provenance[1].source_id: unknown in-world source 'ghost-source'
# VIOLATION: entities[3].provenance[2]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity from_holder 'vault' first occurred at entities[3].provenance[1]
# 6 violation(s); no canon changed
# exit=1
```

Depth finding (minor: ordering only).

### U-7 (row evidence gap) — row 6 cannot demonstrate the suppression it asserts, and the silence is unstated

Row 6 ("source table unavailable") cites `r61-independent-unavailable`, whose
only `provenance` row sits on a **non-item** entity — so the chain was never
eligible and the row cannot show that unavailable sources suppress an eligible
item chain's comparisons. Unlike row 5 (whose fixture README explicitly declares
an injected would-be break), row 6 has no would-fire break.

```sh
# genuine item with a would-fire break (item-chain-broken), sources.json removed
python3 corpus/fixtures/check_bible.py /tmp/jdep3/probes/P5-unavailable-suppression
# VIOLATION: sources.json: cannot load JSON: [Errno 2] No such file or directory: '/tmp/jdep3/probes/P5-unavailable-suppression/sources.json'
# 1 violation(s); no canon changed          <- the record-[2] break is gone

# clean chain, sources.json removed
python3 corpus/fixtures/check_bible.py /tmp/jdep3/probes/P5b-unavailable-clean
# VIOLATION: sources.json: cannot load JSON: [Errno 2] No such file or directory: '/tmp/jdep3/probes/P5b-unavailable-clean/sources.json'
# 1 violation(s); no canon changed
```

The suppression is real, and it is **silent** — no per-record or item-level
disclosure is emitted, unlike the ambiguous-holder path C1 repaired. Row 6 does
not state that, and no row does. Depth finding (also the honest bound on the
calibration gain).

### U-8 (uncovered, minor) — `kind` outside `KINDS` plus `provenance`

```sh
python3 corpus/fixtures/check_bible.py /tmp/jdep3/probes/P18-unknown-kind
# VIOLATION: entities[3].kind: unknown kind 'relic'
# VIOLATION: entities[3].provenance: only valid on item entities
# 2 violation(s); no canon changed
# exit=1
```

Two findings on one entity; no row covers an unknown kind. Depth finding (minor).

### U-9 (uncovered, minor) — non-item + ambiguous holder emits disclosures though the chain was never eligible

Row 3's fixture (`r61-independent-empty`) has a non-item with *dangling* holders,
not an ambiguous one, so this combination is untested:

```sh
python3 corpus/fixtures/check_bible.py /tmp/jdep3/probes/P15-nonitem-ambiguous
# VIOLATION: entities[5].id: duplicate entities id 'vault'
# VIOLATION: entities[3].provenance: only valid on item entities
# VIOLATION: entities[3].provenance[1].from_holder: ambiguous entity 'vault'
# VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons unassessed at this and all later records because holder identity is ambiguous
# VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity from_holder 'vault' first occurred at entities[3].provenance[1]
# VIOLATION: entities[3].provenance[2]: provenance continuity and tick-order comparisons unassessed because ambiguous holder identity from_holder 'vault' first occurred at entities[3].provenance[1]
# 6 violation(s); no canon changed
# exit=1
```

Matches I2's refreshed boundary doc item 4 ("emission does not depend on chain
eligibility"). Depth finding (minor).

### U-10 (uncovered, trivial) — non-item AND non-array `provenance`

```sh
python3 corpus/fixtures/check_bible.py /tmp/jdep3/probes/P9-nonitem-nonarray
# VIOLATION: entities[3].provenance: only valid on item entities
# VIOLATION: entities[3].provenance: expected array
# 2 violation(s); no canon changed
```

Composition of rows 3 and 4; recorded for completeness.

## Coverage matrix — S1 branch map × landed table

| S1 family (`S1.md:10-25`) | landed row(s) | status |
|---|---|---|
| absent `provenance` | 1 | covered |
| wrong entity kind | 3 (+`r61-independent-empty` receipt) | covered (record-local continuation visible only in the receipt) |
| non-array `provenance` | 4 | covered |
| initial gate: unavailable sources | 6 | **U-7** (asserted, not demonstrated; silence unstated) |
| initial gate: duplicate item ID | 5 | covered — fixture README declares an injected would-be break |
| non-object record | 7 | covered |
| wrong key set | 8 | covered |
| tick validation | 9 | covered |
| holder field shape | 10, 11 | covered |
| holder identity resolution | 12, 13 | covered (both directions via `r87-masked-break-{to,from}-ambiguous`) |
| ambiguous-holder disclosure / latch | 14, 15 | covered — C1 after-state, two notices at the origin documented |
| source field and status | 16, 17, 18 | covered |
| source ambiguity prefix | 19 | **U-2, U-3** — anchor cites `:267`/`:271`, fixture exercises only `:269` |
| any invalid record → latch | 26 | **U-5** — fixture record is invalid, not "valid-but-would-break" |
| comparison gate skipped | 26, 28 | covered |
| first eligible record, non-null `from_holder` | 20 | covered (unprefixed) |
| later eligible records | 21–25 | covered |
| row-shape gate above the block | — | **U-1** |
| same-record multi-invalidity | — | **U-6** |
| unknown kind + `provenance` | — | **U-8** |
| non-item + ambiguous holder | — | **U-9** |

## Closed by the landed table (D2-based findings that no longer hold)

Recorded so the parent can see what I1's integration fixed, since I began the
attack against D2's patch:

- D2's `r87-d2-*` commands were not replayable from the tree (verbatim replay of
  `r87-d2-kind-gate` gave 5 JSON-load failures). **Fixed**: the landed table
  cites durable fixtures and all 14 receipts replay byte-identically.
- D2's ambiguous-holder rows encoded pre-C1 behavior (4/5 findings, one notice).
  **Fixed**: rows 14/15 document the C1 after-state, including the two notices at
  the origin record and the per-record disclosure.
- D2 asserted duplicate-item suppression without a would-fire break. **Fixed**:
  row 5 + `r87-probe-entry-shape/README.md` declare the injected break.
- D2 did not cover `from_holder`-only ambiguity. **Fixed**: row 13 cites
  `r87-masked-break-from-ambiguous` and its receipt.

## Per-axis verdicts

Vocabulary: improved / harmed / unchanged / unprovable-but-better. No scalars;
no trade recorded as an improvement.

| axis | verdict | basis |
|---|---|---|
| **depth** (committed tree at `2b48ca7`) | **unchanged** | I1's table and both probe fixtures are untracked (`git status --porcelain` above); nothing depth-related is committed. Measured on the tree, not on intent. |
| **depth** (with I1's landed-but-uncommitted table) | **improved (bounded)** | The C2 artifact now exists: 30 rows across the five lifecycle phases, every row pinned to a code anchor and a durable fixture, 14/14 receipts reproduced byte-identically by this seat, ambiguous-holder rows refreshed to the C1 after-state, and the four D2 defects closed. **Bound:** 9 demonstrated uncovered branches (U-1…U-9), of which U-1 and U-4 are silent-skip classes and U-2/U-3/U-5 are rows whose evidence does not demonstrate their own claim. The verdict is conditional on committing the table and the two probe fixtures; as delivered it is not part of the tree. |
| calibration (observed, not this seat's remit) | **improved (bounded)** | Replicated: the ambiguous-holder output is additive — `P10`/`P12`/`P15` show the per-record disclosure with the legacy notice preserved; `P6` shows the pre-existing residual vector is unchanged, not regressed. Bounds: U-4 (shape-invalid ambiguous record stays silent), U-7 (unavailable-source and duplicate-ID skips stay silent), and the double notice at the origin record (now documented by rows 14/15). |
| coverage (observed, not this seat's remit) | **unchanged** | No new checker rule; 138 census dirs per I3/JCAL1. |

No trade is claimed as an improvement: the added rows and fixtures add depth
coverage without removing any prior finding (verified by the byte-identical
replays above and by JCAL1's 156-case additions-only sweep).

## Handoff

- Land only `lore-shokunin/.ufo/waves/round-87/followup/JDEP3.md` and
  `followup/JDEP3-probes.json`. No tracked file, checker, fixture, knowledge
  file, registry entry, commit or push was made; `/tmp/r87-JDEP3` and
  `/tmp/jdep3/` are untracked and ephemeral.
- **Commit gate:** I1's `corpus/knowledge/r87-provenance-chain-decision-table.md`
  and the two `corpus/fixtures/r87-probe-*/` directories are untracked. The depth
  verdict is `unchanged` until they are committed; the integration is not
  finished.
- **Minimum table fixes before the depth verdict can be called clean:**
  (1) row 26 — replace `rope` r8 with a valid, discontinuous record (see
  `P20-valid-after-latch`) so the latch claim is demonstrated rather than
  asserted, and drop the contradictory "valid-but-would-break" wording;
  (2) rows 19/20 — add a fixture exercising the `:271` first-record prefix and
  the `:267` tick prefix, or narrow row 19's anchor column to `:269`;
  (3) add a row for the row-shape gate (U-1) — this is the most consequential
  gap, since a schema error silently deletes every provenance diagnostic for an
  item; (4) add rows for U-4, U-6, U-8, U-9 and a stated bound for U-7.
- U-1 and U-4 are the two candidates for a future depth *move* (both pre-existing
  and unchanged by round 87; each is a genuine silent-skip class that C1 did not
  close).
- Verification depth: 21 scratch probes (`followup/JDEP3-probes.json`, checker
  `3ae4134d…`), plus a 14/14 byte-identical replay of the landed table's own
  receipts. Gap: I did not re-run the full 138-dir census (I3/JCAL1 cover it) and
  did not read the two new fixtures' `README.md` beyond `r87-probe-entry-shape`
  and `r87-probe-record-and-chain`.
