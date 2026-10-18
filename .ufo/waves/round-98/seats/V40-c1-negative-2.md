# V40 c1-negative-2 — round 98

- Seat: V40 c1-negative-2 (verifier, read-only on lane bytes; leaf seat). Lane
  repo `/home/vgpnk/Projects/shokunin/lore-shokunin`; all commands run from the
  lane root (or the seat scratch) with `python3`. Baseline r97 closure `9a3d648`
  (pre-round bytes via `git show 9a3d648:<path>`); wave tree uncommitted; HEAD
  during the round `dd4df1b36a64b513e75b46da04ee2f3f7f3eb6cb`. No commits, no
  pushes, no network, no nested agents.
- Revision verified (equal to S1's own report and to V04's):
  `corpus/tools/dependency_freeze.py` sha256
  `03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b`;
  `corpus/tools/dependency-freeze-contract.json` sha256
  `153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947`.
- Writes: this report (absolute path) and declared scratch
  `.ufo/waves/round-98/scratch/V40/` (mirrors, scripts, logs). Two throwaway
  snapshots also landed in `/tmp` (`df_9a3d648.py`, `ct_now.json`, `ct_c435.json`)
  — outside the lane tree; no lane file was written by this seat, and the
  delivered tool/contract shas were `03d04365…`/`153ebc5b…` before and after
  every probe.

## 0. Poll-wait record (20 s cadence, 40 tries; never verify a plan)

Poller `scratch/V40/poll.sh` (tool+contract sha vs baseline, plus an `S1-*.md`
report in the seats dir; then a 3-consecutive combined-sha stability gate), log
`scratch/V40/poll.log`:

```
try=4  t=20:31:05 report=none tool=same    contract=same
try=5  t=20:31:25 report=none tool=changed contract=changed     # C1 tool landed
try=9  t=20:32:45 report=none tool=changed contract=changed     # C2 pins landed (contract c435239d…)
try=16 t=20:35:12 report=none tool=changed contract=changed
try=17 t=20:35:25 report=.ufo/waves/round-98/seats/S1-freeze-hygiene.md tool=changed contract=changed
STAB i=1 sha=3be4a9f1… stable=0
STAB i=3 sha=3be4a9f1… stable=2
POLL_HIT try=17 report=.ufo/waves/round-98/seats/S1-freeze-hygiene.md tool=03d04365… contract=153ebc5b…
POLL_STABLE sha=3be4a9f15b385bf7c1257a771be127250b2926e6ce1e64ad194c1aeab639f4b6
```

The contract moved `3a940a9f…` → `c435239d…` → `153ebc5b…` while polling; no
final run was taken before the report existed and the combined sha was stable for
three consecutive checks (~60 s). One stray `nohup` copy of my own poller was
started early and killed (it double-logged tries 2–4); the background-task
poller above is the only one that ran to completion. No all-reports poll was
needed (my dependency was S1 alone); no stall escape required.

## 1. Method

Independent mirror harness (not shared with S1/V04): `build-mirror.sh` copies the
delivered tool+contract and the six chain fixtures into `scratch/V40/post/`;
`post-neg.sh` runs the matrix with every contract mutation applied only to the
mirror copy. Pre-state runs use `scratch/V40/pre/` built from `git show 9a3d648:`
bytes. Every row below was re-run twice on the final revision; the two full-run
logs are byte-identical:

```
$ diff <(grep -vE '^$' exploratory3.log) <(grep -vE '^$' final.log)
exploratory3 vs final: IDENTICAL
```

## 2. Pre-state negatives (baseline `b06275f3…`/`27273be2…`)

```
### pre-a: SELF-TEST-MISMATCH exit (self_test.expected.clean.exit:=1)
SELF-TEST 15/16
FINDING SELF-TEST-MISMATCH: cases failed: ['clean']
RESULT FAIL
EXIT=1

### pre-b: path-less legacy pin under --freeze
FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures/r95-crossing-aftermath: pin r95-crossing-aftermath already names None; freezing a same-named path elsewhere would rewrite the delivered pin
RESULT ERROR
EXIT=2

### pre-b2: path-less legacy pin under verify
FINDING CONTRACT-INVALID: pin r95-crossing-aftermath needs a repo-relative fixture path
RESULT ERROR
EXIT=2

### pre-c: precedence text
semantic inventory findings decide first (exit 1); a content digest change the frozen inventory does not model exits 2
```

