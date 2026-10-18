# Round 29 executor report

Created `.shokunin/lore/corpus/fixtures/r29-near-miss/` with the five JSON tables copied byte-identically from `r28-courier-excerpt/`: `entities.json`, `relations.json`, `sources.json`, `timeline.json`, and `contradictions.json` (all five byte comparisons: `True`). No JSON content was changed.

Added a newly authored fictional `courier-log-excerpt.md` containing the sole sentence “The blue seal was near Mira.” Added `negative-clause-map.md` assessing only `relations[0]`: its `carries` claim is **UNSUPPORTED BY THIS EXCERPT**, not contradicted or false, because proximity does not entail carrying. Mira/seal IDs are fixture-local editorial alignments, not lexical proof; other JSON claims are unassessed. The checker ignores Markdown; this makes no canon or source-truth claim.

Checker runs:
- `python .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r28-courier-excerpt` → exit 0; `CLEAN: schema, citations, relations, timeline; 0 violations`
- `python .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r29-near-miss` → exit 0; `CLEAN: schema, citations, relations, timeline; 0 violations`

Prose contrast: the positive r28 excerpt says “I, Mira, carried the blue seal,” lexically supporting the selected `carries` relation conditional on the editorial ID alignments. The r29 near-miss says only that the seal was near Mira, which does not support carrying. Both clean outputs are structural validation only, not prose validation or relation truth.
