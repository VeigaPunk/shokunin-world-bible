# Round 22 scribe draft — malformed dependency members

**Status:** documentation proposal only. This report does not amend the fixture README or decision table, and it is not evidence that the proposed behavior is safe or admitted.

## Raw observation (baseline source, not recommendation)

In `corpus/fixtures/check_bible.py`, timeline rows are screened before dependency traversal. If any `depends_on` member is not a string, the checker emits one row-level `expected event-id strings` diagnostic and `continue`s. Therefore no string member in that row reaches the existing self/repeated/unknown/ambiguous/inversion checks. The checker does not currently distinguish which member is malformed in its diagnostic. This is a control-flow observation, not yet a paired CLI result and not evidence that partial recovery is correct.

Round 22's declaration identifies the candidate masked case as a mixed list such as `["later", null]` where `later` is independently inspectable and inverts. Its expected paired clean input is `["later"]`. The paired outputs, order controls, and the 64 prior-output replay remain evidence gates, not completed results in this draft.

## Proposed bounded decision table (only if the declared move is implemented and verified)

| Input condition | Candidate diagnostic / handling | What must remain unclaimed |
|---|---|---|
| Every dependency member is a string | Preserve existing member traversal and its self, repeated, unknown, ambiguous, and timeline-inversion behavior. | No change to dependency semantics or chronology beyond the declared test cases. |
| One or more members are non-strings, while other members are strings | Keep the existing list-level malformed-member diagnostic; inspect only string members using existing per-member rules; never coerce or look up a non-string member. | Do not call the malformed member satisfied, absent, or an event ID. Do not silently resolve any canon conflict. |
| A malformed member coexists with an inspectable string edge that inverts | Candidate output retains the malformed-member finding and reports the same inversion as the clean-string paired case. | Checker-input ticks and IDs do not establish source-text chronology, causality, or canon. |

**Diagnostic wording/count is deliberately unresolved here.** The candidate table preserves the currently declared list-level diagnostic; do not add per-member errors or silently change diagnostic count unless the orchestrator records a revised, evidence-backed decision before implementation.

## Evidence gates before promoting this text to user-facing docs

1. Capture baseline raw CLI outputs for the paired clean and mixed inputs (plus relevant order controls); verify the mixed string edge is currently masked and the clean case reports the existing inversion. Record command, stdout, and exit status.
2. Before implementation, settle diagnostic policy and the minimal safe per-member behavior. In particular, establish that malformed values are never hashed, compared, or used as IDs, and that duplicate-string behavior remains consistent with the existing `seen_dependencies` logic.
3. Replay all 64 prior fixture stdout/stderr/exit results against baseline and current versions. Confirm no mixed dependency lists exist among the old fixtures; if any output changes, inventory and adjudicate it rather than claiming exact preservation.
4. Use paired fixtures differing only by the malformed member, plus reversed row order and cases covering repeated/self/unknown/ambiguous string members. Require the clean and mixed forms to preserve the same finding for each inspectable string edge, with the mixed form additionally retaining the malformed-member diagnostic.
5. Obtain non-author reviewer and verifier replay from raw artifacts, then independent axis adjudication. Admit only if coverage improves and no axis is harmed; otherwise leave the round unadmitted and report the result honestly.

This proposal concerns checker handling of fixture input only. It does not verify game mechanics, infer real-world rights, or validate any source-text or canon claim.
