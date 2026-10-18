# V36 — debt-ledger (round 99)

**Seat:** V36 debt-ledger. **Role:** named bounds/debt with owner rounds. No re-adjudication, no axis score, no smoothing. Nothing below is inferred past the pointer.

**Compiled at:** 2026-10-18 01:56 UTC (22:56 -03). Lane root `/home/vgpnk/Projects/shokunin/lore-shokunin`. HEAD `337f0fa` (blocked-dispatch record above standing r99 declaration). Baseline `4265df5`.

**Poll-wait (this seat):** `V36-scratch/poll.sh` + `poll.log`. Content-gated (not existence-only): producer reports S1–S5, S1/S2 bytes different from `4265df5`, r99 JSON/excerpt lapse markers, README and map not byte-identical to r98 and carrying a lapse/window marker, both S5 knowledge files non-empty. 20 s × 40.

```
ABSENT after 40 tries 2026-10-18T01:15:21Z
```

At that line the log still had `MISS report S1`, `MISS report S2`, `MISS report S5`, `MISS S2 bytes unchanged vs 4265df5`, both knowledge files missing. S3 and S4 content markers were present. No all-reports wait. SELF subtracted by not waiting on this file. No stall-escape was used to flip ABSENT into a verification. C1 and C2-component-2 were not run by this seat.

**Post-cap, not a second poll:** at 01:51:29Z `S1-full-file-pins.md` existed (mtime 22:48:57 -03). Tool mtime 22:38:11, so the report is later than the last tool byte measured here. S2 report, S5 report, and both knowledge files were still absent at 01:56:04Z. S1 is recorded, not reproduced.

## What this seat measured

- Census: `ls -d corpus/fixtures/*/ | wc -l` → **173** (01:22Z). V70 later stated 173/39/134/421; this seat did not re-count the clean/negative split.
- `rg -n exit corpus/fixtures/r99-window-lapse/README.md` → no match (`NO_EXIT_TOKEN`).
- Description vs lapse section (python, same snapshot): description is `At the Chalk Stair at tick 15, the clerk records that the crossing-window named in the original minute has closed; the agreement was unfulfilled; no claim was lodged; the matter stands as a historical open entry.` `Chalk Stair` is not in the lapse section. `historical open entry` is in both.
- README:11 contains `the window closed per the original minute's terms` and `so nothing is resolved`. Map:69 contains `per that minute's terms`. Neither phrase is in the lapse quotes (lines 70–74).
- SKILL.md:98–100 (unchanged vs `4265df5`) still says 17 cases and five JSON tables, and `BR-01's markdown/prose half remains open`.
- Parent stray listing: 8 files under `/home/vgpnk/Projects/shokunin/.ufo/waves/round-99/seats/` (V69 empty tool/contract copies; V73 self-test `.out`/`.err`). Not deleted.
- Hashes at 01:51–01:56Z (tool stable across those two reads):

```
fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c  corpus/tools/dependency_freeze.py
8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628  corpus/tools/dependency-freeze-contract.json
294dd56f29ce1fd40be3a80d365b33724c9cd1969d3f7b7abb271fd1adaaa207  corpus/tools/README.md   (unchanged vs 4265df5)
22ffaa822ec7614fa85322f7fa07e6f369c0888e1107f9f297f76a14e18c20c5  SKILL.md                 (unchanged vs 4265df5)
```

Fixture hashes at 01:22Z, still the S4-declared README/map (`b9320941…` / `d2fe20e5…`) and S3 lapse tables (`timeline` `2cdb9fda…`, `sources` `8c215b38…`, excerpts `fefebaf9…`). Full 64-hex in the JSON.

Not run here: `dependency_freeze` self-test, chain verify, `check_bible`, `support_check`, `map_obligations`. Gate numbers below are seat-stated.

## Verdicts recorded as the seats state them

Not adopted as this ledger's scores.

