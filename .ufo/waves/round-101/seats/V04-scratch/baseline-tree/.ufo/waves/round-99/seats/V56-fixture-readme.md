# V56 fixture-readme-review — round 99

Seat: V56 (verifier). Baseline: r98 closure `4265df5`. All commands ran from the lane root `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. Leaf seat: no nested agents, no commits, no pushes, no network. Writes: this report (absolute path) and `.ufo/waves/round-99/seats/V56-scratch/` (poll log, command receipts).

Axes for this seat: (1) command fidelity — every command in S4's README, as written; (2) count match — 6/1/8, 8 sources, 21 map obligations; (3) scope wording — window closed per the original minute, agreement unfulfilled, no claim lodged, matter stays open, no resolution/blame; (4) evidence — quote observed output, never verify a plan.

Scope: S4's two owned files, verified only after both the rewrite and `S4-fixture-docs.md` existed:

1. `corpus/fixtures/r99-window-lapse/README.md` — sha256 `b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049` (6,176 B)
2. `corpus/fixtures/r99-window-lapse/claim-excerpt-map.md` — sha256 `d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d` (17,119 B)

Both hashes match S4's report ("Owned and delivered") and were unchanged at the frozen re-run below.

## 0. Poll-wait record (protocol: 20 s cadence, 40 tries)

- Start: fixture directory already present as S3's r98 placeholder. README heading `# Round 98 clerk-filing continuation`, 5,829 B, sha256 prefix `32efc78f70e6`; map 15,028 B, prefix `c1099d0ee9ee`. No `S4*.md` report.
- Tries 1–3 (`V56-scratch/poll.log`): README and map unchanged; `S4-fixture-docs.md` absent. Not verified.
- Try 4: README and map changed (intermediate README 6,141 B, prefix `1c95ca05aab6`). Report still absent. Not treated as final.
- Try 5: `S4-fixture-docs.md` present; README 6,176 B `b93209417a918a88…`; map 17,119 B `d2fe20e581d1c29b…`. POLL_HIT. No stall-escape. No ABSENT condition.

Existence-only hazard, recorded not fatal: tries 1–3 were satisfied by S3's r98 byte copies of README and claim-excerpt-map (S3's own report says those two files were left as r98 copies on purpose). Verification started only after the r99 heading, the 6,176 B hash, and the producer report were all present.

## 1. Commands in S4's README, run as written

The README contains one `sh` fence and no other commands. Lines 23–29:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r99-window-lapse
python3 corpus/tools/support_check.py corpus/fixtures/r99-window-lapse
python3 corpus/tools/map_obligations.py corpus/fixtures/r99-window-lapse
```

Observed from the lane root, on the hashes above (stderr empty for all three; receipts in `V56-scratch/`):

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r99-window-lapse
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
stderr_bytes=0

$ python3 corpus/tools/support_check.py corpus/fixtures/r99-window-lapse
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23; DISTINCT-ANCHORS 19/19
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
PASS J01: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS J02: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS J03: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS J04: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS J05: source-support; mode=verbatim; anchor=found; 17:> The Chalk Stair is the named rain-dark crossing between Quiet Rise and Salt Court.
PASS J06: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS J07: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS J08: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS J09: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS J10: source-support; mode=verbatim; anchor=found; 18:> After both Tick 9 entries above, Aru and Evin met at the Chalk Stair at tick 10.
PASS J11: source-support; mode=verbatim; anchor=found; 19:> There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.
PASS J12: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS J13: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS J14: source-support; mode=verbatim; anchor=found; 20:> Their tick-10 decision depends on both ninth-bell entries: Aru's north-lantern entry at Quiet Rise and Evin's south-bell entry at Salt Court. After agreeing to share stewardship for this crossing only, they chalked one temporary route mark together at the midpoint.
PASS J15: source-support; mode=verbatim; anchor=found; 26:> Tick 11: I waited at the Chalk Stair through the agreed bell.
PASS J16: source-support; mode=verbatim; anchor=found; 37:> Tick 12: I was at Salt Court through the same agreed bell.
PASS J17: source-support; mode=verbatim; anchor=found; 48:> Tick 13: I received Evin's response at the Chalk Stair.
PASS J18: source-support; mode=verbatim; anchor=found; 60:> I am Maren, clerk of the Chalk Stair registry, and I record the matter OPEN.
PASS J19: source-support; mode=verbatim; anchor=found; 59:> Tick 14: I filed both pending accounts at the Chalk Stair registry.
PASS J20: source-support; mode=verbatim; anchor=found; 59:> Tick 14: I filed both pending accounts at the Chalk Stair registry.
PASS J21: source-support; mode=verbatim; anchor=found; 70:> Tick 15: The crossing-window named in the original minute has closed.
PASS S01: editorial-row; mode=verbatim; anchor=found; 5:> The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that event. […] He called out “Earth,” and the solid land appeared.
PASS S02: editorial-row; mode=verbatim; anchor=found; 5:> The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that event. […] He called out “Earth,” and the solid land appeared.
RECEIPT JSON-FACTS 21; EDITORIAL-ROWS 2; TOTAL-ROWS 23
SOURCE-SUPPORT 21/21; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 23/23; VALIDATED-ROWS 23/23
RESULT PASS
exit=0
stderr_bytes=0

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r99-window-lapse
OBLIGATIONS raw=21 mapped=21
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23
RESULT PASS
exit=0
stderr_bytes=0
```

