# V29 — verdict-depth (round 99)

Seat: V29 `verdict-depth`. Scope: read the C2 seats (both components), run 2 own
replays, issue exactly one DEPTH verdict on the declared C2 before→after with
named bounds.

Declared C2 is one axis-move, two falsifiable components:

1. `corpus/fixtures/r99-window-lapse/` — fifth beat (clerk lapse record: window
   closed per the original minute, agreement unfulfilled, no claim lodged, matter
   stays open; no resolution/blame anywhere). Before 6/1/7, 7 sources at r98.
   After 6/1/8, 8 sources, 21 map obligations (20 inherited + 1 event), CLEAN,
   census 172→173.
2. `corpus/knowledge/r99-gate-blind-spot-table.md` — consolidated blind-spot
   decision table, every row replay-verified on the delivered revision. Companion
   note `corpus/knowledge/r99-lapse-scope-note.md` is the same owner's other file.

Baseline: r98 closure `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`).
Working-tree HEAD at start `337f0fa` (blocked-dispatch log commit; zero corpus
increment). Lane root `/home/vgpnk/Projects/shokunin/lore-shokunin`. All commands
from there with `python3`. Writes by this seat: this report and
`.ufo/waves/round-99/seats/V29-scratch/` (`poll.sh`, `poll.log`,
`poll-hashchain.txt`, `replay-1.txt`, `replay-1-tools.txt`, `replay-2-tools.txt`,
`pre-s4-receipts.txt`, `map-rows.txt`, `map-rows-aligned.txt`, `census.txt`,
`scope-scan-1.txt`, `scope-scan-2.txt`, `r99-hashes-early.txt`,
`r99-hashes-final.txt`, `blind-probes.txt`, `probes/`). No commits, no pushes,
no network, no nested agents.

Axes for this seat: presence (artifacts and producer reports, else ABSENT),
replay fidelity (quoted commands and observed outputs), depth delta (measured
before→after, not a plan), bounds honesty (contradictions kept), exclusive writes.

## 1. Poll record

Background poller `V29-scratch/poll.sh`, 20 s cadence, 40 tries, started
22:01:47 (−03:00). Gate: fixture dir + both knowledge files + S3/S4/S5 reports.
Existence-only was not treated as delivery (r98 placeholder hazard).

- 22:01:47 try 0 — fixture dir present, 10 files. `timeline.json` /
  `sources.json` / `fictional-excerpts.md` already the lapse bytes (mtime
  22:01). `README.md` and `claim-excerpt-map.md` still r98 byte copies (mtime
  21:36, sha256 `32efc78f…` / `c1099d0e…`). `S3-fixture-author.md` present
  (5,069 B). Knowledge `r99-*` absent. S4/S5 reports absent.
- 22:02:12 — pre-S4 receipts (mid-flight, not a defect): `map_obligations`
  `OBLIGATIONS raw=21 mapped=20` / `FINDING missing_obligation: timeline.json#/7
  has no map row` / `RESULT FAIL` exit 1. `support_check` still `20/20 …
  RESULT PASS` exit 0 (it does not see an unmapped event). Same load-bearing
  shape as the r97 pre-map `missing_obligation`.
- 22:02:39 / 22:03:19 — S4 map (`d2fe20e5…`, 17,119 B) and README (`b9320941…`,
  6,176 B) landed. `S4-fixture-docs.md` present by 22:03.
- tries 1–40 — S5 report never appeared; `corpus/knowledge/r99-*` never
  appeared. `POLL-EXHAUSTED 2026-10-17T22:15:12-03:00`.
- Rechecks after exhaustion: 22:20:15 and 22:30:31 — still no
  `corpus/knowledge/r99-gate-blind-spot-table.md`, no
  `corpus/knowledge/r99-lapse-scope-note.md`, no `S5*.md`.

Component 1 producer reports (S3, S4) and the fixture were present inside the
budget. Component 2 is **ABSENT**. Not verified against a plan.

Fixture hashes frozen at 22:20:15 (`V29-scratch/r99-hashes-final.txt`), equal
to the 22:04:03 post-S4 capture and to S4's declared hashes:

```
d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d  claim-excerpt-map.md
b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049  README.md
fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d  fictional-excerpts.md
8c215b38dc02400910ff935eab46ecf82b0381b63a75d092b03bd601a9915f15  sources.json
2cdb9fda5baae1a496b31c004a7e0a9345ac580b257da0d9a04c045214c4c069  timeline.json
db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984  entities.json
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  relations.json
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  contradictions.json
58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37  inspiration-note.md
b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd  source-excerpt.md
```

