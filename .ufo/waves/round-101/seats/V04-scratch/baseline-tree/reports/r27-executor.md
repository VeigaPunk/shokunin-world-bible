# Round 27 executor report

Created `corpus/fixtures/r27-target-only/` and `corpus/fixtures/r27-both-ambiguous/` by copying all five JSON tables from `r25-to-ambiguous`. The control retains its duplicate `seal` row only. The both case appends one structurally admitted character row: `id: mira`, `name: Mira in courier ledger`, `first_appearance: courier-log`, `claims: []`. No unsupported claim was added.

The pair differs only by that extra `mira` entity row. `sources.json`, `relations.json`, `timeline.json`, and `contradictions.json` compare byte-identically.

Commands and exact results:

```text
$ python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r27-target-only
VIOLATION: entities[4].id: duplicate entities id 'seal'
VIOLATION: relations[0].to: ambiguous entity 'seal'
2 violation(s); no canon changed
exit: 1

$ python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r27-both-ambiguous
VIOLATION: entities[4].id: duplicate entities id 'seal'
VIOLATION: entities[5].id: duplicate entities id 'mira'
VIOLATION: relations[0].from: ambiguous entity 'mira'
VIOLATION: relations[0].to: ambiguous entity 'seal'
VIOLATION: timeline[0].entity_id: ambiguous actor entity 'mira'
VIOLATION: timeline[1].entity_id: ambiguous actor entity 'mira'
6 violation(s); no canon changed
exit: 1
```

The additional timeline ambiguity findings arise because the copied fixture already refers to `mira` in two timeline rows; they are not changes to timeline data. This demonstrates simultaneous endpoint diagnostics in this fixture, alongside those downstream findings. It establishes no canon truth, identity resolution, or relation truth.
