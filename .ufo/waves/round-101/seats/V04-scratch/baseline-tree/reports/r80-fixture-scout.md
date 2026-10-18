# Round 80 fixture scout — safe r73 clone and pointer map

## Scope and recommendation

Report-only map for the Round 80 declaration in `.shokunin/lore/LOG.md`, the r73 fixture, and the relevant r77/r79/r73 reports. The r80 action scout proposes a cup/mark two-beat excerpt; this report maps how an authorized candidate could represent it, without endorsing its materiality or treating the proposed prose as corpus text. I did not spawn agents, run the checker, or edit corpus, checker, LOG, or any file other than this report. No commit, push, or merge.

A safe structural route, **if separately authorized after the remaining reviews**, is to clone `.shokunin/lore/corpus/fixtures/r73-jorin-slate-claim/` into a new, separately named fixture, retain all 19 inherited files and their bytes except the two append-target JSON files, and add only the minimum cited source/entity claim and prose pointer files. The sample proposal contains a deliberate action and observable response, but the fixture cannot establish that it earns depth: r77 and r79 show that plausible or coherent invented detail can still be generic or self-justifying. Materiality is a separate non-author prose judgment under the Round 80 test.

## Exact r73 baseline and append pointers

The r73 baseline has 8 source rows and 8 entity rows. Existing relevant rows are `sources.json` `/7` (`jorin-slate-note`) and `entities.json` `/7` (Jorin); its `/7/claims/1` is the inherited slate claim. Do not reuse or alter these rows, attach the new account to Jorin, or imply that the new scene shares a slate, gate, occasion, or source with r73.

For the r80 action scout’s proposed excerpt, the minimal route for a genuinely new speaker is:

1. Preserve every existing `sources.json` row and order; append one uniquely identified, explicitly fictional/unverified source at **`sources.json` `/8`**. Its reliability note should describe only the invented speaker’s account, not authenticate the action or consequence. Use a new source ID (for example, `r80-cup-mark-note` only if that ID is actually chosen and unique).
2. Preserve every existing `entities.json` row and order; append a distinct **character** row at **`entities.json` `/8`**. Set `first_appearance` to the new source ID and add the minimum claim at **`/8/claims/0`**, citing that same ID in `source_id`. The claim must faithfully attribute the action and response in the excerpt to the speaker; do not assert an unqualified fact or add interpretation not present in the wording. The ID example above is illustrative, not a required constant.
3. Add a short excerpt and clause map as new files. Quote the exact excerpt clauses; map the deliberate action to `/8/claims/0/statement`, and the separately described response/consequence to the same statement (or to an additional claim only if the chosen schema/prose truly requires it). Map the claim’s `source_id` to `sources.json` `/8/id`. Keep speaker attribution explicit and make the map an aid to human checking, not evidence independent of the excerpt.

The actual proposed two sentences are in `reports/r80-action-scout.md`; they are not yet an authorized fixture excerpt. Do not silently convert them into established prose or introduce an extra entity for the cup, mark, or folded paper. The declared claim-only representation does not warrant timeline/event, relation, or contradiction records.

## Protected files and preservation boundary

R73 contains these 19 inherited paths: `sources.json`, `entities.json`, `relations.json`, `timeline.json`, `contradictions.json`, `tarin-note-excerpt.md`, `clause-map.md`, `sella-bell7-note-excerpt.md`, `manual-clause-pointer-map.md`, `vela-note-excerpt.md`, `vela-clause-map.md`, `strength-contrast-map.md`, `jorin-note-excerpt.md`, `jorin-clause-map.md`, `vela-slate-note-excerpt.md`, `vela-slate-clause-map.md`, `jorin-slate-note-excerpt.md`, `jorin-slate-clause-map.md`, and `editorial-comparison.md`.

All inherited paths and content should remain byte-identical except `sources.json` and `entities.json`, where only the appended rows are permitted; preserve every old JSON row value and order. In particular, keep `relations.json`, `timeline.json`, and `contradictions.json` byte-identical and add no shared-object, event, timing, causal, or institutional link. Add new excerpt/map (and any narrowly necessary candidate editorial note) as new paths, not by rewriting inherited prose. Outside the candidate fixture, protect all corpus files, `.shokunin/lore/corpus/fixtures/check_bible.py`, `LOG.md`, and every other report. This scout’s only output is `reports/r80-fixture-scout.md`.

## What the evidence can establish

- **Invented in-world attribution:** a source label and cited claim can present the scene as a fictional, unverified speaker’s account. They do not authenticate the speaker or prove that the cup tipped, water spread, or the mark blurred—even as an established fact of the fictional world.
- **Citation-ID/structure checks:** the checker can validate fixture structure and resolve a claim’s `source_id` against source IDs. A clean result, exact JSON pointers, preserved inherited bytes, and regression replay support structural integrity and preservation only. The checker does not read Markdown excerpts/maps or establish exact-span mapping, semantic entailment, scene value, or truth; human review must compare the actual excerpt, claim, and map.
- **Prose truth, canon, rights, mechanics:** neither fictional attribution, citation resolution, nor an editorial depth judgment establishes source authenticity, canon, real-world reuse/license rights, or game mechanics. This report makes no such finding and proposes no world rule.

## Recommendation

**Fixture shape: conditionally mappable; candidate/depth: not adjudicated here.** The source/entity append route is unambiguous, but do not implement merely because it is easy. A non-author must judge the actual candidate against the r77/r79 materiality failures and Round 80’s removal/alternative-presentation test. Reject if the alleged consequence merely restates or flatters the invented action, is removable without changing a meaningful scene choice, or depends on authority, speculative world rules, or unrelated r73 links. No conclusion about the candidate’s prose truth, canon, rights, or mechanics follows from a clean fixture.
