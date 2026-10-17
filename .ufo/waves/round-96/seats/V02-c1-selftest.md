# V02 — c1-selftest seat report (round 96)

- Seat: V02 `c1-selftest`. Report path (only file written by this seat): this file.
- Baseline: r95 closure `dcb2d92` (`lore r95: freeze admitted wave + closure docs`, 2026-10-17 17:19). Round: r96, 64-seat single wave, lore-shokunin.
- Scope: C1(b) self-test / contract cross-check. Poll-wait for Q1 + Q2; `--self-test` at 24/24 PASS exit 0; the persisted contract must carry 24 cases including `schema_drift` and `inventory_mismatch` with expectations matching printed behavior; no regeneration path (`corpus/` hashed before/after); perturbation — flip a persisted expectation in a **scratch copy** of the contract and confirm fail-closed.
- Scratch: `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-96/scratch/V02/` (harness, manifests, perturbation trees, captures). Nothing outside this report path and that scratch dir was written in the repo. No commits, no pushes, no network, no nested agents. All commands run from the lane repo root with `python3`.

## 0. Poll-wait outcome and verified revision

Poll-wait (20 s cadence, 40 tries) using a readiness predicate of *producer report present as `.md`* + contract at 24 cases. First poll attempt was discarded: its predicate matched the `Q2-scratch` **directory** as if it were Q2's report (false positive, no report landed); it was stopped and replaced. Corrected poll (`poll3.sh`) reached READY at try 10, 17:52:23. No ABSENT.

| Artifact | sha256 | bytes | lines | mtime |
|---|---|---|---|---|
| `corpus/tools/map_obligations.py` (Q1) | `2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8` | 37739 | 900 | 17:47:24 |
| `corpus/tools/map-obligations-contract.json` (Q2) | `97b76bb8b1fea97f166ef7586eba69c427ec15bbe7b34eb5345ec65c936493b6` | 3115 | 57 | 17:50:17 |
| `corpus/tools/README.md` (Q2) | `965b29cd41a8af14293eb2e1948f58f310e58c6e752b8fe322c5445b20a91f24` | 18342 | — | 17:51:26 |

Both producer reports pin the same tool and contract hashes (Q1 report line 10; Q2 report lines 9–12), so there is no revision drift between the producer receipts and my runs. Hashes re-checked after every probe below; unchanged throughout.

Mid-flight window (disclosed, reproduced): while Q1's tool was in the tree but Q2's contract still held the r95 22 cases, the tool printed `SELF-TEST CASES 22/24 pinned` / `RESULT PASS` / exit 0 (observed 17:46:07 at tool `c2c284c0…`). This is the subset-tolerant loader (§5); the window state is superseded by the delivered revision.

## 1. C1 — `--self-test` on the delivered revision: 24/24 PASS, exit 0

Hash-guarded harness `.ufo/waves/round-96/scratch/V02/hashcheck.sh` (manifest → run → manifest → diff):

