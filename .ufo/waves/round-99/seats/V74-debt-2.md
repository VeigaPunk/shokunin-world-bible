# V74 — debt-2 (round 99)

**Seat:** V74 debt-2. **Role:** independent debt extraction from this seat's own reads, then merged against V36. No re-adjudication, no axis score, no smoothing. A V36 item is adopted only where this seat re-measured it or where the pointer is a seat report this seat read. Nothing is inferred past that.

**Compiled at:** 2026-10-18 02:12 UTC. Lane root `/home/vgpnk/Projects/shokunin/lore-shokunin`. HEAD `337f0fa` (blocked-dispatch record above the standing r99 declaration). Baseline `4265df5`. Wave tree uncommitted.

**Poll-wait (this seat):** `V74-scratch/poll.sh` + `poll.log`. Content-gated (producer reports, S1/S2 bytes different from `4265df5`, r99 lapse markers, README/map not r98 copies, both knowledge files, and `V36-*.md`). 20 s cadence.

- Tries 1–30 ran under host timeout. The background poll was killed at 600 s (`bash-8gctaodx` timed_out). Log last complete try before the kill: try 30 at 01:12:40Z, still missing S1/S2/S5 reports, S2 bytes, both knowledge files, V36.
- Tries 31–40 resumed in a second process. `ABSENT after 40 tries 2026-10-18T01:25:58Z`. Same misses. No all-reports wait. SELF not included. This is the protocol cap. C2 component 2 was not on disk then; it was not verified as a plan.
- Stall-escape 1 (tries 41–55, recorded): ended still missing `2026-10-18T01:52:11Z`. S1's report had landed during the window; S2/S5/V36/table had not at the escape's own checks.
- Stall-escape 2 (tries 56–70, recorded): ended still missing `2026-10-18T02:05:01Z`.
- Post-escape reads, not a third poll: at 02:07Z `V36-debt.md` and both knowledge files existed; S2 bytes differed from `4265df5`. At 02:11Z `S2-tools-docs.md` and `S5-knowledge-author.md` existed. Those landings are measured below. They do not rewrite the cap.

**Delivered revision this seat re-hashed at 02:11Z** (stable across the 02:07 and 02:11 reads):

- `corpus/tools/dependency_freeze.py` `fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c`
- `corpus/tools/dependency-freeze-contract.json` `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628`
- `corpus/tools/README.md` `837a7f5dfe913047530c7f92f3dd6b3df1b1a83c77ede12ba0c349cc134a049c`
- `SKILL.md` `e0bcb61ab909146e34773dd56219cb1631070c1700a2481f8ad1181f3d864443`
- `corpus/knowledge/r99-gate-blind-spot-table.md` `4670c0b71668c56c53c0bac90091531d3f0e881c7dcb2ac572d09f96ae22182e`
- `corpus/knowledge/r99-lapse-scope-note.md` `96de708f8e984f6f61ee6387342c287a275328a6293da1d225b2ad00040ebb54`
- Earlier tool hashes this seat measured, not the delivered bytes: `65c1ae30…` (01:02Z), `1728ed89…` (01:03Z, markdown parsed as JSON), `6f81f8be…` (01:14–01:19Z, self-test 18/18 and chain 6/6 already held). Contract moved `153ebc5b…` (baseline, still on disk at 01:03Z) → `8c2561b0…` and stayed.

## My own reproduction

Transcripts under `.ufo/waves/round-99/seats/V74-scratch/` (`interim-c1.txt`, `chain-now.txt`, `probe2/`, `replay/`, `mirror-before-real/`, `mirror-after-real/`). Live fixtures were not mutated. Freeze probes used path-bound mirrors because a foreign path is `PATH-MISMATCH`.

