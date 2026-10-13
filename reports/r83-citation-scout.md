# Round 83 citation scout — Vela negation and provenance boundaries

## Scope and finding

I read the Round 83 declaration in `.shokunin/lore/LOG.md`, the relevant Vela fixture excerpts/maps and JSON records, the r28–r32, r34 and r36 precedent noted there, and `.shokunin/lore/corpus/knowledge/reference-ledger.md`. This is a report-only citation audit. The excerpt-to-record pointers below are fixture-local editorial attribution; neither a clean checker result nor these pointers authenticate a source, prove an event, determine canon, establish real-world rights, or concern game mechanics.

## Excerpt → claim/event → source

The target wording appears in `.shokunin/lore/corpus/fixtures/r72-vela-slate-claim/vela-note-excerpt.md` (also retained in r40 and r41/r43-derived fixtures): “I did not see Sella or an envelope.” The complete sentence is Vela's first-person fictional report; it must not be detached from that attribution and treated as objective narration.

In r72 `entities.json`, character `vela`, `claims[0]` says: “Vela reports hearing two strokes she took to be the registry bell during Bell-7 and reports not seeing Sella or an envelope.” The matching `timeline.json` row `/4` is event `vela-listening-report`, actor `vela`, place `harbor`, tick `3`, source `vela-note`; its description similarly says Vela reports she “did not see Sella or an envelope.” These are free-text summaries, not separate structured fields for a Sella non-sighting and an envelope non-sighting. `sources.json` row `/4` identifies `vela-note` as a newly authored fictional, unverified first-person report, not omniscient truth. The clause map attributes the phrase to Vela and limits it to reported sighting; it expressly does not establish either subject's absence.

On ordinary English reading, “did not see Sella or an envelope” can be read distributively as two non-sightings in Vela's account. Replacing it with “did not see Sella with an envelope” naturally denies seeing that joint scene, leaving separate sightings unspecified. But the old claim/event do not encode two independently addressable propositions. A map or editorial paraphrase may distinguish those likely readings; neither they nor the checker make a formal split. If a joint-only excerpt is paired with the inherited stronger paraphrase, the concrete mismatch is that the paraphrase says Vela reports not seeing each target, while the changed excerpt supports only the joint-scene non-sighting. Any repair should narrow the attributed prose (or restore the excerpt); it should not assert a positive sighting or actual presence/absence. This is an editorial scope judgment, not a finding about fictional events.

## Precedent and checker boundary

The fixtures README's r28–r30 examples distinguish lexical support (“carried”), unsupported proximity (“near”), and explicit negation (“did not carry”), conditional on editorial ID and proposition/occasion alignment; r30 does not turn a clause-scoped denial into global canon. They do not test disjunctive versus joint “with” scope. R31–r32 concern source-ID ambiguity and malformed source rows, not negation semantics. R34 changes “saw” to “heard that” (modality); r36 changes the stated date while inherited structured text stays stale. Those are related prose/record calibration precedents, not this exact scope contrast.

The fixture checker reads JSON structure and references, not Markdown prose. It can validate a source ID and event/source links; it cannot decide whether “or” distributes, whether “with” is joint, whether the claim/event paraphrase the excerpt, or whether Vela's account is true. Checker CLEAN on both variants would therefore be expected and would not adjudicate the proposed human editorial mismatch. Local tick 3 is not a timestamp or evidence of a shared Bell-7 occasion.

## Fictional attribution, real-world rights, and limits

The in-world `sources.json` row `vela-note` is a fictional source label for a newly authored fictional excerpt. It does not establish an independently existing in-world document, author identity, authenticity, custody, or corroboration. Vela's claimed Bell-7/date and position are attributed fictional claims, not authenticated chronology or a basis to settle the inherited Tarin/Sella ledger.

Separately, `.shokunin/lore/corpus/knowledge/reference-ledger.md` is explicitly headed “Real-world method references (not in-world canon).” Its PROV-O, JSON Schema Validation, and Python `graphlib` citations attribute method inspiration; the ledger states rights questions are not granted or resolved and AI-training permission is not assessed. That real-world references ledger is not the fictional `sources.json` ledger and supplies no story evidence or rights grant. No legal conclusion is made here.

**Citation-scout conclusion:** the pointer chain consistently attributes the excerpt, summary claim/event, and source ID, but attribution and structural resolution are not authentication or semantic validation. The ordinary-language scope distinction is plausible and the concrete prose-to-summary repair is identifiable, while the two separate negatives are not modeled as separate fields. This finding makes no source-authenticity, canon, real-world rights, or mechanics claim.
