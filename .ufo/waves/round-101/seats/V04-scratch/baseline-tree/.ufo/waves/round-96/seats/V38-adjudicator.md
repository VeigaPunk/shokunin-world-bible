# V38 — adjudicator (round 96, FINAL)

- Seat: V38 adjudicator, round-96 single wave, lane `lore-shokunin`.
- Baseline: r95 closure `dcb2d92`; worktree HEAD `60dba0c2aa344860b10a2fc63e00468d1b134f27` (r95 SCORECARD closure commit).
- Mandate: poll until the other 63 reports exist, read them all, reconcile conflicts
  explicitly, admit ONLY if C1/C2/C3 verify on the delivered revision and no axis is
  harmed; per-axis table; ADMIT/REJECT; exact admission conditions; never re-roll
  harmed findings.
- All commands below ran from `/home/vgpnk/Projects/shokunin/lore-shokunin` with
  `python3`. Every output quoted is my own run on the delivered bytes. My only writes
  are this report and `.ufo/waves/round-96/seats/V38-scratch/`.

## 0. Delivered revision (frozen for this adjudication)

```
$ sha256sum corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json \
    corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json corpus/tools/README.md
2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8  corpus/tools/map_obligations.py
97b76bb8b1fea97f166ef7586eba69c427ec15bbe7b34eb5345ec65c936493b6  corpus/tools/map-obligations-contract.json
a3b57978f0cbf314389ee3f9862920a46cf109fca6d1eec488c39be0457f0980  corpus/tools/dependency_freeze.py
7d568cc422cda42297b7506a1a3e083e8798866efd16d58617bf4ea468576975  corpus/tools/dependency-freeze-contract.json
965b29cd41a8af14293eb2e1948f58f310e58c6e752b8fe322c5445b20a91f24  corpus/tools/README.md
```

Fixture (10 files) — `claim-excerpt-map.md 5093d72e…`, `README.md ff52ced4…`,
`timeline.json ea0225f9…`, `sources.json 9f973f63…`, `relations.json c279254b…`,
`contradictions.json 37517e5f…`, `entities.json 026af0bc…`, `inspiration-note.md 58f5390e…`,
`source-excerpt.md b5edc2fd…`, `fictional-excerpts.md 06b11bec…`.
Knowledge note `corpus/knowledge/r96-response-scope-note.md 6db32ca2…`.
These hashes match the pins quoted by Q1/Q2/Q3 and by V02/V05/V07/V35/V36/V39/V41/V52.

## 1. Report inventory — 64/64 present and read

Present and read: Q1–Q6 (all six producers) + V01–V58 (all 58 verifier seats). This
report is the 64th.

- **V43 and V58 were late landings, not failures** (r95 recorded the same class:
  V33/V59/V57). At my first cutoff (18:02) both were absent and each was polling for 63
  lane reports — a condition that includes this adjudicator report, so the pair was in a
  mutual wait. `V43-scratch/V43-poll.log` shows the resolution: `try=119 lane=63` at
  18:19:08, V43 wrote `V43-receipt.md`; `V58-scratch/poll.log` then read
  `18:19:18 POLL_HIT total=63 others=63` and V58 wrote `V58-presence-final.md`. Both are
  PASS; V43 records the mutual-wait liveness finding itself, and V58 audits 64/64 present
  with no duplicates, no header mismatches and no parent-tree strays.
- **V37-verdict-adjacency is INCOMPLETE**: 34 lines, §1 (`PROVINCE.md` byte-identical,
  blob `7c599c39`) PASS, §2 ends `Placeholder — final battery output to be inserted.`
  No adjacency verdict was ever issued; V31 supplies the adjacency PASS independently.
- **V34-verdict-calibration stayed INCONCLUSIVE (interim)**: it closed before Q1/Q2
  landed. Its baseline half matches mine exactly; its post-change half I re-verified
  myself (§2).
