# V34 — adjudicator (round 99)

- Seat: **V34 adjudicator — FINAL.** Leaf. No nested agents, no commits, no pushes, no network.
- Lane root: `/home/vgpnk/Projects/shokunin/lore-shokunin`. Session cwd is the parent repo; every path below is absolute or lane-root anchored. Commands used `python3` from the lane root unless a scratch mirror is named.
- Baseline: r98 closure `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`). HEAD during the wave `337f0fa` (the blocked-dispatch LOG commit). Wave tree uncommitted.
- Writes: this report only. First-hand probes used `/tmp/v34-*` copies. No lane file was mutated by this seat.
- Delivered revision judged (hashes re-measured at 23:12:48, stable from the times noted):
  - `corpus/tools/dependency_freeze.py` `fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c` (mtime 22:38:11; an earlier in-flight hash `6f81f8be…` was not the delivered tool)
  - `corpus/tools/dependency-freeze-contract.json` `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628`
  - `corpus/tools/README.md` `837a7f5dfe913047530c7f92f3dd6b3df1b1a83c77ede12ba0c349cc134a049c`
  - `SKILL.md` `e0bcb61ab909146e34773dd56219cb1631070c1700a2481f8ad1181f3d864443`
  - `corpus/knowledge/r99-gate-blind-spot-table.md` `4670c0b71668c56c53c0bac90091531d3f0e881c7dcb2ac572d09f96ae22182e` (20526 bytes, mtime 22:57:50)
  - `corpus/knowledge/r99-lapse-scope-note.md` `96de708f8e984f6f61ee6387342c287a275328a6293da1d225b2ad00040ebb54`
  - `check_bible.py` `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` (unchanged vs `4265df5`)

Admission rule applied: admit iff C1 and C2 (both components) verify on the delivered revision and no axis is harmed. Standing FAILs are recorded and not re-rolled into passes.

---

## 0. Poll record and stall-escape

Protocol: artifacts and producer reports; 20 s cadence. This seat polled from 22:01:08 through 23:13:28 (numbered tries 0–53 plus a final check). Early windows correctly saw S1/S2/S5 reports and the knowledge files absent; many seats capped at ABSENT and did not verify a plan. Those ABSENT reports are window-correct. They are not evidence the artifacts never arrived.

Landing, observed:

- S3 report 22:01:40. S4 report 22:03:54. Fixture directory present from 22:00:56 (r98 placeholders until S3/S4 content gates).
- Freeze tool moved several times (`03d04365…` baseline → `6f81f8be…` → `fb9bb9ff…` at 22:38:11). Contract ten-file pins stable at `8c2561b0…` from 22:08:46.
- S1 report `S1-full-file-pins.md` 22:48. Knowledge files 22:57:50. S2 report `S2-tools-docs.md` and S5 report `S5-knowledge-author.md` 23:11.

**Stall-escape (not fatal).** At 23:13:25, V101's poll log (`try2=89`) listed `missing_seats=V34` only (`others=126`, producers present, knowledge present). V101 is waiting on this report. Waiting for V101 would be the mutual-wait class the subtract-SELF rule exists to break. This adjudication does not wait for V101. At 23:13:28 the seats directory held **126** other reports; the only missing other seat was V101.

---

## 1. First-hand verification

### 1.1 C1 — ten-file pin, 18/18, chain 6/6, prose edit named

On the delivered tool+contract, lane root, 23:05 after the hash had held since 22:38:

```
python3 corpus/tools/dependency_freeze.py --self-test
SELF-TEST 18/18
RESULT PASS
EXIT=0
```

`markdown_tamper` printed `exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok`. The other 17 cases matched their persisted exits, including `self_test_mismatch` exit 2.

Chain verify, same invocation, each `RESULT PASS` exit 0:

| fixture | digest | inventory |
|---|---|---|
| r88-m3-maya-cluster | `acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae` | events 2/2; edges 0/0; relations 0/0 |
| r94-paired-crossing | `048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef` | 3/3; 2/2; 1/1 |
| r95-crossing-aftermath | `97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710` | 4/4; 3/3; 1/1 |
| r96-crossing-response | `43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c` | 5/5; 4/4; 1/1 |
| r97-crossing-acknowledgment | `a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54` | 6/6; 5/5; 1/1 |
| r98-clerk-filing | `5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0` | 7/7; 6/6; 1/1 |

These digests match S1's report. `r99-window-lapse` is not pinned: `UNPINNED-FIXTURE` exit 2. That matches the declaration (the chain is the existing six) and S1's explicit non-pin.

