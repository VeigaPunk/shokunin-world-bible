# Round 40 clause scout — Vela auditory and non-sighting clauses

## Scope and evidence boundary

This is a clause-level map of the newly authored Vela wording specified by the Round 40 declaration, not a claim that an excerpt has already been implemented or that any report is true. The declaration gives the proposed two-sentence note verbatim at `.shokunin/lore/LOG.md:659`; the planned output is a separately cited Vela source, character claim, attributed auditory event at Harbor local tick 3, and manual clause map (`.shokunin/lore/LOG.md:659-660`). No r40 fixture is present in the current fixture tree. The exact executed/committed r40 excerpt and row paths therefore cannot yet be independently confirmed here.

## Clause map (declared proposal)

| Exact clause | Intended mapping, as proposed | Limit / not entailed |
|---|---|---|
| “I, Vela” | Identifies the first-person reporter; intended Vela entity/source attribution (`.shokunin/lore/LOG.md:659`). | A source/entity ID would be fixture attribution, not authentication of the speaker or truth of the report. |
| “stood on the Lantern Harbor east steps” | Reported scene/locus; proposal places the auditory event at Harbor (`.shokunin/lore/LOG.md:659`). | Scene assignment does not establish that the reported occurrence happened objectively, nor anyone else’s location. |
| “heard two strokes” | Positive auditory perception claim, attributed to Vela (`.shokunin/lore/LOG.md:659`). | Reports what Vela says she heard; does not prove sound source, count independently, or corroborate other accounts. |
| “I took to be the registry bell” | Explicitly Vela’s identification/interpretation of the sound (`.shokunin/lore/LOG.md:659`). | Do not collapse “took to be” into an objective registry-bell sound. It does not establish bell provenance or that the bell rang. |
| “during Bell-7, the sole seventh-watch registry-bell sounding on the seventh day of Embermonth, year 12” | Source-claimed occasion label, consistent with the r35 fictional date/occasion wording (`.shokunin/lore/LOG.md:553-554,659`). | Bell-7/date/sole-sounding are authored claims, not external timekeeping or authentication. Tick 3 is editorial/local and cannot prove simultaneity (`.shokunin/lore/LOG.md:659`). |
| “I did not see Sella or an envelope.” | First-person report of a **non-sighting** of two named targets, scoped to Vela’s experience (`.shokunin/lore/LOG.md:659`). | Not a claim Sella or an envelope was objectively absent from Harbor, nor that Tarin’s reported sighting is false. No explanation, causal inference, envelope identity, or connection is supplied. |

## Precedent and risks

- Round 23 distinguishes a witness’s negative report from an omniscient absence: the report is an observation, not a cause or world-fact (`.shokunin/lore/reports/r23-clause-scout.md`, “Required clauses” and “No cause”; `.shokunin/lore/LOG.md:345-347`). Apply the same boundary to Vela’s “did not see”; seeing nothing is not proof that the targets were not there.
- Round 35 requires the accounts’ same-date and sole-ringing language to be explicit, and treats it as source-claimed rather than authenticated chronology (`.shokunin/lore/LOG.md:553-554,562,569-570`). Vela’s wording must not be used to independently authenticate Bell-7 or close any timing gap.
- Round 14 was rejected because restating existing claims was not new depth; a clause map alone cannot convert repetition into novel evidence (`.shokunin/lore/LOG.md:203-209`). Here, the candidate distinction is Vela’s attributed auditory perception plus explicit non-sighting, not confirmation of Tarin’s sighting or Sella’s account (`.shokunin/lore/LOG.md:658-660`).
- The proposal’s event location/actor and local tick are editorial fixture alignment, not corroboration, objective chronology, or proof of shared real-world occasion (`.shokunin/lore/LOG.md:659`). Preserve Tarin/Sella texts, rows and unresolved ledger exactly as declared (`.shokunin/lore/LOG.md:659`).

## Falsifiable check

When the scoped fixture is authored, compare its excerpt byte-for-byte to the declared two sentences at `.shokunin/lore/LOG.md:659`, then trace each new source/entity/event claim to the precise clause above. Fail this clause map if any field upgrades “took to be” to objective bell origin, turns “did not see” into objective absence, treats Vela as corroborating Sella/Tarin, maps tick 3 to Bell-7 or real time, or links the envelope to any other item/account. Confirm Tarin/Sella source text, rows and unresolved ledger are unchanged against the declared r35-derived baseline. Checker exit 0 would establish structure only, not these prose semantics or source truth.
