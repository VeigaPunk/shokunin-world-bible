# JDEP2 — Depth judge #2 (attack R8–R10)

Judged on the DELIVERED tree at `1b09f3f` (baseline `51b286b`), never on intent or scratch
patches. Scope: the three new governance rows in
`corpus/knowledge/r88-sourced-inspiration-decision-table.md:22-24` (R8 rights-blocked element
disposition, R9 excerpt delivery-mode, R10 cross-cluster contradiction procedure) plus their
required artifacts (element marker, claim-to-excerpt map, cross-cluster register).
Method: read-only `git`/`grep`/`python3` on the delivered tree; three scratch probes under
`/tmp/jdep2/probes/`, one per row. No tracked write except this report and
`JDEP2-probes.json`. No commit, no push.

Axes named: (a) governance completeness — does each row decide the case it was written for;
(b) traceability — is each row's required artifact defined, unique, and exercised; (c) bounded
verification — can the row's question be answered without editing canon.

## Work performed

- Confirmed the tree under judgement and located the governing text (rows at `:22`, `:23`,
  `:24`; integration notes at `:31-37`).
- Established that no mechanical layer governs these questions: `grep -n
  'excerpt\|inspiration\|delivery\|paraphrase\|translation\|knowledge\|cross-cluster' corpus/fixtures/check_bible.py`
  returns nothing (exit 1). The checker reads only the five JSON sections; the table, notes,
  excerpts, maps and register are unread. The rows are therefore the sole governing text and
  each probe below must be decided by reading, not by replay.
- Built one scratch probe per row and replayed it (all `CLEAN`, exit 0) — the probe's purpose
  is to show the row's question is live *while the checker is silent*, not to change canon.
- Censused the delivered tree for each row's required artifact (marker strings, delivery-mode
  declarations, register).
- Compared the delivered rows against the D1 and D2 drafts to record which draft governs and
  what was dropped.
- Ran the mandated dependency checks: three timestamped 60 s polls of
  `.ufo/waves/round-89/followup/` (04:17:29 / 04:18:29 / 04:19:29, log
  `/tmp/jdep2/waitchecks.log`). At the deadline only `JCOV3.md`, `JCOV3-probes.json` and
  `JCOV4.md` (coverage seats) were present — no peer depth seat (JDEP1/JDEP3) artifact. Gap
  noted; work proceeded on the delivered tree, which was already committed.

## Before → after measurements

**Tree identity.** Command: `git log --oneline -1 && git status --porcelain`

```text
1b09f3f lore r89: C1 cause-branch fixtures + multi-cause summary + FN-1/2, C2 r87 support completion, C3 R8-R10 governance — work wave (32 luna-max seats)
?? .ufo/waves/round-89/followup/
```

The only working-tree entry is this follow-up wave's own scratch dir; the corpus is clean at
`1b09f3f`.

**No mechanical coverage of the rows.** Command:
`grep -n "excerpt\|inspiration\|delivery\|paraphrase\|translation\|knowledge\|cross-cluster" corpus/fixtures/check_bible.py`
→ no output, `exit=1`. The governance rows cannot be replayed; every classification below is a
normative reading of the delivered text plus a probe that the checker passes.

**Probe replays (all three cases pass the checker → the rows carry the whole burden).**

```sh
for d in r8-motif-unrecorded r9-translation-unknown-version r10-cluster-a r10-cluster-b; do
  python3 corpus/fixtures/check_bible.py /tmp/jdep2/probes/$d; echo "exit=$?"; done
```

```text
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
```

**R10 two-directory limit reproduced** (the manual-gate premise). Command:
`python3 corpus/fixtures/check_bible.py /tmp/jdep2/probes/r10-cluster-a /tmp/jdep2/probes/r10-cluster-b`

```text
usage: check_bible.py [-h] bible
check_bible.py: error: unrecognized arguments: /tmp/jdep2/probes/r10-cluster-b
exit=2
```

**Anchors.** `grep -nF -- 'the ring upon the fourth stair' /tmp/jdep2/probes/r9-translation-unknown-version/river-codex-excerpt.md`
→ `11:The keeper set the ring upon the fourth stair.` (exit 0).
`grep -nF -- 'moved to the west stair' corpus/fixtures/r89-inspiration-paraphrase/ash-ledger-excerpt.md`
→ `9:A modern paraphrase says that the keeper later summarized the ledger for the court: the tide-mark had been moved to the west stair.`
(exit 0) — the delivered R9 demo fixture's map line reference (`ash-ledger-excerpt.md:9`) is
accurate.

**Required-artifact census in the delivered tree.**

Command: `grep -rhoE 'external-only / [a-z ]+' corpus/ | sort | uniq -c`

```text
      1 external-only / text not delivered at lore
      1 external-only / unverified
      1 external-only / unverified inspiration
```

