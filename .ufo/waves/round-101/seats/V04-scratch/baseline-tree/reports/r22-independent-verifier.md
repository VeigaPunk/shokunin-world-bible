# Round 22 independent verifier — malformed dependency members

## Integrity and replay

- Baseline is report commit `cc92ecee56fa771d7344df9e85e9c1ce2146be3a`. I extracted that committed checker to `/tmp/r22-baseline-checker.py`; baseline checker SHA-256: `6708bed3bb665093553c06aebcf7075d8cd6d6bbb3fb5406270643b7123ce000`. Current checker SHA-256: `8d5fa4e14f14156c93006ac9da42725216e45de4d1d5e275739197a66a59c226`.
- Enumerated the baseline commit's `.shokunin/lore/corpus/fixtures/**/*.json` paths and compared each baseline blob byte-for-byte to the current worktree. **319/319 JSON paths exist and are byte-identical; 0 missing or changed.** This check covers fixture JSON only.
- Replayed all 64 transcripts in `corpus/live/runs/20261012T193022Z/` through the baseline checker: saved exit code/stdout/stderr exact **64/64** (stderr empty). Replayed through the current checker: exact against baseline **64/64**, including exit, stdout and stderr.
- Replayed all 72 transcripts in `corpus/live/runs/20261012T193930Z/` through the current checker: saved exit code/stdout/stderr exact **72/72** (stderr empty).

## Paired fixture fields and CLI observations

The `r22-clean-inversion` versus `r22-mixed-last` and `r22-mixed-first` fixtures differ only in `timeline.json`, at `timeline[1].depends_on`: `['r20-prereq']` versus `['r20-prereq', null]` or `[null, 'r20-prereq']`. Other JSON fixture files are byte-identical. The clean case reports the inversion `r20-prereq` tick 2 / `r20-dependent` tick 1. Each mixed case retains that inversion and adds exactly one row-level `expected event-id strings` finding first; malformed-first and malformed-last give the same dependency findings/order. `r22-malformed-only` reports only the row-level malformed finding. `r22-multiple-invalid` uses `[null, {}, [], 'r20-prereq']`, safely skips all three invalid members and retains the string-member inversion with one row-level malformed finding; no unhashable-value exception occurred.

Other saved fixture observations:

- `r22-self-repeated`: retains one malformed-list diagnostic, then self-reference, the existing self-edge inversion, and repeated-string finding in traversal order.
- `r22-unknown-mixed`: retains malformed-list diagnostic and inspects the string member, reporting the unknown event.
- `r22-valid-order`: clean, exit 0. The clean inversion control exits 1 with its inversion.

I also made three temporary `/tmp` probes (not repository fixtures). Adding a duplicate `r20-prereq` row to a malformed mixed-list fixture retained the duplicate-ID finding and exposed `ambiguous dependency event 'r20-prereq'` for the string member; baseline emitted only duplicate-ID and malformed-list findings. Setting the prerequisite tick negative retained the negative-tick plus malformed-list findings, with no inversion (same output as baseline): this string edge remains unassessed by the existing negative-endpoint guard. Setting the dependent tick equal to prerequisite tick 2 produced a double-booking, malformed-list, and equal-tick inversion finding; compared with baseline the new inversion was added, while double-booking remained. The modified tick in the latter probe also changes occupancy eligibility, so it is only a guard demonstration, not a paired occupancy-isolation test.

## Assessment and limits

Evidence supports the narrow behavior: one existing list-level malformed diagnostic is retained, non-string values (including unhashable JSON object/array values) are skipped before ID set/dictionary operations, and string siblings are inspected in original order under existing self/repeat/unknown/ambiguous/inversion handling. The tested malformed position did not mask string findings; the valid-order control remains clean. All 64 prior cases are unchanged. This is checker-input behavior only. It proves no fictional event, dependency, source-text chronology, causality, or canon; malformed members and any edge they purport to encode remain unassessed. The negative endpoint guard means an edge with a negative endpoint is deliberately not assessed for inversion. Replay establishes only these saved inputs, not all possible JSON inputs. No source or canon truth has been independently verified.
