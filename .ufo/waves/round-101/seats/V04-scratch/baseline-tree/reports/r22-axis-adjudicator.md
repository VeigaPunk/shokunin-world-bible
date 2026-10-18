# Round 22 — independent axis adjudication

## Verdict: admit the bounded coverage move

| Axis | Verdict | Reason |
|---|---|---|
| Depth | **Unchanged** | No new lore domain, source analysis, or canon fact is added. |
| Coverage | **Improved** | An inspectable string dependency beside a malformed member now receives its existing string-edge finding instead of being masked by the list-wide skip. |
| Calibration | **Unchanged** | The single existing malformed-list diagnostic remains first; malformed members are skipped, never coerced or assessed. String checks keep their prior guards and meaning as input-level findings. |

**None harmed within the tested scope.** The admission rule (at least one improved axis and none harmed) is met. This verdict does not authorize a next round; the operator requested a pause after round 22.

## Independent observations

I checked the round-22 declaration and post-scout policy in `LOG.md`, the checker diff against report commit `cc92ecee56fa771d7344df9e85e9c1ce2146be3a`, eight fixture inputs and saved transcripts in `corpus/live/runs/20261012T193930Z/`, plus the critic, executor, reviewer and independent-verifier reports. The checker diff is limited to binding `dependencies`, removing the malformed-list early `continue`, and skipping each non-string *before* self comparison, `seen_dependencies` hashing and event-ID lookup. The pre-scan still appends exactly one `timeline[1].depends_on: expected event-id strings` finding before any member finding. The occupied-slot code and required-field screening are untouched.

I independently reran all **72/72** current fixture commands and compared their exit code and stdout to the saved outputs: exact throughout. I also ran **64/64** prior fixture commands through the committed baseline checker extracted at `/tmp/r22-baseline-checker.py` (SHA-256 `6708bed3bb665093553c06aebcf7075d8cd6d6bbb3fb5406270643b7123ce000`) against their prior saved output, and the same 64 through the current checker: **64/64 exact exit code and stdout for each checker**. Their saved outputs contain no stderr; executor and non-author verifier separately report exact stderr replay and 319/319 old fixture JSON blobs byte-identical. Current checker SHA-256 is `8d5fa4e14f14156c93006ac9da42725216e45de4d1d5e275739197a66a59c226`. These are saved-input replays, not universal proof.

- `r22-clean-inversion` reports the tick-2 prerequisite versus tick-1 dependent inversion. `r22-mixed-last` and `r22-mixed-first` differ only in that dependency list (`["r20-prereq"]` versus `["r20-prereq", null]` and `[null, "r20-prereq"]`); each mixed case reports **type first, same inversion second**, two findings total. Baseline mixed probes in the critic report had only the type error. Position of `null` does not suppress the string edge or change diagnostic precedence.
- `r22-multiple-invalid` has `[null, {}, [], "r20-prereq"]`: one row-level error, then the inversion; array/object values do not reach unhashable set/dict operations. `r22-malformed-only` emits one type error and no invented edge; `r22-valid-order` remains clean.
- `r22-unknown-mixed` reports type then unknown event; `r22-self-repeated` reports type, self, existing self-edge inversion, self, repeated in the original string-member order. The repeated string is not independently resolved a second time. A temporary input combining object/array, unknown, self twice and the inverted prerequisite likewise yielded type first and string findings in list order.
- Additional temporary probes of the mixed fixture: duplicating prerequisite ID reports duplicate ID, type, then **ambiguous dependency event**, with no inversion of that ambiguous ID; setting either prerequisite or dependent tick negative reports invalid tick and type but **no inversion**; changing to valid prerequisite tick 0 retains the type error but no inversion. These reproduce the existing unique-resolution and nonnegative-endpoint guards. Reviewer and verifier independently exercised ambiguous and negative-endpoint probes as well.
- Occupancy logic is byte-unchanged in the checker diff. The 64 exact prior replays include round-21 clean/malformed and occupancy-certainty controls, and the 72 saved current outputs retain those cases. The verifier's equal-tick temporary probe retains an independent booking and adds only the string inversion; it is not an isolated occupancy pair because tick changed.

## Scope and limits

The previous round-21 statement that malformed lists skip *all* dependency members describes its historical behavior; the explicit round-22 sections in the fixture README and decision table supersede that behavior for string siblings. Every malformed value and any dependency it might denote remains unassessed. A reported ordering conflict is between checker input fields, not proof of source-text chronology, causality, event occurrence or canon. A citation ID alone attests none of those. Exact replay covers the 64 old and 72 saved current fixture invocations, plus the named temporary probes; it does not prove behavior for arbitrary JSON inputs or game mechanics. No push, merge, promotion or SHONEN checkmark follows from this verdict.
