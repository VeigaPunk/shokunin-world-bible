# V32 — verdict-operability (round 97, per-axis verdict)

**Seat:** V32 `verdict-operability`. Role: exactly one independent OPERABILITY verdict for the r97 delivered revision — new gate surfaces runnable, every documented command replays as written, 0/1/2 exit contract honored live, hardening proven on the delivered bytes — with bounds.
**Report path (only file written by this seat):** this file. No product file written, no commit, no push, no network, no nested agents.
**Baseline:** r96 closure `f3e09f9`; HEAD at report time → `2393934237ea076366f3db6dceeff033edb52ab1` (`2393934 lore r96: close round — SCORECARD admitted section`). `git status --porcelain` = 10 entries, all producer paths (` M LOG.md`, 5 modified tool/fixture files, `?? .ufo/waves/round-97/`, `?? corpus/fixtures/r97-crossing-acknowledgment/`, `?? corpus/knowledge/r97-acknowledgment-scope-note.md`).
**Scratch (declared):** `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-97/seats/V32-scratch/` only (copied tool trees, foreign-path copies, logs). Every write used an absolute path under `lore-shokunin/`; the poll and battery logs live there. No `/tmp` use for scratch.
**Poll-wait:** two background polls (20 s cadence, 40 tries). Artifacts landed 18:44–18:55; the last producer report (R3) landed inside the poll window (`REPORTS-READY`), all six producer reports present before any receipt below was taken. One mid-flight observation is disclosed, not smoothed: the r97 `dependency_freeze.py` moved `7428dad4… → 61cee7e5… → b06275f3…` while I read it, and the r96 map repair landed mid-round; every number quoted below is from the frozen revision in §0, re-hashed after all runs (`HASHES-STABLE`).

## 0. Frozen revision (sha256, re-verified after every run — identical)

```
86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9  corpus/tools/map_obligations.py                (R1)
2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41  corpus/tools/map-obligations-contract.json      (R2)
6278e59b8df01c1cb63ca6080cb959999f400d95128b96e84e5476f4c4ebb992  corpus/tools/README.md                          (R2)
b06275f3bbdeabaab615138b3004703fce701a786af882d3b732828b37722130  corpus/tools/dependency_freeze.py               (R3)
27273be27d33ad864f06d656f28dca8eabc9d76f6ebe62583372a88c9e64e781  corpus/tools/dependency-freeze-contract.json    (R3)
e851f068cfd7ed02c97054df18729c4c5a9b8bf60d99d7c9116f427d765440de  corpus/fixtures/r96-crossing-response/claim-excerpt-map.md   (R4 repair)
d9387b7d73264dfc6c01d27cc6bf24c58ef6bdb4461d2ae8fbfdb6376d9e019f  corpus/fixtures/r97-crossing-acknowledgment/README.md        (R5)
49d4834e124fa6cfaa1a73cd5d1a7bc2cb59711c6233b418fe7485a17eedc94f  corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md (R5)
438fb513a62496c41179ead3ea2a55a69ff4ce1fd191c3a7ebccb10651a8dc73  corpus/fixtures/r97-crossing-acknowledgment/sources.json
73063a863a68fc4feae073ce74cfa9e5fddb4f9cc4060d12b333d495a255895b  corpus/fixtures/r97-crossing-acknowledgment/timeline.json
5e3b4225c30de8a2a75b675b59acb5c597b290e5a45f2caa01663da586e042b5  corpus/knowledge/r97-acknowledgment-scope-note.md           (R6)
```

Python 3.14.7; all commands from the lane root unless stated. Transcripts under `V32-scratch/before/`, `V32-scratch/after/` (`battery-*.log`, `c1-*.log`, `exit-contract.log`, `frozen-hashes.txt`, `manifest-diff.txt`).

## 1. New gate surfaces runnable

**`map_obligations --self-test` — 25/25, exit 0, `dual_pointer` persisted:**

```
$ python3 corpus/tools/map_obligations.py --self-test
SELF-TEST CASES 25/25 pinned
… 25 × SELF-TEST PASS … including:
SELF-TEST PASS schema_drift exit=1 findings=['schema_drift']
SELF-TEST PASS inventory_mismatch exit=1 findings=['inventory_mismatch']
SELF-TEST PASS dual_pointer exit=1 findings=['dual_pointer']
RESULT PASS                                                                      exit=0
```

