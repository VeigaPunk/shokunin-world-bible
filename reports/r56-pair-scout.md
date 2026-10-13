# Round 56 pair-scout — holder-reference duplicate calibration

## Independent recommendation: GO, narrowly, for a proposed calibration probe

This supports a single bounded candidate: distinguish a structurally admitted duplicate holder ID from a unique ID at the exact provenance reference path, while retaining the existing global duplicate-ID finding and raw provenance record. It does not warrant a checker edit by itself. There is an operator-facing difference between a duplicate elsewhere in the entity table and identifying which provenance field is unresolved; the proposed local path can show which record’s chain is withheld without implying which duplicate is intended. Confidence is modest: duplicate-ID already invalidates input, so the reviewer should reject if this precise localization is not materially useful.

## Observed repository evidence (not proposed behavior)

- `.shokunin/lore/corpus/fixtures/check_bible.py:132-151` iterates an item’s provenance records; malformed provenance structures disable chain checks.
- `check_bible.py:153-163` reads `from_holder`, `to_holder` and sets `valid=True` per record.
- `check_bible.py:167-185` validates nonempty IDs. A zero entity count yields a field-local `dangling entity` finding at `:173-175` / `:181-184`. A count greater than one only sets `valid=False` at `:176-177` / `:184-185`; no holder-reference-local ambiguity message is appended.
- `check_bible.py:195-208` skips chain comparisons for an invalid record, clearing predecessor state and disabling chain checking; admitted source references are still validated at `:186-194`. Thus baseline already withholds chain comparison on duplicate holder IDs and retains the input records; the missing diagnostic is the exact ambiguous reference location.
- The schema-admitted control is `.shokunin/lore/corpus/fixtures/item-chain-valid/entities.json:1-59`; item `seal` has three records at `:37-58`, with `to_holder: mira` (`:41`), `from_holder: mira` / `to_holder: harbor` (`:47-48`), and `from_holder: harbor` / `to_holder: tower` (`:53-54`). These IDs are otherwise unique in this fixture. Required entity fields are screened before indexing (`check_bible.py:8-43`); admitted IDs are counted (`:59-67`).
- `item-chain-valid/sources.json:1-14` describes in-world reports, not omniscient truth. Its provenance entries are input assertions, not established actual custody.

## Minimal proposed pair and controls

Use temporary copies outside the repository, derived byte-for-byte from `item-chain-valid/`, and run the existing checker as a probe. Do not commit these probes or edit fixtures/checker.

1. **Unique control:** unchanged fixture. Expect no holder-reference ambiguity finding. This is a control for the existing three `from_holder`/`to_holder` fields, not proof of the underlying holder assertions.
2. **`to_holder` duplicate:** append one complete, schema-valid entity row duplicating ID `mira` (copy the existing `mira` row exactly). No provenance/source/text changes. Candidate result: one local ambiguity finding for each affected `to_holder: mira` occurrence, at `entities[3].provenance[0].to_holder` and `[1].from_holder` is not affected; note carefully the second record’s `from_holder` is `mira`, so it is affected too. This gives both field directions if only that one duplicate row is used; require exactly `to_holder` at record 0 and `from_holder` at record 1, with chain comparisons withheld as baseline already does.
3. **`from_holder`-only duplicate:** if isolating direction is required, instead duplicate `harbor` and observe `.provenance[1].to_holder` as well as `.provenance[2].from_holder`; this again touches both directions. Therefore do not call these isolated-direction cases. To isolate field direction, change only a single existing provenance reference to the duplicated ID while retaining other references unique; however that changes raw provenance value and no longer a duplicate-only treatment. Prefer one duplicate-ID treatment and assert every matching reference per direction rather than overselling “to-only/from-only”.
4. **Both directions / no extra pair:** the same `mira` duplicate naturally exercises `to_holder` and `from_holder`, while `harbor` duplicates would exercise the complementary positions. A separate both-ID duplicate case adds little. If desired, a malformed duplicate control (e.g. remove required `name` from the duplicate row) is not admitted and must not count as a duplicate control, per `.shokunin/lore/reports/r26-schema-scout.md` and checker screening at `:32-43`.

**Simplest useful treatment:** a single temporary duplicate `mira` row against unchanged control, with the expected two local sites above. Keep all four JSON files and source text unchanged except `entities.json` adding that row; do not add claims or provenance records. The duplicate row itself will produce the existing global duplicate diagnostic. Exact complete output must be inspected; any extra findings from copied row fields are collateral, not silently ignored.

## Proposed decision table (not implemented or observed)

| Admitted holder-ID count | Existing behavior | Candidate local finding | Safe interpretation |
|---|---|---|---|
| 0 | dangling field finding; record invalid | none in addition | no admitted entity row resolves the ID |
| 1 | no holder ambiguity; may participate in chain check | none | unique fixture ID only |
| >1 | record invalidates chain continuation; duplicate entity finding elsewhere | `ambiguous entity <id>` at that `from_holder` or `to_holder` path | reference does not select one admitted row; no duplicate is chosen |
| one admitted plus malformed same-ID row | malformed row excluded from counts | no ambiguity on that basis | screening result only, not evidence of semantic absence or canon |

Proposed diagnostic must be one per affected non-null reference, not merely one per record. Null `from_holder` remains the initial-value marker and is not looked up. Do not change chain gating, source resolution, duplicate-ID reporting, or raw records. A duplicate ID can produce both global and local findings by design; no cascade should invent a chain-break finding for the same invalid record.

## Axis calibration, falsifier, and collateral

**GO for a narrowly scoped candidate/review; depth unchanged, coverage unchanged, calibration potentially improved.** It makes the existing “invalid due to duplicate” state actionable at the provenance field, without choosing a holder. This is not a claim that actual chain behavior improves: chain comparisons are already withheld by baseline. If review determines the global duplicate diagnostic plus lack of chain findings already identifies this concern adequately, classify calibration unchanged and NO-GO.

**Falsifier:** pair the unique control and schema-valid duplicate probe. If no reader can identify a more precise unresolved provenance site from the proposed field diagnostic, or it merely repeats a global duplicate with no useful location, there is no calibration gain. Also reject if the proposed wording implies an actual holder, a break/removal, or resolves a duplicate. Required-field-malformed duplicate is explicitly not a positive case.

**Anticipated collateral:** extra diagnostic lines can be mistaken for independent evidence or inflate errors; avoid treating them as separate semantic failures. Duplicating `mira` affects two raw references, so expect two local sites—not a to-only test. It invalidates the first two record chain steps and may suppress later comparisons under existing state reset; preserve that baseline behavior and do not attribute it to the new message. Copying a full entity row may also trigger other duplicate-entity-dependent checks; use complete-output diff. No actual custody, source truth, canon, rights, or permission follows from the fixture or diagnostic.

**No implementation or test result claimed.** No repository probe was run; all diagnostic expectations above are proposals inferred from the checked-in code. This report is the sole permitted write.
