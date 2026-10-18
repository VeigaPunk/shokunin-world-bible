# DRAFT (Q6 scratch) — to be finalized into corpus/knowledge/r96-response-scope-note.md

source: `corpus/fixtures/r96-crossing-response/{sources.json,timeline.json,fictional-excerpts.md,README.md,claim-excerpt-map.md,entities.json,relations.json,contradictions.json,inspiration-note.md,source-excerpt.md}`; `corpus/fixtures/r95-crossing-aftermath/{sources.json,timeline.json,fictional-excerpts.md,README.md,claim-excerpt-map.md}`; `corpus/knowledge/r95-aftermath-scope-note.md`; `corpus/fixtures/r35-bell7-conflict/{contradictions.json,timeline.json,manual-clause-pointer-map.md,sella-bell7-note-excerpt.md,tarin-note-excerpt.md}`; `corpus/fixtures/README.md` (Round 35 and Round 95 sections)
verified-at: 2026-10-17 — read every cited local record and excerpt in the delivered r96 fixture and its r95/r35 counterparts; no external URL was fetched in this pass.
recheck: before integrating any r96 response claim, and whenever the response note, the tick-12 event, the inherited r95 rows, the map rows, or the checker receipts change; independently inspect the note's whole proposition before making any breach, duty, performance, identity, or canon claim.

# A second first-person account of one occasion, left unresolved — round 96

This is a bounded knowledge record, not merged canon, not a contradiction finding, and not a verdict on any character. It names one new observation class and the exact records that carry it. The checker does not read prose; a clean run is structural only.

## The observation class

**Second first-person account, same occasion, unresolved** — a second named speaker's own first-person report of the same agreed crossing occasion, added beside the first account, where the record explicitly asserts no accusation, selects no winner, and states that both accounts stand unresolved. The class is defined by what the record says, not by what happened in the fiction: two first-person reports are preserved side by side and neither is declared true, false, or superseded.

This is distinct from the r95 reported-non-performance class in who speaks and what is claimed. r95 records one speaker's report that an agreed action did not occur (`corpus/knowledge/r95-aftermath-scope-note.md`); r96 adds the *other* participant's own account of that same occasion without any counter-accusation. It is also distinct from the r35 Bell-7 class, where a two-sided ledger pair encodes an apparent incompatibility between two reports about one named ringing: r96 asserts no contradiction at all and its `contradictions.json` stays empty (`[]`).

## Records that carry the class (exact)

| Element | Record | Delivered content |
|---|---|---|
| Response source | `corpus/fixtures/r96-crossing-response/sources.json#/4` (`evin-response-note`) | Newly authored fictional first-person note; reliability note: "Evin reports being at Salt Court through the same agreed bell. It asserts no accusation against Aru, selects no winner, and states that both first-person accounts stand unresolved." |
| Note text | `corpus/fixtures/r96-crossing-response/fictional-excerpts.md:33-42` (quoted lines 37-40) | "Tick 12: I was at Salt Court through the same agreed bell. / I make no accusation against Aru. / I select no winner between our two accounts. / Both accounts stand unresolved." |
| Event | `corpus/fixtures/r96-crossing-response/timeline.json#/4` (`response-evin-salt-court`) | tick 12, `entity_id: evin`, `place_id: salt-court`, `depends_on: ["aftermath-missing-evin"]`, `source_id: evin-response-note` |
| Prior account (inherited, unchanged) | `corpus/fixtures/r96-crossing-response/timeline.json#/3` (`aftermath-missing-evin`), parsed-equal to `corpus/fixtures/r95-crossing-aftermath/timeline.json#/3` | tick 11, `entity_id: aru`, `place_id: chalk-stair`, `depends_on: ["paired-crossing-decision"]`, `source_id: aru-aftermath-note` |
| Scope bound (inherited, unchanged) | `corpus/fixtures/r96-crossing-response/relations.json#/0`, byte-identical to `corpus/fixtures/r95-crossing-aftermath/relations.json#/0` | `agreed_co_stewardship_for_this_crossing`, source `crossing-minute`; excerpt `fictional-excerpts.md:19`: "for this crossing only" |
| Map row | `corpus/fixtures/r96-crossing-response/claim-excerpt-map.md:<LINE>` (J16) | 16th canonical pointer with anchor `Tick 12: I was at Salt Court through the same agreed bell.` (line 37), span 33-42, mode `verbatim` |

No entity, relation, or inherited event row changed: `entities.json`, `relations.json`, `contradictions.json`, `inspiration-note.md`, and `source-excerpt.md` are byte-identical to `r95-crossing-aftermath` (verified this pass, `cmp`), `r96 timeline.json[:4] == r95 timeline.json` parsed-equal (`True`), and `r96 sources.json[:4] == r95 sources.json` (`True`).

## Bounds (explicit)

- **Two reports only.** The class rests on two named speakers' authored notes: Aru's inherited tick-11 note (`aru-aftermath-note`) and Evin's added tick-12 response note (`evin-response-note`). Neither is independent corroboration of the other; neither is proof of any world fact.
- **No contradiction asserted — different actors and places.** Aru's report is a non-arrival at the Chalk Stair by actor `aru`; Evin's report is her own presence at Salt Court by actor `evin`. The two records name different actors at different places, so they are not two sides of one field comparison; `contradictions.json` remains empty (`[]`) in r95 and r96 and no ledger pair is added.
- **No testimony truth.** The record does not establish that Evin was at Salt Court as world fact, does not establish that Evin did or did not come to the Chalk Stair, and does not authenticate either source text. Per its reliability note, the response note records one crossing occasion only and is not evidence of a breach, a continuing duty, a perpetual obligation, or an external historical fact.
- **Editorial tick/ID alignments.** The tick integer `12`, the event ID `response-evin-salt-court`, and the `depends_on: ["aftermath-missing-evin"]` edge are editorial encodings of the excerpt's tick label and stated order/dependence, not literal JSON wording in the note. The event's `entity_id: evin` is the schema's single actor slot.
- **Checker validates structure, not testimony.** ...
- **No winner selected and no canon claim.** ...

## Precedent cross-reference

- r95 aftermath scope note (the first account)
- r35 two-sided-preservation precedent

## Receipts (measured this pass, from the lane root)

## Limits of this record
