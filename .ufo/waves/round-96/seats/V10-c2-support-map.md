# V10 — c2-support-map (round 96)

**Seat:** V10 `c2-support-map` (verifier)
**Scope:** C2/depth — run `support_check.py` and `map_obligations.py` on the delivered
`corpus/fixtures/r96-crossing-response/` and report the observed receipts (expected
JSON-FACTS 16/16, EDITORIAL-ROWS 2/2, TOTAL-ROWS 18/18, PASS; `raw=16 mapped=16` PASS),
plus any interaction with Q1's C1 hardening bundle.
**Report path:** `.ufo/waves/round-96/seats/V10-c2-support-map.md` (exclusive)
**Baseline:** r95 closure `dcb2d92`; HEAD during this run `60dba0c` (r95 SCORECARD closure)
**Scratch:** `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-96/seats/V10-scratch/`
(absolute lane path; no repo file outside this report and that scratch dir was written by
this seat — `git status` shows only producers' paths)

## 0. Poll-wait record

Target = Q5's `corpus/fixtures/r96-crossing-response/{README.md,claim-excerpt-map.md}` plus
Q5's producer report. Fixture dir absent at seat start 17:38:17 (poll try 1). Q4's tables
landed 17:38:26–17:40:16; Q5's `claim-excerpt-map.md` 17:43:09 (10172 B) and `README.md`
17:43:17 (4858 B); poll try 17 (17:43:37) reported `files_ok=1`. Q5's producer report
`.ufo/waves/round-96/seats/Q5-fixture-docs.md` was detected 17:45:35, i.e. verification
started only after both artifacts and the producer report existed. Nothing was verified
before it existed and nothing was fabricated. Fixture bytes were re-hashed before and after
every probe and are stable (section 1).

## 1. Revisions verified (all evidence below is from these bytes)

Fixture (sha256, stable 17:46 → 17:52:32; identical before/after all probes):

| File | sha256 | bytes |
|---|---|---:|
| `claim-excerpt-map.md` | `5093d72eb3f22b249033d7ac4c1a85c7df7f5e09bfa673a598aee6a83045bfd8` | 10172 |
| `README.md` | `ff52ced48bf4214721f248328d76da64a42773d44e78154ef1eaf6eb3558c456` | 4858 |
| `timeline.json` | `ea0225f9270db79685ea6f55828c2031d7ac67cd413b04f28b25770b208815b9` | 1677 |
| `sources.json` | `9f973f634cf325a33047020407ffb67b0a0f0a1643e507ebd3771abf9fabf32d` | 1741 |
| `entities.json` | `026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b` | 1449 |
| `relations.json` | `c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9` | 139 |
| `contradictions.json` | `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` | 3 |
| `fictional-excerpts.md` | `06b11bec604f6d68e4d4bc43e78093c00ce7fb8fb86c8cac153e24ee41cb2fe3` | 2588 |
| `inspiration-note.md` | `58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37` | 1956 |
| `source-excerpt.md` | `b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd` | 640 |

Tool revisions (sha256) bracketing the final receipt at 17:52:32:

- `support_check.py` `55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c` — unchanged all round (same bytes as r95's delivered revision).
- `map_obligations.py` `2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8` — stable since 17:47:31.
- `map-obligations-contract.json` `97b76bb8b1fea97f166ef7586eba69c427ec15bbe7b34eb5345ec65c936493b6` — landed 17:50:23, 24 self-test cases, stable after.

## 2. Required command 1 — `support_check.py` (expected PASS)

```
$ python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response
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
exit=0
```

**JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18; RESULT PASS, exit 0** — matches the
expectation, and the map's declared inventory line (`16 JSON facts; 2 editorial rows; 18
total mapped rows; 14 distinct excerpt anchors`) is satisfied exactly (`DISTINCT-ANCHORS
14/14`). New row J16's anchor sits at line 37 inside its declared span 33-42 (the appended
response section), i.e. the new obligation is genuinely in-span. `stderr` empty. Re-run at
17:52:32 with identical output.

## 3. Required command 2 — `map_obligations.py` (expected raw=16 mapped=16 PASS exit 0)

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response
OBLIGATIONS raw=16 mapped=16
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18
RESULT PASS
exit=0
```

**raw=16 mapped=16, RESULT PASS, exit 0** — matches the expectation, with no `FINDING` line
under the hardened revision (no `inventory_mismatch`, no `dual_pointer`, no `schema_drift`
false positive on the canonical r96 map). `stderr` empty.

Independent recount from the raw tables: `first_appearance=5 claims=5 relations=1
timeline=5 total=16`; entities 5, relations 1, events 5, sources 5, contradictions 0
(r95: 5/1/4/4, raw 15). `check_bible.py` → `CLEAN: schema, citations, relations, timeline;
0 violations`, exit 0.

## 4. C2 counting and preservation claims

| C2 claim | Measured | Verdict |
|---|---|---|
| 5 entities / 1 relation / 4→5 events / 4→5 sources | `entities.json` identical to r95 (5 records); `relations.json` identical (1); `timeline.json` r95 prefix identical + 1 new; `sources.json` r95 prefix identical + 1 new | holds |
| 15 inherited map rows carried unchanged | header-driven parse of both maps: 17/17 inherited pointer rows (15 JSON + 2 editorial S01/S02) **parse-value identical** on source ID, excerpt path, line span, R9 mode, and exact anchor; exactly one new row, `J16` | holds |
| no new claims, no new entities/relations | `entities.json`, `relations.json`, `contradictions.json` byte-identical to r95 (`cmp` → IDENTICAL); `inspiration-note.md`, `source-excerpt.md` byte-identical | holds |
| new source `evin-response-note`, new event `response-evin-salt-court` (actor `evin`, place `salt-court`, `depends_on ["aftermath-missing-evin"]`, tick 12) | exactly as declared in `sources.json`/`timeline.json` (diff vs r95 is a single appended record in each file) | holds |
| preserving copy | `fictional-excerpts.md`: r95's 31 lines are an **exact prefix** of r96's 42 lines (11 appended, starting line 32) | holds |
| `check_bible` CLEAN | `CLEAN: schema, citations, relations, timeline; 0 violations`, exit 0 | holds |
| census 169→170 | dirs under `corpus/fixtures` holding ≥1 of the 5 tables: **170 total, 169 excluding `r96-crossing-response`** | holds |
| unresolved second account, no contradiction asserted | `contradictions.json` is `[]` (3 B, byte-identical to r95); `timeline.json#/4` description and `sources.json` reliability note both state no accusation, no winner, both accounts unresolved; `fictional-excerpts.md:38-40` carries the three assertions verbatim; the two accounts name different actors at different places | holds (text-level; semantic review remains manual) |

Observed non-blocking difference, documented by Q5: the R9 excerpt-declaration row's span
moved `fictional-excerpts.md:12-29` (r95) → `12-40` (r96), matching the appended section.
This row is not one of the 17 inherited fact rows, so the "15 inherited rows unchanged"
claim is unaffected; `support_check` normalizes it to path `fictional-excerpts.md` for mode
resolution and reports `MODES 18/18`.

## 5. Q1/Q2 C1-hardening interaction observed (revision timeline)

`map_obligations.py` changed under this seat mid-verification. Sampled every 20 s
(`V10-scratch/toolrev*.log`):

| Time | `map_obligations.py` (12) | contract cases | r96 result |
|---|---|---:|---|
| 17:39:32 → 17:45:xx | `d1c239cc…` (r95 revision) | 22 | raw=16 mapped=16 **PASS** |
| 17:46:05 | `c2c284c0…` | 22 | `--self-test` → `SELF-TEST CASES 22/24 pinned` … `RESULT PASS`, exit 0 |
| 17:46:51 | `6634e176…` | 22 | — |
| 17:47:31 → 17:52:32 | `2b0ba815…` (settled) | 22 → **24 at 17:50:23** | raw=16 mapped=16 **PASS** |

Findings:

- The r96 fixture never produced a FAIL under any revision; it is PASS under the r95
  revision and under every in-flight revision observed.
- At `c2c284c0…` the tool implemented 24 cases while the persisted contract still pinned
  22; the tool reports `22/24 pinned` and still exits 0, because `load_test_expectations`
  gates only on *core* cases being present (`missing = CORE_SELF_TEST_CASES - expected`)
  and rejects *unknown* contract cases; the two new cases are additive and unpinned. Once
  Q2's contract landed (17:50:23), the settled pair prints `SELF-TEST CASES 24/24 pinned`
  … `SELF-TEST PASS schema_drift exit=1`, `SELF-TEST PASS inventory_mismatch exit=1`,
  `RESULT PASS`, exit 0 — i.e. C1(b)'s 22→24 pinning holds at the settled pair. During the
  window in between, a round that had stopped at `c2c284c0…` + 22-case contract would have
  shown an unpinned (but not failing) self-test; no such state survives at report time.
- C1 side-effects on the continuation chain at the settled revision (all run without pipes
  so the exit codes are the tool's): `r88-m3-maya-cluster` 10/10 PASS exit 0;
  `r94-paired-crossing` 14/14 PASS exit 0; `r95-crossing-aftermath` 15/15 PASS exit 0;
  `r87-myth-cluster` → `FINDING unsupported_map: pointer cells must contain one canonical
  inline-code pointer`, exit 2; `r89-c1-multi-cause-valid` → `FINDING map_missing`, exit 2.
  r87/r89 remain fail-closed as claimed.

### C1 mutation classes replayed on scratch copies of the r96 fixture

Copies under `V10-scratch/probe/`; live fixture hashes unchanged after every probe.

| Probe | r95 revision `d1c239cc…` (git `dcb2d92:corpus/tools/map_obligations.py`) | Settled `2b0ba815…` |
|---|---|---|
| `delclass2`: `entities[0].claims` key deleted **and** its J06 row removed | `OBLIGATIONS raw=15 mapped=15` / `INVENTORY … 15/16 … 17/18 MISMATCH` / `RESULT PASS` **exit 0** | same receipt plus `FINDING inventory_mismatch: declared JSON-facts/editorial-rows/total-rows 16/2/18; observed 15/2/17` / `RESULT FAIL` **exit 1** |
| `delclaims`: `claims` renamed to `assertions` **and** J06 row removed | `FINDING schema_drift` exit 1 | `FINDING inventory_mismatch` + `FINDING schema_drift` exit 1 |
| `dual2`: legacy-dialect map (`JSON fact and fields` header, `entities[0].first_appearance` cells), J01 cell naming a second pointer `entities.json#/1/first_appearance` in prose | `OBLIGATIONS raw=16 mapped=16` / `RESULT PASS` **exit 0** (silently ignored) | `FINDING dual_pointer: row J01 (line 22) names a second pointer token 'entities.json#/1/first_appearance' alongside entities.json#/0/first_appearance` / `RESULT FAIL` **exit 1** |
| `del16`: only J16's map row deleted | — | `raw=16 mapped=15`, `FINDING inventory_mismatch` + `FINDING missing_obligation: timeline.json#/4 has no map row`, exit 1 |

So the r95-carried deletion class (C1a) and V37-D1 (C1c) both close on r96 bytes, and the
new tick-12 obligation is really covered: the `inventory_mismatch` FINDING is now gating
(exit 1) rather than a non-gating receipt, and `support_check` independently fails the same
scratch copy (`FAIL: inventory JSON facts mismatch: expected=16 parsed=15`, total-rows 18/17,
distinct anchors 14/13, `RESULT FAIL`, exit 1). The two tools remain complementary:
`support_check` is map-inventory/anchor/mode driven, `map_obligations` is raw-JSON↔map
binding driven.

## 6. Limitations / not verified here

- Whole-claim entailment, canon truth, the unresolved-two-accounts reading, and rights or
  permission are manual reviews; the receipts above are lexical/map-declared only, per the
  tools' own scope statements.
- C1 and C3 are other seats' claims; only the interactions above were observed. My receipts
  are bracketed to `map_obligations.py` `2b0ba815…` + contract `97b76bb8…` (24 cases) at
  17:52:32; if either changes again, sections 2–5 must be re-run.
- `corpus/tools/dependency_freeze.py` (Q3) and `corpus/knowledge/r96-response-scope-note.md`
  (Q6) were outside this seat and were not assessed; the Q3 tool existed but was still being
  rewritten during my window (`f4b5208f…` → `d17297bb…`).

## Bottom line

**PASS** — `corpus/fixtures/r96-crossing-response` verifies as claimed: `support_check`
`INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18; DISTINCT-ANCHORS 14/14`
+ `RESULT PASS` exit 0, and `map_obligations` `raw=16 mapped=16` + `RESULT PASS` exit 0,
with 17/17 inherited map rows parse-value identical, only `J16` (`timeline.json#/4`, span
33-42) added, five copied tables byte-identical, `check_bible` CLEAN exit 0, and census
169→170; Q1's hardening landed mid-seat (`d1c239cc…` → `2b0ba815…`) and changes nothing for
this fixture, while on scratch copies it converts the r95-carried deletion class from silent
exit 0 to `inventory_mismatch` exit 1 and the V37-D1 legacy dual-pointer cell from silent
exit 0 to `dual_pointer` exit 1, with `--self-test` reaching `24/24 pinned` once Q2's
contract landed (17:50:23).
