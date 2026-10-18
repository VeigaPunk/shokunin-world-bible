# Round 72 clause scout — quotation and pointer plan

## Scope

Report-only scout for the Round 72 declaration in `.shokunin/lore/LOG.md`. I read that declaration, the r43 fixture, the r71 executor/reviewer/verifier/adjudicator reports, and `.shokunin/lore/corpus/fixtures/check_bible.py`. No fixture or checker was changed. This report does not decide whether the proposed depth gain is meaningful.

## Exact excerpt and map correction

The r71 executor quotes the newly authored excerpt as:

> I leaned close to the slate beside the east steps and could read, “KEEP THE EAST GATE CLEAR.” The cramped lettering made me think whoever wrote it might have been in a hurry. I did not see the writer, and I do not know who it was.

The r71 independent verifier and axis adjudicator identified the map defect: under “Exact excerpt clause,” the map used curly single quotation marks around `KEEP THE EAST GATE CLEAR`, while the excerpt uses curly double quotation marks. If retaining that r71 exact-quotation label, the map cell must reproduce the source exactly, including punctuation:

> I leaned close to the slate beside the east steps and could read, “KEEP THE EAST GATE CLEAR.”

Do not use `‘KEEP THE EAST GATE CLEAR’` as an exact quotation. The remaining two sentences can be quoted as separate exact spans:

> The cramped lettering made me think whoever wrote it might have been in a hurry.

> I did not see the writer, and I do not know who it was.

These are quotations from the prior r71 candidate, not evidence that this wording has been selected for R72. R72 has not yet supplied a new excerpt; any R72 map must be checked against its own literal source text, character-for-character. A quotation repair does not solve r71’s separate tick-4 calibration failure. R72 appropriately declares no timeline event.

## R72 source → claim pointer plan

The declaration specifies an r43-derived clone, appending one new source and one claim to existing Vela, with no timeline event, relation, dependency, or contradiction. Given the current r43 array order and append-only contract, expected zero-based JSON pointers are:

| Evidence / record | Expected pointer | Use and limit |
|---|---|---|
| New fictional first-person report source row | `sources.json` `/6` | New appended source ID (to be confirmed in the actual candidate). Its reliability note should identify an authored, fictional, unverified report; a source row is attribution, not authentication. |
| Existing Vela entity’s appended claim | `entities.json` `/6/claims/1` | Existing Vela is entity index 6 and has one current claim. New claim should cite the new source ID and say only what the excerpt explicitly attributes to Vela. This pointer is conditional on preserving r43 row order and appending, not inserting/reordering. |
| Source reference in new claim | `entities.json` `/6/claims/1/source_id` | Must equal the ID at `sources.json` `/6/id`; verify literal value in candidate. |

For a clause map, quote each distinct sentence or clause exactly from the actual new excerpt, point it to `/6/claims/1/statement` (and the cited source via `/6/claims/1/source_id` → `/6/id`), then state whether the claim is a faithful attributed summary or an exact quotation. The excerpt’s quoted words must retain curly double quotes if that is what the candidate literally contains. A map must not claim that a claim statement itself is a verbatim excerpt when it is only a summary. If the R72 array order or claim count differs from the declared append-only setup, recompute pointers from the actual JSON rather than copying these expected indices.

Keep reported legibility distinct from tentative inference. Any inference about a possible writer must remain explicitly Vela’s uncertain inference, not an observed identity or fact. Her stated lack of seeing/knowing the writer limits her report; it does not prove no writer was visible to anyone. Do not import the r43 bell/tick or Jorin’s report as support for slate wording, Vela’s reading opportunity, writer, or chronology.

## Source limits and validation boundary

R43 `vela-note-excerpt.md` reports standing on the east steps, hearing the registry bell twice, and not seeing Sella or an envelope; it does not report reading a slate. R43 `jorin-note-excerpt.md` reports seeing Vela on the steps, not a slate or reading. Their existing source/claim rows therefore cannot support the proposed new slate-reading statement. The r43 Vela clause map’s treatment of an attributed report as non-corroborating is a useful limit; its tick-3 note is not a template for adding a timeline position here.

The checker requires entity claims to have nonempty statement/source IDs and checks that cited source IDs resolve uniquely. It does not read excerpts or maps, check quote accuracy, or establish semantic entailment, legibility, source truth, authorship, chronology, canon, rights, or mechanics. A clean checker run can establish structural citation validity only. Non-author review must compare actual excerpt text, source row, claim, and map; the structure alone cannot establish meaningful character depth.

**Boundary:** This is a pointer/quotation plan, not a conclusion that a slate exists, text was objectively legible, Vela authored or verified the report, or the proposed account is canonically true. No rights or game-mechanics conclusion is made.
