# Round 62 — citation-scout: event-ID membership boundary

## Independent judgment

**NO-GO on material new calibration from citation scope.** The proposed timeline availability policy may prevent loaded-row membership diagnostics from being misread as statements about absent in-world events, but ID-level logic does not evaluate source prose or fictional truth. Current observations demonstrate a cascade of diagnostics under unavailable inputs; they do not establish that users interpret these as world/canon claims. I recommend no citation/canon-specific checker change.

## Observed code and evidence

- `.shokunin/lore/corpus/fixtures/check_bible.py:35-60` distinguishes source/entity availability while loading tables, but `timeline` has no corresponding availability flag. Failed JSON loading or non-array input becomes `[]` with a loader/schema error.
- `:88-92` indexes timeline rows and counts event IDs from admitted rows. The ledger consumer (`:108-137`) checks each event ID against admitted timeline rows; a non-unique/missing ID is reported as `expected exactly one timeline event` and skips that side's event-source lookup; an unavailable timeline therefore resembles a loaded empty timeline for membership. **This is an input-index behavior, not a fictional-world assertion.**
- `.shokunin/lore/reports/r7-provenance-scout.md` reports duplicate source-ID probes: duplicate IDs trigger ambiguity/load-index diagnostics, while chain structural checks continue; its limits distinguish duplicate identifier ambiguity from source-text conflict.
- `.shokunin/lore/reports/r39-citation-scout.md` explicitly says a unique ledger event with a missing source pointer yields reference-integrity diagnostics, not adjudication of either account. It warns citations do not prove event truth, chronology, or rights.
- `.shokunin/lore/reports/r60-citation-scout.md` and `r61-citation-scout.md` document entity/source table availability cascades and proposed narrow suppression. R61 remains NO-GO absent matched controls; that prior discussion is analogous but does not establish timeline-specific materiality.

## Interpretation boundary

An event ID in this checker is a membership key. A matching ID means only that an admitted row with that identifier exists in the loaded input; it does not establish the row's source text supports it, that any account is true, or that the event occurred. Missing ID in a loaded table likewise means only no admitted matching row in that input. Neither state establishes fictional-world nonexistence, chronological truth, canon, real-world history, or rights/licensing/permission. Do not infer any such fact or alter event/world/source prose.

## Candidate probe / falsifier

A future calibration probe could hold all other fixture tables byte-identical and compare: unavailable/malformed/non-array timeline, valid loaded-empty timeline, and loaded timeline containing unique/duplicate event IDs referenced from both ledger endpoints. Record direct loader/schema findings separately from derived membership findings; verify independent ledger shape, source-pointer, and other-table checks persist. The probe has not been run for this report; these are proposed cases, not observed outcomes. A falsifier for a future GO would be that loader plus missing-member diagnostics are already an intentionally complete report, or that suppressing membership findings loses actionable repair information without preventing a concrete misleading conclusion.

## Costs and decision

Suppressing event-ID membership findings when timeline input is unavailable might reduce confusion, but also hides which ledger pointers need repair/recheck; broad suppression risks concealing independent ledger errors. Current evidence gives no measured user-facing misinterpretation or matched timeline probe to balance these costs. **NO-GO**: no material calibration claim or implementation recommendation from this citation review.
