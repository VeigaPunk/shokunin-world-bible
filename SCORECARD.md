# lore scorecard — round 18

Owned axes: depth, coverage, calibration. Scores remain unassigned without a
quality rubric; row counts and exit codes are measurements, not scores or verdicts.

| axis | score | evidence / counting command | last change |
|---|---|---|---|
| depth | unmeasured | round 15: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r15-carbon-followup` → exit 0; new Sella later-carbon note and event manually mapped clause-by-clause in `reports/r15-independent-verifier.md`, with mark origin unknown and no Blue Seal attribution; 28 prior outputs unchanged in `corpus/live/runs/20261012T181828Z/`; baseline report `2c5b2f1c13f42f4c42c31ff07773c61043be43a7` lacked this observation; work commit in round-15 report | r15 |
| coverage | unmeasured | round 8: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r8-deps-distinct` → exit 0; `r8-deps-anomalous` → exit 1 with indexed repeat/self + existing inversion; isolated repeated-earlier probe in `reports/r8-independent-verifier.md`; run output `corpus/live/runs/20261012T171326Z/`; baseline report commit `17736ae5ed260c4b99f98efd9b194254ccd2aa87` accepted repeated earlier dependency; work commit in round-8 report | r8 |
| calibration | unmeasured | round 18: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r18-duplicate-pair` and `r18-duplicate-reverse` → exit 1 with duplicate/ambiguous findings only; `r18-unique-pair` still double-books; `r18-known-through-ambiguous` and `r18-duplicate-first-known` keep known tower/quay booking; 45 saved outputs `corpus/live/runs/20261012T185657Z/`; baseline report `82701ce7680fb062a345e379057c8a097c1539e6` asserted raw-ID booking with duplicate `harbor`; `reports/r18-axis-adjudicator.md` admitted narrow move while test-scout exited without report; work commit in round-18 report | r18 |

planned: another independently falsifiable move only; source-text truth remains unverified, and the r15 blue mark must not be called a Blue Seal trace. Round-4 duplicate-name detector remains rejected; no active name check or alias coverage.
retired: hard-failing exact duplicate names without sourced uniqueness; round 4 showed calibration harm. Scores unchanged because the round was rejected.
