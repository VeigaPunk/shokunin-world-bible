# lore scorecard — round 34

Owned axes: depth, coverage, calibration. Scores remain unassigned without a
quality rubric; row counts and exit codes are measurements, not scores or verdicts.

| axis | score | evidence / counting command | last change |
|---|---|---|---|
| depth | unmeasured | round 33: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r33-tarin-envelope` → exit0 structurally; one newly authored Tarin report and manual clause map for third-party positive Sella placement observation, all new rows cited; `reports/r33-reviewer.md` trace and `reports/r33-axis-adjudicator.md` independent python3 replay 84/84 old CLI tuples and 419/419 old JSON bytes at `56f9244`; work commit in round-33 report | r33 |
| coverage | unmeasured | round 31: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r31-source-ambiguous` → exit 1, eight findings including `relations[0].source_id` ambiguity on `carries`; paired unique exits 0; r7 prior allied ambiguity credited; `reports/r31-independent-verifier.md` and `reports/r31-axis-adjudicator.md` each replay 81/81 old CLI tuples and 404/404 JSON bytes at `4da4b94`; work commit in round-31 report | r31 |
| calibration | unmeasured | round 34: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r34-tarin-hearsay` → exit0 structurally like r33; `modality-contrast-map.md` marks fixed `reports seeing` fields unsupported as direct sight by “heard that,” not false; `reports/r34-reviewer.md` and `reports/r34-axis-adjudicator.md` manual contrast, independent 85/85 old CLI tuples and 424/424 JSON bytes at `e717c74`; work commit in round-34 report | r34 |

planned: another independently falsifiable move only; source-text truth remains unverified, and the r15 blue mark must not be called a Blue Seal trace. Round-4 duplicate-name detector remains rejected; no active name check or alias coverage.
retired: hard-failing exact duplicate names without sourced uniqueness; round 4 showed calibration harm. Scores unchanged because the round was rejected.
