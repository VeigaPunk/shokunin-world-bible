# V09 — c2-inherited-equality (round 95)

Seat: V09, verifier. Scope: parsed-value equality of every inherited row of
`corpus/fixtures/r95-crossing-aftermath/` vs `corpus/fixtures/r94-paired-crossing/`
(entities 5, relations 1, timeline first 3, sources first 3, contradictions);
git confirmation that `corpus/fixtures/r94-paired-crossing/` is byte-untouched this
round; byte-prefix confirmation for `fictional-excerpts.md` and `source-excerpt.md`
where P3 claimed it. Read-only; no commits; this report is the only write.

Baseline: HEAD `fb118c42038ed27a747eec704b9aab41bb4b2ebe` (r94 closure `fb118c4`).
Verified at 2026-10-17T16:21–16:23-03:00 against P3's delivered artifacts and report
`.ufo/waves/round-95/seats/P3-fixture-json.md` (complete; ends with its own bottom line).

## Step 0 — poll-wait for P3

20 s cadence loop over `corpus/fixtures/r95-crossing-aftermath/` file count and
`.ufo/waves/round-95/seats/P3-*.md`:

```
try 1-3: files=0 p3report=none
try 4-9: files=8 p3report=none
try 10:  files=8 p3report=.ufo/waves/round-95/seats/P3-fixture-json.md
try 11-12: files=8
try 13:  files=9
```

At verification time the dir holds all 10 files (8 P3-owned + P4's `README.md` and
`claim-excerpt-map.md`, both mtime 16:21). P3's report is complete; nothing ABSENT.

## Step 1 — r94 fixture byte-untouched via git

```
$ git rev-parse HEAD
fb118c42038ed27a747eec704b9aab41bb4b2ebe
$ git log --oneline -1
fb118c4 lore r94: close round — SCORECARD admitted section + LOG closure (corrections, gaps, r95 handoff)

$ git status --porcelain -- corpus/fixtures/r94-paired-crossing/
(empty)
$ git diff --quiet fb118c4 -- corpus/fixtures/r94-paired-crossing/; echo "exit=$?"
exit=0
```

Blob-level proof: `git ls-tree -r fb118c4 corpus/fixtures/r94-paired-crossing/` vs
`git hash-object` on the 10 working-tree files — **10/10 blob hashes identical**:

```
1797bd87bb585909f5f5c2bb9934afe94efef0d0  entities.json
2804ae91240dbf34753bf955d4fab9ffeab0a8df  relations.json
59d08da605c01443f2fe5163a06cee0712c99436  sources.json
7edafa24aef9f789ccbe7ed7a9aebec5584c6321  claim-excerpt-map.md
9a1864013784ded68ea235c183901cda3f0046cb  source-excerpt.md
bd25265efbd21257b54c0a7893edcdba3e2c30a2  timeline.json
c9cb17d552c01f8bbb6c5c15ee429dfcacc34eb5  fictional-excerpts.md
da3d1effb87e29719e74d7a4f1d95a773009a10d  README.md
e6b71d7e67ecff67f12606cf800576dab732c24b  inspiration-note.md
fe51488c7066f6687ef680d6bfaa4f7768ef205c  contradictions.json
```

Supplement: all r94 file mtimes are 14:45:46–14:59:33, before the r95 dispatch
window (~16:16+), consistent with untouched-in-r95.

## Step 2 — parsed-value equality (json.load, key-order sensitive)

Method: `json.load(..., object_pairs_hook=OrderedDict)`; OrderedDict-vs-OrderedDict
equality is order-sensitive (nested objects included). Order-sensitivity self-witness
in the same run: `OrderedDict([("b",1),("a",2)]) != OrderedDict([("a",2),("b",1)])`
→ `True`, so reordered keys would fail this check.

Observed:

```
entities count r94/r95: 5 5
entities whole parsed-equal (OrderedDict, key-order sensitive): True
relations count r94/r95: 1 1
relations whole parsed-equal: True
contradictions count r94/r95: 0 0
contradictions whole parsed-equal: True
sources count r94/r95: 3 4
sources[:3] parsed-equal: True
timeline count r94/r95: 3 4
timeline[:3] parsed-equal: True
```

New rows (delta, out-of-inheritance but consistent with the C2 spec):

```
sources[3]: {"id":"aru-aftermath-note","title":"Aru's Chalk Stair Aftermath Note",
"kind":"fictional first-person note","reliability_note":"Newly authored fictional note; …"}
timeline[3]: {"id":"aftermath-missing-evin","tick":11,"entity_id":"aru","place_id":"chalk-stair",
"depends_on":["paired-crossing-decision"],"description":"…","source_id":"aru-aftermath-note"}
```

