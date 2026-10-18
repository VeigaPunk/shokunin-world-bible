# Round 28 scribe — clause map proposal

Scope: a human-readable map for the constructed excerpt and the single `mira -> seal` `carries` record. It is not source-text truth, recovered evidence, canon, or an assertion that checker logic validates prose. The excerpt must be treated as invented fixture text.

## Clause map (proposed)

| Constructed excerpt clause | Candidate record mapping | Reading / boundary |
|---|---|---|
| “I, Mira” | `entities.json` `mira` (character; name Mira); relation `from: mira` | speaker/self-reference maps to the authored entity identifier; it does not independently prove identity. |
| “carried” | `relations.json` row 0, `type: carries` | maps the reported action/predicate only. |
| “the blue seal” | `entities.json` `seal` (item; name Blue Seal); relation `to: seal` | maps the object mention to the authored item identifier, not proof of a uniquely existing object. |
| whole reported event | `relations.json` row 0, `source_id: courier-log` | citation association in the fixture; citation validity is not entailment verification. |
| any unstated time, place, route, motive, duration, or manner | none | deliberately unmapped; do not infer. |
| objective truth / independent corroboration | none | deliberately unmapped; one fictional first-person excerpt cannot establish these. |

The quoted clause text above is a **proposal** for the new, separately constructed excerpt, not a quotation from an existing file. Use the same compact sentence in the fixture artifact, then replace these clause labels with exact verbatim spans and provide `path:line` evidence before treating the map as traced. Do not retrofit it as evidence for existing `consistent/` claims: that directory currently has no committed courier-log excerpt (`LOG.md:421`).

## Evidence and risks

- `relations.json:2-7` encodes `mira` → `seal`, type `carries`, cited to `courier-log`.
- `sources.json:7-12` identifies `courier-log` as a fictional personal log and explicitly calls it an in-world first-person account.
- `entities.json:2-13` gives Mira and the claim “Mira carried the blue seal”; `entities.json:29-39` gives Blue Seal and the claim “The seal accompanied Mira.” These are authored fixture statements, not independent support for the relation.
- `r23-note-class/witnessed-absence-clause-map.md:1-4,8-17` is precedent for a manual map with explicit unmapped boundaries and an explicit caveat that the checker does not read prose.
- Risk: paraphrasing or splitting clauses can overstate entailment; map exact spans, preserve negation/attribution, and mark unsupported facets out of scope. ID mapping is a fixture interpretation, not evidence of real-world or canonical identity.

## Falsifiable check (proposal only)

After a new separate fictional fixture is authored, a non-author reviewer can check the claim mechanically by line-tracing: every mapped clause is an exact contiguous excerpt span and each maps only to the named relation field; no map row asserts time/place/motive/other facts absent from the excerpt; every unsupported facet is marked unmapped. Reject if any span is not verbatim, any record field is misidentified, or the map implies more than the constructed text says. Separately run the existing fixture checker and compare all 78 prior stdout/stderr/exit tuples plus all 389 prior JSON-path bytes to the declared baseline. This validates the proposal’s traceability and regression boundary, not prose truth or the truth of `carries`.
