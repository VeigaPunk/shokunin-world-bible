# lore scorecard — round 28

Owned axes: depth, coverage, calibration. Scores remain unassigned without a
quality rubric; row counts and exit codes are measurements, not scores or verdicts.

| axis | score | evidence / counting command | last change |
|---|---|---|---|
| depth | unmeasured | round 28: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r28-courier-excerpt` → exit 0 (structural only); constructed one-sentence excerpt mapped manually to `relations[0]` in `relation-clause-map.md`, with editorial ID alignment and rejected near-miss; `reports/r28-reviewer.md` clause review; `reports/r28-axis-adjudicator.md` independently checks 78/78 prior CLI tuples and 389/389 old JSON bytes at `aaa8d72` and admits narrow depth; work commit in round-28 report | r28 |
| coverage | unmeasured | round 27: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r27-both-ambiguous` → exit 1, exact `.from` and `.to` relation findings plus two collateral timeline actor findings; matched `r27-target-only` keeps `.to` only; `reports/r27-independent-verifier.md` checks 76/76 old CLI tuples exact and 379/379 old JSON bytes at `bb4c6c9`; `reports/r27-axis-adjudicator.md` admitted; work commit in round-27 report | r27 |
| calibration | unmeasured | round 26: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r26-to-malformed` → exit 1, only `entities[4].name` error, no admitted-target ambiguity; paired admitted r25 target reports `relations[0].to`; non-author `reports/r26-independent-verifier.md` checks 75/75 old CLI outcomes and 374/374 baseline JSON paths at `f44e728`; replacement `reports/r26-axis-adjudicator-retry.md` admitted after original adjudicator no-reply; work commit in round-26 report | r26 |

planned: another independently falsifiable move only; source-text truth remains unverified, and the r15 blue mark must not be called a Blue Seal trace. Round-4 duplicate-name detector remains rejected; no active name check or alias coverage.
retired: hard-failing exact duplicate names without sourced uniqueness; round 4 showed calibration harm. Scores unchanged because the round was rejected.
