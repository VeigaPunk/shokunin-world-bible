# V41 — anchor-replica-2 (round 99)

**Seat:** V41 `anchor-replica-2` (verifier). **Scope:** independent anchor re-verification, python method, of `corpus/fixtures/r99-window-lapse/claim-excerpt-map.md` — all 21 JSON-fact anchors in-span. **Baseline:** r98 closure `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`); working-tree HEAD at poll start was `337f0fa` (blocked-dispatch note only; r99 wave tree uncommitted). **Repo root:** `/home/vgpnk/Projects/shokunin/lore-shokunin`. **Scratch (exclusive):** `.ufo/waves/round-99/seats/V41-scratch/`. Leaf seat: no nested agents, no commits, no pushes, no network. Writes: this report and that scratch dir only.

Axes for this seat: completeness (all 21, not a sample), independence (own parser, not `support_check.py`), evidence (quoted commands and observed output), freshness (byte-stable delivered revision, never a plan). Kept: own parser plus a `grep -nF` cross-check and an r98 inheritance comparison. Not kept as a verdict input: project-tool receipts (not run).

## 0. Poll-wait evidence

Poller logic in the seat session, log `.ufo/waves/round-99/seats/V41-scratch/poll.log` (20 s cadence, 40 tries; requires all ten fixture files AND `S3-*.md` and `S4-*.md`, plus one consecutive identical md5 of those ten files). SELF subtracted: the poll waited only for S3/S4 reports, not for V41. No stall-escape.

```
POLL-START 22:01:36 max=40 cadence=20
try 1 22:01:36 missing: REPORT:S3 REPORT:S4 partial=aa8e08e6cd2548ce0f9480c187f83a04
try 2 22:01:56 missing: REPORT:S4 partial=aa8e08e6cd2548ce0f9480c187f83a04
try 3 22:02:16 missing: REPORT:S4
try 4 22:02:36 missing: REPORT:S4
try 5 22:02:56 missing: REPORT:S4 partial=4bc81920c0a70a3e7ed4b75ac04534c8
try 6 22:03:16 missing: REPORT:S4 partial=d6119567bb32021d1ef9dfb3f30e5e51
try 7 22:03:36 missing: REPORT:S4 partial=947b4b3d30cf9767b562ffbb65dbe651
try 8 22:03:56 PRESENT stable_window=0 md5set=947b4b3d30cf9767b562ffbb65dbe651
try 9 22:04:16 PRESENT stable_window=1 md5set=947b4b3d30cf9767b562ffbb65dbe651
READY-STABLE try=9 22:04:16 md5set=947b4b3d30cf9767b562ffbb65dbe651
```

Hazard recorded, not fatal: at try 1 the directory already existed, but `claim-excerpt-map.md` and `README.md` were still the r98 placeholder copies (S3's report says so; S4's report says the same). Tries 5–7 show the map hash moving while S4's report was still absent. Verification ran only after READY-STABLE, on the hash S4 declares.

## 1. Method and frozen revision

Checker `.ufo/waves/round-99/seats/V41-scratch/anchor_replica.py`: own markdown-table parser (no project-tool import). In-span means the fixed-string anchor occurs at least once in the referenced excerpt file and every occurrence's line is inside the declared span. JSON pointers are resolved only as a supplementary existence check (the node the pointer names exists); that is not entailment.

Parser calibration on the r98 fixture before trusting the r99 result (`V41-scratch/calibrate-r98.txt`):

```
$ python3 .ufo/waves/round-99/seats/V41-scratch/anchor_replica.py \
    --map corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md \
    --cluster corpus/fixtures/r98-clerk-filing --label r98-selfcal
== r98-selfcal: json=20 editorial=2 distinct=18 tables=3 ==
declared_inventory=(20, 2, 22, 18) parsed=(20, 2, 22, 18)
... 20 JSON rows + S01/S02, all IN-SPAN=True, ptr=OK ...
IN-SPAN 22/22
RESULT PASS failures=0 no-baseline
CAL_EXIT:0
```

Frozen revision (sha256, re-checked `sha256sum` after the r99 run and again at 22:09:12; unchanged):

| File | sha256 |
|---|---|
| `claim-excerpt-map.md` | `d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d` |
| `fictional-excerpts.md` | `fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d` |
| `source-excerpt.md` | `b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd` |

S4's report declares the same map hash (`d2fe20e5…`, 17119 bytes) and README hash `b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049` (6176 bytes). Both reproduced. Map mtime stayed `2026-10-17 22:02:39`; excerpt mtime stayed `22:01:13`. `source-excerpt.md` is sha-identical to r98.

## 2. Result — checker output (verbatim, `V41-scratch/verify-r99.txt`)

Command (lane root, 22:05:04):

