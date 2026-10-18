# E2 — C3 edge clarification wording

Status: proposed replacement wording for the existing R8, R9, and R10 appendices in `corpus/knowledge/r88-sourced-inspiration-decision-table.md`; do not append duplicate decision IDs. These are governance clarifications, not checker changes or case findings.

Axes: C3 decisional coverage, traceable ownership and records, and bounded evidence claims.

## R8 — R2 gate failure and withhold scope

**Owner:** the lore integration editor records the gate result and affected scope; the creator supplies the provenance account; a reviewer identifies and records contrary source-specific evidence.

**Trigger:** an element is proposed for R2, but the creator's no-source account is unavailable or disputed, contrary source-specific evidence exists, or the evidence does not leave only a commonplace motif. A distinctive sequence that conflicts with a no-source account is an explicit review trigger.

**Decision:** R2 is available only when both the creator's no-source account and the integration editor's finding of no contrary source-specific evidence, with only a commonplace motif remaining, are documented. If either part fails or is disputed, R2 is unavailable; failure alone does not establish source use or force an R1 finding. Keep a dated `possible influence: unverified` question, record the account, evidence, and affected scope in the inspiration note/map, and send an unresolved dispute to `l0-questions.md`. While it remains unresolved, withhold only the smallest source-dependent detail from supported canon when that detail is separable and the remainder is independently authored and supported. Withhold the whole element only when the dependency cannot be separated or no independently supportable remainder can be identified. This specific scope governs the parent row's broader “withhold it” shorthand. If both R2 parts later pass, record the basis and remove the provisional note. If review establishes that a source materially informed the element, use R1; do not treat an unresolved case as established general-motif use or apply that use's element marker prematurely.

**Worked example:** the creator says no source was used, but the editor finds the same seven threshold names in the same order as *Kesh Hymn* lines 12–19. R2 is unavailable, but the conflict does not by itself prove source use. Keep the question open and withhold the seven-step sequence; a separately authored crossing motif may remain only if it is independently supported. If the entire element is that sequence, withhold the whole element.

**Verification command (textual completeness only; it does not decide influence):**

```sh
python3 -c 'from pathlib import Path; s=Path(".ufo/waves/round-91/patches/E2-wording.md").read_text(); a=s.split("## R8",1)[1].split("## R9",1)[0]; keys=("**Owner:**","**Trigger:**","R2 is unavailable","failure alone does not establish source use","withhold only the smallest source-dependent detail","Withhold the whole element only when","l0-questions.md","remove the provisional note","**Worked example:**","**Verification command"); missing=[k for k in keys if k not in a]; print(f"R8 wording completeness: {len(keys)-len(missing)}/{len(keys)}"); raise SystemExit(bool(missing))'
```

## R9 — Later reprint boundary and reliability of the tie

**Owner:** the excerpt/map submitter supplies the delivered copy and bibliographic record; the lore integration owner verifies the record, passage, and permitted R5 scope.

**Trigger:** an R5 source-claim relies on a translated excerpt whose bibliographic tie is a later reprint, or whose delivered printing/source-work link is uncertain.

**Decision:** translator name alone, or a generic “reprint of” notice without a verifiable source-work link, fails R5 support. Keep `Delivery mode: translation`; record `Delivered printing:` (edition/year and stable identifier or copy locator) separately from `Source text/version:` and leave either field's unknown status explicit. Do not label a delivered translation `not delivered`. A later reprint qualifies for the narrow R9 exception only when an auditable, item-specific record identifies the actual delivered reprint and its edition/year with a stable identifier or copy locator, names the translator and source work, and ties the cited passage to that translation. A title/imprint/copyright page or publisher/authoritative-library catalogue can qualify when it supplies those details; an untraceable secondary entry, generic reprint notice, translator name, or anchor alone cannot. Record the exact printing and record citation in the excerpt/map, then verify the passage against that exact copy. A qualifying tie supports only a claim about wording in the identified delivered reprint. It does not show that the reprint is unchanged from an earlier printing, and does not support the earlier edition's wording, original-source wording, or an edition-specific variant unless that exact edition is independently identified and compared. If the item-specific tie or source work is unverified, retain `Source text/version: unidentified; unverified` and fail R5 source-claim support.

