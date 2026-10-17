# V29 — doc-parity (round 96) — pre-integration closure-doc inventory

Seat: V29 doc-parity. Leaf seat; no nested agents, no commits, no network. Written
paths: this report (`.ufo/waves/round-96/seats/V29-doc-parity.md`) and
`.ufo/waves/round-96/seats/V29-scratch/` only. Every command quoted below was run
from the lane root `/home/vgpnk/Projects/shokunin/lore-shokunin` with repo-relative
arguments. Baseline: r95 closure `dcb2d92`; working-tree HEAD at verification
`60dba0c` plus uncommitted r96 producer artifacts.

Poll-wait protocol: a 20 s-cadence poller checked the six producer artifacts +
reports up to 40 tries. `ALL_PRESENT try=32` (~17:52:20): Q1–Q6 reports all written,
`map_obligations` self-test 24 cases, `corpus/tools/README.md` carries the Round-96
addendum. No target was verified before its producer report existed; no ABSENT item.

## 0. Delivered revisions and receipts (measured this seat)

Hashes at verification (all producers reported complete):

```
2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8  corpus/tools/map_obligations.py
97b76bb8b1fea97f166ef7586eba69c427ec15bbe7b34eb5345ec65c936493b6  corpus/tools/map-obligations-contract.json
a3b57978f0cbf314389ee3f9862920a46cf109fca6d1eec488c39be0457f0980  corpus/tools/dependency_freeze.py
7d568cc422cda42297b7506a1a3e083e8798866efd16d58617bf4ea468576975  corpus/tools/dependency-freeze-contract.json
965b29cd41a8af14293eb2e1948f58f310e58c6e752b8fe322c5445b20a91f24  corpus/tools/README.md
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
ff52ced48bf4214721f248328d76da64a42773d44e78154ef1eaf6eb3558c456  corpus/fixtures/r96-crossing-response/README.md
5093d72eb3f22b249033d7ac4c1a85c7df7f5e09bfa673a598aee6a83045bfd8  corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
6db32ca24f5eff5baa3ebe589e8d3bcb6b256fec18dee2468211d7d0fae157c6  corpus/knowledge/r96-response-scope-note.md
```

