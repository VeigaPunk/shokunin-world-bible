# V27 — verdict-depth (round 98)

Seat: V27 `verdict-depth`. Scope per seat spec: read the C3 seats (S3, S4, S5),
run 2 own replays, issue exactly one DEPTH verdict on the declared C3 before→after
("institutional filing record asserting no finding" class, 5/1/6→6/1/7) with named
bounds.

Baseline: r97 closure `9a3d648` (HEAD `dd4df1b`). Lane root
`/home/vgpnk/Projects/shokunin/lore-shokunin` for every path below; all commands run
from there with `python3`. Writes by this seat: this report plus scratch
`.ufo/waves/round-98/seats/V27-scratch/` (`poll.sh`, `poll.log`, `replay.py`,
`replay2.py`, `baseline-hashes.txt`, `pre-receipts.txt`, `r95-post-repair.txt`,
`snap-1.txt`, `probe1-receipts.txt`, `replay-1.txt`, `replay-2.txt`,
`census-receipts.json`, `support-full-r98.txt`, `r95-own-replay.txt`,
`r95-prerepair/` (9-file pre-repair copy), `snap-a/b/c/d.txt`, `final-receipts.txt`).
No commits, no pushes, no network, no nested agents.

## 1. Poll record and method

Poll-wait protocol: 20 s cadence, 40 tries, launched 20:28:22 on the r98 fixture dir
plus producer reports. Observed timeline (lane clock, -03:00):

- 20:28:24 — `corpus/fixtures/r98-clerk-filing/` appeared with 10 files, **all
  byte-identical to r97** (`cmp`/sha256 sets equal) — S3's copy step only, i.e. the
  placeholder state; no receipt was run against it (S3's report §D1 and S5's report
  both record the same hazard: an existence-only poll is satisfied by the
  placeholder).
