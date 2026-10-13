# Round 62 loader-scout — timeline availability and event-ID consumers

## Independent verdict: GO to test a narrow calibration move; no implementation authorization

The timeline loader substitutes `[]` after file/JSON errors and also after a successfully loaded non-array, while there is no `timeline_available` state. This creates dependent ledger findings that currently read as established event-ID cardinality failures despite the index being unavailable. The evidence supports testing a timeline-only availability gate. It does not yet prove material net improvement: loaded-empty and loaded-partial inputs also yield zero-match ledger findings, and those distinctions must remain. Recommendation is conditional GO for the declared matched probe and adjudication, not a verdict that code should change.

## Code paths and consumers

At `.shokunin/lore/corpus/fixtures/check_bible.py:40-56`, `timeline.json` load/read/duplicate-member failures set `rows=[]`; non-array also sets `[]`, with an error. Only entities and sources record availability (`:57-60`); timeline has no corresponding flag. Valid timeline rows populate `events` and `event_id_counts` at `:88-92`.

Event-ID consumers:
- Contradiction ledger at `:109-137`: validates each side's local `event_id` and `field` first (`:113-123`), then uses `event_id_counts` (`:124-127`). A count other than one emits `expected exactly one timeline event` and skips event-source evaluation. A unique event's source-status check is separate (`:128-132`). Distinct claim-side comparison (`:133-137`) is independent of timeline loading.
- Timeline dependency validation at `:289-310`: each successfully parsed timeline row checks dependency type, self/repeat, missing/ambiguous target IDs and tick inversion. A failed whole-file load supplies no timeline rows, so this loop cannot produce dependency findings; do not add a speculative cascade or suppress the primary file/shape error.
- The `events` dictionary/index is otherwise not consumed for event membership. Timeline row source citations use the independent sources index (`:279`); entity/place/occupancy and tick checks are separate (`:263-288`).

## Observed matched probes (temporary copies only)

I ran the active checker on temporary copies under `/tmp`; no repository fixtures were changed. First, `consistent` with its other four JSON tables held byte-identical and no contradiction rows:

| timeline state | observed output |
|---|---|
| missing | load error only (exit 1) |
| malformed `{bad` | JSON load error only (exit 1) |
| non-array `{}` | `timeline.json: expected array` only (exit 1) |
| loaded `[]` | clean (exit 0) |
| loaded partial (drop last row) | clean (exit 0) |
| loaded duplicate event ID (duplicate first event) | duplicate timeline ID plus dependent ambiguous dependency (2 findings; exit 1) |

The clean outputs do not exercise ledger membership, so I also used `r39-ledger-source-missing` as the fixed base. Only timeline state varied; `sources`, `entities`, `relations`, and `contradictions` remained unchanged. Its ledger has two valid event references. Missing, malformed, and non-array timeline each retain the primary file/shape error **and add two** `contradictions[0].claim_{a,b}.event_id: expected exactly one timeline event` findings (three total). Loaded empty has the two ledger findings without a loader error. Loaded partial (removing the final event) emits only the missing B-side event finding; A still resolves. These observations establish the proposed false-certainty concern and the required available-table contrast. They do not test every malformed/duplicate-member mode or candidate behavior.

## Prior art, materiality and falsifier

R7 axis adjudication is about source-ID ambiguity and reference qualification, not a failed timeline index. R39 adjudication/reviewer explicitly tests a uniquely identified ledger event with zero matching source rows versus ambiguous source rows; its `event_id` resolves, so this is a different branch. R60/R61 establish entity/source availability gates only. Their status analogies are not proof for timeline; their reports expressly distinguish table-specific callers and require independent testing. R61's source-unavailable ledger probe is especially useful as a control: it preserves ledger event-pointer checks while gating source-derived conclusions, demonstrating the importance of retaining independent ledger checks, not an existing timeline policy.

Falsifier: if a candidate gates the ledger's `event_id` cardinality findings on timeline unavailability, it must still retain the timeline load/shape diagnostic and local ledger side/type validation, distinct-claim checks, and independent checks in other tables. A loaded `[]` must continue to report both unmatched ledger references; loaded partial must report only unmatched IDs; loaded duplicate IDs must remain ambiguous, not unavailable. On unavailable timeline, only conclusions requiring the timeline event index should be withheld; do not suppress independent source-ID, source availability, ledger structure, or unrelated table checks. If the useful output can be framed merely as an availability/status analogy with no meaningful new calibration, reject on materiality. Lost event-side lookup hints are the principal cost; retaining local side pointers/type errors and the actionable timeline file error limits it. Treating the current `expected exactly one` text as harmless would be a competing judgment, but it does not distinguish zero events because the file failed from zero events in a loaded table.

No event row's description establishes that an event occurred, no event-ID membership establishes chronology or source-text support, and no inference about world absence, canon, rights, or permission is made. No code, fixtures, README, LOG, or commit changed. This report is the only repository write.
