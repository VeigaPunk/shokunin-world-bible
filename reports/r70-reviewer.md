# Round 70 independent reviewer — missing-ID pair gate

## Verdict

**NO-GO for admission; calibration gain is plausible but not established, and the discarded pair warning may be independently useful repair guidance.** The narrow candidate preserves the R62 valid-ID/invalid-field warning and correctly isolates the intended output delta. But that does not show that removing the warning for absent/blank IDs improves users’ repairs. In the matched missing-ID fixtures the two fields are already equal, so the old pair warning conveys an additional constraint: after supplying IDs, the two pointers must not end up identical. The candidate discards that early signal. Neither the candidate outputs nor the old-suite replay measure which behavior improves repair.

## Independent matched replay

I read the Round 70 declaration and integration in `.shokunin/lore/LOG.md`, the checker diff, all seven `r70-*` five-table fixtures, their README subsection, and the R70 critic, branch/prior/fixture/validity/regression scouts, simplifier, scribe, and executor reports. I independently extracted checker `5ccbffaf4b593dcfa34bf92a8ac351c83a105ab3` and ran both it and the current checker against each new fixture with the same repository-root command. This is a direct matched old/current probe, not reliance on the executor’s stated output.

The only observed tuple change is the declared one:

- `r70-absent`, `r70-empty`, and `r70-whitespace`: old emits two required-ID findings **and** `claim_a and claim_b references must differ`; current retains the two local required-ID findings and omits the pair finding. Both versions exit 1.
- `r70-valid-id-invalid-field`: both versions retain both field findings and the pair finding (exit 1), consistent with R62’s valid, nonempty ID / invalid-field precedent.
- `r70-valid-identical`: both retain the pair finding (exit 1).
- `r70-valid-different` and `r70-distinct-field`: both remain clean (exit 0).

These are useful controls: the guard does not appear to erase the field diagnostics, broaden comparison to distinct pointers, or suppress the R62-style malformed-field hint. The declarations/scout/executor also report exact preservation of the 130 existing raw CLI tuples; the regression scout’s synthetic replay is not independent candidate validation, and I did not reproduce that entire 130-case run in this review.

## Materiality and axes

**Calibration:** The old comparison treats two missing values as an equal reference and labels them “references must differ,” although neither side supplies an event ID. That is a real mismatch between the pair diagnostic’s apparent target and its inputs. Yet the line can also warn that the two references must ultimately differ, independently of the local requirement to fill in each ID. If both IDs are entered alike, that constraint will matter; the warning could preempt a later repair pass. It is not merely a duplicate local missing-ID message. The seven fixtures demonstrate exactly which assertion is removed, not that it is unhelpful or that removing it leads to better repairs. No repair-task evidence resolves the tradeoff. Thus material net calibration improvement is **unproven**, with a credible risk of losing useful independent guidance.

**Depth:** **Unchanged.** This is a predicate change over existing input diagnostics, not a richer model.

**Coverage:** **Unchanged** if the reported prior 130-case preservation is accurate; none of the existing rule classes is added or removed from the tested valid-ID cases. The new controls improve evidence about this narrow branch, not lore-rule coverage.

The critic’s NO-GO concern remains live. I would reconsider with an explicit repair comparison: identical missing-ID / equal-field input repaired by independent editors with and without the pair warning, alongside a missing-ID / distinct-field control and the retained R62, valid-identical and valid-different controls. Record whether the warning changes the first repair or prevents a follow-up pass. Until then, do not call the removed warning demonstrably unsupported or claim material calibration gain.

This assessment is confined to supplied JSON validation behavior. It makes no source-text, event-truth, story, canon, rights, or game-mechanics claim.
