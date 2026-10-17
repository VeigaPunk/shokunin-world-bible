# F01 — c1-checker (C1 structural verification)

**Seat role:** FOLLOW-UP leaf, C1 structural verifier. Scope: `check_bible.py` cleanliness, parsed fixture counts, tick-10 dependency edge, inherited-record parsed-value identity against `r88-m3-maya-cluster`. Not in scope (other seats): whole-claim entailment, editorial comparison review, C2 tool behavior.

**Environment pin:** lane HEAD `65a93298cb100fdbf5732ac6de55f01a683c02d8` (`git rev-parse HEAD`); WORK candidate `abbc3e0` is an ancestor. All commands run from repo root `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. No files written except this report; no corpus edits.

---

## 1. `check_bible.py` on the new fixture — PASS

Command and full observed output (stdout/stderr captured separately to prove silence):

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r94-paired-crossing > /tmp/f01_out.txt 2>/tmp/f01_err.txt; echo "EXIT=$?"
EXIT=0
STDOUT:
CLEAN: schema, citations, relations, timeline; 0 violations
STDERR:
(stderr bytes: 0)
```

Control run on the inherited cluster (same checker, prior snapshot) also CLEAN, so the new fixture is not passing against a broken baseline:

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-m3-maya-cluster; echo "EXIT_R88=$?"
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT_R88=0
```

Evidence pointer: `/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r94-paired-crossing/` (11 files listed), checker at `corpus/fixtures/check_bible.py`.

**Scope caveat:** `check_bible.py` reports schema/citation/relation/timeline consistency, not source entailment. CLEAN is necessary, not sufficient, for C1.

## 2. Parsed counts 5 entities / 1 relation / 3 events — PASS

Parsed (not grepped) with `json.load`, per file:

```
$ cd corpus/fixtures/r94-paired-crossing && python3 -c "..."
== entities.json type list
  len 5
== relations.json type list
  len 1
== timeline.json type list
  len 3
== sources.json type list
  len 3
== contradictions.json type list
  len 0
```

Matches the declared after-state exactly. Cross-checked against r88 in the same run (`entities 4→5`, `relations 0→1`, `timeline 2→3`, `sources 2→3`), i.e. the deltas are exactly the declared additions and nothing was dropped.

Supporting inventory check for the map's 14-obligation claim (`corpus/fixtures/r94-paired-crossing/claim-excerpt-map.md:3` states "all 14 source-attributed JSON obligations … plus two separately labeled editorial comparisons"):

```
$ grep -oE '/[A-Za-z0-9_./~-]+' claim-excerpt-map.md | sort -u | wc -l
14
```

and the independent lexical preflight agrees on the same row inventory:

```
$ python3 corpus/tools/support_check.py corpus/fixtures/r94-paired-crossing
RECEIPT JSON-FACTS 14; EDITORIAL-ROWS 2; TOTAL-ROWS 16
SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 16/16; VALIDATED-ROWS 16/16
RESULT PASS
EXIT_SUPPORT=0
```

## 3. Tick-10 event depends on BOTH tick-9 event ids — PASS

Full `timeline.json` rows as parsed:

```json
{"id": "aru-ninth-bell",   "tick": 9,  "entity_id": "aru",  "place_id": "quiet-rise",  "depends_on": [], "description": "Aru carries the north lantern at Quiet Rise.",  "source_id": "paired-clock"}
{"id": "evin-ninth-bell",  "tick": 9,  "entity_id": "evin", "place_id": "salt-court",  "depends_on": [], "description": "Evin holds the south bell at Salt Court.",     "source_id": "paired-clock"}
{"id": "paired-crossing-decision", "tick": 10, "entity_id": "aru", "place_id": "chalk-stair",
 "depends_on": ["aru-ninth-bell", "evin-ninth-bell"],
 "description": "At the Chalk Stair, Aru and Evin agree to share stewardship for this crossing only, then chalk one temporary route mark.",
 "source_id": "crossing-minute"}
```

Set-equality assertion, observed output:

```
tick9 ids: ['aru-ninth-bell', 'evin-ninth-bell']
tick10 ids: ['paired-crossing-decision']
tick10 paired-crossing-decision depends_on == both tick9 ids: True
```

Both depended-on ids resolve to real tick-9 rows, so the edge is satisfied by named prior events, not by a dangling string. Dangling/self-reference scan across all five JSON files (entity_id, place_id, source_id, depends_on, relation endpoints, claim source_ids, first_appearance):

```
DANGLING/SELF REFS: NONE
```

The two tick-9 events remain distinct occasions at distinct places (`quiet-rise` vs `salt-court`), and the tick-10 event is at a third place (`chalk-stair`), so the new occasion does not rewrite or merge the inherited entries.

## 4. Inherited r88 records parsed-value identical — PASS (0 field-level differences)

Method: load both fixtures, key rows by `id`, compare with Python `!=` on the whole row object (recursive over nested `claims` arrays), then report every differing field by name. Command and observed output:

```
$ cd corpus/fixtures && python3 - <<'EOF'  (recursive row comparison)
--- sources.json: r88 ids=['paired-clock', 'veil-verse'] | r94 ids=['crossing-minute', 'paired-clock', 'veil-verse'] | shared=['paired-clock', 'veil-verse'] | r94-only=['crossing-minute']
  IDENTICAL (parsed value): paired-clock
  IDENTICAL (parsed value): veil-verse
