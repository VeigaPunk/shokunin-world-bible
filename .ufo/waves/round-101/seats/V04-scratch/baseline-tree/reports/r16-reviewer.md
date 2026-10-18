# Round 16 independent reviewer — unresolved-place occupancy

## Scope and method

Reviewed the working checker diff, all four raw `r16-*` fixtures, the corpus and fixture READMEs, the 2026-10-12 decision table, and the round-16 LOG declaration/clarification. No source files were changed. Replayed every fixture with the documented CLI:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<case>
```

All **33/33** raw fixture runs matched `corpus/live/runs/20261012T182817Z/<case>.txt` on exact exit code and stdout (excluding the capture wrapper). This includes the 29 prior fixtures and four r16 fixtures. I also used disposable copies of `r12-unique-actor` to probe adjacent wrong-kind, duplicate-place, and missing-actor cases; no probe files remain.

## Change and principal result

The source diff is one condition at `check_bible.py` occupancy insertion/comparison: `if actor_id_count == 1:` becomes `if actor_id_count == 1 and place_id_count != 0:`. The earlier timeline validation still emits `dangling entity` for a zero-count place ID. So a row with a missing place is neither compared nor stored in the actor/tick `occupied` slot; uniquely identified actors and all other nonzero place-ID counts retain the existing behavior.

Raw output from the four fixtures:

- `r16-valid-places`: `timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'`; exit 1.
- `r16-missing-place`: only `timeline[1].place_id: dangling entity 'unlisted'`; exit 1, no double-booking assertion.
- `r16-missing-first`: only `timeline[0].place_id: dangling entity 'unlisted'`; exit 1, no double-booking assertion.
- `r16-mixed-three`: dangling for `timeline[1].place_id`, plus `timeline[2]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'`; exit 1.

This confirms symmetry across missing-first/missing-second and that skipping the unresolved middle row does not mask the supported known-harbor/known-tower conflict. The four fixtures share the same entity rows; `missing-place` changes the second row's place ID from `tower` to `unlisted`, `missing-first` puts `unlisted` first, and `mixed-three` retains known `harbor` and `tower` rows around the missing row.

The declared uncertainty distinction is sound: a zero-match ID does not support a *definite different resolved places* inference. Its actual intended location could be the same as a known place, another place, or no valid place. Suppression does **not** establish same-place occupancy or absence of conflict. The retained dangling diagnostic is essential and is present. The known-known pair still asserts conflict. I find the narrow move directionally improves calibration and reduces unsupported conflict noise without changing the known pair result.

## Hidden conflict and noise limits

This guard is deliberately narrower than “only resolved places participate.” I reproduced the out-of-scope behavior using disposable copies:

- Set the second `place_id` to the unique character ID `mira`: checker reports `not a place 'mira'` **and** a `double-booked` finding for `'harbor'` and `'mira'`.
- Add a duplicate `harbor` entity while retaining `harbor`/`tower`: checker reports duplicate ID and ambiguous place, and still reports double-booked.
- Set both actors to absent `absent-actor`: checker emits two dangling-actor diagnostics and no double-booking, as actor count is zero.

These are real residual unsupported occupancy assertions, but the README and decision table correctly say duplicate and wrong-kind IDs retain old raw-ID occupancy behavior and are outside this round. Do not describe the checker as generally verifying locations or definite occupancy. Similarly, two distinct absent place keys would still yield two dangling findings and (with this guard) no occupancy assertion; the possible conflict remains unassessed. The current one-entry-per-slot comparison remains simple and order-dependent in its diagnostic wording, though the three-event order selected here correctly retains the known pair. No evidence here supports general pairwise-comparison behavior beyond these cases.

One fixture-content noise: `r16-missing-place/timeline.json` gives its `unlisted` row the description “A separate record places Mira at North Tower,” and `r16-missing-first` gives its missing `unlisted` row “A record places Mira at Lantern Harbor.” These human-readable descriptions point toward known locations even while the machine ID is dangling. The docs appropriately say descriptions/source IDs do not resolve a location, and the checker does not read descriptions; still, the mismatch weakens the fixture as an intuitive uncertainty example and invites a reader to silently infer the missing target. Treat the absent ID as unresolved for the checker result and do not use those descriptions as resolution evidence.

## Docs and LOG consistency

The fixture README describes the four input shapes and correctly says the missing row cannot participate, while the known pair still double-books. It explicitly states suppression is not proof of no conflict and preserves out-of-scope duplicate/non-place behavior. The decision-table entry makes the same narrow limitation explicit. Corpus README fixture inventory and run-directory references include r16. The LOG claim/clarification correctly distinguishes the zero-match case, records the before-state baseline, and says not to claim general resolved-place occupancy. I found no documentation claim that the guard resolves source truth or canon.

The limitations that matter for later work are: duplicate place IDs and unique wrong-kind entities can still feed raw string comparisons; malformed descriptions can imply a location contrary to the unresolved ID; and suppressed comparisons leave actual conflict status unknown. Keep all three visible if this is admitted.

## Verdict

**Calibration: improved, narrowly. Coverage: unchanged. Depth: unchanged.** No axis harmed by the implementation/documentation under review. The calibration gain is withholding a false-certainty assertion only for count-zero place IDs while preserving both the dangling finding and a known-known conflict. It does not establish general correct occupancy handling: duplicate/wrong-kind residual noise is explicitly out of scope, and an unresolved event may conceal a real conflict. Admit only with that narrow statement and preserve the residuals above for follow-up; no source-text or canon conclusion is warranted.
