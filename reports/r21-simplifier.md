# Round 21 simplifier — control-flow recommendation

## Raw observations

- The round-21 declaration in `.shokunin/lore/LOG.md` describes the candidate: a non-string member in a list-valued `depends_on` triggers a diagnostic and an early `continue` before occupancy checking.
- Source inspection of `corpus/fixtures/check_bible.py` confirms this order. The timeline required-field screen checks that `depends_on` is a `list`, not that every member is a string. In the event loop, `all(isinstance(dep, str) ...)` detects malformed members; its error branch appends `expected event-id strings` and immediately continues. Occupancy checks follow that branch; member-wise dependency lookup follows occupancy.
- The early exit therefore bypasses occupancy for that row. Source inspection alone does not establish the paired runtime output or whether any of the saved 56 cases changes. No CLI probes or replay were run for this report.

## Recommendation (not an observed result)

Keep the type diagnostic and skip dependency iteration for malformed members, but do not skip the independent occupancy check. The smallest clear control-flow change is to compute a `dependencies_valid` boolean once; append the existing diagnostic when false, then run the existing occupancy block normally, and guard the existing `seen_dependencies` / per-member dependency loop with `if dependencies_valid:`. Leave all guards and bodies inside occupancy and the valid dependency path unchanged. In particular, do not coerce/filter malformed members, and do not iterate them into the set-based lookup path.

This should allow a uniquely resolved actor at a nonnegative tick and a uniquely resolved place to retain the existing booking comparison/store despite an invalid dependency member, while preserving the malformed-list diagnostic. It should not change dependency findings for valid string lists. These are intended effects requiring paired CLI and regression verification, not established findings here. A malformed input or a checker report is not evidence about canon or event truth.
