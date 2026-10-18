# CB1 — Boundary-doc drift audit + refresh proposal

Seat: CB1 (round-88 follow-up wave, world-bible lane). Judged tree: `2ea9ef1`
(delivered), baseline `dfd1fbc`. All repository writes by this seat are this
report and `followup/CB1-boundary-refresh.md`. The tracked file
`corpus/knowledge/holder-assessment-boundary.md` was NOT edited.

## Work performed

1. Inventoried `corpus/knowledge/holder-assessment-boundary.md` (329 lines,
   sha256 `5c8c3fe67dde545cefbda2fcd8963c55b527c5a5ce50860eba32ceb8efcb3b6d`,
   blob `6f252d79079b7a473c442da787ba0e3c1d48f20b`) against the r88 checker
   `corpus/fixtures/check_bible.py` (395 lines, sha256
   `dcacffd6981e1af5f60b31bed20c6eccce25970444088e4ee2e30e3249411911`,
   blob `d35a6f714e025838d53b0b95f90ef13dff38c04b`). Confirmed the doc is
   byte-identical at `dfd1fbc` and `2ea9ef1` (`git diff --stat dfd1fbc 2ea9ef1
   -- corpus/knowledge/` lists only `r88-sourced-inspiration-decision-table.md`
   and `reference-ledger.md`): the C1 work commit changed the checker and did
   not touch the doc, so every provenance paragraph in it describes the r87
   branch.
2. Grepped the tree for both notice strings the doc quotes as delivered
   behavior. Both are absent from `corpus/fixtures/check_bible.py`; the only
   surviving occurrences are the doc itself and
   `corpus/knowledge/r87-provenance-chain-decision-table.md` (an r87 record
   artifact that is legitimately historical).
3. Re-ran the doc's own "Commands" replay (five r85 probe inputs) on the
   delivered tree and recorded the actual output.
4. Built scratch probes under `/tmp/cb1/probes2` and `/tmp/cb1/probes3`
   (derived from `corpus/fixtures/item-chain-valid`) to exercise every
   first-stop cause the delivered checker can arm, plus precedence and
   emission-order cases. Scratch only; no fixture was written to the repo.
5. Independently reproduced the C1 preservation census: `git archive dfd1fbc`
   into `/tmp/cb1/base`, then ran the baseline checker and the delivered
   checker against the same 149 fixture directories and compared
   `(exit code, stdout, stderr)` tuples.
6. Re-measured the doc's `UNKNOWN` fixture-inventory claim (provenance-bearing
   fixture directories; provenance records referencing a duplicated holder id).
7. Drafted the full refreshed doc as `followup/CB1-boundary-refresh.md`
   (proposal only).

## Before → after measurements

### 1. The two quoted notice strings are gone from the checker

```sh
grep -rn "unassessed at this and all later records" corpus/ reports/
grep -rn "unassessed because ambiguous holder identity" corpus/ reports/
```

Hits for the first string: `corpus/knowledge/holder-assessment-boundary.md:64`,
`:104`, `:201`, `:209`, `:216` and
`corpus/knowledge/r87-provenance-chain-decision-table.md:54`, `:93`, `:163`,
`:173`, `:210`. Hits for the second: the same doc at `:70`, `:104`, `:134`,
`:202`, `:203`, `:210`, `:217`, `:218` and the r87 table at `:55`, `:164`.
Zero hits in `corpus/fixtures/check_bible.py` for either string. The single
template that replaced them (`check_bible.py:194`) occurs only in
`corpus/fixtures/check_bible.py`:

```text
{record_label}: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: {cause} at {origin_label}
```

### 2. The doc's own replay no longer reproduces

Command (doc lines 183-186, verbatim, run from the lane root):

```sh
for case in r85-control r85-unique-break-control r85-masked-ambiguous r85-isolated-ambiguous r85-harbor-repro; do
  echo "=== $case ==="; python3 corpus/fixtures/check_bible.py corpus/live/runs/round-85/probe-inputs/"$case"; echo "[rc=$?]"
done
```

