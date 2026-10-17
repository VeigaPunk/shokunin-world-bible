# R4 fixture-author — round 97 seat report

- Seat: R4 (producer, exclusive byte-ownership). Lane repo: `/home/vgpnk/Projects/shokunin/lore-shokunin`; baseline `f3e09f9`; all commands run from the lane repo root with `python3`.
- Owned paths written: `corpus/fixtures/r96-crossing-response/claim-excerpt-map.md` (cosmetic repair only) and `corpus/fixtures/r97-crossing-acknowledgment/**` (10 files; 5 data files + `sources.json` + `timeline.json` + `fictional-excerpts.md` are mine, `README.md` + `claim-excerpt-map.md` were created as byte-copy base for R5, who has since extended both).
- Scratch (mine): `.ufo/waves/round-97/seats/R4-scratch/`. No commits, no pushes, no network, no writes outside the above.

## C3-repair half — r96 cosmetic repair (DELIVERED)

Blemishes confirmed by inspection before the edit:

```
$ sed -n 43,44p corpus/fixtures/r96-crossing-response/claim-excerpt-map.md | cat -A | cut -c1-120
| ID | Bounded editorial comparison | Source citation | Excerpt path | Line span | R9 delivery mode | Exact anchor |$
|---|---|---|---|---|---:|---|---|$
$ sed -n 43p ... | awk -F'|' '{print NF-2" cells"}'   -> header: 7 cells
$ sed -n 44p ... | awk -F'|' '{print NF-2" cells"}'   -> 8 cells
$ sed -n 45p ... | awk -F'|' '{print NF-2" cells"}'   -> row: 7 cells
$ grep -c "new relation" corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
1
```

Two edits applied (`Edit` tool, surgical): the editorial delimiter row now carries 7 cells matching its header/rows; the line-50 stale sentence "The new relation encodes only the agreement for this crossing, not perpetual performance or alliance." became "The new tick-12 event encodes only Evin's second account of the same crossing occasion; it asserts no reconciliation, selects no winner between the accounts, and adds no duty beyond this crossing, not perpetual performance or alliance."

Change scope proof (only the two intended lines moved; every data row, pointer, anchor, span and mode byte-unchanged):

```
$ git diff -U0 -- corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
@@ -44 +44 @@
-|---|---|---|---|---|---:|---|---|
+|---|---|---|---|---:|---|---|
@@ -50 +50 @@
-The inherited tick-9 entries ... The new relation encodes only the agreement for this crossing, not perpetual performance or alliance.
+The inherited tick-9 entries ... The new tick-12 event encodes only Evin's second account of the same crossing occasion; it asserts no reconciliation, selects no winner between the accounts, and adds no duty beyond this crossing, not perpetual performance or alliance.
$ git diff --numstat -- corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
2	2	corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
$ grep -c "new relation" corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
0
```

Post-repair blemish re-check: editorial delimiter `NF-2` = 7 cells; no `new relation` occurrence.

Map sha256: before `5093d72eb3f22b249033d7ac4c1a85c7df7f5e09bfa673a598aee6a83045bfd8` → after `e851f068cfd7ed02c97054df18729c4c5a9b8bf60d99d7c9116f427d765440de`.

### Receipts unchanged by the repair

Before-repair (tool revision then in tree = frozen `2b0ba815…` for `map_obligations.py`, `55a5eb27…` for `support_check.py`):

```
$ python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response ; echo EXIT=$?
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18; DISTINCT-ANCHORS 14/14
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
... 18 PASS rows ...
RECEIPT JSON-FACTS 16; EDITORIAL-ROWS 2; TOTAL-ROWS 18
SOURCE-SUPPORT 16/16; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 18/18; VALIDATED-ROWS 18/18
RESULT PASS
EXIT=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response ; echo EXIT=$?
OBLIGATIONS raw=16 mapped=16
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18
RESULT PASS
EXIT=0
```

After-repair, both commands re-run and diffed against the saved before-output:

```
$ diff .ufo/waves/round-97/seats/R4-scratch/r96-support-before.txt .ufo/.../r96-support-after.txt
support receipts IDENTICAL          (diff empty; exit 0 both sides)
$ diff .ufo/waves/round-97/seats/R4-scratch/r96-map-ob-before.txt .ufo/.../r96-map-ob-after.txt
map_obligations receipts IDENTICAL  (diff empty; exit 0 both sides)
```

Independent frozen-baseline proof (not dependent on the tool revisions in the tree, which were moving under me): I wrote the pre-repair map bytes from `git show f3e09f9:…` into a scratch fixture copy and ran the `f3e09f9` tool versions against both the pre-repair copy and the delivered post-repair fixture:

```
$ git show f3e09f9:corpus/tools/{map_obligations,support_check}.py > .ufo/.../R4-scratch/*_frozen.py
$ python3 .../map_obligations_frozen.py .ufo/.../r96-prerepair        -> RESULT PASS exit 0
$ python3 .../map_obligations_frozen.py corpus/fixtures/r96-crossing-response -> RESULT PASS exit 0
$ diff pre-frozen-mapob.txt post-frozen-mapob.txt   -> identical
$ python3 .../support_check_frozen.py .ufo/.../r96-prerepair         -> RESULT PASS exit 0
$ python3 .../support_check_frozen.py corpus/fixtures/r96-crossing-response -> RESULT PASS exit 0
$ diff pre-frozen-support.txt post-frozen-support.txt -> identical
```

Also re-run under an interim R1 revision of `map_obligations.py` (`c1881149…`): `diff r96-map-ob-before.txt r96-mapob-r1tool.txt` → identical. The frozen and revised tools agree that the cosmetic repair does not move the r96 receipt.

## C3-depth half — `corpus/fixtures/r97-crossing-acknowledgment/` (DELIVERED)

Base: 10 files. Nine taken from `git show f3e09f9:corpus/fixtures/r96-crossing-response/<file>` and byte-verified; the map taken from the post-repair working tree:

```
IDENTICAL contradictions.json / entities.json / fictional-excerpts.md / inspiration-note.md /
          relations.json / source-excerpt.md / sources.json / timeline.json / README.md   (cmp vs f3e09f9)
IDENTICAL claim-excerpt-map.md (post-repair)   (cmp vs corpus/fixtures/r96-crossing-response/claim-excerpt-map.md)
```

Authored rows (only appends; inherited values untouched):

```
sources.json:  r96 len=5 r97 len=6  inherited-prefix-identical=True   (also True vs frozen f3e09f9 bytes)
timeline.json: r96 len=5 r97 len=6  inherited-prefix-identical=True   (also True vs frozen f3e09f9 bytes)
entities.json 5=5 / relations.json 1=1 / contradictions.json 0=0     inherited-prefix-identical=True
new source: {"id": "aru-acknowledgment-note", "title": "Aru's Chalk Stair Acknowledgment Note",
             "kind": "fictional first-person note", "reliability_note": "...receipt only; not evidence of a
             resolution, a reconciliation, an accusation, a winner..., a continuing duty, or an external historical fact."}
new event:  {"id": "acknowledgment-aru-records", "tick": 13, "entity_id": "aru", "place_id": "chalk-stair",
             "depends_on": ["response-evin-salt-court"], "description": "At the Chalk Stair at tick 13, Aru reports
             receiving Evin's response and states that both first-person accounts stand unresolved; the note asserts
             no accusation, no reconciliation, no winner between the accounts, and no new duty beyond this crossing.",
             "source_id": "aru-acknowledgment-note"}
counts: entities=5 relations=1 timeline=6 sources=6 contradictions=0
```

`fictional-excerpts.md` is a pure byte-prefix append (`diff <(git show f3e09f9:…r96…fictional-excerpts.md) <r97 file>` → `42a43,53`, nothing else). New section occupies lines 44-53; quoted note lines 48-51:

```
48:> Tick 13: I received Evin's response at the Chalk Stair.
49:> I hold to my own account; both accounts stand unresolved.
50:> I make no accusation against Evin, and I select no winner between us.
51:> I assert no reconciliation, no new duty, and no obligation beyond this crossing.
```

