# lore scorecard — round 32

Owned axes: depth, coverage, calibration. Scores remain unassigned without a
quality rubric; row counts and exit codes are measurements, not scores or verdicts.

| axis | score | evidence / counting command | last change |
|---|---|---|---|
| depth | unmeasured | round 28: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r28-courier-excerpt` → exit 0 (structural only); constructed one-sentence excerpt mapped manually to `relations[0]` in `relation-clause-map.md`, with editorial ID alignment and rejected near-miss; `reports/r28-reviewer.md` clause review; `reports/r28-axis-adjudicator.md` independently checks 78/78 prior CLI tuples and 389/389 old JSON bytes at `aaa8d72` and admits narrow depth; work commit in round-28 report | r28 |
| coverage | unmeasured | round 31: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r31-source-ambiguous` → exit 1, eight findings including `relations[0].source_id` ambiguity on `carries`; paired unique exits 0; r7 prior allied ambiguity credited; `reports/r31-independent-verifier.md` and `reports/r31-axis-adjudicator.md` each replay 81/81 old CLI tuples and 404/404 JSON bytes at `4da4b94`; work commit in round-31 report | r31 |
| calibration | unmeasured | round 32: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r32-source-malformed` → exit 1 only `sources[2].title` required error, versus r31 admitted duplicate eight findings and unique control exit0; `reports/r32-independent-verifier.md` checks 83/83 old CLI tuples and 414/414 JSON bytes at `cfaf03a`; `reports/r32-axis-adjudicator.md` independently admits source-specific screened-row calibration, credits r26 entity precedent; work commit in round-32 report | r32 |

planned: another independently falsifiable move only; source-text truth remains unverified, and the r15 blue mark must not be called a Blue Seal trace. Round-4 duplicate-name detector remains rejected; no active name check or alias coverage.
retired: hard-failing exact duplicate names without sourced uniqueness; round 4 showed calibration harm. Scores unchanged because the round was rejected.