```
$ python3 .ufo/waves/round-99/seats/V41-scratch/anchor_replica.py \
    --map corpus/fixtures/r99-window-lapse/claim-excerpt-map.md \
    --cluster corpus/fixtures/r99-window-lapse \
    --baseline-map corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md \
    --baseline-cluster corpus/fixtures/r98-clerk-filing \
    --label r99-vs-r98
== r99-vs-r98: json=21 editorial=2 distinct=19 tables=3 ==
declared_inventory=(21, 2, 23, 19) parsed=(21, 2, 23, 19)
J01 mapline=22 span=12 py=[12] inside=[12] outside=- IN-SPAN=True mode=verbatim ptr=OK
J02 mapline=23 span=13 py=[13] inside=[13] outside=- IN-SPAN=True mode=verbatim ptr=OK
J03 mapline=24 span=12 py=[12] inside=[12] outside=- IN-SPAN=True mode=verbatim ptr=OK
J04 mapline=25 span=13 py=[13] inside=[13] outside=- IN-SPAN=True mode=verbatim ptr=OK
J05 mapline=26 span=17 py=[17] inside=[17] outside=- IN-SPAN=True mode=verbatim ptr=OK
J06 mapline=27 span=12 py=[12] inside=[12] outside=- IN-SPAN=True mode=verbatim ptr=OK
J07 mapline=28 span=13 py=[13] inside=[13] outside=- IN-SPAN=True mode=verbatim ptr=OK
J08 mapline=29 span=12 py=[12] inside=[12] outside=- IN-SPAN=True mode=verbatim ptr=OK
J09 mapline=30 span=13 py=[13] inside=[13] outside=- IN-SPAN=True mode=verbatim ptr=OK
J10 mapline=31 span=18 py=[18] inside=[18] outside=- IN-SPAN=True mode=verbatim ptr=OK
J11 mapline=32 span=19 py=[19] inside=[19] outside=- IN-SPAN=True mode=verbatim ptr=OK
J12 mapline=33 span=12 py=[12] inside=[12] outside=- IN-SPAN=True mode=verbatim ptr=OK
J13 mapline=34 span=13 py=[13] inside=[13] outside=- IN-SPAN=True mode=verbatim ptr=OK
J14 mapline=35 span=18-20 py=[20] inside=[20] outside=- IN-SPAN=True mode=verbatim ptr=OK
J15 mapline=36 span=22-31 py=[26] inside=[26] outside=- IN-SPAN=True mode=verbatim ptr=OK
J16 mapline=37 span=33-42 py=[37] inside=[37] outside=- IN-SPAN=True mode=verbatim ptr=OK
J17 mapline=38 span=44-53 py=[48] inside=[48] outside=- IN-SPAN=True mode=verbatim ptr=OK
J18 mapline=39 span=60 py=[60] inside=[60] outside=- IN-SPAN=True mode=verbatim ptr=OK
J19 mapline=40 span=59-60 py=[59] inside=[59] outside=- IN-SPAN=True mode=verbatim ptr=OK
J20 mapline=41 span=55-64 py=[59] inside=[59] outside=- IN-SPAN=True mode=verbatim ptr=OK
J21 mapline=42 span=66-76 py=[70] inside=[70] outside=- IN-SPAN=True mode=verbatim ptr=OK
S01 mapline=50 span=5 py=[5] inside=[5] outside=- IN-SPAN=True mode=verbatim
S02 mapline=51 span=5 py=[5] inside=[5] outside=- IN-SPAN=True mode=verbatim
inherited_ok=20/20 new=['J21'] dropped=[]
excerpt_byte_prefix=True base_len=4187 new_len=5114
J21 appended-only=True base_lines=64 hits=[70]
IN-SPAN 23/23
RESULT PASS failures=0 inherited_ok=20 mismatches=0 new=['J21']
EXIT:0
```

**All 21 JSON-fact anchors are in-span.** Each has exactly one occurrence, that occurrence is inside the declared span, and there are zero outside-span occurrences. Declared inventory `(21, 2, 23, 19)` equals parsed. Editorial S01/S02 are also in-span at `source-excerpt.md:5` (not part of the 21).

`grep -nF` cross-check (`V41-scratch/grep-cross.txt`) agrees with the python hit list on all 23 rows (`py_grep_mismatch []`). J21:

```
70:> Tick 15: The crossing-window named in the original minute has closed.
```

inside declared span 66-76, and past r98's 64-line excerpt.

## 3. Inheritance and the new row

Cell diff of the 20 shared JSON rows (`V41-scratch/cell-diff.txt`): 20 cell diffs, all in the path-qualification column, and each is exactly the string substitution `r98-clerk-filing` → `r99-window-lapse` (`namespace_swap_exact True`, checked 20, bad `[]`). Pointer, source id, excerpt path, span, mode, and anchor cells are byte-identical. Resolved hit-line sets are identical (checker `inherited_ok=20/20`). No dropped r98 ids. J21 is the only new id, map line 42:

```
| J21 | `timeline.json#/7` (`tick`, `entity_id`, `place_id`, `depends_on`, `description`, `source_id`) | `clerk-lapse-note` | `r99-window-lapse:clerk-lapse-note` | `fictional-excerpts.md` | 66-76 | `verbatim` | `Tick 15: The crossing-window named in the original minute has closed.` |
```

`fictional-excerpts.md` is a byte prefix of the r98 file (4187 bytes) plus a leading newline and 927 new bytes. The new section (lines 66-76) is the only place the J21 anchor occurs.

Supplementary pointer resolution (not the in-span verdict): `timeline.json` length 8; index 7 is `id=clerk-lapse-recorded`, `tick=15`, `entity_id=clerk-maren`, `place_id=chalk-stair`, `depends_on=['clerk-filing-open']`, `source_id=clerk-lapse-note`. That matches the declaration's event shape. This seat did not judge whether the description entails the prose, and did not run `support_check.py` or `map_obligations.py`.

## 4. Bounds

- Lexical in-span only. No entailment, canon, rights, authenticity, or census claim. Census 172→173 and C1 freeze pinning were not measured here.
- S3's report still says README and the map are r98 placeholders. That was true at S3's write time (22:01) and is stale for the revision verified here: S4 rewrote both, and the verified map hash equals S4's declared hash.
- The verified bytes are the READY-STABLE revision re-hashed at 22:09:12. A later edit of the map or excerpts invalidates this receipt for the changed bytes only.

**Bottom line: PASS** — all 21 r99 JSON-fact anchors independently re-verified in-span (python method, `grep -nF` cross-checked) on frozen map `d2fe20e5…` / excerpts `fefebaf9…`; 20 inherited rows namespace-only versus r98 with identical hit lines; J21 hits only at line 70 inside span 66-76, past the preserved r98 prefix.
