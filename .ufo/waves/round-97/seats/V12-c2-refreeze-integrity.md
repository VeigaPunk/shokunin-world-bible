# V12 — c2-refreeze-integrity (round 97)

Seat: V12 `c2-refreeze-integrity`. Lane repo `/home/vgpnk/Projects/shokunin/lore-shokunin`
(session cwd is the parent repo; every path below is repo-relative and every write is under
`.ufo/waves/round-97/seats/V12-scratch/` plus this report). Baseline `f3e09f9`.
Claim under test: the r96 re-freeze (C2) changed **only** the r96 pin entry, and the r96 pin now
pins the **post-repair map digest** + **unchanged JSON digests** (JSON files unchanged vs `f3e09f9`).

Delivered artifacts measured (stable across a 25 s re-check, then again at 18:59):

```
27273be27d33ad864f06d656f28dca8eabc9d76f6ebe62583372a88c9e64e781  corpus/tools/dependency-freeze-contract.json   (mtime 18:55:14)
b06275f3bbdeabaab615138b3004703fce701a786af882d3b732828b37722130  corpus/tools/dependency_freeze.py             (mtime 18:53:00)
e851f068cfd7ed02c97054df18729c4c5a9b8bf60d99d7c9116f427d765440de  corpus/fixtures/r96-crossing-response/claim-excerpt-map.md (post-repair, mtime 18:43:42)
```

Baseline snapshots kept in scratch: `contract-baseline.json` (f3e09f9, sha256 `c65ac3bd…`),
`r96-map-baseline.md` (`5093d72e…`), `r96-{entities,relations,contradictions,sources,timeline}-baseline.json`.
R3's own pre-freeze snapshot (`R3-scratch/contract-prefreeze.json`) was used as the intermediate state.

## 1. The re-freeze changed only the r96 pin entry — CONFIRMED

Structural leaf diff (scratch `diff_contracts.py`) baseline `f3e09f9` → delivered:

```
$ python3 .ufo/.../V12-scratch/diff_contracts.py V12-scratch/contract-baseline.json V12-scratch/contract-final.json
.pins.r96-crossing-response.revision   '60dba0c2…' -> '2393934237ea…'
.provenance_note                       (text edit: r97 hardening paragraph)
.revision                              '60dba0c2…' -> '2393934237ea…'
.scope                                 (text edit: scope-guard/PATH-MISMATCH sentence)
.self_test.expected.path_mismatch      <absent> -> {'exit': 2, 'finding_ids': ['PATH-MISMATCH'], 'forbid_traceback': True}
.self_test.expected.scope_refused      <absent> -> {'exit': 2, 'finding_ids': ['SCOPE-REFUSED'], 'forbid_traceback': True}
TOTAL leaf diffs: 6
```

Only two of the six are freeze outputs (`.pins.r96-crossing-response.revision` and top-level
`.revision`, both `60dba0c2aa344860b10a2fc63e00468d1b134f27` → `2393934237ea076366f3db6dceeff033edb52ab1`
= current HEAD, `git rev-parse HEAD` → `2393934237ea076366f3db6dceeff033edb52ab1`). The other four are
R3's hardening edits (two text fields + two self-test expectations). **No other pin entry changed at all:**

```
r88-m3-maya-cluster identical: True
r94-paired-crossing identical: True
r95-crossing-aftermath identical: True
```

R3's pre-freeze snapshot → delivered (isolating the freeze step):

```
$ python3 diff_contracts.py R3-scratch/contract-prefreeze.json V12-scratch/contract-final.json
.pins.r96-crossing-response.revision   '60dba0c2…' -> '2393934237ea…'
.provenance_note                       (text)
.revision                              '60dba0c2…' -> '2393934237ea…'
.scope                                 (text)
TOTAL leaf diffs: 4
```

(`prefreeze` vs baseline differs only by the two new self-test expectations — `TOTAL leaf diffs: 2` —
so the snapshot is a legitimate post-hardening, pre-freeze state.) Inside the r96 pin only `revision`
moved: `files`, `events`, `relations`, `counts`, `fixture`, `content_sha256` are byte-identical to baseline.

Independent reproduction (`V12-scratch/refreeze_harness.py`: copy of the delivered tool with
`ROOT`/`CONTRACT_PATH` repointed to a scratch contract, never touching the delivered file):
fresh guarded `--freeze` of every pinned fixture yields

```
r96-crossing-response: identical=True          # byte-identical to the delivered pin, incl. revision 2393934
r88/r94/r95:           identical=False, differs [revision] only (historical 60dba0c2 vs current HEAD)
```

i.e. the delivered r96 pin is exactly what the guarded `--freeze` path produces on the post-repair
fixture, and the other three pins' digests/inventories are exactly what a fresh freeze computes
(no stale or hand-mutated values); only r96 was re-frozen.

## 2. "The r96 pin now pins the post-repair map digest" — NOT SATISFIED

- The pin's digest coverage is the five JSON data files only: `DATA_FILES` in the delivered tool is
  unchanged (`dependency_freeze.py:36`) and the pin's key set is unchanged
  (`['content_sha256','counts','events','files','fixture','relations','revision']`).
