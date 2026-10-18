source: `corpus/fixtures/r95-crossing-aftermath/{sources.json,timeline.json,relations.json,fictional-excerpts.md,README.md,claim-excerpt-map.md,entities.json,contradictions.json,inspiration-note.md,source-excerpt.md}`; `corpus/fixtures/r94-paired-crossing/{relations.json,timeline.json,README.md,sources.json,fictional-excerpts.md}`; `corpus/knowledge/2026-10-12-lore-decision-table.md` (Round 23 row); `corpus/fixtures/r23-note-class/{sella-absence-note-excerpt.md,witnessed-absence-clause-map.md,timeline.json,sources.json}`; `corpus/fixtures/README.md` (Round 94 section)
verified-at: 2026-10-17 — read every cited local record and excerpt in the delivered r95 fixture and its r94/r23 counterparts; no external URL was fetched in this pass.
recheck: before integrating any r95 aftermath claim, and whenever the aftermath note, the tick-11 event, the inherited r94 relation or decision rows, the map rows, or the checker receipts change; independently inspect the note's whole proposition before making any breach, duty, performance, identity, or canon claim.

# Reported non-performance against a crossing-scoped agreement — round 95

This is a bounded knowledge record, not merged canon, not a breach finding, and not a verdict on any character. It names one new observation class and the exact records that carry it. The checker does not read prose; a clean run is structural only.

## The observation class

**Reported non-performance** — one named speaker's first-person report that an agreed action did not occur on one occasion, where the agreement's own record bounds it to that one crossing. The class is defined by what the record says, not by what happened in the fiction: the note reports a non-arrival; it does not establish world-absence, fault, or a broken obligation.

This is distinct from the r23 witnessed-absence class in object and scope. r23 records a speaker reporting that a named *thing* was not found at a named place (`corpus/fixtures/r23-note-class/`); r95 records a speaker reporting that a named *person* did not arrive under a bounded agreement. Both are report-not-proof classes; neither is a contradiction, an occupancy change, or a fact about the world.

## Records that carry the class (exact)

| Element | Record | Delivered content |
|---|---|---|
| Reported non-arrival source | `corpus/fixtures/r95-crossing-aftermath/sources.json#/3` (`aru-aftermath-note`, id at `sources.json:21`) | Newly authored fictional first-person note; reliability note: "Aru reports waiting at the Chalk Stair through the agreed bell and that Evin did not come. It records one crossing occasion only and is not evidence of a breach, a continuing duty, a perpetual obligation, or an external historical fact." |
| Note text | `corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md:22-31` (quoted lines 26-29) | "Tick 11: I waited at the Chalk Stair through the agreed bell. / Evin did not come. / The agreement we chalked covered this crossing only. / I assert no other duty, no breach, and no obligation beyond this crossing." |
| Event | `corpus/fixtures/r95-crossing-aftermath/timeline.json#/3` (`aftermath-missing-evin`, id at `timeline.json:33`) | tick 11, `entity_id: aru`, `place_id: chalk-stair`, `depends_on: ["paired-crossing-decision"]`, `source_id: aru-aftermath-note` |
| Scope bound (inherited, unchanged) | `corpus/fixtures/r95-crossing-aftermath/relations.json#/0`, byte-identical to `corpus/fixtures/r94-paired-crossing/relations.json#/0` | `agreed_co_stewardship_for_this_crossing`, source `crossing-minute`; excerpt `fictional-excerpts.md:19`: "for this crossing only" |
| Map row | `corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md:36` (J15) | 15th canonical pointer with anchor `Tick 11: I waited at the Chalk Stair through the agreed bell.` (line 26), span 22-31, mode `verbatim` |

No entity, relation, or inherited event row changed: `entities.json`, `relations.json`, `contradictions.json`, `inspiration-note.md`, and `source-excerpt.md` are byte-identical to `r94-paired-crossing` (verified this pass), and `r95 timeline.json[:3] == r94 timeline.json` parsed-equal (`True`).

## Bounds (explicit)

- **Aru's report only.** The class rests on one named speaker's authored note. Per its reliability note (`sources.json#/3`) and `fictional-excerpts.md:31`, it records one crossing occasion; it is not proof that Evin was absent as world fact, not proof of any cause, and not independent corroboration.
- **No other-duty or breach assertion.** The record asserts no breach, no continuing or perpetual obligation, no duty beyond this crossing, and supplies no other duty (`README.md:11`; `claim-excerpt-map.md:51`; `fictional-excerpts.md:28-29`). Do not infer abandonment, fault, guilt, an alliance failure, or a standing duty.
- **Editorial tick/ID alignments.** The tick integers (`11`), the event ID `aftermath-missing-evin`, and the `depends_on: ["paired-crossing-decision"]` edge are editorial encodings of the excerpt's tick label and stated order/dependence, not literal JSON wording in the note (`README.md:13`; `claim-excerpt-map.md:49`). The event's `entity_id: aru` is the schema's single actor slot and does not remove Evin from the report (`README.md:11`).
- **Checker validates structure, not testimony.** `check_bible.py` validates schema, citations, relations, and timeline structure; `support_check.py` is a lexical/span/mode receipt; `map_obligations.py` covers raw-JSON↔map completeness and source-ID agreement only. None reads the note as testimony or decides truth, breach, chronology, rights, permission, or canon.
- **No contradiction created.** The tick-11 report does not revise the tick-9 entries or the tick-10 decision, and `contradictions.json` remains empty (`[]`) in both r94 and r95. The inherited occasion comparison stands (`README.md:9`).

