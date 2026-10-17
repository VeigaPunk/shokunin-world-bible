# PROPOSAL ONLY — Round 91 LOG entry (W2)

Scribe proposal only; do not append to `LOG.md` before integration and L1 adjudication. This draft records the persisted claims and W2's r90-closure baseline receipts, not an integrated result, verdict, score, or admission. Keep C1–C3 **PENDING-L1**.

## Round 91 — 2026-10-17 (proposed work-wave evidence record; L1 pending)

- The persisted spec is `.ufo/waves/round-91/wave-spec.md`; baseline `a7c6a1773d5994246a76e4eff30d645f161920e0` (`a7c6a17`, r90 closure). It declares C1 calibration, C2 coverage, and C3 depth. The 32-seat declaration lists 30 seat IDs including W2 (29 named peers); two IDs are not named in the text, and the declared machine-readable `.ufo/waves/round-91/wave-spec.json` is absent at W2's inventory. Treat this as a roster-data/process gap, not as evidence that unnamed seats failed.
- **C1 calibration — PENDING-L1.** W2 measured the existing baseline census only: 164 fixture directories; exits `{0: 32, 1: 132}`; 417 violation lines; empty stderr; checker SHA-256 `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`. The exact command/output is in `.ufo/waves/round-91/W2.md`. The first inventory found no `r91-c1-*` fixture directory and no `corpus/knowledge/r91-c9-watch.md`. TODO: establish that each durable fixture's current output differs from the `e97613c` checker exactly as declared; retain definite `got None`, integer-only tick under a genuinely unresolved compared holder, and qualified chain-break; pin the delivered checker hash and C9 falsification trigger in the watch. No after-state or checker-hash watch is claimed here.
- **C2 coverage — PENDING-L1.** Baseline `support_check.py` receipts: r87 `SOURCE-SUPPORT 22/22`, r88-m3 `10/10`, and the paraphrase demo `0/0` source support with one retelling-only anchor; all exit 0. The r87 denominator is 22 mapped rows (14 JSON-fact rows plus 8 editorial hymn rows), not 22 JSON facts; r88-m3 has 10 mapped JSON facts plus two separate symbolism comparisons. The r88 map has 10 rows but 6 distinct anchor strings, with four repeated-anchor occurrences and no repeated complete rows. TODO: compare each declared map inventory to parsed rows; surface distinct-anchor and duplicate-row counts; warn for missing retelling anchors; split the r87 receipt into JSON facts, editorial rows, and total rows; and rerun the expected-inventory, dropped-section/header, duplicate-row, unreferenced-row/mode-flip, and retelling-anchor-miss controls on the integrated support command. The baseline command output and current-code inspection limits are in W2.md.
- **C3 depth — PENDING-L1.** The r90 appendices exist, but the inherited JDEP2 report identified the prospective residuals now declared for r91: (1) R8 failed-gate disposition and precedence between element-level and detail-level withhold; (2) R9 whether a later reprint can establish the translation tie and what makes that tie reliable; (3) R10 shared `source_id` namespace scoping across clusters (a repeated key is not identity). TODO: quote the adopted rule for each edge, with its owner, trigger, worked example, and verification command; manually compare both landed clusters and verify the register disposition. The baseline register path is absent; this is not proof that it is correctly empty. W2 did not make or adjudicate these policy choices.
- No L1 verdict or numeric score is offered. A patch, authored example, successful checker exit, or absent file is not a substitute for the delivered-tree replay and relevant human review. Keep any unverified after-state as `NOT MEASURED`.

### Process and named debt

- The 60-second peer-report poll, final seat/patch inventory, exact timestamps, and any absent-seat gap belong in `.ufo/waves/round-91/W2.md`; do not infer failure from a report absent at an individual check. The poll covers only the 29 peer IDs explicitly listed by the spec. The two undeclared IDs cannot be polled by name without the missing JSON roster.
- `/tmp` was inode-saturated at preflight (5,614 free; `IUse%=100%`). W2 created no scratch archive, alternate scratch files, or fixture copies; no cleanup was necessary. The exact `df -i` command/output is in W2.md.
- W2 wrote only its report and `patches/W2-*` proposals/scaffold. No tracked file was changed; no patch was integrated, and no commit or push was attempted.

### Handoff

- `.ufo/waves/round-91/patches/W2-scorecard-r91.proposal.md` — candidate SCORECARD section.
- `.ufo/waves/round-91/patches/W2-log-r91.proposal.md` — candidate LOG entry.
- `.ufo/waves/round-91/patches/W2-report-r91.skeleton.md` — phase-2 report scaffold.
- `.ufo/waves/round-91/W2.md` — scribe report with exact receipts, poll terminal record, peer inventory, and named gaps.
- All C1–C3 items remain **PENDING-L1**; no admission, score, integration, or closure is claimed.
