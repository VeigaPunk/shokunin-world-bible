# lore scorecard — round 21

Owned axes: depth, coverage, calibration. Scores remain unassigned without a
quality rubric; row counts and exit codes are measurements, not scores or verdicts.

| axis | score | evidence / counting command | last change |
|---|---|---|---|
| depth | unmeasured | round 15: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r15-carbon-followup` → exit 0; new Sella later-carbon note and event manually mapped clause-by-clause in `reports/r15-independent-verifier.md`, with mark origin unknown and no Blue Seal attribution; 28 prior outputs unchanged in `corpus/live/runs/20261012T181828Z/`; baseline report `2c5b2f1c13f42f4c42c31ff07773c61043be43a7` lacked this observation; work commit in round-15 report | r15 |
| coverage | unmeasured | round 21: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r21-malformed` and `r21-malformed-reverse` → exit 1 with both known-place `double-booked` and `expected event-id strings`; paired clean controls retain booking; same-place/invalid-tick/wrong-kind-place/ambiguous-actor controls do not gain booking; 64 saved outputs `corpus/live/runs/20261012T193022Z/`; baseline report `64d2673fb87ffb25396948840a991ee88472f8bf` masked booking on malformed dependency; `reports/r21-axis-adjudicator.md` admitted narrowly; work commit in round-21 report | r21 |
| calibration | unmeasured | round 20: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r20-negative-dependent` → exit 1 with invalid-tick only; paired `r20-valid-order` clean; valid inverted/equal endpoints still invert and `r20-mixed-edges` preserves valid-edge inversion; 56 saved outputs `corpus/live/runs/20261012T191902Z/`; baseline report `47733bfa36216a28c639fd8d5dc891fb4d8de3f5` asserted raw negative-endpoint inversion; first adjudicator exited without report, replacement `reports/r20-axis-adjudicator-retry.md` admitted narrow move; work commit in round-20 report | r20 |

planned: another independently falsifiable move only; source-text truth remains unverified, and the r15 blue mark must not be called a Blue Seal trace. Round-4 duplicate-name detector remains rejected; no active name check or alias coverage.
retired: hard-failing exact duplicate names without sourced uniqueness; round 4 showed calibration harm. Scores unchanged because the round was rejected.
