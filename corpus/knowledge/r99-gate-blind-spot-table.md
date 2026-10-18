source: `corpus/fixtures/r99-window-lapse/{timeline.json,sources.json,claim-excerpt-map.md,fictional-excerpts.md}`; `corpus/fixtures/r98-clerk-filing/` (pinned chain member used for path-bound freeze replays); `corpus/tools/dependency_freeze.py`; `corpus/tools/dependency-freeze-contract.json`; `corpus/tools/support_check.py`; `corpus/tools/map_obligations.py`; `corpus/fixtures/check_bible.py`; `corpus/tools/boundary_doc_check.py`; `corpus/tools/boundary-doc-contract.json`; `corpus/tools/README.md` (Round-96 `map_obligations` addendum); `.ufo/waves/round-98/seats/V16-c3-dependency-probe.md`; `.ufo/waves/round-98/seats/V47-support-regression.md`; `.ufo/waves/round-98/seats/V33-debt.md`; `.ufo/waves/round-97/seats/V37-debt.md`; `.ufo/waves/round-94/followup/F15-mutation-replays.md`; `LOG.md` (Round 99 declaration, C1 prose half)
verified-at: 2026-10-17 — every command below was run from the lane root `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3` on scratch copies. Live corpus fixtures were not mutated. Freeze quotes that name `DIGEST-MISMATCH` or `REDUCTION-DETECTED` were re-run after `dependency_freeze.py` held at sha256 `fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c` and the contract held at `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628`. Cited debt paths were read this pass. No external URL was fetched.
recheck: before citing any row as current gate behavior, and whenever `dependency_freeze.py`, `dependency-freeze-contract.json`, `check_bible.py`, `support_check.py`, `map_obligations.py`, or `boundary-doc-contract.json` changes. A checker edit that closes a row in-checker is not closed until `boundary-doc-contract.json` `checker.sha256` is re-pinned (row 8).

# Gate blind-spot decision table — round 99

This is a measured decision record, not a canon finding and not a claim that any gate reads testimony. Each row is one demonstrated blind spot from r94–r98, replayed on this revision. "Catches" means the gate exits non-zero and names the mutation. "Does not" means the gate stays green (exit 0) on that mutant. Scratch mirrors used a copy of the delivered tool and the delivered contract so `--freeze` path-binding resolved inside the mirror; the live pin digest for `r98-clerk-filing` is `5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0`.

`r99-window-lapse` is not in the pin set. `python3 corpus/tools/dependency_freeze.py corpus/fixtures/r99-window-lapse` exits 2 `UNPINNED-FIXTURE`. A freeze result on a renamed scratch directory is the same name-lookup miss, not a semantic evaluation of the mutant. Semantic freeze catches below are on path-bound copies of the pinned fixture `r98-clerk-filing`.

Delivered chain, this pass: r88, r94, r95, r96, r97, r98 each `RESULT PASS` exit 0 (6/6). `python3 corpus/tools/dependency_freeze.py --self-test` → `SELF-TEST 18/18` / `RESULT PASS` exit 0, including `CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok`.

Control on the live r99 fixture: `check_bible` `CLEAN: schema, citations, relations, timeline; 0 violations` exit 0; `support_check` `INVENTORY JSON-FACTS 21/21` / `SOURCE-SUPPORT 21/21` / `RESULT PASS` exit 0; `map_obligations` `OBLIGATIONS raw=21 mapped=21` / `RESULT PASS` exit 0.