```
$ python3 corpus/tools/map_obligations.py --self-test
SELF-TEST CASES 24/24 pinned
SELF-TEST PASS complete exit=0 findings=none
SELF-TEST PASS missing exit=1 findings=['missing_obligation']
SELF-TEST PASS duplicate exit=1 findings=['duplicate_mapping']
SELF-TEST PASS phantom exit=1 findings=['phantom_obligation']
SELF-TEST PASS source_id_mismatch exit=1 findings=['source_id_mismatch']
SELF-TEST PASS malformed_json exit=2 findings=['malformed_json']
SELF-TEST PASS map_missing exit=2 findings=['map_missing']
SELF-TEST PASS co_mapped_grammar exit=2 findings=['unsupported_map']
SELF-TEST PASS legacy_grammar exit=2 findings=['unsupported_map']
SELF-TEST PASS invalid_pointer exit=2 findings=['invalid_pointer']
SELF-TEST PASS empty_segment exit=2 findings=['invalid_pointer']
SELF-TEST PASS noncanonical_index exit=2 findings=['invalid_pointer']
SELF-TEST PASS noncanonical_claim_index exit=2 findings=['invalid_pointer']
SELF-TEST PASS foreign_path exit=2 findings=['foreign_path']
SELF-TEST PASS traversal_path exit=2 findings=['unsafe_path']
SELF-TEST PASS symlink_path exit=2 findings=['unsafe_path']
SELF-TEST PASS invalid_arguments exit=2 findings=['invalid_arguments']
SELF-TEST PASS frozen_complete exit=0 findings=none
SELF-TEST PASS frozen_tampered exit=2 findings=['snapshot_tampered']
SELF-TEST PASS frozen_missing_digests exit=2 findings=['unpinned']
SELF-TEST PASS frozen_expected_failure exit=1 findings=['missing_obligation']
SELF-TEST PASS frozen_verdict_mismatch exit=2 findings=['frozen_verdict_mismatch']
SELF-TEST PASS schema_drift exit=1 findings=['schema_drift']
SELF-TEST PASS inventory_mismatch exit=1 findings=['inventory_mismatch']
RESULT PASS
```

`selftest_exit=0`; stdout sha256 `4b9fbb347a2da8fda9f5fa1a3296682e056362f7ee36fa457558cc2bb54567fc` (26 lines = 1 pinned-count line + 24 SELF-TEST lines + 1 RESULT line), stderr **0 bytes**, `grep -c '^SELF-TEST FAIL '` = 0. Two later re-runs byte-identical (`SELFTEST_OUTPUT_IDENTICAL`, third run after the whole perturbation battery `STILL_IDENTICAL_AFTER_ALL_PROBES`) — deterministic. Running from a different cwd (`cd /tmp; python3 …/map_obligations.py --self-test`) also gives `RESULT PASS` exit 0, confirming the contract is loaded from the tool's own directory, not cwd.

## 2. C1 — the persisted 24 cases vs printed behavior (independent parser)

Cross-check `.ufo/waves/round-96/scratch/V02/crosscheck.py` (own regex parser over the captured stdout; no contract-writing code):

```
contract_cases=24 printed_cases=24
id_sets_equal=True
MISMATCHES: NONE
RESULT line: ['RESULT PASS']
special cases: {'schema_drift': {'id': 'schema_drift', 'exit': 1, 'finding_ids': ['schema_drift']},
                'inventory_mismatch': {'id': 'inventory_mismatch', 'exit': 1, 'finding_ids': ['inventory_mismatch']}}
```

Checks satisfied: case-id sets equal; per case the printed exit equals the persisted `exit`; the printed finding-id list equals the persisted `finding_ids`; every case carries `PASS`; exactly one terminal `RESULT PASS`; exit 0; stderr empty.

Contract structure vs the r95 baseline (`git show dcb2d92:corpus/tools/map-obligations-contract.json`):

```
old n = 22   new n = 24
core-22 id set equal: True
value-changed core entries: NONE
core entries in r95 order are a subsequence of the r96 order: True
appended: ['schema_drift', 'inventory_mismatch']
new top-level keys: []          (r95's legacy_pointer_dialect etc. all retained)
exit distribution: {0: 2, 1: 7, 2: 15}
```

So the 22 inherited expectations are value-identical and order-preserved; exactly two entries were appended. `schema_drift` and `inventory_mismatch` are each pinned by **exactly one** case, and that case is the only case in the contract producing its finding id.

## 3. C1 — the two new cases are real, non-vacuous mutations

Implementation (`corpus/tools/map_obligations.py`): `ADDED_SELF_TEST_CASES = ("schema_drift", "inventory_mismatch")` (line 71) appended to the 22 `CORE_SELF_TEST_CASES` (line 72). Case preparation (lines 713–722):