No resolution, no accusation, no reconciliation claim, no new duty; `contradictions.json` stays `[]`.

Verification:

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r97-crossing-acknowledgment ; echo EXIT=$?
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT=0
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response   # control
CLEAN: schema, citations, relations, timeline; 0 violations   EXIT=0
$ ls -d corpus/fixtures/*/ | wc -l
171          # census 170 → 171
```

Pre-R5 state, captured as evidence that the 17th row was genuinely R5's pending work rather than silently satisfied by my byte-copy:

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r97-crossing-acknowledgment
OBLIGATIONS raw=17 mapped=16
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18
FINDING missing_obligation: timeline.json#/5 has no map row
RESULT FAIL
EXIT=1
```

## Post-R5 cross-check (R5's files, observed — not mine)

R5's map landed while I polled (11 × 20 s). Delivered state after it landed:

```
$ python3 corpus/tools/support_check.py corpus/fixtures/r97-crossing-acknowledgment | tail -6
PASS J17: source-support; mode=verbatim; anchor=found; 48:> Tick 13: I received Evin's response at the Chalk Stair.
RECEIPT JSON-FACTS 17; EDITORIAL-ROWS 2; TOTAL-ROWS 19
SOURCE-SUPPORT 17/17; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 19/19; VALIDATED-ROWS 19/19
RESULT PASS   EXIT=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r97-crossing-acknowledgment
OBLIGATIONS raw=17 mapped=17
INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19
RESULT PASS   EXIT=0
```

R5's map inherits my repaired base (its editorial delimiter is 7 cells; `grep -c "new relation"` = 0) and adds `J17` with anchor line 48, declared span 44-53, which is exactly the section I authored. Its inherited J01–J16 rows differ from the r96 map only in the namespace column, as intended. R5's `README.md` also landed ("Round 97 crossing-acknowledgment continuation", 5/1/6 counts). R5's seat report was still absent at my last check (report-last convention; not my file).

## Bounds and notes for adjudication

- **Tool churn:** `map_obligations.py` hash moved under me during the round (frozen `2b0ba815…` → `c1881149…` → `86b52949…`). My r96 before/after receipts were both produced by the frozen revision and were re-proven against a scratch pre-repair copy; the interim revision also reproduces the r96 receipt byte-for-byte. `support_check.py` is unmodified (`55a5eb27…` = frozen).
- **Freeze pin vs the repair:** the r96 pin's `files` map lists only the five JSON tables — `claim-excerpt-map.md` is not a pinned file — and the r96 digest is unchanged by my repair:

  ```
  $ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r96-crossing-response
  FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
  DIGEST d422a9b3d95c4e0b8aac98cc87806a94949896adb962a50d2d55a6c11657d7f6   RESULT PASS   EXIT=0
  chain at report time: r88 15ef230e… PASS / r94 2527beb9… PASS / r95 d541ae64… PASS / r96 d422a9b3… PASS
  ```

  So the C2 "re-freeze through the guarded path" is a pin-format/guard refresh (R3's path-binding + scope work), not a digest change forced by my cosmetic repair. R3 owns that call; I did not run `--freeze` (producer-owned contract).
- **My byte-copies are bases for R5's files:** at creation time the r97 `claim-excerpt-map.md` was byte-identical to the post-repair r96 map and the r97 `README.md` to the r96 README; R5 has since rewritten both. I did not write them after R5 landed.
- Everything else in the lane was read-only for me; the only writes were my owned paths plus `R4-scratch/` and this report.

## Bottom line

**PASS** — r96 cosmetic repair delivered and proven byte-minimal (2 lines changed; `support_check` and `map_obligations` receipts byte-identical before/after under both frozen and current tool revisions), and `r97-crossing-acknowledgment` delivered as a verified pure-append continuation (10 byte-verified base files, `aru-acknowledgment-note` + tick-13 `acknowledgment-aru-records` + receipt-only Aru excerpt, `check_bible` CLEAN exit 0, 5/1/6, 6 sources, census 171; with R5's map landed the fixture is `support_check` 17/17 / 19/19 PASS and `map_obligations` raw=17 mapped=17 PASS).