| # | Mutation class | Catches (exit) | Does not | Debt |
|---|---|---|---|---|
| 1 | emptied `depends_on` | `dependency_freeze` `REDUCTION-DETECTED` exit 1 | `check_bible` CLEAN 0; `support_check` PASS 0; `map_obligations` PASS 0 | V16 P5; r97 NB-15; r98 NB-05 |
| 1b | non-empty edge reduction (drop one of two predecessors) | `dependency_freeze` `REDUCTION-DETECTED` exit 1 | `check_bible` CLEAN 0 | r94 F15-a; BR-01 JSON half |
| 2 | wrong-but-earlier dependency edge | `dependency_freeze` `REDUCTION-DETECTED` + `ADDITION-DETECTED` exit 1 | `check_bible` CLEAN 0; `support_check` PASS 0; `map_obligations` PASS 0 | V16 P8 |
| 3 | deleted terminal event row | `dependency_freeze` `REDUCTION-DETECTED` exit 1; `map_obligations` `phantom_obligation` exit 1 if the map row is kept | `check_bible` CLEAN 0; `support_check` PASS 0 if the map row is kept | V16 P9 |
| 4 | F15 span-break (declared span moved off the anchor line) | `support_check` FAIL exit 1; `dependency_freeze` `DIGEST-MISMATCH` exit 2 (pinned-file edit, not a span finding) | `check_bible` CLEAN 0; `map_obligations` PASS 0 | r94 F15-c. Not support_check-silent — measured |
| 5 | F15 source-id mutant (mapped event rebound to another declared source) | `map_obligations` `source_id_mismatch` exit 1; `dependency_freeze` `DIGEST-MISMATCH` exit 2 (digest only; source_id is outside the semantic inventory) | `check_bible` CLEAN 0; `support_check` PASS 0 | r94 F15-d; r98 V47 |
| 6 | dependency-wording removal from prose | delivered pin: `DIGEST-MISMATCH` exit 2 naming the file. Baseline r98 tool (`4265df5`, sha256 `03d04365…`): same edit `RESULT PASS` exit 0 | lexical gates stay green when the removed wording is not an unmatched anchor (narrative-only, or excerpt+anchor updated together). Excerpt-only removal of the J14 anchor is not invisible: `support_check` FAIL exit 1 | BR-01 prose half; `LOG.md` Round 99 C1. Edit-detectable, not semantics-provable |
| 7 | consistent-regeneration inventory bound | `dependency_freeze` `REDUCTION-DETECTED` exit 1 on the JSON deletion half | `check_bible` CLEAN 0; `support_check` PASS 0; `map_obligations` PASS 0 when the map row and the `**Expected inventory:**` line are restated to match | `corpus/tools/README.md` Round-96 addendum; r97 NB-09 |
| 8 | checker byte-frozen | `boundary_doc_check` `checker_drift` exit 1 on any delivered-checker byte change | blind spots in rows 1–3 cannot be closed inside `check_bible.py` without re-pinning `corpus/tools/boundary-doc-contract.json` `checker.sha256` (`ff9fd2aa…`). The live checker matches that pin; the default run is `CERTIFIED` exit 0 | boundary contract; LOG closure pin reproductions |
| 9 | classes `check_bible` does catch (unknown id / dangling) | `check_bible` exit 1: unknown event, dangling entity, unknown source, missing `depends_on` key, self dependency, repeated dependency, timeline inversion, deleted non-terminal predecessor | not a blind spot. Empty list, wrong-but-earlier edge, and deleted terminal row are rows 1–3 | `check_bible.py:80`, `:113`, `:375`, `:409`; V16 P1–P4, P6–P7 |

## Row 1 — emptied `depends_on`

Mutation: on a path-bound copy of `r98-clerk-filing`, set `clerk-filing-open.depends_on` to `[]`. The same empty-list mutation on `r99-window-lapse` `clerk-lapse-recorded` is the r99 structural twin; `check_bible` / `support_check` / `map_obligations` were run on that twin.

```
python3 corpus/fixtures/check_bible.py .ufo/waves/round-99/seats/S5-scratch/work/m1-empty-deps
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
python3 corpus/tools/support_check.py .ufo/waves/round-99/seats/S5-scratch/work/m1-empty-deps
RESULT PASS
exit=0
python3 corpus/tools/map_obligations.py .ufo/waves/round-99/seats/S5-scratch/work/m1-empty-deps
OBLIGATIONS raw=21 mapped=21
RESULT PASS
exit=0
```

Delivered pin, mirror `work3/empty` (tool `fb9bb9ff…`, contract `8c2561b0…`):

