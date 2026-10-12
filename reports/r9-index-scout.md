# Round 9 index scout — timeline ID counts and consumers

Scope: observational map only. I did not edit the checker or fixtures. Target: `.shokunin/lore/corpus/fixtures/check_bible.py`.

## Timeline ID counts

The checker first validates rows into `data['timeline']`; only structurally valid rows enter that list. `index('timeline')` builds `events` and reports duplicate IDs, but overwrites the prior row (`result[row['id']] = row`), so `events` is last-row-wins. Immediately afterward, `event_id_counts` counts IDs across all structurally valid timeline rows.

I counted valid JSON timeline rows / distinct IDs in the repository fixture directories: `consistent` 2/2; `contradictions` 4/4; `contradictions-ledger-malformed` 4/4; `item-chain-valid` 2/2; `item-chain-broken` 2/2; `r7-item-ambiguous` 2/2; `r8-deps-distinct` 2/2; `r8-deps-anomalous` 2/2. Other existing fixtures with timeline files had 0/0 (the alliance-only ones) or 2/2. None of these checked-in timeline fixtures currently has duplicate IDs. This is a count of fixture data, not a claim that malformed rows contribute to the index.

## Index consumers

- **Contradictions ledger — count-guarded and ambiguity-safe.** For each `claim_a`/`claim_b` event pointer, lines 92–94 require `event_id_counts[event_id] == 1`; otherwise they report `expected exactly one timeline event` and `continue`. Only then (line 95) does the pass read `events[event_id]`, to check event source resolvability. Thus this ledger consumer does not silently use the last duplicate event. It checks pointer resolution, not whether the cited field's assertion is true.
- **Dependency tick validation — not count-guarded.** In timeline pass lines 253–256, unknown IDs are reported if absent from `events`; otherwise `events[dep]['tick']` is compared to the depending row's tick. This uses the last-wins mapping without consulting `event_id_counts`. A duplicate target can therefore be read as a seemingly definite event for inversion checks.
- **Duplicate-ID diagnostic itself.** `index('timeline')` emits one duplicate-ID diagnostic for each later repeated valid row while retaining the final row in `events`; it does not resolve the ambiguity.
- Other references: contradiction `event_id_counts` guard is the only additional use of the count map. `events` is used by the two consumers above. Timeline double-booking and entity/place checks do not dereference event IDs.

## Probe outputs

I copied `consistent/` to `/tmp/r9-index-scout-gnlsenak`, replaced only that temporary `timeline.json` with `same@tick1`, `same@tick5`, and `consumer@tick3 depends_on ['same']`, and ran:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/r9-index-scout-gnlsenak
VIOLATION: timeline[1].id: duplicate timeline id 'same'
VIOLATION: timeline[2].depends_on: timeline inversion 'same' tick 5 not before 'consumer' tick 3
2 violation(s); no canon changed
EXIT:1
```

This confirms the dependency consumer reads the final duplicate row. The prior scout report `.shokunin/lore/reports/r8-schema-scout.md` documents the reverse-order probe: duplicate rows at ticks 5 then 1 plus consumer at 3 yield only the duplicate-ID diagnostic, because the final row then has tick 1. Together these outputs show order-dependent dependency interpretation. On the existing clean control, `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/consistent` printed `CLEAN: schema, citations, relations, timeline; 0 violations` (exit 0).

For a ledger contrast, existing `contradictions-ledger-malformed/contradictions.json` points to absent event `absent-event`; the checker output is `contradictions[1].claim_b.event_id: expected exactly one timeline event 'absent-event'`. That is the exact-one pointer rule. The same run's `arrival` dependency on unique `later@tick3` reports `timeline inversion 'later' tick 3 not before 'arrival' tick 2`.

## Separate recommendations (not implemented)

1. In dependency validation, consult the event-ID count before reading the tick; for a count greater than one, emit a local ambiguity finding at that dependency list entry and skip tick comparison for that ID. Preserve the duplicate-ID finding and both rows.
2. Keep the contradiction ledger's exact-one policy distinct from dependency semantics. It already avoids last-wins resolution; its pointer check should not be described as validating claim truth.
3. Use paired fixtures that differ only by duplicate target row order; require the ambiguity result and all other findings to be invariant. Also retain a unique-target control to demonstrate unchanged inversion behavior.
