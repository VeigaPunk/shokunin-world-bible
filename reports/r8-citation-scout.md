# Round 8 citation-boundary scout

## Observed evidence

- `.shokunin/lore/corpus/fixtures/check_bible.py` requires `timeline[*].source_id` as a nonempty string. In the timeline loop, `source(row['source_id'], location + '.source_id')` reports whether that ID is unknown or ambiguous; under the Round 7 rule, exactly one valid source row makes the ID unique. This establishes identifier resolution only.
- `.shokunin/lore/corpus/fixtures/consistent/sources.json` defines `courier-log` as a fictional personal log and `archive-ledger` as a fictional municipal record. `.shokunin/lore/corpus/fixtures/consistent/timeline.json` has `arrival` cite `courier-log` and list `departure` in `depends_on`. The checker separately checks `departure` as an event ID and its tick; it does not associate the prerequisite with its own `source_id` as evidence for the dependency assertion.
- `.shokunin/lore/corpus/fixtures/README.md` says dependencies must have strictly earlier ticks and sources are in-world fictional records. It also explicitly limits the checker to reference validation, not truth of citations. `.shokunin/lore/LOG.md` round-8 claim is about a self-listed event ID or repeated prerequisite ID in one event's list, not source-text attestation.

## What duplicate/self dependency diagnostics would and would not establish

If implemented as scoped, relation-local list-integrity findings, they can establish only that the input list contains a repeated ID or the event's own ID. A self-dependency also currently reaches the existing `events[dep]['tick'] >= row['tick']` test and emits a timeline-inversion diagnostic; that tick-order result does not independently prove a causal cycle or a canon contradiction. Repeated IDs can also produce repeated downstream inversion findings when the prerequisite is not earlier; those are separate consequences of the current per-entry loop, not citation validation.

Neither new diagnostic establishes that an event occurred, that the named prerequisite is causally necessary, that a source supports the dependency, that two different event IDs denote distinct real-world events, nor that repeated list entries are erroneous in the fiction rather than redundant author input. It does not verify source contents, chronology beyond the explicit integer comparison, or any game mechanics. A unique `source_id` on the event does not cure these limits: current schema/calls validate the event's source ID, not the evidentiary support of each dependency edge.

## Recommendation (separate from observations)

Describe the new rule as input-list integrity, not source-backed causal validation. Keep `source_id` validation for each event distinct from `depends_on` ID-list diagnostics. If a report mentions citation, say only that the event row has a unique resolvable in-world source ID; do not imply the source attests the dependency. Avoid claiming cycle detection: this rule checks self-membership and duplicate membership only, and the existing tick comparison is a direct-edge ordering check, not general graph-cycle analysis.
