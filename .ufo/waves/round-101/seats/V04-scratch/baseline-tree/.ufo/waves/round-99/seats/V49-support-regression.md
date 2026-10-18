# V49 — support-regression (round 99)

**Seat role (as declared):** `support_check` receipts r87–r99 replay unchanged (quote all). Leaf seat; report-only on the live tree. Writes only under `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V49-scratch/` and this report. No commits, no pushes, no network, no nested agents.

**Baseline:** r98 closure `4265df5`. Every command below ran from the lane root `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. HEAD at seat start was `337f0fa` (the blocked-dispatch log commit); the wave tree is uncommitted. Declared r99 text read from `LOG.md` lines 3200–3265 (standing declaration; the blocked-attempt section below it is not a completed round).

**Axes for this seat:** (1) receipt identity of r87–r98 against the r98 V47 files; (2) r99 receipt matches the delivered map's declared inventory and is stable across replays; (3) `support_check.py` immutability; (4) evidence is quoted commands and observed output, not a plan; (5) poll completeness recorded, including absences.

**Status: COMPLETE (2026-10-17, 22:01–22:36).** Receipt battery measured on delivered fixture bytes. Poll of the full producer set hit `POLL_TIMEOUT` at try 40; the missing items are not `support_check` inputs. Final re-run is in §7.

## 1. Precondition — the tool under test is untouched

```
$ sha256sum corpus/tools/support_check.py
55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  corpus/tools/support_check.py
$ git show 4265df5:corpus/tools/support_check.py | sha256sum
55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  -
$ git diff --stat 4265df5 -- corpus/tools/support_check.py | wc -l
0
```

Same hash the r98 V47 seat recorded (`55a5eb27…`). Re-checked at the final battery (22:34:02) and again at report write (22:36:05): still `55a5eb27…`, diff-stat lines vs `4265df5` still 0.

Historical clusters r87–r98, every file vs `4265df5` (`git show` byte compare, re-run after the final battery): `historical_diffs 0`. Counts: r87 14 files, r88 11, r89 8, r93 11, r94–r98 10 each. Map hashes (live = `4265df5`):

```
r87-myth-cluster/claim-excerpt-map.md                 3ad4e810c56e737d505a1963dfb1ffe23498045f5d81d8810e2ce6b779876f1a
r88-m3-maya-cluster/claim-excerpt-map.md              b3b79fe5b5b9272b898b5714291739503c4250c415b3959032fcdba84a73fd43
r89-inspiration-paraphrase/claim-to-excerpt-map.md    7251406154f35d5557874fa17527a88cfc1a0d969c133b94225cb4aa83b21fc8
r93-m2-kojiki-cluster/claim-excerpt-map.md            17f0e8123f26e4f7c534c01a6fe843fe0e8e1278858c0b0ce74623cb7291f7d6
r94-paired-crossing/claim-excerpt-map.md              ed9527c551049a6964adc872fbff722b4bdd6a53aa8713fbb6a5d92254e89a47
r95-crossing-aftermath/claim-excerpt-map.md           80440d61122488a267a4f0a58a55cb54d89c037d93160f1123e5fb3b2f396f61
r96-crossing-response/claim-excerpt-map.md            e851f068cfd7ed02c97054df18729c4c5a9b8bf60d99d7c9116f427d765440de
r97-crossing-acknowledgment/claim-excerpt-map.md      49d4834e124fa6cfaa1a73cd5d1a7bc2cb59711c6233b418fe7485a17eedc94f
r98-clerk-filing/claim-excerpt-map.md                 c1099d0ee9eece241ea1f796320a84453dfc6b6aec33b7b9dd7e39bbef4a94ba
```

Corpus porcelain vs `4265df5` at 22:36:05 (whole `corpus/` + `SKILL.md`):

```
 M corpus/tools/dependency-freeze-contract.json
 M corpus/tools/dependency_freeze.py
