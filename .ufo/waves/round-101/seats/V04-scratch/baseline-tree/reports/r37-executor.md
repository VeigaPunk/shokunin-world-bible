# Round 37 executor — ledger endpoint duplicate

Baseline: `.shokunin/lore/corpus/fixtures/r35-bell7-conflict/`. Created the two requested copies. No existing fixture, checker, LOG, or README was edited; no commit was made.

## Byte comparison against r35 source

`r37-ledger-unique/`: all nine inherited files are byte-identical: `sources.json`, `entities.json`, `relations.json`, `timeline.json`, `contradictions.json`, `tarin-note-excerpt.md`, `clause-map.md`, `sella-bell7-note-excerpt.md`, `manual-clause-pointer-map.md`.

`r37-ledger-ambiguous/`: eight of nine inherited files are byte-identical: every file above except `timeline.json`. The ambiguous timeline is the only changed inherited file; its original four parsed event objects remain unchanged and in order, with the original `tarin-envelope-observation` object appended as `timeline[4]`. This appended object is byte-for-byte equivalent as a JSON value to original `timeline[2]`. JSON textual delta is one appended array object and comma/newline formatting; no original event is changed. The duplicate ID has 2 timeline occurrences; claim_a target therefore has 2. claim_b `sella-bell7-presence` has exactly 1 occurrence. Contradiction pair and all other inherited files (including sources/excerpts) are untouched.

## Checker runs

Command for each: `python3 .shokunin/lore/corpus/fixtures/check_bible.py <fixture-directory>`

Unique control — exit 0; stdout:
```text
CLEAN: schema, citations, relations, timeline; 0 violations
```
stderr: empty.

Ambiguous case — exit 1; stdout:
```text
VIOLATION: timeline[4].id: duplicate timeline id 'tarin-envelope-observation'
VIOLATION: contradictions[0].claim_a.event_id: expected exactly one timeline event 'tarin-envelope-observation'
2 violation(s); no canon changed
```
stderr: empty.

This records checker output only. It demonstrates duplicate-ID detection and the claim_a exact-one lookup failure for this input; it does not resolve the attributed reports, establish source truth, or add semantic/canon inference.
