# Round 22 non-author reviewer — declaration / post-scout policy

## Scope and method

I did not edit checker source, fixtures, or shared docs. I reviewed the round-22 declaration and post-scout policy in `.shokunin/lore/LOG.md`, the checker diff from the current worktree, all eight raw round-22 transcripts under `corpus/live/runs/20261012T193930Z/`, the eight `r22-*` fixture inputs, and the round-22 corpus README / decision-table changes. I independently ran all 72 saved commands from that run directory against the current checker and compared each exit code and stdout with its saved transcript: **72/72 exact**. Saved outputs have no stderr in this corpus. This validates the saved outputs against the current checker; it is not a second baseline-version replay.

## Findings

The implementation matches the declared post-scout choice: one row-level `expected event-id strings` error is appended before member-level findings when any dependency member is non-string. The original list is then traversed in order, with non-strings skipped before the string-only self comparison, `seen_dependencies` membership/update, or ID lookup. Existing string diagnostic logic is otherwise unchanged. This avoids hashing JSON arrays/objects and avoids manufacturing per-member error counts. The source diff is small and leaves required-field screening and occupancy code unchanged.

Paired raw outputs support the narrow coverage claim. `r22-clean-inversion` reports the inversion; `r22-mixed-last` and `r22-mixed-first` each retain the same inversion and add the single malformed-list finding before it. `r22-multiple-invalid` skips null/object/array and still finds the string edge inversion. `r22-unknown-mixed` reports type then unknown; `r22-self-repeated` reports type then self and repeated findings in member order. `r22-valid-order` remains clean; `r22-malformed-only` reports only the list error. Diagnostic counts and order match the stated contract in these controls.

I separately tested an ambiguous event ID plus a malformed member: output retains the one list-level type error and the existing ambiguous dependency event finding. I also paired a negative dependent tick with a malformed member and string edge: it retains the invalid-tick and list-type errors without a timeline inversion, consistent with the prior nonnegative-endpoint gate. The 72/72 exact replay includes the prior `r21` occupancy controls and indicates no saved-output occupancy changes. No control suggests coercion or lookup of a malformed value.

The README and decision-table additions accurately bound the round-22 findings to input-level checks and do not assert source chronology, event truth, or canon. The round-21 decision-table statement that malformed lists make all member lookup unassessed is historically correct for that round; the later round-22 section explicitly supersedes it for string siblings. The docs could make that historical-to-current transition more explicit, but it does not create an inaccurate round-22 claim.

## Axis recommendation

- **Coverage: improved**, narrowly: a malformed sibling no longer suppresses separately inspectable string-member findings.
- **Depth: unchanged.** No new checker domain or source/canon evidence.
- **Calibration: unchanged** on the declared input-scoped contract: malformed entries remain diagnosed and unassessed, while string entries retain existing checks. This does not establish that interpreting strings beside a malformed list is appropriate beyond this stated checker policy.
- **Harmed: none observed** in the reviewed and replayed scope.

Recommend the round-22 move for admission only within this bounded scope. Do not characterize malformed edges as satisfied/absent, or checker tick/order findings as source-text chronology or canon. This is a reviewer recommendation, not the independent axis-adjudicator verdict; the 72 current-output replay alone is not a claim of independent baseline replay.
