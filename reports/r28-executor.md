# Round 28 executor report

## Delivered

Created `.shokunin/lore/corpus/fixtures/r28-courier-excerpt/` with the five JSON files copied byte-for-byte from `consistent/`, and two authored Markdown artifacts. The excerpt is explicitly labeled “Newly authored fictional in-world excerpt” and its sole sentence is “I, Mira, carried the blue seal.” The manual map covers only `relations[0]` (`from=mira`, `type=carries`, `to=seal`), separating lexical content from fixture-local editorial source-to-ID alignment.

## Validation

From repository root, ran:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r28-courier-excerpt
```

Exit 0; output: `CLEAN: schema, citations, relations, timeline; 0 violations`. Compared each of `contradictions.json`, `entities.json`, `relations.json`, `sources.json`, and `timeline.json` as raw bytes against `consistent/`; all five comparisons were equal.

## Limits

Checker validation is structural and does not read Markdown or establish textual entailment. The map is manual; the editorial alignment of “Mira”/“blue seal” to IDs is distinct from the lexical entailment of carrying. All other JSON claims/events are unsupported by this excerpt. It establishes no ownership, duration, destination, provenance, or canon. The near-miss “the seal was near Mira” does not entail carrying and would not support `carries`. No checker, LOG, README, or other files were changed; no commit made.
