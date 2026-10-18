# V11 — c3-support-map (round 98)

**Seat:** V11 `c3-support-map` (verifier)
**Scope:** C3/depth — run `support_check.py` and `map_obligations.py` on the delivered
`corpus/fixtures/r98-clerk-filing/` (expected `map_obligations` `raw=20 mapped=20` PASS), and
re-run both tools on the repaired `corpus/fixtures/r95-crossing-aftermath/` to confirm the r95
receipts are unchanged by S3's carried-wording repair (quote old vs new).
**Report path (exclusive):** `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-98/seats/V11-c3-support-map.md`
**Baseline:** r97 closure `9a3d648`. All commands run from the lane root
`/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`.
**Scratch:** `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-98/seats/V11-scratch/`
(absolute lane path).

**STATUS: COMPLETE — both halves verified. r98 `map_obligations` raw=20 mapped=20 PASS and
`support_check` 20/20 PASS (section 5); r95 receipts unchanged by S3's repair (sections 1–4).**

## 0. Poll-wait record

Targets: S3's `corpus/fixtures/r98-clerk-filing/{entities,sources,timeline}.json` (+ authored
`fictional-excerpts.md`), S4's `corpus/fixtures/r98-clerk-filing/{README.md,claim-excerpt-map.md}`,
and both producer reports under `.ufo/waves/round-98/seats/`. Poller
`V11-scratch/poll.sh` (20 s cadence, 40 tries) logged to `V11-scratch/poll.log`.

| Time | Observation |
|---|---|
| 20:27:45 (try 1) | r98 dir absent (`files=0/2`, `fixdir_entries=0`) |
| 20:28:25 (try 3, poller v1) | **false READY** — poller v1 matched `S4-scratch/` (a *directory*) and reported its contents (`inherited-rows-draft.txt`) as a "report". Not a report; **nothing was verified** at that moment. Poller rewritten to require an `S4*.md` *file* plus moved table bytes. |
| 20:29:08 (v2 try 1) | `entities=moved timeline=moved sources=moved map=same` — S3's tables landed; S4's map still a byte-copy of r97's; no producer reports |
| 20:30:48 (v2 try 6) | `map=moved` — S4's map rewrite landed (still no reports) |
| 20:31:08 (v2 try 7) | `S3report=S3-fixture-author.md` |
| **20:32:08 (v2 try 10)** | **READY** — `S3report=S3-fixture-author.md S4report=S4-fixture-docs.md`, all four owned files moved off r97's bytes. Verification began at 20:32:11. |

Verification of the r98 half started only after S4's own `README.md` + `claim-excerpt-map.md` had
moved off r97's bytes **and** both producer reports existed. The placeholder state seen at
20:28:25–20:30:48 (map and README still r97 byte-copies, `map=same`) was **not** verified — running
the tools then would have scored an unfinished artifact and produced a false FAIL. No stall-escape
and no ABSENT condition arose for this seat.

## 1. Revisions — r95 half

`corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md`:

| Revision | sha256 | Note |
|---|---|---|
| pristine = `git show 9a3d648:…` | `30281ff1a497bbe66f23cbd8a49befb3319595f20990718a0ffe8050741a874a` | baseline bytes |
| pre-repair working tree (captured 20:27:59) | `30281ff1a497bbe66f23cbd8a49befb3319595f20990718a0ffe8050741a874a` | identical to pristine — capture is genuinely pre-repair |
| post-repair working tree (20:28:34, hashed 20:29:17) | `80440d61122488a267a4f0a58a55cb54d89c037d93160f1123e5fb3b2f396f61` | S3's repair |

Tool revisions bracketing every r95 receipt (unchanged across the window):

- `support_check.py` `55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c`
- `map_obligations.py` `86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9`
- `map-obligations-contract.json` `2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41`