--- entities.json: r88 ids=['aru', 'evin', 'quiet-rise', 'salt-court'] | r94 ids=['aru', 'chalk-stair', 'evin', 'quiet-rise', 'salt-court'] | shared=['aru', 'evin', 'quiet-rise', 'salt-court'] | r94-only=['chalk-stair']
  IDENTICAL (parsed value): aru
  IDENTICAL (parsed value): evin
  IDENTICAL (parsed value): quiet-rise
  IDENTICAL (parsed value): salt-court
--- timeline.json: r88 ids=['aru-ninth-bell', 'evin-ninth-bell'] | r94 ids=['aru-ninth-bell', 'evin-ninth-bell', 'paired-crossing-decision'] | shared=['aru-ninth-bell', 'evin-ninth-bell'] | r94-only=['paired-crossing-decision']
  IDENTICAL (parsed value): aru-ninth-bell
  IDENTICAL (parsed value): evin-ninth-bell
TOTAL FIELD-LEVEL DIFFS IN SHARED ROWS = 0
```

No field-level difference was found in any shared row. Nothing was added to, removed from, or rewritten inside an inherited record — including the nested `claims[0].statement` / `source_id` text and the inherited empty `depends_on` arrays.

Key-order check (stronger than value equality; catches a silent reordering/regeneration of the rows):

```
sources.json paired-clock key-order r88= ['id','title','kind','reliability_note'] r94= same_order= True
sources.json veil-verse   key-order r88= ['id','title','kind','reliability_note'] r94= same_order= True
entities.json aru/evin/quiet-rise/salt-court key-order ['id','kind','name','first_appearance','claims'] same_order= True (all four)
timeline.json aru-ninth-bell/evin-ninth-bell key-order ['id','tick','entity_id','place_id','depends_on','description','source_id'] same_order= True (both)
```

`r94-only` rows are exactly the declared additions: source `crossing-minute`, entity `chalk-stair`, event `paired-crossing-decision`. The new relation row `{"from":"aru","to":"evin","type":"agreed_co_stewardship_for_this_crossing","source_id":"crossing-minute"}` has both endpoints present in `entities.json` and its `source_id` present in `sources.json` (covered by the dangling scan above). `contradictions.json` is empty in both fixtures, consistent with "unchanged facts are not contradictions".

## 5. Content pin (reproducibility)

```
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  r94-paired-crossing/contradictions.json
026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b  r94-paired-crossing/entities.json
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  r94-paired-crossing/relations.json
2b627c4c166edf44e1e54bb006964a00e267ab4a4ce0b7b7c0681a0d9f0355d5  r94-paired-crossing/sources.json
f0209f90a6ce795211369bd900ac1d333d16eb0af123f1b170831e192660533c  r94-paired-crossing/timeline.json
ed9527c551049a6964adc872fbff722b4bdd6a53aa8713fbb6a5d92254e89a47  r94-paired-crossing/claim-excerpt-map.md
aa252416abc2c863ec4ae86cf25bd4f6e6e841d89e8586255b53362897282d63  r88-m3-maya-cluster/sources.json
042b6cc0d70c4d747121d9b277ac031cf21e66822d3c9a3e5ffe0282bba2bddc  r88-m3-maya-cluster/entities.json
f74c664b17fd8d575235ab59432a0ce6f938380e9b5a8d07640aae1d38773493  r88-m3-maya-cluster/timeline.json
```

(`sha256sum`; run from `corpus/fixtures`. Checksums confirm the compared bytes are the committed WORK-candidate bytes at HEAD `65a9329`.)

---

## Findings summary

| # | C1 structural claim | Result | Evidence |
|---|---|---|---|
| 1 | `check_bible.py` CLEAN, exit 0 | PASS | exit 0, "0 violations", empty stderr |
| 2 | 5 entities / 1 relation / 3 events | PASS | parsed `len` 5/1/3; r88 delta 4/0/2 |
| 3 | tick-10 `depends_on` lists both tick-9 ids | PASS | `["aru-ninth-bell","evin-ninth-bell"]`, set-equality True, no dangling refs |
| 4 | inherited r88 records parsed-value identical | PASS | 0 field-level diffs across 8 shared rows; key order also identical |
| 5 | 14 map obligations + separate editorial rows | PASS | map line 3 scope text; 14 distinct pointers; `support_check.py` receipt 14/2/16 |

No failure, contradiction, or field-level drift was observed. One honest boundary: this seat verified structure, counts, identity, and the dependency edge — it did **not** perform whole-claim entailment review of the new minute's propositions, which the wave spec assigns to independent manual FOLLOW-UP review. `check_bible` CLEAN and `support_check` PASS are both lexical/structural preflights and are reported here only as such.

**Bottom line: PASS — `check_bible.py` exits 0 CLEAN on `r94-paired-crossing`, parsed counts are exactly 5/1/3, the tick-10 event depends on both `aru-ninth-bell` and `evin-ninth-bell` with zero dangling references, and all 8 shared r88 source/entity/event rows are parsed-value identical with identical key order (0 field-level diffs).**
