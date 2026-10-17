# JDEP1 — Venue judge (r93 follow-up)

Seat: JDEP1, world-bible lane. Judged tree: `65838f867d6ece8e7b8bdcc4ffc667a08a1b785e` (r93 WORK), tree clean at seat start (`git status --porcelain` empty). Baseline: `87779a0`. Mission: R9 venue repair structure proof, worked example presence, no orphaned duplicates, R8 clarified-disposition integrity, dossier required-record-field completeness; verdict recommendation. All evidence below is from the committed tree at `65838f8`; probes were scratch-only (`/tmp/jdep1-*.diff|md`, heredocs). No commit, no push; the only tracked write by this seat is this file.

## Work performed

1. Confirmed tree state: `git rev-parse HEAD` → `65838f8…785e`; `git status --porcelain | head -20` → empty.
2. Read the two judged artifacts in full: `corpus/knowledge/r88-sourced-inspiration-decision-table.md` (125 lines) and `corpus/knowledge/r93-r8-worked-example.md` (73 lines).
3. Ran a structure proof (heading/block line-finder, python heredoc) at HEAD and at baseline (`git show 87779a0:…`).
4. Byte-identity proofs per moved paragraph (git show both revs, paragraph extraction by `**Label` prefix + `\n\n` boundary, equality compare); R8 disposition compared after collapsing the duplicated label; landed diff vs the D1 candidate patch (`git diff 87779a0 65838f8 -- <table>` vs `git show 65838f8:.ufo/waves/round-93/patches/D1-venue.patch`, payload lines only); landed R8 worked example vs the r92 instrument text (`.ufo/waves/round-92/patches/E1-edges.md`).
5. Ran the dossier's own embedded replay verbatim (`D2_DOSSIER=… python3 - <<PY` from repo root) — read-only, exit code captured.
6. Ran the certification tool on the committed tree: `python3 corpus/tools/boundary_doc_check.py` (defaults: doc `corpus/knowledge/holder-assessment-boundary.md`, checker `corpus/fixtures/check_bible.py`); verified the checker pin: `sha256sum corpus/fixtures/check_bible.py` and `git diff --quiet 87779a0 65838f8 -- corpus/fixtures/check_bible.py`.
7. Orphan sweep over `corpus/` for the gate-block labels (`**Manual R9 gate`, `**Required record:`, `**Receipt boundary:`), the old worked-example opener (`A delivered line from a copy marked`), and `copy marked`.
8. Cross-checked the wave records: r92 debt `Q92-002` (`.ufo/waves/round-92/followup/Q1-r92-debt.json`), r93 ledger entries Q92-002/Q92-004 (`.ufo/waves/round-93/patches/Q1-r93-debt.json`), seat reports D1/D2/CERT tails.
9. Two 60 s wait-checks on `.ufo/waves/round-93/followup/` (12:33:02, 12:34:02): sibling followup artifacts present (H4/H5, JCAL1/2/3/5, JDEP2/JDEP4, P3/P4, V2, X1 + JSONs); none conflict with this seat; no dependency gap for JDEP1.

## Before → after measurements

**M1 — R9 manual-gate block placement (structure proof).**

Command (HEAD): heading/block line-finder over `corpus/knowledge/r88-sourced-inspiration-decision-table.md`. Observed at HEAD:

```text
R8 heading:28 Failed-gate:40 R8-WE:[42, 79] R9 heading:44 gate:73 required:75 receipt:77 R10 heading:87
gate INSIDE R9 appendix: True | required: True | receipt: True
gate after Decision para: True | gate before WE: True
```

Observed at baseline (same probe on `git show 87779a0:…`):

```text
BASELINE 87779a0: R8 heading:28 gate-block-start:42 R9 heading:50 R10 heading:94
gate INSIDE R9 appendix: False | failed-gate label count: 2 | Kesh Hymn hits: 0 | old-R9-WE opener present: True
```

The whole gate trio sits at :73/:75/:77, after the appendix's **Decision** paragraph and before its **Worked example** (:79), inside `### R9 appendix` (:44) and before `### R10 appendix` (:87) — exactly the placement r92 E1 specified. Q92-002's core defect (block before the heading) is gone at HEAD. **improved.**