The delivered contract persists exactly 25 case records, including `{'id': 'dual_pointer', 'exit': 1, 'finding_ids': ['dual_pointer']}` (the r96 contract had 24 and no `dual_pointer`).

**`dependency_freeze --self-test` — 16/16, exit 0, both new classes persisted:**

```
$ python3 corpus/tools/dependency_freeze.py --self-test
CASE … clean / reduction_edge_drop / addition_edge_phantom / event_removed / event_endpoint_change /
     relation_endpoint_flip / relation_removed / relation_added / digest_tamper / malformed_json /
     missing_timeline / unpinned_fixture / missing_fixture / invalid_arguments / scope_refused / path_mismatch
CASE scope_refused: exit=2 expected=2 findings=['SCOPE-REFUSED'] ok
CASE path_mismatch: exit=2 expected=2 findings=['PATH-MISMATCH'] ok
SELF-TEST 16/16
RESULT PASS                                                                      exit=0
```

`corpus/tools/dependency-freeze-contract.json` carries 16 `self_test.expected` records and 4 pins (`r88-m3-maya-cluster`, `r94-paired-crossing`, `r95-crossing-aftermath`, `r96-crossing-response`).

## 2. Hardening proven on the delivered bytes (before/after, my own probes)

### C1(a)(b) — pin added and loader tightened (both measured against the r96 baseline)

Baseline (copied tree with the r96 tool `2b0ba815…` + r96 contract `97b76bb8…`), contract edited only in the copy:

```
drop schema_drift        -> SELF-TEST CASES 23/24 pinned / RESULT PASS   exit=0   (fail-open, the r96 defect)
drop inventory_mismatch  -> SELF-TEST CASES 23/24 pinned / RESULT PASS   exit=0   (fail-open)
drop phantom (core)      -> FINDING self_test_contract: contract drops implemented self-test cases: phantom / RESULT ERROR exit=2
```

Delivered revision (copied tree with `86b52949…` + `2142b991…`), each of the 25 pinned cases dropped in turn:

```
drop complete … drop dual_pointer (25 trials)
  -> FINDING self_test_contract: contract drops implemented self-test cases: <id> / RESULT ERROR   exit=2
drops that did NOT fail closed: 0
restored: SELF-TEST CASES 25/25 pinned / RESULT PASS   exit=0
```

Source: `missing = sorted(set(SELF_TEST_CASES) - set(expected))` (was `CORE_SELF_TEST_CASES`) — any missing pinned case fails before a case is exercised.

### C1(c) — the `dual_pointer` pin is load-bearing

Surgical emission neutralization in a tool copy (the emitted finding ID at the `gating.append(("dual_pointer", …))` site renamed; the case name and contract untouched):

```
SELF-TEST CASES 25/25 pinned
SELF-TEST FAIL dual_pointer exit=1 findings=['dual_pointer_emission_neutralized']
FINDING dual_pointer_emission_neutralized: row E1 (line 7) names a second pointer token 'entities[1].first_appearance' alongside entities.json#/0/first_appearance
RESULT FAIL
FINDING self_test_mismatch: isolated CLI outcomes differ from persisted expectations
RESULT ERROR                                                                      exit=2
```

A coarser neutralization (renaming all four `dual_pointer` literals) also fails closed: `FINDING self_test_contract: contract pins unimplemented self-test cases: dual_pointer` exit 2.

### C2(a) — `--freeze` scope guard, live

```
$ python3 corpus/tools/dependency_freeze.py --freeze .ufo/waves/round-97/seats/V32-scratch/foreign/r95-crossing-aftermath
FINDING SCOPE-REFUSED: --freeze refuses …/V32-scratch/foreign/r95-crossing-aftermath …; the frozen scope is corpus/fixtures/** (integration-time operation only)
RESULT ERROR                                                                      exit=2
contract before=27273be27d33ad864f06d656f28dca8eabc9d76f6ebe62583372a88c9e64e781
contract after =27273be27d33ad864f06d656f28dca8eabc9d76f6ebe62583372a88c9e64e781   CONTRACT-UNCHANGED
$ python3 corpus/tools/dependency_freeze.py --freeze corpus/fixtures
FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures itself; the frozen scope is corpus/fixtures/**   exit=2
```

