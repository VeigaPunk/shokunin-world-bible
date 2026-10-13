# Round 70 fixture scout — matched event-ID comparison controls

## Scope and evidence

Report-only fixture design; no fixture or checker files were changed and none of the proposed cases below was created or run. The round-70 declaration in `.shokunin/lore/LOG.md` pins baseline HEAD `5ccbffa` and proposes gating the pair-level comparison on each side having a nonempty string `event_id`, while retaining raw `field` equality and all field-validation diagnostics. It specifically requires missing/blank ID probes, retention of the R62 malformed-field pair warning, valid-identical and valid-distinct controls, and old-fixture raw tuple review.

Active checker: `.shokunin/lore/corpus/fixtures/check_bible.py`. In the ledger loop (lines 119–126), an absent, empty, or whitespace-only event ID gets `required nonempty string`; invalid fields get their own allowed-field diagnostic. Afterward (lines 139–143), the current pair comparison runs whenever both sides are dictionaries and raw `event_id` and `field` values compare equal, including absent/blank IDs and invalid fields. The declared candidate predicate gates only this pair comparison on both event IDs being nonempty strings; it does not gate on `field` validity or event existence. The checker's `strip()` establishes whitespace-only IDs as invalid for local validation.

Useful common base: `.shokunin/lore/corpus/fixtures/r62-loaded/` has a loaded timeline with the unique `tarin-envelope-observation` and `sella-bell7-presence` IDs and a locally valid, different-reference ledger. Its other tables and narrative ledger text can be held fixed. Caveat: baseline replay already reports unrelated `claim_b` unresolved event-source and `timeline[3].source_id` unknown-source diagnostics, so compare complete output tuples and isolate only the target pair finding. A cleaner base can be made from a fixture with known loaded event IDs and sources, after verifying that property; do not assume `consistent/` exercises ledger pairs, because its `contradictions.json` is empty. `.shokunin/lore/corpus/fixtures/r62-malformed-side/` is *not* a matched base: its `timeline.json` is malformed. Its ledger has identical nonempty event IDs and identical invalid `bogus` fields; current replay yields the timeline load error, two field errors, and the pair warning (four findings). It is still the required retention precedent, but the controlled test should transplant that ledger pair into the common loaded-table base.

## Exact matched matrix

For each row, start from the same copied five-table base (prefer `r62-loaded`), retaining `sources.json`, `entities.json`, `relations.json`, timeline, contradiction row `id`/`why`, and every unrelated byte. Change only the two claim pointer objects as shown. `field` values are raw JSON strings. Keep all other fields and record metadata identical. Invoke the checker from repository root with the same command and capture exit code, stdout, and stderr byte-for-byte. Predictions are code-reading expectations, not execution results.

| Case | claim_a | claim_b | Current checker target prediction | Declared candidate target prediction |
|---|---|---|---|---|
| absent IDs | `{field: "place_id"}` (no `event_id` key) | same | Two required-ID findings **plus** `references must differ` | Two required-ID findings; no pair finding |
| empty IDs | `{event_id: "", field: "place_id"}` | same | Two required-ID findings **plus** pair finding | Two required-ID findings; no pair finding |
| whitespace IDs | `{event_id: "  \t", field: "place_id"}` (whitespace only; e.g. two spaces) | same | Two required-ID findings **plus** pair finding | Two required-ID findings; no pair finding |
| valid-ID / invalid-field (R62 retention) | `{event_id: "tarin-envelope-observation", field: "bogus"}` | same | Two allowed-field findings **plus** pair finding | Same: two allowed-field findings **plus** pair finding |
| valid same reference | `{event_id: "tarin-envelope-observation", field: "place_id"}` | same | Pair finding | Pair finding retained |
| valid different references | `{event_id: "tarin-envelope-observation", field: "place_id"}` | `{event_id: "sella-bell7-presence", field: "place_id"}` | No pair finding | No pair finding |

For absent-ID testing, JSON object key omission—not `null`—is the intended absent-value control. Add a `null` variant only if a distinct JSON-type control is desired; the local validator treats it as non-string, but it is not needed to distinguish missing values. The whitespace example is a string containing spaces (the table notation `\t` is explanatory; use literal spaces for a reproducible whitespace-only case). Keep field allowed in the first three cases so the event-ID defect is isolated. Keep event IDs identical and nonempty in the invalid-field case: it directly tests the declared choice not to require a valid field for pair comparison and preserves R62 behavior.

The control rows should compare full tuples, not just exit status. On `r62-loaded`, unrelated diagnostics may remain identical in every row; the target comparison is whether the pair-level message appears or not. The valid-different row should use two unique IDs present in the loaded timeline (both are present in `r62-loaded`) so missing/ambiguous event-index outcomes do not confound the comparison. If selecting another base, verify the IDs against its `timeline.json` first.

## Falsifiers, boundaries, and limitations

The narrow proposal is falsified if the candidate retains the pair finding for absent/empty/whitespace IDs; drops either side's local required-ID finding; removes the pair warning for the R62 valid-ID/invalid-field case; removes a valid identical-reference finding; adds a pair finding for valid distinct references; or changes independent diagnostics. Candidate validation additionally needs the declared old-fixture exact raw tuple comparison; this scout did not replay the corpus or establish regression preservation. The matrix tests the pair-comparison policy, not whether any future event/field assertion is usable or true.

These are checker-input structural diagnostics only. No result establishes event occurrence, source-text support, a story contradiction, chronology, truth, canon, rights, or game mechanics. The common base's unresolved/unknown source outputs are known confounders and must not be recast as conclusions about the fictional material.