Observed at `2ea9ef1` (stderr empty in all five):

```text
=== r85-control ===
CLEAN: schema, citations, relations, timeline; 0 violations
[rc=0]
=== r85-unique-break-control ===
VIOLATION: entities[3].provenance[2]: provenance chain break; expected from_holder 'vault', got 'harbor'
1 violation(s); no canon changed
[rc=1]
=== r85-masked-ambiguous ===
VIOLATION: entities[5].id: duplicate entities id 'vault'
VIOLATION: entities[3].provenance[1].to_holder: ambiguous entity 'vault'
VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: ambiguous holder identity to_holder 'vault' at entities[3].provenance[1]
VIOLATION: entities[3].provenance[2]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: ambiguous holder identity to_holder 'vault' at entities[3].provenance[1]
4 violation(s); no canon changed
[rc=1]
=== r85-isolated-ambiguous ===
VIOLATION: entities[5].id: duplicate entities id 'vault'
VIOLATION: entities[3].provenance[2].to_holder: ambiguous entity 'vault'
VIOLATION: entities[3].provenance[2]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: ambiguous holder identity to_holder 'vault' at entities[3].provenance[2]
3 violation(s); no canon changed
[rc=1]
=== r85-harbor-repro ===
VIOLATION: entities[4].id: duplicate entities id 'harbor'
VIOLATION: entities[3].provenance[1].to_holder: ambiguous entity 'harbor'
VIOLATION: entities[3].provenance[1]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: ambiguous holder identity to_holder 'harbor' at entities[3].provenance[1]
VIOLATION: entities[3].provenance[2]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: ambiguous holder identity to_holder 'harbor' at entities[3].provenance[1]
VIOLATION: entities[3].provenance[2].from_holder: ambiguous entity 'harbor'
VIOLATION: timeline[0].place_id: ambiguous place entity 'harbor'
6 violation(s); no canon changed
[rc=1]
```

Against the doc's pasted r87 block (doc lines 188-223) the counts move
`5 → 4` (masked), `4 → 3` (isolated), `7 → 6` (harbor); the control and the
unique-holder break case are unchanged, and every remaining line's text
differs. No line of the doc's pasted block is reproducible verbatim at
`2ea9ef1`.

### 3. Cause vocabulary, precedence, and emission order (delivered `2ea9ef1`)

Scratch probes built from `corpus/fixtures/item-chain-valid` under
`/tmp/cb1/probes2` and `/tmp/cb1/probes3`; command form
`python3 corpus/fixtures/check_bible.py /tmp/cb1/probes3/<case>`. Each case
below is the *first* stop of its item, so the named cause is the item's actual
first stop.

| Probe | Injected state | Observed `first stop:` clause |
|---|---|---|
| `D-nosources` | `sources.json` absent | `source table unavailable at entities[3].provenance` |
| `B-nonitem` | `provenance` moved onto a `character` | `provenance attached to a non-item entity at entities[0].provenance` |
| `C-dupitemid` | second `seal` row | `duplicate item id 'seal' at entities[3].provenance` (and, separately, at `entities[4].provenance`) |
| `A-nondict` | `provenance[0]` is a string | `malformed record (expected object) at entities[3].provenance[0]` |
| `H-shape-plus-unknownsrc` | extra key **and** unknown `source_id` | `malformed record (unexpected field set) at entities[3].provenance[0]` |
| `I-invalidtick` | `tick = -1` | `malformed record (invalid tick) at entities[3].provenance[0]` |
| `F-dangling` | `to_holder = 'ghost'` | `dangling holder to_holder 'ghost' at entities[3].provenance[0]` |
| `O-dangling-from` | `from_holder = 'ghost'` | `dangling holder from_holder 'ghost' at entities[3].provenance[0]` |
| `M-both-fields-first` | `to_holder` and `from_holder` both duplicated `mira` | `ambiguous holder identity to_holder 'mira', from_holder 'mira' at entities[3].provenance[0]` |
| `E-unknownsrc` | `source_id = 'missing-source'` | `unknown source 'missing-source' at entities[3].provenance[0]` |
| `K-shape-ambiguous` | extra key + ambiguous `to_holder` | `malformed record (unexpected field set); ambiguous holder identity to_holder 'mira' at entities[3].provenance[0]` |

