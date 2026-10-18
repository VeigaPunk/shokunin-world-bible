# PROPOSAL ONLY — Round 89 SCORECARD section (W2)

Do not append this draft to `SCORECARD.md` without integration and L1 review. This is a phase-1 scribe proposal, not a closure record. All three verdicts remain **PENDING-L1**; scores remain unassigned. The declared claims below are requirements, not evidence that they were met.

## Round 89 — proposed claim rows (all verdicts pending)

| # | axis / claim | proposed verdict | measured before → after | evidence and limit |
|---|---|---|---|---|
| C1 | calibration — first-cause branches, complete multi-cause summary, FN-1/FN-2 wording | **PENDING-L1** | **Before:** B1/B2 agree on 149 tuples, exits 31=0 / 118=1, 367 findings, empty stderr. **X1 scratch candidate delta at deadline:** 145 unchanged tuples, 4 changed stdout tuples, no added/removed directories, exit-status changes, or stderr changes; totals remain 149 directories, 31 clean / 118 violating, 367 violation lines. The changed paths are `r87-probe-multi-invalid`, `r87-probe-record-and-chain`, `r88-mixed-stop`, and `r88-nonholder-stop`. X2 and S1's isolated prototypes are separate results; no full delivered C1 after-state. | At cutoff, `X1-c1.patch` plus `X1-tuple-delta.json` supply scratch-candidate evidence, but no `X1.md` report, independent replay, or delivered-tree result was present. The delta shows four changed stdout tuples and no exit/stderr changes; this does not establish the six branch replays, FN-1 distinction, or FN-2 qualification as a delivered result. X2 and S1-A are separate C1(ii) prototypes. S1-B qualifies the F3 unresolved-holder chain break in scratch; S1-C's simple “absent from resolved index” suffix does not distinguish raw absence from a schema-rejected raw row. E1 proposes stronger wording, but no separate verification receipt for it was present. X3's qualification-only patch was present at cutoff without a report/replay. B3 confirms baseline FN-1/FN-2 gaps; F1/F2 patches and the F3 pair are fixture-level evidence, not delivered X1 replays. Exact receipts: B1.md:11-28; X1-tuple-delta.json; X2.md:12-71, 177-220; S1.md:27-62, 76-78; B3.md:20-23; F1.md/F2.md/F3.md. |
| C2 | coverage — complete D1 support anchors for r87 and ETCSL delivery marker | **PENDING-L1** | M1 scratch-applies its two-excerpt patch and verifies 7/7 assigned anchors with whole-claim review; the cluster checker returns CLEAN. S2's deadline report maps 14 targeted facts (6 entities, 4 relations, 4 timeline items) and preflights all 14 anchor phrases against M3 candidate added lines, but reports 0/4 target excerpts delivered and 0/14 exact anchor hits in the current cluster. M5 scratch-verifies ETCSL marker `False → True` and preserves the other three ledger cells. No 22/22 delivered support result or integrated ledger is verified. | M1 covers only `gate-witness`/`dune-register` facts; its CLEAN result is structural, not prose-support evidence. S2 co-maps the six `first_appearance` pointers within the 14 facts and flags that Shell-charter records a pledge, not completed watch performance; `tide-bell-tally` is fixture-local ordering (`S2.md:14-89, 141-146`). M3's four-excerpt patch has no M3 report or delivered anchor verification at cutoff. S4/M1 also flag the pledge/performance boundary. Exact receipts: M1.md:7-10, 28-48; S2.md:14-89, 141-146; M5.md:13-20; S4.md:49-52. |
| C3 | depth — R8/R9/R10 precedents and replay-verified R9 demo | **PENDING-L1** | D1's draft QA reports 7 baseline rows + 3 proposed rows = 10 projected, with six cells per proposal and command/output in each. D1's scratch probes, D2's independent probes, and E1's wording rows are not an integrated table. No durable R9 fixture/replay was present at the deadline cutoff. | D1 verifies that paraphrase text can pass the checker and anchor while not being source wording; its R10 pair is individually CLEAN but has a place conflict and no registry. D2 independently confirms the one-directory CLI limit; E1 reconciles the row governance and warns against treating an uncertain match as a confirmed contradiction. S3 mislabels the six-column table as seven. These support the need for R8–R10 governance, not the required durable R9 demo or an integrated/independently adjudicated table. Keep rights/permission open. |

