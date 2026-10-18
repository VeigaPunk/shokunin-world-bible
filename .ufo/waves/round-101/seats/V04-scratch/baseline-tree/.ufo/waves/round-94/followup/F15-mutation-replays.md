# F15 — mutation-replays

**Seat:** F15 (round-94 FOLLOW-UP wave, lore-shokunin). **Role:** leaf verification seat — mutate scratch copies of `corpus/fixtures/r94-paired-crossing/` and record what `check_bible.py`, `support_check.py` and `map_obligations.py` actually do. Live tree untouched; no corpus edits, no commits.

## 0. Method and live-tree protection

- Scratch root: `.ufo/waves/round-94/followup/F15-scratch/` (allowed by seat); builder: `.ufo/waves/round-94/followup/F15-scratch/make_mutants.py`. It reads the live fixture read-only, `shutil.copytree`s it per mutant, asserts every textual replacement occurs exactly once, and prints a unified diff against the live file (diffs quoted below). Replay: `python3 .ufo/waves/round-94/followup/F15-scratch/make_mutants.py`.
- Symlink guard: `map_obligations.resolve_cluster` fails with `unsafe_path` on any symlinked path component, so I checked first: `symlink components in scratch path: none` (`scratch resolved: /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-94/followup/F15-scratch`).
- Live fixture SHA-256 **before** and **after** all runs — identical, e.g. `ed9527c5…e89a47  corpus/fixtures/r94-paired-crossing/claim-excerpt-map.md`, `f0209f90…60533c  …/timeline.json` (full 10-file list captured both times; byte-identical).
- `git status --short` after all work: only `?? .ufo/waves/round-94/followup/` (my untracked scratch dir). `git diff --stat abbc3e0 -- corpus/` → empty. **No live corpus byte changed.**

## 1. Baseline control (live fixture, unchanged)

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r94-paired-crossing
CLEAN: schema, citations, relations, timeline; 0 violations          exit=0

$ python3 corpus/tools/support_check.py corpus/fixtures/r94-paired-crossing
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16; DISTINCT-ANCHORS 12/12
RECEIPT JSON-FACTS 14; EDITORIAL-ROWS 2; TOTAL-ROWS 16
SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 16/16; VALIDATED-ROWS 16/16
RESULT PASS                                                          exit=0

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing
OBLIGATIONS raw=14 mapped=14
RESULT PASS                                                          exit=0
```

All three start green, so every red below is attributable to the mutation.

## 2. Result matrix (all commands run from repo root)

| Mutant | Mutation | `check_bible` | `support_check` | `map_obligations` |
|---|---|---|---|---|
| `mut-a-drop-dep` | drop `evin-ninth-bell` from tick-10 `depends_on` | **CLEAN exit 0** (not reported) | PASS exit 0 | PASS exit 0 |
| `mut-a2-drop-event` | delete the tick-9 event record itself | **VIOLATION exit 1** | PASS exit 0 | FAIL exit 1 |
| `mut-b-drop-j11-row` | delete map row J11 + restate inventory 13/2/15/11 | CLEAN exit 0 | **PASS exit 0** (blind) | **FAIL exit 1 `missing_obligation`** |
| `mut-b2-drop-j05-row` | delete map row J05 + restate inventory | CLEAN exit 0 | **PASS exit 0** (blind) | **FAIL exit 1 `missing_obligation`** |
| `mut-b3-row-only` | delete row J11, leave inventory 14/2/16/12 | CLEAN exit 0 | FAIL exit 1 (inventory only) | FAIL exit 1 `missing_obligation` |
| `mut-c-break-span` | J05 declared span `17` → `20` | CLEAN exit 0 | **FAIL exit 1** | PASS exit 0 |
| `mut-d-source-id` | timeline event 3 `source_id` `crossing-minute` → `paired-clock` | CLEAN exit 0 | PASS exit 0 | **FAIL exit 1 `source_id_mismatch`** |

## 3. (a) Break the tick-10 dependency — expectation CONTRADICTED

Mutation (`make_mutants.py` diff, `mut-a-drop-dep/timeline.json`):

```diff
     "depends_on": [
-      "aru-ninth-bell",
-      "evin-ninth-bell"
+      "aru-ninth-bell"
     ],
```

```
$ python3 corpus/fixtures/check_bible.py .ufo/waves/round-94/followup/F15-scratch/mut-a-drop-dep
CLEAN: schema, citations, relations, timeline; 0 violations          exit=0