Three different `external-only / …` strings, one occurrence each. R8's element marker
`external-only / unverified inspiration` occurs **only in the R8 row itself**
(`grep -rnF 'external-only / unverified inspiration' corpus/` → single hit at
`corpus/knowledge/r88-sourced-inspiration-decision-table.md:22`); R4 (`:15`) requires
`external-only / unverified`; the landed ETCSL ledger row uses `external-only / text not
delivered at lore` (`corpus/knowledge/reference-ledger.md:8`).

Command: `grep -ro 'external-only' corpus/fixtures/r87-myth-cluster/ | wc -l` → `0`.

Command: `grep -rn '\*\*Delivery mode:\*\*' corpus/` → one hit only,
`corpus/fixtures/r89-inspiration-paraphrase/ash-ledger-excerpt.md:3`. `verbatim`, `translation`
and `summary` modes are declared nowhere in the delivered tree.

Command: `python3 -c 'from pathlib import Path; print("live_register_present=", Path("corpus/knowledge/cross-cluster-contradictions.md").exists()); print("demo_present=", Path("corpus/knowledge/r89-cross-cluster-contradiction.md").exists())'`

```text
live_register_present= False
demo_present= True
```

**Which draft governs.** Row-level comparison of the delivered rows against
`.ufo/waves/round-89/patches/D2-rows.md` and `D1-rows.md`: after removing the inserted Owner
sentence, delivered R8/R9/R10 are D2's text (sequence ratio `0.9998` / `0.9998` / `0.9997`),
with `ratio_D1` `0.1398` / `0.1067` / `0.0791`. `similar names` occurs once in `D1-rows.md`
and **zero times in the delivered table** — D1's explicit name-identity guard was not carried
into the delivered R10.

## Findings & named debt

### Case 1 — R8, a general motif with a plausible-but-unrecorded influence claim → **uncovered**

Probe `/tmp/jdep2/probes/r8-motif-unrecorded`: two elements (`low-water-crossing`, a general
motif; `seven-stair-descent`, a distinctive seven-threshold sequence parallel to ETCSL 1.4.1
lines 122–163) with **no** inspiration note, symbolism map or ledger row. Replay `CLEAN`, exit 0.

Row text applied (`:22`): the R1-vs-R2 decision is made "from recorded provenance, not
resemblance alone"; the materiality screen is performed with "a contemporaneous, non-expressive
provenance note"; the dispositions are (i) "No source was consulted and no specific real-world
lineage is asserted: R2 may apply", (ii) "A recorded source-use or unresolved influence question
is not R2; keep it open", (iii) "If only a general motif **is recorded** … mark the affected
element in the note/map `external-only / unverified inspiration`", (iv) "If distinctive
expression/sequence informed the element, or the screen is unresolved, withhold it".

Every disposition presupposes recorded material. With nothing recorded: (i) is technically
available but R2's own text (`:13`) warns "This row does not excuse omitting a source that
actually informed the work"; (ii)/(iv) need a recorded use or a *performed* screen; (iii) needs
a recorded motif **and** a note/map to carry the marker. So a strict reader defaults to R2
(keeping a source-shaped element in canon as original), while a loose reader treats the
resemblance as an unresolved screen and withholds it — two opposite canon outcomes from the same
facts. The gap is *detection and trigger*, not destination: the row's Owner clause ("unresolved
disputes are appended to `l0-questions.md`") gives a destination, but no procedure says who
raises the unrecorded-influence question or on what evidence, and the required marker has no home
when no note/map exists.

Landed instance, not hypothetical: `corpus/fixtures/r87-myth-cluster/inspiration-note.md:5`
records the ETCSL motif — precisely R8's general-motif branch — and that fixture contains **0**
occurrences of `external-only`. The r89 integration notes (`:31-37`) scope R8's prospectivity
only against the Spence row ("R8 does not retroactively affect the landed Spence row (its text is
delivered)"); the r87 ETCSL element marker is not addressed, so the delivered tree contains an
R8-shaped case with no marker and no named disposition.

### Case 2 — R9, a translation excerpt whose translator is named but version unknown → **uncovered**

Probe `/tmp/jdep2/probes/r9-translation-unknown-version`: excerpt declares
`**Delivery mode:** translation`, `**Translator:** M. A. Translator`,
`**Source version:** not recorded`; the map declares mode + translator and the anchor
`the ring upon the fourth stair` matches at line 11. Replay `CLEAN`, exit 0.

Row text applied (`:23`): the declaration clause says "identify the translator/version for a
translation … **when known**" — the probe is compliant (the version is unknown, so nothing is
missing from the declaration). The eligibility clause is unconditional: "Only delivered source
words, or **an identified translation tied to a named source text/version**, may carry R5
source-claim support" — the probe is *not* eligible, because no source text/version is named. The
two clauses pull opposite ways and the row resolves neither: it prescribes a disposition only for
the paraphrase/summary branch ("label the underlying source text `not delivered / unverified`"),
which is the wrong label here (the delivered text exists; its version does not). No marker, no
open-question record, and no statement whether the `translation` label may stand. Because the
mode set is closed at four values, the compliant-looking label conceals the eligibility defect,
and the row's own warning — "A fixed-string anchor … does not establish delivery mode or
fidelity" — has nothing to attach to.

