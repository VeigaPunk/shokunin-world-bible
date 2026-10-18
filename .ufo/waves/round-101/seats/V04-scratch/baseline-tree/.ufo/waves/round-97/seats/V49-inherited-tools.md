# V49 — inherited-tools (round 97, single-wave)

**Seat scope (verbatim):** *V49 inherited-tools — git diff f3e09f9: check_bible/support_check/boundary/discriminate/contract + r87–r96 JSON tables untouched (r96 map repair excepted — verify its scope via V19).*

Repo root for every command below: `/home/vgpnk/Projects/shokunin/lore-shokunin` (session cwd is the parent repo; all paths absolute or `cd`-anchored here). Baseline: r96 closure `f3e09f9` (lane HEAD `2393934`). Nothing was written outside this report and `.ufo/waves/round-97/seats/V49-scratch/`.

**Poll-wait protocol:** `V49-scratch/poll.sh`, 20 s cadence, 40 tries. Producer reports landed 16/17/22/25/31/40; `ALL_PRODUCER_REPORTS_PRESENT after try=40` (R1–R6 all written). All final checks were run on the delivered revision after that point; `r97` fixture (10 files), `corpus/knowledge/r97-acknowledgment-scope-note.md`, and all five owned `corpus/tools`/r96-map writes were present.

## 0. Baseline freeze (before any producer write)

```
$ git log --oneline -1
2393934 lore r96: close round — SCORECARD admitted section
$ git diff --stat f3e09f9            # at seat start
 LOG.md       | 61 +++++
 SCORECARD.md | 31 +++++
$ python3 .ufo/waves/round-97/seats/V49-scratch/manifest.py f3e09f9
# rev=f3e09f9 tracked=1803 worktree=1803
# CHANGED (0):
# DELETED (0):
# ADDED (0):
```

Baseline sha256 (16 hex) of the inherited-tool set, from `git cat-file -p f3e09f9:<path> | sha256sum`; the 185 `*.json` tables of the r87–r96 namespace are hash-pinned in `V49-scratch/r87-r96-json-baseline.txt`.

## 1. Inherited tool set — byte-identical (PASS)

`V49-scratch/scope_check.py` (walks `corpus/{tools,fixtures,knowledge,live}`, hashes baseline objects vs working tree, classifies every delta against the declared r97 byte-ownership map):

```
## INHERITED TOOL PINS (must be unchanged):
  UNCHANGED corpus/fixtures/check_bible.py            base=ff9fd2aa6811 wt=ff9fd2aa6811
  UNCHANGED corpus/tools/support_check.py             base=55a5eb275390 wt=55a5eb275390
  UNCHANGED corpus/tools/boundary_doc_check.py        base=ebb6a0843e67 wt=ebb6a0843e67
  UNCHANGED corpus/tools/boundary-doc-contract.json   base=e89d2a76d3c8 wt=e89d2a76d3c8
  UNCHANGED corpus/tools/discriminate_check.py        base=6c7b7cd8b667 wt=6c7b7cd8b667
```

Direct per-path diff (empty output = no diff, exit 0):

```
$ git diff --stat f3e09f9 -- corpus/fixtures/check_bible.py corpus/tools/support_check.py \
    corpus/tools/boundary_doc_check.py corpus/tools/boundary-doc-contract.json \
    corpus/tools/discriminate_check.py
(empty)
```

`check_bible.py` pin `ff9fd2aa6811a813` is the r96-closure checker pin reproduced at closure — unchanged here.

## 2. `contract` files — audit (PASS, all deltas inside declared ownership)

Three contract JSONs exist under `corpus/tools/`. `V49-scratch/contract_audit.py` compares each against `f3e09f9` structurally (recursive old-vs-new walk):