- `schema_drift`: drops every `/claims/0` map row, then renames entity 0's `claims` container to `assertions` with content preserved (`entities[0]["assertions"] = entities[0].pop("claims")`). The printed line shows exit 1 with exactly `['schema_drift']`, i.e. the drift branch (line ~444) fires, not a generic mismatch.
- `inventory_mismatch`: writes the fixture with a wrong declaration `declared=(5, 0, 5, 5)` over 4 rows. Printed exit 1 with exactly `['inventory_mismatch']`, i.e. the new gating branch (`inventory_finding`, lines 275–287) fires.

Both cases therefore exercise their target behavior; neither is a stub, and a case whose behavior regressed would print a different exit/finding set and be caught by the persisted expectation (the comparison has teeth — §5 variants A/B).

**Brief-vs-implementation divergence (disclosed by Q2 report lines 55–57; confirmed by me in the source):** the round brief described the `inventory_mismatch` case as "claims key + its map row removed". The delivered case instead uses an **intact** fixture whose map over-declares (5/0/5 declared vs 4 observed rows) — no deletion. The finding id and exit are the same. The deletion-class scenario itself is gated and independently verified below (§6), just not as the pinned case's mutation.

## 4. C1 — no regeneration path, no live-tree writes

Same harness run (`hashcheck.sh`), before/after around the self-test:

```
stray_before=0
selftest_exit=0
stray_after=0
=== corpus hash diff ===   CORPUS_HASH_IDENTICAL
=== contract+tool hash diff ===   CONTRACT_TOOL_HASH_IDENTICAL
=== git status diff ===   GIT_STATUS_IDENTICAL
manifest files = 1804 ; manifest sha256 49d064ff44de5a0dc21dbbef3bfd8ff607db940668cf619f84d7051e6cc718c9 (identical both sides)
stderr bytes = 0
```

- Recursive `corpus/` inventory (excluding `__pycache__`): 1804 files, identical digests and order on both sides.
- Contract **and** tool byte-identical across the run — the tool reads expectations and never writes them back.
- Whole-repo `git status --porcelain` unchanged across the run; no `map-obligations-self-test-*` residue under the repository root (0 before, 0 after).
- Static audit of write paths in the tool: the only writes are `cluster.mkdir`, `(cluster / filename).write_text`, `claim-excerpt-map.md` write, the frozen `expected.json` write, and fixture mutations — all inside the `tempfile.TemporaryDirectory(prefix="map-obligations-self-test-", dir=ROOT)` scratch (`run_self_test`, line 809). The contract filename appears exactly once in the tool, in a read (`load_test_expectations`, line 774). The CLI exposes only `cluster`, `--map`, `--frozen`, `--self-test` — **no flag regenerates or rewrites the contract or any corpus file.**
- Bound honestly: the self-test still creates a transient scratch directory under the repository root (BR-05, unchanged in r96 and stated as open in the README addendum); my check shows no persistent residue and no git-status change.

## 5. C1 — perturbation battery on SCRATCH copies (fail-closed check)

Harness `.ufo/waves/round-96/scratch/V02/perturb.sh` copies the delivered tool **and** contract into `…/scratch/V02/perturb/<variant>/corpus/tools/`, mutates only the copy, runs the copied tool. Live tree untouched (verified: `corpus/tools/` listing unchanged; `git status` unchanged).

