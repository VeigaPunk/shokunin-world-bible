# Round 74 source scout — Vela/Jorin slate-report pointers

## Scope and inputs

Report-only pointer map for the Round 74 declaration in `.shokunin/lore/LOG.md` (2026-10-13T11:09:18.358433+00:00). I checked that declaration, the delivered `r72-vela-slate-claim` and `r73-jorin-slate-claim` fixture excerpts/tables/maps, and the delivered r73 editorial comparison. I also consulted `reports/r73-source-scout.md` for inherited-source context and `reports/r73-prior-scout.md` for prior comparison limits. No fixture, LOG, or other report was edited; this report does not run the checker.

## Vela pointer (r72)

- **Source:** `.shokunin/lore/corpus/fixtures/r72-vela-slate-claim/sources.json`, row `/6`, ID `vela-slate-note` (“Vela’s slate-reading note”). Its reliability note calls this a newly authored fictional, unverified first-person report, not an authenticated slate or writer.
- **Entity claim:** `.../r72-vela-slate-claim/entities.json`, entity `/6` (`vela`), claim `/1`. The statement says Vela reports reading “KEEP THE EAST GATE CLEAR,” tentatively inferring from cramped letters that the unknown writer might have been hurried, and says she could not tell who wrote it. `source_id` is `vela-slate-note`.
- **Excerpt:** `.../r72-vela-slate-claim/vela-slate-note-excerpt.md`: “I leaned close to the slate and could read, ‘KEEP THE EAST GATE CLEAR.’ The cramped letters made me wonder if whoever wrote them had been in a hurry. I could not tell who wrote them.”
- **Map:** `.../r72-vela-slate-claim/vela-slate-clause-map.md` aligns the reported reading, tentative inference, and limit separately to claim `/6/claims/1`, sourced via `sources.json` `/6`. It explicitly treats the excerpt and citation as attribution, not authentication. No time or persistence of the wording is specified.

## Jorin pointer (r73)

- **Source:** `.shokunin/lore/corpus/fixtures/r73-jorin-slate-claim/sources.json`, row `/7`, ID `jorin-slate-note` (“Jorin’s east-steps slate note”). Its reliability note calls it a newly authored fictional, unverified first-person report, not an authenticated slate, inscription, or assignment.
- **Entity claim:** `.../r73-jorin-slate-claim/entities.json`, entity `/7` (`jorin`), claim `/1`. It says Jorin reports that he was sent to copy a gate notice, read “KEEP THE EAST GATE OPEN” on a slate at the east steps, and did not see who put it there; `source_id` is `jorin-slate-note`.
- **Excerpt:** `.../r73-jorin-slate-claim/jorin-slate-note-excerpt.md`: “I was sent to copy a gate notice. At the east steps, I read ‘KEEP THE EAST GATE OPEN’ on a slate. I did not see who put it there.”
- **Map:** `.../r73-jorin-slate-claim/jorin-slate-clause-map.md` maps assignment, reading/wording, and reported limit to claim `/7/claims/1`, sourced via `sources.json` `/7`. It notes that sender, placement, and reading time are unspecified and that the report does not authenticate wording or object.

## Editorial comparison and bounded reading

The delivered `.../r73-jorin-slate-claim/editorial-comparison.md` points to Vela’s `vela-slate-note-excerpt.md` / source `vela-slate-note` and Jorin’s `jorin-slate-note-excerpt.md` / source `jorin-slate-note`. It characterizes the difference only as wording reported by the two accounts. It leaves same slate/inscription, reading times, and source relationship unresolved, and says neither account establishes inscription change or direct contradiction.

These are two separately cited claims and excerpts. The R72/R73 entity JSON positions are local to their respective delivered fixture versions; the pointers above deliberately identify each version. The inherited earlier Jorin account (`r72-vela-slate-claim/entities.json` `/7/claims/0`, source `jorin-note` at `sources.json` `/5`) is a different claim: Jorin reports seeing Vela at the east steps during what he called Bell-7, and says he did not see who struck a bell. Its `jorin-note-excerpt.md` contains no slate reading or inscription wording. Do not substitute that claim for the new r73 slate claim, or use its Bell-7 label to time the slate reading.

The citations resolve only to fictional fixture source IDs and report attribution. These pointers establish neither source truth nor physical slate/inscription identity, common occasion, persistence/change, source independence, contradiction, or canon. The r73 source scout likewise distinguishes the text-level reported wording from any shared artifact/time inference; the prior scout describes the same boundary. This report offers no real-world rights, game-mechanics, or external-source inference.
