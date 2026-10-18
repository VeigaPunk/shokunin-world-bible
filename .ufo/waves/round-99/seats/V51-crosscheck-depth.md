# V51 — crosscheck-depth (round 99)

Seat: V51 `verdict-crosscheck-depth`. Scope: **independent depth verdict; compare V29**. This is my own derivation from delivered bytes and my own commands, not a restatement of the producers' reports. The V29 comparison is in §5. At the first write (22:41) the V29 report was still absent; it landed at 22:33:40 and was read after that write. §5 and the addendum record the comparison against `V29-verdict-depth.md` sha256 `1f8eb8316b844dd64cd832561976dfddbd98c2674778a2d2fef8d5eb156b5e1e`.

Lane repo: `/home/vgpnk/Projects/shokunin/lore-shokunin`. Every command below ran from that root with `python3`. Every path I wrote is absolute under it. The only writes are this report and `.ufo/waves/round-99/seats/V51-scratch/`. Baseline r98 closure `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`). Working-tree HEAD at start was `337f0fa` (the blocked-dispatch log commit; no corpus increment). No commits, no pushes, no network, no nested agents.

Scratch (mine): `V51-scratch/{poll.sh, poll.log, poll-start.txt, depth-check.py, depth-check-run1.txt, census.py, census-run1.txt, scope-scan.py, scope-scan-run1.txt, anchor-check.txt, locative-terms.txt, v29-probe-replay.txt, probes/, r98-baseline-hashes.txt, r99-hashes-early.txt, r99-hashes-post-s4.txt, r99-hashes-final.txt, tool-hashes-early.txt, tool-hashes-run1.txt, tool-hashes-final.txt, check-bible-midflight.txt, check-bible-final.txt, mapobl-midflight.txt, mapobl-final.txt, support-midflight.txt, support-final.txt, final-clock.txt}`.

## 1. Method and poll record

- Pre-registered checks before treating the fixture as delivered: r98 baseline hashes captured 22:02:35 (`r98-baseline-hashes.txt`); own `depth-check.py` (preservation, counts, chain, map-row namespace diff, obligation arithmetic); three gates; own census over every fixture dir.
- Poll-wait: `V51-scratch/poll.sh`, 20 s cadence, gated on a content marker (map sha no longer the r98 placeholder `c1099d0ee9ee`), both knowledge notes, and reports `S3`/`S4`/`S5`/`V29`. Launched 22:03:16. Logged tries 0–29. The background runner was killed by a 600 s tool cap after try 29 (22:12:57); it did not write `POLL-EXHAUSTED`. **Stall-escape, recorded, not fatal:** wall clock from try 0 (22:03:16) to the final presence check (22:33:06) exceeds the 40×20 s budget (try 39 would have been ~22:16:36). Manual checks at 22:19:34, 22:22:22, 22:29:35, and 22:33:06 all still show the same absences. I did not verify a plan and did not fabricate a V29 verdict from `V29-scratch/`.
- Observed landings (lane clock, -03:00): r99 dir already present at first look (22:01:29) as an r98 byte copy plus S3's three edits (`timeline.json` / `sources.json` / `fictional-excerpts.md` mtime 22:01:13). S3 report `S3-fixture-author.md` present at 22:01. Map rewritten 22:02:39 (`d2fe20e5…`). README rewritten 22:03:19 (`b9320941…`). S4 report visible to the poll at 22:03:56 (`S4-fixture-docs.md`).
- **Placeholder hazard (recorded, not a defect of the delivered revision).** At 22:02:35, `claim-excerpt-map.md` and `README.md` were still byte-identical to r98 (`c1099d0ee9ee…` / `32efc78f70e6…`). An existence-only poll is satisfied by that copy. My receipts below are content-gated and hash-pinned.
- **ABSENT at the final check (22:33:06), after the poll budget:**
  - `corpus/knowledge/r99-gate-blind-spot-table.md` — no file anywhere under `/home/vgpnk/Projects/shokunin` (`Glob **/r99-gate-blind-spot-table.md` → no matches)
  - `corpus/knowledge/r99-lapse-scope-note.md`
  - `.ufo/waves/round-99/seats/S5-*.md` (no `S5-scratch/` either)
  - `.ufo/waves/round-99/seats/V29-*.md` (scratch existed and was being written; the report file did not)
  - S1 and S2 reports also absent. Not my gate. Noted only because `dependency_freeze.py` / the contract moved during the round (see bound 8). I did not adjudicate C1.
