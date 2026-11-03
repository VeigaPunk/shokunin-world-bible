# lore: curated source to consider, batch 4 — 2026-11-03

**Status: unassimilated post-hyaku reading.** No training, canon changes, schema migration or candidate execution.

## Web Annotation: identify the passage before assessing the claim

**Source and revision:** [Web Annotation Data Model](https://www.w3.org/TR/2017/REC-annotation-model-20170223/), W3C Recommendation of 23 February 2017. Opened 2026-11-03.

**Source summary:** TextQuoteSelector describes normalized text with optional surrounding context. Multiple remaining matches are not automatically reduced to one. TextPositionSelector uses start-inclusive, end-exclusive character positions, counted as Unicode code points rather than code units. Position selectors are brittle under edits; the specification recommends an accompanying State to identify the representation. These mechanisms locate evidence without evaluating its truth.

**Read first:** §4.2.4 Text Quote Selector, §4.2.5 Text Position Selector and §4.3 States. Read normalization and ambiguous-match rules before examples.

**Domain gap and novelty:** Existing PROV records attribution and revision, SHACL checks declared structure, and ink models narrative state. This adds passage identity inside a cited in-world document, supporting the claim-to-excerpt gate when repeated wording or editorial changes make a citation ambiguous. Web Annotation/Open Annotation and the selector aliases were absent from the reviewed inventory; W3C publisher overlap is not a repeat of PROV or SKOS.

**Rights:** The currently linked [W3C document-use license, 2023 version](https://www.w3.org/copyright/document-license-2023/) conditions copying on source, copyright and status notices, with limits on derivative documents. The document license grants no rights over annotated stories; redistribution and AI-training permission remain separate.

**Original future question, not performed:** Can a lore citation remain explicitly ambiguous instead of silently attaching itself to the wrong repeated sentence? After hyaku, propose an original two-edition witness statement with duplicate wording, an inserted paragraph and a non-BMP character before the cited passage. Compare quote and position selectors against the named edition. Require separate unresolved, multi-match and uniquely located outcomes, leaving the underlying claims unchanged.

**Limits:** A located passage may still be false or contradicted. Selection cannot establish canon, settle competing testimony or substitute for semantic support review.

