# V37 — debt-ledger (round 97)

**Seat:** V37 debt-ledger. **Role:** after the round's seats land, compile the round's named bounds/debt into one honesty ledger — no re-adjudication, no axis score, no smoothing. Every item below is a bound, residual, carry-over, closure item or process observation that some seat or this seat named with evidence; nothing is inferred beyond what the pointers support.

**Compiled at:** 2026-10-17 ~19:11 -03 (**v1**). Lane root `/home/vgpnk/Projects/shokunin/lore-shokunin`; HEAD `2393934237ea076366f3db6dceeff033edb52ab1` (`2393934` r96 close; baseline `f3e09f9`). Worktree at compile (exactly the declared producer set + the declaration):

```
 M LOG.md                                          (round-97 declaration, +61)
 M corpus/fixtures/r96-crossing-response/claim-excerpt-map.md   (R4 repair, 2/2 lines)
 M corpus/tools/README.md                          (R2, +49)
 M corpus/tools/dependency-freeze-contract.json    (R3)
 M corpus/tools/dependency_freeze.py               (R3)
 M corpus/tools/map-obligations-contract.json      (R2)
 M corpus/tools/map_obligations.py                 (R1)
?? .ufo/waves/round-97/
?? corpus/fixtures/r97-crossing-acknowledgment/
?? corpus/knowledge/r97-acknowledgment-scope-note.md
```

**Poll-wait record (my own):** background poll 20 s × 40 (`V37-scratch/poll.sh`, log `V37-scratch/poll.log`) — `ALL-PRESENT at try 38` (18:56:31): all six producer artifacts + all six producer reports. Never verified a plan; every number below was re-run on real files.

**Delivered revision pinned by this seat** (sha256, re-measured at compile 19:10):

- `corpus/tools/map_obligations.py` `86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9`
- `corpus/tools/map-obligations-contract.json` `2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41` (25 cases)
- `corpus/tools/README.md` `6278e59b8df01c1cb63ca6080cb959999f400d95128b96e84e5476f4c4ebb992` (+49 Round-97 addendum, additive only)
- `corpus/tools/dependency_freeze.py` `b06275f3bbdeabaab615138b3004703fce701a786af882d3b732828b37722130`
- `corpus/tools/dependency-freeze-contract.json` `27273be27d33ad864f06d656f28dca8eabc9d76f6ebe62583372a88c9e64e781` (16 cases, 4 pins, r96 pin refreshed to HEAD)
- `corpus/fixtures/r96-crossing-response/claim-excerpt-map.md` `e851f068cfd7ed02c97054df18729c4c5a9b8bf60d99d7c9116f427d765440de` (repair)
- `corpus/fixtures/r97-crossing-acknowledgment/`: `README.md` `d9387b7d…`, `claim-excerpt-map.md` `49d4834e…`, `entities.json` `026af0bc…`, `relations.json` `c279254b…`, `contradictions.json` `37517e5f…`, `sources.json` `438fb513…`, `timeline.json` `73063a86…`, `fictional-excerpts.md` `8ba491cb…`, `inspiration-note.md` `58f5390e…`, `source-excerpt.md` `b5edc2fd…`
- `corpus/knowledge/r97-acknowledgment-scope-note.md` `5e3b4225c30de8a2a75b675b59acb5c597b290e5a45f2caa01663da586e042b5`

## My own reproduction (transcripts under `.ufo/waves/round-97/seats/V37-scratch/`: `c1-probe.txt`, `c2-probe.txt`, `battery.txt`, `c3-r96-probe.txt`, `c3-r97-probe.txt`, `final-state.txt`, `final-hashes.txt`)