| Variant | Mutation | Observed | Verdict |
|---|---|---|---|
| A | `complete` expectation exit 0 → 1 | `SELF-TEST FAIL complete exit=0 findings=none` / `FINDING self_test_mismatch: …` / `RESULT ERROR` / `EXIT=2` | fail-closed ✓ |
| B | `missing` expectation gains `phantom_obligation` | `SELF-TEST FAIL missing exit=1 findings=['missing_obligation']` / `FINDING self_test_mismatch: …` / `RESULT ERROR` / `EXIT=2` | fail-closed ✓ |
| C | drop the `schema_drift` case (24 → 23) | `SELF-TEST CASES 23/24 pinned` / `SELF-TEST PASS inventory_mismatch …` / `RESULT PASS` / `EXIT=0` | **fail-open (bounded, see below)** |
| C2 | drop a **core** case (`phantom`) | `FINDING self_test_contract: contract drops implemented self-test cases: phantom` / `RESULT ERROR` / `EXIT=2` | fail-closed ✓ |
| C3 | drop the `inventory_mismatch` case | `SELF-TEST CASES 23/24 pinned` / `RESULT PASS` / `EXIT=0` | **fail-open (same class as C)** |
| D | duplicate a case id | `FINDING self_test_contract: contract repeats a self-test case ID` / `RESULT ERROR` / `EXIT=2` | fail-closed ✓ |
| E | `exit` changed to the string `"1"` | `FINDING self_test_contract: contract contains an invalid self-test expectation` / `EXIT=2` | fail-closed ✓ |
| F | `finding_ids` changed to a string | same `self_test_contract` / `EXIT=2` | fail-closed ✓ |

The brief's perturbation (flip a persisted expectation) is A/B — both fail closed with `self_test_mismatch` exit 2, so the 24/24 result is a real match, not a harness that always passes. **Bounded residual found by this seat (report exactly, do not paper over):** the two *added* cases are not drop-protected. Removing `schema_drift` or `inventory_mismatch` from the contract leaves `--self-test` green (`RESULT PASS`, exit 0); only the non-gating `SELF-TEST CASES 23/24 pinned` receipt changes. The loader (`load_test_expectations`, lines 794–801) fails closed on unknown ids and on drops of any of the 22 `CORE_SELF_TEST_CASES`, but treats `ADDED_SELF_TEST_CASES` as optional. This is **disclosed by design** — Q1 report item 4 ("Self-test coverage is subset-tolerant by design (core 22 must be pinned; nothing …)") and the README Round-96 addendum ("requires the contract to pin every core case and to pin no unimplemented case, then exercises exactly the pinned cases"). Its consequence for C1(b): the two new behaviors are pinned *at delivery*, but the pinning is not *enforced* — a future contract edit that drops them (or a merge that reverts the two entries) would pass the self-test with only a receipt line as evidence, which is precisely the r95 residual class ("`schema_drift` not pinned by a persisted self-test case") in weakened form.

## 6. Supplementary — C1(a) deletion class reproduced on a real fixture (independent of the isolated case)

Scratch copy of `corpus/fixtures/r95-crossing-aftermath`; mutation deletes entity 1's `claims` key (`entities.json#/1/claims/0` disappears) **and** its map row `J07`; the unmutated copy is the control. Same harness, same mutation, run against both revisions:

```
OLD (r95 tool d1c239cc, before Q1 landed)
  control:  OBLIGATIONS raw=15 mapped=15 / INVENTORY 15/15; 2/2; 17/17 / RESULT PASS        exit=0
  mutated:  OBLIGATIONS raw=14 mapped=14 / INVENTORY JSON-FACTS 14/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/17 MISMATCH
            RESULT PASS                                                                     exit=0   <- the carried deletion class
DELIVERED (r96 tool 2b0ba815)
  control:  OBLIGATIONS raw=15 mapped=15 / INVENTORY 15/15; 2/2; 17/17 / RESULT PASS        exit=0
  mutated:  OBLIGATIONS raw=14 mapped=14 / INVENTORY JSON-FACTS 14/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/17 MISMATCH
            FINDING inventory_mismatch: declared JSON-facts/editorial-rows/total-rows 15/2/17; observed 14/2/16
            RESULT FAIL                                                                     exit=1
```

