# V47 — receipt-wording (round 97, verifier seat)

- **Seat:** V47 receipt-wording. Lane: `/home/vgpnk/Projects/shokunin/lore-shokunin`
  (session cwd is the parent repo; every command below ran from the lane repo root with
  `python3`; this report is the seat's only write, at the absolute path above, plus
  `.ufo/waves/round-97/seats/V47-scratch/`).
- **Baseline:** r96 closure `f3e09f9` (HEAD observed `2393934`). **Round claims audited:**
  the declared ratios 17/17 obligations vs TOTAL 19/19; 25/25; 16/16; 4/4; census 171
  (plus the before/after pairs 24→25, 14→16, 170→171, 5/1/5→5/1/6, sources 5→6, 16 inherited
  map rows, "today 23/24 passes", "today verifies identically").
- **Poll-wait:** all six producer reports absent at seat start (only R2/R4/R5 scratch dirs
  existed; `corpus/fixtures/r97-crossing-acknowledgment/` did not exist). Background poll
  (20 s × 40) hit `READY` at try=37 (18:56:37) with all 10 fixture files and R1–R6 reports
  present. Every measurement below was re-run after the last producer report landed; no plan
  was ever verified.

## 1. Declared ratios vs measured outputs (delivered revision)

| Declaration | Measured | Verdict |
|---|---|---|
| 25/25 (`map_obligations` self-test, contract 24→25) | `SELF-TEST CASES 25/25 pinned`, 25 `SELF-TEST PASS` lines, 0 FAIL, `RESULT PASS`, exit 0; contract sha `2142b991…` has 25 cases, last id `dual_pointer` | TRUE |
| 17/17 obligations vs TOTAL 19/19 (r97 fixture) | `OBLIGATIONS raw=17 mapped=17` / `INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19` / `RESULT PASS`, exit 0 | TRUE |
| 16/16 (`dependency_freeze` self-test, 14→16) | 16 `CASE` lines, `SELF-TEST 16/16`, `RESULT PASS`, exit 0; contract sha `27273be2…` has 16 expectations, new ids `path_mismatch`, `scope_refused` | TRUE |
| 4/4 chain clean | r88 `15ef230e…` / r94 `2527beb9…` / r95 `d541ae64…` / r96 `d422a9b3…` all `RESULT PASS` exit 0 | TRUE |
| census 171 (170→171) | 171 fixture dirs / 37 clean / 134 negative / 421 `VIOLATION` lines / 0 non-0/1 exits | TRUE |
| 5/1/5→5/1/6, sources 5→6 | r96: entities 5, relations 1, timeline 5, sources 5; r97: 5/1/6, sources 6; inherited rows parsed-equal (`timeline[:5] == r96`, `sources[:5] == r96` both `True`) | TRUE |
| 17 obligations = 16 inherited unchanged + 1 new event | J01–J16 differ from the r96 map only in the path-qualification column; J17 `timeline.json#/5` → `aru-acknowledgment-note` is the only new row; 5 copied files byte-identical (`cmp`) | TRUE |
| "today 23/24 passes" (C1 before-state) | r96 tool (`git show f3e09f9:…`) + 23-case contract → `SELF-TEST CASES 23/24 pinned` / `RESULT PASS` **exit 0**; delivered tool on the same contract → exit 2 `FINDING self_test_contract: contract drops implemented self-test cases: dual_pointer, schema_drift` | TRUE |
| "today verifies identically" (C2b before-state) | r96 tool in a mirror root on a byte-identical same-named copy at a foreign path → `RESULT PASS` **exit 0**; delivered tool on the same copy → exit 2 `PATH-MISMATCH` | TRUE |
| r96 receipts unchanged by the cosmetic repair | r96 `map_obligations` `raw=16 mapped=16` / `16/16; 2/2; 18/18` / PASS exit 0; r96 `support_check` `16/16` + `TOTAL-ROWS 18` / PASS exit 0; r96 `check_bible` CLEAN exit 0 | TRUE |

Supporting receipts measured the same pass: r97 `support_check` `RECEIPT JSON-FACTS 17; EDITORIAL-ROWS 2; TOTAL-ROWS 19` / `SOURCE-SUPPORT 17/17; EDITORIAL-ANCHORS 2/2; MODES 19/19; VALIDATED-ROWS 19/19` / `RESULT PASS` exit 0; r97 `check_bible` `CLEAN: schema, citations, relations, timeline; 0 violations` exit 0; `boundary_doc_check.py` CERTIFIED exit 0; `discriminate_check.py` `DISCRIMINATION HELD` exit 0.

Producer report shas all reproduce exactly: `map_obligations.py` `86b52949…` (R1/R2), `map-obligations-contract.json` `2142b991…` (R2), `README.md` `6278e59b…` (R2), `dependency_freeze.py` `b06275f3…` (R3), `dependency-freeze-contract.json` `27273be2…` (R3).

## 2. Independent probes (V47-scratch/probes.py, `probes-out.txt`)

