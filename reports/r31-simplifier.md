# Round 31 simplifier: minimal fixture-only artifact

## Evidence and decision

The existing `r7-ally-reverse-ambiguous` fixture already contains an ambiguous in-world citation: its reverse `allied_with` relation has `source_id: harbor-compact` (`.shokunin/lore/corpus/fixtures/r7-ally-reverse-ambiguous/relations.json:9-13`), and `sources.json` repeats that ID at rows 3 and 15 (`.shokunin/lore/corpus/fixtures/r7-ally-reverse-ambiguous/sources.json:3-6,15-19`). Thus do not claim ambiguous relation citations are wholly untested. It does not cover the selected non-alliance `carries` case.

Minimal controlled pair: clone `consistent/` as two new fixture directories, preserving every JSON file except `sources.json` in the ambiguous member. The control retains the single `courier-log` source (`consistent/sources.json:8-13`); the ambiguous member appends a second structurally admitted source row with ID `courier-log`. Keep the relation exactly as-is in both (`consistent/relations.json:2-7`: mira -> seal, carries, source_id courier-log). Do not add prose or alter the relation. This is fixture-only input, not a checker rule or a claim about canon.

## Expected test and scope

Run the documented checker against both fixture directories. Control should exit 0. Ambiguous case should include `relations[0].source_id: ambiguous in-world source 'courier-log'`, plus any other legitimate diagnostics; record the complete stdout/stderr/exit delta rather than attributing all output changes to the relation. The test is manual replay of the pair; no checker edits. For regression, replay the declared 81 prior fixture outcomes and compare 404 prior JSON path bytes to the baseline, as specified in `.shokunin/lore/LOG.md` (Round 31 declaration). A successful result supports only coverage of an ambiguous citation on a non-alliance relation input class; it does not establish relation falsity, source authenticity, or citation rights.

## Risks

- The r7 precedent means novelty is narrow: generic relation-source ambiguity exists already in an alliance example. The new pair must isolate relation type as the distinguishing coverage.
- Duplicate IDs intentionally make citation identity unresolved; they do not show that the carrying assertion is true or false.
- Other checker findings may accompany the targeted diagnostic, so report the exact delta and avoid claiming a relation-only diagnostic.
- Do not interpret the fictional source row as real-world evidence or as canon.
