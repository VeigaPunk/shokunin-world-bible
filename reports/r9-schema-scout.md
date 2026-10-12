# Round 9 schema scout — malformed timeline rows and duplicate-ID counts

Scope: read-only probes. Inspected `.shokunin/lore/corpus/fixtures/check_bible.py` and copied the committed `.shokunin/lore/corpus/fixtures/consistent/` input into `/tmp/r9-schema-*` probe directories. Each output below comes from the repo-root command `python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/r9-schema-<case>`. No checker or fixture in the repository was changed.

## Observed parser/schema behavior

The loader checks each timeline row against `FIELDS['timeline']` using exact Python types (`type(value) is expected`). Only a dict whose every required field passes is appended to `data['timeline']`; invalid dict rows and non-dict values are skipped for later timeline checks. The timeline index and `event_id_counts` are both built from this valid-row list, not raw JSON rows. Therefore a malformed duplicate row does not contribute to duplicate-ID count or dependency resolution.

Probes from the consistent baseline:

| Probe mutation | Exit / observed output |
|---|---|
| `arrival.depends_on` set to object `{"id":"departure"}` | exit 1: `timeline[1].depends_on: required nonempty list` |
| `arrival.depends_on` set to `["departure", 7]` | exit 1: `timeline[1].depends_on: expected event-id strings` |
| Insert integer `7` as `timeline[1]` | exit 1: `timeline[1]: expected object` |
| Remove `depends_on` from arrival | exit 1: `timeline[1].depends_on: required nonempty list` |
| Append duplicate `departure` with `depends_on` omitted | exit 1: `timeline[2].depends_on: required nonempty list`; no duplicate-ID message |
| Append duplicate `departure` with `tick: true` | exit 1: `timeline[2].tick: required nonempty int`; no duplicate-ID message (`bool` is rejected as not exact `int`) |

The malformed dependency-element case is handled in the timeline pass with a row-level `expected event-id strings` error and `continue`; that skips slot collision and dependency lookups for that otherwise valid event. Invalid schema rows do not reach the timeline pass at all.

## Duplicate-ID counting and lookup probes

For valid rows, `index('timeline')` reports every later repeated ID and overwrites its mapping with the latest valid row. `event_id_counts` separately increments per valid timeline row; the current count is used by contradiction references (`expected exactly one timeline event`), but not by the `depends_on` lookup, which still reads the last-wins `events` dict.

- Two additional valid `departure` rows at ticks 3 and 4 produced two duplicate diagnostics (`timeline[2].id` and `[3].id`) and an inversion against tick 4. Thus count diagnostics are per later duplicate occurrence, while the ID count includes all three valid rows.
- Duplicate target probe A: append valid `same` at ticks 1 then 5, and a tick-3 event depending on `same`. Output included duplicate `same` and inversion against tick 5.
- Duplicate target probe B: reverse `same` row order to ticks 5 then 1. Output included duplicate `same` but no inversion for the dependent event. Thus dependency result remains last-valid-row/order dependent. Both probes also accidentally used an ID `arrival` twice (the added dependent row copied its ID); the resulting `timeline[4].id: duplicate timeline id 'arrival'` appeared in both outputs. This unrelated duplicate does not account for the difference in `same` inversion.

Exact distinguishing outputs (after the common duplicate-ID findings):

- order A: `VIOLATION: timeline[4].depends_on: timeline inversion 'same' tick 5 not before 'arrival' tick 3`
- order B: no dependency inversion line.

## Separate recommendations (not implemented)

1. Keep schema-invalid rows excluded from semantic indexing; if desired, explicitly document that duplicate identity counts are over schema-valid rows, not raw rows. Current behavior is consistent and avoids using incomplete rows as event targets.
2. For dependency resolution, consult the valid-row `event_id_counts` before the last-wins `events` map. A count greater than one should produce a local ambiguous-target diagnostic and skip tick comparison, preserving both rows and the existing duplicate-ID finding.
3. A malformed `depends_on` list currently suppresses independent slot-collision checks on that event due to the early `continue`. Decide separately whether that diagnostic cascade policy is intended; it is outside the round-9 duplicate-ID claim.

These are input-structure observations only; no conclusion about in-world chronology, source truth, or causal meaning is inferred.
