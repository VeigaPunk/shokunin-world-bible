# Round 32 scribe: raw versus admitted source rows

## Decision table

This table describes the existing source-row screening and source-ID reference checks; it proposes no checker rule. A JSON source row enters `data["sources"]` only after all required fields pass screening (`.shokunin/lore/corpus/fixtures/check_bible.py:21-43`); source indexing and duplicate-ID diagnostics consume that admitted list (`:45-56`). `source_status()` counts those same admitted rows (`:64-74`).

| Raw rows for a source ID | Admitted matching rows | Expected local/checker result | Bounded interpretation |
|---|---:|---|---|
| None | 0 | A reference gets `unknown in-world source`; no duplicate-ID finding | No admitted match in this input. |
| One complete row | 1 | No source-resolution finding | Unique ID in the admitted fixture index only. |
| Two complete rows | 2 | Duplicate source-ID finding and `ambiguous in-world source` at each reference to that ID | No row is selected as unique; references remain unresolved. |
| One complete row plus a same-ID row with a blank required `title` | 1 | Row-local `sources[i].title: required nonempty str`; no duplicate-ID finding and no ambiguous-reference findings from the excluded row | The raw duplicate remains present; absence of ambiguity means only one matching row was admitted. It says nothing about canon or evidentiary truth. |

The relation source check calls the generic `source()` helper (`check_bible.py:123-130`), while entity first-appearance/claim and timeline source fields also call it (`:107-116`, `:161-183`). Consequently a duplicate source can fan out across references; do not frame the expected delta as relation-only.

## Pair evidence and precedent

Round 31's declaration records the admitted duplicate-source baseline and explicitly notes the missing malformed-duplicate probe (`.shokunin/lore/LOG.md:496-499`). Its unique control has one `courier-log` source row (`.shokunin/lore/corpus/fixtures/consistent/sources.json:8-13`). The admitted duplicate fixture has the original row and a second complete same-ID row (`.shokunin/lore/corpus/fixtures/r31-source-ambiguous/sources.json:8-19`). References remain unchanged in the paired fixture; for example the relation cites `courier-log` (`.shokunin/lore/corpus/fixtures/r31-source-ambiguous/relations.json:1-7`). The r31 declaration expects the admitted duplicate to produce eight findings, covering the duplicate ID and seven references (`.shokunin/lore/LOG.md:498`).

Round 26 is a precedent for the *screening pattern*, not source-specific coverage: its scribe states malformed entity rows are excluded from `data['entities']` and ID counts, while their schema error remains (`.shokunin/lore/reports/r26-scribe.md`, decision table and evidence). Here the relevant source schema is distinct: `title` is required as a string (`check_bible.py:8-10`), and blank strings fail the required nonempty check (`:37-43`). Do not claim malformed-source screening itself is novel; this round probes the source-ID/reference consequence with the controlled source pair.

## Risks and falsifiable test

**Risks.** Do not say the malformed raw source is deleted, false, irrelevant, non-canonical, or absent from the fictional world. Precisely: it remains in raw JSON but is excluded from this checker's admitted source rows and `source_id_counts`. A unique admitted ID is not proof of source authenticity, textual support, canon, real-world rights, or training permission. A duplicate-ID diagnostic does not falsify any cited claim. Count all output changes rather than attributing every ambiguous citation to the relation.

**Test.** Starting with `r31-source-ambiguous`, change only the second `courier-log` row's `title` from its nonempty string to `""`; retain its ID and all other bytes/fields. Compare that malformed pair with (a) the unchanged admitted duplicate and (b) `consistent/`. Falsifiable expectation: malformed case retains the raw second row and reports its required-title schema error, but has neither duplicate admitted source-ID nor ambiguous-source findings at the seven `courier-log` references; admitted duplicate retains the declared eight findings; unique control remains clean. Verify the one-field-only diff and exact stdout/stderr/exit for all three. As declared, replay all 83 pre-existing fixture outputs and verify the 414 pre-existing JSON path bytes remain unchanged (`.shokunin/lore/LOG.md:498`). These are expected checks, not observations by this scribe; no fixture/checker edits or canon/rights inference are made here.