### Evidence and exact receipts available at the 03:32:29 checkpoint

At 03:28:37 the directory contained only `wave-spec.md`. At 03:32:29 the root reports were `B1.md`, `B3.md`, `F1.md`, `F2.md`, `F3.md`, `W2.md`, and `wave-spec.md`; available claim artifacts included `B1-tuples.json`, `B2-tuples.json`, `B3-before-state.json`, `F1/F2/F3` fixture patches, `X2-c1-summary-only.patch`, `S2-fact-map.json`, `M3-excerpts.patch`, `M5-ledger-marker.patch`, `D2-rows.md`, and `S3-r8-r10-sketches.md`. No X1 implementation report/patch, M4 anchor verification, D3 R9 demo, or R1/T1 row review was present. Exact checkpoint command/output and full path list:

```text
$ date -Is && ls -1 .ufo/waves/round-89/*.md .ufo/waves/round-89/patches/* | sort
2026-10-17T03:32:29-03:00
.ufo/waves/round-89/B1.md
.ufo/waves/round-89/B3.md
.ufo/waves/round-89/F1.md
.ufo/waves/round-89/F2.md
.ufo/waves/round-89/F3.md
.ufo/waves/round-89/W2.md
.ufo/waves/round-89/patches/B1-tuples.json
.ufo/waves/round-89/patches/B2-tuples.json
.ufo/waves/round-89/patches/B3-before-state.json
.ufo/waves/round-89/patches/D2-rows.md
.ufo/waves/round-89/patches/F1-cause-fixtures.patch
.ufo/waves/round-89/patches/F2-cause-fixtures.patch
.ufo/waves/round-89/patches/F3-fn2-fixtures.patch
.ufo/waves/round-89/patches/M3-excerpts.patch
.ufo/waves/round-89/patches/M5-ledger-marker.patch
.ufo/waves/round-89/patches/S2-fact-map.json
.ufo/waves/round-89/patches/S3-r8-r10-sketches.md
.ufo/waves/round-89/patches/W2-log-r89.proposal.md
.ufo/waves/round-89/patches/W2-report-r89.skeleton.md
.ufo/waves/round-89/patches/W2-scorecard-r89.proposal.md
.ufo/waves/round-89/patches/X2-c1-summary-only.patch
.ufo/waves/round-89/wave-spec.md
```

B1's per-fixture command was `python3 corpus/fixtures/check_bible.py corpus/fixtures/<dir>` from its `/tmp` archive. B1 reports `baseline_commit: 51b286b5a1e503e6e6ace1f8da0bd606a3c10d94`, `fixture_count: 149`, `exit_counts: 0=31, 1=118`, `total_violations: 367`, and `stderr_nonempty_count: 0` (`B1.md:11-28`). The local artifact audit command was:

```sh
python3 - <<'PY'
import json
from collections import Counter
from pathlib import Path
root = Path('.ufo/waves/round-89/patches')
paths = [root / 'B1-tuples.json', root / 'B2-tuples.json']
data = [json.loads(p.read_text()) for p in paths]
for p, d in zip(paths, data):
    exits = Counter(row['exit'] for row in d.values())
    violations = sum(row['violation_count'] for row in d.values())
    print(f'{p}: fixtures={len(d)}; exits={dict(sorted(exits.items()))}; violation_count={violations}')
print(f'B1_B2_JSON_equal={data[0] == data[1]}')
PY
```

Observed output: `B1-tuples.json: fixtures=149; exits={0: 31, 1: 118}; violation_count=367`; `B2-tuples.json: fixtures=149; exits={0: 31, 1: 118}; violation_count=367`; `B1_B2_JSON_equal=True`. B1/B2 are before-state receipts, not a post-fix comparison. B3's 16 baseline receipts and F1/F2/F3 commands and stdout are preserved in their seat reports; fixture expectations and patch replays are not proof of integrated behavior.

### Deadline inventory — cutoff 2026-10-17T03:52:52-03:00

