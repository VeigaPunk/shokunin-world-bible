# JDEP4 — round-92 follow-up, depth judge (attack the edge decisions)

Judged on the DELIVERED tree at `c4d4823` (baseline `396c568`), never on intent or scratch
patches. Scope: the r92 edge decisions in `corpus/knowledge/r88-sourced-inspiration-decision-table.md`
— R8 failed-gate disposition clarified r92 (`:40`) and the R9 manual gate / required record /
receipt boundary (`:42-48`) — attacked with one constructed case each (R8: the reviewer IS the
submitter's collaborator; R9: the privately-held scan is complete but the reviewer cannot access
the copy locator afterwards), plus the R10 namespace edge (`:106-109`; a deliberate shared
`source_id` used as a documented cross-cluster alias). Each case classified covered/mis-governs.

Axes named: (a) decisional coverage of the r91 JDEP2 residual edges; (b) traceability of the
delivered decision (owner/trigger/record/reviewer identity); (c) bounded verification (receipted
without upgrading an editorial screen to a mechanical finding); (d) retroactivity/non-regression.

## Work performed

- Pinned the judged tree: `git rev-parse HEAD` → `c4d4823b9a8165a88e8199af136e62d6e961b6b9`;
  `git status --porcelain` → tracked tree clean, only sibling follow-up artifacts untracked.
  Checker hash `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` and support
  command hash `55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c` (both at HEAD).
- **Two 60 s wait-checks** (one background call, timestamps + directory listings):
  check-1 `2026-10-17T10:26:23-03:00` → `[H4-census.json H4-probes.json JCAL1-delta.json
  SF1-freeze.json SF1.md SF2.md]`; check-2 `2026-10-17T10:27:23-03:00` → adds `H4-lineage.json
  H4.md JCAL3-evidence.json JCAL3.md JCAL5-delta.json`. Sibling-seat artifacts only; no JDEP
  peer artifact. Gap noted; this seat's attack targets the committed tree, so no peer content
  was required.
- Read at HEAD: the decision table (`:40`, `:42-48`, `:94-109`, whole file), the r92 diff
  `396c568..c4d4823`, the E1/E2 proposal patches and their reports, the boundary doc
  (`holder-assessment-boundary.md`; contains no R8/R9/R10 governance text — its only
  `reviewer` hits are r85 history at `:228-230` and `:598`), `corpus/tools/support_check.py`,
  `corpus/fixtures/check_bible.py`, the r89 register demo, and the r92 work-wave reports
  (`T1.md`, `CB.md`, `E2.md`).
- Scratch: fresh copy of the surviving r91 JDEP2 private-holding probe at
  `/tmp/lore-r92-JDEP4.r9/case-a-lapsed-access`, extended with the R9 lapsed-access `PASS`
  record; the r91 probe dir was also replayed read-only. `/tmp` inode free 15,408 → 15,398
  (one 10-inode copy; file-frugal).
- Repo writes: this report and `JDEP4-evidence.json` only. No commit, push, or other tracked write.

## Before → after measurements

**The r92 write is one hunk; R10 was not re-decided.** Exact commands:

```sh
git diff 396c568 c4d4823 -- corpus/knowledge/r88-sourced-inspiration-decision-table.md | grep -n "^@@"     # -> 1 hunk: @@ -37,14 +37,15 @@ (R8 paragraph + R9 block region)
git diff 396c568 c4d4823 -- corpus/knowledge/r88-sourced-inspiration-decision-table.md | grep -n "Namespace\|source_id"; echo rc=$?   # -> rc=1 (no R10 text in the diff)
```

**R8 headline defect — the committed label is doubled.** The application duplicated the new
bold label while replacing the old paragraph:

```sh
git show HEAD:corpus/knowledge/r88-sourced-inspiration-decision-table.md | sed -n '40p' | cut -c1-120
# -> **Failed-gate disposition (clarified r92):** **Failed-gate disposition (clarified r92):** **Owner:** the lore integratio
git show HEAD:<table> | sed -n '40p' | grep -o "Failed-gate disposition (clarified r92)" | wc -l   # -> 2
grep -o "Failed-gate disposition (clarified r92)" .ufo/waves/round-92/patches/E1-edges.md | wc -l  # -> 1
grep -o "Failed-gate disposition (clarified r92)" .ufo/waves/round-92/patches/E2-wording.md | wc -l # -> 1
```

The certification could not catch it: T1's r8 check is a substring-presence test
(`T1.md:255`: `'inseparable' in r8 and 'whole element' in r8`; same at `CB.md:202`).

**R8 case — the reviewer IS the submitter's collaborator.** Delivered text (`:40`): "… the
creator supplies the provenance account; **a named reviewer** assesses and records the contrary
source-specific evidence and whether an independently authored, independently supportable
remainder exists." Record fields: "Record the failed condition, contrary evidence, separability
rationale, scope, and next action in the note/map." Receipts:

```sh
git show HEAD:<table> | sed -n '40p' | grep -oi "named reviewer\|not the submitter\|collaborator\|independent reviewer" | sort | uniq -c
# ->       1 named reviewer        (no exclusion term of any kind)
git show HEAD:<table> | grep -n "not the submitter\|second reviewer"
# -> :42 only — the R9 block ("a named lore integration reviewer who is not the submitter … If the integration owner is also the submitter, a second reviewer must be named")
grep -rn "not the submitter\|independent reviewer\|collaborator" corpus/ l0-questions.md PROVINCE.md | grep -v r88-sourced-inspiration-decision-table
# -> corpus/fixtures/README.md:833 (historical r7 ledger sentence) — no global reviewer-independence rule covers R8
grep -cin "R9 manual\|reviewer\|submitter" corpus/fixtures/check_bible.py corpus/tools/support_check.py
# -> check_bible.py:0 ; support_check.py:0
```

Case outcome: a creator plus a declared collaborator satisfies every R8 requirement (editor
records, creator supplies, collaborator "names" itself reviewer and authors the separability
finding). The separability finding is exactly the Trigger for the whole-element hold, so the
failed-gate disposition can be steered — hold imposed or avoided — by the submitter's own
circle, and the record list has no reviewer-identity/date/independence field, so the capture is
invisible. The wave's own independent check verified R9's independence only (`E2.md:178`/`:225`:
`'R9 independent reviewer and trigger'` = `('not the submitter', '@ Trigger …')` → PASS); the
origin wording is E1's proposal (`E1.md:170`: "a named reviewer records contrary evidence and
the separability finding").

**R9 case — the privately-held scan is complete, but the reviewer cannot access the copy
locator afterwards.** Delivered gate (`:42`): "… a privately held item qualifies only if the
reviewer can inspect the exact copy or a complete, legible scan with its copy locator; a
submitter-only assertion is insufficient. If identity, passage, or reviewer access is not
established, record `FAIL` (or `OPEN` before review) and do not grant R5 support." The gate
tests access at review time only; nothing bounds the PASS afterwards:

```sh
git show HEAD:<table> | sed -n '42,48p' | grep -in "archive\|re-inspect\|expire\|re-verif\|valid only while\|remains inspectable\|retained\|downgrade\|withdraw\|afterwards"; echo rc=$?
# -> rc=1 (no retention, re-access, expiry, or downgrade term anywhere in the R9 block)
```

The Required record (`:44`) lists claim pointer, excerpt path/span, printing/edition/year,
identifier or copy locator, translator, source work/version, "evidence citation and inspection
method", reviewer name/role/date, disposition, scope — no retained-evidence location, no
re-verification trigger; and "Only a recorded manual `PASS` can clear this gate."

