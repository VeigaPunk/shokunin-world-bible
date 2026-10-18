# Round 74 independent reviewer — slate wording decision table

## Scope and comparison

I independently compared the candidate `.shokunin/lore/corpus/knowledge/r74-slate-wording-decision-table.md` with r73’s `.shokunin/lore/corpus/fixtures/r73-jorin-slate-claim/editorial-comparison.md`, the r72/r73 reports and clause maps, the earlier decision table `.shokunin/lore/corpus/knowledge/2026-10-12-lore-decision-table.md`, and prior editorial maps/scout findings cited in `reports/r74-prior-scout.md`. This is a prose/editorial review, not a checker or regression verdict. I did not edit the candidate, LOG, fixtures, or other files.

R73 already says the reports give different *reported* wording and leaves same slate/inscription, reading times, and source relationship unresolved; it expressly does not establish change or direct contradiction. The older round-1 decision table chiefly governs structural checker decisions and limits, not this pair of reports or what evidence would separate explanations. Earlier maps/scouts repeatedly caution that shared labels do not prove a shared referent or occasion; they are relevant warnings, not a prior slate-specific three-test table. Therefore the candidate would be redundant if it only relabeled those unresolved questions.

## Are the three evidence tests distinct?

**Mostly yes, narrowly, as prospective tests—not as established evidence or mutually exclusive explanations.** The candidate turns the uncertainty into different things an editor could seek:

1. **Physical identity:** “Two distinct identifiers reliably linked to the respective readings” (candidate row **Different surfaces**) would bear on whether the reports concern separate surfaces. This is not just asking whether the reports say “a slate”: it asks for object-level identifying evidence separately tied to each reported reading. It does not establish either wording’s accuracy.
2. **Same-object, ordered observations:** “Same-surface linkage and ordered observations showing different wording” (row **One surface, readings at unknown times**) requires both common-object linkage and provenance-preserving observations with supported order. That is a different test from identifying two objects: it could bear on different reported readings of one identified surface. The row appropriately says it cannot establish when a difference arose, persistence between observations, cause, or reason. The ordering requirement is not a fact or chronology supplied by the reports.
3. **Occasion-linked independent capture:** a “contemporaneous transcription or image” tied to “that particular reading occasion” (row **Inaccurate report**) could test whether a particular report matches what was present on that occasion. That target differs from comparing ordered observations to distinguish separate surfaces from a possible one-surface account. It substantially overlaps in evidence form with the second test—an independently captured, time-anchored observation could serve both purposes—but the required linkage and question differ: this row requires a specific report/occasion match and addresses accuracy, while the second requires common surface plus ordered observations and addresses the relation between readings. “With an attributable capture/provenance trail” and the conditional limit that a capture without surface-and-occasion linkage does not discriminate are useful safeguards.

These tests are not wholly orthogonal, and “different surfaces” versus “one surface” are alternatives about object identity while inaccuracy can coexist with either. The table expressly calls the possibilities “nonexclusive” and “not an exhaustive diagnosis”; that is correct. The distinction is sufficient for a modest next-evidence aid, not evidence that any test is available or that the possibilities are true. If a reader treats the rows as three exhaustive, exclusive answers, that would exceed the note.

## Calibration audit and pointers

The note keeps both excerpts attributed and separately pointed: Vela’s excerpt plus `entities.json` `/6/claims/1` → `sources.json` `/6` (`vela-slate-note`); Jorin’s excerpt plus `/7/claims/1` → `/7` (`jorin-slate-note`). Its quoted phrases match the reports at the level relevant here: Vela “KEEP THE EAST GATE CLEAR” and Jorin “KEEP THE EAST GATE OPEN.” The r73 comparison pointer is also explicit. These are pointers to fictional reports, not independent authentication.

Conditional framing is sustained: “may concern,” “may refer,” “could support,” “not established here,” “No evidence below is claimed to exist,” and “No such capture is established here.” The note does not claim extant identifiers, images, copies, registries, or other corroboration; it does not infer a shared slate, time, persistence, change, or inaccurate/lying witness. “A single observation may be insufficient” further limits the table. The phrase “different readings of one surface” is bounded by the explicit same-surface and ordering conditions, rather than asserted as the current situation. I find no invented extant evidence, canon, or time.

## Axis verdicts

| Axis | Verdict | Basis |
|---|---|---|
| **Depth** | **GO — narrowly improved** | Beyond r73’s list of unknowns, the note gives three distinct, concrete evidence-to-seek tests and specifies what a positive result could and could not discriminate. The identity / ordered-observation / occasion-accuracy targets are useful though overlapping. This is a modest editorial decision aid only, not a new in-world fact. |
| **Coverage** | **NO-GO for improvement; unchanged** | This is a Markdown knowledge note. It adds no checker behavior, fixture data, or query path. Neither pointers nor a table expand structured coverage. |
| **Calibration** | **GO — no harm; unchanged** | Questions remain conditional and nonexclusive; the note explicitly disclaims known evidence and limits each inference. It preserves the r73 distinction between different reported wording and a proven shared object, change, contradiction, or truth finding. |

**Overall reviewer recommendation: GO, narrowly, for the declared depth move; calibration unharmed.** This is not a regression-replay finding and does not decide source truth, canon, rights, or game mechanics.