The root-only inventory polled every 60 seconds from `03:27:45` through `03:52:45` (25 minutes). The report-and-patch poll began at `03:46:52` and ended at `03:52:52`. Its deadline command was:

```sh
deadline=$(date -d '2026-10-17T03:52:51-03:00' +%s); while [ "$(date +%s)" -lt "$deadline" ]; do printf 'POLL '; date -Is; printf 'REPORTS\n'; ls -1 .ufo/waves/round-89/*.md 2>/dev/null | sort; printf 'PATCHES\n'; ls -1 .ufo/waves/round-89/patches 2>/dev/null | sort; sleep 60; done; printf 'DEADLINE '; date -Is; printf 'REPORTS\n'; ls -1 .ufo/waves/round-89/*.md 2>/dev/null | sort; printf 'PATCHES\n'; ls -1 .ufo/waves/round-89/patches 2>/dev/null | sort
```

Final observed output:

```text
DEADLINE 2026-10-17T03:52:52-03:00
REPORTS
.ufo/waves/round-89/B1.md
.ufo/waves/round-89/B2.md
.ufo/waves/round-89/B3.md
.ufo/waves/round-89/D1.md
.ufo/waves/round-89/D2.md
.ufo/waves/round-89/E1.md
.ufo/waves/round-89/F1.md
.ufo/waves/round-89/F2.md
.ufo/waves/round-89/F3.md
.ufo/waves/round-89/M1.md
.ufo/waves/round-89/M5.md
.ufo/waves/round-89/S1.md
.ufo/waves/round-89/S2.md
.ufo/waves/round-89/S4.md
.ufo/waves/round-89/SE1.md
.ufo/waves/round-89/W2.md
.ufo/waves/round-89/wave-spec.md
.ufo/waves/round-89/X2.md
PATCHES
B1-tuples.json
B2-tuples.json
B3-before-state.json
D1-rows.md
D2-rows.md
E1-r89-wording.md
F1-cause-fixtures.patch
F2-cause-fixtures.patch
F3-fn2-fixtures.patch
M1-excerpts.patch
M3-excerpts.patch
M5-ledger-marker.patch
S2-fact-map.json
S3-r8-r10-sketches.md
W2-log-r89.proposal.md
W2-report-r89.skeleton.md
W2-scorecard-r89.proposal.md
X1-c1.patch
X1-tuple-delta.json
X2-c1-summary-only.patch
X3-c1-qualify-only.patch
```

Thus X1 code and tuple-delta artifacts were present at cutoff, but no X1 report; M3's patch was present, but no M3 report; D3's durable R9 demo patch, M4's final excerpt patch, and independent R1/T1 review were absent. A separate inventory at `03:55:06` first observed after the cutoff showed later artifacts (including `X1.md`, `X3.md`, `W1.md`, `C8.md`, `D3-r9-demos.patch`, and `M4-excerpts-final.patch`); those post-cutoff arrivals are excluded from these proposal measurements. An absent report at cutoff is not evidence its seat failed.

### TODO before SCORECARD integration

- **C1:** use B1/B2's matched baseline manifests; select/review the primary X1 candidate and verify the six branch fixtures, valid-key combined-cause output, FN-1 distinction, and FN-2 qualification against it. X2 is an independently replayed summary-only alternative (one intended stdout tuple changed, 0 exits flipped), not a complete C1. Enumerate all delivered-tree tuple deltas and exit changes.
- **C2:** reconcile M1's two-source excerpt proposal with M3's four-source alternative and S4's R3 scope warning; apply exactly one selected set. Run all 14 fixed-string anchors on delivered text and review full-claim support before claiming 22/22. M5's marker is verified only in scratch; apply/recheck it on the delivered ledger.
- **C3:** reconcile D1/D2/S3/E1 row drafts, correct the six/seven-column inconsistency, then inspect/replay R8–R10 and D3's durable R9 demo if delivered. D1 scratch probes are not a durable in-world fixture or integrated table. Record exact command/output; do not treat a paraphrase as the source's own text or imply a rights/permission decision.
- Keep all verdicts **PENDING-L1** until the delivered tree and independent adjudication are available. Retain any unsupported or absent measurement as named debt; do not award scores or claim admission from proposals.
