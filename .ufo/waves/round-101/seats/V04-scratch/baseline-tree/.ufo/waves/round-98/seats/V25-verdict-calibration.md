# V25 — verdict-calibration (round 98, single-wave swarm)

**Seat:** V25 verdict-calibration — read the C1 seats; own the demos; one CALIBRATION
verdict with bounds. **C1 subject:** `corpus/tools/dependency_freeze.py` (S1) +
`corpus/tools/dependency-freeze-contract.json` (S1) + `corpus/tools/README.md` (S2).

**Repo root for every command:** `/home/vgpnk/Projects/shokunin/lore-shokunin`
(session cwd is the parent repo; every write used absolute paths under the lane repo and
was resolved before writing). **Baseline:** r97 closure `9a3d648` (pre-round bytes via
`git show 9a3d648:<path>`; wave tree uncommitted; HEAD `dd4df1b`).

**Frozen revisions under test** (copied to `V25-scratch/frozen-r98/` before any demo;
every delivered-revision run below used these copies, never the live files):

```
03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b  dependency_freeze.py          (S1)
153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947  dependency-freeze-contract.json (S1)
1d299c16bf9a0b34526f4a799cdd3117867f6d4d278866b66366b78700d79b84  README.md                      (S2)
```

Both tool/contract hashes equal S1's own reported revisions and S2's quoted final
revisions; README equals S2's. Baseline copies (`git show 9a3d648`-era):
tool `b06275f3bbdeabaab615138b3004703fce701a786af882d3b732828b37722130`,
contract `27273be27d33ad864f06d656f28dca8eabc9d76f6ebe62583372a88c9e64e781`.
Live hashes re-checked after the last probe batch — unchanged.

---

## 1. Poll-wait record (protocol compliance)

`V25-scratch/poll.sh` (background, 20 s cadence, 40 tries; condition: tool changed vs
baseline AND `S1-*.md` AND `S2-*.md` present) plus a foreground 10 s loop. Log:

```
try 7  20:30:59 missing: TOOL-UNCHANGED REPORT:S1 REPORT:S2
try 8  20:31:19 missing: REPORT:S1 REPORT:S2          # tool bytes changed (S1 freeze done)
try 19 20:34:59 missing: REPORT:S1                     # S2-tools-docs.md landed 20:34
try 21 20:35:39 ALL-PRESENT                            # S1-freeze-hygiene.md landed 20:35
```

No verification run was taken against a plan or an unreported revision; every
delivered-revision run below postdates READY and ran on the frozen copies. Both C1
seats were read in full before the demos: `S1-freeze-hygiene.md` (14219 B) and
`S2-tools-docs.md` (10223 B). Endgame note: no all-reports poll was needed (only
S1+S2); no stall escape occurred (21/40 tries, well inside budget).

## 2. Pre-state captures (baseline `9a3d648`, my own mirrors)

**(a) SELF-TEST-MISMATCH exit code** — baseline tool, contract copy with
`self_test.expected.clean.exit` 0→1:

```
CASE clean: exit=0 expected=1 findings=[] MISMATCH
…
SELF-TEST 15/16
FINDING SELF-TEST-MISMATCH: cases failed: ['clean']
RESULT FAIL                        # EXIT=1
```

**(b) Legacy path-less pin + `--freeze`** — baseline tool, r95 pin's `fixture` key removed:

```
FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures/r95-crossing-aftermath: pin r95-crossing-aftermath already names None; freezing a same-named path elsewhere would rewrite the delivered pin
RESULT ERROR                       # EXIT=2
```

`fixture` key still absent after the attempt — manual contract edit was the only route.

**(c) Chain** — baseline tool (symlinked mirror root, ROOT-correct): r88/r94/r95/r96
`RESULT PASS` exit 0 with digests `15ef230e…`/`2527beb9…`/`d541ae64…`/`d422a9b3…`;
`r97-crossing-acknowledgment` → `FINDING UNPINNED-FIXTURE … RESULT ERROR` exit 2.

**(d) `precedence`** — baseline text was one sentence with no finding IDs:
`"semantic inventory findings decide first (exit 1); a content digest change the frozen inventory does not model exits 2"`.

## 3. C1(a) — `SELF-TEST-MISMATCH` exits 2, pinned as case 17

Persisted case set grew 16→17 by append, expectation set likewise, no inherited
expectation changed (my demos.py §A):