The five unextended copies (`entities`, `relations`, `contradictions`,
`inspiration-note`, `source-excerpt`) are byte-identical to working-tree r98
and to `4265df5:corpus/fixtures/r98-clerk-filing/`. `git diff --exit-code
4265df5 -- corpus/fixtures/r98-clerk-filing` → exit 0.

## 2. Replay 1 — check_bible, counts, inheritance, census

Tool pins (unchanged across the replays):

```
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9  corpus/tools/map_obligations.py
55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  corpus/tools/support_check.py
2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41  corpus/tools/map-obligations-contract.json
```

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r99-window-lapse
CLEAN: schema, citations, relations, timeline; 0 violations            exit=0
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r98-clerk-filing
CLEAN: schema, citations, relations, timeline; 0 violations            exit=0
```

Own parse (`V29-scratch/replay-1.txt`), r98 working tree = `4265df5` blob:

```
r98 e=6 claims=6 rel=1 ev=7 src=7 contra=0
r99 e=6 claims=6 rel=1 ev=8 src=8 contra=0
entities equal True
relations equal True
contradictions equal True
sources[:-1]==r98 True
timeline[:-1]==r98 True
excerpt byte-prefix True          (4187 B → 5114 B, delta +927 B)
ticks [9, 9, 10, 11, 12, 13, 14, 15]
edges 7 strictly_earlier True
dangling entity/source refs: none; duplicate ids: none
```

New source `clerk-lapse-note` ("Maren's Chalk Stair Lapse Note"). New event
`clerk-lapse-recorded`, tick 15, `entity_id` `clerk-maren`, `place_id`
`chalk-stair`, `depends_on` `["clerk-filing-open"]`, `source_id`
`clerk-lapse-note`. Description: "At the Chalk Stair at tick 15, the clerk
records that the crossing-window named in the original minute has closed; the
agreement was unfulfilled; no claim was lodged; the matter stands as a
historical open entry."

Census, own run over all fixture dirs (`V29-scratch/census.txt`):

```
{"dirs": 173, "clean": 39, "negative": 134, "violation_lines": 421, "odd": []}
```

Baseline directory count: `git ls-tree -d --name-only 4265df5 corpus/fixtures/`
→ 172. Negative 134 and violation lines 421 match the r98 closure figures in
LOG.md. The +1 directory is `r99-window-lapse` (the only new fixture path in
`git status --porcelain -- corpus/fixtures`). Clean 38→39 is inferred from that
dir being CLEAN and those two counts being unchanged, not from a paired
re-census of the `4265df5` tree.

## 3. Replay 2 — map_obligations, support_check, row inheritance

Post-S4, 22:04:03 (`V29-scratch/replay-2-tools.txt`), map and README hashes as
in §1:

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r99-window-lapse
OBLIGATIONS raw=21 mapped=21
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23
RESULT PASS                                                           exit=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r99-window-lapse
PASS J21: source-support; mode=verbatim; anchor=found; 70:> Tick 15: The crossing-window named in the original minute has closed.
RECEIPT JSON-FACTS 21; EDITORIAL-ROWS 2; TOTAL-ROWS 23
SOURCE-SUPPORT 21/21; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 23/23; VALIDATED-ROWS 23/23
RESULT PASS                                                           exit=0
```

Own ID-aligned map parse (`V29-scratch/map-rows-aligned.txt`): r98 rows 22
(J01–J20, S01–S02); r99 rows 23. Only new id `J21`. Inherited 22/22 equal after
swapping `r99-window-lapse:` → `r98-clerk-filing:` in the namespace column;
pointer / anchor / span / mode drift = 0. J01–J20 stay on map lines 22–41.
S01/S02 shift 49→50 and 50→51 because J21 inserted one line above the editorial
table; their cells are otherwise equal. J21 is map line 42:

```
J21 | timeline.json#/7 (tick, entity_id, place_id, depends_on, description, source_id)
    | clerk-lapse-note | r99-window-lapse:clerk-lapse-note
    | fictional-excerpts.md | 66-76 | verbatim
    | Tick 15: The crossing-window named in the original minute has closed.
```

That anchor occurs once in the excerpt, at line 70, inside span 66–76.

Quoted lapse note (`fictional-excerpts.md:70-76`):

```
> Tick 15: The crossing-window named in the original minute has closed.
> The agreement was unfulfilled.
> No claim was lodged.
> The matter stands as a historical open entry.
> I record no resolution, assign no blame, and reconcile nothing.
Scope: … asserts no resolution, no blame, and no reconciliation, and it
creates no new duty; … the matter stays open.
```

`contradictions.json` remains `[]` (3 B, same hash as r98). No new entity,
claim, or relation.

## 4. C2 seats read

