# Round 40 independent verifier

## Baseline replay

Pinned baseline: `729e868b889e5d2ce2bf21dc139fe4a41655a95d`. Extracted it with `git archive` to a separate root, enumerated **92 fixture directories** and **459 JSON paths**, and ran each same root-relative command from both roots: `python3 .shokunin/lore/corpus/fixtures/check_bible.py <fixture-dir>`. Compared raw stdout bytes, raw stderr bytes, and exit status: **92/92 exact matches**. Baseline JSON bytes: **459/459 identical**. No old fixture/checker regression observed.

## Vela fixture independent execution

Command: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r40-vela-listener`

Exit **0**; stdout exactly:
```text
CLEAN: schema, citations, relations, timeline; 0 violations
```
Stderr empty.

## r35 preservation and deltas

Compared fixture `r40-vela-listener` to baseline commit `633ba022b45c71a9049664e1d9ac181950820aee`'s `r35-bell7-conflict`. All four inherited Markdown files (`clause-map.md`, `manual-clause-pointer-map.md`, `sella-bell7-note-excerpt.md`, `tarin-note-excerpt.md`) are byte-identical. JSON arrays preserve every old row as an identical prefix: `entities.json` 6→7 (+1), `sources.json` 4→5 (+1), `timeline.json` 4→5 (+1); `relations.json` remains 1, `contradictions.json` remains 1, both byte-identical. No old row rewritten; additions are appended to entities, sources, timeline only. Two new Markdown files are Vela's excerpt and clause map. Thus the unresolved Bell-7 ledger is unchanged.

The checker result establishes structural schema/pointer consistency, not the truth of authored source content. Vela's text is a fictional first-person assertion about hearing two strokes and taking them for the registry bell, with a stated non-sighting; it does not independently prove bell origin, actual chronology, Sella's location/presence, or envelope placement. The checker does not authenticate her statement or transform editorial tick 3 into shared real-world time. This report is a non-author replay/preservation check, not a canon or truth finding.
