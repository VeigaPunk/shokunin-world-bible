# lore scorecard — round 26

Owned axes: depth, coverage, calibration. Scores remain unassigned without a
quality rubric; row counts and exit codes are measurements, not scores or verdicts.

| axis | score | evidence / counting command | last change |
|---|---|---|---|
| depth | unmeasured | round 23: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r23-note-class` → exit 0; witnessed-absence note (Sella reports the outbound route strip was not found on the registry hook rack) mapped clause-by-clause in `fixtures/r23-note-class/witnessed-absence-clause-map.md` and `reports/r23-reviewer.md`; not the r15 mark; 72 saved outputs exact in `corpus/live/runs/20261012T193930Z/`; 359 baseline JSON paths unchanged at `d6ea676` (r22 cited 319; measured count is 359); `reports/r23-axis-adjudicator.md` admitted; work commit in round-23 report | r23 |
| coverage | unmeasured | round 25: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r25-to-ambiguous` → exit 1 with duplicate-ID and exact `relations[0].to` ambiguity; paired `r25-to-unique` exits 0; `reports/r25-independent-verifier.md` confirms 73/73 old CLI outcomes exact and 364/364 old JSON bytes unchanged at baseline `1919fae`; `reports/r25-axis-adjudicator.md` admitted; work commit in round-25 report | r25 |
| calibration | unmeasured | round 26: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r26-to-malformed` → exit 1, only `entities[4].name` error, no admitted-target ambiguity; paired admitted r25 target reports `relations[0].to`; non-author `reports/r26-independent-verifier.md` checks 75/75 old CLI outcomes and 374/374 baseline JSON paths at `f44e728`; replacement `reports/r26-axis-adjudicator-retry.md` admitted after original adjudicator no-reply; work commit in round-26 report | r26 |

planned: another independently falsifiable move only; source-text truth remains unverified, and the r15 blue mark must not be called a Blue Seal trace. Round-4 duplicate-name detector remains rejected; no active name check or alias coverage.
retired: hard-failing exact duplicate names without sourced uniqueness; round 4 showed calibration harm. Scores unchanged because the round was rejected.
