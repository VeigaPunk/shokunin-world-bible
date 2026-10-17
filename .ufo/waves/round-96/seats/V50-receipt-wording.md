# V50 — receipt-wording (round 96)

Seat: V50 `receipt-wording`. Scope: after all producers, audit the exact ratios and
denominators in LOG.md's r96 declaration (`LOG.md:2863-2928`) against this seat's own
measured outputs — what exactly does "16 map obligations" count, what exactly do "4/4" and
"24/24" count — and list the wording corrections L1 should apply at closure. Leaf seat: no
nested agents, no commits, no pushes, no network. Writes: this report plus seat scratch
`.ufo/waves/round-96/seats/V50-scratch/` (harness, old-tool extraction, mutation copies,
captured outputs). Nothing else touched.

Baseline: HEAD `60dba0c2aa344860b10a2fc63e00468d1b134f27` (r95 close commit; its parent is
`dcb2d92`, the r95 freeze/closure-docs commit the declaration names — see WC-4). All
commands run from `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`.

## 0. Poll status and revision pins

All six producer reports landed (Q1…Q6) before the freeze; the delivered bytes were stable
from 17:52 to 17:53:53 (digest re-check before and after the harness: `DIGESTS STABLE`).
50 seat reports were on disk when this report was written (this seat makes 51). Final digests every
measurement below stands on:

```
$ sha256sum corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json \
    corpus/tools/README.md corpus/tools/dependency_freeze.py \
    corpus/tools/dependency-freeze-contract.json \
    corpus/fixtures/r96-crossing-response/claim-excerpt-map.md \
    corpus/fixtures/r96-crossing-response/README.md \
    corpus/knowledge/r96-response-scope-note.md
2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8  corpus/tools/map_obligations.py
97b76bb8b1fea97f166ef7586eba69c427ec15bbe7b34eb5345ec65c936493b6  corpus/tools/map-obligations-contract.json
965b29cd41a8af14293eb2e1948f58f310e58c6e752b8fe322c5445b20a91f24  corpus/tools/README.md
a3b57978f0cbf314389ee3f9862920a46cf109fca6d1eec488c39be0457f0980  corpus/tools/dependency_freeze.py
7d568cc422cda42297b7506a1a3e083e8798866efd16d58617bf4ea468576975  corpus/tools/dependency-freeze-contract.json
5093d72eb3f22b249033d7ac4c1a85c7df7f5e09bfa673a598aee6a83045bfd8  corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
ff52ced48bf4214721f248328d76da64a42773d44e78154ef1eaf6eb3558c456  corpus/fixtures/r96-crossing-response/README.md
6db32ca24f5eff5baa3ebe589e8d3bcb6b256fec18dee2468211d7d0fae157c6  corpus/knowledge/r96-response-scope-note.md
```

`git status --porcelain` at freeze — exactly the declared write scope, nothing else:

```
 M LOG.md
 M corpus/tools/README.md
 M corpus/tools/map-obligations-contract.json
 M corpus/tools/map_obligations.py
?? .ufo/waves/round-96/
?? corpus/fixtures/r96-crossing-response/
?? corpus/knowledge/r96-response-scope-note.md
?? corpus/tools/dependency-freeze-contract.json
?? corpus/tools/dependency_freeze.py
```

Mid-write transients observed while producers were still running (recorded as a harness
property, not defects): at 17:44 the in-flight `map_obligations.py` (digest `efcdd0ef…`)
failed `r88-m3-maya-cluster` with 20 `missing_obligation`/`phantom_obligation` findings;
the in-flight `dependency_freeze.py` self-test ran `3/14`, then `4/14` (digests `932d0e05…`,
`f3a854fc…`), before settling at `14/14`. Every number in this report is from the final
digests above; none from a transient.

## 1. Denominator ledger — every figure the declaration cites

Measured with the delivered tools. Composition of the r96 obligation count measured with the
tool's own `raw_obligations()`: `first_appearance=5 claim=5 relation=1 timeline=5` = 16.

