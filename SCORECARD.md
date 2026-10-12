# lore scorecard — round 2

Owned axes: depth, coverage, calibration. Scores remain unassigned without a
quality rubric; row counts and exit codes are measurements, not scores or verdicts.

| axis | score | evidence / counting command | last change |
|---|---|---|---|
| depth | unmeasured | round 1: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/consistent` → exit 0; same command with `contradictions` → exit 1, three distinct errors; logs in `corpus/live/runs/20261012T155644Z/`; measured work commit cited in round report | r1 |
| coverage | unmeasured | round 2: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/ally-reciprocal` → exit 0 and `ally-one-way` → exit 1, one relation-local symmetry report; preserved in `corpus/live/runs/20261012T161753Z/`; baseline work commit `d094160bbaa4675d966532e15629d0d6ec728750` had no faction symmetry rule; work commit cited in round-2 report | r2 |
| calibration | unmeasured | independent verifier `lore-r1-independent-verifier` reran both commands, confirmed limits, and left all SHONEN boxes unchecked | r1 |

planned: explicit contradiction records with `claim_a`, `claim_b`, `why` and source citations, then a report-only preservation check; aliases remain future work. Duplicate-source-ID witness diagnostic precision remains uncovered.
retired: none.