$ python3 corpus/tools/support_check.py .ufo/…/F15-scratch/mut-a-drop-dep   (non-PASS lines shown)
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16; DISTINCT-ANCHORS 12/12
SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 2/2; … MODES 16/16; VALIDATED-ROWS 16/16
RESULT PASS                                                          exit=0

$ python3 corpus/tools/map_obligations.py .ufo/…/F15-scratch/mut-a-drop-dep
OBLIGATIONS raw=14 mapped=14
RESULT PASS                                                          exit=0
```

**Observed:** `check_bible` does **not** report a dropped tick-9 dependency. It only validates the dependency edges that remain: unknown/ambiguous/self/repeated ids and tick inversion (`corpus/fixtures/check_bible.py:397-414`). A *reduction* of `depends_on` from two entries to one leaves a still-valid, still-earlier edge, so it stays CLEAN; `support_check` never reads raw JSON, and `map_obligations` only compares pointer existence and source-id binding. The map's own row J14 (`claim-excerpt-map.md:35`) still asserts the excerpt wording “depends on both ninth-bell entries”, and the excerpt (`fictional-excerpts.md:20`) is unchanged — nothing cross-checks the JSON dependency set against that wording.

**Nothing in r94 catches this mutation.** A repo-wide count of `depends_on` readers shows the only Python consumers are `corpus/fixtures/check_bible.py` (7 hits) and its historical copy `corpus/live/rejected-r4/check_bible.py` (7 hits); no tool under `corpus/tools/` reads the field. There is also no r94 frozen digest pin to fall back on: `.ufo/waves/round-94/frozen/` contains only `map-obligations-r93/` (4 pinned inputs, r93 fixture), so byte-level tamper detection exists for r93 only.

Variant `mut-a2-drop-event` (delete the `evin-ninth-bell` record itself, leaving the tick-10 `depends_on` naming it) shows the mutation *is* caught when the dependency becomes referentially dangling:

```
$ python3 corpus/fixtures/check_bible.py .ufo/…/F15-scratch/mut-a2-drop-event
VIOLATION: timeline[1].depends_on: unknown event 'evin-ninth-bell'
1 violation(s); no canon changed                                      exit=1

$ python3 corpus/tools/map_obligations.py .ufo/…/F15-scratch/mut-a2-drop-event
OBLIGATIONS raw=13 mapped=14
FINDING phantom_obligation: timeline.json#/2 is not a raw source-attributed obligation
FINDING source_id_mismatch: timeline.json#/1 does not bind to 'crossing-minute'
RESULT FAIL                                                           exit=1
```

Side observation: the two `map_obligations` findings in a2 are an artifact of positional pointers — deleting record 1 shifts record 2 into index 1, so `timeline.json#/1` re-binds to a different record. Pointer identity is array-positional, not event-id-based.

## 4. (b) Remove one map row — blind spot demonstrated exactly as specified

`mut-b-drop-j11-row`: row J11 (`relations.json#/0`) deleted **and** the map's self-declared inventory restated consistently (`**Expected inventory:** 13 JSON facts; 2 editorial rows; 15 total mapped rows; 11 distinct excerpt anchors.`). `mut-b2-drop-j05-row`: same with J05 (`entities.json#/4/first_appearance`).

```
$ python3 corpus/tools/support_check.py .ufo/…/F15-scratch/mut-b-drop-j11-row
INVENTORY JSON-FACTS 13/13; EDITORIAL-ROWS 2/2; TOTAL-ROWS 15/15; DISTINCT-ANCHORS 11/11
RECEIPT JSON-FACTS 13; EDITORIAL-ROWS 2; TOTAL-ROWS 15
SOURCE-SUPPORT 13/13; EDITORIAL-ANCHORS 2/2; … MODES 15/15; VALIDATED-ROWS 15/15
RESULT PASS                                                           exit=0

$ python3 corpus/tools/map_obligations.py .ufo/…/F15-scratch/mut-b-drop-j11-row
OBLIGATIONS raw=14 mapped=13
FINDING missing_obligation: relations.json#/0 has no map row
RESULT FAIL                                                           exit=1
```