| # | Declaration (LOG line) | Measured receipt | What the denominator counts | Verdict |
|---|---|---|---|---|
| D1 | "contract 22→24 cases" (2880) | `corpus/tools/map-obligations-contract.json` → 24 cases; new ids `schema_drift` (exit 1/`['schema_drift']`) and `inventory_mismatch` (exit 1/`['inventory_mismatch']`) at positions 6–7 | persisted self-test cases | TRUE |
| D2 | "`--self-test` 24/24" (2880) | `map_obligations.py --self-test` → 24 `SELF-TEST PASS` lines + `RESULT PASS` exit 0; every persisted expectation matches the observed `(exit, finding_ids)` (the `complete`/`frozen_complete` cases print `findings=none`) | self-test cases run | TRUE |
| D3 | "(a) … deleting a claims key AND its map row currently exits 0 with the shortfall visible only in the non-gating `INVENTORY … MISMATCH` receipt" (2874-2876) | HEAD tool on such a copy: `OBLIGATIONS raw=14 mapped=14` / `INVENTORY JSON-FACTS 14/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/17 MISMATCH` / `RESULT PASS` exit 0; delivered tool: exit 1 `FINDING inventory_mismatch: declared JSON-facts/editorial-rows/total-rows 15/2/17; observed 14/2/16` | exit code + finding ID | TRUE |
| D4 | "(c) V37-D1 … currently silently ignored — after … a stable `dual_pointer` FINDING and exit 1" (2879-2881) | HEAD tool on r88 copy with a second pointer added to a legacy cell: exit 0, output byte-identical to the clean control; delivered tool: exit 1 `FINDING dual_pointer: row P1 (line 23) names a second pointer token 'timeline.json#/0' alongside entities.json#/0/first_appearance` | exit code + finding ID | TRUE |
| D5 | C2 before "5 entities / 1 relation / 4 events / 5 sources at r95" (2893-2894) | r95 fixture: entities 5, relations 1, timeline 4, sources 4 (`veil-verse`, `paired-clock`, `crossing-minute`, `aru-aftermath-note`) | JSON record counts | **FALSE — before-clause sources must be 4** (WC-1) |
| D6 | C2 after "5/1/5, 5 sources" (2894) | r96 fixture: 5 / 1 / 5, sources 5 (adds `evin-response-note`) | JSON record counts | TRUE |
| D7 | "16 map obligations" (2895) | `OBLIGATIONS raw=16 mapped=16`; `INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18`; `support_check` `MODES 18/18; VALIDATED-ROWS 18/18` | **16 = raw source-attributed obligations = mapped JSON-fact rows** (5 first_appearance + 5 claims + 1 relation + 5 timeline). It is not the map's row total: the same map has 18 rows (16 + 2 editorial) | TRUE (companion figure needed — WC-2) |
| D8 | "15 inherited rows unchanged" (2895) | r95 map rows=15, r96 rows=16; for all 15 shared pointers only column 4 of 8 (`Path-qualified source namespace`) differs (`r95-crossing-aftermath:*` → `r96-crossing-response:*`); columns ID, pointer+fields, in-world source ID, excerpt path, span, mode, anchor identical; new row J16 = `timeline.json#/4` | parsed map cells | TRUE only as "all fields except the path-qualification namespace" (WC-3) |
| D9 | "no new claims/entities/relations" (2895-2896) | `entities.json` and `relations.json` byte-identical to r95 (sha256 match); 5 claims, 1 relation both sides | record counts / bytes | TRUE |
| D10 | "`check_bible` CLEAN exit 0" (2896) | `CLEAN: schema, citations, relations, timeline; 0 violations` exit 0 | checker verdict | TRUE |
| D11 | "inherited r95 rows parsed-value identical" (2896-2897) | see D8: whole-row parsed values are **not** identical — the namespace column differs on all 15 rows | parsed map cells | **imprecise as written** (WC-3) |
| D12 | "census 169→170" (2897) | `census_r95.py --ref dcb2d92 --expected-dirs 170 --allow-new r96-crossing-response` → `CENSUS PASS: dirs=170 files=1010 modified=0 deleted=0 new=10`; full corpus run with the r95 convention: 170 dirs / 36 clean / 134 negative / **421 `VIOLATION` lines** / 0 stderr / 0 non-0/1 exits (r95: 169 / 35 / 134 / 421) | fixture directories / `VIOLATION:` lines | TRUE (421 lines unchanged because r96 is clean) |
| D13 | "No contradiction is asserted" (2897-2898) | `contradictions.json` byte-identical to r95 (empty array), 0 records | record count | TRUE |
| D14 | C3 "expect 4/4 clean" (2913) | `dependency_freeze.py` on the four chain fixtures → each `RESULT PASS` exit 0 (r96: `FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1` / `DIGEST d422a9b3…`) | chain fixtures | TRUE (digit collision — see §2) |
| D15 | C3 "the BR-01 mutation … must exit 1 REDUCTION-DETECTED; an added-edge mutation must also exit 1" (2913-2915) | scratch r94 copy with `evin-ninth-bell` dropped from tick-10: exit 1 `FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']`; scratch copy with a phantom edge added: exit 1 `FINDING ADDITION-DETECTED: event evin-ninth-bell gained depends_on ['aru-ninth-bell']`; inventory-neutral description reword: exit 2 `FINDING DIGEST-MISMATCH: … fixture bytes changed outside the frozen inventory` | exit codes + stable finding IDs | TRUE (0/1/2 contract held) |
| D16 | C3 "closing carried debt BR-01 (dependency reduction is undetectable …)" (2901-2903) | the same reduction copy under the pre-r96 gates: `check_bible` exit 0 CLEAN, `support_check` `RESULT PASS` exit 0, HEAD `map_obligations` `raw=14 mapped=14 RESULT PASS` exit 0 — only the new gate catches it | gate verdicts | TRUE |
| D17 | C3 "Zero corpus modifications beyond the two new tool files" (2915-2916) | `git status` above: C3 adds exactly `dependency_freeze.py` + `dependency-freeze-contract.json`; no other corpus path modified by C3 | working-tree diff | TRUE |
| D18 | "Baseline = r95 closure `dcb2d92`" (2865) | `git rev-parse HEAD` = `60dba0c…`; `git diff --stat dcb2d92 60dba0c` = `SCORECARD.md | 32 +++…`, 1 file changed; the freeze contract's own `revision` pin is `60dba0c…` | revision pin | **imprecise** (WC-4) |

