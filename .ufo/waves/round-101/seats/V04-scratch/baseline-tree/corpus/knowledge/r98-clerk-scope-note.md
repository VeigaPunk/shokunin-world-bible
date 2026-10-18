source: `corpus/fixtures/r98-clerk-filing/{sources.json,timeline.json,entities.json,fictional-excerpts.md,README.md,claim-excerpt-map.md,relations.json,contradictions.json,inspiration-note.md,source-excerpt.md}`; `corpus/fixtures/r97-crossing-acknowledgment/{timeline.json,sources.json,entities.json,relations.json,contradictions.json,claim-excerpt-map.md}`; `corpus/knowledge/r97-acknowledgment-scope-note.md`; `corpus/knowledge/r95-aftermath-scope-note.md`; `corpus/knowledge/r96-response-scope-note.md`; `corpus/fixtures/r10-registry-witness/{registrar-copy-excerpt.md,sources.json,entities.json,relations.json,timeline.json,contradictions.json}`; `corpus/fixtures/README.md` (Round 10, Round 95, Round 96, Round 97 sections); `corpus/knowledge/2026-10-12-lore-decision-table.md` (Round 10 and Round 23 rows)
verified-at: 2026-10-17 — read every cited local record and excerpt in the delivered r98 fixture and its r97/r10 counterparts; every cited path and line was checked to exist this pass; no external URL was fetched.
recheck: before integrating any r98 clerk-filing claim, and whenever the filing note, the tick-14 event, the new entity or its claim, the inherited r97 rows, the map rows, or the checker receipts change; independently inspect the note's whole proposition before making any finding, resolution, adjudication, breach, duty, performance, identity, or canon claim.
citation-convention: bare `file:line` and `file#/N` citations resolve against `corpus/fixtures/r98-clerk-filing/`; records of other fixtures and the `corpus/knowledge/` notes are cited by full path, and a bare `:NN` continues the most recently named path in the same sentence.

# Institutional filing record asserting no finding — round 98

This is a bounded knowledge record, not merged canon, not a finding, not an adjudication, and not a verdict on any character. It names one new observation class and the exact records that carry it. The checker does not read prose; a clean run is structural only.

## The observation class

**Institutional filing record asserting no finding** — a named office-holder's own first-person record that he filed both pending accounts with the registry and recorded the matter OPEN, where the record itself asserts no finding, reaches no verdict, and reconciles nothing. The class is defined by what the record says, not by what happened in the fiction: the note records an institutional act of filing; it does not establish that either account is true or false, does not adjudicate between them, and does not close the matter.

This is the fourth beat of the crossing-arc records: r95 carries Aru's reported non-performance (first account), r96 carries Evin's second account of the same occasion, r97 carries Aru's acknowledgment that he received that response, and r98 carries the harbor clerk's filing of both pending accounts. It is distinct from the r97 acknowledgment class in speaker and object: r97's class rests on a participant's receipt of the other participant's response, while r98's class rests on a non-participant office-holder's institutional act — filing both accounts and recording the matter OPEN — with the unresolved status inherited and re-asserted, not decided.

It is also distinct from the r35 Bell-7 class (`corpus/fixtures/r35-bell7-conflict/contradictions.json#/0`), where a two-sided ledger pair encodes an apparent incompatibility between two reports about one named ringing: r98 asserts no contradiction at all, and its `contradictions.json` stays empty (`[]`).

## Records that carry the class (exact)

