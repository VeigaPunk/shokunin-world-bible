# V14 — c2-whole-claim (round 99)

Seat: V14 `c2-whole-claim`. Manual whole-proposition review of the lapse note. Axes: (1) every proposition traces to an excerpt clause and a JSON row; (2) resolution, blame, reconciliation, and new-duty are not constructible; (3) “the matter stands open” is the clerk’s record, not a world-state; (4) description fields stay scoped to that record.

Baseline: r98 closure `4265df5`. Lane root `/home/vgpnk/Projects/shokunin/lore-shokunin`. Commands with `python3` from that root. Leaf seat: no nested agents, no commits, no pushes, no network. Only write: this report. `corpus/knowledge/r99-lapse-scope-note.md` was absent at review time and is not in this seat’s poll set; it was not used.

## Poll record (observed; not a fabricated 40-try loop)

Artifacts and both producer reports were required. Placeholder r98 copies were not reviewed.

| When (local) | Observation |
|---|---|
| seat start | `corpus/fixtures/r99-window-lapse/` absent; `.ufo/waves/round-99/` absent |
| 22:01:10 | directory present as r98-sized copies (README 5829, map 15028, excerpts 4187, mtimes 21:36). S3/S4 reports absent |
| next check | `fictional-excerpts.md` 5114, `sources.json` 3293, `timeline.json` 2998. README/map still byte-identical to r98. `S3-fixture-author.md` present (5069 bytes). S4 report absent. S4 `poll.log`: `22:01:09 try=1 dir-present content-not-ready` then `22:01:29 POLL_HIT` with `S3_REPORT=absent` |
| 22:03:05 | map rewritten (17119, sha256 `d2fe20e5…`). README mid-edit (6141, sha256 `1c95ca05…`). S4 report still absent |
| 22:05:46 | README at the delivered hash below (6176). S4 report present |
| 22:17:09 and 22:29:03 | ten fixture hashes unchanged; README and map match S4’s reported hashes |

No ABSENT. No stall-escape. Review below is of the bytes at the 22:29:03 freeze, not of a plan.

## Frozen sha256 (22:29:03 -03:00)

```
b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049  README.md                 6176
d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d  claim-excerpt-map.md     17119
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  contradictions.json          3
db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984  entities.json             1793
fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d  fictional-excerpts.md     5114
58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37  inspiration-note.md       1956
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  relations.json             139
b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd  source-excerpt.md          640
8c215b38dc02400910ff935eab46ecf82b0381b63a75d092b03bd601a9915f15  sources.json              3293
2cdb9fda5baae1a496b31c004a7e0a9345ac580b257da0d9a04c045214c4c069  timeline.json             2998
```

README and map hashes equal `S4-fixture-docs.md` exactly. S3 reported the three edited sizes (sources 3293, timeline 2998, excerpts 5114) and did not publish sha256s; the sizes match.

Inheritance vs `git show 4265df5:corpus/fixtures/r98-clerk-filing/<f>`: `entities.json`, `relations.json`, `contradictions.json`, `inspiration-note.md`, `source-excerpt.md` byte-identical. `sources.json[:-1]` and `timeline.json[:-1]` parsed-equal to the r98 arrays. `fictional-excerpts.md` startswith the r98 bytes plus a newline (`True`; r98 4187 is a prefix of 5114). Counts: 6 entities / 1 relation / 8 events / 8 sources / 0 contradictions. No new entity, claim, or relation. New rows: `sources.json#/7` `clerk-lapse-note`; `timeline.json#/7` `clerk-lapse-recorded`, tick 15, `entity_id` `clerk-maren`, `place_id` `chalk-stair`, `depends_on` `["clerk-filing-open"]`, `source_id` `clerk-lapse-note`.

## Quoted lapse note (the record under review)

`fictional-excerpts.md:66-76`. Five quoted lines, matching the attribution “folio 9, lines 1–5”:

```
70:> Tick 15: The crossing-window named in the original minute has closed.
71:> The agreement was unfulfilled.
72:> No claim was lodged.
73:> The matter stands as a historical open entry.
74:> I record no resolution, assign no blame, and reconcile nothing.
76: Scope: … It records that the crossing-window named in the original minute has closed, that the agreement was unfulfilled, that no claim was lodged, and that the matter stands as a historical open entry. It asserts no resolution, no blame, and no reconciliation, and it creates no new duty; … and the matter stays open.
```

The original minute (`fictional-excerpts.md:17-20`, source `crossing-minute`) contains none of: `window`, `crossing-window`, `terms`, `closed`, `unfulfilled`, `claim`, `open`, `blame`, `resolution`, `duty`. It names “the Chalk Stair” and “this crossing only”.

## Axis 2 holds on the quoted note