```
## corpus/tools/boundary-doc-contract.json: BYTE-SEMANTIC IDENTICAL to f3e09f9
## corpus/tools/dependency-freeze-contract.json: 6 deltas, 4 non-additive
   VALUE-CHANGE $.scope: '...no chronology truth, entailment, source, rights, or canon judgment'
                       -> '...; --freeze is scope-guarded to corpus/fixtures/** and every pin records
                           the fixture's repo-relative path, which verification enforces (SCOPE-REFUSED / PATH-MISMATCH)'
   VALUE-CHANGE $.revision: '60dba0c2aa344860b10a2fc63e00468d1b134f27' -> '2393934237ea076366f3db6dceeff033edb52ab1'
   VALUE-CHANGE $.pins.r96-crossing-response.revision: '60dba0c2...' -> '2393934...'
   ADDED-KEY $.self_test.expected.scope_refused   {'exit': 2, 'finding_ids': ['SCOPE-REFUSED'], 'forbid_traceback': True}
   ADDED-KEY $.self_test.expected.path_mismatch   {'exit': 2, 'finding_ids': ['PATH-MISMATCH'], 'forbid_traceback': True}
   VALUE-CHANGE $.provenance_note: '...' -> '... r97 (R3 freeze-hardening): ...'
## corpus/tools/map-obligations-contract.json: 1 deltas, 0 non-additive
   APPENDED $.self_test.cases[24]
```

- `boundary-doc-contract.json` (unowned this round): byte-identical, pin `e89d2a76d3c8c5c4`.
- `map-obligations-contract.json` (R2-owned, C1): **purely additive** — the only delta is the appended case `{"id": "dual_pointer", "exit": 1, "finding_ids": ["dual_pointer"]}` at `cases[24]` (24→25). No existing case or value changed, nothing removed.
- `dependency-freeze-contract.json` (R3-owned, C2): `git diff --numstat` is large — `366 352` — because the file was rewritten by the tool's `indent=2` writer. The rewrite is proven semantics-neutral: after normalising exactly the six deltas above,

```
$ python3 -c "<load both, blank scope/provenance_note/revision, pop the 2 new expected keys, compare>"
EQUAL-AFTER-NORMALISATION: True
```

  All six deltas are declared C2 content (scope guard text, the pin-refresh `revision` moves, the two new self-test expectations 14→16, the provenance note that self-documents the reformat and the pin refresh). `pins.r96-crossing-response.content_sha256` stays `d422a9b3…` — consistent, because the repair touched only the non-pinned Markdown map. Other pins (r88/r94/r95) are byte-identical.
  *Observation for adjudication (not a violation):* the `indent=2` reformat inflates the diff for an owned file; no semantic drift beyond the six deltas, per the normalisation equality above.

## 3. r87–r96 JSON tables — untouched (PASS)

```
$ # baseline: 185 r87..r96 *.json under corpus/fixtures, hashed at f3e09f9
$ while read h f; do n=$(sha256sum "$f" | cut -c1-16); [ "$h" != "$n" ] && echo "CHANGED $f"; done < V49-scratch/r87-r96-json-baseline.txt
(no output)
checked=185 changed=0
$ git ls-tree -r f3e09f9 --name-only -- corpus | grep -E 'r(8[7-9]|9[0-6])' | grep '\.json$' | grep -v '^corpus/fixtures/'
(empty — the whole r87–r96 JSON namespace lives under corpus/fixtures)
$ git diff --name-only f3e09f9 -- corpus/fixtures/r87-* corpus/fixtures/r88-* corpus/fixtures/r89-* \
    corpus/fixtures/r90-* corpus/fixtures/r91-* corpus/fixtures/r93-* corpus/fixtures/r94-* corpus/fixtures/r95-*
(empty — no file of any kind changed in those 37 fixture directories)
```

## 4. The r96 exception — scope verified (PASS), corroborated by V19

```
$ git diff --name-status f3e09f9 -- corpus/fixtures/r96-crossing-response
M	corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
$ python3 V49-scratch/r96_repair_check.py
## files changed in fixture: 1 -> [...claim-excerpt-map.md]
## RESULT: scope == exactly claim-excerpt-map.md (declared cosmetic target)
## lines: base=56 wt=56
## data rows (non-delimiter): base=23 wt=23
## data rows identical positionally: 23/23
```

Exactly two changed line pairs, nothing else (positional compare of both revisions):

```
changed line pairs: 2
  line 44: - |---|---|---|---|---|---:|---|---|
           + |---|---|---|---|---:|---|---|          # delimiter 8 cells -> 7 cells (table has 7 columns)
  line 50: - ...The new relation encodes only the agreement for this crossing, not perpetual performance or alliance.
           + ...The new tick-12 event encodes only Evin's second account of the same crossing occasion; it asserts no
             reconciliation, selects no winner between the accounts, and adds no duty beyond this crossing, not
             perpetual performance or alliance.
```

