# V91 — verdict-crosscheck-freshness (round 99)

Seat: **V91 verdict-crosscheck-freshness**. Brief: independent freshness verdict; compare V32. Report path (absolute): `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V91-crosscheck-freshness.md`. Scratch: `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V91-scratch/` (`realpath` resolved under `lore-shokunin/` before any write). Lane root for every command: `/home/vgpnk/Projects/shokunin/lore-shokunin`. Baseline named in the standing r99 declaration: r98 closure `4265df5`. HEAD during this seat: `337f0fa52b02626b7687eedbb2d99fab30446fe4` (`lore r99: record blocked dispatch attempt … zero increment`); `git merge-base --is-ancestor 4265df5 HEAD` succeeded. Leaf seat: no nested agents, no commits, no pushes, no network. No freshness score was issued on in-flight bytes.

Axes for this seat: independence (own commands, not a copy of V32), completeness (required durable bytes plus producer reports), comparability (agree/disagree against V32 only on a landed report), evidence (quoted commands), non-harm (writes only this report and `V91-scratch/`).

## Verdict

**FRESHNESS: ABSENT** — not scored. The bytes this axis judges (S5's two knowledge notes, plus producer reports for the pin-owning seats) were not on disk after the 40-try budget, and were still absent at the 22:27:08 and 22:43:02 rechecks. I did not replay gates, compare contract digests to files, or treat the in-flight freeze pair or the r99 fixture as a finished freshness surface.

**Comparison with V32: AGREE on ABSENT.** V32's report was absent through my expire and my 22:27:08 check. It landed at `2026-10-17 22:32:25 -0300` (`V32-verdict-freshness.md`, 5550 bytes, sha256 `e94a49e63825fcdeaad4561b45dec05d8676b255317dbe3008e778ca098ad711`). V32's verdict is also **FRESHNESS: ABSENT — not scored**, on the same missing set. No disagreement on the axis. One later observation (freeze `.py` moved again after both of us expired) is recorded below; it does not change either ABSENT.

## Poll-wait record (20 s cadence, 40 tries; never verified a plan)

Gate (artifact AND producer reports; SELF subtracted — V91 was never in the wait set):

- nonempty `corpus/fixtures/r99-window-lapse/` ten-file set
- nonempty `corpus/knowledge/r99-gate-blind-spot-table.md`
- nonempty `corpus/knowledge/r99-lapse-scope-note.md`
- nonempty `corpus/tools/dependency_freeze.py` and `dependency-freeze-contract.json`
- at least five `S[1-5]*.md` producer reports under `.ufo/waves/round-99/seats/` (maxdepth 1)

V32's report was logged each try but was **not** a gate (one-way comparison; no all-reports poll; no mutual wait).

```
POLL_START 2026-10-17T22:03:12-0300
try=1 t=2026-10-17T22:03:12-0300 art=no rep=no v32=no sreports=[S3-fixture-author.md ] freeze12=[65c1ae309385 153ebc5b2092 ]
try=4 t=2026-10-17T22:04:12-0300 art=no rep=no v32=no sreports=[S3-fixture-author.md S4-fixture-docs.md ] freeze12=[1728ed892442 153ebc5b2092 ]
try=40 t=2026-10-17T22:16:12-0300 art=no rep=no v32=no sreports=[S3-fixture-author.md S4-fixture-docs.md ] freeze12=[6f81f8be1974 8c2561b043c2 ]
POLL_EXPIRE try=40 2026-10-17T22:16:32-0300
```

Full log: `.ufo/waves/round-99/seats/V91-scratch/poll.log` (42 lines). Poll pid `1694735` exited after `POLL_EXPIRE`. No stall inside the 40 tries. `art` stayed `no` because the two knowledge files never appeared. `rep` stayed `no` because S1, S2, and S5 reports never appeared. `v32` stayed `no` for all 40 tries.

**Bounded stall-escape (recorded, not a second budget):** after expire, presence checks at 22:19:35, 22:27:08, and 22:43:02. Knowledge notes and S1/S2/S5 reports still absent at all three. V32's report appeared only on the last of those checks (mtime 22:32:25), after my first draft had already recorded it absent. That late landing is folded in here; it is not a reason to score the unsigned tree.

## What was present (presence only — not a freshness judgment)

At 22:19:35, from the lane root:

```
PRESENT 6176  corpus/fixtures/r99-window-lapse/README.md
PRESENT 17119 corpus/fixtures/r99-window-lapse/claim-excerpt-map.md
PRESENT 3    corpus/fixtures/r99-window-lapse/contradictions.json
PRESENT 1793 corpus/fixtures/r99-window-lapse/entities.json
PRESENT 5114 corpus/fixtures/r99-window-lapse/fictional-excerpts.md
PRESENT 1956 corpus/fixtures/r99-window-lapse/inspiration-note.md
PRESENT 139  corpus/fixtures/r99-window-lapse/relations.json
PRESENT 640  corpus/fixtures/r99-window-lapse/source-excerpt.md
PRESENT 3293 corpus/fixtures/r99-window-lapse/sources.json
PRESENT 2998 corpus/fixtures/r99-window-lapse/timeline.json
PRESENT 29104 corpus/tools/dependency_freeze.py
PRESENT 25987 corpus/tools/dependency-freeze-contract.json
```

Producer reports present at expire and still at 22:43:02: `S3-fixture-author.md`, `S4-fixture-docs.md` only.

`git diff --stat -- SKILL.md corpus/tools/README.md` at 22:19:35 and again at 22:27:08 printed nothing. Both files were byte-identical to `4265df5` at poll start (`sha256sum`: README `294dd56f29ce1fd40be3a80d365b33724c9cd1969d3f7b7abb271fd1adaaa207`, SKILL `22ffaa822ec7614fa85322f7fa07e6f369c0888e1107f9f297f76a14e18c20c5`). S2's owned freeze-row update had not landed. V32 independently recorded the same empty `git diff --stat 4265df5 -- corpus/tools/README.md SKILL.md` and mtimes `21:32:05` / `21:34:23`, which predate this wave. Agreed: that unchanged r98 text is not scored as a freshness harm.

Freeze pair versus `4265df5` (observation of movement, not a signed delivery):

```
4265df5 dependency_freeze.py            03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b
4265df5 dependency-freeze-contract.json 153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947
live at try=1                           65c1ae309385 … / 153ebc5b2092 …
live at try=40, 22:27:08, and V32's 22:31:14 recheck
                                        6f81f8be19742372 … / 8c2561b043c25db7 …
live at 22:43:02                        fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c
                                        / 8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628
```

The pair's 12-hex prefix was stable from poll try 18 (`22:08:52`) through 22:27:08, and V32's report quotes the same `6f81f8be…` / `8c2561b0…` pair as stable through 22:31:14. That window-stability is real and shared. It is not a delivery: S1's report never arrived. A later `sha256sum` at 22:43:02 shows `dependency_freeze.py` moved again (`6f81f8be…` → `fb9bb9ff…`) while the contract hash did not. Scoring either hash would be scoring an unfinished write. This seat did not replay `--self-test`, did not recompute pin digests, and did not classify live pins.

Early `git status --porcelain -uall` (excluding `.ufo/`) showed `M corpus/tools/dependency_freeze.py` plus the ten untracked `r99-window-lapse/` paths. That listing is a snapshot, not a freeze. By 22:43 the contract was also modified relative to `4265df5` (hash above); still unsigned.

## What was absent (the gate)

| required | state at expire, 22:27:08, and 22:43:02 |
|---|---|
| `corpus/knowledge/r99-gate-blind-spot-table.md` | ABSENT (`ls corpus/knowledge/r99*` → no such file) |
| `corpus/knowledge/r99-lapse-scope-note.md` | ABSENT |
| `S1*.md` producer report | ABSENT |
| `S2*.md` producer report | ABSENT |
| `S5*.md` producer report | ABSENT |

`find corpus -name 'r99*'` at 22:19:35 returned only `corpus/fixtures/r99-window-lapse`. No alternate knowledge filename.

Scratch correction (does not change ABSENT): my 22:27 `find -maxdepth 2` on `S1-scratch` printed no files and I wrote "empty/missing." That depth cap was wrong. An unbounded find at 22:43:02 shows `S1-scratch/before/mirror/` and `S1-scratch/after/mirror/` with tool and fixture copies (after-mirror `dependency_freeze.py` 29104 bytes). Still no `S1*.md`. V32 at 22:31 described `S1-scratch/before/` as empty-looking and did not mention `after/`. That is a timing difference in an unsigned scratch tree, not a verdict conflict. `S5-scratch/` was still absent. No S2 report.

## Comparison with V32

V32 poll log (read, not authored here), expire before their report:

```
try=40 t=2026-10-17T22:22:00-0300 art=no rep=no sreports=[S3-fixture-author.md S4-fixture-docs.md ] freeze12=[6f81f8be1974 8c2561b043c2 ] know=[]
POLL_EXPIRE try=40 2026-10-17T22:22:20-0300
```

V32's own report (`V32-verdict-freshness.md:5-7`, `:81-83`) says the same thing this seat measured independently: knowledge notes absent, S1/S2/S5 reports absent, README/SKILL unchanged from `4265df5`, freeze pair observed but not scored, no receipt replay. V32's recheck timestamp is `2026-10-17T22:31:14-0300`. Mine is `22:27:08` and `22:43:02`.

| point | V91 | V32 | relation |
|---|---|---|---|
| freshness score | ABSENT, not scored | ABSENT, not scored | agree |
| knowledge notes | absent at 22:43:02 | absent at 22:31:14 | agree |
| S1/S2/S5 reports | absent | absent | agree |
| SKILL.md / tools README vs `4265df5` | empty diff at 22:27:08 | empty diff; mtimes 21:32/21:34 | agree |
| freeze pair through ~22:31 | `6f81f8be…` / `8c2561b0…` | same pair, quoted in full | agree on that window |
| freeze `.py` after 22:32 | `fb9bb9ff…` at 22:43:02 | not in V32's window | later drift; neither scored it |
| S1-scratch contents | mirrors present by 22:43 | `before/` empty-looking at 22:31 | timing, not a verdict split |

No contradiction on the axis. V32 did not claim improved, unchanged, or harmed. This seat does not either.

## What this seat did not do

- Did not issue improved / unchanged / harmed / unprovable on freshness.
- Did not treat the moving freeze pair, the r99 fixture, S3/S4 reports, or S1's scratch mirrors as a delivered revision for pin classification.
- Did not run `measure.py` (written under scratch, unused) against the unsigned tree.
- Did not wait on any other V-seat as a gate. V32 was a comparison target only, read after it landed. No all-reports poll. SELF was never a gate.
- Did not edit corpus, SKILL, LOG, SCORECARD, or any other seat's path.

## Write audit

Writes: this report (rewritten once after V32 landed, same path), plus `V91-scratch/{poll.sh,poll.log,poll.stdout,pin_inventory.py,measure.py,pin-inventory-early.txt,r99-fixture-early.sha,r98-fixture.sha,porcelain-early.txt}`. `pin-inventory-early.txt` is a mid-flight scan and is **not** evidence of a delivered pin set. No parent-tree writes. No commits.

Bottom line: **ABSENT** — knowledge notes and S1/S2/S5 reports still missing at 22:43:02 after a 40-try expire (22:16:32-0300); freshness not scored; agrees with V32's ABSENT (`e94a49e6…`, landed 22:32:25); freeze `.py` moved again after both windows (`6f81f8be…` → `fb9bb9ff…`) and was not scored.
