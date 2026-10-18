# JCAL4 — Round-88 follow-up: wording / overclaim audit of the C1 disclosure template

Judged on the DELIVERED tree at `2ea9ef1` (baseline `dfd1fbc`, tree clean; both
re-verified below). Scratch probes live under `/tmp/jcal4/`; no tracked file was
written except this report. No commit, push, or registry write.

Seat block line references (`check_bible.py:128, 145-147, 229-236`) were resolved
against the delivered file: `:128` is the `cannot assess event …` message, `:145-147`
is the entities-loop voice (`{location}.kind: unknown kind {…!r}`), and `:229-236` is
the combined-summary `first_stop` assignment plus the `report_unassessed` call at
`:233`. All three land on the intended regions; no stale-reference defect.

## Axes named

- **A1 first-stop causal accuracy** — does the disclosure name the record that actually
  stopped the chain, and does that name stay stable down the tail?
- **A2 overclaim boundary** — is the input-structural-not-sourced-canon qualifier on
  every disclosure, and does any disclosure assert a break, a canon fact, or an identity choice?
- **A3 same-record cause completeness** — does the landed string deliver the declared
  "complete summary" of simultaneous causes at the first-stop record?
- **A4 voice / register consistency** — does the new template read like the checker's
  other messages, and is the qualifier rendered consistently inside one file?
- **A5 delivered-tree doc consistency** — do the fixture READMEs and knowledge docs
  describe the strings the delivered checker actually prints?

## Work performed

- Verified tree state and pinned both artifacts:

  ```sh
  git -C /home/vgpnk/Projects/shokunin/lore-shokunin log --oneline -1
  git -C /home/vgpnk/Projects/shokunin/lore-shokunin status --porcelain
  sha256sum corpus/fixtures/check_bible.py
  ```

  ```text
  2ea9ef1 lore r88: C1 stop-cause repair + C2 Maya cluster + C3 inspiration table — work wave (37 luna-max seats)
  <status: empty>
  dcacffd6981e1af5f60b31bed20c6eccce25970444088e4ee2e30e3249411911  corpus/fixtures/check_bible.py
  ```

- Read the single disclosure emitter and all four call sites
  (`check_bible.py:192-194` definition; calls at `:200`, `:206`, `:233`, `:301`), the
  pre-loop latch (`:184-189`), the record-level latch (`:296-301`), the combined-summary
  branch (`:227-233`), and the competing qualifier rendering (`:306`, `:308`, `:310`).
- Built a baseline archive for before→after comparison:

  ```sh
  rm -rf /tmp/jcal4/base && mkdir -p /tmp/jcal4/base && git archive dfd1fbc | tar -x -C /tmp/jcal4/base
  sha256sum /tmp/jcal4/base/corpus/fixtures/check_bible.py
  ```

  ```text
  3ae4134d1d7d0f4b72f5ed0b344de54e886b60ab7cacd8e8ab0008521efcb237  /tmp/jcal4/base/corpus/fixtures/check_bible.py
  ```

  This matches the baseline SHA E1 cited, so the before-state is the same artifact E1 read.
- Ran a mechanical whole-census audit of every disclosure line in all 149 fixture dirs
  (parser, duplicate-per-record check, forbidden-word check, per-chain origin-stability
  check, and an independent "origin == earliest invalid record" check).
- Ran four authored scratch probes under `/tmp/jcal4/probes/` for the multi-cause paths
  the durable fixtures do not cover.
