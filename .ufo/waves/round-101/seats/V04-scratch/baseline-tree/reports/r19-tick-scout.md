# Round 19 tick scout — raw schema and CLI observations

## Raw observations

- `FIELDS['timeline']['tick']` requires `int`, checked using `type(value) is expected`; thus booleans and non-integers are rejected before entering `data['timeline']`. A negative integer passes that field/type screen.
- The timeline pass emits `timeline[i].tick: must be nonnegative` for negative values. It does not invalidate/remove the row. The occupancy guard currently requires exactly one indexed actor and one indexed place of kind `place`; its slot is `(entity_id, tick)`, and it compares/stores the row without checking tick validity. Later dependency processing also continues for the negative-tick row.
- Raw probes used temporary copies of `corpus/fixtures/r18-unique-pair`, changing only both event ticks (and JSON formatting): one directory set tick to `-1`, the other to `0`. Both retain unique actor `mira`, known places `tower`/`harbor`, and two events; no repo fixture was edited.
- CLI command for each: `python .shokunin/lore/corpus/fixtures/check_bible.py <temporary-bible-directory>`.
- Negative (`-1`) stdout:
  ```
  VIOLATION: timeline[0].tick: must be nonnegative
  VIOLATION: timeline[1].tick: must be nonnegative
  VIOLATION: timeline[1]: double-booked 'mira' at tick -1 in timeline[0] ('tower') and 'harbor'
  3 violation(s); no canon changed
  ```
  Exit status 1.
- Zero (`0`) stdout:
  ```
  VIOLATION: timeline[1]: double-booked 'mira' at tick 0 in timeline[0] ('tower') and 'harbor'
  1 violation(s); no canon changed
  ```
  Exit status 1. This is the nonnegative positive collision control.

## Recommendations (not implementation)

- If the round's narrow claim is pursued, skip only occupancy compare/store for negative ticks, leaving their diagnostics and raw rows intact. Do not change the tick schema or infer that such an event is impossible or conflict-free.
- Keep a paired zero-tick control and valid known-known pair before/between/after negative rows to check valid occupancy is preserved. The pair here shows negative-only tick findings alongside an unsupported-by-domain occupancy assertion; the zero control retains the expected occupancy diagnostic.
- No claim about source text, canon, or actual locations is supported by these fixture-input probes. No implementation or fixtures were changed by this scout.
