# Round 30 executor report

Owned artifact: `.shokunin/lore/corpus/fixtures/r30-explicit-negation/` only.

Copied all five JSON tables from `r28-courier-excerpt/` byte-identically: `contradictions.json`, `entities.json`, `relations.json`, `sources.json`, and `timeline.json` (five of five byte comparisons equal). The sole fictional excerpt clause is: “I, Mira, did not carry the blue seal.” `textual-conflict-map.md` classifies it as a textual conflict with only `relations[0].type=carries`, conditional on editorial Mira/seal-to-ID alignment and same-proposition/occasion alignment. It does not claim canonical falsity, resolve the relation, or claim Mira never carried the seal. It distinguishes r28 positive lexical support from r29 proximity unsupported by that excerpt. The checker ignores Markdown; structural success is not prose validation.

Exact repo-root commands and results:

- `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r28-courier-excerpt` — exit 0; stdout `CLEAN: schema, citations, relations, timeline; 0 violations`; stderr empty.
- `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r29-near-miss` — exit 0; stdout `CLEAN: schema, citations, relations, timeline; 0 violations`; stderr empty.
- `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r30-explicit-negation` — exit 0; stdout `CLEAN: schema, citations, relations, timeline; 0 violations`; stderr empty.

No checker, LOG, README, or other files changed; no commit made.
