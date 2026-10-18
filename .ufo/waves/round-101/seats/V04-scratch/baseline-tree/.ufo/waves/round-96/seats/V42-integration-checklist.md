# V42 — integration-checklist (round 96)

Seat: V42 integration-checklist. Scope: L1's exact pre-closure checklist for r96
(C1 calibration, C2 depth, C3 coverage) with evidence sources and measured numbers.
All commands run from `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`.
Baseline `dcb2d92`; working-tree HEAD at verification time `60dba0c`
(`LOG.md` modified by the round declaration; no commits made by this seat).
Scratch: `.ufo/waves/round-96/seats/V42-scratch/` (harness, baseline copies, mutation copies).

## Delivered revision fingerprint (stable over a 25 s re-hash probe)

| Artifact | sha256 |
|---|---|
| `corpus/tools/map_obligations.py` | `2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8` |
| `corpus/tools/map-obligations-contract.json` | `97b76bb8b1fea97f166ef7586eba69c427ec15bbe7b34eb5345ec65c936493b6` |
| `corpus/tools/README.md` | `965b29cd41a8af14293eb2e1948f58f310e58c6e752b8fe322c5445b20a91f24` |
| `corpus/tools/dependency_freeze.py` | `a3b57978f0cbf314389ee3f9862920a46cf109fca6d1eec488c39be0457f0980` |
| `corpus/tools/dependency-freeze-contract.json` | `7d568cc422cda42297b7506a1a3e083e8798866efd16d58617bf4ea468576975` |
| `corpus/knowledge/r96-response-scope-note.md` | `6db32ca24f5eff5baa3ebe589e8d3bcb6b256fec18dee2468211d7d0fae157c6` |
| `corpus/fixtures/r96-crossing-response/claim-excerpt-map.md` | `5093d72eb3f22b249033d7ac4c1a85c7df7f5e09bfa673a598aee6a83045bfd8` |
| `corpus/fixtures/r96-crossing-response/README.md` | `ff52ced48bf4214721f248328d76da64a42773d44e78154ef1eaf6eb3558c456` |
| `corpus/fixtures/r96-crossing-response/timeline.json` | `ea0225f9270db79685ea6f55828c2031d7ac67cd413b04f28b25770b208815b9` |
| `corpus/fixtures/r96-crossing-response/sources.json` | `9f973f634cf325a33047020407ffb67b0a0f0a1643e507ebd3771abf9fabf32d` |

