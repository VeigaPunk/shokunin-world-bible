# JDEP2 — Depth judge #2 (attack the decisions)

Judged on the DELIVERED tree at `ca7f9ef` (baseline `e97613c`), never on intent or scratch
patches. Scope: the three r90 appendices in
`corpus/knowledge/r88-sourced-inspiration-decision-table.md` — R8 (`:28-38`), R9 (`:40-47`),
R10 (`:49-59`) — attacked with one constructed case each, classified covered/uncovered.

Axes named: (a) decisional coverage of the r89 JDEP2 sub-cases; (b) traceability (owner,
trigger, record, destination); (c) bounded verification (can the decision be receipted without
upgrading it to a mechanical finding); (d) retroactivity/non-regression.

## Work performed

- Pinned the judged tree: `git log --oneline -1` → `ca7f9ef …` with a clean tree apart from the
  follow-up scratch directory. Read the three appendices and their provenance line
  (`:61-63`), the parent rows R8 (`:24`), R9 (`:25`), R10 (`:26`), and the D1/D2 draft patches
  under `.ufo/waves/round-90/patches/`.
- **Freeze-then-verify (r88-I1).** Recomposed X2+X3 on `e97613c` in scratch
  `/tmp/lore-r90-JDEP2.j3q8l6` and compared against the delivered checker: exact hash match —
  no blocking finding (receipts below).
- **Dependency wait-checks.** Two 60 s checks (background runner), observed
  `2026-10-17T06:55:05-03:00 check-1: Q1-r90-debt.json` and
  `2026-10-17T06:56:05-03:00 check-2: Q1-r90-debt.json` — at both checks only `Q1-r90-debt.json`
  existed in `followup/`; no peer depth artifact had landed. Gap noted; work proceeded on the
  delivered tree.