Precedence probes (two causes in one shape-valid record):

```text
=== J-tick-plus-ambiguity ===   (tick = -1 AND ambiguous to_holder at [0])
VIOLATION: entities[3].provenance[0].tick: required nonnegative integer
VIOLATION: entities[3].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: malformed record (invalid tick) at entities[3].provenance[0]
...
=== L-ambig-plus-unknownsrc ===   (ambiguous to_holder AND unknown source_id at [0])
VIOLATION: entities[3].provenance[0].to_holder: ambiguous entity 'mira'
VIOLATION: entities[3].provenance[0].source_id: unknown in-world source 'missing-source'
VIOLATION: entities[3].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: ambiguous holder identity to_holder 'mira' at entities[3].provenance[0]
```

Emission order (where the disclosure line sits relative to the record's own
findings):

```text
=== E-unknownsrc ===   (stop armed at [0] by the record's own source_id)
VIOLATION: entities[3].provenance[0].source_id: unknown in-world source 'missing-source'
VIOLATION: entities[3].provenance[0]: provenance continuity ... first stop: unknown source 'missing-source' at entities[3].provenance[0]
...
=== N-later-malformed ===   (stop at [0]; [1] is a non-dict)
VIOLATION: entities[3].provenance[1]: provenance continuity ... first stop: unknown source 'missing-source' at entities[3].provenance[0]
VIOLATION: entities[3].provenance[1]: expected object
```

So: at the arming record the disclosure follows that record's own findings; on
later records it precedes them.

### 4. Preservation census, independently reproduced

```sh
mkdir -p /tmp/cb1/base && git archive dfd1fbc | tar -x -C /tmp/cb1/base
# for each of the 149 direct children of corpus/fixtures: run
#   python3 /tmp/cb1/base/corpus/fixtures/check_bible.py <dir>      (baseline)
#   python3 corpus/fixtures/check_bible.py <dir>                    (delivered)
# and compare (returncode, stdout, stderr)
```

Observed:

```text
dirs= 149
before exits: {1: 118, 0: 31} after exits: {1: 118, 0: 31}
changed tuples: 12
  r61-independent-empty
  r61-independent-unavailable
  r87-masked-break-from-ambiguous
  r87-masked-break-to-ambiguous
  r87-probe-entry-shape
  r87-probe-multi-invalid
  r87-probe-nonitem-kinds
  r87-probe-record-and-chain
  r87-probe-shape-ambiguous
  r88-mixed-stop
  r88-nonholder-stop
  r88-shape-ambiguous-armed
exit changes: []
stderr changes: []
```

This matches the C1 claim (9 pre-existing changed + 4 new directories, of
which the provenance-free `r88-m3-maya-cluster` is tuple-identical, giving 12
changed tuples of 149; 0 exit changes; 0 stderr changes). The two `r61-*`
entries are the pre-r87 additive disclosures the claim names.

### 5. Fixture inventory the doc calls UNKNOWN

Doc lines 315-320 assert: "of the nine fixture directories containing
`provenance`, none does [combine `provenance` with a duplicated holder id]".
Measured at `2ea9ef1` by scanning every direct child of `corpus/fixtures` for
an `entities.json` array:

```text
dirs with provenance: 19
provenance records referencing a duplicated holder id: 11
   r87-masked-break-from-ambiguous   entities[3].provenance[0].from_holder = 'dup'
   r87-masked-break-to-ambiguous     entities[3].provenance[0].to_holder   = 'dup'
   r87-probe-multi-invalid           entities[5].provenance[1].from_holder = 'vault'
   r87-probe-nonitem-kinds           entities[5].provenance[1].from_holder = 'vault'
   r87-probe-record-and-chain        entities[5].provenance[0] (both fields), entities[5].provenance[1], entities[6].provenance[1]
   r87-probe-shape-ambiguous         entities[5].provenance[0].to_holder   = 'dup'
   r88-mixed-stop                    entities[5].provenance[1].to_holder   = 'f1-mixed-dup'
   r88-shape-ambiguous-armed         entities[4].provenance[0].to_holder   = 'f1-shape-dup'
```

Both halves of the doc's sentence are now false: the count is 19 not 9, and
the combination is covered by four durable fixtures (`r87-masked-break-to/from-ambiguous`,
`r88-mixed-stop`, `r88-shape-ambiguous-armed`) plus four r87 probe fixtures.

### 6. Helper still absent

```sh
$ ls corpus/fixtures/measure_holder_disclosure.py
ls: cannot access 'corpus/fixtures/measure_holder_disclosure.py': No such file or directory
```

The doc's "no five-gate score exists" statement is still true at `2ea9ef1`;
only its revision label (`2b48ca7`) is stale.

## Findings & named debt

### Drifted passages, quoted with line numbers (file is 329 lines at both `dfd1fbc` and `2ea9ef1`)

**D1 — front matter, `:3-5`.** "restated verbatim in 'The contract' below" —
the contract section is not a verbatim restatement of anything at `2ea9ef1`,
and its round-1 parenthetical no longer describes the checker.

**D2 — front matter, `:12-16`.** "The provenance branch was then revised by
round-87 seat C1 (commit `03c6746`, delivered tree `2b48ca7`); round-87 seat
I2 replayed the delivered checker and rewrote the contract, decision-table,
limits, and status sections below so they match its observed output" — the
revision now in the tree is the r88 C1 work (`2ea9ef1`), and those four
sections match the r87 output, not the delivered one.

**D3 — front matter, `:18-25`.** "verified-at: RUNTIME REPLAYED on the
delivered tree at `2b48ca7`" and `:20-22` "The `ambiguous entity` holder lines
and both `unassessed` notice forms below are demonstrated by that replay, not
contract text." There is now exactly one disclosure form; "both `unassessed`
notice forms" is not a state the checker can produce.

**D4 — `:27-38` recheck.** "Re-verify whenever the provenance branch of
`corpus/fixtures/check_bible.py` changes, either notice string or format
changes" — singular form now; and the whole paragraph's helper statement is
pinned to `2b48ca7`.

**D5 — `:54`.** "The delivered checker (`2b48ca7`) adds disclosure only:" —
false at `2ea9ef1`. The r88 branch re-bases the stop condition: chain
ineligibility now latches the first stop, and a shape-invalid dict carrying an
ambiguous holder id can arm it. The change is no longer disclosure-only.

**D6 — `:56-60` (contract item 1).** Line refs "delivered `:227` for
`to_holder`, `:238` for `from_holder`" drift; at `2ea9ef1` the two local
`ambiguous entity` lines are `:260` (to) and `:272` (from), with the
shape-invalid scan at `:217-219`. The behavior itself (both references get a
local line) still holds.

**D7 — `:61-65` (contract item 2). The largest single drift.** "Exactly one
item-level notice per item, located at the FIRST ambiguous-holder record —
even if an earlier invalid record already stopped comparisons. Notice text,
verbatim (delivered `:243`):" followed by
`{record_label}: provenance continuity and tick-order comparisons unassessed
at this and all later records because holder identity is ambiguous`. No
item-level notice exists at `2ea9ef1`; that exact string is absent from the
checker. The premise it encodes — that the item-level notice is located at the
first *ambiguous-holder* record — is also the over-attribution the r88 C1 fix
removed: the stop is now located at the first cause of any kind.