`mut-b2-drop-j05-row` — `check_bible` CLEAN exit 0; `support_check` `INVENTORY JSON-FACTS 13/13; … DISTINCT-ANCHORS 11/11` / `RESULT PASS` exit 0; `map_obligations` `OBLIGATIONS raw=14 mapped=13` / `FINDING missing_obligation: entities.json#/4/first_appearance has no map row` / `RESULT FAIL` exit 1.

So a dropped JSON-fact row is invisible to `support_check` as long as the map's own counts are updated to match — precisely the counterexample C2 claims to close, and C2's tool does close it (`missing_obligation`, exit 1).

Contrast `mut-b3-row-only` (row deleted, stale inventory left at 14/2/16/12) — `support_check` notices only the count drift, not the obligation:

```
$ python3 corpus/tools/support_check.py .ufo/…/F15-scratch/mut-b3-row-only   (non-PASS lines)
INVENTORY JSON-FACTS 13/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 15/16; DISTINCT-ANCHORS 11/12
FAIL: inventory JSON facts mismatch: expected=14 parsed=13
FAIL: inventory total mapped rows mismatch: expected=16 parsed=15
FAIL: inventory distinct excerpt anchors mismatch: expected=12 parsed=11
RESULT FAIL                                                           exit=1
```

## 5. (c) Break one anchor span — `support_check` fails as specified

`mut-c-break-span`: J05's declared line span `17` → `20` (`claim-excerpt-map.md:26`), anchor text unchanged.

```
$ python3 corpus/tools/support_check.py .ufo/…/F15-scratch/mut-c-break-span   (non-PASS lines)
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16; DISTINCT-ANCHORS 12/12
FAIL J05: source-support; mode=verbatim; anchor=found; 17:> The Chalk Stair is the named rain-dark crossing between Quiet Rise and Salt Court.; span=20; outside-span=17
RECEIPT JSON-FACTS 14; EDITORIAL-ROWS 2; TOTAL-ROWS 16
SOURCE-SUPPORT 13/14; EDITORIAL-ANCHORS 2/2; … MODES 16/16; VALIDATED-ROWS 15/16
FAIL: J05: anchor hit outside declared line span 20 (hit lines: 17)
RESULT FAIL                                                           exit=1
```

`check_bible` CLEAN exit 0 and `map_obligations` PASS exit 0 on the same mutant (span is not their concern).

## 6. (d) Change one raw source_id — `map_obligations` fails as specified

`mut-d-source-id`: timeline event 3 `"source_id": "crossing-minute"` → `"paired-clock"` (the only occurrence of that string in `timeline.json`; the diff shows exactly one changed line).

```
$ python3 corpus/tools/map_obligations.py .ufo/…/F15-scratch/mut-d-source-id
OBLIGATIONS raw=14 mapped=14
FINDING source_id_mismatch: timeline.json#/2 does not bind to 'paired-clock'
RESULT FAIL                                                           exit=1
```

`check_bible` CLEAN exit 0 (both ids are declared sources, `check_bible.py:104-116` only checks resolvability) and `support_check` PASS exit 0 (`SOURCE-SUPPORT 14/14`) on the same mutant — again the raw-JSON blind spot that C2 closes.

## 7. Supplementary checks

- `python3 corpus/tools/map_obligations.py --self-test` → all 20 persisted cases PASS with the contract's expected exits/finding ids (`complete exit=0 findings=none` … `frozen_verdict_mismatch exit=2 findings=['frozen_verdict_mismatch']`), `RESULT PASS`, exit 0. Matches `corpus/tools/map-obligations-contract.json` case-for-case.
- Frozen replay control on the only snapshot present: `python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93` → `SNAPSHOT inputs=4 digests=verified` / `OBLIGATIONS raw=12 mapped=12` / `FROZEN expected=PASS/0 findings=none matched` / `RESULT PASS`, exit 0. No r94 snapshot exists.

## 8. Bottom line

**FAIL for mutation (a) as specified** — dropping one tick-9 id from the tick-10 `depends_on` leaves `check_bible` CLEAN (exit 0) and every other r94 check green, so the required "check_bible must report it" behaviour is contradicted (the dangling-reference variant `mut-a2` is reported); **(b), (c), (d) PASS exactly as specified** — `missing_obligation` exit 1 on both removed rows while `support_check` stays PASS with a self-consistent inventory, span break caught by `support_check` FAIL exit 1, source-id change caught by `map_obligations` FAIL exit 1; live tree verified byte-identical throughout.
