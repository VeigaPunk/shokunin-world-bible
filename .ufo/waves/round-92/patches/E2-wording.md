# E2 — R8/R9 edge wording and boundary-document header

Status: proposed copy-ready wording only; do not apply beside competing R8/R9 text. R8/R9 policy language follows E1’s round-92 decisions in `patches/E1-edges.md`. The boundary header is a proposal for the independently re-derived document and does not claim that the document has yet passed certification.

Axes: decision fidelity, manual-gate traceability, and accurate reconstruction provenance.

## R8 — failed R2 gate with an inseparable dependency

Replace the existing `**Failed-gate disposition (decided r91):**` paragraph under `### R8 appendix` with:

> **Failed-gate disposition (clarified r92):** **Owner:** the lore integration editor records the two-part R2 gate result, the affected element, and the separability decision in the inspiration note and element map; the creator supplies the provenance account; a named reviewer assesses and records the contrary source-specific evidence and whether an independently authored, independently supportable remainder exists. **Trigger:** either R2 condition fails or remains unresolved, and the reviewer cannot separate the source-dependent detail from the element while leaving such a remainder. **Decision:** withhold the **whole element from supported canon** until it is re-derived without the source-dependent material or a permitted source text is delivered and a separately reviewed R1 decision establishes a claim-specific basis. Do not leave the element in supported canon with an uncertainty notice: when the dependency is inseparable, the notice does not remove the unsupported dependency. Keep the dated `possible influence: unverified` note and mark R2 unavailable; this failed gate is not proof that a source was used, does not establish R1, and does not authorize the `external-only / unverified inspiration` marker by itself. Record the failed condition, contrary evidence, separability rationale, scope, and next action in the note/map. If the influence or separability question remains disputed, add the unresolved question and missing evidence to `l0-questions.md`. Remove the provisional note only after a later review records that both R2 conditions pass, or after a confirmed source-use decision is recorded under R1.
>
> **Worked example:** a proposed lore element consists entirely of the same seven threshold names in the same order as *Kesh Hymn* lines 12–19. The creator denies using a source, but the reviewer records the contrary sequence evidence; no independently authored, supportable remainder survives removing that sequence. R2 is unavailable. Hold the whole element out of supported canon, preserve the neutral note and evidence in the inspiration note/map, and route any unresolved dispute to `l0-questions.md`. Do not keep the element as newly authored fiction merely by attaching a notice. The hold does not itself prove copying or source use.

This is the whole-element branch only. If the dependent detail is separable and a remainder is independently supportable, keep the existing smallest-detail withholding rule.

## R9 — required manual gate for translation-backed support

Append the following within the R9 appendix after its existing **Decision** paragraph and before **Worked example**:

> **Manual R9 gate (required for translation-backed R5 claims):** **Owner:** the excerpt/map submitter supplies the delivered item and bibliographic evidence; a named lore integration reviewer who is not the submitter verifies them and records the outcome. If the integration owner is also the submitter, a second reviewer must be named. **Trigger:** before any claim mapped to `Delivery mode: translation` is accepted as R5 source-claim support or integrated as supported canon. **Review:** inspect the exact delivered translation item (or an item-specific record that identifies it), verify the actual printing/edition and year, with a stable identifier or copy locator, translator, named source work, and that the cited passage is present in that exact copy and supports the whole claim. Record any unknown source-version limitation; support is bounded to wording in the identified delivered translation, not the original source wording, an earlier printing, or an edition-specific variant. Public catalog availability is not required, but a privately held item qualifies only if the reviewer can inspect the exact copy or a complete, legible scan with its copy locator; a submitter-only assertion is insufficient. If identity, passage, or reviewer access is not established, record `FAIL` (or `OPEN` before review) and do not grant R5 support.
>
> **Required record:** add an `R9 manual review` entry adjacent to each translation-backed claim in its claim-to-excerpt map. Include the claim pointer; excerpt path and span; delivered printing/edition and year plus a stable identifier or copy locator; translator; source work and source-text/version field (including explicit unknown status); evidence citation and inspection method; reviewer name/role and review date; disposition `PASS`, `FAIL`, or `OPEN`; and the exact claim scope permitted. Only a recorded manual `PASS` can clear this gate.
>
> **Receipt boundary:** `corpus/tools/support_check.py` is a lexical preflight. Its `RESULT PASS` (or `RESULT PASS WITH WARNINGS`) and `SOURCE-SUPPORT` count report map/inventory/mode/anchor checks; they do not establish translation-version identity, the delivered printing, bibliographic linkage, translation fidelity, or the R9 manual outcome. A successful lexical preflight is necessary but not sufficient for a translation-backed R5 claim. Never present that command's output as the R9 review receipt; cite the separate per-claim manual-review entry. The existing verification command checks wording completeness only and cannot perform this review.

Replace the R9 appendix's **Worked example** with:

> **Worked example:** the submitter maps a line from a privately held 2011 reprint of the 1901 translation by M. A. Translator and supplies a scan and copy locator. `support_check.py` may report `RESULT PASS` because the declared mode and anchor match; that is only lexical preflight. A non-submitter integration reviewer inspects the exact scan, confirms the 2011 item, translator, named source work, and passage, then records a dated `R9 manual review` `PASS` scoped only to “the identified 2011 reprint's translation says …”. The result does not support what the 1901 printing or original source says. If the reviewer cannot inspect the exact copy or the evidence does not tie the passage to the named work, record `FAIL`/`OPEN`, retain `Source text/version: unidentified; unverified` where applicable, and grant no R5 source-claim support regardless of the lexical command's result.

In the R9 **Evidence and integration check** cell, append: “For every translation-backed R5 claim, require the separate per-claim R9 manual-review record; the support command's `RESULT PASS`/`SOURCE-SUPPORT` is lexical preflight only and is not that receipt.” Keep the existing textual-completeness verification command but label it as checking wording only, not whether the manual gate passed.

## Proposed header for the re-derived boundary document

Replace the existing H1 and adjacent reconstruction/refresh comments and banners with this single H1, provenance comment, and banner:

```markdown
# Holder-assessment boundary: reading provenance ambiguity disclosures

<!-- Re-derived at round-92 from the last certifiable contract at `e97613c`, applying seat CB1's r90 section instructions in `.ufo/waves/round-90/followup/CB1-boundary-refresh.md`. Each instruction is matched to its source content; line numbers are verification references, never reconstruction coordinates. The current delivered checker used for code-anchor and pasted-output verification is `corpus/fixtures/check_bible.py` (SHA-256 `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`); this checker revision is distinct from the `e97613c` contract-source revision. -->

> **Re-derived at round-92** from `e97613c`; this document does not extend the r91 reconstruction. The r90 instruction sheet is provenance for the reconstruction, not contract text. Verification claims belong only to the completed replay, anchor, and document-state receipts.
```

The banner deliberately separates the contract source from the checker version and does not claim that pasted blocks replay, anchors resolve, cruft is absent, or the H1 count has passed until those properties are independently receipted.

## Rationale and limits

- R8 records the whole-element hold only for an inseparable dependency/no-supportable-remainder; the failed R2 gate and the hold do not prove source use. The separable-detail rule remains intact.
- R9 gives the lexical receipt a precise boundary and requires an independent, per-claim human decision before R5 acceptance. The recorded reviewer must be able to inspect the private copy or complete legible scan; public catalogue availability is not a requirement.
- The header identifies the required reconstruction method and source/checker distinction without making certification claims ahead of the re-derivation and certifier receipts.

No checker or tracked document is changed by this proposal.