```
FREEZE r98-clerk-filing: events 7/7; dependency-edges 5/6; relations 1/1
FINDING REDUCTION-DETECTED: event clerk-filing-open lost depends_on ['acknowledgment-aru-records']
RESULT FAIL
exit=1
```

`check_bible` on that same r98 mirror: `CLEAN` exit 0. The checker requires the key and a list (`check_bible.py:80` prints `required nonempty list` only when the key is missing or not a list). An empty list is a list, so it stays CLEAN.

## Row 1b — non-empty edge reduction

Mutation: `paired-crossing-decision.depends_on` reduced from `["aru-ninth-bell", "evin-ninth-bell"]` to `["aru-ninth-bell"]` on a path-bound r98 copy (the r94 F15-a / BR-01 JSON-edge bytes, still present in the continuation).

```
FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']
RESULT FAIL
exit=1
```

`check_bible` on that copy: `CLEAN` exit 0. This is the class r96's freeze closed for pinned fixtures. It is not closed for an unpinned fixture.

## Row 2 — wrong-but-earlier edge

Mutation: `clerk-filing-open.depends_on` set to `["response-evin-salt-court"]` (tick 12, earlier than tick 14, not the declared predecessor `acknowledgment-aru-records`). r99 twin: `clerk-lapse-recorded.depends_on` set to `["acknowledgment-aru-records"]` (tick 13, not `clerk-filing-open`).

r99 twin: `check_bible` CLEAN exit 0; `support_check` `RESULT PASS` exit 0; `map_obligations` `OBLIGATIONS raw=21 mapped=21` / `RESULT PASS` exit 0.

Pinned r98 copy:

```
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
FINDING ADDITION-DETECTED: event clerk-filing-open gained depends_on ['response-evin-salt-court']
FINDING REDUCTION-DETECTED: event clerk-filing-open lost depends_on ['acknowledgment-aru-records']
RESULT FAIL
exit=1
```

`check_bible` on that copy: `CLEAN` exit 0. Strict tick order is satisfied; the checker does not require the semantically declared predecessor.

## Row 3 — deleted terminal event row

Mutation: delete `clerk-lapse-recorded` from the r99 timeline and leave the map row. Pinned twin: delete `clerk-filing-open` from an r98 copy (nothing depends on it).

r99, map row kept:

```
python3 corpus/fixtures/check_bible.py .ufo/waves/round-99/seats/S5-scratch/work/m3-delete-terminal
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
python3 corpus/tools/support_check.py …/m3-delete-terminal
RESULT PASS
exit=0
python3 corpus/tools/map_obligations.py …/m3-delete-terminal
OBLIGATIONS raw=20 mapped=21
FINDING phantom_obligation: timeline.json#/7 is not a raw source-attributed obligation
RESULT FAIL
exit=1
```

Pinned r98 copy:

```
FREEZE r98-clerk-filing: events 6/7; dependency-edges 5/6; relations 1/1
FINDING REDUCTION-DETECTED: event clerk-filing-open is missing; 1 frozen dependency edge(s) gone
RESULT FAIL
exit=1
```

`check_bible` on that copy: `CLEAN` exit 0. Deleting a non-terminal predecessor is a different class (row 9): the remaining edge becomes an unknown event and exits 1.

## Row 4 — F15 span-break

Mutation: J05 declared span `17` → `20`, anchor text unchanged. On r99 (`work/m4-span-break`): `check_bible` CLEAN exit 0; `map_obligations` `RESULT PASS` exit 0; `support_check` exit 1:

```
FAIL J05: source-support; mode=verbatim; anchor=found; 17:> The Chalk Stair is the named rain-dark crossing between Quiet Rise and Salt Court.; span=20; outside-span=17
FAIL: J05: anchor hit outside declared line span 20 (hit lines: 17)
RESULT FAIL
exit=1
```

The same span-cell edit on a path-bound r98 copy, delivered pin (`work4/span`):

