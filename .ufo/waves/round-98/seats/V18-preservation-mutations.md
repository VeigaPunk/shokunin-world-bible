# V18 preservation-mutations — round 98 seat report

- Seat: V18 (verifier). Lane repo `/home/vgpnk/Projects/shokunin/lore-shokunin`; baseline r97 closure `9a3d648`; all commands run from the lane repo root with `python3`.
- Written: this report (`.ufo/waves/round-98/seats/V18-preservation-mutations.md`) plus scratch under `.ufo/waves/round-98/seats/V18-scratch/` only. No corpus writes, no commits, no network, no nested agents.
- Poll-wait: producers polled on a 20 s cadence (40-try budget). `POLL_STABLE try=21 t=420s` — all five producer reports (`S1-freeze-hygiene`, `S2-tools-docs`, `S3-fixture-author`, `S4-fixture-docs`, `S5-knowledge-notes`) present, artifact gate satisfied (7 events / 6 entities / r97+r98 pins / 17 self-test cases), and the 13-file combined sha stable across four consecutive checks (`077a4a28…`). Artifacts moved during the poll (S1's contract landed mid-poll, S5's note later); no final run was taken before stability. Endgame convention applied: the poller waits on the five producers, not on verifier reports.

Delivered revisions measured (final, post-POLL_STABLE):

| Artifact | sha256 |
|---|---|
| `corpus/tools/dependency_freeze.py` | `03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b` |
| `corpus/tools/dependency-freeze-contract.json` | `153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947` |
| `corpus/fixtures/r98-clerk-filing/timeline.json` | `eb24e0848e597efa29ed858cb8557d8f3126a47e1231f9469d719257e191e7af` |
| `corpus/fixtures/r98-clerk-filing/entities.json` | `db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984` |
| `corpus/fixtures/r98-clerk-filing/sources.json` | `32ee15b1f3d72d94f4228cbc9cefa69b7185d18b47bbe219833d7aaf30eed0f3` |
| `corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md` | `c1099d0ee9eece241ea1f796320a84453dfc6b6aec33b7b9dd7e39bbef4a94ba` |
| `corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md` (S3 repair) | `80440d61122488a267a4f0a58a55cb54d89c037d93160f1123e5fb3b2f396f61` |
| `corpus/tools/README.md` (S2) | `1d299c16bf9a0b34526f4a799cdd3117867f6d4d278866b66366b78700d79b84` |
| `corpus/knowledge/r98-clerk-scope-note.md` (S5) | `1162262c742441115681d30be588039be4f1a026b755eeb7d15c9ba41952a4b8` |

Contract state measured: pins = `r88-m3-maya-cluster`, `r94-paired-crossing`, `r95-crossing-aftermath`, `r96-crossing-response`, `r97-crossing-acknowledgment`, `r98-clerk-filing`; `self_test.expected` = 17 cases.

## Method

10 mutants, each a full copy of the delivered `corpus/fixtures/r98-clerk-filing` (byte copy; copy keeps the directory basename) with exactly one preservation violation, built by `.ufo/waves/round-98/seats/V18-scratch/mutate.py` into `V18-scratch/mutants/`:

```
$ python3 .ufo/waves/round-98/seats/V18-scratch/mutate.py
SOURCE r98-clerk-filing: entities=6 relations=1 events=7 sources=7
  last event id=clerk-filing-open deps=['acknowledgment-aru-records']
  last entity id=clerk-maren claims=1
  map J-rows=20
  declaration: **Expected inventory:** 20 JSON facts; 2 editorial rows; 22 total mapped rows; 18 distinct excerpt anchors.
MUTANT m1-span-break: last JSON-facts row span 55-64 -> 1 (anchor now outside span)
MUTANT m2-row-drop: last JSON-facts row deleted; declaration untouched
MUTANT m2b-row-drop-declared: last row deleted + declaration downgraded to 19
MUTANT m3a-claims-rename-keep-row: entities.json last entity 'clerk-maren' key claims -> assertions; map row kept
MUTANT m3b-claims-rename-row-removed: entities.json last entity 'clerk-maren' key claims -> assertions + map row removed; declaration untouched
MUTANT m4-claims-row-deletion: entities.json last entity 'clerk-maren' 'claims' key deleted + its map row deleted; declaration untouched
MUTANT m5-deps-reduction: timeline.json record clerk-filing-open depends_on ['acknowledgment-aru-records'] -> []
MUTANT m5b-event-deletion-fully-declared: timeline.json record clerk-filing-open deleted + map row deleted + declaration downgraded (self-consistent)
MUTANT m6-digest-tamper: sources.json title-case-only byte change
```