(Note: these are S1's pre-C1 revisions. S1 owns `dependency_freeze.py` +
`dependency-freeze-contract.json` only; the two tools this seat exercises are byte-stable at the
hashes above across my whole window, checked again at every receipt.)

## 2. r95 `support_check.py` — receipts UNCHANGED

```
$ python3 corpus/tools/support_check.py corpus/fixtures/r95-crossing-aftermath
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17; DISTINCT-ANCHORS 13/13
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
PASS J01: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS J02: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS J03: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS J04: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS J05: source-support; mode=verbatim; anchor=found; 17:> The Chalk Stair is the named rain-dark crossing between Quiet Rise and Salt Court.
PASS J06: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS J07: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS J08: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS J09: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS J10: source-support; mode=verbatim; anchor=found; 18:> After both Tick 9 entries above, Aru and Evin met at the Chalk Stair at tick 10.
PASS J11: source-support; mode=verbatim; anchor=found; 19:> There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.
PASS J12: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS J13: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS J14: source-support; mode=verbatim; anchor=found; 20:> Their tick-10 decision depends on both ninth-bell entries: Aru's north-lantern entry at Quiet Rise and Evin's south-bell entry at Salt Court. After agreeing to share stewardship for this crossing only, they chalked one temporary route mark together at the midpoint.
PASS J15: source-support; mode=verbatim; anchor=found; 26:> Tick 11: I waited at the Chalk Stair through the agreed bell.
PASS S01: editorial-row; mode=verbatim; anchor=found; 5:> The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that event. […] He called out “Earth,” and the solid land appeared.
PASS S02: editorial-row; mode=verbatim; anchor=found; 5:> The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that event. […] He called out “Earth,” and the solid land appeared.
RECEIPT JSON-FACTS 15; EDITORIAL-ROWS 2; TOTAL-ROWS 17
SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 17/17; VALIDATED-ROWS 17/17
RESULT PASS
exit=0
```

**`RESULT PASS`, exit 0**, `stderr` empty. 22 output lines, byte-identical across all four
comparisons below.

## 3. r95 `map_obligations.py` — receipts UNCHANGED

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
RESULT PASS
exit=0
```

**`raw=15 mapped=15`, `RESULT PASS`, exit 0**, no `FINDING` line, `stderr` empty.

## 4. r95 — machine-checked receipt equality (four comparisons)

Files: `V11-scratch/r95-support-{prerepair,pristine,postrepair}.txt` (22 lines each),
`V11-scratch/r95-mapobl-{prerepair,pristine,postrepair}.txt` (3 lines each).
`pristine` = the r95 fixture re-materialized from `git show 9a3d648:…` into
`V11-scratch/r95-pristine/` and run there, so the "unchanged" claim rests on the committed baseline
bytes, not only on my 20:27:59 timing.

```
support:   prerepair(20:27:59) vs pristine(9a3d648)  → IDENTICAL: True
mapobl:    prerepair           vs pristine           → IDENTICAL: True
support:   pristine            vs post-repair        → IDENTICAL: True
mapobl:    pristine            vs post-repair        → IDENTICAL: True
```

So the r95 receipts are unchanged both **across the repair** and **against the committed
baseline**, and the pristine-vs-prerepair identity independently confirms my pre-capture was taken
before any repair byte landed.

### 4a. The repair is prose-only — diff and data-row check

`diff -u <(git show 9a3d648:…/claim-excerpt-map.md) <working tree>` = **exactly one hunk, one
changed line (line 49)**, inside the `## Timeline normalization and scope` prose paragraph:

- OLD: `The new relation encodes only the agreement for this crossing, not perpetual performance or alliance.`
- NEW: `The relation encodes only the agreement for this crossing, not perpetual performance or alliance; the new tick-11 aftermath event records one reported non-arrival on one occasion.`