All three declared pre-states reproduce exactly (exit 1; `…already names None`;
the precedence text lacking the exit-2 order/IDs). Baseline self-test on
untouched bytes: `SELF-TEST 16/16 / RESULT PASS / EXIT=0`.

## 3. Post-state matrix on the delivered revision

`SELF-TEST 17/17 / RESULT PASS / EXIT=0` and the full chain on the delivered
tree; each row below is the mirror mutation, observed finding(s), and exit:

**Mismatch class (C1a)**

```
### P1a: self_test.expected.clean.exit:=1
SELF-TEST 16/17
FINDING SELF-TEST-MISMATCH: cases failed: ['clean']
RESULT ERROR            EXIT=2
### P1b: self_test.expected.digest_tamper.finding_ids:=[]
SELF-TEST 16/17
FINDING SELF-TEST-MISMATCH: cases failed: ['digest_tamper']
RESULT ERROR            EXIT=2
### P1c: expected-set mismatch (delete clean key)
FINDING CONTRACT-INVALID: self-test expectation set mismatch; missing=['clean'] extra=[]
RESULT ERROR            EXIT=2
```

The finding ID and message shape are unchanged from baseline; only the class
moved 1 → 2, and case 17 pins it.

**Migration class (C1b)**

```
### P2a: path-less pin (key removed) + --freeze canonical r95
MIGRATED r95-crossing-aftermath: path-less legacy pin now names corpus/fixtures/r95-crossing-aftermath
FROZEN r95-crossing-aftermath: events 4; dependency-edges 3; relations 1
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
RESULT PASS             EXIT=0
### P2b: migrated pin payload vs base pin (minus revision)
fixture key: corpus/fixtures/r95-crossing-aftermath
content_sha256: EQUAL  files: EQUAL  events: EQUAL  relations: EQUAL  counts: EQUAL
revision: 60dba0c2aa344860b10a2fc63e00468d1b134f27 -> dd4df1b36a64b513e75b46da04ee2f3f7f3eb6cb
### P2c: verify canonical r95 after migration -> RESULT PASS EXIT=0
### P2d: path-less variants fixture=null / fixture='' both
MIGRATED r95-crossing-aftermath: path-less legacy pin now names corpus/fixtures/r95-crossing-aftermath
RESULT PASS             EXIT=0   (pin fixture now: 'corpus/fixtures/r95-crossing-aftermath')
```

**Guard class**

```
### P3a: --freeze out-of-scope target
FINDING SCOPE-REFUSED: --freeze refuses post/target (resolves to …/scratch/V40/post/target); the frozen scope is corpus/fixtures/** (integration-time operation only)
RESULT ERROR            EXIT=2
### P3b: --freeze in-scope foreign same-named path, pin WITH recorded path (r95)
FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures/nested/r95-crossing-aftermath: pin r95-crossing-aftermath already names 'corpus/fixtures/r95-crossing-aftermath'; freezing a same-named path elsewhere would rewrite the delivered pin
RESULT ERROR            EXIT=2
### P3d: same for the NEW pin r98 -> same SCOPE-REFUSED class, EXIT=2
### path-less pin + out-of-scope target -> SCOPE-REFUSED EXIT=2, contract unchanged=yes
### P3c: --freeze in-scope foreign same-named path with a PATH-LESS pin [hole probe]
RESULT PASS             EXIT=0
pin fixture now: corpus/fixtures/nested/r95-crossing-aftermath
```

**Path class**

```
### P4a: verify foreign same-named copy (pin WITH path)
FINDING PATH-MISMATCH: pin r95-crossing-aftermath names corpus/fixtures/r95-crossing-aftermath (resolves to …/post/corpus/fixtures/r95-crossing-aftermath); invoked fixture resolves to …/post/foreign/r95-crossing-aftermath
RESULT ERROR            EXIT=2
### P4b: verify canonical r95 -> RESULT PASS EXIT=0
```

**Tamper class**