Matrix command (exits captured without pipes):

```
$ bash .ufo/waves/round-98/seats/V18-scratch/run-matrix.sh
m0-baseline                          support=0 map=0
m1-span-break                        support=1 map=0
m2-row-drop                          support=1 map=1
m2-row-drop-declared                 support=1 map=1
m3a-claims-rename-keep-row           support=0 map=1
m3b-claims-rename-row-removed        support=1 map=1
m4-claims-row-deletion               support=1 map=1
m5-deps-reduction                    support=0 map=0
m5b-event-deletion-fully-declared    support=0 map=0
m6-digest-tamper                     support=0 map=0
```

Baseline receipts on the delivered bytes (canonical path):

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r98-clerk-filing
OBLIGATIONS raw=20 mapped=20
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22
RESULT PASS                                  exit=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing
SOURCE-SUPPORT 20/20; EDITORIAL-ANCHORS 2/2; … VALIDATED-ROWS 22/22
RESULT PASS                                  exit=0
```

## Mutation matrix (delivered revision, recorded run)

Each row: `python3 corpus/tools/support_check.py $S/mutants/<m>` / `python3 corpus/tools/map_obligations.py $S/mutants/<m>`; the freeze column from the mirror-root harness below. `S=.ufo/waves/round-98/seats/V18-scratch`.

| mutant | support | map | freeze | quoted finding |
|---|---:|---:|---:|---|
| m0 baseline (unmutated copy) | 0 | 0 | 0 | `RESULT PASS` both |
| m1 span break (J20 55-64→1) | 1 | 0 | — | `FAIL J20: source-support; mode=verbatim; anchor=found; 59:> Tick 14: I filed both pending accounts at the Chalk Stair registry.; span=1; outside-span=59` / `FAIL: J20: anchor hit outside declared line span 1 (hit lines: 59)` |
| m2 row drop (declaration untouched) | 1 | 1 | — | map `INVENTORY JSON-FACTS 19/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 21/22 MISMATCH` / `FINDING inventory_mismatch: declared JSON-facts/editorial-rows/total-rows 20/2/22; observed 19/2/21` / `FINDING missing_obligation: timeline.json#/6 has no map row` |
| m2b row drop + declaration 19/2/21 | 1 | 1 | — | map `FINDING missing_obligation: timeline.json#/6 has no map row` (gate satisfied); support `FAIL: inventory distinct excerpt anchors mismatch: expected=18 parsed=17` |
| m3a claims rename, row kept | 0 | 1 | — | map `FINDING phantom_obligation: entities.json#/5/claims/0 is not a raw source-attributed obligation` / `FINDING schema_drift: entities.json#/5: 1 sourced-claim-shaped record(s) under unexpected key 'assertions'` |
| m3b claims rename + row removed | 1 | 1 | — | map `FINDING inventory_mismatch: declared … 20/2/22; observed 19/2/21` / `FINDING schema_drift: entities.json#/5: 1 sourced-claim-shaped record(s) under unexpected key 'assertions'` |
| m4 claims+row deletion (declaration untouched) | 1 | 1 | — | map `INVENTORY JSON-FACTS 19/20; … MISMATCH` / `FINDING inventory_mismatch: declared … 20/2/22; observed 19/2/21` (sole finding) |
| m5 depends_on reduction (map untouched) | 0 | 0 | 1 | freeze `FINDING REDUCTION-DETECTED: event clerk-filing-open lost depends_on ['acknowledgment-aru-records']` |
| m5b fully self-consistent deletion | 0 | 0 | 1 | freeze `FINDING REDUCTION-DETECTED: event clerk-filing-open is missing; 1 frozen dependency edge(s) gone` |
| m6 digest tamper (sources.json title case) | 0 | 0 | 2 | freeze `FINDING DIGEST-MISMATCH: … changed: sources.json …` |

