# Round 9 reviewer — event ID ambiguity guard

## Scope and method

Read `.shokunin/lore/corpus/fixtures/check_bible.py`, the round-9 LOG declaration/clarification, and the raw round-9 fixtures. Replayed all 19 fixture directories with `python3 .shokunin/lore/corpus/fixtures/check_bible.py <fixture-dir>`. Also ran temporary scratch probes outside the repository; no checker or fixture was edited.

## Raw pair and unique control

The two pair fixtures have byte-identical `sources.json`, `entities.json`, `relations.json`, and `contradictions.json`; only `timeline.json` differs, swapping the order of the valid `same` records at ticks 1 and 5. In both orders, checker output is now exactly the duplicate-ID finding plus `timeline[2].depends_on[0]: ambiguous dependency event 'same'`; exit 1, two findings. The unique control has a single `same` at tick 1 and `consumer` at tick 3. It exits 0 with `CLEAN`.

This matches the narrow policy: count valid timeline rows by ID; for a dependency count 0 is unknown, count >1 is ambiguous, and only count 1 reaches the tick comparison. `events` remains last-wins, but the dependency loop consults `events[dep]` only in the count==1 branch. Contradiction event references separately reject counts other than 1 before reading `events[event_id]`. I found no ungated event-dictionary read in the checker that reintroduces order-dependent tick selection.

## Replay and adversarial probes

All 19 raw fixtures replayed with these exit/finding counts: clean (0) — `ally-reciprocal`, `consistent`, `item-chain-valid`, `r8-deps-distinct`, `r9-unique-control`; non-clean — `ally-one-way` (1), `contradictions` (3), `contradictions-ledger-malformed` (4), `item-chain-broken` (1), five `r5-*` fixtures (1 each), `r7-ally-reverse-ambiguous` (3), `r7-item-ambiguous` (7), `r8-deps-anomalous` (3), and both r9 pair fixtures (2 each). Results are the expected preexisting structural/citation findings plus the new paired diagnosis; no unexpected clean/non-clean flip appeared in the raw corpus.

Additional scratch probes:

- Duplicate target referenced twice: one ambiguity at the first occurrence and one existing repeated-dependency finding at the second; no tick comparison. This is consistent with round 8's once-per-distinct-ID lookup rule.
- A dependent row whose own ID is duplicated and depends on that ID: self-dependency and ambiguous-target diagnostics both appear, plus the duplicate-ID finding. No tick is selected. The output accurately separates raw self-reference from unresolved target identity.
- Unique self-dependency still gets the existing self-dependency and equal-tick inversion findings. The new guard did not erase the existing strict-earlier diagnostic for unique IDs.
- A malformed duplicate candidate (one `same` row has a string tick, so fails required-int validation) does not increase valid `event_id_counts`; the remaining valid target is uniquely resolvable. This follows the checker’s documented-in-code construction of `data` from schema-valid rows. It is important not to describe the guard as counting every raw malformed row.
- A dependency array containing a non-string takes the existing malformed-list branch and skips ID resolution, unchanged.

## Calibration judgment / limits

**Calibration: improved; no observed calibration harm.** Row order no longer changes whether the duplicate target is called earlier-than-consumer or non-earlier; the checker reports unresolved identity instead of silently using one row. The unique control demonstrates that the guard does not blanket-disable valid ordering checks. Prior raw fixtures retained expected outcomes.

Keep the claim narrow: this establishes order-invariant diagnostics for the tested duplicate-ID pair, not that either event is canonically true, that the citation text supports either event, or that the dependency is causally valid. An `ambiguous dependency event` means more than one *schema-valid* event row has that ID. Invalid rows are excluded before counting. No evidence here establishes behavior for every malformed JSON/row shape combination beyond the targeted probes.
