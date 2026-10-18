# Round 34 pair scout — modality contrast

## Pair design

Use the existing r33 fixture as the positive control and a separate near-miss whose five JSON tables are byte-identical to r33; alter only the excerpt sentence. The contrast sentence is: “I, Tarin, heard that Sella placed an unlabeled paper envelope on the Lantern Harbor registry desk.” This is a report that Tarin heard an assertion, not a first-person claim of seeing the placement. Pairing it with unchanged rows explicitly stating “Tarin reports seeing” makes the prose/record mismatch legible, while structural validation can still pass both cases.

In r33, the excerpt explicitly says “I, Tarin, saw Sella place…” (`.shokunin/lore/corpus/fixtures/r33-tarin-envelope/tarin-note-excerpt.md:1`); its map scopes “saw” to Tarin’s reported observation, not independent verification (`.shokunin/lore/corpus/fixtures/r33-tarin-envelope/clause-map.md:5-7`). By contrast, the near-miss wording says Tarin heard an assertion. The unchanged Tarin and Sella claims assert “reports seeing” / “reports that Sella placed” (`.shokunin/lore/corpus/fixtures/r33-tarin-envelope/entities.json:51-72`), and the event says “Tarin reports seeing” (`.shokunin/lore/corpus/fixtures/r33-tarin-envelope/timeline.json:23-30`). The original authored source is identified as a fictional first-person note (`.shokunin/lore/corpus/fixtures/r33-tarin-envelope/sources.json:15-19`); source-ID citation alone does not ensure the excerpt supports the claims.

## One-sentence contrast

**r33’s “saw” supports Tarin’s direct-observation report, whereas the near-miss’s “heard that” supports only Tarin’s report of hearing an assertion—not direct sighting or the placement’s truth.**

## Risks and falsifiable check

Risk: collapsing hearsay into sight would miscalibrate evidence, but the pair does not show the hearsay is false; equally, r33 remains Tarin’s reported observation, not independently corroborated fact. Avoid treating matching source IDs or a clean structural check as prose entailment: the r33 report itself says the checker establishes structural/citation validity only (`.shokunin/lore/reports/r33-reviewer.md:31`). Do not infer envelope contents, recipient, ownership, Blue Seal/carbon/route-strip connection, intent, canon, rights, or game mechanics; the r33 map explicitly excludes these (`.shokunin/lore/corpus/fixtures/r33-tarin-envelope/clause-map.md:9-13`).

Falsifiable check: parse and byte-compare all five JSON tables of the positive and near-miss pair; require exact equality, with the excerpt as the sole changed prose artifact and the manual map accurately recording the modality contrast. Run the fixture checker on each and require exit 0, then have a non-author reviewer judge the near-miss **unsupported as direct-sighting evidence** while accepting r33 only as Tarin’s direct-observation report; rejecting the inference must not label the hearsay or r33 JSON false. Any JSON difference, altered additional claim, checker failure, or reviewer treating “heard that” as direct sight falsifies the stated pair check. Calibration is the sole axis; no claim of depth/coverage gain or harm.