Scratch instantiation (attacker-owned; delivered tools). The map carries an explicit
`R9 manual review — PASS` entry that records the post-review access loss ("after the review the
reviewer cannot access the copy or its copy locator; the scan was not retained; no later party
can re-inspect the evidence"):

```sh
python3 corpus/tools/support_check.py /tmp/lore-r92-JDEP4.r9/case-a-lapsed-access
# -> INVENTORY JSON-FACTS 1/1; … SOURCE-SUPPORT 1/1; … RESULT PASS   (rc=0)
python3 corpus/fixtures/check_bible.py /tmp/lore-r92-JDEP4.r9/case-a-lapsed-access
# -> CLEAN: schema, citations, relations, timeline; 0 violations   (rc=0)
python3 corpus/tools/support_check.py /tmp/lore-r91-JDEP2.9x2k/probes-r9-private
# -> … SOURCE-SUPPORT 1/1; … RESULT PASS   (rc=0) — the r91 private-custody probe is still green under the r92 command
```

Case outcome: the PASS is granted and persists although no party (including the reviewer) can
re-inspect the evidence afterwards; "identity, passage, reviewer access established" decays to a
one-time signature, and the rule cannot distinguish an auditable PASS from an ephemeral one
("auditable" also remains undefined in the r91 appendix `:66`, unreconciled with the new
reviewer-access path).

**R10 case — a deliberate shared `source_id` as a documented cross-cluster alias.** Delivered
text (`:106-109`): "`source_id` values are cluster-local identifiers. A `source_id` shared
across clusters is a NAMESPACE COLLISION, not identity evidence … a bare shared id triggers the
namespace check (rename or qualify one side) before any referent comparison. A collision alone
never enters the register." Receipts:

```sh
git show HEAD:<table> | sed -n '94,109p' | grep -in "deliberate\|intentional\|convention\|alias\|sanctioned\|declared"; echo rc=$?   # -> rc=1
git show HEAD:<table> | grep -in "deliberate\|intentional\|convention\|alias\|sanctioned\|declared"
# -> :48 only ("declared mode", the R9 worked example) — R10 blocks carry no intent term
grep -rln "R10 comparison outcomes" corpus/          # -> the decision table only; no landed README contains the section
ls corpus/knowledge/ | grep -i cross                 # -> r89-cross-cluster-contradiction.md (worked example; the named live register cross-cluster-contradictions.md is absent)
python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-myth-cluster corpus/fixtures/r88-m3-maya-cluster
# -> usage: check_bible.py [-h] bible ; error: unrecognized arguments … (rc=2); grep -c "cluster" check_bible.py -> 0
```

Case outcome: the documented alias is relabeled a collision; the mandated fix ("rename or
qualify one side") deletes the convention; leaving it untouched gives the alias no record and
re-flags it at every integration; the README section covers dismissed overlaps and the register
excludes collisions, so a sanctioned alias has no destination. This is the r91 JDEP2
D-JDEP2r91-3 case, still uncovered at `c4d4823` (carried debt; the r92 diff does not touch R10).

## Findings & named debt

Per-case classification (one constructed case per edge):

**1. R8 — reviewer is the submitter's collaborator → MIS-GOVERNS (new at r92).** The r92 branch
decides the inseparable-dependency disposition but delegates the separability finding to "a
named reviewer" with no independence requirement, while the R9 block in the same wave mandates
"not the submitter" plus a second reviewer when the integration owner is the submitter. A
collaborator satisfies R8 as written; the record list has no reviewer-identity/independence
field. No global rule compensates, no tool reads the surface, and the wave's independent check
covered R9's independence only.
**Debt D-JDEP4r92-1:** extend R8's reviewer clause with the same independence standard (not the
submitter/creator; not a declared collaborator; second reviewer when the editor sits in the
submitter's circle) and add reviewer name/role, date, and independence basis to the note/map
record fields.

**2. R8 delivered-text hygiene → application defect in the committed insert.** The bold label
occurs twice at `:40` (HEAD count 2; E1 and E2 patches 1 each); certification checks presence,
not duplication.
**Debt D-JDEP4r92-2:** drop the duplicated label; add a duplication/adjacent-label check to the
application procedure if one is to be re-run at r93.

**3. R9 — complete private scan, copy locator inaccessible afterwards → MIS-GOVERNS (new at
r92; the sustainment edge).** The gate validates reviewer access as a single past event; the
record has no retained-evidence field, no expiry, no re-access requirement, and a collision-free
`PASS` cannot be downgraded when access lapses. The scratch case (access loss recorded on the
map) still returns `RESULT PASS` / `CLEAN`, so nothing in the delivered tree registers the decay.
**Debt D-JDEP4r92-3:** add a sustainment clause — a `PASS` holds only while the inspected copy,
scan, or locator remains inspectable; record the retained inspection copy or its durable
locator; if access lapses, downgrade the entry to `OPEN` and withdraw R5 support until
re-inspection.

**4. R10 — deliberate, documented cross-cluster alias → MIS-GOVERNS (carried; unchanged at
r92).** Intent has no representation; the only prescribed treatment is rename/qualify, which
destroys the documented convention; no recording destination exists (register excludes
collisions; `## R10 comparison outcomes` is for dismissed overlaps and is landed nowhere).
**Debt D-JDEP4r92-4:** decide aliases explicitly — either forbid deliberate shared ids with a
migration/recording requirement, or add a declared-alias channel naming both cluster paths, the
shared id, the shared referent, and the documenting location (e.g. a `sanctioned alias` row in
the incoming README's R10 section).

**Related carried debt still live at c4d4823 (not new).** D-JDEP2r91-4: the R9 appendix's
verification command (`:91`) still reads `.ufo/waves/round-91/patches/D2-edges.patch`, not the
delivered text. D-JDEP2r91-5: translation-mode entries still count as source support regardless
of record fields — the delivered tools have 0 hits for reviewer/submitter/manual-review terms
(receipt above), so the R9 receipt boundary remains a textual fence only.

**Per-axis verdicts (delivered `c4d4823` vs baseline `396c568`).**

- *Decisional coverage:* **improved, bounded** — R8's inseparable branch and R9's mandatory
  manual gate are now decided, structured delivered text; R10 untouched. My three cases remain
  uncovered: R8's reviewer-capture edge and R9's lapsed-access edge are at the margin of the new
  text; R10 is a r91 residual.
- *Traceability:* **improved, bounded** — R9 gains owner/trigger/record/worked example/receipt
  boundary; R8 gains owner/trigger/decision. Gaps: R8's reviewer has no identity/independence/
  date field; the R8 label is duplicated; R10 has no channel at all.
- *Bounded verification:* **unchanged** — both tools read none of the three surfaces (0 hits);
  the scratch R9 negative case returns `RESULT PASS`/`CLEAN`, and the two-directory call remains
  a usage error (rc=2). All three edges are editorial screens, as designed.
- *Retroactivity/non-regression:* **unchanged** — the r92 diff does not touch R10; no retro
  edits; landed clusters' receipts are unaffected by this seat (no re-run of the census here).
- No axis harmed; no blocking finding. The r92 R8/R9 decisions stand as improvements; the
  mis-governance cases are named debt on top of them.

## Handoff

- Written: `.ufo/waves/round-92/followup/JDEP4.md` (this report) and
  `.ufo/waves/round-92/followup/JDEP4-evidence.json` (machine-readable receipts). No other
  tracked write; no commit or push.
- Scratch: `/tmp/lore-r92-JDEP4.r9/case-a-lapsed-access` (8-copy probe + appended R9 record;
  10 inodes); the r91 probe reused read-only; `/tmp` inode free 15,398 at last use.
- Classifications: **R8 collaborator-reviewer → mis-governs (new)**; **R8 doubled label →
  delivered text defect (new)**; **R9 lapsed-access → mis-governs (new)**; **R10 deliberate
  alias → mis-governs (carried, unchanged)**.
- Debt handed forward: D-JDEP4r92-1…-4; related carry-over D-JDEP2r91-4/-5.
- Not done here: no `l0-questions.md` append (not authorized for this seat), no boundary-doc
  certification work (other seats' lane), no full fixture census re-run (out of scope).