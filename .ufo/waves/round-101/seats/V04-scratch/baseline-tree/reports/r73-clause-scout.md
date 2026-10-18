# Round 73 clause scout — Jorin excerpt, claim, and comparison pointers

## Scope and evidence

Report-only pointer plan for the Round 73 declaration in `.shokunin/lore/LOG.md`. I read that declaration, the r72 clone’s five JSON tables and Vela excerpt/map, the inherited r43 Jorin and Vela excerpts/maps, `corpus/fixtures/check_bible.py`, and the available r72 critic / relevant r71–r72 reports. There is no r73 candidate excerpt, source row, claim, or comparison note in the inspected checkout; therefore exact new Jorin clause text cannot yet be quoted or verified. This plan does not compose or certify that missing text.

Relevant literal baseline excerpts:

- Vela’s r72 account: “I leaned close to the slate and could read, “KEEP THE EAST GATE CLEAR.” The cramped letters made me wonder if whoever wrote them had been in a hurry. I could not tell who wrote them.” The marks around the slogan in the actual excerpt are curly double quotes.
- Inherited Jorin’s r43 account: “I, Jorin, am a registrar, and I stood at the Lantern Harbor registry doorway. I saw Vela standing on the Lantern Harbor east steps during what I called Bell-7. I did not see who, if anyone, struck a bell.” Its map attributes the role, vantage, sighting, and Bell-7 label to Jorin; it expressly says the label does not establish a shared occasion and that the east-steps sighting does not verify Vela’s account. It says nothing about reading a slate.
- Inherited Vela r43 account is about hearing the registry bell and not seeing Sella or an envelope; it is not evidence of slate wording.

Thus an r73 Jorin slate-reading report, if added, is a separately authored fictional account. The inherited Jorin sighting does not show he witnessed Vela reading, does not connect his earlier Bell-7 label to a slate-reading occasion, and cannot serve as support for the new wording.

## Expected append-only pointers (verify against actual clone)

The declaration specifies a new five-table clone of r72, one appended source and one Jorin entity claim, with no timeline/relations/contradictions additions. Under that exact append-only arrangement, r72 currently has six source rows and seven entity rows; `jorin` is entity index 7, whose inherited claim array is empty. Expected zero-based JSON pointers are:

| Added evidence / record | Expected pointer | Mapping rule and limit |
|---|---|---|
| New fictional Jorin source row | `sources.json` `/7` | Confirm actual row ID at `/7/id`; describe it as a newly authored, fictional, unverified account. Its presence attributes a claim; it does not authenticate a slate, words, author, or occasion. |
| New claim on existing Jorin entity | `entities.json` `/7/claims/0` | Append to `jorin`; do not add a duplicate Jorin entity. Claim `source_id` must cite the newly appended source ID. |
| Claim’s citation | `entities.json` `/7/claims/0/source_id` → `sources.json` `/7/id` | Confirm literal ID equality and uniqueness in actual files. Keep statement explicitly as what Jorin reports, not as an objective inscription fact. |

These indices are conditional, not assertions about a candidate that has not been supplied. Recompute if rows are inserted, reordered, or otherwise differ from the declared r72 clone. Do not alter Jorin’s inherited first-appearance/source or existing claim; do not use his inherited `jorin-note` as citation for a new slate report.

## Literal clause-to-claim map plan

Once the new excerpt exists, quote each relevant sentence/clause character-for-character in the map, including its actual punctuation and any internal curly quotation marks. Do not fill the map from a paraphrase or copy Vela’s wording. Point every mapped substantive span to `entities.json` `/7/claims/0/statement`, then to `/7/claims/0/source_id` → `/7/id` in `sources.json`. Label claim alignment as an attributed summary unless the statement truly reproduces the excerpt verbatim. A useful map layout is:

| Exact span from new Jorin excerpt (to be filled literally) | Claim/source pointer | Boundary |
|---|---|---|
| Reporter’s exact words that identify what he says he read, including only the literal wording in that excerpt | `/7/claims/0/statement`; citation `/7/claims/0/source_id` → `/7/id` | Jorin’s reported reading only; no objective text, persistent inscription, authorship, placement, or authentication. |
| Any exact phrase that gives his stated observation basis, if the excerpt supplies one | Same claim/source pointers | Preserve only the stated vantage/basis; do not borrow the inherited registry doorway or east steps unless the new excerpt itself says so. |
| Any explicit uncertainty or limit in the new excerpt | Same claim/source pointers | State the limit as Jorin’s, not as universal proof about what was or was not present. |

The map must distinguish two separate accounts and avoid presenting the comparison itself as new in-world evidence. The exact wording difference can only be assessed after the Jorin excerpt is authored; the scout cannot supply the missing words.

## Editorial comparison note plan

Keep the comparison note explicitly editorial and source-bounded. It can juxtapose Vela’s literal r72 reported wording with Jorin’s eventual literal reported wording and state that the wording reported in the two accounts differs, provided the new excerpt actually contains a different line. It should then leave open whether the reports concern the same object/inscription, whether either wording persisted, when either report or reading occurred, and how the sources relate. For example, as a structure rather than candidate copy:

> Editorial comparison: Vela’s r72 account says she read “[exact Vela wording]”; Jorin’s separately cited account says he read “[exact Jorin wording].” The reported wordings differ. These accounts do not establish whether they concern the same slate or inscription, whether either wording was present at the same time, or what relationship exists between the reports.

Use exact quotes from each literal source when completing this template; retain punctuation faithfully. Do not say “the same slate,” “changed,” “overwritten,” “contradicts,” “before/after,” “then,” “at Bell-7,” “contemporaneous,” or that Jorin saw Vela read it unless a source explicitly supports that attributed proposition—and even then do not convert it to verified shared identity/time. Prefer “reported wording differs” over “the inscription differs” or “the accounts conflict.” No contradiction row is warranted by unlike wording alone without supported common referent and occasion. The note is an editorial comparison, not a third source or claim.

## Checker and evidentiary limits

`check_bible.py` checks entity claim nonempty `statement` / `source_id` and resolves source IDs; it does not read Markdown excerpts or maps, check exact quotation, semantic entailment, compare wording, identify a common referent, or establish narrative depth. A clean clone check can support schema/citation validity only. The declaration’s no-event/no-relation/no-contradiction boundary avoids adding a timeline position or structured conflict, but cannot by itself prevent prose from implying shared time or artifact identity.

The exact map and editorial note must be reviewed against the actual Jorin excerpt, source row, and claim. The inherited Jorin and Vela accounts do not authenticate either new report or link slate-reading events. No source truth, objective inscription, slate persistence, source relationship, chronology, canon, real-world rights, or game-mechanics conclusion follows from these pointers. This is a clause/pointer plan only.
