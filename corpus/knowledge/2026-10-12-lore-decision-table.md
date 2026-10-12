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

## Round 2 — faction alliance convention

The rows below describe a **local, invented-world data convention**, not a universal claim about political alliances. The corresponding `ally-*` fixtures cite the invented `harbor-compact` in `sources.json`; they do not draw on a real-world source.

| Input condition | Decision / output | Fixture evidence |
|---|---|---|
| Exact `allied_with` relation links two distinct factions, and a separately cited reverse `allied_with` row exists with a resolvable in-world source ID | This rule passes; each row remains independently cited | `fixtures/ally-reciprocal/{entities,relations,sources}.json` |
| Same forward row, no qualified reverse row | Report missing reciprocal at the forward relation location; never create or select canon | `fixtures/ally-one-way/{entities,relations,sources}.json` |
| Reverse row is present but its `source_id` does not resolve | Report its citation error and missing *qualified* reciprocal for the forward row | `fixtures/check_bible.py` relation and citation passes; independent verifier probe required |
| Endpoint missing, either endpoint not a faction, self-edge, or relation type not exactly `allied_with` | Outside this reciprocal-pair rule; existing dangling-endpoint/citation checks remain applicable | `fixtures/contradictions/relations.json` and `fixtures/consistent/relations.json` guard unrelated directed relations |

The checker does not establish treaty authenticity, source agreement, faction ontology beyond `kind`, or semantic truth. A reciprocal record is a sourced assertion, not an editorial resolution.

## Round 3 — editorial contradiction ledger

| Input condition | Decision / output | Evidence and limit |
|---|---|---|
| Two distinct `claim_a` / `claim_b` event-field pointers resolve to uniquely identified timeline events with valid source IDs, and `why` is nonempty | Accept ledger record structurally, preserve both source-cited events; continue ordinary checks | `fixtures/contradictions/{timeline,contradictions,sources}.json`. The reason is unchecked editorial text, not proof of conflict or truth. |
| A pointer's event/field is missing, ambiguous, or uncited, or `why` is absent | Report a ledger-local violation; never alter either assertion | `fixtures/contradictions-ledger-malformed/contradictions.json` has `absent-event`. |
| `contradictions.json` is absent or invalid JSON | Report load/schema violation like other required tables | Empty `[]` is explicit in fixtures without a pair; absence does not prove none exist. |
| One structural error has only one cited side | Keep its ordinary diagnostic outside the two-sided ledger | `fixtures/contradictions/relations.json` references absent `missing-map`; there is no second claim to cite. |

The ledger is not exhaustive, does not infer conflicts from arbitrary prose, and does not adjudicate source reliability or select canon. Its citations are the existing fictional event `source_id` values; no real-world method citation establishes an in-world claim.

## Round 4 — rejected exact-name experiment

An exact-name review detector was tried and independently replayed, then
rejected because it gave legitimate homonyms a `VIOLATION` and exit 1. The
active checker has **no** name-collision rule. Experimental checker, fixtures,
and output are retained in `corpus/live/rejected-r4/` and
`corpus/live/runs/20261012T163450Z/`; `reports/r4-axis-adjudicator.md` states
coverage improved narrowly but calibration harmed. An equal string is not
evidence of shared identity, invalid canon, or in-world attestation.

## Round 6 — explicit item chain, not inferred possession

| Input condition | Decision / output | Fixture evidence and boundary |
|---|---|---|
| No `provenance` field on an item | No chain asserted; preserve existing checks | `fixtures/consistent/entities.json` cites the seal but asserts no ordered acquisition/transfer. |
| First cited record is acquisition with null `from_holder`, followed by strictly later cited transfers whose `from_holder` equals preceding `to_holder` | Structurally continuous chain; do not infer semantic truth | `fixtures/item-chain-valid/entities.json`; `sources.json` resolves the fictional source IDs. |
| Last transfer names a different predecessor from the prior record's `to_holder` | Report local chain break; retain both assertions and do not choose a source | `fixtures/item-chain-broken/entities.json` changes last `from_holder` from `harbor` to `mira`. |
| Same-item ticks are equal/reversed, holder ID ambiguous, or present provenance malformed | Report input/order issue; do not silently construct a chain | Checker shape checks; independent negative probes needed before claiming specific error coverage. |

Ticks in this optional field are local ordering labels and are not cross-validated against `timeline.json`; `carries` and prose are not transfer evidence. Neither a valid chain nor an in-world source ID establishes that the cited record supports the transfer or proves canon. Holder IDs are entity references, not a legal ownership assertion.

## Round 7 — source-ID uniqueness before qualification

| Input condition | Decision / output | Fixture evidence and limit |
|---|---|---|
| Referenced `source_id` appears once in `sources.json` | Qualify by unambiguous ID only | `fixtures/ally-reciprocal/` and `fixtures/item-chain-valid/` are clean; no source-text support inferred. |
| ID absent | Preserve `unknown in-world source` at reference | `fixtures/r5-invalid-citation/relations.json`. |
| ID appears at least twice | Retain global duplicate-ID finding and report `ambiguous in-world source` at each affected reference; preserve both records | `fixtures/r7-item-ambiguous/` has repeated `archive-ledger`; old last-wins dictionary no longer qualifies it as a unique citation. |
| Reverse alliance edge cites ambiguous ID, forward edge unique | Reverse is not qualified; report missing qualified reciprocal at forward relation in addition to ambiguity | `fixtures/r7-ally-reverse-ambiguous/`; a distinct uniquely cited reverse edge could still satisfy reciprocity. |
| Provenance record source ambiguous | Report local ambiguity; structural holder/tick findings, if present, concern input consistency rather than sourced canon | `fixtures/r7-item-ambiguous/` retains an otherwise continuous chain. |

This rule never ranks, merges, or deletes sources. A unique ID is necessary for a qualified reference in this checker, but it is not evidence that the fictional document says the asserted thing, is reliable, or tells the truth. Local per-reference reports are deliberately plural when one duplicated ID is reused.

## Round 8 — timeline prerequisite-list integrity

| Input condition | Decision / output | Fixture evidence and boundary |
|---|---|---|
| One valid earlier prerequisite ID once in `depends_on` | No list-integrity finding; existing strict-tick check applies | `fixtures/r8-deps-distinct/timeline.json` cites fictional `courier-log`. |
| Same prerequisite ID repeated within one event list | Report repeated occurrence at that list index; do not remove it; check target/tick once per distinct ID | `fixtures/r8-deps-anomalous/timeline.json` repeats earlier `departure`. This is a local input convention, not proof of a canon contradiction. |
| Event ID appears in its own prerequisite list | Report explicit self-dependency and preserve existing same-tick inversion finding | Same anomalous fixture lists `arrival` as its own prerequisite; baseline already reported inversion on that ID. |
| List has non-string member or unresolved ID | Preserve existing type/unknown-ID diagnostic; no fabricated event | Original checker list guard and ID lookup; not a new semantic rule. |

No source text is inspected to show a dependency is actually attested. This check does not traverse a causal graph or resolve ambiguous duplicated event IDs, and it never repairs lore.
