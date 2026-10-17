# Round-89 follow-up seat CB1 — doc-drift audit of `corpus/knowledge/holder-assessment-boundary.md`

Scope: inventory the tracked knowledge doc (refreshed at r88 closure, commit `51b286b`)
against the checker delivered by the r89 work wave (`1b09f3f`), quote every drifted
passage, and draft a refreshed document as a proposal. Baseline for the whole seat:
`51b286b`; delivered tree under audit: `1b09f3f` (tree clean, verified below).

Hard-rule compliance: no commit, no push, no tracked write outside
`.ufo/waves/round-89/followup/CB1.md` and
`.ufo/waves/round-89/followup/CB1-boundary-refresh.md`. Scratch lives in
`/dev/shm/cb1/` instead of `/tmp/cb1/` because `/tmp` hit inode exhaustion
(`df -i /tmp` → `1048576 1048576 0 100%`) mid-seat; `/tmp/cb1/probes2`,
`/tmp/cb1/probes3` and the other prior-seat scratch referenced by the tracked doc
were left untouched and unread beyond the two probe directories named there.

## Work performed

1. Read the tracked doc (492 lines) and diffed it against the r88 proposal it came
   from: the tracked file differs from `.ufo/waves/round-88/followup/CB1-boundary-refresh.md`
   only by the 4-line comment header added at closure — the "PROPOSAL — not applied"
   blockquote was carried into the tracked file verbatim (drift item CB1-R15).
2. Diffed the checker between the two revisions:
   `git diff 51b286b..1b09f3f -- corpus/fixtures/check_bible.py` — three
   amendment families (FN-1 raw-vs-resolved cause wording, multi-cause summary for
   every invalid record, FN-2 identity qualification of comparison findings).
3. Re-derived every delivered-checker line anchor by grepping the delivered file
   (no anchor copied from the doc or from the wave reports).
4. Ran a two-revision census over every input directory in the tree with an
   independent script (`/dev/shm/cb1/census.py`): the r88 checker extracted to
   `/dev/shm/cb1/check_bible_r88.py` (sha256 `dcacffd6…`, identical to the blob the
   doc names) versus the delivered `corpus/fixtures/check_bible.py`
   (sha256 `e2bb9639…`).
5. Replayed every provenance-relevant durable fixture on the delivered tree
   (five r85 live probes, three r88 fixtures, two r87 direction fixtures, ten r89
   fixtures) and pasted the raw output into the refresh proposal.
6. Built seven scratch probes (`/dev/shm/cb1/probes.py` plus an inline `p7`) for the
   branches with no durable fixture: both FN-1 "present in raw … but absent from the
   resolved index" variants, a three-cause valid-key record, and the four FN-2
   sub-branches (expected-side, observed-side, tick, first-record).
7. Re-measured the two inventory claims the doc makes about the tree
   (provenance-carrying directories, records referencing a duplicated holder id) and
   the README claim it makes about in-tree documentation coverage.
8. Wrote the refreshed document as a proposal only.
9. Final pre-handoff pass (same seat): re-ran the census, every pasted replay
   block, the M7 inventory, and all scratch probes against `1b09f3f`. All
   measurements reproduced; three numeric slips in this inventory's first
   draft were found and corrected (CB1-R7 row anchor `:164`; CB1-R9 count 18;
   CB1-R12 anchor `:447-449`), along with the CB1-R16 line set (`:104` carries
   no notice string).

Verification of the audited revision:

```sh
$ git log --oneline -1 && git status --short
1b09f3f lore r89: C1 cause-branch fixtures + multi-cause summary + FN-1/2, C2 r87 support completion, C3 R8-R10 governance — work wave (32 luna-max seats)
$ sha256sum corpus/fixtures/check_bible.py corpus/knowledge/holder-assessment-boundary.md
e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556  corpus/fixtures/check_bible.py
65fe6cfeb33ebe6e3676c210a337e570fa3eff1ccbbe934eccbed1b7fd7bdb60  corpus/knowledge/holder-assessment-boundary.md
$ wc -l corpus/fixtures/check_bible.py corpus/knowledge/holder-assessment-boundary.md
435 corpus/fixtures/check_bible.py
492 corpus/knowledge/holder-assessment-boundary.md
```

