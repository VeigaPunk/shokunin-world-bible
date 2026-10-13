# Round 40 executor — Vela listener fixture

Created `.shokunin/lore/corpus/fixtures/r40-vela-listener/` as a copy of `r35-bell7-conflict`, retaining its nine inherited files. Added `vela-note-excerpt.md` with the exact requested two sentences, `vela-clause-map.md`, and append-only JSON additions: 1 source (`vela-note`), 1 character (`vela`, one attributed report claim), and 1 timeline event (`vela-listening-report`, actor `vela`, place `harbor`, tick 3, `depends_on: []`, source `vela-note`). No relation or contradiction/ledger row was added.

Preservation check: sources 4→5 (4 old rows identical and in original order); entities 6→7 (6 old rows identical and in original order); timeline 4→5 (4 old rows identical and in original order); relations 1→1 (all rows identical); contradictions 1→1 (all rows identical). All four inherited Markdown files compare byte-for-byte identical. The new clause map treats the east steps as broad harbor, distinguishes hearing/tentative identification from objective bell evidence, limits the non-sighting to Vela's report, and does not claim corroboration or canon.

Checker command: `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r40-vela-listener`
Exact stdout:
```
CLEAN: schema, citations, relations, timeline; 0 violations
```
Exact stderr: empty.
Exit code: 0.
