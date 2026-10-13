# Round 41 independent verifier (non-author)

## Pinned-baseline replay

Pinned baseline report commit: `fc8f1c395f08249064e2d0edc8873203845ac1ee`. I extracted it with `git archive` into a separate temporary root, enumerated fixture directories and JSON paths there, and ran each baseline fixture using the identical root-relative argv from both roots: `python3 .shokunin/lore/corpus/fixtures/check_bible.py <fixture-dir>`. Compared raw stdout bytes, raw stderr bytes, and process exit status. **93/93** baseline fixtures match exactly between archive and current roots. The baseline contains **93 fixture directories** and **464 JSON paths**; all **464/464** baseline JSON files remain byte-identical in the current root. No baseline fixture/checker replay or JSON regression observed.

## r40/r41 target comparison

The five JSON files (`entities.json`, `sources.json`, `relations.json`, `contradictions.json`, `timeline.json`) are byte-identical between `r40-vela-listener` and `r41-vela-direct-bell`. All ten inherited files except the Vela excerpt are byte-identical: `clause-map.md`, `contradictions.json`, `entities.json`, `manual-clause-pointer-map.md`, `relations.json`, `sella-bell7-note-excerpt.md`, `sources.json`, `timeline.json`, and `vela-clause-map.md` are unchanged, as is `tarin-note-excerpt.md` (11 inherited files total, including the excerpt). The Vela excerpt changes from her report that she “heard two strokes I took to be the registry bell” to the direct identification “heard the registry bell strike twice.” The only new file is `strength-contrast-map.md`; `vela-clause-map.md` is inherited and byte-identical. No inherited fixture file other than the Vela excerpt changes, and no old JSON row is altered (all JSON tables are identical).

I independently ran the checker on both targets with argv `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture>`. Both exited **0**, stdout exactly `CLEAN: schema, citations, relations, timeline; 0 violations
`, stderr empty. The round-41 README also explicitly documents both commands and their structural limitation.

## Structural result versus source-text epistemics

These executions establish structural JSON/pointer consistency only. The checker does not inspect the prose and cannot validate Vela's source authenticity, objective registry-bell origin, stated date, or non-sighting. The direct wording is a stronger *attributed report* than r40's tentative identification; unchanged JSON wording “she took to be” is compatible as a weaker summary but loses that confidence distinction, as the new contrast map itself says. Neither fixture establishes objective bell fact, Sella/envelope absence, synchronized chronology, or canon. This report records a replay/preservation check, not an authorial or canon determination.
