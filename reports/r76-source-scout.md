# Round 76 source scout — Jorin assignment and slate-reading pointers

## Scope

Read-only source/pointer map for the Round 76 depth declaration in `.shokunin/lore/LOG.md`. I inspected the r76 declaration; delivered `r73-jorin-slate-claim` and its source/claim tables, exact excerpts, clause maps and editorial comparison; the corresponding r72 Vela fixture; and r72–r75 relevant precedent and reports, especially `r73-source-scout.md`, `r74-source-scout.md`, and `r74-evidence-scout.md`. No corpus or LOG file was edited and no checker was run. This report maps existing evidence; no r76 candidate record exists in the inspected corpus.

## Exact Jorin reports and pointers (r73)

There are two distinct Jorin accounts in `corpus/fixtures/r73-jorin-slate-claim/`:

1. **Sighting account, not slate-reading evidence.** `jorin-note-excerpt.md` reads: “I, Jorin, am a registrar, and I stood at the Lantern Harbor registry doorway. I saw Vela standing on the Lantern Harbor east steps during what I called Bell-7. I did not see who, if anyone, struck a bell.” The `jorin` entity is `entities.json` `/7`; this is claim `/7/claims/0`, with `source_id: "jorin-note"`. Its source row is `sources.json` `/5`. The claim reports Jorin’s self-description, his claimed sighting of Vela, and his limit about not seeing who struck a bell. It does **not** mention a slate, notice, reading, copying assignment, or inscription. The existing `jorin-vela-sighting` timeline item (tick 3) represents that sighting report only; it does not timestamp or corroborate the later-described slate reading. The clause map explicitly says Bell-7 and tick 3 do not establish shared occasion or chronology.

2. **Slate-reading / assignment account.** `jorin-slate-note-excerpt.md` reads exactly: “I was sent to copy a gate notice. At the east steps, I read “KEEP THE EAST GATE OPEN” on a slate. I did not see who put it there.” Source row `sources.json` `/7` has ID `jorin-slate-note` (“Jorin’s east-steps slate note”) and describes it as a newly authored fictional, unverified first-person report, not an authenticated slate, inscription, or assignment. In `entities.json`, Jorin is `/7`, and the corresponding claim is `/7/claims/1`; its `source_id` is `jorin-slate-note`, resolving to `sources.json` `/7`. The claim paraphrases that Jorin reports being sent to copy a gate notice, reading the quoted wording on a slate at the east steps, and not seeing who put it there.

`jorin-slate-clause-map.md` maps the assignment sentence, the east-steps reading and exact wording, and the reported not-seeing limit to claim `/7/claims/1`, cited through its `source_id` to the source row `/7`. It says the sender and purpose beyond copying are unspecified; the excerpt does not authenticate a slate, inscription, wording, placement, or time. The map is an editorial pointer aid, not checker-validated semantic support. Its inner quotation marks around the inscription reproduce the excerpt.

These pointer indices are specific to the delivered r73 JSON ordering; do not confuse `/7/claims/0` (`jorin-note`) with `/7/claims/1` (`jorin-slate-note`), or reuse them without rechecking any future clone.

## What r72/r73 and r74 add—and do not

R72 Vela’s separate excerpt (`r72-vela-slate-claim/vela-slate-note-excerpt.md`) says she read “KEEP THE EAST GATE CLEAR,” wondered whether cramped letters meant the writer had been hurried, and could not tell who wrote them. Its source is `vela-slate-note` (`sources.json` `/6`); its Vela claim is `entities.json` `/6/claims/1`, citing that source. It does not identify a shared slate, time, or provenance with Jorin’s account.

R73’s `editorial-comparison.md` already compares only the words reported by Vela and Jorin: CLEAR versus OPEN. It leaves physical slate/inscription identity, reading times, and source relationship unresolved, and does not assert inscription change or direct contradiction. R74’s `evidence-scout.md` gives hypothetical evidence that might distinguish alternatives; it reports no extant registry record, request, sender identity, or independent corroboration. R74’s decision-table work does not turn those evidence requests into records.

## Round 76 attribution boundary and verdict

The r76 proposal is to invent and separately attribute a fictional registry entry about a request for Jorin to copy a gate notice. No such entry appears among the inspected r72/r73 evidence. If authored, it would be a **newly invented fictional attribution**—a second authored source inside the fixture—not authenticated evidence that a real or in-world independent record exists. A distinct source ID or registry-like title proves neither provenance nor independence. It cannot be called independent corroboration of Jorin’s assignment absent established provenance; even a fictional record can only be reported as what its newly authored text says. It also cannot establish who sent Jorin, actual receipt/compliance, sender identity, a shared slate or reading occasion, inscription, chronology, or canon.

**Source-scout verdict: NO-GO for describing this as independent corroboration or a proved tasking.** Existing r73 already contains the entire assignment wording as Jorin’s own first-person report and a source/claim pointer map. A new source repeating that proposition risks merely restating the same point under a separate invented attribution. Whether a carefully distinguished editorial perspective could nevertheless yield the r76 hypothesis’s narrow depth gain is a review/adjudication question; this source map alone does not establish material novelty. Do not write source truth, canon, rights, or game-mechanics conclusions from these citations. Structural pointer validity, if later checked, would establish fixture reference resolution only.
