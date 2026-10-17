# PROPOSAL ONLY — Round 89 LOG entry (W2)

Scribe proposal only; do not append to `LOG.md` before integration and L1 review. This draft records the declared work and evidence status, not a closure, score, verdict, or admission.

## Round 89 — proposed evidence record (phase-1 reports; L1 pending)

- The persisted spec is `.ufo/waves/round-89/wave-spec.md`, baseline `51b286b` (full hash observed locally: `51b286b5a1e503e6e6ace1f8da0bd606a3c10d94`). It declares C1 calibration, C2 coverage, and C3 depth; W2 owns proposals only. The first inventory found only the spec. Exact command and observed output:

  ```text
  $ date -Is && ls -la .ufo/waves/round-89
  2026-10-17T03:28:37-03:00
  total 8
  drwxr-xr-x 1 vgpnk vgpnk   24 Oct 17 03:25 .
  drwxr-xr-x 1 vgpnk vgpnk   48 Oct 17 03:25 ..
  -rw-r--r-- 1 vgpnk vgpnk 4827 Oct 17 03:25 wave-spec.md
  ```
  This was the initial snapshot; timestamped 60-second wait-checks continued through the 25-minute cutoff and their terminal inventory is recorded below. An absent report at one check is not evidence of failure.
- **Wait checks.** The initial check at `2026-10-17T03:28:37-03:00` found only `wave-spec.md`; exact command/output are retained in the SCORECARD proposal. A root-report inventory ran every 60 seconds from `2026-10-17T03:27:45-03:00` through the deadline check at `2026-10-17T03:52:45-03:00`; a second report-and-patch inventory ran from `2026-10-17T03:46:52-03:00` through `2026-10-17T03:52:52-03:00`. Final inventories and exact outputs are recorded in the SCORECARD proposal and W2.md. At the deadline the reports included B1/B2/B3, D1/D2, E1, F1/F2/F3, M1/M5, S1/S2/S4/SE1, X2, W2, and the wave spec; patch-only late arrivals X1's patch and tuple delta were present, but `X1.md` was absent. An absent report at a point-in-time check is not evidence that its seat failed.
- **C1 calibration — PENDING-L1.** B1/B2 independently census the pinned baseline with `python3 corpus/fixtures/check_bible.py corpus/fixtures/<dir>` once per direct fixture: 149 fixtures, exits 31=0 / 118=1, 367 findings, empty stderr; final tuple artifacts match (`B1.md:11-28`, `B2.md:12-26, 60-69`). At deadline, `X1-c1.patch` and `X1-tuple-delta.json` were present without an X1 report. The candidate delta says 145 unchanged tuples and 4 changed stdout tuples (`r87-probe-multi-invalid`, `r87-probe-record-and-chain`, `r88-mixed-stop`, `r88-nonholder-stop`), with 149 directories, 31/118 exit counts, 367 violation lines, and zero exit-status or stderr changes. This is scratch candidate evidence, not a delivered or independently replayed result. X2's separate scratch census/diff (`X2.md:12-71, 177-220`) changes only `r87-probe-multi-invalid` stdout. S1's command `S1_COMPACT=1 python3 /tmp/lore-s1-twjRWB/prototype.py /tmp/lore-s1-twjRWB` reports A: 1 changed tuple, B: 0, C: 3; all with 0 exit flips (`S1.md:27-47`). On the F3 scratch pair, `S1_COMPACT=1 python3 /tmp/lore-s1-twjRWB/prototype.py /tmp/lore-s1-f3-lzUbIj` changes only the unresolved FN-2 fixture, not its control (`S1.md:49-62`). S1's C suffix does not distinguish truly absent IDs from schema-rejected raw rows; E1's stronger raw-presence wording is untested. B3 reports baseline gaps; X3's qualification-only patch has no report/replay. TODO: independently replay the X1 patch and its six durable C1 fixtures, verify FN-1/FN-2 controls, and confirm complete delivered-tree behavior.
- **C2 coverage — PENDING-L1.** M1 applied its two-excerpt patch in `/tmp`, matched 7/7 assigned exact anchors, and reviewed whole-claim support (`M1.md:28-48`); its r87 cluster command returned `CLEAN: schema, citations, relations, timeline; 0 violations`, which is only structural validation. S2's deadline report maps 14 facts (6 entity, 4 relation, 4 timeline) and preflights all 14 phrases against M3 candidate added lines; the delivered cluster still has 0/4 target excerpts and 0/14 exact anchor hits (`S2.md:14-89`). It co-maps six `first_appearance` pointers and cautions that the shell-charter phrase states a pledge, not completed watch performance, and tide-bell-tally is fixture-local ordering (`S2.md:141-146`). M3's four-excerpt patch has no M3 report or delivered anchor verification. M5 scratch-verifies the ETCSL marker: seven pipe-table rows × four columns, marker `False → True`, three other cells unchanged (`M5.md:13-20`). No 22/22 support result or delivered-tree marker check is established.
- **C3 depth — PENDING-L1.** D1's row-shape QA reports seven baseline data rows plus three proposed rows, six cells each, and one command/output per row (`D1.md:13-30`). D1's scratch R9 paraphrase and R10 cross-cluster probes are diagnostic evidence only; D2 confirms that per-fixture `CLEAN` cannot assess cross-cluster consistency. E1 cross-checks the row drafts and offers six-column wording. No durable R9 fixture/replay or integrated table is present at deadline; S3's seven-column statement is a counting error. Preserve rights and training permission as separate open matters.
- No complete C1–C3 delivered after-state or independent L1 verdict is established. Scores remain unassigned; no round admission is claimed.
- **Named debt:** independently replay X1 and the six durable C1 fixtures with FN-1/FN-2 controls; census and explain delivered-tree tuples; resolve C2 excerpt selection and S4/S2 R3 wording, verify delivered anchors and the M5 marker; reconcile D1/D2/S3/E1 rows and verify a durable R9 demo; await independent L1 review. Keep every unavailable check as TODO.

## Handoff

- Proposal artifacts: `.ufo/waves/round-89/patches/W2-scorecard-r89.proposal.md` and `.ufo/waves/round-89/patches/W2-log-r89.proposal.md`.
- Fleet-report scaffold: `.ufo/waves/round-89/patches/W2-report-r89.skeleton.md`.
- Seat report: `.ufo/waves/round-89/W2.md`.
- Do not promote placeholders to verdicts. Integration must use the delivered revision, independent measurements, and L1 adjudication; retain every unresolved item as named debt.