**M2 — Orphaned duplicates.**

- `**Failed-gate disposition (clarified r92):**` count: HEAD **1**, baseline **2** (doubled label repaired).
- `**Worked example:**` line-starts at HEAD: `[42, 79]` (one R8, one R9); a third raw occurrence is the literal key string inside the R9 verification-command fence (:84) — not a rendered example. Baseline had two real R9 worked examples (:48 misplaced new + :79 old).
- Old R9 worked-example opener `A delivered line from a copy marked` : HEAD **0 hits** (baseline present); repo-wide `grep 'copy marked' corpus/` → 0 hits. Old opener absent everywhere in the corpus surface.
- `grep -c 'Manual R9 gate'` over corpus/knowledge: decision table **1**; `r93-r8-worked-example.md` **0**; `holder-assessment-boundary.md` **0**. The gate/record/receipt labels exist only inside the R9 appendix — no copies elsewhere.
- Headings `### R8|R9|R10 appendix`: count 1 each at HEAD.

**improved** — no orphaned duplicates remain.

**M3 — Byte-identity of the move and of the R8 clarified disposition.**

Per-paragraph equality (baseline vs HEAD):

```text
Manual R9 gate: byte-identical across the move = True (old 1345 ch / new 1345 ch)
Required record: byte-identical across the move = True (old 546 ch / new 546 ch)
Receipt boundary: byte-identical across the move = True (old 651 ch / new 651 ch)
R9 worked example (new): byte-identical across the move = True (old 884 ch / new 884 ch)
R8 clarified disposition identical after label dedup: True
R9 evidence-cell append present at HEAD: True (absent at baseline: True)
```

Landed diff vs candidate: `/tmp/jdep1-landed.diff` reverse-applies to the working tree; payload lines equal `.ufo/waves/round-93/patches/D1-venue.patch` except regenerated `@@` hunk-header context annotations (49 payload lines each; only header-context lines differ). Landed R8 worked example equals E1's copy-ready text: `landed R8 WE == E1 copy-ready text: True`. The repair applied the instrument verbatim — no silent rewording anywhere. **improved.**

**M4 — Worked example present.** R8 (Kesh Hymn, seven threshold names) at :42 inside the R8 appendix — byte-equal to E1's r92 wording; R9 worked example at :79 is the single consolidated example (submitter/2011 reprint/scan + copy locator) with the FAIL/OPEN fallback in its final sentence. **improved** (baseline: 0 Kesh hits; two competing R9 examples).

**M5 — Dossier required record fields (r92 decision).** The R8 clarified-disposition paragraph requires recording: failed condition, contrary evidence, separability rationale, scope, next action. Dossier record table (`corpus/knowledge/r93-r8-worked-example.md:15-22`) carries all five (failed condition → **Gate result** row recording R2-unavailable and which limb fails; plus **Contrary evidence**, **Separability rationale**, **Scope / disposition**, **Next action**) and additionally the JDEP4-r92 edge fields (element/scope pointer; creator account; reviewer identity + record date + independence caveat, example-only). Embedded replay run verbatim:

```text
gate_result: PASS
contrary_evidence: PASS
separability_rationale: PASS
scope: PASS
next_action: PASS
R8 record fields: 5/5
EXIT=0
```

**improved** — every required record field present; the replay contract reproduces on the committed tree.

**M6 — Certification tool + checker pin.** `python3 corpus/tools/boundary_doc_check.py` (HEAD):

```text
CHECK receipt replay: PASS
CHECK code anchors: PASS
CHECK document structure: PASS
replay_receipts=3/3
replay_cases=14/14
anchors=2/2
h1_count=1
duplicate_headings=0
instruction_markers=0
CERTIFIED
EXIT=0
```

`sha256sum corpus/fixtures/check_bible.py` → `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` = the pin in `boundary_doc_check.py:389`, `discriminate_check.py:12`, the boundary doc, and the C9 watch; `git diff --quiet 87779a0 65838f8 -- corpus/fixtures/check_bible.py` → unchanged. **improved (bounded)** — see debt for the tool's named limits.

