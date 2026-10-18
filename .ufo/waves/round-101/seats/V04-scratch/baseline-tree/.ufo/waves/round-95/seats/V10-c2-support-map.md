# V10 — c2-support-map (round 95)

**Seat:** V10 `c2-support-map` (verifier)
**Scope:** C2/depth — verify the delivered `corpus/fixtures/r95-crossing-aftermath/`
artifact set with `support_check.py` and `map_obligations.py`, plus the C2 counting
claims (5/1/4, 4 sources, 15 map obligations, 14 inherited rows unchanged, census
168→169, `check_bible` CLEAN, crossing-only scope).
**Report path:** `.ufo/waves/round-95/seats/V10-c2-support-map.md` (exclusive)
**Baseline:** r94 closure `fb118c4` (verified still HEAD during this run)
**Scratch:** `/tmp/v10-scratch/` (outside the repo; no repo file was written or
modified by this seat other than this report)

## 0. Poll-wait record

`corpus/fixtures/r95-crossing-aftermath/` did not exist at seat start (16:16:15).
Poll loop, 20 s cadence: absent at tries 1–16 (16:16:15 → 16:21:15); **READY at
try 17, 16:21:35**, with `claim-excerpt-map.md` (16:21:10, 8563 B) and
`README.md` (16:21:27, 4070 B) present. P3's tables had already landed at 16:18.
No artifact was verified before it existed; nothing was fabricated.

## 1. Revisions verified (all evidence below is from these bytes)

Fixture (stable from 16:21 through report time; sha256):

| File | sha256 | bytes |
|---|---|---:|
| `claim-excerpt-map.md` | `30281ff1a497bbe66f23cbd8a49befb3319595f20990718a0ffe8050741a874a` | 8563 |
| `README.md` | `9d27af4ac9644210d3ee1df26938a4a5592b8cbcfdb5d6fb880de6ccdb1bdd0b` | 4070 |
| `timeline.json` | `3c0faad6bf32f944f9f2a20f3bd15829044afa04f1a8837601903433b00ea177` | 1254 |
| `sources.json` | `fd9e30e8d9ad40013be2172781d13d84ba219377c8433ff6e529ea8e1927e64a` | 1225 |
| `entities.json` | `026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b` | 1449 |
| `relations.json` | `c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9` | 139 |
| `contradictions.json` | `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` | 3 |
| `fictional-excerpts.md` | `0ef6734ae52d28656e75869d942d6b1e8e324b116977a2811b3b36dc0880b282` | 1845 |
| `inspiration-note.md` | `58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37` | 1956 |
| `source-excerpt.md` | `b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd` | 640 |

Tool revision at final verification: `map_obligations.py`
sha256 `d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108`
(mtime 16:26:27), `map-obligations-contract.json` sha256
`8173bb97592a377716866737e8fcb4043014c9814e77a6248500d301a39170db` (22 self-test
cases). This is **not** the pre-round tool: `corpus/tools/map_obligations.py` is
modified in the working tree (P1 landed it at 16:22:28 and it settled at 16:26:27).
The r95 result was reproduced under the pre-P1 tool and under every in-flight P1
revision (section 5).

## 2. Required command 1 — `support_check.py` (expected PASS)

```
$ python3 corpus/tools/support_check.py corpus/fixtures/r95-crossing-aftermath
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
PASS J14: source-support; mode=verbatim; anchor=found; 18-20 span; 20:> Their tick-10 decision depends on both ninth-bell entries: ...
PASS J15: source-support; mode=verbatim; anchor=found; 26:> Tick 11: I waited at the Chalk Stair through the agreed bell.
PASS S01: editorial-row; mode=verbatim; anchor=found; 5:> ... He called out “Earth,” and the solid land appeared.
PASS S02: editorial-row; mode=verbatim; anchor=found; 5:> ... He called out “Earth,” and the solid land appeared.
RECEIPT JSON-FACTS 15; EDITORIAL-ROWS 2; TOTAL-ROWS 17
SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 17/17; VALIDATED-ROWS 17/17
RESULT PASS
exit=0
```

**JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17; RESULT PASS, exit 0** —
matches the expectation, and the declared inventory line
(`15 JSON facts; 2 editorial rows; 17 total mapped rows; 13 distinct excerpt
anchors`) is satisfied by the parse (`DISTINCT-ANCHORS 13/13`).
New row J15's anchor sits at line 26 inside its declared span 22-31 (the appended
aftermath section), i.e. the new obligation is genuinely in-span, not merely
declared. `stderr` empty.

