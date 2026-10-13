# lore scorecard — round 37

Owned axes: depth, coverage, calibration. Scores remain unassigned without a
quality rubric; row counts and exit codes are measurements, not scores or verdicts.

| axis | score | evidence / counting command | last change |
|---|---|---|---|
| depth | unmeasured | round 35: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r35-bell7-conflict` → exit0 structurally; two cited fictional accounts tied by source-claimed single Bell-7 ringing/date and manual two-sided unresolved ledger; initial `reports/r35-reviewer.md` FAIL preserved, `reports/r35-remediation-reviewer.md` PASS conditional, `reports/r35-axis-adjudicator.md` independent replay 86/86 prior CLI tuples and 429/429 JSON bytes at `0b2f416`; work commit in round-35 report | r35 |
| coverage | unmeasured | round 37: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r37-ledger-ambiguous` → exit1 with exactly duplicate timeline ID and `claim_a.event_id` exact-one findings; copied unique control exit0; `reports/r37-reviewer.md` and `reports/r37-axis-adjudicator.md` independently contrast r9 dependency case and replay 88/88 old CLI tuples, 439/439 JSON bytes at `4e5dacf`; work commit in round-37 report | r37 |
| calibration | unmeasured | round 36: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r36-bell7-wrong-date` → exit0 structurally like r35; only Sella excerpt seventh→eighth while five JSON tables remain byte-identical; `reports/r36-reviewer.md` rejects shared-ringing support despite unchanged event/ledger; `reports/r36-axis-adjudicator.md` independently replayed 87/87 old CLI tuples and 434/434 JSON bytes at `356f75b`; work commit in round-36 report | r36 |

planned: another independently falsifiable move only; source-text truth remains unverified, and the r15 blue mark must not be called a Blue Seal trace. Round-4 duplicate-name detector remains rejected; no active name check or alias coverage.
retired: hard-failing exact duplicate names without sourced uniqueness; round 4 showed calibration harm. Scores unchanged because the round was rejected.