- 20:28:55 — S3's four authored files landed (`entities/sources/timeline/
  fictional-excerpts`).
- 20:30:21 / 20:30:41 — S4's `claim-excerpt-map.md` and `README.md` landed.
- 20:31:00 / 20:32:15 / 20:33:42 — S3 / S4 / S5 reports appeared (my gate; all
  three C3 producer reports present by 20:33:42, well inside the 40-try budget).
- ~20:32:5x — first sighting of `corpus/knowledge/r98-clerk-scope-note.md`
  (`a73cd57b…`); S5 revised it at 20:33:01 to the delivered
  `1162262c742441115681d30be588039be4f1a026b755eeb7d15c9ba41952a4b8` (72 lines),
  equal to the hash in S5's report.
- ~20:32:51 — S1's C1 files landed (`dependency_freeze.py` `03d04365…`); S1's report
  was **ABSENT at my final pass** (20:36) — see §6. Not my gate: C3 = S3/S4/S5.

Revision frozen for verification: 10-file fixture sha256 capture `snap-a.txt` at
20:33:55, re-hashed `snap-b.txt` 20:34:40 → `SNAPSHOT STABLE (12 files)` (fixture +
note + r95 map); fixture alone re-hashed `snap-c/d` 20:35:10/20:35:40 → stable. All
receipts below are on that revision. **Nothing in this seat's scope was ABSENT.**

## 2. Replay 1 — check_bible, counts, census, inheritance (`replay-1.txt`, 20:31:40)

```
$ sha256sum corpus/fixtures/check_bible.py
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r98-clerk-filing
CLEAN: schema, citations, relations, timeline; 0 violations            exit=0
$ ls -d corpus/fixtures/*/ | wc -l
172                                                                    # 171 at r97 closure
```

My own parsed checks on the delivered JSON (`replay.py`):

```
r98 counts e/r/ev/s/c: 6/1/7/7/0        (r97: 5/1/6/6/0)
r98 timeline[:-1] == r97 timeline: True ; sources[:-1]: True ; entities[:-1]: True
r98 relations == r97 relations: True
byte-identical inherited copies: relations.json True; contradictions.json True;
  inspiration-note.md True; source-excerpt.md True   (4 untouched copies)
r97 excerpts is byte-prefix of r98: True   (3410B -> 4187B, delta +777B)
new entities entry: {"id": "clerk-maren", "kind": "character", "name": "Maren",
  "first_appearance": "clerk-filing-note", claims[0].source_id "clerk-filing-note"}
new timeline entry: {"id": "clerk-filing-open", "tick": 14, "entity_id":
  "clerk-maren", "place_id": "chalk-stair", "depends_on":
  ["acknowledgment-aru-records"], "source_id": "clerk-filing-note", ...}
new sources entry: {"id": "clerk-filing-note", ... "fictional first-person note"}
r98 contradictions: []
```

## 3. Replay 2 — census receipt, map rows, chain, dangling audit, class text
(`replay-2.txt` 20:32:30; `support-full-r98.txt` 20:32:41)

Census (my own fresh script over all 172 dirs, same convention as r94–r97:
violation lines = lines containing `VIOLATION`):

```
CENSUS {"dirs": 172, "clean": 38, "negative": 134, "violation_lines": 421, "odd": []}
```

= exactly **+1 dir, +1 clean** vs r97 (171/37/134/421), negative and violation
counts unchanged, zero non-0/1 exits.

Map rows (my own parser over both maps):

```
row counts r97/r98: 17 20
r98 new row ids: ['J18', 'J19', 'J20']
inherited-row diffs (modulo namespace col 2): NONE
namespace-column diffs: 17
```

Chain and reference audit on delivered `timeline.json`:

```
ticks: [9, 9, 10, 11, 12, 13, 14]
edges: 6 all strictly backward+earlier-tick: True
duplicates: {'entities': [], 'sources': [], 'events': []}
dangling: []
```

Full tool receipts at the final pass (20:35:04, checker revisions unchanged
`ff9fd2aa…` / `55a5eb27…` / `86b52949…` + contract `2142b991…`):

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r98-clerk-filing
CLEAN: schema, citations, relations, timeline; 0 violations            exit=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r98-clerk-filing
OBLIGATIONS raw=20 mapped=20
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22
RESULT PASS                                                            exit=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 18/18
PASS J18 ... 60:> I am Maren, clerk of the Chalk Stair registry, and I record the matter OPEN.
PASS J19 ... 59:> Tick 14: I filed both pending accounts at the Chalk Stair registry.
PASS J20 ... 59:> Tick 14: I filed both pending accounts at the Chalk Stair registry.
SOURCE-SUPPORT 20/20; EDITORIAL-ANCHORS 2/2; MODES 22/22; VALIDATED-ROWS 22/22
RESULT PASS                                                            exit=0
```

Class-text probes on the delivered bytes (my own):

- reliability note (`sources.json#/6`) contains `no finding` / `no verdict` /
  `no reconciliation` / `no resolution` / `not evidence of a breach` — all True
  (it says "a winner between the accounts", not the literal string "no winner");
- excerpt lines 59–62: `> Tick 14: I filed both pending accounts at the Chalk Stair
  registry.` / `> I am Maren, clerk of the Chalk Stair registry, and I record the
  matter OPEN.` / `> I assert no finding.` / `> I reach no verdict and reconcile
  nothing.`; line 64 scope: "It is an institutional filing only: it asserts no
  finding and no resolution, reaches no verdict, and reconciles nothing; the two
  first-person accounts stand unresolved…".
- corpus-wide resolution-language scan: the only hits for closure-type wording are
  the negative-bound sentences in the r97/r98 scope notes; no file asserts the
  matter closed, settled, or resolved (no constructible resolution/blame reading).

## 4. Preservation battery and the C3 repair half

Inherited byte identity (5 files copied, 4 untouched) and parsed-prefix equality:
see §2. The declared "17 inherited map rows unchanged" holds modulo the namespace
column only (§3).

r95 carried-wording repair (C3's repair half), my own replay: pre-repair map
restored from `9a3d648` into `V27-scratch/r95-prerepair/` (9 files), both revisions
run through all three tools:

```
sha256 pre 30281ff1a497bbe66f23cbd8a49befb3319595f20990718a0ffe8050741a874a
sha256 post 80440d61122488a267a4f0a58a55cb54d89c037d93160f1123e5fb3b2f396f61
$ diff pre post -> 49c49, ONE line (prose in "## Timeline normalization and scope";
  data rows, pointers, anchors, spans, modes byte-unchanged)
pre:  CLEAN exit 0; raw=15 mapped=15 PASS exit 0; 15/15 PASS exit 0
post: CLEAN exit 0; raw=15 mapped=15 PASS exit 0; 15/15 PASS exit 0   # identical receipts
```

Chain pin cross-check (C2-adjacent, read-only): the freeze contract now pins both
`r97-crossing-acknowledgment` and `r98-clerk-filing`, and my own runs match the pins:

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r98-clerk-filing
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
DIGEST 59a0f4fa3d4a47e03649a54d1815c45ee1eef641b63a59ebe7210bc9d9b9b133
RESULT PASS   exit=0   (contract pin r98 = 59a0f4fa…; r97 = 3c922d20…, also PASS)
```

## 5. DEPTH VERDICT (one verdict, bounded)

**DEPTH IMPROVED — bounded, on the delivered revision.**

The institutional-filing-asserting-no-finding class is carried and independently
reproducible: the before→after is exactly the declared one (5/1/6/6 → 6/1/7/7
entities/relations/events/sources; 17 → 20 map obligations, the three new rows
`first_appearance` + `claim` + `event`; census 171 → 172; `check_bible` CLEAN;
`map_obligations` 20/20; `support_check` 20/20, 18/18 distinct anchors; inherited
rows parsed-value identical; four inherited files byte-identical; excerpts
append-only +777B; chain one strict-backward edge longer, 6/6 edges, zero
dangling/duplicate references). No constructible resolution, finding, blame, or
winner reading exists in the delivered bytes: every resolution-adjacent statement
is an explicit negation, and no other corpus file asserts the matter closed.

**Bounds (explicit):**

- **Delivered-revision bound.** The verdict holds for the byte revision frozen at
  20:33:55/20:35:40 (`entities db2d8e5d…`, `sources 32ee15b1…`, `timeline
  eb24e084…`, `fictional-excerpts 29e384bf…`, `README 32efc78f…`, map `c1099d0e…`,
  `contradictions 37517e5f…`, `relations c279254b…`, `inspiration-note 58f5390e…`,
  `source-excerpt b5edc2fd…`). Any change to these bytes voids it; the fixture is
  now also pinned (`59a0f4fa…`), which freezes the digests of the 5 JSON tables.
- **Class is record-scoped.** The class is defined by what the authored note says
  (a filing act + OPEN), not by world fact: one office-holder's note, no independent
  corroboration, no adjudication; "clerk of the Chalk Stair registry" is the note's
  own attributed self-description; `first_appearance` is bible-local.
- **Checker bound.** The receipts are structural/lexical (schema, citations,
  relations, timeline, spans, modes); none of the three tools reads the note as
  testimony or decides truth, finding, chronology, rights, or canon. The
  no-finding reading is supported by receipts + my manual whole-proposition reading,
  not by an entailment proof.
- **Scope bound.** This verdict covers C3's depth claim only. C1 (freeze hygiene)
  and C2 (chain extension) are other seats' scope; my r98 freeze run is only a
  cross-check that the fixture is pinnable and pinned.
- **Rights/canon unassessed** anywhere, as declared by the producers.

## 6. Cross-seat observations (evidence, not verdicts on other seats)

1. **Placeholder-poll hazard confirmed independently** (S3 §D1, S4 §A, S5 poll
   record): between 20:28:24 and 20:30:41 the r98 `README.md`/`map` existed with
   r97 bytes. Existence-only polls can be satisfied by the placeholder; my replays
   ran after content markers and re-ran at 20:35:04 with identical receipts.
2. **S1's report was ABSENT at my final pass (20:36)** while S1's bytes
   (`dependency_freeze.py` `03d04365…`, contract `153ebc5b…`) had landed and both
   new pins verify PASS. C1/C2 verification is not this seat's scope; recorded for
   the endgame tally. No poll of mine waited on S1, and none waited on SELF
   (endgame convention honoured trivially).
3. **Contract hash drift after S5's addendum measurement**: S5's report and the
   r98 note record `dependency-freeze-contract.json` as `c435239d…` at 20:32:51;
   the delivered contract is `153ebc5b…` (still churning under S1 at my pass). The
   r95/r96 addenda pin `map_obligations.py`/its contract (`86b52949…`/`2142b991…`,
   both still current), not the freeze contract, so the addenda are not stale by
   this drift; the r98 note's own checker hashes were re-measured unchanged at my
   final pass.
4. **Note revision mid-round** (`a73cd57b…` → `1162262c…` at 20:33:01): my first
   read was of the pre-revision bytes; the delivered revision is the one cited in
   §3/§5 and it matches S5's report hash. No defect, recorded for exactness.
5. **Parent-tree stray (r94-F01 class, NOT this seat):** `find
   /home/vgpnk/Projects/shokunin -maxdepth 1 -newermt "2026-10-17 20:27" -type f`
   found `/home/vgpnk/Projects/shokunin/baseline-analyze.txt` (mtime 20:30:10,
   105 B, untracked `??` in the parent repo). Content:
   `python3: can't open file '/home/vgpnk/Projects/shokunin/analyze.py': [Errno 2]
   No such file or directory` — a seat ran a command with the session cwd
   (parent) instead of the lane root and redirected the error into the parent
   tree. Not written by V27 (my writes are the report + `V27-scratch/` only, all
   under `lore-shokunin/`; verified by the stray-write guard returning empty for
   both `V27-verdict-depth.md` and `r98-clerk-scope-note.md` outside the lane).
   Left in place — not mine to delete; flagged for the round's bookkeeping.

## Bottom line

PASS — DEPTH improved (bounded): institutional-no-finding class verified end-to-end
on the frozen delivered revision (6/1/7/7, 20/20 map obligations, CLEAN, census
+1 clean, inherited rows/bytes preserved, no resolution reading), r95 one-line
repair receipt-invariant; C1/C2 outside this seat (S1 report ABSENT at final pass).