- **C1** — delivered `--self-test` `SELF-TEST CASES 25/25 pinned` / 25 PASS / `RESULT PASS` exit 0. Loader closed: a scratch contract copy dropping `dual_pointer` → `FINDING self_test_contract: contract drops implemented self-test cases: dual_pointer` / exit 2; the r96 tool on the same 23-case contract printed `SELF-TEST CASES 23/24 pinned` / `RESULT PASS` **exit 0** (the closed laxness, demonstrated). Pin load-bearing: neutralizing `second_pointer_mention` in a mirror → `SELF-TEST FAIL dual_pointer exit=0 findings=none` / `self_test_mismatch` / exit 2. Battery r88 10/10, r93 12/12, r94 14/14, r95 15/15, r96 16/16, r97 17/17, frozen r93 replay PASS, r87/r89 exit 2 `unsupported_map` — all exit 0/2 as pinned.
- **C2** — `--freeze` on a scratch path → `FINDING SCOPE-REFUSED` exit 2, delivered contract sha unchanged across the probe; foreign byte-identical r96 copy → `FINDING PATH-MISMATCH` exit 2 (r96 baseline tool: `RESULT PASS` exit 0 on the same copy); mirror-pinned tamper → `DIGEST-MISMATCH … changed: relations.json (sha256 c279254b… -> 8138d185…)`; `--self-test` 16/16 exit 0 (incl. `scope_refused`, `path_mismatch`); chain r88/r94/r95/r96 4/4 `RESULT PASS`; r97 fixture → `UNPINNED-FIXTURE` exit 2.
- **C3** — r97 `check_bible` `CLEAN … 0 violations` exit 0; `support_check` `SOURCE-SUPPORT 17/17; EDITORIAL-ANCHORS 2/2; MODES 19/19; VALIDATED-ROWS 19/19` / `RESULT PASS` exit 0; `map_obligations` `raw=17 mapped=17` / `INVENTORY 17/17; 2/2; 19/19` / PASS exit 0; J17 row maps `timeline.json#/5` span 44-53; census `ls -d corpus/fixtures/*/ | wc -l` = **171**. r96 receipt invariance: pre-repair map copy vs delivered repaired map → `support_check` and `map_obligations` outputs identical; repair diff exactly `2 2` lines. No `map-obligations-self-test-*`/`dependency-freeze-self-test-*` strays at the repo root at compile.
- **Not mine to verify (read-only observation):** census clean/negative split (V26/V41 measured 171/37/134/421), boundary gate/discriminator (V23), SHONEN (V36), inherited-tool byte set (V49).

**Verdicts recorded as the seats state them at v1:** calibration **PASS** (V31; V38 spec-conformance PASS); depth **improved (bounded)** (V29 + V54 crosscheck PASS); coverage **PASS (bounded)** (V30 + V55 crosscheck PASS); operability **improved (bounded)** (V32); freshness **unchanged** (V33); adjacency **PASS** (V34). Two seat-level **FAILs recorded, not re-rolled**: V12 (its stronger brief proof "r96 pin pins the post-repair map digest" is unmet — see NB-02) and V46 (r97 unpinned → `UNPINNED-FIXTURE`, not `REDUCTION-DETECTED` — see NB-01). Adjudicator seat not present at compile (see PR-10); V38 spec-conformance is not the adjudicator.

**Groups:** **NB** = new bound/debt named in r97 (r98+ candidate); **CO** = carried r96-ledger item with r97 status; **CL** = closure item for the r97 closure commit; **PR** = process/artifact observation; **ST** = stale/superseded during compile.

---

## NB — new bounds/debt named in r97

