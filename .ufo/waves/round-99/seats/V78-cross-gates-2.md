# V78 — cross-gates-2 (round 99)

- Seat: V78 cross-gates-2 (verifier). Lane repo `/home/vgpnk/Projects/shokunin/lore-shokunin`. Baseline r98 closure `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`). All commands from the lane repo root with `python3`.
- Task as briefed: second cross-gate matrix on an r98 copy (four mutations); compare with V09.
- Axes named: calibration (does full-file freeze catch a pinned-file edit the r98 tool missed), cross-gate coverage (which of the five gates catch each mutation), comparison completeness (V09's reported exits, not a plan).
- Writes: this report plus `.ufo/waves/round-99/seats/V78-scratch/` only. No commits, no pushes, no network, no nested agents. Seats dir realpath verified as `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats` before the report write. No corpus byte was written by this seat.

## 0. Poll-wait record

Producer reports required: `S1-freeze-hygiene.md`, `S2-tools-docs.md`, `S3-fixture-author.md`, `S4-fixture-docs.md`, `S5-knowledge-notes.md`. Comparison target: `V09-c1-cross-gates.md`. Cadence 20 s. Log: `.ufo/waves/round-99/seats/V78-scratch/poll.log`.

- Tries 1–15 (`2026-10-18T01:04:18Z`–`01:08:59Z`): S3 and then S4 present; S1, S2, S5 absent. The first poll process was killed by its 300 s tool timeout before try 40.
- Tries 16–40 (`poll-continue.sh`, try 40 at `2026-10-18T01:36:15Z`, `POLL-EXHAUSTED` `01:36:35Z`): S1, S2, S5 still absent; V09 report absent on every try. Contract already schema 2, 18 expected cases, six pins, 10 files each, from try 16 onward.
- Bounded stall-escape, recorded not fatal (`.ufo/waves/round-99/seats/V78-scratch/poll-escape.log`): 8 further tries `01:46:25Z`–`01:49:05Z`, S1 absent, V09 absent, tool hash stable `fb9bb9ff…`.
- Final presence check `2026-10-18T01:59:28Z`: `S1-freeze-hygiene.md` ABSENT, `V09-c1-cross-gates.md` ABSENT. S3 and S4 reports were present from `01:04Z` / `01:03Z` local. S2's README and SKILL.md, and both S5 knowledge files, existed as working-tree paths by `01:59:28Z`, but neither producer report had landed. This seat does not treat those paths as a delivered revision.

V09's scratch mutator existed by `22:33` local (`V09-scratch/mutate.py`) with no report. That file is a plan, not a verdict. It is cited only to show class alignment. No V09 exit was copied from it.

## 1. Revisions actually measured

Freeze quotes in §3 were re-run on the live tool after the one-line detail-string edit below. Other-gate quotes are from the same mutant fixture bytes.

```
fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c  corpus/tools/dependency_freeze.py
8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628  corpus/tools/dependency-freeze-contract.json
03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b  baseline tool (git show 4265df5:corpus/tools/dependency_freeze.py)
153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947  baseline contract (git show 4265df5:…)
```

The matrix was first run on tool `6f81f8be19742372ddc6819f6cf50dad985fe2bca2bee2b6e7c579613f5f4067` (same contract). After that run the live tool moved to `fb9bb9ff…`. The only diff is the DIGEST-MISMATCH detail phrase:

```
- fixture bytes changed outside the frozen inventory
+ pinned-file bytes changed outside the semantic inventory
```

Re-quote on `fb9bb9ff…` (`.ufo/waves/round-99/seats/V78-scratch/requote-fb9bb9ff.txt`) left every freeze exit and finding ID unchanged. Hash `fb9bb9ff…` was still the live tool at `01:59:28Z`.

Not certified: `S1-freeze-hygiene.md` never landed, so these bytes are not a producer-declared delivery. They are the bytes present on disk.

Pin state read from the contract at measurement: schema 2; `self_test.expected` has 18 cases including `markdown_tamper`; pins are the six chain fixtures; each pin's `files` object has 10 entries including the five Markdown files. `r99-window-lapse` is not pinned.

Intact chain on `fb9bb9ff…` at `01:59:28Z`, all exit 0:

```
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0
DIGEST acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae
RESULT PASS
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
DIGEST 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef
RESULT PASS
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710
RESULT PASS
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
DIGEST 43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c
RESULT PASS
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1
DIGEST a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54
RESULT PASS
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
DIGEST 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0
RESULT PASS
```

`--self-test` was run once, on `6f81f8be…` at `01:15:22Z`, not re-run after the detail-string edit: `SELF-TEST 18/18` / `RESULT PASS` / exit 0, including `CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok`. The later edit does not touch finding IDs. That is an observation on a superseded tool hash, not a claim that `fb9bb9ff…` was self-tested.

## 2. Four mutations (r98 copy)

Choice, recorded because the dispatch sentence does not name the four: the first four of V09's five classes (`edge reduction; prose-word removal; map row drop; span break`), omitting V09's fifth (`source-id change`). V09's scratch mutator uses those same four class names on `r96-crossing-response`. This seat applied them to `corpus/fixtures/r98-clerk-filing`, the r98 terminal event and the r98 last map row. Each mutant is a full copy under `.ufo/waves/round-99/seats/V78-scratch/mirrors/delivered-<kind>/corpus/fixtures/r98-clerk-filing`. The only differing file in each copy is the one named below.

1. `edge-reduction` — `timeline.json` only. `clerk-filing-open.depends_on` `["acknowledgment-aru-records"]` → `[]` (key kept).

```
-    "depends_on": [
-      "acknowledgment-aru-records"
-    ],
+    "depends_on": [],
```

2. `prose-word-removal` — `fictional-excerpts.md` only. Deleted the word `depends` from the J14 anchor sentence (same sentence V09's mutator targets):

```
- Their tick-10 decision depends on both ninth-bell entries:
+ Their tick-10 decision on both ninth-bell entries:
```

3. `map-row-drop` — `claim-excerpt-map.md` only. Deleted the `| J20 |` table row. The inventory declaration stayed at 20 JSON facts / 22 total rows.

4. `span-break` — `claim-excerpt-map.md` only. J20 line span `55-64` → `1`. V09's scratch span-break narrows `| 33-42 |` to `| 33-36 |` on r96. Same class (anchor outside the declared span), not the same bytes.

## 3. Cross-gate table

Five gates, same mutant bytes. `check_bible` / `support_check` / `map_obligations` are the lane tools. `dependency_freeze` is the mirror copy of `fb9bb9ff…` plus contract `8c2561b0…`, invoked on the mirror fixture so path binding matches the pin's `corpus/fixtures/r98-clerk-filing`. `boundary_doc_check` takes no fixture input; its receipt was identical on every mutant.

| mutation | check_bible | support_check | map_obligations | dependency_freeze (delivered) | dependency_freeze (r98 tool `03d04365…`) | boundary |
|---|---|---|---|---|---|---|
| clean | 0 CLEAN | 0 PASS 20/20 | 0 raw=20 mapped=20 | 0 PASS digest `5ecf84e1…` | 0 PASS digest `59a0f4fa…` | 0 CERTIFIED |
| edge-reduction | 0 | 0 | 0 | **1 REDUCTION-DETECTED** | **1 REDUCTION-DETECTED** | 0 |
| prose-word-removal | 0 | **1** J14 anchor missing | 0 | **2 DIGEST-MISMATCH** names `fictional-excerpts.md` | 0 PASS digest `59a0f4fa…` (blind) | 0 |
| map-row-drop | 0 | **1** inventory 19/20 | **1** missing `timeline.json#/6` | **2 DIGEST-MISMATCH** names `claim-excerpt-map.md` | 0 PASS digest `59a0f4fa…` (blind) | 0 |
| span-break | 0 | **1** J20 outside span 1 | 0 | **2 DIGEST-MISMATCH** names `claim-excerpt-map.md` | 0 PASS digest `59a0f4fa…` (blind) | 0 |

Quotes (delivered freeze from the `fb9bb9ff…` re-quote; other gates from `.ufo/waves/round-99/seats/V78-scratch/transcripts/gates-*.txt`):

```
$ python3 <mirror>/corpus/tools/dependency_freeze.py <mirror>/corpus/fixtures/r98-clerk-filing
# edge-reduction
FREEZE r98-clerk-filing: events 7/7; dependency-edges 5/6; relations 1/1
FINDING REDUCTION-DETECTED: event clerk-filing-open lost depends_on ['acknowledgment-aru-records']
RESULT FAIL
EXIT=1

# prose-word-removal
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
FINDING DIGEST-MISMATCH: content digest 1ff39c53b95a1c343c58669aa35b2e2cfdea7d2170cac475953ef7373ec8ca8d != pin 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0; changed: fictional-excerpts.md (sha256 29e384bf2eb2ab80858ace9423f29088a552553f87da7f6a9b694cbb050666de -> d36f183fce3ab088449e929cff7362ffa70b7f7ea9646ea64697eea8f399daf1); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
EXIT=2

# map-row-drop
FINDING DIGEST-MISMATCH: … changed: claim-excerpt-map.md (sha256 c1099d0e… -> 3c8b2e4b…); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
EXIT=2

# span-break
FINDING DIGEST-MISMATCH: … changed: claim-excerpt-map.md (sha256 c1099d0e… -> 57de341c…); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
EXIT=2
```

Other gates, same bytes:

```
# edge-reduction
CLEAN: schema, citations, relations, timeline; 0 violations          EXIT=0
SOURCE-SUPPORT 20/20; … VALIDATED-ROWS 22/22
RESULT PASS                                                           EXIT=0
OBLIGATIONS raw=20 mapped=20
RESULT PASS                                                           EXIT=0

# prose-word-removal
CLEAN: … 0 violations                                                 EXIT=0
FAIL J14: source-support; mode=verbatim; anchor=not-found
SOURCE-SUPPORT 19/20; … VALIDATED-ROWS 21/22
FAIL: J14: source-support anchor missing
RESULT FAIL                                                           EXIT=1
OBLIGATIONS raw=20 mapped=20
RESULT PASS                                                           EXIT=0

# map-row-drop
CLEAN: … 0 violations                                                 EXIT=0
INVENTORY JSON-FACTS 19/20; … TOTAL-ROWS 21/22; DISTINCT-ANCHORS 17/18
FAIL: inventory JSON facts mismatch: expected=20 parsed=19
RESULT FAIL                                                           EXIT=1
OBLIGATIONS raw=20 mapped=19
FINDING missing_obligation: timeline.json#/6 has no map row
RESULT FAIL                                                           EXIT=1

# span-break
CLEAN: … 0 violations                                                 EXIT=0
FAIL: J20: anchor hit outside declared line span 1 (hit lines: 59)
SOURCE-SUPPORT 19/20; … VALIDATED-ROWS 21/22
RESULT FAIL                                                           EXIT=1
OBLIGATIONS raw=20 mapped=20
RESULT PASS                                                           EXIT=0

# boundary, every mutant
CERTIFIED (bounded: frozen-document drift + receipts + explicit-anchor range + structure; no semantic/AST validation)
EXIT=0
```

Baseline freeze (`03d04365…` + contract `153ebc5b…`, five-JSON pin, digest `59a0f4fa3d4a47e03649a54d1815c45ee1eef641b63a59ebe7210bc9d9b9b133`) on the same four mutant trees: edge-reduction exit 1 with the same `REDUCTION-DETECTED` line; the three Markdown mutants exit 0 `RESULT PASS` with that unchanged digest. So the r98 tool already caught the edge drop and was blind to the three Markdown edits. The live tool catches all four. The prose case is not freeze-only: `support_check` also fails, because the removed word sits inside the J14 exact anchor.

## 4. Extra controls (not one of the four)

Run on tool `6f81f8be…` before the detail-string edit. Exits DIGEST-MISMATCH phrase was the old wording. Finding ID and named file are the load-bearing part; the four-mutation re-quote shows the phrase change does not change those.

- Non-anchor excerpt edit: `fictional-excerpts.md` scope sentence `institutional filing only` → `institutional record only`. Delivered freeze exit 2, `changed: fictional-excerpts.md`. `check_bible` 0, `support_check` 0 `SOURCE-SUPPORT 20/20` `RESULT PASS`, `map_obligations` 0 `raw=20 mapped=20`. Baseline freeze exit 0 digest `59a0f4fa…`.
- `inspiration-note.md`: `This note records` → `This note notes`. Delivered freeze exit 2, `changed: inspiration-note.md`. The other three gates exit 0 with the same PASS lines. Baseline freeze exit 0 digest `59a0f4fa…`.

That is the BR-01 prose half the declaration describes: a Markdown edit outside anchors was invisible to every gate on the r98 tool, and the live tool reports exit 2 `DIGEST-MISMATCH` naming the file. It is not semantics-provable. The anchor-resident prose mutation in §3 is a different result: `support_check` already caught it before full-file pinning.

## 5. Comparison with V09

`V09-c1-cross-gates.md` was absent at try 40, absent through the 8-try stall-escape, and absent at `01:59:28Z`. No V09 exit, digest, or finding line is available to compare. Result comparison is therefore not done.

Class alignment, from V09's scratch mutator only (not a report, not a verdict):

- Same four class names, plus a fifth `source-id` mutation this seat did not run.
- Prose marker is the same sentence and the same word removal (`depends`).
- Edge reduction empties `depends_on` on that fixture's terminal event (r96 `response-evin-salt-court` vs r98 `clerk-filing-open`).
- Map-row drop deletes the last event row and leaves the inventory declaration (r96 J16 vs r98 J20).
- Span-break is the same class and not the same edit (V09 narrows `33-42` to `33-36`; this seat sets J20's span to `1`).

A later disagreement on span-break bytes would not by itself be a cross-seat contradiction.

## 6. Write audit

Post-run live hashes at `01:59:28Z` still `fb9bb9ff…` / `8c2561b0…`. `git status --porcelain` at that time showed producer-owned paths only (`SKILL.md`, `corpus/tools/README.md`, the freeze tool and contract, untracked `corpus/knowledge/r99-gate-blind-spot-table.md`, `corpus/knowledge/r99-lapse-scope-note.md`, plus the r99 fixture and `.ufo/waves/round-99/` from earlier in the wave). `corpus/fixtures/r98-clerk-filing` was not in that status. This seat's writes are this report and `.ufo/waves/round-99/seats/V78-scratch/` (`poll.sh`, `poll-continue.sh`, `poll.log`, `poll-escape.log`, `run_matrix.py`, `pins.json`, `summary.json`, `requote-fb9bb9ff.txt`, `snapshot/`, `mirrors/`, `transcripts/`, `extra/`, `r98-tools/`).

## Scope of this evidence

Shown, on the bytes hashed in §1, not on a producer-declared delivery: the four mutations' five-gate exits; the r98 tool's blindness to the three Markdown edits; the live tool's `DIGEST-MISMATCH` naming the edited file; chain 6/6 exit 0 on `fb9bb9ff…`. Not shown: V09's exits; that `fb9bb9ff…` is S1's final revision; that the frozen inventories are semantically correct; any r99 fixture or blind-spot-table claim.

## Bottom line

**ABSENT** — `V09-c1-cross-gates.md` never landed (40 tries plus an 8-try stall-escape, still absent at `01:59:28Z`), and `S1-freeze-hygiene.md` never landed, so the four-mutation matrix above is an observation on uncertified bytes (`fb9bb9ff…` / `8c2561b0…`), not a delivered-revision verdict and not a comparison with V09.
