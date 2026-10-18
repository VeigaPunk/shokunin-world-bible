# Round 9 test scout — reversed duplicate dependency targets

Scope: read-only replay matrix. I inspected `.shokunin/lore/corpus/fixtures/check_bible.py` and `.shokunin/lore/corpus/fixtures/r8-deps-distinct/` (copied to `/tmp/lore-r9-replay`; no repository fixture or checker was changed). Each probe ran from the repository root with `python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/lore-r9-replay/<case>`.

## Replay matrix

| Probe | Relevant timeline rows | Observed CLI result |
|---|---|---|
| `forward` | duplicate `same` rows at ticks 1 then 5; `consumer` tick 3 depends on `same` | exit 1; duplicate ID at `timeline[1]`, plus `timeline[2].depends_on: timeline inversion 'same' tick 5 not before 'consumer' tick 3`; 2 violations |
| `reverse` | same duplicate rows reversed (ticks 5 then 1); consumer unchanged | exit 1; duplicate ID at `timeline[1]` only; 1 violation |
| `unique` control | one `same` at tick 1; consumer tick 3 depends on it | exit 0; `CLEAN: schema, citations, relations, timeline; 0 violations` |
| `unknown` control | consumer tick 3 depends on absent `missing` | exit 1; `timeline[0].depends_on: unknown event 'missing'`; 1 violation |

Exact replay output for the pair:

```text
===forward===
VIOLATION: timeline[1].id: duplicate timeline id 'same'
VIOLATION: timeline[2].depends_on: timeline inversion 'same' tick 5 not before 'consumer' tick 3
2 violation(s); no canon changed
EXIT:1
===reverse===
VIOLATION: timeline[1].id: duplicate timeline id 'same'
1 violation(s); no canon changed
EXIT:1
```

## Invariant comparison

The pair keeps IDs, ticks, consumer dependency, and all non-order data fixed; only the two duplicate target rows’ order changes. Desired invariant per the Round 9 claim: both orders retain the duplicate-ID finding and report an `ambiguous dependency event` at the consumer’s `depends_on` entry, without asserting either an inversion or a valid ordering. Current observed output is **not row-order invariant**: forward order produces a last-wins inversion; reverse order omits it. Thus this replay supports the calibration problem and does not pass the proposed invariant. Unique and unknown controls behave as expected in these probes.

Code basis: `index('timeline')` in `.shokunin/lore/corpus/fixtures/check_bible.py` reports a duplicate but assigns `result[row['id']] = row`, so the last duplicate overwrites the prior row. `event_id_counts` is computed, but in the timeline dependency loop the lookup is only `dep not in events` followed by `events[dep]['tick']`; it does not reject IDs whose count exceeds one. The duplicate finding is therefore separate from dependency resolution and does not prevent last-wins tick comparison.

## Separate recommendations (not implemented)

- Before reading a dependency target tick, check the valid timeline-row count for that ID. For counts above one, report the local ambiguous-target diagnostic and skip tick comparison for that dependency; retain the duplicate-ID finding and all rows.
- Keep the unique-ID and unknown-ID branches distinct; the controls above show these should respectively continue to compare ticks and report unknown event.
- For implementation validation, rerun this same pair and compare all non-order findings; require one ambiguity diagnostic in each order and no order-dependent inversion claim. This report does not establish behavior on malformed event rows or combinations with repeated dependency entries.