```
### P5a: cosmetic change r95 timeline.json ("north"->"North")
FINDING DIGEST-MISMATCH: content digest 7e2cce95… != pin d541ae64…; changed: timeline.json (sha256 3c0faad6… -> 367ac00f…); fixture bytes changed outside the frozen inventory
RESULT ERROR            EXIT=2
### P5b: drop r97 tick-13 edge (acknowledgment-aru-records -/-> response-evin-salt-court)
FINDING REDUCTION-DETECTED: event acknowledgment-aru-records lost depends_on ['response-evin-salt-court']
RESULT FAIL             EXIT=1
### P5c: drop r98 tick-14 edge (clerk-filing-open -/-> acknowledgment-aru-records)
FINDING REDUCTION-DETECTED: event clerk-filing-open lost depends_on ['acknowledgment-aru-records']
RESULT FAIL             EXIT=1
```

**Chain (P7)** — all six pins verify clean, exit 0, digests
`15ef230e… / 2527beb9… / d541ae64… / d422a9b3… / 3c922d20a01bbd3f7941ed64f5c8796a619699197ae89fb10fca317cf83abea6 / 59a0f4fa3d4a47e03649a54d1815c45ee1eef641b63a59ebe7210bc9d9b9b133`.

The V46-discharge provenance claim was cross-checked against S1's own scratch
bytes, not just the receipt text:

```
$ sha256sum .ufo/waves/round-98/seats/S1-scratch/r97-depdropped/timeline.json
37a425b97af658d71b8dc8904f43fd75859905bac326489a71adb67004004eb1   # equals the sha the contract provenance cites
$ diff delivered-r97-timeline  S1-scratch/r97-depdropped/timeline.json
59,61c59
<     "depends_on": ["response-evin-salt-court"]
---
>     "depends_on": [],
```

## 4. Byte-level invariants (C1 "must be unchanged")

```
inherited self_test expectations JSON-equal: True   (new-only key: self_test_mismatch; removed: [])
exit_codes equal: True  {'0': 'PASS', '1': 'FAIL', '2': 'ERROR'}
base_fixture unchanged: r95-crossing-aftermath
data_files / required_files / schema_version / scope: unchanged
inherited pin r88/r94/r95/r96: IDENTICAL to baseline contract pins
new pins: r97 (rev dd4df1b36a64, digest 3c922d20…, counts 6/5/1/5/6), r98 (rev dd4df1b36a64, digest 59a0f4fa…, counts 7/6/1/6/7)
contract c435239d… -> 153ebc5b… delta: provenance_note only (pins equal: True; revision unchanged)
```

## 5. Adversarial probes beyond S1's receipts

1. **Neutralization — the 17th case is load-bearing.** Patching the mirror tool
   `emit(2, [("SELF-TEST-MISMATCH"…)])`/`return 2` back to `emit(1…)`/`return 1`:

   ```
   CASE self_test_mismatch: exit=1 expected=2 findings=['SELF-TEST-MISMATCH'] MISMATCH
   SELF-TEST 16/17
   FINDING SELF-TEST-MISMATCH: cases failed: ['self_test_mismatch']
   RESULT FAIL             NEUTRALIZED_EXIT=1
   ```

   The persisted case detects the regression it exists to pin (no vacuous pass).
2. **Self-consistency — corrupting the new case's own expectation** (`self_test_mismatch.exit:=1`)
   → outer run `SELF-TEST 16/17`, `cases failed: ['self_test_mismatch']`,
   `RESULT ERROR` exit 2.
3. **Determinism** — three full `--self-test` runs on the delivered mirror:
   `run1/2/3 exit=0 sha=f2c5c7ba38fb5463` (identical logs).
4. **Fresh-freeze silence** — freezing an unpinned copy emits 0 `MIGRATED` lines
   (the marker is migration-only, not a generic freeze message).
5. **Full-run reproducibility** — exploratory3 vs final logs identical (§1).

## 6. ID comparison with V04 (`V04-c1-regression.md`, same revision shas)