- The r96 pin's `content_sha256` is **unchanged** by the re-freeze: `d422a9b3d95c4e0b8aac98cc87806a94949896adb962a50d2d55a6c11657d7f6`
  in baseline, pre-freeze snapshot and delivered contract alike. That digest is reproduced by hashing
  the five JSON files, so it cannot encode the map.
- The post-repair map digest appears nowhere in the contract:

```
$ grep -c "e851f068" corpus/tools/dependency-freeze-contract.json   -> 0
$ grep -c "5093d72e" corpus/tools/dependency-freeze-contract.json   -> 0
$ grep -c "claim-excerpt-map" corpus/tools/dependency-freeze-contract.json -> 1   (only inside provenance_note prose)
```

- R3's own report records this as "Pin refresh through the guarded path — measured result (a claim
  discrepancy, recorded exactly)", and the contract's `provenance_note` documents it: the map "is not
  a pinned data file, so the content digest … is unchanged and only the pin revision moved".

Consequence: the r96 pin does not pin the post-repair map digest (it does not pin the map at all);
the map repair is invisible to this pin. The LOG-declared C2 wording ("re-frozen through the guarded
`--freeze` path (pin refresh), demonstrating the guard end-to-end") is satisfied — the refresh ran
through the guarded path after the repair (map mtime 18:43:42 < contract mtime 18:55:14) and is
reproducible — but the seat brief's stronger "pins the post-repair map digest" phrasing fails.

## 3. JSON digests unchanged and byte-identical to f3e09f9 — CONFIRMED

```
$ for f in entities relations contradictions sources timeline; do
    b=$(git show f3e09f9:corpus/fixtures/r96-crossing-response/$f.json | sha256sum | cut -d' ' -f1)
    n=$(sha256sum corpus/fixtures/r96-crossing-response/$f.json | cut -d' ' -f1); …done
entities       base=026af0bc2cdab150… now=026af0bc2cdab150… SAME
relations      base=c279254bc7de0636… now=c279254bc7de0636… SAME
contradictions base=37517e5f3dc66819… now=37517e5f3dc66819… SAME
sources        base=9f973f634cf325a3… now=9f973f634cf325a3… SAME
timeline       base=ea0225f9270db796… now=ea0225f9270db796… SAME
$ git diff --stat f3e09f9 -- corpus/fixtures/r96-crossing-response/
 corpus/fixtures/r96-crossing-response/claim-excerpt-map.md | 4 ++--
 1 file changed, 2 insertions(+), 2 deletions(-)
```

Delivered pin's per-file digests match both the actual current bytes and the baseline pin values
(`files` dict identical baseline vs delivered; each of the five `files[*]` re-hashed and MATCH);
the other three pinned fixtures are also byte-unchanged vs `f3e09f9` (`git diff --stat` empty).

## 4. Ancillary confirmations (same delivered revision)

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r96-crossing-response
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
DIGEST d422a9b3d95c4e0b8aac98cc87806a94949896adb962a50d2d55a6c11657d7f6
RESULT PASS                                          (exit 0)

$ python3 corpus/tools/dependency_freeze.py .ufo/.../V12-scratch/foreign/r96-crossing-response
FINDING PATH-MISMATCH: pin r96-crossing-response names corpus/fixtures/r96-crossing-response (…); invoked fixture resolves to …/.ufo/waves/round-97/seats/V12-scratch/foreign/r96-crossing-response
RESULT ERROR                                         (exit 2)

$ python3 corpus/tools/dependency_freeze.py --self-test | tail -2
SELF-TEST 16/16
RESULT PASS
```

Pre-hardening control on the same post-repair fixture (baseline tool bytes): canonical path and
foreign byte-identical copy both `RESULT PASS` with `DIGEST d422a9b3…` — the two hazards the round
targets, reproduced. Repair-scope and receipts (corroborating C3's repair half): the map diff is
exactly two lines (8-cell delimiter row → 7-cell; "the new relation encodes only the agreement…"
→ tick-12-event wording); running `support_check.py` and `map_obligations.py` on a scratch copy of
the fixture carrying the **pre-repair** map yields receipts identical to the post-repair runs
(`SOURCE-SUPPORT 16/16; EDITORIAL-ANCHORS 2/2; MODES 18/18; VALIDATED-ROWS 18/18; RESULT PASS` and
`OBLIGATIONS raw=16 mapped=16; INVENTORY 16/16, 2/2, 18/18; RESULT PASS`).

## Verdict

- Re-freeze integrity (only the r96 pin entry changed; only its `revision` field; reproducible
  through the guarded path): **PROVEN**.
- Unchanged JSON digests vs `f3e09f9`: **PROVEN**.
- "r96 pin now pins the post-repair map digest": **FALSE as delivered** — the pin's coverage is the
  five JSON files only; the map digest appears nowhere in the contract. Recorded by R3 itself as a
  claim discrepancy; the LOG-level C2 wording (pin refresh through the guarded path) holds.

BOTTOM LINE: FAIL — one of the seat's two required proofs is unmet: the re-freeze is integrity-sound (only the r96 pin entry's `revision` changed, JSON digests byte-identical to f3e09f9 and reproduced), but the r96 pin does not pin the post-repair map digest (map md `e851f068…` absent from the contract; `content_sha256 d422a9b3…` unchanged because pin coverage is the five JSON data files).
