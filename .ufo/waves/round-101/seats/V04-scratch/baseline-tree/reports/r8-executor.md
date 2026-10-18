# Round 8 executor report — dependency-list diagnostics

Implemented the scoped checker change in `corpus/fixtures/check_bible.py` only. After the existing all-string guard, each timeline row's `depends_on` list is traversed in input order. A self-ID gets a list-indexed diagnostic; every occurrence after a dependency ID's first occurrence gets a repeated-ID diagnostic at its own index. The original list is not edited or deduplicated. Unknown-event and direct tick/inversion checks run once on each distinct ID, which prevents repeated identical cascades while retaining existing behavior for lists without repeats. The existing self tick inversion is intentionally retained alongside the self-dependency finding.

No dependency target resolution policy was changed: duplicate timeline event IDs still produce the existing duplicate-ID diagnostic and dependencies still consult the existing last-wins event index. Therefore lookup for an ambiguous event ID can remain row-order dependent; this round does not claim uniquely resolved prerequisite records.

## Fixture outputs

Command: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture>`.

`r8-deps-distinct` (exit 0):
```
CLEAN: schema, citations, relations, timeline; 0 violations
```

`r8-deps-anomalous` (exit 1; raw list retained as `["departure", "departure", "arrival"]`):
```
VIOLATION: timeline[1].depends_on[1]: repeated dependency 'departure'
VIOLATION: timeline[1].depends_on[2]: self dependency 'arrival'
VIOLATION: timeline[1].depends_on: timeline inversion 'arrival' tick 2 not before 'arrival' tick 2
3 violation(s); no canon changed
```

The anomalous fixture's repeated prerequisite is earlier, so the output isolates list repetition without an inversion cascade. Self-reference also retains the established tick-inversion finding.

## Regression evidence

Compared stdout and exit status byte-for-byte for all 14 pre-existing fixture directories against the checker extracted from baseline `17736ae5ed260c4b99f98efd9b194254ccd2aa87`. All matched: `ally-one-way`, `ally-reciprocal`, `consistent`, `contradictions`, `contradictions-ledger-malformed`, `item-chain-broken`, `item-chain-valid`, `r5-invalid-citation`, `r5-invalid-json`, `r5-missing-file`, `r5-row-shape`, `r5-wrong-top-level`, `r7-ally-reverse-ambiguous`, and `r7-item-ambiguous`.

In particular, `contradictions` remains exit 1 with exactly three findings: dangling relation endpoint, one inversion (`later` at tick 3 not before `arrival` at tick 2), and double-booking. No fixture JSON, source citation, event, or duplicate event-ID lookup behavior was changed.
