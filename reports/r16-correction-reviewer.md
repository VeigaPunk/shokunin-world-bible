# Round 16 correction review — non-author

## Scope

Read the correction plan in `LOG.md`, `reports/r16-correction.md`, the rejected `reports/r16-axis-adjudicator.md`, the four round-16 fixture inputs, the fixture README and decision table, the checker, and prior non-author replay reports. Replayed the four round-16 CLI cases. No source or fixture files were edited.

## Corrected descriptions and source support

The correction report records only three `timeline.json` description changes and before/after SHA-256 hashes. Direct inspection confirms the three affected `place_id` values remain `unlisted`; all event IDs, ticks, actors, source IDs, event order and other rows are unchanged. Each relevant row still has `source_id: "courier-log"`. The fixture entity list contains `harbor` (Lantern Harbor) and `tower` (North Tower), but no `unlisted` place. The source catalog supplies only the Courier Mira’s Route Log title and a generic reliability note; there is no source excerpt establishing what text the log contains.

The edits remove the original adjudicator’s concrete contradiction: none of the corrected descriptions names Harbor, Tower, or any resolved place for the `unlisted` row. No new place, identity, or canon claim is established by the checker. However, the replacement text says “A [separate] record uses unresolved place ID unlisted,” while that same timeline row cites `courier-log`. Read with the source reference, this can still be read as claiming the cited in-world record itself uses/reports that ID. The correction plan expressly says not to claim that the existing courier-log text attests the unresolved ID; unique source identity is not textual support. No excerpt or other evidence resolves this ambiguity. A clearly input-scoped description such as “Fixture row has unresolved `place_id` `unlisted`” would avoid attributing the ID to the source. Thus the original known-place contradiction is removed, but I cannot affirm that the correction fully satisfies the no-source-attestation constraint as written.

## Replay and controls

Replayed `python3 .shokunin/lore/corpus/fixtures/check_bible.py <fixture>` for all four fixtures. Each exited 1, with empty stderr:

- `r16-valid-places`: definite double-booking for `harbor` versus `tower`.
- `r16-missing-place`: dangling `unlisted` only; no double-booking.
- `r16-missing-first`: dangling `unlisted` only; no double-booking.
- `r16-mixed-three`: dangling middle `unlisted` plus the known `harbor`/`tower` double-booking.

The outputs match the saved transcripts in `corpus/live/runs/20261012T182817Z/` and the results recorded by the non-author verifier. The verifier reports the 29 preexisting fixture cases are byte-identical between baseline and current checker (stdout, stderr, exit), and all baseline JSON paths are unchanged. The correction report says only three prose strings changed; the saved CLI outcomes are unchanged by these prose edits. These controls support the narrow count-zero behavior, not a general resolved-place rule.

## Residual behavior and hidden uncertainty

The checker guard skips occupancy only when the place-ID match count is zero. As the reviewer’s disposable probes document, a unique wrong-kind entity (`mira`) still produces both its `not a place` diagnostic and a raw-ID `double-booked` assertion; a duplicate/ambiguous `harbor` still produces duplicate/ambiguous diagnostics and can still feed a `double-booked` assertion. Those are meaningful residual unsupported assertions, correctly documented as unchanged/out of scope; they prevent general claims that occupancy only compares resolved places. For `unlisted`, suppression leaves the real location and any resulting conflict unassessed. It does not prove no conflict, same-place occupancy, or a canon location. The mixed-three control establishes only that the known harbor/tower pair is still reported in this selected event order.

## Recommendation

**Reject / do not admit yet.** The narrow checker calibration improvement and four-case behavior are supported, and the prior Harbor/Tower prose harm is corrected. But the corrected description’s “record uses” phrasing, paired with its `courier-log` source ID, leaves a plausible unsupported source-text assertion contrary to the explicit correction constraint. Ask for a strictly fixture-input-scoped description and fresh review/readjudication; do not infer that the corrected prose is source-backed. If the adjudicator determines the description is unambiguously fixture metadata rather than an assertion about courier-log contents, this residual concern could be judged harmless, but the current artifact itself does not make that distinction explicit.