Supporting commands and exact outputs:

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response
OBLIGATIONS raw=16 mapped=16
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18
RESULT PASS
rc=0

$ python3 corpus/tools/map_obligations.py --self-test | tail -2
SELF-TEST PASS inventory_mismatch exit=1 findings=['inventory_mismatch']
RESULT PASS
rc=0   (24 SELF-TEST PASS lines)

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
RESULT PASS
rc=0

$ python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response | tail -2
SOURCE-SUPPORT 16/16; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 18/18; VALIDATED-ROWS 18/18
RESULT PASS
rc=0

$ python3 corpus/tools/dependency_freeze.py --self-test | tail -2
SELF-TEST 14/14
RESULT PASS
rc=0

$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r96-crossing-response
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
DIGEST d422a9b3d95c4e0b8aac98cc87806a94949896adb962a50d2d55a6c11657d7f6
RESULT PASS
rc=0

$ python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93
SNAPSHOT inputs=4 digests=verified
OBLIGATIONS raw=12 mapped=12
INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15
FROZEN expected=PASS/0 findings=none matched
RESULT PASS
rc=0
```

Non-regression sweep (old = `git show HEAD:corpus/tools/map_obligations.py`, new = delivered
`2b0ba815…`): all 37 `r87*`–`r96*` fixture directories — **0 exit diffs, 0 stdout diffs**
(byte-identical output on every fixture). `r87-myth-cluster` and `r89-inspiration-paraphrase`
exit 2 `unsupported_map`; r88/r93/r94/r95/r96 exit 0 with `raw=10/12/14/15/16` respectively.

## 2. Collision ledger — same digits, different units

| digits | referent A | referent B (and C) |
|---|---|---|
| `4/4` | C3 chain fixtures (four fixtures clean, LOG 2913) | r96 freeze receipt `dependency-edges 4/4` (four edges **inside** r96-crossing-response) |
| `5/5` | r96 freeze receipt `events 5/5` (five events in the fixture) | C2 after-clause `5/1/5` events count (same 5, different unit) |
| `14/14` | `dependency_freeze.py --self-test` cases | r94 `OBLIGATIONS raw=14 mapped=14` |
| `16/16` | r96 obligations raw/mapped (D7) | r96 `support_check` `SOURCE-SUPPORT 16/16` (same referent, different tool) |
| `18/18` | r96 map `TOTAL-ROWS 18/18` (D7) | r96 `support_check` `MODES 18/18` / `VALIDATED-ROWS 18/18` |
| `24/24` | `map_obligations.py --self-test` cases (C1) | — (unambiguous, but the closure note should name the tool) |

Any closure sentence must name the tool, the unit, and the fixture. In particular the
declaration's bare "4/4" (C3) is not the same `4/4` that the gate itself prints.

## 3. Wording corrections for L1's closure note

**WC-1 (required, `LOG.md:2893-2894`).** The before-clause "5 sources" is wrong and the
sentence contradicts itself ("… / 4 events / 5 sources at r95. After: 5/1/5, 5 sources wait
— r95 has 4 sources …"). Measured r95 sources = 4. Replace the pair with:

> Before: 5 entities / 1 relation / 4 events / 4 sources at r95. After: 5 entities / 1
> relation / 5 events / 5 sources (the tick-12 response event and `evin-response-note`).

**WC-2 (required, `LOG.md:2895`).** "16 map obligations" needs its companion figure and
attribution, exactly as r95's correction (4) required: "16 obligations (`OBLIGATIONS raw=16
mapped=16`); the same fixture's map has 18 rows (16 JSON facts + 2 editorial), matching
`support_check`'s `MODES 18/18`." Without it a reader can take 16 as the map's row total.

**WC-3 (precision, `LOG.md:2895-2897`).** "15 inherited rows unchanged" and "inherited r95
rows parsed-value identical" are true only in the r95-WC-3 sense. Measured: of the 8 columns
in the 15 shared rows, only the path-qualification namespace column differs on all 15 rows
(`r95-crossing-aftermath:*` → `r96-crossing-response:*`); pointer, in-world source ID,
excerpt path, span, mode, and anchor are identical. Say: "15 inherited rows carried with
pointer, source-ID, span, mode, and anchor values identical; only the path-qualification
namespace column was re-namespaced."

**WC-4 (precision, `LOG.md:2865`).** "Baseline = r95 closure `dcb2d92`" names the parent of
the actual working-tree HEAD. `git rev-parse HEAD` = `60dba0c…` (the r95 close commit;
`dcb2d92` is its parent and the r95 freeze/closure-docs commit). The delta is
`SCORECARD.md` only (+32 lines), so no corpus measurement is affected, but the freeze
contract pins `revision: 60dba0c…` and a closure note that says `dcb2d92` will not match
its own artifact. Say "Baseline = r95 closure `60dba0c` (`dcb2d92` its parent)".

**WC-5 (precision, `LOG.md:2906-2908, 2913`).** Name the C3 finding IDs rather than
"addition/endpoint change": measured IDs are `REDUCTION-DETECTED` (exit 1),
`ADDITION-DETECTED` (exit 1), `ENDPOINT-CHANGE` (exit 1), `DIGEST-MISMATCH` (exit 2) —
the last is the "could-not-evaluate" arm and is *not* one of the 1-arm variants the LOG's
parenthetical implies. Also disambiguate "4/4": "the four chain fixtures (4/4 clean)".

**WC-6 (optional, `LOG.md:2908`).** Record the third ratio the round now carries:
`dependency_freeze.py --self-test` is 14/14 cases (distinct from C1's 24/24 and C3's 4/4),
so a future reader can tell which self-test a bare "self-test" refers to.

## 4. Bounds

- This seat audited ratios/denominators and the declaration's before/after factual claims;
  it did not judge literary content, canon, entailment, or the per-axis verdicts (other
  seats own those). `contradictions.json` emptiness was checked as bytes, not as an
  interpretation of the two accounts.
- The census used the r95 seat's own script for the directory/file diff and a fresh loop for
  the clean/negative/`VIOLATION` counts; the `VIOLATION`-line convention (uppercase lines
  only, excluding the `N violation(s)` summary and the clean line) was reverse-engineered to
  reproduce r95's 421 and is stated here explicitly rather than assumed.
- All measurements are pinned to the digests in §0; producer artifacts were still moving
  earlier (transients in §0), so any re-run must re-check the digests first.

Bottom line: **PASS** — every declared ratio and before/after count verifies on the frozen
delivered revision except the C2 before-clause sources figure ("5 sources" must be 4) and
three precision items (18-row companion for "16", namespace-column qualification for "15
inherited rows unchanged / parsed-value identical", baseline commit `dcb2d92` → `60dba0c`);
24/24, 4/4 (chain), 16/16 vs TOTAL 18/18, and census 169→170 all measured as declared.
