# Round 9 simplifier — exact-one dependency lookup guard

Scope: inspect the current checker and run read-only CLI probes; no checker, fixture, shared document, or commit was changed. Relevant implementation: `.shokunin/lore/corpus/fixtures/check_bible.py`.

## Smallest exact-one guard

In the timeline dependency loop, after the existing unknown-ID branch and before reading `events[dep]['tick']`, test the already-computed `event_id_counts[dep]`. If the count is greater than one, emit one local diagnostic at `dep_location` (the existing `timeline[i].depends_on[j]` label), e.g. `ambiguous dependency event 'same'`, then skip the tick comparison. Otherwise retain the existing unique-event tick comparison. In pseudocode:

```python
if dep not in events:
    ...  # existing unknown diagnostic
elif event_id_counts[dep] > 1:
    errors.append(f'{dep_location}: ambiguous dependency event {dep!r}')
else:
    ...  # existing tick comparison
```

This is one narrow guard on the dependency lookup. `index('timeline')` already emits the duplicate event-ID finding and `event_id_counts` is already populated before the dependency loop. Do not alter the index, discard either row, or change unrelated event consumers (the contradiction ledger already requires exactly one event).

## Probe evidence

- Ran `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/consistent`: exit 0, exact stdout `CLEAN: schema, citations, relations, timeline; 0 violations`.
- Ran the same CLI on `.shokunin/lore/corpus/fixtures/r8-deps-distinct`: exit 0 with the same clean line. On `.shokunin/lore/corpus/fixtures/r8-deps-anomalous`: exit 1 and the existing three findings (repeated `departure`, self `arrival`, and its tick inversion). These cases confirm ordinary unique dependency behavior as currently observed.
- Built two temporary copies of the consistent fixture under `/tmp/r9-simplifier-yg4f3a8j` (not repository fixtures). Each had duplicate `same` event rows at ticks 1 and 5 and a tick-3 `consumer` depending on `same`; only duplicate-row order differed. CLI for ticks `(5, 1)` exited 1 with only `timeline[1].id: duplicate timeline id 'same'` (1 violation); ticks `(1, 5)` exited 1 with that duplicate finding plus `timeline[2].depends_on: timeline inversion 'same' tick 5 not before 'consumer' tick 3` (2 violations). Thus observed last-wins lookup changes the dependency conclusion with row order. Both CLI probes used `python3 .shokunin/lore/corpus/fixtures/check_bible.py <temporary-directory>` from repo root.
- Code evidence: `index('timeline')` reports duplicate IDs and assigns `result[row['id']] = row`, so `events` retains the last row. `event_id_counts` is computed from valid timeline rows. In the final timeline loop, dependency handling currently tests `dep not in events`, then reads `events[dep]['tick']`; it does not consult the count. The proposed guard reuses the available count and leaves unique/unknown handling alone.

## Separate recommendations (not part of the minimal guard)

1. Keep the existing duplicate-ID report and both timeline rows; do not choose or merge a canonical event.
2. Keep the ambiguity diagnostic local to each dependency list entry. Do not add source-text, causal, or event identity claims beyond identifier multiplicity.
3. Verify on paired fixtures that reverse duplicate target order yields the same ambiguity finding and no inversion conclusion, while old fixtures with unique dependency targets retain their exact stdout/exit results.