```
FINDING DIGEST-MISMATCH: content digest 09858d77de0ecc37b4f7f5cf2c4e4772f01649fc441b9ad1618f69d0e7434a41 != pin 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0; changed: claim-excerpt-map.md (sha256 c1099d0ee9eece241ea1f796320a84453dfc6b6aec33b7b9dd7e39bbef4a94ba -> f5d2c13674cfc5b564efad86140d3e31b05ff99f98f7a20af7d635cdd0e320e6); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
exit=2
```

Span-break is not support_check-silent. The r94 F15 record already had `support_check` FAIL exit 1 for this mutant. What stayed silent, and still stays silent, is row 5.

## Row 5 — F15 source-id mutant

Mutation: r99 `clerk-lapse-recorded.source_id` `clerk-lapse-note` → `clerk-filing-note` (both ids exist). `check_bible` CLEAN exit 0; `support_check` `SOURCE-SUPPORT 21/21` / `RESULT PASS` exit 0; `map_obligations` exit 1:

```
FINDING source_id_mismatch: timeline.json#/7 does not bind to 'clerk-filing-note'
RESULT FAIL
exit=1
```

Pinned r98 twin (`clerk-filing-open.source_id` → `aru-acknowledgment-note`, `work4/srcid`): `map_obligations` `FINDING source_id_mismatch: timeline.json#/6 does not bind to 'aru-acknowledgment-note'` / `RESULT FAIL` exit 1. Freeze does not emit a semantic source-id finding. It exits 2 because the JSON bytes changed:

```
FINDING DIGEST-MISMATCH: … changed: timeline.json (sha256 eb24e0848e597efa29ed858cb8557d8f3126a47e1231f9469d719257e191e7af -> 17e9230e58ad9f9c436c4f1a7be51291239465259898d7a76c6232b25b0e996d); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
exit=2
```

`support_check` never reads raw `source_id`. That silence is the F15-d class. `map_obligations` closes the binding; the full-file pin closes the byte edit. Neither proves the excerpt entails the id.

## Row 6 — dependency-wording removal from prose

Two edits, both measured. C1 detects the edit. It does not prove the dependency sentence is still true.

**Historically invisible (baseline tool).** `git show 4265df5:corpus/tools/dependency_freeze.py` (sha256 `03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b`) plus the r98-closure contract, on a path-bound r98 copy whose excerpt and J14 anchor both had `depends on both ninth-bell entries` replaced with `follows both ninth-bell entries`:

```
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
DIGEST 59a0f4fa3d4a47e03649a54d1815c45ee1eef641b63a59ebe7210bc9d9b9b133
RESULT PASS
exit=0
```

The digest is the pre-C1 JSON-only digest. Markdown was not in the pin.

**Delivered pin, same excerpt+anchor edit** (`work3/prose`, tool `fb9bb9ff…`, contract `8c2561b0…`):

```
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
FINDING DIGEST-MISMATCH: content digest 1f73326f38eb20f75d6c2541df5ec67ae20e157e5b4c1053dc10464ae88d67f2 != pin 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0; changed: claim-excerpt-map.md (sha256 c1099d0ee9eece241ea1f796320a84453dfc6b6aec33b7b9dd7e39bbef4a94ba -> fc4633b90098539deb32566660ad7a6a4bd012595bc7985a7f78b9fd6d43e398), fictional-excerpts.md (sha256 29e384bf2eb2ab80858ace9423f29088a552553f87da7f6a9b694cbb050666de -> dbcd5f11f4260f0e85c3271698afe1bac79ace52c31e9b651187371fb79e4b26); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
exit=2
```

That coherent edit stays green for the other gates (`work/m7-prose-coherent`): `check_bible` CLEAN exit 0; `support_check` `RESULT PASS` exit 0; `map_obligations` `OBLIGATIONS raw=20 mapped=20` / `RESULT PASS` exit 0. So "invisible to every gate" was true of this edit before C1, and is false of the delivered freeze. The freeze finding is a byte mismatch. It does not say the dependency wording was removed, and it does not prove the remaining prose.

**Narrative-only edit** (map scope sentence `depends on both (\`aru-ninth-bell\` and \`evin-ninth-bell\`)` → `is recorded after both …`; anchors untouched), path-bound r98, delivered pin (`work4/narr`):