```
A delivered FROZEN_CASES n=17 added=['self_test_mismatch'] removed=[]
A contract expected n=17 added=['self_test_mismatch'] removed=[]
A inherited expected entries changed vs baseline: []
```

Frozen delivered tool `--self-test` (frozen root, symlinked fixtures):

```
$ python3 <frozen-r98>/corpus/tools/dependency_freeze.py --self-test
…
CASE self_test_mismatch: exit=2 expected=2 findings=['SELF-TEST-MISMATCH'] ok
SELF-TEST 17/17
RESULT PASS                        # exit=0
```

**My own independent mismatch demo** (distinct from both producers'): frozen delivered
tool, contract copy with `clean` expectation flipped 0→1:

```
CASE clean: exit=0 expected=1 findings=[] MISMATCH
CASE self_test_mismatch: exit=2 expected=2 findings=['SELF-TEST-MISMATCH'] ok
SELF-TEST 16/17
FINDING SELF-TEST-MISMATCH: cases failed: ['clean']
RESULT ERROR                       # exit=2; traceback in output: False
```

Same scenario on baseline bytes: `RESULT FAIL`, exit 1 (§2a) — the flip 1→2 is real.
The case is load-bearing under two single-sided falsifications:

```
H (tool copy with the exit-2 emit reverted to exit-1): CASE self_test_mismatch: exit=1 expected=2 … MISMATCH; RESULT FAIL exit=1
I (contract copy with expected self_test_mismatch exit 2→1): CASE self_test_mismatch: exit=2 expected=1 … MISMATCH; RESULT ERROR exit=2
```

Fail-closed bounds: dropping the expectation from a contract copy →
`FINDING CONTRACT-INVALID: self-test expectation set mismatch; missing=['self_test_mismatch'] extra=[]`, exit 2.
Alignment with `map_obligations.py` verified in-tree (`corpus/tools/map_obligations.py:877-878`:
`FINDING self_test_mismatch: isolated CLI outcomes differ from persisted expectations` /
`RESULT ERROR`).

## 4. C1(b) — path-less legacy pin migrated in place by `--freeze`

Frozen delivered tool, mirror with the r95 pin's `fixture` key removed:

```
$ python3 <mirror>/corpus/tools/dependency_freeze.py --freeze corpus/fixtures/r95-crossing-aftermath
MIGRATED r95-crossing-aftermath: path-less legacy pin now names corpus/fixtures/r95-crossing-aftermath
FROZEN r95-crossing-aftermath: events 4; dependency-edges 3; relations 1
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
RESULT PASS                        # exit=0; pin's fixture after: 'corpus/fixtures/r95-crossing-aftermath'
```

Guard retained (r97 hardening not weakened): pin recording
`corpus/fixtures/r95-crossing-aftermath`, freeze invoked on a byte-identical same-named
copy at `corpus/fixtures/elsewhere/r95-crossing-aftermath` →

```
FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures/elsewhere/r95-crossing-aftermath: pin r95-crossing-aftermath already names 'corpus/fixtures/r95-crossing-aftermath'; freezing a same-named path elsewhere would rewrite the delivered pin
RESULT ERROR                       # exit=2
```

Verification alone on a path-less pin still fails closed: `FINDING CONTRACT-INVALID: pin
r95-crossing-aftermath needs a repo-relative fixture path`, exit 2. Migration scope is
exactly the path-less class (absent/`null`/empty recorded path — S1's code and S2's
`null` variant both probed).

## 5. C1(c) — `precedence` names the full exit-2 order and finding IDs

Delivered text (contract field, byte-quoted in §2d delta): exit-1 IDs
(`REDUCTION-DETECTED, ADDITION-DETECTED, ENDPOINT-CHANGE`), then "Exit-2
(could-not-evaluate) checks run in this order and the first failing check decides:
UNPINNED-FIXTURE … or CONTRACT-INVALID …, FIXTURE-MISSING …, PATH-MISMATCH …,
FILE-MISSING / MALFORMED-JSON / MALFORMED-MODEL …, DIGEST-MISMATCH …,
INVALID-ARGUMENTS …, SELF-TEST-MISMATCH …; `--freeze` additionally raises
SCOPE-REFUSED …; a path-less legacy pin is migrated in place". Every exit-2 finding ID
the tool can emit appears; order matches the tool's check sequence in `verify()` /
`freeze()` / `main()` (read against the delivered diff).

## 6. Non-regression — inherited cases, pins, chain

- **Executed 16-case comparison:** untampered baseline `--self-test` → `SELF-TEST 16/16`
  `RESULT PASS` exit 0; delivered run → 17 rows; the only differing row is the added
  `self_test_mismatch`; all 16 inherited rows byte-identical (`ok`, same exits/findings).
- **Body diff:** delivered `self_test_cases()` = baseline body with exactly one blank
  line + a 12-line insertion (8 code + 4 comment lines) before `return cases`;
  line-for-line reconstruction equals baseline (`True`). `compare()`, `verify()`,
  `build_model()` untouched in `git diff 9a3d648 -- corpus/tools/dependency_freeze.py`.
- **Contract:** all four inherited pins JSON-identical to baseline; `exit_codes`,
  `self_test.base_fixture`, `scope`, `data_files`, `required_files` equal; pins added
  `['r97-crossing-acknowledgment', 'r98-clerk-filing']`, removed `[]`; `revision` field
  advanced `2393934…` → `dd4df1b…` (expected).
- **Chain 6/6** on the frozen delivered tool: all `RESULT PASS` exit 0; the four
  inherited digests byte-identical to baseline (§2c); r97 `3c922d20…`, r98 `59a0f4fa…`.
  r98 pin event `clerk-filing-open` → `depends_on ["acknowledgment-aru-records"]`,
  endpoint `{tick: 14, entity_id: clerk-maren, place_id: chalk-stair}` (read from the
  frozen contract).
- **V46 discharge reproduced by me** (C2-adjacent, independent): scratch mirror of the
  r97 fixture at its pinned path, tick-13 edge dropped; mutated `timeline.json` sha256
  `37a425b97af658d71b8dc8904f43fd75859905bac326489a71adb67004004eb1` (byte-equal to
  V46's recorded sha and S1's quote); control `RESULT PASS` exit 0, mutated
  `FREEZE … dependency-edges 4/5` / `FINDING REDUCTION-DETECTED: event
  acknowledgment-aru-records lost depends_on ['response-evin-salt-court']` / `RESULT
  FAIL` exit 1.
- `git diff 9a3d648 --stat -- corpus/tools/`: only README (+56), contract (+193/-10),
  tool (+42/-10); `map_obligations.py`, `support_check.py`, `boundary_doc_check.py`
  byte-unchanged.

## 7. Cross-read of the C1 seats

- **S1 (`S1-freeze-hygiene.md`)** and **S2 (`S2-tools-docs.md`)** both report PASS. My
  independent runs agree on every point I re-derived: pre/post exit codes, the persisted
  17th case, migration + retained refusal, precedence text, 17/17, chain 6/6, digests,
  inherited expectations unchanged. S2's contract-intermediate hashes (`b06275f3…` →
  `3a940a9f…` → `c435239d…` → `153ebc5b…`) and S1's final `153ebc5b…` match my frozen
  copy; S2's recorded mid-flight staleness (provenance_note "four fixtures" while six
  pins existed) is resolved in the final contract I froze.
