# V03 c1-before-after — round 99

Seat: V03 c1-before-after (verifier). Lane root `/home/vgpnk/Projects/shokunin/lore-shokunin`. Baseline r98 closure `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`). HEAD during the round `337f0fa52b02`. No commits, no pushes, no network, no nested agents. Wrote only this report and `.ufo/waves/round-99/seats/V03-scratch/`. Live fixtures were not edited. `--freeze` was not run against the live contract.

Claim under test: C1 before/after. Declaration (`LOG.md` Round 99): editing fixture Markdown, including removing dependency wording from an excerpt, was invisible to every gate; after, any pinned-file edit exits 2 `DIGEST-MISMATCH` naming the file. Seat ask: reproduce the before on the r98 tool (`git show 4265df5`) with every gate green, and the delivered tool with `DIGEST-MISMATCH` exit 2.

## Axes

- Before fidelity: r98 tool really misses a prose edit (quoted).
- After detection: delivered tool exits 2 and names the file (quoted).
- Gate completeness: "every gate" means the SKILL.md registry plus the checklist checker `check_bible`, not a subset that stays green.
- Evidence lock: quotes are command output on bytes that match the post-report hashes.

## Poll

Artifacts are the two S1 files. They were still the `4265df5` bytes at 22:01 (empty `git diff --stat 4265df5 --` those paths). Formal poll, 20 s cadence, for `seats/S1*.md` plus hash change:

- Tries 1–15 (background poll killed at the 300 s tool cap; log in the task output): report absent. Tool hash changed once, at try 3, `6f81f8be…` → `fb9bb9ff…` (detail-string edit only: "fixture bytes changed outside the frozen inventory" → "pinned-file bytes changed outside the semantic inventory"). Contract stayed `8c2561b0…`.
- Tries 16–24: report absent, both hashes unchanged.
- Try 25: `S1-full-file-pins.md` present. Hashes still `fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c` (tool) and `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628` (contract).

Post-report lock at 23:00:04: same two hashes; `cmp` of the r98 extract against `git show 4265df5:corpus/tools/dependency_freeze.py` still matched. Final quotes below are from that locked pair. Producer report was present before the final after re-run. Not ABSENT.

## Setup

r98 tool and contract extracted with `git show 4265df5:corpus/tools/dependency_freeze.py` and `git show 4265df5:corpus/tools/dependency-freeze-contract.json`, then `cmp` against those blobs: both `CMP_OK`. Extracted tool sha256 `03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b`. r98 pins cover five JSON files only (no `payload_schema_version`; self-test 17 cases, no `markdown_tamper`).

Path binding since r97 refuses a foreign copy (`PATH-MISMATCH`). Both halves therefore use a mirror whose `corpus/tools/dependency_freeze.py` makes `ROOT = parents[2]` the mirror, with the fixture at `corpus/fixtures/r94-paired-crossing` so the pin path resolves. The delivered mirror holds copies of the locked tool and contract. The live r94 tree was not written.

