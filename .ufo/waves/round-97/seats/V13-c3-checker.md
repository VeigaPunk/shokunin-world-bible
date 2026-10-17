# V13 c3-checker — round 97 seat report

- Seat: V13 (verifier, c3-checker). Lane repo: `/home/vgpnk/Projects/shokunin/lore-shokunin`; baseline `f3e09f9` (HEAD `2393934`); all commands run from the lane repo root with `python3`.
- Exclusive write path: this file (`.ufo/waves/round-97/seats/V13-c3-checker.md`, absolute). Scratch: `.ufo/waves/round-97/seats/V13-scratch/`. No commits, no pushes, no network, no other writes.
- Poll-wait gate: **R4 report present** (`.ufo/waves/round-97/seats/R4-fixture-author.md`, mtime 18:50:14) and all 10 r97 fixture files present. Polling stopped on the first try that found it; no plan was verified, nothing fabricated.

## Seat checklist

| # | Requirement | Result |
|---|---|---|
| 1 | `check_bible` r97 CLEAN exit 0 | PASS |
| 2 | `json.load` counts 5 entities / 1 relation / 6 events / 6 sources | PASS |
| 3 | `acknowledgment-aru-records` tick 13, `depends_on [response-evin-salt-court]` | PASS |
| 4 | no dangling references / no duplicate ids | PASS |
| 5 | r96 still CLEAN post-repair | PASS |

## 1–2. check_bible and json.load counts

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r97-crossing-acknowledgment ; echo EXIT=$?
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT=0
```

```
$ python3 -c "import json;[print(t, len(json.load(open('corpus/fixtures/r97-crossing-acknowledgment/%s.json'%t)))) for t in ('entities','relations','timeline','sources','contradictions')]"
entities 5
relations 1
timeline 6
sources 6
contradictions 0
```

Counts are exactly the declared 5/1/6/6 (contradictions correctly empty — the claim asserts no resolution).

## 3. Tick-13 acknowledgment event

`json.load` of `timeline.json`, entry id `acknowledgment-aru-records`:

```
{"id": "acknowledgment-aru-records", "tick": 13, "entity_id": "aru", "place_id": "chalk-stair",
 "depends_on": ["response-evin-salt-court"],
 "description": "At the Chalk Stair at tick 13, Aru reports receiving Evin's response and states that both first-person accounts stand unresolved; the note asserts no accusation, no reconciliation, no winner between the accounts, and no new duty beyond this crossing.",
 "source_id": "aru-acknowledgment-note"}
```

tick 13, actor `aru`, place `chalk-stair`, `depends_on == ["response-evin-salt-court"]` — all as declared.

## 4. Dangling / duplicate audit

Checked every `entity_id`, `place_id`, `source_id`, `depends_on` target on all 6 events, both endpoints and `source_id` on the relation, every entity `first_appearance`, and every entity claim `source_id`:

```
duplicates {'entities': [], 'sources': [], 'events': []}
dangling   []
```

No dangling reference and no duplicate id in any of the three id spaces.

## 5. r96 still CLEAN post-repair

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response ; echo EXIT=$?
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT=0
```

Independent repair-scope confirmation (not R4's own claim):

```
$ git diff --numstat HEAD -- corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
2	2	corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
$ git diff -U0 HEAD -- corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
@@ -44 +44 @@   -|---|---|---|---|---|---:|---|---|   +|---|---|---|---|---:|---|---|
@@ -50 +50 @@   -The ... new relation encodes only the agreement ...   +The ... new tick-12 event encodes only Evin's second account ...
```

Exactly two lines changed, neither a data row: the editorial delimiter 8→7 cells (now matching its 7-column header), and the stale "new relation" sentence replaced. `grep -c 'new relation'` → 0. All 16 J rows and both S rows byte-unchanged (no `| J`/`| S` line appears in the diff). Post-repair r96 receipts unchanged:

```
$ python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response | tail -1
RESULT PASS
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response
OBLIGATIONS raw=16 mapped=16 ; INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18 ; RESULT PASS
```

r96 map sha256 = `e851f068cfd7ed02c97054df18729c4c5a9b8bf60d99d7c9116f427d765440de`, matching R4's reported after-hash independently.

## Supporting evidence beyond the seat checklist

Inherited-table integrity (independent, fresh hashing + structural compare):

- `entities.json`, `relations.json`, `contradictions.json`, `inspiration-note.md`, `source-excerpt.md` are **byte-identical** between r96 and r97 (`sha256` equal pairwise).
- `timeline.json`: r96 list `==` r97 list prefix (5 inherited events unchanged); one appended event. `sources.json`: same, 5 inherited sources unchanged + `aru-acknowledgment-note` appended.
- Map rows J01–J16: pointer, in-world source id, excerpt path, span, mode and anchor columns **identical** to r96's J01–J16; only the path-qualification column names the r97 cluster path, which the map declares explicitly. J17 is the new `timeline.json#/5` row, anchor `Tick 13: I received Evin's response at the Chalk Stair.` verified present at `fictional-excerpts.md:48` within declared span 44–53.

```
$ python3 corpus/tools/support_check.py corpus/fixtures/r97-crossing-acknowledgment | tail -2
SOURCE-SUPPORT 17/17; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 19/19; VALIDATED-ROWS 19/19
RESULT PASS
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r97-crossing-acknowledgment
OBLIGATIONS raw=17 mapped=17 ; RESULT PASS
```

Census (independent repo-relative replica, fresh implementation):

```
pre-r97 : {'fixture_dirs': 170, 'clean_exit0': 36,  'negative_exit1': 134, 'violation_lines': 421, 'non_0_1_exits': []}
post-r97: {'fixture_dirs': 171, 'clean_exit0': 37,  'negative_exit1': 134, 'violation_lines': 421, 'non_0_1_exits': []}
```

170→171, +1 clean, zero non-0/1 exits, 421 violation lines unchanged — matches the declared census delta exactly.

## Verification stability

Final artifact hashes (`V13-scratch/final-hashes.txt`), re-hashed after the poll loop: unchanged. All r97 mtimes (18:44:16–18:49:14) precede my checks; r96 map mtime 18:43:42. No producer wrote to the fixture during or after verification, so the bytes I checked are the settled revision. Note: R5 and R6 seat reports were not yet present as `.md` at my verification time, but R5's owned files (`claim-excerpt-map.md`, `README.md`) were written and stable (hashes unchanged across the re-check); this did not affect my gate, which polls R4.

## Caveats

- One mid-flight race: my first J-row count read 16 because `claim-excerpt-map.md` was still being written at that instant (mtime 18:48:56). Re-run on the settled file gives 17 rows J01–J17, consistent with the declared 17 obligations. Reported here for transparency; not a defect in the delivered artifact.
- Everything above is a structural/lexical check on the delivered bytes. It is not a judgment on source authenticity, truth, rights, or canon, and `support_check` receipts are lexical preflight, not whole-claim entailment.

**Bottom line: PASS — r97 `check_bible` CLEAN exit 0, counts exactly 5/1/6/6, tick-13 `acknowledgment-aru-records` depends only on `response-evin-salt-court`, zero dangling/duplicate ids, r96 CLEAN post-repair with a 2-line repair diff that leaves every data row byte-unchanged.**
