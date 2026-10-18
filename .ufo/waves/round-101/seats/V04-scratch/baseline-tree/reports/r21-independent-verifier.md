# Round 21 independent verifier — malformed dependency list and occupancy

## Integrity and replay

- Baseline: report commit `64d2673fb87ffb25396948840a991ee88472f8bf` (the same `64d2673` recorded in the round declaration). I loaded the baseline checker using `git show` into `/tmp/r21-independent-baseline-checker.py`; no repository files outside this report were written.
- Enumerated the 279 `.json` fixture paths tracked at that commit with `git ls-tree -r`, then compared each baseline blob byte-for-byte against the current worktree file. **279/279 present and identical; 0 missing, 0 changed.** This establishes fixture JSON integrity relative to the requested baseline, not integrity of non-JSON files.
- Replayed all **56** paths in `corpus/live/runs/20261012T191902Z/` through both baseline and current checkers. Baseline `(exit code, stdout, stderr)` matched each saved transcript exactly **56/56**; current checker matched baseline on all **56/56**. The 56 inputs contain no list-valued `depends_on` with a non-string member, so this is a regression replay, not coverage of the changed malformed-list branch.
- Replayed every one of the **64** saved run transcripts in `corpus/live/runs/20261012T193022Z/` against the current checker. `(exit code, stdout, stderr)` matched **64/64** exactly.

## Paired fields and controls

I inspected and ran the current checker on all eight committed `r21-*` fixture directories. The `r21-clean` / `r21-malformed` pair differs only at `timeline[1].depends_on` (`[]` vs `[null]`); both report the same known-place booking, while the malformed case retains `expected event-id strings`. The reversed pair also differs only in that field and retains the booking with the reversed place order. All CLI runs exited 1 with empty stderr.

| Fixture | Observed relevant findings |
|---|---|
| `r21-clean` | Double booking: `mira`, tick 9, `tower` / `harbor`. |
| `r21-malformed` | Same booking plus `timeline[1].depends_on: expected event-id strings`. |
| `r21-clean-reverse` | Double booking: `mira`, tick 9, `harbor` / `tower`. |
| `r21-malformed-reverse` | Same reversed booking plus malformed-list diagnostic. |
| `r21-same-place` | Malformed-list diagnostic; no booking. |
| `r21-invalid-tick` | Both negative-tick findings and malformed-list diagnostic; no booking. |
| `r21-wrong-kind-place` | Not-a-place finding and malformed-list diagnostic; no booking. |
| `r21-ambiguous-actor` | Duplicate/ambiguous actor findings and malformed-list diagnostic; no booking. |

Two additional temporary `/tmp` probes tested order and list-wide semantics. With `[null]` on the **first** row followed by the otherwise-valid second row, output retained the malformed-list diagnostic and reported the booking on row 1. With `["r21-event-1", null]` on the first row (mixed valid and malformed members), output likewise reported the malformed-list diagnostic and booking, but no dependency inversion diagnostic. This is consistent with list-wide skip: occupancy proceeds independently; dependency-member traversal is skipped for the entire malformed list. Temporary probes were not retained in the repository.

## Assessment and limits

The raw observations support the declared narrow result: malformed dependency-member validation no longer suppresses an otherwise-eligible occupied-slot finding; the malformed-list diagnostic remains, and the tested same-place / invalid-tick / wrong-kind-place / ambiguous-actor controls do not gain a booking. Existing valid dependency-list behavior is supported by exact 56-case regression replay, but those old fixtures do not contain malformed list members. Mixed-list probing confirms all-member skip, not per-member recovery; no claim is made that valid members in a malformed list are individually diagnosed.

This tests the checker against fixture input only. It does not establish that any fictional event, actor, place, or timeline field is true, source-attested, or canon. Findings are checker contradictions, not real-world or in-world verification. Coverage is improved for one masked finding class; depth and calibration appear unchanged within these probes. No broad malformed-input behavior or exhaustive arbitrary input space was assessed.
