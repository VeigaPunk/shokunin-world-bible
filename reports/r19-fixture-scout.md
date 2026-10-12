# Round 19 fixture scout — invalid timeline ticks

## Raw observations (baseline CLI)

I invoked the baseline checker from the repo root with temporary copies of the `r18-unique-pair` fixture, changing only timeline rows. Temporary probe inputs were removed afterward. Each event description remained the fixture-input-only text: “Fixture input: event 0 has a place_id field; no source-text location is asserted.” (with the corresponding event number). The inherited source IDs satisfy input structure; they do not attest to the event descriptions or locations.

- **Negative pair:** the two otherwise-identical `mira` rows at distinct unique places `tower` and `harbor` both have tick `-1`. Exit 1. Output contains `timeline[0].tick: must be nonnegative`, `timeline[1].tick: must be nonnegative`, and `timeline[1]: double-booked 'mira' at tick -1 ...`.
- **Nonnegative control:** same two rows and places, both tick `9`. Exit 1. Output contains the `timeline[1]` double-booked finding at tick 9, and no invalid-tick findings.
- **Mixed known/invalid/known control:** unique `tower`/`mira` at tick 9, then unique `harbor`/`mira` at tick -1, then a second distinct event at unique `harbor`/`mira` tick 9. Exit 1. Output retains the middle row's `must be nonnegative` finding and reports a tick-9 double-booking between the first and third rows. There is no tick -1 double-booking because the only negative row has no other negative-tick counterpart.

These outputs are raw behavior on constructed JSON inputs only. They do not establish that any event occurred or that any place assignment is supported by source text or canon.

## Recommendation (not an observation)

Use the negative pair and nonnegative control as the minimal paired fixture design: identical actor, distinct unique places, row order and other fields, with only the tick value changed from `-1` to `9`. Expected bounded behavior for a proposed change: preserve both negative-tick diagnostics and raw rows but do not compare/store the negative rows for occupied-slot findings; retain the nonnegative control's double-booking. For preservation, use a three-row valid/invalid/valid sequence at ticks `9, -1, 9` as above; the two valid known rows must still conflict across the invalid middle row. If useful, include an all-negative pair to explicitly confirm invalid rows do not conflict with one another after the change, while retaining their per-row invalid-tick diagnostics.

Keep row descriptions explicitly fixture-only; do not treat `source_id` as attestation. An omitted checker conflict for invalid numeric input says only that the checker withholds this particular definite occupied-slot comparison; it does not mean the events are impossible, nonconflicting in-world, or canon-false. This scout makes no checker, fixture, or shared-document edits.
