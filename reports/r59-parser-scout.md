# Round 59 parser scout — duplicate JSON object members

## Scope and evidence

No checker, fixture, README, or LOG edits. Temporary copies of `consistent/` were made outside the repository and passed to the existing CLI; each changed only `timeline.json`. The probes concern repeated *object member names*, not separate rows with repeated IDs.

`corpus/fixtures/check_bible.py:18-26` reads each section file then calls `json.loads`; parse/read failures are caught and reported as `cannot load JSON`. `:28-43` validates the decoded list and row dictionaries, and `:38-40` checks required field types only after decoding. Python's default JSON decoder accepts repeated names and retains the final value. `:45-62` separately diagnoses duplicate IDs across rows; that is not protection against same-object key repetition.

The active documented malformed matrix (`corpus/knowledge/2026-10-12-malformed-error-patterns.md`, rows r5 missing-file, invalid-json, wrong-top-level, row-shape, invalid-citation) covers parse failure, shape, and citation—not duplicate object members. It explicitly limits observations to those exact inputs and says JSON parser wording/offsets are nonportable. `corpus/fixtures/README.md` documents required schema and checker as reporting violations, not repairing data; it does not specify duplicate-member semantics. I found no precedent there for rejecting duplicate members.

## Raw CLI observations

Each probe cloned the five `consistent/` JSON files into a temporary directory. In `timeline.json` only, the first `"place_id": "harbor"` was replaced with a duplicate `place_id` pair. With values `harbor` then `tower`, the CLI exited 0 and printed exactly `CLEAN: schema, citations, relations, timeline; 0 violations`. Reversing order (`tower` then `harbor`) produced the same exit 0 and same CLEAN output. Thus the first value is discarded and these specific valid values do not alter the current effective decoded record; the experiment does **not** demonstrate different occupancy decisions or clean-versus-violation behavior.

A malformed-type pair demonstrates order-dependent masking: `"place_id": "harbor", "place_id": 7` exited 1 with `timeline[0].place_id: required nonempty str` plus an unrelated downstream `timeline[1].depends_on: unknown event 'departure'`; reversed (`7` then `"harbor"`) exited 0 CLEAN. This shows last-value-wins can hide a malformed earlier value, but does not establish that both values are intended assertions or that treating either as authoritative is correct.

## Assessment

**Material CALIBRATION: NO-GO on current evidence.** There is a real parser behavior and an actual order-dependent malformed-type probe, but no observed valid-value semantic divergence in the controlled swapped pair, and the proposed universal hard rejection is not established by the schema/README or r5 cases. JSON permits consumers to choose policies for duplicate names; the checker currently uses Python's documented decoder behavior. Rejecting every repeated name could improve input transparency, but without demonstrated reader consequence and regression/cascade analysis it could also impose a new format rule and expand errors across nested objects.

A narrow future probe should include duplicates in nested `claims`, `claim_a`/`claim_b`, and unknown keys, plus valid unique-key controls and pinned raw outputs. If a policy is considered, report one file-level parse diagnostic and suppress downstream findings from that undecoded file rather than arbitrarily validating one member; assess whether that cascade behavior is itself compatible with current contracts. Do not conflate duplicate object members with duplicate row IDs.

**Falsifier / reversal condition:** independently reproduce an actionable reader error on a schema-valid input containing duplicate members (or establish an explicit existing format contract that forbids them), show that last-wins makes the CLI materially misleading relative to that contract, and demonstrate a bounded deterministic diagnostic with no material harm to unique-key controls or the 95 existing raw CLI tuples. No inference here concerns fictional-world truth, canon, chronology, source support, or rights.