Fixture/tool receipts (verbatim tails):

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response
CLEAN: schema, citations, relations, timeline; 0 violations          exit 0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response
OBLIGATIONS raw=16 mapped=16
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18
RESULT PASS                                                          exit 0
$ python3 corpus/tools/map_obligations.py --self-test
SELF-TEST CASES 24/24 pinned
RESULT PASS                                                          exit 0
$ python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response   (tail)
RECEIPT JSON-FACTS 16; EDITORIAL-ROWS 2; TOTAL-ROWS 18
SOURCE-SUPPORT 16/16; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 18/18; VALIDATED-ROWS 18/18
RESULT PASS                                                          exit 0
$ python3 corpus/tools/dependency_freeze.py --self-test               (tail)
SELF-TEST 14/14
RESULT PASS                                                          exit 0
$ for d in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response; do python3 corpus/tools/dependency_freeze.py corpus/fixtures/$d; done
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0      RESULT PASS  exit 0
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1      RESULT PASS  exit 0
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1   RESULT PASS  exit 0
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1    RESULT PASS  exit 0
```

Regression surface (post-hardening, unchanged): r93 `12/12` PASS; r88 `10/10` PASS;
frozen r93 replay `SNAPSHOT inputs=4 digests=verified … RESULT PASS`; r87 and r89
exit 2 `unsupported_map` fail-closed.

Census (fresh replica, method validated against `dcb2d92` first):

```
$ python3 .ufo/waves/round-96/seats/V29-scratch/census_r96.py          # working tree
{"dirs": 170, "clean": 36, "negative": 134, "other": 0, "violation_lines": 421}
# same script on a git-archive materialization of dcb2d92:
{"dirs": 169, "clean": 35, "negative": 134, "other": 0, "violation_lines": 421}
```

The `dcb2d92` run exactly reproduces the r95 closure census (169/35/134/421), so the
working-tree 170/36/134/421 is measured on a validated method. (Two transient
`/tmp` "No space left on device" failures during the round — 64-seat tmpfs load;
workaround: scratch-local `TMPDIR`. Also observed independently by Q2.)

C9 r96 re-check receipts (for the row below):

```
$ sha256sum corpus/fixtures/check_bible.py
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
$ python3 corpus/tools/discriminate_check.py            → RESULT: DISCRIMINATION HELD      exit 0
$ python3 corpus/tools/discriminate_check.py --checker e97613c
REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved — pinned delivered semantics not present   exit 2 (expected control)
```

Independent before/after for the gating deletion class (scratch copy of r96 with
entity 0's `claims` key deleted and its `J06` map row removed):

```
$ python3 <scratch>/map_obligations_r95.py <scratch-copy>   # HEAD revision d1c239cc…
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/18 MISMATCH
RESULT PASS                                                          exit 0
$ python3 corpus/tools/map_obligations.py <scratch-copy>    # delivered 2b0ba815…
…same receipt…
FINDING inventory_mismatch: declared JSON-facts/editorial-rows/total-rows 16/2/18; observed 15/2/17
RESULT FAIL                                                          exit 1
```

## 1. fixtures README Round-96 section — ABSENT (L1 to append)

Measured state: `corpus/fixtures/README.md` is 1196 lines, ends with the Round-95
pin note; `grep -c "Round 96\|Round-96\|r96"` = 0. Proposed exact append after
line 1196:

````markdown
## Round 96 — `r96-crossing-response` (2026-10-17)

Added at round 96: a preserving continuation of `r95-crossing-aftermath`. A second account of the same occasion: Evin's authored response note (`evin-response-note`) and one tick-12 event (`response-evin-salt-court`, actor `evin`, place `salt-court`, `depends_on: ["aftermath-missing-evin"]`) record that Evin was at Salt Court through the same agreed bell. The two first-person accounts stand unresolved: the note asserts no accusation and selects no winner, and no contradiction is asserted (the accounts name different actors at different places). Inherited r95 records are parsed-value identical; the r95 fixture itself is untouched. Map: 16 obligations (15 inherited rows unchanged + the new event row); support receipt 16 JSON facts + 2 editorial rows.

Replay commands and receipts (measured at the r96 closure, HEAD cited in LOG.md):

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response
# CLEAN: schema, citations, relations, timeline; 0 violations   exit 0
python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response
# OBLIGATIONS raw=16 mapped=16; INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18 / RESULT PASS   exit 0
```

Round 96 also hardened `map_obligations` (see the tools README Round-96 addendum): a declared-vs-observed inventory mismatch is now GATING (the r95 deletion class → exit 1, stable `inventory_mismatch` FINDING), `schema_drift` and `inventory_mismatch` behaviors are pinned by persisted self-test cases (24 total), and a legacy-dialect map cell naming a second pointer in prose exits 1 `dual_pointer` (V37-D1 closed). The new `dependency_freeze` gate (see the tools README Round-96 addendum) freezes dependency-edge inventories, event endpoints and relation endpoints for the continuation chain; the delivered chain verifies 4/4 clean and the BR-01 reduction mutation exits 1 `REDUCTION-DETECTED`.

### 2026-10-17 census re-declaration

A full repo-relative corpus run at the r96 closure observed **170 fixture directories: 36 clean (exit 0), 134 intentional negative (exit 1), 421 violation lines, zero non-0/1 exits**. This supersedes the Round-95 census (169/35/134/421) as a measured statement at this revision, not a pinned invariant. One directory was added (`r96-crossing-response`); zero inherited tuples changed.

Dated pin note: this Round-96 append changes this file's bytes; the W05 preservation pin recorded at `.ufo/waves/round-94/work/W05-baseline-corpus.sha256` for this file no longer matches (third consecutive round; the census re-declaration above is the measured state at closure).
````

## 2. corpus/README.md bullets — stale / absent (L1 to edit)

Measured state: line 36 still says `(rounds 94–95)` and `--self-test` (22 persisted
cases); no r96 fixture bullet; no `dependency_freeze` bullet; line 37's tool list
omits `dependency_freeze.py`. Proposed edits:

(a) after the r95 bullet (line 22) insert:

- `fixtures/r96-crossing-response/README.md` — continuation of the r95 fixture: a second account of the same occasion — Evin's response note reports Evin at Salt Court through the same agreed bell (tick-12 event depending on the tick-11 aftermath event). The two first-person accounts stand unresolved: no accusation, no winner, no contradiction asserted. Navigate `claim-excerpt-map.md` (16 obligations) and `fictional-excerpts.md`.