The mutant map/support exits are exactly the r96/r97 accumulated classes carried onto r98: span class lives only in `support_check` (m1: map exit 0); row drop is caught twice over with the declaration untouched (gating `inventory_mismatch` + `missing_obligation`) and once (`missing_obligation`) when the declaration is downgraded; claims rename is the `schema_drift` class (m3a couples it with `phantom_obligation` when the row is kept; m3b with `inventory_mismatch` when the row is removed and the declaration is untouched); claims+row deletion is the r96 `inventory_mismatch` class reproduced on r98 (m4, sole finding). The two self-consistent tampers (m5, m5b) pass **both** map and support (0/0) and are caught only by the frozen inventory.

## Freeze half on r98/r97 copies (mirror-root harness, delivered pins)

`dependency_freeze.py` binds each fixture to its pin's repo-relative path against the running tool's own `ROOT`; verifier seats may not write under `corpus/`. `.ufo/waves/round-98/seats/V18-scratch/freeze-harness.sh` copies the delivered tool + contract **byte-for-byte** into a scratch ROOT (shas verified equal in the log: tool `03d04365…`, contract `153ebc5b…`) and places fixture copies at the pin's repo-relative paths, so the **delivered** pins (r97 and r98, added by S1 this round) bind directly. Mutations are applied in place to the harness copies.

```
== f0 baseline verify r98 (delivered pin binds) ==
$ python3 $H/corpus/tools/dependency_freeze.py $H/corpus/fixtures/r98-clerk-filing
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
DIGEST 59a0f4fa3d4a47e03649a54d1815c45ee1eef641b63a59ebe7210bc9d9b9b133
RESULT PASS                                  exit=0
== f1 baseline verify r97 (delivered pin binds) ==
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1
DIGEST 3c922d20a01bbd3f7941ed64f5c8796a619699197ae89fb10fca317cf83abea6
RESULT PASS                                  exit=0

== f2 r98 deps reduction in place ==
FREEZE r98-clerk-filing: events 7/7; dependency-edges 5/6; relations 1/1
FINDING REDUCTION-DETECTED: event clerk-filing-open lost depends_on ['acknowledgment-aru-records']
RESULT FAIL                                  exit=1
== f2b same copy through map/support (expect 0/0) ==
OBLIGATIONS raw=20 mapped=20 … RESULT PASS   exit=0
SOURCE-SUPPORT 20/20; … VALIDATED-ROWS 22/22; RESULT PASS   exit=0

== f3 r98 fully self-consistent event deletion ==
FREEZE r98-clerk-filing: events 6/7; dependency-edges 5/6; relations 1/1
FINDING REDUCTION-DETECTED: event clerk-filing-open is missing; 1 frozen dependency edge(s) gone
RESULT FAIL                                  exit=1
== f3b same copy through map/support ==
OBLIGATIONS raw=19 mapped=19 … RESULT PASS   exit=0
SOURCE-SUPPORT 19/19; … VALIDATED-ROWS 21/21; RESULT PASS   exit=0

== f4 r98 digest tamper (title case) ==
FINDING DIGEST-MISMATCH: content digest 5475eafe… != pin 59a0f4fa…; changed: sources.json (sha256 32ee15b1… -> 94685d48…); fixture bytes changed outside the frozen inventory
RESULT ERROR                                 exit=2

== f5 r97 deps reduction in place (C2 discharge demo) ==
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 4/5; relations 1/1
FINDING REDUCTION-DETECTED: event acknowledgment-aru-records lost depends_on ['response-evin-salt-court']
RESULT FAIL                                  exit=1

== f6 foreign-path r98 copy through DELIVERED repo tool (expect PATH-MISMATCH) ==
$ python3 corpus/tools/dependency_freeze.py $S/foreign/r98-clerk-filing
FINDING PATH-MISMATCH: pin r98-clerk-filing names corpus/fixtures/r98-clerk-filing (resolves to …/corpus/fixtures/r98-clerk-filing); invoked fixture resolves to …/V18-scratch/foreign/r98-clerk-filing
RESULT ERROR                                 exit=2
```

f3's declaration was recomputed dynamically to what `support_check` observes (19 facts / 2 editorial / 21 total / 17 anchors), so the deletion is fully self-consistent for map+support (both exit 0) and only the pin sees it. f0's digest `59a0f4fa…` equals the canonical chain digest below — the harness copy is byte-identical to the delivered fixture, so the pin is load-bearing on the delivered bytes, not on a reconstruction.

## Context corroborations (adjacent claims, cheap to confirm)