**D8 — `:66-78` (contract item 3).** The quoted per-record text
`{record_label}: … unassessed because ambiguous holder identity {field} {id!r}
first occurred at {origin_label}` (line 70) is absent from the checker, as are
its line refs `:250` and `:189-195`. The two behavioral claims inside this
item survive and should be re-pointed, not deleted: several references at one
record are joined `, ` in `to_holder` then `from_holder` order (confirmed
`M-both-fields-first`), and the disclosure names the first stop even when a
different duplicated id appears later (confirmed `L-ambig-plus-unknownsrc`,
`r88-mixed-stop`). The third claim — that the disclosure "appears on later
records that are not objects or lack the required keys" — survives
(`N-later-malformed`, `r87-probe-record-and-chain` entities[3]).

**D9 — `:79-82` (contract item 4).** "Emission does not depend on chain
eligibility: the disclosures appear even when `can_check_chain` was already
false, e.g. `provenance` on a non-item entity or an item whose own id is
duplicated (probes `p8`, `p7`)." The disclosures do still appear in those
cases, but the framing is now wrong: non-item provenance and duplicate item id
are themselves the named first cause (`B-nonitem`, `C-dupitemid`,
`r87-probe-nonitem-kinds`, `r87-probe-entry-shape`), i.e. chain ineligibility
is no longer orthogonal to the disclosure.

**D10 — `:83-92` (contract item 5).** "the 133 pre-round-87 fixture
directories … 0 tuple changes" plus line refs `:260-263`, `:264-271`,
`:272-273`. The analogous measured statement at `2ea9ef1` is 149 directories,
12 changed tuples (9 pre-existing + 3 new), 0 exit changes (§4 above); the
delivered refs are `:303` (the `first_stop is None` comparison gate),
`:311-312` (previous-value update), `:385-395` (CLI/exit).