The stale wording ("the new relation") was wrong for r95 — that round added a tick-11 *event*
(the inherited `relations.json#/0` row J11 is unchanged from r94), so the repaired sentence now
attributes "new" to the right record. No table row, header, delimiter, pointer cell, anchor, line
span, or `**Expected inventory:**` declaration is touched; the diff has no `|` lines at all. This
matches C3's claim that the r95 repair leaves the receipts unchanged — and the receipts were
**measured**, not assumed (sections 2–4).

`git status --porcelain` at 20:29 confirms the r95 fixture's only modified file is
`claim-excerpt-map.md` (plus `M LOG.md`, `?? .ufo/waves/round-98/`, `?? corpus/fixtures/r98-clerk-filing/`).

## 5. r98 `support_check.py` + `map_obligations.py` — both PASS

### 5.0 Revisions verified

`corpus/fixtures/r98-clerk-filing/` (sha256, stable 20:32:14 → 20:32:41 across every receipt):

| File | sha256 | bytes | vs r97 |
|---|---|---:|---|
| `claim-excerpt-map.md` | `c1099d0ee9eece241ea1f796320a84453dfc6b6aec33b7b9dd7e39bbef4a94ba` | 15028 | new (S4) |
| `README.md` | `32efc78f70e6de4f9670134080711923199e8693015d3ebea75a4a1ca6362926` | 5829 | new (S4) |
| `entities.json` | `db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984` | — | new (S3) |
| `sources.json` | `32ee15b1f3d72d94f4228cbc9cefa69b7185d18b47bbe219833d7aaf30eed0f3` | — | new (S3) |
| `timeline.json` | `eb24e0848e597efa29ed858cb8557d8f3126a47e1231f9469d719257e191e7af` | — | new (S3) |
| `fictional-excerpts.md` | `29e384bf2eb2ab80858ace9423f29088a552553f87da7f6a9b694cbb050666de` | — | new (S3) |
| `relations.json` | `c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9` | — | byte-copy of r97 |
| `contradictions.json` | `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` | — | byte-copy of r97 |
| `inspiration-note.md` | `58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37` | — | byte-copy of r97 |
| `source-excerpt.md` | `b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd` | — | byte-copy of r97 |

