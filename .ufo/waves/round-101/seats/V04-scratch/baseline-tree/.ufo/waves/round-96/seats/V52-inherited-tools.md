# V52 — inherited-tools (round 96)

**Seat role:** leaf verifier. Claim under test: `git diff dcb2d92` — `check_bible` /
`support_check` / `boundary` / `discriminate` / `contract` byte-untouched; r88–r95
fixtures untouched. Baseline `dcb2d92` (r95 closure); HEAD `60dba0c` (one commit beyond
baseline — see §7). All commands from the lane repo root
(`/home/vgpnk/Projects/shokunin/lore-shokunin`); all scratch under
`.ufo/waves/round-96/seats/V52-scratch/`. No commits, no network, no nested agents.

**Revision under test:** final snapshot taken 2026-10-17 **17:52:38** (manifest-3),
after all six producer reports landed (poll loop saw 6/6 at 17:52:29). A second full
snapshot at 17:51:37 (manifest-2) is byte-identical to manifest-3, so the verified
revision is stable across the Q2-report landing window.

## 0. Reading of the brief (the "contract" item)

Of the five named groups, four are read-only inherited tools and one — **`contract` =
`corpus/tools/map-obligations-contract.json`** — is a declared-change file: the round
declaration in `LOG.md` (uncommitted, +67 lines vs `dcb2d92`) assigns it to producer Q2
and requires the C1(b) change "contract 22→24". The only other tracked `*contract*`
file in the corpus is `corpus/tools/boundary-doc-contract.json` (covered under
"boundary"). So the literal claim "contract byte-untouched" is *false by design*; the
verifiable integrity claim is "no *undeclared* modification of any inherited tool, and
the contract changes only as declared". Both are checked below, and §6 resolves the
literal reading explicitly.

## 1. Verification set

| Group | Path(s) | Role |
|---|---|---|
| check_bible | `corpus/fixtures/check_bible.py` (+ historical copy `corpus/live/rejected-r4/check_bible.py`) | must be untouched |
| support_check | `corpus/tools/support_check.py` | must be untouched |
| boundary | `corpus/tools/boundary_doc_check.py`, `corpus/tools/boundary-doc-contract.json` | must be untouched |
| discriminate | `corpus/tools/discriminate_check.py` | must be untouched |
| contract | `corpus/tools/map-obligations-contract.json` | Q2-owned, declared 22→24 |
| (declared, for context) | `corpus/tools/map_obligations.py` (Q1), `corpus/tools/README.md` (Q2) | expected to change |
| context | `corpus/fixtures/README.md` | must be untouched |
| r88–r95 fixtures | 164 tracked files in 24 dirs (r88×4, r89×11, r90×4, r91×2, r93×1, r94×1, r95×1; no r92 dirs exist) | must be untouched |

## 2. Byte evidence — baseline blob vs worktree bytes

Method (`V52-scratch/manifest.sh`): for each path, `git ls-tree dcb2d92` mode,
`git cat-file -p dcb2d92:<path> | sha256sum` (baseline), and worktree
`sha256sum` / `git hash-object`. 174 lines = 10 tool/doc files + 164 fixtures.

- **manifest-1** (17:41, pre-landing): `lines=174`, `diffs=0`,
  sha256 `e802243f8e553141a7b681f2b049938afd0ba60d8e7dcc4113bd5ebd0f905c1f`.
- **manifest-2** (17:51:37, post Q1/Q2 file landing): `lines=174`, `diffs=3` —
  exactly the three declared producer files.
- **manifest-3** (17:52:38, post all six producer reports): `diffs=3`,
  `diff manifest-2.txt manifest-3.txt` → **IDENTICAL**
  (manifest-3 sha256 recorded in scratch).

Final per-file verdicts (baseline sha256 → worktree sha256):

