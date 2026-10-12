# lore scorecard — round 1

Owned axes: depth, coverage, calibration. Scores remain unassigned without a
quality rubric; row counts and exit codes are measurements, not scores or verdicts.

| axis | score | evidence / counting command | last change |
|---|---|---|---|
| depth | unmeasured | round 1: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/consistent` → exit 0; same command with `contradictions` → exit 1, three distinct errors; logs in `corpus/live/runs/20261012T155644Z/`; measured work commit cited in round report | r1 |
| coverage | unmeasured | round 1: checker handles sourced claims, source IDs, relation endpoints and timeline location/dependency checks; unchecked alias and free-text cases remain explicit in decision table | r1 |
| calibration | unmeasured | independent verifier `lore-r1-independent-verifier` reran both commands, confirmed limits, and left all SHONEN boxes unchecked | r1 |

planned: round 2 may implement explicit contradiction records and alias checks;
this is not a round-1 achievement.
retired: none.