### Case 3 — R10, two clusters sharing a referent name but different occasions → **uncovered (partial)**

Probe `/tmp/jdep2/probes/r10-cluster-a` + `r10-cluster-b`: both carry a timeline event with id
`moon-basin-vow`; A is tick 3 / `mother-tide-gate` / "Saltmonth 4", B is tick 7 / `reed-arch` /
"Saltmonth 9". Each replays `CLEAN`, exit 0; together the checker rejects two directories
(exit 2); `cross-cluster-contradictions.md` does not exist.

Answer to the posed question, and why it does not settle: the durable entry is required only
"For each supported **incompatible** pair" (`:24`) — these two accounts are compatible once the
occasions differ, so no register entry. That part is **covered**. But the row's other branch fires
only "If identity or occasion is **unestablished**". Here identity rests entirely on a shared
referent *name* and the occasion is established as *different* — neither trigger applies cleanly.
Reading (i), different occasion establishes distinct referents: nothing is required, and the
overlap is dismissed with no record, so the manual gate leaves no audit trail. Reading (ii), the
name overlap leaves identity unestablished (the row states no identity test, and the guard D1
drafted — "similar names or wording alone do not establish identity" — is absent from the
delivered row): a "candidate discrepancy and missing evidence" is required, but the row names no
destination for it (the register is defined only for confirmed pairs). Two readings, two
different required artifacts, and the near-miss is exactly the false-positive the row's
"confirm a shared referent" step exists to prevent.

### Named debt (for the round record)

- **D-JDEP2-1 (R8 detection gap).** R8 decides only cases with recorded material. Add a trigger
  for an unrecorded-but-plausible influence (who raises it, on what evidence, to which record)
  and state the disposition when no note/map exists to carry the element marker.
- **D-JDEP2-2 (marker-string proliferation).** Three `external-only / …` variants coexist
  (element `… / unverified inspiration`, passage `… / unverified`, ledger `… / text not
  delivered at lore`). Which string is authoritative per surface is unstated; R8 requires one
  string for the element and free prose for the ledger cell.
- **D-JDEP2-3 (R8 unexercised; landed r87 case unmarked).** No R8 demo fixture exists (only R9
  got one), the R8 marker occurs 0 times outside the row, and the landed r87 ETCSL motif carries
  no element marker with no named disposition in the integration notes.
- **D-JDEP2-4 (R9 single mode exercised; unknown-version gap).** Only `paraphrase` is declared
  anywhere in the tree; `verbatim`, `translation`, `summary` have no worked example. Add the
  disposition (label and record) for a translation whose source text/version is unidentified.
- **D-JDEP2-5 (R10 record and identity test).** State whether an overlap that is compared and
  dismissed must be recorded, and where; restore or replace D1's name-identity guard; name the
  destination for a candidate discrepancy.
- **D-JDEP2-6 (provenance of the rows).** The delivered rows are D2's drafts plus an Owner
  sentence; D1's independent draft was not used and its name-identity guard was dropped. Worth
  recording so the round's row-set provenance is auditable.

## Handoff

- **Per-case classification: R8 uncovered; R9 uncovered; R10 uncovered (partial — the
  no-register-entry answer is covered, the required record is not).** All three cases pass the
  checker (`CLEAN`, exit 0), so the gap is purely in the governing text, not in a broken fixture.
- **Depth-axis relevance (C3).** C3's declared deliverable — three rows governing JDEP3's
  uncovered classes, plus an R9 demo fixture and an R10 worked example — is present and
  verifiable in the delivered tree, and the R9 demo replays `CLEAN` with an accurate map line
  reference. What C3 did not deliver is closure of the classes it claims to govern: each row
  leaves one sub-case that its own text cannot decide. I do not rule the depth axis here; this
  seat's contribution is the three case classifications and debt items above.
- **Limits.** The probes are scratch (`/tmp/jdep2/probes/`, contents embedded in
  `JDEP2-probes.json`) and were not landed, per the write-scope rule; the classifications are
  normative readings of the delivered row text, not mechanical results, because no layer reads
  the rows. No peer depth seat (JDEP1/JDEP3) artifact existed at the 04:19:29 deadline — only
  `JCOV3`/`JCOV4` (coverage) — so no independent depth judgement was available to cross-check
  against. `JDEP1.md`, `JDEP4.md` and other peer artifacts appeared at 04:20, after this seat's
  deadline; they were not read before this report was written. `JDEP1` covers the same three
  rows from the verification side (replaying the commands the rows cite, row shape and GFM
  rendering) rather than by constructed counter-cases, so the two judgements are complementary
  and do not overlap in method.
- **Files written (tracked, repo-local):** `.ufo/waves/round-89/followup/JDEP2.md` (this
  report) and `.ufo/waves/round-89/followup/JDEP2-probes.json` (probe fixtures, replay receipts,
  classifications, debt ids). No other tracked write, no commit, no push.