- Built three scratch probes under `/tmp/lore-r90-JDEP2.j3q8l6/` (case text in
  `JDEP2-probes.json`):
  - `probes-r8-denial` — valid fixture plus `inspiration-note.md` recording a dated creator
    denial ("No outside source was consulted … the resemblance … is coincidence") together with
    an editor finding of a distinctive sequence match (seven threshold names and their order).
  - `probes-r9-reprint` — excerpt `reprint-excerpt.md` (`**Delivery mode:** translation`,
    `**Translator:** M. A. Translator`, `**Source text/version:** unidentified; unverified`,
    `**Re-issue record:** 2011 reprint of the 1901 translation`) plus a matching map row.
  - `probes-r10/srcid-a` + `srcid-b` — both clusters carry source id `salt-chronicle` with
    divergent record content (A: municipal registry copy; B: courier's route log).
- Ran the delivered checker and support command; grepped the appendix for the governing terms of
  each attack case; re-verified the live-register absence and the cluster source-id disjointness.
- No tracked write except this report and `JDEP2-probes.json`. No commit or push.

## Before → after measurements

**Freeze-then-verify (X2+X3 composed on `e97613c` = delivered checker).** Commands:

```sh
sha256sum corpus/fixtures/check_bible.py
git show e97613c:corpus/fixtures/check_bible.py > "$scratch"/check.py
cd "$scratch" && mkdir -p corpus/fixtures && cp check.py corpus/fixtures/check_bible.py
patch --fuzz=0 -p1 < .../patches/X2-c1-nullonly.patch && patch --fuzz=0 -p1 < .../patches/X3-c1-tickonly.patch
sha256sum "$scratch"/corpus/fixtures/check_bible.py
diff -q "$scratch"/corpus/fixtures/check_bible.py corpus/fixtures/check_bible.py
```

Observed: delivered `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`;
baseline `e97613c` checker `e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556`;
both patches applied with `--fuzz=0` (X3 hunk succeeded at offset 2 lines); composite
`ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`; `diff -q` silent →
**HASH-MATCH OK. No mismatch; nothing blocking on C1.**

**The appendices are new in this commit and the mechanical layer is blind to them.**

```sh
git show e97613c:corpus/knowledge/r88-sourced-inspiration-decision-table.md | grep -c appendix   # -> 0
git diff e97613c ca7f9ef --stat -- corpus/knowledge/r88-sourced-inspiration-decision-table.md
grep -n "inspiration\|excerpt\|delivery\|translation\|knowledge" corpus/fixtures/check_bible.py   # -> no output, exit 1
```

Observed: baseline appendix count `0`; delivered diff `37 insertions(+)`; checker grep exit `1`
(no output). The appendices are the sole governing text for all three cases.

**Case probe replays** (the checker passes every attack case, so each classification is a
normative reading of the delivered text and the support command):

```sh
python3 corpus/fixtures/check_bible.py /tmp/lore-r90-JDEP2.j3q8l6/probes-r8-denial
python3 corpus/fixtures/check_bible.py /tmp/lore-r90-JDEP2.j3q8l6/probes-r9-reprint
python3 corpus/tools/support_check.py /tmp/lore-r90-JDEP2.j3q8l6/probes-r9-reprint
python3 corpus/fixtures/check_bible.py /tmp/lore-r90-JDEP2.j3q8l6/probes-r10/srcid-a
python3 corpus/fixtures/check_bible.py /tmp/lore-r90-JDEP2.j3q8l6/probes-r10/srcid-b
python3 corpus/fixtures/check_bible.py /tmp/lore-r90-JDEP2.j3q8l6/probes-r10/srcid-a /tmp/…/srcid-b
```

Observed:

```text
R8 probe:      CLEAN: schema, citations, relations, timeline; 0 violations   (exit 0)
R9 probe:      CLEAN: schema, citations, relations, timeline; 0 violations   (exit 0)
R9 support:    PASS T1: source-support; mode=translation; anchor=found; 8:The keeper set the ring upon the fourth stair in slow measure.
               SOURCE-SUPPORT 1/1; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 1/1
               RESULT PASS                                                     (exit 0)
R10 A:         CLEAN … 0 violations (exit 0)      R10 B: CLEAN … 0 violations (exit 0)
R10 two dirs:  usage: check_bible.py [-h] bible / error: unrecognized arguments: …srcid-b  (exit 2)
```

The support command counts a `translation`-mode entry as **source support** regardless of the
`Source text/version: unidentified; unverified` field: `SOURCE-SUPPORT 1/1 … RESULT PASS`.

**Term-silence receipts in the delivered appendices** (each attack case turns on a term that is
absent):

```sh
f=corpus/knowledge/r88-sourced-inspiration-decision-table.md
grep -n -i "source_id\|source id" <(sed -n '28,63p' "$f")   # exit 1
grep -n -i "reprint\|printing\|later edition" <(sed -n '40,48p' "$f")   # exit 1
grep -n -i "remove\|withdraw\|clear" <(sed -n '28,38p' "$f")   # exit 1
grep -rn "possible influence" corpus/   # only 2 hits, both inside the R8 appendix itself (:31, :36)
```

**Retroactivity / non-regression surfaces.**

```sh
test -e corpus/knowledge/cross-cluster-contradictions.md   # REGISTER_ABSENT
# source-id intersection across the two landed clusters:
r87= ['dune-register','gate-witness','lowwater-hymn','shell-charter','tide-bell-tally']
r88m3= ['paired-clock','veil-verse']    shared_source_ids= []
grep -n "external-only\|ETCSL" corpus/fixtures/r87-myth-cluster/inspiration-note.md  # marker at :21 present
python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster    # SOURCE-SUPPORT 22/22; RESULT PASS (exit 0)
python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster # SOURCE-SUPPORT 10/10; RESULT PASS (exit 0)
grep -c "| .translation. |" corpus/fixtures/*/claim-excerpt*.md            # 0 and 0 (exit 1: no translation rows)
```

## Findings & named debt

Per-case classification (one constructed case per appendix):

**1. R8 — influence claim the creator denies, but a distinctive sequence matches → PARTIALLY
COVERED.** Covered half: the two-part gate decides the R2 question against the case — "R2 (no
source used) requires BOTH the creator's no-source account AND the editor finding no contrary
source-specific evidence AND only a commonplace motif" (`:32-34`), so the denial alone cannot
yield R2 while the distinctive match stands. Uncovered half (three edges):
- *Disposition of the failed gate is unspecified.* The only outputs the appendix names are the
  `possible influence: unverified` note (`:30-32`, "records uncertainty, not influence") and the
  `external-only / unverified inspiration` marker reserved for "established general-motif use"
  (`:34-36`); neither fits a denial contradicted by a distinctive-sequence finding, and no
  outcome (element status, label, or review route) is stated.
