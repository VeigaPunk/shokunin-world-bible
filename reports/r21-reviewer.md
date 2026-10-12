# Round 21 independent reviewer report

## Scope and replay

I did not edit source, fixtures, shared documentation, or commits. I independently inspected the round-21 checker diff, all eight raw `r21-*` fixture directories, the saved outputs under `corpus/live/runs/20261012T193022Z/`, and the round-21 scope notes. I replayed each of the 64 saved CLI commands against the current checker; exit code, stdout, and stderr matched all 64 saved transcripts.

The paired fixture inputs `r21-clean` / `r21-malformed` differ only in the second row's dependency list (`[]` / `[null]`). The clean case reports the known distinct-place booking. The malformed case retains that same booking and adds `expected event-id strings`. The reverse-order pair does likewise, with the reported first/second place following the reversed input order. The current diff moves the unchanged actor/place/tick-guarded slot comparison/store before the malformed-list test; the malformed-list branch still continues before any member-wise dependency traversal.

I also made a temporary, uncommitted probe with a first-row mixed dependency list `['missing-dependency', null]`, followed by a valid row at a distinct place for the same actor/tick. It reported the malformed-list diagnostic and the later-row booking, but no unknown-dependency diagnostic for the string member. This is consistent with the declared list-wide skip policy. The temporary probe was outside the repository and removed.

Controls behave within the stated guard: `r21-same-place` reports only the malformed-list diagnostic; `r21-invalid-tick` retains both invalid-tick findings and the malformed-list diagnostic without a booking; `r21-wrong-kind-place` retains the wrong-kind and malformed-list diagnostics without a booking; `r21-ambiguous-actor` retains duplicate/ambiguous-actor and malformed-list diagnostics without a booking. No control shows relaxed actor/place/tick certainty. The executor's separate baseline replay reports 56/56 saved round-20 cases exact and no non-string dependency member among those inputs; my 64/64 replay is current-checker versus saved-current-output reproducibility, not an independent baseline-versus-current comparison.

## Axis judgment

- **Coverage: improved.** For the demonstrated input shape, a malformed dependency member no longer masks an otherwise independently definite booking under the existing occupancy rule. Both row orders and the listed certainty controls support this narrow claim.
- **Depth: unchanged.** No new entity/relation model, inference class, or richer semantic analysis was introduced.
- **Calibration: unchanged.** The preexisting unique-actor, unique known-place, nonnegative-tick gates remain intact, and malformed dependency members still produce an error and skip all dependency-member traversal. Evidence does not establish improvement or harm to source/canon calibration.
- **Harmed axes: none observed within this scope.** The 56-case baseline replay and current-output replay are bounded evidence, not proof for arbitrary inputs.

## Source and canon boundary

These are checker-input tests. IDs, locations, ticks, and descriptions in the fixture rows are not evidence that the events occurred, that a source text attests them, or that the fictional canon contains a contradiction. A structurally resolvable `source_id` is not source-text support. The booking is a checker finding under the project's existing same-actor/tick, distinct-known-place rule; it is not a canon ruling. The malformed member does not itself invalidate those independent fields, but this probe does not verify them against source text.

**Recommendation:** The evidence supports admitting this narrowly bounded coverage move, with depth and calibration unchanged and no scoped harm observed. Do not generalize the result to per-member recovery, other malformed structures, or canon truth.
