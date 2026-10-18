# V24 — verdict-coverage (round 95)

Seat: V24 verdict-coverage. Scope per seat spec: read V05–V07, V15, V18; run my own
r88 dialect replay; issue exactly one COVERAGE verdict on the declared C3 (r88 dialect
under the gate; new fixture class instance) with named bounds.

Baseline: `fb118c4` (r94 closure). No commits, no pushes, no network, no repo writes
outside this report (all scratch work under `/tmp/v24/`).

## 0. Revision pins used by this report

```
baseline  corpus/tools/map_obligations.py  cc1df4dc406870b6fc4ddbc3291e3690cf87dfb061f76ec3b4fec5cfcfbab790  (691 lines, @fb118c4)
FROZEN    corpus/tools/map_obligations.py  d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108  (P1 delivered; stable 16:26:31 → end of verification)
FROZEN    corpus/tools/map-obligations-contract.json  8173bb97592a377716866737e8fcb4043014c9814e77a6248500d301a39170db  (22 cases; P2 delivered)
untouched corpus/tools/support_check.py   55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  (identical to pre-delivery capture)
```

Transient revisions seen while P1 was still editing (`74a88346`, `52d838b0`, `8eb5051d`,
`3f87fe8b`) are **not** verdict evidence. Two of them crashed on r93/r94/r95 with an
uncaught `ValueError: too many values to unpack (expected 2, got N)` in `compare()`
(mid-write state; also recorded by P5 §Findings.1); `3f87fe8b` still failed r88 with
`unsupported_map: co-mapped or unsupported pointer grammar` because the legacy branch
was reachable only when the canonical cell regex failed to match. All of that is
superseded by the frozen revision, which I re-measured end to end.

## 1. Before-state (baseline tool, my own run)

```
$ python3 /tmp/v24/map_obligations.baseline.py corpus/fixtures/r88-m3-maya-cluster
FINDING unsupported_map: table needs one JSON fact pointer and one source-ID column
RESULT ERROR
EXIT=2
```

Baseline CLI sweep over **all `corpus/fixtures/*/` (169 dirs at sweep time, including the
just-created empty r95 dir)**, recorded `/tmp/v24/before.txt`:

```
164 × exit 2  FINDING map_missing: expected exactly one conventional claim-to-excerpt map
  3 × exit 2  FINDING unsupported_map: table needs one JSON fact pointer and one source-ID column
              (r87-myth-cluster, r88-m3-maya-cluster, r89-inspiration-paraphrase)
  2 × exit 0  r93 OBLIGATIONS raw=12 mapped=12 ; r94 OBLIGATIONS raw=14 mapped=14
```

Consistent with the r94 census declaration (`corpus/fixtures/README.md:1173`: 168 dirs),
since the 169th dir is the r95 fixture.

