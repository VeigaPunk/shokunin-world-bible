# lore scorecard — round 13

Owned axes: depth, coverage, calibration. Scores remain unassigned without a
quality rubric; row counts and exit codes are measurements, not scores or verdicts.

| axis | score | evidence / counting command | last change |
|---|---|---|---|
| depth | unmeasured | round 10: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r10-registry-witness` → exit 0; `registrar-copy-excerpt.md` clause mapping to Sella’s registrar claim, recorded observation, and requested blank destination/kept carbon manually verified in `reports/r10-independent-verifier.md`; all 19 old outputs unchanged in `corpus/live/runs/20261012T173416Z/`; baseline report `29159c263771d425f215f275491c6614219cea59` had no second account; work commit in round-10 report | r10 |
| coverage | unmeasured | round 8: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r8-deps-distinct` → exit 0; `r8-deps-anomalous` → exit 1 with indexed repeat/self + existing inversion; isolated repeated-earlier probe in `reports/r8-independent-verifier.md`; run output `corpus/live/runs/20261012T171326Z/`; baseline report commit `17736ae5ed260c4b99f98efd9b194254ccd2aa87` accepted repeated earlier dependency; work commit in round-8 report | r8 |
| calibration | unmeasured | round 13: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r13-missing-actor` → exit 1 with two dangling findings but no definite double-booking; `r13-unique-actor` retains exit 1 with double-booking; `corpus/live/runs/20261012T180109Z/` preserves 28 outputs; baseline report `97f766762ac78ab6bcf6523aadbd2ffa92d4f4f5` asserted double-booking for the missing actor too; work commit in round-13 report | r13 |

planned: seek a separately falsifiable cited lore-depth or new coverage move; source-text support remains unverified. Round-4 duplicate-name detector remains rejected; no active name check or alias coverage.
retired: hard-failing exact duplicate names without sourced uniqueness; round 4 showed calibration harm. Scores unchanged because the round was rejected.
