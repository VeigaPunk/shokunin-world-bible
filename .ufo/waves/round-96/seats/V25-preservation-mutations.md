# V25 — preservation-mutations (r96)

Seat: V25, verifier seat, round 96 single-wave swarm. Scope: the accumulated
preservation-mutation suite on r96 copies — span break, row drop, key+row
deletion, depends_on reduction — one combined matrix with exits.

Delivered revision under test (working tree, uncommitted by design; all hashes
captured before the matrix run at 2026-10-17 ~17:52 -03):

| Artifact | sha256 |
|---|---|
| `corpus/tools/map_obligations.py` | `2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8` |
| `corpus/tools/map-obligations-contract.json` | `97b76bb8b1fea97f166ef7586eba69c427ec15bbe7b34eb5345ec65c936493b6` |
| `corpus/tools/dependency_freeze.py` | `a3b57978f0cbf314389ee3f9862920a46cf109fca6d1eec488c39be0457f0980` |
| `corpus/tools/dependency-freeze-contract.json` | `7d568cc422cda42297b7506a1a3e083e8798866efd16d58617bf4ea468576975` |
| `corpus/fixtures/r96-crossing-response/timeline.json` | `ea0225f9270db79685ea6f55828c2031d7ac67cd413b04f28b25770b208815b9` |
| `corpus/fixtures/r96-crossing-response/claim-excerpt-map.md` | `5093d72eb3f22b249033d7ac4c1a85c7df7f5e09bfa673a598aee6a83045bfd8` |
| `corpus/fixtures/r96-crossing-response/entities.json` | `026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b` |

Method: every mutation is applied to a fresh `shutil.copytree` copy of the
delivered `corpus/fixtures/r96-crossing-response/` inside my exclusive scratch
dir (copy keeps the directory basename `r96-crossing-response`, which is what
`dependency_freeze.py:pin_for` resolves pins by). No corpus byte was modified.
Harness: `.ufo/waves/round-96/seats/V25-preservation-mutations.scratch/mutate.py`;
per-mutation full gate outputs: `m0-baseline.log` … `m5-addition.log` in the
same dir.

## Combined mutation matrix (final revision)

Run command (from repo root):

```sh
python3 .ufo/waves/round-96/seats/V25-preservation-mutations.scratch/mutate.py
```

| mutation (exact edit) | check_bible | support_check | map_obligations | dependency_freeze |
|---|---:|---:|---:|---:|
| m0 baseline (unmutated copy) | 0 | 0 PASS | 0 PASS | 0 PASS |
| m1 span break: J16 `Line span` `22-40` → `1` (anchor is at line 37) | 0 | **1 FAIL** | 0 PASS | 0 PASS |
| m2 row drop: delete map row J16 (`timeline.json#/4`) | 0 | **1 FAIL** | **1 FAIL** `inventory_mismatch` + `missing_obligation` | 0 PASS |
| m3 key+row deletion: delete `entities[0].claims` + its map row J06 (`entities.json#/0/claims/0`) | 1 | **1 FAIL** | **1 FAIL** `inventory_mismatch` | 2 `DIGEST-MISMATCH` |
| m4 depends_on reduction: `paired-crossing-decision.depends_on` `[aru-ninth-bell, evin-ninth-bell]` → `[aru-ninth-bell]` | 0 | 0 PASS | 0 PASS | **1 FAIL** `REDUCTION-DETECTED` |
| m5 (extra) depends_on addition: `+ aftermath-missing-evin` | 1 | 0 PASS | 0 PASS | **1 FAIL** `ADDITION-DETECTED` |

Exact observed outputs for the four claimed detections:

- m1 (span break) — `python3 corpus/tools/support_check.py <copy>`:
  `FAIL J16: source-support; mode=verbatim; anchor=found; 37:> Tick 12: I was at Salt Court through the same agreed bell.; span=1; outside-span=37`
  `FAIL: J16: anchor hit outside declared line span 1 (hit lines: 37)`; `RESULT FAIL`; exit 1.
  `map_obligations` stays exit 0 (spans are support_check's domain — expected, not a defect).
- m2 (row drop) — `python3 corpus/tools/map_obligations.py <copy>`:
  `FINDING inventory_mismatch: declared JSON-facts/editorial-rows/total-rows 16/2/18; observed 15/2/17`
  `FINDING missing_obligation: timeline.json#/4 has no map row`; `RESULT FAIL`; exit 1.
- m3 (key+row deletion) — `python3 corpus/tools/map_obligations.py <copy>`:
  `FINDING inventory_mismatch: declared JSON-facts/editorial-rows/total-rows 16/2/18; observed 15/2/17`; `RESULT FAIL`; exit 1.
  Raw/declared counts still reconcile against each other (`raw=15 mapped=15`), so the
  only signal is the declaration-vs-observation gate — exactly the class C1(a) targets.
- m4 (reduction) — `python3 corpus/tools/dependency_freeze.py <copy>`:
  `FREEZE r96-crossing-response: events 5/5; dependency-edges 3/4; relations 1/1`
  `FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']`; exit 1.

The two non-target exits are consistent with the delivered contracts, not defects:
m3's `dependency_freeze` exit 2 `DIGEST-MISMATCH` is the contract's declared
precedence ("a content digest change the frozen inventory does not model exits 2";
`entities.json` changed, which the dep model does not inventory); m5's
`check_bible` exit 1 reflects that a tick-10 event depending on the tick-11
aftermath inverts chronology. m5's support/map stay green because only
`timeline.json` changed and no map obligation binds `depends_on` values.

## Before/after evidence for the deletion class (C1(a))

Before (pre-hardening tool, r95 closure revision `git show HEAD:corpus/tools/map_obligations.py`,
sha256 `d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108`,
contract 22 cases): same key+row deletion applied to a scratch copy of the r95
fixture —

```sh
$ python3 .../before-repro/map_obligations_r95.py <r95 copy with entities[0].claims + J06 row removed>
OBLIGATIONS raw=14 mapped=14
INVENTORY JSON-FACTS 14/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/17 MISMATCH
RESULT PASS
BEFORE_EXIT=0
```

After (delivered revision, r96 copy): exit 1 `inventory_mismatch` (m3 above).
The carried deletion class is closed. Reproducible receipt saved at
`.ufo/waves/round-96/seats/V25-preservation-mutations.scratch/before-repro/before-r95-deletion-class.out`.

## Supporting context (not my axis, cheap to confirm)

- `python3 corpus/tools/map_obligations.py --self-test` → 24 `SELF-TEST PASS`
  lines (including `schema_drift` and `inventory_mismatch`), no FAIL, `RESULT PASS`, exit 0.
- `python3 corpus/tools/dependency_freeze.py --self-test` → `SELF-TEST 14/14`, `RESULT PASS`, exit 0.
- `dependency_freeze.py` on the delivered chain: r88-m3-maya-cluster, r94-paired-crossing,
  r95-crossing-aftermath, r96-crossing-response all `RESULT PASS` (4/4 clean).

## Side finding (outside my matrix, reported as-is): foreign pin in a delivered artifact

`corpus/tools/dependency-freeze-contract.json` (delivered revision, mtime
17:44:27) contains a pin `c3red` whose `fixture` label is
`.ufo/waves/round-96/seats/V41-scratch/c3red` — another seat's scratch
directory — with `content_sha256 eff4b354…`. V41's own scratch log
`.ufo/waves/round-96/seats/V41-scratch/c3-freeze.out` shows the cause:

```
FROZEN c3red: events 3; dependency-edges 1; relations 1
DIGEST eff4b354c092a9c4a3ea6de6857ee1a21be1ab4bafac957568b6813dac8dbd28
RESULT PASS
```

and that scratch copy's `paired-crossing-decision.depends_on` is `['aru-ninth-bell']`
— i.e. a verifier ran `dependency_freeze.py --freeze <scratch copy>`, and
`freeze()` persists the pin into the shared delivered contract with no
path/ownership guard. Effect on my matrix: none — the r96 pin still matches the
delivered fixture (m0 baseline exit 0), and extra pins are inert unless a
directory named `c3red` is verified. But the delivered contract now carries a
foreign, scratch-referencing pin, and any future `--freeze` run silently mutates
the shared artifact. The `pins` list is
`['c3red', 'r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response']`.

## Bottom line

PASS — on the delivered r96 revision the combined matrix is exactly as specified: baseline all-green (0/0/0/0), span break → support_check exit 1, row drop → map_obligations exit 1 (`inventory_mismatch` + `missing_obligation`), key+row deletion → map_obligations exit 1 `inventory_mismatch` (before the hardening: exit 0 PASS), depends_on reduction → dependency_freeze exit 1 `REDUCTION-DETECTED` (and added edge → exit 1 `ADDITION-DETECTED`); with one side finding outside the matrix: the delivered dependency-freeze contract carries a foreign `c3red` pin written by V41's `--freeze` on its scratch copy.
