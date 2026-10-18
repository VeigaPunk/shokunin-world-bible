# PROPOSAL ONLY — Round 87 SCORECARD section

Do not copy into `SCORECARD.md`: current Round 87 reports contain baselines only for C1, no C1 candidate after-run, no C2/C3 result, and no independent axis verdict. Scores remain unassigned; no axis movement or admission is asserted here.

## Round 87 — proposed evidence row (incomplete; TODOs retained)

| axis / claim | before → after | evidence / counting command | measured commit |
|---|---|---|---|
| calibration — C1 masked-break disclosure | **Before (measured at baseline):** the masked record receives one ambiguous-holder finding and one stop notice; later records have no local disclosure, while an equivalent unique-holder break is reported. **After:** TODO — candidate checker not measured in available reports. | Before: `python3 corpus/fixtures/check_bible.py corpus/live/runs/round-85/probe-inputs/r85-masked-ambiguous` (.ufo/waves/round-87/V2.md:10-19) and the four `r87-*` replays (.ufo/waves/round-87/F1.md:19-70). Baseline full-corpus counting: `python3 census_b1.py` in `/tmp/r87-B1` → 133 fixtures, exits `{0:28,1:105}`, 660 fixture JSON paths, 705 corpus JSON paths, 259 violations, 0 nonempty stderr (.ufo/waves/round-87/B1.md:7-25). After replay, output-delta tuple inventory, and preservation count: **TODO**; do not report 0 changed tuples. | Baseline `28706dc73a9b7667851fd82adb71e905ae5eb896`; candidate measured commit `<TODO>` |
| depth — C2 provenance decision table | **Before → after:** TODO — no C2 table/replay report present at the second checkpoint. | TODO: actual table path, every stop/latch condition and finding signature, exact named-fixture replay commands and pasted outputs, plus verified row/case counting command. `.ufo/waves/round-87/W2.md:8-14` also leaves C2 evidence pending. | `<TODO: verified work/evidence commit>` |
| coverage — C3 myth cluster | **Before → after:** TODO — no C3 fixture inventory or checker report present at the second checkpoint. | Candidate command, once built: `python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-myth-cluster`. TODO: paste observed stdout/stderr/exit and exact counts/commands for required records, dependency edge, clause-map, and inspiration note. Keep attribution, rights, and AI-training-permission as three separate questions. | `<TODO: verified work/evidence commit>` |

### C1 baseline transcript (not a candidate after-measurement)

From `.ufo/waves/round-87/F1.md:49-70`, the commands below used the pinned, unmodified checker:

```text
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-chain-unique-valid
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT_CODE=0

$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-chain-unique-broken
VIOLATION: entities[3].provenance[2]: provenance chain break; expected from_holder 'harbor', got 'mira'
1 violation(s); no canon changed
EXIT_CODE=1
```

For the masked pair, `.ufo/waves/round-87/F1.md:21-47` records `r87-masked-break-to-ambiguous` and `r87-masked-break-from-ambiguous`: each exits 1 with three findings (duplicate `dup`, one field-local ambiguous holder, and one global “unassessed at this and all later records” notice at `provenance[0]`). `.ufo/waves/round-87/V2.md:12-19` independently records the existing r85 masked case: `python3 corpus/fixtures/check_bible.py corpus/live/runs/round-85/probe-inputs/r85-masked-ambiguous` emits duplicate `vault`, ambiguous `entities[3].provenance[1].to_holder`, the single stop notice at `[1]`, `3 violation(s); no canon changed`, exit 1. These are baseline outputs only.

`.ufo/waves/round-87/V2.md:41-47` says the attempted `git apply --check .ufo/waves/round-87/patches/X2-c1-alt.patch` failed with exit 128 because that path was absent; V2 therefore has no candidate output or tuple delta. `.ufo/waves/round-87/F1.md:72,78` likewise states that its fixture-only work did not measure a post-fix checker. TODO: obtain the delivered candidate replay and enumerate every changed existing-fixture tuple finding-by-finding, with all preserved outputs evidenced by the verifier.

TODO before landing: add the actual C2/C3 reports, candidate pin and C1 before/after tuple inventory, exact commands/outputs, final report paths/line pointers and independent per-axis verdict. Keep scores unassigned under the existing SCORECARD convention; counts and exit codes are measurements, not scores.