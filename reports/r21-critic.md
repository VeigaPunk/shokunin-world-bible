# Round 21 critic — independent occupancy certainty and masking

## Raw observations (baseline checker at `64d2673`)

I copied the existing `r20-valid-order` fixture to temporary directories, changed only the second timeline row to tick `0` (same as the first row), and compared `depends_on: []` with `depends_on: [null]`. Running `check_bible.py` directly:

- Empty dependency list: exit 1; reports `timeline[1]: double-booked 'mira' at tick 0 in timeline[0] ('tower') and 'harbor'`.
- `[null]`: exit 1; reports only `timeline[1].depends_on: expected event-id strings`; the same booking is masked.

Both rows have the same uniquely indexed actor `mira`, uniquely indexed place IDs `tower` / `harbor` (both kind `place`), and nonnegative equal ticks. The malformed value does not alter those occupancy facts. This confirms the proposed coverage gap for this fixture pattern; it is not evidence about any in-world event.

I also reversed the two rows and assigned `[null]` to whichever row was being tested. With malformed row first, its early `continue` skips slot insertion, so the later otherwise-valid row yields no booking either. With malformed row second, the first row inserts the slot, but the malformed row's early `continue` skips comparison. Thus list order does not rescue coverage; both orderings mask the distinct-place same-slot conflict.

## Falsification / independent-certainty assessment

I do not find a counterexample to the narrow claim: dependency-member validity is independent of the actor/tick/place evidence used by this occupancy rule. `depends_on` is already screened as a list at required-field validation. A non-string list member triggers an error and should prevent unsafe member-wise dependency processing, but need not invalidate the other fields. A check/store of occupancy before the malformed-dependency `continue` can preserve the dependency diagnostic while exposing the booking. It should retain the existing actor uniqueness, known-place-kind and nonnegative-tick gates unchanged; do not relax them or infer occupancy from ambiguous/dangling/non-place IDs or negative ticks.

One side effect to guard: slot insertion is order-sensitive and retains the first place. With multiple rows in the same actor/tick slot, preserve current behavior for valid rows: report each later different-place row against the retained first row; same-place rows do not replace it. A malformed-dependency row that passes the independent occupancy gates should participate in the same comparison/store sequence, whether it appears first or later. Continue skipping dependency-member resolution for that row. This does not establish that any row is true; it identifies an input-level conflict under existing checker semantics.

## Recommendation (not raw evidence)

The declared one-axis move appears supportable as **coverage**, narrowly for malformed dependency member(s) masking otherwise-definite known-place occupancy. Keep it conditional on regression evidence: replay all 56 saved round-20 outputs and inventory any changed output; test both row orders, same-place control, actor/place ambiguity and invalid tick guards, and ensure malformed dependency members still produce their diagnostic without member lookups. If those gates pass, recommend coverage improved, depth unchanged, calibration unchanged (no weakened certainty guard); otherwise report the exact regression and do not admit. I did not edit checker, fixture, shared docs, or commit. I did not independently replay the 56-output corpus.
