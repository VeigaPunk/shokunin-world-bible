# Round 29 critic — unsupported is not false

## Falsification attempt

The proposed negative control is conceptually sound only as a statement about what one authored sentence entails. “The blue seal was near Mira” expresses proximity; it does not entail that Mira carried the seal. It also does not entail that she did **not** carry it at another time, that another clause/source does not establish carrying, or that the `carries` record is false in canon. The unchanged JSON row is simply not supported by this excerpt. This distinction is explicit in the r29 decision table (`.shokunin/lore/reports/r29-scribe.md:3-6`) and is consistent with the r28 map's boundary that only `relations[0]` is mapped, while other JSON claims remain unsupported (`.shokunin/lore/corpus/fixtures/r28-courier-excerpt/relation-clause-map.md:11-17`).

## Specific overreach risks

1. **Closed-world inference:** Calling the row false because this one sentence omits carrying would treat the excerpt as exhaustive. It is not described as exhaustive; its text is a single authored sentence (`.shokunin/lore/corpus/fixtures/r28-courier-excerpt/courier-log-excerpt.md:1-3`).
2. **Identity slippage:** “Mira” and “the blue seal” do not by themselves identify entity IDs. The r28 map calls `mira`/`seal` alignment editorial, not lexical entailment (`.shokunin/lore/corpus/fixtures/r28-courier-excerpt/relation-clause-map.md:7-9`). The negative map must retain that condition; otherwise it overstates even which record the sentence concerns.
3. **Structural checker confusion:** The positive fixture's clean result is explicitly only structural and the checker reads neither Markdown (`.shokunin/lore/corpus/fixtures/r28-courier-excerpt/relation-clause-map.md:15`). Therefore matching exit 0 on a near-miss variant cannot prove either support or contradiction. It demonstrates only no JSON/checker structural change, if verified.
4. **Over-broad negative claim:** Rejecting *this clause as support* is warranted; rejecting `carries` as supported by every possible source or asserting no carrying occurred is not. Round 29's stated negative decision correctly labels it “unsupported,” not “contradicted/false” (`.shokunin/lore/reports/r29-scribe.md:6`).

## Falsifiable test

Compare the exact pair: r28 excerpt sentence at `.shokunin/lore/corpus/fixtures/r28-courier-excerpt/courier-log-excerpt.md:3` (“I, Mira, carried the blue seal.”) versus the proposed r29 replacement (“The blue seal was near Mira.”), with all five JSON tables and source IDs verified byte-identical. A named non-author reviewer should (a) accept only narrow lexical support for `relations[0].type=carries` in the positive, conditional on the editorial ID stipulations, (b) reject the negative sentence as entailment of carrying, and (c) refuse to label the existing relation false, contradicted, or canonically absent on that basis. If the negative map says the relation is false, if it silently treats proximity as carrying, if the ID alignment is represented as text-proven, or if JSON differs, the calibration claim fails. A checker exit 0 is not a substitute for (a)-(c).

## Limitation

I could not inspect a committed r29 near-miss fixture or reviewer artifact in this checkout; only the r29 decision-table draft and r28 control were present. Thus this is a falsification criterion, not verification that the paired artifact or replay was completed. No assertion about canon truth follows from either unsupportedness or the r28 positive fictional example.
