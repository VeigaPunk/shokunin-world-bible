.shokunin/lore — Round 21 test-scout report

## Raw observations

- Baseline: commit `64d2673fb87ffb25396948840a991ee88472f8bf`; baseline checker loaded with `git show` into `/tmp/r21-baseline-checker.py`. I replayed each of the 56 fixture paths recorded in `corpus/live/runs/20261012T191902Z/*.txt` using that checker and compared exit status plus stdout with the saved transcript. All **56/56** matched exactly (including clean/error cases).
- I inspected all 56 corresponding `timeline.json` inputs for list-valued `depends_on` fields containing any non-string member. **None** of those 56 inputs contains such a member. Thus no saved baseline case exercises this malformed-list branch, and no legacy output is predicted to change by the proposed adjustment on these inputs. This is not evidence for arbitrary unsaved inputs.
- The replay script came from the baseline commit rather than the current working checker, so the comparison is baseline-output reproducibility, not a baseline-versus-modified-checker comparison. I made no source, fixture, or shared-document changes.

## Recommendation (separate from observations)

For new behavior, preserve the malformed `depends_on` diagnostic and avoid iterating malformed members, while still running the independent guarded occupancy analysis. The paired probe in `r21-control-scout.md` reports a lost known-place booking when `[null]` replaces `[]`; my replay did not independently reproduce that probe. Keep the existing certainty guards (unique actor, uniquely resolved place entity of kind `place`, nonnegative tick) and valid dependency behavior. Treat the additional checker finding as input analysis only, not proof of fictional canon. Since none of the 56 saved cases is malformed-list coverage, a separate changed-output regression comparison is still needed after any implementation.
