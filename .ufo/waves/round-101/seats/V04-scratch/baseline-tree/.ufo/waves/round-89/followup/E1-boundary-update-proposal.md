# E1 — round-89 follow-up: proposed updates to `corpus/knowledge/holder-assessment-boundary.md`

> **PROPOSAL — not applied.** Seat E1 (round-89 follow-up) holds no write scope
> on `corpus/knowledge/`. Every block below is proposed replacement text for
> the tracked file as it stands at `1b09f3f` (492 lines, unchanged from
> `51b286b`: `git diff --stat 51b286b 1b09f3f -- corpus/knowledge/holder-assessment-boundary.md`
> is empty). The machine-readable drift inventory is `E1-drift.json`; the
> report with pasted receipts is `E1.md`; the round-89 sibling refresh of the
> same file is `CB1-boundary-refresh.md` (seat CB1), cross-referenced
> throughout as `CB1-R1…R19` (in `CB1.md`). Every delivered string quoted
> below was re-measured by seat E1 on the delivered tree at `1b09f3f`.

Basis (all measured by E1 at `1b09f3f`; commands and outputs pasted in
`E1.md` §Before → after):

- checker pin: `sha256sum corpus/fixtures/check_bible.py` →
  `e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556`, 435 lines;
- census: 160 fixture dirs, 9 stdout-changed tuples, 0 exit changes, 0 stderr
  changes (re-run of `E1.md`'s two-revision census);
- delivered cause strings: six r89 fixture replays + four `r89-c1-*` replays +
  three scratch probes, all pasted in `E1.md`;
- anchors: `check_bible.py:72-76` (raw counters), `:82-83` + `:85-91` + `:97`
  (resolved index), `:164-166` (`entity_id_counts`), `:168-173`
  (`holder_identity_detail`), `:185-352` (provenance loop), `:198-203`
  (item-level tests), `:206-208` (disclosure template), `:212-214`
  (top-of-loop emission), `:215-221` (non-dict), `:223-248` (key-set branch;
  combined string `:241-244`), `:249-312` (field validation + cause list),
  `:313-319` (latch), `:320-352` (comparison gate), `:425-435` (CLI).

Application routes (pick one):

1. **Adopt CB1's full refresh** — replace the tracked file's body with
   `CB1-boundary-refresh.md`'s body (drop its proposal banner). Before doing
   so apply the three corrections in §F below (CB1's refresh is otherwise
   accurate to E1's measurements).
2. **Cherry-pick** — apply only the §A–§D blocks below to the current file.

## A. Status and metadata blocks (DR-9, DR-11, DR-12, DR-13)

### A1. Header comment (`:3-5`) — replace with

```text
<!-- Refreshed at round-89 from CB1's round-89 proposal
     (.ufo/waves/round-89/followup/CB1-boundary-refresh.md); line anchors
     re-verified against the delivered checker (e2bb9639…, 435 lines) at
     1b09f3f. The r88-closure text this replaces described the 2ea9ef1
     checker; it is superseded. -->
```

If the content is applied, do **not** keep any "PROPOSAL — not applied"
banner (see A2); the r88 closure shipped the proposal banner inside the
tracked file, which is the self-contradiction recorded as DR-11 / CB1-R15.

### A2. Banner (`:7-13`) — two options

- Applied file: delete the banner entirely.
- Kept as an in-wave proposal: replace with

```text
> **Proposal status.** Refreshed at round-89 from seat CB1's proposal
> (.ufo/waves/round-89/followup/CB1-boundary-refresh.md); drift inventory in
> .ufo/waves/round-89/followup/CB1.md (CB1-R1…R19) and E1.md (DR-1…DR-17).
> Drop this block when the round-89 closure applies the text.
```

### A3. Checker pin (`:395-396`) — replace the `2ea9ef1` / `dcacffd6…` cell with

```text
- Checker at delivered `1b09f3f` (`corpus/fixtures/check_bible.py`, 435
  lines, sha256 `e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556`):
```

with the anchor remap listed in the basis block above (the doc's current list
`:157-159`, `:168`, `:171-312`, … is wrong by +14…+18 lines throughout;
CB1-R8/CB1-R9 hold the same remap).

### A4. Revision labels

Replace every delivered-behavior mention of `2ea9ef1` with `1b09f3f`
(20 occurrences per CB1-R9). Baseline `5eb9451` references stay.

### A5. Census / inventory / README evidence block (`:424-432`, `:445-449`, `:455-461`, `:473-477`, `:480-482`)

- Inventory paragraph (`:424-432`) — replace counts with the delivered
  measurement: 29 provenance directories; 105 provenance records; 12 records
  carry a duplicated-holder reference (13 field references) across 10
  directories (the ten:
  `r87-masked-break-from-ambiguous`, `r87-masked-break-to-ambiguous`,
  `r87-probe-multi-invalid`, `r87-probe-nonitem-kinds`,
  `r87-probe-record-and-chain`, `r87-probe-shape-ambiguous`, `r88-mixed-stop`,
  `r88-shape-ambiguous-armed`, `r89-c1-multi-cause-valid`,
  `r89-fn2-unresolved-chain-break`).
- README sentence (`:447-449`) — replace with: the `corpus/fixtures/README.md`
  has a `## Round 88` section at `:1008-1012` pointing readers to this
  document as the contract; it has **no** `## Round 89` section at `1b09f3f`,
  so the r89 amendments are stated only here (DR-13/CB1-R19; adding the README
  section is a separate r90 parity action, §E).
- Delivered-OBSERVED bullet (`:455-461`) — replace census numbers with
  160 fixture dirs / 9 changed stdout tuples / 0 exit changes / 0 stderr
  changes (E1 census; CB1's 165-directory run = the same 160 fixtures plus the
  five `corpus/live/runs/round-85/probe-inputs/*` dirs). Inventory: 29 dirs /
  105 records; 12 records carry a duplicated-holder reference (13 field
  references — `r87-probe-record-and-chain` record [0] hits both fields; this
  reconciles the "13 records" of earlier counts) across 10 dirs.
- UNKNOWN item (`:480-482`) — the second clause is now measured: the
  duplicated-holder reference set is fully enumerated (the ten dirs above);
  no other fixture references a duplicated holder id (`r60-unavailable*` have
  unparseable `entities.json` by design). Keep only "any external reader
  behavior change" as unknown.
- r87-table sentence (`:473-477`) — **factually wrong clause, fix the
  wording** (E1-measured; contradicted by CB1's refresh status split too, see
  §F1). Replace the final clause "and is not marked as historical anywhere in
  the tree" with: "which carries a `SUPERSEDED (round-88 closure)` banner at
  `:1-6` naming this document as the current contract
  (`sed -n '1,5p' corpus/knowledge/r87-provenance-chain-decision-table.md`,
  measured at `1b09f3f`); treat its notice/disclosure rows as history."

## B. Cause vocabulary (DR-1, DR-2, DR-3)

### B1. Cause-table rows 9, 10, 13 (`:152-153`, `:156`) — replace with

```text
| 9 | `holder reference to_holder {id!r} {raw_presence} absent from the resolved index` | `to_holder` resolves to no entity in the resolved index; `{raw_presence}` = `present in raw entities but` when ≥1 raw entity row carries the id, else `absent from raw entities and` | `:269-273` |
| 10 | `holder reference from_holder {id!r} {raw_presence} absent from the resolved index` | same for `from_holder` | `:279-286` |
| … | … | … | … |
| 13 | `source reference {id!r} {raw_presence} absent from the resolved index` | `source_id` resolves to no source row; `{raw_presence}` uses `raw sources` | `:302-307` |
```

(The local diagnostics `{record_label}.{field}: dangling entity {id!r}` and
`{record_label}.source_id: unknown in-world source {id!r}` are unchanged and
still match the doc — no edit there.)

### B2. Contract item 4 (`:104-112`, the "only place two cause phrases are combined") — replace the final sentence ("This is the only place two cause phrases are combined.") with

```text
On any invalid record, every cause the record reached is appended to a list
in check order and the list is joined with `; ` when the record is the
arming record (`:313-316`); no reached cause is dropped in favour of an
earlier one. The shape-invalid entry above is one such entry, not a special
case.
```

### B3. Contract item 2 (`:89-94`) — replace "the first stop condition the checker reached" with "the stop conditions the record reached (check order, joined with `; ` when several)";

## C. Decision table (DR-3, DR-4)

### C1. Row "Unique holder IDs; real discontinuity" (`:164`)

Restrict the row title to "Holder IDs each uniquely resolvable in the raw
table and the resolved index; real discontinuity" and note that the `input-structural finding, not sourced-canon; ` prefix is also hard-coded by the
qualified FN-2 forms (`:342`, `:348`), not only by an ambiguous source
citation. Evidence line gains `r89-fn2-control`.

### C2. Insert a fourth reference state after that row

(Adapt CB1's refresh row; text accepted as measured):

```text
| A referenced holder ID is not uniquely resolvable: ≥ 2 raw entity rows carry it but exactly one survives the field check | The comparison still runs, but findings involving that ID are qualified: `{record_label}: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: {detail}; got {…!r}` and/or `{record_label}.tick: input-structural finding, not sourced-canon; holder identity is not uniquely resolvable: {details}; provenance tick {…} must be greater than previous tick {…}` (`:327-333`, `:334-344`, `:345-350`); `{detail}` is `{reference} {id!r} is not uniquely resolvable ({raw} raw entity rows carry this id, but only {indexed} is in the resolved index)` (`:168-173`) | That the chain is definitely broken, or definitely intact — the expected or observed holder is not a single row | Repair the duplicate first (rename or merge), rerun, and re-read the comparison as a definite finding. Delivered evidence: `r89-fn2-unresolved-chain-break` vs `r89-fn2-control`. |
```

### C3. Row "Two causes in one shape-valid record" (`:169`) — replace with

```text
| Two or more causes in one record that passes the key-set check (e.g. bad tick AND ambiguous holder AND unknown source) | Every individual finding is emitted, and the `first stop:` clause names **all** of them, in check order, joined with `; ` — e.g. `malformed record (invalid tick); ambiguous holder identity to_holder 'x'; source reference 'y' absent from raw sources and absent from the resolved index` | A ranking, a single root cause, or severity order — the clause is an assessment-boundary statement; item-level causes (rows 1-3) still pre-empt it entirely | Read the record's own `VIOLATION:` lines for the full defect list; repair them together. Delivered evidence: `r89-c1-multi-cause-valid` (tick + ambiguity); three-cause record: scratch probe only (CB1.md §M4). |
```

## D. Limits, scratch/durable status, replay blocks (DR-3, DR-16, DR-17)

### D1. Precedence bullet (`:219-225`) — replace with

```text
- Causes are collected, not selected. Inside one record every reached cause
  is appended in check order and joined with `; ` at the arming record
  (`:313-316`). The join order is the order of the checks: `malformed record
  (invalid tick)` → `malformed record (invalid from_holder)` → `malformed
  record (invalid to_holder)` → dangling `to_holder` → dangling `from_holder`
  → `ambiguous holder identity` → `malformed record (invalid source_id)` →
  the source-reference causes. Item-level causes (rows 1-3) still pre-empt
  the record loop entirely.
```

### D2. "verified by CB1's scratch probes only … no durable fixture" (`:361-367`) and status list (`:462-467`) — refresh (DR-16)

Durable as of `1b09f3f` (E1 replays in `E1.md`):

- invalid tick — `r89-c1-invalid-tick`;
- invalid `from_holder` — `r89-c1-invalid-from-holder`;
- invalid `to_holder` — `r89-c1-invalid-to-holder`;
- malformed `source_id` — `r89-c1-malformed-source-id`;
- dangling `to_holder` / `from_holder` — `r89-f2-dangling-to` / `-from`
  (their README expectation strings are stale, see §E1);
- unknown source — `r89-f2-invalid-source-id` (misnomer; see §E1);
- multi-cause valid-key record — `r89-c1-multi-cause-valid`;
- FN-2 pair — `r89-fn2-unresolved-chain-break` / `r89-fn2-control`.

Still scratch-only (CB1-R14, corroborated): the two `present in raw … but`
FN-1 variants (E1 probe `p2-raw-present`, CB1 §M5), a three-cause record
(CB1 §M4), and the four FN-2 sub-branches (expected-side / observed-side /
tick / first-record). Keep those marked scratch-only.

### D3. Durable-fixture replay block (`:334-359`) — two of three pasted outputs are stale (DR-17, also H5 debt 2)

At `1b09f3f`, `r88-mixed-stop` and `r88-nonholder-stop` no longer print the
pasted `first stop: unknown source '…'` clause; the delivered clause is
`first stop: source reference 'f1-mixed-missing-source' absent from raw
sources and absent from the resolved index` (and `…'f1-nonholder-missing-source'…`
respectively). `r88-shape-ambiguous-armed` still reproduces byte-for-byte.
Refresh the two blocks or mark the section as an r88-era capture.

## E. Adjacent tracked files (outside the doc; r90 polish list)

### E1. Three `r89-f2-*` fixture READMEs quote pre-FN-1 cause strings (DR-8, CB1-R18, V2 check 2, JCAL3 debt 1, H2 F3) — exact fixes

- `corpus/fixtures/r89-f2-dangling-to/README.md:9` — replace
  ``names `dangling holder to_holder 'r89-f2-missing-to'` `` with
  ``names `holder reference to_holder 'r89-f2-missing-to' absent from raw entities and absent from the resolved index` ``.
- `corpus/fixtures/r89-f2-dangling-from/README.md:9` — same with
  `from_holder` / `r89-f2-missing-from`.
- `corpus/fixtures/r89-f2-invalid-source-id/README.md:9` — replace
  ``names `unknown source 'r89-f2-unknown-source'` `` with
  ``names `source reference 'r89-f2-unknown-source' absent from raw sources and absent from the resolved index` ``.
  Additionally re-scope or rename the directory: it exercises an *unknown*
  source, not a malformed/empty `source_id` (that branch is durably covered by
  `r89-c1-malformed-source-id`).

### E2. Nine fixture READMEs still say integration is pending (CB1-R17) — replace "integration verification pending" / "Expected after the C1 fix" with the delivered expectation

`r88-mixed-stop`, `r88-nonholder-stop`, `r88-shape-ambiguous-armed`,
`r89-c1-invalid-from-holder`, `r89-c1-invalid-tick`, `r89-c1-invalid-to-holder`,
`r89-c1-multi-cause-valid`, `r89-fn2-control`, `r89-fn2-unresolved-chain-break`
(measured with `grep -rln 'integration verification pending\|Expected after the C1 fix' corpus/fixtures/*/README.md`).

### E3. CB1-R18 overcount — `r87-probe-record-and-chain/README.md` does not quote a stale cause string

`grep -n "dangling holder\|unknown source '" corpus/fixtures/r87-probe-record-and-chain/README.md`
returns only prose class names (`:5-6`), no quoted expected output; the
stale-string README set is exactly the three files in §E1.

### E4. Other r90 parity items

- `corpus/fixtures/README.md` — add a `## Round 89` section covering the 11
  new dirs and the 4 excerpts (DR-13; also H5 debt 3, JDEP4, V2).
- `SCORECARD.md` — r89 closure record must retire the r88 bound "shape-valid
  multi-cause records name the first defect in field order" (`:135`, DR-14).
- Register naming — decide `corpus/knowledge/cross-cluster-contradictions.md`
  vs the demo `r89-cross-cluster-contradiction.md` before the first real
  conflict (DR-15).
- Code polish (r90, not doc): DR-5 null `from_holder` helper fix + fixture,
  DR-6 dedupe the double identity clause, DR-7 drop the unreachable
  `or 'malformed record'` fallback (`check_bible.py:316`).

## F. Corrections to apply to CB1's refresh (`CB1-boundary-refresh.md`) before adoption

1. **Status-split r87-table clause (refresh `:616-620`).** It repeats the
   tracked doc's false sentence "it is not marked as historical anywhere in
   the tree." Replace with the §A5 wording (banner at `:1-6` verified by
   `sed -n '1,5p' …` at `1b09f3f`). CB1's own evidence section (`:580-584`)
   already says "treat it as history", so the refresh is internally
   inconsistent on this point.
2. **Census basis.** The refresh's status split ("165-directory two-revision
   census") counts the 160 fixture dirs plus the 5 live probe-input dirs; state
   both so the number reconciles with the 160-dir fixture census and with the
   tracked doc's replacement numbers (§A5).
3. **CB1-R18 overcount** — see §E3; apply the stricter three-file set.

Reconciliation map (E1 drift → CB1 item): DR-1→CB1-R1, DR-2→CB1-R2,
DR-3→CB1-R4/R5/R6, DR-4→CB1-R7, DR-9→CB1-R8/R9, DR-10→CB1-R10/R11/R12,
DR-11→CB1-R15, DR-12→CB1-R12 + §F1 (residual), DR-16→CB1-R14, DR-17→H5 debt 2
(new). DR-5/6/7 (code defects), DR-8 (fixture READMEs → CB1-R17/R18),
DR-13/14/15 (README/SCORECARD/register) are outside the doc and outside
CB1's refresh; they stay on the r90 polish list (§E).
