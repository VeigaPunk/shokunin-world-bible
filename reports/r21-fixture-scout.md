# Round 21 fixture scout — paired occupancy probes

## Raw observations

Baseline commit: `64d2673fb87ffb25396948840a991ee88472f8bf` (the checked-out checker). I copied the `consistent` fixture to temporary directories and replaced only each copy’s `timeline.json`. The two rows used the same uniquely identified actor `mira`, tick `7`, and distinct uniquely identified places `harbor` and `tower`; each row had a unique ID and a resolvable in-world source. Their descriptions were explicitly input-scoped: “Input row A/B: test booking only; not a canon assertion.” Both dependency lists were empty in the clean member of each pair. I invoked the fixture checker on each directory.

| Order | Second-row `depends_on` | Checker stdout finding | Exit |
|---|---|---|---|
| A (`harbor`), then B (`tower`) | `[]` | `timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'` | 1 |
| A, then B | `[null]` | `timeline[1].depends_on: expected event-id strings` only; no double-booking finding | 1 |
| B (`tower`), then A (`harbor`) | `[]` | `timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('tower') and 'harbor'` | 1 |
| B, then A | `[null]` | `timeline[0].depends_on: expected event-id strings` only; no double-booking finding | 1 |

Thus both input orders reproduce the masking: the malformed member suppresses occupancy at whichever row contains it, while the clean paired case reports the collision at the second row. Other output was the ordinary final “1 violation(s); no canon changed” line in each run. This is checker behavior on constructed input, not a statement that the fictional source records are true or that the events happened in-world.

## Recommendation (not an observation)

A minimal fixture pair should hold the two uniquely resolved actor/tick/place rows, IDs, citations, descriptions, and order fixed; vary only the target row’s dependency member from `[]` to `[null]`. To prove order independence, repeat that pair with the two rows reversed, keeping the malformed value attached to the same logical booking row. In every description use plainly input-scoped language, e.g. “Fixture input row for checker occupancy test; not a canon assertion.” Do not describe the output as proof of a real or canonical booking.

For a future checker change, the intended result is to retain the malformed-list finding while still evaluating independent occupancy, and to avoid iterating malformed dependency values. Keep the paired clean controls and both orders. A follow-on same-place control can check that the test detects differing-place occupancy rather than mere same-tick duplication, but it should not replace the minimal pair. This scout does not alter a checker, fixture, or shared documentation.
