# V28 — verdict-calibration (round 99, single-wave swarm)

**Seat:** V28 verdict-calibration — read the C1 seats; own the demos (markdown tamper + before/after); one CALIBRATION verdict with bounds.

**Repo root for every command:** `/home/vgpnk/Projects/shokunin/lore-shokunin` (session cwd is the parent repo; every write used an absolute path under the lane and was resolved before writing). **Baseline:** r98 closure `4265df5`. HEAD at poll start `337f0fa` (blocked-dispatch LOG-only commit; tool/contract bytes equal `4265df5`).

**Frozen revision under test** (copied to `V28-scratch/frozen-r99/` at 2026-10-17T22:59:00-03:00, after S1's report existed; every delivered-revision run used these copies):

```
fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c  dependency_freeze.py
8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628  dependency-freeze-contract.json
```

Baseline copies (`git show 4265df5`): tool `03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b`, contract `153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947`. Live tool/contract re-checked at 23:07:20 — still equal to the frozen copies.

---

## 1. Poll-wait, then a recorded stall-escape

Condition: tool hash ≠ baseline AND contract hash ≠ baseline AND `seats/S1-*.md` AND `seats/S2-*.md`. Cadence 20 s, max 40. Log: `.ufo/waves/round-99/seats/V28-scratch/poll.log`.

Tries 1–15 ran in one background shell that the tool host killed at its 300 s cap (recorded stall, not protocol exhaustion). Resume continued the count at try 16.

```
POLL-START 22:02:04
try 1  22:02:04 tool=65c1ae309385 contract=153ebc5b2092 s1=ABSENT s2=ABSENT missing: CONTRACT-UNCHANGED REPORT:S1 REPORT:S2
try 8  22:04:25 tool=1728ed892442 contract=73b28933f148 s1=ABSENT s2=ABSENT missing: REPORT:S1 REPORT:S2
try 15 22:06:45 tool=1728ed892442 contract=8f9c1f531614 s1=ABSENT s2=ABSENT missing: REPORT:S1 REPORT:S2
POLL-RESUME 22:11:39 after tool-timeout at try 15
try 16 22:11:39 tool=6f81f8be1974 contract=8c2561b043c2 pins=10 s1=ABSENT s2=ABSENT missing: REPORT:S1 REPORT:S2
try 40 22:19:39 tool=6f81f8be1974 contract=8c2561b043c2 pins=10 s1=ABSENT s2=ABSENT missing: REPORT:S1 REPORT:S2
POLL-EXHAUSTED 22:19:59
```

`s1=ABSENT` and `s2=ABSENT` on all 40 tries. Post-checks at 22:22:24, 22:35:24, and 22:48:54 still had zero `S1*.md` / `S2*.md`. An interim report filed ABSENT at 22:50:40. That text is superseded by this file.

**Stall-escape (recorded, not silent):** `S1-full-file-pins.md` appeared at mtime 22:48:57 (11971 B), detected on the next presence check at 22:53. S1 was then read in full. The tool hash had already moved from the poll-stable `6f81f8be1974` to `fb9bb9ff608c` (mtime 22:38:11) before that report; the contract stayed `8c2561b043c2`. Demos below ran only after the report existed, on frozen copies of that post-report pair. The intermediate `6f81f8be` tool was not verified. `S2-*.md` was still absent at 23:10:12. No all-reports poll, so SELF-subtraction does not apply.

## 2. C1 seat cross-read

**S1 (`S1-full-file-pins.md`)** reports PASS: payload schema 2, ten-file pins, chain 6/6, self-test 18/18, `DIGEST-MISMATCH` names `fictional-excerpts.md`, and explicitly contradicts the declaration's "invisible to every gate" for the anchored sentence (support_check J14 exit 1 before). My independent runs agree on every point I re-derived, including the exact digest and per-file sha transitions S1 quoted for the r94 wording replacement (`68ae0332…`, `585f4d07… -> 6b67dcda…`) and the non-anchor heading edit (`f559baaa…`, `585f4d07… -> 1deff015…`). Those were produced on my own scratch copies, not by replaying S1's trees.

**S2 (`S2-tools-docs.md`)** was absent through the 23:10:12 check and landed at mtime 23:10:49 (11040 B). Read in full after the demos. S2 also records a stall-escape (docs written before S1's report, then reconciled). It agrees with the runs below: schema 2, ten-file pins, self-test 18/18, the six digests, edit-detectable not semantics-provable, support_check J14 on the anchored removal, r88 `symbolism-clause-map.md` unpinned. No contradiction.

README/SKILL were still the r98 hashes (`294dd56f29ce…` / `22ffaa822ec7…`) through try 40. Freeze snapshot at 22:59:00 was README `646784ae…`, SKILL `e0bcb61a…`. Live README at 23:11:15 is S2's quoted `837a7f5dfe913047530c7f92f3dd6b3df1b1a83c77ede12ba0c349cc134a049c` (mtime 23:08:16). Diff against the freeze snapshot is only the J14 paragraph (support_check exit 1, map and check_bible exit 0). SKILL stayed `e0bcb61ab909146e34773dd56219cb1631070c1700a2481f8ad1181f3d864443`. Tool and contract hashes were unchanged by that doc edit.

## 3. Before (baseline tool `03d04365…`, not the live file)

Control, baseline tool, live `r98-clerk-filing` via a symlink root:

```
$ python3 V28-scratch/before/root/corpus/tools/dependency_freeze.py \
    V28-scratch/before/root/corpus/fixtures/r98-clerk-filing
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
DIGEST 59a0f4fa3d4a47e03649a54d1815c45ee1eef641b63a59ebe7210bc9d9b9b133
RESULT PASS
EXIT=0
```

Dependency sentence deleted (142 chars, count 1) from a scratch copy of `r98-clerk-filing/fictional-excerpts.md`: same receipt, same digest `59a0f4fa…`, `RESULT PASS`, exit 0. Same deletion on a scratch `r94-paired-crossing`: digest `2527beb9…`, `RESULT PASS`, exit 0. The r98 freeze gate does not see that prose edit.

Same r98 scratch copy, other gates: `check_bible` exit 0 CLEAN; `map_obligations` exit 0 `RESULT PASS`; `support_check` exit 1 `FAIL J14: source-support; mode=verbatim; anchor=not-found` / `RESULT FAIL`. Untampered live r98 `support_check` was exit 0. So the mapped verbatim sentence is already visible to `support_check` and invisible to the other three.

**Non-anchor before** (the class that is invisible to every gate). Scratch r94, baseline tool+contract, heading `# Authored in-world excerpts` extended with ` (dependency wording left intact)`:

```
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
DIGEST 2527beb938b474a28d66e1c716f54ba829ae3cc2e616513cd2960a8f7ecebe75
RESULT PASS
EXIT=0
```

`support_check` exit 0 `SOURCE-SUPPORT 14/14` `RESULT PASS`; `map_obligations` exit 0 `RESULT PASS`; `check_bible` exit 0 CLEAN.

## 4. After (frozen delivered tool+contract, own scratch copies)

Chain verify, six fixture copies under a mirror root so the pin path binds. Each exit 0 `RESULT PASS`. Digests equal S1's and the frozen contract:

| fixture | digest | receipt |
|---|---|---|
| r88-m3-maya-cluster | `acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae` | events 2/2 edges 0/0 relations 0/0 |
| r94-paired-crossing | `048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef` | 3/3, 2/2, 1/1 |
| r95-crossing-aftermath | `97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710` | 4/4, 3/3, 1/1 |
| r96-crossing-response | `43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c` | 5/5, 4/4, 1/1 |
| r97-crossing-acknowledgment | `a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54` | 6/6, 5/5, 1/1 |
| r98-clerk-filing | `5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0` | 7/7, 6/6, 1/1 |

Against the baseline contract, all six pins: five JSON file digests identical, `events` / `relations` / `counts` identical. Added: `payload_schema_version` 2, `pinned_files` equal to the ten declared names, five Markdown digests, new content digest. Root `schema_version` 1→2, root `payload_schema_version` 2, root and every pin `revision` `337f0fa52b02626b7687eedbb2d99fab30446fe4`. `r99-window-lapse` is not a pin. Contract `data_files` is still the five JSON names; the ten-file set is `pinned_files` plus each pin's `files`.

Self-test expectation set 17→18, added `['markdown_tamper']`, removed `[]`, inherited objects changed `[]`. Persisted case: `{"exit": 2, "finding_ids": ["DIGEST-MISMATCH"], "forbid_traceback": true, "names_file": "fictional-excerpts.md"}`.

```
$ python3 <frozen-root>/corpus/tools/dependency_freeze.py --self-test
CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
SELF-TEST 18/18
RESULT PASS
EXIT=0
```

The other 17 rows were `ok` with the inherited exits and finding IDs. Harness: `V28-scratch/demos.py`.

**Wording replacement** (S1's mutation, my copy): r94 sentence `depends on both` → `follows both`. Confirmed `depends on both ninth-bell` absent.

```
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
FINDING DIGEST-MISMATCH: content digest 68ae0332a911e4d1cef8b93c18aab567b19ebc656f23ad6089b95810b1882f76 != pin 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef; changed: fictional-excerpts.md (sha256 585f4d0746eadffcdd13a12aa4068392820201ae668dc9b66e9154beccf495c2 -> 6b67dcdaef2e4048bc466bd1e00a154c627883471415dd40635fbceb66b999b0); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
EXIT=2
```

Same copy: `support_check` exit 1 `FAIL: J14: source-support anchor missing`; `map_obligations` exit 0; `check_bible` exit 0 CLEAN.

**Non-anchor after** (same heading edit as §3):

```
FINDING DIGEST-MISMATCH: content digest f559baaa7e6facbefb8a65f6be4eb4b5feb622c233e18bd4ace5ba03c332a034 != pin 048b8ff3…; changed: fictional-excerpts.md (sha256 585f4d07… -> 1deff0153f063b504cb4e2414c1d6bfd5d9c889c8a1c92fbf279c41d7f18be33); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
EXIT=2
```

`support_check` / `map_obligations` / `check_bible` all still exit 0. This is the before/after that was green on every gate and is now named.

**Any of the five Markdown files, trailing newline, r98 copy, each exit 2 naming only that file:** `README.md`, `claim-excerpt-map.md`, `fictional-excerpts.md`, `inspiration-note.md`, `source-excerpt.md`. **entities.json trailing newline** also exit 2 naming `entities.json` (`026af0bc… -> 3489f303…`). **Delete `fictional-excerpts.md`:** exit 2, `changed: fictional-excerpts.md (sha256 29e384bf… -> None)`.

**Semantic findings still decide first.** r94 copy, drop `evin-ninth-bell` from `paired-crossing-decision.depends_on` and append a newline to `README.md`:

```
FREEZE r94-paired-crossing: events 3/3; dependency-edges 1/2; relations 1/1
FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']
RESULT FAIL
EXIT=1
```

No `DIGEST-MISMATCH` on that path.

**Outside the ten.** Newline appended to `r88-m3-maya-cluster/symbolism-clause-map.md`: `RESULT PASS` exit 0, digest still `acf677a7…`.

`--freeze` was not re-run. It rewrites the delivered contract.

## 5. Calibration verdict (with bounds)

**C1 verdict: calibration improved (bounded).** On the frozen post-report revision, independently of S1's trees: a non-anchor prose edit that was `RESULT PASS` exit 0 on the r98 freeze gate and exit 0 on `support_check`, `map_obligations`, and `check_bible` is now exit 2 `DIGEST-MISMATCH` naming `fictional-excerpts.md`. A mapped dependency-wording replacement is likewise named. Each of the five Markdown files and `entities.json` names itself; a deleted pinned file is named with `-> None`. Chain 6/6, inherited JSON digests and inventories identical, self-test 17→18 with `markdown_tamper` ok, semantic exit 1 still wins over a concurrent Markdown byte change.

Bounds (named, not netted):

1. **Stall-escape.** The 40-try poll ended with both C1 reports absent. This verdict exists only because S1's report landed afterward and the demos were then run on frozen copies. The poll-stable tool `6f81f8be1974` was not the revision tested (`fb9bb9ff608c` is).
2. **Edit-detectable, not semantics-provable.** The gate reports a byte change. It does not judge whether the remaining prose still states the dependency. Replacing `depends on` with `follows` is a digest change, not a semantic proof.
3. **The declaration's "invisible to every gate" is false for the mapped verbatim sentence.** On the r98 tool that sentence removal is already `support_check` exit 1 `FAIL J14`. It is invisible to r98 `dependency_freeze`, `map_obligations`, and `check_bible`. The class that was green on all four gates before, and named after, is the non-anchor edit (§3 vs §4).
4. **The pin set is the declared ten, not every file in the fixture.** `symbolism-clause-map.md` on r88 can change and still verify clean.
5. **Semantic inventory still decides first.** An edge drop plus a Markdown newline exits 1 `REDUCTION-DETECTED`, not 2.
6. **Self-test binds consistency, not truth.** Case 18 pins exit 2, finding `DIGEST-MISMATCH`, and `names_file: fictional-excerpts.md` for a newline append. A tool and contract edited together would stay green. This seat did not single-side-falsify that expectation.
7. **`data_files` is still the five JSON names.** The ten-file payload is `pinned_files` and each pin's `files`, not that list.
8. **`r99-window-lapse` is unpinned.** C1's chain is the existing six.
9. **S2 landed after this verdict was drafted.** Absent through the 23:10:12 check; `S2-tools-docs.md` mtime 23:10:49 was then read in full. It agrees: schema 2, ten files, 18/18, the six digests, edit-detectable not semantics-provable, support_check J14 on the anchored removal, r88 extra file unpinned. No contradiction with these runs. README hash moved after the freeze snapshot (`646784ae…` at 22:59) to S2's quoted `837a7f5d…` (mtime 23:08:16); the only diff is the J14 paragraph already measured here. SKILL stayed `e0bcb61a…`.
10. **Pin `revision` is HEAD `337f0fa`**, the blocked-dispatch commit, not a new work commit. Expected while the wave tree is uncommitted.

## 6. Hygiene

Writes confined to `V28-scratch/` (baseline copies, before mirrors, `frozen-r99/`, `demos.py`, `poll.log`) and this report. Producer files were not edited. No `--freeze` against the delivered contract. No commits, no pushes, no network, no nested agents. Report path resolved before the replacement write: `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V28-verdict-calibration.md`.

**Bottom line: PASS — calibration improved (bounded): non-anchor prose edit verified invisible to all four gates before (freeze digest `2527beb9…` exit 0) and exit 2 `DIGEST-MISMATCH` naming `fictional-excerpts.md` after; chain 6/6 with inherited JSON digests and inventories identical; self-test 18/18 including `markdown_tamper`; semantic exit 1 still wins; bounds recorded (late S1 and S2 landings after the 40-try poll, not semantics-provable, anchored sentence already support_check-visible, r88 extra file unpinned, `data_files` still five, r99 unpinned, pin revision `337f0fa`).**
