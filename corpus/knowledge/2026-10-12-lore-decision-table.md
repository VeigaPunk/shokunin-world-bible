# Lore consistency decisions — round 1

This is a decision table for **fictional** records, not a claim that the
underlying in-world source tells the truth. `fixtures/check_bible.py` implements
the indicated checks; fixture citations are the IDs in `fixtures/consistent/sources.json`.

| Input condition | Decision / output | Fixture evidence and governing source |
|---|---|---|
| Claim, relation, or event has no resolvable in-world `source_id` | Report schema/citation violation; do not assert canon | `fixtures/consistent/entities.json` claims cite `courier-log` or `archive-ledger`; W3C PROV-O, https://www.w3.org/TR/prov-o/ §2, provides a general model for attributing entities to agents/activities. Our required ID is a local editorial rule, not a PROV-O mandate. |
| Relation endpoint absent from the entity index | Report dangling endpoint; do not invent the missing entity | `fixtures/contradictions/relations.json` (`missing-map`); JSON Schema Validation, https://json-schema.org/draft/2020-12/json-schema-validation §6.5, defines object constraints (`required`/`properties`); cross-record referential integrity is our application-specific rule, not a built-in JSON Schema guarantee. |
| One entity recorded at one tick in different places | Report both locations and source records; do not pick a winner | `fixtures/contradictions/timeline.json` `arrival` (`courier-log`) versus `false-sighting` (`archive-ledger`); local invented-world exclusivity assumption in `fixtures/README.md`. |
| A stated prerequisite has a tick equal to or later than its dependent event | Report inversion and both ticks; do not reorder canon | `fixtures/contradictions/timeline.json` `arrival` depends on `later`; local strict-order convention in `fixtures/README.md`; Python `graphlib.TopologicalSorter`, https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter, illustrates predecessor ordering and cycle detection, but this checker compares ticks directly. |
| Distinct real-world inspiration appears | Record attribution, rights, and AI-training permission independently; never infer one from another | `reference-ledger.md` describes the three unanswered questions; real-world permission is outside this province. |

## Scope and negative claims

The checker does not yet check aliases, free-text semantic contradictions,
source reliability, or competing in-world dating systems. Its graph edge
direction is `depends_on` (prerequisite → event), and strict tick ordering
prevents a cycle among events with valid integer ticks. The seed checklist is
a proposal, not a claim that these other checks ran. A future round may add
explicit contradiction records with `claim_a` / `claim_b` / `why`; none is
silently resolved in round 1.
