# Round 64 non-author reviewer — malformed-row raw ID

## Verdict: NO-GO before executor

The evidence supports the stated current behavior, but not a material operator benefit from changing it. Keep the current schema error plus dangling reference findings; do not advance to implementation. This is a calibration no-go, not a claim that the raw ID is false or that a fictional entity is absent.

## Independent temporary probe

I copied the `consistent` fixture into temporary directories and invoked the unchanged checker. I tested a valid `mira` row, no `mira` row, an invalid `{"id":"mira"}` row (missing required fields), a valid duplicate `mira`, and an unavailable `entities.json`. Results:

- Valid row: CLEAN.
- No row: three `mira` dangling findings (relation source and two timeline actors).
- Malformed matching row: four row-local required-field findings plus those same three dangling findings.
- Valid duplicate: duplicate-ID and affected-reference ambiguity findings; it is not collapsed into dangling.
- Unavailable table: loader error only; dependent reference findings are gated.

These are observations of the current checker, not candidate behavior. The raw ID in the invalid object does not resolve identity or serve as a kind, holder, place, faction, or occupancy witness. The controls also preserve the R60 loaded-vs-unavailable distinction. Temporary files only; no corpus/checker edits.

## Materiality and prior art

The malformed-ID and absent-ID outputs differ because the malformed case adds actionable row-local schema locations. Yet the dangling findings still give the reference-side repair pointer: investigate the reference or add/fix an admitted target. Removing that pointer in favor of “cannot assess” has no demonstrated operator decision improvement. Emitting both a new uncertainty status and dangling may duplicate diagnostics rather than improve actionability. This is precisely the materiality concern from R56: extra local precision can be technically accurate without earning an axis gain.

R26 establishes the boundary that a malformed raw duplicate does not count as admitted identity/ambiguity evidence; it does not require suppressing dangling. R60 distinguishes wholly unavailable input from a loaded array and explicitly leaves malformed rows excluded from the retained valid-row index. Neither precedent proves benefit for a second raw-ID index. The pair/row scouts’ temporary probes corroborate the current behavior; they do not test a candidate policy or an operator repair outcome. The eight-scout set is overwhelmingly NO-GO, with the scribe’s conditional willingness to probe not an admission recommendation.

## Falsifier and scope

Reconsider only if a concrete, matched repair exercise shows that schema-plus-dangling materially misdirects an operator, and a reference-local invalid-row message improves the chosen repair while preserving a useful pointer. Compare valid, genuinely absent/loaded-empty, malformed exact ID, malformed no-ID or near-match, valid duplicate, and unavailable controls. Preserve schema findings and independent source/tick/dependency checks. Any candidate must leave the malformed row ineligible as a valid unique entity or as any kind/holder/place/faction/occupancy witness, and must not hide actual absence or valid-duplicate ambiguity.

Per-axis: calibration unchanged / claimed material improvement unproved; depth unchanged; coverage unchanged. No candidate output was tested, and this review does not certify a hypothetical implementation.

## Scope and integrity

Reviewed the r64 LOG declaration, all eight scout reports, checker paths, and the r26 malformed-duplicate, r56 rejected-local-provenance, and r60 loaded-row admission precedents. No corpus, checker, fixture, README, or LOG edits; no commit. Only this report was written. No world/canon/source-truth/rights inference.
