# Round 83 semantics scout — separate versus joint non-sighting

## Question and source pointers

The controlled excerpt in `.shokunin/lore/corpus/fixtures/r72-vela-slate-claim/vela-note-excerpt.md` says: “I did not see Sella or an envelope.” Its claim is paraphrased in `entities.json` under `vela` / `claims[0]`; the corresponding `timeline.json` event is `vela-listening-report`. The local `vela-clause-map.md` quotes the clause and correctly limits it to Vela’s reported sighting; it says it does not establish either Sella or an envelope was absent. These are editorially authored fictional, unverified materials, not authenticated source evidence.

## Semantic distinction

On the ordinary distributive reading, “I did not see Sella or an envelope” negates either object of sight: Vela reports no sighting of Sella and no sighting of an envelope (in the contextually relevant observation). It does not say either was absent from the place or that Vela could see everything. It leaves other people’s observations and the underlying events open.

“I did not see Sella with an envelope” instead negates the joint scene/configuration: Vela reports no sighting of Sella together with an envelope. It leaves open that she saw Sella without an envelope, saw an envelope without Sella, or saw neither. It does not entail any of those positive possibilities. “With” can be context-sensitive, but in this controlled contrast its natural joint reading is distinct from separately denying both sightings; a reviewer should not promote it to either separate absence claim without more wording.

Thus the replacement is not a mere stylistic paraphrase if the structured paraphrase keeps “not seeing Sella or an envelope”: it would assert more than the changed authored clause supports. The only warranted inference is about the scope of Vela’s attributed report, not what actually was present.

## Concrete editorial repair

If the excerpt is changed to the joint wording and the existing structured claim/event are retained, revise the Vela claim and `vela-listening-report` description to the narrower attribution, e.g. “Vela reports not seeing Sella together with an envelope.” Update the local clause map to quote the exact replacement and state that separate sightings are unspecified. Do not leave “reports not seeing Sella or an envelope” as the paraphrase: that preserves the old, stronger scope. The repair is to prose-to-record alignment, not to assert that Vela saw either item, that either was absent, or that any other account is resolved. Keep the source link as attribution only.

## Boundaries and assessment

- **Authored attribution vs source authenticity:** the excerpt and map are constructed fictional text attributed to Vela. Neither source metadata nor a source ID authenticates a real or in-world original, Vela’s identity, or the reported observation.
- **Checker structure:** the checker validates structured files and references; it does not interpret this Markdown negation or establish semantic support. A clean result for either wording cannot settle the scope distinction. The manual claim/event/map alignment is where the mismatch should be repaired.
- **Canon, rights, mechanics:** this is no finding about fictional-world truth/canon, real-world rights, or game mechanics. It adds no record of actual presence, absence, envelope placement, or shared occasion.
- **Novelty/materiality:** r34 distinguishes direct sight from hearsay; r30 distinguishes explicit negation from unsupported proximity and warns against global/temporal overreach; neither distinction alone is the same as negation taking scope over a disjunction versus a joint “with” predicate. Still, this is a narrow semantic contrast and appears to call for a manual wording/map repair, not a new checker rule. Its value depends on a non-author actually identifying the stronger old paraphrase and choosing the narrower repair; a cleaner explanation alone would not prove broader coverage gain.

Falsifier: if a non-author reads the two clauses as conveying the same separate non-sightings, or cannot identify any concrete structured paraphrase that must be narrowed, this is not a useful new calibration case. Do not infer any absence in either variant.
