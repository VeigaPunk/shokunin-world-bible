# V05 — C3 dialect coverage: r88-m3-maya-cluster

Seat: V05 (verifier, C3 axis — r88 map dialect). Round 95, baseline `fb118c4`.
Report path (exclusive): `.ufo/waves/round-95/seats/V05-c3-dialect-r88.md`

**Verified revision (frozen):**

```
$ sha256sum corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json
d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108  corpus/tools/map_obligations.py
8173bb97592a377716866737e8fcb4043014c9814e77a6248500d301a39170db  corpus/tools/map-obligations-contract.json
```

`map_obligations.py` mtime `2026-10-17 16:26:27 -0300`, unchanged from 16:26:27 to 16:28:25
(2 min stable window; P1's report `.ufo/waves/round-95/seats/P1-tool-code.md` present). All numbers
below are from this revision. `corpus/tools/support_check.py` is untouched
(`git status --porcelain corpus/tools/` lists only `map_obligations.py` and
`map-obligations-contract.json`).

**Process disclosure (not a defect of the delivered artifact).** P1 edited in place; I observed
non-final intermediate states: at 16:22:48 the constants `POINTER_COLUMN_ROLES` /
`LEGACY_POINTER_COLUMN` / `EXPECTED_INVENTORY` existed but `parse_map_text` still hardcoded the old
role set (r88 still exit 2), and at 16:23:09 `r93`/`r94` crashed with
`ValueError: too many values to unpack (expected 2, got 12)` because `compare()` had not yet been
adapted to the widened row tuples. Any seat that sampled the tool inside 16:22–16:24 would have seen
a broken tool; verification must be dated to `d1c239cc`.

## 1. C3 "After" clause — r88 now passes

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r88-m3-maya-cluster
OBLIGATIONS raw=10 mapped=10
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12
RESULT PASS
exit=0
```

Before (reproduced on the untouched baseline tool):

```
FINDING unsupported_map: table needs one JSON fact pointer and one source-ID column
RESULT ERROR
exit=2
```

**Wording contradiction with the round declaration (evidence).** C3 declares "12/12 PASS over the
r88 map's obligations". r88 has **10** raw source-attributed obligations, not 12. "12" is the map's
declared *total mapped row count* (10 JSON facts + 2 editorial rows). The tool prints both numbers,
correctly labelled: `OBLIGATIONS raw=10 mapped=10` (obligations) and
`INVENTORY ... TOTAL-ROWS 12/12` (rows). An honest `raw=12 mapped=12` is impossible here — the two
editorial rows point at `source-excerpt.md`, not at JSON pointers, so counting them as obligations
would raise `phantom_obligation` and exit 1. P1's report §6.1 raises the same contradiction.

## 2. Independent hand enumeration vs the tool's parse (no phantom, no missing)

Enumerated by hand from the r88 JSON — `first_appearance` + per-entity `claims` + `relations` +
`timeline`:

```
INDEPENDENT ENUMERATION: 10 raw source-attributed JSON obligations
  entities.json#/0/first_appearance             src=paired-clock   (entity[0] aru)
  entities.json#/0/claims/0                     src=paired-clock   (entity[0].claims[0])
  entities.json#/1/first_appearance             src=paired-clock   (entity[1] evin)
  entities.json#/1/claims/0                     src=paired-clock   (entity[1].claims[0])
  entities.json#/2/first_appearance             src=paired-clock   (entity[2] quiet-rise)
  entities.json#/2/claims/0                     src=paired-clock   (entity[2].claims[0])
  entities.json#/3/first_appearance             src=paired-clock   (entity[3] salt-court)
  entities.json#/3/claims/0                     src=paired-clock   (entity[3].claims[0])
  timeline.json#/0                              src=paired-clock   (timeline[0] aru-ninth-bell)
  timeline.json#/1                              src=paired-clock   (timeline[1] evin-ninth-bell)
relations count: 0 | contradictions count: 0
sources.json ids: ['veil-verse', 'paired-clock']
```

I then imported the delivered parser and diffed its translation against that list (frozen revision):

```
FROZEN-REVISION CROSS-CHECK
 tool raw_obligations: 10 | drift findings: []
 tool map rows: 10 | editorial rows: 2 | declared: (10, 2, 12, 8) | malformed: False
 hand enumeration: 10
 EXACT SET MATCH tool==hand: True | rows==hand: True
 phantom: [] | missing: []
 compare findings: []
 receipt would read: INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12
```

Tool-parsed rows, verbatim:

```
  entities.json#/0/first_appearance          paired-clock
  entities.json#/1/first_appearance          paired-clock
  entities.json#/2/first_appearance          paired-clock
  entities.json#/3/first_appearance          paired-clock
  entities.json#/0/claims/0                  paired-clock
  entities.json#/1/claims/0                  paired-clock
  entities.json#/2/claims/0                  paired-clock
  entities.json#/3/claims/0                  paired-clock
  timeline.json#/0                           paired-clock
  timeline.json#/1                           paired-clock
```

So: **no phantom** (no row for `veil-verse`, `sources.json`, `contradictions.json`, or any
non-obligation field) and **no missing** (all 10 raw pointers covered). The legacy grammar
`entities[0].first_appearance` / `entities[0].claims[0]` / `timeline[1]` is translated to canonical
pointers, and the two editorial rows (S1/S2) are counted in the inventory receipt but are *not*
treated as obligations — which is exactly what `support_check`'s `MODES 12/12` on r88 counts.

## 3. Anchors / spans / modes — agreement with the map's declared rows

Hand-transcribed the 12 declared rows (P1–P4, E1–E4, T1–T2, S1–S2) and checked each declared anchor
against the declared excerpt file and line:

```
P1  fictional-excerpts.md:12  mode=verbatim anchor_present_on_declared_line=True char_span=10..53
P2  fictional-excerpts.md:13  mode=verbatim anchor_present_on_declared_line=True char_span=10..48
P3  fictional-excerpts.md:12  mode=verbatim anchor_present_on_declared_line=True char_span=10..53
P4  fictional-excerpts.md:13  mode=verbatim anchor_present_on_declared_line=True char_span=10..48
E1  fictional-excerpts.md:12  mode=verbatim anchor_present_on_declared_line=True char_span=2..54
E2  fictional-excerpts.md:13  mode=verbatim anchor_present_on_declared_line=True char_span=2..49
E3  fictional-excerpts.md:12  mode=verbatim anchor_present_on_declared_line=True char_span=26..53
E4  fictional-excerpts.md:13  mode=verbatim anchor_present_on_declared_line=True char_span=24..48
T1  fictional-excerpts.md:12  mode=verbatim anchor_present_on_declared_line=True char_span=2..54
T2  fictional-excerpts.md:13  mode=verbatim anchor_present_on_declared_line=True char_span=2..49
S1  source-excerpt.md:5       mode=verbatim anchor_present_on_declared_line=True char_span=148..170
S2  source-excerpt.md:5       mode=verbatim anchor_present_on_declared_line=True char_span=171..199
HAND CHECK: 12/12 declared anchors occur on their declared excerpt lines
distinct (path,line) anchors: 8
```

All 12 declared rows are `verbatim`; the 8 distinct anchors equal the map's declared
"8 distinct excerpt anchors".

**Scope bound (honest).** The tool does **not** parse, report, or validate anchors, line spans, or R9
modes — its legacy path reads only the pointer column and the source-ID column (plus a cell-count
equality check). The declared anchor count is captured by the inventory regex as a fourth group and
then discarded (`facts, editorial, total, _anchors = declared`, `map_obligations.py:264`), so
`TOTAL-ROWS 12/12` never checks "8 anchors". "The same anchors/spans/modes" is therefore established
by (a) the r88 map being byte-identical to baseline and (b) my hand check above — not by the tool.

## 4. Fail-closed controls (must not change)

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r87-myth-cluster
FINDING unsupported_map: pointer cells must contain one canonical inline-code pointer
RESULT ERROR
exit=2

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r89-inspiration-paraphrase
FINDING unsupported_map: table needs one JSON fact pointer and one source-ID column
RESULT ERROR
exit=2
```

Both stay exit 2 `unsupported_map`. r87's *message* changed from `table needs one JSON fact pointer
and one source-ID column` (baseline) to `pointer cells must contain one canonical inline-code
pointer` (delivered), because r87's pointer column is now recognised and the rejection happens one
step later at cell parsing. Finding ID, exit code and RESULT line are unchanged, so C3's
"stay exit 2 fail-closed" holds; the message delta is disclosed for the record.

Adversarial probes on **in-memory copies** of the r88 map text (the real fixture was never written):

| Probe | Observed |
|---|---|
| baseline r88 (control) | parsed=10, findings=[], declared=(10,2,12,8) |
| drop the T2 row | parsed=9, findings=`['missing_obligation']` |
| duplicate a row | parsed=11, findings=`['duplicate_mapping']` |
| P1 row's source cell → `veil-verse` | findings=`['source_id_mismatch']` |
| add phantom row `entities[0].name` | `ToolError unsupported_map: co-mapped or unsupported pointer grammar` |
| co-mapped legacy cell (`` `entities[0].first_appearance`, co-map `entities[0].name` ``) | `ToolError unsupported_map: pointer cells must contain one canonical inline-code pointer` |
| legacy cell under a canonical `JSON fact pointer` header | `ToolError unsupported_map: co-mapped or unsupported pointer grammar` |
| declared inventory tampered to 11 facts | declared=(11,2,12,8), findings=[] → prints ` MISMATCH`, **exit unchanged** |
| `**Expected inventory:**` line removed | declared=None, no receipt line, findings=[] |

The last two rows are C3-relevant scope bounds: the inventory declaration is echoed, never gated, so
a tampered inventory line is reported as ` MISMATCH` / `INVENTORY declaration-malformed` but does not
change the exit code (the receipt print at `map_obligations.py:267` is not routed into `emit`'s
findings). Consistent with P1's §6.4.

## 5. "Zero corpus modifications" (C3's explicit constraint)

54 fixture files under `corpus/fixtures/{r87-myth-cluster,r88-m3-maya-cluster,r89-inspiration-paraphrase,r93-m2-kojiki-cluster,r94-paired-crossing}`
were hashed **before** P1's delivery and re-checked after:

```
$ sha256sum -c /tmp/v05-fixture-hashes-before.txt | grep -v ': OK$'
(no output — all 54 unchanged)

$ git status --porcelain corpus/
 M corpus/tools/map-obligations-contract.json
 M corpus/tools/map_obligations.py
?? corpus/fixtures/r95-crossing-aftermath/
?? corpus/knowledge/r95-aftermath-scope-note.md
```

r88's map hash is unchanged: `b3b79fe5b5b9272b898b5714291739503c4250c415b3959032fcdba84a73fd43`
before and after. No r87/r88/r89/r93/r94 fixture byte was touched — the dialect support is genuinely
tool-surface only, as C3 requires.

## 6. Regression sweep — exactly one fixture changed

Replicated P1's §4 claim independently: executed the `fb118c4` revision (loaded from `git show` into
memory, no file written) and the delivered revision over **every** `corpus/fixtures/*` directory,
comparing `(exit code, sorted finding-id list)`:

```
fixtures scanned: 169
fixtures whose (exit, finding-ids) changed: 1
  CHANGED r88-m3-maya-cluster: old rc=2 ['unsupported_map']  ->  new rc=0 []
--- explicit controls ---
  r87-myth-cluster: old rc=2 ['unsupported_map'] | new rc=2 ['unsupported_map']
  r88-m3-maya-cluster: old rc=2 ['unsupported_map'] | new rc=0 []
  r89-inspiration-paraphrase: old rc=2 ['unsupported_map'] | new rc=2 ['unsupported_map']
  r93-m2-kojiki-cluster: old rc=0 [] | new rc=0 []
  r94-paired-crossing: old rc=0 [] | new rc=0 []
  r95-crossing-aftermath: old rc=0 [] | new rc=0 []
```

Exactly the one intended change; r93/r94 and all other 167 fixtures identical. (r95-crossing-aftermath
already exits 0 under the old tool — it uses canonical grammar; not my seat.)

## 7. Support_check receipts and sibling gates (corroboration)

```
$ python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster | tail -2
SOURCE-SUPPORT 10/10; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 12/12; VALIDATED-ROWS 12/12
RESULT PASS
```

Identical before and after delivery; r93 `SOURCE-SUPPORT 12/12` and r94 `SOURCE-SUPPORT 14/14` also
unchanged, all exit 0. `support_check.py` is not in the modified set.

Corroborating gates on the same frozen revision (C1's declared gates, not my axis):

```
$ python3 corpus/tools/map_obligations.py --self-test      # 22/22 SELF-TEST PASS, RESULT PASS, exit=0
  ... includes map_missing exit=2 ['map_missing'] and invalid_arguments exit=2 ['invalid_arguments']
$ python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93
SNAPSHOT inputs=4 digests=verified
OBLIGATIONS raw=12 mapped=12
INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15
FROZEN expected=PASS/0 findings=none matched
RESULT PASS
exit=0
```

`corpus/tools/map-obligations-contract.json` now carries 22 cases (was 20), including `map_missing`
and `invalid_arguments`.

## 8. C3 verdict

C3 as declared is **verified on the frozen revision**, with one wording correction:

- `r88` moves from exit 2 `unsupported_map` to `RESULT PASS` exit 0; the tool's 10 parsed obligation
  rows are an exact set match to my independent hand enumeration (no phantom, no missing), and the
  `TOTAL-ROWS 12/12` receipt reconciles as 10 JSON facts + 2 editorial rows.
- `r87`/`r89` remain exit 2 fail-closed; `r93` 12/12 and `r94` 14/14 unchanged; `support_check`
  receipts unchanged; all 54 r87/r88/r89/r93/r94 fixture bytes unchanged; the corpus-wide sweep shows
  exactly the one intended fixture change out of 169.
- **Correction:** the declaration's "12/12 PASS over the r88 map's obligations" conflates rows with
  obligations — the obligation count is 10, the mapped-row count is 12. The delivered output states
  both, correctly labelled.
- **Not established by the tool:** anchors/spans/modes per row (the tool reads neither the excerpt
  path, line span, mode, nor anchor columns; the declared anchor count is parsed and discarded), and
  the inventory declaration is echoed but not gated (a tampered inventory prints ` MISMATCH` at exit
  0). The anchors/spans/modes agreement rests on the unmodified fixture plus my 12/12 hand check.

Bottom line: PASS — on `map_obligations.py` `d1c239cc` (contract `8173bb97`, 22 cases), r88 goes
exit 2 `unsupported_map` → exit 0 PASS with the tool's 10 parsed obligations exactly matching my
independent hand enumeration (no phantom, no missing) and `TOTAL-ROWS 12/12` reconciling as 10 JSON
facts + 2 editorial rows, while r87/r89 stay exit 2, r93/r94 and all `support_check` receipts are
unchanged, and all 54 relevant fixture bytes are untouched — with the caveat that "12/12" counts
mapped rows, not obligations, and the tool does not validate anchors/spans/modes or gate the
inventory declaration.