## 3. Required command 2 — `map_obligations.py` (expected raw=15 mapped=15 PASS exit 0)

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
RESULT PASS
exit=0
```

**raw=15 mapped=15, RESULT PASS, exit 0** — matches the expectation. `stderr`
empty. (The `INVENTORY` line is new in P1's revision; the pre-P1 tool printed only
the `OBLIGATIONS` line, and the r95 verdict was PASS under both.)

Independent recount from the raw tables: `first_appearance=5 claims=5 relations=1
timeline=4 total=15` (r94: `5/5/1/3 = 14`).

## 4. C2 counting and preservation claims

| C2 claim | Measured | Verdict |
|---|---|---|
| 5 entities / 1 relation / 3→4 events / 3→4 sources | `entities.json` identical to r94 (5 records); `relations.json` identical (1); `timeline.json` r94 prefix identical + 1 new; `sources.json` r94 prefix identical + 1 new | holds |
| 14 inherited map rows carried unchanged | header-driven parse of both maps: 14/14 inherited pointer rows **parse-value identical** on source ID, excerpt path, line span, R9 mode, and exact anchor; only `timeline.json#/3` is new | holds |
| no new claims, no new entities/relations | `entities.json`, `relations.json`, `contradictions.json` byte-identical to r94 (`cmp` → IDENTICAL); `inspiration-note.md`, `source-excerpt.md` byte-identical | holds |
| new source `aru-aftermath-note`, new event `aftermath-missing-evin` (actor `aru`, place `chalk-stair`, `depends_on ["paired-crossing-decision"]`, tick 11) | exactly as declared in `sources.json`/`timeline.json` | holds |
| preserving copy | `fictional-excerpts.md`: r94's 20 lines are an **exact prefix** of r95's 31 lines; 11 lines appended | holds |
| `check_bible` CLEAN | `CLEAN: schema, citations, relations, timeline; 0 violations`, exit 0 | holds |
| census 168→169 | dirs under `corpus/fixtures` holding ≥1 of the 5 tables: **169 total, 168 excluding `r95-crossing-aftermath`**; r95 present | holds |
| crossing-only scope, no breach/other-duty assertion | `fictional-excerpts.md:29` "I assert no other duty, no breach, and no obligation beyond this crossing."; `:31` and `timeline.json` description and `sources.json` reliability note and `README.md:11` all repeat the crossing-only/no-breach bound; no alliance/perpetual-duty language asserted | holds (text-level; semantic review remains manual) |

Note on the path-qualification column: r95's map renames the namespace column to
`r95-crossing-aftermath:…` (r94 used `r94-paired-crossing:…`). That is the one
intended, documented difference; the 14 rows' pointer/source-ID/span/mode/anchor
values are unchanged, as the claim requires.

## 5. Tool-revision interaction observed (P1/C1/C3 side-effects)

My seat's instruction was to report exactly what I observe if P1's `schema_drift`
work interacts with the r95 fixture. Timeline observed while running:

| Time | `map_obligations.py` sha256 (12) | contract cases | r95 result |
|---|---|---:|---|
| 16:22:33 | `cc1df4dc…` (pre-P1, mtime 15:04) | 20 | raw=15 mapped=15 **PASS** |
| 16:22:40 | `28d308be…` | 20 | raw=15 mapped=15 **PASS**; `--self-test` → `FINDING self_test_contract: contract self-test cases do not match the implemented cases`, exit 2 |
| 16:23:06 | `85c237c3…` | 20 | raw=15 mapped=15 **PASS** |
| 16:23:26 | `74a88346…` | 20 | **uncaught traceback**, `ValueError: too many values to unpack (expected 2, got 15)` at `compare()` (no FINDING, no RESULT line) |
| 16:23:46 | `52d838b0…` | 20 | same uncaught traceback |
| 16:24:06 → 16:26:53 | `feea13c9…`, `3f87fe8b…`, `9224a684…`, `d1c239cc…` | 20 → 22 | raw=15 mapped=15 **PASS** (+ `INVENTORY` line) |
| 16:27:29 → report | `d1c239cc…` (settled) | 22 | raw=15 mapped=15 **PASS** |

Findings:
- The r95 fixture never produced a FAIL under any revision; the two traceback
  revisions were mid-write states of P1's file (both replaced within 20 s), not a
  property of the fixture. No delivered revision crashed on it.