- Verdict census of the 63 others: **1 FAIL (V23)**, 1 INCONCLUSIVE-interim (V34),
  1 INCOMPLETE (V37), the rest PASS, many with disclosed bounds.

## 2. C1 — calibration: VERIFIED (all three parts)

### (a) Deletion class becomes gating — VERIFIED

Baseline captured before Q1 landed (tool md5 `d31b8182…`, sha256 `d1c239cc…`); delivered
revision `2b0ba815…`:

```
$ python3 corpus/tools/map_obligations.py <scratch copy of r95-crossing-aftermath with entity 0's
      claims key deleted and its entities.json#/0/claims/0 map row removed>
# baseline d1c239cc:
OBLIGATIONS raw=14 mapped=14
INVENTORY JSON-FACTS 14/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/17 MISMATCH
RESULT PASS                                    EXIT=0        <- the r95-carried defect
# delivered 2b0ba815:
OBLIGATIONS raw=14 mapped=14
INVENTORY JSON-FACTS 14/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/17 MISMATCH
FINDING inventory_mismatch: declared JSON-facts/editorial-rows/total-rows 15/2/17; observed 14/2/16
RESULT FAIL                                    EXIT=1        <- closed, stable ID
```

**Named bound (verified, not waived):** deletion accompanied by a *consistently updated*
declaration still exits 0 — `INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS
16/16` / `RESULT PASS` / exit 0. The gate compares declared vs observed; a coherent
regeneration is indistinguishable. Same bound V42 measured.

### (b) Persisted pinning, 22→24 — VERIFIED and load-bearing

```
$ python3 -c "import json;print(len(json.load(open('corpus/tools/map-obligations-contract.json'))['self_test']['cases']))"
24
$ python3 corpus/tools/map_obligations.py --self-test | head -2
SELF-TEST CASES 24/24 pinned
SELF-TEST PASS complete exit=0 findings=none
$ python3 corpus/tools/map_obligations.py --self-test | grep -E "schema_drift|inventory_mismatch|RESULT"
SELF-TEST PASS schema_drift exit=1 findings=['schema_drift']
SELF-TEST PASS inventory_mismatch exit=1 findings=['inventory_mismatch']
RESULT PASS                                    EXIT=0
```

Load-bearing proven three ways on isolated copies (never the delivered files):
1. `inventory_finding()` neutralized → `SELF-TEST FAIL inventory_mismatch exit=0 findings=none`
   / `RESULT ERROR` exit 2.
2. `schema_drift` emission neutralized → `SELF-TEST FAIL schema_drift exit=0 findings=none`
   / exit 2.
3. Contract expectation flipped (`inventory_mismatch` → exit 0) → `SELF-TEST FAIL` / exit 2.

**Two confirmed residuals (V02, V07 D1; I reproduced both):**
- **Subset tolerance:** dropping either *added* case keeps the self-test green —
  `SELF-TEST CASES 23/24 pinned` / `RESULT PASS` exit 0 (my run; V07 D1 calls it MEDIUM).
  The tool requires only the 22 CORE cases (`missing = set(CORE_SELF_TEST_CASES) - set(expected)`).
  The delivered contract pins 24, so the declared C1(b) claim holds; the residual is that
  a later contract edit could silently drop the two new pins.
- **`dual_pointer` is pinned by no persisted case:** the 24 case IDs contain no
  `dual_pointer`, and `--self-test` output mentions it zero times. C1(c)'s new gate has
  no durable regression pin — a silent revert would evade `--self-test` (the r91
  Q90-001 class). C1(c) is nevertheless verified first-hand below.

### (c) V37-D1 dual pointer — VERIFIED, with controls

Reproduced V37's exact matrix (legacy header `JSON fact and fields`, `raw=3 mapped=3`):