- **S1 (post-cap):** PASS — ten-file pins, schema 2, chain 6/6, self-test 18/18, `DIGEST-MISMATCH` names the file. Own bound: anchored r94 "depends on" removal is not invisible to `support_check` (exit 1, J14) before the upgrade; a non-anchor excerpt edit is the invisible-before case. `r99-window-lapse` not pinned, on purpose.
- **S3:** PASS on 6/1/8, CLEAN, seven files byte-identical to r98. README/map clause in that report was true at write time and is stale after S4.
- **S4:** PASS on 21/21 map and the three gates. Lexical PASS is not a whole-claim pass (V14).
- **Depth:** V29 **INCONCLUSIVE** (component 1 bounded on delivered bytes; component 2 ABSENT). V51 **INCONCLUSIVE** (same split; its V29 crosscheck was ABSENT at its own poll — V29 later landed). V105 **FAIL**, V14 **FAIL**, V95 **FAIL** — recorded, not re-rolled.
- **Coverage slice:** V63 **FAIL** (tick-15 edge unpinned, `UNPINNED-FIXTURE` exit 2). V81 ABSENT-as-poll, same bound on the stable contract.
- **Calibration:** not scored here. V52 ABSENT (S1/S2 reports missing at its cap). C1 seats that PASS'd against `6f81f8be…` (V62, V76, V94) are stale relative to `fb9bb9ff…` unless re-run (V91). V06/V07/V89/V97 ABSENT at their caps, before S1's 22:48 report.
- **Freshness:** V32 ABSENT; V91 ABSENT, agreeing, and naming the `6f81f8be…` → `fb9bb9ff…` move.
- **Operability:** V26 ABSENT for the missing addendum/notes; S4's three commands ran exit 0 as written. V82 ABSENT.
- **Adjacency:** V33 and V27 ABSENT (producer gate). V68 PASS (two sibling HEADs predate `4265df5`).
- **Registry:** V73 FAIL and V96 FAIL — SKILL freeze row still 17 cases / five JSON tables while the executed tool (on the bytes they ran) printed 18/18 and ten-file pins. V96 also says five registry rows, not six — recorded as stated, not re-counted here.
- **Presence:** V39 PASS at a 15-report census that V123 already called stale. V123 **INCONCLUSIVE** (73/127 others at 22:46:33; S1/S2/S5 and both notes ABSENT then). S1's report did not exist at that cutoff.

## NB — bounds named this round

