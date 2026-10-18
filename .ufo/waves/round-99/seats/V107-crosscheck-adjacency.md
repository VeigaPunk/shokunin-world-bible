# V107 — crosscheck adjacency (round 99)

**Seat:** V107 (verdict-crosscheck-adjacency), round-99 single wave (128 seats), lane `lore-shokunin`.
**Subject:** the delivered r99 working tree vs baseline r98 closure `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`). HEAD at start and at the post-battery recheck was `337f0fa` (`337f0fa52b02626b7687eedbb2d99fab30446fe4`, "lore r99: record blocked dispatch attempt … — zero increment"). No r99 seat commit. This seat makes **no** C1/C2 verdict, no admission verdict, and no lore-truth ruling.
**Mandate:** one independent ADJACENCY verdict, then compare V33 (`V33-verdict-adjacency.md`). Battery ran only after artifacts and all five producer reports existed.
**Axes:** (1) `PROVINCE.md` byte-identity vs `4265df5`; (2) write boundary and declared producer byte-ownership; (3) mythology editorial-only plus rights/canon/mechanics refusal in the new bytes; (4) reports-vs-bytes ordering and post-report stability; (5) r99-specific adjacency — SKILL.md freeze-row-only, pin paths stay inside `corpus/fixtures/**`, chain fixtures unmutated.
**Measurement freeze:** producer gate met `2026-10-17 23:11:13 -0300`. Battery `23:11:18`–`23:11:21`. Hash recheck `23:12:24` matched the freeze prefixes. Commands from `/home/vgpnk/Projects/shokunin/lore-shokunin` unless noted. This seat's only writes are this report and `.ufo/waves/round-99/seats/V107-scratch/`.

## Poll-wait record

