# Round 32 collateral citation diagnostics scout

## Scope and evidence

Read-only inspection of checker citation call sites, Round 31 pair report, and Round 26 malformed-entity screening precedent. No checker, fixture, LOG, or README changes. The r32 declaration in `.shokunin/lore/LOG.md` requires blanking the second duplicate source row’s `title`; the question is the collateral fan-out of an excluded source row, not whether malformed screening is novel.

The seven ambiguous reference findings reported in the admitted r31 duplicate pair are four entity citations, one relation citation, and two timeline citations. The exact output is recorded at `.shokunin/lore/reports/r31-executor.md` (r31-source-ambiguous output); its control is byte-identical to `consistent/` and exits 0. Their relevant unchanged citation sites are `consistent/entities.json:1` (`mira` first_appearance), `entities.json:1` claims[0], `entities.json:4` first_appearance, `entities.json:4` claims[0], `relations.json:1`, and `timeline.json:1-2` (source rows). Together these account for seven references to `courier-log`.

## Screening and collateral paths

At `corpus/fixtures/check_bible.py:21-43`, required fields are checked before rows enter `data[section]`; a missing, wrong-type, or blank required string emits a row-local error and excludes that row. `sources` requires `id`, `title`, `kind`, and `reliability_note` (`:8-14`). Thus blanking only the second duplicate row’s title should exclude it while preserving the original valid `courier-log` row.

The source index and multiplicity are built from screened `data['sources']` (`check_bible.py:45-56`), and `source_status` yields ambiguous only when that screened count exceeds one (`:64-74`). Each of the seven citations goes through `source()` at the entity, relation, or timeline loops (`:123-130`, `:293-303`, with entity citation handling at `:108-116`). Therefore those seven ambiguous-reference findings should disappear when the malformed duplicate is excluded. The row-local `sources[2].title: required nonempty str` finding should remain. The duplicate-ID finding should disappear too: `index('sources')` only sees admitted rows (`:45-51`). This predicts eight findings in the admitted duplicate case (duplicate ID plus seven citations) versus one title-schema finding in the malformed case, assuming no independent errors introduced.

Round 26 precedent documents the same ordering for entity rows: schema screening precedes indexing and ID counts, and malformed duplicate rows do not contribute to endpoint ambiguity (`reports/r26-screen-scout.md`, especially Evidence and Test). That is precedent for the structural pattern, not evidence that source-specific behavior was previously tested.

## Risks and falsifiable test

Risk: do not describe the raw duplicate as gone, nonexistent, or resolved. It remains in JSON, but this checker’s admitted-source index/count excludes that row. The surviving unique count is an implementation-level result, not a claim about fictional-world source identity or truth. Also do not infer canon, authenticity, source-text support, copyright, licensing, or AI-training permission from the reduced diagnostics.

Falsifiable test: compare the unchanged r31 unique control, admitted-duplicate r31 fixture, and a temporary/new malformed-source copy where exactly the second `courier-log` row has `title` changed to `""`. Assert exact stdout/stderr/exit; expect control exit 0, admitted duplicate exit 1 with eight findings, malformed case exit 1 with only `sources[2].title: required nonempty str` among source-duplication and citation findings (no duplicate ID and none of the seven ambiguous references). Then replay the 83 existing fixture outputs byte-for-byte at stdout/stderr/exit and verify all 414 prior JSON path bytes unchanged. A mismatch—especially any of the seven ambiguous citation lines remaining, or loss of the title error—falsifies the collateral prediction. Depth and coverage should remain unharmed; this is one calibration axis only.