| ID | Axis | Bound | Evidence | Owner round |
|---|---|---|---|---|
| NB-01 | process | Producer conjunction failed. Poll cap 01:15:21Z missed S1, S2, and S5. At 01:56Z S2 and S5 reports and both knowledge files are still absent. C2 component 2 was not delivered. | poll.log; `ls` at 01:56:04Z; V18/V19/V32/V44/V59/V60/V84/V98/V122 | r99 L1 (do not treat the table as delivered); r100 if still missing at closure |
| NB-02 | depth | `clerk-lapse-recorded` description locative `At the Chalk Stair` is not in the lapse note (quotes or scope) and the map does not flag it. `place_id: chalk-stair` is the schema slot, not the out-claim. | my containment check; V105 FAIL; V14 O2 | r99 closure (S3 string) or r100 |
| NB-03 | depth/docs | README:11 `per the original minute's terms` and `so nothing is resolved`, and map:69 `per that minute's terms`, are not in the lapse quotes. S4's seat prompt asked for the first phrase; the declaration does not. | my reads of README:11 and map:69; V14 FAIL; V105 adjacent note | r99 closure (S4) or r100 |
| NB-04 | depth | Quoted lines 70–73 have no first person. Under V95's criterion they are world-assertions, not the r98 first-person recording class. Only line 74 is clerk-record. Not re-judged against the declaration. | V95 FAIL; my print of lines 70–74 (`I` only on 74) | r99 closure or r100, if that class is adopted |
| NB-05 | depth | V14 treats the description's post-semicolon `historical open entry` clause as its own claim. V105 treats the same phrase as in-note and not an out-claim. Divergence stands. | V14 bottom line; V105 phrase table | same owner as NB-02; do not smooth |
| NB-06 | coverage | `r99-window-lapse` is not a freeze pin. Verify is `UNPINNED-FIXTURE` exit 2. S1 says the chain is the existing six, on purpose. Declaration did not require a seventh pin. Same class as r97 before r98. | S1 §What changed; V63 FAIL; V81; V21 | r100 |
| NB-07 | calibration/docs | BR-01 prose half is **not closed in the docs**, and S1's own before-state is narrower than the declaration. Anchored "depends on" removal exits 1 on `support_check` (J14) before the upgrade. A non-anchor excerpt edit is the invisible-before case. Edit-detectable is not semantics-provable. This seat did not replay either half. | S1 bottom line; SKILL.md:100; tools README Round-98 addendum still says the half is open | S2 if it lands; else r99 closure doc pass / r100 |
| NB-08 | freshness | SKILL.md:98–100 still says 17 cases and five JSON tables. Tools README is the r98 closure text. V73 and V96 FAIL the registry row against the executed tool. | SKILL.md:98–100; V73; V96; `git diff --name-status 4265df5` omits SKILL.md and tools README | S2 / r99 closure |
| NB-09 | docs | r99 fixture README replay block (lines 23–29) lists three commands and records no exit. Sixth recurrence of the r94-BR-17 / r98-NB-08 class. V56 ran them green; the file does not say so. | my `rg`; README:23–29; V56 | r100 fixture docs |
| NB-10 | process | Placeholder-poll hazard recurred. S3 left README and the map as r98 byte copies until S4 rewrote them. Existence-only polls are unsafe on this fixture. | S3 §Not done; S4 §A; V80 first look; V105 poll table | r100 wave design |
| NB-11 | process | Tool bytes moved during the wave: `1728ed89…` (early), `6f81f8be…` (01:22–01:33), `fb9bb9ff…` (mtime 22:38:11, stable at 01:51 and 01:56). Contract stayed `8c2561b0…` from 22:08:46. Receipts pinned to `6f81f8be…` are not receipts for `fb9bb9ff…`. S1's report does not print its own file hash. | my sha256 reads; V91 | r99 closure re-measure; do not credit C1 from the earlier hash |
| NB-12 | hygiene | Parent-repo writes, r94-F01 / r98-NB-07 class: 8 files under `/home/vgpnk/Projects/shokunin/.ufo/waves/round-99/seats/` — V69-scratch empty `dependency_freeze.py` and contract copies; V73-scratch self-test stdout/stderr (three `.out` empty, three `.err` 126–129 B). Lane tree is not the parent tree. | `find` at 01:51Z; V87 (8 parent-repo files) | r99 closure hygiene (L1) |
| NB-13 | process | S3's "README and map still say r98" was true at S3's write and false after S4 (map `d2fe20e5…`, README `b9320941…`). | S3 §Not done; S4 §E; V14 producer cross-check | record |
| NB-14 | calibration | Persisted `markdown_tamper` appends one newline. That pins edit detection, not a dependency-wording proof. `r88-m3-maya-cluster/symbolism-clause-map.md` is an eleventh file outside the declared ten and is not pinned. | S1 §What changed and §Self-test | accepted; r100 only if an eleventh file is wanted |
| NB-15 | process | V92 FAIL: one of eight quoted outputs mismatched (V105's fenced `IN_QUOTES=True` is exact-containment false, casefold true). Does not reverse V105's locative FAIL. V50 was absent, so the "different than V50" half is a stall-escape. | V92 | record |
| NB-16 | freshness | Closure surfaces still at `4265df5`: no Round-99 fixtures README section, corpus README still 17-case / five JSON tables, C9 row-8 not shown to this seat (V45 absent). Census on disk is 173 dirs. | V25; V70; my `wc -l` | r99 closure (L1) if the round is completed; else r100 |

## CO — carried r98 items, r99 status

Pointers: `.ufo/waves/round-98/seats/V33-debt.md` and the r98 SCORECARD block. Not re-argued.

| ID | r98 item | r99 status | Owner |
|---|---|---|---|
| CO-01 | BR-01 prose half (CO-19) | **not closed here.** S1 claims edit-detectable, with the anchor caveat in NB-07. Docs still say open (NB-08). Not replayed. | S2 / r99 closure / r100 |
| CO-02 | markdown unpinned (CO-02) | **on-disk claim only, uncredited.** S1 says the ten declared files are pinned. Eleventh file remains (NB-14). | NB-07 / NB-14 |
| CO-03 | checker blind spots (NB-05) | **open.** Consolidated table absent (NB-01). | S5 missed the cap; r100 |
| CO-04 | consistent regeneration exits 0 (CO-09) | **open.** Was a table row. Not re-tested. | r100 |
| CO-05 | `dual_pointer` legacy-dialect scope (CO-08) | **open / accepted.** Not this round's claim. | standing |
| CO-06 | `MALFORMED-MODEL` unpinned (CO-20) | **open.** Not this round's claim. | standing |
| CO-07 | migration broader than path-less (NB-11) | **open.** V89 ABSENT; not probed here. | r100 wording |
| CO-08 | BR-05 scratch at repo root, gitignored | **open / accepted** (relocation only). | standing |
| CO-09 | self-test binds consistency, not truth | **standing.** | standing |
| CO-10 | path-less pin outside `--freeze` still needs a migration run | **standing** (r98 operability). | standing |
| CO-11 | fixture README replay without exits (NB-08) | **recurred** → NB-09 | r100 |
| CO-12 | placeholder-poll hazard (NB-03) | **recurred** → NB-10 | r100 |
| CO-13 | in-round tool-revision flux (NB-06) | **recurred** → NB-11 | r99 closure |
| CO-14 | C9 next row due | **open** (row-8). | r99 closure / r100 |
| CO-15 | SKILL / corpus README / fixtures README stale for the new round | **open.** S2 owns the freeze row and has not landed. | S2 + r99 closure |
| CO-16 | new fixture outside the pin set (r97 class) | **recurred, named as intentional** → NB-06 | r100 |

r98 closure items that the r98 LOG marks discharged (gitignore wording, "lists only", stale `c435239d…` pin, parent `baseline-analyze.txt`, C9 row-7, census 172) are not re-opened here. This seat did not re-audit those closure bytes.

## CL — closure items if anyone later admits a slice

| ID | Item | Owner |
|---|---|---|
| CL-01 | Do not admit C2 component 2. The table and the lapse scope note were absent at the cap and at 01:56Z. | r99 L1 |
| CL-02 | Do not credit C1 from `6f81f8be…` receipts. If C1 is admitted, re-measure on `fb9bb9ff…` / contract `8c2561b0…` after reading S1, and record the anchor-vs-non-anchor before-state (NB-07). This ledger did not do that. | r99 L1 |
| CL-03 | SKILL freeze row and tools README still describe 17 cases and five JSON tables (NB-08). S2 or a closure erratum. | S2 / r99 closure |
| CL-04 | Fixtures README Round-99 append + census 173/39/134/421 (V70; dir count 173 here). | r99 closure |
| CL-05 | Corpus README bullets (r99 fixture, 18-case, ten-file payload) — still the r98 text per V25. | r99 closure |
| CL-06 | C9 row-8. V45 absent; content not prepared here. | r99 closure |
| CL-07 | Repair or explicitly bound NB-02/NB-03/NB-04/NB-05. Do not net V105 and V14 into one sentence. | r99 closure or r100 |
| CL-08 | Parent stray sweep (NB-12). Do not attribute to this seat. | r99 closure (L1) |
| CL-09 | Roster: S2 and S5 absent at write. Verifier absence was still moving (79 reports at 01:47:37Z, 85 at 01:51:29Z). Do not use V39's 15-report census. V123's 73/127 is a later but still pre-S1 snapshot. | r99 L1 / V101 |
| CL-10 | Do not silently pin r99 at closure unless that is a new decision. S1 left it unpinned on purpose (NB-06). | r100 |

## PR — process observations

| ID | Observation | Pointer |
|---|---|---|
| PR-01 | Content gate held. An existence poll would have accepted the r98 README/map copies (NB-10). | poll.log try 1 vs try 4 |
| PR-02 | Many seats correctly returned ABSENT rather than scoring a plan. That is the protocol, not a wave failure by itself. | V06, V07, V17–V19, V32, V33, V44, V52, V59, V60, V84, V98 |
| PR-03 | S1's report at 22:48:57 is after those caps. Seats that stopped at try 40 did not see it. Not a mutual wait. | S1 mtime; V07 cap 22:13:56 |
| PR-04 | V64's ABSENT is the knowledge note, not the excerpt. The excerpt was on disk (`fefebaf9…`) the whole time. | V64 bottom line; my hash |
| PR-05 | V51's "V29 absent" was true at V51's poll and false later. | V51; V29 file |
| PR-06 | V92's quote mismatch (NB-15) is an audit finding, not a second locative ruling. | V92 |
| PR-07 | This ledger did not wait for V34 or V101 (they wait on others, including this file). Subtract-SELF. | roster lines for V34 and V101 |

## ST — stale during compile

| ID | What moved | Pointer |
|---|---|---|
| ST-01 | Tool `6f81f8be…` superseded by `fb9bb9ff…` (mtime 22:38:11). | NB-11; V91 |
| ST-02 | S3's README/map placeholder claim superseded by S4. | NB-13 |
| ST-03 | V39's 15-report census superseded before V123, and V123's 73/127 superseded before S1's report. | V39; V123; S1 mtime |
| ST-04 | Contract interim states before 22:08:46 are not the `8c2561b0…` bytes. | contract mtime |

**Bottom line: ABSENT — producer set incomplete after 40 content-gated tries (01:15:21Z) and still incomplete at 01:56Z (S2 report and bytes absent; S5 report and both knowledge notes absent); S1's report landed after the cap and is recorded, not reproduced; three fixture FAILs stand unre-rolled (V105 locative, V14 glosses plus description clause, V95 world-assertion class) and the tick-15 edge is unpinned (V63).**

## Post-write note (2026-10-18 02:06Z)

The 01:56Z absence of the knowledge files was true at that `ls`. At 02:06:28Z both files exist (mtime 22:57:50 -03, after the snapshot, before this note):

```
4670c0b71668c56c53c0bac90091531d3f0e881c7dcb2ac572d09f96ae22182e  corpus/knowledge/r99-gate-blind-spot-table.md  (20526 B, 270 lines)
96de708f8e984f6f61ee6387342c287a275328a6293da1d225b2ad00040ebb54  corpus/knowledge/r99-lapse-scope-note.md        (14990 B, 71 lines)
```

`S5-*.md` and `S2-*.md` were still absent at that `ls`. The table was not replayed. NB-01's "files absent" clause is the 01:56 snapshot only; the "S5 report absent, component 2 not credited" clause still holds. Bottom line unchanged.