- *Withhold-scope conflict between delivered texts.* The parent row says "If distinctive
  expression/sequence informed the element … withhold **it** from supported canon" (`:24`,
  element-level); the appendix narrows this to "Withhold only the affected **detail** … the
  element otherwise remains newly authored fiction" (`:36-38`, detail-level). Both are delivered
  text with opposite canon outcomes and no stated precedence.
- *Dispute routing is diluted.* The Owner sentence only says "unresolved disputes go to
  `l0-questions.md`" (`:38`) without defining whether creator-denial-vs-distinctive-evidence is
  such a dispute. Both drafts had explicit language — D1: `patches/D1-decisions.md:13` "If the
  account is unavailable, **disputed**, or identifies distinctive expression/sequence, keep the
  question open in `l0-questions.md` and withhold …"; D2 R8 row: "If the influence question is
  unanswered or materiality unresolved … log the missing evidence in `l0-questions.md`" — and
  neither survived the merge.
- Adjacent merge omission: both drafts required removing the provisional note when R2 applies
  (D1 `:13`, D2 R8 row); the delivered appendix has no remove/withdraw step (grep exit 1), so an
  R2-cleared element can retain `possible influence: unverified`.

**2. R9 — a translation whose "reliable bibliographic tie" is itself a later reprint →
PARTIALLY COVERED (boundary uncovered).** The decided half is the translator-alone rule
("Translator name alone, with the source/version link unverified, FAILS R5 support", `:42-43`);
my case has a record, so it falls under the exception — "a reliable bibliographic record tying
the delivered passage and translator to a named source work permits support ONLY for a claim
about that identified translation — never original wording or an edition-specific variant"
(`:44-47`). Uncovered edges:
- *"Identified translation" vs "edition-specific variant" is undefined for a reprint.* The
  delivered witness is the 2011 reprint's text; a claim about that wording is simultaneously a
  claim about "that identified translation" (permitted) and possibly an "edition-specific
  variant" (barred). The appendix decides neither which identity the record must reach (the 1901
  translation's text, or the reprint edition) nor how a silent reprint revision is treated.
- *"Reliable" has no criterion and printing-identity is not a required field.* No
  reprint/printing term appears (grep exit 1); neither draft's recording step survived — D1
  required recording the limitation, D2 required marking the printing unknown.
- *Mechanical receipt over-counts if reused.* The delivered support command accepts a
  `translation` entry with an unidentified/unverified source-version field as full source
  support (`SOURCE-SUPPORT 1/1 … RESULT PASS`) while the appendix says such a tie "FAILS R5
  support". The appendix is honest that it is an editorial screen (`## Integration boundary`),
  but the tree's only R9 receipt counts the opposite way. Current exposure is zero — the
  delivered maps contain no translation rows (`grep -c` → 0 and 0) and both clusters are
  `verbatim`-only — so the case is prospective.

**3. R10 — a shared `source_id` across clusters → UNCOVERED.** The appendix's trigger is
"Shared names/IDs trigger comparison but do not prove identity (events are not entities;
occasion and field must match)" (`:51-52`); it never scopes the ID namespace, and `source_id`
appears nowhere in the appendices (grep exit 1). A source-record key is neither an event nor an
entity, so the parenthetical does not reach it. Probe result: same `salt-chronicle` id with
divergent record content passes `CLEAN` in each cluster alone (exit 0) and the checker cannot
see across clusters (two-dir invocation, exit 2). Two incompatible readings remain available:
(i) shared source citations are expected and benign, so no comparison record is owed — but then
the trigger text over-triggers on every repeated citation; (ii) any shared ID owes a
compared-overlap record in the incoming README — but the appendix gives no dismissal criterion
and no destination for divergent record *content* (the register is defined for referent/field/
occasion conflicts, `:55-57`). The case is prospective — the landed clusters share no source ids
(`shared_source_ids= []`, re-verified) and the register is correctly absent — but the
prospective boundary for source-id collisions is not governed.

