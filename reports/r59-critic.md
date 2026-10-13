# Round 59 critic — parser ambiguity calibration

## Scope and evidence

- Candidate is duplicate JSON object member detection, not duplicate row/entity/source/event IDs. The latter are decoded rows and checked later.
- Current decoder is `corpus/fixtures/check_bible.py:21-27`: each file is read and passed to `json.loads`; the exception list includes `JSONDecodeError` but not duplicate-member detection. Python's default object decoder accepts repeated keys and keeps the last value.
- Validation then sees only the decoded dictionary (`check_bible.py:32-43`), so it cannot know that a key was repeated. A duplicate required member such as `place_id` may therefore yield CLEAN or a semantic result based solely on the last value. Reversing the values can change that result; if the last one is schema-invalid, ordinary field checks can instead issue a field error while masking the raw ambiguity. This is a genuine parse observability gap, distinct from repeated row IDs.
- The format documents required fields and semantic checks but does not explicitly specify duplicate-member policy: `corpus/fixtures/README.md` schema section (check current file for exact lines). Thus ambiguity is not already resolved by a stated last-wins convention.
- Prior malformed matrix `corpus/knowledge/2026-10-12-malformed-error-patterns.md` lines 1-18 tests absent file, invalid JSON, top-level shape, non-object row, and invalid citation. Its explicit caveat says it is not comprehensive; it does not test valid JSON with duplicate object members. This is not a contradiction of r5 coverage.

## Actual vs proposed raw behavior

Actual: valid JSON containing `{"place_id":"harbor","place_id":"tower"}` is accepted by `json.loads` as `{"place_id":"tower"}`; swapping member order yields `{"place_id":"harbor"}`. Downstream behavior can differ and no diagnostic identifies the ambiguous raw input. Nested repeated members in `claim_a`/`claim_b` likewise collapse before pointer validation. This does not mean checker claims either place true; it means the checker silently selects a representation.

Proposed candidate behavior (not implemented in this round): use an object-pairs-aware decoder and report duplicate member names as an input-format violation before semantic validation, with deterministic path/member diagnostics. Do not append a partial dict for that file/row or generate consequential occupancy/ledger errors from whichever duplicate happened to win. A parser-wide hook will also see nested objects; diagnostics should identify JSON path where feasible and avoid asserting unsupported row index when duplicate detection occurs before row processing. Preserve the existing generic missing-file/invalid-JSON/shape diagnostics for controls. This should apply to every repeated member, not just one magic field; otherwise the ambiguity persists elsewhere.

## Material calibration assessment: GO, conditional on narrow implementation and validation

This is a material calibration opportunity: distinguish unambiguous structured input from syntactically valid but semantically ambiguous input, instead of silently endorsing Python's last-wins choice. It affects the checker’s reliability as an input validator, not lore truth. A reader can correct the source JSON or resolve which value was intended before relying on downstream checks. It does not add story coverage or factual depth.

The implementation must avoid cascading errors. If a duplicate makes the document undecodable for validation, emit the duplicate error and suppress dependent claims from that rejected object/file, rather than arbitrarily selecting a value and producing occupancy, dangling-reference, or contradiction-pointer conclusions. Do not suppress unrelated valid sections. Explicitly test duplicate valid values in both orders, duplicate with an invalid-type value in both orders, nested duplicate claim pointer, and unique-key control. Compare raw stdout/stderr/exit against all pinned old fixtures; any behavior delta on old cases needs justification. Existing fixture bytes must not be silently rewritten.

## Risks / falsifier

Risk: rejecting repeated members could be stricter than an intended producer convention, and a global hook may add noisy diagnostics or alter malformed-input cascades. The repository currently states no last-wins convention; if an authoritative schema/producer contract is found that defines such members as legal and last-wins, that falsifies this gain. Also NO-GO if duplicate detection cannot avoid validating a chosen partial value, if unique-key controls change, or if old raw outputs acquire unjustified cascades. Duplicate JSON object keys must not be conflated with duplicate row IDs. No inference about fictional source support, actual story truth, canon, rights, or permission follows from this structural check.
