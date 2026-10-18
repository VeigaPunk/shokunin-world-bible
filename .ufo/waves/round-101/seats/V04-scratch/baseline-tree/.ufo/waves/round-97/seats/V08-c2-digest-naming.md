# V08 — c2-digest-naming (round 97)

- Seat: V08 `c2-digest-naming`. Scope per seat spec: poll for R3, then (a) tamper one file in an
  r95 scratch copy → `DIGEST-MISMATCH` names the changed file (quoted); (b) confirm all four pins
  name paths.
- Leaf seat: no nested agents, no commits, no pushes, no network. Writes: this report plus
  `.ufo/waves/round-97/seats/V08-c2-digest-naming.scratch/` only (absolute paths under the lane
  repo). The real corpus was never written; all mutations ran in scratch copies (write audit §7).
- Lane repo `/home/vgpnk/Projects/shokunin/lore-shokunin`; declared baseline r96 closure `f3e09f9`
  (HEAD `2393934`, differs by `SCORECARD.md` only: `git diff --stat f3e09f9 HEAD` → 1 file, +31).
  All commands from the repo root with `python3`.
- No artifact was verified from a plan. The only pre-R3 runs below are explicitly labelled
  **baselines on the r96 revision** (pre-hardening), never reported as verification of r97 work.

## 0. Poll-wait result

R3 target: `corpus/tools/dependency_freeze.py` + `corpus/tools/dependency-freeze-contract.json`
and report `.ufo/waves/round-97/seats/R3-*.md`. Poll started 18:43:23, 20 s cadence.

- R3-scratch first appeared 18:54 (active work); R4/R5/R6 reports landed 18:50–18:53; R3's
  `R3-freeze-hardening.md` landed at **18:56:23.55** (13017 B) — found by the detached poll on its
  final try (40/40), no ABSENT cutoff reached.
- Stability gate (30 s + 15 s re-check): `POLL_STABLE`, both artifacts byte-identical across the
  gate; frozen revision recorded twice independently (18:56–18:57 and post-run):

```
$ sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json
b06275f3bbdeabaab615138b3004703fce701a786af882d3b732828b37722130  corpus/tools/dependency_freeze.py
27273be27d33ad864f06d656f28dca8eabc9d76f6ebe62583372a88c9e64e781  corpus/tools/dependency-freeze-contract.json
$ stat -c "%y %s %n" …
2026-10-17 18:53:00 25044 corpus/tools/dependency_freeze.py
2026-10-17 18:55:14 12025 corpus/tools/dependency-freeze-contract.json
```

All results below are on this frozen revision; hashes re-checked unchanged after my full run.

## 1. Pre-r97 baselines (r96 revision, `a3b57978…` tool / `7d568cc4…` contract — context only)

The two C2 hazards, reproduced on the r96 bytes for a clean before/after:

- Foreign-path same-named pristine copy of r95 verified **identically** (the C2(b) hazard):
  `python3 corpus/tools/dependency_freeze.py <scratch>/foreign/r95-crossing-aftermath` →
  `RESULT PASS` / `EXIT=0`.
- Mirror tamper of `sources.json` (one char) → exit 2 but the finding did **not** name the file:
  `FINDING DIGEST-MISMATCH: content digest f024ac81… != pin d541ae64…; fixture bytes changed
  outside the frozen inventory`.

## 2. Check (b) — all four pins name paths (PASS)

`python3 .ufo/…/V08-c2-digest-naming.scratch/check_pins.py`:

```
pin count: 4
pin 'r88-m3-maya-cluster': fixture='corpus/fixtures/r88-m3-maya-cluster' path_named=True revision='60dba0c2…' digest=15ef230e…
pin 'r94-paired-crossing': fixture='corpus/fixtures/r94-paired-crossing' path_named=True revision='60dba0c2…' digest=2527beb9…
pin 'r95-crossing-aftermath': fixture='corpus/fixtures/r95-crossing-aftermath' path_named=True revision='60dba0c2…' digest=d541ae64…
pin 'r96-crossing-response': fixture='corpus/fixtures/r96-crossing-response' path_named=True revision='2393934237ea076366f3db6dceeff033edb52ab1' digest=d422a9b3…
ALL_FOUR_NAME_PATHS
keys match: True
```