Both S4-declared hashes reproduce exactly (`claim-excerpt-map.md` `c1099d0e…`, `README.md`
`32efc78f…`, and S4's byte counts 15,028 / 5,829 match). Tools unchanged across the whole window:
`support_check.py` `55a5eb27…`, `map_obligations.py` `86b52949…`, contract `2142b991…` (re-hashed
20:32:41). S1's C1 edits touch only `dependency_freeze.py` (`03d04365…`) and
`dependency-freeze-contract.json` (`3a940a9f…`) — neither tool this seat exercises.

### 5.1 Required command — `support_check.py` on r98

```
$ python3 corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 18/18
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
PASS J01: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS J02: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS J03: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS J04: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS J05: source-support; mode=verbatim; anchor=found; 17:> The Chalk Stair is the named rain-dark crossing between Quiet Rise and Salt Court.
PASS J06: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS J07: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS J08: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS J09: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS J10: source-support; mode=verbatim; anchor=found; 18:> After both Tick 9 entries above, Aru and Evin met at the Chalk Stair at tick 10.
PASS J11: source-support; mode=verbatim; anchor=found; 19:> There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.
PASS J12: source-support; mode=verbatim; anchor=found; 12:> Tick 9: Aru carried the north lantern at Quiet Rise.
PASS J13: source-support; mode=verbatim; anchor=found; 13:> Tick 9: Evin held the south bell at Salt Court.
PASS J14: source-support; mode=verbatim; anchor=found; 20:> Their tick-10 decision depends on both ninth-bell entries: Aru's north-lantern entry at Quiet Rise and Evin's south-bell entry at Salt Court. After agreeing to share stewardship for this crossing only, they chalked one temporary route mark together at the midpoint.
PASS J15: source-support; mode=verbatim; anchor=found; 26:> Tick 11: I waited at the Chalk Stair through the agreed bell.
PASS J16: source-support; mode=verbatim; anchor=found; 37:> Tick 12: I was at Salt Court through the same agreed bell.
PASS J17: source-support; mode=verbatim; anchor=found; 48:> Tick 13: I received Evin's response at the Chalk Stair.
PASS J18: source-support; mode=verbatim; anchor=found; 60:> I am Maren, clerk of the Chalk Stair registry, and I record the matter OPEN.
PASS J19: source-support; mode=verbatim; anchor=found; 59:> Tick 14: I filed both pending accounts at the Chalk Stair registry.
PASS J20: source-support; mode=verbatim; anchor=found; 59:> Tick 14: I filed both pending accounts at the Chalk Stair registry.
PASS S01: editorial-row; mode=verbatim; anchor=found; 5:> The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that event. […] He called out “Earth,” and the solid land appeared.
PASS S02: editorial-row; mode=verbatim; anchor=found; 5:> The beginning of this interesting book is taken up with the Kiche story of the creation, and what occurred directly subsequent to that event. […] He called out “Earth,” and the solid land appeared.
RECEIPT JSON-FACTS 20; EDITORIAL-ROWS 2; TOTAL-ROWS 22
SOURCE-SUPPORT 20/20; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22; VALIDATED-ROWS 22/22
RESULT PASS
exit=0
```

**`RESULT PASS`, exit 0**, `stderr` empty, 27 output lines, byte-identical across two consecutive
runs (`V11-scratch/r98-support-run{1,2}.txt`, `diff -q` clean). The map's own declaration
(`**Expected inventory:** 20 JSON facts; 2 editorial rows; 22 total mapped rows; 18 distinct
excerpt anchors.`, map line 5) is satisfied on all four counts.

### 5.2 Required command — `map_obligations.py` on r98

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r98-clerk-filing
OBLIGATIONS raw=20 mapped=20
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22
RESULT PASS
exit=0
```

**`raw=20 mapped=20`, `RESULT PASS`, exit 0** — **matches the claim exactly**, with no `FINDING`
line (no `missing_obligation`, no `phantom`, no `inventory_mismatch`, no `dual_pointer`), `stderr`
empty, stable across two runs (`V11-scratch/r98-mapobl-run{1,2}.txt`).

### 5.3 What the round actually added — receipt diff vs r97

`diff` of the r97 receipt against the r98 receipt isolates the change to exactly three new PASS
lines plus the count lines (17 inherited PASS lines byte-identical, including their excerpt line
numbers 12/13/17/18/19/20/26/37/48 and the editorial rows at line 5):

```
1c1
< INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19; DISTINCT-ANCHORS 15/15
---
> INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 18/18
19a20,22
> PASS J18: … 60:> I am Maren, clerk of the Chalk Stair registry, and I record the matter OPEN.
> PASS J19: … 59:> Tick 14: I filed both pending accounts at the Chalk Stair registry.
> PASS J20: … 59:> Tick 14: I filed both pending accounts at the Chalk Stair registry.
```

`DISTINCT-ANCHORS 15→18` = the three new rows' three distinct anchor strings. Every new anchor
lies inside its declared span (J18 anchor 60 in span `60`; J19 anchor 59 in span `59-60`; J20
anchor 59 in span `55-64`), and all three resolve inside the **appended** excerpt section only
(r98 `fictional-excerpts.md` lines 54–64; r97's file ends at line 53), so no inherited anchor
changed meaning.

### 5.4 Independent recount and parsed-row inheritance

Independent recount from the raw tables (not via the tool): r98 `first_appearance=6, claims=6,
relations=1, timeline=7` → **20**; `sources=7` (r97: `5/5/1/6 = 17`, `sources=6`). Via the tool's
own `map_obligations.raw_obligations()`: `obligations=20` (r97: 17). The three new pointer tokens
are `entities.json#/5/first_appearance`, `entities.json#/5/claims/0`, `timeline.json#/6`, all bound
to source `clerk-filing-note` — the same three S4 records S3's interim run flagged as
`missing_obligation` before the map rewrite, now discharged.

Parsed-row inheritance using the tools' own parser (`support_check.parse_map`), ID-keyed:

```
inv97 (17, 2, 19, 15) → inv98 (20, 2, 22, 18)
new ids: ['J18','J19','J20']   dropped: []
field diffs on inherited rows (kind/mode/anchor/path/span, all 19 rows): 0
```

So all 19 inherited rows (J01–J17 + S01/S02) are **parse-value identical**; the only additions are
J18/J19/J20. JSON-level inheritance likewise holds: `entities.json`, `relations.json`,
`timeline.json`, `sources.json`, `contradictions.json` all `prefix_identical=True` vs r97, and
`fictional-excerpts.md` r97 (53 lines) is a strict byte-prefix of r98's (64 lines), the appended
section being lines 54–64.

**One scoped correction to S4's report (receipt-neutral).** S4's scratch check reports
`map_line_numbers_identical: True`. That holds for the 17 JSON rows (J01–J17 at lines 22–38 in both
maps) but **not** for the two editorial rows, which move because the three new rows are inserted
inside the JSON section: `S01` 46 → 49 and `S02` 47 → 50 (`grep -nE "^\| S0[12] "` on both maps).
S4's sentence does name J01–J17 explicitly, so the claim is accurate as scoped; the bare label is
the over-generalization. This is not a defect in the artifact and not a receipt change —
`map_obligations` compares rows as a set, and `support_check` re-derives the editorial anchors at
line 5, which did not move.

Corroboration only (V13's gate, not mine): `python3 corpus/fixtures/check_bible.py
corpus/fixtures/r98-clerk-filing` → `CLEAN: schema, citations, relations, timeline; 0 violations`,
exit 0.

## 6. Limitations

- My receipts are lexical/map-declared preflight (row inventory, fixed-string anchors, spans, R9
  modes, pointer↔row binding). Whole-claim entailment, the no-finding/no-resolution bound, and
  canon truth are manual/adversarial reviews — other seats' scope.
- Receipts are bracketed to the three tool hashes in section 1 (`support_check.py` `55a5eb27…`,
  `map_obligations.py` `86b52949…`, contract `2142b991…`), re-hashed at 20:32:41 at the end of my
  window; if either tool revision moves again during the round, sections 2–5 must be re-run at
  closure. S1's C1 revision of `dependency_freeze.py` / `dependency-freeze-contract.json` does not
  touch these two tools.
- `map_obligations` maps obligations one-to-one and `support_check` checks fixed-string anchors and
  declared spans; neither reads the *meaning* of the new clerk-filing record. The claim that the
  record asserts no finding / no resolution is a prose bound (map lines 62–66, README) and is
  V13's / the adversarial seats' scope, not mine.
- The two new editorial-row line numbers are not asserted anywhere in my receipts; I checked them
  only because S4's report claimed line-number stability (section 5.4).

**Bottom line: PASS** — on the delivered r98 bytes (`claim-excerpt-map.md` `c1099d0e…`, README
`32efc78f…`), `support_check` reports `20/20; 2/2; 22/22; 18/18` with `RESULT PASS` (exit 0) and
`map_obligations` reports **`raw=20 mapped=20`** with `RESULT PASS` (exit 0) — the C3 expectation
met, the three new tokens (`entities.json#/5/first_appearance`, `entities.json#/5/claims/0`,
`timeline.json#/6`) mapped, all 19 inherited rows parse-value identical; and S3's r95 repair is
prose-only, leaving the r95 receipts byte-identical both across the repair and against the
committed `9a3d648` baseline. One scoped correction to S4's report (editorial rows S01/S02 move
46/47 → 49/50; its stated J01–J17 claim holds) — receipt-neutral, no finding on the artifact.
