# Round 12 critic — duplicate actor IDs and occupancy

## Observed raw paths and CLI output

I replayed the active checker at `.shokunin/lore/corpus/fixtures/check_bible.py` against temporary copies of the `consistent/` fixture. The probes are under `/tmp/lore-r12-o7m_t4ea/` (duplicate-ID case) and `/tmp/lore-r12-unique-net27xy4/` (unique-ID control); these paths are scratch, not committed artifacts.

The duplicate-ID probe retained the valid `mira` character row, appended a second schema-valid entity row also named `mira`, and used two distinct timeline event rows (`event-a`, `event-b`) for `mira`, both tick 5, at `harbor` and `tower`. CLI stdout:

```text
VIOLATION: entities[4].id: duplicate entities id 'mira'
VIOLATION: timeline[1]: double-booked 'mira' at tick 5 in timeline[0] ('harbor') and 'tower'
2 violation(s); no canon changed
```

Exit 1; stderr empty. Thus the claimed observable behavior is reproducible: duplicate valid rows do not prevent a `double-booked` result. The unique-ID probe used the same two event rows but only the original unique `mira` entity. CLI stdout:

```text
VIOLATION: timeline[1]: double-booked 'mira' at tick 5 in timeline[0] ('harbor') and 'tower'
1 violation(s); no canon changed
```

Exit 1; stderr empty. This confirms the unique-actor control still detects the collision. Both probes' event rows are distinct IDs, so duplicate event IDs are not responsible. These probes do not establish what either repeated entity row means in-world.

## Critique / falsification

The premise is **partly supported, not established as a safe removal rule**. The raw observation establishes a duplicate entity ID and two different places assigned to that ID at one tick. It does not establish that the rows denote two different actors. They may be two competing descriptions/records of one actor, in which case the existing occupancy conflict could be a true finding. Or they may represent two distinct actors whose IDs collide, in which case calling them one person is unwarranted. Schema validity is only field-shape validity; citations likewise do not decide identity. Distinct timeline event rows prove distinct input records, not distinct actors or independent witnesses.

Therefore simply skipping occupancy whenever an actor ID is duplicated risks deleting a true contradiction, while retaining an unqualified `double-booked` finding risks false identity attribution. The calibration problem is the certainty and label of the inference, not a demonstrated false positive in every duplicated-ID case. A local ambiguity diagnostic could itself add noise if it is repeated once per event, or if a generic duplicate-ID finding already adequately identifies the malformed input. The premise also relies on duplicate *schema-valid* entity rows; invalid entity rows are excluded from `data['entities']` and should not silently count as identity candidates.

## Recommendations (not observed behavior)

- Avoid stating that ambiguous actor references prove two people or that occupancy is impossible. Phrase any proposed behavior as “identity unresolved; do not assert a definite actor-level collision from this ID,” not as a conclusion about canon.
- Before suppressing the existing finding, test/consider both materially plausible readings of the same duplicate-ID input: duplicate rows for one actor (where the collision may remain real) and ID collision across actors (where it may be spurious). The current schema has no discriminator that can resolve these readings; neither interpretation should be silently selected.
- If the axis move is retained, document whether the old `double-booked` assertion is removed, weakened/reclassified, or accompanied by an indeterminate result. Preserve raw event rows, the duplicate-ID finding, and the unique-ID control. Do not claim this one rule resolves actor identity generally.
- Keep tests narrowly scoped: same-tick/different-place is the decision case; same-tick/same-place should not become a collision merely due to duplicate actor rows; unique actor remains detected; dangling/malformed actor references and earlier fixtures should not gain unrelated changes. A probe pair can test row order, but row-order invariance alone cannot establish which semantic identity interpretation is correct.

No checker, fixture, or shared documentation was changed for this critique.
