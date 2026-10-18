# Round 22 executor report — dependency member inspection

Scope: `.shokunin/lore/corpus/fixtures/check_bible.py` and this report only. No fixtures, docs, LOG, or commits changed by executor.

## Change

Retained the existing single row-level `expected event-id strings` finding whenever any `depends_on` member is not a string. The diagnostic is appended before dependency-member findings. Removed the outer early-continue; the existing member loop skips each non-string before self comparison, set membership, or event-ID dictionary lookup. String members continue through the original self, repeated, unknown, ambiguous, and inversion checks in their original order. Occupancy remains before dependency validation and is unchanged. Required-field screening is unchanged. No malformed member is treated as a dependency.

## Verification

Baseline was checker from `cc92ecee56fa771d7344df9e85e9c1ce2146be3a` (round-21 report commit). Replayed all 64 saved commands in `.shokunin/lore/corpus/live/runs/20261012T193022Z/` against that baseline checker: **64/64 exit code, stdout, and stderr exact** (all stderr empty). Replayed the same 64 commands against the changed checker: **64/64 exit code and stdout exact**; stderr empty for all. The captured baseline checker SHA-256 is `6708bed3bb665093553c06aebcf7075d8cd6d6bbb3fb5406270643b7123ce000`. The changed checker SHA-256 is `8d5fa4e14f14156c93006ac9da42725216e45de4d1d5e275739197a66a59c226`. Aggregate SHA-256 over the 64 saved transcript filenames and bytes (sorted filename order, NUL-delimited) is `aa7314c25f7bf43dd844fb6b44d10c421d801d21a0316f863ce36a38692e885f`.

Ran the seven available `r22-*` fixtures. Results (each violation exit 1 except valid-order exit 0):

- `r22-clean-inversion`: inversion only.
- `r22-malformed-only`: one `expected event-id strings` finding only.
- `r22-mixed-first`, `r22-mixed-last`, `r22-multiple-invalid`: row-level malformed finding first, then preserved inversion.
- `r22-self-repeated`: malformed finding first, then self/repeated findings in member order; self-reference also retains the existing inversion result.
- `r22-unknown-mixed`: malformed finding first, then unknown event finding.
- `r22-valid-order`: clean, zero violations.

The mixed controls establish that string members remain inspectable regardless of malformed-member position. They do not establish source-text chronology or canon; only input-field checks are reported. Non-string members and their purported edges remain unassessed.

## Limits

Replay coverage establishes compatibility only for these 64 saved inputs; scout inventory found no mixed string/non-string dependency list among them. Fixture coverage is limited to the seven `r22-*` cases present when run. No independent review or axis verdict is claimed here.
