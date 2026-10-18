# Fleet round 1 — lore scribe: report contract, SHONEN box states, evidence ledger

**Path discipline.** This file is the lane-internal scribe artifact declared by
`reports/round-1/current-dispatch.json` (`reports/round-1/r1-current-scribe.md`). It is **not** the
contract round report: per `PROTOCOL.md:139-141` that is `.ufo/reports/round-1/<id>.md` with
`<id>` = the roster id `lore` (`MANIFEST.json` roster row: `{"id":"lore","name":"lore-shokunin",
"repo":"shokunin-world-bible"}`), i.e. `.ufo/reports/round-1/lore.md`, which does not exist and is
parent-owned. No placeholder was drafted there.

**Evidence status.** Static inspection only. I ran no checker, fixture, gate, test, build, lint or
formatter; I invoked no runtime probe of the artifact; I ran no `git` history rewrite and made no
commit, push, config, routing or delegation change. Everything below is either (a) an observed
static fact with a pointer, or (b) marked `UNRUN`. Lane references to the parent's probe outputs
are the parent's executions, not mine, and this session does not claim the inherited dispatch
(`reports/round-1/{dispatch.json,critic.md,baseline-probes.json}` and the declaration edits predate
it).

**Authority.** Lane-internal. Every dispatched reviewer here is a subagent of this lane and
therefore still the lane (`PROTOCOL.md:63-66`); nothing in this report is an external verifier, an
admission, a promotion, a canon/truth/rights/mechanics claim, or a verdict on a sibling lane.

---

## 1. Exact report and numeric-evidence requirements (extracted)

**Pointer drift warning (fleet-meta, disclosed):** `PROTOCOL.md` is being edited in the main repo
during this session — `git status` shows `M PROTOCOL.md`, mtime `01:56-03:00`, sha256
`72b51097f5fc6645b2082c0dd874c29c182d5135beb10adcc363e44d83f1d137`, 513 lines (an earlier read in
this same session saw 505 lines and the `SHONEN` seed at 421-428; the seed now sits at 429-436).
Line numbers below are the current ones; the quoted phrase is the stable anchor and must be
re-resolved at closure. This is a live main-repo integrator file; I did not edit it.

| # | Requirement | Canonical pointer (phrase anchors) |
|---|---|---|
| R1 | Report path/filename `.ufo/reports/round-<N>/<id>.md` in the main repo; `<id>` is the roster id; "a report under any other name does not satisfy the contract" | `PROTOCOL.md:137` ("Every dispatched lane writes its report at") |
| R2 | Minimum content: work performed + evidence pointers; **changes landed in the child repo, each tied to a `LOG.md` entry**; cross-domain evidence with its domain; a `SHONEN` heading with one line per box (`[x]`/`[ ]`/`[~]` + pointer); `[~]` means asserted-by-author, not skipped | `PROTOCOL.md:143-152` ("Minimum content:") |
| R3 | Driver completion check validates content, not existence: `SHONEN` heading + one mark per box **and** minimum substance **and a checkable commit-hash citation**; a contentless marker closes nothing | `PROTOCOL.md:174-181` ("A file at the report path is not automatically a report") |
| R4 | Report **lands last**: written only after the child-repo work is committed; it must cite that commit's hash; the hash must exist in the repo and be an ancestor of `HEAD` at closure (`git merge-base --is-ancestor`); uncommitted report ≠ landed | `PROTOCOL.md:116-121` ("A lane report **lands last**") |
| R5 | `[x]` only from a named non-author verifier; a subagent the lane dispatched is still the lane; `[x]` with no named non-author verifier counts as `[~]`; box minimums (box 1: ≥1 decision table + error-pattern list + checklist, each citing a resolvable source; box 2: an end-to-end task executed and logged; box 3: `SKILL.md`/`corpus/` instructions self-contained with resolvable pointers; box 4: no cross-domain bleed, `PROVINCE.md` accurate) | `PROTOCOL.md:63-72` ("**shonen → shokunin.**") |
| R6 | `SHONEN.md` mechanical form: seed block byte-identical modulo `<name>`, marks confined to the box character plus one indented evidence line per box; no added/removed boxes or other prose | `PROTOCOL.md:421` (file-contract `SHONEN.md` row) |
| R7 | Every score is a claim: axis 0–10 → evidence pointer → last-change round, **with the counting command and the commit it was measured against**; SCORECARD also carries `planned` + `retired` | `PROTOCOL.md:424` ("Every score is a claim"), `:492` ("An axis-move inherits the evidence standard"); `AXES.md` §SCORECARD contract |
| R8 | Stale-lane duty: a dispatched lane's report must list any mission open >2 driver ticks (age from launch timestamp) and say *progressing* / *silent* / `progressing-weak` | `PROTOCOL.md:156-168` ("every dispatched lane's report must list any mission") |
| R9 | Gate naming: fleet gate verdicts are `0` clean / `1` failed, and "closure grades no gate conformant until its registry row exists in the lane's own `SKILL.md`" | `PROTOCOL.md:364` ("- **Verdict.**"), `:407` ("closure grades no gate conformant") |
| R10 | Child-lane items the dispatched prompt must carry verbatim: report path/filename; commit-before-report ordering; `SHONEN` heading rule; commit-hash citation rule; the lane's write scope | `PROTOCOL.md:99-104` ("five child-lane items"); fidelity check `:217-220` |

