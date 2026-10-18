# V18 — scope creep (round 100)

Axes: scope/adjacency, report exclusivity and roster fidelity, parent-tree cleanliness, and scratch operability. This is a filesystem/process-boundary report, not a C1/C2/C3 admission or semantic verdict. The production-path audit passes; the delivered seat count contradicts the 32-seat declaration.

Baseline: `fe1ce466e9d7427948c0abe4ecfbf961880b72ff`. Observed HEAD: `b5fe472957ab1e4e9c90f5613acc14cd24a288ae`; the wave is uncommitted. Unless explicitly disclosed below, shell audits ran from `/home/vgpnk/Projects/shokunin/lore-shokunin`, and Python used `python3`.

## V18 writes and reproducibility

Only these two absolute paths were created by V18:

- `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V18-scope-creep.md`
- `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V18-scope-creep-scratch/audit.py`

The declared scratch directory is the latter file's parent. Destinations were resolved/asserted under the lane before each Write. The helper is read-only when executed. No production file, another seat's report/scratch, parent file, commit, push, network operation, or nested agent was written/performed by V18. No needed background task remains.

Actual principal audit command, executed successfully several times, including the final pre-report snapshot:

```sh
python3 /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V18-scope-creep-scratch/audit.py
```

Observed final pre-report interval: `2026-10-18T02:46:52.524116+00:00`–`02:46:52.634975+00:00`, exit 0. The command prints the complete non-scratch status rows, scratch groups, report hashes, exclusivity findings, scratch sizes, and parent findings. Measurements below refer to that bounded snapshot unless another timestamp is given; later landings must not be silently attributed to it.

## 1. Poll and concrete roster/count contradiction

The producer/readiness check required all 16 declared artifact paths, nonempty T1/T2/T3/T4 reports, and the r99 contract pin. The all-reports condition subtracted SELF V18. The first four 20-second checks mistakenly constructed a contiguous V1–V28 expected set; observed V29/V30 scratch identifiers disproved that assumption. That poll was cancelled, its four attempts retained, and attempts 5–40 used unique non-self report counts rather than invented verifier IDs. No completion was credited from the mistaken roster.

The corrected actual `python3 -u - <<'PY'` poll used this report-count logic:

```python
for attempt in range(5, 41):
    reports = {}
    for p in seats.iterdir():
        if p.is_file() and p.suffix == '.md':
            m = re.fullmatch(r'([TV])0*(\d+)-.+\.md', p.name)
            if m and p.stat().st_size:
                reports.setdefault(m.group(1) + str(int(m.group(2))), []).append(p.name)
    others = set(reports) - {'V18'}
    missing_producers = sorted({'T1', 'T2', 'T3', 'T4'} - set(reports))
    # The executed poll also checked each of the 16 actual artifact paths and r99 pin.
    if len(others) >= 31 and not missing_artifacts and not missing_producers and r99_pin:
        break
    if attempt < 40:
        time.sleep(20)
```

Observed milestone output, excerpted without claiming the omitted report lists are absent:

```text
2026-10-18T02:40:17.516012+00:00 TRY 24/40 OTHER_REPORTS 14/31 SELF V18 SUBTRACTED PRODUCERS_MISSING [] ARTIFACTS_MISSING [] R99_PIN True DUPLICATES {}
2026-10-18T02:45:37.527897+00:00 TRY 40/40 OTHER_REPORTS 31/31 SELF V18 SUBTRACTED PRODUCERS_MISSING [] ARTIFACTS_MISSING [] R99_PIN True DUPLICATES {}
ALL_OTHER_SEATS_AND_ARTIFACTS_PRESENT
```

The poll exited 0. It reached the declared numerical threshold on attempt 40: no timeout/stall escape, no producer absence, and no absent-as-present artifact credit. The last success label is **only a count-threshold statement**, not a proven dispatch-roster reconciliation.

The subsequent independent namespace/count command was:

```sh
python3 - <<'PY'
from pathlib import Path
from datetime import datetime, timezone
import re
r = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
s = r / '.ufo/waves/round-100/seats'
reports = {}
namespaces = {}
for p in sorted(s.iterdir()):
    m = re.match(r'^([TV])0*(\d+)-', p.name)
    if not m:
        continue
    seat = m[1] + str(int(m[2]))
    namespaces.setdefault(seat, []).append(p.name)
    if p.is_file() and p.suffix == '.md':
        reports.setdefault(seat, []).append(p.name)
print('UTC', datetime.now(timezone.utc).isoformat())
print('TOP_LEVEL_REPORT_COUNT', sum(len(v) for v in reports.values()))
print('UNIQUE_REPORTED_SEATS', len(reports))
print('UNIQUE_REPORT_OR_SCRATCH_NAMESPACES', len(namespaces))
print('NAMESPACES_WITHOUT_REPORT', {k: v for k, v in namespaces.items() if k not in reports})
PY
```

Observed at `2026-10-18T02:46:30.293138+00:00`, before this report existed:

```text
TOP_LEVEL_REPORT_COUNT 32
UNIQUE_REPORTED_SEATS 32
UNIQUE_REPORT_OR_SCRATCH_NAMESPACES 34
NAMESPACES_WITHOUT_REPORT {'V18': ['V18-scope-creep-scratch'], 'V29': ['V29-scratch']}
```

The 32 delivered identifiers were **T1–T4, V01–V17, V19–V28, and V30**. V24's actual late landing was `.ufo/waves/round-100/seats/V24-verdict-depth.md` (35,631 bytes; SHA-256 `698fcc54704e9e41faa07f45bdefe60a1f603cc3b61f31f47827a3628a6f7209`). It raised the unique non-self count from 31 to 32. The full audit independently confirmed `OTHER_REPORT_SEATS_SELF_V18_SUBTRACTED 32` at `02:46:52`.

Thus landing this V18 report makes **at least 33** unique reports, not the declared 32. This is not duplicate-prefix inflation. Additionally, `V29-scratch/poll_reports.py:8` explicitly identifies `self_id = 'V29'`, and `V29-scratch/delivery-evidence.json` exists; V29 had no top-level report at the snapshot. Scratch is not credited as a report, and V29's verdict is not inferred. There are 34 observed report-or-scratch seat namespaces, not a proven 34-agent dispatch result.

**L1 action:** reconcile the actual dispatch result/agent IDs with all delivered report identifiers; correct the declared seat total or explain excluded/extra seats explicitly; then refresh receipt/report hashes after the last landing. Do not label a 32-count threshold “all seats” solely by cardinality. No report was deleted, overwritten, or reclassified by V18 to force the count to match.

## 2. Bucketed `git status --porcelain -uall`

The helper actually executed:

```sh
git status --porcelain=v1 -uall
git diff --cached --name-status
git diff fe1ce46 HEAD --name-status
```

Observed raw-status SHA-256: `885a9aafa748ac58bf72eb69403a09600314ae95c7cbc2574b254f15562b737c`. The index diff was empty. Before V18 report creation there were **2,272** status paths:

- **T1 production: 3** — modified `SKILL.md`, `corpus/tools/README.md`, `corpus/tools/dependency-freeze-contract.json`.
- **T2 production: 8** — untracked r100 fixture `contradictions.json`, `entities.json`, `fictional-excerpts.md`, `inspiration-note.md`, `relations.json`, `source-excerpt.md`, `sources.json`, `timeline.json`.
- **T3 production: 2** — untracked r100 fixture `README.md`, `claim-excerpt-map.md`.
- **T4 production: 3** — modified `corpus/knowledge/r99-gate-blind-spot-table.md`; untracked `r100-crossing-arc-synthesis.md` and `r100-provenance-semantics-boundary.md`.
- **Round-100 seat reports: 32** — the identifiers listed above; all top-level regular Markdown files.
- **Round-100 per-seat scratch: 2,223** — grouped under `seats/<seat>-…/` and the declared `scratch/V08-c2-anchors/`, `scratch/V19-freshness/` namespaces.
- **Pre-existing out-of-round untracked note: 1** — `.ufo/waves/round-98/seats/V58-scratch/original-run-resume-note.md`; already present in the initial status before r100 files/reports landed. It is not attributed to this wave and was not removed.
- **Outside declared production/report/scratch ownership: 0**.

The production scope is exactly 16 paths: four tracked changes and twelve new fixture/knowledge files. T2's initialization of all ten baseline fixture copies, followed by T3's exclusive edits to README/map, is the declared handoff, not an extra producer path.

`git diff fe1ce46 HEAD --name-status` showed only `LOG.md` and `SCORECARD.md`. Actual attribution command:

```sh
git log --oneline fe1ce46..HEAD
git log --oneline fe1ce46..HEAD -- SCORECARD.md
```