Producers:

- **S3** `S3-fixture-author.md` — **PASS** on its write set (read in full).
  6/1/8, CLEAN exit 0, seven files byte-identical to `4265df5` r98 at its
  report time, excerpt prefix true. Its "README and map still say r98" clause
  was true then and is stale after S4 (S4 §E records the same). Census not
  measured by S3.
- **S4** `S4-fixture-docs.md` — **PASS** (read in full). Map `d2fe20e5…`,
  README `b9320941…`, 20 inherited rows modulo namespace, J21 span 66–76,
  three gates PASS exit 0. Those hashes and exits match my replay.
- **S5** — **ABSENT**. No report. No knowledge files. Not read. Not inferred.

Verifier seats that landed on component 1 (bottoms read; V10/V11/V13/V80 tails
read; V105 read in full). Concordant with my measurements unless noted:

- V10 c2-checker **PASS** — CLEAN, 6/1/8/8, edge tick 15 → `clerk-filing-open`,
  no dangling/duplicate ids. Same hashes as §1.
- V11 c2-inherited-equality **PASS** — parsed-value identity, five `cmp`
  copies, prefix extensions. Hashes match.
- V12 c2-support-map **PASS** — 21/21 and raw=21 mapped=21 on map `d2fe20e5…`.
- V13 c2-anchors **PASS** — 21 JSON anchors + 2 editorial in-span; J21 only at
  line 70. Same false zip-vs-J21 scratch hazard I hit and corrected by
  ID-alignment.
- V41 anchor-replica-2 **PASS**; V47 byte-prefix-2 **PASS**; V77 map-inventory
  **PASS** (independent raw = 21); V80 c2-prose-prefix **PASS** (r94⊂…⊂r99
  excerpt chain; lapse section once, terminal); V86 c2-no-new-entity **PASS**
  (entities/relations byte-identical; map delta +1 event row); V109
  inherited-map-rows **PASS** (20/20 modulo namespace); V119 c2-anchors-3
  **PASS**.
- **V105 c2-event-description FAIL** — confirmed by me, not re-rolled. See §6
  bound 4. The four recorded clauses and `historical open entry` are in both
  the description and the note. The locative "At the Chalk Stair" is in the
  description and not in the lapse section.

No component-2 verifier report was available to read: the table does not exist,
so no seat could have replay-verified its rows. I did not treat any scratch
draft as the table.

## 5. Component 2 — ABSENT

Declared after-state: one cited table at
`corpus/knowledge/r99-gate-blind-spot-table.md`, every row replay-verified, plus
`corpus/knowledge/r99-lapse-scope-note.md`. At 22:30:31 both paths and `S5*.md`
were still missing (`ls` → "No such file or directory"). Before-state (blind
spots scattered across prior debt ledgers) is therefore unchanged by this
round's knowledge tree. I did not verify a plan, a LOG.md sentence, or another
seat's scratch.

Own measurements on the delivered fixture, recorded as bounds for the fifth-beat
edge, **not** as a substitute for the missing table
(`V29-scratch/blind-probes.txt`; copy-then-mutate under scratch, live fixture
untouched):

```
P0-control:            exit=0  CLEAN
P5-emptied-depends_on: exit=0  CLEAN          # depends_on = []
P8-wrong-but-earlier:  exit=0  CLEAN          # depends_on = ["response-evin-salt-court"]
P9-delete-terminal:    exit=0  CLEAN          # pop clerk-lapse-recorded
P1-drop-key:           exit=1  VIOLATION: timeline[7].depends_on: required nonempty list
P3-tick-inversion:     exit=1  VIOLATION: timeline inversion 'clerk-filing-open' tick 14 not before 'clerk-lapse-recorded' tick 14
```

So on this revision the tick-15→tick-14 edge is still only partially policed:
a dropped key and a non-increasing tick fail; an emptied list, a wrong-but-earlier
edge, and a deleted terminal row stay CLEAN. The P1 wording "required nonempty
list" is false of the empty-list case (P5). F15 silent mutants, dependency-wording
removal, consistent-regeneration, and frozen-pin status were **not** replayed
here — those rows were not delivered, and recollecting prior rounds would
violate the declaration's "measured this round, not recollected" rule.

## 6. DEPTH VERDICT (exactly one)

**DEPTH — UNPROVEN as a whole.** Component 1 is delivered and is an improvement
on the measured bytes, with the bounds below. Component 2 was not delivered.
The declaration makes the two components one axis-move. A missing half means
the declared before→after is not established. This is not a finding that the
lapse fixture is false, and it is not a finding that a table which does not
exist failed a replay.