Frozen re-run on the same two hashes reproduced exit 0/0/0, byte-identical stdout (`cmp` of the two runs), and empty stderr.

## 2. Counts check (README and map vs JSON and receipts)

`python3` `json.load` of the fixture:

```
entities=6 ['aru', 'evin', 'quiet-rise', 'salt-court', 'chalk-stair', 'clerk-maren']
relations=1
timeline=8
sources=8 ['veil-verse', 'paired-clock', 'crossing-minute', 'aru-aftermath-note', 'evin-response-note', 'aru-acknowledgment-note', 'clerk-filing-note', 'clerk-lapse-note']
contradictions=[]
entity_claims=6
```

Tick-15 row: `id=clerk-lapse-recorded`, `tick=15`, `entity_id=clerk-maren`, `place_id=chalk-stair`, `depends_on=["clerk-filing-open"]`, `source_id=clerk-lapse-note`. No new entity. `clerk-maren.first_appearance` remains `clerk-filing-note`.

| Claim | Declared | Observed | Verdict |
|---|---|---|---|
| README line 3 | 6 entities / 1 relation / 8 events / 8 sources | 6 / 1 / 8 / 8 | match |
| README line 3 inheritance | six entities, one relation, seven events, seven sources copied; added tick-15 event and its note | entities still 6; sources 7 inherited + `clerk-lapse-note`; events 7 inherited + `clerk-lapse-recorded` | match |
| README line 7 | added source `clerk-lapse-note`; no entity added; actor remains `clerk-maren`; added event `clerk-lapse-recorded` | same IDs in `sources.json` / `entities.json` / `timeline.json` | match |
| README line 9 | tick-15 ordered after and depends on `clerk-filing-open` | `timeline.json` last event `depends_on: ["clerk-filing-open"]` | match |
| README line 21 | 21 obligations = 20 inherited rows + `timeline.json#/7` | map rows J01–J21; J21 pointer `timeline.json#/7` | match |
| Map line 3 | six first-appearance, six claims, one relation, eight timeline events | 6+6+1+8 = 21 `| J` rows | match |
| Map line 5 | 21 JSON facts; 2 editorial; 23 total; 19 distinct anchors | support_check `21/21`, `2/2`, `23/23`, `19/19` | match |
| Map line 18 | new row anchored only in lines 66–76 | J21 span 66–76; support_check hit line 70, inside the span; file ends at line 76 | match |

Census 172→173 is not stated in the README and is not one of its commands. Not measured here.

## 3. Inherited-rows check (independent of S4's script)

Parsed `| J…` table rows in `r98-clerk-filing/claim-excerpt-map.md` and `r99-window-lapse/claim-excerpt-map.md`. Compared ID, pointer, in-world source ID, excerpt path, span, mode, and anchor. Namespace column excluded (intentional `r98-clerk-filing` → `r99-window-lapse`):

```
r98_rows=20 r99_rows=21
inherited_mismatches=0
line_numbers: J01–J20 at map lines 22–41 in both maps
new_rows=['J21'] at map line 42
table namespace cells containing r98-clerk-filing: 0
editorial S01/S02 rows: identical to r98 (2 rows)
```

J21: pointer `timeline.json#/7`, source `clerk-lapse-note`, namespace `r99-window-lapse:clerk-lapse-note`, span 66–76, anchor `Tick 15: The crossing-window named in the original minute has closed.` Every JSON-fact namespace cell is `r99-window-lapse:<source-id>` matching that row's in-world source ID. `r98-clerk-filing` remains only in the historical inherited-namespace sentence (map line 18) and the R9 declaration's inherited-namespace list (map line 11), which also names `r99-window-lapse:clerk-lapse-note`.

## 4. Scope-wording check