No resolution, blame, reconciliation, or new duty is constructible from lines 70-76 without contradicting the note.

- Resolution: line 74 “I record no resolution”; line 76 “asserts no resolution”. “has closed” (line 70) is the crossing-window, and line 73 keeps the matter an open entry. Equating window-close with matter-resolution contradicts 73-74.
- Blame: line 74 “assign no blame”. “unfulfilled” (line 71) is a status of the agreement. It names no party and does not attribute fault.
- Reconciliation: line 74 “reconcile nothing”; line 76 “no reconciliation”. No positive reconciliation sentence.
- New duty: the five quoted lines contain no duty/obligation wording. Line 76 denies “creates no new duty”. Nothing in 70-74 states a duty to cure, lodge, or continue performance.

Risk hits in the new excerpt section are only lines 70, 71, 73, 74, 76. Inherited hits (lines 29-64) are the prior beats’ negations, unchanged.

`sources.json#/7.reliability_note` keeps the same four content clauses under “the clerk reports that” and then denies resolution, blame, and reconciliation. It does not assert a breach; it says “not evidence of a breach finding” (narrower than the inherited notes’ “not evidence of a breach” — observation O5, not a constructed breach).

## Axis 1 / 3 / 4 — trace, then the failures

| ID | Proposition | Excerpt clause | JSON row | Trace |
|---|---|---|---|---|
| Q1 | Tick 15; window named in the original minute has closed | line 70 | `timeline.json#/7.tick=15`; description clause 1 and `reliability_note` under the clerk’s report | traced as the clerk’s sentence. “window” is the clerk’s term, not a minute token (O1) |
| Q2 | The agreement was unfulfilled | line 71 | `reliability_note` (“the clerk reports … that the agreement was unfulfilled”) | excerpt + reliability note traced. Description clause 2 is not under “records” (F1) |
| Q3 | No claim was lodged | line 72 | `reliability_note` (“that no claim was lodged”) | same split as Q2. No new `entities.json` claim; the sentence is institutional, not a JSON claim row |
| Q4 | The matter stands as a historical open entry | line 73, inside the note attributed at line 68 to `clerk-lapse-note` | `reliability_note` (“and that the matter stands as a historical open entry”) | the quoted sentence is the clerk’s record. Description clause 4 is not (F1) |
| Q5 | I record no resolution, assign no blame, and reconcile nothing | line 74 | `reliability_note` (“It asserts no resolution, no blame, and no reconciliation”) | traced to excerpt + reliability note. Absent from `timeline.json#/7.description` |
| P1 | creates no new duty; matter stays open | line 76 scope paratext, not a quoted line | not in the description; map:69 restates both | editorial denial / paraphrase of Q4+Q5. Not a new duty. Not the clerk’s words |
| R-terms | “the window closed per the original minute's terms” | absent from 17-20 and 66-76 | absent from both new JSON rows | untraceable (F2). README:11 calls it “explicit in the record” |
| M-terms | “has closed per that minute's terms”, attributed to the clerk | absent | absent | untraceable (F2). map:69 |
| R-world | “so nothing is resolved” | absent. Line 74 is “I record no resolution”, a speech-act | absent | not the clerk’s record (F3) |
| R-only | tick-15 event “records only” the window closing | contradicted by lines 71-74 | description also carries unfulfilled / no-claim / open-entry clauses | false completeness (F4) |

### F1 — description field is not scoped (axes 3 and 4)

`timeline.json#/7.description`:

```
At the Chalk Stair at tick 15, the clerk records that the crossing-window named in the original minute has closed; the agreement was unfulfilled; no claim was lodged; the matter stands as a historical open entry.
```

Semicolon split (observed):

```
1 HAS_RECORDS :: At the Chalk Stair at tick 15, the clerk records that the crossing-window named in the original minute has closed
2 NO_RECORDS :: the agreement was unfulfilled
3 NO_RECORDS :: no claim was lodged
4 NO_RECORDS :: the matter stands as a historical open entry.
```

Clauses 2-4 are independent clauses. “the matter stands as a historical open entry” is not grammatically the clerk’s record in this field. The reliability note shows the scoped form was available (“the clerk reports that …, that …, that …, and that the matter stands as a historical open entry”) and was not used here. The description also drops line 74’s denials, so the unscoped clauses are not paired with “I record no resolution” inside the same field.

This is the failure the seat asked for: the open-matter claim in the event description is not kept as the clerk’s record.

### F2 — “minute’s terms” is not in the excerpt or the JSON (axis 1)

README:11: “The lapse bound is explicit in the record: the window closed per the original minute's terms”.

map:69: “the clerk records that the crossing-window named in the original minute has closed per that minute's terms”.

