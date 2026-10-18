# Round 33 simplifier — minimum fixture-only depth proposal

## Baseline and precedent

- Round 33 targets a source-cited observation by a newly named character of Sella placing an unlabeled envelope on the registry desk; it explicitly excludes envelope contents and causal inference (`.shokunin/lore/LOG.md:513-515`). The `r33-` fixture inventory is empty at baseline (`.shokunin/lore/LOG.md:514`).
- Round 10’s smallest coherent precedent used a separate fixture, one new witness/source, cited relation and event, plus an invented excerpt; it preserved `consistent/` and required exact clause mapping (`.shokunin/lore/LOG.md:135-141,147-149`; `.shokunin/lore/reports/r10-simplifier.md`). Its excerpt remains a separate file because the source schema has no excerpt field (`.shokunin/lore/corpus/fixtures/r10-registry-witness/registrar-copy-excerpt.md`).
- Round 23’s witnessed-absence addition shows that a separate fixture can inherit baseline rows and add only a source, one event and one short excerpt/map; it cautions that the checker does not read prose maps (`.shokunin/lore/reports/r23-simplifier.md`; `.shokunin/lore/corpus/fixtures/r23-note-class/witnessed-absence-clause-map.md`). For r33, reuse the r10-style separate fixture pattern, not r23’s absence semantics.
- The clean baseline has four entities and two events; `harbor` is the Lantern Harbor place and Mira already departs there at tick 1 (`.shokunin/lore/corpus/fixtures/consistent/entities.json:1-50`; `.shokunin/lore/corpus/fixtures/consistent/timeline.json:1-23`). The checker requires event actor/place/source references and a nonnegative tick; dependencies, if any, must target an earlier event (`.shokunin/lore/corpus/fixtures/check_bible.py`, timeline validation). It checks structure and IDs, not excerpt entailment (`.shokunin/lore/LOG.md:514-515`; `.shokunin/lore/corpus/fixtures/README.md`).

## Minimum artifact recommendation (not implementation)

Use one new directory, `.shokunin/lore/corpus/fixtures/r33-envelope-observation/`, copied from `consistent/`. Keep all inherited JSON rows byte-identical. Add only:

1. One `sources.json` row with a unique fictional source ID such as `tarin-harbor-note`, explicitly labeled as newly authored in-world fiction (not recovered evidence).
2. One character entity, Tarin, with `first_appearance` set to that source ID and only the minimal cited character-name/identity claim needed by schema.
3. One timeline event, e.g. `tarin-sees-envelope`, with `entity_id: tarin`, `place_id: harbor`, a tick after the existing local sequence (3 is sufficient), no dependency, and the new source citation. Its description should say only that Tarin reports seeing Sella place an unlabeled paper envelope on the registry desk.
4. One short, clearly labeled authored excerpt file with the same single observation in first person. Include a manual clause map only if needed for non-author review; do not present the map as checker-validated.

Do not add a relation: the single event already records the relevant actor, place, action and source; a relation would add no necessary observation. Do not add a Sella entity or second event, since Sella is already named in the target sentence and the assertion concerns Tarin’s report. Avoid “later,” exact clock time, sequence dependency, contents, ownership, recipient, destination, Blue Seal, motive, or causal wording. Tick 3 is only a local fixture ordering choice, not a claim about when the observation occurred.

## Risks and falsifiable check

**Risks:** the checker’s clean exit only establishes schema/reference consistency, not that Tarin’s excerpt entails the row, that Tarin is truthful, or that the event is canon. “Registry desk” must be clearly the registry at `harbor`, without asserting more than the excerpt. A generic row-count increase is not depth; depth depends on a human-traceable new observation class. Do not infer envelope contents, ownership, destination, or any Blue Seal connection; no real-world rights or source provenance claims follow from the fictional citation.

**Falsifiable check:** require the new fixture to exit 0; a non-author must map each of the event’s actor, Lantern Harbor/registry location and placement-action clauses to exact excerpt wording and reject any unsupported addition. Compare all 84 pre-existing fixture CLI stdout/stderr/exit results and all 419 existing JSON paths byte-for-byte to the declared baseline; any drift falsifies the no-collateral-change claim. If the clause map cannot trace the complete bounded observation, or review finds any forbidden implication, do not count depth improvement. This report proposes only; it does not run the checker or establish a verdict.

Scope: report-only recommendation. No fixture, checker, README, LOG, or commit changes.