Observed:

```text
b5fe472 lore r100: declare sol-max 32-seat round before dispatch
ae67105 lore r99: close round — SCORECARD admitted section
SCORECARD attribution: ae67105 lore r99: close round — SCORECARD admitted section
```

LOG is the pre-dispatch declaration; SCORECARD is the earlier r99 closure-bookkeeping commit. They are not uncommitted wave-seat writes. An earlier progress note grouped both as declaration bookkeeping; this exact attribution supersedes that simplification.

A parsed comparison of the live freeze contract with `git show fe1ce46:corpus/tools/dependency-freeze-contract.json` actually observed:

```text
CONTRACT_TOP_LEVEL_ADDED []
CONTRACT_TOP_LEVEL_REMOVED []
CONTRACT_NON_PIN_FIELDS_CHANGED ['revision']
PIN_NAMES_ADDED ['r99-window-lapse']
PIN_NAMES_REMOVED []
OLD_PINS_CHANGED []
```

The disclosed guard-managed revision refresh is not concealed as a literally addition-only text diff. V18 did not invoke `--freeze` or certify execution provenance solely from a JSON comparison.

## 3. Report exclusivity — filesystem pass, roster failure

Observed full-audit output:

```text
UNIQUE_REPORT_SEATS 32
OTHER_REPORT_SEATS_SELF_V18_SUBTRACTED 32
PRODUCER_MISSING []
DUPLICATE_REPORT_PREFIXES {}
UNEXPECTED_REPORT_FILENAMES []
EMPTY_REPORTS []
REPORT_LINK_ANOMALIES []
REPORT_HEADER_MISMATCHES []
```

Each observed report had one unique normalized prefix, a nonempty payload, a consistent explicit header identifier, one regular-file link, and no symlink. A separate whole-wave symlink walk found `WAVE_SYMLINKS []`. These are filesystem exclusivity observations, not proof of which process wrote each byte or a substitute for real dispatch/agent IDs. The total-count failure in section 1 remains.

## 4. Parent-tree strays — zero observed

The helper ran parent Git status through `subprocess` while the shell stayed in the lane, and metadata-walked the parent outside every `*-shokunin` lane and `.git`, since the declaration's timestamp `2026-10-18T02:30:55+00:00`.

Actual status command inside that explicit parent subprocess:

```sh
git status --porcelain=v1 -uall
```

Observed final output:

```text
(empty)
PARENT_STATUS_PATHS 0
PARENT_WRONG_CWD_ROUND100_EXISTS False
PARENT_WRONG_CWD_CORPUS_EXISTS False
PARENT_WRONG_CWD_SKILL_EXISTS False
RECENT_PARENT_FILES_OUTSIDE_ALL_LANES_SINCE_DECLARATION []
PARENT_SCRATCH_ENTRIES []
```

No parent `.ufo/waves/round-100`, parent `corpus`, parent `SKILL.md`, or parent `.scratch` residue was found. This is a bounded on-disk observation, not process tracing of deleted temporaries or a claim to audit independent sibling-lane work.

A separate lane metadata sweep outside this wave found exactly **17** recent files: LOG plus the 16 declared producer artifact paths. Passing those paths through actual `git check-ignore --stdin` returned stdout `''`, exit **1** (the normal no-matches result): `RECENT_IGNORED_FILES_OUTSIDE_WAVE []`. No recent ignored cache or root self-test residue was observed outside the wave; interactive-session storage and `.git` were excluded explicitly.

## 5. Scratch size — no oversized scratch to flag

The helper walks all round-100 per-seat scratch, including ignored files. Local audit flag thresholds were **file >=10 MiB** or **per-seat scratch directory >=50 MiB**; these are disclosed screening thresholds, not invented project admission rules.

Observed:

```text
SCRATCH_TOTAL_FILES 2225
SCRATCH_TOTAL_LOGICAL_BYTES 17741594
SCRATCH_FILES_GE_10MiB []
```

No scratch directory met 50 MiB. Largest directories:

- `seats/V03-scratch`: **7,667,582 bytes / 1,015 files**.
- `seats/V16-scratch`: **2,879,630 bytes / 341 files**.
- `seats/V28-scratch`: **1,551,606 bytes / 155 files**.