```
$ for c in legacy-paren-hidden-canonical legacy-paren-hidden-legacy legacy-colon-hidden-pointer; do
    python3 corpus/tools/map_obligations.py .../base/d1/$c; done
# baseline d1c239cc — all three: RESULT PASS, EXIT=0 (silently ignored)
# delivered 2b0ba815:
legacy-paren-hidden-canonical  rc=1 | FINDING dual_pointer: row R1 (line 7) names a second pointer token 'relations.json#/0' alongside entities.json#/0/first_appearance
legacy-paren-hidden-legacy     rc=1 | FINDING dual_pointer: row R1 (line 7) names a second pointer token 'entities[9].claims[0]' alongside entities.json#/0/first_appearance
legacy-colon-hidden-pointer    rc=1 | FINDING dual_pointer: row R1 (line 7) names a second pointer token 'entities[9].claims[0]' alongside entities.json#/0/first_appearance
```

**False-positive controls (mine):**
- `` `entities[0].first_appearance` (see relations notes, entities.json) `` → `RESULT PASS`
  exit 0 — no blunt "second backtick" rule.
- Canonical-header cell with an embedded pointer → `unsupported_map` exit 2, **unchanged**
  (the pre-existing screening, not converted to `dual_pointer`).
- r88's real legacy cells — including `` `timeline[0]` (`description`, `source_id`): … `` —
  still `RESULT PASS` exit 0, `raw=10 mapped=10`, `TOTAL-ROWS 12/12`.

**Self-correction recorded:** an exit-0 I briefly saw on the paren-hidden-canonical probe
was my own earlier edit of that scratch cell, not a regression; I rebuilt all four probes
from scratch and re-ran. No seat should read that intermediate observation as a harm.

### C1 non-regression battery (delivered revision)

```
r88-m3-maya-cluster     rc=0  raw=10 mapped=10  INVENTORY 10/10; 2/2; 12/12   RESULT PASS
r93-m2-kojiki-cluster   rc=0  raw=12 mapped=12  INVENTORY 12/12; 3/3; 15/15   RESULT PASS
r94-paired-crossing     rc=0  raw=14 mapped=14  INVENTORY 14/14; 2/2; 16/16   RESULT PASS
r95-crossing-aftermath  rc=0  raw=15 mapped=15  INVENTORY 15/15; 2/2; 17/17   RESULT PASS
r96-crossing-response   rc=0  raw=16 mapped=16  INVENTORY 16/16; 2/2; 18/18   RESULT PASS
r87-myth-cluster        rc=2  FINDING unsupported_map: pointer cells must contain one canonical inline-code pointer
r89-fn2-control         rc=2  FINDING map_missing: expected exactly one conventional claim-to-excerpt map
r89-inspiration-paraphrase rc=2 FINDING unsupported_map: table needs one JSON fact pointer and one source-ID column
$ python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93
SNAPSHOT inputs=4 digests=verified / FROZEN expected=PASS/0 findings=none matched / RESULT PASS  EXIT=0
```

All 22 inherited cases still pass; the 0/1/2 contract and the `INVENTORY` receipt surface
are unchanged. Q5's and Q6's receipts, taken pre-C1, were re-run by me post-C1 and hold.

## 3. C2 — depth: VERIFIED

```
entities 5 / relations 1 / timeline 5 (r95: 4) / sources 5 (r95: 4) / contradictions []
new event: response-evin-salt-court tick 12, entity_id evin, place_id salt-court,
           depends_on ['aftermath-missing-evin'], source_id evin-response-note
inherited timeline prefix equal to r95: True
five byte copies (entities, relations, contradictions, inspiration-note, source-excerpt):
  md5 identical to r95 — SAME/SAME/SAME/SAME/SAME
```

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response
OBLIGATIONS raw=16 mapped=16
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18
RESULT PASS                                    EXIT=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response
... SOURCE-SUPPORT 16/16; EDITORIAL-ANCHORS 2/2; MODES 18/18; VALIDATED-ROWS 18/18
PASS J16: source-support; mode=verbatim; anchor=found; 37:> Tick 12: I was at Salt Court through the same agreed bell.
RESULT PASS                                    EXIT=0
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response
CLEAN: schema, citations, relations, timeline; 0 violations   EXIT=0
```

Inherited-row equality (my own column-wise comparison of the two maps): headers equal;
**0 diffs** across the 15 inherited rows in every column except the path-qualified
namespace column, which changed on all 15 by design; the 16th row is the sole new
pointer `timeline.json#/4`.

