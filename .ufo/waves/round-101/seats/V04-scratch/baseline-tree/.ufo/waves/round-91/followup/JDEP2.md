# JDEP2 — round-91 follow-up, depth judge #2 (attack the edge decisions)

Judged on the DELIVERED tree at `c2ab3d0` (baseline `a7c6a17`), never on intent or scratch
patches. Scope: the r91 edge decisions in `corpus/knowledge/r88-sourced-inspiration-decision-table.md`
— R8 failed-gate disposition + withhold precedence (`:40-47`), R9 reprint boundary (`:49-91`),
R10 `source_id` namespace (`:105-108`) — attacked with one constructed case each:
R8 gate fails but the detail is inseparable from the element; R9 the item-specific reprint
record is privately held, not publicly auditable; R10 two clusters deliberately share a
`source_id` as a cross-reference convention. Each case classified covered/uncovered.

Axes named: (a) decisional coverage of the r90 JDEP2 residuals; (b) traceability
(owner/trigger/record/example of the delivered decision); (c) bounded verification (can the
edge be receipted without upgrading it to a mechanical finding); (d) retroactivity/non-regression.

## Work performed

- Pinned the judged tree: `git rev-parse HEAD` → `c2ab3d07eaa86ce58f3f9c7fdff702f4b91ea7b7`;
  `git status --porcelain` → only `?? .ufo/waves/round-91/followup/`. Delivered checker
  unchanged at `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`; support
  command `9da149b8e51f5c6c39477f17b8b19d17da3568a1a7c72412079efccff1f330bf`.
- **Dependency wait-checks.** Two 60 s checks (one background call, timestamped):
  check-1 `2026-10-17T08:33:15-03:00` → `followup/` empty; check-2
  `2026-10-17T08:34:15-03:00` → `[H4-census.json H4-lineage.json H4-probes.json JCAL5-delta.json ]`
  (sibling-seat artifacts only; no C3/JDEP2 peer artifact). Gap noted; work proceeded on the
  delivered tree.
- Read the three delivered inserts and their provenance line, the parent rows R8 `:24`,
  R9 `:25`, R10 `:26`, the r90 appendices, the D1/D2 r91 proposals, R1's review, the r90
  `.ufo/waves/round-90/followup/JDEP2.md` + probes, `corpus/tools/README.md`, and
  `corpus/tools/support_check.py` (r91 format contract).
- Built one scratch probe for my R9 case (adapted from the persisted r90 probe, rewritten to
  the r91 support-command format): `/tmp/lore-r91-JDEP2.9x2k/probes-r9-private` (8 files).
  Reused the persisted r90 probes read-only for R8/R10 mechanical receipts. No repo write
  except this report; no commit or push.

## Before → after measurements

**The three r91 inserts exist only after `a7c6a17`.**

```sh
git show a7c6a17:corpus/knowledge/r88-sourced-inspiration-decision-table.md | grep -c "decided r91"   # -> 0
grep -n "decided r91\|clarified r91" corpus/knowledge/r88-sourced-inspiration-decision-table.md       # -> :40, :44, :49, :105
git diff --numstat a7c6a17 c2ab3d0 -- corpus/knowledge/r88-sourced-inspiration-decision-table.md      # -> 56  7
git show c2ab3d0 --numstat -- corpus/knowledge/r88-sourced-inspiration-decision-table.md             # -> 14  0 (R8 insert :40-47, R10 insert :105-108)
```

**Delivered R8 insert (:40-47).** "…if the two-part R2 gate FAILS … the element is NOT proven
influenced — the uncertainty note stays, the `R2` claim is not available, and the affected
detail is withheld pending re-derivation or permitted review; the element otherwise remains
newly authored fiction. Withhold-scope precedence (decided r91): detail-level withholding wins
over element-level when they conflict — withhold only what carries the source dependency."

**Term-silence receipts in the delivered doc** (each attack case turns on a term the delivered
text never uses; `grep -ci <pat> corpus/knowledge/r88-sourced-inspiration-decision-table.md`):

```text
constitutive=0  inseparable=0  remainder=0  "whole element"=0  "nothing remains"=0
private=0  privately=0  inspectable=0  deliberate=0  intentional=0  convention=0  declared=0
```

**R8 case — gate fails, detail inseparable from the element** (e.g. the element *is* the
distinctive seven-name sequence; nothing supportable remains). Mechanical layer blind:
`grep -n "inspiration\|excerpt\|delivery\|translation\|knowledge" corpus/fixtures/check_bible.py`
→ no output (rc=1); `python3 corpus/fixtures/check_bible.py /tmp/lore-r90-JDEP2.j3q8l6/probes-r8-denial`
→ `CLEAN: schema, citations, relations, timeline; 0 violations` (rc=0). Both the r91 author
and its reviewer had written the deciding clause, which the delivered text does not contain:

```sh
grep -n "withhold the whole element" .ufo/waves/round-91/patches/D1-edges.patch   # D1: "Withhold the whole element only when the dependency is inseparable/constitutive or no independently supportable remainder exists." + worked example "no separable supportable remainder, withhold the whole element"
grep -n "whole element only when" .ufo/waves/round-91/R1.md                       # R1.md:284 same clause
# delivered doc: 0 hits for constitutive/inseparable/remainder/whole element (above)
```

**R9 case — item-specific reprint record privately held, not publicly auditable.** Delivered
rule (:63-70): qualifies "only when an auditable, item-specific record identifies the actual
delivered reprint and its edition/year (and a stable identifier or copy locator) … Accept a
title/imprint/copyright page or publisher/authoritative-library catalogue entry; a generic
reprint notice, untraceable secondary entry, translator name, or anchor alone is insufficient."
D1's "inspectable" qualifier was available and dropped (D1 patch: 1 hit; delivered: 0). Probe
replay (attacker-owned scratch; delivered tools):

```sh
python3 corpus/fixtures/check_bible.py /tmp/lore-r91-JDEP2.9x2k/probes-r9-private
# -> CLEAN: schema, citations, relations, timeline; 0 violations   (rc=0)
python3 corpus/tools/support_check.py /tmp/lore-r91-JDEP2.9x2k/probes-r9-private
# -> INVENTORY JSON-FACTS 1/1; EDITORIAL-ROWS 0/0; TOTAL-ROWS 1/1; DISTINCT-ANCHORS 1/1
#    PASS T1: source-support; mode=translation; anchor=found; 8:The keeper set the ring upon the fourth stair in slow measure.
#    SOURCE-SUPPORT 1/1; ... RESULT PASS   (rc=0)
```

The tool reads only path/mode/anchor; the privately held, unverifiable record
(`Delivered copy record: … privately held … no publisher or authoritative-library catalogue
entry; copy locator: private collection, shelf B2.`) is counted as full source support — the
delivered rule's undefined "auditable" is the only gate. Related receipts: the persisted r90
probe no longer parses under the r91-format command —
`support_check.py /tmp/lore-r90-JDEP2.j3q8l6/probes-r9-reprint` → `FAIL: fact table must be
under a JSON facts or Editorial rows heading` (rc=2) — and the delivered doc's own R9
verification command (`:90`) validates the wave patch artifact, not the delivered text:
replayed verbatim → `R9 reprint decision completeness: 11/11` (rc=0).

**R10 case — two clusters deliberately share a `source_id` as a cross-reference convention.**
Delivered rule (:105-108): "`source_id` values are cluster-local identifiers. A `source_id`
shared across clusters is a NAMESPACE COLLISION, not identity evidence … a bare shared id
triggers the namespace check (rename or qualify one side) before any referent comparison. A
collision alone never enters the register." Receipts: `deliberate/intentional/convention` = 0
hits; register absent (`REGISTER_ABSENT`); landed-cluster ids disjoint re-verified
(`r87 ids: [dune-register, gate-witness, lowwater-hymn, shell-charter, tide-bell-tally]`;
`r88-m3 ids: [paired-clock, veil-verse]`; `shared ids: []`); cross-cluster view absent
(`check_bible.py <A> <B>` → usage error, rc=2; each probe `CLEAN`, rc=0).

**Retroactivity receipts (delivered command on landed clusters).**

```sh
python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster    # -> JSON-FACTS 14/14; EDITORIAL-ROWS 8/8; ... RESULT PASS (rc=0)
python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster # -> JSON-FACTS 10/10; WARN: unreferenced excerpt declaration: source-excerpt.md; RESULT PASS WITH WARNINGS (rc=0)
```

## Findings & named debt

Per-case classification (one constructed case per r91 edge):

