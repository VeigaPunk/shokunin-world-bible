# V72 — spec-conformance-2 (round 99)

- **Seat:** V72 spec-conformance-2. Lane `/home/vgpnk/Projects/shokunin/lore-shokunin`. Commands from that root with `python3` unless a scratch mirror root is named. No commits, no network, no corpus writes.
- **Declaration mapped:** `LOG.md` Round 99 declaration (standing; the blocked-dispatch entry does not replace it). Baseline `4265df5`. HEAD at measurement `337f0fa52b02626b7687eedbb2d99fab30446fe4` (ancestor of `4265df5`; no seat commit).
- **Grouping (not V37's):** measurement class, not declaration order. V37's report was absent at the last check (`ls …/seats/V37*.md` → no such file, 23:11). Classes below: payload identity, negative detection, positive receipts, structural delta, prose bound, table replay, doc sentences. Producer reports were read after these runs and are cross-checks, not evidence.
- **Delivered hashes (this seat, after the last tool edit `22:38` and the table write `22:57`):** `dependency_freeze.py` `fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c`; contract `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628`; `check_bible.py` `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`; table `4670c0b71668c56c53c0bac90091531d3f0e881c7dcb2ac572d09f96ae22182e`. Baseline tool extracted to scratch: `03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b` (matches the table's cited r98 tool).
- **Poll:** content-gated, 20 s cadence, under the 40-try cap. S3 report `22:01`, S4 `22:03`, S1 `22:48`, knowledge files `22:57`, S2 and S5 reports `23:10`. No stall-escape. This poll was the five producers plus declared artifacts, not an all-reports poll, so SELF subtraction does not change the set. Nothing below was scored against a plan.

Scratch: `.ufo/waves/round-99/seats/V72-scratch/` (`probe.py`, `probe-out.txt`, `replay_table.py`, `replay-out.txt`, `poll.log`).

## 1. Payload identity

Declaration: each chain pin covers all ten files; payload schema versioned.

Observed contract: root `schema_version` 1→2 and `payload_schema_version` 2. Six pins (`r88-m3-maya-cluster`, `r94-paired-crossing`, `r95-crossing-aftermath`, `r96-crossing-response`, `r97-crossing-acknowledgment`, `r98-clerk-filing`), each `payload_schema_version` 2, `pinned_files` exactly

`entities.json`, `relations.json`, `timeline.json`, `sources.json`, `contradictions.json`, `README.md`, `claim-excerpt-map.md`, `fictional-excerpts.md`, `inspiration-note.md`, `source-excerpt.md`

and `files` those ten sha256s, no missing, no extra. Revision on every pin `337f0fa52b02626b7687eedbb2d99fab30446fe4`.

Against `git show 4265df5:corpus/tools/dependency-freeze-contract.json`: the five JSON file digests, `events`, and `relations` are unchanged on all six pins. Content digests moved (r98 `59a0f4fa3d4a47e0…` → `5ecf84e19121ea12…`) because Markdown entered the payload. `r99-window-lapse` is not pinned. `symbolism-clause-map.md` exists under r88 and is not in that pin's `files`.

## 2. Negative detection

Declaration: any pinned-file edit → exit 2 `DIGEST-MISMATCH` naming the file; prose-wording removal was invisible to every gate before and named after.

**Ten semantic-neutral edits**, scratch mirror of the delivered tool+contract plus `r98-clerk-filing`, one file changed at a time, then `python3 corpus/tools/dependency_freeze.py corpus/fixtures/r98-clerk-filing`. All ten exited 2 `DIGEST-MISMATCH` and the finding named that file only. Representative (README newline append):

```
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
FINDING DIGEST-MISMATCH: content digest 3322eda76a6885f76f251bb35651ada8dce3f853f344d653c43acf6843416f70 != pin 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0; changed: README.md (sha256 32efc78f70e6de4f9670134080711923199e8693015d3ebea75a4a1ca6362926 -> d2a1d6596c8e875bd54fd17d6695d7e90945867a724bc116daada2f653c48ffa); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
```

exit 2. Same shape for `contradictions.json`, `entities.json`, `relations.json`, `sources.json`, `timeline.json`, `claim-excerpt-map.md`, `fictional-excerpts.md`, `inspiration-note.md`, `source-excerpt.md` (full lines in `probe-out.txt`).

**The literal "any edit" does not hold.** Inventory-modeled edits exit 1 with the semantic finding first (row 1 below: emptied `depends_on` → `REDUCTION-DETECTED` exit 1, not `DIGEST-MISMATCH`). The self-test's `malformed_json` exits 2 `MALFORMED-JSON`, not `DIGEST-MISMATCH`. That matches the delivered contract `precedence` ("semantic inventory findings decide first") and contradicts a universal reading of the declaration sentence and of `SKILL.md` "any pinned-file edit exits 2". The prose-detectability claim is the one that holds.

**Before / after, coherent dependency-wording removal** (the class the table identifies as the real blind spot). On a path-bound r98 copy, replace `depends on both ninth-bell entries` with `follows both ninth-bell entries` in both `fictional-excerpts.md` and the J14 anchor.

Before, `git show 4265df5` tool+contract in the mirror:

```
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
DIGEST 59a0f4fa3d4a47e03649a54d1815c45ee1eef641b63a59ebe7210bc9d9b9b133
RESULT PASS
```

exit 0. That digest is the pre-C1 JSON-only pin. Same copy: `check_bible` CLEAN exit 0; `support_check` `SOURCE-SUPPORT 20/20` / `RESULT PASS` exit 0; `map_obligations` `OBLIGATIONS raw=20 mapped=20` / `RESULT PASS` exit 0. Invisible to those four fixture gates.

After, delivered tool+contract, same edit:

```
FINDING DIGEST-MISMATCH: content digest 1f73326f38eb20f75d6c2541df5ec67ae20e157e5b4c1053dc10464ae88d67f2 != pin 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0; changed: claim-excerpt-map.md …, fictional-excerpts.md …; pinned-file bytes changed outside the semantic inventory
RESULT ERROR
```

exit 2. Names both files. Lexical gates on that copy stay exit 0. The finding is a byte mismatch, not a proof the dependency sentence is gone or still true.

**The declaration's "every gate" does not hold for excerpt-only removal of that sentence.** Same replacement in `fictional-excerpts.md` only, map anchor left in place, r99 copy: `check_bible` CLEAN exit 0; `map_obligations` PASS exit 0; `support_check` exit 1 `FAIL J14: source-support anchor missing` / `RESULT FAIL`. An earlier r98-copy probe of the same class against the `4265df5` freeze tool was exit 0 `DIGEST 59a0f4fa…` while `support_check` already failed J14. README-only replacement of one `depends on` was invisible to freeze, `check_bible`, `support_check`, and `map_obligations` before, and after is exit 2 naming `README.md`.

`boundary_doc_check` and `discriminate_check` do not take a fixture directory; they are not fixture-prose gates.

**Unpinned file stays invisible.** Append `V72-symbolism-marker` to a mirror copy of `corpus/fixtures/r88-m3-maya-cluster/symbolism-clause-map.md`, delivered tool:

```
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0
DIGEST acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae
RESULT PASS
```

exit 0.

## 3. Positive receipts

Declaration: chain re-frozen through the guarded `--freeze`, 6/6 clean; self-test 17→18.

```
python3 corpus/tools/dependency_freeze.py --self-test
```

18 `CASE … ok` lines, last `CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok`, then `SELF-TEST 18/18` / `RESULT PASS`, exit 0. Re-run after the final tool hash `fb9bb9ff…`. Against `4265df5` expectations: 17 inherited objects identical, added only `markdown_tamper`, removed none.

Live verify, each exit 0 `RESULT PASS`:

| fixture | digest |
|---|---|
| r88-m3-maya-cluster | `acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae` |
| r94-paired-crossing | `048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef` |
| r95-crossing-aftermath | `97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710` |
| r96-crossing-response | `43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c` |
| r97-crossing-acknowledgment | `a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54` |
| r98-clerk-filing | `5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0` |

Scratch reproducibility: copy delivered tool+contract+six fixtures, delete all pins, `--freeze` each. All six exit 0 and the rewritten pin objects compare equal to the delivered pins (`pin_equal True` × 6). Digests match the table above.

Scope guard, live tool, target under this seat's scratch (not `corpus/fixtures/**`):

```
FINDING SCOPE-REFUSED: --freeze refuses …/V72-scratch/not-a-fixture …; the frozen scope is corpus/fixtures/** (integration-time operation only)
RESULT ERROR
```

exit 2. Contract sha256 unchanged (`8c2561b0…`).

`python3 corpus/tools/dependency_freeze.py corpus/fixtures/r99-window-lapse` → `FINDING UNPINNED-FIXTURE: no pin for 'r99-window-lapse'` / `RESULT ERROR`, exit 2. The declaration's 6/6 is the existing chain, not r99.

## 4. Structural delta (lapse fixture)

Declaration: preserving copy of r98 plus `clerk-lapse-note` and tick-15 `clerk-lapse-recorded` (`clerk-maren`, `chalk-stair`, `depends_on: ["clerk-filing-open"]`); window closed per the original minute, agreement unfulfilled, no claim lodged, matter stays open; no resolution, blame, or reconciliation asserted; 6/1/7→6/1/8, sources 7→8, 21 obligations (20 inherited + 1 event), `check_bible` CLEAN, inherited rows parsed-value identical, census 172→173.

Parsed counts: entities 6, relations 1, timeline 8, sources 8, contradictions `[]`. r98 is 6/1/7 and 7 sources. `entities.json`, `relations.json`, `contradictions.json` parsed-equal to r98 and to `4265df5` r98, and byte-identical to that blob (`1793`, `139`, `3`). `sources.json[:-1]` and `timeline.json[:-1]` parsed-equal to r98. `inspiration-note.md` and `source-excerpt.md` byte-identical (`1956`, `640`). `fictional-excerpts.md` startswith the r98 bytes (`4187`) then `\n## Round 99 lapse n` (now `5114`).

New source `sources.json` last object: id `clerk-lapse-note`, title `Maren's Chalk Stair Lapse Note`. New event:

```
id clerk-lapse-recorded, tick 15, entity_id clerk-maren, place_id chalk-stair,
depends_on ["clerk-filing-open"], source_id clerk-lapse-note
description: At the Chalk Stair at tick 15, the clerk records that the crossing-window named in the original minute has closed; the agreement was unfulfilled; no claim was lodged; the matter stands as a historical open entry.
```

No new entity. `clerk-maren` remains `entities.json#/5`, `first_appearance` `clerk-filing-note`.

Gates on the live fixture:

```
python3 corpus/fixtures/check_bible.py corpus/fixtures/r99-window-lapse
CLEAN: schema, citations, relations, timeline; 0 violations
```

exit 0.

```
python3 corpus/tools/map_obligations.py corpus/fixtures/r99-window-lapse
OBLIGATIONS raw=21 mapped=21
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23
RESULT PASS
```

exit 0.

```
python3 corpus/tools/support_check.py corpus/fixtures/r99-window-lapse
SOURCE-SUPPORT 21/21; EDITORIAL-ANCHORS 2/2; … MODES 23/23; VALIDATED-ROWS 23/23
RESULT PASS
```

exit 0. Includes `PASS J21` at excerpt line 70.

Map rows: r98 `J01`–`J20`, r99 those plus `J21`. Inherited rows identical after swapping the namespace column `r98-clerk-filing` / `r99-window-lapse` (`changed_inherited 0`). New row only `J21`, pointer `timeline.json#/7`, span 66-76, anchor the tick-15 sentence. Map line 5 states `21 JSON facts; 2 editorial rows; 23 total mapped rows; 19 distinct excerpt anchors.`

Census, full `check_bible` sweep of `corpus/fixtures/*/`: dirs `173`, clean `39`, negative `134`, other `0`, `VIOLATION:` lines `421`. r98 closure recorded `172/38/134/421`. Delta is +1 directory and +1 clean.

## 5. Prose bound

The new beat's resolution/blame/reconciliation wording is negation, not a positive assertion.

- Excerpt line 74: `I record no resolution, assign no blame, and reconcile nothing.`
- Scope line 76: asserts no resolution, no blame, and no reconciliation; matter stays open.
- Source reliability note: `It asserts no resolution, no blame, and no reconciliation`.
- Event description does not contain those words. It records the closed window, the unfulfilled agreement, no claim lodged, and a historical open entry.
- README line 11: window closed per the original minute's terms; matter stays open; asserts no resolution, no blame, and no reconciliation; closes no one; assigns blame to neither.

Inherited beats also use those words only as denials. This seat did not treat a clean gate run as testimony, entailment, or canon.

## 6. Table replay

Declaration: one cited table, one row per r94–r98 blind spot (emptied `depends_on`; wrong-but-earlier edge; deleted terminal row; F15 support_check-silent mutants; dependency-wording removal, historical invisibility and the C1 close; consistent-regeneration bound; checker frozen-pin status), each with mutation class, gates that catch, gates that do not, and a command replayed on this revision.

`corpus/knowledge/r99-gate-blind-spot-table.md` has rows 1, 1b, 2, 3, 4, 5, 6, 7, 8, 9. Row 4 records that the F15 span-break is **not** support_check-silent; row 5 is the silent class. That split is more precise than the declaration's "F15 support_check-silent mutants" phrase, and the measurements support the split.

Independent replays on fresh copies under `V72-scratch/table-replay/` (not S5's trees). Freeze side is a path-bound r98 mirror. Lexical side is an r99 copy where the table uses the r99 twin.

| row | this seat | matches table quote |
|---|---|---|
| 1 emptied `depends_on` | freeze exit 1 `REDUCTION-DETECTED: event clerk-filing-open lost depends_on ['acknowledgment-aru-records']` (`events 7/7; dependency-edges 5/6`); `check_bible` CLEAN 0. r99 twin: bible/support/map all exit 0 (`raw=21 mapped=21`) | yes |
| 1b drop `evin-ninth-bell` | exit 1 `paired-crossing-decision lost depends_on ['evin-ninth-bell']`; bible CLEAN 0 | yes |
| 2 wrong-but-earlier | exit 1 `ADDITION-DETECTED` gained `response-evin-salt-court` and `REDUCTION-DETECTED` lost `acknowledgment-aru-records`; bible CLEAN 0. r99 twin lexical gates exit 0 | yes |
| 3 deleted terminal | r99, map kept: bible CLEAN 0, support PASS 0, map exit 1 `phantom_obligation: timeline.json#/7 is not a raw source-attributed obligation` (`raw=20 mapped=21`). r98 pin: exit 1 `event clerk-filing-open is missing; 1 frozen dependency edge(s) gone`; bible CLEAN 0 | yes |
| 4 span 17→20 | r99 support exit 1 `anchor hit outside declared line span 20 (hit lines: 17)`; bible 0; map 0. r98 pin exit 2 digest `09858d77de0ecc37…` naming `claim-excerpt-map.md` | yes, including that digest |
| 5 source-id rebound | r99 map exit 1 `source_id_mismatch: timeline.json#/7 does not bind to 'clerk-filing-note'`; bible 0; support PASS 0. r98 pin exit 2 naming `timeline.json`; map exit 1 `timeline.json#/6 does not bind to 'aru-acknowledgment-note'`; support PASS 0 | yes |
| 6 prose | before exit 0 digest `59a0f4fa…`; after exit 2 digest `1f73326f…` naming map and excerpt; lexical gates on the coherent edit exit 0. Narrative-only map sentence: freeze exit 2 naming the map, lexical gates 0. Excerpt-only: support exit 1 J14 | yes, including both digests |
| 7 consistent regen | delete `clerk-filing-open`, delete J20, restate inventory `19/2/21/17`: bible CLEAN 0, support `SOURCE-SUPPORT 19/19` PASS 0, map `raw=19 mapped=19` PASS 0, freeze exit 1 `clerk-filing-open is missing` | yes |
| 8 checker pin | live checker sha256 equals `boundary-doc-contract.json` `checker.sha256` `ff9fd2aa…`. `python3 corpus/tools/boundary_doc_check.py` → `CERTIFIED` exit 0. One extra comment on a scratch checker → `FINDING checker_drift` / `CERTIFICATION FAIL` exit 1 | yes |
| 9 classes the checker does catch | all exit 1 on r99 copies: unknown event, dangling entity, unknown source, missing `depends_on` key (`required nonempty list`), self-dependency plus inversion, repeated dependency, tick-14 inversion, deleted predecessor → `unknown event 'clerk-filing-open'` | yes |

Row 6's own text records the declaration overclaim: "invisible to every gate" was true of the coherent excerpt+anchor edit, and false of excerpt-only J14 removal. This seat's runs agree. The freeze close is edit detection, not a semantic proof.

The declaration line "every row replay-verified by at least two seats" is a process claim about other seats. This seat replayed every row. A filename search found the emptied-edge finding string in other reports (`V30`, `V31`, `V50`, `V55`, `V69`, `V78`, `S5`); that is not an audit of their method, so the two-seat clause is not closed here.

`corpus/knowledge/r99-lapse-scope-note.md` citations checked against the live fixture: `sources.json:45/46/48`, excerpt lines 70-74, `timeline.json:77/84`, `entities.json:63/66/69`, map lines 5/42/69, README lines 3/11/21 match the note's claims. README line 15 does say the lapse note does not re-present the clerk's first appearance. The note's "does not add a claim" is a paraphrase of that line, not a second sentence; the JSON has no new claim. r94 excerpt line 19 is the "for this crossing only" sentence the note cites.

## 7. Doc sentences

`corpus/tools/README.md` Round-99 addendum and `SKILL.md` dependency_freeze row (S2, mtimes `23:08` and `22:51`) state schema 2, ten files, chain 6/6, self-test 18/18, guarded `--freeze`, and the prose-half close as edit detection. Those match sections 1–3. The README's later paragraph (after `23:08`) records that the r95 excerpt `depends on` removal is not invisible to `support_check` (exit 1 J14) while the r98 freeze stayed green. This seat reproduced that split on r98/r99, not S2's r95 scratch path. Both docs still contain "any edit / any pinned-file edit exits 2 `DIGEST-MISMATCH`" beside "semantic inventory findings still decide first." The second sentence is the one the tool implements.

S1's report agrees on chain digests, 18/18, and the J14 exception. S3's report is stale on README/map (it correctly said those files were still r98 copies at S3's write); S4 rewrote them. Delivered map is not the r98 placeholder (`changed_inherited 0` plus J21, gates 21/21).

Tracked diff vs `4265df5` at the last check: `LOG.md`, `SCORECARD.md`, `corpus/tools/dependency_freeze.py`, `dependency-freeze-contract.json`, `corpus/tools/README.md`, `SKILL.md`, plus untracked `corpus/fixtures/r99-window-lapse/` and `corpus/knowledge/r99-*.md` and `.ufo/waves/round-99/`. No other tool was in that diff. This seat did not re-run `map_obligations.py --self-test` or `discriminate_check.py`.

## Bounds

- Not whole-claim entailment, chronology truth, rights, or canon. CLEAN and freeze receipts are structural or digest checks.
- "Any edit" and "every gate" in the declaration are false as universals. Non-inventory edits of all ten pinned files are named `DIGEST-MISMATCH`. Inventory edits stay exit 1. Excerpt-only J14 removal was already a `support_check` fail. The delivered table states that bound.
- `r99-window-lapse` is unpinned. Freeze catches rows 1–3 and 7 only on the six pinned fixtures.
- Two-seat replay clause not audited here.
- S2's exact r95 before/after stdout was not re-run; the same mutation class was.

## Bottom line

**PASS** — C1 and both C2 components reproduce on the delivered revision under this seat's runs: ten-file schema-2 pins, scratch `--freeze` pin-equal 6/6, self-test 18/18, semantic-neutral edits of all ten files exit 2 `DIGEST-MISMATCH` naming the file, coherent prose removal invisible before (digest `59a0f4fa…`) and named after (digest `1f73326f…`); lapse fixture 6/1/8 with inherited prefixes equal, 21/21 obligations, `check_bible` CLEAN, census 173/39/134/421; every blind-spot table row replayed with the table's findings — the declaration's "every gate" and "any edit" universals narrowed, not hidden, by those same measurements.
