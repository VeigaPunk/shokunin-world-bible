# lore scorecard — round 60

Owned axes: depth, coverage, calibration. Scores remain unassigned without a
quality rubric; row counts and exit codes are measurements, not scores or verdicts.

| axis | score | evidence / counting command | last change |
|---|---|---|---|
| depth | unmeasured | round 43: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r43-jorin-vela-sighting` → exit0 structurally; newly authored Jorin visual report of Vela at east steps connects to Vela’s own reported position only conditionally; no verified shared occasion/bell/absence; `reports/r43-reviewer.md` and `reports/r43-axis-adjudicator.md` compare r10/r33/r40 and independently replay 94/94 prior CLI tuples, 469/469 JSON bytes at `e810eb0`; work commit in round-43 report | r43 |
| coverage | unmeasured | round 39: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r39-ledger-source-missing` → exit1 exactly ledger `claim_b` no-resolvable-source and timeline unknown-source findings; clean r35 clone exit0; r7 executed ambiguous but not zero-source ledger probe (`r7-reviewer.md:38,52`); `reports/r39-reviewer.md` and `reports/r39-axis-adjudicator.md` independently replay 90/90 prior CLI tuples, 449/449 JSON bytes at `793a3a8`; work commit in round-39 report | r39 |
| calibration | unmeasured | round 60: `reports/r60-reviewer.md`, `reports/r60-independent-verifier.md`, `reports/r60-axis-adjudicator.md` distinguish unavailable entity table (file-load error only) from loaded empty (six dangling) and partial (three), preserving independent tick/source/dependency faults. Pinned r59 report `d766194`: 98/99 prior raw tuples identical; only r59 nested 7→1 removes six dependent entity lookups; 494/494 old JSON bytes unchanged. Whole-table status only; loaded arrays with rejected rows still yield absent-from-retained-input findings and unavailable sources/timeline remain out of scope. Work commit in round-60 report | r60 |

planned: another independently falsifiable move only; source-text truth remains unverified, and the r15 blue mark must not be called a Blue Seal trace. Round-4 duplicate-name detector remains rejected; no active name check or alias coverage.
retired: hard-failing exact duplicate names without sourced uniqueness; round 4 showed calibration harm. Scores unchanged because the round was rejected.
