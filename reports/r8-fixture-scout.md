# Round 8 fixture scout — timeline dependency list

## Observed baseline

- `.shokunin/lore/corpus/fixtures/consistent/timeline.json` has `departure` at tick 1 with `depends_on: []`, then `arrival` at tick 2 with `depends_on: ["departure"]`; this is the smallest existing clean dependency witness. Both events cite `courier-log`.
- `.shokunin/lore/corpus/fixtures/consistent/sources.json` contains the in-world source ID `courier-log` (Courier Mira’s Route Log). This supports reference resolution only; it does not establish documentary truth.
- `.shokunin/lore/corpus/fixtures/check_bible.py` indexes timeline events by ID, then loops through each `depends_on` entry at the timeline-check block. It reports unknown IDs and dependencies whose tick is not strictly earlier (`timeline inversion`). The loop shown there does not currently check repeated entries or an event depending on itself as a distinct list anomaly; a self-reference currently reaches the inversion check.
- `.shokunin/lore/corpus/fixtures/README.md` documents the local tick convention and strict-earlier dependency rule, and says checker contradictions prompt editorial review rather than choosing canon.

## Minimal pair recommendation (fixtures only)

Use two copies of the clean `consistent/` bible, changing only `timeline.json`'s `arrival.depends_on`:

1. **Clean distinct-list control:** set it to `["departure"]` (retain baseline exactly). Expected clean result; establishes that an ordinary, unique prerequisite is accepted.
2. **Anomalous list:** set it to `["departure", "departure", "arrival"]`. Keep event rows and citations unchanged. Expected relation-local diagnostics for the repeated `departure` entry and self-dependency `arrival`; do not remove either entry or infer a causal order. Since `departure` is already earlier than `arrival`, its repeated occurrence should isolate duplicate-list handling from inversion. The self reference is an intentional anomaly.

This is the smallest practical pair using observed event IDs and cited records: no new lore facts or source records are needed. Both rows retain their existing `courier-log` citations. A fixture should not claim that the citation proves either event true.

## Separate recommendations / boundaries

- **Fixture authoring:** create paired copies from `consistent/`, mutate only the dependency array, and record the exact diff. Do not use `contradictions/timeline.json` as the clean control: its `arrival -> later` edge intentionally points from tick 2 to tick 3, and it also includes a same-tick sighting.
- **Checker behavior:** report duplicate and self references at the dependency relation/list location; do not silently deduplicate or discard the self-edge. Keep existing unknown-ID and strict-earlier checks independent. A duplicate occurrence of an otherwise valid earlier ID should not create a timeline inversion finding.
- **Scope:** these fixtures test input-list integrity, not whether dependencies are causally true in the fictional world, source-text support, event order outside the declared ticks, or game mechanics.
- **Optional stronger distinct-prerequisite control:** if the round specifically requires two *different* prerequisite IDs in one clean list, add one earlier, cited event to both copies (same tick 1, same entity/place as `departure`, so existing same-tick/location rules remain clean) and use `["departure", "signal"]` for `arrival`. That is not minimal and introduces another event assertion, so prefer the one-prerequisite control unless the claim requires plurality.