| Element | Record | Delivered content |
|---|---|---|
| Filing source | `sources.json#/6` (`clerk-filing-note`, id at `sources.json:39`) | Newly authored fictional first-person note; title "Maren's Chalk Stair Registry Filing Note" (`sources.json:40`); reliability note (`sources.json:42`): "Newly authored fictional note; the clerk reports filing both pending accounts at the Chalk Stair registry and recording the matter OPEN. It asserts no finding, no verdict, no reconciliation, and no resolution; it is not evidence of a breach, a continuing duty, a winner between the accounts, or an external historical fact." |
| Note text | `fictional-excerpts.md:55-64` (quoted lines 59-62) | "Tick 14: I filed both pending accounts at the Chalk Stair registry. / I am Maren, clerk of the Chalk Stair registry, and I record the matter OPEN. / I assert no finding. / I reach no verdict and reconcile nothing." |
| New entity | `entities.json#/5` (`clerk-maren`, id at `entities.json:63`) | `kind: character`, `name: "Maren"`, `first_appearance: clerk-filing-note` (`entities.json:66`); one claim (`entities.json#/5/claims/0`, statement at `:69`, `source_id` at `:70`): "The filing note names Maren, the clerk of the Chalk Stair registry, as the officer who filed both pending accounts." |
| Event | `timeline.json#/6` (`clerk-filing-open`, id at `timeline.json:66`) | tick 14, `entity_id: clerk-maren`, `place_id: chalk-stair`, `depends_on: ["acknowledgment-aru-records"]`, `source_id: clerk-filing-note`; description (`timeline.json:73`): "At the Chalk Stair at tick 14, the clerk filed both pending accounts and recorded the matter OPEN, asserting no finding and no resolution." |
| Prior acknowledgment (inherited, unchanged) | `timeline.json#/5` (`acknowledgment-aru-records`), parsed-equal to `corpus/fixtures/r97-crossing-acknowledgment/timeline.json#/5` | tick 13, `entity_id: aru`, `place_id: chalk-stair`, `depends_on: ["response-evin-salt-court"]`, `source_id: aru-acknowledgment-note` |
| Scope bound (inherited, unchanged) | `relations.json#/0`, byte-identical to r97 `relations.json#/0` | `agreed_co_stewardship_for_this_crossing`, source `crossing-minute`; excerpt `fictional-excerpts.md:19`: "for this crossing only" |
| Map rows | `claim-excerpt-map.md:39` (J18), `:40` (J19), `:41` (J20) | J18: `entities.json#/5/first_appearance`, anchor `I am Maren, clerk of the Chalk Stair registry` (line 60), span 60, `verbatim`. J19: `entities.json#/5/claims/0`, anchor `I filed both pending accounts at the Chalk Stair registry.` (line 59), span 59-60, `verbatim`. J20: `timeline.json#/6`, anchor `Tick 14: I filed both pending accounts at the Chalk Stair registry.` (line 59), span 55-64, `verbatim`. Bounded readings at `:62`, `:64`, `:66`. |

No inherited row changed: `contradictions.json`, `inspiration-note.md`, `relations.json`, and `source-excerpt.md` are byte-identical to `r97-crossing-acknowledgment` (verified this pass with `cmp`); `r98 entities.json[:5] == r97 entities.json`, `r98 sources.json[:6] == r97 sources.json`, and `r98 timeline.json[:6] == r97 timeline.json` parsed-equal (`True`); the 17 inherited map rows J01-J17 are identical modulo the namespace column (0 other diffs). The fixture declares 6 entities / 1 relation / 7 events / 7 sources (`README.md:3`) and 20 map obligations — the 17 inherited rows unchanged plus the three new clerk rows (`README.md:21`; `claim-excerpt-map.md:3`, `:5`).

## Bounds (explicit)

