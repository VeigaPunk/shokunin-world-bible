# V39 — dialect-audit-2 (round 95)

Seat: V39 dialect-audit-2. Scope per seat spec: after P1 lands, (1) independently
recount r88 raw obligations from JSON by a different enumeration method than
V05's; (2) confirm the tool's dialect output matches both enumerations
one-to-one; (3) confirm anchor/span/mode agreement with the r88 map rows.

Verified revision: `corpus/tools/map_obligations.py` sha256
`d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108`
(P1's report `P1-tool-code.md` present; sha identical before and after my
29-run battery — recorded in `V39-scratch/probes-results.json` fields
`tool_sha256` / `tool_sha256_after`). Baseline `fb118c4`. All scratch work in
`.ufo/waves/round-95/seats/V39-scratch/`; the corpus was not modified (fixture
hashes below identical pre/post; `git status --porcelain -- corpus/fixtures/r88-m3-maya-cluster` empty).

## 1. Independent recount — my own method (distinct from V05's)

Method A: standalone recursive walker (no import of `corpus/tools`) that emits a
pointer for every dict field named `source_id` (parent pointer) and every
`first_appearance` (own pointer). Method B: text-level regex cross-count of
`"source_id"` / `"first_appearance"` occurrences per raw file, checked against
parsed array lengths. V05's method was a hand transcription of a fixed list with
character spans; both of mine are scripted and structural, so the two seats'
enumerations share no code and no manual step.

```
$ python3 .ufo/waves/round-95/seats/V39-scratch/enumerate_r88.py corpus/fixtures/r88-m3-maya-cluster
METHOD A obligations:
  entities.json/0/claims/0 -> paired-clock
  entities.json/0/first_appearance -> paired-clock
  entities.json/1/claims/0 -> paired-clock
  entities.json/1/first_appearance -> paired-clock
  entities.json/2/claims/0 -> paired-clock
  entities.json/2/first_appearance -> paired-clock
  entities.json/3/claims/0 -> paired-clock
  entities.json/3/first_appearance -> paired-clock
  timeline.json/0 -> paired-clock
  timeline.json/1 -> paired-clock
METHOD A count: 10
METHOD B text cross-count per file (source_id, first_appearance, expected):
  entities.json: (4, 4, 8)
  relations.json: (0, 0, 0)
  timeline.json: (2, 0, 2)
METHOD B count: 10
AGREE
exit=0
```

**Result: 10 raw source-attributed obligations** (4 `first_appearance` + 4 entity
claims + 2 timeline events; `relations.json` empty). Both methods agree.

## 2. Both enumerations vs the tool — one-to-one

- V05's list, extracted programmatically from its report (sha256
  `f6904a379886eaaab4190996790e7cab5292691f87ca897c5a53180656a49bea`, still the
  INTERIM version at extraction time): 10 pointers, 0 duplicates; set equality
  with my 10 confirmed (`equal: True`, `v05-only: []`, `v39-only: []`).
- My own markdown-table reader + dialect translator (`parse_r88_map.py`) maps the
  bracket cells to exactly the same 10 canonical pointers, all bound to
  `paired-clock`: `TOTAL rows=12 dialect_pointer_rows=10 nonpointer_rows=2`.
- Tool on the frozen revision:

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r88-m3-maya-cluster
OBLIGATIONS raw=10 mapped=10
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12
RESULT PASS
exit=0
```

`raw=10` equals both enumerations; `mapped=10` equals my map parse's fact-row
count. The 2 editorial rows (S1/S2) are counted only in the receipt
(`EDITORIAL-ROWS 2/2`), never as obligations — consistent with the map's own
"not extra JSON facts" statement and with C3's phrasing: the `12/12` in the round
claim is the declared **total-row** count (10 obligations + 2 editorial rows),
exactly as P1's report §6.1 states.

One-to-one is proven differentially, not just by counts (29 runs, all
pre-registered expectations met; full stdout in `V39-scratch/probes-results.json`):

| Probe (scratch copy, one change) | Observed on d1c239cc |
|---|---|
| 10 × single raw `source_id`/`first_appearance` mutation | exit 1, **exactly one** `source_id_mismatch` naming that pointer (e.g. `source_id_mismatch: entities.json#/0/first_appearance does not bind to 'v39-mutated'`) |
| all 10 raw values mutated at once | exit 1, exactly 10 findings whose pointer set equals my enumeration |
| 10 × single map-row drop (P1–P4, E1–E4, T1–T2) | exit 1, **exactly one** `missing_obligation` naming that row's pointer (e.g. `missing_obligation: timeline.json#/0 has no map row`) |
| 2 × editorial row drop, both editorial rows dropped | exit 0, no findings (receipt shows the count loss — see §5) |

