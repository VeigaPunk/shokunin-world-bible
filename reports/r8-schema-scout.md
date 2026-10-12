# Round 8 schema scout — dependency shape and duplicate timeline IDs

Scope: observational probes only; no checker or fixture was changed. Checker examined: `.shokunin/lore/corpus/fixtures/check_bible.py`. Baseline input copied from `.shokunin/lore/corpus/fixtures/consistent/` to `/tmp/r8-schema-scout`; each probe ran the repository-root CLI `python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/r8-schema-scout`.

## Observed behavior

- `timeline.depends_on` is declared as a `list` in `FIELDS`. A non-list object therefore gets the generic loader validation `timeline[1].depends_on: required nonempty list`; the timeline pass then attempts iteration on valid stored rows? Here invalid rows are excluded by `valid` and absent from `data['timeline']`, so no crash occurred.
- A list containing a non-string (tested `[{}]`) is accepted by row-shape validation, then diagnosed as `timeline[1].depends_on: expected event-id strings` in the timeline pass. The loop `continue`s, skipping slot collision and dependency lookup for that event. It did not crash.
- A list of strings is not checked for duplicates. On the consistent fixture, changing arrival dependencies to `['departure', 'departure']` produced exit 0 and `CLEAN`.
- Self dependency does not crash: arrival changed to `depends_on: ['arrival']` produced exit 1 with `timeline[1].depends_on: timeline inversion 'arrival' tick 2 not before 'arrival' tick 2`. A self-reference to a unique event is therefore caught indirectly by the `>=` tick rule, not by a distinct self-dependency diagnostic.
- Duplicate timeline IDs are diagnosed by `index('timeline')`, but the ID dictionary is last-row-wins (`result[row['id']] = row`). The timeline dependency loop uses that dictionary. Probe with two `same` events at ticks 1 and 5 plus a tick-3 consumer depending on `same` produced duplicate-ID diagnostic and inversion against tick 5. Reversing duplicate row ticks to 5 then 1 left only the duplicate-ID finding: the tick-3 consumer was tested against last-row tick 1 and passed. Thus outcome depends on row order; ambiguous IDs still resolve to the last row for dependency tick comparisons. No crash in either case.
- A duplicate-ID self-reference can likewise compare to the last duplicate row rather than identify which event the current row references. A dependency pointing at any repeated ID is ambiguous; current dependency pass does not reject it as ambiguous.

## Evidence and boundaries

The checker’s relevant code is in `.shokunin/lore/corpus/fixtures/check_bible.py`: `FIELDS['timeline']['depends_on']` specifies `list`; `index(section)` reports duplicates and overwrites the dictionary entry; `event_id_counts` is collected; the final timeline loop validates string elements and then checks `dep not in events` / `events[dep]['tick']`. The `event_id_counts` guard is used for contradiction ledger event pointers, not dependency references. Existing committed baseline example `.shokunin/lore/corpus/fixtures/consistent/timeline.json` has one unique `departure` prerequisite and no duplicates.

Observed exit/output facts above are for the exact temporary copies and current checker; no repository fixture was mutated. Error count/order for further malformed combinations was not exhaustively explored.

## Separate recommendations (not implemented)

1. Consider a local diagnostic for repeated IDs in one `depends_on` list; duplicate prerequisite values currently pass cleanly and do not add information over one prerequisite.
2. Consider a distinct self-dependency diagnostic if the schema intends to identify self-edges rather than rely on timeline inversion wording.
3. Treat dependencies naming a duplicate timeline ID as ambiguous (local diagnostic) rather than resolving through the last-wins index; apply an explicit event-ID-count check before reading dependency ticks. This removes row-order-dependent dependency interpretation without selecting a record.
4. Preserve the existing behavior of reporting duplicate event IDs, and avoid silently choosing either duplicate as the dependency target. These recommendations are suggestions, not claims about intended canon or causal semantics.