Census (my sweep, all 170 dirs):

```
ALL dirs=170 clean=36 negative=134 other=0 violation_lines=421
```

vs the r95 closure (169 / 35 / 134 / 421): exactly **+1 clean directory, zero inherited
tuple changes, zero non-0/1 exits**. File count 1010 (r95: 1000), r96 fixture 10 files.
Matches V24/V44/V56 independently.

Unresolved scope: `contradictions.json` is `[]`; the r35 Bell-7 counterpart carries 1
contradiction, so the "second account, same occasion, unresolved" class is genuinely
distinct. No accusation, winner, canon-truth, rights or identity inference appears in the
new bytes (V13/V37/V46/V53/V54 concur; V12's F1 and V54's wording note are cosmetic, §5).

## 4. C3 — coverage: VERIFIED functionally, with confirmed deviations

```
$ for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response; do
    python3 corpus/tools/dependency_freeze.py corpus/fixtures/$f; done
r88  FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0   DIGEST 15ef230e…  EXIT=0
r94  FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1   DIGEST 2527beb9…  EXIT=0
r95  FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1 DIGEST d541ae64… EXIT=0
r96  FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1  DIGEST d422a9b3… EXIT=0
```

Mutations on scratch copies (BR-01 is the exact carried debt):

```
reduction (drop evin-ninth-bell from r94 tick-10 depends_on)
  rc=1  FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']
addition (new event post-crossing-note depending on the tick-10 decision)
  rc=1  FINDING ADDITION-DETECTED: unpinned event post-crossing-note introduces depends_on ['paired-crossing-decision']
endpoint (relations[0].to: evin -> chalk-stair)
  rc=1  FINDING ENDPOINT-CHANGE: relation endpoints changed: removed [aru, evin, …]; added [aru, chalk-stair, …]
```

Exit-2 surface (correctly-named copies, so the pin lookup succeeds):

```
missing timeline.json    rc=2  FINDING FILE-MISSING
malformed timeline.json  rc=2  FINDING MALFORMED-JSON
digest-only tamper       rc=2  FINDING DIGEST-MISMATCH      (declared precedence)
unpinned/absent dir      rc=2  FINDING UNPINNED-FIXTURE / FIXTURE-MISSING
usage error              rc=2  FINDING INVALID-ARGUMENTS
clean control            rc=0
$ python3 corpus/tools/dependency_freeze.py --self-test
SELF-TEST 14/14 / RESULT PASS                   EXIT=0
$ git diff --stat HEAD -- <the four chain fixtures>
(empty)      -> zero corpus modification beyond the two new tool files
```

All four replay commands documented in the r96 README exit 0. BR-01's **JSON-edge half is
genuinely closed**: the r94 reduction that leaves `check_bible` and `map_obligations`
green now exits 1. I also confirmed the inverse control: emptying `depends_on` leaves
`check_bible` CLEAN while `dependency_freeze` reports `REDUCTION-DETECTED` exit 1.

### Confirmed C3 deviations (not re-rolled)

**H1 — V23's FAIL is confirmed.** The delivered contract carries **five** pins, not four:

```
$ python3 -c "import json;print(sorted(json.load(open('corpus/tools/dependency-freeze-contract.json'))['pins']))"
['c3red', 'r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response']
c3red.fixture = .ufo/waves/round-96/seats/V41-scratch/c3red   (a scratch path)
```

