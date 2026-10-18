# V35 — verdict-operability (round 96, per-axis verdict)

**Seat:** V35 `verdict-operability`. Role: exactly one independent OPERABILITY verdict for the r96 delivered revision — new gate surfaces runnable, every documented command replays as written, 0/1/2 exit contract honored live — with bounds.
**Report path (only file written by this seat):** this file. No product file written, no commit, no push, no network, no nested agents.
**Baseline:** r95 closure `dcb2d92`; `git rev-parse HEAD` at report time → `60dba0c2aa344860b10a2fc63e00468d1b134f27` (r95 SCORECARD close commit; only ` M LOG.md` on top).
**Seats read as instructed:** `V19-c3-selftest.md` (landed at poll t=540), `V02-c1-selftest.md` (poll 2 t=240) and `V30-operability.md` (poll 2 t=300) — all three read in full, all bottom-line PASS. Every operative point below is independently reproduced by me, including the residuals V02 and V30 raise, which I re-derived myself rather than carrying over.
**Scratch (declared):** `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-96/seats/V35-scratch/` only (mutation copies, baseline tool extract, battery logs). No repo scratch dir, no `/tmp` use (the host's `/tmp` tmpfs was full — `mkdir /tmp/v35-r96` → `No space left on device`; all scratch moved under the lane). Nothing outside this report path and that scratch dir was written in the repo.

## 0. Frozen revision (hash-pinned; re-verified before and after every run below)

```
2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8  corpus/tools/map_obligations.py            (Q1)
97b76bb8b1fea97f166ef7586eba69c427ec15bbe7b34eb5345ec65c936493b6  corpus/tools/map-obligations-contract.json (Q2)
965b29cd41a8af14293eb2e1948f58f310e58c6e752b8fe322c5445b20a91f24  corpus/tools/README.md                     (Q2)
a3b57978f0cbf314389ee3f9862920a46cf109fca6d1eec488c39be0457f0980  corpus/tools/dependency_freeze.py          (Q3)
7d568cc422cda42297b7506a1a3e083e8798866efd16d58617bf4ea468576975  corpus/tools/dependency-freeze-contract.json (Q3)
ff52ced48bf4214721f248328d76da64a42773d44e78154ef1eaf6eb3558c456  corpus/fixtures/r96-crossing-response/README.md
5093d72eb3f22b249033d7ac4c1a85c7df7f5e09bfa673a598aee6a83045bfd8  corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
6db32ca24f5eff5baa3ebe589e8d3bcb6b256fec18dee2468211d7d0fae157c6  corpus/knowledge/r96-response-scope-note.md
```

Fixture data bytes (Q4): `entities.json 026af0bc…`, `relations.json c279254b…`, `sources.json 9f973f63…`, `timeline.json ea0225f9…`, `contradictions.json 37517e5f…`. Tool/contract hashes match Q1 §, Q2 §, Q3 § declared revisions; every hash was re-checked after the last run and is unchanged. Python 3.14.7; all commands from the repo root unless stated.

**Mid-flight states were not verified and are not evidence of the delivered revision** (disclosed, not smoothed): at 17:43 the in-flight `dependency_freeze.py` (`d17297bb…`) printed `SELF-TEST 5/14` / `RESULT FAIL` exit 1 with nine cases resolving to one `missing_timeline` scratch path — I observed this live before Q3's report landed (independently corroborating V19 §2's R1 receipt); the repair revision `a3b57978…` is 14/14 exit 0 and is what every receipt below uses. The r95 revision `d1c239cc…` was extracted from Git (`git show dcb2d92:… > …/map_obligations.r95.py`) for the "before" halves.

## 1. New gate surfaces runnable

**`map_obligations --self-test` — 24/24, exit 0, including the two new persisted cases:**

```
$ python3 corpus/tools/map_obligations.py --self-test
SELF-TEST CASES 24/24 pinned
... 24 × SELF-TEST PASS ...
SELF-TEST PASS schema_drift exit=1 findings=['schema_drift']
SELF-TEST PASS inventory_mismatch exit=1 findings=['inventory_mismatch']
RESULT PASS
exit=0
```

