# JDEP4 — Depth judge #4 (capabilities), round 90

Seat JDEP4. Judged on the DELIVERED tree only: HEAD `ca7f9ef1646cf3fcbe58747785a8cb2e9075ae13`
(baseline `e97613c`); `git status --porcelain` was empty at session start (06:50 `-03:00`) and
shows only follow-up seats' own artifacts later — none written by this seat. All probes ran from the repository root
`/home/vgpnk/Projects/shokunin/lore-shokunin`. Scratch was two files under `/tmp/jdep4-r9/`
(removed on exit); `/tmp` was at 100% inode use (90 free at start), so the freeze check ran
entirely in memory and the probe was kept to two files.

**Question posed to this seat:** recommend for or against a THIRD `capabilities` row, candidate
*sourced-inspiration disposition decisions* (the r90-decided R8/R9/R10 governance), or argue the
two rows suffice. Evidence must be a runnable command.

**Recommendation: AGAINST a third row as phrased — the two rows suffice.** The round's real
capabilities change is that row 2 became corpus-resident and reproducible (its r89 evidence
pointer was wave-resident). The decided governance itself has no runnable demonstration: two of
its three r90 sub-cases have no command at all, and the third (R9 translator/version) is passed
by the only delivered command where the decided verdict says fail. `AXES.md:57-64` admits a row
only through a round that demonstrates the capability running; under either the mission's
runnable-command test or AXES' looser "command or path" pointer, the r90 decisions did not run.

## Work performed

- Read `AXES.md` §Capabilities (row contract), the delivered `SCORECARD.md` (the two rows at
  lines 72-79), the delivered decision table incl. the three r90 appendices (lines 28-59), both
  delivered claim-to-excerpt maps, `corpus/tools/README.md`, the r89 paraphrase demo, and the
  r90 wave artifacts (wave-spec closure amendments, X2/X3/C9, M5, W3, SE3, Q1 debt ledger).
- **Freeze-then-verify (r88-I1)**, fully in memory: composed X2 + X3 on the `e97613c` checker by
  exact-block application of both patch hunks; sha256 compared to the delivered checker (M0).
- Ran the delivered support command on both cluster maps and the paraphrase control (M1); built
  and ran a translator-known / version-unidentified probe cluster (M2); negative checks for R8
  and R10 (M3).
- Ran the SCORECARD row-1 fixture loop, the four new r90 fixtures, and the fn2 pair (M4); re-ran
  all 164 fixture directories and byte-compared the 160 baseline dirs against B1's baseline tuple
  manifest (exit, stdout sha256, violation count) (M5).
- Two 60 s dependency wait-checks, timestamped (M6); no JDEP1–JDEP3 or P1 artifact landed in my
  window, so this seat judged with what exists.

## Before → after measurements

**M0 — freeze-then-verify (blocking gate).** Command: python here-doc (recorded verbatim in
`JDEP4-evidence.json`) that reads `git show e97613cc276f5fa9cac49ff1900798cf6863c020:corpus/fixtures/check_bible.py`,
applies the X2 hunk (null-gate in `holder_identity_detail`) and the X3 hunk (integer-only tick
gate, per the C9 ruling), asserting each hunk's search block occurs exactly once, then hashes.

```text
baseline e97613c sha256 = e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556
X2+X3 composed sha256  = ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
delivered ca7f9ef sha256 = ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
FREEZE-MATCH = True
```

No mismatch → no blocking finding. The delivered checker IS X2+X3 composed; the spec's
superseded X1 boundary is reconciled in the wave-spec closure amendments (`wave-spec.md:130-139`).

**M1 — row 2's command, corpus-resident at ca7f9ef.**

```sh
python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster
python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster
python3 corpus/tools/support_check.py corpus/fixtures/r89-inspiration-paraphrase
```

```text
r87: SOURCE-SUPPORT 22/22; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22
     RESULT PASS   exit=0
r88-m3: SOURCE-SUPPORT 10/10; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 10/10
     RESULT PASS   exit=0
r89-paraphrase: SOURCE-SUPPORT 0/0; RETELLING-SUPPORT-ONLY 1 entries (1/1 anchors); MODES 1/1
     RESULT PASS   exit=0
```

Baseline `e97613c`: `git ls-tree` finds no `corpus/tools/` and neither map — the r89 row-2
evidence pointer (grep over `.ufo/waves/round-89/patches/S2-fact-map.json`, 14/14) was
wave-resident. Delivered hashes: `corpus/tools/support_check.py` `66a3c4bb2ae7fc2049227e480864661606b65a629c64cbc3ce05e14589add472`;
r87 map `8c1b600d28c130f998a0765ae9c4ae30d828b11fe96e3cbd763cd0cf79089b9d`;
r88-m3 map `d314d22ec2bbba149354ef30df96f39468f8f7a54e6c3a4cf824eb9d58dad290`;
decision table `a5ee4dec31083f5cede3a19ec5b36f89d82942a85ea3e10e47cf28e1fc07a344`. All four are
tracked at HEAD.

