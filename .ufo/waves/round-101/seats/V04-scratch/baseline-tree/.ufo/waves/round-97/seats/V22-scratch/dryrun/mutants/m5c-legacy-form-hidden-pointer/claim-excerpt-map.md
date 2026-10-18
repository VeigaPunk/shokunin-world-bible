# r96 crossing-response: canonical claim-to-excerpt map

Scope: all 16 source-attributed JSON obligations in this continuation (five first-appearance pointers, five entity claims, one relation, and five timeline events), plus two separately labeled editorial comparisons. JSON pointers are relative to this fixture. `source_id` values remain cluster-local in JSON and are qualified in the map as `(cluster path, source ID)` pairs.

**Expected inventory:** 16 JSON facts; 2 editorial rows; 18 total mapped rows; 14 distinct excerpt anchors.

## R9 excerpt declarations

| Excerpt path | Source namespace / citation | Delivery mode | Status |
|---|---|---|---|
| `fictional-excerpts.md:12-40` | `r96-crossing-response:paired-clock`; `r96-crossing-response:crossing-minute`; `r96-crossing-response:aru-aftermath-note`; `r96-crossing-response:evin-response-note` | `verbatim` | Newly authored fictional register, minute, aftermath note, and response note; JSON sources in this fixture. Inherited namespaces were `r95-crossing-aftermath:paired-clock`, `r95-crossing-aftermath:crossing-minute`, `r95-crossing-aftermath:aru-aftermath-note`, `r94-paired-crossing:paired-clock`, `r94-paired-crossing:crossing-minute`, and (before that) `r88-m3-maya-cluster:paired-clock`. |
| `source-excerpt.md:5` | Lewis Spence, *The Myths of Mexico & Peru* (1913), English prose | `verbatim` | Delivered external comparison only; not an in-world source or support for JSON facts. The underlying K'iche primary text is not reproduced (`external-only`). |

`verbatim` names the delivered wording, not a claim that every normalized JSON field is a literal quotation. Review each whole proposition and its bounded scope.

## JSON facts (16 canonical pointers)

The 15 inherited rows carry the r94 JSON pointers, excerpt anchors, spans, and delivery modes unchanged; only the path-qualification column names this fixture's cluster path. The raw source IDs are cluster-local, resolved here as `r96-crossing-response:paired-clock` and `r96-crossing-response:crossing-minute`; the prior namespaces were `r95-crossing-aftermath:paired-clock` and `r95-crossing-aftermath:crossing-minute`. The new row resolves as `r96-crossing-response:evin-response-note`.

| ID | JSON fact and fields | In-world source ID | Path-qualified source namespace | Excerpt path | Line span | R9 delivery mode | Exact anchor |
|---|---|---|---|---|---:|---|---|
| J01 | `entities.json#/0/first_appearance` (`aru`) | `paired-clock` | `r96-crossing-response:paired-clock` | `fictional-excerpts.md` | 12 | `verbatim` | `Aru carried the north lantern at Quiet Rise` |
| J02 | `entities.json#/1/first_appearance` (`evin`) | `paired-clock` | `r96-crossing-response:paired-clock` | `fictional-excerpts.md` | 13 | `verbatim` | `Evin held the south bell at Salt Court` |
| J03 | `entities.json#/2/first_appearance` (`quiet-rise`) | `paired-clock` | `r96-crossing-response:paired-clock` | `fictional-excerpts.md` | 12 | `verbatim` | `Aru carried the north lantern at Quiet Rise` |
| J04 | `entities.json#/3/first_appearance` (`salt-court`) | `paired-clock` | `r96-crossing-response:paired-clock` | `fictional-excerpts.md` | 13 | `verbatim` | `Evin held the south bell at Salt Court` |
| J05 | `entities.json#/4/first_appearance` (`chalk-stair`) | `crossing-minute` | `r96-crossing-response:crossing-minute` | `fictional-excerpts.md` | 17 | `verbatim` | `The Chalk Stair is the named rain-dark crossing between Quiet Rise and Salt Court.` |
| J06 | `entities.json#/0/claims/0` (`statement`, `source_id`) | `paired-clock` | `r96-crossing-response:paired-clock` | `fictional-excerpts.md` | 12 | `verbatim` | `Tick 9: Aru carried the north lantern at Quiet Rise.` |
| J07 | `entities.json#/1/claims/0` (`statement`, `source_id`) | `paired-clock` | `r96-crossing-response:paired-clock` | `fictional-excerpts.md` | 13 | `verbatim` | `Tick 9: Evin held the south bell at Salt Court.` |
| J08 | `entities.json#/2/claims/0` (`statement`, `source_id`) | `paired-clock` | `r96-crossing-response:paired-clock` | `fictional-excerpts.md` | 12 | `verbatim` | `north lantern at Quiet Rise` |
| J09 | `entities.json#/3/claims/0` (`statement`, `source_id`) | `paired-clock` | `r96-crossing-response:paired-clock` | `fictional-excerpts.md` | 13 | `verbatim` | `south bell at Salt Court` |
| J10 | `entities.json#/4/claims/0` (`statement`, `source_id`) | `crossing-minute` | `r96-crossing-response:crossing-minute` | `fictional-excerpts.md` | 18 | `verbatim` | `After both Tick 9 entries above, Aru and Evin met at the Chalk Stair at tick 10.` |
| J11 | `relations.json#/0` (`from`, `to`, `type`, `source_id`) | `crossing-minute` | `r96-crossing-response:crossing-minute` | `fictional-excerpts.md` | 19 | `verbatim` | `There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.` |
| J12 | `timeline.json#/0` (`tick`, `entity_id`, `place_id`, `depends_on`, `description`, `source_id`) | `paired-clock` | `r96-crossing-response:paired-clock` | `fictional-excerpts.md` | 12 | `verbatim` | `Aru carried the north lantern at Quiet Rise` |
| J13 | `timeline.json#/1` (`tick`, `entity_id`, `place_id`, `depends_on`, `description`, `source_id`) | `paired-clock` | `r96-crossing-response:paired-clock` | `fictional-excerpts.md` | 13 | `verbatim` | `Evin held the south bell at Salt Court` |
| J14 | `timeline.json#/2` (`tick`, `entity_id`, `place_id`, `depends_on`, `description`, `source_id`) | `crossing-minute` | `r96-crossing-response:crossing-minute` | `fictional-excerpts.md` | 18-20 | `verbatim` | `Their tick-10 decision depends on both ninth-bell entries: Aru's north-lantern entry at Quiet Rise and Evin's south-bell entry at Salt Court. After agreeing to share stewardship for this crossing only, they chalked one temporary route mark together at the midpoint.` |
| J15 | `timeline.json#/3` (`tick`, `entity_id`, `place_id`, `depends_on`, `description`, `source_id`) | `aru-aftermath-note` | `r96-crossing-response:aru-aftermath-note` | `fictional-excerpts.md` | 22-31 | `verbatim` | `Tick 11: I waited at the Chalk Stair through the agreed bell.` |
| J16 | `timeline[4]` (also `relations.json#/0`) | `evin-response-note` | `r96-crossing-response:evin-response-note` | `fictional-excerpts.md` | 33-42 | `verbatim` | `Tick 12: I was at Salt Court through the same agreed bell.` |

