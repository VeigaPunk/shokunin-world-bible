# lore: graphs, datasets and unasserted propositions

Candidate reading only, checked 2026-11-03. Assimilation requires the user’s later manual instruction. No parser trials, corpus edits, canon decisions or assimilation occurred. This is a standards-history comparison with a current draft frontier, not evidence that the newest representation improves narrative quality.

## Timeline and source roles

- **2004 baseline:** [RDF Concepts and Abstract Syntax](https://www.w3.org/TR/2004/REC-rdf-concepts-20040210/), Recommendation dated February 10, defines graph-based assertions. A useful historical baseline is a collection of ordinary triples, with source/claim records modeled explicitly rather than assumed from storage layout.
- **2014 organization:** [RDF 1.1 Concepts](https://www.w3.org/TR/2014/REC-rdf11-concepts-20140225/), Recommendation dated February 25, adds datasets containing a default graph and named graphs. Section 4 warns that a graph name need not denote its graph. The same-day [dataset-semantics Working Group Note](https://www.w3.org/TR/2014/NOTE-rdf11-datasets-20140225/) explicitly says dataset semantics were not standardized. A Note is not another Recommendation.
- **2026 frontier:** the [RDF 1.2 Concepts snapshot](https://www.w3.org/TR/2026/CR-rdf12-concepts-20260407/), April 7, is a **Candidate Recommendation Snapshot**. The [current publication endpoint](https://www.w3.org/TR/rdf12-concepts/) still resolves to that status on this check and identifies RDF 1.1 as the latest Recommendation. Sections 1.5 and 3 introduce triple terms in object position and reifiers. Describing an unasserted proposition does not assert it; multiple reifiers can relate to the same proposition. Parser support and final standardization must not be presumed.

## What changes, what survives

For a world bible, these are different tools: a graph expresses relations, a dataset organizes graphs, and a reifier can distinguish an utterance or belief from its proposition. The newer mechanism does not decide whether a witness is reliable, a statement is canon, or two contradictory accounts should be reconciled.

My proposed design rule is to keep claim identity, speaker, source passage, time and canon status explicit regardless of representation. Existing PROV, SHACL and Web Annotation notes remain complementary baselines: attribution, structural validation and passage targeting do not themselves establish truth. Retaining an ordinary RDF 1.1 claim-record model is sensible when available tools cannot round-trip the candidate syntax, or when interoperability matters more than shorter expressions. Named graphs remain useful for grouping, provided their interpretation is documented rather than inferred from a convenient name.

## Original post-hyaku comparison question

Can the same two witnesses' incompatible reports be represented as ordinary claim records, named-graph groups and RDF 1.2 reifiers without accidentally asserting either report as canon? Compare stable claim identity, source preservation and round-trip loss; explicitly test an unsupported-parser outcome. No such experiment has run.

**Rights:** Copyright © 2004–2026 W3C. Source-specific status and links are preserved. The 2026 snapshot links a permissive document license; earlier documents use W3C document-use terms. This original synthesis reproduces no specification examples, diagrams, story text or code and grants no rights to narrative source material.