Every single-point mutation/drop names exactly the pointer I enumerated and
nothing else, in both directions, so the tool's r88 row set is one-to-one with
my enumeration and with V05's.

## 3. Anchor / span / mode

Tool side: the dialect parser builds rows as `(pointer, source_id)` only
(`map_obligations.py:302-312`); the anchor/span/mode columns are neither read nor
rewritten, and the declared anchor count is captured by `EXPECTED_INVENTORY` but
unused (`_anchors`, `:264`). So the tool's contribution is that the 10+2 rows
pass through with their columns untouched.

Map side, independently verified by me (`check_anchor_span_mode.py`, no tool
import): for all 12 rows the declared `Excerpt path:line` resolves and the exact
anchor occurs on that line; every row's `R9 mode` (`verbatim`) equals the mode
declared in the map's R9 declarations table for that file;
`fictional-excerpts.md` line 3 itself declares `` `verbatim` ``. Distinct
`(span, anchor)` pairs = **8**, matching the declared `8 distinct excerpt
anchors`. Output ends `ANCHOR/SPAN/MODE AGREE` exit 0. (Note: `source-excerpt.md`
does not itself contain the word "verbatim"; its mode declaration lives in the
map's declarations table — recorded as an observation, not a defect.)

## 4. Dialect boundary and fail-closed controls (frozen revision)

```
canonical header + bracket cells   -> FINDING unsupported_map: co-mapped or unsupported pointer grammar   exit=2
co-mapped legacy cell              -> FINDING unsupported_map: pointer cells must contain one canonical inline-code pointer  exit=2
corpus/fixtures/r87-myth-cluster   -> FINDING unsupported_map: pointer cells must contain one canonical inline-code pointer  exit=2
corpus/fixtures/r89-inspiration-paraphrase -> FINDING unsupported_map: table needs one JSON fact pointer and one source-ID column  exit=2
corpus/fixtures/r93-m2-kojiki-cluster -> OBLIGATIONS raw=12 mapped=12 ... RESULT PASS  exit=0
corpus/fixtures/r94-paired-crossing   -> OBLIGATIONS raw=14 mapped=14 ... RESULT PASS  exit=0
```

The bracket grammar is gated to the legacy `JSON fact and fields` column only;
r87/r89 stay exit 2 as declared.

## 5. Bounded observation (evidence; corroborates P1 report §6.4)

The inventory receipt is not gated. Dropping the S1 editorial row:

```
OBLIGATIONS raw=10 mapped=10
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 1/2; TOTAL-ROWS 11/12 MISMATCH
RESULT PASS
exit=0
```

Dropping both editorial rows: `EDITORIAL-ROWS 0/2; TOTAL-ROWS 10/12 MISMATCH`,
still `RESULT PASS` exit 0. So a map whose declared inventory disagrees with its
parsed rows prints ` MISMATCH` but is not failed. This does not contradict C3 as
declared (C3 requires r88 in-tree → 12/12 PASS and r87/r89 fail-closed, both
observed) and P1 disclosed the bound itself; recorded here for the round's
adjudication as an un-gated receipt surface.

## 6. Corpus integrity (zero corpus modifications)

`sha256sum corpus/fixtures/r88-m3-maya-cluster/*` captured before P1 landed and
re-run after the battery: all 11 files identical, including
`claim-excerpt-map.md` `b3b79fe5…` and `entities.json` `042b6cc0…`;
`git status --porcelain` on the fixture is empty. The r88 pass comes from the
tool alone.

## Bottom line

PASS — on the frozen revision (`d1c239cc…`), my independent enumeration (two
methods, 10 obligations) and V05's list are the same set, the tool's r88 dialect
output matches both one-to-one (proven by 29 single-point differential probes,
all expectations met), the map rows' anchors/spans/modes are independently
confirmed consistent (12/12 anchors on declared lines, modes match declarations,
8 distinct anchors as declared), r87/r89 stay fail-closed at exit 2 with zero
corpus modifications; one bounded, non-contradicting observation recorded
(inventory receipt prints ` MISMATCH` without failing).
