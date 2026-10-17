# E1 — R9 transition and R8 replay calibration

Status: Copy-ready wording and replay recommendations for the proposed D1/D2 artifacts only. This does not modify the corpus or authorize applying either seat's patch.

Axes: **transition clarity**, **evidence-to-claim calibration**, **dossier field coverage**.

## R9 — keep D1's venue; clarify inspection and receipt boundaries

D1's candidate places the R9 manual gate, required record, and receipt boundary after the R9 Decision and before one replacement worked example; the R8 example remains under R8. That is the correct venue and sequence. Two phrases can still blur what the evidence establishes.

In the R9 **Manual R9 gate**, replace the sentence beginning `**Review:**` with:

> **Review:** Inspect the exact delivered translation item itself—either the physical copy or a complete, legible scan tied to its copy locator. An item-specific bibliographic record may support identification of the item and its translator/source-work link, but it cannot substitute for inspecting the cited passage in that exact copy. Verify the actual printing/edition and year, a stable identifier or copy locator, translator, named source work, and that the passage is present in that copy and supports the whole claim. Record any unknown source-version limitation; support is bounded to wording in the identified delivered translation, not the original source wording, an earlier printing, or an edition-specific variant.

This keeps the record's identity role separate from passage inspection; a catalog or other record alone must not appear to satisfy review of the cited translation.

In the **Receipt boundary**, replace `The existing verification command checks wording completeness only and cannot perform this review.` with:

> The separate R9 appendix `Verification command (textual completeness only; it does not validate the source)` below is a wording-presence check only, not an item-inspection or manual-review receipt. Re-anchor its input to the delivered R9 appendix before treating its output as a check of that text.

The current command reads `.ufo/waves/round-91/patches/D2-edges.patch`; keep Q92-004 as separate named debt until it is re-anchored and rerun. Do not imply that the command verifies the delivered table or that `support_check.py` output establishes the manual outcome.

## R8 — retain the scenario limits; narrow the replay claim

D2 appropriately labels the dossier as an illustrative model record, says the passage is not reproduced or independently authenticated, and disclaims an observed submission, source-use finding, rights assessment, and canon assertion. Preserve those limits. The schema-proxy `CLEAN` result is not an R8 editorial review; D2 already records that boundary.

The dossier replay's five predicates are not record-value checks. In an in-memory mutation, all eight `Recorded value` cells were emptied while their field labels stayed intact; the five predicates still passed. Three field labels are not asserted as rows at all: `Element and scope pointer`, `Creator account`, and `Reviewer / record date`. The other checks also search for phrases across the whole dossier/reference text rather than validating the corresponding cell.

If the replay remains phrase-based, replace its description with:

> This checks five phrase-presence predicates across the dossier, R8 decision, and E1 scenario. It does not parse or validate the illustrative record's `Recorded value` cells, establish that every required field is populated, or establish that a live review occurred.

Change the output label from `R8 record fields: ...` to `R8 text-traceability predicates: ...`. Also narrow D2's report wording that “five dossier fields replay” to “five text-traceability predicates pass.” If D2 intends to claim record-field coverage instead, the test must locate each required field row and validate its actual value, including the element/scope pointer, creator account, and reviewer identity/date; missing, empty, or contradictory values must fail.

Keep the seven-threshold sequence described as the scenario premise, not an authenticated source passage or proof that a creator used it. D2's current disclaimer does this well.