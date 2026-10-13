# Round 59 regression scout — duplicate JSON object members

## Scope and baseline

This scout only read files and ran temporary probes outside the repository; it did not edit the checker, fixtures, README, or LOG. Baseline is round 58 work commit `054b99979f4c5cfa5f615bf26717070510555101` and report commit `7e93686877f7773f946ab89984dee920da8e0cf7`. The active corpus has 95 fixture directories and 474 fixture JSON files. I scanned all 474 raw JSON objects with an object-pairs hook: **zero files contain repeated object member names**. This is a finding about active fixtures, not a guarantee about external inputs. The current checker file is byte-identical to the pinned baseline (`git diff --quiet <baseline> -- .../check_bible.py`, exit 0).

`check_bible.py:18-26` reads each table and calls `json.loads`; `:28-43` validates only the resulting rows. Default Python decoding retains the last repeated member. Later ID ambiguity checks (`:45-51`) concern IDs repeated across array rows, not keys repeated inside one object. No evidence here conflates these cases.

## Existing malformed precedent

`corpus/knowledge/2026-10-12-malformed-error-patterns.md:7-20` records r5's missing file, invalid JSON, wrong top-level type, non-object row, and invalid citation cases. It explicitly limits the cases and notes parser wording/offsets are nonportable. Duplicate object members are valid JSON under the current decoder and are not an r5 case. `corpus/fixtures/README.md` documents schema and checker behavior but no duplicate-member policy. r9's order-swapped duplicate **timeline row IDs** (`reports/r9-axis-adjudicator.md`, opening) were material because baseline last-wins lookup produced an inversion in one order but not the other; the adopted rule reports both rows as ambiguous. That is a useful analogy for order-dependent inference, not a direct precedent for repeated keys in a single JSON object.

## Raw behavior: actual vs proposed

For a temp clone of `consistent/`, I inserted a second `place_id` into the second timeline row, preserving the two distinct valid strings `harbor` and `tower`. Actual CLI output for `harbor` then `tower` **and** the reverse order was exit 0, exactly `CLEAN: schema, citations, relations, timeline; 0 violations`. Because the decoder keeps the final member, swapping the values changes the decoded row from one value to the other; this particular fixture still has no checker rule that makes either value fail.

A separate temporary malformed-type probe puts `"place_id":"harbor","place_id":7` in the first timeline row. That order exits 1 with a `timeline[0].place_id` required-string finding and a downstream unknown dependency for `arrival`; reversing the duplicate members (`7` then `"harbor"`) exits 0 CLEAN. This confirms last-wins can mask a raw member ambiguity and even a wrong-typed earlier value, but is not by itself proof that either member is authoritative or that a new rejection policy is required.

Proposed parser behavior—**not implemented or observed**—would retain member pairs or otherwise detect repeats and reject the affected JSON input rather than select a value. That likely changes the first valid-value probe from CLEAN to an input error in both orders. Exact diagnostic granularity and whether downstream checks are suppressed are undecided. A recursive `object_pairs_hook` sees nested objects too, so scope includes `claims` and contradiction pointers unless intentionally constrained. A malformed/duplicate file could currently produce several semantic findings; parser rejection may suppress them, so error-count/output changes need explicit treatment.

## Material CALIBRATION: NO-GO

The proposed case establishes real silent last-wins parsing, but the **material benefit is not established**: both swapped valid values currently yield the same CLEAN status, and no documented input convention says repeated object members are forbidden or resolve to multiple assertions. The malformed probe shows order-sensitive masking, but adding a new reject-all rule could impose an undocumented format constraint and alter useful error reporting in nested records. The active 474 fixtures offer no duplicate-key example to prove a current-in-corpus misclassification. Therefore do not claim calibration GO merely because a parser hook can detect duplicates or because r9 dealt with repeated row IDs.

**Explicit verdict: CALIBRATION NO-GO on available evidence.** Depth and coverage are unchanged; no axis gain is demonstrated. This is not an assertion that last-wins is semantically correct or that duplicate keys are desirable.

**Falsifier / reversal condition:** establish an explicit existing format contract rejecting repeated members, or independently show an actionable reader decision materially misled by last-wins (for example, a controlled duplicate changes a required semantic result or masks a schema-invalid value), then specify deterministic bounded diagnostics and cascade handling. Validate swapped-order duplicates and nested keys, ensure unique-key controls retain raw output, and replay the pinned 95 fixture CLI stdout/stderr/exit tuples (or enumerate every justified delta). If a producer/schema contract explicitly defines last-wins as intended, that would instead falsify the proposed calibration gain.

## Risks and boundaries

- A universal recursive rejection can affect nested claim objects and alter error cascades; a partial policy leaves ambiguity elsewhere.
- Diagnostic location may be file/object-level because duplicate discovery precedes row validation; do not invent an exact row path unless actually tracked.
- Duplicate JSON object members are not duplicate row IDs. Neither kind of structural diagnostic decides fictional story truth, source-text support, canon, chronology, or rights.
- No actual location/value was selected by this audit; `harbor` and `tower` are fixture strings used solely to demonstrate raw decoder behavior.