`git status --short` printed nothing (clean tree, no tracked write from this seat).

## Before → after measurements

### M1 — two-revision census (all input directories in the tree)

Command (script body in `/dev/shm/cb1/census.py`; each directory is run once with
each checker, `subprocess.run([sys.executable, checker, dir])`, tuples compared on
`(returncode, stdout, stderr)`):

```sh
python3 /dev/shm/cb1/census.py
```

Observed summary (verbatim):

```text
{
 "total_dirs": 165,
 "fixture_dirs": 160,
 "live_dirs": 5,
 "changed": [
  "fixtures/r87-probe-multi-invalid",
  "fixtures/r87-probe-record-and-chain",
  "fixtures/r88-mixed-stop",
  "fixtures/r88-nonholder-stop",
  "fixtures/r89-c1-multi-cause-valid",
  "fixtures/r89-f2-dangling-from",
  "fixtures/r89-f2-dangling-to",
  "fixtures/r89-f2-invalid-source-id",
  "fixtures/r89-fn2-unresolved-chain-break"
 ],
 "rc_changed": [],
 "stderr_changed": []
}
```

Before (doc claim, tracked `:118-128`): 149 fixture directories, 0 exit changes,
0 stderr changes, 12 changed stdout tuples (nine pre-existing + three r88).
After: 160 fixture directories, 0 exit changes, 0 stderr changes, **9** changed
stdout tuples — four pre-existing directories (`r87-probe-multi-invalid`,
`r87-probe-record-and-chain`, `r88-mixed-stop`, `r88-nonholder-stop`) plus five of
the eleven new `r89-*` directories. The other six new directories
(`r89-c1-invalid-from-holder`, `r89-c1-invalid-tick`, `r89-c1-invalid-to-holder`,
`r89-c1-malformed-source-id`, `r89-fn2-control`, `r89-inspiration-paraphrase`) are
tuple-identical to the r88 checker. This independently reproduces the wave's
"4 changed + 11 new" delta on the delivered tree and confirms 0 exit changes.

### M2 — the five r85 probe replays (the doc's "Commands" block)

```sh
for case in r85-control r85-unique-break-control r85-masked-ambiguous r85-isolated-ambiguous r85-harbor-repro; do
  echo "=== $case ==="; python3 corpus/fixtures/check_bible.py corpus/live/runs/round-85/probe-inputs/"$case"; echo "[rc=$?]"
done
```

Observed output is byte-identical to the block the doc pastes under "Commands"
(4 / 3 / 6 findings for masked / isolated / harbor-repro, control `CLEAN`, unique
break unchanged). The doc's pasted r85 block therefore survives r89 unedited; only
its revision label is stale.

### M3 — the drifted cause strings, before → after (durable fixtures)

Dangling `to_holder` (new r89 fixture, no r88 counterpart):

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r89-f2-dangling-to
```

```text
--- r88 checker (51b286b)
VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: dangling holder to_holder 'r89-f2-missing-to' at entities[3].provenance[1]
--- delivered checker (1b09f3f), same directory
VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: holder reference to_holder 'r89-f2-missing-to' absent from raw entities and absent from the resolved index at entities[3].provenance[1]
```

Unknown source (durable r88 fixture, wording changed in place):

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-mixed-stop
```

```text
--- r88 checker
first stop: unknown source 'f1-mixed-missing-source' at entities[5].provenance[0]
--- delivered checker
first stop: source reference 'f1-mixed-missing-source' absent from raw sources and absent from the resolved index at entities[5].provenance[0]
```

### M4 — multi-cause summary, before → after

