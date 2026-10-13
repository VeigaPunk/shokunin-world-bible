# Round 36 regression scout — exact replay plan

## Scope and evidence

This is a plan, not a replay: I did not run the checker or alter fixtures, README, LOG, or other artifacts. Round 36’s declared calibration test is a separate r35-derived wrong-date near-miss: sole source-text change is Sella’s date, from seventh to eighth day of Embermonth, year 12; all five JSON tables remain byte-identical; the intended historical baseline is 87 CLI tuples / 434 JSON files (`.shokunin/lore/LOG.md:574-576`). The previous round’s pin is work commit `633ba022b45c71a9049664e1d9ac181950820aee` and report commit `356f75b32afed9abb85687689c8d5f55965c0cb3` (`LOG.md:574`). R35 established its exact-replay method and caveat that a clean checker does not establish semantics (`reports/r35-regression-scout.md`, “Proposed replay and baseline check”; `.shokunin/lore/LOG.md:558,565,569`). The preserved r35 initial reviewer failure found that separate “day of this note” references did not establish one shared date; the corrected, source-claimed date/unique ringing supported only conditional incompatibility (`LOG.md:562,565,569`).

## Replay plan

1. Pin and identify the exact r35 baseline tree before measuring. Enumerate sorted baseline fixture directories and JSON paths in the declared scope; preserve manifests and hashes, rather than deriving counts from the candidate. Record both commit IDs and verify the expected 87 CLI / 434 JSON denominator. The target r36 fixture must be absent from baseline.
2. Run each baseline fixture at both baseline and candidate with exactly the same repo-root argv and cwd: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture>`. Capture raw stdout, raw stderr, and exit status independently, keyed by fixture path. Require all 87 triples to match exactly; retain manifests/results so path-spelling differences cannot masquerade as behavioral differences.
3. Compare every one of the 434 baseline JSON paths byte-for-byte between pinned baseline and candidate. Do not normalize JSON, use only hashes without reproducible paths, or include the newly added r36 artifact in the old denominator. Separately confirm the new near-miss fixture is present and checker-clean structurally.
4. Treat semantic review as an independent manual check. Compare Tarin’s seventh-day account against Sella’s eighth-day account, plus the unchanged structured Sella event and ledger `why`. The unchanged structured records still describe the r35 seventh-day claim; a clean checker only demonstrates structural validity, not source-text entailment, shared occasion, contradiction, truth, or canon. Require the comparison map to flag this deliberate mismatch and decline the same-occasion inference.

## Risks

- A wrong pin, changed corpus scope, or candidate-derived inventory can produce a misleading 87/434 claim. Record baseline path manifests and explain any count drift.
- The checker echoes paths; inconsistent cwd/argv spellings may create false stream mismatches or mask real ones. Use the same root-relative invocation at both trees and compare raw streams/status, not just return codes.
- Unchanged JSON is the test’s design, but creates an intentional mismatch: Sella’s structured event/source citation/ledger rationale still encode the seventh-day version while her excerpt says eighth. Checker success cannot repair or validate that mismatch; report it, do not “fix” it by editing JSON.
- Two source-claimed dates do not prove which account is true, nor establish Sella’s location on the seventh day. The near-miss only removes the accounts’ asserted common date/occasion. No canon winner follows.

## Falsifiable check

The regression claim passes only if an independent replay against the pinned r35 baseline finds exact stdout bytes, stderr bytes, and exit status for all 87 baseline fixture paths, and exact bytes for all 434 baseline JSON paths; the r36 near-miss is absent at baseline and structurally checker-clean at candidate. Any missing/extra baseline path, stream/status difference, JSON byte difference, or failing/missing new fixture falsifies the replay claim. The calibration test additionally passes only if a reviewer verifies the sole excerpt date change and unchanged five tables, identifies that the structured Sella event/ledger still reflect the seventh-day account, and declines to infer a shared occasion or r35-style conditional conflict from these different-date excerpts. A clean checker alone is not that evidence.