**Before / after, non-anchor class (the class every prior gate missed).** Independent mirror, same mutation S1 used on r94 is not re-copied here; the r98 coherent replacement I ran is the table's row 6:

- Baseline tool+contract from `git show 4265df5:` (`dependency_freeze.py` sha `03d04365…`), path-bound r98 copy, `depends on both ninth-bell entries` → `follows both ninth-bell entries` in both excerpt and map: `RESULT PASS` exit 0, digest `59a0f4fa3d4a47e03649a54d1815c45ee1eef641b63a59ebe7210bc9d9b9b133` (the r98 JSON-only pin). Markdown was invisible.
- Same bytes, delivered tool+contract: exit 2 `DIGEST-MISMATCH` naming `claim-excerpt-map.md` (`c1099d0e…` → `fc4633b9…`) and `fictional-excerpts.md` (`29e384bf…` → `dbcd5f11…`), content digest `1f73326f…` ≠ pin `5ecf84e1…`. Those sha256s match the table's row-6 quote byte-for-byte.
- Same coherent edit: `check_bible` CLEAN exit 0; `support_check` exit 0; `map_obligations` `raw=20 mapped=20` exit 0.

Excerpt-only replacement (map anchor left): `support_check` exit 1 (`SOURCE-SUPPORT 19/20`); delivered freeze exit 2 naming `fictional-excerpts.md` (`29e384bf…` → `dbcd5f11…`). So an anchored verbatim removal was **not** invisible to every gate before. S1, V03, and the table record that bound. I reproduce it. I do not cite the declaration's "invisible to every gate" sentence as true of the J14 anchor.

A non-semantic append on a delivered-pin r98 mirror (`<!-- v34 non-anchor probe -->`) also exited 2 naming `fictional-excerpts.md`. README newline tamper on an earlier in-flight tool named `README.md`; the delivered message string is `pinned-file bytes changed outside the semantic inventory`.

Semantic edits still decide first. Emptying `clerk-filing-open.depends_on` on a path-bound r98 copy: exit 1 `REDUCTION-DETECTED` (`lost depends_on ['acknowledgment-aru-records']`), no `DIGEST-MISMATCH` line. That is V55's counterexample to the unqualified "any edit → exit 2 naming the file" sentence. Reproduced. Not a pin failure. The contract's precedence (semantic inventory first) is what the tool does.

### 1.2 C2 component 1 — r99-window-lapse

On the delivered fixture (README `b9320941…`, map `d2fe20e5…`, matching S4):

```
python3 corpus/fixtures/check_bible.py corpus/fixtures/r99-window-lapse
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT=0
python3 corpus/tools/support_check.py corpus/fixtures/r99-window-lapse
SOURCE-SUPPORT 21/21; EDITORIAL-ANCHORS 2/2; … VALIDATED-ROWS 23/23
RESULT PASS
EXIT=0
python3 corpus/tools/map_obligations.py corpus/fixtures/r99-window-lapse
OBLIGATIONS raw=21 mapped=21
RESULT PASS
EXIT=0
```

Parsed counts: entities 6, relations 1, timeline 8, sources 8, contradictions 0. Census `ls -d corpus/fixtures/*/ | wc -l` = **173** (172 at r98 closure). Event `clerk-lapse-recorded` is tick 15, `entity_id` `clerk-maren`, `place_id` `chalk-stair`, `depends_on` `["clerk-filing-open"]`, `source_id` `clerk-lapse-note`. Source `clerk-lapse-note` is the eighth source. Excerpt lines 70–74 state the four clauses plus "I record no resolution, assign no blame, and reconcile nothing." J21 anchor hit at excerpt line 70 inside span 66–76 (`support_check` PASS J21).

Inherited equality vs live `r98-clerk-filing`: `entities.json`, `relations.json`, `contradictions.json`, `inspiration-note.md`, `source-excerpt.md` byte-identical. `sources.json[:-1]` and `timeline.json[:-1]` parsed-equal. `fictional-excerpts.md` has the r98 file (4187 bytes) as a byte prefix of the r99 file (5114 bytes). No new entity, claim, or relation.

Bounds that are not re-rolled (see §3): the description's "At the Chalk Stair" is not in the lapse quotes (V105); README/map "per the minute's terms" is not in the note (V14); lines 70–73 are impersonal world-mood (V95). The reliability note and excerpt scope sentence frame them as the clerk's record and deny breach/duty/winner/external fact. The declaration's required content is present as negations plus the four stated clauses. That is a bounded depth gain, not a resolution.

### 1.3 C2 component 2 — blind-spot table, rows replayed

