# Round 26 regression-scout — baseline replay plan

## Scope and exact baseline

Round 26 declares baseline work commit `0bc30269b07f05dd79eb45d3a217d3027bf1edf4` and baseline report commit `f44e7281a5438dc86e4fd8a03b19476e4cce7371` (`.shokunin/lore/LOG.md:383`). The requested regression scope is all 75 existing directories and 374 existing JSON paths under `.shokunin/lore/corpus/fixtures/` (observed directory/file counts). Treat the **work commit** checker and fixture corpus as the oracle; do not use the evolving checker as its own baseline.

## Replay protocol

From the repository root, enumerate sorted immediate fixture directories and recursively enumerate sorted `*.json` relative paths. For each directory run the baseline and candidate checker in separate invocations, capturing exit status, stdout bytes, and stderr bytes; compare each tuple exactly. Preserve per-directory records so any delta names its fixture and distinguishes stdout, stderr, and status. Independently compare baseline and candidate bytes for every pre-existing JSON relative path, including paths under each fixture; require 374/374 identical. Do not include newly proposed r26 fixture paths in this old-corpus identity comparison. Record actual command, baseline revision, counts, and aggregate unchanged count in the verifier report; this plan is not evidence that replay has occurred.

A suitable baseline extraction is `git show 0bc30269b07f05dd79eb45d3a217d3027bf1edf4:.shokunin/lore/corpus/fixtures/check_bible.py`; replay its content against the checked-out fixture directories only after verifying those directories match the declared baseline. If baseline corpus identity cannot be established, report that as a blocker rather than silently calling current fixtures historical baseline.

## Expected scoped behavior and risk

The checker admits a section row only after every required field has the declared exact type and nonempty-string condition (`check_bible.py:21-43`). Entity ID indexing and duplicate counts use only those admitted rows (`check_bible.py:45-58,118-129`). Thus a duplicate target row missing one required field should produce its schema violation but should not contribute to duplicate entity count or make the cited relation's `to` ambiguous. The admitted duplicate control should retain the r25 endpoint ambiguity; this is a screening-boundary calibration, not proof that malformed evidence is false, absent, or non-canon. Main risk: a test or report could mistake absence of ambiguity for proof of a unique real-world referent, or overlook other independent violations. Exact replay guards against collateral output changes; JSON byte identity guards against accidental fixture edits.

## Focused test

Make only one required-field mutation to the second `seal` entity row in a copy of `r25-to-ambiguous`, keeping the first valid `seal`, relation, and citation unchanged. Prefer deleting one required field (rather than changing unrelated rows); verify the resulting row is malformed and all other JSON rows/bytes match the admitted-duplicate case. Run the checker on that case, `r25-to-ambiguous`, and `r25-to-unique`: expect malformed case exit 1 with the selected field's required-field diagnostic and no `relations[0].to: ambiguous entity 'seal'`; admitted duplicate still has that ambiguity; unique control has no such ambiguity. These expected outcomes must be observed by an independent replay before calibration is admitted.

## Evidence locations

- Round declaration, exact baseline revisions and 75/374 acceptance condition: `.shokunin/lore/LOG.md:383-385`.
- Row admission gate: `.shokunin/lore/corpus/fixtures/check_bible.py:21-43`.
- Indexing from valid rows: `.shokunin/lore/corpus/fixtures/check_bible.py:45-58`.
- Duplicate count and relation endpoint ambiguity: `.shokunin/lore/corpus/fixtures/check_bible.py:118-129`.
