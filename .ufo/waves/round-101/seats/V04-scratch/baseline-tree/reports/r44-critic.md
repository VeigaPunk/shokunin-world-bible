# Round 44 critic — universal character-actor rule

## Finding: ontology premise fails; no-go on unconditional kind gate

The timeline schema does not encode an actor as a character: checker `FIELDS` declares `timeline.entity_id: str` (`.shokunin/lore/corpus/fixtures/check_bible.py:12-13`). Its timeline loop resolves `entity_id` multiplicity and labels ambiguity, but never checks the resolved entity kind (`check_bible.py:230-237`); by contrast, it explicitly checks `place_id` kind (`:237-245`). The README's sentence “A character cannot occupy different places at the same tick” states the occupancy convention, not that every event's subject must be a character (`.shokunin/lore/corpus/fixtures/README.md:17-19`). Thus a generic entity subject is an explicit schema capability, and no universal character-only convention is established.

A plausible noncharacter event is an event with an **item** as subject: “The Blue Seal was displayed at the registry desk at tick 3” or “the bell rang at Lantern Harbor.” The former naturally has an item entity ID as subject; the latter could use an item/bell entity. This is not merely theoretical: `KINDS` explicitly includes `item` (`check_bible.py:7`), entity records may be items (`:8-10`), and the README describes item provenance and holder references as entity IDs without converting all entities into characters (`README.md: item-chain section`, especially holder IDs paragraph). A hard `entity_id.kind == character` diagnostic would reject such coherent event modeling despite the generic `entity_id` contract.

## Precedent boundaries

- R11 tests non-place **place_id** values and ambiguous place IDs, not actor kind; see `reports/r11-critic.md` “Raw probes” and `corpus/fixtures/README.md` Round 11. Its recommendation is explicitly local to `place_id`.
- R12 tests unique versus duplicate `mira` actor IDs for occupancy, and cautions that duplicate rows do not establish actor semantics (`reports/r12-critic.md`, “Critique / falsification”). It does not establish character-only actor semantics.
- R21 gates occupancy on uniquely resolved actor, known place, and valid tick while independently handling malformed dependencies; its fixture README states those guards, with no actor-kind rule (`README.md`, Round 21). `reports/r21-critic.md` supports independence of dependency validity, not an ontology restriction.

## Calibration harm and risk

Unconditional enforcement would turn valid item-subject or other noncharacter-subject events into violations and force authors to misrepresent an event by assigning a character as `entity_id`. It would also conflate “can occupy different places” with “can be an event subject.” A narrowly worded event such as an item being moved/recorded can be modeled directly, while the existing character occupancy rule need not apply to it. The checker currently checks occupancy for any uniquely resolved actor ID (`check_bible.py:245-252`), which itself may deserve separate design, but it does not justify asserting a universal character requirement. Avoid adding a kind error or changing occupancy semantics absent an explicit event taxonomy/schema convention.

## Falsifiable decision

**NO-GO** for the proposed universal actor-kind rule and any fixture/checker implementation based only on a place-ID swap. Go only if repository-level schema/docs or an agreed domain contract explicitly states that every timeline subject must be a character, and a counterexample showing item/noncharacter subjects are invalid is documented. Falsifier: identify that explicit convention and demonstrate a well-formed, source-cited character event is the only permitted timeline event class; absent that evidence, retain generic entity IDs and existing behavior. A future narrower rule would need a declared event-class distinction and paired character/item-subject cases, not an unconditional kind check. No checker, fixture, README, or LOG was changed.