| ID | Axis | Description | Evidence pointer | Proposed owner |
|---|---|---|---|---|
| NB-01 | coverage | **r97 fixture is not in the freeze chain.** `dependency_freeze` on `r97-crossing-acknowledgment` exits 2 `UNPINNED-FIXTURE`; a dropped tick-13 `depends_on` is therefore not caught as BR-01 by any gate until the fixture is pinned (scratch mirror reproduces `REDUCTION-DETECTED` once pinned). V46's FAIL is this bound; the chain stays 4/4 per the declaration. | V46 bottom line (FAIL); R3 §Residuals-2; V53 §4 obs 3; my C2 probe | r98 (pin it or accept) |
| NB-02 | coverage | **The refreshed r96 pin does not cover the repaired map.** Pin coverage is the five JSON tables (`DATA_FILES`); `claim-excerpt-map.md` (`e851f068…`) appears nowhere in the contract (`grep -c e851f068` → 0). The re-freeze moved only the pin `revision` `60dba0c2…`→`2393934…` and reformatted the file. V12's FAIL is its stronger brief proof ("pins the post-repair map digest") unmet; the LOG wording ("pin refresh through the guarded path") holds. | V12 bottom line (FAIL) + §2; R3 §"Pin refresh…" (recorded discrepancy); V10; V38 §1–2; V57 | r98 (extend coverage?) / closure record |
| NB-03 | docs | **`corpus/tools/README.md:175` still describes the pre-r97 `dependency_freeze`** (self-test "14/14"; all three r96 hazards listed as open — all closed). No Round-97 C2 addendum exists (R2's addendum covers `map_obligations` only). R2-owned byte. | R3 §Residuals-1; V26 §3.5; V38 residual 1; V39 P5; my grep of `:175` | r97 closure (L1) |
| NB-04 | docs/freshness | **Registry rows stale:** `SKILL.md:87` ("24 cases"; "`dual_pointer` … not pinned"; "the two r96-added pins are droppable … both r97 debt") and `corpus/README.md:37` ("24 persisted cases") — all closed by C1; `:89`/`:38` freeze rows likewise pre-r97. | R2 obs 1; V26 §3.2; V38 residual 1; V39 P2/P4; my greps | r97 closure (L1) |
| NB-05 | docs/freshness | **`corpus/fixtures/README.md` Round-97 section absent**; census text still 170 (lines 1213/1217); the `:1213` "r97 candidates" sentence is resolved by R4's repair and needs a dated correction. | V26 §3.1; V39 P1; V18; V33 | r97 closure (L1) |
| NB-06 | freshness | **Carried stale note pins unrepaired:** `corpus/knowledge/r95-aftermath-scope-note.md:51` pins `9224a684…`; `r96-response-scope-note.md:55` pins `6634e176…` (both self-caveated "re-run before citing"). | V33 bottom line; my greps (`:51`, `:55`) | r98 |
| NB-07 | freshness | **r97 note's own caveat:** its receipts cite the delivered `86b52949…` with the earlier in-flight `70795150…` run as history and a standing "re-run against the closure revision" sentence. Corrected before final bytes; recorded so the caveat is not lost. | `r97-acknowledgment-scope-note.md:64`; R6 §Receipts; V33; V39 P9.4 | closure record |
| NB-08 | calibration | **`dual_pointer` remains legacy-dialect-scoped:** a second *bare field-path token* in a canonical-dialect parenthetical passes silently; a second `.json#` pointer there exits 2 `unsupported_map` (fail-closed, different class). The new pin records the legacy emission only. | V31 bound 2 | r98 / accepted |
| NB-09 | calibration | **Consistent regeneration still exits 0** (declared-vs-observed gate; a coherent regenerated declaration is indistinguishable). Carried r96 bound; restated in R2's README addendum. | V31 bound 3; R2 README Round-97 addendum | accepted |
| NB-10 | process/operability | **BR-05 now covers both tools:** `map_obligations` self-test scratch (`dir=ROOT`) and now `dependency_freeze` self-test scratch (`dir=ROOT`, moved off `/tmp` this round) both create transient dirs under the repo root, not gitignored. Transient `map-obligations-self-test-*` entries observed live (V31 ~21:50:20Z; V48); none persisted at my compile check. | R3 report (scratch choice); V31 bound 4; V48; V38 note 3; my final-state check | r98 (relocate/gitignore) |
| NB-11 | host | **`/tmp` inode exhaustion** (`df -i /tmp` → 1048576/1048576, 100%): any `tempfile`-based self-test run dies `ENOSPC` unless `TMPDIR` is redirected; `dependency_freeze` is now immune (`dir=ROOT`), `map_obligations` unaffected (`dir=ROOT`), other tools/probes are not. | V09; V20; V26 §1; V30 §6; V53 obs 1; V38 note 3; R3 | operator/harness (record) |
| NB-12 | process | **R1 report quote slip (LOW):** its neutralized-run quote says `exit=1 findings=[]`; the actual output is `exit=0 findings=none` (tool unaffected; my run agrees with the actual). | V05 bottom line; my `c1-probe.txt` | record |
| NB-13 | process | **R3 report paraphrase:** its "recorded discrepancy" rebuts a "digest changes by the repair" wording that does not appear in `LOG.md`; the measured facts it reports are correct. | V38 §1/§2; V57 bottom line; V39 P9.1 | record (closure errata) |
| NB-14 | docs | **The repaired r96 map lost its standalone relation-bound sentence** (the rewritten line names the tick-12 event); the bound survives in the J11 anchor, README, `sources.json` reliability notes and the scope note. Flagged for the closure pass. | V51 obs 1; V29 (repaired-map prose) | closure note |
| NB-15 | depth | **Checker dependency blind spots:** with `check_bible`, an emptied `depends_on`, a wrong-but-earlier edge, and a deleted terminal event all stay `CLEAN`; only missing/unknown/self/repeated ids and non-increasing ticks fail. The map/README/scope-note carry the other half. | V20 bounds paragraph | accepted |
| NB-16 | process | **Poll-wait/endgame hazards:** one concurrent mutual-polling window (R4↔R5 ~3 min, non-cyclic, no deadlock); the endgame all-reports triangle `{V24,V35,V40}` is the standing risk; one poll glob matched scratch directories instead of reports (R6). | V56 §6 + §5; V36 poll record | process (r98 wave design) |
| NB-17 | coverage | **Freeze verify-side bounds:** pin lookup is name-gated (renamed fixture → `UNPINNED-FIXTURE`; missing pinned name → `FIXTURE-MISSING`), `resolve()` symlink semantics apply to both scope and binding, and the pin payload is JSON-only (markdown never hashed) — see NB-01/NB-02. | V30 §4; V11; R3 | accepted |
| NB-18 | coverage | **`SELF-TEST-MISMATCH` exit convention still diverges** (freeze tool `emit(1, …)` at `dependency_freeze.py:544`; sibling `map_obligations` uses exit 2). Carried r96 NB-09; unclaimed in r97. | my code read `:544`; r96 V40 NB-09 | r98 |
| NB-19 | process | **Tool-revision flux within the round:** `map_obligations.py` ≥5 sha256s (`2b0ba815` → `70795150` → `c398e26c` → `86b52949`), contract `97b76bb8` → `2142b991`; `dependency_freeze.py` `fbaca38f` → `7428dad4` → `b06275f3`, contract `c65ac3bd` → `8015e1f9` → `625ccfac` → `27273be2`. Receipts must cite the frozen revision (pre-delivery receipts valid for their revision only). | my poll log; R2 §; R6 §Receipts; V31 §8 | record (pin revisions in receipts) |
| NB-20 | coverage | **r97 fixture README replay block lists the three commands without recorded exits** — the r94 BR-17 / r95 NB-11 / r96 CO-09 pattern recurs a fourth time. | `r97-crossing-acknowledgment/README.md` replay block (my read) | r98 (fixture docs) |

## CO — carried r96-ledger items, r97 status

Pointers into `.ufo/waves/round-96/seats/V40-debt.{md,json}` for items not re-argued here.

| ID | r96 item | r97 status | Evidence |
|---|---|---|---|
| CO-01 | NB-25 (`dual_pointer` unpinned; droppable added pins) | **CLOSED** — pin persisted; loader fails closed on any dropped pinned case; baseline 23/24-exit-0 reproduced as the closed pre-state. | my C1 probe; R1; R2; V01/V02/V31/V38 |
| CO-02 | NB-04 (`--freeze` scope guard; foreign `c3red`) | **CLOSED** — `SCOPE-REFUSED` exit 2 with no contract write (plus symlink/scope-root/same-named-shadow refusals); `c3red` was already removed at r96 closure. | my C2 probe; R3; V06/V11/V26/V30/V45 |
| CO-03 | NB-06 (basename-only pins) | **CLOSED** — path binding: foreign same-named copy exits 2 `PATH-MISMATCH` naming both resolved paths; baseline verified identically (exit 0). | my C2 probe; R3; V07/V45 |
| CO-04 | NB-08 (`DIGEST-MISMATCH` names no file) | **CLOSED** — names the changed file(s) with before/after sha256. | my digest probe; R3; V08/V11 |
| CO-05 | NB-05 (freeze pin-set validation) | **CLOSED** — 16-case exact-set loader (`missing`/`extra` both fail `CONTRACT-INVALID`); `scope_refused`/`path_mismatch` pinned. | my self-test run; R3; V09/V11 |
| CO-06 | NB-10 first half (`freeze()` discards verify result) | **CLOSED** — freeze now propagates the post-freeze verify exit code. | R3 report; V11 |
| CO-07 | NB-07 (BR-01 prose/wording half) | **OPEN** — not claimed in r97; markdown layer still unhashed (see NB-02/NB-17). | declaration C2 (no prose claim); R3; V30 §4 |
| CO-08 | NB-09 (`SELF-TEST-MISMATCH` exit convention) | **OPEN** — see NB-18. | NB-18 pointers |
| CO-09 | NB-10 second half (`MALFORMED-MODEL`/`CONTRACT-INVALID` unpinned; zero-dependency wording) | **OPEN** — the 16 cases pin `MALFORMED-JSON`/`FILE-MISSING`/`CONTRACT-INVALID` loader paths but not `MALFORMED-MODEL`; not claimed. | R3 contract; V11 (16-case list) |
| CO-10 | NB-15 (r96 map nits) | **2/3 CLOSED** — delimiter row and stale sentence fixed (2-line diff, receipts unchanged); the `:18` "carry the r94 JSON pointers" imprecision remains. | R4; V19; my diff/read |
| CO-11 | NB-14/NB-26 (stale note pins) | **r95/r96 pins still OPEN (NB-06); r97 corrected before final bytes (NB-07).** | V33; note texts |
| CO-12 | NB-18/BR-05 (self-test scratch under repo root) | **OPEN, now both tools** — see NB-10. | NB-10 pointers |
| CO-13 | NB-17 (`/tmp` inode exhaustion) | **OPEN (host)** — see NB-11. | NB-11 pointers |
| CO-14 | NB-20/NB-21 (drift scope; consistent regeneration) | **OPEN/accepted** — see NB-08/NB-09. | NB-08/09 pointers |
| CO-15 | NB-16 (docs presupposition; generalized dependence wording) | **NOT RAISED in r97** — no seat re-opened it; whole-claim reviews (V17/V43) found no constructible overclaim on the new bytes. Status from r96 stands. | V17; V43 |
| CO-16 | r96 CO-09 (fixture README replay without exits) | **RECURRED** — see NB-20. | NB-20 pointer |
| CO-17 | r96 CL-04 (C9 watch row-6) | **PROPOSED, not written** — V48 supplies the row-6 block for L1; the watch still ends "Next re-check: r97". | V48 §4; my watch read |
| CO-18 | r96 CO-10 (r94/r93 carry-overs: BR-04 phantom set-membership; `--help` zero-RESULT; r94 map/README polish; boundary-doc CR items; poll-helper; legacy receipts) | **UNADDRESSED except where r97 touched the same file** — r97's deliverable set does not intersect those paths; r96 statuses stand. Poll-helper debt recurred in kind (NB-16). | r96 V40 CO-10; V56; V36 |

## CL — closure items for the r97 closure commit

| ID | Axis | Description | Evidence pointer | Proposed owner |
|---|---|---|---|---|
| CL-01 | freshness/coverage | **fixtures README Round-97 append + census** (171 dirs / 37 clean / 134 negative / 421 lines / 0 unexpected exits) + dated correction of the `:1213` "r97 candidates" sentence + W05 pin note. | V39 P1; V26 §3.1; V41; V21; my census | r97 closure (L1) |
| CL-02 | freshness/docs | **`corpus/README.md` bullets** (r97 fixture bullet; `:37` 24→25 + strict loader + `dual_pointer` pinned; `:38` 14→16 + guard/path-binding/digest-naming). | V39 P2; V26 §3.2 | r97 closure |
| CL-03 | freshness | **C9 watch row-6 append** (V48's block verbatim; `DISCRIMINATION HELD` + `e97613c` control; "Next re-check: r98"; gate 3 not met). | V48 §4; V23; V26 §2.6; V33 | r97 closure |
| CL-04 | freshness/docs | **`SKILL.md` registry rows refresh** (`:87`, `:89`, `:96-100`). | V39 P4; V26 §3.3 | r97 closure |
| CL-05 | docs | **`corpus/tools/README.md` Round-97 C2 addendum** (supersede `:175`; document `SCOPE-REFUSED`, `PATH-MISMATCH`, digest naming, 16 cases). R2-owned byte; R2's report does not mention `dependency_freeze`. | R3 §Residuals-1; V26 §3.5; V38; V39 P5 | r97 closure (R2/L1) |
| CL-06 | coverage | **Re-freeze record + errata:** record the r96 pin refresh (revision/format only; digest measured unchanged), the V12 FAIL (not re-rolled) and the V46 FAIL, and the LOG-vs-report paraphrase. | V12; V46; R3; V38; V57; V39 P6/P9 | r97 closure (L1) |
| CL-07 | process | **Receipt fill / bookkeeping / commit split** (producer paths vs integration files; no promotion; no push). | V39 P7; V36 fleet set | r97 closure (L1) |
| CL-08 | process | **Do-not-touch constraints:** PROVINCE/SHONEN/SKILL/READMEs/c9-watch producer-untouched; pins not to be moved by closure edits. | V39 P8; V28/V34; my final-state check | r97 closure |
| CL-09 | process | **Adjudicator/roster accounting:** V24/V35/V40/V58 absent at this compile (V35 scratch active 19:08); no adjudicator report existed when this ledger compiled — the L1 must obtain or record it. | my seats listing; V56 §6 | r97 closure (L1) |
| CL-10 | freshness | **r95/r96 note stale pins** (NB-06) — decide: re-run + update, or dated erratum. | V33; note texts | r97 closure / r98 |
| CL-11 | process | **SHONEN state + fleet round report + receipt** (four `[~]`, zero `[x]` at HEAD; same-lane rule — no promotion expected). | V36 §1; V39; r96 CL-08 precedent | r97 closure (L1) |
| CL-12 | coverage | **r97 fixture freeze-pin decision** (NB-01) — record in SCORECARD's r97 debt head either as an r98 candidate or as an accepted bound. | V46; R3 §Residuals-2; V53 obs 3 | r97 closure (record) / r98 |

## PR — process/artifact observations (record, no re-adjudication)

| ID | Description | Evidence pointer |
|---|---|---|
| PR-01 | **V12 FAIL recorded, not re-rolled** — its brief's "pins the post-repair map digest" proof is unmet (NB-02); the facts it measured (only the r96 pin entry changed; only `revision`; JSON digests byte-identical to `f3e09f9`; reproducible through the guarded path) are confirmed by V10/V38/V57. | V12; V10; V38; V57 |
| PR-02 | **V46 FAIL recorded, not re-rolled** — the BR-01 catch on the r97 fixture requires a pin; unpinned it is `UNPINNED-FIXTURE` exit 2 (NB-01). | V46 |
| PR-03 | **Mutual poll-wait windows:** R4↔R5 ~3 min (18:46:48–18:49:50), R1↔R2 ~60 s, no trapped pair observed 18:43–18:54; endgame triangle `{V24,V35,V40}` the standing risk. | V56 §5–6 |
| PR-04 | **R1 report quote slip** (NB-12). | V05; my run |
| PR-05 | **R3 report paraphrase** (NB-13). | V38; V57; V39 P9.1 |
| PR-06 | **Host `/tmp` inode exhaustion** during the wave; seats redirected `TMPDIR` to scratch; R3 moved freeze self-test scratch to `dir=ROOT` (no strays left). | V09/V20/V26/V30/V53/V38; R3; my final check |
| PR-07 | **Tool-revision flux** (NB-19): mid-flight states included an incomplete freeze revision (`scope_guard` defined but not yet called; new cases declared but not implemented) — verifier polls correctly deferred; no plan was verified. | my poll log; V09/V30/V45 poll records; R3 |
| PR-08 | **Interim→final updates:** V30 and V45 first wrote PENDING (R3 absent), then final PASS; V09/V26 interim; V14 preliminary → final; V36 placeholder → final PASS; R6 note `56981af5…` → `5e3b4225…`. | seat files; V29 §; my reads |
| PR-09 | **Mid-flight r97 README/map were r96 byte copies** (until 18:48:56/18:49:14) and `map_obligations` correctly failed `missing_obligation: timeline.json#/5` then — recorded as evidence J17 is load-bearing, not a defect. | R4; R5; V26 §2.3; V29; my poll |
| PR-10 | **Seats absent at this compile:** V24, V35 (scratch active 19:08), V40, V58. 59 seat `.md` present at compile (6/6 producers + 53 verifiers), plus this ledger. | my listing 19:11 |
| PR-11 | **Poll-glob hazard:** one producer poll matched `*-scratch` directories as "reports" (R6) and V56 records naming mismatches across seats; poll hygiene debt (recurred class). | V36 poll record; V56 §5 |
| PR-12 | **V39's integration checklist P0–P9** produced for L1 (admission inputs, doc sites, C9 row, re-freeze, receipt/bookkeeping, do-not-touch, errata). | V39 |
| PR-13 | **Cross-seat audits:** V53 5/5 quoted outputs reproduced (0 mismatched); V47 seven stale-doc/wording corrections listed; V38 spec-conformance PASS; V57 claim-text audit PASS. | V53; V47; V38; V57 |

## ST — stale/superseded during compile

| ID | Description | Evidence pointer |
|---|---|---|
| ST-01 | V30 and V45 interim PENDING verdicts superseded by their final PASS on R3's delivered revision. | V30; V45 |
| ST-02 | V09/V26 interim states ("R3 absent") superseded by R3's delivery (my battery + V30/V45 finals). | V09; V26 |
| ST-03 | Mid-flight r97 `README.md`/`claim-excerpt-map.md` (r96 copies) superseded by R5's rewrites; mid-flight map failure `raw=17 mapped=16` superseded. | R4; R5; V26 §2.3 |
| ST-04 | R6 note first revision (`56981af5…`, pinning in-flight `70795150…`) superseded by final `5e3b4225…` (delivered revision cited, in-flight run as history). | V33; note `:64` |
| ST-05 | V36's placeholder bottom line superseded by its final PASS. | V36 |
| ST-06 | V14 "preliminary" status (per V29) superseded by its final PASS. | V14; V29 §7 |
| ST-07 | r96 fixtures README `:1213` "Known cosmetic debts (r97 candidates)" superseded by R4's repair — dated correction queued at CL-01. | V39 P1; my read |

---

## Compile-time notes (my own checks, stated plainly)

1. All sha256s above re-measured at compile (19:10–19:11); delivered tool/contract/fixture hashes match R1/R2/R3/R4/R5's declared revisions and V32/V38/V57's frozen sets.
2. I reproduced the three claims' head receipts myself (C1 a/b/c with baseline controls, C2 guard/path/digest/self-test/chain, C3 gates + repair invariance + census) rather than citing seat output alone; seat outputs are used for the *bounds* they name, with pointers.
3. Nothing here is a verdict: FAIL-class/stale/absent items are recorded as observed; whether any NB/CO/CL item blocks r97 admission is the L1's ruling, not this ledger's. The two FAILs (V12, V46) are recorded exactly with their scope.
4. The four seats absent at compile (V24, V35, V40, V58) are named in PR-10/CL-09; no adjudicator report existed when this ledger compiled. If one lands after this write, it is not folded in — this is v1.
5. Producer byte-ownership was honoured by every seat as far as I read (the r96 V41-class breach did not recur; V28/V34/V49 checked lane-locality; my writes are this report, its JSON, and `V37-scratch/` only).

**Bottom line: PASS (ledger compiled) — 20 new bounds named in r97 (r97 unpinned from the freeze chain; the refreshed r96 pin not covering the repaired map; four stale doc sites; carried stale note pins; BR-05 now on both tools; the `/tmp` host condition; legacy-scoped `dual_pointer`; checker blind spots; process items), 18 carried r96 items with explicit r97 status (6 closed, 4 open/accepted, the rest unchanged or recurred), 12 closure items, 13 process observations and 7 supersession notes, transcribed with evidence pointers from 59 seat files plus my own reproduction of the three round claims; verdicts recorded as the seats state them at v1 (calibration PASS — V31; depth improved bounded — V29+V54; coverage PASS bounded — V30+V55; operability improved bounded — V32; freshness unchanged — V33; adjacency PASS — V34; two seat FAILs recorded, not re-rolled: V12 and V46).**