?? corpus/fixtures/r99-window-lapse/
```

No r87–r98 fixture byte changed. `corpus/tools/README.md` and `SKILL.md` were not modified in this wave as of 22:36:05. `support_check.py` is not in the change set.

## 2. Poll-wait record

Pollers: `V49-scratch/poll.sh` (tries 1–15) then `V49-scratch/poll-cont.sh` (tries 16–40). Cadence 20 s. Condition: five producer reports `S1-*.md`…`S5-*.md`, `corpus/tools/README.md` modified, `corpus/knowledge/r99-lapse-scope-note.md` present, `corpus/knowledge/r99-gate-blind-spot-table.md` present, and the r99 map containing `21 JSON facts`. SELF was never counted. Log: `V49-scratch/poll.log`.

| Time (try) | reports | tools_readme_mod | dep_freeze_mod | lapse_note | blind_table | r99_map | inv21 |
|---|---|---|---|---|---|---|---|
| 22:01:56–22:02:36 (1–3) | 1 | 0 | 1 | 0 | 0 | 1 | 0 |
| 22:02:56–22:03:36 (4–6) | 1 | 0 | 1 | 0 | 0 | 1 | 1 |
| 22:03:56 (7) | 2 | 0 | 1 | 0 | 0 | 1 | 1 |
| 22:04:16–22:06:36 (8–15) | 2 | 0 | 2 | 0 | 0 | 1 | 1 |
| stall | tool timeout killed `poll.sh` after try 15; resumed 22:17:07 at try 16 (recorded, not a skipped try) | | | | | | |
| 22:17:07–22:25:08 (16–40) | 2 | 0 | 2 | 0 | 0 | 1 | 1 |
| 22:25:08 | `POLL_TIMEOUT after 40 tries` (exit 1) | | | | | | |

Tries 1–3 of the log wrap `inv21`/`ns` onto extra lines (`0` then `0`) because `grep -c … || echo 0` prints grep's own `0` and then echo's `0`. From try 4 the line is single-line. The table above is the corrected reading of that log, not a second measurement.

Present at timeout and still present at 22:36:05: `S3-fixture-author.md` (22:01, 5069 bytes), `S4-fixture-docs.md` (22:03, 9303 bytes), the ten `corpus/fixtures/r99-window-lapse/` files, and modified `dependency_freeze.py` + `dependency-freeze-contract.json` (S1 bytes landed; S1 report did not).

**ABSENT at try 40 and still absent at 22:36:05** (not `support_check` inputs; not graded as receipts):

- `S1-*.md`, `S2-*.md`, `S5-*.md`
- `corpus/knowledge/r99-lapse-scope-note.md`
- `corpus/knowledge/r99-gate-blind-spot-table.md`
- `corpus/tools/README.md` unmodified; `SKILL.md` unmodified

No plan was verified. The 22:01 r99 probe below was an in-flight r98 map copy and is not the claimed receipt.

## 3. Discarded early probe (not the claimed r99 receipt)

At 22:01:45 the r99 map was still the r98 byte-copy (`sha256 c1099d0ee9eece241ea1f796320a84453dfc6b6aec33b7b9dd7e39bbef4a94ba`, inventory line `20 JSON facts; … 22 total mapped rows; 18 distinct excerpt anchors`).

```
$ python3 corpus/tools/support_check.py corpus/fixtures/r99-window-lapse
EXIT=0
SHA=090fa430b8a3aff279bbb09fb07060b0020e76d1fa4dda59db2cc278742e7926
```

`cmp` of that stdout against the same-minute r98 pass1 stdout: `r99 early receipt BYTE-IDENTICAL to r98 pass1`. S3's report (written 22:01) says the same thing: README and map still said r98, and `support_check` should be expected to see the inherited r98 map until S4 landed. That sentence was true at 22:01 and stale after 22:02:39. It is recorded, not claimed.

## 4. Receipt battery — r87 → r99 (quoted in full)

Command per cluster: `python3 corpus/tools/support_check.py corpus/fixtures/<cluster>`. Exit captured immediately. Stderr empty (0 bytes) on every run below. Pass-1 files are `V49-scratch/receipts/<cluster>.pass1.out` (r87–r98, 22:01:45). Delivered r99 is `r99-window-lapse.passA.out` (22:03:51), on map `d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d`.

### r87-myth-cluster — EXIT=0 — sha256 `952354ac759646a2ee4b0f6c14c8ddf8202bb311d12aff11db8309a23e991b95`

```
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 8/8; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 22/22
ANCHORS repeated-references=0; DUPLICATE-ROWS 0
PASS E1: source-support; mode=verbatim; anchor=found; 7:> I am Hara, keeper of the Mother-Tide Gate.
PASS E2: source-support; mode=verbatim; anchor=found; 7:> I, Sen, serve as recorder at Ash-Dune Sanctuary.
PASS E3: source-support; mode=verbatim; anchor=found; 8:> Place of keeping: Ash-Dune Sanctuary is a record-keeping place.
PASS E4: source-support; mode=verbatim; anchor=found; 9:> Shellweavers signed this charter as a signatory faction.
PASS E5: source-support; mode=verbatim; anchor=found; 10:> Reedwardens signed this charter as a signatory faction.
PASS E6: source-support; mode=verbatim; anchor=found; 11:| 1 | We carried the Reed Bell for the low-water signal. |
PASS R1: source-support; mode=verbatim; anchor=found; 11:> By this charter, Shellweavers stand allied with Reedwardens.
PASS R2: source-support; mode=verbatim; anchor=found; 12:> By this charter, Reedwardens stand allied with Shellweavers.
PASS R3: source-support; mode=verbatim; anchor=found; 13:> Watch clause: Under this charter's pledge, Shellweavers keep watch with the Reed Bell.
PASS R4: source-support; mode=verbatim; anchor=found; 9:> At Ash-Dune Sanctuary, Sen kept the register.
PASS T1: source-support; mode=verbatim; anchor=found; 8:> I sounded the Reed Bell at the Mother-Tide Gate before the Moon-Basin Vow, at the first low-water bell.
PASS T2: source-support; mode=verbatim; anchor=found; 12:| 2 | At Ash-Dune Sanctuary, Sen's tally records the return of the first low-water signal before the Moon-Basin Vow. |
PASS T3: source-support; mode=verbatim; anchor=found; 9:> I record the single Moon-Basin Vow of Saltmonth 4 at the Mother-Tide Gate during the first low-water bell.
PASS T4: source-support; mode=verbatim; anchor=found; 10:> I record that same single Moon-Basin Vow of Saltmonth 4 at Ash-Dune Sanctuary during the first low-water bell.
PASS H1: editorial-row; mode=verbatim; anchor=found; 5:> At low water we set the shell ring beside the bowl at the Mother-Tide Gate.
PASS H2: editorial-row; mode=verbatim; anchor=found; 5:> At low water we set the shell ring beside the bowl at the Mother-Tide Gate.
PASS H3: editorial-row; mode=verbatim; anchor=found; 5:> At low water we set the shell ring beside the bowl at the Mother-Tide Gate.
PASS H4: editorial-row; mode=verbatim; anchor=found; 5:> At low water we set the shell ring beside the bowl at the Mother-Tide Gate.
PASS H5: editorial-row; mode=verbatim; anchor=found; 6:> The bowl keeps no name, and no voice owns the tide.
PASS H6: editorial-row; mode=verbatim; anchor=found; 6:> The bowl keeps no name, and no voice owns the tide.
PASS H7: editorial-row; mode=verbatim; anchor=found; 7:> We pass the reed-bell hand to hand and let the water return it.
PASS H8: editorial-row; mode=verbatim; anchor=found; 7:> We pass the reed-bell hand to hand and let the water return it.
RECEIPT JSON-FACTS 14; EDITORIAL-ROWS 8; TOTAL-ROWS 22
SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 8/8; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22; VALIDATED-ROWS 22/22
RESULT PASS
```

### r88-m3-maya-cluster — EXIT=0 — sha256 `b5c4075d65284f3d73cde11bc09b6f3678010474a291705ed3fd7be6830e2e3b`

```
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12; DISTINCT-ANCHORS 8/8
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
PASS P1: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS P2: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS P3: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS P4: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS E1: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS E2: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS E3: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS E4: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS T1: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS T2: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS S1: editorial-row; mode=verbatim; anchor=found; 5:> The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that event. […] He called out “Earth,” and the solid land appeared.
PASS S2: editorial-row; mode=verbatim; anchor=found; 5:> The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that event. […] He called out “Earth,” and the solid land appeared.
RECEIPT JSON-FACTS 10; EDITORIAL-ROWS 2; TOTAL-ROWS 12
SOURCE-SUPPORT 10/10; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 12/12; VALIDATED-ROWS 12/12
RESULT PASS
```

### r89-inspiration-paraphrase — EXIT=0 — sha256 `ec3cd3fb29b7c0e619ed471ed02742b69dc7bfe9479944298919f131447786c8`

Map name is the fallback `claim-to-excerpt-map.md`. The one row is `retelling-support-only` (`paraphrase`) and contributes 0 to `SOURCE-SUPPORT`.

```
INVENTORY JSON-FACTS 1/1; EDITORIAL-ROWS 0/0; TOTAL-ROWS 1/1; DISTINCT-ANCHORS 1/1
ANCHORS repeated-references=0; DUPLICATE-ROWS 0
PASS entities.json#/0/claims/0: retelling-support-only; anchor=found; mode=paraphrase; 9:A modern paraphrase says that the keeper later summarized the ledger for the court: the tide-mark had been moved to the west stair.
RECEIPT JSON-FACTS 1; EDITORIAL-ROWS 0; TOTAL-ROWS 1
SOURCE-SUPPORT 0/0; EDITORIAL-ANCHORS 0/0; RETELLING-SUPPORT-ONLY 1 entries (1/1 anchors); MODES 1/1; VALIDATED-ROWS 1/1
RESULT PASS
```

### r93-m2-kojiki-cluster — EXIT=0 — sha256 `63f90ea53c14708882932dba8eb3c2ced411ea96008d127a86300abc90e7e6da`

```
INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15; DISTINCT-ANCHORS 15/15
ANCHORS repeated-references=0; DUPLICATE-ROWS 0
PASS E1: source-support; mode=verbatim; anchor=found; 5:M-17 identifies Teva as the initial recorder and names the Slate Table as its filing place.
PASS E2: source-support; mode=verbatim; anchor=found; 6:Teva names the paper folio "Lorn Index" as the sheet she opened for the check.
PASS E3: source-support; mode=verbatim; anchor=found; 7:Orni writes on the margin: "not weighed; mark unmeasured."
PASS E4: source-support; mode=verbatim; anchor=found; 8:The folio identifies Teva and Orni as its two annotators.
PASS E5: source-support; mode=verbatim; anchor=found; 5:M-17 identifies Teva as the initial recorder and names the Slate Table as its filing place.
PASS E6: source-support; mode=verbatim; anchor=found; 9:The inventory lists the Slate Table as the place holding the folio.
PASS E7: source-support; mode=verbatim; anchor=found; 6:Teva names the paper folio "Lorn Index" as the sheet she opened for the check.
PASS E8: source-support; mode=verbatim; anchor=found; 12:The register gives no measured weight for the Lorn Index.
PASS E9: source-support; mode=verbatim; anchor=found; 10:Entry A: Teva files the Lorn Index on the Slate Table.
PASS E10: source-support; mode=verbatim; anchor=found; 11:Entry B: after Entry A, Orni adds "not weighed; mark unmeasured" to the Lorn Index at the Slate Table.
PASS E11: source-support; mode=verbatim; anchor=found; 10:Entry A: Teva files the Lorn Index on the Slate Table.
PASS E12: source-support; mode=verbatim; anchor=found; 11:Entry B: after Entry A, Orni adds "not weighed; mark unmeasured" to the Lorn Index at the Slate Table.
PASS S1: editorial-row; mode=translation; anchor=found; 8:> Then the whole Plain of High Heaven was obscured and all the Central Land of Reed-Plains darkened. Owing to this, eternal night prevailed.
PASS S2: editorial-row; mode=translation; anchor=found; 9:> Therefore did the eight hundred myriad deities assemble in a divine assembly in the bed of the Tranquil River of Heaven, […]
PASS S3: editorial-row; mode=translation; anchor=found; 10:> So when the Heaven-Shining-Great-August deity had come forth, both the Plain of High Heaven and the Central-Land-of-Reed-Plains of course again became light.
RECEIPT JSON-FACTS 12; EDITORIAL-ROWS 3; TOTAL-ROWS 15
SOURCE-SUPPORT 12/12; EDITORIAL-ANCHORS 3/3; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 15/15; VALIDATED-ROWS 15/15
RESULT PASS
```

### r94-paired-crossing — EXIT=0 — sha256 `d0ff69820d619bc5a5350efa96522effcb991f6243588ff3db16a4383ba17e15`

```
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16; DISTINCT-ANCHORS 12/12
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
PASS S01: editorial-row; mode=verbatim; anchor=found; 5:> The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that event. […] He called out “Earth,” and the solid land appeared.
PASS S02: editorial-row; mode=verbatim; anchor=found; 5:> The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that event. […] He called out “Earth,” and the solid land appeared.
RECEIPT JSON-FACTS 14; EDITORIAL-ROWS 2; TOTAL-ROWS 16
SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 16/16; VALIDATED-ROWS 16/16
RESULT PASS
```

### r95-crossing-aftermath — EXIT=0 — sha256 `efae7be25d213fea277cc1457413e65deb2720a56c20c594aa2a8b40673b9420`

```
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17; DISTINCT-ANCHORS 13/13
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
PASS S01: editorial-row; mode=verbatim; anchor=found; 5:> The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that event. […] He called out “Earth,” and the solid land appeared.
PASS S02: editorial-row; mode=verbatim; anchor=found; 5:> The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that event. […] He called out “Earth,” and the solid land appeared.
RECEIPT JSON-FACTS 15; EDITORIAL-ROWS 2; TOTAL-ROWS 17
SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 17/17; VALIDATED-ROWS 17/17
RESULT PASS
```

### r96-crossing-response — EXIT=0 — sha256 `ca7a6815077f87e8e415588a312e3644ccaa44c5fbafb8ed3405a4b53aaf6be1`

```
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18; DISTINCT-ANCHORS 14/14
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
PASS S01: editorial-row; mode=verbatim; anchor=found; 5:> The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that event. […] He called out “Earth,” and the solid land appeared.
PASS S02: editorial-row; mode=verbatim; anchor=found; 5:> The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that event. […] He called out “Earth,” and the solid land appeared.
RECEIPT JSON-FACTS 16; EDITORIAL-ROWS 2; TOTAL-ROWS 18
SOURCE-SUPPORT 16/16; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 18/18; VALIDATED-ROWS 18/18
RESULT PASS
```

### r97-crossing-acknowledgment — EXIT=0 — sha256 `a109856d383efa18e6f19120f62aa81ac1bdcb6cfc3080703cbabfe151f921ba`

```
INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19; DISTINCT-ANCHORS 15/15
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
PASS S01: editorial-row; mode=verbatim; anchor=found; 5:> The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that event. […] He called out “Earth,” and the solid land appeared.
PASS S02: editorial-row; mode=verbatim; anchor=found; 5:> The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that event. […] He called out “Earth,” and the solid land appeared.
RECEIPT JSON-FACTS 17; EDITORIAL-ROWS 2; TOTAL-ROWS 19
SOURCE-SUPPORT 17/17; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 19/19; VALIDATED-ROWS 19/19
RESULT PASS
```

### r98-clerk-filing — EXIT=0 — sha256 `090fa430b8a3aff279bbb09fb07060b0020e76d1fa4dda59db2cc278742e7926`

```
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 18/18
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
PASS S01: editorial-row; mode=verbatim; anchor=found; 5:> The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that event. […] He called out “Earth,” and the solid land appeared.
PASS S02: editorial-row; mode=verbatim; anchor=found; 5:> The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that event. […] He called out “Earth,” and the solid land appeared.
RECEIPT JSON-FACTS 20; EDITORIAL-ROWS 2; TOTAL-ROWS 22
SOURCE-SUPPORT 20/20; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22; VALIDATED-ROWS 22/22
RESULT PASS
```

### r99-window-lapse (delivered map) — EXIT=0 — sha256 `03a1dfd5c7722eb7c2810871f6c693e1770b39086a37261262721053a5981f73`

Measured 22:03:51 after the map's inventory line became `21 JSON facts; 2 editorial rows; 23 total mapped rows; 19 distinct excerpt anchors` (map sha256 `d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d`; excerpt sha256 `fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d`). Immediate re-run (pass B) `cmp`: IDENTICAL, same sha256.

```
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
```

That matches the map's own inventory line and C2's declared "21 map obligations (20 inherited rows unchanged + 1 new event row)". J21's anchor is inside the declared span 66–76 (hit at excerpt line 70). `ANCHORS repeated-references=4` is the inherited repeated anchor, unchanged from r88/r94–r98. `DUPLICATE-ROWS 0`. No `WARN:` and no `FAIL:`.

`diff -u` of the r98 pass1 stdout against this r99 stdout moves only the two count lines and adds one row. No inherited PASS line moves:

```
-INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 18/18
+INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23; DISTINCT-ANCHORS 19/19
 ANCHORS repeated-references=4; DUPLICATE-ROWS 0
 ... J01–J20 and S01/S02 unchanged ...
