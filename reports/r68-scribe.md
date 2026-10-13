# Round 68 scribe: README wording proposal

## Suggested addition to `.shokunin/lore/corpus/fixtures/README.md`

> **Dependency identifiers are input strings, not evidence of events.** Each `timeline[*].depends_on` member must be a nonempty event-ID string. A blank or whitespace-only member is malformed input; it must not be described as proof that an event is absent. A nonempty ID with no uniquely matching timeline row is an unknown-event reference. When IDs resolve uniquely and both ticks are nonnegative, the checker applies its existing strict-earlier ordering rule. These checks concern the supplied fictional JSON and the fixture's local tick convention only. They do not establish that a referenced event occurred, that a dependency is true in the story, or what is canon. The checker does not read source prose or choose canon.

Keep this short and near the existing dependency/tick explanation in the fixture README. If round 68 lands, add its exact fixture names and observed outcomes only after the matched cases and independent replay are available; do not imply the proposed behavior is already active.

## Evidence and limits

- `.shokunin/lore/LOG.md`, Round 68 declaration, states the baseline precisely: `check_bible.py` accepts any `str` dependency member, so empty/whitespace values take the unknown-event path. It proposes a field-local required-nonempty-string diagnosis and explicitly makes the improvement conditional on matched empty, whitespace, nonempty-unknown controls and independent replay.
- `.shokunin/lore/corpus/fixtures/check_bible.py:295-316` reports one row-level `expected event-id strings` only if a member is not a string; it then iterates strings, and a zero-count ID gets `unknown event`. There is currently no nonempty test at this dependency site.
- The existing README already says that `tick` is a nonnegative integer in an invented world's local sequence and dependencies must have strictly earlier ticks; it also says a contradiction is for editorial review, not for the checker to choose canon. The suggested paragraph extends those boundaries without making source-text or story-truth claims.
- `.shokunin/lore/corpus/fixtures/r20-negative-dependent/timeline.json` and `r20-negative-prereq/timeline.json` mark their values as fixture input and disclaim source-text chronology; `.shokunin/lore/corpus/fixtures/r22-clean-inversion/timeline.json` provides a nonempty inversion control. They support the fictional-input framing, but are not round-68 matched blank/whitespace controls.
- No `r68-*` fixtures are present in `.shokunin/lore/corpus/fixtures/` at this inspection. I did not run or claim candidate behavior, matched outcomes, regression preservation, or independent validation. This is a prose recommendation only, not a canon claim or an assertion that checker behavior changed.