- Final fixture revision, stable `r99-hashes-post-s4.txt` (22:03:31) == `r99-hashes-final.txt` (22:22:22) == re-diff at 22:33:06 (`FIXTURE_STABLE`):

```
d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d  claim-excerpt-map.md
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  contradictions.json
db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984  entities.json
fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d  fictional-excerpts.md
58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37  inspiration-note.md
b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049  README.md
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  relations.json
b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd  source-excerpt.md
8c215b38dc02400910ff935eab46ecf82b0381b63a75d092b03bd601a9915f15  sources.json
2cdb9fda5baae1a496b31c004a7e0a9345ac580b257da0d9a04c045214c4c069  timeline.json
```

## 2. Independent findings — C2 component 1 (fixture)

**F1 — preservation and extension of `r99-window-lapse` (PASS).** Own script `depth-check.py` (run1, exit 0; `FAILS: none`), on the bytes that remained the final revision:

```
OK byte-identical contradictions.json | r98=37517e5f3dc66819 r99=37517e5f3dc66819
OK byte-identical entities.json       | r98=db2d8e5d3866009b r99=db2d8e5d3866009b
OK byte-identical inspiration-note.md | r98=58f5390e5928ebad r99=58f5390e5928ebad
OK byte-identical relations.json      | r98=c279254bc7de0636 r99=c279254bc7de0636
OK byte-identical source-excerpt.md   | r98=b5edc2fd3c2e3d4f r99=b5edc2fd3c2e3d4f
OK entities 6->6 | 6->6      OK relations 1 | 1|1
OK timeline 7->8 | 7->8      OK sources 7->8 | 7->8
OK contradictions [] | []|[] OK claims 6 | 6|6
OK entities parsed-equal     OK relations parsed-equal
OK sources[:7] parsed-equal  OK timeline[:7] parsed-equal
OK r98 excerpts is byte-prefix of r99 | r98=4187B r99=5114B delta=927B
OK obligation arithmetic == 21 | 6 fa + 6 claims + 1 rel + 8 ev = 21
```

New source (`sources.json` last object): id `clerk-lapse-note`, title `Maren's Chalk Stair Lapse Note`, kind `fictional first-person note`. Reliability note contains, verbatim, "the crossing-window named in the original minute has closed", "the agreement was unfulfilled", "no claim was lodged", "historical open entry", "no resolution", "no blame", "no reconciliation".

New event (`timeline.json` last object):

```
id clerk-lapse-recorded
tick 15
entity_id clerk-maren
place_id chalk-stair
depends_on ["clerk-filing-open"]
source_id clerk-lapse-note
description: "At the Chalk Stair at tick 15, the clerk records that the crossing-window named in the original minute has closed; the agreement was unfulfilled; no claim was lodged; the matter stands as a historical open entry."
```

Dependency chain (own parse): ticks `[9, 9, 10, 11, 12, 13, 14, 15]` nondecreasing; 7 edges, all strictly earlier, including `clerk-lapse-recorded -> clerk-filing-open` (exists=True, strictly-earlier=True). No new entity, claim, or relation.

Appended excerpt (byte tail after the r98 prefix), lines 66–76:

```
## Round 99 lapse note (2026-10-17)
> Tick 15: The crossing-window named in the original minute has closed.
> The agreement was unfulfilled.
> No claim was lodged.
> The matter stands as a historical open entry.
> I record no resolution, assign no blame, and reconcile nothing.
```

Scope sentence on line 76: "It asserts no resolution, no blame, and no reconciliation, and it creates no new duty; the crossing-scoped agreement above is unchanged, and the matter stays open."

**F2 — map completeness and inherited-row discipline (PASS).** Own column parse (`depth-check.py`): r99 map `d2fe20e5…` declares "21 JSON facts; 2 editorial rows; 23 total mapped rows; 19 distinct excerpt anchors"; row ids J01–J21 + S01/S02. Inherited rows present 22/22 (J01–J20 + S01/S02); **namespace-only diffs = 20; other diffs = 0**. New row exactly:

```
J21 | timeline.json#/7 (tick, entity_id, place_id, depends_on, description, source_id)
    | clerk-lapse-note | r99-window-lapse:clerk-lapse-note
    | fictional-excerpts.md | span 66-76 | verbatim
    | anchor `Tick 15: The crossing-window named in the original minute has closed.`
```

Own anchor check (`anchor-check.txt`): all 21 JSON rows, anchor string found inside the declared span, `FAILS 0`. J21's only hit is line 70, inside 66–76, not inside any inherited span.

**F3 — gates on the hash-pinned revision (PASS).** Tools byte-equal to `4265df5` (`git diff --stat` empty at 22:33:06): `check_bible.py` `ff9fd2aa…`, `map_obligations.py` `86b52949…`, `support_check.py` `55a5eb27…`.

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r99-window-lapse
CLEAN: schema, citations, relations, timeline; 0 violations     exit=0

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r99-window-lapse
OBLIGATIONS raw=21 mapped=21
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23
RESULT PASS                                                     exit=0

$ python3 corpus/tools/support_check.py corpus/fixtures/r99-window-lapse
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23; DISTINCT-ANCHORS 19/19
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
PASS J21: source-support; mode=verbatim; anchor=found; 70:> Tick 15: The crossing-window named in the original minute has closed.
RECEIPT JSON-FACTS 21; EDITORIAL-ROWS 2; TOTAL-ROWS 23
SOURCE-SUPPORT 21/21; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors);
MODES 23/23; VALIDATED-ROWS 23/23
RESULT PASS                                                     exit=0
```

Final gate run 22:22:22; hashes unchanged at 22:33:06. An earlier mid-flight run (22:02:4x) already saw the post-S4 map (`raw=21 mapped=21`); I do not treat the pre-S4 placeholder as a delivered receipt. I did not capture a pre-S4 `map_obligations` of my own; S3's report predicts `missing` the 21st row while the map was still the r98 copy. That is a mid-flight state, not a defect of the pinned revision.

**F4 — census and non-harm (PASS for the fixture increment).**

```
$ git ls-tree -d --name-only 4265df5:corpus/fixtures | wc -l
172
$ ls -d corpus/fixtures/*/ | wc -l
173
```

Own census (`census.py`, exit 0), repo-relative `check_bible` over every fixture dir, violation lines = lines containing `VIOLATION`:

```
{"fixture_dirs": 173, "clean_exit0": 39, "negative_exit1": 134, "violation_lines": 421, "non_0_1_exits": []}
```

r98 closure LOG records 172/38/134/421. This is one clean increment; negatives and violation-line count unchanged. `git diff --stat 4265df5 -- corpus/fixtures/check_bible.py corpus/tools/map_obligations.py corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing` empty at 22:33:06. r97 fixture not in that diff either (checked earlier the same way). I did not re-census after 22:04; dir count was still 173 at 22:33:06 and the fixture hash set had not moved, so the increment is still the one r99 directory.

**F5 — adversarial scope review, my own (PASS, bounded).** From the delivered bytes I tried to construct:

- a resolution — blocked by excerpt line 74 "I record no resolution, assign no blame, and reconcile nothing.", the reliability note "It asserts no resolution, no blame, and no reconciliation", README line 11 "nothing is resolved", and map line 69 "it asserts no resolution, no blame, and no reconciliation".
- blame — blocked by line 74 "assign no blame" and the reliability note. "The agreement was unfulfilled." (line 71) is a positive non-performance record, not a blame or breach finding; the reliability note says "not evidence of a breach finding".
- reconciliation / a winner — blocked by line 74 "reconcile nothing" and the inherited empty `contradictions.json` (byte-identical to r98). The two accounts still name different actors at different places.
- a closed matter — blocked by line 73 "historical open entry" and line 76 "the matter stays open". "Window closed" and "matter stays open" are different objects (the crossing occasion vs the registry entry). `contradictions.json` stays `[]`.
- a new duty — blocked by line 76 "creates no new duty" and the inherited crossing-only relation (byte-identical `relations.json`).
- a new person or a new claim — entities and claims parsed-equal to r98; actor is the existing `clerk-maren`.

**Lexical bound, not a structural fail:** the token `window` occurs 0 times in the r98 excerpt and 0 times in the r99 inherited prefix. The original minute (lines 17–20) says "for this crossing only"; the aftermath (line 26) says "through the agreed bell". Neither names a "window". The lapse note's "crossing-window named in the original minute" is the clerk's characterization, anchored by `support_check` to the lapse note itself (line 70), not a quotation of a window-name in the minute. "Closes no one" is README/map editorial framing (README line 11; map lines 55 and 69), not a sentence in the quoted note.

## 3. C2 component 2 — ABSENT

Declared deliverable: `corpus/knowledge/r99-gate-blind-spot-table.md` (plus S5's `corpus/knowledge/r99-lapse-scope-note.md`). Neither file existed at 22:33:06. No S5 report. I did not invent rows, did not replay a table that was not written, and did not treat prior-round debt notes as this round's table.

The declaration's row classes (emptied `depends_on`; wrong-but-earlier edge; deleted terminal row; F15 `support_check`-silent mutants; dependency-wording removal, historical invisibility plus the C1 close; consistent-regeneration bound; checker frozen-pin status) are therefore **unverified this seat**. Component 2 is not a depth pass and not a depth fail. It is absent.

## 4. Independent depth verdict (partial)

**DEPTH — IMPROVED (bounded) on component 1 only.** On the hash-pinned fixture the crossing arc gains a fifth beat: a clerk lapse record. Before (r98, `4265df5`): 6 entities / 1 relation / 7 events / 7 sources / 20 map obligations. After: 6/1/8, 8 sources, 21 map obligations (20 inherited JSON rows carried unchanged modulo the namespace cell + J21), tick-15 event dependency-linked to the tick-14 filing, `check_bible` CLEAN exit 0, `map_obligations raw=21 mapped=21` PASS exit 0, `support_check` 21/21 + 2/2 + 23/23 PASS exit 0, census 172→173 (39/134/421, one clean increment), empty contradiction ledger, no new entity/claim/relation. No harm observed in the depth tools or the r98 fixture.

**The full C2 depth claim is not closed.** Component 2 was not delivered inside the poll budget. I do not promote component 1's pass into an admission of C2.

Named bounds:

1. Structural/lexical evidence plus hand scope review only. No testimony truth, canon, chronology, rights, or identity claim. The three gate receipts are preflight, not entailment.
2. "Lapse record that closes no one" is an authored class label. "Closes no one" is not a quoted sentence in the note. The note's own bounds are line 74 and the reliability note.
3. "Crossing-window named in the original minute" is the clerk's characterization. The minute excerpt does not contain the word `window` (F5). Tick `15`, event id, and the `depends_on` edge are editorial encodings. Two further prose gaps, confirmed after V29 named them (`locative-terms.txt`): the description's "At the Chalk Stair" is not in lapse lines 66–76 (`section_has_Chalk_Stair False`), and README line 11's "per the original minute's terms" is not in the note (the note says "named in the original minute has closed"). Support gaps, not blame.
4. "Unfulfilled" is a non-performance record, explicitly not a breach finding and not blame. It does not select a winner and does not fill `contradictions.json`.
5. Checker blind spots are carried, not re-demonstrated here. `check_bible` still cannot see an emptied `depends_on`, a wrong-but-earlier edge, or a deleted terminal row. The tick-15 edge is verified as bytes + map row + prose, not by a rule. That is exactly the class component 2 was supposed to table, and that table is absent.
6. Preservation is four-level, not map-file byte equality: byte (5 copies), parsed equality (entities, relations), parsed prefix (sources, timeline), strict byte-prefix (excerpts, +927 B), column equality modulo namespace (20 inherited JSON rows; S01/S02 identical).
7. Placeholder hazard (§1). All quoted receipts are on the hash-pinned post-S4 revision, stable 22:03:31–22:33:06.
8. Tool-revision flux outside this verdict: at 22:29 `dependency_freeze.py` was `6f81f8be…` and the contract `8c2561b0…` (baseline contract at round start was `153ebc5b…`). Depth receipts do not depend on those files. C1 was not adjudicated. S1/S2 reports were absent.
9. Census script ran once (~22:04), before the freeze files moved. Dir count rechecked 173 at 22:33:06. I did not re-walk all 173 checkers at the final minute; the r98 tools and r98 fixture were still byte-unchanged vs `4265df5`.

## 5. Crosscheck vs V29

Read `.ufo/waves/round-99/seats/V29-verdict-depth.md` after the first write (file mtime 22:33:40, sha256 `1f8eb831…`, 18,341 B). It was absent at my 22:33:06 presence check and present by 22:47. V29's verdict: **DEPTH — UNPROVEN as a whole**; bottom line **INCONCLUSIVE**. Component 1 verifies on the delivered bytes; component 2 ABSENT; the one depth axis-move is not established. That is the same call as mine, with a stricter single headline (UNPROVEN) where I split "improved on component 1 / not closed as a whole."

| Check | V29 | V51 (me) | Agreement |
|---|---|---|---|
| before→after | 6/1/7, 7 sources, 20 obligations → 6/1/8, 8 sources, 21 | same | yes |
| 10-file sha256 | `d2fe20e5…` / `b9320941…` / `fefebaf9…` / `8c215b38…` / `2cdb9fda…` and the five unextended copies | same set, re-diff stable 22:03:31–22:33:06 | yes |
| `check_bible` | CLEAN exit 0 @`ff9fd2aa` | same | yes |
| `map_obligations` | `raw=21 mapped=21` PASS @`86b52949` | same | yes |
| `support_check` | 21/21, 23/23, J21 at line 70, PASS | same | yes |
| census | 173/39/134/421; dirs 172→173; clean 38→39 inferred | same; I also did not re-census the `4265df5` tree | yes |
| inheritance | 5 byte copies; parsed prefix; excerpts +927 B; 22 inherited rows modulo namespace | same (20 JSON rows namespace-only, S01/S02 identical) | yes |
| J21 | `timeline.json#/7`, span 66–76, anchor line 70 | same; own anchor check `FAILS 0` | yes |
| component 2 | ABSENT at 22:30:31 (no table, no scope note, no S5) | ABSENT at 22:50:35, same three paths | yes |
| pre-S4 map | `raw=21 mapped=20` / `missing_obligation: timeline.json#/7` / FAIL exit 1 | not captured live; reproduced in scratch after reading V29 (below) | yes, after replay |
| window token | "named in the original minute" is the note's wording, not an external minute | independently: `window` count in r98 excerpt and r99 inherited prefix = 0 | yes |
| locative gap | description "At the Chalk Stair…" not in lines 66–76 | confirmed after V29 named it: `section_has_Chalk_Stair False`; description has the phrase | yes |
| "per the terms" gloss | README:11 / map:69 stronger than the note | confirmed: README line 11 says "per the original minute's terms"; lapse section has neither `terms` nor `per the` | yes |
| checker blind spots on the new edge | P5/P8/P9 CLEAN; P1 and P3 exit 1 | reproduced in scratch after reading V29 (below); live fixture hash unchanged | yes |

**No material divergence** on the delivered bytes, the component-2 absence, or the refusal to close the axis-move. Differences are scope and timing, not disagreement:

- V29 captured the pre-S4 `missing_obligation` live (22:02:12). I only had S3's prediction until I reproduced it in scratch. J21 is load-bearing. I agree.
- V29 additionally read other C2 seats (V10, V11, V12, V13, V41, V47, V77, V80, V86, V105, V109, V119) and records V105's FAIL. I did not adopt those bottoms. After V29 named the two prose gaps, I checked them myself (`V51-scratch/locative-terms.txt`) and they hold. They bound how far the description and README may be quoted as the note. They are not resolution or blame, and they do not make the fifth beat false.
- V29's poll exhausted cleanly at 22:15:12 (40 tries). Mine was killed by a 600 s tool cap at try 29 (22:12:57); a later manual check covered the rest of the budget. Same absences.
- Headline wording: V29 "UNPROVEN as a whole" vs my "IMPROVED (bounded) on component 1 only, full C2 not closed." Same substance. I do not treat component 1's pass as an admission of C2.

Scratch replays after reading V29, live fixture not written (`timeline.json` still `2cdb9fda…`, map still `d2fe20e5…`):

```
PRE-S4 map_obligations (r98 map copied over the r99 map, scratch only)
OBLIGATIONS raw=21 mapped=20
FINDING missing_obligation: timeline.json#/7 has no map row
RESULT FAIL                                          exit=1

P5-emptied depends_on=[]           bible exit=0 CLEAN
P8-wrong-but-earlier               bible exit=0 CLEAN
P9-delete-terminal                 bible exit=0 CLEAN
P1-drop-key                        bible exit=1 VIOLATION: timeline[7].depends_on: required nonempty list
P3-same-tick (tick 15→14)          bible exit=1 VIOLATION: timeline inversion 'clerk-filing-open' tick 14 not before 'clerk-lapse-recorded' tick 14
```

Those five exits match V29 §5. The crosscheck is **AGREE**.

## 6. Bottom line at 22:47 (superseded)

The 22:47 line was **INCONCLUSIVE** because component 2 was still absent and V29 agreed with that absence. It is superseded by the final line below. Do not cite §6 as the verdict.

## Addendum — V29 landed after the first write

1. First write of this report (22:41) recorded V29 as ABSENT. That was true of the 22:33:06 check. The report file `V29-verdict-depth.md` has mtime 22:33:40, sha256 `1f8eb831…`, and was on disk at 22:47. §5 is that comparison. The first-write absence was a timing miss, not a disagreement.
2. Component 2 was still absent at 22:50:35. That sentence is stale after 22:57. See addendum 2.
3. Scratch probes lived under `V51-scratch/probes/` and `V51-scratch/table-replay/`. They were not copied into `corpus/`. Live `timeline.json` stayed `2cdb9fda…`.

## Addendum 2 — component 2 landed at 22:57; rows replayed

Knowledge files appeared after both my 22:50 check and V29's 22:30/22:33 cutoff. Pinned at 23:09, unchanged after the replays:

```
4670c0b71668c56c53c0bac90091531d3f0e881c7dcb2ac572d09f96ae22182e  corpus/knowledge/r99-gate-blind-spot-table.md  (20526 B, mtime 22:57:50)
96de708f8e984f6f61ee6387342c287a275328a6293da1d225b2ad00040ebb54  corpus/knowledge/r99-lapse-scope-note.md       (14990 B, mtime 22:57:50)
```

S5's report `S5-knowledge-author.md` was absent at 22:57 and present when I finished the replays. I did not adopt its bottom line. The quotes below are my commands.

Tool pins at replay time matched the table's cited pins: `dependency_freeze.py` `fb9bb9ff…`, contract `8c2561b0…`, `check_bible.py` `ff9fd2aa…`, `support_check.py` `55a5eb27…`, `map_obligations.py` `86b52949…`. Live r98 pin digest in the contract is `5ecf84e1…`, as the table says.

Live controls (`replay-table.txt`):

```
check_bible r99          CLEAN exit 0
map_obligations r99      raw=21 mapped=21 RESULT PASS exit 0
support_check r99        SOURCE-SUPPORT 21/21 RESULT PASS exit 0
dependency_freeze r99    FINDING UNPINNED-FIXTURE … RESULT ERROR exit 2
dependency_freeze --self-test   SELF-TEST 18/18 RESULT PASS exit 0
  including CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
chain r88/r94/r95/r96/r97/r98   each RESULT PASS exit 0
boundary_doc_check       CERTIFIED exit 0
```

Own scratch replays, live fixtures untouched. Each matched the table's catch/miss claim:

| Row | What I ran | Observed |
|---|---|---|
| 1 | r99 `depends_on=[]` on `clerk-lapse-recorded` | bible CLEAN 0; support PASS 0; map `raw=21 mapped=21` PASS 0 |
| 1 | r98 path-bound mirror, `clerk-filing-open.depends_on=[]` | freeze `REDUCTION-DETECTED` … `lost depends_on ['acknowledgment-aru-records']` RESULT FAIL exit 1; bible CLEAN 0 |
| 1b | r98, drop `evin-ninth-bell` from `paired-crossing-decision` | freeze `REDUCTION-DETECTED` … `lost depends_on ['evin-ninth-bell']` exit 1; bible CLEAN 0 |
| 2 | r99 edge → `acknowledgment-aru-records` | bible/support/map all exit 0 |
| 2 | r98 edge → `response-evin-salt-court` | freeze `ADDITION-DETECTED` + `REDUCTION-DETECTED` RESULT FAIL exit 1 |
| 3 | r99 delete terminal, map row kept | bible CLEAN 0; support PASS 0; map `phantom_obligation: timeline.json#/7` RESULT FAIL exit 1 |
| 3 | r98 delete `clerk-filing-open` | freeze `REDUCTION-DETECTED: event clerk-filing-open is missing` RESULT FAIL exit 1 |
| 4 | r99 J05 span 17→20 | support `outside-span` RESULT FAIL exit 1; bible CLEAN 0; map PASS 0 |
| 4 | r98 same span edit, path-bound | freeze `DIGEST-MISMATCH` content digest `09858d77…` != pin `5ecf84e1…` RESULT ERROR exit 2 (same digest the table quotes) |
| 5 | r99 `source_id` → `clerk-filing-note` | bible CLEAN 0; support PASS 0; map `source_id_mismatch: timeline.json#/7 does not bind to 'clerk-filing-note'` exit 1 |
| 5 | r98 `clerk-filing-open.source_id` → `aru-acknowledgment-note` | map `source_id_mismatch: timeline.json#/6 does not bind to 'aru-acknowledgment-note'` exit 1; freeze `DIGEST-MISMATCH` exit 2 naming `timeline.json` |
| 6 | coherent excerpt+anchor swap, baseline tool `4265df5` (`03d04365…`) | `DIGEST 59a0f4fa…` RESULT PASS exit 0 (the table's pre-C1 digest) |
| 6 | same edit, delivered pin | `DIGEST-MISMATCH` content digest `1f73326f…` != `5ecf84e1…` naming `claim-excerpt-map.md` and `fictional-excerpts.md` RESULT ERROR exit 2 (same digest the table quotes) |
| 6 | excerpt-only, map anchor left | bible CLEAN 0; map PASS 0; support `FAIL J14: source-support; mode=verbatim; anchor=not-found` / `anchor missing` RESULT FAIL exit 1 |
| 6 | narrative-only map sentence | bible CLEAN 0; support `20/20` PASS 0; map PASS 0; freeze `DIGEST-MISMATCH` exit 2 naming `claim-excerpt-map.md`. My replacement wording was not byte-identical to S5's, so the content digest (`07be7de9…`) is not the table's `85b16b4f…` map sha. The decision claim matches. |
| 7 | r99 delete event + J21 + restate inventory 21/2/23/19 → 20/2/22/18 | bible CLEAN 0; support `20/20` PASS 0; map `raw=20 mapped=20` PASS 0 |
| 7 | r98 delete `clerk-filing-open` + J20 + restate 20→19 | bible CLEAN 0; support `19/19` PASS 0; map `raw=19 mapped=19` PASS 0; freeze `events 6/7` `REDUCTION-DETECTED: event clerk-filing-open is missing` RESULT FAIL exit 1 |
| 8 | one-comment checker copy | `boundary_doc_check --checker` `FINDING checker_drift` CERTIFICATION FAIL exit 1 |
| 9 | unknown event, dangling entity, unknown source, drop key, self, repeat, tick 14, delete predecessor | each exit 1. Delete-predecessor: `VIOLATION: timeline[6].depends_on: unknown event 'clerk-filing-open'` |

Scope note claims I had already measured on the fixture (6/1/8, prefixes, five byte copies, J21, empty contradictions, receipts) match the note. It also states the minute does not itself record the close (`r94` lines 15–20 / "for this crossing only" at line 19). That matches my earlier `window` count of 0 in the inherited excerpt. The note's "closes no one" is the class label; the quoted note still does not contain that sentence (bound 3).

**V29 comparison, updated.** V29's measurements of component 1 still agree with mine (table in §5). V29's component-2 ABSENT was true at 22:30:31 and at the report mtime 22:33:40. The table did not exist then. The divergence is timing, not a conflicting measurement: V29 did not see bytes that landed 24 minutes later. I do not call V29 wrong. I do not treat V29's INCONCLUSIVE as the verdict on the 22:57 tree.

Round-admission phrase "every row replay-verified by at least two seats" is not something this seat can close. I am one replay. S5's report claims the same exits; I did not count that as the second independent replay.

## Final bottom line

**PASS — both C2 components verify on the late delivered revision: fixture 6/1/7→6/1/8, sources 7→8, 21/21 obligations, CLEAN/PASS, census 172→173, with the locative and "per the terms" bounds; blind-spot table rows 1–9 replayed in scratch and matched the quoted catch/miss exits (including the pre-C1 prose digest `59a0f4fa…` PASS and the delivered `DIGEST-MISMATCH` `1f73326f…`); V29 crosscheck AGREE on component 1 and on component-2-absent-at-V29's-cutoff; the table landed at 22:57 after V29's report, so V29's whole-claim INCONCLUSIVE is a timing bound, not a measurement conflict**
