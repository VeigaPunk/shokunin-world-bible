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

## Round 9 — ambiguous dependency target identity

| Referenced timeline event ID (schema-valid rows) | Diagnostic / decision | Example and limit |
|---|---|---|
| Zero matching records | Keep existing unknown-event finding. | No event can be chosen. |
| Exactly one matching record | Keep strict-earlier tick comparison. | `fixtures/r9-unique-control/` has one earlier `same`; no dependency finding. |
| More than one matching record | Report `ambiguous dependency event` at first referenced dependency-list index; skip target tick comparison. Retain duplicate timeline-ID finding and both records. | `fixtures/r9-dup-{low-high,high-low}/` swap only the two `same` rows. A last-row inversion or apparent valid order is not justified. |
| Repeated dependency token, regardless of target identity | Retain round-8 list-indexed repeat finding and one lookup per distinct token. | Input list integrity is independent of duplicate event records. |

Counts concern schema-valid timeline rows; no textual source support, causal inference, or canon selection follows from a matching ID.

## Round 10 — authored registry account, manual claim correspondence

| New assertion in `fixtures/r10-registry-witness/` | Exact invented `registrar-copy-excerpt.md` clause | Limit |
|---|---|---|
| `sella` named character, claimed registrar at Lantern Harbor | “I, Sella, registrar there” after “at Lantern Harbor” | Attributed fictional self-description, not independent identity proof. |
| `sella` `records_departure` of `mira` | “recorded seeing Mira leave” | The record claims Sella saw and recorded this; it does not independently prove the departure. |
| `registry-entry` at harbor assigned the same local tick as `departure`, destination omitted at Mira's request and carbon kept | “At first bell at Lantern Harbor”; “At Mira’s request, I left the registry destination blank and kept the carbon.” | Tick 1 is an authoring convention, not independent proof of simultaneity or a clock conversion; blank destination is no conflicting destination assertion. |

The checker does not parse the excerpt or certify that source text entails the JSON. `courier-log` and `archive-ledger` baseline assertions remain unchanged and have no excerpt in this fixture; do not claim textual support for them. This is an authored second perspective, not external corroboration or canon resolution.

## Round 11 — timeline place entity identity

| `place_id` count among schema-valid entity rows | Field-local decision | Control and boundary |
|---|---|---|
| Zero | Existing dangling entity finding. | `fixtures/r11-dangling-place/`: `unlisted`; no invented entity. |
| One, kind `place` | Accepted by kind check. | `fixtures/consistent/`: unique `harbor`, clean. |
| One, other kind | Existing `not a place`. | `fixtures/r11-unique-nonplace/`: unique `mira` character. |
| More than one | Ambiguous place entity; skip last-wins kind classification and retain duplicate-ID finding. | `fixtures/r11-{place-character,character-place}/` differ only in duplicate `harbor` row order; both cite existing fictional `archive-ledger` but source identity does not settle entity identity. |

This is an input-key ambiguity for timeline places, not a duplicate-name rule or a global entity-resolution policy. It says nothing about canon truth, occupancy semantics, or source-text entailment.

## Round 12 — occupancy depends on actor identity

| Actor ID count among schema-valid entity rows | Decision for two same-tick different-place events | Interpretation |
|---|---|---|
| Exactly one | Retain `double-booked` same-actor diagnostic. | `fixtures/r12-unique-actor/` supports the local input convention, not source truth. |
| More than one | Report `ambiguous actor entity` at each affected event's actor field; do not assert definite same-actor double-booking. Preserve duplicate entity ID and raw events. | `fixtures/r12-ambiguous-actor/` does not prove whether duplicate rows describe one or two actors; conflict remains indeterminate. |
| Zero | Retain prior dangling-entity diagnostic **and** prior occupancy behavior for this round. | Existing dangling ID can still produce a misleading double-booked message; excluded from this single move and recorded as a limit. |

A malformed duplicate entity row is excluded from the schema-valid count. This does not decide canon identity or use cited source metadata to infer witness truth.

## Round 13 — occupancy with an absent actor key

| Matching required-field-screened entity rows for `timeline.entity_id` | Report and occupancy behavior | Limit |
|---|---|---|
| Zero | Keep dangling actor finding at each affected event; do not compare/update occupancy for that ID. | `fixtures/r13-missing-actor/` has `unlisted` in two tick-7 records; possible same-actor conflict remains unassessed. |
| One | Retain strict same-tick/different-place double-booking. | `fixtures/r13-unique-actor/` uses `mira` with identical event structure. |
| More than one | Retain round-12 per-event ambiguous actor findings and skip occupancy. | `fixtures/r12-ambiguous-actor/` does not resolve whether duplicate rows mean one or two actors. |

Malformed rows missing required fields do not count; a nonempty but unrecognized `kind` string does count and gets a separate unknown-kind finding. This is structural identity handling, not evidence that either cited event occurred or that a possible conflict is absent.

