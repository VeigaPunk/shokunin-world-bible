# V39 — integration-checklist (round 97)

**Seat:** V39 integration-checklist (leaf; no nested agents; no commits; no pushes; no network). This report is the only file this seat writes outside its scratch dir `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-97/seats/V39-scratch/`. Every write used an absolute path under the lane repo (the session cwd is the parent `/home/vgpnk/Projects/shokunin`; the r94-F01 stray-write class). All commands run from the lane repo root with `python3`.

**Role per seat spec:** after all seats land, enumerate L1's exact pre-closure checklist with priorities, each item with its evidence source — the round-97 claims C1 (map_obligations pinning hardening), C2 (dependency_freeze hardening + r96 re-freeze), C3 (r97 third beat + r96 cosmetic repair), plus the integration-time doc surfaces, receipt, bookkeeping, and do-not-touch constraints.

**Baseline:** r96 closure `f3e09f9`; lane HEAD `2393934237ea076366f3db6dceeff033edb52ab1` (`2393934`). **Wave:** round-97 single wave, 64 seats (6 producers + 58 verifiers), declaration in the uncommitted `LOG.md` tail.

**At write (18:58; updated ~19:03):** all six producer artifacts + all six producer reports present; 55 seat reports in `.ufo/waves/round-97/seats/` (verifiers still landing); no r97 commit yet (work uncommitted, expected). Verdict seats V30/V32/V34/V25 landed after the first write and are folded in below.

## 0. Poll-wait record