- **The clerk's filing only.** The class rests on one named office-holder's authored note. Per its reliability note (`sources.json:42`) and `fictional-excerpts.md:64`, it records one filing; it is not proof that the accounts were in fact filed as world fact, not independent corroboration, and not an adjudication.
- **No finding, no resolution truth.** The note asserts no finding (`fictional-excerpts.md:61`) and reaches no verdict and reconciles nothing (`:62`); the two first-person accounts stand unresolved (`:64`; `README.md:11`). Do not infer that the matter is closed, that either account is true or false, or that the filing settles, merges, or reconciles the accounts.
- **No winner, no new duty.** The record selects no winner between the accounts and adds no duty beyond this crossing; the crossing-only bound is retained (`relations.json#/0`; `fictional-excerpts.md:19`). Do not infer fault, guilt, an alliance failure, a standing duty, or an adjudication.
- **First-appearance bound.** `first_appearance: clerk-filing-note` identifies the source that first presents Maren as a named entity in this JSON bible; it asserts no office beyond the filing, no finding, and no other record (`README.md:15`; `claim-excerpt-map.md:62`). The office wording ("clerk of the Chalk Stair registry") is the note's own attributed self-description (`fictional-excerpts.md:60`), not independent identity proof.
- **Editorial tick/ID alignments.** The tick integer `14`, the event ID `clerk-filing-open`, and the `depends_on: ["acknowledgment-aru-records"]` edge are editorial encodings of the excerpt's tick label and stated order/dependence, not literal JSON wording in the note (`README.md:13`; `claim-excerpt-map.md:54`). The event's `entity_id: clerk-maren` is the schema's single actor slot and does not remove the two participants from the record (`README.md:11`; `claim-excerpt-map.md:66`).
- **Checker validates structure, not testimony.** `check_bible.py` validates schema, citations, relations, and timeline structure; `support_check.py` is a lexical/span/mode receipt; `map_obligations.py` covers raw-JSON↔map completeness and source-ID agreement only. None reads the note as testimony or decides truth, finding, chronology, adjudication, rights, permission, or canon.
- **No contradiction created.** The tick-14 filing does not revise the tick-11..13 rows, and `contradictions.json` remains empty (`[]`) in r95, r96, r97, and r98 (`README.md:11`).

## Precedent cross-reference

