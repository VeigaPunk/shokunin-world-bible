# V16 — preservation-mutations (round 95)

Seat V16, leaf verifier. Scope per seat spec: scratch mutations on copies of
`corpus/fixtures/r95-crossing-aftermath/` — span break on the new anchor,
map-row removal (blind-spot closure), raw event `source_id` change, and the
BR-02 `claims`-key-rename + row-removal schema-drift class. Live tree untouched;
no commits; writes confined to `.ufo/waves/round-95/seats/V16-scratch/` and this
report. Baseline: r94 closure `fb118c4`.

## 0. Verified revision, polling, and live-tree protection

- **Poll 1** fired at 16:23:38 as soon as `schema_drift` appeared in
  `corpus/tools/map_obligations.py` (sha256 `52d838b0…`). That revision was
  **mid-write and crashed on every cluster** — `ValueError: too many values to
  unpack (expected 2, got 15)` at `compare()` line 418, exit 1 with a traceback
  and no `RESULT` line. Evidence kept in `V16-scratch/replay-midwrite-crash.txt`;
  nothing from it is credited.
- **Poll 2** was gated on P1's report existing AND a clean exit 0 on the live
  fixture. P1's report (`.ufo/waves/round-95/seats/P1-tool-code.md`) landed and
  the tool stabilized. All receipts below are from the frozen revision
  **sha256 `d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108`**,
  identical before and after the final run (`replay.txt` header + post-run check).
- Companion revisions at verification time: contract
  `8173bb97592a377716866737e8fcb4043014c9814e77a6248500d301a39170db` (P2),
  `support_check.py` `55a5eb27…`, `check_bible.py` `ff9fd2aa…`; git-baseline tool
  extracted via `git show fb118c4:corpus/tools/map_obligations.py` →
  `cc1df4dc406870b6fc4ddbc3291e3690cf87dfb061f76ec3b4fec5cfcfbab790`
  (`V16-scratch/map_obligations_OLD.py`).
- Context (not this seat): `python3 corpus/tools/map_obligations.py --self-test`
  on the frozen revision → `RESULT PASS`, exit 0, 22 `SELF-TEST PASS` / 0 FAIL
  lines including `map_missing` and `invalid_arguments`
  (`V16-scratch/selftest-final.out`).
- Producer reports at write time: P1, P3, P4, P5 present; P2's report absent, its
  artifact (22-case contract) present.

Method: builder `V16-scratch/build_mutants.py` copytrees the live fixture per
mutant, applies one asserted single-occurrence edit per mutant, and runs the
three checkers (delivered tool, git-baseline tool, `support_check`, `check_bible`)
recording every command and exit code into `V16-scratch/replay.txt`. Commands are
quoted repo-root-relative below; the log holds the exact absolute invocations.

Live protection: all ten live fixture files SHA-256 identical before==after
(`# live fixture byte-identical before==after: True`). `git status --short` after
all runs:

```
 M LOG.md
 M corpus/tools/map-obligations-contract.json
 M corpus/tools/map_obligations.py
?? .ufo/waves/round-95/
?? corpus/fixtures/r95-crossing-aftermath/
?? corpus/knowledge/r95-aftermath-scope-note.md
```

No modification under `corpus/fixtures/r95-crossing-aftermath/` (still untracked
as delivered); the only `M` files are P1/P2 artifacts, not touched by this seat.

## 1. Baseline control (live fixture, unchanged)

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath
CLEAN: schema, citations, relations, timeline; 0 violations            [exit=0]

$ python3 corpus/tools/support_check.py corpus/fixtures/r95-crossing-aftermath
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17; DISTINCT-ANCHORS 13/13
RECEIPT JSON-FACTS 15; EDITORIAL-ROWS 2; TOTAL-ROWS 17
SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 17/17; VALIDATED-ROWS 17/17
RESULT PASS                                                            [exit=0]

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
RESULT PASS                                                            [exit=0]

