# Round 21 citation scout — fixture input, occupancy, and source truth

## Scope and evidence

Read-only scout of `.shokunin/lore/corpus/fixtures/check_bible.py`, its README, and a paired temporary probe made by copying `consistent/` outside the repository. No repository fixture, checker, shared document, or canon was changed. The two probe inputs differed only in the second event’s `depends_on` value (`[]` versus `[null]`); both had two rows with actor `mira`, tick `1`, and distinct existing place IDs `harbor` and `tower`. The descriptions were explicitly labeled as checker test data, not as statements from a fictional source.

## Raw observations (not recommendations)

- With `depends_on: []`, the checker reported `timeline[1]: double-booked 'mira' at tick 1 in timeline[0] ('harbor') and 'tower'`.
- With `depends_on: [null]`, the checker reported `timeline[1].depends_on: expected event-id strings` and did **not** report the otherwise same occupancy finding. Both CLI runs exited 1. The malformed member triggers `continue` before the occupancy check, as the checker control flow predicts.
- The paired inputs establish behavior for those supplied rows and IDs only. The actor/place/tick values, dependency list, and descriptions were test inputs. The source IDs inherited from the copied fixture resolve structurally, but the checker does not dereference fictional source text to establish whether Mira was at either place, whether the two events occurred, or whether they share a real in-world tick. CLI wording that no canon changed likewise does not verify canon.
- README framing describes local fictional sequence and occupancy conventions; it is project documentation, not a cited source passage attesting either probe row. Structural source-ID resolution is not text support or a canon ruling.

## Recommendations (separate from observations)

- Treat this as a potential checker coverage gap only: an invalid dependency member currently masks a separate occupancy finding in this paired input. Any proposed repair/evaluation should preserve the dependency-list diagnostic and avoid iterating unsafe members, while separately testing independently known actor/tick/place occupancy.
- Keep fixture descriptions and reports scoped to checker inputs and outputs. Do not describe the rows as events established by `courier-log` or any source; do not infer that a valid-looking citation proves place, tick, event occurrence, dependency satisfaction, or contradiction in canon.
- Keep the paired occupancy claim conditional on unique, resolvable actor and place IDs and a nonnegative tick, as exercised here. Broader malformed-input behavior, other slot controls, and any source-text/canon review require separate evidence.

This is a scout report, not an implementation proposal, axis verdict, or round-admission decision.
