# Round 56 scribe — holder-reference decision table

**Scope:** decision-table calibration only; no checker, fixture, README, LOG, or source edits. Counts refer to schema-admitted entity rows. This table describes observed baseline behavior and proposed interpretation separately; it does not assert actual custody, source-text support, canon, or rights.

## Observed baseline

`check_bible.py:142-148` initializes provenance chain state and permits chain checks only for a uniquely indexed item row. At `:167-185`, each non-null `from_holder` and each `to_holder` is checked for type/shape and entity-ID cardinality. Count zero emits a field-local dangling-entity finding (`:173-175, :181-183`); count greater than one sets `valid=False` without a holder-reference-local diagnostic (`:176-177, :184-185`). The invalid record clears `previous_holder`/`previous_tick` and disables subsequent chain comparison (`:195-198`). The duplicate entity ID is independently reported by `index()` (`:45-51`), and raw provenance input is not rewritten.

The existing `item-chain-valid` fixture provides a unique-holder chain control (`entities.json`, provenance entries; `sources.json` supplies IDs only). The `item-chain-broken` fixture changes the final predecessor and demonstrates the chain-break diagnostic. The checker does not establish that any source text supports the records or that a reported holder had actual custody.

## Proposed table (not implemented)

| Holder reference count among admitted entity rows | Proposed local finding | Proposed chain treatment / boundary |
|---|---|---|
| 0 | Keep existing dangling entity finding; no additional ambiguity finding. | Preserve current invalid-record handling; no chain conclusion for that record. |
| 1 | No holder ambiguity finding. | Preserve current validation/comparison behavior; a unique ID is structural resolution only. |
| >1 | Retain global duplicate-ID finding and add a local `ambiguous entity` finding at the exact `.to_holder` or `.from_holder` field. Report each affected reference independently. | Keep chain comparison withheld as it is now; do not select a row, combine records, or call chain continuity/discontinuity. |

A `null` `from_holder` is the first-acquisition form and is not an entity reference, so it has no 0/1/>1 lookup. Malformed records remain governed by existing shape/type checks. As established in round 26, malformed entity rows are excluded from admitted-row counts; they must not inflate multiplicity.

## Materiality and falsifier

**Independent material calibration judgment: NO-GO on current evidence.** A local report would improve the *location* of an already globally reported duplicate, but the checker already suppresses holder-chain comparison on multiplicity and retains the raw provenance fields. Prior analogous rules (r7 source ambiguity and r11/r24 relation/place endpoint ambiguity) demonstrate a consistent locality pattern, but do not by themselves prove readers need another report here. Unlike those cases, the relevant chain result is already withheld, so no changed or overconfident chain judgment is evidenced. Do not count an extra line as a calibration improvement without evidence that it prevents a plausible misreading.

A falsifier for this NO-GO: independent review of a schema-valid paired probe (duplicate at only `to_holder`, then only `from_holder`, plus unique control) shows the global duplicate finding does not let a reader locate which provenance assertion is unresolved, and that a field-local report materially prevents mistaken chain interpretation while preserving withheld comparison. The proposed signal must remain independent of source citation status and must not imply custody.

**Anticipated collateral if pursued:** additional diagnostics on existing duplicate-holder fixtures (if any), increasing violation counts; potential noise from repeating an entity-level duplicate at every use; accidental conflation of holder-ID ambiguity with actual-person identity or ownership; and regression risk if the local branch changes invalid-record/chain reset behavior. Preserve global duplicate and raw provenance; do not modify source records, chain state, or unique/unknown outputs.

## Evidence pointers

- `.shokunin/lore/corpus/fixtures/check_bible.py:45-51` — duplicate IDs diagnosed while last-row index is retained.
- `.shokunin/lore/corpus/fixtures/check_bible.py:142-148` — chain eligibility and provenance iteration.
- `.shokunin/lore/corpus/fixtures/check_bible.py:167-198` — holder resolution and chain invalidation/reset.
- `.shokunin/lore/corpus/knowledge/2026-10-12-lore-decision-table.md` Round 6 and Round 7 — holder ambiguity boundary and local source-ambiguity precedent.
- `.shokunin/lore/reports/r6-axis-adjudicator.md` — duplicate holders block chain judgment; no actual custody/source support inferred.
- `.shokunin/lore/reports/r11-scribe.md` — its place-specific ambiguity rule explicitly left provenance-holder ambiguity outside scope.
- `.shokunin/lore/reports/r24-scribe.md` and `r24-reviewer.md` — field-local endpoint precedent; do not resolve duplicate entity rows.
- `.shokunin/lore/reports/r26-scribe.md` and `r26-axis-adjudicator-retry.md` — only admitted rows count; malformed duplicates are excluded.

No fixture/checker/README/LOG edit or commit was made.