Mutation (the declaration's dependency-wording removal; same sentence S1 used): in `fictional-excerpts.md` only, `depends on both ninth-bell entries` → `follows both ninth-bell entries`. That sentence is the J14 exact anchor in `claim-excerpt-map.md`. A second, historical V20 wording (`follows the ninth-bell entries`) was also run; same gate split. A third, unanchored wording removal (`We leave its name unowned in the rain.` → `We leave its name in the rain.`; that sentence is not an anchor) is the class that actually stays green.

Registry gates (`SKILL.md` Gate registry): `boundary_doc_check`, `discriminate_check`, `support_check`, `map_obligations`, `dependency_freeze`. `check_bible` is the checklist checker, not a registry row; it is included because the historical "every gate" demonstration included it. `boundary_doc_check` and `discriminate_check` do not take a fixture and do not read `fictional-excerpts.md`. Their live default runs are quoted so they are not silently omitted; they are not witnesses of the edit.

## Before — r98 tool, dependency-wording removal

Cwd for freeze: `.ufo/waves/round-99/seats/V03-scratch/before-mirror-s1exact`. Tool in that mirror is the `4265df5` extract.

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r94-paired-crossing
RC=0
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
DIGEST 2527beb938b474a28d66e1c716f54ba829ae3cc2e616513cd2960a8f7ecebe75
RESULT PASS
```

stderr empty. That digest is the r98 JSON-only pin. The excerpt edit was invisible to this gate.

Companion gates on the same mutated fixture (absolute paths, cwd lane root):

```
$ python3 corpus/fixtures/check_bible.py <before-mirror-s1exact>/corpus/fixtures/r94-paired-crossing
RC=0
CLEAN: schema, citations, relations, timeline; 0 violations
```

```
$ python3 corpus/tools/map_obligations.py <same fixture>
RC=0
OBLIGATIONS raw=14 mapped=14
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16
RESULT PASS
```

```
$ python3 corpus/tools/support_check.py <same fixture>
RC=1
FAIL J14: source-support; mode=verbatim; anchor=not-found
SOURCE-SUPPORT 13/14; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 16/16; VALIDATED-ROWS 15/16
FAIL: J14: source-support anchor missing
RESULT FAIL
```

Pristine live r94 `support_check` (no mutation) was `SOURCE-SUPPORT 14/14` / `RESULT PASS` / exit 0, including `PASS J14` on the original "depends on both ninth-bell entries" sentence. The exit 1 is caused by the wording removal, not a pre-existing failure.

The V20 string (`follows the ninth-bell entries`) on a separate r98 mirror: freeze exit 0, same `DIGEST 2527beb9…` / `RESULT PASS`; `check_bible` exit 0 CLEAN; `map_obligations` exit 0 `RESULT PASS`; `support_check` exit 1, same `FAIL J14` / `RESULT FAIL`.

So the before half "every gate green" is false for the dependency-wording removal. It is invisible to r98 `dependency_freeze`, `check_bible`, and `map_obligations`. It is visible to `support_check`.

## Before — unanchored prose-wording removal (the class that is every fixture-gate green)

Mutation: `We leave its name unowned in the rain.` → `We leave its name in the rain.` Not an anchor. r98 mirror `before-mirror-unanchored`.

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r94-paired-crossing
RC=0
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
DIGEST 2527beb938b474a28d66e1c716f54ba829ae3cc2e616513cd2960a8f7ecebe75
RESULT PASS
```

```
$ python3 corpus/fixtures/check_bible.py <that fixture>
RC=0
CLEAN: schema, citations, relations, timeline; 0 violations
```

```
$ python3 corpus/tools/map_obligations.py <that fixture>
RC=0
OBLIGATIONS raw=14 mapped=14
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16
RESULT PASS
```

```
$ python3 corpus/tools/support_check.py <that fixture>
RC=0
SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 16/16; VALIDATED-ROWS 16/16
RESULT PASS
```

J14 still `PASS` (dependency sentence untouched). This prose edit is invisible to every gate that reads the fixture. `boundary_doc_check` and `discriminate_check` were not pointed at it; they cannot be.

## After — delivered tool, same dependency-wording removal

Locked tool `fb9bb9ff…`, locked contract `8c2561b0…`. Re-run at 23:00:04 after `S1-full-file-pins.md` existed; hashes unchanged from the 22:43 re-run that first saw the final detail string. Cwd: `.ufo/waves/round-99/seats/V03-scratch/after-mirror-s1exact`.

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r94-paired-crossing
RC=2
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
FINDING DIGEST-MISMATCH: content digest 68ae0332a911e4d1cef8b93c18aab567b19ebc656f23ad6089b95810b1882f76 != pin 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef; changed: fictional-excerpts.md (sha256 585f4d0746eadffcdd13a12aa4068392820201ae668dc9b66e9154beccf495c2 -> 6b67dcdaef2e4048bc466bd1e00a154c627883471415dd40635fbceb66b999b0); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
```

stderr empty. Exit 2. Finding id `DIGEST-MISMATCH`. Names `fictional-excerpts.md`. Pin digest `048b8ff3…` is the delivered r94 full-file pin (also printed by a pre-detail-string live verify of unmodified `corpus/fixtures/r94-paired-crossing`: `DIGEST 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef` / `RESULT PASS` / exit 0, at 22:19).

Companion gates on that same after copy, post-report:

- `check_bible` exit 0, `CLEAN: schema, citations, relations, timeline; 0 violations`
- `map_obligations` exit 0, `OBLIGATIONS raw=14 mapped=14` / `RESULT PASS`
- `support_check` exit 1, `FAIL: J14: source-support anchor missing` / `RESULT FAIL`

The new detection is the freeze pin, not a change in the other gates. This is edit detection, not a semantic proof that a dependency was removed.

Same delivered tool, unanchored wording removal (`after-mirror-unanchored`, locked bytes):

```
RC=2
FINDING DIGEST-MISMATCH: content digest b7db7b9aaf3ee3461fbc5602a01afcdbe4be68147fdcbe18152fdc9a54d6c45c != pin 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef; changed: fictional-excerpts.md (sha256 585f4d0746eadffcdd13a12aa4068392820201ae668dc9b66e9154beccf495c2 -> e5ddf7952ac3309ae6b36b68d9955ac57b9107dcdcf2de24bb73721af53b9cd1); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
```

Exit 2. Names `fictional-excerpts.md`. This is the before/after pair where every fixture-reading gate was green before and the delivered freeze names the file after.

## Gates that do not read the excerpt

Live defaults, not pointed at the mutation. Quoted so "every gate" is not a hidden subset. They stay green whether or not the excerpt changes.

```
$ python3 corpus/tools/boundary_doc_check.py
RC=0
CERTIFIED (bounded: frozen-document drift + receipts + explicit-anchor range + structure; no semantic/AST validation)
```

```
$ python3 corpus/tools/discriminate_check.py
RC=0
RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression
```

## What this does and does not confirm

Confirmed, on scratch copies, locked delivered bytes:

- r98 `dependency_freeze` (`git show 4265df5`) does not see either prose edit: exit 0, JSON-only digest `2527beb9…`, `RESULT PASS`.
- Delivered tool exits 2 `DIGEST-MISMATCH` and names `fictional-excerpts.md` for both edits.
- Unanchored prose-wording removal is invisible to `dependency_freeze` (r98), `check_bible`, `map_obligations`, and `support_check`, and is named after.

Not confirmed, and contradicted:

- "Invisible to every gate" for the dependency-wording removal. `support_check` exits 1 `FAIL J14` / `RESULT FAIL` on the r98-tool copy. The declaration's parenthetical example is the case `support_check` already catches, because that wording is the J14 anchor. S1's report records the same split; this seat measured it independently (same after sha256 `6b67dcda…` on the `follows both` mutation).

Not run here: chain 6/6, self-test 18/18, per-file newline tampers. Those are other seats. This seat did not re-freeze.

Bottom line: FAIL — dependency-wording removal is not invisible to every gate before (`support_check` exit 1, J14); the freeze before/after holds (r98 exit 0 `RESULT PASS`; delivered exit 2 `DIGEST-MISMATCH` naming `fictional-excerpts.md`).