- The `self_test_contract` mismatch at `28d308be…` was P1 landing before P2's
  contract (20 vs 22 cases); it cleared when the contract reached 22 cases at
  ~16:27:11. At the settled revision `--self-test` prints `RESULT PASS`, exit 0.
- C3 side-effects at the settled revision: `r88-m3-maya-cluster` →
  `OBLIGATIONS raw=10 mapped=10 / INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2;
  TOTAL-ROWS 12/12 / RESULT PASS`, exit 0; `r87-myth-cluster` → `FINDING
  unsupported_map: pointer cells must contain one canonical inline-code pointer`,
  exit 2 (fail-closed, message wording changed from the pre-P1
  "table needs one JSON fact pointer and one source-ID column"); `r89-c1-multi-cause-valid`
  → `FINDING map_missing`, exit 2. r87/r89 remain exit 2 as claimed.

### C1 mutation class, run on a scratch copy of the r95 fixture (`/tmp/v10-scratch/drift`)

Renamed `entities.json#/0`'s `claims` key to `claims_renamed` (claim content
preserved) and removed the corresponding map row:

```
$ python3 corpus/tools/map_obligations.py /tmp/v10-scratch/drift        # delivered tool
OBLIGATIONS raw=14 mapped=14
INVENTORY JSON-FACTS 14/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/17 MISMATCH
FINDING schema_drift: entities.json#/0: 1 sourced-claim-shaped record(s) under unexpected key 'claims_renamed'
RESULT FAIL
exit=1

$ python3 /tmp/v10-scratch/old_tool.py /tmp/v10-scratch/drift           # git show fb118c4:…
OBLIGATIONS raw=14 mapped=14
RESULT PASS
exit=0
```

The before→after C1 behavior reproduces on r95 bytes: silent PASS at `fb118c4`,
`exit 1` with a stable `schema_drift` FINDING at the settled revision.

## 6. Adversarial probes (scratch copies, live tree untouched)

| Probe (on a `/tmp` copy of r95) | Observed |
|---|---|
| delete the new `timeline.json#/3` map row | `OBLIGATIONS raw=15 mapped=14`; `FINDING missing_obligation: timeline.json#/3 has no map row`; `RESULT FAIL`, exit 1 |
| same copy under `support_check.py` | `FAIL: inventory JSON facts mismatch: expected=15 parsed=14` (+ total-rows 17/16, distinct anchors 13/12); `RESULT FAIL`, exit 1 |
| corrupt J15's map source ID to `crossing-minute` | `FINDING source_id_mismatch: timeline.json#/3 does not bind to 'aru-aftermath-note'`; `RESULT FAIL`, exit 1 |
| same corruption under `support_check.py` | `RESULT PASS` (15/15) — `support_check` does not check raw-JSON↔map source-ID binding |

So the new obligation is really covered by both tools in their documented
domains, and the two tools are complementary rather than redundant. Live fixture
hashes after all probes are unchanged (`claim-excerpt-map.md` `30281ff1…`,
`timeline.json` `3c0faad6…`); `git status` shows the r95 directory as untracked
content only, with no modification by this seat.

## 7. Limitations / not verified here

- Whole-claim entailment, canon truth, and the "no breach" reading are manual
  reviews; the receipts above are lexical/map-declared only, per the tools' own
  scope statements.
- C1 and C3 are other seats' claims; only the interactions above were observed.
  At report time P1/P2 bytes were settled for ~1.5 min (`d1c239cc…`, 22 cases);
  if they change again, the r95 verdicts above must be re-run.
- `corpus/knowledge/r95-aftermath-scope-note.md` (P5) and `LOG.md`/README
  addenda were outside this seat and were not assessed.

## Bottom line

**PASS** — `corpus/fixtures/r95-crossing-aftermath` verifies as claimed:
`support_check` RESULT PASS (JSON-FACTS 15/15, EDITORIAL-ROWS 2/2, TOTAL-ROWS
17/17, exit 0) and `map_obligations` raw=15 mapped=15 RESULT PASS exit 0, with
all 14 inherited map rows parse-value identical, only `timeline.json#/3` added,
copied tables byte-identical, `check_bible` CLEAN exit 0, and census 168→169;
P1's in-flight revisions produced two transient tracebacks and one
self-test-contract mismatch that had cleared by the settled revision
`d1c239cc…` (22 cases), and the C1 `schema_drift` mutation class reproduces on
r95 scratch bytes (exit 1, vs silent PASS at `fb118c4`).