Durable fixture:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r89-c1-multi-cause-valid
```

```text
--- r88 checker
VIOLATION: entities[2].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: malformed record (invalid tick) at entities[2].provenance[0]
--- delivered checker
VIOLATION: entities[2].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: malformed record (invalid tick); ambiguous holder identity to_holder 'r89-c1-multi-cause-valid-ambiguous-holder' at entities[2].provenance[0]
```

Scratch probe with three simultaneous causes (no durable fixture; `/dev/shm/cb1/probes.py`, probe `p3-triple-cause-valid`):

```text
VIOLATION: entities[2].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: malformed record (invalid tick); ambiguous holder identity to_holder 'dup'; source reference 'ghost-source' absent from raw sources and absent from the resolved index at entities[2].provenance[0]
```

### M5 — FN-1 raw-vs-resolved variants (scratch only)

Both `present in raw … but` variants have no durable fixture in the tree
(`grep -o "present in raw [a-z]* but" /dev/shm/cb1/census.json` → no match).
Probes `/dev/shm/cb1/probes.py` `p1-raw-present-holder` / `p2-raw-present-source`
(one raw row per id, rejected by the field check):

```text
VIOLATION: entities[1].first_appearance: required nonempty str
VIOLATION: entities[2].provenance[1].to_holder: dangling entity 'ghost'
VIOLATION: entities[2].provenance[1]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: holder reference to_holder 'ghost' present in raw entities but absent from the resolved index at entities[2].provenance[1]
VIOLATION: sources[1].title: required nonempty str
VIOLATION: entities[1].provenance[1].source_id: unknown in-world source 's-ghost'
VIOLATION: entities[1].provenance[1]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: source reference 's-ghost' present in raw sources but absent from the resolved index at entities[1].provenance[1]
```

Excerpts: each probe also repeats the same disclosure once more on its next
record (`entities[2].provenance[2]` / `entities[1].provenance[2]`) and ends
with its `N violation(s)` count line; both elided above.

Note the asymmetry the doc must state: the local finding lines keep the old shape
(`… dangling entity {id!r}` / `… unknown in-world source {id!r}`); only the
`first stop:` clause distinguishes "no raw row at all" from "raw rows exist but none
survives the field check".

### M6 — FN-2 qualification, before → after

Durable fixture pair:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r89-fn2-unresolved-chain-break
python3 corpus/fixtures/check_bible.py corpus/fixtures/r89-fn2-control
```

```text
--- r89-fn2-unresolved-chain-break, r88 checker
VIOLATION: entities[4].provenance[1]: provenance chain break; expected from_holder 'f3-dup', got 'mira'
--- r89-fn2-unresolved-chain-break, delivered checker
VIOLATION: entities[4].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'
--- r89-fn2-control, delivered checker (unchanged from r88)
VIOLATION: entities[3].provenance[1]: provenance chain break; expected from_holder 'f3-dup', got 'mira'
```

Excerpts: on `r89-fn2-unresolved-chain-break` both revisions print the
unrelated `entities[1].first_appearance: required nonempty str` schema error
before the quoted line (complete output in the refresh proposal §Commands);
the `r89-fn2-control` output above is complete.

Scratch sub-branches (no durable fixture):

```text
p4-fn2-from-only  : …: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'a'
p7-fn2-observed-only: …: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'a'; got 'dup'; from_holder 'dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index)
p5-fn2-tick       : entities[3].provenance[1].tick: input-structural finding, not sourced-canon; holder identity is not uniquely resolvable: expected from_holder 'dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); from_holder 'dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); provenance tick 5 must be greater than previous tick 5
p6-fn2-first-record: entities[2].provenance[0]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: from_holder 'dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); first record must have from_holder null
```

Reachability, read off the delivered code (`:168-173`, `:257-297`, `:320-350`):
a record only reaches a comparison when it is valid, and a valid record requires
each referenced holder id to have resolved-index count exactly 1. The detail
function returns `None` only when raw count and resolved count are both 1, so the
qualifier fires **exactly** when the referenced id has ≥ 2 raw rows of which exactly
one survives the field check (`raw_entity_id_counts` counts dict rows with a
nonempty string `id`, `:72-76`, regardless of schema validity; the resolved index is
built from rows that pass the field check, `:82-83`, `:85-91`). A plain
duplicate — two rows both schema-valid — never reaches a comparison at all, because
it makes the referencing record ambiguous and therefore invalid. Consequently FN-2
fires on the "one duplicate row was rejected by the field check" class only, which
is what the durable fixture pins.