```
FINDING DIGEST-MISMATCH: … changed: claim-excerpt-map.md (sha256 c1099d0ee9eece241ea1f796320a84453dfc6b6aec33b7b9dd7e39bbef4a94ba -> 85b16b4f7c952fbfa80649edca86cb1a89220653f49c52f51ff8b1017b8352d0); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
exit=2
```

Same copy: `check_bible` CLEAN exit 0; `support_check` `SOURCE-SUPPORT 20/20` / `RESULT PASS` exit 0; `map_obligations` `RESULT PASS` exit 0.

**Not invisible to every gate.** Excerpt-only replacement of `depends on both ninth-bell entries`, map anchor left unchanged (`work/m7b-excerpt-only`): `check_bible` CLEAN exit 0; `map_obligations` PASS exit 0; `support_check` exit 1 `FAIL J14: source-support; mode=verbatim; anchor=not-found` / `FAIL: J14: source-support anchor missing` / `RESULT FAIL`. The J14 anchor is that sentence. Removing it without updating the map was already a lexical fail. The BR-01 prose half that every prior gate missed is the edit that keeps anchors and inventory coherent, or that edits prose no gate tokenizes.

## Row 7 — consistent-regeneration inventory bound

The gate compares the map's declared inventory to the rows it parsed, and the raw JSON pointers to the map rows. A deletion that updates both sides is indistinguishable from a smaller legitimate fixture.

r99 twin (`work/m6-consistent-regen`): delete `clerk-lapse-recorded`, delete the J21 row, restate inventory `21/2/23/19` → `20/2/22/18`. `check_bible` CLEAN exit 0; `support_check` `INVENTORY JSON-FACTS 20/20` / `RESULT PASS` exit 0; `map_obligations` `OBLIGATIONS raw=20 mapped=20` / `RESULT PASS` exit 0.

Pinned r98 twin (`work4/regen`): delete `clerk-filing-open`, delete the J20 row, restate `20/2/22/18` → `19/2/21/17`.

```
python3 corpus/tools/map_obligations.py <mirror>
OBLIGATIONS raw=19 mapped=19
INVENTORY JSON-FACTS 19/19; EDITORIAL-ROWS 2/2; TOTAL-ROWS 21/21
RESULT PASS
exit=0
python3 corpus/tools/support_check.py <mirror>
INVENTORY JSON-FACTS 19/19; … DISTINCT-ANCHORS 17/17
SOURCE-SUPPORT 19/19; … VALIDATED-ROWS 21/21
RESULT PASS
exit=0
python3 corpus/fixtures/check_bible.py <mirror>
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
python3 <mirror>/corpus/tools/dependency_freeze.py <mirror>/corpus/fixtures/r98-clerk-filing
FREEZE r98-clerk-filing: events 6/7; dependency-edges 5/6; relations 1/1
FINDING REDUCTION-DETECTED: event clerk-filing-open is missing; 1 frozen dependency edge(s) gone
RESULT FAIL
exit=1
```

`map_obligations` and `support_check` do not catch a coherent regeneration. The freeze catches the JSON event deletion, not the regenerated declaration. A coherent markdown-only restatement that does not drop a pinned edge is row 6, not this row.

## Row 8 — checker byte-frozen

Live `corpus/fixtures/check_bible.py` sha256 `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` equals `corpus/tools/boundary-doc-contract.json` `checker.sha256`.

```
python3 corpus/tools/boundary_doc_check.py
CHECK pinned inputs: PASS
…
CERTIFIED (bounded: frozen-document drift + receipts + explicit-anchor range + structure; no semantic/AST validation)
exit=0
```

A scratch copy with one extra comment line (`work/check_bible-drift.py`, sha256 `76dc4f51…`):

```
python3 corpus/tools/boundary_doc_check.py --checker .ufo/waves/round-99/seats/S5-scratch/work/check_bible-drift.py
CHECK pinned inputs: FAIL
FINDING checker_drift: delivered checker digest differs from the committed pin
CERTIFICATION FAIL
exit=1
```

