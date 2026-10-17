# JCOV3 — Denominators judge (round-92 FOLLOW-UP, world-bible lane)

Seat JCOV3. Judgment surface: committed tree `HEAD = c4d4823b9a8165a88e8199af136e62d6e961b6b9`
(baseline `396c568`); `git status --porcelain --untracked-files=no` was empty at judgment start
and finish — untracked entries exist only inside `.ufo/waves/round-92/followup/` and are
follow-up seats' artifacts. Mission: independent recount (r87 14+8; r88-m3 10 JSON + 2
editorial); every map row pointer resolves; the Inventory lines match. No commit, no push.
This seat's repo writes: this report and `JCOV3-census.json`. Scratch was `/tmp/jcov3-before`
(removed; final cleanup line `cleaned=0`; `df -i /tmp` stayed at 99% throughout, no scratch
leak).

## Work performed

- Ran the prescribed two 60-second wait-checks first (receipt below). HEAD stayed at
  `c4d4823` and the tracked tree stayed clean; peer follow-up artifacts (SF1/SF2 present,
  then H4/JCAL1/JCAL3 and later JCOV1/JCOV2/H3 files appearing) were visible through `ls`
  only and were not used as evidence anywhere in this report.
- Built an independent parser/walker (`PYTHONDONTWRITEBYTECODE=1 python3 -I - <<'PY' …`,
  stdin driver; it never imports `corpus/tools/support_check.py`). It parses the three maps
  carrying an `**Expected inventory:**` line and, on the committed tree:
  - recounts JSON / editorial / total rows and distinct `(excerpt path, exact anchor)` pairs;
  - resolves every backticked JSON pointer (`entities[i]…`, `relations[i]…`, `timeline[i]…`,
    and r89's `entities.json#/0/claims/0` JSON-pointer form) against the cluster JSON;
  - checks every row's `source_id` cell against `sources.json`;
  - checks each declared `path:line` actually contains its exact anchor, and records
    off-line hits;
  - compares r87's ten quoted statements/descriptions byte-for-byte against the JSON values;
  - checks r88 S1/S2's `symbolism-clause-map.md:7` / `:8` pointers carry the cited clause
    text in-line;
  - lists declared excerpt paths that no row references (the WARN's subject).
- Cross-checked my numbers against the delivered checker's `INVENTORY`/`RECEIPT` lines on the
  committed tree, and against the r91 baseline map extracted from `396c568` into scratch to
  isolate the WARN-closure claim from the tool change.
- Full arithmetic is in `JCOV3-census.json` (validated with `json.load`; declared == counted,
  `inventory_match=true` for all three maps).
- Checker provenance measured in-session: `corpus/fixtures/check_bible.py` sha256
  `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` (the unchanged pin);
  `corpus/tools/support_check.py` sha256
  `55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c`.

## Before → after measurements

**Wait-checks (t=60s, t=120s).** Command:

```sh
for i in 1 2; do sleep 60; printf 'WAITCHECK t=%ss HEAD=%s dirty=%s peers=' "$((i*60))" "$(git rev-parse --short HEAD)" "$(git status --porcelain | wc -l)"; ls .ufo/waves/round-92/followup/ | tr '\n' ',' ; echo; done
```

Observed:

```text
WAITCHECK t=60s HEAD=c4d4823 dirty=0 peers=SF1-freeze.json,SF1.md,SF2.md,
WAITCHECK t=120s HEAD=c4d4823 dirty=3 peers=H4-census.json,H4-probes.json,JCAL1-delta.json,SF1-freeze.json,SF1.md,SF2.md,
WAIT_TERMINAL checks=2
```

(`dirty` counts untracked peer artifacts; the tracked-file check stayed empty across both.)

**Independent recount, committed tree c4d4823 (judged receipt).** Driver as described in Work
performed. Observed summary:

```text
MAP r87-myth-cluster: declared=(14, 8, 22, 22) counted=(14, 8, 22, 22) match=True distinct=22
  tokens=42/42 failed=[] idx={'entities': [0, 1, 3, 4, 5, 6], 'relations': [0, 1, 2, 3], 'timeline': [0, 1, 2, 3]}
  anchors rows=22 exact=22 bad=[] quotes=10/10
  unreferenced=[] clause_map=[] cell_failures=[]
MAP r88-m3-maya-cluster: declared=(10, 2, 12, 8) counted=(10, 2, 12, 8) match=True distinct=8
  tokens=10/10 failed=[] idx={'entities': [0, 1, 2, 3], 'timeline': [0, 1]} bare fields=4/4
  anchors rows=12 exact=12 bad=[] quotes=0/0
  clause_map=[{'ptr': 'symbolism-clause-map.md:7', 'clause_in_line': True}, {'ptr': 'symbolism-clause-map.md:8', 'clause_in_line': True}]
  unreferenced=[] cell_failures=[]
MAP r89-inspiration-paraphrase: declared=(1, 0, 1, 1) counted=(1, 0, 1, 1) match=True distinct=1
  tokens=1/1 failed=[] anchors rows=1 exact=1 bad=[] cell_failures=[]
```

**Row `source_id` membership** (same driver, per-row source cell vs `sources.json` ids):
`r87 row_src_ok=22 bad=0`; `r88 row_src_ok=10 bad=0`; `r89 row_src_ok=1 bad=0`.

**Delivered checker on the committed tree** (cross-check; commands run from `lore-shokunin/`):

- `python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster` →
  `INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 8/8; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 22/22`
  … `SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 8/8; …` → `RESULT PASS`, exit=0.
- `python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster` →
  `INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12; DISTINCT-ANCHORS 8/8`
  … no `WARN:` line … `RESULT PASS`, exit=0.
- `python3 corpus/tools/support_check.py corpus/fixtures/r89-inspiration-paraphrase` →
  `INVENTORY JSON-FACTS 1/1; EDITORIAL-ROWS 0/0; TOTAL-ROWS 1/1; DISTINCT-ANCHORS 1/1` →
  `RESULT PASS`, exit=0.

**Before state (r91 baseline `396c568`, scratch archive).** Commands:

```sh
git archive 396c568 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster | tar -x -C /tmp/jcov3-before
python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster   # old checker on baseline map
```

Observed: `INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 0/0; TOTAL-ROWS 10/10; DISTINCT-ANCHORS 6/6`;
`WARN: unreferenced excerpt declaration: source-excerpt.md (mode=verbatim)`;
`RESULT PASS WITH WARNINGS`; exit=0. My recount on the same baseline map:
`declared=(10, 0, 10, 6) counted=(10, 0, 10, 6)`, `unreferenced=['source-excerpt.md']`.
After (committed): `10/2/12/8`, `unreferenced=[]`, `RESULT PASS` (no WARN).
`git diff --stat 396c568 c4d4823` lists the r88-m3 map (14 ±) and `support_check.py` (55 ±) but
not the r87 map — r87's 14+8 denominators predate r92 and are unchanged by it.

## Findings & named debt

- **Denominator verdict (this seat's axis): verified — improved, bounded.** The r92 coverage
  claim reproduces exactly under an independent recount: r87 = 14 JSON facts + 8 editorial
  rows = 22 mapped rows, 22 distinct anchors; r88-m3 = 10 JSON + 2 editorial = 12 rows,
  8 distinct anchors; the third map carrying an Inventory line (r89, 1/0) also holds. The
  declared Inventory lines equal my counts equal the delivered checker's INVENTORY/RECEIPT
  lines on all three maps. No axis is harmed by these claims.
- **WARN closure verified end-to-end.** Before (scratch replay of `396c568`): 10/0/10/6 with
  `WARN: unreferenced excerpt declaration: source-excerpt.md`. After (`c4d4823`): 10/2/12/8,
  zero unreferenced declared paths, `RESULT PASS`. The closure is produced by the two Spence
  rows: both anchors resolve at `source-excerpt.md:5`, and their
  `symbolism-clause-map.md:7/:8` pointers carry the cited clause text in-line.
- **Every map row pointer resolves** (r87 + r88-m3, the judged pair). r87: 42/42 JSON field
  pointers resolve, 22/22 anchors on their declared lines, 10/10 quoted statements/descriptions
  byte-equal to the JSON, 22/22 source_id cells in `sources.json`. r88: 10/10 pointers, 4/4
  named sub-fields (`description`, `source_id`) present on the referenced records, 12/12
  anchors on their lines, 10/10 source_id cells, 2/2 clause-map pointers. r89 (sweep): 1/1
  pointer, 1/1 anchor.
- **r87 scope is honest, not a silent omission.** The r87 JSON side holds 7 entity claims;
  6 are mapped (entities `[0,1,3,4,5,6]`) and entities[2] (mother-tide-gate; claim
  `source_id=lowwater-hymn`, `first_appearance=lowwater-hymn`) is explicitly documented at
  `claim-excerpt-map.md:60` as an off-scope D1 crosswalk pointer (the string `entities[2]`
  appears twice in the map's notes). All 4 relations and all 4 timeline events are mapped.
- **Bounds (named, not debts).**
  (i) Lexical only — anchor/pointer agreement is preflight evidence and establishes no prose
  fidelity, source authenticity, or canon.
  (ii) The checker's unreferenced-declaration WARN is path-scoped, not range-scoped: any row
  referencing `fictional-excerpts.md` also covers the veil-verse declaration lines; only
  `source-excerpt.md`'s closure is a true range-level closure (S1/S2 are its only referencing
  rows).
  (iii) r88's 12 rows collapse to 8 distinct anchors (`repeated-references=4`: P1/P3, P2/P4,
  E1/T1, E2/T2 share anchors); r87's 8 editorial rows sit on 3 excerpt lines (H1–H4 on line 5,
  H5–H6 on line 6, H7–H8 on line 7) while all 22 anchors are distinct. "Distinct anchors" must
  not be read as "distinct lines".
  (iv) The Inventory lines are self-declared by the maps; agreement between three independently
  written parsers (mine, the checker's, the map authors') is today's result, not a pinned
  invariant — no map carries its own hash pin.
  (v) The support command's failure contract (RESULT FAIL/ERROR, exit alignment) is JCOV1's
  axis; not re-judged here. The boundary doc / JDEP2 edges are C1's axis; not re-judged here.
- No new debt is charged by this seat to the C1/C2/C3 claims. Nothing in my recount contradicts
  the committed tree at `c4d4823`.

## Handoff

- Deliverables: `.ufo/waves/round-92/followup/JCOV3.md` (this) and
  `.ufo/waves/round-92/followup/JCOV3-census.json` (machine receipt; `json.load`-validated;
  carries declared/counted tuples, pointer/anchor/quote stats, and `inventory_match=true`).
- For the round record: C2's denominators (r87 14+8; r88-m3 10 JSON + 2 editorial) are
  **confirmed by independent recount at `c4d4823`**; the r88-m3 unreferenced-declaration WARN
  is **closed by the two Spence rows**; every judged map row pointer resolves; all three
  Inventory lines match declared counts and delivered checker receipts. The before-state was
  replayed from `396c568` for the record.
- Independence: JCOV1/JCOV2/JCAL/H-series peer artifacts landed during my wait window; no peer
  artifact was read as evidence — my numbers and bounds stand on my own receipts above.
- No commit, no push; tracked tree untouched by this seat
  (`git status --porcelain --untracked-files=no` empty at finish). Scratch removed
  (`cleaned=0`).
- Gaps: none blocking. If recount must be re-run after follow-up artifacts are integrated
  (they are untracked), `JCOV3-census.json` carries the expected numbers and the driver
  method is described above.