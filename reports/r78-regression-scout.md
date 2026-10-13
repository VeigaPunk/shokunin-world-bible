# Round 78 regression scout — pinned corpus archive and replay gate

## Scope and pin

Report-only regression scout. I read the active Round 78 LOG declaration, `.shokunin/lore/corpus/fixtures/README.md`, the active `check_bible.py`, and prior r3/r7/r39/r62/r63 and r77 regression/prior reports. The baseline is `dd47e67387b05705e819e04c4176eb07ad0fb00d`; `git rev-parse HEAD` matches. The worktree already has a modification to `.shokunin/lore/LOG.md`, which I did not edit. I made no checker, fixture, README, or other repository edits; this report is the only repository file written.

I archived the pinned corpus with `git archive` to `/tmp/lore-r78-pin/.shokunin/lore/corpus`. The archived corpus has **1,356 files**; its pinned checker SHA-256 is `88c9b1d003f51738b9fa9b2921a939f94e7ebbc2369c4445a947b282cfed9b81`. Comparing full relative-path manifests and file hashes, the current corpus is exactly the same: **1,356/1,356 identical**, with zero additions, removals, or changed files at the time of this baseline capture.

## Raw baseline tuples

From the archive root I ran the documented root-relative command form for every immediate fixture directory:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture-directory>
```

The archive contains **132 fixture directories**. I captured each exact `(fixture name, exit status, stdout bytes, stderr bytes)` tuple; stdout/stderr are stored losslessly as hex in `/tmp/lore-r78-baseline-tuples.json` (SHA-256 `011c28f2ea080942f7e12ae9b7a6e320bf24022d0a3329584a1282ee8fb8ff93`). Baseline outcomes: **27 exit 0; 105 exit 1**. Replaying those same 132 names with the current checkout’s checker and fixtures, using the same root-relative argv and repository-root cwd, yielded **132/132 exact tuple matches**. This is baseline verification, not evidence about a proposed change.

## Relevant boundaries and precedent

The active checker validates contradiction sides using `event_id` and `field` to resolve a timeline event and then obtains the citation from that event’s `source_id`. README round 3 documents side references as `{event_id, field}` and says the event’s own source is the citation; it does not say optional side metadata is forbidden. The checker validates required fields but generally tolerates extra object members. Thus the hypothesized copied `source_id` is not an accepted second citation path in current code; any concern that readers might treat a conflicting copy as authoritative is a presentation/calibration hypothesis, not a checker/source-truth finding.

Prior reports bound nearby behavior rather than settle this proposal: r3 establishes the cited-event design and its limits; r7 tests duplicate/ambiguous source handling, not an inconsistent copied side citation; r39 tests unknown source status at a uniquely resolved event; r62 covers timeline availability versus absence; r63 discusses permissive extra members in an unrelated JSON parsing case. The r77 verifier/scout reports demonstrate a useful regression method: archive the exact pin, compare all raw paths/bytes, and replay all old fixtures with root-relative CLI arguments. No prior report I inspected establishes that an extra side `source_id` is diagnosed, materially misleads readers, or needs a new rule.

## Post-candidate replay plan (not performed)

If a candidate is later authorized and built, preserve this pinned baseline and compare the candidate corpus against `/tmp/lore-r78-pin/.shokunin/lore/corpus` by complete relative-path manifest and raw bytes. Require every old path and byte to remain unchanged; enumerate all additions/removals/changes. Replay the exact **132** archived fixture names with the pinned checker+fixture set and candidate checker+fixture set, each using the same root-relative invocation and cwd; compare raw `(exit, stdout, stderr)` bytes per fixture, with no normalization. The old tuple record above is the comparison oracle. Keep temporary probes outside the repository and outside the old-fixture denominator. Separately report each new control/candidate probe’s exact files, command, exit, stdout, and stderr; do not substitute a CLEAN result for old-corpus replay.

For the hypothesis itself, ensure a matched unique-event pair differs only in copied side `source_id` (equal to target event citation versus inconsistent), plus absent-copy, malformed/unresolved endpoint, and appropriate loaded/unavailable controls as dictated by the actual change. Confirm precisely what the checker emits before and after and which repair would differ. Do not reject arbitrary harmless extension fields unless evidence supports that narrower rule. Regression success cannot establish material reader confusion or justify a policy change; that requires independent review. Do not infer prose/source truth, canon, chronology, rights, or mechanics from these structural checks.

## Verdict and limits

**GO for the regression baseline/archive gate:** the pinned archive is captured, and all 132 old raw CLI tuples replay exactly against the unchanged checkout. **Not a GO for checker implementation or admission.** There is no candidate yet and no post-candidate replay; the only established result is preservation at the baseline. A candidate that changes any old tuple or old corpus byte requires explanation and independent review, not silent acceptance. This report does not judge the proposed reader-confusion hypothesis or make any source-truth/canon/rights/mechanics inference.
