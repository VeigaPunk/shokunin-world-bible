# Round 47 independent verifier report

## Scope and pinned baseline

I verified the committed baseline `6959fecffd36542262b3499b4989afb25f23d654`. I created a separate archive root from that commit with `git archive` containing `.shokunin/lore/corpus`; replayed baseline fixtures from that root and the current repository root. Both invocations used the same argv from their respective roots: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture-dir>`.

## Results

- Enumerated 95 prior fixture directories in the pinned archive, with 474 JSON paths total.
- Replayed all 95 fixtures in both roots. Raw stdout bytes, raw stderr bytes, and exit status matched for all 95 (95/95 exact matches).
- Compared every one of the 474 fixture JSON files byte-for-byte between the archive and current root: all matched.
- Compared `check_bible.py` bytes: exact match.
- No `r47-*` fixture directory exists in the pinned baseline corpus.

## Limits

This verifies reproducibility and unchanged baseline inputs/checker for the enumerated corpus. It does not establish any proposed slip was executed or that its source is true. It makes no canon, source-authenticity, or semantic-truth finding.
