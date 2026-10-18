# V113 c2-support-inventory-line

Seat: V113. Lane root: `/home/vgpnk/Projects/shokunin/lore-shokunin`. Leaf seat. No commits, no pushes, no network, no nested agents. Exclusive writes: this report and `.ufo/waves/round-99/seats/V113-scratch/`. Live corpus bytes were not written.

Axes: (1) presence of the delivered r99 map and S4 report before any check; (2) honest inventory assertion on that map; (3) a falsified inventory line fails closed on a scratch copy; (4) isolation (only the declaration line changes; live map unchanged); (5) evidence fidelity (commands and outputs quoted).

## Poll-wait

Cadence 20s. Did not verify the pre-S4 placeholder.

```
poll-start 2026-10-17T22:02:09-03:00
try=1 time=22:02:09 map_bytes=15028 j21=0 s4=ABSENT
  inv=5:**Expected inventory:** 20 JSON facts; 2 editorial rows; 22 total mapped rows; 18 distinct excerpt anchors.
try=2 time=22:02:29 map_bytes=15028 j21=0 s4=ABSENT
try=3 time=22:02:49 map_bytes=15028 j21=0 s4=ABSENT
try=4 time=22:03:09 map_bytes=17119 j21=1 s4=ABSENT
  inv=5:**Expected inventory:** 21 JSON facts; 2 editorial rows; 23 total mapped rows; 19 distinct excerpt anchors.
try=5 time=22:03:29 map_bytes=17119 j21=1 s4=ABSENT
try=6 time=22:03:49 map_bytes=17119 j21=1 s4=ABSENT
try=7 time=22:04:09 map_bytes=17119 j21=1 s4=.../seats/S4-fixture-docs.md
READY
poll-end 2026-10-17T22:04:09-03:00
```

S3 report `S3-fixture-author.md` was already present (5069 bytes, 22:01). S4 report landed at try 7 (`S4-fixture-docs.md`, 9303 bytes, 22:03). No stall-escape. This seat did not run an all-reports poll, so subtract-SELF does not apply.

S4's delivered map pin, reproduced here before and after the demo: sha256 `d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d`, 17119 bytes. Line 5 of the delivered map:

```
**Expected inventory:** 21 JSON facts; 2 editorial rows; 23 total mapped rows; 19 distinct excerpt anchors.
```

Tool under test, unchanged across the demo: `corpus/tools/support_check.py` sha256 `55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c`, 17006 bytes. Python `3.14.7`. Commands from the lane root.

Documented contract (`corpus/tools/README.md` lines 10 and 22, read at 22:11): parsed category counts, total rows, and distinct `(excerpt path, anchor)` pairs are checked against the one inventory line; inventory mismatches exit non-zero; `RESULT FAIL` is exit 1.

## Honest assertion (delivered map)

```
$ python3 corpus/tools/support_check.py corpus/fixtures/r99-window-lapse
exit 0
stderr (empty)
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23; DISTINCT-ANCHORS 19/19
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
PASS J01 … PASS J21
PASS S01; PASS S02
RECEIPT JSON-FACTS 21; EDITORIAL-ROWS 2; TOTAL-ROWS 23
SOURCE-SUPPORT 21/21; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 23/23; VALIDATED-ROWS 23/23
RESULT PASS
```

J21's printed hit was `70:> Tick 15: The crossing-window named in the original minute has closed.` Full stdout: `.ufo/waves/round-99/seats/V113-scratch/live.stdout`. This matches S4's reported receipt (21/21, exit 0) on the same sha256.

Scratch control copy of the whole fixture, map byte-identical to live (`filecmp` True, same sha256), same command against the copy: exit 0, same `INVENTORY` line, `RESULT PASS`, stderr empty. The copy itself does not cause a failure.

## Falsified inventory line (scratch copies only)

Each case is `shutil.copytree` of `corpus/fixtures/r99-window-lapse` into `V113-scratch/copies/<name>/`, then a single replacement of the honest inventory line, then:

```
python3 corpus/tools/support_check.py <scratch-copy>
```

`diff -u` of control vs each mutated map is one line (the inventory declaration). Scope prose still says "21 source-attributed JSON obligations"; the checker does not read that sentence. Full stdout/stderr saved as `V113-scratch/<name>.stdout` and `<name>.stderr`.

### undercount — r98 counts on the r99 rows (arithmetically consistent lie)

Declaration replaced with `20 JSON facts; 2 editorial rows; 22 total mapped rows; 18 distinct excerpt anchors.` Map sha256 `cc08f01988fb9ac2fba73bfaca6f4a8405c1eb25e4076c0952ee0ec1c22b0741`, still 17119 bytes.

