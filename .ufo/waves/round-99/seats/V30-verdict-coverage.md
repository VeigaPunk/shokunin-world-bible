# V30 — verdict-coverage (round 99, single-wave)

**Seat scope (verbatim):** *V30 verdict-coverage — report .ufo/waves/round-99/seats/V30-verdict-coverage.md — Read the cross-cutting seats; one COVERAGE verdict (honest — what surface actually grew).*

Lane root for every command: `/home/vgpnk/Projects/shokunin/lore-shokunin` (session cwd is the parent repo). Baseline r98 closure `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`). HEAD during the wave `337f0fa` (blocked-dispatch record; wave tree uncommitted). Leaf seat: no nested agents, no commits, no pushes, no network. Writes: this report and `.ufo/waves/round-99/seats/V30-scratch/` only. Seats-dir realpath checked before writing: `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats`.

## 0. Revision pinned for the verdict (re-checked 2026-10-17T23:10:32-0300)

```
fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c  corpus/tools/dependency_freeze.py
8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628  corpus/tools/dependency-freeze-contract.json
837a7f5dfe913047530c7f92f3dd6b3df1b1a83c77ede12ba0c349cc134a049c  corpus/tools/README.md
e0bcb61ab909146e34773dd56219cb1631070c1700a2481f8ad1181f3d864443  SKILL.md
4670c0b71668c56c53c0bac90091531d3f0e881c7dcb2ac572d09f96ae22182e  corpus/knowledge/r99-gate-blind-spot-table.md
96de708f8e984f6f61ee6387342c287a275328a6293da1d225b2ad00040ebb54  corpus/knowledge/r99-lapse-scope-note.md
```

Baseline freeze pair, copied before S1 wrote (`V30-scratch/baseline-*`): tool `03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b`, contract `153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947` (schema 1, 17 cases, six pins, five JSON files each).

Mid-flight, recorded, not scored as the verdict: an early tool (`65c1ae30…`, then `1728ed89…`) JSON-parsed Markdown and a scratch `--freeze` exited 2 `MALFORMED-JSON: README.md`. S1's report records the same failed attempt. The delivered `build_model` parses only `DATA_FILES`. A later string edit moved the tool `6f81f8be…` (29104 bytes, 22:07:33) → `fb9bb9ff…` (29110 bytes, 22:38:11). Every number below was re-run on `fb9bb9ff…` / `8c2561b0…` except where a quote is labeled as the earlier tool.

## 1. Poll-wait record

Content-gated. A byte-identical r99 copy of r98 (present at 22:01, ten `cmp` identical) was not delivery.