Provenance is self-disclosed by **V41** (`V41-spec-conformance.md` F1): its own
`--freeze` harness run wrote the key at 17:44:27; `V41-scratch/c3-freeze.out` reads
`FROZEN c3red: events 3; dependency-edges 1; relations 1 … RESULT PASS`. Q3 §7 disclosed
it and deliberately left it so two verifier receipts stay valid. Impact: none on
verification semantics (pins are basename-keyed and no corpus fixture is named `c3red`;
`--self-test` is 14/14 with it present). It is nonetheless a **byte-ownership breach**
(a verifier wrote a producer-owned delivered artifact) and a delivered artifact that
references a seat scratch path. V16/V17/V18/V19/V20(D2)/V21/V22/V23/V25/V30/V33/V35(D1/D5)
/V36/V41/V42/V48/V57 all flag it.

**H2 — no path binding (V20 D3, MEDIUM; I reproduced it).** A pristine copy of r94 at a
foreign path produces a **byte-identical** receipt:

```
$ python3 corpus/tools/dependency_freeze.py .ufo/waves/round-96/seats/V38-scratch/d3/r94-paired-crossing > shadow.txt
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r94-paired-crossing > real.txt
$ diff shadow.txt real.txt && echo IDENTICAL
IDENTICAL
$ grep -n '"fixture"' corpus/tools/dependency_freeze.py
302:        "fixture": fixture_label,        <- written, never read
448:    parser.add_argument("fixture", …)   <- CLI positional
```

So a "chain 4/4 clean" receipt does not prove the delivered paths were the ones verified.

**H3 — BR-01's prose half remains open (V20 D4, MEDIUM; I reproduced it).** Removing the
dependency wording from a scratch copy of the r94 excerpt leaves every gate green:

```
dependency_freeze.py  rc=0 | FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
check_bible.py        rc=0 | CLEAN … 0 violations
map_obligations.py    rc=0 | OBLIGATIONS raw=14 mapped=14 … RESULT PASS
```

The declaration's C3 text names the JSON-edge instance ("dropping `evin-ninth-bell` from
the r94 tick-10 `depends_on`"), which is closed; the markdown-layer cross-check the debt
also named is not.

**LOW items confirmed by other seats and not contradicted by me:** F4
`MALFORMED-MODEL`/`CONTRACT-INVALID` have no persisted case; F5 `SELF-TEST-MISMATCH`
exits 1 in `dependency_freeze` vs 2 in `map_obligations` (I observed the exit-1 form
first-hand mid-flight); F6 `freeze()` discards its `verify()` result; F7 wording; F8
`DIGEST-MISMATCH` does not name the changed file; `--freeze` has no `corpus/fixtures/`
scope guard (V20 D2, V23 reproduced it in isolation, V22 T4c).

## 5. Other confirmed defects on delivered bytes (outside the three claims)

- **V12 F1 (minor, Q5's file) — confirmed.** `corpus/fixtures/r96-crossing-response/claim-excerpt-map.md:44`
  is `|---|---|---|---|---|---:|---|---|` (8 cells) while its header (line 43) and data rows
  (45–46) have 7; r95's equivalent was a 7-cell delimiter. Under strict GFM the editorial
  table would not render. No gate reads it (`EDITORIAL-ROWS 2/2` on every run).
- **V54 obs 2 (LOW) — confirmed.** r96 map line 50 says "The new relation encodes only the
  agreement for this crossing…" although r96 adds no relation (the new row is a tick-12
  *event*). Carried wording staleness from r95 line 49.
- **V50 — confirmed declaration erratum.** `LOG.md:2893` declares the C2 before-clause as
  "5 entities / 1 relation / 4 events / **5 sources** at r95"; r95 has **4** sources
  (`sources.json` length 4). Delivered documents say "four inherited sources" correctly
  (`r96 README:3`, scope note:26). The erratum is in the round declaration, not the
  artifact.