- Six-fixture chain at canonical paths (delivered tool, delivered contract):

```
r88-m3-maya-cluster       exit=0  DIGEST 15ef230e…
r94-paired-crossing       exit=0  DIGEST 2527beb9…
r95-crossing-aftermath    exit=0  DIGEST d541ae64…   (equals r95 pin; unchanged by S3's map repair)
r96-crossing-response     exit=0  DIGEST d422a9b3…
r97-crossing-acknowledgment exit=0 DIGEST 3c922d20…
r98-clerk-filing          exit=0  DIGEST 59a0f4fa…
```

  The r97 line is the C2 discharge: V46's recorded r97 FAIL (tick-13 edge unfrozen) is closed — the r97 pin verifies and the edge is frozen (f5 shows the scratch REDUCTION-DETECTED on it). The r95 line confirms S3's repair did not move the pinned digest.
- `python3 corpus/tools/dependency_freeze.py --self-test` → `SELF-TEST 17/17`, `RESULT PASS`, exit 0, including `CASE self_test_mismatch: exit=2 expected=2 findings=['SELF-TEST-MISMATCH'] ok`.
- C1(a) corroboration on a scratch mirror (corrupted expectation in a contract copy): `CASE clean: exit=0 expected=1 … MISMATCH` / `SELF-TEST 16/17` / `FINDING SELF-TEST-MISMATCH: cases failed: ['clean']` / `RESULT ERROR` **exit=2** (the pre-round exit-1 class is closed; the case is pinned).

## Interpretation

- All five accumulated preservation-mutation classes reproduce on the delivered r98 revision with quoted exits: span break → `support_check` exit 1 (map exit 0); row drop → `map_obligations` exit 1 (`inventory_mismatch` + `missing_obligation`, or `missing_obligation` alone with a downgraded declaration); claims rename → `schema_drift` exit 1 (with `phantom_obligation` or `inventory_mismatch` as the coupled finding); claims+row deletion → `inventory_mismatch` exit 1; `depends_on` reduction → `REDUCTION-DETECTED` exit 1.
- New this round: the freeze half is exercisable **on the delivered contract** for both r97 and r98 (f0/f1 bind and pass; f2/f5 catch edge reductions; f3 catches a fully self-consistent deletion that map+support pass 0/0; f4 names the tampered file; f6 returns `PATH-MISMATCH` — the class that returned `UNPINNED-FIXTURE` for r98 at r97). No mirror-root re-pin was needed to exercise the delivered pins; the harness only relocated the ROOT so verifier scratch could mutate copies.
- The preservation argument carried from r96/r97 holds on r98: the freeze pin is the only gate that sees an edge reduction or a fully declared deletion.

## Residuals and notes

1. The matrix mutants were run as copies (basename-preserving); the freeze column comes from the mirror-root harness with delivered tool+contract byte copies, and the delivered contract's path binding is demonstrated directly by f6.
2. Not my axis (other seats): census counts, `check_bible`, map self-test loader, knowledge-note/doc parity. The r98 map/support baseline receipts quoted above are the delivered revision's.
3. Poll context: the r98 fixture directory existed mid-authoring (5 entities / 6 events at first observation); `beat=0` gates in the poller prevented any premature run. The r98 fixture's JSON tables and the r97/r98 pins landed in separate steps during the poll window.
4. Parent-tree hygiene: no writes by this seat outside the lane; scratch and harness under `V18-scratch/` only. (Two parent-repo paths with fresh mtimes — `MANIFEST.json` 20:25, untracked `baseline-analyze.txt` 20:30 — predate or do not belong to this seat's writes; not touched by any command here.)

## Bottom line

**PASS** — on the delivered r98 revision (tool `03d04365…`, contract `153ebc5b…` with six pins and 17 cases) the accumulated mutation matrix reproduces exactly: span break → `support_check` exit 1; row drop → `map_obligations` exit 1 (`inventory_mismatch` + `missing_obligation`); claims rename → `schema_drift` exit 1; claims+row deletion → `inventory_mismatch` exit 1; `depends_on` reduction → `REDUCTION-DETECTED` exit 1 **now through the delivered r98 pin** (and the r97 pin, discharging V46's recorded FAIL), with the two self-consistent tampers invisible to map+support (0/0) and caught only by the pin, and a foreign-path copy refused `PATH-MISMATCH` exit 2.
