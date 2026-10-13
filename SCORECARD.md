# lore scorecard — round 25

Owned axes: depth, coverage, calibration. Scores remain unassigned without a
quality rubric; row counts and exit codes are measurements, not scores or verdicts.

| axis | score | evidence / counting command | last change |
|---|---|---|---|
| depth | unmeasured | round 23: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r23-note-class` → exit 0; witnessed-absence note (Sella reports the outbound route strip was not found on the registry hook rack) mapped clause-by-clause in `fixtures/r23-note-class/witnessed-absence-clause-map.md` and `reports/r23-reviewer.md`; not the r15 mark; 72 saved outputs exact in `corpus/live/runs/20261012T193930Z/`; 359 baseline JSON paths unchanged at `d6ea676` (r22 cited 319; measured count is 359); `reports/r23-axis-adjudicator.md` admitted; work commit in round-23 report | r23 |
| coverage | unmeasured | round 25: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r25-to-ambiguous` → exit 1 with duplicate-ID and exact `relations[0].to` ambiguity; paired `r25-to-unique` exits 0; `reports/r25-independent-verifier.md` confirms 73/73 old CLI outcomes exact and 364/364 old JSON bytes unchanged at baseline `1919fae`; `reports/r25-axis-adjudicator.md` admitted; work commit in round-25 report | r25 |
| calibration | unmeasured | round 20: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r20-negative-dependent` → exit 1 with invalid-tick only; paired `r20-valid-order` clean; valid inverted/equal endpoints still invert and `r20-mixed-edges` preserves valid-edge inversion; 56 saved outputs `corpus/live/runs/20261012T191902Z/`; baseline report `47733bfa36216a28c639fd8d5dc891fb4d8de3f5` asserted raw negative-endpoint inversion; first adjudicator exited without report, replacement `reports/r20-axis-adjudicator-retry.md` admitted narrow move; work commit in round-20 report | r20 |

planned: another independently falsifiable move only; source-text truth remains unverified, and the r15 blue mark must not be called a Blue Seal trace. Round-4 duplicate-name detector remains rejected; no active name check or alias coverage.
retired: hard-failing exact duplicate names without sourced uniqueness; round 4 showed calibration harm. Scores unchanged because the round was rejected.