Rows 1–3 are `check_bible` blind spots. Closing any of them by editing `check_bible.py` changes `ff9fd2aa…`. `boundary_doc_check` then exits 1 `checker_drift` until `corpus/tools/boundary-doc-contract.json` `checker.sha256` (and the revision field that pin cites) is re-pinned. That re-pin is outside this record. A blind spot is not closed in-checker without that contract edit. The pin proves byte identity with the recorded checker, not that the checker's rules are complete.

## Row 9 — classes `check_bible` does catch

All on scratch copies of `r99-window-lapse`, terminal event `clerk-lapse-recorded` unless noted. Each exits 1.

| Probe | Observed |
|---|---|
| `depends_on = ["no-such-event-id"]` | `VIOLATION: timeline[7].depends_on: unknown event 'no-such-event-id'` |
| `entity_id = "no-such-entity"` | `VIOLATION: timeline[7].entity_id: dangling entity 'no-such-entity'` |
| `source_id = "no-such-source"` | `VIOLATION: timeline[7].source_id: unknown in-world source 'no-such-source'` |
| drop the `depends_on` key | `VIOLATION: timeline[7].depends_on: required nonempty list` |
| `depends_on = ["clerk-lapse-recorded"]` | `self dependency 'clerk-lapse-recorded'` and `timeline inversion 'clerk-lapse-recorded' tick 15 not before 'clerk-lapse-recorded' tick 15` |
| `depends_on = ["clerk-filing-open", "clerk-filing-open"]` | `repeated dependency 'clerk-filing-open'` |
| tick set to 14, edge left on `clerk-filing-open` | `timeline inversion 'clerk-filing-open' tick 14 not before 'clerk-lapse-recorded' tick 14` |
| delete predecessor `clerk-filing-open` | `VIOLATION: timeline[6].depends_on: unknown event 'clerk-filing-open'` |

Unknown-id and dangling-entity are caught. An emptied list, a wrong-but-earlier resolvable edge, and a deleted terminal row are not (rows 1–3).

## Limits

Scratch command paths under `.ufo/waves/round-99/seats/S5-scratch/` are this seat's replay trees, not corpus. Re-run the mutation on a fresh copy if those trees are gone; the quoted outputs are this pass's measurements, not a promise that the scratch still exists. This table does not authenticate sources, does not decide the lapse, and does not extend a clean gate run into a finding, a resolution, or a canon claim. `r99-window-lapse` remains unpinned: freeze catches the classes above only on the six pinned chain fixtures.

## Dated addendum — 2026-10-17, round 100

The r99 text above is preserved unrewritten. These three measured rows scope its overbroad prose in accordance with r99 adjudication AC-1/AC-2/AC-3 (`LOG.md:3303-3313`). They add no new checker behavior. Commands below were run from `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3` on this delivered revision, using path-bound mirrors under `.ufo/waves/round-100/seats/T4-scratch/replays/`; no live fixture was mutated and no live contract was re-frozen by this author. The delivered freeze tool SHA-256 was `fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c`; the contract was `ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5` before and after all replays. Complete stdout and exact exits: `.ufo/waves/round-100/seats/T4-scratch/replay-output.txt`; rerun harness: `python3 .ufo/waves/round-100/seats/T4-scratch/replay.py run` (exit 0, `REPLAY failures=[]`).

