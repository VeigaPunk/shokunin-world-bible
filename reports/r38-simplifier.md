# Round 38 simplifier — minimum duplicated endpoint-source probe

## Minimal change

Use two independent copies of `.shokunin/lore/corpus/fixtures/r35-bell7-conflict/`: an unchanged unique-source control and a negative that adds exactly one copied row to `sources.json`. The endpoint already cites `sella-bell7-note` (`sources.json:21-25`; `timeline.json:32-39`), and the two ledger event IDs are distinct (`timeline.json:23-39`; `contradictions.json:4-10`). Append a byte-identical copy of the existing Sella source row (rather than inventing a competing title or reliability claim). Leave the excerpts, timeline, event IDs, ledger, and all other files unchanged. Do not mutate the original r35 fixture.

This is the narrow missing branch: after a uniquely identified ledger endpoint event is fetched, the checker checks that event's source and reports ambiguity on that ledger side (`.shokunin/lore/corpus/fixtures/check_bible.py:92-100`). The expected endpoint-local finding is `contradictions[0].claim_b.source_id: ambiguous in-world source 'sella-bell7-note'`; duplicate indexing should also report the appended duplicate source ID. `claim_a` cites `tarin-note` and remains unique (`sources.json:15-19`, `timeline.json:23-30`). No checker change is warranted.

## Risks and limits

Duplicating the source ID makes the identity of the citation ambiguous; it does not establish that either copy is canonical, select a winner, invalidate the authored account, or make the reported event false. The event pointer remains unique; the ambiguity is specifically its cited source. Do not characterize the checker as proving a contradiction or selecting between Tarin and Sella. Keep the probe to one added row: changing source text, event identity, ledger fields, or excerpt wording would confound the coverage axis. Existing r7/r31 duplicate-source cases cover alliance/relation citations, not this two-sided ledger endpoint branch (`reports/r7-simplifier.md:5-13`; `reports/r31-simplifier.md:5-17`).

## Falsifiable check

Run `python3 .shokunin/lore/corpus/fixtures/check_bible.py <control-dir>` and the same command on the negative. Control must exit 0; negative must exit 1 and include the duplicate-ID finding plus the endpoint-local `claim_b.source_id` ambiguity above. Capture all output and verify no unanticipated collateral finding is concealed. Confirm the only fixture delta is the single appended byte-identical source row; both event IDs and ledger pointers remain unique/unchanged, and the original r35 tree is untouched. If either expected diagnostic is absent, control is not clean, or any other fixture input changes, the proposed coverage claim fails. This proves structural citation ambiguity only, not source authenticity, rights, account truth, or canon resolution.

Scope: report only; no fixture, checker, LOG, README, or commit changes.