Copied-tree allow/deny pair (ROOT = copy root): out-of-scope target → `SCOPE-REFUSED` exit 2; in-scope `corpus/fixtures/v32-in-scope` → `FROZEN v32-in-scope …` / `RESULT PASS` exit 0 with the copy's pin list gaining the entry. Baseline (r96 tool, copied tree): an out-of-corpus target froze cleanly and the copy's contract gained the pin — no guard.

### C2(b) — pin path binding, live

```
$ python3 corpus/tools/dependency_freeze.py .ufo/waves/round-97/seats/V32-scratch/foreign/r94-paired-crossing
FINDING PATH-MISMATCH: pin r94-paired-crossing names corpus/fixtures/r94-paired-crossing (resolves to …/corpus/fixtures/r94-paired-crossing); invoked fixture resolves to …/V32-scratch/foreign/r94-paired-crossing
RESULT ERROR                                                                      exit=2
```

Baseline on the same byte-identical foreign copy: `FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1 / DIGEST 2527beb9… / RESULT PASS` exit 0 — exactly the r96 defect the claim names.

### C2(c) — `DIGEST-MISMATCH` names the changed file

```
$ python3 …/dependency_freeze.py <copytree>/corpus/fixtures/r95-crossing-aftermath     # timeline.json gained a trailing newline
FINDING DIGEST-MISMATCH: content digest c7c29b5e… != pin d541ae64…; changed: timeline.json (sha256 3c0faad6bf32f944f9f2a20f3bd15829044afa04f1a8837601903433b00ea177 -> bd64e666f77d6981d2871fdab750d5622942c7c18ceca8cfdd8bc82fa6aa6ff2); fixture bytes changed outside the frozen inventory
RESULT ERROR                                                                      exit=2
```

Baseline wording ended at `…outside the frozen inventory` with no file named.

### C2(d) — self-test 14→16 and drop-protection of the expectation set

Delivered `--self-test` is 16/16 (§1). Dropping any expectation (`scope_refused`, `path_mismatch`, `clean`) or adding a bogus one fails closed in a copied tree: `FINDING CONTRACT-INVALID: self-test expectation set mismatch; missing=['scope_refused'] extra=[]` exit 2 (exact-set loader, unchanged from r96).

### C2 pin refresh through the guarded path (r96 re-freeze after the repair)