- Poll v1 killed immediately (false hit: pin shape was a dict, and S3's report appeared while the contract was still five-file). Log kept as `V30-scratch/poll-v1.log`.
- Poll v2 (`V30-scratch/poll.sh`), 20 s, 40 tries, 22:02:29–22:15:29. Try 40: `ev=1 note=1 schema=2 npins=6 pins10=6 mdcase=yes table=no s1=no s3=yes s4=yes s5=no`. Line: `ABSENT after 40 tries`. SELF was not in the wait set.
- Bounded stall-escape (`poll-escape.sh`), 15 more tries, expired 22:34:07 still `s1=no s5=no table=no`. Recorded, not fatal.
- After the budget, not a 41st protocol try: S1 report landed 22:48 (`S1-full-file-pins.md`); README/SKILL moved 22:51 (and README again by 23:08, hash above); table + lapse note landed 22:57. S2 and S5 reports were still absent at 23:10:32. The table was scored from its bytes and from a replay of S5's scratch mutants, not from a plan and not from an S5 report.

## 2. What surface actually grew

### 2.1 Pin payload width (C1) — grew, 5 files → 10

Contract `schema_version` 1→2, root `payload_schema_version` 2. Pin set is still exactly the six chain names. Against the saved baseline contract, every pin's five JSON digests are identical and the five added keys are `README.md`, `claim-excerpt-map.md`, `fictional-excerpts.md`, `inspiration-note.md`, `source-excerpt.md`. Each delivered pin has `payload_schema_version` 2 and `nfiles=10`.

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r88-m3-maya-cluster
DIGEST acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae
RESULT PASS
EXIT:0
```

Same command, the other five, each `RESULT PASS` exit 0: r94 `048b8ff3…`, r95 `97cffd7b…`, r96 `43911900…`, r97 `a28b9ea0…`, r98 `5ecf84e1…`. **6/6.** Content digests moved because Markdown entered the payload. JSON-table digests did not.

```
$ python3 corpus/tools/dependency_freeze.py --self-test
CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
SELF-TEST 18/18
RESULT PASS
EXIT:0
```

17 inherited case ids still pass. The 18th persisted case is a trailing newline on `fictional-excerpts.md` only. The other nine files are not persisted cases; they were probed (below).

Before, baseline tool, path-bound mirror, append `\nThe window closed.\n` to `inspiration-note.md`:

```
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
DIGEST 59a0f4fa3d4a47e03649a54d1815c45ee1eef641b63a59ebe7210bc9d9b9b133
RESULT PASS
exit=0
```

That digest is the r98 JSON-only pin. The edit was invisible.

After, delivered tool `fb9bb9ff…` in `V30-scratch/mirror` (live contract not written; mirror restored to `RESULT PASS` after):

```
FINDING DIGEST-MISMATCH: content digest 3dfc28b40f129772674026536aa6d3d198c921008e5a9666dd46e8d8b5acd637 != pin 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0; changed: inspiration-note.md (sha256 58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37 -> 76faa1e01f5bb5e4730924c40029a9eb7f8314c660c9ac1c6c7cc0d61802e3e1); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
exit=2
```

Companion gates on that same edited copy: `check_bible` CLEAN exit 0, `support_check` RESULT PASS exit 0, `map_obligations` RESULT PASS exit 0. This is the class that grew: a non-anchor Markdown byte edit, previously green on every fixture gate, now exit 2 naming the file.

On tool `6f81f8be…` (pre string-edit, same contract) a one-trailing-newline tamper of each of the ten r98 files, path-bound mirror, each exited 2 `DIGEST-MISMATCH` and the finding named that file. S1's report and V02 (`V02-c1-markdown-tamper.md`, PASS) cover the same class on the delivered tool, including one-word edits of all five r94 Markdown files. I did not re-walk all ten on `fb9bb9ff…`; the inspiration-note case above is the one re-quoted on the final tool. The finding suffix changed with the string edit (`pinned-file bytes changed outside the semantic inventory`); the exit and the named file did not.

`r88-m3-maya-cluster/symbolism-clause-map.md` exists and is not in that pin's `files`. Files outside the declared ten did not enter the surface.

### 2.2 Fixture extent (C2 component 1) — grew by one directory, not by one pin

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r99-window-lapse
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT:0

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r99-window-lapse
OBLIGATIONS raw=21 mapped=21
RESULT PASS
EXIT:0

$ python3 corpus/tools/support_check.py corpus/fixtures/r99-window-lapse
SOURCE-SUPPORT 21/21
RESULT PASS
EXIT:0
```

Parsed counts: entities 6, relations 1, timeline 8, sources 8, contradictions 0. Last event `clerk-lapse-recorded` tick 15, `entity_id` `clerk-maren`, `place_id` `chalk-stair`, `depends_on` `["clerk-filing-open"]`, `source_id` `clerk-lapse-note`. Before S4's map landed, the same fixture was `OBLIGATIONS raw=21 mapped=20` / `FINDING missing_obligation: timeline.json#/7` exit 1. After S4: 21/21. J21 anchor is the tick-15 window-closed sentence.

Census: `find corpus/fixtures -mindepth 1 -maxdepth 1 -type d | wc -l` → 173; excluding `r99-window-lapse` → 172. V40 and V70 independently report archive `4265df5` = 172/38/134/421 and the delivered tree = 173/39/134/421, delta exactly this directory. I did not re-run their full census script.

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r99-window-lapse
FINDING UNPINNED-FIXTURE: no pin for 'r99-window-lapse' in corpus/tools/dependency-freeze-contract.json (pinned: ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response', 'r97-crossing-acknowledgment', 'r98-clerk-filing'])
RESULT ERROR
EXIT:2
```

Declared chain is 6/6, not 7/7. S1 states the same. The new beat is covered by the existing lexical gates. It is not freeze-gated.

### 2.3 Blind-spot table (C2 component 2) — a record landed; the blinds did not close

`corpus/knowledge/r99-gate-blind-spot-table.md` (20526 bytes, 22:57:50, sha256 `4670c0b7…`) and `corpus/knowledge/r99-lapse-scope-note.md` (`96de708f…`) were absent through the poll and the stall-escape. They were on disk at the 22:59 recheck. S5's producer report was still absent at 23:10:32. The table's own header says freeze quotes were re-run on tool `fb9bb9ff…` / contract `8c2561b0…`, which matches the bytes I measured.

I re-ran the lexical gates on S5's scratch mutants (live tools, no corpus write). Observed exits match the table's "does not" / "catches" columns:

| mutant | bible | support | map |
|---|---|---|---|
| m1-empty-deps | 0 CLEAN | 0 PASS | 0 raw=21 mapped=21 |
| m2-wrong-earlier | 0 CLEAN | 0 PASS | 0 PASS |
| m3-delete-terminal | 0 CLEAN | 0 PASS | 1 `phantom_obligation` timeline.json#/7 |
| m4-span-break | 0 CLEAN | 1 J05 outside span 20 | 0 PASS |
| m5-source-id | 0 CLEAN | 0 PASS 21/21 | 1 `source_id_mismatch` … `clerk-filing-note` |
| m6-consistent-regen | 0 CLEAN | 0 PASS 20/20 | 0 raw=20 mapped=20 |
| m7-prose-coherent | 0 CLEAN | 0 PASS | 0 PASS |
| m7b-excerpt-only | 0 CLEAN | 1 J14 anchor missing | 0 PASS |
| m9-unknown-event | 1 unknown event | 0 PASS | 0 PASS |
| m9-drop-depends-key | 1 required nonempty list | 0 PASS | 0 PASS |
| m9-delete-predecessor | 1 unknown event `clerk-filing-open` | 0 PASS | 1 (phantom + source_id_mismatch) |

Path-bound freeze mirrors, tool hash prefix `fb9bb9ff608c`:

- `work3/empty`: exit 1 `REDUCTION-DETECTED: event clerk-filing-open lost depends_on ['acknowledgment-aru-records']`
- `work3/prose`: exit 2 `DIGEST-MISMATCH` naming `claim-excerpt-map.md` (and the table's quote also names `fictional-excerpts.md`; my print was truncated at 240 chars, exit class matches)
- `work4/span`: exit 2 `DIGEST-MISMATCH` naming `claim-excerpt-map.md`, content digest `09858d77…` as the table quotes
- `work4/regen`: exit 1 `REDUCTION-DETECTED: event clerk-filing-open is missing`
- `work4/narr`: exit 2 `DIGEST-MISMATCH` naming `claim-excerpt-map.md`

```
$ python3 corpus/tools/boundary_doc_check.py
CERTIFIED (bounded: frozen-document drift + receipts + explicit-anchor range + structure; no semantic/AST validation)
exit=0
```

I did not re-run row 8's drifted-checker probe or every row-9 twin. The rows I did re-run match. The table does not close rows 1–3, 5's `support_check` silence, 7's coherent regeneration, or 8's frozen checker. It consolidates them. Row 6 records both the historical invisibility and the C1 close, and it records the contradiction with the declaration: excerpt-only removal of the J14 anchor is already `support_check` exit 1. S1's report and V03 (`FAIL` on that overclaim, freeze before/after holds) say the same thing. I agree. The surface that grew is byte-edit detection, not a semantic dependency proof.

"Every row replay-verified by at least two seats" is not something I can confirm from reports. The table-citation seats I read (V17, V18, V44, V59, V60, V98, V122) filed ABSENT before 22:57. My replay is one seat, after delivery, on the scratch trees the table names.

### 2.4 Documented command surface — grew late

At poll cap, README `294dd56f…` and SKILL `22ffaa82…` were byte-identical to my baseline snapshot, and V102 correctly reported ABSENT (no Round-99 section, no commands to run). By 23:10 both files had moved. `corpus/tools/README.md:290` is `### Round-99 addendum: full-file pin payload, Markdown-tamper detectability, 18-case self-test, chain re-frozen 6/6`. The addendum says the five-JSON-only bound and "prose half remains open" are superseded, and that `python3 corpus/tools/dependency_freeze.py --self-test` prints `SELF-TEST 18/18`. That command, run by me on the pinned tool, did. SKILL freeze row now says 18 cases, `payload_schema_version` 2, ten declared files, six chain fixtures, prose half edit-detectable not semantics-provable. S2's report was still absent. Historical hazard paragraphs remain in place and are marked superseded; a reader who stops at the Round-96 section still sees the old surface.

## 3. What did not grow

- Freeze **chain length**. Still six fixtures. r99 is `UNPINNED-FIXTURE` exit 2. This is the coverage class r98 improved (four → six). It did not move.
- Semantic inventory. A prose edit that leaves `depends_on` alone is `DIGEST-MISMATCH`, not `REDUCTION-DETECTED`. BR-01's JSON-edge half was already closed. The prose half is now edit-detectable, not semantics-provable.
- `check_bible` / `support_check` / `map_obligations` detection classes. They cover the new fixture's 21 obligations. Emptied `depends_on`, wrong-but-earlier edge, and a coherently regenerated deletion stay green on those gates (section 2.3).
- Files outside the declared ten.
- Producer reports for S2 and S5, as of 23:10:32.

## 4. Cross-cutting seats read

Read after their files existed. Several expired before S1's report (22:48), the doc edit (22:51), and the table (22:57). Their ABSENT is about their gate, not a contradiction of bytes that landed later.

- **V69 crosscheck-coverage-2** (23:07): `PASS — COVERAGE unchanged (not harmed)` on `fb9bb9ff…` / `8c2561b0…`; chain 6/6; ten-file pin called C1, not a new coverage class; V30 comparison ABSENT because this file did not exist yet. I agree on chain extent and on "not harmed." I do not hide the pin-width growth; I label it C1, which is what the declaration does.
- **V29 verdict-depth** and **V51 crosscheck-depth**: component 1 measured (6/1/7→6/1/8, 21 obligations, census 172→173); component 2 ABSENT at their write. V51 bottom line INCONCLUSIVE. The table has since landed; their component-2 absence is stale. My section 2.3 is the later measurement.
- **V32 / V91 freshness, V33 / V27 adjacency, V26 / V82 operability, V24 / V65 / V88 freshness, V87 scope-final, V52 calibration crosscheck, V06 refreeze, V18 / V17 / V44 / V59 / V60 / V98 / V122 / V64 / V103 table seats:** ABSENT. Their gates required S1/S2/S5 reports and/or the knowledge files. Correct at their expire times. Not a coverage measurement.
- **V94 c1-two-mutation:** PASS on tool `6f81f8be…` (pre string-edit). Simultaneous JSON+Markdown edit names both files. I did not re-run that pair on `fb9bb9ff…`.
- **V01 payload:** PASS, six pins, ten files, schema 2. Agrees with section 2.1.
- **V02 markdown-tamper:** PASS, five Markdown and five JSON one-word/inventory-clean edits each named. Agrees with the class in section 2.1.
- **V03 before-after:** FAIL on the declaration's "invisible to every gate" for an anchor-bearing sentence (`support_check` exit 1 J14); freeze before/after holds. Agrees with the table's row 6 and with S1.
- **V40 / V70 census:** PASS 172→173. Agrees with my directory count.
- **V25 doc-parity:** PASS as a pre-integration inventory; Round-99 section absent at 22:39. Stale relative to README `837a7f5d…`.
- **V102 doc-commands:** ABSENT, no Round-99 commands at 22:15. Stale. The command they would have run now exists and passed when I ran it (section 2.4).
- **V35 shonen-format:** PASS, four `[~]`, zero `[x]`. **V73 shonen-2** (rewritten 23:06, after the SKILL edit): I read an earlier tail that FAILed a 17-case registry row. I did not re-read the 23:06 rewrite. Current SKILL row (section 2.4) says 18 cases and ten files. I do not carry V73's earlier mismatch as a current coverage hole.
- **V68 adjacency-2:** PASS, sibling HEADs predate the wave. Not a corpus-coverage result.
- **V39 receipt:** presence audit; S1/S2/S5 absent at their snapshot. S1 has since landed.
- **V16 c2-dependency-probe:** FAIL tail is the missing-key / unknown-id / inversion class, which the table's row 9 says `check_bible` catches. Not a contradiction of row 1 (empty list stays CLEAN). I did not re-read V16's full FAIL reason.
- **S1** report read in full. Measurements agree, including the anchored-sentence contradiction. **S3** and **S4** reports read. Fixture and map measurements agree. **S2 / S5** reports absent.

## 5. COVERAGE verdict

**COVERAGE: unchanged (not harmed) on chain extent; the surfaces that grew are pin width, one unpinned fixture, and a cited blind-spot record.**

Chain coverage — the class this lane has been scoring as coverage since r96 — did not grow and was not harmed. Six fixtures still verify clean. Semantic inventories of those pins match the r98 JSON digests. r99 is outside the pin set, which is what the declaration asked for (6/6, not 7/7).

What actually grew, measured on the bytes in section 0:

1. The freeze gate's watched bytes, 5 JSON tables → 10 declared files, schema 2, self-test 17→18. A non-anchor Markdown edit that was `RESULT PASS` on the r98 tool is exit 2 `DIGEST-MISMATCH` naming the file. That is C1/calibration. It is not a longer chain and it is not a semantic proof.
2. Corpus extent: one new fixture directory (census 172→173), 6/1/8, map 21/21, `support_check` 21/21, `check_bible` CLEAN. Existing gates, new object. Not freeze-covered.
3. Decision-record extent: one table, rows 1–9, replayed here against S5's scratch trees on the delivered tool. The blinds in rows 1–3, 5, 7, and 8 are written down. They are not closed. The "two seats" replay claim is unmet in the reports I read.

Docs caught up after the poll (README addendum at line 290, SKILL freeze row). S2 and S5 reports had not landed at 23:10:32.

## 6. Bottom line

**PASS (bounded)** — chain coverage unchanged and not harmed (6/6 clean on tool `fb9bb9ff…` / contract `8c2561b0…`; r99 `UNPINNED-FIXTURE` exit 2); watched-byte surface grew 5→10 and a non-anchor prose edit is now named `DIGEST-MISMATCH`; fixture census 172→173 with map 21/21; blind-spot table `4670c0b7…` landed and the rows I replayed match, without closing those blinds; S2 and S5 reports absent at 23:10:32.