## Editorial rows (2 bounded Spence comparisons; not JSON facts)

These rows compare delivered Spence clauses with the fictional design; they do not make Spence an in-world witness, assign cultural meaning, or add canon. `verbatim` describes the English prose delivered in `source-excerpt.md`, not an authenticated K'iche-language text.

| ID | Bounded editorial comparison | Source citation | Excerpt path | Line span | R9 delivery mode | Exact anchor |
|---|---|---|---|---:|---|---|
| S01 | Spence's phrase has the narrator call out “Earth”; the fiction's named Chalk Stair is a bounded crossing, not a world-making act. | Lewis Spence (1913), cited above | `source-excerpt.md` | 5 | `verbatim` | `He called out “Earth,”` |
| S02 | Spence says solid land appeared; the fiction's chalk stair remains “a crossing, never a map,” a limited design contrast rather than a shared cosmology. | Lewis Spence (1913), cited above | `source-excerpt.md` | 5 | `verbatim` | `and the solid land appeared.` |

## Timeline normalization and scope

The inherited tick-9 entries are separate occasions at distinct places; the inherited tick-10 decision is ordered after and depends on both (`aru-ninth-bell` and `evin-ninth-bell`); the inherited tick-11 aftermath event is ordered after and depends on the tick-10 decision (`paired-crossing-decision`); the new tick-12 response event is ordered after and depends on the tick-11 report (`aftermath-missing-evin`). The tick integers and `depends_on` event IDs are editorial encodings of the excerpts' explicit tick/order/dependence wording, not literal JSON syntax in the sources. Each inherited empty dependency list means no earlier dependency is represented in this mapped sequence, not that no earlier event exists anywhere. The new tick-12 event encodes only Evin's second account of the same crossing occasion; it asserts no reconciliation, selects no winner between the accounts, and adds no duty beyond this crossing, not perpetual performance or alliance.

J15's anchor is the tick-11 waiting sentence (line 26); its declared span 22-31 is exactly the inherited aftermath section, whose remaining quoted lines carry the non-arrival (`Evin did not come.`, line 27), the crossing-only bound, and the explicit no-other-duty/no-breach assertion (lines 28-29). The event records one non-arrival on one occasion: it asserts no breach, no continuing duty, and no obligation beyond this crossing, and the record supplies no other duty. The event's `entity_id` is Aru because the schema has one actor slot; its description names Evin's non-arrival, so the field does not exclude the second participant.

J16's anchor is the tick-12 response sentence (line 37); its declared span 33-42 is exactly the appended response section, whose remaining quoted lines carry the no-accusation assertion (`I make no accusation against Aru.`, line 38), the no-winner selection (`I select no winner between our two accounts.`, line 39), and the unresolved-status statement (`Both accounts stand unresolved.`, line 40). The event records one second account of the same occasion: Evin reports being at Salt Court through the same agreed bell, while Aru's inherited report placed himself at the Chalk Stair. The two accounts name different actors at different places, so no contradiction is asserted and `contradictions.json` remains empty; neither account is selected as winner, no accusation is made, and the record asserts no breach, no continuing duty, and no obligation beyond this crossing. The event's `entity_id` is Evin because the schema has one actor slot; its description names Aru's account, so the field does not exclude the other participant.

`support_check.py` checks declared row inventory, fixed-string anchors, spans, and R9 mode; its receipt is lexical preflight, not manual whole-claim entailment or a verdict on source authenticity, truth, rights, permission, or canon.
