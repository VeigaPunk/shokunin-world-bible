# Round 58 independent preservation verifier

## Method

Pinned baseline: report commit `2ca7d08bbcda2fc4c404b1c47bc63cd4b87982c2`. I independently extracted its `git archive` to `/tmp/lore-r57-independent`, separate from the working tree. Comparisons used raw file bytes. Each fixture checker was run from its respective repository root, using the identical root-relative argv:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture-name>
```

For each invocation I compared exit status, stdout bytes, and stderr bytes.

## Results

- Corpus: 1,149 files in the pinned archive and 1,149 in the working tree; all paths and raw bytes match.
- Fixture directories: 95.
- Fixture JSON: 474 paths in each tree; all paths and raw bytes match.
- Checker executions: all 95 fixtures produced identical exit status, stdout, and stderr.
- Candidate status: no r58 candidate is present in this working tree; this is baseline preservation verification only, not evidence of depth or canon.

## Scope

This report verifies that the current corpus and fixture-checker behavior preserve the pinned r57 baseline. It does not assess or establish depth, correctness of canon, or candidate quality.