Component 1, on the frozen revision in §1: the crossing arc gains a fifth beat
that records a closed window, an unfulfilled agreement, no claim lodged, and an
open matter, and that asserts no resolution, no blame, and no reconciliation in
the note. Before (r98 at `4265df5`): 6/1/7, 7 sources, 20 map obligations.
After: 6/1/8, 8 sources, 21 map obligations (20 inherited rows unchanged modulo
namespace + J21), `check_bible` CLEAN exit 0, `map_obligations raw=21 mapped=21`
PASS exit 0, `support_check` 21/21 PASS exit 0, census directories 172→173
(clean 38→39 inferred as in §2). No new entity, claim, relation, or
contradiction. r98 fixture byte-untouched vs `4265df5`. The pre-S4
`missing_obligation` on `timeline.json#/7` shows J21 is load-bearing.

Named bounds:

1. **Structural and lexical only.** Receipts do not prove testimony truth,
   canon, chronology, rights, or identity. `support_check` is anchor preflight.
2. **The class is an authored in-record status.** The note's own sentences
   carry "has closed", "unfulfilled", "No claim was lodged", "historical open
   entry", and "I record no resolution, assign no blame, and reconcile nothing."
   No gate reads that prose. `contradictions.json` being `[]` is an empty file,
   not a proof that no contradiction exists.
3. **Window-closed is the note's wording, not an external minute.** "Named in
   the original minute has closed" is the quote. Tick 15 and
   `depends_on: ["clerk-filing-open"]` are editorial encodings (README:13,
   map:55).
4. **Two prose gaps, confirmed, not hidden (V105 FAIL stands for its seat).**
   - Description locative: "At the Chalk Stair at tick 15, the clerk records…"
     is not in lapse-section lines 66–76 (`section_has_Chalk_Stair False`).
     `place_id: chalk-stair` is the declared schema slot. The description
     sentence places the recording act at the stair; the lapse note does not.
     Tick-14's note did name the place; tick 15 copies the template without a
     matching sentence. Not resolution and not blame. Unflagged in the map's
     "encodes only" sentence (map:55).
   - Manner gloss: README:11 says "the window closed per the original minute's
     terms"; map:69 says "has closed per that minute's terms". The note says
     "named in the original minute has closed", not "per … terms". The
     declaration uses the stronger phrasing. The note does not.
5. **Checker blind spots on this edge, measured this round (§5), not table-verified.**
   Emptied `depends_on`, wrong-but-earlier edge, and deleted terminal row stay
   CLEAN. The dependency claim is bytes + prose + J21, not a rule that those
   three mutants fail.
6. **Preserving continuation at named levels.** Byte-identical for the five
   unextended copies; parsed-prefix for `timeline`/`sources`; strict byte-prefix
   for the excerpt (V80's longer chain not re-run by me past r98⊂r99); column
   equality modulo namespace for 22 inherited map rows. Not map-file byte equality.
7. **Census bound.** Directory count 172 (`git ls-tree` on `4265df5`) → 173
   (live). Clean 39 / negative 134 / violation lines 421 / odd empty is the live
   census. The 38→39 clean step is inferred, not a paired baseline re-run.
8. **Component 2 absent.** No table, no scope note, no S5 report inside 40
   polls or at the 22:30:31 recheck. "Every row replay-verified by at least two
   seats" is not met, because there are no rows. Prior-round blind spots were
   not recollected into a fake table.
9. **S3's doc clause is stale, not a fixture defect.** At S3's report time the
   map was the r98 copy and `map_obligations` correctly failed. After S4 it
   passes. Mid-flight, recorded.

No harm observed inside component 1's data: r98 untouched; no new entity,
relation, or contradiction; resolution/blame/reconciliation in the new section
occur only as negations. The locative and the "terms" gloss are support gaps,
not inserted blame. They do not by themselves make the fifth beat false. They
do bound how far the description and the README may be quoted as the note.

## 7. Non-axis notes

- Host: this seat's poller completed (pid gone after `POLL-EXHAUSTED`). No
  `/tmp` failure observed in this seat's commands.
- Other producers (S1/S2, C1) are outside this verdict. Not read as depth
  evidence.
- This seat did not write under `corpus/`. Scratch mutations lived under
  `V29-scratch/probes/` and were not copied back.

## Bottom line

**INCONCLUSIVE — C2 component 1 verifies on the delivered bytes (6/1/7→6/1/8, 7→8 sources, 20→21 obligations, J21 load-bearing, CLEAN/PASS, census dirs 172→173) with the locative and "per the terms" gloss bounds; C2 component 2 ABSENT after 40 polls (no blind-spot table, no lapse scope note, no S5 report), so the one depth axis-move is not established as a whole.**
