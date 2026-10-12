# lore scorecard — round 7

Owned axes: depth, coverage, calibration. Scores remain unassigned without a
quality rubric; row counts and exit codes are measurements, not scores or verdicts.

| axis | score | evidence / counting command | last change |
|---|---|---|---|
| depth | unmeasured | round 3: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/contradictions` → exit 1 with original three findings and validated two ledger pointers; `contradictions-ledger-malformed` → exit 1 with ledger-local unresolved event plus original three; outputs in `corpus/live/runs/20261012T162704Z/`; baseline report commit `ba110ea3495571ce027699dc9bfabc9d2912cffb` had no ledger; work commit in round-3 report | r3 |
| coverage | unmeasured | round 6: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/item-chain-valid` → exit 0; `item-chain-broken` → exit 1, one local predecessor error; saved `corpus/live/runs/20261012T165220Z/`; baseline `8f56fbdecc0f88db1139410becfc7436ea75f8b1` had no provenance check; work commit in round-6 report | r6 |
| calibration | unmeasured | round 7: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r7-ally-reverse-ambiguous` → exit 1 with duplicate ID, ambiguous reverse source, missing qualified reciprocal; `r7-item-ambiguous` → exit 1 with six local ambiguous citations; outputs `corpus/live/runs/20261012T170333Z/`; baseline report commit `4f6eaba9c7f4807b4a28ba9883af5bf479252294` qualified duplicates by membership; work commit in round-7 report | r7 |

planned: timeline edge cases or source-text attestation model as one move with cited raw evidence; duplicate-source-ID identity qualification is now handled, but source-text support remains unverified. Round-4 duplicate-name detector remains rejected; no active name check or alias coverage.
retired: hard-failing exact duplicate names without sourced uniqueness; round 4 showed calibration harm. Scores unchanged because the round was rejected.
