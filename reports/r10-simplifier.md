# Round 10 simplifier — least coherent cited depth extension

Scope: read-only inspection of the round-10 declaration, clean fixture, checker, and fixture guidance. This report proposes a minimal assertion set; it does not add or validate fixture content.

## Observations (with paths)

- The declared target is an archivist/registry witness to Mira’s departure, with each new entity claim, relation, and event uniquely cited and supported by an invented, inspectable excerpt: `.shokunin/lore/LOG.md` (Round 10 declaration).
- The baseline is four entities (`mira`, `harbor`, `tower`, `seal`), one `carries` relation, and `departure` at tick 1 plus `arrival` at tick 2: `.shokunin/lore/corpus/fixtures/consistent/{entities,relations,timeline}.json`.
- Existing `archive-ledger` source has a reliability note but no excerpt text; `courier-log` likewise has no excerpt: `.shokunin/lore/corpus/fixtures/consistent/sources.json`. The fixture guidance distinguishes in-world fictional citations from any real-world reference ledger and says the checker validates citation IDs, not truth or textual support: `.shokunin/lore/corpus/fixtures/README.md`.
- Checker-required entity fields include a kind, name, first-appearance source, and claims; each relation has `from`, `to`, `type`, and source; each timeline event has an ID, nonnegative integer tick, entity/place IDs, dependencies, description, and source: `.shokunin/lore/corpus/fixtures/check_bible.py` (`FIELDS`, entity/relation/timeline checks).
- Timeline dependencies require a unique earlier event; entity/place IDs must resolve, and place IDs must designate places. Multiple entities can have events at the same tick; the occupancy check only rejects one entity assigned to different places at one tick: same checker, timeline loop.

## Least new assertion set (recommendation, not observation)

Add one fictional registrar, one sourced witness relation, and one co-timed witness event. Use a **new, unique in-world source ID** for an authored registry excerpt, and make the excerpt explicit in the new fixture’s source material (the current source schema has no excerpt field, so do not imply that a source title alone is evidence).

1. **Entity:** `nera`, a character/registrar at Lantern Harbor; a single claim can state that she is the registry clerk who records departures. Give `first_appearance` and that claim the new source ID.
2. **Relation:** `nera` `witnesses_departure_of` `mira`, cited to the same source. This makes the relationship between the new character and the existing protagonist explicit; the relation type is a narrative assertion, not a checker-verified semantic rule.
3. **Timeline event:** a uniquely named event for `nera` at `harbor`, tick 1, with no dependency, cited to that source. Describe the concrete act/details the excerpt supports—for example, Nera records Mira’s departure but leaves the destination blank at Mira’s request. This is a second perspective synchronized with existing `departure` (tick 1), not a second claim that Mira departed at another time or place.
4. **Source excerpt:** the new source record’s accompanying fictional excerpt should directly state Nera’s role, that she witnessed/recorded Mira’s departure, and the destination omission/request if that detail is retained. Keep those clauses visibly mappable to the entity claim, relation, and event description. Mark the source as invented/in-world and avoid presenting it as independent real-world evidence.

This adds three lore assertions beyond the source entry (one entity claim, one relation, one event), while connecting the new witness to the existing departure instead of adding unrelated rows. If the destination-blank detail is not useful to the narrative, omit it from both excerpt and event description; don’t retain it as unsupported color. No extra location, item, faction, conflict ledger row, or event dependency is needed for this beat.

## Boundaries / recommendations

- Preserve the original `consistent` fixture; use a separate micro-bible as the round declaration requires.
- The checker's clean result can establish schema, resolvable citations, and structural consistency only. Manual comparison of excerpt clauses to claims is necessary to assess source-to-claim fit; neither a clean run nor unique source IDs prove the fictional account true.
- The declaration’s depth claim is earned only if the source makes the two perspectives narratively meaningful and supports every added clause. Mere additional entity/relation/event rows would be row-count growth, not demonstrated depth.