| File | Baseline | Worktree (final) | Verdict |
|---|---|---|---|
| `corpus/tools/support_check.py` | `55a5eb27…b442c` | same | **byte-untouched** |
| `corpus/tools/boundary_doc_check.py` | `ebb6a084…6b0053` | same | **byte-untouched** |
| `corpus/tools/boundary-doc-contract.json` | `e89d2a76…539871` | same | **byte-untouched** |
| `corpus/tools/discriminate_check.py` | `6c7b7cd8…108eef` | same | **byte-untouched** |
| `corpus/fixtures/check_bible.py` | `ff9fd2aa…7d1421` | same | **byte-untouched** |
| `corpus/live/rejected-r4/check_bible.py` | `1eb06de5…2f62eb` | same | **byte-untouched** |
| `corpus/fixtures/README.md` | `f3733aad…e11141c` | same | **byte-untouched** |
| `corpus/tools/map-obligations-contract.json` | `8173bb97…a39170db` | `97b76bb8…936493b6` | **changed — declared C1(b), Q2-owned** |
| `corpus/tools/map_obligations.py` | `d1c239cc…e4212108` | `2b0ba815…edc4a3ba8` | changed — declared Q1-owned |
| `corpus/tools/README.md` | `5d033c9d…879a264` | `965b29cd…20a91f24` | changed — declared Q2-owned |
| 164 r88–r95 fixture files | — | — | **all byte-untouched (0 diffs)** |

So among the five named groups: `check_bible`, `support_check`, `boundary` (both files)
and `discriminate` are byte-untouched; `contract` changed exactly as declared. All 171
non-declared lines of the manifest are baseline==worktree.

## 3. git diff commands (quoted)

```
$ git diff dcb2d92 --stat -- corpus/tools/ corpus/fixtures/
 corpus/tools/map_obligations.py | 139 +++++++++++++++++++++++++++++++++-------
 1 file changed, 115 insertions(+), 24 deletions(-)          # (at 17:46; final also lists README + contract, per repo-wide below)

$ git diff dcb2d92 --name-status            # final, repo-wide
M	LOG.md
M	SCORECARD.md
M	corpus/tools/README.md
M	corpus/tools/map-obligations-contract.json
M	corpus/tools/map_obligations.py

$ git status --porcelain                    # final
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

Tracked changes repo-wide are exactly: the round declaration (`LOG.md`), the r95-closure
bookkeeping commit (`SCORECARD.md`, from `60dba0c`), and the three declared corpus/tools
files. Untracked additions are exactly the declared r96 artifacts. **No scope
violation found** — nothing else in the corpus (or repo) is added, removed, or modified.

File modes/types (baseline `git ls-tree` vs worktree `stat`): all eight corpus/tools +
check_bible files are `100644` / `644 regular` on both sides — no mode flips.

## 4. r88–r95 fixtures

- File sets: baseline tree (`git ls-tree -r dcb2d92 --name-only corpus/fixtures/`,
  filtered r88–r95) vs worktree (`find corpus/fixtures -type f`) → 164 vs 164,
  `diff` → **FILE SETS IDENTICAL** (no deletions, no additions).
- Bytes: `V52-scratch/fixture-bytecheck.sh` (baseline blob hash vs `git hash-object`)
  → `CHECKED=164 DIFFERING=0`, run twice (17:41 pre-landing and 17:51:37 post-landing).
- `git status --porcelain -- corpus/fixtures corpus/live corpus/tools` shows only the
  untracked `r96-crossing-response/` — the r88–r95 dirs are clean.
- Note: `r95-crossing-aftermath` is the declared byte-copy source for the new r96
  fixture (Q4); the r95 source itself is untouched (all 10 of its files identical).

## 5. Behavioral corroboration (untouched tools still function on the delivered tree)

Three runs spanning the producer landing window (17:40–17:41 pre-landing; 17:51:37 on
the final revision), full transcripts in `V52-scratch/inherited-behavior-{1,2,3}.out`:

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath
CLEAN: schema, citations, relations, timeline; 0 violations          EXIT=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r95-crossing-aftermath
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17; DISTINCT-ANCHORS 13/13
SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS 2/2; MODES 17/17; VALIDATED-ROWS 17/17
RESULT PASS                                                          EXIT=0
$ python3 corpus/tools/boundary_doc_check.py
CERTIFIED …; replay_receipts=3/3; replay_cases=14/14; anchors=2/2      EXIT=0
$ python3 corpus/tools/boundary_doc_check.py --self-test
SELF-TEST PASS (8/8 controls)                                         EXIT=0
$ python3 corpus/tools/discriminate_check.py
mode=delivered checker_sha256=ff9fd2aa…7d1421 matches_pin=True
RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression  EXIT=0
```