### M7 — anchor, inventory, and README claims

| Doc claim (tracked line) | Delivered observation |
|---|---|
| checker "395 lines, sha256 `dcacffd6…`" (`:395`) | 435 lines, sha256 `e2bb9639…` |
| "19 directories carry `provenance`; 11 provenance records across eight of them" (`:424-432`) | 29 directories carry `provenance`; 13 records across ten directories reference a duplicated holder id (command below) |
| "The README has no `## Round 88` section, so this document is the only in-tree statement of the delivered provenance behavior" (`:447-449`) | false: `corpus/fixtures/README.md:1008` is `## Round 88: stop-cause disclosure + second cluster`, added at `51b286b`, and it points readers to this document. No `## Round 89` section exists at `1b09f3f` |
| "`corpus/fixtures/measure_holder_disclosure.py` does not exist at `2ea9ef1`" (`:52`, `:380`) | still absent at `1b09f3f`: `ls corpus/fixtures/*.py` → `corpus/fixtures/check_bible.py` only |

Inventory command (stdlib walk of `corpus/fixtures/*/entities.json`):

```sh
python3 - <<'EOF'   # full script in the seat transcript; counts dirs, provenance dirs, dup-holder records
EOF
```

```text
fixture dirs: 160
dirs carrying provenance: 29
records referencing a duplicated holder id: 13
  r87-masked-break-from-ambiguous   entities[3].provenance[0].from_holder  'dup'
  r87-masked-break-to-ambiguous     entities[3].provenance[0].to_holder    'dup'
  r87-probe-multi-invalid           entities[5].provenance[1].from_holder  'vault'
  r87-probe-nonitem-kinds           entities[5].provenance[1].from_holder  'vault'
  r87-probe-record-and-chain        entities[5].provenance[0].to_holder    'dup'
  r87-probe-record-and-chain        entities[5].provenance[0].from_holder  'dup'
  r87-probe-record-and-chain        entities[5].provenance[1].from_holder  'dup'
  r87-probe-record-and-chain        entities[6].provenance[1].to_holder    'dup'
  r87-probe-shape-ambiguous         entities[5].provenance[0].to_holder    'dup'
  r88-mixed-stop                    entities[5].provenance[1].to_holder    'f1-mixed-dup'
  r88-shape-ambiguous-armed         entities[4].provenance[0].to_holder    'f1-shape-dup'
  r89-c1-multi-cause-valid          entities[2].provenance[0].to_holder    'r89-c1-multi-cause-valid-ambiguous-holder'
  r89-fn2-unresolved-chain-break    entities[4].provenance[0].to_holder    'f3-dup'
```

Baseline anchors the doc keeps as history were spot-checked against
`git show 5eb9451:corpus/fixtures/check_bible.py` (330 lines): `:168` relation-endpoint
ambiguity, `:212-224` dangling/silent branches, `:234-237` `can_check_chain = False`
latch, `:238-245` comparison gate, `:246-247` previous-value update — all match, so
the "The contract" paragraph's baseline half needs no change.

## Findings & named debt

### Drift inventory (quote → delivered)

Cause-table rows (`## First-stop causes`, tracked `:136-157`):

- **CB1-R1** (`:152`) — `| 9 | \`dangling holder to_holder {id!r}\` | \`to_holder\` absent from entities | \`:255-258\` |`
  → delivered `holder reference to_holder {id!r} absent from raw entities and absent from the resolved index` (no raw row) or `holder reference to_holder {id!r} present in raw entities but absent from the resolved index` (raw rows, none field-valid), `:269-273`.
- **CB1-R2** (`:153`) — same for `from_holder`: `| 10 | \`dangling holder from_holder {id!r}\` |` → `holder reference from_holder {id!r} {raw_presence} absent from the resolved index`, `:279-286`.
- **CB1-R3** (`:156`) — `| 13 | \`unknown source {id!r}\` | \`source_id\` resolves to no source row |` → `source reference {id!r} absent from raw sources and absent from the resolved index` / `… present in raw sources but absent from the resolved index`, `:302-307`.
- **CB1-R4** (`:110`) — "(`:227-230`). This is the only place two cause phrases are combined."
  → false at `1b09f3f`: every invalid record joins all of its simultaneous causes with `; ` (`:313-316`); the shape-invalid branch keeps its own combined string (`:236-244`) as one of several entries in that list.
