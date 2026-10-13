# Round 25 non-author reviewer report

## Finding

The new pair is a controlled duplicate-target fixture. It supports the narrow structural claim that a relation `to` endpoint resolving to two admitted entity rows is diagnosed as ambiguous. It does not establish whether `carries` is true, whether both rows refer to one item, or any canon fact. No both-endpoints case is included or needed for this declared target-side probe.

## Evidence

- `r25-to-unique/` and `r25-to-ambiguous/` each contain the same five JSON tables. Their `contradictions.json`, `relations.json`, `sources.json`, and `timeline.json` are byte-identical. The ambiguous `entities.json` equals the unique file with exactly one appended row: `id: seal`, `kind: item`, name `Seal in courier ledger`, `first_appearance: courier-log`, and empty `claims`.
- The original `seal` entity remains unchanged. Both rows satisfy the checker’s required entity-field types and nonempty strings; `claims: []` is a valid list. The added first-appearance source ID resolves locally to `courier-log` in the identical `sources.json`. Thus the second row is admitted rather than an invalid-row artifact.
- The unchanged relation is `mira -> seal`, type `carries`, `source_id: courier-log` in both fixtures. `mira` and `seal` each resolve in the unique fixture; the relation citation resolves to the local source. The referenced source is explicitly a fictional first-person account (`sources.json`), not an omniscient authority.
- Independent checker replay: unique exits 0 with `CLEAN: schema, citations, relations, timeline; 0 violations`; ambiguous exits 1 with `entities[4].id: duplicate entities id 'seal'` and `relations[0].to: ambiguous entity 'seal'`, two violations, and `no canon changed`. Stderr is empty in both. There is no `relations[0].from` ambiguity.

## Risks and limits

- The checker verifies citation-ID resolution, not whether the cited courier log’s text supports the relation or any entity claim. The fixture files contain fictional source descriptions and claims, but this review did not validate their correspondence to source text. Do not describe the pair as source-text or canon proof.
- The duplicate row has no claims; its resolved first-appearance citation does not independently substantiate the row’s identity or the relation. No target row is selected by the ambiguity finding.
- The duplicate-ID violation is expected and distinct from the relation-local `to` ambiguity; coverage rests on the latter, not merely the total violation count.

Verdict: evidence supports the declared narrow `to`-endpoint ambiguity probe, with no observed pair confound or invented source-text/canon claim in the fixture construction. No production edits made.
