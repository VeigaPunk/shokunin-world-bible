# Round 63 critic — strict non-finite token policy

## Independent verdict: NO-GO on material CALIBRATION (probe evidence only)

The failure mode is real and reproducible, but a new parser policy is not yet shown to improve a user-facing lore decision enough to justify whole-file unload and compatibility risk. I recommend no implementation/admission on the present evidence.

## Evidence and controlled observations

- `.shokunin/lore/corpus/fixtures/check_bible.py:41-57` decodes all five files with `json.loads(..., object_pairs_hook=unique_object)`. `unique_object` (`:16-22`) rejects repeated names (r59); no `parse_constant` handler exists. Required schema fields/types are checked at `:65-76`; extra fields are not rejected. The contradiction ledger and later indexes consume parsed rows. This is input-validation behavior, not a finding about the fictional record's truth.
- The r63 declaration and `reports/r63-parser-scout.md` report an out-of-repository probe: inserting `extra: NaN` into `sources[0]` yields exit 0 CLEAN. I independently repeated outside the repo against `consistent/`: `NaN`, `Infinity`, and `-Infinity` in that ignored extra field each yielded exit 0 CLEAN. A nested ignored field in `entities[0].claims[0]` with NaN likewise remained CLEAN.
- Typed probes do not demonstrate equivalent risk: NaN in `timeline[0].tick` or `entity_id` is rejected by existing required-type checks; a finite decimal in the int slot is also rejected. `type(value) is int` is deliberate schema validation (`:70-76`, tick use later). This limits the demonstrated gap to tolerated extension/ignored members, not all numeric fields.
- R5 (`LOG.md`, Round 5 closure; `corpus/knowledge/2026-10-12-malformed-error-patterns.md`) already has an invalid-JSON/load-error class, but did not probe Python's non-standard constants. R59 (`LOG.md`, Round 59 closure) established recursive duplicate-member rejection and its whole-file cascade costs; that policy is adjacent prior art, not proof that a strict-number grammar was promised. README/schema material inspected does not specify producer-side strict JSON conformance. A repository search over current fixture JSON found zero `NaN`, `Infinity`, or `-Infinity` spellings, but this says nothing about external supported producers.

## Materiality and possible harm

The observed ignored-field case is malformed JSON accepted as CLEAN, a plausible calibration concern. Yet no known downstream consumer uses the extra value, and no actual entity/source/event/index decision changes: the required schema fields and all known checks remain unaffected. Thus the CLEAN is about an unchecked extension member, not a demonstrated false lore result. R5's invalid-JSON class does not settle expected treatment of decoder extensions. A blanket `parse_constant` rejection would convert any occurrence at any depth into a file-level error; if in `entities.json`, `sources.json`, or `timeline.json`, it can hide otherwise usable rows and create downstream reference/index cascades. R59 documents why such cascades are consequential. Before admission, a supported producer/input contract or a concrete checker-facing semantic risk is needed, alongside measured cascade behavior and preservation of independent checks. Absence from this fixture corpus is not producer compatibility evidence.

Falsifier that would change this verdict: establish that supported producers promise standards-conformant JSON (or show a relevant typed/nested consumer where acceptance bypasses a material rule), then compare minimal matched cases for all three constants versus finite controls, record exact error and unload cascades, and prove independent checks survive. If only ignored metadata is affected and compatibility is undocumented, retain NO-GO or make the strictness boundary an explicit operator decision; do not silently impose it.

## Boundary

Rejecting a token would establish only input-format rejection. It would not establish source support, citation validity, event existence, chronology, fictional-world absence, canon, real-world attribution, rights, license, or permission. The producer contract remains unverified. No checker/fixture/README/LOG edits or commits were made.