**D11 — `:99` and `:104-106` (decision table).** Row `:104` quotes both
removed strings ("PLUS the item-level `…unassessed at this and all later
records because holder identity is ambiguous` notice … PLUS a per-record
`…unassessed because ambiguous holder identity {field} {id!r} first occurred
at {origin_label}` disclosure") and its "4 findings vs 5" figure is now
`3 vs 4`. Row `:105` ("Both stop notices still appear at the first
ambiguous-holder record even though comparisons stopped earlier … the
per-record disclosure names the ambiguity as cause even when an earlier
invalidity had already latched the gate (`I2.md` probe `p3`)") states exactly
the r87 defect the r88 fix closed; it is now inverted. Row `:103`'s "No
`ambiguous entity` line or `unassessed` notice is owed" still holds for
dangling holders but the word "notice" no longer names a distinct form.

**D12 — `:130-136` (editor checklist step 5).** "Every record at or after the
ambiguous-holder stop carries its own `unassessed because ambiguous holder
identity …` disclosure" — removed string, and "the ambiguous-holder stop"
should be "the first stop".

**D13 — `:146-149` (limits).** "Two notice forms, one boundary: the
item-level notice states the scope once ("at this and all later records"); the
per-record disclosure states the local status and the origin stop on every
affected record." There is one form and one emission per affected record; the
scope phrase "at this and all later records" no longer appears anywhere in the
output.

**D14 — `:140-145` (limits).** "at the ambiguous-holder record and ALL later
records of that item … delivered latch `:260-263`, gate `:264-271`" — the stop
is no longer tied to holder ambiguity, and both line refs drift.

**D15 — `:164-169` (limits).** "Chain eligibility upstream of this contract is
unchanged … The disclosures are NOT gated by it — they are emitted on any item
that carries `provenance`, even one whose chain was never eligible (delivered
`:189-195,242-250`)". Same drift as D9, plus stale refs.

**D16 — `:170-174` (limits).** Measurement-ceiling paragraph is still
accurate; only "No such score exists for `2b48ca7`" needs the revision label
updated (helper still absent — §6).

**D17 — `:176-250` (Commands).** The entire pasted r87 output block and the
"Against the pinned baseline this is 1 → 5 findings on `r85-masked-ambiguous`,
1 → 4 on `r85-isolated-ambiguous`, and 2 → 7 on `r85-harbor-repro`" sentence
(§2 above). The paragraph at `:229-233` describing the two `r87-masked-break-*`
fixtures is still behaviorally true and only needs re-pointing.

**D18 — `:252-268` (Evidence and citations).** Every "Checker at delivered
`2b48ca7` … (356 lines)" line ref drifts; the file is 395 lines. The baseline
`5eb9451` refs (`:157-159`, `:212-224`, `:234-237`, `:238-245`, `:246-247`,
`:168`, `:320-330`) are historical and stay.

**D19 — `:269-274`.** Round-87 evidence list cites `.ufo/waves/round-87/CB1.md`
"pre-C1 replay of the same five probes at `28706dc`" — that is a different
artifact from this report (same seat id, different round and different
mission); the refreshed doc should point at this file for the `2ea9ef1`
inventory and note the collision explicitly so the two are not conflated.

**D20 — `:298-320` (Status split).** "OBSERVED on the delivered tree (round-87
seat I2, `2b48ca7`)" plus the `UNKNOWN / UNMEASURED` sentence "of the nine
fixture directories containing `provenance`, none does" (§5 above: 19
directories, and the combination is covered by four durable fixtures).

**D21 — `:322-329` (Measured results).** Pinned to `2b48ca7`.

### Findings beyond drift (new information the refreshed doc should carry)

**F1 — "combined same-record cause summary" is narrower than the commit
message implies.** The `2ea9ef1` commit message says the fix names
"same-record simultaneous causes as a complete summary (parent amendment
closing seat C5B's over-attribution falsification)". Measured: the combined
summary is emitted only on the shape-invalid (wrong key set) branch, where the
cause is `malformed record (unexpected field set); ambiguous holder identity
{refs}`. In a shape-valid record the cause is the FIRST failing check in code
order — `malformed record (invalid tick)` → `malformed record (invalid
from_holder)` → `malformed record (invalid to_holder)` → `dangling holder
to_holder` → `dangling holder from_holder` → `ambiguous holder identity {refs}`
→ `malformed record (invalid source_id)` → `unknown source` → `source table
unavailable` — and later causes are not appended. Probe `J-tick-plus-ambiguity`
(invalid tick + ambiguous `to_holder` at one record) names only the tick;
probe `L-ambig-plus-unknownsrc` (ambiguous `to_holder` + unknown `source_id` at
one record) names only the ambiguity, while both local findings still print.
This is not a defect — every individual finding is still emitted, and the
disclosure is a statement about the assessment boundary rather than a complete
defect list — but the refreshed doc must state the bound, because an editor
reading only the cause clause would otherwise under-count the record's
problems. The refreshed doc carries this as an explicit precedence list.

**F2 — emission order differs between the arming record and later records.**
At the arming record the disclosure is appended after that record's own
findings (`check_bible.py:206`, `:233`, `:300-301`); on every later record it
is emitted at the top of the record loop, before them (`:198-200`). An editor
scanning "the line above my finding" will therefore see a different layout at
the stop record than after it. Named as a documentation fact, not as a defect.

**F3 — an item whose `provenance` is not a list gets no disclosure at all.**
`check_bible.py:178-180` reports `{label}: expected array` and `continue`s
before `first_stop` is computed. Confirmed on the delivered fixture
`r87-probe-entry-shape` (`entities[4].provenance: expected array`, no
`remain unassessed` line). The r87 doc never covered this; the refreshed doc
does, so the boundary is stated for all four entry shapes.

**F4 — a non-dict record cannot arm a holder-ambiguity cause.** The
shape-invalid holder scan (`:211-219`) only inspects dict records; a non-dict
record hits `:201` first. This is the stated bound in the C1 claim and is
confirmed by `A-nondict`.

**F5 — ambiguous SOURCE still does not stop comparisons.** The stop vocabulary
includes `unknown source` and `source table unavailable`, but `ambiguous`
source status only sets `chain_has_ambiguous_source` (`:294-295`) and prefixes
the comparison findings with `input-structural finding, not sourced-canon; `.
Confirmed on `r7-item-ambiguous` and `r87-probe-source-prefix`, whose chain
breaks and tick findings are still reported. This distinction is easy to lose
in the new cause vocabulary and is called out in the refreshed doc.

### Named debt

- **ND1 (this seat's scope, not resolved).** `corpus/knowledge/r87-provenance-chain-decision-table.md`
  (an r87 record artifact) also quotes both removed strings at `:54`, `:55`,
  `:93`, `:163`, `:164`, `:173`, `:210`. It is a historical round record and
  arguably should NOT be rewritten; but nothing in the tree currently marks it
  as superseded-by-r88. A future round should either add a one-line header
  pointing at the refreshed boundary doc or leave it and say so. CB1 did not
  touch it (no write scope for it).
- **ND2.** The refreshed doc cannot claim any five-gate score:
  `corpus/fixtures/measure_holder_disclosure.py` is still absent at `2ea9ef1`.
  Either land the helper or drop the entry point from the doc's contract
  surface in a later round.
- **ND3.** The refreshed doc's cause-precedence table is verified by CB1's
  scratch probes (`/tmp/cb1/probes2`, `/tmp/cb1/probes3`), which are not
  durable. The three landed `r88-*` fixtures cover unknown-source-first,
  unknown-source-only, and shape-ambiguous-armed; the precedence pairs
  (tick-vs-ambiguity, ambiguity-vs-unknown-source), dangling-holder causes,
  non-dict cause, non-item cause, and duplicate-item-id cause have no durable
  fixture. Named for the fixture-author seats.
- **ND4.** `corpus/fixtures/README.md` has no `## Round 88` section, so the
  boundary doc is currently the only place a reader can learn the delivered
  provenance behavior — which raises the cost of it being stale. Not this
  seat's scope.

### Verdict on this seat's mission (drift audit)

The mission was to inventory drift and draft a refresh; both are delivered.
The drift is total, not marginal: of the doc's five contract items, one
survives verbatim in behavior and wording (item 1's local `ambiguous entity`
lines), one survives only behaviorally with new wording (item 3's two claims),
one is inverted (item 4's eligibility framing), one is deleted outright
(item 2's item-level notice), and one is stale in its figures and line refs
(item 5). Two decision-table rows and one limits bullet state the r87 defect
as if it were current behavior. Per-axis: the audit itself is a measurement,
not an axis move; the refresh proposal is the axis-relevant artifact and is
handed off as a proposal only, since CB1 has no write scope on the tracked
file.

## Handoff

- `followup/CB1.md` — this report (drift inventory D1-D21, findings F1-F5,
  named debt ND1-ND4, exact commands and observed output for every claim).
- `followup/CB1-boundary-refresh.md` — the full refreshed doc, ready to be
  applied over `corpus/knowledge/holder-assessment-boundary.md` by whoever
  holds that write scope (round-1 dispatch names seat `R1Guide`; the r88 wave
  has no seat scoped to it). Every behavior in it is taken from the delivered
  tree at `2ea9ef1` and backed by a command in this report; nothing was
  written to the tracked file.
- Scratch material (not durable, not in the repo): `/tmp/cb1/base` (baseline
  archive of `dfd1fbc`), `/tmp/cb1/probes2`, `/tmp/cb1/probes3`,
  `/tmp/cb1/fixture-outputs.txt`, `/tmp/cb1/census.txt`.
- What the parent should decide: (a) whether the refresh is applied in this
  round by an authorized seat, in the next round, or not at all; (b) whether
  ND1 (the r87 decision table's stale quotes) gets a superseded-by marker;
  (c) whether F1's precedence bound belongs in the doc as a table (CB1's
  proposal does it that way) or as a footnote.
- No commit, push, registry write, tracked-file edit, or sibling-repo change
  was made by this seat.
