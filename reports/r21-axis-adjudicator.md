# Round 21 — final independent axis adjudication

## Decision

**Admit the narrow coverage move.** Coverage **improved**; depth **unchanged**; calibration **unchanged**. No harmed axis is observed within the declared scope. This is an input-level checker result, not a claim that either fictional event occurred or a canon contradiction was proved.

## Independent inspection and replay

I read the round-21 declaration and post-scout clarification in `LOG.md`, the current checker and its diff against baseline report commit `64d2673`, all eight raw `fixtures/r21-*` inputs, their eight saved outputs, the critic/executor/reviewer/independent-verifier reports, and the 64 saved outputs in `corpus/live/runs/20261012T193022Z/`. My direct CLI replay of those 64 commands matched each saved exit code and output **64/64**. The old run directory `20261012T191902Z/` contains **56** transcripts, all byte-identical to their counterparts in the new 64-output directory. The non-author verifier additionally ran *both* baseline and current checkers on those 56 old inputs, finding **56/56** exact baseline-versus-saved and **56/56** exact baseline-versus-current exit/stdout/stderr matches; it checked **279/279** baseline-tracked JSON fixtures byte-identical. That old replay is bounded: none of those inputs has a non-string member in a list-valued `depends_on`.

The code diff only relocates the existing unique-actor, unique-place-of-kind-`place`, nonnegative-tick occupancy compare/store before the malformed dependency-list branch; its `all(isinstance(dep, str) ...)` test, single list diagnostic, `continue`, and valid-list dependency traversal remain otherwise unchanged.

## Falsification checks

- `r21-clean` and `r21-malformed` differ only in second-row `depends_on: []` versus `[null]`. Both emit the identical definite checker booking for unique `mira`, tick 9, `tower`/`harbor`; malformed also emits `expected event-id strings`. `r21-clean-reverse`/`r21-malformed-reverse` repeat that pairing with place order reversed, retaining the corresponding `harbor`/`tower` booking. These fixtures put the malformed list on the second row; reverse place order alone does **not** test malformed-first insertion. Reviewer and independent verifier separately ran temporary malformed-**first** probes, finding the first row participates in the occupied slot and the later valid row reports the booking.
- A mixed string/null dependency list is intentionally **list-wide skipped** for dependency lookup. The reviewer’s temporary `['missing-dependency', null]` probe found the malformed diagnostic and booking, but no unknown-dependency diagnostic for the valid string; the verifier’s `['r21-event-1', null]` malformed-first probe likewise found booking and the list diagnostic without inversion. No per-member recovery is claimed; a potentially meaningful string dependency in a malformed list remains unassessed, not declared satisfied.
- `r21-same-place` emits only the list diagnostic, not a booking. `r21-invalid-tick` emits two negative-tick findings and the list diagnostic, not a booking. `r21-wrong-kind-place` emits the not-a-place and list diagnostics, not a booking. `r21-ambiguous-actor` emits duplicate and ambiguous actor findings plus list diagnostic, not a booking. Thus tested equal-place and ineligible time/place/actor inputs do not gain unsupported occupancy assertions. These are targeted controls, not exhaustive malformed-input proof.

## Per-axis reasoning and boundary

- **Coverage: improved.** On uniquely resolved, distinct known places at one valid actor/tick slot, a malformed dependency member no longer masks an independent occupancy finding. Both order directions and malformed-first probes support it; the malformed-list error remains.
- **Depth: unchanged.** No new ontology, contradiction class, dependency inference, or source-text analysis is added.
- **Calibration: unchanged.** The pre-existing certainty gates are unrelaxed and the malformed dependency list still blocks all member-wise checks. No observed spurious booking on the listed controls. This does not prove calibration over arbitrary malformed rows or imply that missing dependency diagnostics are impossible.

Fixture rows, descriptions and structurally resolving `source_id` values are test inputs, not source passages. The checker neither validates source-text support for actor/place/time nor adjudicates canon. A booking finding reports contradiction under its input rule only; absence of a dependency finding on a malformed list is unassessed. Admit only this bounded coverage change, with no source/canon, broader recovery, or universal-regression claim.