**M2 — the candidate's strongest possible evidence command, run: it passes the case the decided
governance says fails.** Two-file probe cluster (`claim-to-excerpt-map.md` + `excerpt.md`) whose
map cell reads `` `translation`; translator named; source text/version: unidentified (unverified) ``
and whose excerpt declares `Delivery mode (R9): translation`:

```sh
python3 corpus/tools/support_check.py /tmp/jdep4-r9/probe-cluster
```

```text
PASS entities.json#/0/claims/0: source-support; mode=translation; anchor=found; 6:The keeper moved the tide-mark to the west stair.
SOURCE-SUPPORT 1/1; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 1/1
RESULT PASS   exit=0
```

The decided R9 appendix (delivered table lines 40-47) says: translator name alone, source/version
link unverified → FAILS R5 support. The tool cannot see translator/version fields:
`grep -n -i "translator\|version\|source text" corpus/tools/support_check.py` → no match, exit 1;
and `corpus/tools/README.md:14` disclaims by contract "that a translation is identified to the
required text/version". So no delivered command returns the decided verdict for this sub-case.

**M3 — R8 and R10 have no command.** `grep -rn "possible influence" corpus/` → only the decision
table's own appendix lines 31 and 36 (no fixture instance, no note); `ls corpus/knowledge/cross-cluster-contradictions.md`
→ `No such file or directory` (register absent; R10 is an "explicit manual integration gate",
table line 26; the only worked example is `r89-cross-cluster-contradiction.md`, whose second
cluster is explicitly hypothetical and absent).

**M4 — row 1 and the new C1 fixtures (unchanged behavior + new receipts).**
`for d in r88-shape-ambiguous-armed r88-mixed-stop r88-nonholder-stop` → 5/6/4 violations, exit 1
each (matches the SCORECARD row-1 pointer). New r90 fixtures: `r90-c1-three-causes` → 4
violations, exit 1 (combined first-stop names three causes: invalid tick + absent holder +
absent source); `r90-c1-rawpresent-from` → 5, `-to` → 5, `-source` → 4 violations, exit 1, each
with the raw-present/schema-invalid wording "present in raw … but absent from the resolved
index". fn2 pair: `r89-fn2-control` → 1 violation, definite chain break, exit 1;
`r89-fn2-unresolved-chain-break` → 2 violations, qualified "possible provenance chain break, not
a definite identity mismatch", exit 1.

**M5 — census, independently re-run at ca7f9ef.** All 164 dirs: exit distribution `32 0` /
`132 1`. Every one of B1's 160 baseline dirs replayed against `patches/B1-tuples.json`
(exit, stdout sha256, violation count): `missing=0 exit_changes=0 stdout_sha_changes=0 violation_count_changes=0`.
New dirs are exactly the four `r90-c1-*` fixtures; 0 dirs missing.

**M6 — dependency wait-checks** (two 60 s waits, three timestamped checks, `followup/` listing):
`06:55:34` → only `Q1-r90-debt.json`; `06:56:34` → only `Q1-r90-debt.json`; `06:57:34` →
`H2-delta.json Q1-r90-debt.json`. No JDEP1–JDEP3/P1 artifact landed in this window; judged with
what exists (gap noted, not blocking for a delivered-tree capabilities verdict).

**M6b — post-window cross-check (dated addendum, 07:02 `-03:00`).** JDEP2/JDEP3 landed after my
waits. JDEP2's Handoff independently reports the same freeze result (X2+X3 composed == delivered,
`ff9fd2aa…`, "no mismatch to report"), so two seats agree on M0. JDEP3's Handoff independently
confirms `corpus/knowledge/cross-cluster-contradictions.md` is absent at baseline and delivered
and that no r90 artifact manufactures a shared referent — consistent with my F2(c)/F5(iii). JDEP2
classifies the R8/R9 attack cases as partially covered and R10 as uncovered (its debts
D-JDEP2r90-1…-5), which sharpens, but does not contradict, my no-runnable-demonstration finding.
A `corpus/tools/__pycache__/` directory appeared transiently in `git status` during the follow-up
window (not from my script runs) and was gone by 07:02 — no action recorded for this seat.

## Findings & named debt

**F1 — freeze-then-verify passes.** Composed == delivered (`ff9fd2aa…` both). No blocking finding.

