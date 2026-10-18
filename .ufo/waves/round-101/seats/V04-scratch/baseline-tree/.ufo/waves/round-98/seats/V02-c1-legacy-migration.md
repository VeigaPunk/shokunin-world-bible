# V02 c1-legacy-migration — round 98

- Seat: V02 c1-legacy-migration (verifier, C1(b) half). Lane repo
  `/home/vgpnk/Projects/shokunin/lore-shokunin`; baseline r97 closure `9a3d648`;
  HEAD during the round `dd4df1b36a64b513e75b46da04ee2f3f7f3eb6cb` (wave tree
  uncommitted). All commands from the lane root with `python3`.
- Verified against the delivered bytes (== S1's declared hashes in
  `S1-freeze-hygiene.md`):
  - `corpus/tools/dependency_freeze.py`
    sha256 `03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b`
  - `corpus/tools/dependency-freeze-contract.json`
    sha256 `153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947`
  - Re-checked after the final matrix re-run: both hashes unchanged.
- Scratch (declared): `.ufo/waves/round-98/seats/scratch/V02/` and
  `.ufo/waves/round-98/seats/scratch/V02-poll.sh`, plus this report. Leaf seat:
  no nested agents, no commits, no pushes, no network. Nothing outside those
  paths written.

## 0. Poll record (20 s cadence, 40 tries max; never verify a plan)

```
try 1  23:28:58 changed=[] report=[none]
…
try 7  23:30:58 changed=[] report=[none]
try 8  23:31:18 changed=[corpus/tools/dependency-freeze-contract.json corpus/tools/dependency_freeze.py] report=[none]
…
try 21 23:35:38 changed=[…] report=…/.ufo/waves/round-98/seats/S1-freeze-hygiene.md
```

S1 artifact bytes landed at try 8 (23:31:18); S1's report at try 21 (23:35:38).
Interim verification began on artifact bytes only (a plan was never verified);
the matrix was re-run against the final bytes after the report landed and the
hashes matched S1's declaration. No all-reports poll was needed; no stall
escape required. One self-inflicted script bug was caught and corrected (first
rebuild script resolved its argv paths against the wrong cwd, so the observed
`exit=2` was Python's "can't open file", not the tool; all quoted results below
come from absolute-path runs).

## 1. Pre-state control (baseline `9a3d648` bytes, reproduced independently)

Scratch root `.ufo/waves/round-98/seats/scratch/V02/pre/` = baseline tool +
r97 contract with the `fixture` key removed from pin `r95-crossing-aftermath`
(the path-less class; pin keys become
`['content_sha256','counts','events','files','relations','revision']`, the
pre-r97 shape documented in r97 `V11-c2-code-review.md` §2.3 D1 and S1's
report §2) + the r95 fixture at its in-scope path.

```
$ python3 pre/corpus/tools/dependency_freeze.py --freeze pre/corpus/fixtures/r95-crossing-aftermath
FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures/r95-crossing-aftermath: pin r95-crossing-aftermath already names None; freezing a same-named path elsewhere would rewrite the delivered pin
RESULT ERROR
exit=2
$ python3 pre/corpus/tools/dependency_freeze.py pre/corpus/fixtures/r95-crossing-aftermath
FINDING CONTRACT-INVALID: pin r95-crossing-aftermath needs a repo-relative fixture path
RESULT ERROR
exit=2
$ sha256sum pre/corpus/tools/dependency-freeze-contract.json   # before and after both runs
5598e9152019aea5bf1eca5b7d8e75b41dd794cd546986259a7de4bf4fbfa310  (unchanged)
```

The "was manual-only" half of the claim is thus reproduced: the only route to
a path-ful pin was a manual contract edit (V11 §2.3 D1). Both refusals leave
the contract byte-identical (no partial write).

## 2. Delivered behavior — legacy pin migrates in place

Case root `.ufo/waves/round-98/seats/scratch/V02/cases/legacy_missing_key/`
(delivered tool + delivered contract copy with the same key removal + fixture
copy). Quoted before/after:

```
pin BEFORE: fixture_key=False keys=['content_sha256','counts','events','files','relations','revision']

$ python3 <case>/corpus/tools/dependency_freeze.py --freeze <case>/corpus/fixtures/r95-crossing-aftermath
MIGRATED r95-crossing-aftermath: path-less legacy pin now names corpus/fixtures/r95-crossing-aftermath
FROZEN r95-crossing-aftermath: events 4; dependency-edges 3; relations 1
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
RESULT PASS
exit=0

pin AFTER: fixture_key=True value='corpus/fixtures/r95-crossing-aftermath'
```

Fresh-process verify after migration:

```
$ python3 <case>/corpus/tools/dependency_freeze.py <case>/corpus/fixtures/r95-crossing-aftermath
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
RESULT PASS
exit=0
```

Preservation on the same run (parsed comparison of the case contract copy):

```
top-level keys same: True
other pins identical: True            # all other pins, incl. the r97/r98 pins, byte-equal
self_test block identical: True
target pin content fields identical: True   # content_sha256/files/events/relations/counts
```

Migration also holds for the other path-less shapes (delivered bytes):

| variant | recorded `fixture` | observed |
|---|---|---|
| `legacy_missing_key` | (key absent) | `MIGRATED …` → PASS exit 0 |
| `legacy_null` | `null` | `MIGRATED …` → PASS exit 0 |
| `legacy_nonstring` | `123` | `MIGRATED …` → PASS exit 0 |
| `legacy_empty_string` | `""` | `MIGRATED …` → PASS exit 0 |