Post-repair map sha256 `e851f068cfd7ed02c97054df18729c4c5a9b8bf60d99d7c9116f427d765440de` — the same hash V19 recorded post-repair. V19 (`V19-c3-r96-repair-scope.md`) independently reports "**PASS** — the r96 map repair is byte-minimal (exactly the two declared cosmetic lines; all 18 data rows, anchors, spans and modes byte-identical; nothing else in the r96 fixture changed)". My positional 23/23 non-delimiter-row identity and single-file scope agree with V19's 18 data rows / two `@@` hunks (V19 counts only `J*/S*` rows; I count header+data rows).

## 5. Whole-revision diff scope (PASS)

```
$ git status --porcelain --untracked-files=all | grep -v '^?? \.ufo/'
 M LOG.md
 M corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
 M corpus/tools/README.md
 M corpus/tools/dependency-freeze-contract.json
 M corpus/tools/dependency_freeze.py
 M corpus/tools/map-obligations-contract.json
 M corpus/tools/map_obligations.py
?? corpus/fixtures/r97-crossing-acknowledgment/{README.md,claim-excerpt-map.md,contradictions.json,entities.json,
     fictional-excerpts.md,inspiration-note.md,relations.json,source-excerpt.md,sources.json,timeline.json}
?? corpus/knowledge/r97-acknowledgment-scope-note.md
```

`scope_check.py` classification of every delta: 6 CHANGED all OWNED (R1/R2/R3/R4), 11 ADDED all declared r97 artifacts, 0 DELETED, **VIOLATIONS=0** (`V49-scratch/scope-final.txt`, sha256 `626047ed28981ab9…`). No inherited knowledge file changed; the only `corpus/knowledge` delta is the new R6 scope note.

Supporting smoke checks (inherited tools still operate in place — supporting evidence only, C-claims are other seats' to prove):

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r97-crossing-acknowledgment
CLEAN: schema, citations, relations, timeline; 0 violations        exit=0
$ python3 corpus/tools/boundary_doc_check.py            -> CERTIFIED (bounded: ...)
$ python3 corpus/tools/discriminate_check.py            -> RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression
$ python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response
SOURCE-SUPPORT 16/16; EDITORIAL-ANCHORS 2/2; MODES 18/18; VALIDATED-ROWS 18/18
RESULT PASS   exit=0
```

The r96 `support_check` receipt (18/18, PASS) is byte-equal to the pre-repair receipt V19 captured, consistent with a Markdown-only repair.

## 6. Delivered-revision stability (no write landed after the sweep)

Worktree hashes re-taken after the final sweep match every producer's declared delivered hash, and were unchanged on a second re-run:

| path | observed sha256 (worktree) | declared by |
|---|---|---|
| `corpus/tools/map_obligations.py` | `86b52949…` | R1, R2 |
| `corpus/tools/map-obligations-contract.json` | `2142b991…` | R2 |
| `corpus/tools/README.md` | `6278e59b…` | R2 |
| `corpus/tools/dependency_freeze.py` | `b06275f3…` | R3 |
| `corpus/tools/dependency-freeze-contract.json` | `27273be2…` | R3 |
| `corpus/fixtures/r96-crossing-response/claim-excerpt-map.md` | `e851f068…` (pre-repair `5093d72e…`) | R4 |

## Bounds and notes

- This seat verified **scope/byte-identity only**. It does not re-derive C1/C2/C3 semantics; those are the producer and subject-seat claims.
- `corpus/live/**` was inside my walk: zero deltas.
- The `indent=2` reformat of `dependency-freeze-contract.json` is reported as an observation, not a finding: ownership is R3's and semantic equality after normalisation is proven.
- Producer report files themselves are under `.ufo/waves/round-97/seats/` and are out of the inherited scope.

## Bottom line

**PASS** — against `f3e09f9`, `check_bible.py`/`support_check.py`/`boundary_doc_check.py`/`boundary-doc-contract.json`/`discriminate_check.py` are byte-identical (pins ff9fd2aa/55a5eb27/ebb6a084/e89d2a76/6c7b7cd8), all 185 r87–r96 JSON tables and all 37 r87–r96 fixture directories are untouched, the only r96-fixture change is the declared cosmetic two-line map repair (scope corroborated by V19's PASS), and every other delta is a declared producer-owned or new r97 path — 0 violations.