## Round 15 — bounded follow-up account and source limits

| New `r15-carbon-followup/` assertion | Exact `sella-carbon-followup-excerpt.md` clause | Limit |
|---|---|---|
| Sella's later look at retained carbon at harbor | “Later, at Lantern Harbor, I looked again at the carbon I had kept.” | Relative later report only; tick 3/dependency is a fixture ordering choice, not clock conversion or independent custody proof. |
| Report of blurred blue oval mark on carbon | “I saw a blurred blue oval mark on it.” | Sella's authored observation, not verified objective provenance or a claim it came from the Blue Seal. |
| Origin unidentified to Sella | “I cannot identify where the mark came from” | Does not prove origin is unknowable to everyone. |
| No attribution to Mira's Blue Seal | “I do not attribute it to Mira’s Blue Seal.” | This does not prove the seal did or did not cause the mark. |

No new entity claim/relation was added. The original `registrar-copy` and all inherited JSON rows remain unchanged; its “first bell” has no proven numeric tick conversion. Checker does not read excerpts. These newly authored in-world sentences are internally inspectable fiction, not recovered evidence or independent corroboration.

## Round 16 — missing place and definite occupancy

| Same uniquely screened actor/tick place references | Output policy | Limit |
|---|---|---|
| Two unique resolved places, distinct IDs | Retain `double-booked`. | `fixtures/r16-valid-places/`: `harbor` and `tower`. |
| One or both place IDs absent (count zero) | Keep each dangling-place finding; do not compare/store missing-place event in occupancy. | `fixtures/r16-{missing-place,missing-first}/`; no conclusion that the event is at either known place or conflict-free. |
| Known place, absent place, distinct known place | Keep dangling for middle row and definite booking for the known pair. | `fixtures/r16-mixed-three/`; unresolved row cannot hide supported conflict. |

Duplicate IDs and uniquely identified non-place rows retain old separate diagnostics and old raw-ID occupancy behavior in this round; do **not** generalize this missing-place guard to those cases without a new experiment. Source IDs resolve citations, not locations or canon.

## Round 17 — unique non-place entity as timeline place

| Same uniquely screened actor/tick place inputs | Definite occupancy decision | Limit |
|---|---|---|
| Paired second ID `tower` (unique place) versus `mira` (unique character) after `harbor` | Keep `double-booked` for `tower`; keep `not a place` but withhold definite booking for `mira`. | `fixtures/r17-{valid-places,wrong-after}/` differ only in second-row `place_id`. Actual location of wrong-kind row unassessed. |
| Unique wrong-kind ID before a known place | Keep `not a place`; do not store wrong-kind row as occupied. | `fixtures/r17-wrong-before/` is the reversed two-event control. |
| Wrong-kind row first, middle, or last around known distinct places | Keep `not a place` and the known harbor/tower pair finding in each tested order. | `fixtures/r17-wrong-{first,middle,last}/`; selected schedules do not prove exhaustive pairwise handling. |

The guard applies only to exactly one indexed entity row with `kind != 'place'`, not duplicate/ambiguous IDs, whose separate diagnostics and raw-ID occupancy behavior remain. Required-field malformed entities are excluded from the index; unknown but nonempty kind remains indexed and wrong-kind. Fixture descriptions and unique source IDs are not source-text or canon proof; suppressed possible conflicts remain unassessed.

## Round 18 — ambiguous place entity ID

| Same uniquely screened actor/tick inputs | Definite occupancy decision | Limit |
|---|---|---|
| Unique `tower` + unique `harbor` versus otherwise identical input with second complete `harbor` entity | Keep known-pair booking in `r18-unique-pair`; retain duplicate/ambiguous findings but withhold booking involving `harbor` in `r18-duplicate-pair`. | The added entity row is the only paired difference; neither display name nor cited source resolves duplicate ID. |
| Ambiguous `harbor` first or with mixed-kind duplicate | Retain ambiguity finding; do not store/compare that row. | `r18-duplicate-reverse`, `r18-mixed-kind`; ambiguity is by ID count even when kinds differ. |
| Known `tower`, ambiguous `harbor`, known test-only `quay`; also ambiguous first | Retain tower/quay booking and ambiguity finding. | `r18-known-through-ambiguous`, `r18-duplicate-first-known`; finite order controls, not exhaustive pairwise proof. |

The checker retains raw timeline rows. Its guard for occupied slots now requires a unique actor and exactly one required-field-screened entity row with `kind == 'place'` for each participating event. This is an input-ID diagnostic, not a source-text or canon verdict. Unknown actual locations and any conflict involving an ambiguous row remain unassessed.

## Round 19 — negative timeline tick and definite occupancy