## 2. `SHONEN` — one line per box, justified possible state

Lane `SHONEN.md` currently carries four canonical boxes (2 marked `[~]`, 2 `[ ]`). Static check of
R6: head lines and all four box texts are byte-equal to the canonical seed at `PROTOCOL.md:429-436`
modulo `<name>` = `lore-shokunin`; the only deltas are the mark characters and one indented evidence
line under each `[~]` box — permitted form. (The inherited uncommitted edit replaced a non-canonical
`# SHONEN — probation` variant; see D1.)

- `[ ] SKILL.md contains real decision tables, error patterns, checklists, cited sources` — **`[ ]` is the only defensible state; `[~]` is not available as written.** `SKILL.md` does not exist in the lane repo (`git ls-files` lists only `LOG.md`, `PROVINCE.md`, `README.md`, `SCORECARD.md`, `SHONEN.md`, `l0-questions.md` at root; no `SKILL.md`, no `AGENTS.md`), and the lane `README.md:10-11` declares that absence ("absent on lanes still in shonen seed form — see `corpus/`"). The *substance* named by the box does statically exist elsewhere: `corpus/knowledge/2026-10-12-lore-decision-table.md` (26,630 B, rows carrying fixture paths + external citations), `corpus/knowledge/2026-10-12-malformed-error-patterns.md` (2,729 B), `corpus/knowledge/2026-10-12-lore-consistency-checklist.md` (515 B, a mint backlog not an executable checklist). Box text names `SKILL.md`, so a `[~]` assertion there would point at a non-resolvable path. Possible states: `[ ]` now; `[~]` only after `SKILL.md` exists and the lane asserts it.
- `[~] At least one end-to-end domain task executed and logged in LOG.md` — **`[~]` justified; `[x]` impossible this round.** Pointer resolves: `LOG.md:1574` "Fleet round 1 — calibration declaration before batched dispatch" exists (head of the new 57-line LOG append, `git diff --stat`) and `reports/round-1/baseline-probes.json` exists (untracked, 1,164 B). The LOG entry itself attributes the five CLI results to the parent and states "Lane assertion, not external promotion verification." A `[x]` requires a named non-author verifier; per R5 every dispatched reviewer is this lane, so any `[x]` here would be author attestation counting as `[~]`.
- `[ ] Instructions executable by an agent without oral context` — **`[ ]` is required; the box is not yet satisfiable.** No `SKILL.md`, and the `corpus/` instruction surface has a concrete resolvable-pointer defect: `corpus/fixtures/README.md:6-7` and `corpus/knowledge/2026-10-12-malformed-error-patterns.md:6` still document `python3 .shokunin/lore/corpus/fixtures/check_bible.py ...`, but `.shokunin/` does not exist in the lane repo or at the fleet root — the documented prefix is un-resolvable from this standalone lane root. The working form is the root-relative one used by `reports/round-1/current-baseline.json` (`corpus/fixtures/check_bible.py ...`). Content-wise the knowledge files are self-contained and cite resolvable sources (`fixtures/...` paths; W3C PROV-O, JSON Schema, Python `graphlib`), and the *newly landed* `corpus/fixtures/check_bible.py` additions are code, not documentation.
- `[~] No cross-domain bleed (PROVINCE.md still accurate)` — **`[~]` justified, with one adjacent-surface caveat.** `PROVINCE.md:3-11` is accurate as a boundary statement, and its write-surface line was corrected this round from `.shokunin/lore/**` to `lore-shokunin/` + its own fleet round report + allowed append-only L0 questions (`git diff -- PROVINCE.md`, +1/−1). Every write in this session's worktree is inside the lane repo or the lane's `reports/round-1/` path; the main-repo path the lane may write (`.ufo/reports/round-1/lore.md`) resolves as a directory. Caveat: the lane `README.md:12-14` declares `corpus/QUALITY.md` and `corpus/lessons/`, and neither resolves (`corpus/` = `README.md`, `fixtures/`, `knowledge/`, `live/`) — a declared-surface defect on an adjacent lane file, not cross-domain bleed. Two historical cross-domain items remain routed outside this round: `l0-questions.md` round-4 (duplicate-display-name decision) and round-81 (Git identity / unauthorized-push incident assigned to a fleet coordination lane).