Table `4670c0b7…` and note `96de708f…` were stable from 22:57:50 through 23:13. I did not treat S5's scratch trees as the measurement. Independent copies under `/tmp/v34-replay` and `/tmp/v34-r7`, delivered tool `fb9bb9ff…` / contract `8c2561b0…`, path-bound `r98-clerk-filing` unless noted:

| row | mutation | observed | matches table |
|---|---|---|---|
| 1 | `clerk-filing-open.depends_on = []` | freeze exit 1 `REDUCTION-DETECTED` lost `acknowledgment-aru-records`; `check_bible` CLEAN 0 | yes |
| 1 r99 twin | empty `clerk-lapse-recorded.depends_on` | `check_bible` CLEAN 0; `map_obligations` raw=21 mapped=21 exit 0 | yes |
| 1b | drop `evin-ninth-bell` from `paired-crossing-decision` | freeze exit 1 `REDUCTION-DETECTED`; bible CLEAN 0 | yes |
| 2 | edge to `response-evin-salt-court` | freeze exit 1 `ADDITION-DETECTED` + `REDUCTION-DETECTED`; bible CLEAN 0 | yes |
| 3 | delete `clerk-filing-open` | freeze exit 1 `REDUCTION-DETECTED` missing event, 1 edge gone; bible CLEAN 0 | yes |
| 4 | J05 span `17` → `20` | freeze exit 2 digest `09858d77…` naming `claim-excerpt-map.md` (`c1099d0e…` → `f5d2c136…`); support exit 1 `FAIL J05 … span=20; outside-span=17`; map PASS; bible CLEAN | yes, including the digest the table quotes |
| 5 | `clerk-filing-open.source_id` → `aru-acknowledgment-note` | freeze exit 2 naming `timeline.json` (`eb24e084…` → `17e9230e…`); map exit 1 `source_id_mismatch` `timeline.json#/6`; support exit 0; bible CLEAN | yes, including `17e9230e…` |
| 6 | coherent `depends on` → `follows` in excerpt and map | baseline freeze exit 0 digest `59a0f4fa…`; delivered exit 2 digest `1f73326f…` naming both files (`fc4633b9…`, `dbcd5f11…`); bible/support/map exit 0 | yes, quote-identical |
| 6b | excerpt-only same replacement | support exit 1; freeze exit 2 naming `fictional-excerpts.md` | yes |
| 7 | delete terminal event, drop J20, restate inventory to 19/2/21/17 | bible CLEAN 0; support `19/19` PASS; map `raw=19 mapped=19` PASS; freeze exit 1 `REDUCTION-DETECTED` missing `clerk-filing-open` | yes |
| 8 | live `boundary_doc_check` | `CERTIFIED` exit 0; checker sha `ff9fd2aa…` equals the pin the table cites | live half yes; the one-comment drift probe was not re-run here (S5's quote stands as their measurement) |

Row 9's eight `check_bible` catches were not re-run by me. V16 independently reproduced dropped-key → `required nonempty list` exit 1, unknown event exit 1, tick-14 inversion exit 1, and deleted predecessor → `unknown event` exit 1, on timeline `2cdb9fda…` and checker `ff9fd2aa…`. That is a second seat for those four probes. I do not invent the other four.

The table's own limit is correct and was observed: `r99-window-lapse` freeze is `UNPINNED-FIXTURE` exit 2, so semantic freeze catches are on the pinned r98 twin, not on the new fixture.

---

## 2. Seat reconciliation

Producer reports S1–S5 all present. S1 PASS matches my C1 runs, including the J14 bound. S2 PASS matches the delivered README addendum and SKILL freeze row on the hashes above (S2's poll missed S1 inside 40 tries; the report records the stall-escape and then reconciles). S3 PASS is true of the three data files and was stale about README/map at write time; S4 rewrote those two and the gates pass on S4's bytes. S5 PASS matches the table I replayed. S5 notes a 29/30 citation-needle miss (`assign blame` vs map line 69 `assigns blame to neither`); that is a paraphrase miss, not a missing denial.

Axis seats that scored the delivered revision: V28 calibration **PASS improved (bounded)**; V30 coverage **PASS unchanged, not harmed**; V31 operability **PASS** on README `837a7f5d…`. V29 depth was **INCONCLUSIVE** because component 2 was absent in that seat's 40-try window. I do not rewrite V29. I complete component 2 myself (§1.3). V32 freshness and V33 adjacency were **ABSENT** for the same early window. V26 and V82 operability ABSENT are the same class. V120's "V31 FAIL" was stale relative to the V31 text I read (bottom line PASS). V39's receipt is a 22:22 skeleton (15 reports hashed; S1/S2/S5 and both notes ABSENT then). Not the final collection.

Early C1 ABSENT seats (V06, V07, V97, and others) refused to review without an S1 report. Correct for their window. The tool they declined to score is the one I ran.

---

## 3. Standing FAILs — not re-rolled

These remain FAILs on the criteria those seats stated. I do not convert them to passes. I also do not adopt every one as an axis harm; the distinction is stated.

1. **V55 — declaration/doc universal is false.** Emptying `clerk-filing-open.depends_on` exits 1 `REDUCTION-DETECTED` and does not name the file. Reproduced. `corpus/tools/README.md:310` and `SKILL.md:100` repeat "Any edit to any of the ten pinned files exits 2 `DIGEST-MISMATCH` naming that file." False for inventory-modeled edits. Condition AC-1. Not a failure of the prose-edit mechanism.
2. **V03 / S1 bound — "invisible to every gate" is false for the J14 anchor.** Excerpt-only removal of `depends on both ninth-bell entries` is `support_check` exit 1 before and after. The invisible class is the coherent or non-anchor edit. Condition AC-2.
3. **V110 — precedence order vs combined invocation.** Reproduced: a README-tampered r98 copy invoked as `fixture --freeze fixture` prints only `INVALID-ARGUMENTS: pass either a fixture (verify) or --freeze DIR, not both` / `RESULT ERROR` exit 2. No `DIGEST-MISMATCH`. V118's verify-pipeline order can hold at the same time. Condition AC-3. Not re-rolled.
4. **V105 — locative out-claim.** Description "At the Chalk Stair at tick 15, the clerk records…" places the recording act. Lines 70–74 and the scope sentence do not. Stands.
5. **V14 — "per the minute's terms" and the description's own clause.** The note does not construct resolution, blame, reconciliation, or a new duty. README:11 / map:69 add a gloss the quotes do not carry. Stands.
6. **V95 — lines 70–73 are impersonal world-mood; only line 74 is first person.** Stands as a framing FAIL against a clerk-record-mood criterion. The declaration asked for those four statements. The reliability note denies world-fact status. Bound, not a hidden resolution.
7. **V16 / V63 — tick-15 edge unpinned.** `UNPINNED-FIXTURE` exit 2, not `REDUCTION-DETECTED`. S1 states the omission is intentional (chain stays six). Their FAILs stand against a "pin the new edge" criterion the declaration did not require. Condition AC-4, not a C1 miss.
8. **V85 — r88 eleventh file.** `symbolism-clause-map.md` is not in the ten-file pin. The other five chain fixtures match the pin file-for-file. S1 and SKILL.md:100 name this exclusion. FAIL stands against "every file in the directory." Condition AC-5.
9. **V23 / V107 — parent-tree strays.** Confirmed: `/home/vgpnk/Projects/shokunin/.ufo/waves/round-99/seats/V69-scratch/` holds 0-byte tool copies; `V73-scratch/selftests/` holds wrong-cwd stderr (`freeze.err` 128 bytes, `map.err` 126, `boundary.err` 129, empty `.out` files). V107: charter byte-identical to `4265df5`; in-lane porcelain is the declared S1–S5 set. FAILs stand on the zero-stray bar. Not adopted as adjacency harm (out-of-lane scratch, no province write). Condition AC-7. V40's archive mirror is flagged by V23, not deleted by me.

---

## 4. Per-axis table

| Axis | Movement | Who scored the delivered revision | This adjudication |
|---|---|---|---|
| Calibration | improved (bounded) | V28 PASS | **improved (bounded)** — ten-file schema-2 pins; non-anchor/coherent prose edit invisible to the r98 freeze (digest `59a0f4fa…` or `2527beb9…` on S1's r94 non-anchor) and exit 2 naming the file after; self-test 17→18; semantic findings still exit 1 first |
| Coverage | unchanged, not harmed | V30 PASS bounded; V69 PASS unchanged | **unchanged, not harmed** — chain still six, 6/6 clean, inventories unchanged; r99 unpinned by declaration; ten-file payload is the calibration move, not a new lore-rule class |
| Depth | improved (bounded) | V29 INCONCLUSIVE (component 2 absent in that window) | **improved (bounded)** — component 1: 6/1/7→6/1/8, sources 7→8, obligations 20→21, CLEAN, census 172→173, no resolution/blame/reconciliation asserted as a positive finding. Component 2: table `4670c0b7…` replayed (§1.3). V29 not rewritten |
| Operability | PASS (bounded) | V31 PASS on `837a7f5d…`; V26/V82 ABSENT were early windows | **PASS (bounded)** — documented replay commands match observed exits. The false universal at README:310 / SKILL.md:100 is AC-1, not a failed command |
| Freshness | improved (bounded) | V32 ABSENT (early window, not scored) | **improved (bounded)** — README addendum supersedes the carried "five JSON tables only / prose half remains open / 17 cases" sentences with dated 2026-10-17 text. New overclaim is AC-1, not a return of the old stale pin |
| Adjacency | not harmed (bounded) | V33 ABSENT (early); V107 FAIL on parent strays, charter identical | **not harmed (bounded)** — `git status` outside `.ufo/` is exactly the declared ownership (`dependency_freeze.py`, contract, README, SKILL.md, `r99-window-lapse/`, two knowledge files). Parent strays are AC-7. V23/V107 FAILs stand |

**No axis is harmed** on this reading. Every bound is named. No harmed finding is re-labeled as a pass.

---

## 5. Admission

C1 verifies on the delivered revision for the operative move: schema-2 ten-file pins, chain 6/6, self-test 18/18 with `markdown_tamper` exit 2, and a prose edit the r98 freeze missed now named `DIGEST-MISMATCH`. C2 component 1 verifies (counts, gates, census, inherited prefixes, no positive resolution). C2 component 2 verifies (table rows replayed; quoted digests match). No axis harmed.

### RECOMMENDATION: **ADMIT** (bounded), with conditions

- **AC-1 (V55, not re-rolled).** Before any closure citation, qualify README:310, SKILL.md:100, and the declaration's "any edit to any pinned file → exit 2 `DIGEST-MISMATCH` naming the file." Semantic inventory findings decide first and exit 1 without that finding. `DIGEST-MISMATCH` names the file only when the inventory is clean.
- **AC-2 (V03 / S1).** Do not cite "invisible to every gate" for removal of a mapped verbatim anchor. That edit is `support_check` exit 1. The demonstrated invisible class is a non-anchor edit or a coherent excerpt+anchor replacement.
- **AC-3 (V110, reproduced).** Precedence prose that lists `DIGEST-MISMATCH` before `INVALID-ARGUMENTS` does not describe `fixture --freeze fixture` on a tampered pin: that invocation exits 2 `INVALID-ARGUMENTS` only.
- **AC-4 (V16 / V63, not re-rolled).** `r99-window-lapse` is unpinned. Do not claim the tick-15 edge is freeze-covered. Freeze catches in the table are on pinned r98 twins.
- **AC-5 (V85, not re-rolled).** `r88-m3-maya-cluster/symbolism-clause-map.md` is outside the declared ten and is not pinned.
- **AC-6 (V105, V14, V95, not re-rolled).** Do not cite the tick-15 description's "At the Chalk Stair" as lapse-note wording, do not cite "per the minute's terms" as a quoted clause, and do not cite lines 70–73 as first-person clerk-record mood. Line 74 and the reliability note are the denial frame. No resolution, blame, or reconciliation is positively asserted.
- **AC-7 (V23 / V107, not re-rolled).** Clean `/home/vgpnk/Projects/shokunin/.ufo/waves/round-99/` (V69 0-byte copies, V73 wrong-cwd stderr) and decide the V40 archive mirror. Charter was not the write.
- **AC-8.** Closure docs are not this wave's producer set. V25: fixtures README has no Round-99 section; corpus README still lacks the r99 bullet. L1 owns census re-declaration (173) and SCORECARD. Do not cite V39's 22:22 skeleton as the collection.
- **AC-9.** V101 was still polling for V34 at 23:13:25. This report is the stall-escape. A receipt refresh after V101 lands is L1's, not a missing claim.

---

## 6. Bounds of this adjudication

- C1/C2 were re-run on `fb9bb9ff…` / `8c2561b0…`, not on the 22:11 in-flight tool. An earlier self-test on `6f81f8be…` is discarded as pre-delivery.
- Row 8's checker-drift probe and four of row 9's eight probes were not re-run here. Cited as S5 / V16, not as my measurements.
- I did not read all 126 reports line by line. Axis verdicts, producer reports, and every FAIL bottom I could find were read. Where I rely on another seat I name it.
- No canon, rights, identity, or entailment ruling. Clean gates are structural. The table is a measured blind-spot record, not a finding about the fiction.

---

## Bottom line

**PASS — ADMIT round 99 (bounded): C1 and C2 both components verify on the delivered revision (`fb9bb9ff…` / `8c2561b0…`, table `4670c0b7…`); no axis harmed; conditions AC-1..AC-9; standing FAILs (V03, V14, V16, V23, V55, V63, V85, V95, V105, V107, V110) not re-rolled. V101 was the sole remaining other seat and was waiting on this report (stall-escape).**
