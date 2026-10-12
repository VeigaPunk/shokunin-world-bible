# lore scorecard — round 5

Owned axes: depth, coverage, calibration. Scores remain unassigned without a
quality rubric; row counts and exit codes are measurements, not scores or verdicts.

| axis | score | evidence / counting command | last change |
|---|---|---|---|
| depth | unmeasured | round 3: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/contradictions` → exit 1 with original three findings and validated two ledger pointers; `contradictions-ledger-malformed` → exit 1 with ledger-local unresolved event plus original three; outputs in `corpus/live/runs/20261012T162704Z/`; baseline report commit `ba110ea3495571ce027699dc9bfabc9d2912cffb` had no ledger; work commit in round-3 report | r3 |
| coverage | unmeasured | round 2: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/ally-reciprocal` → exit 0 and `ally-one-way` → exit 1, one relation-local symmetry report; preserved in `corpus/live/runs/20261012T161753Z/`; baseline work commit `d094160bbaa4675d966532e15629d0d6ec728750` had no faction symmetry rule; work commit cited in round-2 report | r2 |
| calibration | unmeasured | round 5: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<case>` for `consistent` and five `r5-*` cases → control exit 0, malformed exit 1 with named classes in `corpus/live/runs/20261012T164316Z/`; independently replayed by `lore-r5-independent-verifier`; baseline `b6ca1e9` lacked measured table, work commit in round-5 report | r5 |

planned: source-backed item provenance chains or timeline edge cases as one next move. Round-4 duplicate-name detector remains rejected; no active name check. Duplicate-source-ID witness precision and aliases remain uncovered.
retired: hard-failing exact duplicate names without sourced uniqueness; round 4 showed calibration harm. Scores unchanged because the round was rejected.
