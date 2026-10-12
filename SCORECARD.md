# lore scorecard — round 17

Owned axes: depth, coverage, calibration. Scores remain unassigned without a
quality rubric; row counts and exit codes are measurements, not scores or verdicts.

| axis | score | evidence / counting command | last change |
|---|---|---|---|
| depth | unmeasured | round 15: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r15-carbon-followup` → exit 0; new Sella later-carbon note and event manually mapped clause-by-clause in `reports/r15-independent-verifier.md`, with mark origin unknown and no Blue Seal attribution; 28 prior outputs unchanged in `corpus/live/runs/20261012T181828Z/`; baseline report `2c5b2f1c13f42f4c42c31ff07773c61043be43a7` lacked this observation; work commit in round-15 report | r15 |
| coverage | unmeasured | round 8: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r8-deps-distinct` → exit 0; `r8-deps-anomalous` → exit 1 with indexed repeat/self + existing inversion; isolated repeated-earlier probe in `reports/r8-independent-verifier.md`; run output `corpus/live/runs/20261012T171326Z/`; baseline report commit `17736ae5ed260c4b99f98efd9b194254ccd2aa87` accepted repeated earlier dependency; work commit in round-8 report | r8 |
| calibration | unmeasured | round 17: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r17-wrong-after` and `r17-wrong-before` → exit 1 with `not a place` only; `r17-valid-places` still double-books; `r17-wrong-{first,middle,last}` retain known harbor/tower finding; 39 saved outputs `corpus/live/runs/20261012T184609Z/`; baseline report `1dd6f27ae89a096c8fb99d2750f35e5118fda5d3` asserted raw-ID booking with wrong-kind `mira`; `reports/r17-axis-adjudicator-retry.md` admitted narrow move after first adjudicator lane exited without report; work commit in round-17 report | r17 |

planned: another independently falsifiable move only; source-text truth remains unverified, and the r15 blue mark must not be called a Blue Seal trace. Round-4 duplicate-name detector remains rejected; no active name check or alias coverage.
retired: hard-failing exact duplicate names without sourced uniqueness; round 4 showed calibration harm. Scores unchanged because the round was rejected.