**1. R8 — gate fails but the detail is inseparable from the element → UNCOVERED.** The
delivered insert decides the common disposition (note stays, `R2` unavailable, detail withheld)
and states a precedence, but for an inseparable/constitutive dependency the delivered text
leaves two contradictory readings: "detail-level withholding wins over element-level when they
conflict — withhold only what carries the source dependency" versus the retained "the element
otherwise remains newly authored fiction". When the detail *is* the element, one reading keeps
a fiction with no supportable remainder (recording unspecified), the other withholds the whole
element (status/record unspecified) — and the delivered text says neither. The clause that
decided this exact case, present in both D1's proposal and R1's review recommendation, did not
survive integration (0 term hits), and the delivered insert carries no worked example or
routing clause for R8 (D1's "dispute for `l0-questions.md`" wording was also dropped).
**Debt D-JDEP2r91-1:** reinstate the "inseparable/constitutive or no independently supportable
remainder → withhold the whole element" branch, state the element-status recording (note/map),
and state whether a failed gate routes to `l0-questions.md`.

**2. R9 — item-specific reprint record privately held, not publicly auditable → UNCOVERED
(ambiguous).** "Auditable" is never defined; private vs public custody is never mentioned;
"stable identifier or copy locator" is undefined for a private collection; D1's "inspectable"
qualifier was dropped; the Owner sentence requires the lore integration owner to verify
bibliographic identity but gives no method for a record only the submitter can produce. The
mechanical layer cannot compensate (probe: a privately held, unverified translation returns
`SOURCE-SUPPORT 1/1; RESULT PASS`). Two materially different readings remain — private copy
qualifies (it is a title page and has a locator) or fails (not publicly traceable; "untraceable
secondary entry" insufficient) — and the rule never chooses.
**Debt D-JDEP2r91-2:** define "auditable"/inspectability and state whether privately held
item-specific records qualify, on what evidence (submitted copy/scan, custodian declaration,
verification route), and who must be able to inspect the exact copy.

**3. R10 — deliberate shared `source_id` as a cross-reference convention → UNCOVERED
(mis-governs).** The rule's predicate is the bare fact of sharing; intent has no representation
(0 hits for deliberate/intentional/convention). A declared, documented convention is
relabeled a "namespace collision" and its mandated fix ("rename or qualify one side") deletes
the convention as such, with no owner, no recording obligation, and no destination (the
register excludes collisions; README `## R10 comparison outcomes` covers dismissed overlaps,
not sanctioned conventions). The decision governs accidental reuse but provides no channel
for a genuine intentional cross-reference.
**Debt D-JDEP2r91-3:** state whether deliberate shared ids are forbidden outright (with a
migration/recording requirement) or provide a declared-convention channel naming where the
intent and the sanctioned cross-reference are recorded.

**Secondary named items.** **D-JDEP2r91-4:** the delivered R9 insert embeds a verification
command that reads `.ufo/waves/round-91/patches/D2-edges.patch`, not the delivered text — a
text-completeness receipt that cannot detect delivered-doc drift (evidence: replayed command
→ 11/11). **D-JDEP2r91-5** (inherited, still live under the new command): translation-mode
entries count as source support regardless of the source/version or record fields (adapted
probe receipt); parity with D2's named R9 receipt debt remains for the delivering lane.

**Per-axis verdicts (delivered tree `c2ab3d0` vs baseline `a7c6a17`).**

- *Decisional coverage of the r90 JDEP2 residuals:* **improved**, bounded — all three r90
  residuals now have decided delivered text (R8 disposition + precedence; R9 reprint threshold;
  R10 namespace), and each of my three attack sub-cases above remains uncovered.
- *Traceability:* **improved** — the R9 insert carries Owner/Trigger/Worked example/Verification
  command; R8/R10 inserts inherit the r90 Owner lines and the provenance line (`:110-112`)
  names the merged seats. Gaps: no worked-example/trigger fields for the R8/R10 inserts; R8's
  routing clause dropped; R9's command targets a patch artifact (D-JDEP2r91-4).
- *Bounded verification:* **unchanged** — all three edges remain editorial screens; the
  checker reads none of the governed surfaces (rc=1 grep), and the support command counts the
  R9 negative case green.
- *Retroactivity/non-regression:* **unchanged** — register absent; landed clusters' ids
  disjoint; no retro edits (provenance `:110-112`); both landed clusters pass the delivered
  support command (r87 14/14 `RESULT PASS`; r88-m3 10/10 `RESULT PASS WITH WARNINGS`).
- No axis harmed; no blocking finding. The three uncovered sub-cases are named debt, not
  reversals of the r91 coverage improvement.

## Handoff

- Written: `.ufo/waves/round-91/followup/JDEP2.md` (this report; the only repo write).
  Scratch: `/tmp/lore-r91-JDEP2.9x2k/probes-r9-private` (8 files; replayable evidence for the
  R9 case, r91 support-command format); r90 probes reused read-only; `/tmp` inode check at
  last use: `15484` free (`df -i /tmp | tail -1` → `tmpfs 1048576 1033092 15484 99% /tmp`).
  No commit or push.
- Classifications: **R8 inseparable → uncovered** (deciding clause existed in D1 + R1, dropped
  by the `c2ab3d0` integration); **R9 private record → uncovered/ambiguous** ("auditable"
  undefined; private custody unaddressed; support command blind); **R10 deliberate convention
  → uncovered/mis-governs** (no intent category, no record/channel; mandatory rename/qualify
  deletes the convention).
- Debt handed forward: D-JDEP2r91-1…-3 (substantive governance edges), D-JDEP2r91-4/-5
  (traceability/parity).
- Not done here: the boundary-doc reconstruction and C1/C2 surfaces are other seats' lanes;
  the r91 C1 fixtures were not replayed (out of this seat's scope; checker identity only was
  pinned, `ff9fd2aa…`). Dependency gap recorded above (no C3/JDEP2 peer artifact at either
  60 s check).