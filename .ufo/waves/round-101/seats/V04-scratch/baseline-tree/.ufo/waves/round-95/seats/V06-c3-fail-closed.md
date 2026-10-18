# V06 — c3-fail-closed (round 95)

- Seat: V06, verifier. Claim under test: C3 — the `map_obligations` dialect widening
  must NOT loosen fail-closed behavior (r87/r89 stay exit 2 `unsupported_map`; mutations
  under dialect mode must exit 1 with stable FINDING IDs).
- Verified revision (frozen for every measurement below; re-hashed before and after each
  batch, unchanged): `corpus/tools/map_obligations.py` sha256
  `d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108`;
  contract `corpus/tools/map-obligations-contract.json` sha256
  `8173bb97592a377716866737e8fcb4043014c9814e77a6248500d301a39170db`.
- Poll-wait: P1's report `.ufo/waves/round-95/seats/P1-tool-code.md` was absent for the
  first ~16 poll cycles; the tool hash evolved `cc1df4dc → 28d308be → feea13c9 →
  3f87fe8b → 9224a684 → d1c239cc` (settled 16:26:27). All verification below was run
  only after P1's report existed and the hash was stable across consecutive polls.
- Scratch: `.ufo/waves/round-95/seats/V06-scratch/` (declared seat scratch). Only scratch
  files and this report were written. Real corpus untouched:
  `git diff --stat HEAD -- corpus/fixtures/r87-myth-cluster corpus/fixtures/r88-m3-maya-cluster corpus/fixtures/r89-inspiration-paraphrase` → empty;
  `git diff --stat HEAD -- corpus/tools/support_check.py` → empty.

## 1. Before → after on the legacy forms

Command form: `python3 <tool> corpus/fixtures/<fixture>`. OLD tool =
`git show HEAD:corpus/tools/map_obligations.py > .ufo/waves/round-95/seats/V06-scratch/map_obligations_OLD.py`
(sha256 `cc1df4dc406870b6…`, verified by re-running).

| fixture | OLD (r94 HEAD) | NEW (`d1c239cc…`) |
|---|---|---|
| r87-myth-cluster | exit 2 · `FINDING unsupported_map: table needs one JSON fact pointer and one source-ID column` | exit 2 · `FINDING unsupported_map: pointer cells must contain one canonical inline-code pointer` (identical ×2 runs) |
| r88-m3-maya-cluster | exit 2 · same header finding | exit 0 · `OBLIGATIONS raw=10 mapped=10` / `INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12` / `RESULT PASS` |
| r89-inspiration-paraphrase | exit 2 · same header finding | exit 2 · same header finding, byte-identical detail |

Findings:

- r87: finding ID (`unsupported_map`) and exit code unchanged — fail-closed preserved —
  but the detail string changed. Cause verified by reading the map: r87's JSON-facts
  table header is `| ID | JSON fact and fields | …` (the new legacy dialect column), so
  the tool now enters legacy row parsing and rejects the row cell, which is co-mapped
  (`entities[0].claims[0].statement`, …, co-map `entities[0].first_appearance`) and
  untranslatable. No `OBLIGATIONS` line is printed on either path — nothing is accepted.
- r89 still fails at header level: its pointer column is `Claim pointer`, which is not in
  the dialect roles (`json fact pointer`, `json fact pointer and fields`,
  `json fact and fields`).
- The r88 PASS receipt is `raw=10 mapped=10` plus the inventory line
  `JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12` (10 JSON facts + 2 editorial
  rows = the claimed 12/12).

## 2. Mutation probes (dialect mode; byte copies of r88 under V06-scratch)

Mutations applied with a python3 heredoc to the scratch copies only; the real r88 fixture
was never modified (git diff empty, and the real fixture still PASSes after the probes).

A. **drop one row** (P1 row deleted) — exit 1, stable ×2:
```
FINDING missing_obligation: entities.json#/0/first_appearance has no map row
INVENTORY JSON-FACTS 9/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 11/12 MISMATCH
RESULT FAIL
```

B1. **break one excerpt-anchor cell** (P1 anchor `Aru carried the north lantern at Quiet
Rise` → `south`) — exit 0 PASS: `map_obligations` does not read anchor text (that class
belongs to `support_check`, by design). Class not silently lost — `support_check.py` on
the same copy exits 1:
```
FAIL P1: source-support; mode=verbatim; anchor=not-found
SOURCE-SUPPORT 9/10; EDITORIAL-ANCHORS 2/2; …; VALIDATED-ROWS 11/12
FAIL: inventory distinct excerpt anchors mismatch: expected=8 parsed=9
```
So the seat's "break one anchor" was probed in the pointer-anchor sense (B2), which is
what `map_obligations` owns.

B2. **break one pointer anchor** (the row's anchor into the raw JSON), two forms, each
exit 1 and stable ×2:
- → `entities[0].claims[0]` (valid token, collides with E1):
  `FINDING duplicate_mapping: entities.json#/0/claims/0 appears 2 times` +
  `FINDING missing_obligation: entities.json#/0/first_appearance has no map row`.
- → `entities[0].claims[9]` (valid grammar, nonexistent):
  `FINDING phantom_obligation: entities.json#/0/claims/9 is not a raw source-attributed obligation` +
  `FINDING missing_obligation: entities.json#/0/first_appearance has no map row`.

C. **dialect-path fail-closed probe** (untranslatable legacy token
`symbolism[0].claims[0]`): exit 2 ·
`FINDING unsupported_map: co-mapped or unsupported pointer grammar` — dialect acceptance
is validated per row, not granted by header alone.

## 3. Corroborating receipts (same frozen revision)

- `python3 corpus/tools/map_obligations.py --self-test` → exit 0, 22 × `SELF-TEST PASS`,
  `RESULT PASS`. Contract `self_test.cases` = 22 entries including `map_missing` and
  `invalid_arguments` (adjacent C1 evidence; C1's own demo not re-run here).
- `python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93`
  → exit 0, `SNAPSHOT inputs=4 digests=verified` … `FROZEN expected=PASS/0 findings=none matched`.
- `support_check` receipts unchanged on the real fixtures: r88 PASS
  `SOURCE-SUPPORT 10/10; EDITORIAL-ANCHORS 2/2; MODES 12/12; VALIDATED-ROWS 12/12`;
  r93 PASS 12/12 + 3/3, MODES 15/15; r94 PASS 14/14 + 2/2, MODES 16/16.
- Corpus immutability: r87/r88/r89 byte-identical to `fb118c4`; the only untracked
  fixture is `?? corpus/fixtures/r95-crossing-aftermath/` (P3/P4's new dir, expected).

## 4. Limits and disclosures

- The r87 message-text drift is a real before/after difference. Read as "same finding ID
  + same exit code + still no acceptance" the seat requirement holds; read as
  "byte-identical detail string" it does not. Flagged for the adjudicator rather than
  silently netted. P1's own report declares the same new message.
- B1 shows `map_obligations` alone cannot detect a corrupted excerpt-anchor cell; that is
  unchanged behavior (the OLD tool never read anchors either) and the class is caught by
  `support_check`, evidenced above.

Bottom line: PASS — dialect widening did not loosen fail-closed behavior: r87/r89 remain
exit 2 `unsupported_map` (r87 detail string changed, ID/exit unchanged), r88 dialect
PASSes 12/12 with zero corpus modification, and row-drop plus pointer-anchor-break
mutations exit 1 with stable FINDING IDs; the excerpt-anchor class remains covered by
`support_check`.
