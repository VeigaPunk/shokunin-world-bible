.shokunin/lore — Round 21 control-flow scout

## Scope and raw observation

I inspected baseline checker `64d2673fb87ffb25396948840a991ee88472f8bf` and ran its CLI from the current checkout (HEAD at probe: same baseline) on two temporary, input-identical bible directories. Both begin from `corpus/fixtures/consistent`; I changed the timeline to two rows with the same actor `mira`, tick `1`, and distinct known places `harbor` and `tower`. The only difference between the two JSON inputs is the second event's `depends_on` value: `[]` versus `[null]`. These are temporary `/tmp` probe inputs, not canon or committed fixtures.

**Raw CLI, `depends_on: []`:**
```text
VIOLATION: timeline[1]: double-booked 'mira' at tick 1 in timeline[0] ('harbor') and 'tower'
1 violation(s); no canon changed
EXIT:1
```

**Raw CLI, `depends_on: [null]`:**
```text
VIOLATION: timeline[1].depends_on: expected event-id strings
1 violation(s); no canon changed
EXIT:1
```

The occupancy finding disappears in the malformed-list case, while the malformed-list diagnostic appears. The pair differs only in that dependency member. Both rows otherwise satisfy the relevant definite-occupancy conditions: actor ID resolves uniquely; both place IDs resolve uniquely to `place` entities; tick is nonnegative; slot is same actor/tick and place differs.

## Control-flow map (baseline source)

Within the timeline-row loop (`check_bible.py`, around the occupied-slot block):

1. Entity and source checks run; negative ticks are diagnosed.
2. `if not all(isinstance(dep, str) for dep in row['depends_on']):` emits `expected event-id strings` and immediately `continue`s the outer timeline-row loop.
3. Only after that branch does the checker compute `comparable_place`, apply unique-actor / unique-known-place / nonnegative-tick guards, and inspect/update `occupied` for a double-booking.
4. The per-member dependency diagnostic/order loop follows occupancy.

Thus this exact early `continue` skips both independent occupancy analysis and dependency member lookup. The `[null]` case correctly cannot safely run string-ID lookup over every member, but that need not preclude the independent occupancy check.

## Recommendation (not an observed result)

Keep the malformed dependency-list diagnostic and avoid member-wise dependency lookup when any member is non-string, but do not let that validation branch skip independent occupancy analysis. A small control-flow adjustment could evaluate the guarded occupancy block before malformed-dependency handling, then skip only the dependency traversal for malformed lists. Preserve existing occupancy certainty guards and leave dependency semantics unchanged. This probe supports the candidate as an independent missing finding; it does not establish fictional-world truth, nor does it assess other malformed inputs or legacy-output replay.