Largest file: `seats/V03-scratch/results.json`, **169,239 bytes**. The difference between 2,223 status-listed scratch paths and 2,225 on-disk scratch files is two ignored files inside scratch, not out-of-wave leakage. No 100–300 MB archive class was present. L1 may retain or prune scratch by policy; V18 removed nothing.

## 6. Protected bytes, validation, and diagnostic exceptions

Actual final preservation command, run through `python3`/`subprocess` from the lane:

```sh
git diff --exit-code fe1ce46 -- PROVINCE.md SHONEN.md corpus/fixtures/check_bible.py corpus/tools/dependency_freeze.py corpus/tools/support_check.py corpus/tools/map_obligations.py corpus/tools/boundary_doc_check.py
```

Observed stdout `''`, stderr `''`, exit **0**. All seven protected paths were also directly SHA-256 compared against `git show fe1ce46:<path>` earlier and were byte-identical. Actual `git diff --check` likewise produced stdout `''`, stderr `''`, exit **0**; it does not validate untracked Markdown whitespace. The r100 fixture contained exactly its ten declared filenames and no extra file or symlink. No build/test run or C1/C2/C3 semantic result is claimed by this seat; the delivered V18 executable audit itself ran successfully on the actual wave.

Diagnostic failures/deviations are retained rather than hidden:

- Initial `ls -la "/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats"` exited **2**, `No such file or directory`, before the producers created the directory. No report/artifact was credited from this probe.
- One premature guessed Read of `.../seats/T2-fixture-build.md` returned “does not exist.” The actual delivered `T2-fixture-author.md` was subsequently read; the guessed path was not used as evidence.
- The initial four-check contiguous-roster poll was cancelled and corrected as described above, without resetting the cumulative 40-attempt bound.
- Two initial read-only parent-status shell probes used the parent as shell cwd, contrary to the lane-cwd convention. Subsequent parent checks used a lane-root `python3` subprocess with an explicit parent `cwd`. Neither probe wrote any file; all V18 Writes stayed in the two declared absolute paths.

No contrary production-path, parent-stray, protected-byte, or scratch-size result was suppressed. Full dispatch closure remains for L1, because the late report-count overrun is real and a scratch namespace is not a completed report.

## 7. Post-landing deliverable verification

After this report landed, the same actual audit helper was executed again through a lane-root `python3` subprocess. Its result was stdout findings, empty stderr, and exit 0 (successful evidence collection, not a substantive pass verdict). Snapshot: `2026-10-18T02:47:59.121958+00:00`–`02:47:59.235552+00:00`.

Observed output excerpts:

```text
BUCKET T1 production: 3 paths
BUCKET T2 production: 8 paths
BUCKET T3 production: 2 paths
BUCKET T4 production: 3 paths
BUCKET pre-existing round-98 note: 1 paths
BUCKET round-100 seat reports: 33 paths
BUCKET round-100 seat scratch: 2225 paths
TOTAL_STATUS_PATHS 2275
OUTSIDE_OWNERSHIP_COUNT 0
UNIQUE_REPORT_SEATS 33
OTHER_REPORT_SEATS_SELF_V18_SUBTRACTED 32
PRODUCER_MISSING []
DUPLICATE_REPORT_PREFIXES {}
UNEXPECTED_REPORT_FILENAMES []
EMPTY_REPORTS []
REPORT_LINK_ANOMALIES []
REPORT_HEADER_MISMATCHES []
SCRATCH_TOTAL_FILES 2227
SCRATCH_TOTAL_LOGICAL_BYTES 17778023
SCRATCH_FILES_GE_10MiB []
PARENT_STATUS_PATHS 0
RECENT_PARENT_FILES_OUTSIDE_ALL_LANES_SINCE_DECLARATION []
PARENT_SCRATCH_ENTRIES []
AUDIT_STDERR '' AUDIT_EXIT 0
V29_REPORTS []
WAVE_ROOT_FILES []
```

The delivered report's final-line contract was read back by that verification command. Thus **33 reports is now an observed delivered count, not a projection**. V29 remained unreported at this post-landing snapshot. Later V29/receipt landings are for L1 to collect; this report does not invent them or change any other report to force 32. The small scratch-size/count increase belongs to continuing in-wave output; no new production or parent path appeared.

FAIL — 33 unique reports are delivered against the declared 32-seat total, with an additional V29 scratch namespace still unreported; production ownership, parent-stray, protected-byte, and scratch-size checks pass on the delivered snapshot.