Poll `.ufo/waves/round-97/seats/V39-scratch/poll.sh` (20 s cadence, log `poll.log`; terminated POLL-TIMEOUT at try 40, 18:57:35 — every target below was already observed present by 18:56; the timeout came from my script's multi-line comparison defect, recorded rather than smoothed).

| Target | First present / stable | Status at write |
|---|---|---|
| R1 `map_obligations.py` | 18:45:37, stable `86b52949…` | present + report |
| R2 contract `2142b991…` / `tools/README.md` `6278e59b…` | 18:46:12 / 18:47:13 | present + report |
| R4 r96 map repair (`e851f068…`) / r97 dir (10 files) | 18:43:42 / 18:44 | present + report 18:50 |
| R5 r97 map 17 rows (`49d4834e…`) / README (`d9387b7d…`) | 18:48–18:49 | present + report 18:51 |
| R6 note (`5e3b4225…`, rewritten 18:52:38) | ~18:50 | present + report 18:54 |
| R3 tool `b06275f3…` / contract `27273be2…` | 18:53:00 / 18:55:14, stable | present + report ~18:56 |
| Verifier reports | landing throughout | 37 at write |

Host condition (not a repo finding): `/tmp` inode-exhausted — `df -i /tmp` → `tmpfs 1048576 inodes, 1048576 used, 0 free (100%)` (reproduced; recorded by V09/V26/V30). All my `dependency_freeze --self-test` runs set `TMPDIR=.ufo/waves/round-97/seats/V39-scratch/tmp`; the delivered self-test no longer needs it (R3 moved scratch to `dir=ROOT`).

## 1. Evidence base — my own commands on the delivered revision

All producer-artifact hashes at write (also the hashes to cite in closure docs):

```
86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9  corpus/tools/map_obligations.py
2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41  corpus/tools/map-obligations-contract.json
6278e59b8df01c1cb63ca6080cb959999f400d95128b96e84e5476f4c4ebb992  corpus/tools/README.md
b06275f3bbdeabaab615138b3004703fce701a786af882d3b732828b37722130  corpus/tools/dependency_freeze.py
27273be27d33ad864f06d656f28dca8eabc9d76f6ebe62583372a88c9e64e781  corpus/tools/dependency-freeze-contract.json
e851f068cfd7ed02c97054df18729c4c5a9b8bf60d99d7c9116f427d765440de  corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
49d4834e124fa6cfaa1a73cd5d1a7bc2cb59711c6233b418fe7485a17eedc94f  corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md
d9387b7d73264dfc6c01d27cc6bf24c58ef6bdb4461d2ae8fbfdb6376d9e019f  corpus/fixtures/r97-crossing-acknowledgment/README.md
73063a863a68fc4feae073ce74cfa9e5fddb4f9cc4060d12b333d495a255895b  corpus/fixtures/r97-crossing-acknowledgment/timeline.json
438fb513a62496c41179ead3ea2a55a69ff4ce1fd191c3a7ebccb10651a8dc73  corpus/fixtures/r97-crossing-acknowledgment/sources.json
5e3b4225c30de8a2a75b675b59acb5c597b290e5a45f2caa01663da586e042b5  corpus/knowledge/r97-acknowledgment-scope-note.md
```

Census (my replica `.ufo/waves/round-97/seats/V39-scratch/census_v39.py`, the r95/r96 closure recipe: `python3 corpus/fixtures/check_bible.py corpus/fixtures/<dir>` over sorted top-level dirs, repo-relative argv):

```
{"dirs": 171, "clean": 37, "negative": 134, "other": 0, "violation_lines": 421, "stderr_nonempty": 0}
```

Self-tests / gates (delivered revision):

```
python3 corpus/tools/map_obligations.py --self-test   → SELF-TEST CASES 25/25 pinned … RESULT PASS, exit 0
python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93
  → SNAPSHOT inputs=4 digests=verified / FROZEN expected=PASS/0 findings=none matched / RESULT PASS, exit 0
TMPDIR=… python3 corpus/tools/dependency_freeze.py --self-test   → SELF-TEST 16/16 / RESULT PASS, exit 0
dependency_freeze chain: r88 0 / r94 0 / r95 0 / r96 0, digests 15ef230e…, 2527beb9…, d541ae64…, d422a9b3…
python3 corpus/tools/discriminate_check.py            → RESULT: DISCRIMINATION HELD, exit 0
python3 corpus/tools/discriminate_check.py --checker e97613c → REGRESSION-DETECTED …, exit 2 (expected control)
python3 corpus/tools/boundary_doc_check.py            → CERTIFIED (bounded…), exit 0
python3 corpus/tools/boundary_doc_check.py --self-test → SELF-TEST PASS 8/8, exit 0
sha256sum: check_bible.py ff9fd2aa…d1421; holder-assessment-boundary.md 7f815a93…c33e (pins fresh)
```

map_obligations receipts (delivered): r88 10/10, r93 12/12, r94 14/14, r95 15/15, r96 16/16, r97 17/17 all `RESULT PASS`; r87 and r89 fail-closed `unsupported_map` exit 2.

r97 fixture receipts (delivered):

```
check_bible  → CLEAN: schema, citations, relations, timeline; 0 violations, exit 0
support_check → INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19; DISTINCT-ANCHORS 15/15
                SOURCE-SUPPORT 17/17; EDITORIAL-ANCHORS 2/2; MODES 19/19; VALIDATED-ROWS 19/19 / RESULT PASS, exit 0
map_obligations → OBLIGATIONS raw=17 mapped=17; INVENTORY 17/17; 2/2; 19/19 / RESULT PASS, exit 0
dependency_freeze → UNPINNED-FIXTURE exit 2 by design (chain is the four declared fixtures; R3 §Residuals-2)
```

r96 cosmetic-repair receipt neutrality (my own pre/post run: baseline-map copy from `git show f3e09f9:…` vs delivered, same tools):

```
diff r96-support-pre.txt r96-support-post.txt → IDENTICAL
diff r96-mapobl-pre.txt r96-mapobl-post.txt   → IDENTICAL
git diff f3e09f9 -- …/r96-crossing-response/claim-excerpt-map.md → exactly 2 lines (7-cell delimiter; "new relation" sentence)
```

C2 probes on the delivered tool (safe, no live writes; outputs in `V39-scratch/probe-*.txt`):

```
--freeze .ufo/…/V39-scratch            → FINDING SCOPE-REFUSED … RESULT ERROR, rc=2
--freeze corpus/fixtures               → "refuses corpus/fixtures itself" SCOPE-REFUSED, rc=2
<foreign shadow copy>/r96-crossing-response → FINDING PATH-MISMATCH … RESULT ERROR, rc=2
isolated tree + re-indented sources.json → DIGEST-MISMATCH … changed: sources.json (sha256 9f973f63… -> 9b4b9140…), rc=2
```

## 2. The checklist (priority order)

### P0 — Decide admission before anything is appended (gate)

Per the LOG.md r97 declaration (uncommitted): admit iff C1, C2, C3 each verify on the delivered revision and no axis is harmed; per-axis verdicts, no scalars. Inputs at write:

- depth — `.ufo/waves/round-97/seats/V29-verdict-depth.md` **PASS — improved (bounded)** + `V54-crosscheck-depth.md` PASS.
- calibration — `V31-verdict-calibration.md` **PASS** (C1's three sub-claims independently verified on `86b52949…`/`2142b991…`).
- coverage — `V30-verdict-coverage.md` **PASS (coverage, bounded)** (final write after R3 landed; every C2 item verified on `b06275f3…`/`27273be2…`; its §6 confirms the tools-README doc-parity gap and the r96 digest discrepancy recorded here).
- operability — `V32-verdict-operability.md` **PASS / improved (bounded)** (its D1 bound: the dep self-test now creates transient repo-root scratch — BR-05 spread — and D2: the tools README r97 dep hardening is undocumented).
- freshness — `V25-freshness.md` **PASS** (flags `corpus/fixtures/README.md:1213/1217`, `SKILL.md:87/89`, `corpus/README.md:37/38` as closure-side stale docs, and tools README `:175` as the one within-wave gap).
- adjacency — `V34-verdict-adjacency.md` **PASS** (province-clean; PROVINCE byte-identical; no sibling writes).
- adjudicator — none present at write (r96 had V38). L1 must run the all-axis reconciliation or record its absence, not silently skip it.
- C-claim inputs: C1 R1/R2 + V01/V02/V03/V04/V05/V31/V44; C2 R3 + V07/V08/V09/V11/V45 (and V30 coverage); C3 R4/R5/R6 + V13–V20/V29/V42/V50/V51/V52/V53.

### P1 — `corpus/fixtures/README.md`: append the Round-97 section + census 171 (REQUIRED; pin-affecting)

- Site: EOF, after `:1219` (file is 1219 lines; Round-96 section occupies `:1198-1219`; append-only precedent).
- Required content: third beat of the crossing arc — `aru-acknowledgment-note` + tick-13 `acknowledgment-aru-records` (actor `aru`, place `chalk-stair`, `depends_on: ["response-evin-salt-court"]`); 5/1/5→5/1/6, sources 5→6, 17 map obligations (16 inherited rows unchanged + 1 new event row); receipts measured on the delivered revision (my §1 runs; also R5/R6/R14/V15/V16/V20): `check_bible` CLEAN; `support_check` 17/17 + 2/2 + 19/19 + MODES 19/19; `map_obligations` `raw=17 mapped=17`.
- Also: the r96 cosmetic repair + re-freeze through the guarded `--freeze` path (pin refresh: revision/format; digest measured unchanged — see P6); r96 receipts unchanged by the repair (my IDENTICAL diffs; V19).
- `### 2026-10-17 census re-declaration`: **171 dirs / 37 clean / 134 negative / 421 violation lines / zero non-0/1 exits / zero stderr**, superseding Round-96 (170/36/134/421); one directory added; zero inherited tuples changed (V14/V20/V24-class evidence).
- `Dated pin note:` this append changes the file's bytes; the W05 pin no longer matches (fourth consecutive round).
- Dated correction (append-only, do not rewrite r96 text): the `:1213` "Known cosmetic debts (no gate reads them; r97 candidates)" sentence is resolved by R4's repair this round.
- Evidence sources: my §1 runs; `V26-doc-parity.md` §2.4–2.5/§3.1; `V19-c3-r96-repair-scope.md`; `R4-fixture-author.md`; `R3-freeze-hardening.md`; `V14/V20`.

### P2 — `corpus/README.md`: three bullets (REQUIRED; pin-neutral)

1. Insert the r97 fixture bullet after the r96 bullet (`:23`) — pattern of `:22-23`.
2. `:37` `tools/map_obligations.py` — "(rounds 94–96)" → "(rounds 94–97)"; "24 persisted cases" → "25 persisted cases"; note the strict loader (any missing pinned case fails closed) and that `dual_pointer` is pinned.
3. `:38` `tools/dependency_freeze.py` — "(round 96)" → "(rounds 96–97)"; "14-case" → "16-case"; add the guard/path-binding/digest-naming note (`--freeze` restricted to `corpus/fixtures/**`; same-named copy at a foreign path exits 2 `PATH-MISMATCH`; `DIGEST-MISMATCH` names the changed file).
- Evidence sources: `V26-doc-parity.md` §3.2; `corpus/tools/README.md:177-208` (R2 addendum); my self-test runs; `R3-freeze-hardening.md`.

### P3 — `corpus/knowledge/r91-c9-watch.md`: append row 6 (REQUIRED; unowned — no producer byte-owns this file)

- Site: EOF after `:289`; the r96 row ends "Next re-check: r97". Append the sixth re-check using **V48's listed block verbatim** (`V48-pins-c9.md` §4; draft `V48-scratch/row6-block-draft.md`): dated section + cumulative table row (r92=1 … r96=5 → this is row 6), checker pin `ff9fd2aa…d1421`, discriminator pair (`DISCRIMINATION HELD` exit 0; `e97613c` control `REGRESSION-DETECTED` exit 2), "Next re-check: r98", gate 3 remains **not met**.
- Evidence sources: `V48-pins-c9.md` §1–§5; `V23-gates-boundary.md` §3–§4; my §1 runs.

### P4 — `SKILL.md`: refresh both gate-registry rows (REQUIRED; unowned extra finding)

- `map_obligations` row (`:83-90`): `:87` "24 cases … `dual_pointer` … not pinned … 23/24 still passes — both r97 debt" → **25 cases**, debts closed (loader strict; `dual_pointer` pinned as the 25th case); `:89` scope "(r93–r96 clusters)" → include r97, and update the residual list (per the tools README addendum only BR-16 / BR-05 scratch remain).
- `dependency_freeze` row (`:92-101`): `:96` entry — note the `--freeze` scope guard; `:98` "14 cases" → **16 cases**; `:100` scope — drop "Not path-bound (a same-named copy verifies identically)", "(no scope guard — r97 debt)", "`DIGEST-MISMATCH` does not name the changed file"; state guarded/path-bound/naming facts; add exit-2 classes `SCOPE-REFUSED` / `PATH-MISMATCH` (+ `CONTRACT-INVALID` for out-of-scope pin paths).
- Evidence sources: `V26-doc-parity.md` §3.3; `R3-freeze-hardening.md`; `corpus/tools/README.md:177-208`; my §1 runs.

### P5 — `corpus/tools/README.md`: Round-97 C2 addendum (REQUIRED; currently MISSING)

- State: `:175` still says self-test "14/14" and lists the three r96 hazards as open (`--freeze` no scope guard; receipts not path-bound; `DIGEST-MISMATCH` does not name the changed file); the Round-97 addendum at `:177-208` covers only `map_obligations`. R2's report does not mention `dependency_freeze`; R3's report records the gap as an open doc-parity item (byte-ownership is R2's).
- Required: a dependency_freeze Round-97 section (or an extension of the existing addendum) documenting the scope guard (`SCOPE-REFUSED`, no write on refusal, symlink + same-named-shadow refusals), path binding (`PATH-MISMATCH`), `DIGEST-MISMATCH` naming, the 16-case self-test, and the r96 re-freeze/format note; the `:175` hazard list must be superseded (keep earlier text as delivered history, addendum framing).
- Evidence sources: `R3-freeze-hardening.md` §Residuals-1 (records the gap); `V26-doc-parity.md` §3.5; my probes (§1).

### P6 — r96 re-freeze / pin refresh (DONE by R3; L1 verifies + records one claim discrepancy)

- Delivered contract `27273be2…`: top-level `revision` and the `r96-crossing-response` pin `revision` → `2393934…`; `content_sha256` **unchanged** (`d422a9b3…`); other three pins byte-identical; `provenance_note` (c3red removal) preserved; `self_test.expected` = 16 cases. Re-freeze ran through the guarded `--freeze corpus/fixtures/r96-crossing-response` (R3 §"Pin refresh"; my contract inspection + chain 4/4).
- **Claim discrepancy to record in LOG/SCORECARD (R3 §"Recorded discrepancy"):** the freeze digest covers only the five JSON tables (`DATA_FILES`), and R4's repair touched only `claim-excerpt-map.md`, so the digest did **not** change; the refresh is a guard/format/revision refresh through the guarded path, not a digest change. The declaration's "pin refresh … demonstrating the guard end-to-end" holds; any reading that the digest moved is inaccurate.
- Formatting: the writer's `indent=2` reindented the whole contract (`+366/-352` numstat), content-preserving.
- Evidence sources: `R3-freeze-hardening.md`; my §1 (contract inspection, chain 4/4, probes); `V45-c2-guard-2.md`; `V09-c2-selftest.md`.

### P7 — receipt fill, bookkeeping, and commit split

- **Receipt:** `.ufo/waves/round-97/` contains only `seats/` (no `receipt.json`, no wave-spec). L1 fills the receipt from the dispatch result with **real agent IDs** (r95/r96 precedent: do not invent; record late/absent seats and duplicate-seat files). At write the seat-report roster is 37 files (R1–R6 + 31 verifiers); more verifier seats are still landing.
- **Commits:** no seat committed (lane `git log` still ends `2393934`; all round work is worktree/untracked). L1 follows the r96 split: one admitted-wave commit (docs/registry/census/C9/receipt) + one closure commit (SCORECARD + LOG).
- **Strays (r94-F01 class):** parent repo `git status --porcelain` empty; no parent `.ufo/waves/round-97/`; all round writes are in-lane and confined to declared paths (`git status`: `M LOG.md`, `M corpus/fixtures/r96-crossing-response/claim-excerpt-map.md`, `M corpus/tools/{map_obligations.py,map-obligations-contract.json,README.md,dependency_freeze.py,dependency-freeze-contract.json}`, `?? corpus/fixtures/r97-crossing-acknowledgment/`, `?? corpus/knowledge/r97-acknowledgment-scope-note.md`, `?? .ufo/waves/round-97/`).
- **Scratch hygiene:** V48 observed transient `map-obligations-self-test-*` dirs under the repo root (auto-removed; explained by the tool's `dir=ROOT`); R3's self-test uses `dir=ROOT` too and leaves nothing behind (V32 D1 records the BR-05 spread: the dep self-test now creates transient repo-root scratch — self-cleaning, none persisting). Check `ls -d map-obligations-self-test-* dependency-freeze-self-test-*` is empty at closure.
- **SHONEN:** four `[~]`, zero `[x]` (V36 PASS, checker 10/10 exit 0); no promotion, no push; PROVINCE byte-identical.
- Evidence sources: my `git`/`ls` checks; `V36-shonen-format.md`; `V48-pins-c9.md` §Bounds; `R3-freeze-hardening.md`.

### P8 — Do-not-touch constraints (verified this round)

- `corpus/knowledge/holder-assessment-boundary.md` `7f815a93…c33e` and `corpus/fixtures/check_bible.py` `ff9fd2aa…d1421` are whole-file pinned; V23 §5 shows all 19 boundary-pinned paths byte-identical to `f3e09f9` (my hashes agree). No r97 doc edit may touch them.
- C9 pinned set (`check_bible.py`, `discriminate_check.py`, the two r91 fixtures, the watch file) diff-clean vs `f3e09f9` (V48 §1/§5; my discriminate runs).
- Frozen r93 snapshot replay stays `RESULT PASS` (my run; P1 receipts above).
- `SHONEN.md`, `PROVINCE.md`, `SKILL.md`, `corpus/README.md`, `corpus/fixtures/README.md`, `corpus/knowledge/r91-c9-watch.md` are producer-untouched (`git diff --stat f3e09f9` empty on all six) — they are integration-time files for L1.

### P9 — Errata and notes for the closure record

1. The P6 digest discrepancy (record it; do not re-roll the claim).
2. V30 coverage verdict landed **PASS** after the first write (folded into P0) — no longer outstanding.
3. Host condition: `/tmp` inode exhaustion this round (V09/V26/V30; my measurement) — record as a host condition, not a repo finding (r96 precedent).
4. `r97-acknowledgment-scope-note.md` (`5e3b4225…`) cites the delivered `map_obligations.py 86b52949…` with the earlier `70795150…` run noted as history and a standing "re-run before citing" caveat — no erratum strictly needed; receipts re-verify on the delivered revision (my §1).
5. r97 fixture is deliberately not added to the freeze chain (chain stays 4/4); pinning it is an r98 candidate (R3 §Residuals-2).

## 3. Verification boundary

This seat ran read-only checks plus scratch-only probes (census sweep, self-tests, gates, receipts, `git`, `sha256sum`, isolated-tree freeze probes); it implemented nothing and edited no corpus, tool, or sibling artifact. Every cited output is from a command quoted in §1 or from a named seat report; the one item not yet satisfiable is marked (P5, the tools-README C2 doc half); the verdict seats that landed after the first write (V30 coverage, V32 operability, V34 adjacency, V25 freshness) are folded in. No axis verdict is issued here — P0 is an input list for L1's admission ruling.

**Bottom line: PASS (checklist produced; one integration item outstanding)** — the prioritized pre-closure checklist is enumerated with exact sites and evidence sources: P0 admission inputs (depth V29/V54 PASS, coverage V30 PASS, calibration V31 PASS, operability V32 PASS, freshness V25 PASS, adjacency V34 PASS; adjudicator absent at write — L1 runs it or records), P1 fixtures-README Round-97 append + census 171/37/134/421/0 + r96 repair correction (my sweep; V26/V19/R4/R3), P2 corpus/README bullets `:23/:37/:38`, P3 C9 row-6 append from V48 §4, P4 SKILL.md rows `:87/:89/:96-100`, P5 tools README C2 half **MISSING** (R3 §Residuals-1; V26 §3.5; V30 §6; V25 §flag), P6 re-freeze verified (revision/format refresh; digest measured unchanged — recorded discrepancy), P7 receipt/bookkeeping/commit split (55 seat reports at final write; BR-05 spread bound from V32 D1), P8 do-not-touch pins, P9 errata (digest discrepancy; `/tmp` host condition).
