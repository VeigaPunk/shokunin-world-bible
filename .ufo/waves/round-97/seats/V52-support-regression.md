# V52 — support-hardening-regression (round 97)

**Seat role (as declared):** support_check receipts r87–r97 all replay unchanged (quote); r94-round silent-failure vectors still fail/warn on scratch. Leaf seat; report-only on the live tree; all writes under `.ufo/waves/round-97/seats/V52-scratch/` plus this report. No commits, no network.

**Revision under test:** HEAD `2393934237ea076366f3db6dceeff033edb52ab1` (r96 closure line; round baseline `f3e09f9`). Working tree during the battery: `M LOG.md` (r97 declaration), `M corpus/fixtures/r96-crossing-response/claim-excerpt-map.md` (R4 repair), `M corpus/tools/README.md` + `M corpus/tools/map-obligations-contract.json` + `M corpus/tools/map_obligations.py` (R1/R2), `M corpus/tools/dependency_freeze.py` (R3, landed 18:52:21), untracked `.ufo/waves/round-97/`, `corpus/fixtures/r97-crossing-acknowledgment/` and `corpus/knowledge/r97-acknowledgment-scope-note.md` (R6). `corpus/tools/support_check.py` is **unmodified** by the round (`git status` clean for it).

**Producer-report state at my final check (18:54):** reports present — R1 `R1-map-pinning.md`, R2 `R2-contract-docs.md`, R4 `R4-fixture-author.md`, R5 `R5-fixture-docs.md`, R6 `R6-knowledge-note.md`; report **absent** — R3 (poll-wait window 18:48→18:54, 40-try cadence not exhausted), whose artifacts (`dependency_freeze.py` sha `7428dad4…`, `dependency-freeze-contract.json`) were nonetheless on disk. Reported exactly as observed; no plan was verified. The r87–r97 battery was re-run after the producer landing window (`receipts/*.pass3.out`): every receipt is byte-identical to the earlier pass, and the r97 receipt is byte-identical after R5's and R6's reports landed (`r97-support-final.out` == `r97-support-final2.out` == `r97-support-final3.out`, sha `a109856d…`).

## 1. Precondition — the tool under test is the r94–r96 revision, unchanged

```
$ sha256sum corpus/tools/support_check.py
55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  corpus/tools/support_check.py
$ git show f3e09f9:corpus/tools/support_check.py | sha256sum
55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  -
```

`55a5eb27…` is the same hash the r95 V52 seat recorded for the r95 delivered revision, so the survival question this seat answers is behavioral: does the r91/r92 hardening still hold on the r97 tree?

## 2. Receipt battery — r87, r88-m3, r89-inspiration-paraphrase, r93-m2, r94, r95, r96, r97

Command per cluster (cwd = repo root): `python3 corpus/tools/support_check.py corpus/fixtures/<cluster>`; exit captured immediately after each run.