## 2. Frozen-revision r88 replay (C3 after-state)

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r88-m3-maya-cluster     # d1c239cc
OBLIGATIONS raw=10 mapped=10
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12
RESULT PASS
exit=0
```

The r88 dialect is accepted and the acceptance binds real obligations. Independent
enumeration of the r88 raw obligations (10, all `paired-clock`) and of the map's cells
(tool's own parser, `PYTHONDONTWRITEBYTECODE=1 python3 -B` import, no repo writes):

```
entities.json#/0/first_appearance  <- `entities[0].first_appearance`              (P1)
entities.json#/0/claims/0          <- `entities[0].claims[0]`                     (E1)
entities.json#/1/first_appearance  <- `entities[1].first_appearance`              (P2)
entities.json#/1/claims/0          <- `entities[1].claims[0]`                     (E2)
entities.json#/2/first_appearance  <- `entities[2].first_appearance`              (P3)
entities.json#/2/claims/0          <- `entities[2].claims[0]`                     (E3)
entities.json#/3/first_appearance  <- `entities[3].first_appearance`              (P4)
entities.json#/3/claims/0          <- `entities[3].claims[0]`                     (E4)
timeline.json#/0                   <- `timeline[0]` (`description`, `source_id`)  (T1)
timeline.json#/1                   <- `timeline[1]` (`description`, `source_id`)  (T2)
```

`legacy_pointer()` translates exactly these four cell shapes
(`entities[i].first_appearance`, `entities[i].claims[j]`, `timeline[i]`, `relations[i]`)
and the gate is keyed on the legacy pointer-column role `JSON fact and fields`
(`parse_pointer_cell(cell, legacy=True)` tries the legacy branch first at `:173-179`).

## 3. Discrimination controls on the frozen revision (r88 copies under /tmp, no repo writes)

| Probe (mutation of an r88 copy) | Observed |
|---|---|
| T2 row deleted | exit 1 `missing_obligation: timeline.json#/1 has no map row` (`raw=10 mapped=9`) |
| phantom row `entities[9].first_appearance` added | exit 1 `phantom_obligation: entities.json#/9/first_appearance is not a raw source-attributed obligation` |
| T2 row duplicated | exit 1 `duplicate_mapping: timeline.json#/1 appears 2 times` |
| T1 source `paired-clock` → `veil-verse` | exit 1 `source_id_mismatch: timeline.json#/0 does not bind to 'paired-clock'` |
| P1 cell → bare `` `entities[0]` `` | exit 2 `unsupported_map: co-mapped or unsupported pointer grammar` |
| T2 cell → `` `timeline[1].description` `` (r87 field-path style) | exit 2 `unsupported_map: pointer cells must contain one canonical inline-code pointer` |
| E1 cell → two-token co-map `` `entities[0].claims[0]`, `entities[0].first_appearance` `` | exit 2 `unsupported_map: pointer cells must contain one canonical inline-code pointer` |
| `**Expected inventory:**` tampered to 11/2/13 | exit 0 `INVENTORY JSON-FACTS 10/11; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/13 MISMATCH` — receipt is echoed, not gated |

Harness note (honesty): my first source-ID-mismatch probe was a **no-op edit** — the T1
cell carries a `: <description>` suffix, so my replace string did not match and the
guard assert tripped on a pre-existing `veil-verse` mention elsewhere in the file. The
resulting "exit 0 PASS" was my harness's false negative, not a tool hole; the corrected
probe (verified landed by `grep '^| T1 |'` before running) fails closed as shown above.

## 4. Fail-closed controls and corpus-wide regression surface (frozen revision)

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r87-myth-cluster
FINDING unsupported_map: pointer cells must contain one canonical inline-code pointer
RESULT ERROR   exit=2

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r89-inspiration-paraphrase
FINDING unsupported_map: table needs one JSON fact pointer and one source-ID column
RESULT ERROR   exit=2
```

Full sweep, baseline vs frozen revision (`/tmp/v24/before.txt` vs `/tmp/v24/after-frozen.txt`),
compared as `dir|exit|first-finding-or-OBLIGATIONS` — **exactly 3 changed lines**:

```
r87-myth-cluster        exit 2 → exit 2   (detail moved to the pointer-cell class; class unchanged)
r88-m3-maya-cluster     exit 2 → exit 0   OBLIGATIONS raw=10 mapped=10     <- the declared C3 change
r95-crossing-aftermath  exit 2 → exit 0   OBLIGATIONS raw=15 mapped=15     <- P4's map landing
```

Post-state distribution: 4 × exit 0 (r88, r93, r94, r95), 165 × exit 2, 0 × exit 1. No
other fixture changed acceptance; nothing flipped to exit 0 that should not have. r87
must stay rejected because its cells co-map several field paths in one comma list; r89
because its headers are `Claim pointer` / `In-world source` (no "ID").

Frozen-snapshot replay also re-measured green:
`--frozen .ufo/waves/round-94/frozen/map-obligations-r93` → `SNAPSHOT inputs=4
digests=verified` / `OBLIGATIONS raw=12 mapped=12` / `FROZEN expected=PASS/0 findings=none
matched` / `RESULT PASS`, exit 0.

## 5. New fixture class instance — r95-crossing-aftermath under the gate

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
RESULT PASS   exit=0
```

