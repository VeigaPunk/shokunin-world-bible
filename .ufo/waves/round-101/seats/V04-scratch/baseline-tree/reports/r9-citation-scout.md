# Round 9 citation scout — identifier ambiguity and truth limits

Scope: read-only scout. I changed no checker, fixture, README, shared document, or commit. I wrote only this report. Commands below ran from the repository root; probe inputs were disposable copies under `/tmp/r9-citation-scout-*` based on `.shokunin/lore/corpus/fixtures/consistent/`.

## Observed distinction

The round-9 claim concerns **timeline event IDs**, not source IDs. In `.shokunin/lore/corpus/fixtures/check_bible.py`, `index('timeline')` reports repeated event IDs but stores the last valid row in `events`; `event_id_counts` separately counts valid timeline rows. The dependency loop currently checks membership in `events` and compares `events[dep]['tick']`, without consulting `event_id_counts`. The existing `.shokunin/lore/reports/r8-schema-scout.md` documents the same issue with duplicate target rows: reversing their order changed whether a consumer got a tick-inversion finding.

I independently copied the clean fixture, added a second valid `departure` event at tick 9, and retained `arrival` at tick 2 depending on `departure`. CLI: `python3 .shokunin/lore/corpus/fixtures/check_bible.py <temp-dir>`.

- Original then duplicate: exit 1; `timeline[2].id: duplicate timeline id 'departure'` and `timeline[1].depends_on: timeline inversion 'departure' tick 9 not before 'arrival' tick 2` (2 violations).
- Duplicate then original: exit 1; `timeline[1].id: duplicate timeline id 'departure'` only (1 violation).

This reproduces last-row lookup order dependence. It supports treating a dependency target with multiple valid rows as ambiguous rather than selecting a tick; it does not establish which event is canon.

## Event identity is not source attestation

The event's `source_id` is a separate reference into `sources.json`. The checker already counts valid source rows and classifies their IDs as unknown/unique/ambiguous (`source_id_counts` / `source_status`). `source(...)` reports unknown or ambiguous source references. A unique source ID therefore means only that exactly one valid source row has that identifier. It does **not** mean the source text was read, that the text supports an event, or that the event happened. Conversely, a duplicated event ID is an event-target identity problem even if each duplicate row cites a unique source ID; a duplicated source ID is a citation-identity problem even when the event ID is unique. Neither count resolves the other.

Probe: from a fresh clean copy, I added a second valid `courier-log` source row (same ID, distinct title) and a second valid `departure` event. CLI exited 1 with both `sources[2].id: duplicate sources id 'courier-log'` and `timeline[2].id: duplicate timeline id 'departure'`, plus local `ambiguous in-world source 'courier-log'` reports at affected references. The arrival dependency still yielded the last-wins tick inversion. The output demonstrates that current source-ID checks do not protect the separate event lookup.

The fixture ledger `.shokunin/lore/corpus/fixtures/consistent/sources.json` describes its fictional records with reliability notes, including that they are not omniscient truth. `.shokunin/lore/corpus/fixtures/README.md` likewise says the checker validates citation references, not citation truth. Those boundaries align with round 7's note in `.shokunin/lore/LOG.md`: unique IDs qualify by identity only, never text support.

## Truth limits

A count-based `ambiguous dependency event` diagnostic would say only: “this dependency identifier names multiple valid event rows, so the checker cannot select one for the local tick comparison.” It should not say the events are false, that either row is the intended event, or that the source proves/disproves a causal relation. Suppressing tick comparison for an ambiguous target avoids an order-selected inference; it does not validate the dependency or make the underlying event assertions true. Unique event ID and unique source ID are both identity facts, not semantic verification.

## Separate recommendations (not implemented)

1. For a dependency ID with count greater than one among schema-valid timeline rows, report a local ambiguity at that dependency-list entry and skip tick comparison; retain the existing duplicate-event-ID finding and every row. Keep unknown and exactly-one target cases distinct.
2. Keep this event-target guard separate from source-ID qualification. Do not present unique source IDs as proof of textual support or canon truth.
3. When describing the behavior, call it identifier-resolution / input-structure validation, not causal-truth verification. Preserve the order-pair replay and unique-ID control as evidence for the bounded claim.