- **CB1-R5** (`:219-225`) — "Cause precedence inside a shape-valid record (first failing check wins, and later causes are NOT appended to the clause)" and "The only combined clause is the shape-invalid one, item 5 of the cause table."
  → false. Check order still fixes the order *inside* the joined string, and item-level causes still pre-empt the record loop (`:198-203`), but no record cause is dropped any more.
- **CB1-R6** (`:169`) — decision-table row "Two causes in one shape-valid record": "the named `first stop:` clause names only the FIRST check in precedence order — a bad tick masks a simultaneous ambiguity; an ambiguous holder masks a simultaneous unknown source" and "Only the shape-invalid branch combines two cause phrases".
  → false; both masking statements are contradicted by `r89-c1-multi-cause-valid` (M4) and probe `p3` (three causes).

FN-2, absent from the doc in every section:

- **CB1-R7** — the doc's "Unique holder IDs; real discontinuity" row (`:164`) and its "What the output does NOT say" cell assert the unconditional form `{record_label}: … provenance chain break; expected from_holder {…!r}, got {…!r}`. Delivered adds three qualified forms (`:334-344`, `:345-350`, `:327-333`) plus the detail string `{reference} {id!r} is not uniquely resolvable ({raw} raw entity rows carry this id, but only {indexed} is in the resolved index)` (`:168-173`), and the doc never states that a comparison finding can now be non-definite. The row's claim that `input-structural finding, not sourced-canon; ` is prefixed only by an ambiguous **source** citation (`:164`, `:253-256`) is also incomplete: the qualified chain-break form hard-codes that prefix (`:342`, `:348`).

Anchor and revision drift (all of `## First-stop causes`, `## Decision table`, `## Precise limits`, `## Evidence and citations`, `## Status split`, `## Measured results`):

- **CB1-R8** — every delivered-checker anchor the doc cites is an r88 anchor. Delivered mapping: disclosure template `:194` → `:206-208`; item-level tests `:183-189` → `:198-203`; top-of-loop emission `:198-200` → `:212-214`; non-dict branch `:201-206` → `:215-221`; key-set branch `:208-234` → `:222-248`; field validation `:239-295` → `:249-312`; latch `:296-302` → `:313-319`; comparison gate `:303-312` → `:320-352`; ambiguous-source flag `:294-295` → `:311-312`; CLI `:385-395` → `:425-435`. New code the doc must cite: raw counters `:38-39`, `:72-76`; resolved index `:82-83`, `:85-91`, `:97`; `holder_identity_detail` `:168-173`.
- **CB1-R9** — revision label `2ea9ef1` appears 18 times (`grep -o 2ea9ef1 corpus/knowledge/holder-assessment-boundary.md | wc -l`); the four on `:9`, `:28`, `:29`, `:35` are historical statements about the r88 rewrite and its verification that stay correct, while the other 14 label the current/delivered tree and are stale (delivered `1b09f3f`): `:52`, `:72`, `:120`, `:136`, `:218`, `:267`, `:273`, `:380`, `:395`, `:424`, `:455`, `:462`, `:478`, `:486`. The checker size/hash cell `:395` (`395` lines, `dcacffd6…`) is now `435` lines, `e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556`.
- **CB1-R10** (`:118-128`) — the preservation census numbers (149 dirs / 12 changed tuples) are superseded by M1 (160 dirs / 9 changed tuples, 0 exit changes, 0 stderr changes).
- **CB1-R11** (`:424-432`) — the provenance inventory (19 dirs / 11 records / eight dirs) is superseded by M7 (29 dirs / 13 records / ten dirs).
- **CB1-R12** (`:447-449`) — the "README has no `## Round 88` section" claim is false (README `:1008`), and the doc's own evidence line asserting the README dependency is therefore backwards: the README now cites this doc, which raises the cost of the doc being stale.
- **CB1-R13** (`:48-53`, `:376-382`) — the recheck trigger list does not mention the r89 triggers: the raw counters, `holder_identity_detail`, the `not uniquely resolvable` string, or the `; ` joining.
- **CB1-R14** (`:462-467`) — the "OBSERVED only in scratch probes at `2ea9ef1` (no durable fixture)" list is now partly durable: invalid tick, invalid `from_holder`, invalid `to_holder`, invalid `source_id`, dangling `to_holder`, dangling `from_holder`, unknown source all have r89 fixtures. Still scratch-only: the two FN-1 `present in raw … but` variants, the three-cause valid-key record, and the four FN-2 sub-branches (expected-only, observed-only, tick, first-record). Both-fields ambiguity, non-item provenance, duplicate item id, unavailable source table, and non-dict record are covered by older fixtures (`r87-probe-record-and-chain`, `r61-*`), not by scratch.

