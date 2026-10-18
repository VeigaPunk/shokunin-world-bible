# Round 37 pair scout — unique versus duplicate ledger endpoint

## Minimal controlled pair

Use `.shokunin/lore/corpus/fixtures/r35-bell7-conflict/` as the positive control. Its four timeline events include one `tarin-envelope-observation` and one `sella-bell7-presence` (`corpus/fixtures/r35-bell7-conflict/timeline.json:20-37`); `bell7-location-reports` points to those distinct events' `place_id` fields (`.../contradictions.json:2-13`). Its citations and two attributed reports stay intact. The expected clean result is documented in `reports/r35-executor.md:9-16` (checker command, exit 0).

For the negative case, clone that fixture and append exactly one duplicate timeline row with `id: "tarin-envelope-observation"` (preferably copied byte-for-byte from the original event); leave every other file and row unchanged. The duplicate row necessarily shares the same ID but adds a second candidate event. Keep the ledger pair and all citations untouched. This is the smallest mutation exercising uniqueness of a ledger endpoint without changing either narrative account.

## Checker evidence and expected findings

`check_bible.py:60-62` counts every timeline ID; `:92-95` requires the ledger endpoint count to equal one and only then resolves `events[event_id]`. Thus the unique control resolves both endpoints, while the duplicate case must report both the timeline duplicate and the ledger-local ambiguity for claim A: `timeline[4].id: duplicate timeline id 'tarin-envelope-observation'` and `contradictions[0].claim_a.event_id: expected exactly one timeline event 'tarin-envelope-observation'`. Claim B remains uniquely resolvable. Inventory all output from the actual run; do not assume these are the only diagnostics without running the checker. The checker indexes timeline by ID and accumulates counts (`check_bible.py:57-62`), so the cardinality check prevents treating whichever row won the index as a unique ledger target.

R9 is related precedent, not equivalent coverage: its duplicate-ID pair varies row order and observes dependency inversion behavior (`reports/r9-fixture-scout.md:7-13,19-31`). The r37 case adds a two-sided contradiction ledger whose endpoint must uniquely resolve, a distinct exercised branch (`check_bible.py:77-100`).

## Interpretation, risks, falsifiable check

A duplicated ID makes the ledger's claim-A endpoint ambiguous; it does **not** make Tarin's or Sella's testimony false, invalidate their citations as testimony, or resolve canon. The attributed reports and Bell-7 account remain narrative material; the malformed/ambiguous input cannot select either duplicate row as the ledger endpoint. Do not claim the checker tests whether the prose conflicts, who is physically located where, or which account is true. R35 explicitly bounds the Harbor pointer as Tarin's reported observation scene, not Tarin's own location (`reports/r35-executor.md:18-22`).

Falsifiable check: run `python3 .shokunin/lore/corpus/fixtures/check_bible.py <control-dir>` and the same command on the duplicate clone from repository root. Control should exit 0. Duplicate should exit nonzero, include the exact duplicate-ID and claim-A cardinality findings above, leave claim B free of an endpoint-cardinality finding, and retain the same source/citation content. Compare the two outputs and inventory every additional diagnostic; if the duplicate case lacks the ledger-local finding or the control is not clean, this pair fails to demonstrate the stated coverage. Do not change checker or fixture in this scout task.
