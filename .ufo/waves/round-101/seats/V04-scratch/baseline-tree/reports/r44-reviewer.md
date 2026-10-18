# Round 44 independent reviewer — timeline entity kind

## Decision

**NO-GO** on the proposed unconditional `timeline.entity_id: not a character` diagnostic and coverage candidate. The field is normatively generic in the checker’s declared contract, not normatively character-only. The probe is evidence of present checker acceptance, not evidence that the input is invalid. No r44 candidate fixture or code change is warranted.

## Evidence

- `.shokunin/lore/corpus/fixtures/check_bible.py:7-13` admits four entity kinds (`character`, `place`, `faction`, `item`) and declares timeline `entity_id` as `str`, without a character constraint. This is the explicit structural contract in the checker.
- `.shokunin/lore/corpus/fixtures/check_bible.py:228-252` resolves actor references and ambiguity, explicitly checks `place_id` for kind `place` (237-241), but does not inspect the unique actor’s kind. Occupancy uses the resolved ID/tick and a valid place (245-252). Thus actor-kind omission is real, but does not by itself establish a defect.
- `.shokunin/lore/corpus/fixtures/README.md:29-34` says “A character cannot occupy different places at the same tick.” This is an occupancy rule about characters; it does not say every event subject must be a character. The specific r12 text at `README.md:243-265` likewise covers unique/ambiguous actor identity and occupancy, not actor kind.
- The r11 precedent is explicitly bounded: `README.md:235-241` validates `place_id` kind and says it does not change actor identity or occupancy rules. It is not a non-character `entity_id` test. R12 (`README.md:243-265`) tests duplicate-ID ambiguity with `mira`; r21 (`README.md:443-468`) concerns malformed dependencies and independent occupancy guards, not actor kind. None establishes character-only ontology.
- LOG’s r44 declaration itself labels the hypothesis as unestablished and notes plausible non-character subjects (`.shokunin/lore/LOG.md:737-741`). That is consistent with the schema and avoids treating fixture convention as a normative restriction.

The temporary `/tmp` `harbor` substitution reportedly changes only the first event actor from `mira` to the uniquely identified place `harbor`, retains `place_id=harbor`, and returns CLEAN alongside the control. This is a useful observed acceptance probe. It is not a committed fixture, a semantic oracle, or proof of invalid input: it shows what the current structural checker accepts. It does not establish that a place actually acts in any fictional source or that the project prohibits such subjects.

## Calibration and coverage

A blanket character-only diagnostic could harm calibration by rejecting legitimate place-, faction-, or item-subject events that the generic schema currently permits. No cited source or precedent rules those out. The README’s character occupancy assertion cannot safely be inverted into “only characters may be timeline actors.” The guard would therefore encode a new ontology decision rather than close a demonstrated false-negative. Coverage gain is unproven; calibration risk is material. Do not claim the candidate improves coverage.

## Falsifier / uncertainty

This conclusion would change if an authoritative schema or documented project convention explicitly stated that all timeline `entity_id` values—or a clearly typed event subset—must identify characters. No such event-class discriminator or universal rule appears in the inspected contract. A future scoped proposal should cite that rule, distinguish occupancy events from other event subjects, and test paired controls; absent it, preserve generic actor IDs. Conversely, one supported non-character-subject event under the present contract would directly falsify an unconditional guard.

**Verdict: NO-GO.** No code or fixture change recommended.