Parsed-row comparison via the tool's own parser (r94 map vs r95 map):

```
r94 rows: 14   r95 rows: 15
first 14 identical: True
new row: ('timeline.json#/3', 'aru-aftermath-note')      raw obligation timeline.json#/3 = aru-aftermath-note
r95 findings: []
```

Negative control (copy in /tmp, J15 row deleted):

```
OBLIGATIONS raw=15 mapped=14
FINDING missing_obligation: timeline.json#/3 has no map row
RESULT FAIL   exit=1
```

The new row is load-bearing and binds the tick-11 event's own source. `support_check` on
r95: `INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17; DISTINCT-ANCHORS
13/13` + `SOURCE-SUPPORT 15/15; … MODES 17/17; VALIDATED-ROWS 17/17`, exit 0.
`check_bible.py` on r95: `CLEAN: schema, citations, relations, timeline; 0 violations`,
exit 0.

## 6. "Zero corpus modifications" and unchanged receipts

```
$ git status --porcelain corpus/fixtures/r88-m3-maya-cluster corpus/fixtures/r87-myth-cluster \
      corpus/fixtures/r89-inspiration-paraphrase corpus/fixtures/r93-m2-kojiki-cluster corpus/fixtures/r94-paired-crossing
(empty)
$ git diff fb118c4 --stat -- corpus/fixtures/r88-m3-maya-cluster corpus/fixtures/r93-m2-kojiki-cluster corpus/fixtures/r94-paired-crossing
(empty)
```

The r88 fixture was not rewritten to make the tool pass. `support_check.py` sha256 is
byte-identical to my pre-delivery capture, and the receipt stdout sha256 for r88
(`bd2d46ca005f7492…`), r93 (`25631d31b1de299f…`) and r94 (`c028de7c17d1bb81…`) are
identical before and after delivery, with `MODES 12/12` / `15/15` / `16/16` unchanged:

```
r88  INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12; DISTINCT-ANCHORS 8/8
     SOURCE-SUPPORT 10/10; EDITORIAL-ANCHORS 2/2; … MODES 12/12; VALIDATED-ROWS 12/12   exit 0
r93  … SOURCE-SUPPORT 12/12; EDITORIAL-ANCHORS 3/3; … MODES 15/15; VALIDATED-ROWS 15/15 exit 0
r94  … SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 2/2; … MODES 16/16; VALIDATED-ROWS 16/16 exit 0
```

(For the record: V05 §2's `DISTINCT-ANCHORS 8/8` quote is real — it is printed earlier in
the same `support_check` output than the `RECEIPT`/`SOURCE-SUPPORT` lines. No
contradiction; I checked before flagging it.)

## 7. Read set

- **V05** (`.ufo/waves/round-95/seats/V05-c3-dialect-r88.md`, sha256 `f6904a379886eaaa…`,
  mtime 16:21:43) — read. It is still the **interim** version written before P1 landed:
  baseline before-state, independent hand enumeration of the 10 raw obligations, hand
  check of the 12 declared anchors/spans/modes, dialect survey, fixture hashes, bottom
  line INCONCLUSIVE. Its expectations (10 obligations, 12 mapped rows, 8 anchors, all
  `verbatim`) agree with what I measured at the frozen revision; it contains no
  delivered-revision claim yet, so nothing in it contradicts my verdict.
- **V07** (`.ufo/waves/round-95/seats/V07-c3-receipts-unchanged.md`) — read; complete
  report, pinned to the same frozen revision `d1c239cc` and the same untouched
  `support_check.py` sha256. It corroborates my §6 with a stronger method (Git blob
  identity plus literal `cmp` for 24 map+JSON files, full-tree `git ls-tree` equality for
  all four fixture dirs, and pre/post receipt runs at 16:17 vs post-P1). Bottom line
  PASS; its four receipts (r88 10+2, r93 12+3, r94 14+2, r87 14+8) match mine exactly.
  No contradiction with my verdict.