| Cluster | Quoted receipt lines | Exit |
|---|---|---|
| r87-myth-cluster | `INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 8/8; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 22/22` / `ANCHORS repeated-references=0; DUPLICATE-ROWS 0` / `RECEIPT JSON-FACTS 14; EDITORIAL-ROWS 8; TOTAL-ROWS 22` / `SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 8/8; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22; VALIDATED-ROWS 22/22` / `RESULT PASS` | 0 |
| r88-m3-maya-cluster | `INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12; DISTINCT-ANCHORS 8/8` / `ANCHORS repeated-references=4; DUPLICATE-ROWS 0` / `RECEIPT JSON-FACTS 10; EDITORIAL-ROWS 2; TOTAL-ROWS 12` / `SOURCE-SUPPORT 10/10; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 12/12; VALIDATED-ROWS 12/12` / `RESULT PASS` | 0 |
| r89-inspiration-paraphrase | `INVENTORY JSON-FACTS 1/1; EDITORIAL-ROWS 0/0; TOTAL-ROWS 1/1; DISTINCT-ANCHORS 1/1` / `ANCHORS repeated-references=0; DUPLICATE-ROWS 0` / `RECEIPT JSON-FACTS 1; EDITORIAL-ROWS 0; TOTAL-ROWS 1` / `SOURCE-SUPPORT 0/0; EDITORIAL-ANCHORS 0/0; RETELLING-SUPPORT-ONLY 1 entries (1/1 anchors); MODES 1/1; VALIDATED-ROWS 1/1` / `RESULT PASS` | 0 |
| r93-m2-kojiki-cluster | `INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15; DISTINCT-ANCHORS 15/15` / `ANCHORS repeated-references=0; DUPLICATE-ROWS 0` / `RECEIPT JSON-FACTS 12; EDITORIAL-ROWS 3; TOTAL-ROWS 15` / `SOURCE-SUPPORT 12/12; EDITORIAL-ANCHORS 3/3; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 15/15; VALIDATED-ROWS 15/15` / `RESULT PASS` | 0 |
| r94-paired-crossing | `INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16; DISTINCT-ANCHORS 12/12` / `ANCHORS repeated-references=4; DUPLICATE-ROWS 0` / `RECEIPT JSON-FACTS 14; EDITORIAL-ROWS 2; TOTAL-ROWS 16` / `SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 16/16; VALIDATED-ROWS 16/16` / `RESULT PASS` | 0 |
| r95-crossing-aftermath | `INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17; DISTINCT-ANCHORS 13/13` / `ANCHORS repeated-references=4; DUPLICATE-ROWS 0` / `RECEIPT JSON-FACTS 15; EDITORIAL-ROWS 2; TOTAL-ROWS 17` / `SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 17/17; VALIDATED-ROWS 17/17` / `RESULT PASS` | 0 |
| r96-crossing-response | `INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18; DISTINCT-ANCHORS 14/14` / `ANCHORS repeated-references=4; DUPLICATE-ROWS 0` / `RECEIPT JSON-FACTS 16; EDITORIAL-ROWS 2; TOTAL-ROWS 18` / `SOURCE-SUPPORT 16/16; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 18/18; VALIDATED-ROWS 18/18` / `RESULT PASS` | 0 |
| r97-crossing-acknowledgment | `INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19; DISTINCT-ANCHORS 15/15` / `ANCHORS repeated-references=4; DUPLICATE-ROWS 0` / `RECEIPT JSON-FACTS 17; EDITORIAL-ROWS 2; TOTAL-ROWS 19` / `SOURCE-SUPPORT 17/17; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 19/19; VALIDATED-ROWS 19/19` / `RESULT PASS` | 0 |