Phrase search on the frozen files: “per the original minute's terms” hits only README; “per that minute's terms” hits only the map. Neither phrase is in `fictional-excerpts.md`, `timeline.json`, or `sources.json`. The minute has no “terms” and no closing rule. “for this crossing only” (line 19) is not a closing term. Attributing the extra phrase to the clerk (map:69) or calling it explicit in the record (README:11) is an out-claim.

### F3 — “so nothing is resolved” is an editorial world-state (axis 3)

README:11: “The lapse note asserts no resolution, no blame, and no reconciliation, so nothing is resolved”.

“I record no resolution” (line 74) is the clerk refusing to record a resolution. “nothing is resolved” is a concluded world-fact. It is not in the excerpt or either JSON row. It does not construct a resolving act (axis 2 still holds), but it does take the open/unresolved status out of the clerk’s record.

### F4 — README:9 “records only” contradicts the note (axis 1)

README:9: the tick-15 event “records only that the crossing-window named in the original minute has closed.”

Lines 71-74 and the description’s later clauses are further recorded content. “Only” is false. Line 11 then restates the missing clauses, but adds F2 and F3 while doing so. Map:55’s “encodes only that …” list does include unfulfilled / no-claim / open-entry and does not use the “minute’s terms” phrase; that sentence is the scoped reading. Map:69 then puts the terms phrase back in.

## What the lexical gates do not prove

Tools at the 22:29 freeze:

```
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  corpus/tools/support_check.py
86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9  corpus/tools/map_obligations.py
```

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r99-window-lapse
CLEAN: schema, citations, relations, timeline; 0 violations
bible_exit:0

$ python3 corpus/tools/support_check.py corpus/fixtures/r99-window-lapse
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23; DISTINCT-ANCHORS 19/19
PASS J21: source-support; mode=verbatim; anchor=found; 70:> Tick 15: The crossing-window named in the original minute has closed.
SOURCE-SUPPORT 21/21; … VALIDATED-ROWS 23/23
RESULT PASS
support_exit:0

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r99-window-lapse
OBLIGATIONS raw=21 mapped=21
RESULT PASS
map_exit:0
```

`support_check` matches the J21 anchor (line 70) inside span 66-76. It does not read clauses 71-74, the description’s semicolon scope, or the “minute’s terms” gloss. A lexical PASS is not a whole-proposition pass. S4’s report says the same bound and asks a verifier to re-read the J21 paragraph against lines 66-76. That re-read is F2.

## Observations (not the FAIL grounds)

- O1. “crossing-window named in the original minute” is the clerk’s characterization (line 70). The minute does not contain “window”. Scoped where the JSON says the clerk reports/records it. Not an independent fact that the minute text uses that name.
- O2. Description opens “At the Chalk Stair”. Lines 70-74 do not name the place. `place_id: chalk-stair` is the declared schema slot. The prose location is an inference from minute line 17, not a lapse-excerpt clause.
- O3. “I” appears only on line 74. Actor `clerk-maren` traces through line 68, the source title “Maren's Chalk Stair Lapse Note”, and the inherited entity. This section does not re-state “I am Maren”.
- O4. `depends_on: ["clerk-filing-open"]` is not in the lapse sentences. Map:55 calls the chain’s edges “editorial encodings of the excerpts' explicit tick/order/dependence wording”. The lapse note has a tick label and no dependence clause. Same precision note as prior rounds; the same paragraph also says the edges are not literal JSON.
- O5. New reliability note and README:11 deny a “breach finding”, not a breach. “unfulfilled” is not a breach sentence. Breach is not one of this seat’s four banned constructs. No positive breach is asserted.
- O6. “closes no one” (README:11, map:55, map:69) is not a quoted clause. It is a negation paraphrase of line 74, not a positive close.

## Producer cross-check

- S3: three-file edit, seven files byte-identical to `4265df5` r98, `check_bible` CLEAN, no new entity/claim/relation. Reproduced. S3’s note that README/map still said r98 was true at S3 report time and is stale now (S4 rewrote both). Not a defect of the delivered tree.
- S4: reported README `b9320941…` and map `d2fe20e5…` match the freeze. Gate receipts (CLEAN, 21/21, raw=21 mapped=21) reproduced on those bytes. S4’s own J21 reading adds “per that minute's terms” (F2). S4’s bottom-line PASS is not adopted; the lexical gates do not cover F1-F3.

## Bottom line

FAIL — the quoted lapse note does not construct resolution, blame, reconciliation, or a new duty, and line 73 is the clerk’s sentence, but `timeline.json#/7.description` states “the matter stands as a historical open entry” as its own clause after the semicolon, and README:11 / map:69 add “closed per the minute’s terms” and “so nothing is resolved”, which are in neither the excerpt nor the JSON rows.