**M7 — Q92-002 ledger state.** r93 ledger (wave-time snapshot): `"current_status": "open; D1/D2 candidate-only"`. At HEAD every evidence row of Q92-002 is flipped by M1–M4: label 2→1, Kesh 0→1, gate/record/receipt 0/0/0→1/1/1 inside the appendix, legacy R9 example 1→0, evidence-cell receipt 0→1.

## Findings & named debt

- **No-trade check on the worked-example replacement:** replacing the old R9 example (generic re-issue note, FAIL branch) loses no decisional coverage — the FAIL rule stays in the R9 **Decision** paragraph ("a generic reprint notice, untraceable secondary entry, translator name, or anchor alone is insufficient", :63-65) and the new example's closing sentence carries the FAIL/OPEN + `Source text/version: unidentified; unverified` fallback (:79). Consolidation, not a coverage cut.
- **Q92-002 — recommend CLOSE** on committed-tree evidence (M1–M4, M7). The wave-time "open; candidate-only" status is superseded by the integrated tree this seat verified.
- **Q92-004 — carried open (named).** The R9 textual-completeness verification command (table :84) still reads `.ufo/waves/round-91/patches/D2-edges.patch` — a wave artifact, not the committed table; D1 left it unchanged deliberately. A reader replaying the command verifies the r91 patch, not HEAD.
- **Dossier probe-precision nit (new, minor — name for r94).** The dossier's five replay probes require `'**Gate result**'`-style bold names; the record-table rows are unbolded (`| Gate result |`, dossier :15-22), so the bold-name probes are satisfied only by the embedded script's own source text inside the same file (:50-54). The contract still exits 0 and this seat verified all five fields present by direct read, but the probes would not flip if the table rows were deleted while the script text remained. r94 suggestion: probe the row forms (`'| Gate result |' in dossier`) or bold the rows.
- **Cert-tool limits (named r94 debt, confirmed present, not re-probed here).** CERT.md states the line-anchor gate validates cited line numbers only — no AST/content-signature or C9-semantic review; Q1's candidate receipt records CB-audit's false-accept probes (wrong-citation, contradictory-tick, modified-checker) still accepting with exit 0. `CERTIFIED` therefore covers receipts/anchors/structure only.
- **Scope note.** Dossier seat D2 and venue seat D1 produced the artifacts; CERT integrated and ran the tool pre-landing; this seat re-ran everything on the committed tree. Baseline defects were delivered at r92 WORK `c4d4823` and persisted into `87779a0`.

## Handoff

- **Verdict recommendation (per-axis, committed tree `65838f8` only):**
  - C1 venue-repair sub-claim (R9 gate placement + example consolidation + evidence-cell receipt): **improved** — structure, byte-identity, uniqueness, and instrument fidelity all verify; no trade found on the corpus surface.
  - C1 dossier sub-claim: **improved** — required record fields complete (incl. reviewer identity/date/independence edge fields); embedded replay 5/5, exit 0; probe-precision nit named, non-blocking.
  - C1 certification sub-claim: **improved (bounded)** — tool runs `CERTIFIED` exit 0 on HEAD; checker pin `ff9fd2aa…d1421` matches and the checker is unchanged across the round; AST/content-signature validation and the CB-audit false-accept limits are named r94 debt.
  - Q92-002: **close.** Q92-004 and the two r94 items above: carry.
- Wave-dependency wait-checks: 2 × 60 s (12:33:02, 12:34:02) — sibling followup artifacts present and growing (JDEP2/JDEP4/JCAL*/H4/H5/P3/P4/V2/X1 at first check; V2 by second); no JDEP1 dependency gap; no conflicts observed.
- This seat wrote only `.ufo/waves/round-93/followup/JDEP1.md`. Scratch: `/tmp/jdep1-landed.diff`, `/tmp/jdep1-baseline-table.md` (removable). No commit, no push, no other tracked writes.