```
== A: foreign-path same-named copy ==
$ python3 corpus/tools/dependency_freeze.py .ufo/.../V47-scratch/probeA/foreign/r94-paired-crossing
FINDING PATH-MISMATCH: pin r94-paired-crossing names corpus/fixtures/r94-paired-crossing (resolves to …/corpus/fixtures/r94-paired-crossing); invoked fixture resolves to …/probeA/foreign/r94-paired-crossing
RESULT ERROR            exit=2

== B: --freeze outside corpus/fixtures ==
$ python3 corpus/tools/dependency_freeze.py --freeze .ufo/.../V47-scratch/probeB/target
FINDING SCOPE-REFUSED: --freeze refuses …/probeB/target; the frozen scope is corpus/fixtures/** (integration-time operation only)
RESULT ERROR            exit=2     contract unchanged: True (sha before == after)

== C: mirror-root prose drift (edge inventory untouched) ==
FINDING DIGEST-MISMATCH: content digest 9711a1c1… != pin 2527beb9…; changed: timeline.json (sha256 f0209f90… -> 20bb964e…); fixture bytes changed outside the frozen inventory
RESULT ERROR            exit=2

== D: loader before/after (23-case contract) ==
r96 tool      -> SELF-TEST CASES 23/24 pinned / RESULT PASS / exit 0
delivered tool-> FINDING self_test_contract: contract drops implemented self-test cases: dual_pointer, schema_drift / exit 2
```

Census method validation: my harness (repo-relative `corpus/fixtures/<name>` args, `VIOLATION`-line count) reproduces the declared r96 census exactly — 170 dirs / 36 clean / 134 negative / 421 lines / 0 odd — before r97 landed; the final run gives 171 / 37 / 134 / 421 / 0 (clean +1 = the new clean fixture, negative and line counts unchanged). No stray self-test dirs at the repo root; `git status` shows only the six producer-owned files plus `LOG.md` (declaration) modified, and the r97 fixture/knowledge note/wave dir untracked.

## 3. Corrections list for L1

All numeric declarations audited are accurate; the corrections are stale-doc / wording items:

1. **`SKILL.md:87`** — still "24 cases (r96 added `schema_drift`, `inventory_mismatch`)" and still carries the now-closed note "`dual_pointer` behavior is demonstrated by mutation demos, not pinned by a persisted case; the two r96-added pins are droppable under the subset-tolerant loader (23/24 still passes) — both r97 debt". Update to 25 cases and strike/close the residual sentence (line 86 already lists `dual_pointer`).
2. **`corpus/README.md:37`** — "`--self-test` (24 persisted cases)" → 25.
3. **`corpus/tools/README.md:175`** — the `dependency_freeze` paragraph still says self-test "14/14" and still lists three closed hazards ("`--freeze` has no scope guard", "receipts are not path-bound (a same-named copy at a foreign path verifies identically)", "`DIGEST-MISMATCH` does not name the changed file"); the new ids `SCOPE-REFUSED` / `PATH-MISMATCH` / `CONTRACT-INVALID` are undocumented. R2 owns this file and its report does not mention `dependency_freeze` (R3's report flags the same gap); needs a Round-97 freeze-tool addendum or a doc-parity owner at closure.
4. **`corpus/fixtures/README.md:1217`** — census text still states the r96 census (170 dirs). Measured r97: 171 dirs / 37 clean / 134 negative / 421 violation lines. Read-only this round (no producer owns it) → closure-side append, as with the r95/r96 census re-declarations.
5. **`LOG.md` C2(b) wording nuance (not an error):** "pins record the fixture's repo-relative path and verify compares the invoked path" — the `fixture` field already existed in the r96 contract (`c65ac3bd…`); r97 adds read-time pin validation plus verify-time enforcement. Optional tightening if the declaration is re-read strictly.
6. **`LOG.md` C2 "(pin refresh)" — digest did not change.** Measured semantic contract diff vs `f3e09f9`: pins 4→4, three pins byte-identical, r96 pin changed **only** in `revision` (`60dba0c2…` → `2393934…`), `content_sha256` stays `d422a9b3…` (the repair touched only `claim-excerpt-map.md`, which is not a pinned data file); top-level `revision` likewise `60dba0c2…` → `2393934…`. The LOG declaration makes no digest claim, so no erratum is required — but the closure record should state that the refresh is a revision/guard refresh with an unchanged digest (R3's report already records this; the seat-prompt parenthetical "digest changes by the repair" was inaccurate).
7. **Pin revisions now name HEAD `2393934`** (the r96 closure commit). If the closure pass re-freezes, the `revision` fields move again; expected, worth one line in the closure note so the r97 receipt records the revision it was measured at.

## 4. Bounds / non-claims

- I audited declared ratios and receipt wording only; I do not adjudicate C1/C2/C3 semantics beyond the receipts above, entailment, canon, chronology, or the R4/R5 fixture's literary reading.
- Census counts directories; it is a measured snapshot, not a pinned invariant (same convention as the r95/r96 re-declarations).
- My census `VIOLATION`-line rule was calibrated against the declared r96 number (421) before use; it counts `VIOLATION`-prefixed stdout lines only.
- All my scratch lives under `.ufo/waves/round-97/seats/V47-scratch/`; no writes outside this report and that directory; no commits, no network, no nested agents.

## Bottom line

**PASS** — every declared ratio reproduces on the delivered revision (map self-test 25/25 exit 0; r97 `raw=17 mapped=17` / `TOTAL-ROWS 19/19` exit 0; freeze self-test 16/16 exit 0 with contract 14→16; chain 4/4 clean; census 171 dirs / 37 clean / 134 negative / 421 lines; before-states "23/24 passes" and "foreign copy verifies identically" both reproduced against the r96 tool), with seven stale-doc/wording corrections listed for L1 — none of which contradict a measured declaration.