- **Documentation gaps (unowned paths, closure items):** `corpus/tools/README.md` gained a
  thorough Round-96 addendum for `map_obligations` but **mentions `dependency_freeze` zero
  times** (`grep -c -i freeze` → 0), leaving V23's check (c) PARTIAL; `corpus/README.md`'s
  tool registry and `SKILL.md`'s row carry no `dependency_freeze` entry (V29, V35 D3);
  `corpus/fixtures/README.md` has no Round-96 section and its census is not re-declared
  (V29, V35 D6). These paths are outside every producer's byte ownership and cannot be
  fixed by a seat.
- **BR-05 (carried, live):** `map_obligations`' self-test scratch still lives under the
  repo root and is not gitignored. I observed a transient
  `map-obligations-self-test-e1crqgdu/` at the repo root that vanished on the next check
  (cleaned on normal exit); V27 reports `corpus/tools/__pycache__/` gaining a
  `dependency_freeze` `.pyc` (gitignored, pre-existing dir). Q1 §7.5 notes the same.

## 6. Conflicts reconciled explicitly

| Conflict | Resolution |
|---|---|
| **V23 FAIL** (5 pins, not 4) vs every other C3 seat's PASS | **V23 stands as a confirmed harm** on the scope-shape sub-check; it is not re-rolled. The other seats PASS the *detection semantics*, which also verify. Both are true: the gate works, and the delivered contract carries a foreign pin. |
| **V34 INCONCLUSIVE (interim)** vs my post-change verification | V34 closed before Q1/Q2 landed and never updated. Its baseline half matches mine exactly. I re-verified its post-change scope myself (§2); the interim status is a timing artifact, not a disagreement. No seat's verdict is overridden by reading; I supply the missing post-change half first-hand. |
| **V37-verdict-adjacency INCOMPLETE** | No adjacency verdict exists. Its §1 (`PROVINCE.md` byte-identical, blob `7c599c39`) is usable evidence; §2 is a placeholder. V31 independently issues the adjacency PASS (charter byte-identical, change set lane-local, zero sibling writes). |
| **V02/V07: added pins are droppable** vs C1(b) "22→24" | Both true: the delivered contract pins 24 and the self-test reports `24/24`; the *mechanism* tolerates a 23-case contract. C1(b)'s declared claim holds; the tolerance is a named residual. |
| **V20 D4 (BR-01 prose half open)** vs C3 "closes BR-01" | The declaration names the JSON-edge instance, which is closed and demonstrated; the broader debt wording is not fully closed. C3's claim holds as declared; the wider reading is a carried residual. |
| **V20 D3 (no path binding)** vs "chain 4/4 clean" | The receipts are real but not path-bound; a same-named copy is indistinguishable. Bounded: I verified the *delivered* paths myself by running the tool against `corpus/fixtures/<name>` and by `git diff` on those exact paths. |
| **V50 "5 sources"** vs delivered docs | The erratum is in `LOG.md` (declaration), not in the artifact; delivered docs are correct. |
| **My own intermediate exit-0 on a D1 probe** | Self-inflicted scratch edit, corrected and re-run; not a harm. Recorded so no seat cites it as evidence. |
| **V27 `/tmp` inode exhaustion, V40 host conditions** | Host conditions, not repo findings; every seat that hit it re-ran under scratch. My own `/tmp` was never needed. |
| **Roster: V43/V58 initially ABSENT** | Resolved as late landings: a mutual poll-wait on 63 reports including mine (their own poll logs), broken when my report landed at 18:04 and V43's stall escape fired at 18:19:08. Both PASS; V43 itself records the liveness finding. Neither altered any verdict. |

No conflict was resolved by preferring a seat's authority; each was resolved by my own run
or by the artifact's own bytes.

## 7. Per-axis table