## 3. Acceptance checklist for the contract report (`.ufo/reports/round-1/lore.md`)

Each item states its pass condition and the exact re-derivation; `UNRUN` marks items no static
inspection of this session can settle.

1. **Path/filename** `.ufo/reports/round-1/lore.md`, id `lore` (R1). Static: absent today; `ls .ufo/reports/round-1/` shows the pre-existing fleet-round files and no `lore.md`.
2. **`SHONEN` heading** matching `^#{1,6} *SHONEN` with exactly four box lines, one per seeded box, each mark carrying a pointer (R2, R3, R6, R10).
3. **Work performed** as one bullet per item, each with a path/command/hash pointer (R2).
4. **Landed changes each tied to a `LOG.md` entry and to the commit that carries it** (R2, R4). Currently **UNMET**: `git status --porcelain` = `M LOG.md`, `M PROVINCE.md`, `M SCORECARD.md`, `M SHONEN.md`, `M corpus/fixtures/check_bible.py` plus untracked `reports/round-1/*`; `HEAD` = `5eb9451baff217c19d5786405f9b2aa500b7c1b7` (baseline). No commit is permitted in this session, so a work hash cannot exist until the parent integrates.
5. **Checkable commit-hash citation** (R3, R4). The only hash citable today is the baseline pin `5eb9451baff217c19d5786405f9b2aa500b7c1b7`, and it must be labelled as the *baseline*, not as the round's work commit (see §4).
6. **Cross-domain evidence section** naming the domain each item belongs to (R2) — candidates: fleet-meta (prompt placeholder, dispatch/ledger process), coherence with the already-routed round-81 L0 incident.
7. **Stale-lane line** (R8) if the driver treats this round as driver-dispatched. Observed static driver evidence, not a lane action: `.ufo/prompts/lore-round-1.md` exists; `.ufo/state/lore.round` = `1`; `.ufo/state/lore.mission` = `2684656`; `.ufo/watchdog.log` records `launch lore round=1 pid=2651196` at `01:45:42-03:00`, `lane-dead-no-report lore round=1; retry same round` at `01:50:57-03:00`, and `launch lore round=1 pid=2684656` at `01:50:57-03:00`. Age must come from launch timestamps, not the tick counter (`PROTOCOL.md:153-158`; appendix "Stale-lane actuator").
8. **Before → after measurement per claim** with counting command and measured commit (R7) — see §4; the before/after numbers are `UNRUN` here.
9. **Axis scores preserved as `unmeasured`** for depth/coverage/calibration, with the sample metric in a distinctly labelled column (R7).
10. **No placeholder tokens** anywhere (no `LANE_HASH`-class text): appendix rows "Orphaned report" and metric M20 (`placeholder=1`, `round-12/kotoba.md:224`).
11. **Gate-vs-measurement naming** (R9): if the new artifact is presented as a "gate", R9's registry-row-in-`SKILL.md` condition cannot be met (no `SKILL.md`), so it must be reported as a measurement/sample, not a registered gate.
12. **Declaration fidelity** of the dispatched prompt (R10 / `PROTOCOL.md:216-220`) — see D3.