Self-referential header drift:

- **CB1-R15** (`:7-14`) — the tracked file still opens with `> **PROPOSAL — not applied.** This file is round-88 seat CB1's refreshed version of \`corpus/knowledge/holder-assessment-boundary.md\`` while *being* that file: `diff <(git show 51b286b:corpus/knowledge/holder-assessment-boundary.md) .ufo/waves/round-88/followup/CB1-boundary-refresh.md` shows the tracked file adds only the 4-line comment header, so the closure applied the proposal verbatim and kept its banner. The comment header's "every line anchor re-verified against the r88 checker (dcacffd6) by seat CB1" was true at `51b286b` and is false at `1b09f3f`.

Adjacent drift (outside the doc, reported not fixed — no write scope):

- **CB1-R16** — `corpus/knowledge/r87-provenance-chain-decision-table.md` still quotes the removed r87 notice strings; measured at `1b09f3f`, the two strings occupy lines `:60`, `:61`, `:99`, `:169-172`, `:179-182`, `:216-218`, `:222-223`, `:238-240`, `:268-269`, `:271`, `:281-283` (identical positions at `51b286b` — the table was last revised at r88 closure and is unchanged at `1b09f3f`). The tracked doc's pointer to that file (`:475-477`) cites `:54`, `:55`, `:93`, `:163`, `:164`, `:173`, `:210`; those match the r87-era revision (`dfd1fbc`) where the strings sat at `:54`, `:55`, `:93`, `:163-166`, `:173-176`, `:210-212` among others — so the doc's own evidence line is stale too. Row 33 (`:104`) still expects the r87 six-finding output including an `item-level notice` the delivered checker never prints (`r87-probe-multi-invalid` delivered = 5 findings). The table is still not marked historical anywhere in the tree.
- **CB1-R17** — 9 fixture READMEs still describe their expectations as pending integration: `corpus/fixtures/{r88-mixed-stop,r88-nonholder-stop,r88-shape-ambiguous-armed,r89-c1-invalid-from-holder,r89-c1-invalid-tick,r89-c1-invalid-to-holder,r89-c1-multi-cause-valid,r89-fn2-control,r89-fn2-unresolved-chain-break}/README.md` contain "integration verification pending" or "Expected after the C1 fix", although the fix is delivered.
- **CB1-R18** — 4 fixture READMEs quote cause strings that no longer exist: `corpus/fixtures/{r87-probe-record-and-chain,r89-f2-dangling-from,r89-f2-dangling-to,r89-f2-invalid-source-id}/README.md` still print `dangling holder …` / `unknown source '…'` as expected output.
- **CB1-R19** — `corpus/fixtures/README.md` has `## Round 88` but no `## Round 89` section, so the delivered FN-1/FN-2/multi-cause behavior is stated nowhere in the tree except the refreshed doc proposed here.

### Independent corroboration from sibling seats (r89 follow-up)