| Axis | Verdict on the delivered revision | Evidence (first-hand unless marked) |
|---|---|---|
| **calibration** | **improved (bounded)** | C1(a) deletion class exit 0 → 1 `inventory_mismatch`; C1(c) three V37-D1 forms exit 0 → 1 `dual_pointer` with no false positives and the canonical/r88 controls unchanged; C1(b) 24/24 pinned, both new cases proven load-bearing three ways; full non-regression battery green. Bounds: consistent-regeneration exits 0; the two added pins are droppable (23/24 still PASS); `dual_pointer` has no persisted pin; Q1's subset-tolerant contract rule. |
| **depth** | **improved (bounded)** | C2: 5/1/5 counts, 5 sources, 16/16 obligations with 15 inherited rows diff-free outside the namespace column, J16 anchored at `fictional-excerpts.md:37`, `check_bible` CLEAN, `support_check` 16/16+18/18, census 169→170 with +1 clean and zero inherited changes, no contradiction asserted (r35 counterpart has 1). Bounds: V12 F1 delimiter cell count; stale "new relation" wording; V13/V54 trace notes. |
| **coverage** | **improved (bounded)** | C3: new gate + persisted contract; chain 4/4 clean exit 0; `REDUCTION-DETECTED` on the exact BR-01 mutation (previously invisible to every gate) plus addition/endpoint exit 1 with stable IDs; exit-2 surface complete; `--self-test` 14/14; zero corpus modification. Bounds: **H1 foreign `c3red` pin (V23's FAIL, confirmed)**; H2 no path binding; H3 BR-01 prose half open; `--freeze` unguarded; four LOW items. |
| **operability** *(witnessed)* | **improved (bounded)** | 24/24 and 14/14 self-tests exit 0, every documented command replays, one terminal `RESULT` line, empty stderr, 0/1/2 contract holds; corpus manifest byte-identical around runs (V05/V19/V21/V30/V35/V42/V44/V52 concur). Harm: the delivered contract's foreign scratch pin and the unguarded `--freeze` write path (V35 D1/D5, V30, V20 D2) — a delivered-artifact defect that changes no chain verdict. |
| **freshness** *(witnessed)* | **unchanged / not harmed** | All six producer artifacts present and green on the delivered revision; no stale HEAD pins; every spot-checked citation resolves; carried r95 wording accurate with counts updated (V28/V36). Gaps are closure-side: `corpus/fixtures/README.md` Round-96 census not re-declared, `corpus/README.md`/`SKILL.md` registry rows stale (V29/V35 D3/D6). |
| **adjacency** *(witnessed)* | **not harmed** | `PROVINCE.md` byte-identical to `dcb2d92` (blob `7c599c39`, empty diff); the whole change set is lane-local and inside the declared byte ownership; zero writes to sibling lanes or domain source trees; no r96 strays in the parent tree (V31 PASS, V37 §1, V27 OTHER=0, V39). |

No scalar score is assigned; the axes are reported as verdicts with named bounds, per the
round's rule.

## 8. Verdict: ADMIT (conditional)

**C1, C2 and C3 each verify on the delivered revision, and none of the three owned axes
(depth, coverage, calibration) is harmed.** Every declared C3 assertion — gate and
contract exist, chain 4/4 clean, the BR-01 mutation exits 1 `REDUCTION-DETECTED`, an
added edge exits 1, exit-2 could-not-evaluate, persisted `--self-test`, zero corpus
modification beyond the two new tool files — is true of the bytes on disk under my own
commands.

Admission is conditional on the following closure actions. They are hygiene and
documentation items; none of them changes a chain verdict, and none of them re-opens a
harmed finding.

**Mandatory (must land at closure, or be explicitly accepted by the L1 in writing):**

1. **C-1 — remove `pins.c3red`** from `corpus/tools/dependency-freeze-contract.json` (or
   explicitly accept it in the closure record), then re-run
   `python3 corpus/tools/dependency_freeze.py --self-test` (expect `SELF-TEST 14/14`,
   exit 0) and the chain 4/4 (expect four `RESULT PASS` exit 0). This discharges V23's
   FAIL. If the pin is kept, the closure must state that the delivered contract
   references a seat scratch path and that the frozen set is five, not four.
2. **C-2 — record the byte-ownership breach**: V41's `--freeze` probe wrote into a
   producer-owned delivered artifact (self-disclosed, owner-informed). Record it as a
   round property alongside the r94-F01 cwd-defect class.
3. **C-3 — record the `--freeze` hazard as r97 debt**: no `corpus/fixtures/` scope guard;
   any `--freeze <dir>` rewrites the delivered contract. Either add the guard in r97 or
   mark `--freeze` delivery-time-only in the tool README.
4. **C-4 — record H2 (no path binding) as r97 debt**, or add the `ROOT / pin["fixture"]`
   comparison so a receipt proves which paths were verified.
5. **C-5 — record H3**: BR-01's markdown-layer half remains open; C3 closes the JSON-edge
   instance only.
6. **C-6 — record the calibration bounds**: consistent regeneration exits 0; the two
   added self-test pins are droppable (23/24 still passes); `dual_pointer` has no
   persisted pin.
7. **C-7 — close the two open report gaps**: V43 and V58 landed late (18:19) and both are
   PASS, so no collection is outstanding for them; the remaining gap is
   **V37-verdict-adjacency's unfinished §2**. Either have it completed or record in the
   closure that the adjacency verdict rests on V31 alone. Do not read V37's incomplete
   report as a verdict.
8. **C-8 — documentation items on unowned paths**: `corpus/tools/README.md`
   `dependency_freeze` addendum, `corpus/README.md` tool-registry row, `SKILL.md`
   registry row, `corpus/fixtures/README.md` Round-96 section with the re-declared census
   (170 / 36 clean / 134 negative / 421 lines). All are outside seat byte ownership.

**Recommended (cosmetic, non-blocking):** fix the r96 map's 8-cell delimiter row
(line 44); correct the stale "new relation" wording (line 50); correct the `LOG.md`
before-clause to "4 sources at r95"; consider a `dual_pointer` self-test case; align the
`SELF-TEST-MISMATCH` exit code (1 vs 2) between the two tools.

**Same-lane rule respected:** no `[x]`, no promotion, no commits, no pushes. Nothing on
any axis is claimed to have regressed materially; nothing harmed is smoothed away —
V23's FAIL stands recorded as a confirmed deviation with its own reproduction, and my
verdict does not depend on the three reports that are absent or incomplete.

## 9. Bottom line

**ADMIT (conditional)** — on the delivered revision (`map_obligations.py 2b0ba815…`,
contract `97b76bb8…`, `dependency_freeze.py a3b57978…`, freeze contract `7d568cc4…`,
fixture 10 files, census 170/36/134/421) C1, C2 and C3 each verify first-hand: the r95
deletion class and all three V37-D1 legacy forms now exit 1 with stable
`inventory_mismatch` / `dual_pointer` IDs and 24/24 persisted pins proven load-bearing
(calibration, improved-bounded); the r96 fixture delivers 5/1/5, 5 sources, 16/16
obligations with 15 inherited rows unchanged outside the namespace column, CLEAN, no
contradiction (depth, improved-bounded); and the new freeze gate closes BR-01's JSON-edge
half with 4/4 clean, REDUCTION-/ADDITION-DETECTED/ENDPOINT-CHANGE exit 1, a complete
exit-2 surface, 14/14 self-test and zero corpus modification (coverage, improved-bounded)
— subject to eight exact closure conditions, chief among them V23's **confirmed and
un-re-rolled** FAIL: the delivered contract carries a foreign `c3red` scratch pin written
by V41's `--freeze` probe, which must be removed or explicitly accepted, together with
the recorded `--freeze` scope-guard, path-binding and BR-01-prose-half residuals, and the
completion or explicit waiver of V37's unfinished adjacency battery (V43 and V58 landed
late and both PASS; 64/64 reports are now present). No axis is harmed; no scalar score is
assigned.