Exactly the four declared chain fixtures, each `fixture` = `corpus/fixtures/<name>`. The r96 pin is
the only refreshed one (`revision` → `2393934…` = HEAD at refresh; `content_sha256` unchanged
`d422a9b3…`), matching R3 §"Pin refresh" and corroborating its recorded claim discrepancy (the
declaration's "digest changes by the repair" is inaccurate — the repair touched
`claim-excerpt-map.md`, outside `DATA_FILES`). Path naming is load-bearing at read time too:
`validate_pin` (tool lines 259–267) rejects a missing/absolute/out-of-scope `fixture` with
`CONTRACT-INVALID`.

## 3. Check (a) — tamper in an r95 scratch copy → DIGEST-MISMATCH names the changed file (PASS)

Method: workspace mirror (`scratch/ws/`) holding byte copies of the frozen tool + contract at
`corpus/tools/` and a fresh copy of the real r95 fixture at `corpus/fixtures/r95-crossing-aftermath`
— the pinned repo-relative path inside that mirror root, which is the only path the delivered
binding accepts (R3 mirror-root note). Mirror copies confirmed byte-identical to the frozen
revision (`b06275f3…` / `27273be2…`, §0). Clean control first: pristine mirror copy → `RESULT
PASS` / `EXIT=0`.

**T1 — one character in `sources.json` (`note` → `Note`), inventory-neutral:**

```
$ python3 <mirror>/corpus/tools/dependency_freeze.py <mirror>/corpus/fixtures/r95-crossing-aftermath
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
FINDING DIGEST-MISMATCH: content digest f024ac819cfbc7cae8e2571973d8bb63acd6395056532bed88225af23e17922b != pin d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9; changed: sources.json (sha256 fd9e30e8d9ad40013be2172781d13d84ba219377c8433ff6e529ea8e1927e64a -> 08cf9041be456f373d967be29c5f54f35ffce626574b892fc8b0b968b6997849); fixture bytes changed outside the frozen inventory
RESULT ERROR
EXIT=2
```

**T2 — description-only edit in `timeline.json` (`south bell at Salt Court` → `South …`; edges and
endpoints untouched):**

```
FINDING DIGEST-MISMATCH: content digest 871a3981bf58cca98cc034f5f6aeee8fe39643c16d9c9ab70929b49d13bcd835 != pin d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9; changed: timeline.json (sha256 3c0faad6bf32f944f9f2a20f3bd15829044afa04f1a8837601903433b00ea177 -> 05b3b532ed63f16748ff9bcab0397b6517819fe54e884e868bb99886ad68c296); fixture bytes changed outside the frozen inventory
RESULT ERROR
EXIT=2
```

**T3 — two files at once (`sources.json` + `entities.json`): both named, sorted:**

```
FINDING DIGEST-MISMATCH: content digest 39bffb8f… != pin d541ae64…; changed: entities.json (sha256 026af0bc… -> 70919512…), sources.json (sha256 fd9e30e8… -> 08cf9041…); fixture bytes changed outside the frozen inventory
RESULT ERROR
EXIT=2
```

Mechanical exactness check (`verify_naming.py`, fresh copies per case): for every named entry,
`before == pin.files[file]` and `after == actual sha256 of the tampered file`, and the named set
equals the tampered set exactly —

```
T1: named ['sources.json'] | exact_match=True | before==pin_hash=True after==actual_file_hash=True
T2: named ['timeline.json'] | exact_match=True | before==pin_hash=True after==actual_file_hash=True
T3: named ['entities.json','sources.json'] | exact_match=True | before==pin_hash=True after==actual_file_hash=True
```

Edge probe beyond the seat ask: deleting the non-required `entities.json` names it with
`-> None` (`changed: entities.json (sha256 026af0bc… -> None)`, exit 2) — added/removed files are
covered by `changed_files`' union, tool lines 308–317.

**Foreign-path same-named copy on the delivered tool (C2(b) closure, sanity):**