- Compared `.ufo/waves/round-88/patches/E1-r88-wording.md` (E1's three templates) against
  the landed string, element by element, and read the docs that describe the provenance
  branch (`corpus/knowledge/holder-assessment-boundary.md`,
  `corpus/knowledge/r87-provenance-chain-decision-table.md`, the three r87/r88 fixture READMEs).

## Before → after measurements

### Baseline vs delivered on the same fixtures

```sh
cd /tmp/jcal4/base && python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-probe-shape-ambiguous
cd /home/vgpnk/Projects/shokunin/lore-shokunin && python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-probe-shape-ambiguous
```

```text
BASE (dfd1fbc)                                              DELIVERED (2ea9ef1)
VIOLATION: entities[1].id: duplicate entities id 'dup'      VIOLATION: entities[1].id: duplicate entities id 'dup'
VIOLATION: entities[5].provenance[0]: expected exactly …    VIOLATION: entities[5].provenance[0]: expected exactly …
2 violation(s); no canon changed                            VIOLATION: entities[5].provenance[0].to_holder: ambiguous entity 'dup'
                                                            VIOLATION: entities[5].provenance[0]: … remain unassessed (input-structural finding, not sourced-canon); first stop: malformed record (unexpected field set); ambiguous holder identity to_holder 'dup' at entities[5].provenance[0]
                                                            VIOLATION: entities[5].provenance[1]: … remain unassessed (input-structural finding, not sourced-canon); first stop: malformed record (unexpected field set); ambiguous holder identity to_holder 'dup' at entities[5].provenance[0]
                                                            5 violation(s); no canon changed
```

Baseline: 2 findings, 0 unassessed lines (the r87 residual). Delivered: 5 findings,
2 disclosure lines, both naming the shape-invalid record as the first stop.

```sh
cd /tmp/jcal4/base && python3 corpus/fixtures/check_bible.py /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r88-mixed-stop
cd /home/vgpnk/Projects/shokunin/lore-shokunin && python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-mixed-stop
```

```text
BASE tail (over-attribution):                               DELIVERED tail (correct attribution):
VIOLATION: entities[5].provenance[1]: … unassessed because  VIOLATION: entities[5].provenance[0]: … remain unassessed (input-structural finding, not sourced-canon); first stop: unknown source 'f1-mixed-missing-source' at entities[5].provenance[0]
  ambiguous holder identity to_holder 'f1-mixed-dup'        VIOLATION: entities[5].provenance[1]: … first stop: unknown source 'f1-mixed-missing-source' at entities[5].provenance[0]
  first occurred at entities[5].provenance[1]               VIOLATION: entities[5].provenance[2]: … first stop: unknown source 'f1-mixed-missing-source' at entities[5].provenance[0]
```

The mixed-stop over-attribution is closed on a durable fixture: the later ambiguity at
`[1]` no longer replaces the earlier unknown source at `[0]`.

```sh
cd /tmp/jcal4/base && python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-masked-break-to-ambiguous
cd /home/vgpnk/Projects/shokunin/lore-shokunin && python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-masked-break-to-ambiguous
```

```text
BASE: 6 findings — includes BOTH forms:                       DELIVERED: 5 findings — ONE form only:
  … unassessed at this and all later records because holder     (no item-level notice)
    identity is ambiguous                                     VIOLATION: entities[3].provenance[0]: … remain unassessed (input-structural finding, not sourced-canon); first stop: ambiguous holder identity to_holder 'dup' at entities[3].provenance[0]
  … unassessed because ambiguous holder identity to_holder      VIOLATION: entities[3].provenance[1]: … first stop: ambiguous holder identity to_holder 'dup' at entities[3].provenance[0]
    'dup' first occurred at entities[3].provenance[0]           VIOLATION: entities[3].provenance[2]: … first stop: ambiguous holder identity to_holder 'dup' at entities[3].provenance[0]
```

The r87 item-level notice is removed; one accurate per-record disclosure replaces the
two-form (redundant, over-attributing) pair. Disclosures: 3 → 3, but each is now the same
string and the stop-record notice no longer appears twice.

### Whole-census mechanical audit (149 dirs, delivered tree)

```sh
python3 - <<'PY'   # full script in this session; parser + invariants, output below
PY
```

```text
dirs=149 findings=367 disclosure_lines=47
dirs_with_disclosure=12
violations_found=0        # 0 unparsed lines, 0 duplicate-per-record, 0 forbidden-word hits
clean_dirs= 31 nonzero= 118     # matches the commit's 31 clean / 118 violations claim
chains_with_disclosures=17  chains_with_inconsistent_origin_or_cause=0
first-stop-index_mismatches: 0 record-level (all 3 reported lines were array-label pre-loop origins)
distinct first-stop cause forms (normalized):
   11  malformed record (expected object)
   10  unknown source 'X'
    6  duplicate item id 'X'
    5  provenance attached to a non-item entity
    5  ambiguous holder identity from_holder 'X'
    4  malformed record (unexpected field set); ambiguous holder identity
    3  ambiguous holder identity to_holder 'X'
    2  ambiguous holder identity to_holder 'X', from_holder 'X'
    1  source table unavailable
```

Invariants proven mechanically on the delivered tree:

- **A2 — qualifier on every disclosure.** The disclosure is emitted from exactly one
  f-string (`:194`); all 47 disclosure lines across all 149 dirs match
  `remain unassessed \(input-structural finding, not sourced-canon\); first stop: …`.
  `grep -n "unassessed\|first stop" corpus/fixtures/check_bible.py` returns only `:192`
  and `:194` plus the four call sites — there is no second disclosure emitter.
- **A1 — carried stability.** All 17 chains with disclosures name exactly one
  (origin, cause) pair across every record of the chain. 0 chains disagree.
- **A1 — origin accuracy.** For the 14 chains whose origin is a record locator, the named
  origin equals the earliest record in that chain carrying an invalidating finding
  (0 mismatches). The other 3 chains are pre-loop stops whose origin is the `.provenance`
  array label.
- **A2 — no forbidden assertion.** 0 disclosure lines contain `break`, `chose`, `choice`,
  or `canon` outside the negated qualifier.
- One disclosure per record: 0 duplicate-per-record hits.

### A3 — multi-cause probes (scratch, `/tmp/jcal4/probes/`)

Case A — valid key set, `tick: -1` **and** ambiguous `to_holder`:

```sh
python3 corpus/fixtures/check_bible.py /tmp/jcal4/probes/A
```

```text
VIOLATION: entities[4].provenance[0].tick: required nonnegative integer
VIOLATION: entities[4].provenance[0].to_holder: ambiguous entity 'f1-shape-dup'
VIOLATION: entities[4].provenance[0]: … remain unassessed (input-structural finding, not sourced-canon); first stop: malformed record (invalid tick) at entities[4].provenance[0]
VIOLATION: entities[4].provenance[1]: … first stop: malformed record (invalid tick) at entities[4].provenance[0]
```

Case B — valid key set, dangling `to_holder` **and** unknown `source_id`:

```sh
python3 corpus/fixtures/check_bible.py /tmp/jcal4/probes/B
```

```text
VIOLATION: entities[4].provenance[0].to_holder: dangling entity 'f1-shape-ghost'
VIOLATION: entities[4].provenance[0].source_id: unknown in-world source 'f1-shape-missing'
VIOLATION: entities[4].provenance[0]: … first stop: dangling holder to_holder 'f1-shape-ghost' at entities[4].provenance[0]
VIOLATION: entities[4].provenance[1]: … first stop: dangling holder to_holder 'f1-shape-ghost' at entities[4].provenance[0]
```

Durable confirmation on the shipped fixture `r87-probe-multi-invalid`
(`entities[5].provenance[1]` carries ambiguous `from_holder` **and** unknown source):

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-probe-multi-invalid
```

```text
VIOLATION: entities[5].provenance[1].from_holder: ambiguous entity 'vault'
VIOLATION: entities[5].provenance[1].source_id: unknown in-world source 'ghost-source'
VIOLATION: entities[5].provenance[1]: … first stop: ambiguous holder identity from_holder 'vault' at entities[5].provenance[1]
```

Cause selected by `record_stop_cause = record_stop_cause or …` (`:246`, `:250`, `:254`,
`:258`, `:270`, `:281`, `:285`, `:290`, `:293`): the first cause in field order wins and
the rest are dropped from the summary. The complete-summary join exists only in the
unexpected-key-set branch (`:227-230`) and for multiple ambiguous holder fields
(`:277-281`).

### A4 — voice measurements

```sh
python3 -  # static scan of error templates in check_bible.py
```

```text
static error-message templates: 48
templates containing a literal "(" : 3   (:125 expected-one-of list, :194 disclosure, :357 double-booked prior_place)
assess-verb  :128  {side_location}.event_id: cannot assess event {event_id!r}: timeline.json unavailable
assess-verb  :194  {record_label}: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: …
disclosure :194 len=167   other 47 templates: min=23 median=53 max=188
```

### A5 — doc drift at the delivered tree

```sh
git diff --name-only dfd1fbc 2ea9ef1 -- corpus/knowledge/
```

```text
corpus/knowledge/r88-sourced-inspiration-decision-table.md
corpus/knowledge/reference-ledger.md
```

Neither `holder-assessment-boundary.md` nor `r87-provenance-chain-decision-table.md` was
touched, and neither were the r87 fixture READMEs. Their stated contracts:

- `corpus/knowledge/holder-assessment-boundary.md` (declares `verified-at: RUNTIME REPLAYED
  … at 2b48ca7`, `:12-14`) still states the **two**-form contract and quotes strings that no
  longer exist at `:64`, `:70`, `:104-106`, `:201-218`, with line anchors `:243`, `:250`,
  `:189-195` that no longer point at any disclosure (the delivered emitter is `:194`).
  Its own recheck clause says "Re-verify whenever the provenance branch of
  `corpus/fixtures/check_bible.py` changes" — the r88 wave changed that branch and did not
  re-verify.
- `corpus/knowledge/r87-provenance-chain-decision-table.md` rows 14-15 (`:54-55`) quote the
  removed item-level notice and the old per-record wording. The file declares its snapshot
  as `2b48ca7`, so it is not a false claim about the delivered tree — but no r88 superseding
  row was added, so the tree's decision table now describes the previous round's strings.
- `corpus/fixtures/r87-probe-shape-ambiguous/README.md:1` still asserts "Expected: 2 findings
  … Zero 'unassessed' lines. Pre-existing behavior, unchanged by C1; candidate r88
  calibration/depth move." Delivered: 5 findings, 2 unassessed lines.
- `corpus/fixtures/r87-masked-break-to-ambiguous/README.md:1` and
  `…-from-ambiguous/README.md:1` still expect "the item-level stop notice, and a per-record
  disclosure …". Delivered output has no item-level notice (5 findings, 3 disclosures).

### E1 templates vs landed string (drift table)

| E1 element (`patches/E1-r88-wording.md`) | Landed at `2ea9ef1` | Drift |
|---|---|---|
| T1: `… remain unassessed from {first_stop_label} onward in this chain (input-structural finding, not sourced-canon); the shape-invalid dict at {first_stop_label} carried ambiguous holder reference {field} {id!r}, recognized as a stop trigger` | `… remain unassessed (input-structural finding, not sourced-canon); first stop: malformed record (unexpected field set); ambiguous holder identity to_holder 'dup' at entities[5].provenance[0]` | scope phrase "from X onward in this chain" dropped; "the shape-invalid dict … carried ambiguous holder reference …" replaced by a two-part cause summary; "recognized as a stop trigger" dropped |
| T2: `first stop at {first_stop_label}: {summary}` | `first stop: {cause} at {origin_label}` | word order swapped (cause before locator); the trailing ` at X` now attaches after a possibly multi-part cause |
| T3: `first stop at {label}: non-holder cause {summary}` | `first stop: {cause} at {label}` | the `non-holder cause` marker is gone; holder and non-holder causes are no longer distinguished lexically |
| Emission rule: choose T1/T2/T3 by first-stop kind | one template; the cause string varies | three templates collapsed to one |
| Bound: pre-loop cases (unavailable source, non-item, duplicate item id) "need a separate scope decision; do not invent a record-level first cause when no stop record was established" | `:184-189` assigns `first_stop` to those pre-loop conditions and prints `first stop: … at entities[k].provenance` | E1's reserved case was resolved **in the opposite direction**: a `first stop` is emitted with the array label as origin |

Drift that is a **gain**: dropping "recognized as a stop trigger" removes a claim about
internal latch behaviour that E1 itself warned could drift. Drift that is **neutral**:
dropping "in this chain" — the landed locators are absolute record locators, so the
cross-chain ambiguity JCAL2 raised is mitigated by construction. Drift that is a **cost**:
the pre-loop `first stop … at <array>` phrasing (A1/A4 debt below).

## Findings & named debt

**Verdicts (per axis, on the delivered tree at `2ea9ef1`; no scalars):**

- **A1 first-stop causal accuracy — improved.** 14/14 record-level chains name the earliest
  invalid record as the origin; 17/17 chains keep one stable (origin, cause) down the tail;
  the mixed-stop over-attribution is closed on the durable `r88-mixed-stop` fixture and on
  `r87-probe-record-and-chain` (`entities[6]` now keeps `entities[6].provenance[0]` instead
  of the later ambiguity at `[1]`). This is the axis C1 targeted and it moved.
- **A2 overclaim boundary — improved.** The qualifier is on all 47 disclosure lines by
  construction (one emitter), and 0 disclosure lines assert a break, a canon fact, or an
  identity choice. The wording deliberately names only "provenance continuity and tick-order
  comparisons", so "remain unassessed" stays literally true even though schema/keys/dangling/
  source diagnostics do keep running on later records — that is a real precision gain over
  the r87 "unassessed because …" phrasing.
- **A3 same-record cause completeness — claim accuracy harmed; landed string unchanged.**
  The landed string never asserts completeness, so it is not false. But the round's own
  claim text ("same-record simultaneous causes named as a complete summary", commit message;
  "the record's complete simultaneous causes", `r88-shape-ambiguous-armed/README.md:9`)
  holds only for the unexpected-key-set branch and for multiple ambiguous holder fields.
  On valid-key-set records with several causes, one cause is named and the rest are dropped:
  case A (tick + ambiguous holder → only the tick), case B (dangling holder + unknown source
  → only the dangling holder), and the shipped `r87-probe-multi-invalid` (ambiguous
  `from_holder` + unknown source → only the holder). The fixture README's phrase is
  fixture-local and true there, but reads as a general contract.
- **A4 voice / register consistency — unchanged, with named debt.** Structurally the
  disclosure matches the checker's house shape (`VIOLATION: `, `<locator>: `, `; `-joined
  clauses, `N violation(s); no canon changed` trailer), so it is not a register break. Two
  concrete inconsistencies remain: (i) the same qualifier is rendered as a parenthetical at
  `:194` but as a prefix `input-structural finding, not sourced-canon; ` at `:306`/`:308`/`:310`
  — two house styles for one phrase in one file; (ii) the assess verb is `remain unassessed`
  at `:194` versus `cannot assess event … :` at `:128`, the closest analogue. The disclosure
  is also the longest message in the file (167 chars vs median 53) and is one of only three
  templates containing a literal `(`.
- **A5 delivered-tree doc consistency — harmed.** Three fixture READMEs and two knowledge
  docs still describe the strings the r88 change removed, including the r87 residual
  (`r87-probe-shape-ambiguous/README.md` still says "Zero 'unassessed' lines … unchanged by
  C1", which the delivered checker contradicts) and the editor-facing
  `holder-assessment-boundary.md`, whose recheck clause the wave did not honour.

**Named debt (for round closure):**

1. **A3** — either narrow the claim to the branch that implements it, or extend the
   `:296-301` latch to join all of the record's causes the way `:227-230` does. The landed
   wording needs no change either way; only the claim text or the join does.
2. **A5** — refresh `corpus/knowledge/holder-assessment-boundary.md` (two-form contract →
   one-form contract, re-anchor `:243/:250/:189-195` → `:194`, `:200/:206/:233/:301`) and add
   a superseding row set or snapshot note to `r87-provenance-chain-decision-table.md`.
   Update the three fixture READMEs' expected-output sections.
3. **A1/A4** — the pre-loop origins (`source table unavailable`, `provenance attached to a
   non-item entity`, `duplicate item id …`) are printed as `first stop: … at
   entities[k].provenance`, i.e. an array label presented as a stop. It is accurate (the
   array label is genuinely earlier than any record) and it closes the r87 no-disclosure gap
   for those paths, but E1 explicitly reserved this case as a scope decision. Either accept
   the array-label origin as the decided scope and say so in the boundary doc, or use a
   different phrase for non-record stops.
4. **A4** — pick one rendering for the qualifier inside `check_bible.py` (parenthetical or
   prefix) so the file has a single house style.

**Not found (checked, clean):** no fabricated receipt; no second disclosure emitter; no
duplicate disclosure per record; no disclosure line asserting a break, canon, or identity
choice; no exit-status change from the wording work (`r87-probe-shape-ambiguous` and the
new r88 fixtures all still exit 1 with the same non-disclosure diagnostics).

## Handoff

- Report: `.ufo/waves/round-88/followup/JCAL4.md` (this file). No other repo write.
- **Verdict recommendation: keep the C1 wording change.** It is improved on A1 and A2, the
  two axes C1 targeted, and it removes an over-attributing notice form; A3's gap is in the
  claim text, not in the emitted string, so it does not falsify the wording. Do not record
  A3 as satisfied and do not record A5 as satisfied: both are open at the delivered tree.
  Recommend the round record carry A3 and A5 as named debt rather than a claim of closure.
- Evidence for the parent: baseline checker SHA `3ae4134d…` (`dfd1fbc`), delivered SHA
  `dcacffd6…` (`2ea9ef1`); 149 dirs, 367 findings, 47 disclosure lines, 31 clean / 118
  violations; 17/17 chains origin-stable; 14/14 record-level origins == earliest invalid
  record; 0/47 qualifier or forbidden-word violations; A3 gap reproduced on case A, case B,
  and `r87-probe-multi-invalid`; A5 drift reproduced on 3 READMEs + 2 knowledge docs.
- Scratch (not evidence of record, retained for replay): `/tmp/jcal4/base` (baseline
  archive), `/tmp/jcal4/probes/A`, `/tmp/jcal4/probes/B`.
- Gap: I did not run a human/reader-interpretation test of the disclosure string, so
  "no causal overclaim" is established for the string's own assertions and for the
  mechanical invariants above, not for reader comprehension.
- **Overlap with a sibling seat (do not double-count).** `followup/JDEP4.md` reaches the
  same conclusion independently on the knowledge-doc half of A5 ("depth: harmed", both
  `corpus/knowledge` docs present the superseded r87 wording as current). Treat the
  knowledge-doc drift as one corroborated finding, not two. JCAL4's unique A5 contribution
  is the fixture-README half (`r87-probe-shape-ambiguous/README.md` "Zero 'unassessed'
  lines … unchanged by C1"; the two `r87-masked-break-*` READMEs' "item-level stop notice"),
  plus the E1-template-vs-landed drift table and the A3 claim-vs-delivery gap. JDEP4 also
  records the same delivered checker SHA `dcacffd6…`, so the two audits share an artifact.
- Round-record note (not my seat's write): `SCORECARD.md:113` still labels the r88 claims
  "planned", and `l0-questions.md` carries a K1 round-88 append; both are outside the
  wording audit and are flagged only so the parent does not read them as JCAL4 output.