| class | V40 observed | V04 observed | agree |
|---|---|---|---|
| SELF-TEST-MISMATCH | exit 1 → 2, ID/message unchanged | exit 1 → 2, same | yes |
| CONTRACT-INVALID (strict loader) | `missing=['clean'] extra=[]` exit 2 | same text, exit 2 | yes |
| MIGRATED / path-less freeze | `MIGRATED …` + PASS exit 0 | same text, exit 0 | yes |
| SCOPE-REFUSED (out of scope / foreign same-name, r95+r98) | exit 2, both | exit 2, both | yes |
| PATH-MISMATCH (foreign copy) | r95 exit 2 | r95 + r98 exit 2 | yes |
| REDUCTION-DETECTED (semantic tamper) | r95 baseline edge, r97 tick-13, r98 tick-14 → exit 1 | r95 edge + r97/r98 stripped edges → exit 1 | yes |
| DIGEST-MISMATCH (cosmetic tamper) | names timeline.json, exit 2 | names timeline.json, exit 2 | yes |
| 17/17 + 6/6 chain digests | same six digests | same six digests | yes |
| 14-ID inventory vs precedence text | all named | all named (same 14) | yes |

Differences are coverage, not contradiction: V04 additionally ran the ambient
env-marker probe (§8.1 below, independently reproduced here) and verify-side
foreign copies for r98; V40 additionally ran the neutralization/self-consistency
probes, the null/empty path-less variants, determinism, and the V46-mutation-sha
cross-check. No ID or exit-code disagreement anywhere.

## 7. Bounds (recorded, none harmful to a C1 axis)

1. **Path-less migration adopts the invoked in-scope path** (P3c): with a
   path-less pin, `--freeze` on `corpus/fixtures/nested/r95-crossing-aftermath`
   migrates the pin to that foreign path (exit 0, `MIGRATED` printed). This is
   the declared C1(b) semantics (no recorded path exists to preserve) and stays
   inside `corpus/fixtures/**`; but the tool docstring's "(the same-named-elsewhere
   refusal stays)" holds only for pins that already record a path. Low severity;
   worth one clause in the closure docs if the wording is touched again.
2. **Ambient env-marker sensitivity** (V04 §8.1, reproduced):
   `DEPENDENCY_FREEZE_SELF_TEST_CHILD=1 python3 … --self-test` →
   `CASE self_test_mismatch: exit=2 expected=2 findings=['FIXTURE-MISSING'] MISMATCH`,
   `SELF-TEST 16/17`, `FINDING SELF-TEST-MISMATCH`, exit 2. Fails closed; verify
   is unaffected (`DEPENDENCY_FREEZE_SELF_TEST_CHILD=1 … verify r95` → PASS
   exit 0); nothing in the lane sets the variable.
3. **Order-text nuance** (C1c): the precedence sentence's list places
   `INVALID-ARGUMENTS` after `DIGEST-MISMATCH`, while CLI-usage errors are
   checked pre-dispatch. Completeness (all 14 IDs, exit-1 clause) holds; only the
   strict first-failure ordering of that one pre-dispatch check is loose.
4. Inherited bounds unchanged: pins cover the five JSON tables only (fixture
   Markdown unpinned); `--self-test` scratch stays at the repo root under the
   gitignored `*-self-test-*/` pattern.

## 8. Write audit

`git status --porcelain` (10 entries) shows only producer-owned paths plus
`.ufo/waves/round-98/`; `git diff 9a3d648 -- corpus/tools/` lists only the two
S1-owned files. All matrix mutations were applied to mirror copies under
`scratch/V40/`; the delivered tool/contract shas were `03d04365…`/`153ebc5b…`
before and after every run. Not mine, recorded: the parent-tree stray
`/home/vgpnk/Projects/shokunin/baseline-analyze.txt` (105 bytes, 20:30; content
`python3: can't open file '/home/vgpnk/Projects/shokunin/analyze.py'` — the
r94-F01 stray-write class, unattributed; also noted by S3 and V04).

## Bottom line

**PASS** — on the delivered revision (`03d04365…`/`153ebc5b…`) the independent
mismatch/migration/guard/path/tamper matrix reproduces every declared C1
behavior (SELF-TEST-MISMATCH exit 1 → 2 pinned by load-bearing case 17; path-less
legacy pin migrated by `--freeze` with payload intact and the path-bearing
refusal retained; precedence text naming all 14 finding IDs), the 16 inherited
cases and four inherited pins are byte-identical, the chain verifies 6/6, and
V04's IDs agree class-for-class — with two recorded low-severity bounds (path-less
migration adopts the invoked in-scope path; ambient env-marker fails the
self-test closed).
