# Round 29 positive lexical map scout

## Exact r28 positive evidence

- The excerpt is expressly labeled newly authored fictional in-world material and gives one sentence: “I, Mira, carried the blue seal.” (`.shokunin/lore/corpus/fixtures/r28-courier-excerpt/courier-log-excerpt.md:1-3`). The literal clause contains first-person speaker, carrying event, and blue-seal object; it does not name record IDs.
- The map identifies the text-to-record step as an editorial stipulation: Mira → `entities` ID `mira`, blue seal → ID `seal`, explicitly not lexical entailment or external verification (`.shokunin/lore/corpus/fixtures/r28-courier-excerpt/relation-clause-map.md:7-9`).
- Conditional on those fixture-local alignments, “carried” is the lexical basis for `type=carries`, with subject/object mapped to `relations[0].from=mira` and `.to=seal`; map scope is only `relations[0]` (`.../relation-clause-map.md:11-13`). The actual row has those endpoints, `type: carries`, and `source_id: courier-log` (`.../relations.json:2-7`); the source registry labels that ID as a fictional first-person log (`.../sources.json:9-13`). The registry is metadata, not proof that the sentence occurred in an independently existing source.
- The map excludes all other JSON claims/events and says checker reads neither Markdown; it disclaims ownership, duration, destination, provenance, and canon (`.../relation-clause-map.md:15-17`).

## Calibration / risk

The positive supports the narrow lexical predicate “carried” as `carries`, conditional on the declared editorial subject/object identity alignment. Do not inflate that to authenticated citation, external source truth, or canon. A reader could otherwise mistake a well-mapped fictional example for evidence that the JSON relation is factually true. Conversely, absence of an entailment is not a contradiction: if a paired clause merely says the seal was near Mira, classify `carries` as unsupported by that clause, not false in canon. This preserves separation between textual entailment and world-truth.

## Falsifiable test

Keep the five r28 JSON tables and source IDs byte-identical; replace only the excerpt sentence with “The blue seal was near Mira.” In a manual clause map, retain the same explicit editorial ID alignments, then ask a reviewer blind to the expected label whether the clause entails that Mira carried the seal. Expected: reject support for `relations[0]` because proximity does not entail carrying, while explicitly labeling the relation unsupported by this excerpt—not contradicted or canonically false. Control: with the original r28 sentence and same alignments, reviewer accepts narrow lexical support. If either decision changes due to the wording while IDs/JSON stay fixed, or the negative is called false rather than unsupported, the calibration claim fails.