| # | Date / round | Mutation or invocation class | Catches / observed exit | Does not establish / scoped bound |
|---|---|---|---|---|
| 10 | 2026-10-17 / r100 | Mapped-verbatim-anchor removal, excerpt-only; r99 AC-2 | Pre-r99 `4265df5` and delivered `support_check`: `FAIL: J14: source-support anchor missing`, `RESULT FAIL`, exit 1. Delivered freeze: `DIGEST-MISMATCH` naming `fictional-excerpts.md`, exit 2. Commands and control below. | “Invisible to every gate” never covered an unmatched mapped anchor. Historical JSON-only freeze passes this edit, but support checking does not. Row 6's all-green historical bound is non-anchor prose or a coherent excerpt+anchor replacement; no gate here proves prose entailment. |
| 11 | 2026-10-17 / r100 | Simultaneous dropped edge and prose edit; r99 AC-1 | Delivered freeze: only `REDUCTION-DETECTED`, `RESULT FAIL`, exit 1; no `DIGEST-MISMATCH`. Prose-only twin: named `DIGEST-MISMATCH`, `RESULT ERROR`, exit 2. Commands below. | Semantic-inventory findings precede digest reporting after the verification guards. “Any edit → exit 2” is conditional on a clean modeled inventory, not a universal exit rule and not natural-language semantics. |
| 12 | 2026-10-17 / r100 | Combined `fixture --freeze fixture`; r99 AC-3 | Delivered CLI: only `INVALID-ARGUMENTS`, `RESULT ERROR`, exit 2; live contract hash unchanged. Exact command below. | The historical precedence list does not describe an invalid combined invocation. This receipt exercises neither inventory verification nor the guarded freeze write. Exit 2 alone is not a digest finding. |

### Row 10 replay — the mapped-anchor class was already visible

Two r95 mirrors received exactly the same mutation: in `fictional-excerpts.md` line 20, replace `depends on both ninth-bell entries` with `follows both ninth-bell entries`, leaving the map's J14 anchor and every JSON byte unchanged. This removes the mapped verbatim anchor by replacement, not a dependency edge. The historical mirror's tools and contract were extracted with `git show 4265df5:<path>`; its `support_check.py` SHA-256 is the same as delivered, `55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c`. Its freeze tool is `03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b`, contract `153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947`.

```sh
python3 .ufo/waves/round-100/seats/T4-scratch/replays/pre-r99-anchor/corpus/tools/support_check.py .ufo/waves/round-100/seats/T4-scratch/replays/pre-r99-anchor/corpus/fixtures/r95-crossing-aftermath
python3 corpus/tools/support_check.py .ufo/waves/round-100/seats/T4-scratch/replays/delivered-anchor/corpus/fixtures/r95-crossing-aftermath
```

Both printed these observed lines and exited 1 (other unchanged PASS rows omitted):

```text
FAIL J14: source-support; mode=verbatim; anchor=not-found
SOURCE-SUPPORT 14/15; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 17/17; VALIDATED-ROWS 16/17
FAIL: J14: source-support anchor missing
RESULT FAIL
```

Historical freeze control:

```sh
python3 .ufo/waves/round-100/seats/T4-scratch/replays/pre-r99-anchor/corpus/tools/dependency_freeze.py .ufo/waves/round-100/seats/T4-scratch/replays/pre-r99-anchor/corpus/fixtures/r95-crossing-aftermath
```

```text
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
RESULT PASS
```

Exit 0. This is a freeze blind spot, not evidence that every historical gate passed. Delivered freeze, same mutation:

```sh
python3 .ufo/waves/round-100/seats/T4-scratch/replays/delivered-anchor/corpus/tools/dependency_freeze.py .ufo/waves/round-100/seats/T4-scratch/replays/delivered-anchor/corpus/fixtures/r95-crossing-aftermath
```

```text
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
FINDING DIGEST-MISMATCH: content digest b97a3b80df29110f6f369c7bd52ee09cd733e46f3f7d84420563c931744f7dca != pin 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710; changed: fictional-excerpts.md (sha256 0ef6734ae52d28656e75869d942d6b1e8e324b116977a2811b3b36dc0880b282 -> b0725e215a8c51bd0dda5b384396913a6d8ea36e58caa928d5b0315d47fc1aae); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
```

Exit 2. Delivered `python3 corpus/fixtures/check_bible.py .ufo/waves/round-100/seats/T4-scratch/replays/delivered-anchor/corpus/fixtures/r95-crossing-aftermath` printed `CLEAN: schema, citations, relations, timeline; 0 violations`, exit 0. Delivered `python3 corpus/tools/map_obligations.py .ufo/waves/round-100/seats/T4-scratch/replays/delivered-anchor/corpus/fixtures/r95-crossing-aftermath` printed `OBLIGATIONS raw=15 mapped=15` / `RESULT PASS`, exit 0.