$ python3 .ufo/…/V16-scratch/map_obligations_OLD.py corpus/fixtures/r95-crossing-aftermath
OBLIGATIONS raw=15 mapped=15
RESULT PASS                                                            [exit=0]
```

All green, so every red below is attributable to the single mutation applied.

## 2. Result matrix

| Mutant | Mutation | `support_check` | `map_obligations` (delivered `d1c239cc`) | `map_obligations` (git `fb118c4`) | `check_bible` |
|---|---|---|---|---|---|
| `mut-c-break-span` | J15 span `22-31` → `32` (anchor hit line 26) | **FAIL exit 1** | PASS exit 0 | — | CLEAN exit 0 |
| `mut-b-drop-new-row` | delete J15 row + restate inventory 15/2/17/13 → 14/2/16/12 | **PASS exit 0** (blind) | **FAIL exit 1 `missing_obligation`** | — | CLEAN exit 0 |
| `mut-b2-drop-inherited-row` | delete J06 row + restate inventory | **PASS exit 0** (blind) | **FAIL exit 1 `missing_obligation`** | — | — |
| `mut-d-source-id` | `timeline.json#/3` `source_id` `aru-aftermath-note` → `crossing-minute` | PASS exit 0 | **FAIL exit 1 `source_id_mismatch`** | — | CLEAN exit 0 |
| `mut-e-schema-drift` | entity 4 `claims` → `assertions` (content preserved) + delete J10 row + restate inventory | PASS exit 0 | **FAIL exit 1 `schema_drift`** | **PASS exit 0 (silent)** | VIOLATION exit 1 (3) |

## 3. (c) Span break on the new anchor — `support_check` fails closed

`# broke span for timeline.json#/3: 22-31 -> 32 (anchor hit at line 26)` — the
J15 row's declared span replaced; anchor text unchanged.

```
$ python3 corpus/tools/support_check.py .ufo/…/V16-scratch/mut-c-break-span
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17; DISTINCT-ANCHORS 13/13
FAIL J15: source-support; mode=verbatim; anchor=found; 26:> Tick 11: I waited at the Chalk Stair through the agreed bell.; span=32; outside-span=26
SOURCE-SUPPORT 14/15; EDITORIAL-ANCHORS 2/2; … MODES 17/17; VALIDATED-ROWS 16/17
FAIL: J15: anchor hit outside declared line span 32 (hit lines: 26)
RESULT FAIL                                                            [exit=1]

$ python3 corpus/tools/map_obligations.py .ufo/…/V16-scratch/mut-c-break-span
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
RESULT PASS                                                            [exit=0]

$ python3 corpus/fixtures/check_bible.py .ufo/…/V16-scratch/mut-c-break-span
CLEAN: schema, citations, relations, timeline; 0 violations            [exit=0]
```

Exactly one row fails, the failure names the outside-span hit, and exit is 1.

## 4. (b) Map row removed — `map_obligations` exit 1 while `support_check` PASSes

`mut-b-drop-new-row`: the J15 row deleted and the map's self-declared inventory
restated consistently (`# restated inventory -> 14 JSON facts; 2 editorial rows; 16 total; 12 anchors`).

```
$ python3 corpus/tools/support_check.py .ufo/…/V16-scratch/mut-b-drop-new-row
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16; DISTINCT-ANCHORS 12/12
RECEIPT JSON-FACTS 14; EDITORIAL-ROWS 2; TOTAL-ROWS 16
SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 2/2; … MODES 16/16; VALIDATED-ROWS 16/16
RESULT PASS                                                            [exit=0]

$ python3 corpus/tools/map_obligations.py .ufo/…/V16-scratch/mut-b-drop-new-row
OBLIGATIONS raw=15 mapped=14
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16
FINDING missing_obligation: timeline.json#/3 has no map row
RESULT FAIL                                                            [exit=1]
```

`mut-b2-drop-inherited-row` (J06, `entities.json#/0/claims/0`, an inherited r94
row) — same shape:

```
$ python3 corpus/tools/support_check.py .ufo/…/V16-scratch/mut-b2-drop-inherited-row
INVENTORY JSON-FACTS 14/14; … TOTAL-ROWS 16/16; DISTINCT-ANCHORS 12/12
RESULT PASS                                                            [exit=0]

$ python3 corpus/tools/map_obligations.py .ufo/…/V16-scratch/mut-b2-drop-inherited-row
OBLIGATIONS raw=15 mapped=14
FINDING missing_obligation: entities.json#/0/claims/0 has no map row
RESULT FAIL                                                            [exit=1]
```

So a dropped JSON-fact row remains invisible to `support_check` as long as the
map's own counts are updated, while the delivered `map_obligations` catches it at
exit 1 — the blind-spot closure is re-demonstrated on the r95 fixture, for both
the new and an inherited obligation. `check_bible` is CLEAN exit 0 on mut-b.

## 5. (d) Raw event `source_id` changed — `source_id_mismatch`