```
$ python3 corpus/tools/dependency_freeze.py .ufo/waves/round-97/seats/V08-c2-digest-naming.scratch/foreign/r95-crossing-aftermath
FINDING PATH-MISMATCH: pin r95-crossing-aftermath names corpus/fixtures/r95-crossing-aftermath (resolves to /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r95-crossing-aftermath); invoked fixture resolves to /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-97/seats/V08-c2-digest-naming.scratch/foreign/r95-crossing-aftermath
RESULT ERROR
EXIT=2
```

(`bind_path`, tool lines 290–296: observed fixture must resolve exactly to `ROOT/pin["fixture"]`.)

## 4. Supporting receipts on the frozen revision

- `--self-test` → all 16 cases `ok`, `SELF-TEST 16/16`, `RESULT PASS`, exit 0 (including
  `scope_refused` → `SCOPE-REFUSED` and `path_mismatch` → `PATH-MISMATCH`, and the legacy
  `digest_tamper` → `DIGEST-MISMATCH` case).
- Chain 4/4 clean, exit 0 each: r88 `15ef230e…`, r94 `2527beb9…`, r95 `d541ae64…`,
  r96 `d422a9b3…` — r96's receipt unchanged by R4's cosmetic repair (JSON tables only).
- Real r95 fixture re-verified clean after all mirror work (`RESULT PASS` exit 0); real
  `r95/r96` `sources.json`/`timeline.json` hashes equal the pinned values (`fd9e30e8…`,
  `3c0faad6…`, `9f973f63…`, `ea0225f9…`).
- `ls -d dependency-freeze-self-test-*` → `No such file or directory` (no stray scratch).

## 5. Write audit

```
$ git status --short
 M LOG.md
 M corpus/fixtures/r96-crossing-response/claim-excerpt-map.md   # R4
 M corpus/tools/README.md                                       # R2
 M corpus/tools/dependency-freeze-contract.json                 # R3
 M corpus/tools/dependency_freeze.py                            # R3
 M corpus/tools/map-obligations-contract.json                   # R2
 M corpus/tools/map_obligations.py                              # R1
?? .ufo/waves/round-97/
?? corpus/fixtures/r97-crossing-acknowledgment/                 # R4/R5
?? corpus/knowledge/r97-acknowledgment-scope-note.md            # R6
```

Tool/contract sha256 unchanged across my entire run (§0 values); my writes confined to this
report + `V08-c2-digest-naming.scratch/` (poll.sh, poll.log, harness.sh, check_pins.py,
verify_naming.py, logs/, ws/, ws-probe/, foreign/).

## 6. Findings and residuals (reported, not concealed)

1. **Doc-parity gap (not V08's to fix; R2-owned README).** `corpus/tools/README.md:175`
   (mtime 18:47, before the 18:53/18:55 tool/contract) still describes `dependency_freeze` with
   self-test "14/14" and lists the three r96 hazards as open ("`--freeze` … has no scope guard;
   receipts are not path-bound …; `DIGEST-MISMATCH` does not name the changed file") — all three
   are closed by the delivered revision per §2–§4. R3's residual #1 is accurate and still open at
   my end; material for adjudication, no effect on this seat's verdict.
2. **R3's recorded discrepancy corroborated.** The C2 claim's parenthetical that the r96 digest
   changed by the repair is inaccurate; measured `d422a9b3…` unchanged (§2), consistent with R4's
   repair touching only `claim-excerpt-map.md` (outside `DATA_FILES`).
3. `r97-crossing-acknowledgment` is deliberately unpinned (`UNPINNED-FIXTURE` by design, R3
   residual #2) — outside my seat's four-pin scope.

## Bottom line

PASS — on the frozen R3 revision (`dependency_freeze.py` `b06275f3…`, contract `27273be2…`, R3
report present at 18:56:23, artifacts stable across the gate): all four pins name repo-relative
paths (r96's refresh digest-unchanged), a same-named foreign-path copy exits 2 `PATH-MISMATCH`,
and in an r95 scratch mirror a one-file tamper (sources.json), a description-only timeline edit,
and a two-file tamper each exit 2 with `DIGEST-MISMATCH` naming exactly the changed file(s) —
before-hash equal to the pin, after-hash equal to the actual tampered bytes; self-test 16/16,
chain 4/4 clean; sole residual is the R2-owned stale README paragraph.