## 4. Unmeasured scores and commit self-reference — explicit handling

- **Three owned axes stay `unmeasured`.** `SCORECARD.md:3-5` states scores are unassigned without a rubric and that row counts/exit codes are measurements, not scores; the inherited rows for depth (r43), coverage (r39), calibration (r83) remain `unmeasured`, and the fleet-round-1 section records the unresolved tie plus the calibration falsifiability tie-break (`SCORECARD.md` "Fleet round 1" section). Handling: do not assign `0`, do not copy the sample ceiling into an axis row, do not rank the three numerically. The five-check sample is a separate labelled metric with `total=5`, `score = 2 × passed`, and its own `measured_revision`.
- **Rubric before number.** The lane's own plan text requires a bounded, reproducible 0–10 rubric "before recording new numeric scores" and forbids calling a sample ceiling whole-domain saturation. Handling: record the sample as `passed/total` and `score`, labelled a targeted disclosure sample — not whole-domain calibration, expertise, admission, coverage, or saturation.
- **`measured_revision` semantics.** The measurement entry point must test checker **and** input data from the requested git revision in isolated temporary trees; the revision label must describe the inputs actually tested (shared interface; inherited critic `:…` §"6 → 10" and its warnings against running a worktree checker while naming an old commit). Handling: two distinct revisions must appear — baseline `5eb9451baff217c19d5786405f9b2aa500b7c1b7` (which backs the five recorded r85 outputs) and the **post-fix revision that does not exist yet**. `--revision 5eb9451b...` measures the *old* checker; the default/worktree mode measures the *new* dirty-tree checker. Both numbers must say which mode produced them.
- **The r85 five probe runs are not the five sample checks.** `reports/round-1/current-baseline.json` and `baseline-probes.json` hold the same five `corpus/live/runs/round-85/probe-inputs/*` CLI tuples (static JSON compare: `measured_commit`, `command_template` and the `runs` array all equal; return codes `0,1,1,1,1`; all `stderr` empty; the only key difference is an extra `cwd` in `baseline-probes.json`). Those cases exercise clean/unique-break and two ambiguity directions already; they do not execute the sample's dangling-holder-explicitness, ambiguous-to-with-scope, or ambiguous-from checks, and the five probe inputs are telemetry outside `corpus/fixtures/` (133 fixture directories exist there — static count). Relabelling the old five outputs as the five sample checks is a defect, not a measurement. Both revisions' sample scores are therefore `UNRUN`.
- **Commit self-reference.** R4/R3 require a checkable commit-hash citation, and the cited hash must be the lane repo `HEAD` at the moment the report is written. Consequences to honor: (i) the hash that *adds* the fleet report cannot be cited inside that report; (ii) the parent-owned integration hash must never be pre-filled or guessed; (iii) the round-work hash is unavailable in this session because commits are forbidden — the report must cite the baseline pin for baseline evidence and mark the round-work/measured-after hash as **pending parent integration**, never as a placeholder (`LANE_HASH`-class text is a recorded defect form). Ancestry (`git merge-base --is-ancestor <hash> HEAD`) is `UNRUN` for any work hash, since no work hash exists.

## 5. Inherited declaration / publishing defects (disclosed verbatim, not fixed here)

