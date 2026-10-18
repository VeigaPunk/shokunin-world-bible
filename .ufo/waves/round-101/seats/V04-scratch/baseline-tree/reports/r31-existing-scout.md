# Round 31 existing-coverage scout

## Prior coverage and ambiguity

- The r7 fixture is `.shokunin/lore/corpus/fixtures/r7-ally-reverse-ambiguous/relations.json:8-13`. Its `relations[1]` is `bell-wardens -> quay-guild`, type `allied_with`, with `source_id: harbor-compact` at line 12. The matching source ID appears twice in `.shokunin/lore/corpus/fixtures/r7-ally-reverse-ambiguous/sources.json:3` and `:15` (the second row is identified at line 16). Thus r7 already covers a relation with an ambiguous in-world citation; it is specifically an alliance reverse edge, not a generic `carries` relation. Do not claim ambiguous relation citations are wholly uncovered.
- The generic relation citation path calls `source(...)` for each relation: `.shokunin/lore/corpus/fixtures/check_bible.py:64-74` defines unknown/unique/ambiguous status and reports `ambiguous in-world source`; `.shokunin/lore/corpus/fixtures/check_bible.py:100-105` (relation validation) applies it. Alliance reciprocity is separately special-cased at `:210-226`, including qualification by unique source. The existing r7 case therefore does not demonstrate the generic non-alliance relation path in isolation.
- The r7 scout already documents the distinction: `.shokunin/lore/reports/r7-fixture-scout.md` (“Proposed paired fictional-source fixtures,” alliance duplicate reverse citation) describes the ambiguous alliance reverse edge and calls for a unique-source control; its “Scope” says proposals are not observed behavior. The report also warns that source identity is not textual support. Avoid duplicating the alliance claim or presenting its proposal as a `carries` probe.

## Coverage gap and minimal test

A narrowly new input class remains: a non-alliance relation (`carries`) whose `source_id` is duplicated. `.shokunin/lore/corpus/fixtures/consistent/relations.json:1-7` gives the clean `mira -> seal / carries` relation citing `courier-log`; `.shokunin/lore/corpus/fixtures/consistent/sources.json:7-12` has one such source. A controlled pair can preserve the relation byte-for-byte and add a second structurally valid `courier-log` source row only in the ambiguous case. Expected behavior per round31 declaration: control clean; ambiguous variant reports `relations[0].source_id: ambiguous in-world source 'courier-log'` and any other legitimate findings caused by the duplicated ID. Inventory the entire output delta; do not imply relation-only output.

The duplicate ID means the citation is ambiguous in the fictional input, not that the relation is false, that either source record is selected, or that source text corroborates the claim. This is a coverage observation, not a request for a new checker rule: generic `source()` already emits the ambiguity diagnostic. Keep the change on the coverage axis only.

## Risks and verification

- **Duplicate-claim risk:** describe this as new coverage for a non-alliance relation citation, not first relation/ambiguous-citation coverage. R7's alliance case is real prior coverage.
- **Scope risk:** do not broaden into alliance reciprocal semantics, citation-rights conclusions, or canon assertions.
- **Diagnostic-count risk:** duplicate source row may trigger its own duplicate-ID finding; record every output line and exit status, not only the desired relation diagnostic.
- **Regression test:** run the checker on the clean control and the one-row-duplicated variant; verify control exit 0 and ambiguous case contains the exact relation ambiguity diagnostic plus all separately legitimate findings. Then replay all 81 prior fixture stdout/stderr/exit results and verify the 404 old JSON path bytes remain unchanged, as required by the round31 declaration.

Scout-only report. No checker, fixture, LOG, or README edits; no commit.
