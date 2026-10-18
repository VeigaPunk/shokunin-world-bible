# Round 16 critic — missing-place occupancy tradeoff

## Observed evidence and assessment

The concern is real, but “skip occupancy” is defensible only as a narrow calibration rule, not as a claim that no conflict exists. In `.shokunin/lore/corpus/fixtures/check_bible.py`, the timeline loop emits a dangling finding for a missing `place_id`, then independently compares raw `(entity_id, tick)` slot values: if another place-ID string differs, it prints `double-booked`. It does not establish that either value resolves to a place before making that assertion.

Raw CLI reproductions:

- `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r11-dangling-place` reports `timeline[0].place_id: dangling entity 'unlisted'` and exits 1. The fixture’s second Mira event is at tick 2, so it does not exercise same-tick pairing.
- `... r12-unique-actor` reports a double-booked Mira at tick 7 in `harbor` and `tower`; both IDs resolve uniquely to places. This is the important positive control and must remain.
- `... r13-unique-actor` likewise reports the same resolved-place conflict.
- `... r11-unique-nonplace` reports `place_id: not a place 'mira'`; duplicate-ID `r11-place-character` and `r11-character-place` report an ambiguous place. Thus “entity exists” is not equivalent to “resolved place.”
- `... r13-missing-actor` emits only dangling actor findings and no occupancy result, showing actor identity already gates this comparison; it does not establish whether location gating is useful.

The most direct failure mode is a same-tick pair for one uniquely identified actor, one row at a valid place and one row with a missing ID: current raw-string comparison can label them “double-booked.” That is overconfident: the dangling value might ultimately refer to the same place, a different place, or no real place at all. Withholding the *definite different-resolved-place* assertion for that pair reduces false-positive certainty/noise while retaining the dangling diagnostic and raw event.

But withholding is not discovery of truth. The missing reference could conceal a genuine conflict (the unknown place may differ from the valid one), and two missing IDs could also refer to distinct places. So this is a deliberate reduction in both unsupported assertions and conflict detection in malformed inputs. The output must not imply “no conflict,” “same place,” or successful validation. Keep the dangling finding prominent; do not discard the raw event or silently substitute a place.

## Ambiguity / noise cautions

- Gate pairwise conclusions on both place IDs being uniquely resolved entities of kind `place`, not merely different strings or IDs present in the entity index. A unique character/item ID is currently separately diagnosed as “not a place”; duplicate IDs are ambiguous even though `index()` retains one row internally. A broader change that treats these as definite places would retain noise.
- Apply the gate per pair, not as a blanket skip of the actor/tick slot. If three events share a slot (known Harbor, known Tower, missing ID), the Harbor/Tower pair still supports a definite conflict and should still be reported. The missing row should not suppress that independent finding.
- Avoid inventing claims from dangling IDs. If an unresolved row is paired with a resolved row, report the reference defect, but no double-booking conclusion for that pair. If all rows are unresolved, there is likewise no place-based conclusion; only reference defects are evidenced.
- The positive control is essential: the clean, uniquely resolved `harbor`/`tower` pair at the same tick must continue to produce a conflict. Existing `r12-unique-actor` and `r13-unique-actor` are raw CLI controls.

## Recommendations (not edits)

1. Narrowly suppress only an occupancy assertion whose pair includes a `place_id` with zero matching valid entity rows; retain dangling-place output. Require both pair members to have exactly one matching entity row and `kind == 'place'` before calling different IDs a definite different-place conflict. Treat the broader ambiguous/non-place policy as an explicit scope decision, since those already have their own diagnostics.
2. Make the occupancy comparison pairwise (or equivalent) so an unresolved row cannot overwrite or mask a later known-place pair in the same actor/tick slot.
3. Add a same-tick paired fixture with one valid place and one missing place. Expected: dangling finding, no pairwise definite double-booked finding. Add/retain a valid two-place positive control, plus a three-row control (two valid distinct places and one missing ID) to prove the unknown row does not mask the supported conflict.
4. Describe the rule as uncertainty/calibration (“not enough resolved place evidence for this pair”), not as resolving or ignoring the underlying conflict. Keep existing checker contract that it reports violations and does not change canon.