**Worked example:** a delivered line is labelled “2011 reprint of the 1901 translation” and names M. A. Translator, but the only record is a generic re-issue note and does not tie the passage to a named source work. Keep `Delivery mode: translation`, record `Delivered printing:` as unverified and `Source text/version: unidentified; unverified`, and fail R5 support. If an authoritative record identifies that exact 2011 copy, translator, source work, and passage, support only “the identified 2011 reprint's translation says …”, not what the 1901 printing said or a variant in another edition.

**Verification command (textual completeness only; it does not validate the source or fidelity):**

```sh
python3 -c 'from pathlib import Path; s=Path(".ufo/waves/round-91/patches/E2-wording.md").read_text(); a=s.split("## R9",1)[1].split("## R10",1)[0]; keys=("**Owner:**","**Trigger:**","later reprint qualifies","auditable, item-specific record","actual delivered reprint","stable identifier or copy locator","names the translator and source work","ties the cited passage","verify the passage against that exact copy","Delivered printing:","earlier printing","**Worked example:**","**Verification command"); missing=[k for k in keys if k not in a]; print(f"R9 wording completeness: {len(keys)-len(missing)}/{len(keys)}"); raise SystemExit(bool(missing))'
```

## R10 — `source_id` is cluster-local

**Owner:** the incoming-cluster integration owner records the comparison; both cluster owners supply their local source records and any independently supported cross-reference; a reviewer checks the outcome before registration.

**Trigger:** a cross-cluster comparison finds the same `source_id` string in the two clusters' `sources.json` files.

**Decision:** each cluster root defines its own `sources.json` namespace; the comparison key is `(cluster-relative path, source_id)`, not the bare string. The same `source_id` in two clusters is a namespace collision, not identity. Even identical row contents do not make IDs global, and differing contents do not establish that the records are distinct real-world sources. Resolve each citation only against its own cluster's source table, do not merge the rows, and do not carry citation validity or support from one cluster to the other. Compare the full source rows and record every repeated ID, both cluster paths, row pointers, compared fields, and why the overlap is dismissed or unresolved in the incoming cluster's `README.md` under `## R10 comparison outcomes`. If unresolved source-record identity is material to a claim, record the missing evidence there and in `l0-questions.md`. An ID collision alone is not a discrepancy or a live-register entry; the register still requires source-backed claims about the same fictional referent, field, and occasion that are incompatible as stated.

**Worked example:** JDEP2's two probes repeat `registrar-copy` with identical rows and `salt-chronicle` with different titles (municipal registry copy versus courier's route log). Record both overlaps as cluster-local comparisons in the incoming README. Neither equality nor difference proves global identity or creates a live-register conflict; any unresolved cross-reference needs independent evidence.

**Verification command (textual completeness only; it does not establish source identity):**

```sh
python3 -c 'from pathlib import Path; s=Path(".ufo/waves/round-91/patches/E2-wording.md").read_text(); a=s.split("## R10",1)[1]; keys=("**Owner:**","**Trigger:**","comparison key is `(cluster-relative path, source_id)`","namespace collision, not identity","Even identical row contents do not make IDs global","Compare the full source rows","incoming cluster\x27s `README.md`","l0-questions.md","not a discrepancy or a live-register entry","registrar-copy","salt-chronicle","**Worked example:**","**Verification command"); missing=[k for k in keys if k not in a]; print(f"R10 wording completeness: {len(keys)-len(missing)}/{len(keys)}"); raise SystemExit(bool(missing))'
```

## Rationale and over-claim risks

- **R8 rationale:** the conjunctive R2 gate now has a state for failed or contested cases, and the specific-detail rule reconciles the appendix with the parent row without withholding unrelated material by default. **Over-claim risk:** a failed gate or a distinctive resemblance is not proof of consultation, copying, rights infringement, or canon truth; a neutral open question must not be presented as established source use.
- **R9 rationale:** an item-specific, traceable reprint record resolves the reprint boundary while limiting any support to the exact delivered copy. This preserves the narrow translation exception without treating the JDEP2 probe's generic re-issue note as a reliable tie. **Over-claim risk:** catalog metadata and a matching anchor do not establish translation fidelity or unchanged wording across editions. The support command's translation-mode PASS is not a receipt for this manual R5 decision.
- **R10 rationale:** scoping `source_id` to each cluster prevents key equality from being mistaken for cross-cluster identity or portable support, while retaining the existing evidence threshold for register entries. **Over-claim risk:** a namespace collision proves neither that two records are the same source nor that they are distinct real-world sources; any crosswalk and any canon comparison remain separately evidenced manual decisions.

These proposed words do not edit the decision table, create an R10 entry, or mechanically verify any of the three governance decisions.