```
exit 1
stderr (empty)
INVENTORY JSON-FACTS 21/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/22; DISTINCT-ANCHORS 19/18
SOURCE-SUPPORT 21/21; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 23/23; VALIDATED-ROWS 23/23
FAIL: inventory JSON facts mismatch: expected=20 parsed=21
FAIL: inventory total mapped rows mismatch: expected=22 parsed=23
FAIL: inventory distinct excerpt anchors mismatch: expected=18 parsed=19
RESULT FAIL
```

Gate did not open. Editorial count 2/2 was not a false failure.

### anchor-only — one field, sum still holds

Declaration: `21 JSON facts; 2 editorial rows; 23 total mapped rows; 18 distinct excerpt anchors.` sha256 `1732d1f6c39ebd8d7f24bcc8269a29a07694d966a4efada0d879790e1fe5b11e`.

```
exit 1
stderr (empty)
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23; DISTINCT-ANCHORS 19/18
FAIL: inventory distinct excerpt anchors mismatch: expected=18 parsed=19
RESULT FAIL
```

### overcount — the other direction

Declaration: `22 JSON facts; 2 editorial rows; 24 total mapped rows; 20 distinct excerpt anchors.` sha256 `0f0cafed4b5ad5d7f0d9835d550ab249e1df217ca52a85c825febddcd1472670`.

```
exit 1
stderr (empty)
INVENTORY JSON-FACTS 21/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/24; DISTINCT-ANCHORS 19/20
FAIL: inventory JSON facts mismatch: expected=22 parsed=21
FAIL: inventory total mapped rows mismatch: expected=24 parsed=23
FAIL: inventory distinct excerpt anchors mismatch: expected=20 parsed=19
RESULT FAIL
```

### sum-break — declaration does not add (21+2 != 22)

```
exit 1
stdout:
RESULT FAIL
stderr:
FAIL: expected JSON facts and editorial rows must sum to total mapped rows
```

No `INVENTORY` receipt and no row lines. `InventoryError` is raised in `parse_map` before `run` prints receipts (`support_check.py` lines 137-138, caught at 409-412 as exit 1 / `RESULT FAIL`, not exit 2).

### malformed token

Line starts with `**Expected inventory:**` but the first count is `twenty-one`.

```
exit 1
stdout: RESULT FAIL
stderr: FAIL: expected inventory declaration is malformed
```

### missing line

The inventory line deleted. No `Expected inventory` line remains.

```
exit 1
stdout: RESULT FAIL
stderr: FAIL: map must contain exactly one expected inventory declaration
```

## Isolation

```
live_map_before d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d  17119
live_map_after  d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d  17119
tool_sha_after  55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  17006
control_map_identical_to_live True
```

`git status --short -- corpus/fixtures/r99-window-lapse/claim-excerpt-map.md corpus/tools/support_check.py` showed only `?? corpus/fixtures/r99-window-lapse/claim-excerpt-map.md` (producer-untracked fixture file, sha256 still S4's pin). This seat did not edit it.

## Bounds (observed, not hidden)

- Count-mismatch cases do not abort before row receipts. Per-row lines still say `PASS`, and `SOURCE-SUPPORT 21/21` / `VALIDATED-ROWS 23/23` still print, then the `FAIL:` inventory lines and `RESULT FAIL`, exit 1. Fail-closed here is the process contract (non-zero exit, final `RESULT FAIL`, named mismatch), not suppression of those row lines. A consumer that greps only `^PASS ` would miss it. A consumer that checks the exit code or the `RESULT` line does not.
- Arithmetic, malformed, and missing declarations fail earlier: stdout is only `RESULT FAIL`; the reason is on stderr. Still exit 1, not exit 2. README line 22 assigns inventory failures to exit 1; that is what was observed.
- The checker does not compare the scope sentence ("21 source-attributed JSON obligations") to the inventory line. A prose/inventory disagreement with a still-accurate inventory line was not the case under test.
- Distinct anchors are `(excerpt path, anchor)` pairs. Delivered run reported `repeated-references=4` and `DISTINCT-ANCHORS 19/19` on 23 rows (23 − 4 = 19). Not re-derived row by row beyond that receipt.

## Bottom line

PASS — on the delivered r99 map (`d2fe20e5…`, inventory 21/2/23/19) `support_check.py` asserts the declaration against parsed counts and exits 0 `RESULT PASS`; a scratch copy whose only change is a falsified inventory line fails closed (exit 1, `RESULT FAIL`, mismatch or malformed/missing declaration named) in both undercount and overcount, on a single-field anchor lie, and on a sum that does not add.
