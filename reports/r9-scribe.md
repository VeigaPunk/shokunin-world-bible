# Round 9 scribe — bounded decision table and README wording

Scope: documentation proposal only, based on the round-9 claim in `.shokunin/lore/LOG.md` and the current checker. No checker, fixture, or shared README was changed. The only artifact written is this report.

## Observed basis

- `.shokunin/lore/corpus/fixtures/check_bible.py` builds `events = index('timeline')`; `index()` emits a duplicate-ID violation but assigns `result[row['id']] = row`, so later valid rows overwrite earlier ones. The dependency check then compares `events[dep]['tick']` to the depending event's tick. `event_id_counts` is already computed for contradiction pointers, but dependency validation does not consult it.
- `.shokunin/lore/reports/r8-schema-scout.md` records disposable probes copied from the consistent fixture. Two valid timeline rows named `same` at ticks 1 and 5 plus a tick-3 consumer depending on `same` produced a duplicate-ID diagnostic and an inversion against tick 5. Reversing the duplicate rows produced only the duplicate-ID finding: the consumer was compared against tick 1. These are direct outputs on temporary inputs, not committed r9 fixture outputs.
- Baseline `.shokunin/lore/corpus/fixtures/consistent/timeline.json` uses a unique `departure` prerequisite; `.shokunin/lore/corpus/fixtures/README.md` describes dependency IDs as requiring strictly earlier ticks. Current checker prints violations and a no-canon-changed summary; it does not edit data.

## Bounded decision table (proposed wording of expected outcomes)

| Dependency target among schema-valid timeline rows | Dependency result | Existing / expected other result |
|---|---|---|
| No row has the referenced ID | Keep existing unknown-event diagnostic; do not compare ticks. | No event is selected. |
| Exactly one row has the referenced ID | Keep existing strict earlier-tick comparison. | Unique-ID baseline prerequisites retain their current result. |
| More than one row has the referenced ID | Emit one local `ambiguous dependency event` diagnostic at this dependency list entry; do not compare any candidate tick. | Keep the global duplicate timeline-ID finding and all event rows; do not choose first/last or infer inversion/valid ordering from them. |
| Depending event itself has a duplicated ID and references that ID | Apply the same more-than-one rule to the referenced ID. | The ambiguity is about target identity; retain duplicate-ID diagnostics. |

This table is bounded to dependency lookup by event ID. It does not prescribe changes to contradiction-ledger pointers, which already require exactly one matching timeline event, nor does it resolve event records, infer causality from prose, or validate game mechanics. If a repeated dependency value is present, the existing round-8 repeated-list finding is independent; this proposal does not redefine that behavior.

## Proposed README text (recommendation, not observed active documentation)

> Timeline dependency IDs are resolved only when exactly one schema-valid event has the referenced ID. If no event has that ID, the checker reports an unknown event. If multiple events share it, the checker reports an ambiguous dependency at that list entry and does not compare ticks for that dependency. The duplicate event rows and duplicate-ID finding remain; array order does not select a target. For a uniquely identified prerequisite, its tick must be strictly earlier than the depending event's tick. These checks validate input structure and the stated local tick convention; they do not establish causal truth or choose canon.

Suggested placement: append a short Round 9 subsection to `.shokunin/lore/corpus/fixtures/README.md` near Round 8's dependency-list section, once implementation/replay confirms the exact diagnostic wording and output. Do not present the proposal as active behavior before that validation.

## Limits / next evidence needed

The current checkout has no `r9-*` fixture directories or r9 run artifact at this writing; this scribe report therefore does not claim the round-9 behavior has been implemented or verified. Before adopting the README text, non-author replay should compare duplicate-target permutations, show the same local ambiguity diagnosis and other findings, and confirm unique-target and prior-fixture outputs remain unchanged. Keep raw CLI stdout/stderr/exit status with the round's run artifacts.
