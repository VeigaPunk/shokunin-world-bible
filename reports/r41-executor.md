# Round 41 executor — Vela direct bell

Created `.shokunin/lore/corpus/fixtures/r41-vela-direct-bell/` by cloning `r40-vela-listener`. The full inherited filename inventory is retained; the sole addition is `strength-contrast-map.md`. Changed only the requested clause in `vela-note-excerpt.md` from “heard two strokes I took to be the registry bell” to “heard the registry bell strike twice”; the remaining date and non-sighting text is preserved. The other ten inherited files are byte-identical to r40. All five JSON tables (`sources.json`, `entities.json`, `relations.json`, `timeline.json`, `contradictions.json`) are byte-identical.

The map records the distinction: r40 is a tentative Vela-attributed identification; r41 is her stronger direct identification, not objective evidence the bell rang. The unchanged fixed claim/event wording (“she took to be”) remains logically compatible as a weaker summary, but loses epistemic precision. It is not false or unsupported and creates no canon contradiction. Date/non-sighting remain source claims only.

For both fixtures ran `python3 .shokunin/lore/corpus/fixtures/check_bible.py <fixture-path>`.

r40 exact stdout:
```
CLEAN: schema, citations, relations, timeline; 0 violations
```
r40 exact stderr: empty. Exit: 0.

r41 exact stdout:
```
CLEAN: schema, citations, relations, timeline; 0 violations
```
r41 exact stderr: empty. Exit: 0.

Limits: this clone/byte comparison and structural checker establish artifact preservation and schema/citation/relations/timeline cleanliness only. They do not establish that a real bell rang, that the citation authenticates the account, or that Sella/an envelope were absent; nor do they adjudicate whether this calibration distinction is materially novel.