**F2 — Recommendation: AGAINST a third capabilities row as phrased; the two rows suffice.**
Grounds, each with a receipt: (a) `AXES.md:57-64` admits a row only through a round demonstrating
the capability running; (b) the only runnable slice of the governance is R9's mode screen, which
is already row 2's own text ("delivery-mode declaration (R9)") and is demonstrated by M1's
paraphrase control (`RETELLING-SUPPORT-ONLY 1 entries`, `SOURCE-SUPPORT 0/0`); (c) the three
r90-decided sub-cases have no runnable demonstration — R8 no fixture/command (M3), R9
translator/version not enforced and in fact passed by the tool (M2), R10 an explicit manual gate
with no register entry (M3); (d) entering the row with any of these commands as its pointer would
be pre-claiming.

**F3 — The round's actual capabilities change: row 2 becomes corpus-resident and reproducible.**
At r89 the row's pointer was wave-resident (`S2-fact-map.json`); at ca7f9ef a committed tool plus
committed maps give `python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster` →
`SOURCE-SUPPORT 22/22 … MODES 22/22`, exit 0, and the same command on `r88-m3-maya-cluster` →
10/10, exit 0 (M1), with the paraphrase negative control. The closure should update row 2's
evidence pointer to this command set and keep first-working r89 with a corpus-residency note
(r90). Suggested bound text: lexical preflight only; span-enforced (M5 attack receipts in
`M5.md`); translator/source-version tie is NOT checked (the R9 appendix remains editorial).

**F4 — What would justify a third row later (named r91 candidate).** Make at least one decided
disposition mechanically decidable — e.g. extend the map format + `support_check.py` to require
a translator/source-version tie for `translation` mode (fail when unidentified) and/or land a
durable fixture for R8's `possible influence: unverified` note — so a command returns the decided
verdict. Until then the governance correctly lives in the depth-axis decision table.

**F5 — Named debts.** (i) The three decided appendices landed with no durable fixtures on the
delivered tree; the four new fixtures are all C1 calibration, so the only governance-exercising
fixture remains r89's paraphrase demo. (ii) r88-m3's Spence `source-excerpt.md` carries its R9
mode only in the map declaration table, and the two Spence comparison rows are bullets, not table
rows, so they are outside the tool's fact census — consistent with the tool README's scope, but
worth stating in the row-2 bounds. (iii) The R10 register procedure has never run on two real
landed clusters (only a hypothetical demo plus empty-set probes), so its first real exercise
remains prospective.

**Per-axis verdicts (this seat's remit).**
- **depth: improved (bounded)** — the three undecided sub-cases are decided in the delivered
  table (appendices at lines 28-59, committed at ca7f9ef), closing JDEP2's r89 finding; bounds
  F2/F5 (decided governance without fixtures/commands; capability table correctly unchanged at
  two rows).
- **coverage: improved (bounded)** — maps + support command corpus-resident; receipts 22/22 and
  10/10 with exit 0; census 164 dirs with 0 changes among the 160 baseline dirs; bound: lexical
  preflight only, translator sub-case outside the tool, Spence comparison rows not consumed.
- **calibration: unchanged (per this seat's slice; bounded)** — freeze hash-match, 0 exit
  changes, 0 stdout-byte changes and 0 violation-count changes over all 160 baseline dirs (M5),
  row-1 fixtures still 5/6/4, fn2 pair definite/qualified as intended (M4). The C1
  wording-definiteness repair is claimed by its own seats; a fixture-manifest-visible byte delta
  is exactly zero, so no regression is visible in my slice.

## Handoff

- **Verdict: AGAINST a third capabilities row as phrased.** The two rows suffice; update row 2's
  evidence pointer at closure (F3) instead. If the parent still wants the governance recorded as
  a capability, the honest form is a bounded r91 row admitted only with a command that returns
  the decided disposition (F4) — not this round.
- Reproduce everything: M0's python here-doc, M1/M2's commands, M4/M5's loops and the B1-tuple
  comparison are recorded verbatim in `followup/JDEP4-evidence.json` (commands + raw outputs).
- Files written by this seat: `followup/JDEP4.md` and `followup/JDEP4-evidence.json` only. No
  SCORECARD/LOG/README edit (not authorized), no commit, no push, no sibling-repo writes; the
  `/tmp` probe was removed.
- Gaps: no JDEP1–JDEP3/P1 artifact in the dependency window (M6); JDEP2/JDEP3 landed after it
  and were cross-checked in M6b (freeze agreement; register/no-referent agreement). This seat's
  judgement uses the delivered tree and wave evidence only; the full byte-census and closure
  bookkeeping remain with the JCAL/P1 seats.
