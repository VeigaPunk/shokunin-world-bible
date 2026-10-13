# Round 71 citation scout — witness report and source boundaries

## Scope

Read the Round 71 declaration in `.shokunin/lore/LOG.md:1253-1256`, the r43 five-table fixture and its prose/maps, the checker, and relevant prior citation reports. This report addresses citation traceability and epistemic limits only. No fixture, checker, LOG, or other report was changed.

## Existing source and citation pattern

- `.shokunin/lore/corpus/fixtures/r43-jorin-vela-sighting/sources.json` identifies `jorin-note` as a newly authored, unverified fictional first-person report. `jorin-note-excerpt.md` attributes the registrar role, vantage, sighting, occasion label, and non-observation to Jorin; `jorin-clause-map.md` links those words to the fixture’s claim/event and limits what follows. The map specifically treats a source ID and local tick as neither authentication nor chronology.
- In the same fixture, `vela-note` and `vela-listening-report` cite the earlier Vela report. `vela-note-excerpt.md` says she stood on the east steps, heard what she directly identifies as the registry bell, and did not see Sella or an envelope. Its `vela-clause-map.md` says those are her attributed report, not proof of objective ringing or absence. Its broad entity alignment is `harbor`; east steps are not the registry desk.
- The r43 precedent is consistent with `.shokunin/lore/reports/r43-citation-scout.md` and `.shokunin/lore/reports/r41-citation-scout.md`: structural IDs do not authenticate fictional accounts, and stronger or differently worded excerpt claims must not be silently upgraded by unchanged JSON summaries. `.shokunin/lore/reports/r43-independent-verifier.md` likewise limits checker results to structure/citations and explicitly disclaims source truth, shared occasion, chronology, and canon.
- `.shokunin/lore/corpus/fixtures/check_bible.py` checks source-ID resolution and schema/pointers; it does not read excerpt prose or test whether a source entails a claim. A clean run is not citation-content validation.

## Round 71 citation safeguards

1. Give the newly authored Vela account its own source ID (for example, a distinct `vela-slate-note`), with a `sources.json` row explicitly calling it a newly authored, fictional, unverified first-person account. Do not reuse `vela-note`: the new slate response is a distinct report, not a revision or authentication of the earlier Harbor account.
2. Every newly asserted fixture fact must point to that new source ID: the added Vela entity claim and timeline report event, at minimum. The event description should say Vela *reports* what she read and what she inferred; do not make the report’s source pointer imply that the slate or its author was independently verified. If the excerpt contains multiple separable assertions, the claim/event wording must preserve the distinctions rather than flattening them into an objective fact.
3. The excerpt and clause map should distinguish (a) marks/words Vela says were legible, (b) any interpretation she makes about who wrote or placed them, and (c) what she does not know. Reading wording does not establish who authored, placed, sealed, or authenticated the slate. In particular, do not infer Blue Seal provenance from a blue mark or mention of a seal; `.shokunin/lore/LOG.md:1254` expressly says prior r15 blue mark is not a Blue Seal trace.
4. Treat Bell-7/date wording and `tick: 3` as attributed/local fixture conventions, not authenticated time or proof this account coincides with the inherited reports. Do not use Vela’s slate account to resolve the Tarin/Sella ledger or assert a contradiction is resolved. Do not turn her not seeing an author into proof of absence or attribution.
5. Map each material excerpt clause to exact source/entity/event row(s), and state the limits at the clause level. Where JSON uses a weaker summary than the excerpt, identify that as under-specific rather than silently claiming exact correspondence. The non-author verifier should check every newly asserted clause against the exact row and confirm all new facts have in-world citations.

## In-world citations versus real-world reference ledger

No external source is needed for the proposed fictional witness report. Use the fixture’s `sources.json` and row-level `source_id` fields for its in-world assertions; do **not** add a real-world reference-ledger row merely to cite the fictional excerpt or its invented source. `.shokunin/lore/corpus/knowledge/reference-ledger.md` is expressly for real-world method references, says those references are not in-world canon, and separates rights questions from AI-training permission. If external methods are actually consulted, cite them there for the method only, keep rights and training permission distinct, and do not treat those references as story evidence. No rights, license, reuse, or training-permission status is established by an in-world source ID or by the “newly authored” label.

## Limits and falsifiers

This citation plan does not establish slate existence, wording as an objective artifact, authorship, placement, seal provenance, chronology, a resolved contradiction, canon, or mechanics. Falsify the proposed mapping if any new factual clause lacks the new in-world `source_id`, if a row states more than Vela says she could know, or if the map turns an inference into a witnessed/authenticated fact. The checker can confirm structural citation resolution only; prose-to-row correspondence requires manual non-author review. No real-world source was used in this audit, so no external reference-ledger entry is warranted.
