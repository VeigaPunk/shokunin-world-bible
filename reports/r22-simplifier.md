# Round 22 simplifier — per-member malformed dependency handling

## Raw observation (source inspection; no CLI probe performed)

At the dependency branch in `corpus/fixtures/check_bible.py`, current behavior first applies `all(isinstance(dep, str) ...)` to the whole list. If any element is non-string, it emits exactly one row-level `expected event-id strings` error and `continue`s, so no string member in that row is checked for self/repeated/unknown/ambiguous dependency or timeline inversion. The subsequent loop already has an index-based location, explicit string-ID duplicate tracking, unique-ID resolution, and the nonnegative-endpoint inversion guard. Its map/set operations are safe for arbitrary malformed members only because the whole-list guard currently prevents entry. This inspection establishes control flow, not raw paired CLI output or fixture/canon truth.

## Recommendation (smallest safe change)

Keep the existing loop and its semantics, but move the string-type test inside it. For each member, if it is not a string, emit the existing row-level type diagnostic only once for that row and `continue` to the next member; otherwise run the existing self/repeated/ID-resolution/inversion code unchanged. A local boolean (or equivalent) can preserve the current one-diagnostic-per-row wording/count even with multiple malformed members. Do not add malformed values to `seen_dependencies`, coerce them, or infer that their edge is absent/satisfied. This inspects only independently safe string IDs while retaining input order and all existing string-member policies. Ensure the duplicate/self behavior remains exactly as written for string members.

This is a recommendation only: first obtain paired raw CLI evidence for mixed-vs-clean inputs and controls, and replay all 64 saved prior outputs. In particular, disclose that formerly list-wide-skipped mixed inputs may now gain string-member errors; this is intended candidate behavior, not evidence of source chronology or canon.
