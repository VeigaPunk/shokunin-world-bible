# Round 44 independent non-author verification

Baseline pinned to report commit `83d62fcde1badb26adfc6c0a99fd17dcd91c782a` (HEAD at verification). I extracted `.shokunin/lore/corpus/fixtures` from `git archive` into `/tmp/r44-baseline-83d62fc`, separate from the working tree, then replayed all fixture directories from each root.

- Enumerated **95** immediate old fixture directories and **474** root-relative JSON paths. Current inventory has the same 95 directory names and 474 JSON paths; both path sets match exactly.
- The fixture checker bytes are identical (SHA-256 both: `5a389f1f5c0ccf104d9109f7a4740f398a73d6b372ad82c4e9abb3d4a4052d27`); all 474 corresponding JSON file bytes are identical.
- For every old fixture directory, ran the identical root-relative argv `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<directory>` with cwd set first to the archive root and then to the current repository root. Compared captured raw stdout bytes, raw stderr bytes, and exit code: all 95 triples matched exactly.
- No r44-named fixture directory exists in that corpus. The fixture-scout report’s `/tmp/r44-place-actor-probe` path exists separately, but is not among the corpus directories and is not included in the 474 JSON paths.

This verifies fixture/checker preservation and byte-for-byte replay equivalence only. It makes no claim that the probe is semantically invalid, and no claim of new corpus coverage.