These match the r95 closure battery exactly. Byte-identity to baseline makes behavioral
identity implied; the runs are corroboration, and they were executed from the scratch
cwd so any tool-side scratch landed in `V52-scratch/`, not the corpus.

## 6. The contract item, resolved explicitly

- `corpus/tools/boundary-doc-contract.json` — byte-untouched (`e89d2a76…`).
- `corpus/tools/map-obligations-contract.json` — changed `8173bb97…` → `97b76bb8…`.
  Parsing the delivered file: `self_test.cases` = **24** case IDs, adding exactly
  `schema_drift` and `inventory_mismatch` to the r95 22
  (`complete, missing, duplicate, phantom, source_id_mismatch, schema_drift,
  inventory_mismatch, malformed_json, co_mapped_grammar, legacy_grammar,
  invalid_pointer, empty_segment, noncanonical_index, noncanonical_claim_index,
  foreign_path, traversal_path, symlink_path, frozen_complete, frozen_tampered,
  frozen_missing_digests, frozen_expected_failure, frozen_verdict_mismatch,
  map_missing, invalid_arguments`).
- Independent cross-check: Q2's report (`Q2-contract-docs.md`) declares contract
  `97b76bb8…` and README `965b29cd…`; Q1's report (`Q1-tool-hardening.md`) declares
  tool `2b0ba815…` and cites the same live contract `97b76bb8…`; all three match the
  worktree bytes in manifest-3.

So the literal statement "contract byte-untouched" **fails as stated**, and the failure
is precisely the declared C1(b) delivery — not an integrity violation. A verifier
asserting "all five groups untouched" would be wrong; a verifier calling the contract
change a violation would also be wrong.

## 7. Bounds and observations

- **HEAD beyond baseline:** HEAD is `60dba0c` ("lore r95: close round — SCORECARD
  admitted section"), one commit after the stated baseline `dcb2d92`; it touches only
  `SCORECARD.md` (+32 lines) — no corpus bytes. `LOG.md`'s r96 declaration (+67) is
  uncommitted.
- **Q1 revised its tool mid-round:** worktree `map_obligations.py` was `c2c284c0…` at
  17:44 and `2b0ba815…` from ~17:50; my final snapshots are on the final revision.
- **Transient stray dirs at repo root** (BR-05 class, self-test scratch): 
  `map-obligations-self-test-eqw27d_f/` present 17:39:22, gone by 17:42:21;
  `map-obligations-self-test-if1614id/` present 17:49:43, gone by 17:51:37. Both absent
  from the final `git status`. Not mine; recorded as observed.
- **Environment:** one transient `/tmp` "No space left on device` (17:41, tmpfs); it
  cleared within a minute (8.5G free at 17:42) and all my scratch was moved to
  `V52-scratch/`. No impact on the verified evidence.
- **Bounds:** this seat certifies byte-identity (and light behavioral corroboration) of
  the named files; it does not re-verify C1/C2/C3 semantics (other seats' claims), and
  it does not claim the untouched files are correct, only unchanged.

**Bottom line: PASS (with the contract reading corrected) — `check_bible`,
`support_check`, `boundary` (both files), and `discriminate` are byte-untouched vs
`dcb2d92` (sha256 unchanged: `ff9fd2aa…`, `55a5eb27…`, `ebb6a084…` + `e89d2a76…`,
`6c7b7cd8…`; 171/174 manifest lines baseline==worktree), all 164 r88–r95 fixture files
are byte-untouched with identical file sets, and the only change in the five named
groups is `map-obligations-contract.json` → `97b76bb8…`, changed exactly as declared by
C1(b) (24 cases incl. `schema_drift` + `inventory_mismatch`, Q2-owned, cross-checked
against Q1/Q2 reports); repo-wide diff contains no undeclared path and no scope
violation.**
