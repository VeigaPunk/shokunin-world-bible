# Round 67 prior scout — claim source_id nonempty requirement

## Decision

**GO, narrowly, to the declared matched calibration experiment; do not count an axis gain yet.** The reviewed r5/r7/r61 evidence overlaps the broad topics of malformed input, claim citations, duplicate IDs, and unavailable source tables, but I found no observed prior case that tests an empty/whitespace `entities[*].claims[*].source_id` specifically when `sources.json` is unavailable. This is a prospective claim-input validation distinction, not new source-membership behavior. Materiality remains unproven until the proposed control pair is run and independently reviewed.

## Commands and observed results

From repository root, I read `.shokunin/lore/LOG.md` Round 67 and `/tmp/mission-lore-standing.md`, then inspected these primary records: `.shokunin/lore/reports/r5-{loader-scout,schema-scout,citation-scout,reviewer,axis-adjudicator}.md`, `.shokunin/lore/reports/r7-{source-scout,fixture-scout,reviewer,independent-verifier}.md`, and `.shokunin/lore/reports/r61-{prior-scout,executor,reviewer,independent-verifier,axis-adjudicator}.md`. Search command:

```sh
grep -RniE 'claim.*source_id|claims\[[^]]+\].*source|whitespace|empty source|nonempty source_id' .shokunin/lore/reports/r5-* .shokunin/lore/reports/r7-* .shokunin/lore/reports/r61-*
```

Observed search hits include r5 citation scout's *proposal* to change `entities.json[0].claims[0].source_id` to an absent ID (not an executed empty-ID case); r7's ordinary/ambiguous claims; and r61's source-table availability reports. No result documents a blank/whitespace claim source ID probe. This is a bounded search of the named reports, not proof that no private or unrecorded probe ever existed.

Inspected `.shokunin/lore/corpus/fixtures/check_bible.py` directly. Its claim predicate checks that `statement` is a nonempty stripped string and `source_id` is a string, but does not check `source_id.strip()`. If so, it calls `source()`. `source_status()` returns `unavailable` before examining IDs when `sources_available` is false; `source()` emits only for `unknown` or `ambiguous`. Thus a string `''` or whitespace-only passes this claim-local predicate and yields no claim-local finding with unavailable sources. This is code-path inspection, not a run of the proposed mutation.

I ran existing controls, without changing them:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r61-direct-unavailable
```

Observed exit 1; stdout was exactly a `sources.json: cannot load JSON` violation and `1 violation(s); no canon changed`. Its claims have ordinary nonempty IDs (`courier-log` / `archive-ledger`), so it demonstrates r61's unavailable-index behavior, not the empty-ID case.

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r61-direct-empty
```

Observed exit 1 with 11 `unknown in-world source` findings for populated references, including claim `.source_id` locations; summary `11 violation(s); no canon changed`. This is a loaded-empty source index control, not a blank claim ID.

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r5-invalid-citation
```

Observed exit 1 with `relations[0].source_id: unknown in-world source 'absent-source'` and one violation. This r5 case is a relation citation, not a malformed claim field.

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r7-item-ambiguous
```

Observed exit 1 with duplicate `archive-ledger` plus local ambiguous findings, including two claim source locations; seven total. These are nonempty IDs in a successfully loaded, duplicate-source table. R7's `reports/r7-reviewer.md` also records an executed temporary ledger ambiguity probe, not an empty claim ID.

## Prior-art overlap and boundary

- **R5:** `.shokunin/lore/reports/r5-loader-scout.md` did observe missing/invalid/nonarray `entities.json` cascades, and `.shokunin/lore/reports/r5-schema-scout.md` exercised malformed entity/claim shapes. The admitted r5 fixture/table cases in `.shokunin/lore/reports/r5-axis-adjudicator.md` concern loader/error classes and a relation's unknown source; the citation scout's claim-source mutation is explicitly a recommendation. These establish malformed-input and cascade prior art, not this claim-field defect or its behavior under source-index unavailability.
- **R7:** `.shokunin/lore/reports/r7-reviewer.md` and `r7-item-ambiguous` demonstrate claims routed through source status and duplicate-ID ambiguity; `.shokunin/lore/reports/r7-source-scout.md` bounds these as ID membership/uniqueness only. Neither is a nonempty-field check: the observed IDs are populated and source tables load. The source-text, truth, and canon boundary remains unchanged.
- **R61:** `.shokunin/lore/reports/r61-prior-scout.md`, `r61-reviewer.md`, and `r61-axis-adjudicator.md` establish the broad unavailable-versus-loaded-empty distinction and that unavailable source status withholds membership-derived conclusions at direct references, including claims. This is the closest overlap and the feature is not novel as a source-table availability policy. But r61's direct controls use populated source IDs; its exact policy explains why a malformed empty claim ID can now escape a claim-local diagnostic. R61 therefore supplies the interaction/prior behavior, not this required-field validation. Do not call this a new source-status rule or rediscover r61's general availability distinction.

## Materiality, falsifier, and limits

The potential incremental value is narrow: flag an invalid required claim field locally even when the independent source index cannot be consulted. The direct file error already tells the operator to repair/retry `sources.json`, while a claim-local nonempty-field finding can identify a second input defect without asserting that any source exists or supports the claim. This is plausible but not yet measured as useful; one crafted edge case alone does not establish broad calibration improvement.

Retain the declared falsifier: compare otherwise-identical unavailable-source inputs with (a) a structurally valid nonempty claim ID and (b) empty/whitespace claim ID; verify the control does not gain a fabricated lookup result, the invalid claim gets exactly the intended claim-local required-field diagnostic, and there is no extra unknown-source cascade. Also check loaded-source behavior and existing raw outcomes as planned. NO-GO if current behavior already emits the required claim-local defect, the change mislabels membership/support, or the result adds no useful distinction beyond the load error. GO here means only proceed to that bounded test, not implementation approval or admission.

No source prose was inspected. This report makes no claim about source-text support, fictional-world facts, canon, rights, or game mechanics. No checker or fixture was edited; only this report is written by this scout.
