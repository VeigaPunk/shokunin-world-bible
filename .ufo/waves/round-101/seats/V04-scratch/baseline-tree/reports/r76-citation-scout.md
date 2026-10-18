# Round 76 citation scout — attribution and rights boundary

## Scope and verdict

Report-only review of the r76 declaration in `.shokunin/lore/LOG.md`, the delivered r73 Jorin excerpt/source/claim/map and comparison, plus relevant r72/r74 and withdrawn-r75 precedent. No `r76-*` fixture exists at inspection, so this checks the proposed citation contract, not a realized record, excerpt, clause map, or candidate. No checker was run and no external reference consulted.

**GO, narrowly, for the declared citation/pointer discipline if a candidate is authored; NO-GO for treating it as corroboration or as an established event.** A new fictional source can separately attribute a record’s wording to its invented narrator, but that attribution alone is not proof of an independent provenance chain or authenticated corroboration of Jorin. This report does not recommend a candidate or determine whether it would add material depth.

## Existing Jorin pointers and support

The r73 excerpt `.shokunin/lore/corpus/fixtures/r73-jorin-slate-claim/jorin-slate-note-excerpt.md` reads verbatim: “I was sent to copy a gate notice. At the east steps, I read “KEEP THE EAST GATE OPEN” on a slate. I did not see who put it there.” In that fixture:

- `sources.json` `/7` has `id: "jorin-slate-note"`; its title and reliability note describe a newly authored, fictional, unverified first-person report, not an authenticated slate, inscription, or assignment.
- `entities.json` `/7/claims/1` cites `jorin-slate-note` and says Jorin reports the request, reading, and not seeing who placed the slate.
- `jorin-slate-clause-map.md` maps each quoted excerpt span to that claim and its source pointer. It preserves the uncertainty: the sender, placer, and reading time are unspecified.
- `editorial-comparison.md` separately points to Vela’s r72 excerpt/source (`vela-slate-note`) and Jorin’s r73 excerpt/source (`jorin-slate-note`). It compares the *reported* wording only and leaves common slate/inscription, time, and source relationship unresolved.

The exact words and `I was sent` clause support only what this fictional Jorin narrator says. They do not identify a sender, show that a request was actually made, establish why it was made, show that Jorin complied, or link the account to a particular registry entry. The r72 Vela excerpt reports “KEEP THE EAST GATE CLEAR”; its separate `entities.json` `/6/claims/1` → `vela-slate-note` pointer likewise attributes Vela’s account, not an authenticated inscription. Neither source is independent authentication of the other.

## Candidate citation guardrails

If the declared r76 fixture is built, keep its source row uniquely identified and explicitly fictional/newly authored/unverified. Point the new Jorin claim to that row and map exact excerpt spans to the claim and `source_id`; distinguish quotation from paraphrase and retain report attribution. A copied source ID, unsupported extra assertion, altered quote, or clause-map pointer mismatch is a citation/support failure. Do not change inherited claims or smuggle request, sender, receipt, compliance, slate identity, inscription, occasion, or time into the claim/comparison unless the new excerpt literally says it—and even then phrase it as the narrator’s report, not fact.

The r72/r73/r74 precedents consistently distinguish a source-ID pointer and clause map from textual support or authentication. `check_bible.py` checks structure and source-ID resolution; it does not read Markdown, check exact quotations or entailment, or authenticate a source. A CLEAN result therefore cannot validate the excerpt’s meaning or corroboration. Manual comparison of source, excerpt, claim, and map is necessary. The r75 exact-row-duplicate work was a separate, rejected checker proposal and supplies no precedent for this fictional source claim; the concurrently withdrawn r75 depth declaration remains incident telemetry, not evidence or a completed candidate.

## Real-world reference ledger and rights

`corpus/fixtures/README.md` distinguishes in-world `source_id` references to fictional records from the real-world reference ledger. `corpus/knowledge/reference-ledger.md` labels its entries method references, not canon, and says they attribute method inspiration; fictional story facts are separately cited in fixture `sources.json`. No real-world work is needed to cite an invented registry entry or Jorin excerpt, so do **not** add a ledger entry merely for this attribution. If a real-world method source is actually consulted, record it there as method inspiration, not fictional evidence.

The ledger states that expressive-material rights and AI-training permission are separate questions and are not assessed/granted by its citations. This scout makes no copyright, license, reuse-permission, or AI-training-permission finding. A new fictional attribution, repository authorship, or `source_id` does not establish rights status.

## Limits

No r76 source, claim, excerpt, or map exists to verify; this is not a candidate review and does not decide novelty, material depth, or whether an invented registry voice is useful. **Newly invented fictional attribution is not authenticated independent corroboration.** No truth of the request or slate account, source authenticity, sender, compliance, artifact identity, chronology, canon, rights, or game mechanics is established. Recheck concrete text and pointers if a candidate is produced.
