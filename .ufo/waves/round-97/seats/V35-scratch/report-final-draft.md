# V35 — adjudicator (round 97, FINAL)

- Seat: V35 adjudicator, round-97 single wave, lane `lore-shokunin`.
- Baseline: r96 closure `f3e09f9`; worktree HEAD `2393934237ea076366f3db6dceeff033edb52ab1` (`2393934`, r96 SCORECARD closure; `git diff HEAD -- SCORECARD.md` empty).
- Mandate: poll until the other 63 reports exist, read them all, reconcile conflicts explicitly, admit ONLY if C1/C2/C3 verify on the delivered revision and no axis is harmed; per-axis table; exact admission conditions; never re-roll harmed findings.
- All commands below ran from `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. My only writes are this report and `.ufo/waves/round-97/seats/V35-scratch/`. No commits, no pushes, no network, no nested agents.

## 0. Delivered revision (frozen for this adjudication)

```
86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9  corpus/tools/map_obligations.py            (R1)
2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41  corpus/tools/map-obligations-contract.json (R2, 25 cases)
6278e59b8df01c1cb63ca6080cb959999f400d95128b96e84e5476f4c4ebb992  corpus/tools/README.md                     (R2)
b06275f3bbdeabaab615138b3004703fce701a786af882d3b732828b37722130  corpus/tools/dependency_freeze.py          (R3)
27273be27d33ad864f06d656f28dca8eabc9d76f6ebe62583372a88c9e64e781  corpus/tools/dependency-freeze-contract.json (R3, 16 cases)
e851f068cfd7ed02c97054df18729c4c5a9b8bf60d99d7c9116f427d765440de  corpus/fixtures/r96-crossing-response/claim-excerpt-map.md (R4 repair)
d9387b7d73264dfc6c01d27cc6bf24c58ef6bdb4461d2ae8fbfdb6376d9e019f  corpus/fixtures/r97-crossing-acknowledgment/README.md       (R5)
49d4834e124fa6cfaa1a73cd5d1a7bc2cb59711c6233b418fe7485a17eedc94f  corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md (R5)
438fb513a62496c41179ead3ea2a55a69ff4ce1fd191c3a7ebccb10651a8dc73  corpus/fixtures/r97-crossing-acknowledgment/sources.json
73063a863a68fc4feae073ce74cfa9e5fddb4f9cc4060d12b333d495a255895b  corpus/fixtures/r97-crossing-acknowledgment/timeline.json
8ba491cb249dd57f6aee8ca216133b07c06287c0240be658ea2e68da0cf5703c  corpus/fixtures/r97-crossing-acknowledgment/fictional-excerpts.md
026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b  corpus/fixtures/r97-crossing-acknowledgment/entities.json
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  corpus/fixtures/r97-crossing-acknowledgment/relations.json
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  corpus/fixtures/r97-crossing-acknowledgment/contradictions.json
58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37  corpus/fixtures/r97-crossing-acknowledgment/inspiration-note.md
b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd  corpus/fixtures/r97-crossing-acknowledgment/source-excerpt.md
5e3b4225c30de8a2a75b675b59acb5c597b290e5a45f2caa01663da586e042b5  corpus/knowledge/r97-acknowledgment-scope-note.md          (R6)
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py  (unchanged pin)
55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  corpus/tools/support_check.py   (unchanged)
```

Change surface vs `f3e09f9` (`git status --porcelain`, my run): exactly the declared set — 7 modified files (`LOG.md` +61/−0 declaration; 5 tool files; r96 map) and the untracked r97 fixture (10 files) + R6 note + `.ufo/waves/round-97/`. `SCORECARD.md`'s delta is committed in `2393934`, not an r97 write. r94/r95/r88 fixtures: `git diff --stat f3e09f9` empty. Parent tree `git status --porcelain` empty. No strays (my runs; V28/V34 concur).

## 1. Report inventory — 64/64 present and read

Present and read: R1–R6 (all six producers) + V01–V58 (all 58 verifiers), 63 others + this report. Every landed report was read (full reads for all producer reports, all verdict seats, and every report carrying a non-PASS status or a named bound; a structured per-report digest of verdict/flag lines for the remainder, plus full re-reads of any report whose status changed mid-wave).

- **Verdict census of the 63 others: 2 FAIL (V12, V46), 0 other FAILs; V56 initially IN PROGRESS (final: PASS); all other reports PASS with disclosed bounds.** Both FAILs are seat-brief-level (brief stricter than the LOG declaration) and are recorded, not re-rolled (§3, §6).
- **Late landings / timing artifacts (recorded, no fabrication):** V09/V26/V30/V45 were written before R3's report landed (poll-window expiry just before/at 18:56:23) and were finalized after; V37's poll hit at try 38; V33/V52/V53/V55 polled to expiry and then verified delivered bytes. V58 (presence-final) hit its 1800 s watcher deadline at 19:19 with 61/64 and recorded V24/V35/V40 as absent-with-active-work, not fabricated. V40 (receipt) wrote at 19:29 with V24/V35 absent. V24 (scope-creep) capped at ~19:58:27 — the last landing — and is read below. V56 names the endgame quad {V24, V35, V40, V58} and the residual pair V24↔V35 with its escapes; the r96 "all-reports poll must subtract self" class recurred and is recorded as process debt (V24's condition `ALL ≥ 64` is unreachable until it writes itself).
- **No seat was verified against a plan anywhere; every quoted output in every report is from executed commands on delivered bytes.**

## 2. C1 — calibration: VERIFIED (all three parts)

### (a) `dual_pointer` persisted as case 25 — VERIFIED

```
$ python3 -c "import json;c=json.load(open('corpus/tools/map-obligations-contract.json'));print(len(c['self_test']['cases']),[x for x in c['self_test']['cases'] if x['id']=='dual_pointer'])"
25 [{'id': 'dual_pointer', 'exit': 1, 'finding_ids': ['dual_pointer']}]
$ python3 corpus/tools/map_obligations.py --self-test | head -1
SELF-TEST CASES 25/25 pinned
$ python3 corpus/tools/map_obligations.py --self-test | grep dual_pointer
SELF-TEST PASS dual_pointer exit=1 findings=['dual_pointer']
$ python3 corpus/tools/map_obligations.py --self-test >/dev/null; echo exit=$?
exit=0
```

### (b) Loader tightened: ANY missing pinned case fails — VERIFIED, with the closed pre-state

My before-state run on a copy of the r96 tool + contract (scratch): dropping `schema_drift` → `SELF-TEST CASES 23/24 pinned` / `RESULT PASS`, exit 0 (the r96 tolerance). Delivered revision, my runs on scratch contract copies:

```
$ (contract copy: dual_pointer dropped, 25 -> 24)
FINDING self_test_contract: contract drops implemented self-test cases: dual_pointer
RESULT ERROR                                    exit=2
$ (contract copy: schema_drift dropped, 25 -> 24)
FINDING self_test_contract: contract drops implemented self-test cases: schema_drift
RESULT ERROR                                    exit=2
```

Loader line: `missing = sorted(set(SELF_TEST_CASES) - set(expected))` (was `set(CORE_SELF_TEST_CASES)`). The complementary half is unchanged: a contract pinning an unimplemented case fails closed (V31/V32/V38 re-probed).

### (c) The pin is load-bearing — VERIFIED

Scratch copy of the delivered tool with the emission neutralized (`if mention is not None:` → `if False:` in `parse_map_text`), live 25-case contract:

```
SELF-TEST FAIL dual_pointer exit=0 findings=none
FINDING self_test_mismatch: isolated CLI outcomes differ from persisted expectations
RESULT ERROR                                    exit=2
```

(The `RESULT PASS` line inside the failure block is the failing case's own subprocess stdout, printed by the harness diagnostics; the tool's verdict is `RESULT ERROR`, exit 2 — the same reading R1/V01/V05/V31/V32/V53 recorded. V01/V05 note R1's scratch-log label `exit=1 findings=[]` vs the actual `exit=0 findings=none`: cosmetic labeling at a different probe point; the verdict is identical everywhere.) R2/V31/V32/V53 reproduce with independent probe points (`second_pointer_mention()` short-circuit; expectation flip; renamed emission) — all turn exactly the pinned case red.

### C1 non-regression battery (my runs, delivered revision)

```
r88  raw=10 mapped=10 / 10/10; 2/2; 12/12  PASS exit=0      r93  raw=12 mapped=12 / 12/12; 3/3; 15/15  PASS exit=0
r94  raw=14 mapped=14 / 14/14; 2/2; 16/16  PASS exit=0      r95  raw=15 mapped=15 / 15/15; 2/2; 17/17  PASS exit=0
r96  raw=16 mapped=16 / 16/16; 2/2; 18/18  PASS exit=0      r97  raw=17 mapped=17 / 17/17; 2/2; 19/19  PASS exit=0
r87  unsupported_map exit=2    r89  unsupported_map exit=2    --frozen r93: FROZEN expected=PASS/0 findings=none matched  exit=0
```

V03's byte-diff shows every r88–r96 battery output byte-identical to the pre-R1 baseline; the only diffs are the declared new surfaces (r97, self-test 24→25). V57 audits 4/4 C1 clauses; V31 25-drop sweep: 0 still-green; V44's 17-probe matrix matches V04's 26-case matrix on a different base.

## 3. C2 — coverage: VERIFIED (with two seat-level FAILs recorded)

### C2(a)–(d) on the delivered revision (my runs)

```
$ python3 corpus/tools/dependency_freeze.py --freeze <scratch>/foreign-r95   # out of corpus/fixtures/**
FINDING SCOPE-REFUSED: --freeze refuses …; the frozen scope is corpus/fixtures/** (integration-time operation only)
RESULT ERROR                                    exit=2      # pins before = pins after (no write)
$ python3 corpus/tools/dependency_freeze.py <scratch>/foreign/r96-crossing-response   # byte-identical copy
FINDING PATH-MISMATCH: pin r96-crossing-response names corpus/fixtures/r96-crossing-response (resolves to …/corpus/fixtures/r96-crossing-response); invoked fixture resolves to …/foreign/r96-crossing-response
RESULT ERROR                                    exit=2      # real path: RESULT PASS exit=0
$ (tamper at the pinned path: timeline.json description word)
FINDING DIGEST-MISMATCH: content digest 509478fa… != pin d422a9b3…; changed: timeline.json (sha256 ea0225f9… -> 2d5f5dd6…); fixture bytes changed outside the frozen inventory
RESULT ERROR                                    exit=2
$ python3 corpus/tools/dependency_freeze.py --self-test | tail -2
SELF-TEST 16/16
RESULT PASS                                     exit=0      # no TMPDIR redirect needed (scratch dir=ROOT)
```

Chain: r88/r94/r95/r96 all `RESULT PASS` exit 0 with the r96 digests (`15ef230e…/2527beb9…/d541ae64…/d422a9b3…`). Contract: 4 pins, each `fixture` = repo-relative path; r96 pin `revision` refreshed `60dba0c2…→2393934…`; `content_sha256`/`files`/`events`/`relations`/`counts` byte-unchanged. `--freeze corpus/fixtures` itself and a symlink escaping the scope are refused; the in-scope same-named shadow freeze is refused (extra fail-closed behavior beyond the four items, reported under the pinned `SCOPE-REFUSED` id); `freeze()` now propagates the post-freeze verify exit code. V06/V07/V08/V09/V10/V11/V30/V32/V45/V55 all reproduce the battery independently; V53 re-ran 6/6 quoted outputs REPRODUCED; V38 line-by-line confirms every C2 clause.

### The two seat-level FAILs (confirmed, recorded, not re-rolled)

**V12 — `c2-refreeze-integrity` FAIL.** Its brief required proof that "the r96 pin now pins the post-repair map digest". I reproduced the measurement first-hand: `grep -c "e851f068" corpus/tools/dependency-freeze-contract.json` → `0`; `claim-excerpt-map` appears once, only in the `provenance_note` prose; the pin's key set is `['content_sha256','counts','events','files','fixture','relations','revision']`; `content_sha256` is `d422a9b3…` before and after the refresh because `DATA_FILES` covers only the five JSON tables. So the stronger proof is **unmet as delivered** — the map digest is not pinned (the map is not a pinned file at all). V12 also proved the complementary half: the re-freeze changed only the r96 pin's `revision`, is reproducible through the guarded path (its `refreeze_harness.py` reproduces the delivered r96 pin byte-for-byte), and the JSON digests are byte-identical to `f3e09f9`. R3's own report records the same measured discrepancy against the claim's "digest changes by the repair" implication, and the contract's `provenance_note` self-documents it. **Reconciliation:** the LOG-declared C2 wording — "re-frozen THROUGH the guarded `--freeze` path (pin refresh), demonstrating the guard end-to-end" — holds and is verified (the refresh ran after the repair, `map mtime 18:43:42 < contract mtime 18:55:14`, and is reproducible); the r96-closure errata's "digest change" implication and the seat brief's stronger phrasing are inaccurate. V12's FAIL stands as a recorded claim-text/scope-shape harm; the delivered artifact is internally consistent.

**V46 — `cross-gates-r97` FAIL.** Its brief required the BR-01 catch on the r97 fixture's new tick-13 edge. Delivered revision: `dependency_freeze.py corpus/fixtures/r97-crossing-acknowledgment` → `FINDING UNPINNED-FIXTURE … exit 2` on intact and mutated bytes alike (the fixture is not in the pin set); `check_bible`/`support_check`/`map_obligations` correctly stay green on the dropped-edge copy. The catch reproduces exactly one integration-time pin away: with the fixture pinned in a scratch mirror through the delivered guarded `--freeze`, the same mutation → `FINDING REDUCTION-DETECTED: event acknowledgment-aru-records lost depends_on ['response-evin-salt-court']` / `RESULT FAIL` exit 1 (`dependency-edges 4/5`). **Reconciliation:** the declaration claims "chain verifies 4/4 clean at closure" (r88/r94/r95/r96) — verified; it does not claim r97 is pinned. R3's residual 2 and V22/V30/V32/V34/V55 name the same bound (r97 unpinned; r98 candidate). V46's FAIL stands as a recorded coverage-gap finding: the round's one new `depends_on` edge is not frozen; its completeness is covered lexically by `map_obligations` (17/17) and `check_bible` (structure), not by the edge pin.

## 4. C3 — depth: VERIFIED

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r97-crossing-acknowledgment
CLEAN: schema, citations, relations, timeline; 0 violations     exit=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r97-crossing-acknowledgment | tail -3
RECEIPT JSON-FACTS 17; EDITORIAL-ROWS 2; TOTAL-ROWS 19
SOURCE-SUPPORT 17/17; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 19/19; VALIDATED-ROWS 19/19
RESULT PASS                                                     exit=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r97-crossing-acknowledgment
OBLIGATIONS raw=17 mapped=17 / INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19 / RESULT PASS  exit=0
```

- **Counts 5/1/5→5/1/6, sources 5→6:** verified by `json.load` counts and by R4/R5/R6/V13/V14/V18/V29/V43/V50/V54. New source `aru-acknowledgment-note`; new event `acknowledgment-aru-records` (tick 13, `aru`, `chalk-stair`, `depends_on: ["response-evin-salt-court"]`); inherited rows parsed-value identical; five copy files byte-identical; `fictional-excerpts.md` strict byte-prefix (2588→3410); map J01–J16 identical modulo the namespace column; J17 span 44-53, anchor line 48, in-section only.
- **Unresolved preserved:** the note's four clauses (lines 48-51) trace to `timeline.json#/5` + `sources.json#/5`; no resolution/accusation/reconciliation/winner/new-duty/contradiction/verdict reading is constructible from any delivered byte (V17, V43's 12-probe constructibility matrix, V29 §6, V54 §F7 — all concur; `contradictions.json` stays `[]`). The r96 cosmetic repair is exactly two lines with 18 data rows byte-unchanged and both r96 receipts byte-identical pre/post (my runs; R4/V12/V18/V19/V28/V29/V33/V34/V38/V52 concur).
- **Census 170→171:** my own full sweep → `CENSUS dirs=171 clean=37 negative=134 other=0 violation_lines=421` (V13/V21/V32/V41/V55 reproduce; V41's file-level receipt: 1020 files, modified=1, new=10).

## 5. Other confirmed defects/observations on delivered bytes (outside the three claims)

1. **Doc-parity gap (closure-side, unowned paths):** `corpus/tools/README.md:175` still describes `dependency_freeze` in its pre-r97 form (self-test "14/14"; all three r96 hazards listed as open — every clause false on the delivered revision); the r97 addendum covers `map_obligations` only. Same class: `SKILL.md:87/98/100`, `corpus/README.md:37/38`, `corpus/fixtures/README.md` (no Round-97 section; census text 170), `corpus/knowledge/r91-c9-watch.md` (row 6 due). V26's 13-item list + V39's P1–P5 checklist + V47's seven wording corrections are the closure worklist; V33 names the README paragraph as condition C-R97-C2DOC. R2's report does not mention `dependency_freeze` (grep 0) — the C2 landing post-dated R2's report.
2. **V32 D1 (MEDIUM, delivered behavior):** the `dependency_freeze` self-test scratch moved from system temp to the repo root (`dir=ROOT`), spreading BR-05 to the second tool; observed transient repo-root dirs during concurrent self-tests; not gitignored. R3 justified it by the `/tmp` inode exhaustion, which has since cleared (D7). Bounded operability regression vs r96; recorded.
3. **V11 D1/D2 (LOW, fail-closed):** a path-less (legacy) pin cannot be refreshed in place (`SCOPE-REFUSED … already names None` / verify `CONTRACT-INVALID`; migration requires a manual contract edit); the contract `precedence` text does not name the new exit-2 order/ids (`SCOPE-REFUSED`, `PATH-MISMATCH`) — only `scope`/`provenance_note` do.
4. **Carried stale receipt pins in knowledge notes:** `r95-aftermath-scope-note.md:51` pins `9224a684…`; `r96-response-scope-note.md:55` pins `6634e176…`/`8173bb97…`; R6's note records its mid-flight `70795150…`/`97b76bb8…` explicitly as in-flight with a re-run instruction (V25/V33; same class as r96's C-F1/C-NOTE).
5. **Carried checker blind spots (documented bounds, unchanged):** `check_bible` does not see an emptied `depends_on`, a wrong-but-earlier edge, or a deleted terminal row (V20/V29); `support_check` is silent on the two documented F15 mutants (V52); the freeze pin covers the five JSON tables only (BR-01's prose half remains open).
6. **V31 bound (feature scope):** `dual_pointer` detection is legacy-dialect-scoped — a second bare field-path token in a canonical-header parenthetical passes silently; a second `.json#` pointer stays `unsupported_map` exit 2 (fail-closed).
7. **V51 observation (bounded prose):** the mandated r96 repair removed the map's standalone relation-bound sentence from the normalization prose; the bound survives in the J11 anchor, README, `sources.json` reliability note, and both scope notes. V18 records the pre-existing right-align colon position in the repaired delimiter (render-only, not introduced by the repair). V25 records the carried "new relation" sentence in the r95 map (outside this round's declared repair scope; r98 candidate).
8. **Host conditions (not repo findings):** `/tmp` inode exhaustion recurred this round (100% at 18:43, recovered to 2% by 18:57); seats re-ran under repo scratch; `fake-contract-backup.json` (r96-baseline contract bytes) disclosed in `/tmp` by V28/V34. `kotodama-shokunin`'s concurrent round-10 activity attributed by path ownership (V28/V34). BR-05 (repo-root self-test scratch) now covers both tools (V32 D1/D6).
9. **Adjacency:** `PROVINCE.md`/`SHONEN.md`/`SKILL.md`/`README.md`/`l0-questions.md` byte-identical to `f3e09f9` (V28/V34); change set exactly the declared ownership; no sibling/domain writes; no parent-tree strays; no commits/pushes (reflog clean; V34 A6). SHONEN four `[~]`, zero `[x]` (V36).

## 6. Conflicts reconciled explicitly

| Conflict | Resolution |
|---|---|
| **V12 FAIL** ("pin pins the post-repair map digest" unmet) vs C2's "(pin refresh)" | Both true at their levels: the refresh ran through the guarded path and is reproducible (revision-only), but the map is not in the pin payload, so the stronger phrasing fails. V12 stands as recorded; the LOG wording holds; closure must append the erratum (C-1). I reproduced V12's measurement first-hand. |
| **V46 FAIL** (BR-01 catch on r97) vs "chain 4/4 clean" | The declaration claims 4/4 (r88/r94/r95/r96) — verified. r97 unpinned is a declared-scope bound (R3 residual 2), not a claim failure; the catch reproduces one pin away. V46 stands as recorded (C-2). |
| Re-freeze "digest change" implication (r96 errata) vs measured `d422a9b3…` unchanged | The errata's implication is inaccurate; R3/V10/V12/V30/V45/V53/V55/V57/V33 all record the measured fact; the declaration's "(pin refresh)" is satisfied. Erratum correction at closure (C-1). |
| V09/V26/V30/V45 interim PENDING/INCONCLUSIVE vs final PASS | Timing artifacts (poll expiry at/just before R3's 18:56:23 report); all finalized on delivered bytes; V30/V45 verified R3's bytes before its report landed. No verdict conflict. |
| V01/V05: R1's scratch-log label (`exit=1 findings=[]`) vs actual (`exit=0 findings=none`) | Cosmetic label at a different neutralization point; all verdicts identical; recorded so no seat cites it as a discrepancy. |
| V29 vs V54 (depth), V30 vs V55 (coverage) | Independent verdicts, AGREE, no material divergence (V54 §4 table; V55 §5 table). |
| V56 IN PROGRESS vs final | Final version PASS: mutual-wait quad {V24,V35,V40,V58} found and characterized; unwound by V58 (19:18) and V40 (19:28:48); residual pair V24↔V35 bounded by V24's cap ≈19:58:27 / my deadline ≈21:42:51. Process-debt class recorded (r96 recurrence). |
| V58/V40 "V35 ABSENT" vs this report | Presence-seat timing artifacts: both wrote before my (last) report by their own deadlines; neither fabricated anything; their absent-entries are expected under the protocol and are not findings against this adjudication. |
| "5 sources at r96" erratum class (r96 V50) | Not recurred in r97 declarations; delivered docs consistent (V25). |
| `/tmp` exhaustion, kotodama activity, SCORECARD delta | Host/sibling/attribution items, not repo findings (V28/V34). |

No conflict was resolved by preferring a seat's authority; each was resolved by my own run or by the delivered bytes.

## 7. Per-axis table

| Axis | Verdict on the delivered revision | Evidence (first-hand unless marked) |
|---|---|---|
| **calibration** | **improved (bounded)** | C1: `dual_pointer` pinned as case 25 (25/25 exit 0, my run); loader fails closed on any dropped pinned case (my runs: dual_pointer/schema_drift → exit 2; r96 tool 23/24 exit 0 as the closed pre-state); pin load-bearing under neutralization (my run); full r87–r97 battery + frozen r93 + r87/r89 fail-closed byte-stable. Bounds: self-test binds consistency, not truth; `dual_pointer` legacy-dialect-scoped (V31); regenerated-declaration bound carried; BR-05 scratch now on both tools (V32 D1). |
| **depth** | **improved (bounded)** | C3: 5/1/6, 6 sources, 17/17 obligations with 16 inherited rows unchanged outside the namespace column, J17 span 44-53 anchor line 48, CLEAN/17/17/19/19 PASS, census 171/37/134/421, repair byte-minimal with receipts unchanged, unresolved preserved (no constructible resolution/blame reading). Bounds: structural/lexical evidence; authored class label; checker blind spots (V20); editorial tick encodings; r95 map's carried sentence (V25/V51). |
| **coverage** | **improved (bounded)** | C2: scope guard (SCOPE-REFUSED, no write), path binding (PATH-MISMATCH exit 2 on byte-identical foreign copy; real path exit 0), DIGEST-MISMATCH names the file, self-test 16/16, guarded-path re-freeze (revision-only, reproducible), chain 4/4. **Two seat-level FAILs stand recorded: V12 (map digest not pinned) and V46 (r97 edge unfrozen)** — both brief-stricter-than-declaration, both with the declaration-level claims verified. Bounds: r97 unpinned; JSON-only pin payload; resolve()-based semantics; doc surfaces stale (V26/V30/V33/V55). |
| **operability** *(witnessed)* | **improved (bounded)** | 25/25 + 16/16 self-tests, every documented command replays (V27/V32), 0/1/2 contract with one terminal RESULT line and empty stderr across 23 invocations (V32), corpus manifest byte-identical around runs, census 171/37/134/421. Bound: D1 repo-root self-test scratch on both tools (BR-05 spread); D2 README stale; D5 r97 unpinned (V32). |
| **freshness** *(witnessed)* | **unchanged / not harmed** | All live pins fresh and reproduced (checker `ff9fd2aa…`, C9 pair green + expected control, frozen r93, chain pins, self-tests, census); historical captures append-only (LOG +61/−0; round-96 tree untouched); one bounded new staleness — the tools README dependency_freeze paragraph (F-1, condition C-R97-C2DOC); two carried stale note pins unrepaired (conditions). No improvement claimed (V33). |
| **adjacency** *(witnessed)* | **not harmed** | `PROVINCE.md` byte-identical (blob `7c599c39`); change set exactly the declared ownership; zero sibling/domain writes; no parent-tree strays (r94-F01 class did not recur); no commits/pushes; mythology editorial-only in new bytes; rights/mechanics scan clean (V28/V34). Disclosed caveats: `/tmp` scratch, lane-root self-test scratch, r97 unpinned. |

No scalar score is assigned; axes are verdicts with named bounds.

## 8. Verdict: ADMIT (conditional)

**C1, C2 and C3 each verify on the delivered revision, and none of the three owned axes is harmed.** The two seat-level FAILs (V12, V46) are confirmed and recorded — they concern brief-phrasings stronger than the LOG declaration and a declared-scope gap (r97 unpinned), not failures of any declared C1/C2/C3 claim. Admission is conditional on the following closure actions; none changes a chain verdict, none re-opens a harmed finding.

**Mandatory (must land at closure, or be explicitly accepted by the L1 in writing):**

1. **C-1 — append the re-freeze erratum.** Record that the r96 re-freeze was a guarded-path **revision/format refresh** (pin `revision` `60dba0c2…→2393934…`, top-level `revision` likewise) and that the pin covers only the five JSON tables — the map digest `e851f068…` is not (and cannot be) pinned; the r96-closure errata's "digest change" implication is inaccurate. V12's FAIL stands recorded and is discharged by this erratum, not re-rolled.
2. **C-2 — record the r97-unpinned bound.** The chain is exactly the declared 4/4; the r97 fixture's new tick-13 edge is not frozen (V46's FAIL stands recorded). Either pin r97 in r98 or record the bound and its lexical coverage (map_obligations 17/17 + check_bible).
3. **C-3 — closure doc pass (unowned paths; V26 §3/§4 exact texts, V39 P1–P5, V47 corrections):** tools README C2 addendum (or dated supersession note under the r96 "Hazards (r97 debt)" sentence; append-only convention); `SKILL.md:87/98/100` rows; `corpus/README.md:37/38`; `corpus/fixtures/README.md` Round-97 section + census 171/37/134/421 + fourth-round pin note; `corpus/knowledge/r91-c9-watch.md` row 6 (V48 content).
4. **C-4 — record the operability bound V32 D1/D6:** the `dependency_freeze` self-test scratch now lives at the repo root (`dir=ROOT`, BR-05 on both tools, transient `??` entries visible to concurrent seats); consider gitignoring the pattern at closure.
5. **C-5 — record the carried conditions:** the two stale note receipt pins (r95 `9224a684…`, r96 `6634e176…`/`8173bb97…`); R6's note in-flight pins (self-labelled); V11 D1/D2 (path-less pin migration; `precedence` text); V31 canonical-dialect bound; check_bible/support_check blind spots; BR-01 prose half open.
6. **C-6 — record the process/host items:** the r96-recurring all-reports poll class (V24's `ALL ≥ 64` unreachable before self-write; V56's characterization); late landings V58/V40/V24 and their absent-entries; `/tmp` inode exhaustion and disclosed `/tmp` scratch; `kotodama-shokunin` concurrent activity (attributed); `SCORECARD.md` baseline/HEAD distinction.

**Recommended (cosmetic, non-blocking):** r98 candidates — pin r97; repair the r95 map's carried "new relation" sentence; relocate self-test scratch or gitignore it; align `SELF-TEST-MISMATCH` exit-code wording between the two tools (carried); the pre-existing render-only colon position (V18).

**Same-lane rule respected:** no `[x]`, no promotion, no commits, no pushes. V12's and V46's FAILs stand recorded with their own reproductions; nothing harmed is smoothed away.

## 9. Bottom line

**ADMIT (conditional)** — on the delivered revision (`map_obligations.py 86b52949…` + contract `2142b991…`; `dependency_freeze.py b06275f3…` + contract `27273be2…`; r96 map `e851f068…`; r97 fixture 10 files; R6 note `5e3b4225…`; checker pin `ff9fd2aa…`) C1, C2 and C3 each verify first-hand: `dual_pointer` is persisted case 25 with a loader that fails closed on any dropped pinned case and a pin proven load-bearing (calibration, improved-bounded); the guarded `--freeze`/`PATH-MISMATCH`/file-naming `DIGEST-MISMATCH`/16-case self-test and the revision-only r96 refresh with chain 4/4 clean all reproduce (coverage, improved-bounded) — with **V12's FAIL recorded** (the r96 pin does not pin the post-repair map digest; the map is not a pinned file) and **V46's FAIL recorded** (the r97 tick-13 edge is not frozen because r97 is unpinned), both standing, both brief-stricter-than-declaration; the r97 fixture delivers the third beat (5/1/5→5/1/6, 5→6 sources, 16→17 obligations, 16 inherited rows unchanged, J17 load-bearing, CLEAN/17-17-19-19, census 170→171, unresolved preserved, repair byte-minimal with receipts unchanged) (depth, improved-bounded); operability improved-bounded (repo-root self-test scratch bound); freshness unchanged (one bounded README staleness, carried stale note pins); adjacency not harmed (charter byte-identical, change set exactly the declared ownership, no strays, no commits). 64/64 reports present and read; conflicts reconciled explicitly; admission subject to six exact closure conditions (C-1 re-freeze erratum, C-2 r97-unpinned bound, C-3 doc pass, C-4 D1/D6 bound, C-5 carried conditions, C-6 process/host items). No axis harmed; no scalar score assigned.