- **D1 — `SHONEN.md` inherited form was non-canonical.** The pre-edit tracked file began `# SHONEN — probation` with four bare boxes plus extra prose. The inherited uncommitted edit regenerated the canonical seed; it is now byte-equal modulo `<name>` with marks confined to box character + one indented evidence line (static check, §2). Uncommitted.
- **D2 — two dispatch declarations coexist, with different artifact names and write scopes.** Inherited `dispatch.json` names `reports/round-1/{planner,connector,checker-executor,measurement-executor,documentation-executor,scribe,surface-scout,reviewer,critic}.md` and write scope `corpus/fixtures/measure_holder_calibration.py` / `corpus/knowledge/round-1-holder-assessment.md`; `current-dispatch.json` names `reports/round-1/r1-current-*.md`, `corpus/fixtures/measure_holder_disclosure.py`, `corpus/knowledge/holder-assessment-boundary.md`. The session interface's entry point (`measure_holder_disclosure.py`) matches only `current-dispatch.json`. At read time neither measurement file nor the guide file existed.
- **D3 — driver prompt carries an unsubstituted placeholder.** `.ufo/prompts/lore-round-1.md:1` reads `Working dir: /home/vgpnk/Projects/shokunin/<lore-repo>.` — the template variable was not substituted. The prompt does carry the report path, the `SHONEN` heading rule, the commit-hash citation rule and the marker rule, and it states `commit (round-1) inside your lane repo, then push`; it does not state the lane's write scope as an item (R10 item (v)) and quotes no L2 route map (`PROTOCOL.md:216-220` requires any quoted map to match the current `MISSION.md` bucket).
- **D4 — two baseline artifacts for one measurement.** `baseline-probes.json` (with `cwd`) and `current-baseline.json` (without) hold identical `measured_commit`, `command_template` and `runs`; the report must name one as canonical to avoid two provenance claims.
- **D5 — required lane files absent.** No `SKILL.md` and no `AGENTS.md` (file contract lists both). This blocks box 1 as written, box 3, and R9's gate-registry row.
- **D6 — declared surfaces that do not resolve.** `README.md:12-14` declares `corpus/QUALITY.md` and `corpus/lessons/`; neither exists. `corpus/README.md` declares `live/runs/` evidence for specific rounds — the directory resolves.
- **D7 — uneven command-prefix correction.** `PROVINCE.md` was corrected this round; `corpus/fixtures/README.md:6-7` and `corpus/knowledge/2026-10-12-malformed-error-patterns.md:6` still use the non-resolvable `.shokunin/lore/...` prefix — 86 occurrences of that exact checker path in `corpus/fixtures/README.md` alone (static `grep -c`), spanning its round-1 through round-22 instruction blocks (§2 box 3).
- **D8 — all lane-authored round-1 changes are uncommitted.** `M LOG.md`, `M PROVINCE.md`, `M SCORECARD.md`, `M SHONEN.md`, `M corpus/fixtures/check_bible.py`, and untracked `reports/round-1/*`. Landed-means-committed is unmet; an uncommitted file at the contract report path would still fire the driver's existence signal.
- **D9 — substrate deviation from `MISSION.md` §L2.** `MISSION.md` requires ≥8 L2 subagents in **one batched AgentSwarm call** (Kimi host surface); both dispatch files declare substrate `OMP native task`, `batch_calls`/`observed_batch_calls_this_session` = 1, 9 members, 9 spawned, "not a validated generic UFO same-shape wave", route authority `~/.omp/agent/config.yml:318-332` (operator-owned, unchanged), and `promotion_verifiers: none`. This is a declaration to name in the round notes, not a config edit.
- **D10 — two critic artifacts, one inherited.** `reports/round-1/critic.md` (inherited, 14,397 B) and `reports/round-1/r1-current-critic.md` (this session, 14,406 B) both exist; their authority must not be merged, and the inherited one predates this session.
- **D11 — two L0 files.** The lane repo tracks `l0-questions.md` (2 historical lines: round-4, round-81) while the dispatched prompt names `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md`. Neither was modified this session.
- **D12 — roster id vs remote/directory name.** The `lore` roster row's `repo` field is `shokunin-world-bible` (matching `git remote -v`), while the directory is `lore-shokunin/`; the report-path id remains `lore`.
- **D13 — driver recorded a dead first mission.** `lane-dead-no-report lore round=1; retry same round` at `01:50:57-03:00` after the `01:45:42-03:00` launch; the fleet report's §Dispatch digest must record that retry with its timestamp, and per R8 the lane must state *progressing* (write-scope files modified since the retry launch) rather than *silent*.
- **D14 — the canonical protocol file moved under this round.** `PROTOCOL.md` is `M` in the main repo, mtime `01:56-03:00`, sha256 `72b51097f5fc6645b2082c0dd874c29c182d5135beb10adcc363e44d83f1d137`, 513 lines; an earlier read inside this same session saw 505 lines with the `SHONEN` seed at 421-428 (now 429-436). Line citations into it — including this report's §1 pointers — must be re-anchored by quoted phrase at closure, and the integration commit must not treat any single line number as stable.