- **S2's poll record** notes S1's report was ABSENT at their hand-off; all their claims
  were verified against delivered bytes, not a plan (protocol-compliant). My poll
  observed S1 landing at 20:35:39 (same window) — no contradiction, the endgame class
  the declaration warned about.
- **One contradiction found — S2's README, docs-level, recorded exactly.** The r97
  supersession paragraph in `corpus/tools/README.md` says self-test scratch is "covered
  by `.gitignore` (`*-self-test-*/`)"; the r98 addendum's opening says "the open r94
  residual BR-05 (the self-test scratch still lives under the repository root and **is
  not gitignored** — unchanged in r98)". Ground truth: `.gitignore:4` is
  `*-self-test-*/` (present since r97 commit `9d25df9`), and
  `git check-ignore -v` matches `dependency-freeze-self-test-abc123/`,
  `map-obligations-self-test-x/`, and the observed lane-root `v05-self-test-scratch/`
  (all `.gitignore:4`). The "not gitignored" parenthetical is wrong and self-
  contradictory; C1's functional calibration is unaffected, but the sentence is a
  closure-doc item.
- **Strays:** `/home/vgpnk/Projects/shokunin/baseline-analyze.txt` exists (105 B, mtime
  2026-10-17 20:30:10, parent tree) — the r94-F01 class, flagged by S2 and by S1 (via
  S3's D5); not mine. `v05-self-test-scratch/` at the lane root is a seat scratch
  matching the gitignore pattern (BR-05-class residue, not a stray in git terms).

## 8. Calibration verdict (with bounds)

**C1 verdict: calibration improved (bounded).** All three sub-claims verify on the
delivered revision independently of the producers' demos: (a) `SELF-TEST-MISMATCH` now
exits 2 (`RESULT ERROR`) where baseline exited 1 (`RESULT FAIL`), pinned as persisted
case 17 with the 16 inherited cases byte-identical and load-bearing under tool-side and
contract-side single falsifications; (b) a path-less legacy pin migrates in place under
`--freeze` (baseline: `SCOPE-REFUSED … already names None`, manual edit only) with the
recorded-path guard and verify-side fail-closed behavior intact; (c) the contract
`precedence` text names the full exit-1/exit-2 order and every finding ID. Non-regression:
16/16 inherited rows executed-identical, four inherited pins JSON-identical, chain 6/6
with inherited digests byte-identical, V46 mutation reproduced.

Bounds (named, not netted):

1. **The 1→2 flip is a deliberate contract change.** Any consumer that treated exit 1
   from `--self-test` as "a finding was detected" must re-read; the new code aligns with
   `map_obligations.py`'s could-not-evaluate treatment (verified in-tree). Only the
   self-test-mismatch path moved; the other exit-1 findings are unchanged.
2. **The self-test binds consistency, not truth.** H and I each show a single-sided edit
   fails; a tool+contract edited consistently together (behavior and expectation moved in
   tandem) stays green — inherent to a persisted self-test, not closable here.
3. **Assertion breadth of case 17.** It pins exit 2 + exactly `FINDING SELF-TEST-MISMATCH`
   at the outer level of a corrupted-mirror replay; the nested inner cascade (inner run
   additionally mismatching its own `self_test_mismatch` case; depth-2 failing
   `FIXTURE-MISSING`) is not asserted — bounded on purpose, and the recursion is provably
   finite via `DEPENDENCY_FREEZE_SELF_TEST_CHILD` (read in the delivered diff).
4. **Migration trusts the invocation for path-less pins.** Demonstrated: a path-less pin
   + a byte-identical same-named copy elsewhere migrates and binds the *foreign* path
   (`MIGRATED … now names corpus/fixtures/elsewhere/r95-crossing-aftermath`, exit 0). A
   legacy pin has no recorded path to defend; the guard protects recorded paths only
   (path-bearing case still `SCOPE-REFUSED`, exit 2).
5. **`precedence` is prose.** No checker parses it (`grep -rn "precedence"
   --include=*.py corpus/tools/` → only the tool's own docstring mention); its accuracy
   is review-maintained, not machine-pinned.
6. **Pin payload scope unchanged:** the five JSON tables only; fixture Markdown is not
   pinned (inherited r97 bound, still open).
7. **README docs contradiction (S2's file) recorded in §7** — "not gitignored" vs
   `.gitignore:4`; a closure-doc repair item, not a C1 behavior defect.
8. **Verdict scope:** C1 demos ran on frozen copies; my chain/V46 evidence is behavioral
   support for C2 whose claim verdicts rest with the C2 seats.

## 9. Hygiene

Writes confined to `V25-scratch/` (frozen copies, mirrors, harnesses `demos.py`/
`demos2.py`/`demos3.py`, logs) and this report (absolute path
`/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-98/seats/V25-verdict-calibration.md`,
resolution verified before writing); producer files read-only throughout (all
delivered-revision runs on frozen copies). No commits, no pushes, no network, no nested
agents. Live tool/contract/README hashes re-checked after the last probe batch —
unchanged (`03d04365…` / `153ebc5b…` / `1d299c16…`).

**Bottom line: PASS — calibration improved (bounded): `SELF-TEST-MISMATCH` verified exit 1→2 with persisted case 17 (16 inherited cases byte-identical, load-bearing under both single-sided falsifications), path-less legacy pin verified migrated by `--freeze` with the recorded-path guard and verify fail-closed behavior intact, and the contract `precedence` verified naming the full exit-2 order and finding IDs; chain 6/6 with inherited digests byte-identical and V46's mutation reproduced (`37a425b9…` sha, `REDUCTION-DETECTED` exit 1); bounds recorded (exit-shift re-read, consistency-not-truth, case-17 assertion breadth, path-less migration trusts invocation, prose precedence, five-table pin scope, README BR-05 gitignore contradiction in S2's file, C2 verdicts with their seats).**
