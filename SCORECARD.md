# lore scorecard — round 30

Owned axes: depth, coverage, calibration. Scores remain unassigned without a
quality rubric; row counts and exit codes are measurements, not scores or verdicts.

| axis | score | evidence / counting command | last change |
|---|---|---|---|
| depth | unmeasured | round 28: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r28-courier-excerpt` → exit 0 (structural only); constructed one-sentence excerpt mapped manually to `relations[0]` in `relation-clause-map.md`, with editorial ID alignment and rejected near-miss; `reports/r28-reviewer.md` clause review; `reports/r28-axis-adjudicator.md` independently checks 78/78 prior CLI tuples and 389/389 old JSON bytes at `aaa8d72` and admits narrow depth; work commit in round-28 report | r28 |
| coverage | unmeasured | round 27: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r27-both-ambiguous` → exit 1, exact `.from` and `.to` relation findings plus two collateral timeline actor findings; matched `r27-target-only` keeps `.to` only; `reports/r27-independent-verifier.md` checks 76/76 old CLI tuples exact and 379/379 old JSON bytes at `bb4c6c9`; `reports/r27-axis-adjudicator.md` admitted; work commit in round-27 report | r27 |
| calibration | unmeasured | round 30: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r30-explicit-negation` → exit 0 structurally like r28/r29; `textual-conflict-map.md` distinguishes conditional explicit denial from unsupported proximity without canon falsity; `reports/r30-reviewer.md` triad; `reports/r30-axis-adjudicator.md` independently replays 80/80 old CLI tuples using same argv and 399/399 JSON bytes at `533e367` after verifier referenced uncommitted /tmp script; one simplifier failed no-report; work commit in round-30 report | r30 |

planned: another independently falsifiable move only; source-text truth remains unverified, and the r15 blue mark must not be called a Blue Seal trace. Round-4 duplicate-name detector remains rejected; no active name check or alias coverage.
retired: hard-failing exact duplicate names without sourced uniqueness; round 4 showed calibration harm. Scores unchanged because the round was rejected.