**C1, on `fb9bb9ff…` / `8c2561b0…` (02:07Z re-run, after S1's report existed):**

```
python3 corpus/tools/dependency_freeze.py --self-test
SELF-TEST 18/18
RESULT PASS
EXIT:0
```

including `CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok`. Inherited expectations vs `4265df5`: 17 identical, added `markdown_tamper` only, dropped none.

Chain, same bytes:

```
r88-m3-maya-cluster exit 0 DIGEST acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae
r94-paired-crossing exit 0 DIGEST 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef
r95-crossing-aftermath exit 0 DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710
r96-crossing-response exit 0 DIGEST 43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c
r97-crossing-acknowledgment exit 0 DIGEST a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54
r98-clerk-filing exit 0 DIGEST 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0
r99-window-lapse exit 2 FINDING UNPINNED-FIXTURE: no pin for 'r99-window-lapse'
```

6/6 on the declared chain. r99 is not a seventh pin. S1 says that was intentional. This seat agrees the declaration asked for 6/6, not 7/7.

Before/after, scratch only. Baseline tool `git show 4265df5:corpus/tools/dependency_freeze.py` is `03d04365…`. Phrase removed from an r98 excerpt copy: `depends on both ninth-bell entries` → `follows both ninth-bell entries`.

- Baseline: `RESULT PASS` exit 0, digest `59a0f4fa3d4a47e03649a54d1815c45ee1eef641b63a59ebe7210bc9d9b9b133` (unchanged). Newline-append on a second copy: same digest, exit 0.
- Delivered tool+contract, same wording removal: exit 2 `FINDING DIGEST-MISMATCH: … changed: fictional-excerpts.md (sha256 29e384bf… -> dbcd5f11…); pinned-file bytes changed outside the semantic inventory`.
- Non-anchor heading edit on an r94 copy (`# Authored in-world excerpts` plus ` (dependency wording left intact)`): baseline exit 0 digest `2527beb938b474a28d66e1c716f54ba829ae3cc2e616513cd2960a8f7ecebe75`. Delivered: exit 2 `DIGEST-MISMATCH` digest `f559baaa7e6facbefb8a65f6be4eb4b5feb622c233e18bd4ace5ba03c332a034`, changed `fictional-excerpts.md` (`585f4d07… -> 1deff015…`). Same copy: `check_bible` CLEAN exit 0; `support_check` `SOURCE-SUPPORT 14/14` `RESULT PASS` exit 0; `map_obligations` `raw=14 mapped=14` `RESULT PASS` exit 0.

That non-anchor pair matches S1's quoted digests. The anchored removal is not invisible to every gate: on an earlier r98 wording-removal copy, `support_check` stdout contained `FAIL: J14: source-support anchor missing` and `RESULT FAIL`. The exit code of that one run was lost to a pipe (`tail`); this seat does not invent it. S1 quotes exit 1 for the same class on r94. Edit-detectable is not semantics-provable.

Interim defect, closed before the delivered freeze: on tool `1728ed89…` a scratch `--freeze` of r98 printed `FINDING MALFORMED-JSON: README.md: Expecting value: line 1 column 1 (char 0)` exit 2, because `build_model` JSON-parsed every loaded file including Markdown. Current `build_model` parses `DATA_FILES` only. S1's report records the same failed attempt and the fix. Not an open defect on `fb9bb9ff…`.

Contract root `payload_schema_version` is 2 and `pinned_files` lists the ten declared files. Root `data_files` still lists only the five JSON tables. `dependency_freeze.py` does not read `data_files` (no occurrence). A reader of that field alone would think Markdown is unpinned. The scope text and `pinned_files` contradict it.

`names_file` is load-bearing: `dependency_freeze.py:611` requires `names_file` to occur in the case output when the expectation sets it. `markdown_tamper` sets `names_file: fictional-excerpts.md`.

**C2 component 1, live r99 fixture (01:03Z, re-checked still the S4 hashes at V36's 01:22Z snapshot and not rewritten after):**

```
python3 corpus/fixtures/check_bible.py corpus/fixtures/r99-window-lapse
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT:0
python3 corpus/tools/support_check.py corpus/fixtures/r99-window-lapse
SOURCE-SUPPORT 21/21; … VALIDATED-ROWS 23/23
RESULT PASS
EXIT:0
python3 corpus/tools/map_obligations.py corpus/fixtures/r99-window-lapse
OBLIGATIONS raw=21 mapped=21
RESULT PASS
EXIT:0
ls -d corpus/fixtures/*/ | wc -l
173
```

Parsed shape: 6 entities, 1 relation, 8 events, 8 sources, contradictions `[]`. Event `clerk-lapse-recorded` tick 15, actor `clerk-maren`, place `chalk-stair`, `depends_on: ["clerk-filing-open"]`, source `clerk-lapse-note`. Map row J21 is `timeline.json#/7`, span 66-76, anchor the tick-15 sentence at excerpt line 70. This seat did not re-count the 38/134 clean/negative split. V36 cites V70's 173/39/134/421; not adopted as this seat's measurement.

**C2 component 2, table replayed by this seat after it existed (02:08Z, tool/contract hashes above).** Not a verification of S5's scratch trees. Fresh copies under `V74-scratch/replay/`.

| Row | This seat's command result | Matches table exit class |
|---|---|---|
| 1 emptied `depends_on` on r99 `clerk-lapse-recorded` | bible CLEAN 0; support 21/21 PASS 0; map raw=21 mapped=21 PASS 0 | yes |
| 1 freeze, r98 `clerk-filing-open` emptied | `REDUCTION-DETECTED` `lost depends_on ['acknowledgment-aru-records']` exit 1 | yes |
| 2 wrong-but-earlier, r98 edge set to `response-evin-salt-court` | `ADDITION-DETECTED` + `REDUCTION-DETECTED` exit 1; bible CLEAN 0 | yes |
| 3 delete r99 terminal event, map row kept | bible CLEAN 0; support PASS 0; map `phantom_obligation: timeline.json#/7` exit 1 | yes |
| 4 J05 span `17`→`20` | support FAIL `outside-span=17` exit 1; map PASS 0; bible CLEAN 0 | yes |
| 5 r99 `source_id` rebound to `clerk-filing-note` | bible CLEAN 0; support 21/21 PASS 0; map `source_id_mismatch: timeline.json#/7 does not bind to 'clerk-filing-note'` exit 1 | yes |
| 6 non-anchor / wording removal | see C1 above | yes for the classes this seat ran |
| 8 checker pin | live checker `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`; `boundary_doc_check` `CERTIFIED` exit 0; one-comment copy `checker_drift` exit 1 | yes |
| 9 unknown event `no-such-event` | `VIOLATION: timeline[7].depends_on: unknown event 'no-such-event'` exit 1 | yes (not a blind spot) |

Not re-run by this seat: row 1b (drop one of two predecessors) and row 7 (consistent regeneration). S5's report states both. This seat does not adopt those two as its own measurements and does not contradict them.

**Depth bounds re-read on the live lapse files (02:11Z):**

- Description: `At the Chalk Stair at tick 15, the clerk records that the crossing-window named in the original minute has closed; the agreement was unfulfilled; no claim was lodged; the matter stands as a historical open entry.`
- `Chalk Stair` is not in the Round-99 lapse section. `historical open entry` is in both the description and quote line 73.
- `minute's terms` is in `README.md` and `claim-excerpt-map.md`, not in the lapse section.
- Quote lines 70–73 contain no standalone `I`. Line 74 does: `I record no resolution, assign no blame, and reconcile nothing.`
- `rg`/`in` check: `exit` is not in `corpus/fixtures/r99-window-lapse/README.md`.

**Docs this seat read after S2's bytes landed:**

- `SKILL.md:98-100` now says 18 cases, ten-file payload, schema 2, and "BR-01's prose half is now any prose edit is detectable, not dependency semantics provable." The r88 extra file is named as unpinned. This supersedes the 17-case / five-table sentence V36 read at 01:56Z.
- `corpus/tools/README.md:290-310` Round-99 addendum supersedes the r97/r98 "five JSON tables only" and "prose half remains open" sentences and the 17-case count. Historical sentences are kept. This seat did not re-run S2's r95 scratch demo.
- `corpus/README.md:40` still says rounds 96–98, 17-case, five JSON tables only. Not S2's file.
- `corpus/fixtures/README.md:1259` still says 17 cases, five JSON tables, BR-01 prose half open. No Round-99 section found by this seat's grep. Census line at `:1263` is still 172. On-disk count is 173.

**Parent strays (02:11Z, `find`):** 8 files under `/home/vgpnk/Projects/shokunin/.ufo/waves/round-99/seats/` — V69-scratch empty tool/contract copies (2) and V73-scratch self-test `.out`/`.err` (6). Lane `git status --porcelain --untracked-files=no` is only `SKILL.md`, `corpus/tools/README.md`, `dependency_freeze.py`, `dependency-freeze-contract.json`. Not deleted.

## Merge against V36

V36 file: `.ufo/waves/round-99/seats/V36-debt.md` (136 lines at the 01:56Z body, plus a 02:06Z post-write note). V36's bottom line is **ABSENT**. That line was true of their poll cap (01:15:21Z) and of their 01:56Z `ls`. Their post-write note already records that both knowledge files existed at 02:06Z and that they did not replay the table. This seat does not re-roll that ABSENT. It records what changed after it, from commands this seat ran.

**Agree (re-measured, same fact):**

- NB-02 locative `At the Chalk Stair` is in the description and not in the lapse section.
- NB-03 `per the original minute's terms` / `minute's terms` is in README and the map, not in the lapse quotes.
- NB-04 quotes 70–73 have no `I`; line 74 does.
- NB-06 / CO-16 r99 is `UNPINNED-FIXTURE` exit 2. Declaration asked for 6/6. Same class as r97 before r98.
- NB-09 / CO-11 README replay block has no exit token. Sixth recurrence.
- NB-10 / CO-12 placeholder-poll hazard. S3 left README and the map as r98 copies; S4 rewrote them. This seat's content gate did not accept the placeholders.
- NB-11 / CO-13 tool-revision flux. This seat adds an earlier hash (`65c1ae30…`) before the three V36 named.
- NB-12 parent-repo writes: 8 files, same two seats. Confirmed, not deleted.
- NB-13 S3's "README and map still say r98" was true at S3's write and false after S4.
- NB-14 `markdown_tamper` appends a newline. Edit detection, not a wording proof.
- CO-08 BR-05 scratch-at-root, gitignored. `git check-ignore -v` on `dependency-freeze-self-test-abc/` → `.gitignore:4:*-self-test-*/`.
- Depth FAILs V105 / V14 / V95 and coverage FAIL V63 are recorded as those seats state them. This seat confirmed the textual facts under NB-02/03/04 and the unpinned edge. It does not pick a winner between V14 and V105 on whether `historical open entry` is its own claim (V36 NB-05). The phrase is in the note (line 73) and in the description.

**Supersede (true at V36's snapshot, false on the bytes this seat read at 02:11Z):**

- NB-01 / CL-01 "knowledge files absent / do not admit component 2 because the files are missing." The files exist (`4670c0b7…`, `96de708f…`). S5's report exists. This seat replayed rows 1–5, 6 (the classes above), 8, and 9; they match the table's exit classes. Row 1b and row 7 were not re-run here. V36's "not replayed" clause remains true of V36. It is not true of this seat.
- NB-07 / NB-08 / CL-03 / CO-01 / CO-15 as applied to `SKILL.md` and `corpus/tools/README.md`. Those two files now state 18 cases, ten-file pins, and edit-detectable-not-semantics-provable, including the support_check J14 bound (S2's report, and this seat's read of `SKILL.md:98-100` and README `:290-310`). The "docs still say open" clause remains true of `corpus/README.md:40` and `corpus/fixtures/README.md:1259`.
- CL-02 "this ledger did not re-measure C1 on `fb9bb9ff…`." V36 did not. This seat did. Chain digests match S1's report. Self-test 18/18. Non-anchor before/after digests match S1's quotes.

**Add (not in V36, because they had not read the contract or the later bytes):**

- Contract root `data_files` still names only the five JSON tables while `pinned_files` names ten. The tool does not consult `data_files`. See NB-17 below.
- Interim `MALFORMED-JSON` on README during S1's edit (`1728ed89…`), fixed before the delivered freeze. S1 discloses it. See ST-05.
- Host killed this seat's first poll at 600 s / try 30. The protocol cap was still completed (tries 31–40). See PR-08.
- S2 and S5 reports exist at 02:11Z. V36's roster line (CL-09) is the 01:56Z snapshot. Do not use it as the closure census.

**Contradict:** none on a fact both seats measured on the same bytes. V36's ABSENT is a time-bounded producer-set finding, not a claim that the later files are empty. This seat does not call that finding false.

## NB — bounds named from this seat's reads

V36 IDs are kept where the fact is the same. NB-17 is new.

| ID | Axis | Bound | Evidence | Owner |
|---|---|---|---|---|
| NB-02 | depth | Description locative `At the Chalk Stair` is not in the lapse section. `place_id` is the schema slot. | this seat's containment check; V36 NB-02; V105 FAIL (as V36 records it) | r99 closure or r100 |
| NB-03 | depth/docs | `minute's terms` is in README and the map, not in the lapse quotes. | this seat's reads; V36 NB-03; V14 FAIL (as V36 records it) | r99 closure or r100 |
| NB-04 | depth | Quotes 70–73 have no first person. Line 74 does. | this seat's print; V36 NB-04; V95 FAIL (as V36 records it) | r99 closure or r100, if that class is adopted |
| NB-05 | depth | V14 and V105 disagree on whether the description's `historical open entry` clause is its own claim. The phrase is in quote line 73. Not smoothed. | V36 NB-05 | same owner as NB-02 |
| NB-06 | coverage | r99 is outside the freeze chain. `UNPINNED-FIXTURE` exit 2. Declaration asked for 6/6. A dropped tick-15 edge is not a freeze finding until a later pin. | this seat's chain run; S1; V36 NB-06; V63 FAIL (as V36 records it) | r100 |
| NB-09 | docs | r99 README replay block records no exits. | this seat's `in` check; V36 NB-09 | r100 fixture docs |
| NB-10 | process | Placeholder-poll hazard recurred. | S3 §Not done; S4 §A; this seat's content gate | r100 wave design |
| NB-11 | process | Tool bytes moved during the round (`65c1ae30…`, `1728ed89…`, `6f81f8be…`, `fb9bb9ff…`). Contract settled at `8c2561b0…`. Receipts pinned to `6f81f8be…` are not receipts for `fb9bb9ff…`. | this seat's sha256 reads; V36 NB-11 | r99 closure re-measure |
| NB-12 | hygiene | 8 parent-repo files under `/home/vgpnk/Projects/shokunin/.ufo/waves/round-99/seats/` (V69, V73). | this seat's `find`; V36 NB-12 | r99 closure (L1) |
| NB-16 | freshness | `corpus/README.md:40` and `corpus/fixtures/README.md:1259` still say 17 cases / five JSON tables / BR-01 open. Fixtures README census line is still 172. On-disk dirs: 173. SKILL and tools README are no longer in this class. | this seat's greps; V36 CL-04/CL-05, narrowed | r99 closure (L1) |
| NB-17 | freshness | Contract `data_files` still lists the five JSON tables. `pinned_files` lists ten. The tool does not read `data_files`. | this seat's contract read and grep of `dependency_freeze.py` | r99 closure or r100 wording |

## CO — carried r98 items, r99 status

Pointers: V36's CO table, `.ufo/waves/round-98/seats/V33-debt.md`, r98 SCORECARD. Not re-argued except where this seat re-measured.

| ID | Item | r99 status |
|---|---|---|
| CO-01 | BR-01 prose half | **narrowed, not semantics-closed.** Delivered pin names a non-anchor excerpt edit (`DIGEST-MISMATCH` exit 2) that the r98 tool missed (exit 0). Anchored removal was already `support_check` FAIL. SKILL and tools README now say that. `corpus/README.md` and fixtures README still say the half is open (NB-16). |
| CO-02 | markdown unpinned | **closed for the declared ten** on the six chain fixtures (this seat's chain run and pin key count). **open** for r99 (NB-06) and for any eleventh file S1/SKILL name (`symbolism-clause-map.md` — seat-stated, not re-listed here). |
| CO-03 | checker blind spots | **documented and re-measured** for rows 1, 2, 3, 4, 5, 8, 9. Rows 1–3 still leave `check_bible` CLEAN. Row 1b and row 7 not re-run here. |
| CO-04 | consistent regeneration exits 0 | **not re-tested by this seat.** S5 states map/support/bible stay green and freeze still catches the JSON deletion. |
| CO-08 | BR-05 scratch at repo root, gitignored | **open / accepted** (relocation only). check-ignore confirmed. |
| CO-11 | README replay without exits | **recurred** → NB-09 |
| CO-12 | placeholder-poll hazard | **recurred** → NB-10 |
| CO-13 | in-round tool flux | **recurred** → NB-11 |
| CO-14 | C9 next row | **open.** This seat did not see a row-8. V36 CO-14 stands. |
| CO-15 | registry/README staleness | **split.** SKILL freeze row and tools README updated. Corpus README and fixtures README not (NB-16). |
| CO-16 | new fixture outside the pin set | **recurred, named as intentional** → NB-06 |

r98 closure items the r98 LOG marks discharged (gitignore wording, "lists only", stale `c435239d…` pin, parent `baseline-analyze.txt`) were not re-opened. This seat confirmed the gitignore half only.

## CL — closure items

| ID | Item | Owner |
|---|---|---|
| CL-01 | Do not treat V36's 01:56Z ABSENT as the producer census. S1–S5 reports and both knowledge files existed at 02:11Z. Do not treat this seat's cap (01:25:58Z) as that census either. | r99 L1 |
| CL-02 | If C1 is admitted, the re-measure is already on `fb9bb9ff…` / `8c2561b0…` (this seat and S1). Record the anchor-vs-non-anchor before-state. Do not credit `6f81f8be…` receipts as the final tool. | r99 L1 |
| CL-03 | Corpus README `:40` and fixtures README `:1259` plus census 172 → 173. SKILL and tools README are done. | r99 closure (L1) |
| CL-04 | C9 row-8. Not prepared here. | r99 closure |
| CL-05 | Repair or explicitly bound NB-02/NB-03/NB-04/NB-05. Do not net V105 and V14 into one sentence. | r99 closure or r100 |
| CL-06 | Parent stray sweep (NB-12). Not this seat's files. | r99 closure (L1) |
| CL-07 | Do not silently pin r99 at closure unless that is a new decision (NB-06). | r100 |
| CL-08 | Contract `data_files` vs `pinned_files` (NB-17). | r99 closure or r100 |
| CL-09 | Row 1b and row 7 were not replayed by this seat. If admission of component 2 requires every row, use S5's quotes or re-run. This seat's rows 1–5, 6 (classes above), 8, 9 matched. | r99 L1 |

## PR — process

| ID | Observation | Pointer |
|---|---|---|
| PR-01 | Content gate held. An existence poll would have accepted the r98 README/map copies. | this seat's poll try 1; S4 §A |
| PR-02 | V36 returned ABSENT at their cap rather than scoring a plan. Correct for 01:15Z. | V36 poll.log |
| PR-03 | V36 did not stall. This seat did, twice, after the cap, and recorded both. The later landings are why this ledger is not a copy of V36's ABSENT. | poll.log stall markers |
| PR-04 | S1, S2, and S5 reports all landed after verifier caps that waited only 40 tries. Not a mutual wait. V36's poll does not wait on V74. | S1/S2/S5 mtimes vs cap lines |
| PR-05 | This seat did not wait on an all-reports poll and did not include itself. | protocol |
| PR-08 | Host timeout killed the first poll at 600 s / try 30. The remaining tries were a resume, not a second 40. | task `bash-8gctaodx` |

## ST — stale during this compile

| ID | What moved | Pointer |
|---|---|---|
| ST-01 | Tool `6f81f8be…` superseded by `fb9bb9ff…`. Chain digests did not move between those two hashes on the runs this seat kept. | NB-11 |
| ST-02 | S3's README/map placeholder claim superseded by S4. | NB-13 |
| ST-03 | V36's 01:56Z "S2/S5/files absent" superseded by the 02:06Z note (files) and by this seat's 02:11Z `ls` (reports). V36's bottom line was not rewritten. | V36 post-write note; this seat's `ls` |
| ST-04 | V36 NB-07/NB-08 as applied to SKILL and tools README. Those files changed after 01:56Z. | SKILL `e0bcb61a…`; README `837a7f5d…` |
| ST-05 | `1728ed89…` `MALFORMED-JSON` on README. Fixed before the delivered freeze. S1 records it. | this seat's scratch `--freeze`; S1 §Chain |

---

This seat wrote only this report and `V74-scratch/`. No commit. No push. Producer bytes were not edited.

**Bottom line: PASS (ledger compiled and merged) — independent extraction on `fb9bb9ff…` / `8c2561b0…` (self-test 18/18, chain 6/6, r99 `UNPINNED-FIXTURE` exit 2, non-anchor prose edit invisible before and `DIGEST-MISMATCH` naming the file after) plus a post-landing replay of blind-spot rows 1–5, 6 (classes run here), 8, and 9 matching the table; merged against V36 without re-rolling their 01:56Z ABSENT; their doc-staleness and "table absent" clauses are superseded for SKILL, tools README, and the two knowledge files, and still open for corpus README, fixtures README census 172, C9 row-8, the unpinned r99 edge, the locative/first-person depth bounds, contract `data_files`, and the 8 parent-repo strays.**
