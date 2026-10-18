# Round 65 scribe — forward/reverse source-status decision table

## Decision and scope

**NO-GO for material calibration.** The proposed distinction—only demand a sourced reverse edge when the forward edge itself has a unique source—has a plausible policy rationale, but existing code and prior decisions establish a different bounded convention: check each eligible faction-directed `allied_with` row for a uniquely sourced reverse witness, while separately reporting the forward row's citation status. No measured matched probe demonstrates that withholding the missing-reciprocal finding improves repair, and it would remove an independent structural pointer. Do not change code or fixtures on this evidence.

This is about checker input/status only. It makes no claim about alliance truth, source prose, canon, or rights.

## Current behavior (code inspection)

In `corpus/fixtures/check_bible.py`, `source_status()` at lines 97–101 classifies a source ID by availability and admitted-row multiplicity. `source()` at 103–112 reports the direct citation finding. The relation citation pass invokes that helper independently for every relation row (around 157). The alliance loop at 249–267 selects `allied_with` rows, requires unique faction endpoints (256–259), then searches for a reverse row whose `source_status(candidate['source_id']) == 'unique'` (260–265). It does **not** require unique status on the forward row. The missing-reciprocal message is suppressed when sources are unavailable (266), but not when available and the reverse is absent/unknown/ambiguous.

| Forward row source status | Reverse row state/status | Sources loaded? | Observed decision from code | Other diagnostic |
|---|---|---:|---|---|
| unique | absent | yes | report missing sourced reciprocal | none on forward citation |
| unique | present, unique | yes | reciprocal satisfied | none on either citation |
| unique | present, unknown or ambiguous | yes | report missing sourced reciprocal | reverse unknown/ambiguous citation; duplicate-ID finding for ambiguity |
| unknown or ambiguous | absent | yes | report missing sourced reciprocal | direct forward unknown/ambiguous citation; duplicate-ID finding for ambiguity |
| unknown or ambiguous | present, unique | yes | reciprocal satisfied | direct forward citation finding remains |
| any | any | no | no missing-reciprocal conclusion | loader error; direct source statuses are unavailable, not unknown |

“Reverse row state/status” means a reverse relation record and its source-ID status, not source-text support. Endpoints must separately satisfy the unique faction conditions. Self-relations are skipped. Other relation types are outside this loop.

## Relevant precedent and evidence limits

Round 2's proposed table says a valid faction `allied_with` with no reverse edge gets a missing-reciprocal finding, and that a reverse edge without a valid source does not satisfy the condition. It does not make the forward citation a precondition. Round 7 deliberately established that the reverse candidate must have a unique source; `r7-ally-reverse-ambiguous` reports the duplicated source, reverse local ambiguity, and missing qualified reciprocal. The r7 adjudicator treats this as calibration, specifically “no uniquely cited reverse witness,” not alliance falsity. Round 31 confirms generic relation citation status is diagnosed independently from alliance-specific qualification. Round 61 gates the alliance missing-reciprocal conclusion when the source table is unavailable, while retaining unrelated relation checks.

These reports establish the reverse-witness qualification and unavailable-source boundary. They do **not** test forward unknown/ambiguous source with absent reverse. Current-round LOG's hypothesized policy (forward source must also be unique) remains hypothetical; no candidate or probe output has been supplied. Do not convert a plausible convention into evidence.

## Falsifier, repair-pointer risk, and minimum evidence

A useful falsifier is a byte-matched pair with the same valid faction endpoints and absent reverse: unique forward citation versus unknown forward ID, then a second pair with that ID made ambiguous. Capture exact checker outputs. Also test the reverse-present cases (unique, unknown, ambiguous) and source table unavailable. Any candidate must preserve direct forward citation errors, endpoint checks, reverse citation errors, and the r7 ambiguous-reverse result; source-unavailable must continue suppressing only source-dependent conclusions. If the unknown/ambiguous forward case loses a useful “add or inspect reverse record” pointer without reducing misleading or redundant output, the proposed gating is harmed and should be rejected. Conversely, material GO would require actual matched output evidence showing that suppressing this finding improves operator repair without obscuring a distinct defect; policy preference alone is insufficient.

No implementation, fixture, README, or LOG change is recommended. This report is the only authorized write.