So 12 inherited rows (5+1+0+3+3), all parsed-value identical; entities/relations
whole-file equality also proves no new entities, no new relations, and no new claims
rows. Note: P3's report says "all 14 inherited rows are value-identical" — the JSON
tables hold **12** inherited rows (14 is the map-obligation count from the round spec);
the equality claim itself holds for every inherited row present. Minor count-label
discrepancy, not a substantive one.

## Step 3 — byte checks (cmp)

```
$ for f in entities.json relations.json contradictions.json inspiration-note.md source-excerpt.md; do cmp -s $R94/$f $R95/$f; done
cmp entities.json: IDENTICAL
cmp relations.json: IDENTICAL
cmp contradictions.json: IDENTICAL
cmp inspiration-note.md: IDENTICAL
cmp source-excerpt.md: IDENTICAL

fictional-excerpts sizes: r94=1116 r95=1845
$ head -c 1116 corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md | cmp - corpus/fixtures/r94-paired-crossing/fictional-excerpts.md
fictional-excerpts.md: r94 bytes are a byte-prefix of r95   (P3 claimed strict byte-prefix, cur[:1116] → VERIFIED)

source-excerpt sizes: r94=640 r95=640
$ head -c 640 corpus/fixtures/r95-crossing-aftermath/source-excerpt.md | cmp - corpus/fixtures/r94-paired-crossing/source-excerpt.md
source-excerpt.md: r94 bytes are a byte-prefix of r95   (P3 claimed byte-identical; 640=640 → VERIFIED as full equality)
```

Direct blob cross-check of the five r95 full copies vs `fb118c4` blobs (not just the
working tree): `git hash-object r95/<f>` vs `git rev-parse fb118c4:…/<f>` →
entities.json MATCH `1797bd87bb585909f5f5c2bb9934afe94efef0d0`, relations.json MATCH
`2804ae91240dbf34753bf955d4fab9ffeab0a8df`, contradictions.json MATCH
`fe51488c7066f6687ef680d6bfaa4f7768ef205c`, inspiration-note.md MATCH
`e6b71d7e67ecff67f12606cf800576dab732c24b`, source-excerpt.md MATCH
`9a1864013784ded68ea235c183901cda3f0046cb`.

Delivered sha256 reproduce P3's report table exactly:

```
fd9e30e8d9ad40013be2172781d13d84ba219377c8433ff6e529ea8e1927e64a  sources.json
3c0faad6bf32f944f9f2a20f3bd15829044afa04f1a8837601903433b00ea177  timeline.json
0ef6734ae52d28656e75869d942d6b1e8e324b116977a2811b3b36dc0880b282  fictional-excerpts.md
026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b  entities.json
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  relations.json
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  contradictions.json
58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37  inspiration-note.md
b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd  source-excerpt.md
```

The five unchanged copies hash-match their r94 values (same five hashes above are
also the working-tree r94 hashes). r94 hashes re-verified unchanged, e.g.
fictional-excerpts.md `585f4d0746eadffcdd13a12aa4068392820201ae668dc9b66e9154beccf495c2`,
sources.json `2b627c4c166edf44e1e54bb006964a00e267ab4a4ce0b7b7c0681a0d9f0355d5`.

## Step 4 — supplementary gate (not my seat's primary criterion)

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath
CLEAN: schema, citations, relations, timeline; 0 violations   exit=0
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r94-paired-crossing
CLEAN: schema, citations, relations, timeline; 0 violations   exit=0
```

Working-tree snapshot at verification time: `M LOG.md`, `M corpus/tools/map_obligations.py`
(P1 landed), `?? .ufo/waves/round-95/`, `?? corpus/fixtures/r95-crossing-aftermath/` —
r94 path clean. Map-dependent receipts (15/15 obligations, support_check) are other
seats' scope and were not run here.

## Verdicts (per check)

| check | verdict |
|---|---|
| r94 byte-untouched (status/diff/blob/mtime) | PASS |
| entities 5/5 whole parsed-equal, key-order sensitive | PASS |
| relations 1/1 whole parsed-equal | PASS |
| contradictions 0/0 whole parsed-equal | PASS |
| timeline first 3 parsed-equal (of 4) | PASS |
| sources first 3 parsed-equal (of 4) | PASS |
| no new entities/relations/claims rows | PASS |
| fictional-excerpts.md r94 bytes as byte-prefix | PASS |
| source-excerpt.md byte-identical (⇒ prefix) | PASS |
| check_bible CLEAN (supplementary) | PASS |

No failures, no contradictions found. One minor count-label discrepancy recorded in
Step 2 (P3 "14 inherited rows" vs actual 12 JSON rows).

Bottom line: PASS — all 12 inherited rows parsed-value identical (key-order sensitive),
r94 fixture byte-untouched at blob level, byte-prefix/byte-identity claims reproduced,
new rows match spec; P3's only slip is the "14 rows" label.
