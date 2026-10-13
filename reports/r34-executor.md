# Round 34 executor report

Owned artifacts: `.shokunin/lore/corpus/fixtures/r34-tarin-hearsay/` and this report only. No checker, LOG, README, or existing fixture was edited; no commit made.

Copied the five JSON tables (`sources.json`, `entities.json`, `relations.json`, `timeline.json`, `contradictions.json`) byte-identically from `r33-tarin-envelope` (5/5 byte comparisons passed). Authored the required sole-sentence fictional excerpt and `modality-contrast-map.md`. The map distinguishes hearing an assertion from direct sight: unchanged `entities[tarin].claims` and `timeline[2].description` reports of seeing are unsupported by this excerpt as direct sight. Sella's placement remains attributed hearsay, neither verified nor false. IDs/tick are editorial metadata; no informant, contents, or canon is asserted. r33's “saw” contrast is included.

Checker commands and results:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r33-tarin-envelope
CLEAN: schema, citations, relations, timeline; 0 violations
exit 0

python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r34-tarin-hearsay
CLEAN: schema, citations, relations, timeline; 0 violations
exit 0
```

Five JSON byte comparisons: all **5/5 identical**.