`pins.r96-crossing-response`: `fixture = corpus/fixtures/r96-crossing-response`, `revision = 2393934237ea…` (current HEAD, i.e. after R4's repair), `content_sha256 = d422a9b3d95c4e0b8aac98cc87806a94949896adb962a50d2d55a6c11657d7f6` — equal to the digest the delivered tool prints for that fixture (`DIGEST d422a9b3… / RESULT PASS` exit 0), consistent with the map not being a pinned data file. The other three pins still carry `60dba0c2aa34` (r95 closure), so the refresh touched exactly the repaired fixture. I did **not** re-run live `--freeze` (it writes the delivered contract); the end-to-end refresh is evidenced by the pin's revision/digest plus the copied-tree allow/deny pair above.

## 3. Documented commands replay as written

**(a) r97 fixture README replay block (`corpus/fixtures/r97-crossing-acknowledgment/README.md:23-29`), run exactly as written:**

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r97-crossing-acknowledgment
CLEAN: schema, citations, relations, timeline; 0 violations                        exit=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r97-crossing-acknowledgment
INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19; DISTINCT-ANCHORS 15/15
RECEIPT JSON-FACTS 17; EDITORIAL-ROWS 2; TOTAL-ROWS 19
SOURCE-SUPPORT 17/17; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 19/19; VALIDATED-ROWS 19/19
RESULT PASS                                                                        exit=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r97-crossing-acknowledgment
OBLIGATIONS raw=17 mapped=17
INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19
RESULT PASS                                                                        exit=0
```

Every declared count reproduces: README:21 "17 source-attributed JSON pointer obligations" → `raw=17 mapped=17`; map:5 `**Expected inventory:** 17 JSON facts; 2 editorial rows; 19 total mapped rows; 15 distinct excerpt anchors` → the tool's `17/17; 2/2; 19/19` and `DISTINCT-ANCHORS 15/15`; README:3 "5 entities / 1 relation / 6 events / 6 sources" → `json.load` counts `5 1 6 6 0`; the new tick-13 event reads `{'id': 'acknowledgment-aru-records', 'tick': 13, 'entity_id': 'aru', 'place_id': 'chalk-stair', 'depends_on': ['response-evin-salt-court'], …}`; J17 is the only new map row (map:38).

**(b) r96 fixture (post-repair) receipts — unchanged by the repair.** `git diff HEAD` for `r96-crossing-response/claim-excerpt-map.md` is exactly 2 lines (editorial delimiter 8→7 cells at :44; the stale "The new relation encodes…" sentence at :50 rewritten to name the tick-12 event). `check_bible` CLEAN exit 0; `support_check` `JSON-FACTS 16/16; TOTAL-ROWS 18/18` PASS exit 0; `map_obligations` `raw=16 mapped=16` PASS exit 0 — identical to the same receipts run on a `git show HEAD:` extraction of the pre-repair fixture, so the repair moved no receipt.

**(c) R6 note receipts (`corpus/knowledge/r97-acknowledgment-scope-note.md`, "Receipts" block)** were taken at mid-flight tool revisions (`map_obligations.py 70795150…` / contract `97b76bb8…`) and the note itself says to re-run before citing. Re-run at the delivered revision: the three commands above, with identical numbers (`17/17`, `19/19`, `raw=17 mapped=17`).

**(d) tools README r97 addendum** — its one runnable command (`map_obligations.py --self-test`) replays (`SELF-TEST CASES 25/25 pinned` / `RESULT PASS` exit 0); its quoted drop-probe and neutralization outputs match my independent probes (§2, different probe points, same verdict).

**(e) Retained documented commands**: r93 addendum `boundary_doc_check.py` default and its `mktemp` negative control both replay as written now (`FINDING document_drift: document digest differs from pinned 65838f86… bytes` / `CERTIFICATION FAIL` exit 1, script assertion satisfied) — see D7. `map_obligations` r88/r93/r94/r95 paths and the `--frozen` r93 replay all replay (`raw=10/12/14/15`, frozen `SNAPSHOT inputs=4 digests=verified` / `FROZEN expected=PASS/0 findings=none matched`, exit 0).

**(f) Context independence**: both tools run from a foreign cwd with absolute paths (`cd /home/vgpnk` → map r97 `raw=17 mapped=17` PASS exit 0; dep r96 `events 5/5; dependency-edges 4/4; relations 1/1` PASS exit 0).

## 4. Exit contract 0/1/2 honored live (23 invocations, 0 mismatches)

| Path | exit | terminal RESULT lines | stderr | traceback |
|---|---|---|---|---|
| map r97 / r96 / `--self-test` / `--frozen` r93 | 0 | 1 | 0 | no |
| map r87 / r89 fail-closed, no-arg, misuse, missing cluster | 2 | 1 | 0 | no |
| map `--help` | 0 | **0** | 0 | no |
| dep r96 verify, `--self-test` | 0 | 1 | 0 | no |
| dep r87 / r97 unpinned, foreign path `PATH-MISMATCH`, `--freeze` refusals, no-arg, misuse, missing fixture | 2 | 1 | 0 | no |
| dep `--help` | 0 | **0** | 0 | no |
| check_bible r97 / support_check r97 | 0 | — / 1 | 0 | no |

Stable finding IDs observed exactly as documented: `inventory_mismatch`, `dual_pointer`, `missing_obligation`, `duplicate_mapping`, `phantom_obligation`, `source_id_mismatch`, `malformed_json`, `map_missing`, `unsupported_map`, `invalid_arguments`, `unsafe_path`, `foreign_path`, `snapshot_tampered`, `unpinned`, `frozen_verdict_mismatch`, `self_test_contract`, `self_test_mismatch`; dep: `REDUCTION-DETECTED`, `ADDITION-DETECTED`, `ENDPOINT-CHANGE`, `DIGEST-MISMATCH`, `FILE-MISSING`, `MALFORMED-JSON`, `UNPINNED-FIXTURE`, `FIXTURE-MISSING`, `INVALID-ARGUMENTS`, `SCOPE-REFUSED`, `PATH-MISMATCH`, `CONTRACT-INVALID`. `--help` exiting 0 with zero RESULT lines remains the documented caveat (exit 0 alone is not a PASS).

## 5. No live-tree writes; hygiene; census

```
$ find corpus -type f ! -path "*__pycache__*" | LC_ALL=C sort | xargs sha256sum > pre.digests   # 1815 files
$ map --self-test; dep --self-test; dep verify r96; support_check r97; check_bible r97
$ … > post.digests; diff pre.digests post.digests
NO-WRITES-IN-WINDOW
```

All frozen hashes re-checked after the battery: `HASHES-STABLE`. Live-tree mutations for the probes were made only on copies under my scratch tree (foreign-path copies, copied tool/contract trees); the live `--freeze` refusal left the delivered contract byte-identical (§2).

**Independent census replay** (my own loop over `corpus/fixtures/*/`, `check_bible.py`): `dirs=171 clean=37 negative=134 other_exits=0 violation_prefix_lines=421` — the declared 170→171 with one new clean fixture and zero non-0/1 exits.

## 6. Defects, gaps and bounds (reported exactly, none waived)

**D1 (MEDIUM, delivered behavior — new this round) — the `dependency_freeze` self-test scratch moved under the repository root, spreading BR-05 to the second tool.** r96 tool (`git show HEAD:corpus/tools/dependency_freeze.py:411`): `tempfile.TemporaryDirectory(prefix="dependency-freeze-self-test-")` — system temp, no repo residue (r96 V35 recorded this as the r96 improvement). Delivered (`dependency_freeze.py:517`): `tempfile.TemporaryDirectory(prefix="dependency-freeze-self-test-", dir=ROOT)`. Witnessed live: `dependency-freeze-self-test-ceek7qgp` appeared in the repo root during `--self-test` and was gone after; `map-obligations-self-test-118euut9` likewise. `.gitignore` has no `self-test` entry, so concurrent seats see both as transient `??` entries. R3 §4 justifies it by this host's `/tmp` inode exhaustion, but that condition no longer holds (`df -i /tmp` → `1048576 15694 1032882 2%`) and Python's `tempfile` fallback to `/var/tmp` worked at r96, so the r97 change is a regression on the operability axis rather than a required workaround.

**D2 (MEDIUM, documentation gap) — the r97 `dependency_freeze` hardening is undocumented in the delivered docs, and the r96 paragraph now misdescribes the tool.** `corpus/tools/README.md:175` (R2-owned, final revision `6278e59b…`) still says self-test "14/14" and lists all three r96 hazards as open ("`--freeze <dir>` … has no `corpus/fixtures/` scope guard — integration-time only; receipts are not path-bound …; `DIGEST-MISMATCH` does not name the changed file") — every one of them is closed on the delivered revision, and `SCOPE-REFUSED`, `PATH-MISMATCH`, the changed-file digest wording, the same-named-shadow refusal and the 16-case self-test appear nowhere in the README (`grep -c "SCOPE-REFUSED" corpus/tools/README.md` → 0). The r97 addendum covers `map_obligations` only. R3 §1 raises the same gap; byte-ownership is R2's.

**D3 (LOW, stale prose outside producer write scope) — `SKILL.md`'s gate registry is stale.** `SKILL.md:87` still reads "24 cases (r96 added `schema_drift`, `inventory_mismatch`)" and carries both r96 notes ("`dual_pointer` behavior is demonstrated by mutation demos, not pinned by a persisted case; the two r96-added pins are droppable under the subset-tolerant loader (23/24 still passes) — both r97 debt") — all three statements are false on the delivered revision. `SKILL.md:98` says the dep self-test is "14 cases" and its entry line does not mention the scope guard or path binding. Closure items.

**D4 (LOW, closure item) — `corpus/fixtures/README.md` has no Round-97 section.** Its last census line is the r96 one (`170 fixture directories: 36 clean …`), measured state is `171/37/134/421`, and `:1213` still lists the two r96 cosmetic debts as "r97 candidates" although both are repaired this round.

**D5 (LOW, design bound by declaration) — the r97 fixture is not pinned in the dependency chain.** The chain stays the four declared fixtures (4/4 PASS exit 0); `dependency_freeze.py corpus/fixtures/r97-crossing-acknowledgment` → `FINDING UNPINNED-FIXTURE … (pinned: ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response'])` exit 2. The round's one new `depends_on` edge is therefore not frozen; R3 §2 records it as an r98 candidate.

**D6 (LOW, carried and disclosed) — BR-05 remains open for `map_obligations` and now also covers `dependency_freeze`** (D1). Both self-tests create repo-root scratch transiently and neither is gitignored; the tools README r97 addendum discloses the map residual as unchanged history but does not disclose the new dep one.

**D7 (RESOLVED, recorded for accuracy) — the r96 environment defect cleared.** `/tmp` is no longer inode-exhausted (`1048576 15694 1032882 2%`), so the tools README r93 addendum's `mktemp` negative control now replays as written and produces the documented `FINDING document_drift … 65838f86…` exit 1 instead of the r96 wrong-reason pass (`document_unreadable`). No documented command failed as written this round.

**Bounds:** exit 0 from either gate means mapping completeness / frozen-inventory agreement only — not entailment, fidelity, chronology truth, source authenticity, rights, permission, or canon. `--help` exit 0 with no RESULT line is a documented non-PASS. D1 bounds how clean the self-test surface is (transient repo-root scratch on both tools); D5 bounds what the frozen chain covers (the r97 fixture's new edge is unfrozen). This verdict covers operability of the delivered artifacts only; it is not an admission, a capability row, or a whole-round verdict.

## 7. OPERABILITY VERDICT — **improved (bounded)**

On the frozen revision the round's operability surface grew in four runnable, measured ways and no operability property was harmed:

- **Runnable new surfaces:** `map_obligations --self-test` is 25/25 exit 0 with `dual_pointer` persisted in the contract and proven load-bearing; `dependency_freeze --self-test` is 16/16 exit 0 with `scope_refused` and `path_mismatch` persisted.
- **Hardening proven live, not just declared:** the loader fails closed on a dropped pinned case in 25/25 trials (baseline fail-open at 23/24); a same-named foreign copy goes from `RESULT PASS` exit 0 to `PATH-MISMATCH` exit 2; `--freeze` refuses out-of-scope targets with the delivered contract byte-unchanged (baseline wrote freely); `DIGEST-MISMATCH` names the changed file with both digests; the r96 pin was refreshed through the guarded path (revision `2393934237ea…`, digest unchanged).
- **Documented commands replay:** every command in the r97 fixture README, the r96 fixture README (post-repair), the tools README r97 addendum, the R6 note (re-run at the delivered revision as the note requests), and the retained r93/r94/r95 commands replays as written with the recorded text and exit; both tools also run from a foreign cwd.
- **Exit contract honored:** 0/1/2 with one terminal RESULT line, stable FINDING IDs, empty stderr and no traceback across 23 probed invocations; census 171/37/134/421; corpus manifest byte-identical around the whole battery; the r96 environment defect (D7) has cleared.

**Bounds (all disclosed, none waived):** D1 — the dep self-test now creates transient repo-root scratch (BR-05 spread; regression vs r96, no longer justified by the host's `/tmp` state); D2 — the r97 dep hardening is undocumented and the r96 README paragraph still lists the closed hazards as open; D3 — the `SKILL.md` registry rows are stale for both tools; D4 — `corpus/fixtures/README.md` is not re-declared for r97; D5 — the r97 fixture is unpinned, so its new edge is not frozen; D6 — BR-05 open for both tools. D1 is a delivered-behavior bound; D2–D4 are documentation/closure items outside the producers' byte-ownership; D5 is a declared-scope bound.

## Bottom line

**PASS / operability improved (bounded)** — on the frozen r97 revision (map tool `86b52949…`, map contract `2142b991…`, dep tool `b06275f3…`, dep contract `27273be2…`, r96 map repair `e851f068…`, r97 fixture `README d9387b7d…`/`map 49d4834e…`/`timeline 73063a86…`/`sources 438fb513…`, note `5e3b4225…`) the map self-test is 25/25 exit 0 with a persisted, load-bearing `dual_pointer` pin and a loader that fails closed on any dropped pinned case (25/25 trials; baseline 23/24 pass), the dep self-test is 16/16 with live `SCOPE-REFUSED` (contract byte-unchanged on refusal), `PATH-MISMATCH` on a same-named foreign copy (baseline PASS exit 0), file-naming `DIGEST-MISMATCH`, and a guarded-path r96 pin refresh; the r97 fixture replays 17/17 (`check_bible` CLEAN, `support_check` 17/17, `map_obligations raw=17 mapped=17`), the r96 receipts are unchanged by the 2-line cosmetic repair, every documented command replays as written, the 0/1/2 contract holds with one terminal RESULT line and empty stderr on 23 invocations, census is 171/37/134/421, and the corpus manifest is byte-identical around the runs; the verdict is bounded by the new repo-root self-test scratch on both tools (D1/D6), the undocumented r97 dep hardening plus the stale r96 README paragraph (D2), the stale `SKILL.md` registry rows (D3), the un-re-declared fixtures census (D4), and the unpinned r97 fixture (D5).
