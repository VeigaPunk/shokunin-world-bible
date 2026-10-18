.shokunin/lore — Round 22 test-scout report

## Raw observations

- Baseline checker was read from commit `cc92ece` (`.shokunin/lore/corpus/fixtures/check_bible.py`). I replayed all 64 fixture commands recorded in `corpus/live/runs/20261012T193022Z/*.txt` with that checker from the repository root. **64/64** exit codes and stdout matched the saved transcripts exactly; stderr was empty on all 64. The only repository change I made is this report.
- I inspected each corresponding fixture `timeline.json`. Across 140 event rows, all 140 `depends_on` values were lists. There are six malformed lists, all exactly `[null]`: rows `r21-event-1` in `r21-ambiguous-actor`, `r21-invalid-tick`, `r21-malformed`, `r21-malformed-reverse`, `r21-same-place`, and `r21-wrong-kind-place`. None contains a string member alongside its malformed member. The other 134 lists contain only strings (including empty lists).
- Therefore the replay set has malformed-member coverage, but no mixed valid-string/malformed-member case and no string edge whose inspection is currently masked by a malformed sibling. This inventory says nothing about inputs outside these saved fixtures.

## Recommendation (separate from observations)

The replay supports exact legacy output reproducibility and indicates the proposed traversal change has no changed-output precedent in the 64 saved inputs: the only malformed lists contain no string members to newly inspect. It does not establish safety for arbitrary mixed lists. Before implementing partial member traversal, use a controlled mixed-list probe such as `depends_on: ["later", null]` versus `["later"]` with a uniquely resolved later event and a clear inversion, plus an order-reversed equivalent. Preserve the malformed-member diagnostic and establish explicitly whether it is one list-level error or member-local errors; do not infer dependency satisfaction or fictional chronology from checker-input results.
