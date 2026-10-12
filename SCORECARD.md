# lore scorecard — round 3

Owned axes: depth, coverage, calibration. Scores remain unassigned without a
quality rubric; row counts and exit codes are measurements, not scores or verdicts.

| axis | score | evidence / counting command | last change |
|---|---|---|---|
| depth | unmeasured | round 3: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/contradictions` → exit 1 with original three findings and validated two ledger pointers; `contradictions-ledger-malformed` → exit 1 with ledger-local unresolved event plus original three; outputs in `corpus/live/runs/20261012T162704Z/`; baseline report commit `ba110ea3495571ce027699dc9bfabc9d2912cffb` had no ledger; work commit in round-3 report | r3 |
| coverage | unmeasured | round 2: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/ally-reciprocal` → exit 0 and `ally-one-way` → exit 1, one relation-local symmetry report; preserved in `corpus/live/runs/20261012T161753Z/`; baseline work commit `d094160bbaa4675d966532e15629d0d6ec728750` had no faction symmetry rule; work commit cited in round-2 report | r2 |
| calibration | unmeasured | independent verifier `lore-r1-independent-verifier` reran both commands, confirmed limits, and left all SHONEN boxes unchecked | r1 |

planned: consider name/citation collision rule or malformed-bible decision table as one next axis move; duplicate-source-ID witness precision and aliases remain uncovered.
retired: none.
