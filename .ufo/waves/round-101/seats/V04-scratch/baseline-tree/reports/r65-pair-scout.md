# Round 65 pair scout — forward source status × reverse witness

## Scope and method

Independent calibration assessment of the proposed rule: withhold a derived “lacks a sourced reciprocal relation” finding when that *forward row* has an unknown or ambiguous source ID. No repository code or fixtures were changed. I made nine temporary copies of the committed fictional `ally-reciprocal` input under `/tmp/r65-pair-l_lx6g4i/`; both factions, all other tables, and relation shape were held fixed. The forward edge was `quay-guild -> bell-wardens`; reverse edge was absent, uniquely cited, or ambiguous. For unknown I used `ghost`; for ambiguity I duplicated `harbor-compact` in `sources.json`. Executed `python3 .shokunin/lore/corpus/fixtures/check_bible.py <tempdir>`.

## Actual current output

| Forward source | Reverse source | Relevant exact current stdout lines |
|---|---|---|
| unique | absent | `VIOLATION: relations[0]: allied_with faction relation 'quay-guild' -> 'bell-wardens' lacks a sourced reciprocal relation` |
| unique | unique | `CLEAN: schema, citations, relations, timeline; 0 violations` |
| unique | ambiguous | `VIOLATION: sources[1].id: duplicate sources id 'harbor-compact'`; `VIOLATION: relations[0].source_id: ambiguous in-world source 'harbor-compact'`; `VIOLATION: relations[1].source_id: ambiguous in-world source 'harbor-compact'`; plus missing-sourced-reciprocal lines for **both** `relations[0]` and `relations[1]` |
| unknown | absent | `VIOLATION: relations[0].source_id: unknown in-world source 'ghost'`; plus `relations[0] ... lacks a sourced reciprocal relation` |
| unknown | unique | forward unknown diagnostic; reverse row receives `relations[1] ... lacks a sourced reciprocal relation` (the reverse row’s own expected reciprocal is the unknown forward edge) |
| unknown | ambiguous | forward unknown; reverse ambiguous citation; duplicate `sources[1].id`; both relation rows report missing sourced reciprocal |
| ambiguous | absent | duplicate source ID; forward ambiguous citation; forward row reports missing sourced reciprocal |
| ambiguous | unique | duplicate source ID and ambiguous citation diagnostics on both relation rows; both rows report missing sourced reciprocal |
| ambiguous | ambiguous | duplicate source ID, ambiguous diagnostics on both relation rows; both rows report missing sourced reciprocal |

All runs exited 1 except unique/unique (exit 0); stderr was empty. Relevant findings above are verbatim; findings from relation endpoint validation and unrelated checks are omitted from table. In my first exploratory pass I accidentally replaced the source table with only source IDs, producing unrelated citation/dangling errors; those runs were discarded. The table above comes from corrected probes preserving the committed fixture’s source rows and valid endpoints.

## Code and precedent

Current checker lines 249–267 iterate each admitted `allied_with` row; after unique faction endpoint checks, `reciprocal = any(...)` asks only whether a reverse edge has `source_status(candidate['source_id']) == 'unique'` (263), and reports if no such reverse exists while sources are available (266–267). It never tests `source_status(row['source_id'])` for the forward row. Generic `source()` independently reports unknown/ambiguous forward citations, so the unqualified derived finding is demonstrably concurrent with the direct error, not a replacement for it.

R2 adjudication describes the rule as requiring a reversed row “with a source ID in the source index”; it does not establish forward-source qualification. R7 explicitly calibrated ambiguous **reverse** source IDs: unique-forward / ambiguous-reverse keeps the ambiguity findings and missing qualified reciprocal. Its reviewer also tested a separate uniquely cited reverse edge and found the forward missing finding disappears. R31 concerns non-alliance relation citation ambiguity, not forward eligibility. R61 gates alliance checks when source table unavailable; it does not settle loaded-table unknown/ambiguous forward IDs. These precedents support current reverse-witness qualification, but do not prescribe the proposed forward gate.

## GO / NO-GO: NO-GO for material calibration gain

The hypothetical policy would suppress only the forward row’s *derived reciprocal absence* when its own citation is not unique. Current direct unknown/ambiguous citation is already a repair pointer to that exact row, and with an unknown forward plus absent reverse the present output explicitly says both what citation needs repair and that no sourced reciprocal is available. The r7 uniquely cited-forward/ambiguous-reverse case already preserves local ambiguity diagnostics and rejects an unqualified reverse witness. I find no demonstrated operator action that improves by hiding the forward-derived pointer; conversely it can obscure that the reverse edge is also absent. In the unknown-forward/unique-reverse pair, the reverse row’s reciprocal finding remains because its reverse witness (forward edge) is unqualified; gating only the forward evaluation would create an asymmetric, more complex policy without resolving that diagnostic. The matched data establish a distinction, not material benefit. No candidate output was implemented or measured; no preservation claim is made.

**Falsifier for this NO-GO:** a concrete matched operator task where retaining the current missing-reciprocal finding alongside the direct citation error causes an incorrect repair choice, while suppressing it reliably improves that choice and preserves reverse-edge/source diagnostics. Mere preference for fewer lines would not suffice.

**Repair-pointer harm / smallest possible future test:** if independently justified, test a narrow condition at lines 260–267 that requires the current row’s own `source_status(row['source_id']) == 'unique'` before emitting its derived finding, while retaining all `source()` diagnostics and reverse checks. That would remove a useful relation-level pointer whenever forward citation is bad, so a future candidate must show why that loss is beneficial. Do not generalize to other relation checks.

The strings `ghost`, `harbor-compact`, and fixture source metadata here are input identifiers/fictional test data only. This assesses row membership/uniqueness, not source prose, support, alliance truth, canon, chronology, authorship, authenticity, ownership, copyright, license, permission, or rights.
