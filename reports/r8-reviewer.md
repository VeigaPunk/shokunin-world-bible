# Round 8 independent reviewer replay

## Raw fixture replay

Ran `python3 .shokunin/lore/corpus/fixtures/check_bible.py <fixture-dir>` from the repository root against all 16 raw fixture directories. Outcomes: `consistent`, `ally-reciprocal`, `item-chain-valid`, and `r8-deps-distinct` exited 0. The other 12 exited 1. The two new cases are isolated as intended: `r8-deps-distinct` is clean; `r8-deps-anomalous` reports exactly (1) repeated `departure` at `timeline[1].depends_on[1]`, (2) self dependency `arrival` at index 2, and (3) the pre-existing equal-tick inversion for `arrival`. No citation, entity, or other diagnostic appears in these fixtures.

To check regressions, extracted `check_bible.py` at baseline commit `17736ae5ed260c4b99f98efd9b194254ccd2aa87` and replayed each of the 14 pre-round-8 fixture directories against it. All 14 current exit codes and stdout were byte-identical to baseline. The two raw r8 fixtures have their expected clean/anomalous split.

## Targeted dependency probes

Used the checker function against copied in-memory fixture tables (no fixture or checker edits) to vary only dependency lists:

- Repeated unknown ID `missing, missing`: one unknown-event diagnostic plus a local repeated-ID diagnostic at the second occurrence. No duplicate unknown lookup cascade.
- Repeated later/known ID `later, later` with the target event at tick 3: one timeline-inversion diagnostic plus the repeated-ID diagnostic. No duplicate inversion cascade.
- Self-only `arrival`: explicit self-dependency and existing equal-tick inversion. This matches the LOG clarification to retain the baseline inversion rather than suppress it.
- Self repeated twice: first entry yields self + inversion; second yields self + repeated. Each raw self occurrence is visibly reported, and no second inversion is emitted.
- Distinct valid earlier ID `departure`: no findings.

The implementation's `seen_dependencies` set suppresses only the repeat's downstream lookup; each raw repeated occurrence still gets a location-specific repeat finding. Citation behavior remains separate: every event row is source-checked by the existing timeline loop, and the dependency-list checks do not claim the cited source text supports causality.

## Known duplicate event-ID limitation

Confirmed the stated limitation. `index('timeline')` retains the last row for a duplicated ID, and the dependency traversal tests membership then reads `events[dep]['tick']`; it does not consult `event_id_counts`. A dependency on duplicated ID `dup` can therefore appear as an inversion if the last `dup` row has tick 3, but not if the same rows are reversed and the last row has tick 1 (with dependent tick 2). The duplicate-ID finding remains in either case. Thus dependency resolution remains order-dependent/ambiguous for duplicate event IDs; this round makes no claim to resolve that ambiguity. This is a separate existing limitation, not a false cascade from repeated dependency entries.

## Review conclusion

Round-8 coverage claim is supported: a repeated prerequisite ID that previously passed silently is now rejected locally, while independent distinct prerequisites remain clean. Self-specific output is diagnostic clarity in addition to the prior inversion, as clarified in LOG. No false repeated-lookup cascades appeared in the tested repeated unknown/future cases. No code edits made; only this report was written.
