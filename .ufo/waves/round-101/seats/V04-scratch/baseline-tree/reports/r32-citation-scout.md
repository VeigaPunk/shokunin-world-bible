# Round 32 citation scout — source ID linkage and rights boundary

## Scope and evidence

Read-only calibration review of the proposed malformed duplicate-source probe. The round 32 LOG declaration at `.shokunin/lore/LOG.md:497-499` limits the claim to source-row admission and ID counting, explicitly says this is analogous to (not novel beyond) r26 entity screening, and bars canon or rights inference.

- `.shokunin/lore/corpus/fixtures/check_bible.py:21-43` validates required fields for every table row and adds a row to `data[section]` only if all fields pass. In particular, a blank `title` on a duplicate source should produce a row-local required-title error and keep that row out of `data['sources']`.
- `.shokunin/lore/corpus/fixtures/check_bible.py:45-56` indexes admitted source rows, reports duplicate IDs, then counts IDs from admitted `data['sources']`. `.shokunin/lore/corpus/fixtures/check_bible.py:64-74` maps those counts to unknown/unique/ambiguous and emits an ambiguity diagnostic for counts greater than one. `.shokunin/lore/corpus/fixtures/check_bible.py:107-117,123-130` applies source lookup to entity citations and relation citations; timeline lookups are at `:96-100` and `:186-194`.
- `.shokunin/lore/corpus/fixtures/r31-source-ambiguous/sources.json:8-19` contains the valid `courier-log` row and its duplicate. The duplicate is currently admitted: `.shokunin/lore/reports/r31-executor.md:17-24` records duplicate-ID plus seven ambiguous-reference findings (four entity, one relation, two timeline). That report also notes a separate pre-existing alliance fixture at `:31-36`; do not conflate it with the controlled `carries` pair.
- `.shokunin/lore/reports/r26-citation-scout.md:5-8,13-17` draws the relevant precedent: malformed entity-row screening is not evidence of absence, truth, canon, or rights. Its logic is analogous but its table and reference target differ.
- `.shokunin/lore/corpus/knowledge/reference-ledger.md:3-10` separately distinguishes real-world methodological references from fictional in-world source IDs and says no rights grant or AI-training permission is asserted.

## Boundary and risks

A `source_id` is an internal link to a fictional row in these fixtures. Unique/ambiguous/unknown describes whether this checker's admitted rows let it resolve that link. It does not establish that a source exists outside the fiction, is authentic or authoritative, supports a proposition, or is legally reusable. Likewise, excluding a malformed duplicate from the checker’s count does not make the raw row nonexistent and does not resolve the story's truth or canon. No real-world source text, rights assessment, or training-consent inference belongs in this test.

Risk: wording such as “citation invalidated” or “source removed” can imply evidentiary or legal conclusions. Prefer “row rejected by schema screening” and “no duplicate-ID/ambiguous-reference finding among admitted rows.” Preserve the fact that the raw duplicate remains in the fixture.

## Falsifiable test

Compare the existing `r31-source-ambiguous` input to its proposed new copy, changing only the second `courier-log` row's `title` from nonempty text to `""`; preserve every other byte/table. Run the existing checker. The prediction is one row-local `sources[2].title: required nonempty str` finding, with no duplicate `sources` ID and none of the seven ambiguous-reference findings attributable to the excluded duplicate. The unmodified admitted-duplicate case must retain its eight findings, and the unique r31 control must remain clean. A contrary output falsifies the predicted admission/count boundary. This tests structural linkage only—not factual support, truth, canon, authenticity, ownership, rights clearance, or permission to train.