Excerpt lapse section (`fictional-excerpts.md` lines 66–76), quoted lines:

```
70:> Tick 15: The crossing-window named in the original minute has closed.
71:> The agreement was unfulfilled.
72:> No claim was lodged.
73:> The matter stands as a historical open entry.
74:> I record no resolution, assign no blame, and reconcile nothing.
76: Scope: … the matter stays open.
```

JSON description of `clerk-lapse-recorded`: "the clerk records that the crossing-window named in the original minute has closed; the agreement was unfulfilled; no claim was lodged; the matter stands as a historical open entry." `contradictions.json` is `[]`. `sources.json` `clerk-lapse-note` reliability note: "asserts no resolution, no blame, and no reconciliation; it is not evidence of a breach finding".

README and map against that record:

- README line 9 records only that the crossing-window named in the original minute has closed, and says the event does not resolve or create a contradiction, assign blame, or convert either account into a verdict. Matches the excerpt's line 70 and the empty contradictions file.
- README line 11 states the required bound: window closed per the original minute; agreement unfulfilled; no claim lodged; historical open entry; matter stays open; asserts no resolution, no blame, and no reconciliation; closes no one; assigns blame to neither; `contradictions.json` remains empty; no other duty; no breach finding; no continuing obligation. The negation half matches excerpt line 74 and the open-entry lines 73 and 76. "no breach finding" matches the lapse source's reliability note, not a positive breach.
- README line 15: lapse note does not re-present Maren's first appearance and asserts no office beyond the filing, no finding, and no resolution. Matches `first_appearance: clerk-filing-note` (unchanged) and excerpt line 74.
- README line 19: Spence remains a bounded external design prompt; rights and AI-training permission unassessed; neither granted. Editorial rows S01/S02 unchanged from r98.
- Map J21 paragraph names lines 71–74 by those exact sentences (unfulfilled agreement, no claim lodged, historical open entry, "I record no resolution, assign no blame, and reconcile nothing.") and states the matter stays open and the record creates no new duty. Span 66–76 is the whole appended section (file ends at 76).

Glosses, recorded, not contradictions of the negation bound:

- README line 11 says "the window closed per the original minute's terms"; the J21 paragraph says "closed per that minute's terms". Those two phrases are not in the excerpt. The excerpt says "named in the original minute has closed" (line 70). README line 9 uses that exact wording. The minute itself (lines 17–20) does not name a crossing-window or state closing terms. This is an editorial paraphrase of the note's "named in" claim, not a resolution or blame assertion.
- "so nothing is resolved" and "closes no one" (README line 11) are inferences in the same sentence that leads with "asserts no resolution, no blame, and no reconciliation". The excerpt's act is "I record no resolution, assign no blame", plus the open entry. They do not assert a finding, a verdict, or blame.

No positive resolution, blame, verdict, or canon-truth assertion found in the README lapse bound or the J21 paragraph.

## 5. Cross-checks

- S4's declared hashes and receipts (check_bible CLEAN exit 0; support_check 21/21 PASS exit 0; map_obligations raw=21 mapped=21 PASS exit 0) match this seat's runs.
- Nit (S4 report wording, not the deliverable): S4 says README lines 25–29 are the three replay commands. The commands are on lines 26–28; line 25 opens the fence and line 29 closes it. The commands themselves are exactly the three that were run.
- S3's report says README and the map still say r98 (20 obligations, 6/1/7). That was true at poll tries 1–3 (placeholder hashes `32efc78f70e6` / `c1099d0ee9ee`) and is stale for the delivered tree. S4 records the same. Not a defect in the delivered README or map.
- Bounds of these receipts: the three tools are lexical preflight and pointer-to-row mapping, not whole-claim entailment, source authentication, chronology truth, rights, or canon. Census and freeze pinning are outside this seat. This seat wrote only this report and `V56-scratch/`.

## Bottom line

**PASS** — every command in S4's README runs as written on the delivered bytes with exit 0 (check_bible CLEAN; support_check 21/21, 2/2, 23/23, 19/19 anchors PASS; map_obligations raw=21 mapped=21 PASS; stderr empty; frozen re-run identical), counts 6/1/8 plus 8 sources and 21 obligations (20 inherited rows unchanged modulo namespace + J21 `timeline.json#/7`) match the JSON and the receipts, and the scope wording (window closed per the original minute, agreement unfulfilled, no claim lodged, matter stays open, no resolution/blame) is present and consistent with excerpt lines 70–76 and the empty contradictions file; hashes stable at verification and at the re-run (README `b9320941…`, map `d2fe20e5…`), S4 report present at poll try 5.
