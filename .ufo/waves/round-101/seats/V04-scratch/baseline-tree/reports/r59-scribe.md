# Round 59 scribe — duplicate JSON object members

## Evidence and scope

- The round-59 declaration (`.shokunin/lore/LOG.md:1008–1010`) distinguishes duplicate JSON member names inside one object from repeated row IDs. It asks whether Python's last-wins decoding creates material uncertainty, not whether fictional records are true.
- Active loader calls `json.loads(path.read_text(...))` and then checks decoded row fields (`.shokunin/lore/corpus/fixtures/check_bible.py:18–43`). The `FIELDS` table requires typed `place_id` and other fields (`check_bible.py:8–15`); after ordinary decoding the checker has no indication that a name appeared twice. `index()` separately reports repeated record IDs (`check_bible.py:45–51`), which does not catch duplicate object members.
- Decision-table precedent treats duplicate *row IDs* as ambiguous when a consumer would otherwise select a last row, retaining the raw records and withholding the choice: ambiguous dependency target (`2026-10-12-lore-decision-table.md:93–102`), place entity ID (`:114–123`), and actor identity (`:125–143`). These are analogous caution, not proof that duplicate JSON names have a previously established policy. No JSON format/schema rule in the inspected decision table resolves duplicate names.
- Round-5 malformed observations concern absent file, syntactically invalid JSON, wrong top-level value, non-object row and invalid citation (`2026-10-12-malformed-error-patterns.md:11–20`). In particular invalid JSON is currently reported as `cannot load JSON` (`:14–15`), while row shape is detected after parsing (`:16–17`). Repeated object names are syntactically accepted by the current Python decoder, so r5 does not test or settle them. Keep exact parser wording/offset portability limits from `:20` in mind.

## Actual behavior (temporary raw probes; no repository inputs changed)

Using copies of `fixtures/consistent/` outside the repository and the active checker:

1. Unique-key control exits 0 (`CLEAN`).
2. A duplicate `timeline[1].place_id` with values `harbor` then `tower` decodes as `tower`; reversing raw order decodes as `harbor`. With original tick 2 both happen to exit `CLEAN`, so this control alone would be a weak demonstration.
3. With only the temporary arrival tick changed to 1 and `depends_on` emptied to isolate occupancy, `harbor` then `tower` yields `double-booked` against departure, whereas `tower` then `harbor` yields `CLEAN`. Thus a duplicate member can change the checker conclusion solely by order: last value wins. This is an input-structure finding, not evidence about actual place, chronology, canon, or source support.

The checker emits no duplicate-member diagnostic today. Its ordinary malformed-JSON behavior is the generic per-file `cannot load JSON` from the `json.JSONDecodeError` handler (`check_bible.py:23–30`); duplicate names do not raise that exception. Row validation then sees just one value (`:37–43`).

## Proposed raw-input behavior

Treat any repeated object member name as an ambiguous input condition and refuse to use a silently selected value. Preferred narrow form: use `json.loads(..., object_pairs_hook=...)` to detect duplicate names in every JSON object, report a deterministic file-local duplicate-member diagnostic, and avoid downstream semantic checks on values/rows whose object has duplicate members. Preserve other independently parseable rows where feasible; never arbitrarily keep first/last as authoritative. A generic file-local diagnostic is safer than claiming precise `timeline[i]` locations unless the parser hook can provide that context without relying on object/key ordering assumptions.

The hook naturally sees nested objects too (including `claims`, `claim_a`, and source/entity rows); if adopted, document this as parser-level behavior across all tables and nested objects, not merely `place_id`. Do not reject unique keys or alter duplicate row-ID policy. If the implementation cannot avoid downstream cascades based on one arbitrarily chosen value, suppress those cascades for affected objects rather than treating a duplicate as valid data. Preserve the existing invalid-JSON class for genuinely malformed syntax. A duplicate where one value has the wrong type should still be diagnosed as duplicate-member ambiguity; validation of a chosen last value must not mask that ambiguity.

## Calibration verdict

**MATERIAL CALIBRATION GO.** The temporary same-tick occupancy pair demonstrates an order-only switch from `double-booked` to `CLEAN` under current last-wins parsing. Rejecting/flagging duplicate members would accurately expose unresolved input ambiguity and avoid an unjustified definite checker decision. This is not a new lore rule, canon inference, or rights inference.

**Falsifier:** after an implementation, a non-author must replay a raw duplicate pair with swapped values and show both report duplicate-member ambiguity, neither produces a definite occupancy conclusion derived from either value, while the unique-key control retains byte-identical output. The same replay must show a duplicate with a wrong-typed counterpart is not masked; nested objects are either consistently covered or explicitly bounded. If paired order still changes a semantic conclusion, or unique-key/r5 behavior changes unexpectedly, the calibration claim is falsified / NO-GO for admission.

### Risks / boundaries

- Generic rejection may suppress valid independent findings elsewhere in the file; per-object isolation versus file rejection is a deliberate implementation tradeoff to measure, not assume harmless.
- A global pairs hook flags duplicate names in nested objects too; that is broader than top-level row-field examples and must be stated. Error messages should be stable without asserting exact JSON parser offsets.
- Do not conflate duplicate member names with duplicate row IDs: they are different raw structures and require distinct diagnostics.
- No semantic interpretation of the competing values, actual story truth, canon, citations' textual support, chronology, or rights is established.