### Row 11 replay — semantic findings precede a digest mismatch

In a path-bound r98 mirror, reduce `paired-crossing-decision.depends_on` from `["aru-ninth-bell", "evin-ninth-bell"]` to `["aru-ninth-bell"]` and make the same excerpt-only prose replacement as row 10. A separate r98 twin has only that prose replacement and retains every JSON byte.

```sh
python3 .ufo/waves/round-100/seats/T4-scratch/replays/delivered-precedence/corpus/tools/dependency_freeze.py .ufo/waves/round-100/seats/T4-scratch/replays/delivered-precedence/corpus/fixtures/r98-clerk-filing
```

Observed complete stdout, exit 1:

```text
FREEZE r98-clerk-filing: events 7/7; dependency-edges 5/6; relations 1/1
FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']
RESULT FAIL
```

No `DIGEST-MISMATCH` was emitted despite the additional prose edit. Inventory-clean prose-only control:

```sh
python3 .ufo/waves/round-100/seats/T4-scratch/replays/delivered-prose-control/corpus/tools/dependency_freeze.py .ufo/waves/round-100/seats/T4-scratch/replays/delivered-prose-control/corpus/fixtures/r98-clerk-filing
```

Observed complete stdout, exit 2:

```text
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
FINDING DIGEST-MISMATCH: content digest c811669ea2534d48122939e270599376160b8f5936eecb2e766c141464b6808b != pin 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0; changed: fictional-excerpts.md (sha256 29e384bf2eb2ab80858ace9423f29088a552553f87da7f6a9b694cbb050666de -> dbcd5f11f4260f0e85c3271698afe1bac79ace52c31e9b651187371fb79e4b26); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
```

The finding is byte-level, not proof that the changed sentence lost its dependency meaning. “Semantic-first” refers to modeled JSON inventory comparison, not prose interpretation (`corpus/knowledge/r100-provenance-semantics-boundary.md`).

### Row 12 replay — combined invocation is invalid only

```sh
python3 corpus/tools/dependency_freeze.py corpus/fixtures/r98-clerk-filing --freeze corpus/fixtures/r98-clerk-filing
```

Observed complete stdout, exit 2:

```text
FINDING INVALID-ARGUMENTS: pass either a fixture (verify) or --freeze DIR, not both
RESULT ERROR
```

There was exactly one FINDING, no FREEZE/DIGEST receipt, no semantic or digest finding, and no contract write: SHA-256 remained `ea012b9c362bac369056e67f55b6e0d258cb0956194ca66922a35b31f26104a5`. The invalid-argument check runs before the selected operation, so this is not an exception to valid-verification semantic precedence.

### Dated coverage supersession (2026-10-17, r100)

The old “r99 unpinned / six fixtures” sentences in this file describe the r99 pass, not current coverage. On this pass `python3 corpus/tools/dependency_freeze.py corpus/fixtures/r99-window-lapse` printed `FREEZE r99-window-lapse: events 8/8; dependency-edges 7/7; relations 1/1`, `DIGEST 7fe7e3b065088e59863697bdf8223eef9b91ba44efce5c696d0986fb506e470e`, `RESULT PASS`, exit 0. The other six named pins also passed, for 7/7. This discharges the r99 coverage bound without changing the table's semantic limits; no claim is made that r100 is pinned.

## Dated addendum (2026-10-18, round-101 closure, AC-2)

Row 2 ("wrong-but-earlier dependency edge") is closed by the delivered
gate: a `depends_on` repointed to a different valid earlier event now
produces BOTH `REDUCTION-DETECTED` and `ADDITION-DETECTED` in one run,
exit 1 — pinned as the persisted self-test case `repointed_edge` (contract
19 cases; replayed by seats V03/V05/V20 and the r101 adjudicator). Prior
rows unmodified; this record was appended by the closure integrator
because the table was outside r101 producer byte-ownership.