**Named debt.**

- **D-JDEP2r90-1 (R8 failed-gate disposition).** State the outcome when the creator's no-source
  account is contradicted by source-specific evidence: which record, which scope of withhold
  (detail vs element, reconciling `:24` with `:36-38`), and whether `l0-questions.md` is
  mandatory.
- **D-JDEP2r90-2 (R8 note lifecycle).** Add the note-removal step for the R2 branch (present in
  both drafts, absent in the delivered text; grep `remove|withdraw|clear` exit 1).
- **D-JDEP2r90-3 (R9 reprint boundary).** Define "reliable bibliographic record" and whether a
  later-reprint tie can identify the translation for support; require recording the delivered
  printing. Until then the exception's scope is integrator discretion.
- **D-JDEP2r90-4 (R10 namespace).** Scope "Shared names/IDs" to entity/event referents and state
  whether a shared `source_id` requires a comparison record; if yes, name the artifact for
  divergent source-record content.
- **D-JDEP2r90-5 (R9 receipt parity, informational).** `corpus/tools/support_check.py` counts
  translation-mode entries as source support irrespective of the source/version field; if it is
  ever used as an R9 receipt for translation-bearing maps, the numerator will not reflect the
  appendix's FAILS rule.

**Per-axis verdicts (delivered tree `ca7f9ef` only).**

- *Decisional coverage (of the r89 JDEP2 sub-cases):* **improved.** At `e97613c` the appendices
  did not exist (grep count 0) and r89 JDEP2 classified all three sub-cases uncovered; the three
  core questions are now decided in delivered text (R8 trigger + note + two-part gate; R9
  translator-alone FAILS; R10 name≠identity with README/register destinations). Residual edges
  above are named debt, not reversals.
- *Traceability:* **improved.** Owner, record homes (note/map, `Source text/version`,
  `## R10 comparison outcomes`, `l0-questions.md`, register) are stated per appendix; provenance
  of the merged text is recorded (`:61-63`).
- *Bounded verification:* **unchanged.** The appendices are manual screens by design; my R9
  probe shows no mechanical enforcement was added (support command counts unverified-version
  translations as source support), and the Integration boundary disclaims mechanical
  verification. No harm, no overclaim in the appendix text itself.
- *Retroactivity/non-regression:* **unchanged.** Register absent, cluster source-id sets
  disjoint, r87 ETCSL marker intact (`inspiration-note.md:21`), both support receipts green
  (22/22, 10/10), two-dir CLI limit unchanged (exit 2). No retroactive re-marking found in the
  delivered diff on the clusters.
- No axis harmed. No blocking finding: the freeze-then-verify hash match holds.

## Handoff

- **Classifications:** R8 attack case partially covered (R2 gate decided; disposition,
  withhold-scope, and dispute routing ambiguous; note-removal step dropped at merge);
  R9 attack case partially covered (translator-alone rule decided; later-reprint tie boundary
  undefined, reliability criterion absent, receipt counts the opposite way);
  R10 attack case uncovered (source_id namespace not addressed; shared source records with
  divergent content have no governing artifact; prospective — landed ids disjoint).
- **Freeze-then-verify:** PASS — X2+X3 composed on `e97613c` reproduce the delivered
  `corpus/fixtures/check_bible.py` byte-for-byte (`ff9fd2aa…`); no mismatch to report.
- **Dependency gap:** at both 60 s checks (06:55:05, 06:56:05 `-03:00`) only Q1's debt JSON
  existed in `followup/`; no peer seat artifact was available to cross-check.
- **Debt handed forward:** D-JDEP2r90-1 … -5 above; -1/-3/-4 are the substantive governance
  edges, -2 and -5 are merge/receipt parity items.
- **Not done here:** the appendices' worked examples were not re-enacted end-to-end (probes are
  scratch only, contents in `JDEP2-probes.json`); I did not re-audit R1/T1's pasted receipts or
  rule on C1/C2 axes beyond the freeze-verify obligation.