(b) replace line 36 with:

- `tools/map_obligations.py` (rounds 94–96) — raw-JSON↔map obligation completeness and source-ID agreement for canonical one-obligation-per-row cluster maps and the r88-m3 legacy dialect; a declared-vs-observed inventory mismatch is gating (`inventory_mismatch`, exit 1), legacy-dialect hidden-second-pointer cells exit 1 `dual_pointer`, `--self-test` persists 24 cases, and a digest-pinned `--frozen` snapshot is available. Mapping completeness only, never entailment, authentication, chronology, rights, permission, or canon.

(c) new bullet after (b):

- `tools/dependency_freeze.py` (round 96) — frozen dependency-edge inventory, event endpoints and relation endpoints for the continuation chain (`r88-m3-maya-cluster`, `r94-paired-crossing`, `r95-crossing-aftermath`, `r96-crossing-response`) pinned with fixture content digests; exit 0 clean / 1 reduction, addition, or endpoint change with stable FINDING IDs / 2 could-not-evaluate; `--self-test` persists 14 cases. Detects silent dependency reduction (BR-01); not a canon or chronology judgment.

(d) line 37: add `tools/dependency_freeze.py` to the tools/README tool list.

## 3. SKILL.md registry row for `dependency_freeze` — ABSENT (L1 to append)

Measured state: no `dependency_freeze` row; the `map_obligations` row (lines 83–89)
still says "22 cases", carries the "(r95 debt)" `schema_drift` note, and lists the
r96-debt residuals. Proposed registry row (fleet schema, matching sibling rows),
to be inserted after the `map_obligations` section:

````markdown
### Dependency freeze (continuation chain)

- **name:** `dependency_freeze`
- **gate/probe:** gate
- **entry command:** `python3 corpus/tools/dependency_freeze.py <fixture-directory>` (repository root; `--freeze <fixture-directory>` (re)builds the pin and is delivery-time only, not part of the verify path)
- **code → class:** `0 → clean`; `1 → failed` (`REDUCTION-DETECTED` / `ADDITION-DETECTED` / `ENDPOINT-CHANGE` with stable FINDING IDs); `2 → could-not-evaluate` (`DIGEST-MISMATCH` for content changes outside the frozen inventory, `UNPINNED-FIXTURE`, `FIXTURE-MISSING`, `FILE-MISSING`, `MALFORMED-JSON`, `MALFORMED-MODEL`, `CONTRACT-INVALID`, `INVALID-ARGUMENTS`, `SELF-TEST-MISMATCH`); other codes → `could-not-evaluate`
- **self-test command:** `python3 corpus/tools/dependency_freeze.py --self-test`; 14 isolated cases with persisted expected exits and finding IDs under `self_test.expected` in `corpus/tools/dependency-freeze-contract.json`
- **pinned-values path:** `corpus/tools/dependency-freeze-contract.json` (per-fixture event → sorted `depends_on` sets, event endpoints, relation endpoint triples, per-file and content SHA-256 digests)
- **scope:** verifies the frozen dependency edges, event endpoints and relation endpoints of the named continuation-chain fixtures against the committed pin; semantic inventory findings decide first (exit 1), and a content change the inventory does not model exits 2. Not a canon, chronology, entailment, rights, or permission judgment.
- **owner:** `lore-shokunin`
````

Also update the `map_obligations` row: `22 cases (r95 added …)` → `24 cases (r96
added persisted `schema_drift` and `inventory_mismatch` cases)`; delete the
"(r95 debt)" sentence; add `inventory_mismatch` / `dual_pointer` to the exit-1
finding list and scope; replace the residuals sentence (the deletion class, D1 and
the drift-scope pinning are closed; BR-01 is now closed by `dependency_freeze`).

## 4. C9 r96 re-check row — ABSENT (L1 to append to corpus/knowledge/r91-c9-watch.md)

Measured state: the last table row is r95, "Next re-check: r96". Proposed exact
append (receipts in §0 above; date 2026-10-17):

````markdown
## 2026-10-17 — r96 re-check (fifth)

Fifth periodic re-check, executed at the r96 closure (2026-10-17). Checker byte pin verified fresh:

```text
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
```

Discriminator pair from the repository root: `python3 corpus/tools/discriminate_check.py` → `RESULT: DISCRIMINATION HELD` (exit 0); `python3 corpus/tools/discriminate_check.py --checker e97613c` → `REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved` (exit 2, expected control).

| Date | Checker SHA-256 | Discrimination re-check |
|---|---|---|
| 2026-10-17 (r96) | `ff9fd2aa…d1421` | **DISCRIMINATION HELD** — re-check 5 (r96 closure): delivered discrimination held; the `e97613c` control reported REGRESSION-DETECTED as expected; ruling retained. Next re-check: r97. |

Gate 3 remains **not met**; the four-gate falsification trigger remains unsatisfied; nothing in r96 changes the sequence-scope evidence state.
````

## 5. Stale-wording list (live claims vs historical sections)

Live claims that must change at closure:
1. `corpus/README.md:36` — "(22 persisted cases)" → 24; "(rounds 94–95)" → 94–96; classes list (§2b).
2. `corpus/README.md:37` — tool list omits `dependency_freeze.py` (§2d).
3. `SKILL.md:87` — "22 cases (r95 added …)" → 24; the "(r95 debt)" `schema_drift` sentence is false after C1(b) → delete.
4. `SKILL.md:89` — residuals "round-95 r96-debt items (deletion class, hidden-second-pointer D1, drift scope)" are superseded by C1.

Historical sections that stay as delivered history (verified, not defects):
5. `corpus/tools/README.md:101-119` Round-95 addendum "22 cases" / "receipt, not a
   gate" — Q2's Round-96 addendum (line 121) explicitly extends and supersedes it
   ("this addendum supersedes the r95 sentence 'The inventory line is a receipt,
   not a gate'"); prior text kept as history, per the addendum pattern. Verified
   the Round-96 addendum covers gating inventory mismatch, `dual_pointer`, the
   24-case self-test, and an "Unchanged" list.
6. `corpus/fixtures/README.md:1190` Round-95 section "22 total" — historical;
   superseded by the Round-96 section (§1), which is still to be appended.
7. `SCORECARD.md:461` "planned (r96)" debt block — superseded by L1's r96 admitted
   section at closure (L1-owned, not a stale claim yet).

## 6. Anomalies / closure action items for L1

- `corpus/tools/dependency-freeze-contract.json` carries a fifth, foreign pin
  `c3red` (`fixture: .ufo/waves/round-96/seats/V41-scratch/c3red`, revision
  `60dba0c…`) written by a verifier `--freeze` probe (Q3 §7 reports it; V22/V33
  receipts quote the pin list including it). Verification semantics are unaffected
  (pins are basename-keyed) but it is a tool hazard and a doc wart: either delete
  `pins.c3red` at closure or add a `--freeze` scope guard refusing paths outside
  `corpus/fixtures/`. The registry row (§3) deliberately does not claim a pin
  count, so it stays true either way.
- Q2 disclosed a brief-vs-implementation divergence: the pinned `inventory_mismatch`
  self-test case is a map over-declaration on an **intact** fixture, not the
  deletion mutation the brief described. Finding/exit identical; the deletion-class
  scenario is gated and verified separately (my §0 before/after, V01, Q1). Closure
  text should say the `inventory_mismatch` behavior is pinned, not that the deletion
  mutation is the pinned case.
- `/tmp` tmpfs/inode exhaustion under the 64-seat load (transient; two failures in
  this seat, one noted by Q2). Harness observation, not a lane defect.

## Bottom line

**PASS** — all six producer artifacts verified present and green on the delivered
revision (`map_obligations` 24/24 self-test, r96 `raw=16 mapped=16`, r96 support
16/16, `dependency_freeze` 14/14 + chain 4/4, census 170/36/134/421/0 validated
against `dcb2d92` 169/35/134/421, C9 pair held + expected control, deletion-class
before/after reproduced), and the five closure-doc targets are inventoried with
exact proposed texts: fixtures README Round-96 section (census 170) ABSENT,
corpus/README bullets stale/absent, SKILL.md `dependency_freeze` registry row ABSENT,
C9 r96 row 5 ABSENT (receipts supplied), stale-wording list classified live vs
historical; one doc-relevant anomaly flagged (`c3red` foreign pin).