- **V06, V15, V18** — **ABSENT** at report time (polled at 20 s cadence beyond the
  protocol cutoff, plus an extended ~8-minute re-poll; the only entry under those
  prefixes was the scratch dir `V06-scratch/`). Per the poll-wait rule I do not verify
  against a plan: their conclusions are recorded here as ABSENT, and my verdict rests on
  my own measurements plus V05/V07.

## 8. COVERAGE verdict on C3 (exactly one)

**COVERAGE: IMPROVED (bounded) — C3's three clauses verify on the frozen revision
`d1c239cc`; the declared "12/12" figure is traceable but is not an obligation count.**

- r88 before → after: exit 2 `unsupported_map` → exit 0 with
  `OBLIGATIONS raw=10 mapped=10` + `INVENTORY … TOTAL-ROWS 12/12` (§1, §2). The declared
  "12/12" is the r88 map's **declared total mapped rows** (10 JSON facts + 2 editorial),
  which the delivered tool now echoes as `TOTAL-ROWS 12/12`; the tool's obligation counter
  reads **10/10** because `relations.json` is empty and editorial rows are not
  obligations. Both numbers appear, correctly labelled, on the same exit-0 run — so the
  claim is measurable, but "12/12" must not be read as 12 obligations.
- r87/r89 stay exit 2 fail-closed (§4); the full 169-dir sweep changes exactly the two
  intended fixtures plus r87's finding detail text.
- `support_check` receipts on r88 (10 JSON + 2 editorial), r93, r94 unchanged, and no
  fixture bytes changed (§6).
- New fixture class instance: r95 under the gate is 15/15 with the 14 inherited rows
  parse-identical to r94 and the new row binding `timeline.json#/3 ← aru-aftermath-note`;
  removing that row fails closed (§5).

Named bounds (what this verdict does **not** cover):

1. **Denominator bound.** "12/12" = declared total rows (10 obligations + 2 editorial),
   not obligations; the tool's own count is `raw=10 mapped=10`.
2. **Grammar bound.** Acceptance is limited to the legacy column role `JSON fact and
   fields` plus the four bracket cell shapes; bare `entities[i]`, field paths
   (`timeline[1].description`), and co-mapped multi-token cells stay exit 2 — all
   verified by probes (§3).
3. **Gate-strength bound.** Acceptance is discriminating for missing / phantom /
   duplicate / source-ID-mismatch rows (§3), but the `INVENTORY` receipt is echoed and
   not gated (a tampered inventory line exits 0 with a ` MISMATCH` suffix, §3), matching
   P1's disclosed residual §6.4.
4. **Scope bound.** Tool surface only. This verdict says nothing about excerpt support,
   entailment, translation fidelity, canon, breach, or identity — `support_check`'s
   receipt is lexical preflight, and the r88/r95 excerpt claims are not re-adjudicated here.
5. **Revision bound.** The verdict is pinned to `d1c239cc` / contract `8173bb97`. Earlier
   in-flight revisions (one of which crashed on r93/r94/r95) are excluded by
   construction; any later edit invalidates this measurement.
6. **Read-set bound.** V06/V15/V18 are ABSENT (§7); the verdict does not depend on them
   but also does not incorporate any cross-check they might have provided. V05 (interim)
   and V07 (complete) were read and neither contradicts the verdict.

## 9. Bottom line

PASS — C3 coverage verified on frozen revision `d1c239cc`: r88 flips exit 2 → exit 0 with
all 10 obligations bound (12/12 total mapped rows), r87/r89 stay exit 2, the corpus-wide
diff shows only the two intended acceptances, receipts and fixture bytes are unchanged,
and every discrimination/edge probe fails closed; bound: the "12/12" headline is the
map's total-row count, not an obligation count (tool prints `raw=10 mapped=10`), and
V06/V15/V18 were ABSENT (V05 interim, V07 complete and corroborating).