Gate: 16 producer artifacts (S1 tool + contract, S2 `corpus/tools/README.md` + `SKILL.md`, ten `corpus/fixtures/r99-window-lapse/` files, S5's two knowledge notes) and five `S*-*.md` reports. Endgame: the gate was those five reports, not all 128 seats. SELF was never in the count.

- Loop 1, `V107-scratch/poll.sh`, `POLL_START 2026-10-17 22:02:26 -0300`. Hosting command killed at its 300 s tool ceiling after try 15 (`22:07:06`, `arts=14/16 reps=1/5`). Not a protocol ABSENT. **Filename error, disclosed:** this loop watched `V33-adjacency.md`. The roster path is `V33-verdict-adjacency.md`. That miss did not change the producer gate.
- Loop 2 restarted the counter at `22:13:28` (tool-kill gap, not an extra protocol sleep) and ran its own 40 tries. Close:

```
POLL t=22:26:29 try=40 arts=14/16 reps=2/5 v33=0 … names=[S3-fixture-author.md S4-fixture-docs.md ] missing=[ corpus/knowledge/r99-gate-blind-spot-table.md corpus/knowledge/r99-lapse-scope-note.md]
TIMEOUT t=2026-10-17 22:26:49 -0300 arts=14 reps=2 v33=0
```

`grep -c '^POLL t=' V107-scratch/poll.log` → `55` (15 + 40). No `ALL-PRESENT`. At that close the delivered revision was not assembled. I did not score it.

- Stall-escape 1 (`poll-escape.sh`, recorded, 30 tries, start `22:48:17`): S1 report appeared at try 3 (`S1-full-file-pins.md`). S2's README/SKILL hashes moved at try 12. Knowledge files appeared at try 30 (`22:57:57`, `arts=16/16 reps=3/5`) and the escape then exited 2 (`ESCAPE1_TIMEOUT … arts=16 reps=3`). Still not scored.
- Stall-escape 2 (`poll-escape2.sh`, recorded, start `23:06:13`): `ALL-PRESENT t=2026-10-17 23:11:13 -0300 try=16` with `reps=5/5` and names `[S1-full-file-pins.md S2-tools-docs.md S3-fixture-author.md S4-fixture-docs.md S5-knowledge-author.md ]`. Battery started after that line.

## Comparison with V33

V33 report: `.ufo/waves/round-99/seats/V33-verdict-adjacency.md`, 68 lines, mtime `22:27`, sha256 `61ba3ac0f6f3aced04ff5d3764086f7136cb7869ccd5ab24a25b512ec9448138` (re-hashed `23:12:24`, unchanged). Bottom line: **ABSENT**. Battery not run. Their window was 40 poll lines `22:01:29`–`22:19:09`, recheck `22:25:40`: S1/S2/S5 reports missing, both knowledge files absent.

That ABSENT was correct for that window. I saw the same absence independently through `22:26:49` (knowledge files absent, reports only S3 and S4, `dependency_freeze.py` prefix `6f81f8be1974` with no S1 report). V33 scored nothing, so there is no scored disagreement to reconcile. The divergence is timing: producers finished after V33 closed (`S1` report `22:48:57`, knowledge files `22:57:50`, `S2` `23:10:49`, `S5` `23:10:56`). My verdict below is on that later tree, not a contradiction of V33's poll facts.

---

## A1 — `PROVINCE.md` byte-identical to `4265df5`

```
$ sha256sum PROVINCE.md
94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa  PROVINCE.md
$ git show 4265df5:PROVINCE.md | sha256sum
94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa  -
$ git hash-object PROVINCE.md
7c599c395e1710b6a7c7aca6d485c373bed6deb7
$ git rev-parse 4265df5:PROVINCE.md
7c599c395e1710b6a7c7aca6d485c373bed6deb7
$ git diff 4265df5 -- PROVINCE.md | wc -c
0
```

Same three values at `23:12:24`. Other charter docs vs `4265df5`:

```
PROVINCE.md      IDENTICAL 7c599c395e1710b6a7c7aca6d485c373bed6deb7
SHONEN.md        IDENTICAL 561b3f8ce99e35200fcfa2269198a7f7f68f1a5e
README.md        IDENTICAL 7c46413cf7781ae3cdbaa7bae7e265f7ddcbbe70
l0-questions.md  IDENTICAL f9fdff500e043c63d7bbfd0ffad90f8cfd66de4e
SKILL.md         DIFF (S2 freeze row; §A5) work=c5d4b74177ae09fdcb748e34c6924d24dde0cc12
SCORECARD.md     DIFF vs 4265df5, IDENTICAL to HEAD (committed 111b9a3, not an r99 write)
```

**Result: PASS.**

---

## A2 — in-lane change set is the declared byte-ownership

```
$ git diff --name-status HEAD
M	SKILL.md
M	corpus/tools/README.md
M	corpus/tools/dependency-freeze-contract.json
M	corpus/tools/dependency_freeze.py

$ git diff --numstat HEAD
3	3	SKILL.md
73	0	corpus/tools/README.md
146	17	corpus/tools/dependency-freeze-contract.json
61	6	corpus/tools/dependency_freeze.py
```

Blob audit vs `4265df5` (`V107-scratch/audit_tree.py`, `23:11:18`):

```
baseline non-ufo tracked files: 2840
CHANGED (6):
  LOG.md
  SCORECARD.md
  SKILL.md
  corpus/tools/README.md
  corpus/tools/dependency-freeze-contract.json
  corpus/tools/dependency_freeze.py
MISSING (0):
UNTRACKED non-ufo (12): the 10 corpus/fixtures/r99-window-lapse/ files
  + corpus/knowledge/r99-gate-blind-spot-table.md
  + corpus/knowledge/r99-lapse-scope-note.md
```

Attribution: tool + contract → **S1**; tools README + SKILL freeze row → **S2**; r99 JSON tables + `fictional-excerpts.md` → **S3**; r99 README + claim-excerpt-map → **S4**; the two knowledge files → **S5**. `LOG.md` vs HEAD is empty (`git diff HEAD -- LOG.md | wc -c` → `0`); the `91 0` delta vs `4265df5` is the committed blocked-dispatch record in `337f0fa`, not a seat write this wave. `SCORECARD.md` vs HEAD is empty; `git log -1 -- SCORECARD.md` → `111b9a3 2026-10-17 21:37:06 lore r98: close round — SCORECARD admitted section`.

Census: `ls -d corpus/fixtures/*/ | wc -l` → **173**. Chain fixtures vs `4265df5`: `git diff --name-only 4265df5 -- corpus/fixtures/<d>` file count **0** for r88-m3, r94, r95, r96, r97, r98. New files mode 644, `find corpus/fixtures/r99-window-lapse -type l | wc -l` → `0`.

`21:36:10` mtimes on the seven unchanged r99 copies match `4265df5`'s commit time (`git log -1 --format='%ci' 4265df5` → `2026-10-17 21:36:10 -0300`), i.e. `git archive` timestamps, not a pre-wave stray.

**Result: PASS for the lane-internal change set.**

---

## A3 — writes outside `lore-shokunin` — FAIL

Parent-tree wave directory, absent at my `22:02` check (`ls -d /home/vgpnk/Projects/shokunin/.ufo/waves/round-99` → `No such file or directory`), present at the battery:

```
$ ls -la /home/vgpnk/Projects/shokunin/.ufo/waves/round-99/seats
V69-scratch   22:11
V73-scratch   22:17
$ find /home/vgpnk/Projects/shokunin/.ufo/waves/round-99 -type f | wc -l
8
$ git -C /home/vgpnk/Projects/shokunin status --porcelain
?? .ufo/waves/round-99/
```

The eight files (`find -printf`):

- `V69-scratch/before/baseline-root/corpus/tools/dependency_freeze.py` — 0 bytes, `22:11:27`
- `V69-scratch/before/baseline-root/corpus/tools/dependency-freeze-contract.json` — 0 bytes, `22:11:27`
- `V73-scratch/selftests/{boundary,map,freeze}.out` — 0 bytes, `22:17:58`
- `V73-scratch/selftests/boundary.err` — 129 bytes
- `V73-scratch/selftests/map.err` — 126 bytes
- `V73-scratch/selftests/freeze.err` — 128 bytes

`freeze.err` is one line: `python3: can't open file '/home/vgpnk/Projects/shokunin/corpus/tools/dependency_freeze.py': [Errno 2] No such file or directory`. `boundary.err` is the same class for `boundary_doc_check.py`. No markdown reports in the parent tree. Both seats did file their real reports inside the lane (`V69-crosscheck-coverage-2.md` `23:07`, `V73-shonen-2.md` `23:06`). This is the warned parent-cwd miss (session cwd is `/home/vgpnk/Projects/shokunin`), seat-attributed, the r94 parent-stray class. r98's adjacency close called out zero seat-intentional strays. This round has two.

Sibling lanes, files newer than `2026-10-17 21:55`, excluding `.git`: every `*-shokunin` lane **0** except `kotodama-shokunin` **2050** and `lore-shokunin` **4578**. Kotodama's paths are its own `reports/round-15/` and `.scratch/r15o08/`. Lore-string scan:

```
$ grep -l -r "r99-window-lapse\|r99-gate-blind-spot\|clerk-lapse-note" /home/vgpnk/Projects/shokunin/kotodama-shokunin
(no paths)
```

No sibling domain source tree was written by this wave. I did not sweep `/tmp`; I do not claim a `/tmp` count.

Lane-internal, not a province breach, disclosed: `.ufo/waves/round-99/receipt.json` (wave top, `22:37`); `.ufo/waves/round-98/seats/V58-scratch/original-run-resume-note.md` (`22:32`, 4208 bytes) is a resumed r98 V58 seat recording that it did not overwrite the frozen r98 report. Not an r99 producer write.

**Result: FAIL.** Seat-intentional writes outside the lane. Charter and sibling source trees were not mutated.

---

## A4 — mythology editorial-only; rights/mechanics scan

Scan blob `V107-scratch/round-new-bytes.txt`, 116375 bytes: `git diff 4265df5` of the four owned tool/doc files, plus the two knowledge notes and all ten r99 fixture files. `23:11:21`.

```
$ grep -n -i -E "mechanic|gameplay|ruleset|damage|hit ?point|dice|combat|level.?up|public domain|fair use|free to (use|reuse)|may be (used|reproduced)|licensed under|permission is granted" round-new-bytes.txt
(no output)
$ grep -n -i -E "Spence|Kojiki|Chamberlain|Gutenberg|ETCSL|Inana|Ovid|Maya|Kiche|K'iche" corpus/fixtures/r99-window-lapse/*.json
(no output)
```

The two path hits are not sibling writes: the `../PROTOCOL.md` line is diff-hunk context (unchanged SKILL preamble; `git diff 4265df5 -- SKILL.md | grep -c '^@@'` → `1`, and the changed bullets do not add `../`); the `/home/vgpnk/Projects/shokunin/lore-shokunin` string is the blind-spot table's `verified-at` line naming the lane root. Spence remains two labeled editorial rows, not JSON facts (`claim-excerpt-map.md:44` "Editorial rows (2 bounded Spence comparisons; not JSON facts)"; `:46` "they do not make Spence an in-world witness, assign cultural meaning, or add canon"). The lapse note refuses resolution, blame, and reconciliation (`r99-lapse-scope-note.md:8`, `:12`).

**Result: PASS.**

---

## A5 — r99-specific adjacency

SKILL.md vs `4265df5` is one hunk, `3 3` in `--numstat`, only the `dependency_freeze` bullets (self-test 17→18 `markdown_tamper`; pinned-values path names schema 2 and the ten files; scope says prose-edit detectability, not dependency-semantics proof; `--freeze` still scope-guarded to `corpus/fixtures/**`). No other SKILL row changed. Tools README vs `4265df5` is `73 0` (append only).

Delivered contract (`python3` read of `dependency-freeze-contract.json` at freeze): `schema_version` 2, `payload_schema_version` 2, `pin_count` 6, each pin `files` length 10, `pinned_files` the declared ten names, every `fixture` value starts with `corpus/fixtures/`, `bad_fixture_paths []`. Chain fixture trees unmutated (§A2). `r99-window-lapse` is not a pin (S1 and the blind-spot table both say so); that is scope, not a stray pin.

**Result: PASS.**

---

## A6 — reports match the bytes

Artifact mtime precedes the owning report:

| Seat | artifact mtime | report mtime |
|---|---|---|
| S1 | contract `22:08:46`, tool `22:38:11` | `S1-full-file-pins.md` `22:48:57` |
| S2 | SKILL `22:51:39`, README `23:08:16` | `S2-tools-docs.md` `23:10:49` |
| S3 | JSON/excerpts `22:01:13` (archive copies `21:36:10`) | `S3-fixture-author.md` `22:01:40` |
| S4 | map `22:02:39`, README `22:03:19` | `S4-fixture-docs.md` `22:03:54` |
| S5 | both notes `22:57:50` | `S5-knowledge-author.md` `23:10:56` |

S2's report quotes the freeze hashes I measured: tool `fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c`, contract `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628`, README `837a7f5dfe913047530c7f92f3dd6b3df1b1a83c77ede12ba0c349cc134a049c`, SKILL `e0bcb61ab909146e34773dd56219cb1631070c1700a2481f8ad1181f3d864443`. Recheck `23:12:24` still those prefixes, plus notes `4670c0b71668` / `96de708f8e98` and timeline `2cdb9fda5baa`. `git reflog -1` still `337f0fa`. No seat commit.

S3's report claimed all ten fixture files; the declaration gives README and the map to S4. S4 replaced those two before its own report. Final mtimes put S4's bytes before S4's report and leave S3's three edited files before S3's report. Not a post-report rewrite.

**Result: PASS.**

---

## Bottom line

**FAIL — seat-intentional writes outside `lore-shokunin`: parent tree `/home/vgpnk/Projects/shokunin/.ufo/waves/round-99/` (8 files, V69-scratch + V73-scratch, 22:11–22:17, cwd-miss stderr and 0-byte copies); charter is byte-identical to `4265df5` and the in-lane change set is the declared S1–S5 ownership. V33's ABSENT (22:27, sha256 `61ba3ac0…`) was correct for its window and is not a scored disagreement.**