| Unique actor, two uniquely indexed places | Occupancy output | Limit |
|---|---|---|
| Paired same-tick `9` versus `-1` | Keep known-place booking at `9`; keep two invalid-tick findings at `-1` but withhold definite booking. | `fixtures/r19-{valid-tick,negative-tick}/` differ only in `tick` values; invalid time is not disproved narrative occurrence. |
| Known valid-time pair around invalid middle, or after invalid first | Retain each invalid-tick finding and known-place pair booking. | `fixtures/r19-{valid-around-negative,negative-first-valid}/`; selected orders only. |

Exactly typed integer ticks enter the timeline; bool/float fail required-field screening. Negative integer rows remain available to existing dependency validation, whose raw-tick inversion policy is not changed here. No source ID, event description or checker output establishes source-text time/canon; possible conflict at invalid numeric tick remains unassessed.

## Round 20 — invalid negative tick endpoint in dependency ordering

| Unique dependency ID and endpoint tick inputs | Ordering result | Limit |
|---|---|---|
| Prereq/dependent `0,1` versus `0,-1` | Valid control clean; negative dependent retains invalid-tick finding but withholds raw-tick inversion. | `fixtures/r20-{valid-order,negative-dependent}/` differ only in dependent tick; suppressed comparison does not prove edge satisfied. |
| `-1,1` and `-2,-1` | Retain each negative-tick diagnostic; do not compare ordering across invalid endpoint. | `fixtures/r20-{negative-prereq,both-negative}/`; do not count absence of inversion as definite valid chronology. |
| Valid `2,1` and equal `1,1` | Preserve inversion finding for nonnegative endpoints; equal tick also produces distinct occupied-slot finding. | `fixtures/r20-{valid-inversion,valid-equal}/`; occupancy is separate. |
| Negative prerequisite and separate valid inverted prerequisite to one dependent | Keep valid-edge inversion while invalid edge remains unassessed. | `fixtures/r20-mixed-edges/`; per-edge only, not graph-level proof. |

Unknown, ambiguous, self and repeated dependency-ID diagnostics retain their own behavior. Malformed tick types fail required-field screening; accepted negative integers retain raw rows/IDs. This checker does not validate source-text chronology, causal truth or canon.

## Round 21 — malformed dependency member and independent occupancy

| Two same-actor/tick fixture rows | Checker findings | Limit |
|---|---|---|
| Distinct known places; second `depends_on: []` versus `[null]` | Clean-list pair has known-place `double-booked`; malformed pair retains `expected event-id strings` **and** the same independent booking. | `fixtures/r21-{clean,malformed}/` differ only in dependency list; reversed place order at `r21-{clean-reverse,malformed-reverse}/`. |
| Same place or ineligible actor/place/tick with `[null]` | Keep dependency type and existing certainty diagnostics; no definite booking added. | `fixtures/r21-{same-place,invalid-tick,wrong-kind-place,ambiguous-actor}/`. |

A malformed list member makes **all dependency-member lookup on that row** unassessed; it does not invalidate otherwise resolved actor/place/tick occupancy. No coercion or partial list recovery is claimed. Fixture descriptions and source IDs do not prove event occurrence, source text, or canon.

## Round 22 — partial safe inspection of mixed dependency lists

| Dependent `depends_on` fixture input | Checker finding policy | Limit |
|---|---|---|
| `["r20-prereq"]` versus `["r20-prereq", null]` | Retain valid string-edge inversion in both; mixed adds one row-level type finding **before** inversion. | `fixtures/r22-{clean-inversion,mixed-last}/`; member order reversed in `r22-mixed-first/`. |
| `null`, object, array, then valid string | Emit one type finding, skip all invalid members without hashing/lookup, still inspect string edge. | `fixtures/r22-multiple-invalid/`; invalid edges unassessed, not satisfied. |
| Unknown string or repeated self strings beside `null` | Preserve existing string diagnostics in input order, plus single type finding. | `fixtures/r22-{unknown-mixed,self-repeated}/`. |
| Ordered valid edge or malformed member alone | Keep clean ordered case or one type error alone. | `fixtures/r22-{valid-order,malformed-only}/`; occupancy and global schema unchanged. |

A string edge's checker ordering is input-level only. The cited source ID does not attest chronology, occurrence or canon, and no truth is inferred for skipped malformed edges.

## Round 23 — witnessed-absence note class

| Input condition | Decision / output | Fixture evidence and limit |
|---|---|---|
| A named speaker reports, in a newly authored private note, that a named thing was not found at a named place. The note does not state a cause, does not say the thing was absent as world fact, and does not identify the thing with Mira’s Blue Seal or with the r15 mark. | Record the report as a **witnessed-absence** note. Map each clause to a fixture field by hand. Do not delete entities, clear occupancy, or treat the report as proof. | `fixtures/r23-note-class/` excerpt, timeline event `strip-absence-note`, and `witnessed-absence-clause-map.md`. Checker does not read the excerpt. Source-text truth is unverified. Distinct from `fixtures/r15-carbon-followup/` (present mark, origin unknown, not attributed to the Blue Seal). |

The checker still validates schema, citations, relations, and timeline structure only. A clean run is not a prose check and not canon.