- **r97 acknowledgment scope note (immediate predecessor).** `corpus/knowledge/r97-acknowledgment-scope-note.md` records the cross-account-acknowledgment-without-reconciliation class carried by `aru-acknowledgment-note` and the tick-13 event `acknowledgment-aru-records` (`corpus/fixtures/r97-crossing-acknowledgment/sources.json#/5`; `corpus/fixtures/r97-crossing-acknowledgment/timeline.json#/5`). The r98 fixture inherits that event and both first-person accounts unchanged and adds one source, one entity, and one event (`README.md:3`, `:7`, `:9`). The filing is measured against exactly that record: the acknowledgment left both accounts unresolved, and the filing records the matter OPEN without deciding them.
- **r10 registry-witness precedent (the earlier institutional-record discipline).** `corpus/fixtures/r10-registry-witness/` adds an authored in-world registry account by a registrar: Sella's invented excerpt (`registrar-copy-excerpt.md`, source `registrar-copy` at `corpus/fixtures/r10-registry-witness/sources.json#/2`) is an authored second perspective, and its `registry-entry` event (`corpus/fixtures/r10-registry-witness/timeline.json#/2`) carries the registrar's act of recording with the destination deliberately left blank; the `records_departure` relation is `corpus/fixtures/r10-registry-witness/relations.json#/1`. The documented limits are the same discipline r98 applies: the entry "does **not** assert a different destination or settle whether Sella's report is true" (`corpus/fixtures/README.md:209-210`); the fixture is "an authored second perspective, not external corroboration or canon resolution" (`corpus/knowledge/2026-10-12-lore-decision-table.md:112`); and the checker "does not parse the excerpt or certify that source text entails the JSON" (`:112`). r98 applies that discipline to a different object: r10's registrar records a departure with a blank destination; r98's clerk files two pending accounts and records the matter OPEN, asserting no finding. Both are institutional records of an act of recording, not adjudications, and neither settles the truth of the accounts it carries. The two fixtures must not be read as the same class.
- **r95/r96 notes (the arc's earlier beats).** `corpus/knowledge/r95-aftermath-scope-note.md` (Aru's reported non-performance) and `corpus/knowledge/r96-response-scope-note.md` (Evin's second account) carry the earlier beats; both were continued unchanged into r97 and r98, and both gained a dated correction addendum this round correcting their stale tool-revision pins (see Receipts).
- **r23 witnessed-absence class (report-not-proof discipline).** Decision-table row `corpus/knowledge/2026-10-12-lore-decision-table.md:226-230`: record a report as a note class, map each clause by hand, "do not delete entities, clear occupancy, or treat the report as proof"; the checker does not read the excerpt. The clerk's filing is held to that discipline.

## Receipts (measured this pass, from the lane root)

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r98-clerk-filing
# CLEAN: schema, citations, relations, timeline; 0 violations   exit 0
python3 corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing
# INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 18/18
# ANCHORS repeated-references=4; DUPLICATE-ROWS 0
# RECEIPT JSON-FACTS 20; EDITORIAL-ROWS 2; TOTAL-ROWS 22
# SOURCE-SUPPORT 20/20; EDITORIAL-ANCHORS 2/2; MODES 22/22; VALIDATED-ROWS 22/22
# RESULT PASS   exit 0
python3 corpus/tools/map_obligations.py corpus/fixtures/r98-clerk-filing
# OBLIGATIONS raw=20 mapped=20 / INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22 / RESULT PASS   exit 0
```

Tool revisions at these receipts (2026-10-17T20:31-03:00, from the lane root): `check_bible.py` sha256 `ff9fd2aa…`, `support_check.py` `55a5eb27…`, `map_obligations.py` `86b52949…` (contract `2142b991…`). The r95/r96 receipts were re-derived at the same revisions this pass and are unchanged (`raw=15 mapped=15` and `raw=16 mapped=16`, both `RESULT PASS` exit 0); the r97 fixture reads `raw=17 mapped=17` / `RESULT PASS` exit 0. Round 98's C1 work owns `corpus/tools/dependency_freeze.py` and `corpus/tools/dependency-freeze-contract.json`, and those two files still read their r97-closure bytes at this pass's receipt measurement (20:31-03:00); S1's C1 revisions landed shortly after (`dependency_freeze.py` `03d04365…`, contract `c435239d…` at 20:32:51-03:00), while the three checker revisions above were re-measured unchanged at that later time. Re-run all three commands and re-measure the tool revisions against the delivered revision before citing these receipts.

Same-round adjacent change (recorded, not owned by this seat): `corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md:49` carries the declared carried-wording repair (the stale "new relation" sentence now names the tick-11 aftermath event as well); the data rows are byte-unchanged and the r95 receipts are unchanged by it (re-run this pass). The r95 and r96 knowledge notes gained append-only correction addenda this round for their stale tool-revision pins.

Path and line checks (python3, this pass): every path named in this record exists; the four inherited tables/notes are byte-identical between r97 and r98 (`cmp`); `r98 entities.json[:5] == r97 entities.json`, `r98 sources.json[:6] == r97 sources.json`, `r98 timeline.json[:6] == r97 timeline.json` → `True`; map rows J01-J17 identical modulo the namespace column (0 other diffs), J18-J20 the only new rows; census `ls -d corpus/fixtures/*/ | wc -l` = **172** (171 at the r97 closure). No other corpus file is claimed to have changed.

## Limits of this record

This is an author-seat knowledge note, not independent verification, admission, or a non-author review. It does not authenticate the fictional sources, does not adjudicate either character or the clerk, and does not extend to any record outside the cited paths. The r98 fixture is a declared continuation of `r97-crossing-acknowledgment`, itself a continuation of `r96-crossing-response`, `r95-crossing-aftermath`, `r94-paired-crossing`, and `r88-m3-maya-cluster`; source IDs remain cluster-local and path-qualified comparisons are not identity evidence. Rights and AI-training permission remain unassessed here.

## Dated correction (2026-10-17, round-98 closure, adjudication AC-3)

The "Tool revisions at these receipts" paragraph above records the round-98
tool revisions in flight as `dependency_freeze.py` `03d04365…`, contract
`c435239d…` (20:32:51 -03:00). The delivered r98 revisions are
`dependency_freeze.py` `03d04365…` and contract `153ebc5b…` (the contract
gained its final two pins and precedence text after that in-flight
measurement). Re-derive against the delivered revision before citing. The
historical paragraph is kept unrewritten; this correction supersedes its
contract pin only.
