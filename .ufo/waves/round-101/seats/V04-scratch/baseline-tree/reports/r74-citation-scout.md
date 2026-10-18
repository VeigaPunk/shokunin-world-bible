# Round 74 citation scout

## Scope

Read the Round 74 declaration in `.shokunin/lore/LOG.md` (Round 74, declaration before dispatch), the delivered r73/r72 slate-claim fixture excerpts and maps, the source/claim records, the r73 editorial comparison, and the corpus reference-ledger/knowledge notes. This is a citation and scope check only; it does not establish source truth, canon, rights, or mechanics.

## Exact in-world pointers

- **Vela report (inherited r72):** `.shokunin/lore/corpus/fixtures/r72-vela-slate-claim/vela-slate-note-excerpt.md` says: “I leaned close to the slate and could read, ‘KEEP THE EAST GATE CLEAR.’ … I could not tell who wrote them.” The full excerpt also reports cramped letters and Vela’s tentative wondering about the writer’s haste.
- **Vela claim/source pointer (r73 delivered clone):** `.shokunin/lore/corpus/fixtures/r73-jorin-slate-claim/entities.json`, `/6/claims/1`, attributes a paraphrase of her reported wording and tentative inference to `vela-slate-note`; `sources.json` `/6` is the row with `id: "vela-slate-note"`. The exact-span map is `vela-slate-clause-map.md` in both the r72 and r73 fixture directories. It labels the material fictional and unverified and says the citation does not authenticate a slate, inscription, writer, or chronology.
- **Jorin report (new in r73):** `.shokunin/lore/corpus/fixtures/r73-jorin-slate-claim/jorin-slate-note-excerpt.md` says: “I was sent to copy a gate notice. At the east steps, I read ‘KEEP THE EAST GATE OPEN’ on a slate. I did not see who put it there.”
- **Jorin claim/source pointer:** The same r73 `entities.json`, `/7/claims/1`, paraphrases that account and cites `jorin-slate-note`; r73 `sources.json` `/7` is the matching source row. `jorin-slate-clause-map.md` maps the exact excerpt spans to that claim and explicitly limits the citation to fixture attribution, not authentication of the slate, wording, placement, time, or canon.
- **Comparison:** r73 `editorial-comparison.md` identifies the two separate reports and their source IDs, states only that their reported wording differs, and leaves same slate/inscription, reading times, and source relationship unresolved. It explicitly does not establish inscription change or direct contradiction. The r72 fixture predates Jorin’s r73 report; Jorin’s source/excerpt is not part of the r72 fixture.

These are precise pointers to fictional *reports and claims*, not independent evidence of the reported objects or text. In particular, the excerpts do not provide an authenticated inscription, common object identifier, dated reading, or provenance link between the reports. Do not turn “at the east steps” in Jorin’s account or Vela’s “the slate” into proof of a shared surface.

## External references and rights

I found no external work cited or used as a factual/in-world source for these slate claims. The corpus `.shokunin/lore/corpus/knowledge/reference-ledger.md` is explicitly a separate ledger of real-world **method** references (PROV-O, JSON Schema Validation, and Python `graphlib`), not in-world canon; it says citations attribute method inspiration and that fictional story facts are separately cited in `sources.json`. The slate excerpt, claim maps, and comparison cite the fictional source rows above, not those external works.

The ledger keeps expressive-material rights and AI-training permission as separate questions and says neither is granted or assessed there. This scout makes no rights or training-permission finding; it does not imply a license, permission, infringement, or need to add an external citation for the fictional reports. No external-source or rights inference should be added to the r74 table on this evidence.

## Limits / useful citation guardrail

For an editorial table, cite each report through its own exact excerpt path and its own claim/source pointer (`entities.json` `/6/claims/1` → `vela-slate-note` and `/7/claims/1` → `jorin-slate-note`). Keep any proposed evidence need clearly prospective and in-world; these files do not establish that a particular inscription, copy, witness, or record exists. The checker does not validate quoted wording or semantic support, as the two clause maps state. No conclusion about which report is correct, whether the surface/text changed, or whether the accounts conflict is supported here.
