# V37 — code-review-c1 (round 95)

Seat: V37 `code-review-c1`. Scope per seat spec: after P1 lands, line-by-line read of
`git diff fb118c4 -- corpus/tools/map_obligations.py`, hunt unsound `schema_drift` rules,
verify dialect-parser fidelity to the r88 map grammar, preserved exit/RESULT contract,
stdlib-only, no live-tree writes; run the full r87–r94 fixture battery myself; report
defects by severity.

Reviewed revision (frozen by me at review start, unchanged through the whole review):

```
d31b8182953e9088a155f4ed2978af5b  corpus/tools/map_obligations.py
d2a77aa09e5cd38d73d772bb11a5914e  corpus/tools/map-obligations-contract.json
```

Frozen copies: `.ufo/waves/round-95/seats/V37-scratch/map_obligations_reviewed.py`,
`diff-reviewed.patch` (282 lines, 17 hunks). Baseline tool copy
`V37-scratch/map_obligations_baseline.py` (md5 `882eeebdeb2ac6ea05a8cdb1afff7ba3`,
verified identical to `git show fb118c4:corpus/tools/map_obligations.py`). P1 report
`P1-tool-code.md` and P2 report `P2-contract-docs.md` were present; P1's reported
`git diff --numstat` `130 12 corpus/tools/map_obligations.py` matches the delivered bytes
exactly. `git status --porcelain` shows P1's only tracked write is
`corpus/tools/map_obligations.py` (ownership respected; no commits, no pushes, no network).

## 1. What the diff does (17 hunks, read line-by-line)

- `:19-25` new constants: `POINTER_COLUMN_ROLES` gains `"json fact and fields"`;
  `LEGACY_POINTER_COLUMN` is that same role; `LEGACY_POINTER` bracket grammar
  `(entities|relations|timeline)[i](.first_appearance|.claims[j])?`; `LEGACY_CELL`
  (`token`, optional `(parenthetical)`, optional `: prose`); `EXPECTED_INVENTORY`.
- `:154 legacy_pointer` — translates bracket tokens to canonical pointers; rejects
  non-canonical indices (`ARRAY_INDEX`), field suffixes (`.statement`), bare `entities[i]`.
- `:173 parse_pointer_cell(cell, legacy=False)` — legacy attempt first, then the unchanged
  canonical parse (so canonical cells stay accepted under a legacy header; no false
  negatives introduced).
- `:220-268 declared_inventory / editorial_row_count / print_inventory_receipt` — new
  advisory stdout receipt.
- `:292-303 parse_map_text` — the legacy flag is gated on the pointer column's normalized
  header being exactly `json fact and fields`.
- `:357 claim_shaped` + `:377-388` — `schema_drift` finding for a non-empty list under an
  entity key other than `claims` whose items are dicts with non-empty str `statement` and
  `source_id`; returned as an exit-1 finding (not a `ToolError`), merged with `compare()`.
- `:529/:553 run_frozen` — same merge on the frozen path; inventory receipt added.
- `:635/:648/:725` — new self-test cases `map_missing` (map unlinked → exit 2) and
  `invalid_arguments` (CLI invoked with no cluster argument → exit 2).

## 2. C1 core: BR-02 closed, stably

Mutation class = renamed `claims` key (content preserved) + removed map row, on scratch
copies of `corpus/fixtures/r94-paired-crossing`:

```
old run1 rc=0 | OBLIGATIONS raw=13 mapped=13~RESULT PASS~
new run1 rc=1 | OBLIGATIONS raw=13 mapped=13~INVENTORY JSON-FACTS 13/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 15/16 MISMATCH~FINDING schema_drift: entities.json#/0: 1 sourced-claim-shaped record(s) under unexpected key 'claim_records'~RESULT FAIL~
old run2 rc=0 | OBLIGATIONS raw=13 mapped=13~RESULT PASS~
new run2 rc=1 | ... identical to new run1 ...
```

Stable across 3 further runs with varied `PYTHONHASHSEED` (`determinism.txt`), and the
rename variants `assertions`/`entries`/`claim_records`/`records`/`claim-list` all exit 1
with the same finding ID. `mut-rename-row-kept` → `phantom_obligation` + `schema_drift`,
exit 1. `ctrl-row-removed-only` → `missing_obligation` only, exit 1 (no drift false-fire).

## 3. Full battery: 169 fixture dirs, old vs new

Baseline (`battery-baseline-full.tsv`): 2 dirs rc=0 (r93, r94), 167 rc=2.
New (`battery-new-full.tsv`): 4 dirs rc=0, 165 rc=2. Exit-code changes:

