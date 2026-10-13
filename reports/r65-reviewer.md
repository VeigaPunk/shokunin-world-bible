# Round 65 non-author reviewer — forward-source eligibility

## Verdict

**NO-GO before executor; no demonstrated material calibration or operator-repair gain.** The active policy’s asymmetry is real, but it supports a bounded reading of reciprocity: each eligible directed faction row requires a reverse witness with a unique source ID; ordinary citation validation independently diagnoses the row itself. Requiring the forward citation to resolve uniquely before reporting a missing reverse is a plausible alternative, not an established correction. Suppressing the finding would lose a distinct reverse-edge repair pointer while retaining only the direct citation error. No source prose, fictional alliance truth, canon, chronology, or rights inference is made.

## Precedent and active checker

R2’s decision wording says an eligible `allied_with` row with valid faction endpoints and no reverse edge is reported at the original relation; a reverse edge without valid source does not satisfy the condition. It does not say that the forward citation must resolve uniquely. R7 explicitly narrows the *reverse witness*: a uniquely cited forward plus ambiguous reverse must still report missing qualified reciprocity. R31 exercises generic, non-alliance relation citation ambiguity independently; it does not define forward eligibility. R61 gates source-index-dependent findings when the entire source table is unavailable, distinct from an available index containing an unknown/ambiguous ID.

The active checker independently calls `source()` for each relation, then the alliance pass accepts a reverse only when `source_status(candidate['source_id']) == 'unique'`. It does not test forward status. I made temporary probes from `ally-one-way`, changing relations/source JSON only in `/tmp`; no pair-scout source files were copied or used. Exact observed current tuples (stdout; stderr empty):

- Unique forward / absent reverse: exit 1; `VIOLATION: relations[0]: allied_with faction relation 'quay-guild' -> 'bell-wardens' lacks a sourced reciprocal relation` then `1 violation(s); no canon changed`.
- Unknown (`ghost`) forward / absent reverse: exit 1; `VIOLATION: relations[0].source_id: unknown in-world source 'ghost'`; `VIOLATION: relations[0]: allied_with faction relation 'quay-guild' -> 'bell-wardens' lacks a sourced reciprocal relation`; `2 violation(s); no canon changed`.
- Unknown (`ghost`) forward / unique reverse: exit 1; forward unknown citation plus `VIOLATION: relations[1]: allied_with faction relation 'bell-wardens' -> 'quay-guild' lacks a sourced reciprocal relation`; `2 violation(s); no canon changed`. This is the directional asymmetry: the reverse row’s required witness is the unknown forward row, which does not qualify.
- R7 reverse-ambiguous control: exit 1 and stderr empty. It reports duplicate `harbor-compact`, the local ambiguous citation at both relation rows, the associated entity first-appearance/claim ambiguity findings, and missing-sourced-reciprocal findings for both rows. Duplicate-ID ambiguity alters all references to that ID; these output lines must not be interpreted as isolated relation-only effects. R7’s intended unique-forward/ambiguous-reverse finding is preserved among them.

These are present-checker outputs, not a candidate’s hypothetical outputs or a claim that the IDs support source content.

## Axes, falsifier, and limits

- **Calibration:** no material gain shown; the direct citation finding identifies a citation defect, while the reciprocal finding locates a separate absent direction. Removing the latter may impair repair. Falsifier: a concrete matched operator task showing the present two-pointer output causes a wrong repair and a narrowly gated output reliably improves it without hiding reverse-edge guidance or other diagnostics.
- **Depth:** unchanged; no deeper relation or source-text evaluation.
- **Coverage:** unchanged; no new checker coverage admitted.

The ambiguous-source probe’s global duplicate naturally causes collateral reference findings; do not claim it isolates one relation row. Forward-source gating could also create asymmetric expectations in the unknown-forward/unique-reverse case. No candidate was run, and no regression/preservation claim is made here. I verified the checker and corpus were not modified by this review; only this report is written. No source-prose, canon, rights, or permission claim follows from source-ID membership/uniqueness.