This matches S1's report §2 ("only the path-less class (absent/`null`/empty
`fixture`) migrates") and extends it with the non-string probe.

## 3. Fail-closed half — un-migratable garbage refused with a named exit-2 finding

A pin whose recorded `fixture` is a non-empty string naming a different path is
un-migratable; `--freeze` refuses with the named finding and the contract is
byte-unchanged (no partial write). Quoted (each run on a fresh case root):

```
$ python3 <case>/corpus/tools/dependency_freeze.py --freeze <case>/corpus/fixtures/r95-crossing-aftermath
# legacy_other_path (recorded 'corpus/fixtures/r96-crossing-response'):
FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures/r95-crossing-aftermath: pin r95-crossing-aftermath already names 'corpus/fixtures/r96-crossing-response'; freezing a same-named path elsewhere would rewrite the delivered pin
RESULT ERROR
exit=2   contract hash unchanged=True

# legacy_out_of_scope_path (recorded 'corpus/knowledge'): same SCOPE-REFUSED shape, exit=2, unchanged=True
# garbage_traversal (recorded '../../outside'):
FINDING SCOPE-REFUSED: --freeze refuses corpus/fixtures/r95-crossing-aftermath: pin r95-crossing-aftermath already names '../../outside'; freezing a same-named path elsewhere would rewrite the delivered pin
RESULT ERROR
exit=2   contract hash unchanged=True
```

`garbage_traversal` is the un-migratable garbage variant of the seat brief: the
recorded value cannot be migrated to the invoked in-scope path, so the tool
fails closed with `SCOPE-REFUSED` (exit 2, could-not-evaluate class) and leaves
the contract untouched. Two additional probes:

- equivalent-but-differently-spelled recorded paths (`./corpus/fixtures/r95-crossing-aftermath`,
  `/corpus/fixtures/r95-crossing-aftermath`) → `SCOPE-REFUSED` exit 2, unchanged
  (the comparison is string-exact on the repo-relative label — fail-closed bound).
- path-less pin + `--freeze` target outside `corpus/fixtures/**` →
  `SCOPE-REFUSED` ("the frozen scope is corpus/fixtures/**"), exit 2, unchanged —
  the scope guard still runs first; migration does not weaken it.

Un-migrated path-less pins stay refused at verify time (unchanged fail-closed
inherited behavior):

```
$ python3 <case>/corpus/tools/dependency_freeze.py <case>/corpus/fixtures/r95-crossing-aftermath
FINDING CONTRACT-INVALID: pin r95-crossing-aftermath needs a repo-relative fixture path
RESULT ERROR
exit=2
```

Bounded observation (inherited, not a regression): a pin whose value is not a
dict at all (e.g. `"garbage-not-an-object"`) is silently replaced by a valid pin
(`FROZEN … RESULT PASS`, exit 0, no `MIGRATED` line). The r97 baseline behaved
the same way (`isinstance(existing, dict)` was already the gate), there is no
recorded path to rewrite, and the write remains scope-guarded; recorded as a
bound, not a defect.

## 4. Adjacent sanity checks (not my claim, cheap corroboration)

- `--self-test` on the delivered bytes (run from a scratch root so the temp dir
  lands there, not at the repo root): `SELF-TEST 17/17`, `RESULT PASS`, exit 0;
  all 16 inherited cases print `ok`; the new `self_test_mismatch` case exits 2
  with `SELF-TEST-MISMATCH`. Contract `self_test.expected` has exactly 17 keys
  including `self_test_mismatch`.
- Delivered contract `precedence` text (C1(c), read-only cross-check) ends with
  "A path-less legacy pin is migrated in place by --freeze instead of refused."
  and names the exit-2 order/ids.

## 5. Write audit

- My writes: `V02-poll.sh`, `build_cases.py`, `drive.py`, `matrix.py`, `cases/`,
  `pre/`, `post/`, `garbage/`, `self_test_root/`, `matrix-run-*.log`,
  `final-matrix.log` (all under `.ufo/waves/round-98/seats/scratch/V02*`) and
  this report. No files at the lane root, no self-test temp at the repo root
  (`ls -d dependency-freeze-self-test-*` → none), no tracked file touched.
- `git status --porcelain` tracked modifications are exactly the producers'
  declared paths (S1's two tool files, S2 README, S3 r95 map repair, S5 notes,
  `LOG.md`); `git diff 9a3d648 -- corpus/tools/` lists only S1's two files.

## Bottom line

**PASS** — on the delivered revision (tool `03d04365…`, contract `153ebc5b…`,
matching S1's declared hashes) a simulated r96-style path-less pin (missing key,
`null`, non-string, empty string) is migrated in place by `--freeze` (`MIGRATED
…` → `FROZEN` → `RESULT PASS`, exit 0) with the path recorded and all other pins,
top-level keys, `self_test`, and the target pin's content fields unchanged; the
un-migratable garbage variant (recorded `'../../outside'`, as well as any other
different non-empty path) fails closed with the named `SCOPE-REFUSED` exit-2
finding and a byte-unchanged contract; the r97 baseline's `already names None`
refusal and `CONTRACT-INVALID` verify refusal are reproduced as the closed
pre-state.