+PASS J21: source-support; mode=verbatim; anchor=found; 70:> Tick 15: The crossing-window named in the original minute has closed.
-RECEIPT JSON-FACTS 20; EDITORIAL-ROWS 2; TOTAL-ROWS 22
-SOURCE-SUPPORT 20/20; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22; VALIDATED-ROWS 22/22
+RECEIPT JSON-FACTS 21; EDITORIAL-ROWS 2; TOTAL-ROWS 23
+SOURCE-SUPPORT 21/21; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 23/23; VALIDATED-ROWS 23/23
 RESULT PASS
```

## 5. Cross-round byte identity

`cmp -s` of each r87–r98 pass1 stdout against the r98 V47 seat's saved `*.pass2.out` under `.ufo/waves/round-98/seats/V47-scratch/receipts/`:

```
IDENTICAL r87-myth-cluster vs r87-myth-cluster.pass2.out
IDENTICAL r88-m3-maya-cluster vs r88-m3-maya-cluster.pass2.out
IDENTICAL r89-inspiration-paraphrase vs r89-inspiration-paraphrase.pass2.out
IDENTICAL r93-m2-kojiki-cluster vs r93-m2-kojiki-cluster.pass2.out
IDENTICAL r94-paired-crossing vs r94-paired-crossing.pass2.out
IDENTICAL r95-crossing-aftermath vs r95-crossing-aftermath.pass2.out
IDENTICAL r96-crossing-response vs r96-crossing-response.pass2.out
IDENTICAL r97-crossing-acknowledgment vs r97-crossing-acknowledgment.pass2.out
IDENTICAL r98-clerk-filing vs r98-clerk-filing.pass2.out
```

Those nine hashes are the same full sha256 the r98 seat recorded by 16-hex prefix (`952354ac…`, `b5c4075d…`, `ec3cd3fb…`, `63f90ea5…`, `d0ff6982…`, `efae7be2…`, `ca7a6815…`, `a109856d…`, `090fa430…`). r87/r88/r93/r94 therefore still match the r95 V52 manifest, and r89/r95/r96/r97 still match the r97 V52 manifest, by transitivity of those `cmp`s plus the r98 seat's recorded identity. This seat did not re-open the r95/r97 files; the identity claim against them is that transitive one.

S4's report independently quotes the same r99 terminal lines (`INVENTORY … 21/21 … 23/23 … 19/19`, `SOURCE-SUPPORT 21/21 … MODES 23/23`, `RESULT PASS`, `support_exit=0`) and the same J21 line (`anchor=found; 70:> Tick 15: …`). S4's quoted delivered README sha256 `b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049` matches the live README at 22:31:51 and at the post-battery check. README edits do not enter `support_check` (it reads the map and excerpts only).

## 6. Bounds

- `support_check` is a lexical preflight (declared inventory, fixed-string anchors, declared spans, R9 mode consistency). None of these receipts proves entailment, mode fidelity beyond the declared token, source authentication, chronology, rights, permission, or canon. The r99 content claims (6/1/8, lapse bound, census 172→173, freeze pinning) belong to S3/S4/S5/S1 and the C2 seats. This seat only replays the map↔excerpt receipt.
- Not verified here, and not claimed: S1's `dependency_freeze` C1 behavior (bytes are modified; the report is absent), S2's README/SKILL freeze row (files unmodified as of 22:36:05; report absent), S5's blind-spot table and lapse note (both files absent; report absent).
- The 22:01 r99 stdout is not a regression. It is the receipt of an in-flight r98 map copy, discarded once the 21-row map landed.
- Write-scope: this seat wrote only `V49-scratch/**` and this report. No live fixture byte was modified by this seat. Historical fixture identity was re-checked after the battery (`historical_diffs 0`). r99 map sha256 after the battery was still `d2fe20e5…`; excerpt sha256 still `fefebaf9…`.

## 7. Final status after the poll window

**Poll outcome: `POLL_TIMEOUT after 40 tries` at 22:25:08.** Still absent at 22:36:05: S1/S2/S5 reports, both r99 knowledge files, and any edit to `corpus/tools/README.md` or `SKILL.md`. Present and stable: S3 and S4 reports, the delivered r99 fixture, and S1's two freeze files (modified, unread by this tool). Bounded stall: the first poller was killed by a 300 s tool cap after try 15 (22:06:36) and resumed at try 16 (22:17:07); that gap is recorded in `poll.log` and is not a skipped try. No stall-escape was used to grade a missing artifact.

Final battery 22:34:02, same command, stdout saved as `*.final.out`. Observed log (`V49-scratch/logs/final-battery.txt`):

```
support_check 55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  corpus/tools/support_check.py
diffstat_vs_4265df5 0
r87-myth-cluster EXIT=0 SHA=952354ac759646a2ee4b0f6c14c8ddf8202bb311d12aff11db8309a23e991b95 vs-r98-pass2=IDENTICAL stderr_bytes=0
r88-m3-maya-cluster EXIT=0 SHA=b5c4075d65284f3d73cde11bc09b6f3678010474a291705ed3fd7be6830e2e3b vs-r98-pass2=IDENTICAL stderr_bytes=0
r89-inspiration-paraphrase EXIT=0 SHA=ec3cd3fb29b7c0e619ed471ed02742b69dc7bfe9479944298919f131447786c8 vs-r98-pass2=IDENTICAL stderr_bytes=0
r93-m2-kojiki-cluster EXIT=0 SHA=63f90ea53c14708882932dba8eb3c2ced411ea96008d127a86300abc90e7e6da vs-r98-pass2=IDENTICAL stderr_bytes=0
r94-paired-crossing EXIT=0 SHA=d0ff69820d619bc5a5350efa96522effcb991f6243588ff3db16a4383ba17e15 vs-r98-pass2=IDENTICAL stderr_bytes=0
r95-crossing-aftermath EXIT=0 SHA=efae7be25d213fea277cc1457413e65deb2720a56c20c594aa2a8b40673b9420 vs-r98-pass2=IDENTICAL stderr_bytes=0
r96-crossing-response EXIT=0 SHA=ca7a6815077f87e8e415588a312e3644ccaa44c5fbafb8ed3405a4b53aaf6be1 vs-r98-pass2=IDENTICAL stderr_bytes=0
r97-crossing-acknowledgment EXIT=0 SHA=a109856d383efa18e6f19120f62aa81ac1bdcb6cfc3080703cbabfe151f921ba vs-r98-pass2=IDENTICAL stderr_bytes=0
r98-clerk-filing EXIT=0 SHA=090fa430b8a3aff279bbb09fb07060b0020e76d1fa4dda59db2cc278742e7926 vs-r98-pass2=IDENTICAL stderr_bytes=0
r99-window-lapse EXIT=0 SHA=03a1dfd5c7722eb7c2810871f6c693e1770b39086a37261262721053a5981f73 vs-passA=IDENTICAL stderr_bytes=0
FAILFLAG=0
```

A second r99 re-run immediately after (`r99-window-lapse.final2.out`) was `cmp` IDENTICAL to `final.out`, `passA.out`, and `passB.out` (four files, one sha256 `03a1dfd5…`, all EXIT=0). r99 is therefore stable across four runs on the delivered map, from 22:03:51 through 22:34:02, while the map hash stayed `d2fe20e5…`.

**Bottom line: PASS — every `support_check` receipt r87→r99 replays on the delivered bytes (r87 14+8, r88 10+2, r89 1 paraphrase, r93 12+3, r94 14+2, r95 15+2, r96 16+2, r97 17+2, r98 20+2, r99 21+2; all `RESULT PASS`, exit 0, stderr empty; r87–r98 stdout `cmp` IDENTICAL to the r98 V47 `*.pass2.out` files; r99 `03a1dfd5…` stable across four runs and differs from r98 only by the count lines plus `PASS J21` at excerpt line 70). Poll of the full producer set is `POLL_TIMEOUT` at try 40: S1/S2/S5 reports and both r99 knowledge files remain ABSENT and were not graded; they are not `support_check` inputs. The 22:01 r99 probe was an in-flight r98 map copy and is not the claimed receipt.**
