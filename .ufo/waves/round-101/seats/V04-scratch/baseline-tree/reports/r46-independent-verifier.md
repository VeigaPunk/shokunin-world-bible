# Round 46 independent verifier report

## Baseline and comparison

Pinned baseline commit: `9bcd67fadaa9e02c7f973c3c52d69ba8a7f6c2b8`. I extracted `git archive` to `/tmp/lore-r46-baseline-5gv4lr8h` as a separate root and compared it with the current working root. Both have **95** immediate fixture directories and **474** fixture JSON paths; their path sets match. All 474 JSON files and `check_bible.py` are byte-identical. There is no `r46` fixture directory. These counts refer to the fixture corpus, not active story truth.

## Full replay

For every one of the 95 fixture directory names, I ran in each root the identical argv from that root (using its root as cwd):

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture-directory>
```

Compared raw process return status, stdout bytes, and stderr bytes. **95/95 triples match exactly; zero differences.** This is replay equivalence, not a semantic correctness or calibration verdict.

## Limits

This verifies only these committed inputs and checker execution. It does not establish source truth, provenance/identity, prose entailment, or canon. I make no inference about a planned one-clause variant: this replay does not show that variant was executed or identify an executed candidate. No checker or fixture was changed; only this report was written.