Baseline tool for the "before" runs is reproducible via
`git show dcb2d92:corpus/tools/map_obligations.py` (sha256 `d1c239cc…`, verified by Q4's report).

All six producer reports are filed: `Q1-tool-hardening.md`, `Q2-contract-docs.md`,
`Q3-dependency-freeze.md`, `Q4-fixture-json.md`, `Q5-fixture-docs.md`, `Q6-knowledge-note.md`.

## C1 — calibration: map_obligations hardening bundle

| # | Check | Command | Observed | Verdict |
|---|---|---|---|---|
| C1a | deletion class is gating (before) | `git show dcb2d92:… > /tmp/tool.py`; scratch copy of `r95-crossing-aftermath` with entity 0 `claims` deleted + its `entities.json#/0/claims/0` map row removed | `INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/17 MISMATCH` / `RESULT PASS` / **exit 0** | defect reproduced |
| C1a | deletion class is gating (after) | same mutation on a copy of `corpus/fixtures/r96-crossing-response`; `python3 corpus/tools/map_obligations.py <copy>` | `OBLIGATIONS raw=15 mapped=15` / `INVENTORY JSON-FACTS 15/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/18 MISMATCH` / `FINDING inventory_mismatch: declared JSON-facts/editorial-rows/total-rows 16/2/18; observed 15/2/17` / `RESULT FAIL` / **exit 1** | PASS |
| C1b | self-test pins both new cases | `python3 corpus/tools/map_obligations.py --self-test` | `SELF-TEST CASES 24/24 pinned`, 24 `SELF-TEST PASS` lines, 0 FAIL, `RESULT PASS`, **exit 0**; `SELF-TEST PASS schema_drift exit=1 findings=['schema_drift']`; `SELF-TEST PASS inventory_mismatch exit=1 findings=['inventory_mismatch']` | PASS |
| C1b | contract 22 → 24 | `python3 -c "…len(c['self_test']['cases'])"` | 24 ids, includes `schema_drift` {exit 1, `['schema_drift']`} and `inventory_mismatch` {exit 1, `['inventory_mismatch']`} | PASS |
| C1c | dual pointer (before) | baseline tool on `r88-m3-maya-cluster` copy with cell `` `entities[0].claims[0]`: … (see also `entities[1].first_appearance`) `` | `RESULT PASS` / **exit 0** | defect reproduced |
| C1c | dual pointer (after) | same mutation, delivered tool | `FINDING dual_pointer: row E1 (line 27) names a second pointer token 'entities[1].first_appearance' alongside entities.json#/0/claims/0` / `RESULT FAIL` / **exit 1** | PASS |
| C1 | non-regression matrix | `map_obligations.py corpus/fixtures/<d>` for r87/r88/r89/r93/r94/r95/r96 | r87 **exit 2** (fail-closed), r88 `10/10` exit 0, r89 **exit 2** (fail-closed), r93 `12/12`, r94 `14/14`, r95 `15/15`, r96 `16/16` — all exit 0, identical to baseline | PASS |
| C1 | frozen r93 replay | `map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93` | `SNAPSHOT inputs=4 digests=verified` / `12/12` / `FROZEN expected=PASS/0 findings=none matched` / exit 0 | PASS |

**Bound (measured, disclosed):** a *consistent regeneration* — deletion of the claims key
and map row **with** the `**Expected inventory:**` line updated to match (15/2/17) — still
prints `RESULT PASS` exit 0. The new gate keys on declared-vs-observed mismatch; a
self-consistent edit remains invisible to it (as the round declaration itself frames it).
The declared anchor count stays a receipt field only (README r96 addendum, line 144).

## C2 — depth: `corpus/fixtures/r96-crossing-response/`

| # | Check | Command / source | Observed | Verdict |
|---|---|---|---|---|
| C2 | counts 5/1/5 + 5 sources | `json.load` of the five tables | entities 5, relations 1, timeline 5, sources 5, contradictions 0 (r95: 5/1/4/4) | PASS |
| C2 | new event shape | timeline[4] | `response-evin-salt-court`, tick 12, entity `evin`, place `salt-court`, `depends_on ["aftermath-missing-evin"]`, source `evin-response-note` | PASS |
| C2 | preserving copies | `cmp` r95 vs r96 | byte-identical: `entities.json`, `relations.json`, `contradictions.json`, `inspiration-note.md`, `source-excerpt.md`; `fictional-excerpts.md` strict byte-prefix 1845 → 2588 B (note appended) | PASS |
| C2 | 16 obligations, 15 inherited unchanged | row parse of both maps (cluster path normalized) | 17 common rows (15 facts + 2 editorial) with **0 field differences**; exactly **1** new row `J16` (`timeline.json#/4`); declared `16 JSON facts; 2 editorial; 18 total; 14 anchors` | PASS |
| C2 | gate receipts | `map_obligations.py corpus/fixtures/r96-crossing-response` | `OBLIGATIONS raw=16 mapped=16` / `INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18` / `RESULT PASS` exit 0 | PASS |
| C2 | source support | `support_check.py corpus/fixtures/r96-crossing-response` | `SOURCE-SUPPORT 16/16; EDITORIAL-ANCHORS 2/2; MODES 18/18; VALIDATED-ROWS 18/18` / `RESULT PASS` exit 0 | PASS |
| C2 | bible check | `check_bible.py corpus/fixtures/r96-crossing-response` | `CLEAN: schema, citations, relations, timeline; 0 violations` exit 0 | PASS |
| C2 | census 169 → 170 | loop `check_bible.py corpus/fixtures/<d>` over all dirs with `entities.json` | **170 dirs: 36 clean / 134 negative / 0 other** (r95 closure: 169 / 35 / 134) | PASS |
| C2 | unresolved, no contradiction asserted | `contradictions.json` (empty list) + note/README text | note states no accusation, no winner, both accounts stand unresolved; README states the two accounts name different actors at different places, so no contradiction is asserted | PASS |

## C3 — coverage: `dependency_freeze.py` + contract (BR-01 closure)

| # | Check | Command | Observed | Verdict |
|---|---|---|---|---|
| C3 | chain 4/4 clean | `dependency_freeze.py corpus/fixtures/<d>` for r88-m3 / r94 / r95 / r96 | r88 `events 2/2; edges 0/0; rel 0/0`; r94 `3/3; 2/2; 1/1`; r95 `4/4; 3/3; 1/1`; r96 `5/5; 4/4; 1/1` — all `RESULT PASS` exit 0 | PASS |
| C3 | self-test persisted | `dependency_freeze.py --self-test` | `SELF-TEST 14/14` / `RESULT PASS` exit 0 | PASS |
| C3 | BR-01 mutation | copy of r94 with `evin-ninth-bell` dropped from `paired-crossing-decision.depends_on` | `dependency-edges 1/2` / `FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']` / exit **1** | PASS |
| C3 | addition | phantom edge added | `FINDING ADDITION-DETECTED: … gained depends_on ['aftermath-missing-evin']` / exit 1 | PASS |
| C3 | endpoint change | relation `from`/`to` flipped | `FINDING ENDPOINT-CHANGE: relation endpoints changed: removed [aru, evin, agreed_co_stewardship_for_this_crossing]; added [evin, aru, …]` / exit 1 | PASS |
| C3 | event endpoint change | tick 10 → 11 | `FINDING ENDPOINT-CHANGE: event paired-crossing-decision.tick: 10 -> 11` / exit 1 | PASS |
| C3 | could-not-evaluate | cosmetic byte change (unmodelled digest) | `FINDING DIGEST-MISMATCH: …` / `RESULT ERROR` exit 2; unpinned/missing dir → `UNPINNED-FIXTURE` exit 2 | PASS |
| C3 | zero corpus modifications | `git diff --stat HEAD -- corpus/fixtures` and `git status --porcelain` | diff **empty**; only untracked additions are `dependency_freeze.py`, `dependency-freeze-contract.json`, `r96-crossing-response/`, `r96-response-scope-note.md`; modified: `LOG.md`, `corpus/tools/{README.md,map_obligations.py,map-obligations-contract.json}` (C1/Q2 scope) | PASS |

BR-01 "before" evidence (captured while the baseline gates were still green): the same
`evin-ninth-bell` drop on an r94 copy printed `map_obligations` `14/14 RESULT PASS` exit 0,
`check_bible` `CLEAN … 0 violations` exit 0, and `support_check` `SOURCE-SUPPORT 14/14`
`RESULT PASS` exit 0 — three green gates, exactly the carried debt.

## Integration items for L1's pre-closure list

- **Existing battery unharmed:** `boundary_doc_check.py` → `CERTIFIED (bounded: …)` exit 0;
  `discriminate_check.py` → `RESULT: DISCRIMINATION HELD …` exit 0.
- **Producer self-test hazard closed mid-round:** the first delivered `dependency_freeze.py`
  printed `SELF-TEST 5/14` exit 1; the 9 failures all replayed against
  `…/missing_timeline/r95-crossing-aftermath` (per-case lambdas captured `scratch` by
  reference — late binding). Q3's report records the same defect and the fix; the delivered
  revision is 14/14 PASS (hashes above). This is a *fixed* defect, not an open one.
- **Pin keys are basenames:** `pin_for()` uses `fixture.resolve().name`, so a mutation copy
  named anything other than the fixture's own name exits 2 `UNPINNED-FIXTURE`. Mutation
  probes must keep the basename (my first probe hit this; reported for the record).

## Anomalies and bounds (open)

1. **Foreign pin `c3red` in the delivered contract.** `corpus/tools/dependency-freeze-contract.json`
   carries `pins.c3red` with `fixture: ".ufo/waves/round-96/seats/V41-scratch/c3red"` —
   written by a verifier's `--freeze` probe, not by a producer. `--freeze <dir>` accepts
   paths outside `corpus/fixtures/` and rewrites the delivered contract. Harmless to
   verification semantics (pins are basename-keyed; no corpus fixture is named `c3red`), but
   it is a real scope hazard and a delivered-file artifact. Q3 reported it and left it in
   place because V22/V33 receipts quote the pinned list. Recommend deletion at closure or a
   `--freeze` scope guard for r97.
2. **C1 bound:** consistent regeneration of a deleted claims key + row (declaration updated)
   still exits 0 (see C1 table).
3. **BR-05 remains open and documented:** the `map_obligations` self-test scratch is created
   under the repository root and is not gitignored (README r96 addendum line 123 says
   "unchanged in r96"). A clean `--self-test` run left no residual directory (verified
   immediately after a run), but a concurrent mid-run snapshot showed
   `?? map-obligations-self-test-_4j0rfkn/` transiently.

## Bottom line

PASS — every checklist item for C1, C2 and C3 verifies on the delivered revision
(hashes above): C1 gating `inventory_mismatch` exit 1 and `dual_pointer` exit 1 with the
24-case self-test green and the r87–r96/frozen-r93 matrix unchanged; C2 counts 5/1/5 + 5
sources, 15 inherited rows field-identical + 1 new row, `raw=16 mapped=16`, `check_bible`
CLEAN, census 170/36/134/0; C3 chain 4/4 clean, BR-01 mutation `REDUCTION-DETECTED` exit 1,
addition/endpoint exit 1, digest/unpinned exit 2, 14/14 self-test, zero corpus modifications
beyond the two new tool files — with one open anomaly (foreign `c3red` pin in the delivered
contract) and one measured C1 bound (consistent regeneration exits 0).