```
corpus/fixtures/r88-m3-maya-cluster rc=2 rc=0     # intended C3
corpus/fixtures/r95-crossing-aftermath rc=2 rc=0  # fixture landing, not the tool:
#   baseline tool on r95 now also exits 0 (OBLIGATIONS raw=15 mapped=15) — its map landed mid-battery
```

r87 unchanged exit 2 (message moved from the header stage to the cell stage, same finding
ID `unsupported_map`); r89 unchanged exit 2 (`table needs one JSON fact pointer and one
source-ID column`); r93/r94 keep `raw=12/14` and gain one documented INVENTORY stdout line.
No other fixture changed exit code, message, or finding set.

## 4. Dialect fidelity to the r88 grammar

`python3 corpus/tools/map_obligations.py corpus/fixtures/r88-m3-maya-cluster` →
`OBLIGATIONS raw=10 mapped=10` / `INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12` /
`RESULT PASS`, exit 0. Note the C3 claim's "12/12 PASS" is this INVENTORY TOTAL-ROWS
receipt; the obligations line itself is 10/10 (10 JSON-fact rows; the 2 editorial rows are
counted only by the receipt). Same anchors/spans/modes: `support_check.py` is untouched
(`support_check` r88 still `SOURCE-SUPPORT 10/10; EDITORIAL-ANCHORS 2/2; VALIDATED-ROWS 12/12`).

16 hand-built dialect probes (`.ufo/waves/round-95/seats/V37-scratch/dialect-probes/`):

| probe | new exit | note |
|---|---|---|
| `entities[0].first_appearance` (Aru) | 0 | accepted |
| `entities[0].claims[0]`: prose | 0 | accepted |
| `timeline[0]` (field-list) : prose | 0 | accepted |
| `entities[0].first_appearance`: prose | 0 | trailing prose accepted |
| `entities[00].first_appearance` | 2 | noncanonical index rejected |
| `entities[0].claims[00]` | 2 | rejected |
| `entities[0].claims[0].statement` | 2 | field suffix rejected (no silent widening) |
| `entities[0].nickname` | 2 | unknown field rejected |
| `entities[0]` (bare) | 2 | rejected (no default field) |
| `entities.0.first_appearance` | 2 | dotpath rejected |
| two tokens in one cell | 2 | r87-style co-map rejected |
| bracket token under a canonical header | 2 | dialect gate holds (contract `fallback` claim verified) |
| `entities[9].first_appearance` | 1 | valid pointer, no record → phantom_obligation |

Translation fidelity is correct for every r88 row (P1–P4, E1–E4, T1–T2), and the rejects
are all fail-closed exit 2. r87's comma-separated co-map cells and r89's `Claim pointer`
header stay exit 2.

## 5. Defects by severity

**D1 — MEDIUM (unsound acceptance, legacy dialect only).** Under a legacy
`JSON fact and fields` header a pointer cell may name a second pointer in its parenthetical
or in its colon-prose, and the tool silently ignores it and PASSes:

```
legacy-paren-hidden-canonical  rc=0 | OBLIGATIONS raw=3 mapped=3~RESULT PASS~   # `entities[0].first_appearance` (also `relations.json#/0`)
legacy-paren-hidden-legacy     rc=0 | OBLIGATIONS raw=3 mapped=3~RESULT PASS~   # (also `entities[9].claims[0]`)
legacy-colon-hidden-pointer    rc=0 | OBLIGATIONS raw=3 mapped=3~RESULT PASS~   # : also `entities[9].claims[0]`
canonical-note-hidden-pointer  rc=2 | FINDING unsupported_map: co-mapped or unsupported pointer grammar~RESULT ERROR~
```

The canonical path screens notes for embedded pointers (`fail("unsupported_map", "co-mapped
or unsupported pointer grammar")`); the legacy path does not — `LEGACY_CELL`'s
`(?:\s*\([^()]*\))?` and `(?:\s*:\s*.*)?` swallow the rest of the cell. This contradicts the
tool's own stated grammar ("pointer cells must contain one canonical inline-code pointer",
README r94 section; `legacy_pointer_dialect` in the contract) and produces a false negative
on phantom detection plus a co-map row that can masquerade as a single-fact row. Bounded:
the r87 delivered co-map map still exits 2, and the primary completeness direction is
unaffected (`legacy-colon-hidden-mapped` → `missing_obligation`, exit 1). Not exploited by
any delivered corpus map: r88's cells carry exactly one pointer token (the other backticked
tokens are the field-list parenthetical).

**D2 — LOW–MEDIUM (calibration residual: the drift rule is shape-specific and evadable).**
All of the following still silently PASS exit 0 while the claim content is preserved
somewhere in the entity:

```
evade-renamed-fields   rc=0 | OBLIGATIONS raw=13 mapped=13~...~RESULT PASS~   # assertions: [{text, src}]
evade-renamed-dict     rc=0 | ...~RESULT PASS~                                # assertions: {0: {statement, source_id}}
evade-empty-statement  rc=0 | ...~RESULT PASS~                                # statement: ""
evade-nested-claims    rc=0 | ...~RESULT PASS~                                # record: {claims: [...]}
evade-timeline-shape   rc=0 | ...~RESULT PASS~                                # claim-shaped list on a timeline record
```

The declared C1 class (key renamed, inner field names preserved, map row removed) is closed,
and the README bounds the rule honestly ("bounded to entity claim containers: it is not
general JSON-schema or unknown-key validation"), so this is a residual of the same defect
family rather than a failed claim. It is worth recording because BR-02's family is not fully
closed: any rename that also renames the inner fields, nests the list, or drops to a
non-list container still yields the original silent PASS.

**D3 — LOW (hypothetical false-positive class; no live impact).**
`legit-claim-shaped-extra-key` (`rejected_claims: [{statement, source_id}]`) → exit 1
`schema_drift`, with no suppression mechanism. A census over all 169 fixture dirs found
zero entity/relation/timeline keys outside the known sets (`EXTRA KEYS: {}`), and the
`provenance` lists (tick/from_holder/to_holder/source_id; 43 entity records in 35 fixture
dirs) do not
trip the rule because `claim_shaped` requires `statement` — so there is no live regression,
but a future legitimate non-obligation list of claim-shaped records now hard-fails.

**D4 — LOW (documented advisory, observation not defect).**
`inv-declared-wrong` (map declares 99 JSON facts) → `INVENTORY ... MISMATCH` printed but
`RESULT PASS`, exit 0; `inv-malformed` → `INVENTORY declaration-malformed`, exit 0. The
README states this explicitly ("The inventory line is a receipt, not a gate ... does not by
itself change the exit code"), so behavior and docs agree; readers of the C3 "12/12 PASS"
phrasing should not mistake the receipt for a gate.

**D5 — INFO.** r87's `unsupported_map` detail text changed stage (header → cell); finding ID
and exit code preserved. r93/r94/r95 runs gain one INVENTORY stdout line (documented in the
README r95 addendum).

## 6. Preserved exit/RESULT contract, self-test, frozen, hygiene

- 169-dir audit (`stderr + RESULT-line audit`): zero violations — no stderr anywhere,
  exactly one `RESULT ` line per run, exits ⊆ {0,1,2}, no `RESULT PASS` with findings, no
  exit 2 without a FINDING.
- Arg surface unchanged: no-map dir → `map_missing` exit 2; `--self-test <cluster>` →
  `invalid_arguments` exit 2; `--bogus` → `invalid_arguments` exit 2; no args →
  `invalid_arguments` exit 2; `--frozen <dir> <cluster>` → `invalid_arguments` exit 2;
  `--help` → exit 0 with 0 RESULT lines (documented caveat intact).
- `--self-test` → 22 `SELF-TEST PASS` lines including `map_missing` and `invalid_arguments`,
  `RESULT PASS`, exit 0; contract now persists 22 cases (diff adds the two cases plus the
  `legacy_pointer_dialect` block, consistent with the implementation). The baseline tool
  against the new contract exits 2 (`self_test_contract`) — correct: expectations are
  persisted and consumed, not regenerated.
- `--frozen .ufo/waves/round-94/frozen/map-obligations-r93` → digests verified,
  `OBLIGATIONS raw=12 mapped=12`, `RESULT PASS`, exit 0. A hand-built drifted snapshot
  (claims renamed + row removed, digests repinned) → exit 1,
  `FROZEN expected=FAIL/1 findings=['schema_drift'] matched` — drift propagates correctly
  into the frozen verdict machinery.
- Stdlib-only: AST scan imports `argparse, collections, hashlib, json, os, pathlib, re,
  subprocess, sys, tempfile`; `non-stdlib: []`.
- No live-tree writes: corpus tree md5 `47d650d0…` and repo-root listing md5 `66f9775d…`
  identical before/after cluster, `--map`, r88 and `--frozen` runs; `--self-test` residue
  count before=0 after=0 (BR-05 scratch-under-root behavior unchanged, as the README states).

## Bottom line

**PASS** — C1 verifies on the delivered revision (`d31b818…`): the BR-02 mutation now exits 1
with a stable, deterministic `schema_drift` FINDING while the baseline silently PASSed, the
22-case self-test and frozen/r87/r89 controls are preserved, no `schema_drift` false
positive exists on the delivered corpus, and the code is stdlib-only with no live-tree
writes; the only real defect is D1 (MEDIUM: the legacy dialect silently ignores a second
pointer named in a parenthetical or colon-prose, where the canonical dialect rejects it),
with D2/D3 as bounded residuals and D4/D5 as documented or informational.