So C1(a) is independently confirmed on the delivered revision with a real fixture (not only in the isolated self-test fixture), and the before→after flip is exact. (C1(a)/C1(c) are other seats' primary scope; this is a cross-check, not a substitute for them. Note `dual_pointer` — added the same round — is pinned by **no** persisted self-test case: `any('dual_pointer' in c['finding_ids'] for c in contract cases)` = False, so that new gate's behavior rests on other seats' demonstrations only.)

## 7. Adjacent non-regression evidence on the same delivered revision

```
r95-crossing-aftermath   OBLIGATIONS raw=15 mapped=15  INVENTORY 15/15; 2/2; 17/17  RESULT PASS  exit=0
r96-crossing-response    OBLIGATIONS raw=16 mapped=16  INVENTORY 16/16; 2/2; 18/18  RESULT PASS  exit=0
r94-paired-crossing      OBLIGATIONS raw=14 mapped=14  INVENTORY 14/14; 2/2; 16/16  RESULT PASS  exit=0
```

The inherited r95 fixture and the new r96 fixture both stay clean under the hardened tool; the 0/1/2 exit contract is unchanged (exit-0 clean, exit-1 gating findings, exit-2 could-not-evaluate, exercised across the 24 cases). Full r87–r96 regression and frozen replay belong to the C1-regression seats (V03/V04) and Q1/Q2's own batteries; I did not duplicate them.

## 8. Findings for the round (evidence; adjudication belongs to closure)

1. **Added-case pinning is not enforced** (§5 C/C3): dropping `schema_drift` or `inventory_mismatch` from the contract keeps `--self-test` at `RESULT PASS` exit 0 with only a `23/24 pinned` receipt; the 22 core cases are drop-protected. Disclosed as "subset-tolerant by design" by Q1/README, but it means the r96 C1(b) pinning guarantee is weaker for exactly the two new behaviors the round adds.
2. **`dual_pointer` (C1(c)) has no persisted self-test case** (§6), unlike the other two C1 behaviors — coverage asymmetry within the same bundle.
3. **`inventory_mismatch` case mutation differs from the brief** (§3): over-declared intact fixture rather than the deletion-class mutation; same finding id and exit. Disclosed by Q2, reproduced by me from the source. The deletion class itself is separately gated and verified (§6).
4. **BR-05 remains open** (§4): self-test scratch is created under the repository root; unchanged in r96 and documented as open in the README addendum.
5. **Harness defect caught in my own poll** (§0): matching `Q*-scratch` directories as producer reports would have produced a false READY; recorded so other seats' poll predicates are checked for the same pattern.

## 9. Reproducibility

Scratch artifacts kept under `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-96/scratch/V02/`: `hashcheck.sh` (§1/§4 harness), `crosscheck.py` (§2), `selftest.out` / `selftest2.out` / `selftest3.out` / `selftest.err`, `corpus.hash.{before,after}`, `contract.hash.{before,after}`, `gitstatus.{before,after}`, `contract.r95.json`, `deletion_probe.sh` + `deletion/` (§6), `perturb.sh` + `perturb/{A_flip_exit,B_flip_findings,C_drop_case,C2,C3,D_dup_case,E_bad_exit_type,F_bad_findings_type}` (§5), `poll{,2,3}.sh` + logs. All commands were run from the lane repo root with `python3` on the pinned revision; no `/tmp` scratch was used (Q2's report notes `/tmp` is inode-exhausted in this environment).

Bottom line: **PASS** — on the pinned delivered revision (tool `2b0ba815…`, contract `97b76bb8…`, both matching the producers' pins), `--self-test` prints `SELF-TEST CASES 24/24 pinned` + 24 SELF-TEST PASS + `RESULT PASS`, exit 0, stderr empty, deterministic; all 24 persisted expectations match printed exits and finding-ids exactly under an independent parser; the two new cases are present, uniquely identified, non-vacuous, and the 22 inherited entries are value-identical; `corpus/` (1804 files), the contract and the tool are byte-identical before/after with no residue, no git-status change and no CLI path that could rewrite them; flipped expectations (the brief's perturbation) fail closed with `self_test_mismatch` exit 2 — with two residuals recorded, not waived: dropping either *added* case keeps the self-test green (`23/24 pinned` receipt only), and `dual_pointer` is pinned by no persisted case.