- **H2** (`H2.md:260-265`) reproduces the same delta — "4 changed / 11 added / 0 removed of 160 dirs, 0 exit changes / 0 violation-count changes" — and files F5: "stale behavioural claims and shifted anchors in `corpus/knowledge/holder-assessment-boundary.md`, the file the guide cites as the current contract".
- **H5** (`H5.md:136-152`, `:229-235`) calls the same doc "stale on every surface the r89 wording change touched" (cause rows 9/10/13, the precedence paragraph, the decision row, a replay block that "no longer reproduces") and reports shifted code lines (`:184-185`→`:199`, `:255-258`→`:269-272`, `:304-310`→`:331-350`).
- **E1** (`E1.md:176-185`) carries a parallel drift inventory against the same doc (DR-1, DR-2: cause rows 9/10/13 and the raw-presence wordings).
- **JCAL3** (`JCAL3.md:53-57`, `:85-87`) and **V2** (`V2.md:200-203`) measure the fixture-README side of the same drift (3 of 11 r89 fixture READMEs quote pre-FN-1 strings — "no — quoted string differs"), matching CB1-R17/R18.
- **H1** (`H1.md:29-31`) independently reproduces the census delta ("145 unchanged, 4 changed, 0 exit flips, 0 stderr cases" of 160).
- **JCAL1** (`JCAL1.md:229-234`) rules calibration "improved (bounded)" on the same two cause-text changes this doc fails to describe.
- **P3** (`P3-log-r89.md:209`) records the staleness as "a documentation harm … not netted"; **P4** (`P4-shonen.md`, D3) recommends refreshing the doc at `:365-367`/`:462-465`.
- JCOV1/JCOV3/JCOV4 and JDEP2/JDEP4 do not mention this doc (grep across the followup directory); their C2/C3 surfaces are outside the drift inventory above.

### Named debt (this seat)

1. **No write scope on the tracked doc** — the refresh is a proposal; applying it needs a seat holding scope on `corpus/knowledge/holder-assessment-boundary.md` (or a parent integration). Unchanged from r88.
2. **Two FN-1 variants and four FN-2 sub-branches have no durable fixture.** The refreshed doc marks them scratch-only; a fixture seat should promote at least `present in raw … but` for holders and sources and the tick/first-record FN-2 forms, since those strings are now contract text.
3. **`measure_holder_disclosure.py` is still absent at `1b09f3f`** — no five-gate score can exist for the delivered tree; the refreshed doc keeps the "REPLAYED, not scored" status.
4. **Scratch location deviation** — this seat's probes live in `/dev/shm/cb1/`, not `/tmp/cb1/`, because `/tmp` inodes are exhausted. If `/tmp` is cleaned, the r88 scratch evidence the tracked doc cites (`/tmp/cb1/probes2`, `/tmp/cb1/probes3`) is itself at risk; that is fleet-level debt worth recording.

## Handoff

- **Deliverable 1**: `.ufo/waves/round-89/followup/CB1.md` (this file) — drift inventory CB1-R1…R19 with quoted passages, independent census, replays, and scratch probes.
- **Deliverable 2**: `.ufo/waves/round-89/followup/CB1-boundary-refresh.md` — the complete refreshed document, marked as a proposal, written against the delivered checker at `1b09f3f` (sha256 `e2bb9639…`, 435 lines), with every anchor re-derived and every pasted output reproduced by this seat. Apply by replacing `corpus/knowledge/holder-assessment-boundary.md` with its body (drop the proposal banner), or cherry-pick the sections flagged CB1-R1…R15.
- **Judging note for the round record**: the doc is the lane's only statement of the delivered provenance contract, and three of its 14 cause rows (9, 10, 13), its combined-clause statement, its precedence bullet, one whole decision-table row, and every line anchor were wrong at `1b09f3f`. The r85 replay block and the baseline half of "The contract" were still correct; the drift is concentrated in the r88→r89 amendments and in the README claim.
- **Untouched / not verified**: nothing in `corpus/live/` beyond the five r85 probe directories; the C2/C3 r89 artifacts (excerpts, D1 rows) are outside this seat's mission; `corpus/knowledge/r89-cross-cluster-contradiction.md` was not audited.
- **No receipt was fabricated**: every command in this report was run on the delivered tree at `1b09f3f`, and every pasted output is the observed stdout (stderr empty in all runs except where noted; no run produced stderr).
