# JCAL2 — calibration judge #2 (adversarial cause-falsification), round 88 follow-up

Tree judged: `2ea9ef1` (work commit; `dfd1fbc` = r87 closure baseline), working tree clean at
start and end of this seat's work. No tracked file was written by this seat; no commit, push,
or registry write. Scratch: `/tmp/JCAL2/` (probes, receipts, scripts). Baseline checker for
every before-state was extracted with
`git show dfd1fbc:corpus/fixtures/check_bible.py > /tmp/JCAL2-base-checker.py`.

```
sha256 delivered corpus/fixtures/check_bible.py @2ea9ef1 = dcacffd6981e1af5f60b31bed20c6eccce25970444088e4ee2e30e3249411911
sha256 baseline  (dfd1fbc:corpus/fixtures/check_bible.py) = 3ae4134d1d7d0f4b72f5ed0b344de54e886b60ab7cacd8e8ab0008521efcb237
```

## Work performed

Mission: try to make the delivered first-stop disclosure name a cause that did **not** operate,
using 6 constructed inputs with controls that prove which causes actually operated. All probes
are scratch-only (`/tmp/JCAL2/probes`, `probes2`, `probes3`); every measurement below is a run of
the delivered checker (or, for the before-state, of the dfd1fbc checker) on a real directory.

Probe generation and runs:

```
python3 /tmp/JCAL2/gen.py    # 30 dirs: the 6 required families + controls + x-* extras
python3 /tmp/JCAL2/run.py    # runs baseline+delivered on each; writes receipts/probe-receipts.json
python3 /tmp/JCAL2/gen2.py   # 8 dirs: decisive contrast + item-row/empty-table controls
python3 /tmp/JCAL2/gen3.py   # 4 dirs: invalid item row carrying provenance; non-dict-then-ambiguity
python3 /tmp/JCAL2/audit.py  # whole-corpus census + mechanical cause audit of every disclosure
```

The 6 required inputs and their controls (all dirs under `/tmp/JCAL2/`):

