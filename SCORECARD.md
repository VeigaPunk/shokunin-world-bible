# lore scorecard — round 16

Owned axes: depth, coverage, calibration. Scores remain unassigned without a
quality rubric; row counts and exit codes are measurements, not scores or verdicts.

| axis | score | evidence / counting command | last change |
|---|---|---|---|
| depth | unmeasured | round 15: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r15-carbon-followup` → exit 0; new Sella later-carbon note and event manually mapped clause-by-clause in `reports/r15-independent-verifier.md`, with mark origin unknown and no Blue Seal attribution; 28 prior outputs unchanged in `corpus/live/runs/20261012T181828Z/`; baseline report `2c5b2f1c13f42f4c42c31ff07773c61043be43a7` lacked this observation; work commit in round-15 report | r15 |
| coverage | unmeasured | round 8: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r8-deps-distinct` → exit 0; `r8-deps-anomalous` → exit 1 with indexed repeat/self + existing inversion; isolated repeated-earlier probe in `reports/r8-independent-verifier.md`; run output `corpus/live/runs/20261012T171326Z/`; baseline report commit `17736ae5ed260c4b99f98efd9b194254ccd2aa87` accepted repeated earlier dependency; work commit in round-8 report | r8 |
| calibration | unmeasured | round 16 second-corrected candidate: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r16-missing-place` and `r16-missing-first` → exit 1 with dangling only; `r16-valid-places` still double-books; `r16-mixed-three` keeps known harbor/tower finding; 33 saved outputs `corpus/live/runs/20261012T182817Z/`; baseline report `3995486def3c9fceb95449362f6e8dab8cc130f7` asserted booking with missing `unlisted`; first submission and first correction rejected, final `reports/r16-readjudicator.md` admitted after two prose corrections; work commit in round-16 report | r16 |

planned: another independently falsifiable move only; source-text truth remains unverified, and the r15 blue mark must not be called a Blue Seal trace. Round-4 duplicate-name detector remains rejected; no active name check or alias coverage.
retired: hard-failing exact duplicate names without sourced uniqueness; round 4 showed calibration harm. Scores unchanged because the round was rejected.
