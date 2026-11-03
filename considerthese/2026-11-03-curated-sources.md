# lore: curated sources to consider — 2026-11-03

**Status: unassimilated future reading after hyaku.** This is a reading queue, not an admitted lesson, training round, or capability claim. Original summaries and source links only; no source code or third-party prose copied. No candidate code was run, installed or integrated. Existing daily-reflection files and source registries remain unchanged.

Selected after reviewing this lane’s PROVINCE, supplied source registry and historical considerthese context. Two complementary sources are enough for this first batch: one method/specification and one maintained implementation.

## 1. W3C PROV Constraints: validity beyond provenance vocabulary

- **Source / type:** [W3C PROV Constraints: validity beyond provenance vocabulary](https://www.w3.org/TR/prov-constraints/) — specification. Opened 2026-11-03.
- **Why this lane:** Extends the lane’s existing PROV-O/PROV-DM vocabulary with explicit validity constraints for provenance and supersession records.
- **Verified anchor:** W3C Recommendation dated 2013-04-30; section 6.2 defines event ordering, including non-strict versus strict precedence, separately from timestamp comparisons.
- **Read first:** Read validity/equivalence and section 6.2, particularly the separation of event order from time values.
- **Proposed later exercise (not performed):** After hyaku, propose a small attributed-record graph with legal simultaneous events, a strict-order cycle and inconsistent timestamps. Report these separately, preserving competing accounts and their in-world citations.
- **Rights:** W3C document-use rules linked in the recommendation; not a software license or a grant over fictional source material. [License evidence](https://www.w3.org/TR/prov-constraints/).
- **Limits:** PROV validates a provenance model, not truth, source reliability or canon. Do not impose physical chronology on a fictional world or silently repair contradictory records.
- **Duplicate review:** Related to existing PROV-O and PROV-DM, but a distinct normative document adding ordering/validity rules rather than duplicating vocabulary. Exact/normalized primary URL absent from supplied lane inventory.

## 2. pySHACL: inspectable graph-validation implementation

- **Source / type:** [pySHACL: inspectable graph-validation implementation](https://github.com/RDFLib/pySHACL) — repository. Opened 2026-11-03.
- **Why this lane:** Turns the already-listed SHACL specification into concrete implementation reading for named relation/reference violations.
- **Verified anchor:** README documents RDF graphs validated against SHACL shapes, structured results, and separate inference/rule capabilities; repository includes examples and tests.
- **Read first:** Inspect validation return data, inference controls and failure handling, then map a few existing lore checks to explicit shapes.
- **Proposed later exercise (not performed):** After hyaku, propose a throwaway graph with one valid relationship and one dangling endpoint. Preserve focus node, path, shape and severity in the result; keep inferred triples distinct from asserted records.
- **Rights:** Apache-2.0 per LICENSE.txt; dependency and source-data licenses remain separate. [License evidence](https://github.com/RDFLib/pySHACL/blob/master/LICENSE.txt).
- **Maintenance evidence:** GitHub release metadata records v0.40.2 published 2026-10-28; rechecked 2026-11-03. [History/release evidence](https://github.com/RDFLib/pySHACL/releases).
- **Limits:** Not a general contradiction detector or PROV-Constraints implementation. A pass only covers declared shapes. Never let inferred triples establish canon or silently replace the existing bible format.
- **Duplicate review:** SHACL specification is already listed; pySHACL is a new implementation source, not a re-submission of that standard. Exact/normalized primary URL absent from supplied lane inventory.

## Family-overlap and revision check

Method/specification: targeted new surface in existing source family. Repository: new source family in supplied lane inventory. These checks include repository identity and publisher-domain overlap, not just exact URLs.

Repository revision evidence: [v0.40.2; release page opened](https://github.com/RDFLib/pySHACL/releases/tag/v0.40.2). This is a reading anchor, not proof of host compatibility; mutable README/license links above were inspected separately on 2026-11-03.

## Admission gate, later

Re-open and pin versions when hyaku work is authorized. State the narrow claim, build original positive and negative cases within this lane’s province, and retain measured limitations. Reading or successful third-party tests alone does not admit a capability. Attribution, redistribution rights and AI-training permission remain distinct; this queue makes no training-permission or asset-rights determination.