`corpus/tools/map-obligations-contract.json` persists exactly 24 case records (`self_test.cases`), including `{'id': 'schema_drift', 'exit': 1, 'finding_ids': ['schema_drift']}` and `{'id': 'inventory_mismatch', 'exit': 1, 'finding_ids': ['inventory_mismatch']}` — the r95 `schema_drift` gap is closed, not merely demonstrated (the r95 contract had no such case; `grep -c schema_drift` was 0 per the r95 record).

**`dependency_freeze` — self-test 14/14 exit 0; chain verifies 4/4 clean:**

```
$ python3 corpus/tools/dependency_freeze.py --self-test
CASE clean: exit=0 expected=0 findings=[] ok
CASE reduction_edge_drop: exit=1 expected=1 findings=['REDUCTION-DETECTED'] ok
... 14 cases ...
SELF-TEST 14/14
RESULT PASS   exit=0

$ for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response; do
    python3 corpus/tools/dependency_freeze.py corpus/fixtures/$f; done
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0    RESULT PASS exit=0
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1    RESULT PASS exit=0
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1 RESULT PASS exit=0
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1  RESULT PASS exit=0
```

**The BR-01 blind spot is closed live** (scratch copies under my scratch dir; the live fixtures were never mutated): dropping `evin-ninth-bell` from the r95 tick-10 `depends_on` gives `dependency-edges 2/3` / `FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']` / `RESULT FAIL`, exit 1; adding a phantom edge gives `ADDITION-DETECTED` exit 1. The same reduction on the *r95-era* tooling chain left every gate green (Q3 §, V17/V18/V22 — not re-run by me beyond the delivered tool's behavior).

## 2. Documented commands — every r96 command replays as written (one inherited command does not, for an environmental reason)

**(a) r96 fixture README replay block (`corpus/fixtures/r96-crossing-response/README.md`, run exactly as written):**

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response
CLEAN: schema, citations, relations, timeline; 0 violations                      exit=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18; DISTINCT-ANCHORS 14/14
RECEIPT JSON-FACTS 16; EDITORIAL-ROWS 2; TOTAL-ROWS 18
SOURCE-SUPPORT 16/16; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 18/18; VALIDATED-ROWS 18/18
RESULT PASS                                                                       exit=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response
OBLIGATIONS raw=16 mapped=16
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18
RESULT PASS                                                                       exit=0
```

All documented counts reproduce: README "16 source-attributed JSON pointer obligations" → `raw=16 mapped=16`; map declaration `16 JSON facts; 2 editorial rows; 18 total mapped rows; 14 distinct excerpt anchors` → the tool's `16/16; 2/2; 18/18` and support_check's `DISTINCT-ANCHORS 14/14`; README "5 entities / 1 relation / 5 events / 5 sources" → `json.load` counts 5/1/5/5/0.

**(b) Q6's note receipts (`corpus/knowledge/r96-response-scope-note.md:46-52`)** — the note discloses that its receipts ran at the r95/in-flight tool revision and asks for a re-run "before citing"; I re-ran all three on the delivered revision: `check_bible` CLEAN exit 0, `support_check` `SOURCE-SUPPORT 16/16; MODES 18/18; VALIDATED-ROWS 18/18` / `RESULT PASS` exit 0, `map_obligations` `raw=16 mapped=16` / `RESULT PASS` exit 0 — identical to the note's quoted results. The note's own numbers (census 170, `timeline.json[:4] == r95` inheritance) are separately confirmed by my census (§4).

**(c) Tools README Round-96 addendum (`corpus/tools/README.md:121-169`)** — the one runnable command line replays (`SELF-TEST CASES 24/24 pinned` / `RESULT PASS` exit 0), and both documented before/after demos reproduce byte-for-byte on scratch copies:

- deletion class, addendum's exact recipe (r94 copy, entity 0 `claims` deleted + its `entities.json#/0/claims/0` row removed): r95 tool → `OBLIGATIONS raw=13 mapped=13` / `INVENTORY JSON-FACTS 13/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 15/16 MISMATCH` / `RESULT PASS` exit 0; delivered tool → same receipt lines plus `FINDING inventory_mismatch: declared JSON-facts/editorial-rows/total-rows 14/2/16; observed 13/2/15` / `RESULT FAIL` exit 1.
- `dual_pointer`, addendum's exact recipe (r88 copy, row P1 cell → `` `entities[0].first_appearance` (Aru; also `entities[0].claims[0]`) ``): r95 tool → `RESULT PASS` exit 0; delivered tool → `FINDING dual_pointer: row P1 (line 23) names a second pointer token 'entities[0].claims[0]' alongside entities.json#/0/first_appearance` / `RESULT FAIL` exit 1 — the row ID, line number, token and pointer text all match the addendum.

**(d) LOG declaration commands** — `python3 corpus/tools/dependency_freeze.py <dir>` verify, `--self-test`, and the 0/1/2 contract all replay as declared (§1, §3). `--freeze` was deliberately **not** run against the live tool: it writes the delivered contract (see §5 D1/D5); I exercised it in a copied tree instead.

**(e) Context independence** — both tools run from a non-repo cwd with absolute paths: `cd /home/vgpnk && python3 …/map_obligations.py …/r96-crossing-response` → `raw=16 mapped=16` / `RESULT PASS` exit 0; `…/dependency_freeze.py …` → `events 5/5; dependency-edges 4/4; relations 1/1` / `RESULT PASS` exit 0.

**(f) One documented command does NOT replay as written on this host — environment-induced (reported exactly; see D9).** The tools README r93 addendum's `mktemp`-based negative control, run verbatim, exits 1 for the wrong reason because `/tmp` is inode-exhausted (`df -i /tmp` → `1048576 1048576 0 100%`):

```
$ tmp="$(mktemp)"; trap 'rm -f "$tmp"' EXIT; cp corpus/knowledge/holder-assessment-boundary.md "$tmp"; printf '\nDeliberate R05 pin-drift probe.\n' >> "$tmp"; python3 corpus/tools/boundary_doc_check.py --doc "$tmp"; rc=$?; printf 'observed_exit=%s\n' "$rc"; test "$rc" -eq 1
mktemp: failed to create file via template '/tmp/tmp.XXXXXXXXXX': No space left on device
cp: cannot create regular file '': No such file or directory
CHECK pinned inputs: FAIL
FINDING document_unreadable: cannot read document /home/vgpnk/Projects/shokunin/lore-shokunin: [Errno 21] Is a directory
CERTIFICATION FAIL
observed_exit=1          # the script's own `test "$rc" -eq 1` passes — wrong-reason pass
```

The documented `FINDING document_drift` does not appear. Control with a scratch path substituted for `mktemp` (`--doc .ufo/waves/round-96/seats/V35-scratch/drift-probe.md`) prints `FINDING document_drift: document digest differs from pinned 65838f86… bytes` / `CERTIFICATION FAIL` exit 1 — so the checker behavior is correct; the environment breaks the documented command. Independently reproduced from V30 §6.

## 3. Exit contract 0/1/2 honored live (30 invocations)

| Path | exit | terminal RESULT line | FINDING lines | stderr bytes | traceback |
|---|---|---|---|---|---|
| r96 / r95 / r94 / r93 / r88 default | 0 | 1 | 0 | 0 | 0 |
| `--self-test` (map) / `--self-test` (dep) / `--frozen` r93 replay | 0 | 1 | 0 | 0 | 0 |
| `--help` (map) / `--help` (dep) | 0 | **0** | 0 | 0 | 0 |
| r87 / r89 fail-closed | 2 | 1 | 1 | 0 | 0 |
| no-arg (map) / no-arg (dep) | 2 | 1 | 1 | 0 | 0 |
| live fail: deletion class / dual pointer / missing row / duplicate row / source-ID mismatch | 1 | 1 | 1–2 | 0 | 0 |
| live err: malformed JSON / map missing / dep malformed JSON / dep unpinned fixture | 2 | 1 | 1 | 0 | 0 |
| dep fail: BR-01 reduction / added edge | 1 | 1 | 1 | 0 | 0 |
| misuse: `--self-test`+cluster, `--frozen`+cluster (map), `--self-test`+fixture (dep) | 2 | 1 | 1 | 0 | 0 |

Live exit-1/exit-2 cases ran on scratch copies under my scratch dir; live fixtures untouched. Stable finding IDs observed exactly as documented: `inventory_mismatch`, `dual_pointer`, `missing_obligation`, `duplicate_mapping`, `source_id_mismatch`, `malformed_json`, `map_missing`, `unsupported_map`, `invalid_arguments`, `REDUCTION-DETECTED`, `ADDITION-DETECTED`, `MALFORMED-JSON`, `UNPINNED-FIXTURE`. `--help` exiting 0 with zero RESULT lines is the documented BR-06 caveat (exit 0 alone is not a PASS); both tools print exactly one terminal `RESULT` line on every operational path, with empty stderr and no traceback everywhere.

## 4. No live-tree writes; hygiene

```
$ find corpus -type f ! -path "*__pycache__*" | LC_ALL=C sort | xargs sha256sum > pre.digests
$ python3 corpus/tools/map_obligations.py --self-test && python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response
$ python3 corpus/tools/dependency_freeze.py --self-test && 4 × verify
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response && python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response
$ find corpus -type f ! -path "*__pycache__*" | LC_ALL=C sort | xargs sha256sum > post.digests
$ diff pre.digests post.digests → NO-WRITES-IN-WINDOW
```

`git status --porcelain` after the whole battery lists only producer paths (` M LOG.md`, ` M corpus/tools/{README.md,map-obligations-contract.json,map_obligations.py}`, `?? corpus/tools/{dependency_freeze.py,dependency-freeze-contract.json}`, `?? corpus/fixtures/r96-crossing-response/`, `?? corpus/knowledge/r96-response-scope-note.md`, `?? .ufo/waves/round-96/`) — nothing from tool runs.

**Independent census replay** (my own loop over `corpus/fixtures/*/`, `check_bible.py`), run twice bracketing the producers' final landings: `dirs=170 clean=36 negative=134 violation_prefix_lines=421` both times (`CENSUS-IDENTICAL-TO-EARLIER`), matching the declared 169→170 with one new clean fixture and zero changed inherited tuples. Zero non-0/1 exits.

**BR-05 witnessed live (unchanged in r96):** during the battery, `git status` showed `?? map-obligations-self-test-3et3_5ug/` and `?? map-obligations-self-test-80qlg6l8/` (concurrent self-test runs), and a re-check 25 s later found the directory set changed and then empty (`GONE`). The r96 addendum discloses this residual explicitly. The new `dependency_freeze --self-test` does **not** share this defect: its scratch is `tempfile.TemporaryDirectory(prefix="dependency-freeze-self-test-")` under `/var/tmp`, and no repo-root residue was observed from it.

## 5. Defects, gaps and bounds (reported exactly, none waived)

**D1 (MEDIUM, delivered artifact) — the delivered `dependency-freeze-contract.json` carries a foreign pin.** `pins` = `['c3red', 'r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response']`, where `c3red.fixture = ".ufo/waves/round-96/seats/V41-scratch/c3red"` with `content_sha256 eff4b354…` — a verifier's scratch copy of the BR-01 *reduction* mutation, i.e. a mutated fixture frozen into the delivered contract. Provenance is unambiguous in V41's own log (`c3-freeze.out`: `FROZEN c3red … DIGEST eff4b354…`; `c3-interim.log:34` shows the pin list before it existed). The gate's own output exposes it: `UNPINNED-FIXTURE … (pinned: ['c3red', …])`. Impact: inert for the four chain fixtures and the self-test (pins are basename-keyed; no corpus fixture is named `c3red`) — but the delivered contract is no longer self-contained and contradicts the declared four-fixture shape. Q3 §7 and V19 §6 F1 report it and deliberately left it in place (V22/V33 receipts quote the pin list); closure/r97 must delete it or guard `--freeze`.

**D2 (MEDIUM, documentation gap) — the new gate is undocumented in the delivered docs.** `grep -c dependency corpus/tools/README.md` → **0**; `dependency_freeze`/`dependency-freeze` appear outside `.ufo/` only in `LOG.md` (the round declaration) and the contract itself — not in the tools README r96 addendum, not in the r96 fixture README, not in `corpus/fixtures/README.md`, not in `SKILL.md`'s gate registry. A runnable gate with persisted expectations has no documented entry command/verdict map outside a seat report, which is exactly the operability surface this axis judges.

**D3 (LOW, stale prose outside producer write scope) — `SKILL.md` gate registry is stale.** The `map_obligations` row still says "22 cases (r95 added `map_missing`, `invalid_arguments`)" and carries the note "`schema_drift` behavior is demonstrated by mutation demos, not pinned by a persisted self-test case (r95 debt)" — both false on the delivered revision (24 cases; `schema_drift` pinned). There is no `dependency_freeze` row. Closure items.

**D4 (LOW, carried and disclosed) — BR-05 still open:** `map_obligations --self-test` scratch lives under the repo root and is not gitignored (witnessed §4); concurrent seats make it visible in `git status` transiently. Explicitly disclosed in the r96 addendum as unchanged.

**D5 (MEDIUM mechanism, same hole as D1) — `--freeze` writes the delivered contract unconditionally.** `ROOT = Path(__file__).resolve().parents[2]`, `CONTRACT_PATH = ROOT/"corpus/tools/dependency-freeze-contract.json"`, and `freeze()` writes it with no scope guard. Reproduced safely: with tool+contract copied into my scratch tree and a probe fixture added, `--freeze` wrote the **copy** (pins gained `v35-probe-fixture`) while the live contract stayed byte-identical — the write target is `__file__`-relative, so any seat running the *live* tool with a scratch target rewrites the delivered contract, which is how D1 landed. Nothing detects a foreign pin: V19's P6 added a bogus pin and the self-test still printed 14/14 PASS.

**D6 (LOW, closure item) — `corpus/fixtures/README.md` census re-declaration is still the r95 one** (`169 fixture directories: 35 clean …`), with no Round-96 section, while the measured state is 170/36/134/421 (§4).

**D7 (MEDIUM, delivered behavior bound) — the two added self-test cases are pinned but not drop-protected.** Independently reproduced (tool+contract copied into my scratch tree, contract mutated only in the copy, live contract byte-unchanged):

```
drop `inventory_mismatch` (24 → 23 cases): SELF-TEST CASES 23/24 pinned / RESULT PASS / exit=0   <- fail-open
drop `schema_drift`       (24 → 23 cases): SELF-TEST CASES 23/24 pinned / RESULT PASS / exit=0   <- fail-open
drop a core case `phantom` (24 → 23)     : FINDING self_test_contract: contract drops implemented self-test cases: phantom / RESULT ERROR / exit=2
```

The loader fails closed on unknown ids, duplicate ids, malformed expectations and drops of any of the 22 core cases, but treats `ADDED_SELF_TEST_CASES` as optional — so a future contract edit (or a revert of those two entries) that removes `schema_drift`/`inventory_mismatch` leaves `--self-test` green with only the non-gating `23/24 pinned` receipt. Q1/README disclose subset tolerance by design; the consequence is that the r96 C1(b) pinning guarantee is weaker for exactly the two behaviors the round adds. Same finding as V02 §5 C/C3 and §8.1, re-derived here.

**D8 (LOW, coverage asymmetry) — `dual_pointer` (C1(c)) is pinned by no persisted self-test case.** `any('dual_pointer' in c['finding_ids'] …)` over the 24 contract cases → `False` (`schema_drift` and `inventory_mismatch` → `True`). The new dual-pointer gate's behavior therefore rests on mutation demonstrations and verifier replays (mine included: exit 1 with the stable id), not on a persisted expectation. Same finding as V02 §6/§8.2.

**D9 (LOW, environment-induced, reported not papered over) — one documented command wrong-reason-passes on this host.** `/tmp` is a 16 G tmpfs with all 1 048 576 inodes used (`df -i /tmp` → `1048576 1048576 0 100%`), so `mktemp` fails and the tools README r93 addendum's negative control exits 1 via `FINDING document_unreadable` on the repo directory instead of the documented `FINDING document_drift` — while the script's own `test "$rc" -eq 1` assertion still passes. Reproduced verbatim in §2(f); control with a scratch path gives the documented finding and exit 1. This is the one documented command in the delivered docs that does not replay as written here; the checker itself is correct. Independently reproduced from V30 §6.

**Bounds:** exit 0 from either gate means mapping completeness / frozen-inventory agreement only — not entailment, fidelity, chronology truth, source authenticity, rights, permission, or canon. `--help` exit 0 with no RESULT line remains a documented non-PASS. D7 bounds how much of C1(b)'s pinning guarantee survives a future contract edit; it does not change any delivered verdict (24/24 passes today). D9 is an environment defect on the host, not a delivered-artifact defect. This verdict covers operability of the delivered artifacts only; it is not an admission, a capability row, or a whole-round verdict.

## 6. OPERABILITY VERDICT — **improved (bounded)**

On the frozen revision the round's operability surface grew in three runnable, documented ways and no operability property was harmed:

- **Runnable new surfaces:** `map_obligations --self-test` is 24/24 exit 0 with `schema_drift` and `inventory_mismatch` persisted in the contract (r95's unpinned-drift gap closed); the two new exit-1 classes (`inventory_mismatch`, `dual_pointer`) fire live on scratch mutations exactly as documented; the new `dependency_freeze` gate runs (chain 4/4 PASS, self-test 14/14) and closes BR-01 live (reduction → exit 1 `REDUCTION-DETECTED`).
- **Documented commands replay:** every command in the r96 fixture README, Q6's note (re-run at the delivered revision as the note requests), the tools README Round-96 addendum, and the LOG declaration replays as written with the recorded result text and exit; both tools also run from a foreign cwd.
- **Exit contract honored:** 0/1/2 with one terminal RESULT line, stable FINDING IDs, empty stderr and no traceback across 30 probed invocations; `--help` remains the documented RESULT-less exit-0 caveat.
- **No live-tree writes:** corpus manifest byte-identical around the admitted path; census 170/36/134/421 reproduced twice; no repo residue except the disclosed transient BR-05 scratch.

**Bounds (all disclosed, none waived):** D1/D5 — the delivered contract carries a foreign `c3red` scratch pin written through the unguarded `--freeze` path, and nothing validates the pin set; D2 — the new gate has no documented entry outside seat reports; D3 — `SKILL.md`'s registry row is stale and has no `dependency_freeze` row; D4 — BR-05 transient repo-root scratch; D6 — fixtures-README census not re-declared for r96; D7 — the two added self-test cases are pinned but not drop-protected (a future contract edit that removes them stays green); D8 — `dual_pointer` is pinned by no persisted self-test case; D9 — the r93 addendum's `mktemp` control wrong-reason-passes on this inode-exhausted host. D1/D5/D7 are delivered-behavior bounds on the operability axis even though they change no delivered verdict; D2/D3/D6 are documentation/closure items outside the producers' byte-ownership; D9 is environmental.

## Bottom line

**PASS / operability improved (bounded)** — on the frozen r96 revision (tool `2b0ba815…`, map contract `97b76bb8…`, tools README `965b29cd…`, dep gate `a3b57978…`/`7d568cc4…`) `map_obligations --self-test` is 24/24 exit 0, the new `dependency_freeze` gate verifies the chain 4/4 and its self-test 14/14, the r96 fixture replays 16/16 (check_bible CLEAN, support_check 16/16), every r96-documented command replays as written, the 0/1/2 contract holds with one terminal RESULT line and empty stderr on 30 invocations, and the corpus manifest is byte-identical around the runs; the verdict is bounded by the delivered foreign `c3red` scratch pin plus its unguarded `--freeze` mechanism (D1/D5), the undocumented new gate (D2), the stale `SKILL.md` registry row (D3), the open BR-05 scratch residual (D4), the un-re-declared fixtures census (D6), the non-drop-protected added self-test cases (D7), the unpinned `dual_pointer` case (D8), and one environment-induced wrong-reason pass on the r93 `mktemp` control (D9). V02, V19 and V30 were all read and all three corroborate; no seat's finding is carried without my own re-derivation.