Every receipt matches its declared expectation (r87 14+8, r88 10+2, r89 1 paraphrase row, r93 12+3, r94 14+2, r95 15+2, r96 16+2, r97 17+2 = the r97 map's own `**Expected inventory:** 17 JSON facts; 2 editorial rows; 19 total mapped rows; 15 distinct excerpt anchors.`). Full transcripts: `V52-scratch/receipts/*.pass2.out`, `V52-scratch/receipts/r97-support-final.out`.

Determinism / cross-round stability (sha256 of the full stdout file, first 16 hex):

```
r87-myth-cluster.pass2.out             952354ac759646a2
r88-m3-maya-cluster.pass2.out          b5c4075d65284f3d
r89-inspiration-paraphrase.pass2.out   ec3cd3fb29b7c0e6
r93-m2-kojiki-cluster.pass2.out        63f90ea53c147088
r94-paired-crossing.pass2.out          d0ff69820d619bc5
r95-crossing-aftermath.pass2.out       efae7be25d213fea
r96-crossing-response.pass2.out        ca7a6815077f87e8
r97-support-final.out                  a109856d383efa18
```

The r87/r88/r93/r94 hashes are byte-identical to the r95 V52 seat's manifest (`952354ac…`, `b5c4075d…`, `63f90ea5…`, `d0ff6982…`), i.e. these receipts have not moved across the r95→r96→r97 tool work.

r97 detail beyond the summary: rows `J01`–`J16` are cell-identical to r96's rows except the path-qualification column (16/16 diffs are exactly `r96-crossing-response:` → `r97-crossing-acknowledgment:`); the new `J17` is the only added row and is anchored at `fictional-excerpts.md:48` → `PASS J17: source-support; mode=verbatim; anchor=found; 48:> Tick 13: I received Evin's response at the Chalk Stair.` Before the r97 map landed, the same tool on the same fixture reported `INVENTORY JSON-FACTS 16/16; … TOTAL-ROWS 18/18` (r96 map still in place) — the receipt follows the map bytes, as designed.

## 3. The r96 cosmetic repair is receipt-neutral (proven, not assumed)

R4's repair of `corpus/fixtures/r96-crossing-response/claim-excerpt-map.md` is exactly two lines (`git diff --numstat` → `2  2`):

```
-|---|---|---|---|---|---:|---|---|
+|---|---|---|---|---:|---|---|
```
(editorial-table delimiter row, 8 cells → 7, matching its header and data rows)

```
-The … inherited tick-11 aftermath event … The new relation encodes only the agreement for this crossing, not perpetual performance or alliance.
+The … inherited tick-11 aftermath event … The new tick-12 event encodes only Evin's second account of the same crossing occasion; it asserts no reconciliation, selects no winner between the accounts, and adds no duty beyond this crossing, not perpetual performance or alliance.
```

Proof method: a scratch copy of the whole r96 fixture (`V52-scratch/r96-pre/`) with the map replaced by the frozen `f3e09f9` bytes, run with the same delivered tool:

```
$ git show f3e09f9:corpus/fixtures/r96-crossing-response/claim-excerpt-map.md > …/r96-pre/claim-excerpt-map.md
$ python3 corpus/tools/support_check.py …/r96-pre > receipts/r96-old-map-support.out ; echo EXIT=$?
EXIT=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response > receipts/r96-new-map-support.out ; echo EXIT=$?
EXIT=0
$ diff receipts/r96-old-map-support.out receipts/r96-new-map-support.out && echo IDENTICAL
DIFF: IDENTICAL (pre-repair f3e09f9 map vs repaired map)
$ sha256sum receipts/r96-old-map-support.out receipts/r96-new-map-support.out
ca7a6815077f87e8e415588a312e3644ccaa44c5fbafb8ed3405a4b53aaf6be1  …/r96-old-map-support.out
ca7a6815077f87e8e415588a312e3644ccaa44c5fbafb8ed3405a4b53aaf6be1  …/r96-new-map-support.out
```

`map_obligations` on the same pair is likewise unchanged: `OBLIGATIONS raw=16 mapped=16` / `INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18` / `RESULT PASS`, exit 0, both before (frozen bytes) and after (repaired bytes). The other five r96 fixture files are byte-identical to `f3e09f9` (checked for all five). So the C3 repair half's "r96 receipts unchanged" claim holds on the delivered bytes.

## 4. Silent-failure vectors on scratch — delivered tool vs r90/r91 historical controls

Builder `V52-scratch/make_demos.py` (copies the live fixtures read-only; every replacement asserts exactly one occurrence). Controls: `V52-scratch/support_check_r90.py` = `git show a7c6a17:corpus/tools/support_check.py` (sha256 `66a3c4bb…`, the pre-hardening tool), `V52-scratch/support_check_r91.py` = `git show 6332115:…` (sha256 `9da149b8…`, first hardened tool).

| # | vector (scratch copy) | delivered tool | r90 tool |
|---|---|---|---|
| T1 | r87 fact-table `ID` header → `Ref` | `INVENTORY JSON-FACTS 0/14; EDITORIAL-ROWS 8/8; TOTAL-ROWS 8/22` + 4 `WARN: unreferenced excerpt declaration` + `FAIL: inventory JSON facts mismatch: expected=14 parsed=0`, **exit 1** | `SOURCE-SUPPORT 8/8; … MODES 8/8` / `RESULT PASS`, **exit 0 (silent)** |
| T2 | r87 `## Editorial rows` section dropped | `EDITORIAL-ROWS 0/8; TOTAL-ROWS 14/22` + `WARN … lowwater-hymn-excerpt.md` + 3 `FAIL: inventory …` / `RESULT FAIL`, **exit 1** | `SOURCE-SUPPORT 14/14; … MODES 14/14` / `RESULT PASS`, **exit 0 (silent)** |
| T3 | r87 `E1` row duplicated | `JSON-FACTS 15/14; TOTAL-ROWS 23/22` + `FAIL: duplicate mapped row E1 appears 2 times` / `RESULT FAIL`, **exit 1** | `SOURCE-SUPPORT 23/23` / `RESULT PASS`, **exit 0 (inflated, silent)** |
| T4 | r87 hymn declaration `verbatim`→`summary` (referenced) | 8× `FAIL H*: editorial-row; mode=verbatim; …`, `EDITORIAL-ANCHORS 0/8; MODES 14/22` / `RESULT FAIL`, **exit 1** | `FAIL H1…` / exit 1 (already failing) |
| T5a | r88 Spence declaration flip on the **current** map (S1/S2 reference it) | `FAIL S1/S2: editorial-row; mode=verbatim; excerpt-mode=summary`, `EDITORIAL-ANCHORS 0/2; MODES 10/12` / `RESULT FAIL`, **exit 1** | `FAIL S1/S2 …` exit 1 |
| T5b | r88 r90-era shape (editorial rows removed, inventory restated) + same flip | `WARN: unreferenced excerpt declaration: source-excerpt.md (mode=summary)` / `SOURCE-SUPPORT 10/10` unchanged / `RESULT PASS WITH WARNINGS`, **exit 0 (surfaced, not silent)** | `SOURCE-SUPPORT 10/10` / `RESULT PASS`, **exit 0 (silent)** |
| T6 | r89 paraphrase anchor made absent | `WARN entities.json#/0/claims/0: retelling-support-only; anchor=not-found`, `RETELLING-SUPPORT-ONLY 1 entries (0/1 anchors)`, `VALIDATED-ROWS 0/1`, `WARN: retelling anchor not found … excluded from source support` / `RESULT PASS WITH WARNINGS`, **exit 0** | `RETELLING-SUPPORT-ONLY 1 entries (0/1 anchors)` / `RESULT PASS`, exit 0 (count only, no WARN) |
| T7 | r87 inventory declaration line removed | stderr `FAIL: map must contain exactly one expected inventory declaration`, stdout `RESULT FAIL`, **exit 1** | `SOURCE-SUPPORT 22/22` / `RESULT PASS`, **exit 0 (silent)** |
| T8 | r87 distinct-anchor declaration 22→21 | `DISTINCT-ANCHORS 22/21` + `FAIL: inventory distinct excerpt anchors mismatch: expected=21 parsed=22` / `RESULT FAIL`, **exit 1** | `SOURCE-SUPPORT 22/22` / `RESULT PASS`, **exit 0 (silent)** |

All eight vectors fail or warn on the delivered tool; six of them (T1, T2, T3, T5b, T7, T8) were silent passes under the r90 tool. Two honest deltas against the r91 JCOV4 table, both in the non-silent direction and attributable to the r92 "contract deviations closed" work (README `### Terminal statuses`, `corpus/tools/README.md:18-23`): T7 now exits **1** with a `RESULT FAIL` line (r91 tool: exit 2, empty stdout — re-run control `support_check_r91.py …/T7-no-inventory` → `EXIT=2`, `stdout lines: 0`), and T8 now prints a `RESULT FAIL` terminal line (r91 tool: exit 1 with no RESULT line). Neither change reintroduces silence.

## 5. The r94-round mutant vectors (F15) — which are closed, which are by-design blind spots

`V52-scratch/demos/` built from r94-paired-crossing:

| mutant | `support_check` | where the blind spot is closed |
|---|---|---|
| F15-b2 — fact row `J05` dropped **and** inventory restated to match | `INVENTORY JSON-FACTS 13/13; … TOTAL-ROWS 15/15` / `RESULT PASS`, exit 0 (still silent by design; map-only lexical check) | `map_obligations …` → `OBLIGATIONS raw=14 mapped=13` / `FINDING missing_obligation: entities.json#/4/first_appearance has no map row` / `RESULT FAIL`, exit 1 |
| F15-b3 — row dropped, stale inventory kept | `INVENTORY JSON-FACTS 13/14; … DISTINCT-ANCHORS 11/12` + 3 `FAIL: inventory …` / `RESULT FAIL`, exit 1 | — (support_check's own drift catch) |
| F15-a — tick-10 `depends_on` reduced to one entry (raw JSON) | `INVENTORY … 14/14 … 16/16` / `RESULT PASS`, exit 0 (documented: `support_check` never reads raw JSON) | `check_bible` CLEAN exit 0 (reproduces F15's finding); `dependency_freeze` on the scratch copy exits 2 `FINDING UNPINNED-FIXTURE … (pinned: [r88-m3-maya-cluster, r94-paired-crossing, r95-crossing-aftermath, r96-crossing-response])` on both the r96 revision (`a3b57978…`) and the delivered r97 revision (`7428dad4…`) — the mutant is outside the pinned set, so this seat makes **no** claim that the reduced-dependency mutation is caught; that is C2/`dependency_freeze` territory (V45 etc.) |

These match F15's r94 records exactly (`mut-b2` PASS, `mut-b3` FAIL, `mut-a` invisible to both `check_bible` and `support_check`). They are named as blind spots of this tool, not regressions: the r94 round recorded them as such and the closing tools are the r94/r96 `map_obligations` and `dependency_freeze` additions.

## 6. Live-tree protection and bounds

- All demos are copies under `V52-scratch/demos/`; the live fixture maps and the tool hash are unchanged after the whole battery: r87 `3ad4e810…`, r88 `b3b79fe5…`, r89 `72514061…`, r93 `17f0e812…`, r94 `ed9527c5…`, r95 `30281ff1…`, r96 `e851f068…`, `support_check.py` `55a5eb27…` (identical to the values read before the demos).
- `support_check` is a lexical preflight (fixed-string anchors, declared spans, R9 mode consistency, declared inventory); none of these receipts proves entailment, mode fidelity, source authentication, chronology, rights, permission, or canon. Quoting it as support evidence is out of scope here.
- The r97 fixture's own contents (5/1/6, 6 sources, the appended note, the J17 anchor) are the C3 depth claim and belong to other seats; this seat only replays the map↔excerpt receipt on the delivered bytes.
- Not verified by this seat (out of its scope): R3's `dependency_freeze.py` hardening (delivered revision `7428dad4…` observed only as the tool that answered my scratch invocation; its C2 claims belong to the C2 seats) and R6's knowledge note. The R3 report was absent at my final check (recorded above); R4's r96-map repair and R5's r97 map/README bytes were verified as delivered.

**Bottom line: PASS — every `support_check` receipt r87→r97 replays unchanged/exactly as declared (r87 14+8, r88 10+2, r89 1 paraphrase, r93 12+3, r94 14+2, r95 15+2, r96 16+2, r97 17+2, all `RESULT PASS`, exit 0; r87/r88/r93/r94 outputs byte-identical to the r95 manifest), the r96 cosmetic repair is proven receipt-neutral by diffing the frozen f3e09f9 map against the repaired map (identical output, sha `ca7a6815…`), and all eight r94-round silent-failure vectors still fail/warn on scratch against r90/r91 controls — with the two r94 F15 mutants that remain silent in `support_check` reported exactly as the documented, tool-scoped blind spots they are.**