`# timeline.json aftermath-missing-evin source_id 'aru-aftermath-note' -> 'crossing-minute'`.

```
$ python3 corpus/tools/map_obligations.py .ufo/…/V16-scratch/mut-d-source-id
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
FINDING source_id_mismatch: timeline.json#/3 does not bind to 'crossing-minute'
RESULT FAIL                                                            [exit=1]

$ python3 corpus/tools/support_check.py .ufo/…/V16-scratch/mut-d-source-id
SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS 2/2; … MODES 17/17; VALIDATED-ROWS 17/17
RESULT PASS                                                            [exit=0]

$ python3 corpus/fixtures/check_bible.py .ufo/…/V16-scratch/mut-d-source-id
CLEAN: schema, citations, relations, timeline; 0 violations            [exit=0]
```

Both source IDs are declared, so the other two checkers stay green; only the
pointer-to-source binding check catches the drift, naming the exact pointer.

## 6. (e) `claims`-key rename + row removal — NEW `schema_drift` exit 1

`# entities.json: 5th "claims" key renamed to "assertions" (content preserved)`
(chalk-stair, `entities.json#/4`); `# removing map row containing
'entities.json#/4/claims/0'` (J10); inventory restated to 14/2/16/12.

```
$ python3 corpus/tools/map_obligations.py .ufo/…/V16-scratch/mut-e-schema-drift
OBLIGATIONS raw=14 mapped=14
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16
FINDING schema_drift: entities.json#/4: 1 sourced-claim-shaped record(s) under unexpected key 'assertions'
RESULT FAIL                                                            [exit=1]

$ python3 .ufo/…/V16-scratch/map_obligations_OLD.py .ufo/…/V16-scratch/mut-e-schema-drift
OBLIGATIONS raw=14 mapped=14
RESULT PASS                                                            [exit=0]
```

The git-baseline (`fb118c4`) tool is **silently PASS exit 0** on the identical
mutant — the BR-02 class reproduced — while the delivered revision emits the
stable `schema_drift` finding and exits 1. Supporting checkers on the same
mutant: `support_check` `INVENTORY 14/14; 2/2; 16/16; 12/12` / `SOURCE-SUPPORT
14/14` / `RESULT PASS` exit 0 (map and excerpts untouched by the mutation), and
`check_bible` exit 1:

```
VIOLATION: entities[4].claims: required nonempty list
VIOLATION: timeline[2].place_id: dangling entity 'chalk-stair'
VIOLATION: timeline[3].place_id: dangling entity 'chalk-stair'
3 violation(s); no canon changed
```

The two dangling-place violations are a cascade of the first: entity 4 fails
`check_bible`'s required-`claims` field check, so it is excluded from the
resolved index and its timeline uses become dangling. This does not weaken the
C1 claim — the declared silent-PASS was specific to `map_obligations`, and that
exact before/after (old PASS exit 0 vs delivered `schema_drift` exit 1) is shown
above.

## 7. Bounds and anomalies (reported exactly)

- **Mid-write revision not credited**: at 16:23:38–16:24:25 the working tree held
  a crashing intermediate (shas `52d838b0…`, `feca13c9…`, `3f87fe8b…`); the
  final run was taken only after P1's report landed and the sha froze
  (`d1c239cc…`, unchanged across the run). The traceback log is preserved.
- **Scope of each checker demonstrated by the mutants**: span integrity is
  invisible to `map_obligations` and `check_bible` (mut-c PASS/CLEAN);
  pointer-to-source binding is invisible to `support_check` and `check_bible`
  (mut-d PASS/CLEAN); a row removed with restated inventory is invisible to
  `support_check` and `check_bible` (mut-b PASS/CLEAN).
- The delivered tool's new `INVENTORY …` receipt line is present on every run
  above; no ` MISMATCH` suffix appears because each mutant's inventory was
  restated to be self-consistent (deliberate, to isolate the checks).
- Concurrent seats' transient `map-obligations-self-test-*` temp dirs appeared
  and were cleaned during the window; none are this seat's residue.

## Bottom line

**PASS** — on frozen delivered revision `d1c239cc…`, all four required mutation
classes behave exactly as declared (span break → `support_check` FAIL exit 1;
removed map row → `missing_obligation` exit 1 while `support_check` stays PASS;
raw `source_id` change → `source_id_mismatch` exit 1; `claims`-key rename + row
removal → new `schema_drift` exit 1 where the `fb118c4` tool stayed silently
PASS exit 0), with the live fixture byte-identical throughout.