## 6. Evidence ledger — observed vs unrun

| Item | Status | Pointer / exact basis |
|---|---|---|
| Baseline revision pin | observed | `git rev-parse HEAD` → `5eb9451baff217c19d5786405f9b2aa500b7c1b7` |
| Dirty worktree, 5 modified + 9 untracked paths (excluding this file) at `01:58-03:00`; peers still landing | observed | `git status --porcelain --untracked-files=all` |
| Five r85 baseline tuples recorded (rc `0,1,1,1,1`, stderr empty) | observed (recorded evidence, not my run) | `reports/round-1/baseline-probes.json`; `current-baseline.json`; equal on static JSON compare |
| Masked-ambiguous output = only `duplicate entities id 'vault'` | observed (recorded evidence) | `current-baseline.json` runs[2]; mechanism pointer `corpus/fixtures/check_bible.py` chain gate |
| Checker now voices both ambiguous holder fields | observed (static diff) | `git diff -- corpus/fixtures/check_bible.py` (+9/−0): `:218` `to_holder: ambiguous entity`, `:228` `from_holder: ambiguous entity`, `:185` per-item `holder_ambiguity_notice_emitted = False` (inside the `for location, item in data['entities']` loop, so one notice per item), notice emitted at the first ambiguous-holder record (`:231-233`, before the source-id check and before `if not valid: continue`, and independent of `can_check_chain`); file sha256 `e8f241623aa84eb1dce192a03c9e70b8f4ba386344f0b22a99ba1ac0d4942132` |
| Old diagnostics / exit behavior / comparison state machine preserved | observed (static diff: additions only, no deletions) | same diff; the `valid = False` / `can_check_chain = False` latch lines are unchanged |
| `SHONEN.md` canonical form (head + 4 box texts modulo `<name>`) | observed (static text compare vs `PROTOCOL.md:429-436`) | §2 |
| `SKILL.md`, `AGENTS.md`, `corpus/QUALITY.md`, `corpus/lessons/`, `.shokunin/` absent | observed (static existence checks) | §2, D5, D6 |
| 133 fixture directories | observed (static count of `corpus/fixtures/*/`) | D-section / §4 |
| Measurement script `measure_holder_disclosure.py` absent | observed at read time (`01:56`-`01:58` local) | `ls corpus/fixtures/measure_holder_disclosure.py` → no such file |
| Guide artifact `corpus/knowledge/holder-assessment-boundary.md` absent | observed at read time (`01:58`) | `ls` → no such file |
| Driver dispatch/retry timeline for lore round 1 | observed (log lines, not lane action) | `.ufo/watchdog.log:339,369,370`; `.ufo/state/lore.round`, `lore.mission`, `lore.out`; `.ufo/prompts/lore-round-1.md` |
| Any checker invocation (five r85 cases; 133 fixture triples; any sample check) | **UNRUN** (forbidden this session) | — |
| Five-check sample score on baseline and on the fixed tree | **UNRUN** | §4; no script exists yet |
| `--revision` vs worktree measurement mode distinction | **UNRUN** | §4 |
| `git merge-base --is-ancestor <work-hash> HEAD` | **UNRUN** | no work hash exists (D8) |
| Driver content check / contract-report acceptance at `.ufo/reports/round-1/lore.md` | **UNRUN**; report not written (parent-owned) | §3 |

## 7. Out of scope for this artifact

Writing or amending `LOG.md`, `SCORECARD.md`, `SHONEN.md`, `PROVINCE.md`, `check_bible.py`, the
measurement script, the guide note, the fleet report, indexes, `MANIFEST.json`, L0 files, prompts or
any other lane's files; any commit, push, merge, route/config edit, new delegation, or runtime
probe; any promotion, admission, or external-verifier claim; any assertion of canon, truth, rights,
or game mechanics. The fixture and corpus records referenced above are authored fictional data and
are unverified as sources; a structural `CLEAN`/violation result is not evidence about them.