## Precedent cross-reference

- **r94 continuation decision row (precedent for the bounded agreement).** The r94 continuation's decision is the tick-10 event `paired-crossing-decision` at `corpus/fixtures/r94-paired-crossing/timeline.json#/2` (id at `timeline.json:21`), carried unchanged at `corpus/fixtures/r95-crossing-aftermath/timeline.json#/2`; its source `crossing-minute` (`corpus/fixtures/r94-paired-crossing/sources.json#/2`) states it "records one bounded crossing decision and agreement, not evidence of continuing performance, a standing alliance, or an external historical fact," and the r94 README bounds it: "It is not evidence of an alliance, a continuing practice, or perpetual performance" (`corpus/fixtures/r94-paired-crossing/README.md:9`). The r95 aftermath report is measured against exactly that bounded row — the crossing-only scope is the reason a reported non-arrival is not automatically a breach. Catalogued in `corpus/fixtures/README.md` (Round 94 section, `:1154-1173`).
- **r23 witnessed-absence class (precedent for report-not-proof discipline).** Decision-table row `corpus/knowledge/2026-10-12-lore-decision-table.md:226-230`: record the report as a note class, map each clause by hand, "do not delete entities, clear occupancy, or treat the report as proof"; the checker does not read the excerpt and source-text truth is unverified. Fixture evidence: `corpus/fixtures/r23-note-class/sella-absence-note-excerpt.md`, timeline event `strip-absence-note` (`timeline.json#/2`), and `witnessed-absence-clause-map.md:1-3`. The r95 note applies the same discipline to a different object (a person's reported non-arrival under a bounded agreement rather than a thing's reported non-finding).

## Receipts (measured this pass, from the lane root)

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath
# CLEAN: schema, citations, relations, timeline; 0 violations   exit 0
python3 corpus/tools/support_check.py corpus/fixtures/r95-crossing-aftermath
# JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17; DISTINCT-ANCHORS 13/13; MODES 17/17; VALIDATED-ROWS 17/17 / RESULT PASS   exit 0
python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
# OBLIGATIONS raw=15 mapped=15 / RESULT PASS   exit 0
```

Tool revisions at these receipts (2026-10-17T16:25-03:00): `check_bible.py` sha256 `ff9fd2aa…`, `support_check.py` `55a5eb27…`, `map_obligations.py` `9224a684…`. The C1 tool revision was still in flight during this round: earlier receipts in this pass also passed at the r94 baseline (`map_obligations.py` `cc1df4dc…`), while an intermediate in-flight revision (`ca05159e…`) raised an uncaught `ValueError` on both the r94 and r95 maps — recorded with timestamps in `.ufo/waves/round-95/seats/P5-knowledge-note.md`. Re-run all three commands against the delivered revision before citing these receipts.

Cited-path existence and inheritance checks (python3, this pass): every path named in this record exists; `entities.json`/`relations.json`/`contradictions.json`/`inspiration-note.md`/`source-excerpt.md` byte-identical (`cmp`) between r94 and r95; `r95 timeline.json[:3] == r94 timeline.json` → `True`; sources `r95[:3] == r94` → `True`; all 14 inherited map rows J01-J14 identical modulo cluster-path qualification; r95 adds only J15.

## Limits of this record

This is an author-seat knowledge note, not independent verification, admission, or a non-author review. It does not authenticate the fictional sources, does not adjudicate any character, and does not extend to any record outside the cited paths. The r95 fixture is a declared continuation of `r94-paired-crossing`, itself a continuation of `r88-m3-maya-cluster`; source IDs remain cluster-local and path-qualified comparisons are not identity evidence. Rights and AI-training permission remain unassessed here.

## Correction addendum (2026-10-17, round 98, S5 knowledge-notes seat)

The receipts paragraph above is preserved unrewritten, but its tool-revision pin is stale. `map_obligations.py` `9224a684…` was an in-flight intermediate revision during round 95 and never entered the file's committed history (the committed revisions are `cc1df4dc…` r94, `d1c239cc…` r95, `2b0ba815…` r96, `86b52949…` r97). Current delivered revisions measured at this addendum's run time (2026-10-17T20:28:35-03:00, from the lane root):

```sh
sha256sum corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json
# 86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9  corpus/tools/map_obligations.py
# 2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41  corpus/tools/map-obligations-contract.json
```

`check_bible.py` `ff9fd2aa…` and `support_check.py` `55a5eb27…` named above are still current (re-measured the same pass). The three receipts above were re-derived at this current revision this pass and are unchanged: `check_bible` CLEAN exit 0; `support_check` `JSON-FACTS 15/15` / `EDITORIAL-ROWS 2/2` / `TOTAL-ROWS 17/17` / `RESULT PASS` exit 0; `map_obligations` `raw=15 mapped=15` / `RESULT PASS` exit 0.

Instruction: on the next touch of this note, re-derive all three receipts and re-measure the tool revisions before citing them; do not cite `9224a684…` as current. Round 98's C1 work owns `corpus/tools/dependency_freeze.py` and `corpus/tools/dependency-freeze-contract.json`, not `map_obligations.py` or its contract, so the two hashes above should hold unless a later round changes them. The historical text above stays unrewritten; this addendum is the correction of record.
