# Round 29 negative scout — proximity without carrying

## Proposed proximity sentence

Use the matched near-miss sentence: “The blue seal was near Mira.” It states spatial proximity only; it has no carrying predicate and does not entail the directed relation `mira -> seal / carries`.

## Evidence and scope

- The positive control's authored sentence is `.shokunin/lore/corpus/fixtures/r28-courier-excerpt/courier-log-excerpt.md:3`: “I, Mira, carried the blue seal.” Its map explicitly grounds `carries` in the word “carried” (`.shokunin/lore/corpus/fixtures/r28-courier-excerpt/relation-clause-map.md:9`).
- The corresponding structured row is `.shokunin/lore/corpus/fixtures/r28-courier-excerpt/relations.json:2-6`; it records `from=mira`, `to=seal`, `type=carries`, `source_id=courier-log`. The map says its ID matches are editorial alignment, not lexical entailment (`.shokunin/lore/corpus/fixtures/r28-courier-excerpt/relation-clause-map.md:7`).
- The negative sentence is the near-miss named in the prior map (`.shokunin/lore/corpus/fixtures/r28-courier-excerpt/relation-clause-map.md:13`) and in the round-28 plan (`.shokunin/lore/LOG.md:444`); it is a proposed test sentence, not existing source evidence.

## Risk and falsifiable test

Risk: a reader may mistake proximity for custody or treat the structurally valid `carries` row as prose-supported. Conversely, calling the relation false would exceed the evidence: this sentence does not say whether Mira carried the seal at some other time. “Unsupported by this clause” is not “false in canon.”

Falsifiable test: pair the r28 excerpt/map unchanged with a matched negative excerpt containing only “The blue seal was near Mira.” Have a non-author reviewer quote each exact sentence and label r28's `carries` row supported by its explicit “carried” predicate, but the negative's corresponding row **unsupported by the clause**, not contradicted/false. Both fixture check runs may remain structurally valid; checker success is not entailment evidence. The calibration claim fails if the reviewer accepts proximity as carrying, calls the negative canonically false, or cannot distinguish the positive predicate from its absence. No checker, fixture, LOG, or README changes are proposed here; no canon or authenticity claim is made.