| # | required input | probe dir | controls that prove which causes operated |
|---|---|---|---|
| 1 | well-formed record, invalid tick AND ambiguous holder | `probes/p1-invalid-tick-ambiguous` | `p1-ambiguous-only` (tick 0), `p1-invalid-tick-only` (unique holder), `p1-clean` |
| 2 | same-record key-set violation + ambiguous holder | `probes/p2-shape-ambiguous` | `p2-shape-only`, `p2-shape-ambiguous-unknown-source`, `p2-shape-ambiguous-invalid-tick` |
| 3 | non-dict record after an armed stop | `probes/p3-nondict-after-stop` | `p3-nondict-first`, `p3-nondict-last-clean-prefix`, `probes3/z-nondict-then-ambiguity` |
| 4 | second item in one bible with a healthy chain | `probes/p4-two-items` | `p4-two-items-brokenB` (B's break still reported ⇒ B was assessed), `p4-two-items-stopB-clean` (no disclosure may touch item A) |
| 5 | `from_holder` null vs missing | `probes/p5-null-midchain-after-stop`, `p5-missing-fromholder`, `p5-missing-fromholder-ambiguous-to` | `p5-null-midchain-no-stop`, `p5-null-fromholder-first` |
| 6 | dup-id holder, all other record fields valid | `probes/p6-dup-holder-all-valid` | `p6-unique-holder`, `p6-dup-holder-one-row-invalid`, `p6-dup-holder-unknown-source`, `p6-dup-holder-invalid-tick` |

Extra families: `x-*` (holder row / source row schema-invalid, ambiguous source + break,
duplicated item id, provenance on non-item), `y-*` (true-dangling vs present-but-invalid row in
one bible, sources.json absent vs empty, ambiguity first occurring at record 1, shape-invalid
`from_holder` ambiguity, ambiguity + dangling in one record), `z-*` (invalid item row carrying
provenance, non-dict then ambiguity, invalid item row + ambiguous holder).

Dependencies: no sibling report was waited on for this seat's method; `JCAL1/3/4/5`, `CB1`,
`JDEP*` landed in `followup/` while I worked and were read only after my measurements, to avoid
claiming their findings as mine. No gap was left by an absent dependency.

## Before → after measurements

### 1. Independent census — reproduces the C1 claim exactly

```
$ python3 /tmp/JCAL2/audit.py
before_dirs=145 (dfd1fbc)  after_dirs=149 (2ea9ef1, +4 new)
pre-existing 145 dirs: violation lines 331 → 352
exit 0: 30 → 30 ; exit != 0: 115 → 115 ; exit changes: [] ; stderr non-empty: 0 → 0
changed tuples among the 145: 9
  r61-independent-empty, r61-independent-unavailable, r87-masked-break-from-ambiguous,
  r87-masked-break-to-ambiguous, r87-probe-entry-shape, r87-probe-multi-invalid,
  r87-probe-nonitem-kinds, r87-probe-record-and-chain, r87-probe-shape-ambiguous
delivered 149 dirs: exit 0 = 31, exit != 0 = 118
new-dir exits: r88-m3-maya-cluster 0, r88-mixed-stop 1, r88-nonholder-stop 1, r88-shape-ambiguous-armed 1
```

`git ls-tree dfd1fbc corpus/fixtures/ | grep -c '^040000'` → `145`;
`git ls-tree 2ea9ef1 corpus/fixtures/ | grep -c '^040000'` → `149`. The 9 changed tuples and
0 exit changes match the C1 claim tuple-for-tuple, and the two r61 entries are the claimed
pre-r87 additive disclosures. Independent of `B1/B2/X1`.

### 2. Whole-corpus cause audit — every disclosure's named cause checked against its fixture

`audit.py` re-derives, for each of the 149 fixtures, the expected disclosure set (item-level
precondition → earliest cause-bearing record → every record from there on), then for each
emitted disclosure verifies that the named cause is among the causes that actually operate at
the named origin record, that the origin record is the earliest cause-bearing record of that
item, and that no disclosure is emitted for a record before the stop.

```
47 disclosure records in 12 fixtures (18 fixtures carry provenance on a valid entity row)
fixtures with cause-audit mismatches: NONE (0)
distinct named causes observed in the delivered corpus:
  ambiguous holder identity to_holder 'dup' | from_holder 'dup' | to_holder 'dup', from_holder 'dup'
  ambiguous holder identity from_holder 'vault'
  malformed record (expected object)
  malformed record (unexpected field set); ambiguous holder identity to_holder 'dup'
  malformed record (unexpected field set); ambiguous holder identity to_holder 'f1-shape-dup'
  duplicate item id 'rope' | provenance attached to a non-item entity | source table unavailable
  unknown source 'ghost-source' | unknown source 'f1-mixed-missing-source' | unknown source 'f1-nonholder-missing-source'
```

So on the landed corpus, **no named cause fails to operate**, none is missing, and none is
emitted before the stop. My audit's expected-cause model is a re-reading of the delivered code,
so its independent value is the origin/precedence check plus the raw-file cross-check below;
the falsification power comes from the probes in §3.

### 3. The 6 required inputs — delivered vs baseline, with controls

**(1) invalid tick + ambiguous holder, well-formed key set** — `p1-invalid-tick-ambiguous`:

```
after : entities[4].provenance[0].tick: required nonnegative integer
        entities[4].provenance[0].to_holder: ambiguous entity 'dup'
        ... [0]: ... first stop: malformed record (invalid tick) at entities[4].provenance[0]
        ... [1]: ... first stop: malformed record (invalid tick) at entities[4].provenance[0]
before: ... [0]: ... unassessed because ambiguous holder identity to_holder 'dup' first occurred at [0]
```

Controls: `p1-ambiguous-only` names `ambiguous holder identity to_holder 'dup'` (so the
ambiguity arms a stop on its own); `p1-invalid-tick-only` names `malformed record (invalid
tick)`; `p1-clean` exits 0. **Both causes operated in record 0; the disclosure names one of
them (the tick). No false naming — but the disclosure is not a combined summary.** Precedence
changed from the baseline (which named the holder ambiguity here): the delivered precedence is
field-branch order, not detection order (see FN-4).

**(2) key-set violation + ambiguous holder** — `p2-shape-ambiguous`:

```
after : entities[4].provenance[0]: expected exactly tick, from_holder, to_holder, source_id
        entities[4].provenance[0].to_holder: ambiguous entity 'dup'
        ... first stop: malformed record (unexpected field set); ambiguous holder identity to_holder 'dup' at entities[4].provenance[0]
```

Controls: `p2-shape-only` → `malformed record (unexpected field set)`; `p2-shape-ambiguous-unknown-source`
(source `missing-source` on the same record) and `p2-shape-ambiguous-invalid-tick` (tick `-1`)
produce the **identical** disclosure and **no line at all** for the unknown source or the
invalid tick. The summary is therefore complete only with respect to the causes the shape
branch inspects (FN-5). No false naming: both named causes operated.

**(3) non-dict record after an armed stop** — `p3-nondict-after-stop` (record 0 unknown source):

```
after : ... [1]: ... first stop: unknown source 'missing-source' at entities[2].provenance[0]
        entities[2].provenance[1]: expected object
        ... [2]: ... first stop: unknown source 'missing-source' at entities[2].provenance[0]
```

Controls: `p3-nondict-first` names `malformed record (expected object)`; `z-nondict-then-ambiguity`
(non-dict at 0, ambiguous holder at 1) names `malformed record (expected object)` at `[0]` and
does **not** name the later ambiguity — the r87 over-attribution is closed. **Pass.**

**(4) per-item isolation** — `p4-two-items`: item A (`entities[3]`) stops, item B (`entities[4]`)
is a healthy 3-record chain; delivered output contains disclosures for A's records only, and
**no** disclosure line mentions `entities[4]`. Control `p4-two-items-brokenB` still reports
`entities[4].provenance[1]: provenance chain break; expected from_holder 'mira', got 'tower'`,
proving B was assessed rather than skipped. Control `p4-two-items-stopB-clean` puts the stop on
B and leaves A untouched. **No leak in either direction. Pass.**

**(5) `from_holder` null vs missing** — three probes, all consistent:

```
p5-null-midchain-after-stop   → disclosure names the earlier unknown source only; no from_holder cause claimed
p5-null-midchain-no-stop      → entities[2].provenance[1]: provenance chain break; expected from_holder 'mira', got None
p5-missing-fromholder         → ... first stop: malformed record (unexpected field set)
p5-missing-fromholder-ambiguous-to → ... first stop: malformed record (unexpected field set); ambiguous holder identity to_holder 'dup'
p5-null-fromholder-first      → CLEAN (exit 0)
```

Control `p5-null-midchain-no-stop` proves the null-mid-chain cause operates when assessable, so
its absence in the stopped variant is the stop, not a missed check. Missing vs null are never
conflated in the wording. **Pass.** (Delivered `check_bible.py:215-216`,
`if field == 'from_holder' and holder_id is None: has_holder_id = False`, is a no-op — `None`
already fails `isinstance(holder_id, str)`; harmless, named below.)

**(6) dup-id holder, all other fields valid** — `p6-dup-holder-all-valid`:

```
after : entities[1].id: duplicate entities id 'dup'
        entities[4].provenance[0].to_holder: ambiguous entity 'dup'
        ... first stop: ambiguous holder identity to_holder 'dup' at entities[4].provenance[0]   (records [0] and [1])
```

Control `p6-unique-holder` exits 0 (proves the duplicate armed the stop); `p6-dup-holder-unknown-source`
and `p6-dup-holder-invalid-tick` show the single-cause naming of FN-4. **Naming accurate. Pass.**
But see FN-2 for the variant of this same input where the duplicate is invisible to the index.

### 4. Decisive control for the false-naming class (FN-1)

`y-true-dangling-vs-invalid-row` puts, in one bible, an item whose `to_holder` is `mira`
(entities.json `entities[0]`, present but schema-invalid: empty `first_appearance`) and an item
whose `to_holder` is `ghost` (does not occur in entities.json at all):

```
after : entities[0].first_appearance: required nonempty str
        entities[2].provenance[0].to_holder: dangling entity 'mira'
        entities[2].provenance[0]: ... first stop: dangling holder to_holder 'mira' at entities[2].provenance[0]
        entities[3].provenance[0].to_holder: dangling entity 'ghost'
        entities[3].provenance[0]: ... first stop: dangling holder to_holder 'ghost' at entities[3].provenance[0]
```

Byte-identical wording for a present-but-invalid row and an absent id. Same class for sources
(`x-source-row-schema-invalid`: `first stop: unknown source 's2'` while `sources[1]` carries
`s2` with an empty `title`, and `sources[1].title: required nonempty str` is printed alongside).

### 5. Silence class (FN-3)

`z-invalid-item-row-with-provenance`: the item row is schema-invalid (`first_appearance: ""`)
and carries two provenance records whose first cites an unknown source.

```
after : entities[2].first_appearance: required nonempty str
        (1 violation; no provenance diagnostic, no disclosure, no notice)
control z-valid-item-row-control (same records, valid row):
        entities[2].provenance[0].source_id: unknown in-world source 'missing-source'
        ... [0] and [1]: ... first stop: unknown source 'missing-source' at entities[2].provenance[0]
```

`z-invalid-item-and-ambiguous-holder` (invalid item row + ambiguous holder in record 0) prints
only `entities[4].first_appearance` and `entities[1].id: duplicate entities id 'dup'` — no
`ambiguous entity` line, no disclosure. Baseline output is identical in both (before == after).

## Findings & named debt

**Axis verdict — calibration: improved (bounded).** On the delivered tree the three C1 residuals
are closed on the paths C1 targeted: shape-invalid dict records with ambiguous holders arm the
stop and disclose (`r88-shape-ambiguous-armed`, `r87-probe-shape-ambiguous`); the earlier cause,
not the later ambiguity, is named (`z-nondict-then-ambiguity`, `r88-mixed-stop`); non-holder
causes now disclose (`r88-nonholder-stop`, `x-item-id-duplicated`, `x-provenance-on-nonitem`,
`y-sources-missing`). No axis is harmed: 0 exit changes, 0 stderr changes, every one of the 9
changed tuples is additive-or-replacement disclosure text, and all 47 landed disclosures name a
cause that operated. **No false naming was found anywhere in the landed corpus.** The verdict is
bounded, not clean, because three input classes outside the corpus still defeat the claim; each
is pre-existing (before == after), so none of them is a regression introduced by this round.

**FN-1 (confirmed false naming; bounded, r88-promoted).** `dangling holder …` is named as the
first stop for a holder id that **is present in `entities.json`** but on a schema-invalid row
(the index keeps only fully valid rows). Evidence: `y-true-dangling-vs-invalid-row` (identical
string for a present-but-invalid id and an absent id), `x-holder-row-schema-invalid`,
`x-source-row-schema-invalid` (same for `unknown source`). The named cause "dangling"/"unknown"
does not hold — the row exists. Mitigation: the row's own field violation is printed, so a
reader can reconcile, and the underlying `dangling entity` line is baseline behavior; r88's
change is that this imprecision is now promoted into the named stop cause. Severity: bounded.
Fix direction (not applied): distinguish "absent from entities.json" from "present but
schema-invalid" in the cause text, or suppress the stop when the holder id is present in the raw
file.

**FN-2 (confirmed gap, unmitigated; inverse of false naming — no in-corpus instance).**
`p6-dup-holder-one-row-invalid`: the holder id `dup` occurs **twice** in entities.json but one
row is schema-invalid, so the valid-row count is 1. Delivered output:

```
after : entities[1].first_appearance: required nonempty str
        entities[4].provenance[1]: provenance chain break; expected from_holder 'dup', got 'mira'
```

No `ambiguous entity` line, no stop, no disclosure — and a **definite** continuity finding is
issued about an identity that is not resolvable in the file. This is the exact class C1 set out
to close for ambiguous holder ids; the delivered detection keys on the valid-row index, so the
ambiguity is invisible and the chain is assessed as if the holder were unique. In-corpus reach
checked mechanically over all 18 provenance-bearing fixtures (`raw occurrence ≥ 2` and
`valid-index occurrence == 1` for any referenced holder): **no instance**. Named debt: r89 should
either count raw occurrences for holder resolution or treat "id present more than once, some row
invalid" as an unassessable-identity stop.

**FN-3 (confirmed silence class).** A `provenance`-carrying entity row that fails any required
field check is dropped before the provenance loop, so its entire chain is neither assessed nor
disclosed as unassessed — including when a record's holder is ambiguous (`z-invalid-item-and-ambiguous-holder`).
The C1 claim's enumerated causes do not include this case, so the claim is not literally
violated, but the delivered scope of "every record at/after ANY stop discloses the actual first
cause" is narrower than the wording suggests. Baseline identical. Named debt: emit an
unassessed-chain notice for provenance attached to a schema-invalid row.

**FN-4 (incomplete combined summary; no false naming).** The combined same-record summary exists
only in the shape-invalid branch (`check_bible.py:208-234`) and for multiple holder references
within one record (`:276-281`). For a valid-key record with several causes, only one is named —
`record_stop_cause` is latched by `or`, so the first branch to fire wins: tick beats holder
ambiguity (`p1-invalid-tick-ambiguous`, `p6-dup-holder-invalid-tick`), holder ambiguity beats
unknown source (`p6-dup-holder-unknown-source`, `y-ambiguous-plus-unknown-source-valid-keys`),
and `from_holder` dangling beats `to_holder` ambiguity **even though the ambiguity is detected
first** (`y-two-ambiguous-one-dangling` → `first stop: dangling holder from_holder 'ghost'`).
Every named cause operated, and the unnamed ones keep their own `…: ambiguous entity` /
`unknown in-world source` lines, so nothing is silently lost here. The claim wording
"combined same-record cause summary" should be read as bounded to the shape-invalid case.
(Independently reached by JCAL4 §A3 case A/B.)

**FN-5 (shape-branch silent omissions).** On a key-set-invalid record, `invalid tick` and
`unknown source` produce no violation line at all and are not in the summary
(`p2-shape-ambiguous-invalid-tick`, `p2-shape-ambiguous-unknown-source` — output byte-identical
to `p2-shape-ambiguous`). Pre-existing (the branch `continue`s before field/source validation);
not a false naming, but it caps how complete any same-record summary can be for that class.

**D-1 (documentation drift at the delivered commit).** `corpus/knowledge/holder-assessment-boundary.md`
is unchanged in `2ea9ef1` (`git log --oneline -2 -- corpus/knowledge/holder-assessment-boundary.md`
→ `dfd1fbc`, `28706dc`) and still specifies the r87 two-notice contract verbatim
(`:64`, `:70`, "unassessed at this and all later records …" / "… first occurred at …"), citing
checker lines `:227`, `:238`, `:243`, `:250`, `:189-195`, `:212-224`, `:234-237`, `:238-245`
that no longer exist — the delivered checker emits one form, at `check_bible.py:194`. Its
decision-table row at `:105` also still describes the over-attribution that C1(ii) removed
("the per-record disclosure names the ambiguity as cause even when an earlier invalidity had
already latched the gate"). The doc's own recheck rule ("re-verify whenever the provenance
branch … changes") was not executed in the work commit. CB1's `CB1-boundary-refresh.md`
(PROPOSAL, not applied) and JCAL4/JCAL5 already inventory this; this is my independent
confirmation, and I add that the drift makes the *contract text* — not just examples — wrong.

**D-2 (dead code, no behavioral effect).** `check_bible.py:215-216` is a no-op (see §3(5)); the
record-level `'source table unavailable'` branch at `:291-293` is unreachable, because an
unavailable source table latches the item-level precondition at `:184-185` first (verified by
`y-sources-missing`: the named origin is `entities[2].provenance`, the item label, never a
record).

**Passes with controls (no finding).** Per-item isolation (§3(4)); non-dict-after-stop (§3(3));
null vs missing `from_holder` (§3(5)); dup-id holder on an all-valid record (§3(6));
ambiguity first occurring after a clean record — `y-ambiguity-at-record1` emits **no** disclosure
on record 0 and starts at record 1; item-level causes — `duplicate item id 'seal'` and
`provenance attached to a non-item entity` are named accurately (`x-item-id-duplicated`,
`x-provenance-on-nonitem`); `source table unavailable` vs `unknown source` distinguished
(`y-sources-missing` vs `y-sources-empty`). Negative controls `p1-clean`, `p5-null-fromholder-first`,
`p6-unique-holder` all exit 0 — no spurious disclosures.

## Handoff

- **Deliverables (untracked, under `.ufo/waves/round-88/followup/`):** `JCAL2.md` (this report),
  `JCAL2-receipts.json` — checker SHA-256s, the 145/149 census summary with the 9 changed tuple
  names and exit distribution, the cause-audit totals and named-cause list, and the full
  exit/stdout/stderr receipts for all 42 probe dirs before and after.
- **Scratch (not deliverables):** `/tmp/JCAL2/{gen.py,gen2.py,gen3.py,run.py,audit.py}`,
  `/tmp/JCAL2/probes*`, `/tmp/JCAL2/receipts/`, `/tmp/JCAL2-base-checker.py`.
- **For the L1 / r89 work wave:** (a) FN-2 — decide whether holder resolution counts raw
  occurrences or treats "id present more than once with an invalid row" as an unassessable
  identity; it is the one class where the delivered checker still issues a definite continuity
  finding about an unresolvable identity, and it has no durable fixture. (b) FN-1 — the
  `dangling`/`unknown` cause strings are emitted for ids that exist in the file; consider
  distinct wording. (c) FN-3 — provenance on a schema-invalid row is silently unexamined.
  (d) D-1 — the delivered tree's contract doc contradicts the delivered checker; CB1's proposal
  file is the ready-made refresh.
- **Claims this seat can be cited for:** the 331→352 / 30→30 / 0-exit-change / 9-changed-tuple
  census (independent reproduction of the C1 delta claim); 47 disclosures / 12 fixtures / 0
  cause-audit mismatches on the delivered corpus; the `y-true-dangling-vs-invalid-row` control;
  the `p6-dup-holder-one-row-invalid` gap; the `z-invalid-item-row-with-provenance` silence class.
- **Not done / gaps:** no durable fixture was added for FN-1/FN-2/FN-3 (my write scope is this
  report plus receipts only, and fixture authoring belongs to a fixture seat); FN-2's fix is not
  prototyped. I did not re-verify JCAL1/3/4/5, CB1, or the C2/C3 axes — this seat's evidence is
  C1 calibration only. Verdict stated per axis without scalars; no commit or push was made and no
  tracked file was modified by this seat. `git status --porcelain` at the end of my run showed
  `?? .ufo/waves/round-88/followup/` (untracked, this and sibling seats) and ` M l0-questions.md`
  — the one-line append by the seat authorized for it (K1), not by me.
