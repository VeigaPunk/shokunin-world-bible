# V36 — shonen-format (round-97 verification seat, lore-shokunin)

**Seat role:** (a) mechanical check of `SHONEN.md` — canonical four-box form, four `[~]`,
zero `[x]` (round-93 form checker replayed, plus an independent seed-block diff against
`PROTOCOL.md`, an independent mark census, evidence-pointer and ancestry resolution, and
three negative controls proving the checker discriminates); (b) enumerate the round-97
fleet-report landing set for L1 (path, sections, evidence bar, commit rules,
round-specific items); (c) poll the round's six producer artifacts and seat landings.
LEAF scope: read-only checks; this report is my only write outside my scratch dir
`.ufo/waves/round-97/seats/V36-scratch/`.

**Revision tested:** lane HEAD `2393934237ea076366f3db6dceeff033edb52ab1` (`2393934 lore
r96: close round — SCORECARD admitted section`; its parent is the brief's baseline
`f3e09f9`). Working tree at open: `git status --short` →

```
 M LOG.md
?? .ufo/waves/round-97/
```

## 1. `SHONEN.md` — canonical, four `[~]`, zero `[x]` (PASS)

Mechanical checker (`.ufo/waves/round-93/deepseek/F29-shonen-format-check.py`) replayed
twice — at seat open and again after all six producer reports and artifacts had landed —
**exit 0, 10/10 PASS** both times (output below is the post-write replay; the pre-write
replay printed the same ten PASS lines and the same three hashes):

```
$ python3 .ufo/waves/round-93/deepseek/F29-shonen-format-check.py
PASS title matches seed modulo <name>
PASS seed frame (blank + manifest line)
PASS four boxes, seed order and text
PASS marks confined to box character
PASS no [x] promotion claim present
PASS at most one evidence line per box
PASS both [~] boxes carry their required pointer
PASS box2 evidence names the LOG.md entry
PASS box2 evidence names reports/round-1/baseline-probes.json
PASS box4 evidence cites PROVINCE.md:3-11 within range
SHA256 SHONEN.md 03b832c75efbf81300e87f6a95713a48b21b00d654c1222aee251a27c103d7d1
SHA256 SKILL.md a2f1e4c6a49bafbf4a14f6b28a45f4e2d9d183d60932321c3757ba35feb8d61a
SHA256 PROVINCE.md 94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa
EXIT=0
```

Mark census (independent of the checker):

```
$ grep -c '^- \[~\]' SHONEN.md   → 4
$ grep -c '^- \[x\]' SHONEN.md   → 0
$ grep -c '^- \[ \]' SHONEN.md   → 0
$ grep -c '^- \[' SHONEN.md      → 4
$ grep -n '\[x\]' SHONEN.md      → no match (grep exit 1)
```

Byte-unchanged against HEAD — `git diff HEAD -- SHONEN.md | wc -l` → `0` — and
`git diff 9c2eea3 -- SHONEN.md | wc -l` → `0`: the file is byte-identical to the r93
commit `9c2eea3` that last touched it, and its digest `03b832c7…` equals the one recorded
by the r94 F28, r95 V30 and r96 V39 seats — no drift across four closures.

**Independent seed-block check (not the checker).** The canonical seed lives in
`PROTOCOL.md:425-433` (indented code block). Stripping the code-block indent and
substituting `<name>` → `lore-shokunin`, the frame lines and the four box texts match the
live file exactly, and the seed's own marks are all `[ ]` (so the live `[~]` marks are the
lane's assertion applied to the box character, as the form requires):

```
frame match: True
box texts match (marks/evidence excluded): True
seed marks all '[ ]': True
  frame 1..3 OK; box 1..4 OK
```

Evidence pointers: every path named in the four evidence lines resolves (13/13 `OK` —
`SKILL.md`, `LOG.md`, `reports/round-1/baseline-probes.json`, `PROVINCE.md`,
`.ufo/waves/round-93/recovery/R08-skill-check.py`,
`.ufo/waves/round-93/deepseek/{F21,F29,F01,F31,F03,F24}.md`,
`.ufo/waves/round-93/deepseek/{F25-replay.py,F14-postrepair-check.py}`), the LOG entry
named in box 2 exists once (`grep -c "Fleet round 1 — calibration declaration before
batched dispatch" LOG.md` → `1`), the `PROVINCE.md:3-11` citation is in range
(`sed -n '3,11p' PROVINCE.md` → owns/refuses/scope text), and the cited commit is real and
an ancestor:

```
$ git cat-file -t 8e5a68d → commit
$ git merge-base --is-ancestor 8e5a68d HEAD → ANCESTOR yes
$ git log --oneline -1 8e5a68d → 8e5a68d lore r93: record DeepSeek review and resolve source precision findings
```

**Negative controls (the PASS is not vacuous).** Sandbox copy of the checker at
`V36-scratch/negctl/a/b/c/d/check.py` (its root resolves to `parents[4]` = the sandbox
dir, with `SHONEN.md`/`LOG.md`/`PROVINCE.md`/`SKILL.md`/`reports/round-1/baseline-probes.json`
copied alongside); three separate tampers, each reverted before the next:

```
NEGCTL-1 first box [~]→[x]        → EXIT=1, FAIL no [x] promotion claim present
NEGCTL-2 box2 evidence line removed → EXIT=1, FAIL both [~] boxes carry their required pointer
NEGCTL-3 fifth box appended        → EXIT=1, FAIL four boxes, seed order and text
```

(Each sandbox run also reports `FAIL title matches seed modulo <name>` — an artifact of the
sandbox directory being named `negctl`, not a live-file defect.)

Governing gate text re-checked: `PROTOCOL.md:63-68` — `[x]` requires a reviewer who did not
author the round's changes, and "a subagent the lane dispatched is still the lane"; the 64
round-97 seats cannot convert any box to `[x]`. `PROTOCOL.md:417` fixes the canonical form
(seed byte-identical modulo `<name>`; marks confined to the box character plus one indented
evidence line per box).

**Digest-drift note (not a defect):** `SKILL.md` hashes `a2f1e4c6…` where the r96 V39 seat
recorded `749b04d1…` at `60dba0c`; carried by the r96 closure commit `f3e09f9`
(`git diff --stat 60dba0c..HEAD -- SKILL.md` → `1 file changed, 14 insertions(+), 3
deletions(-)`). `SHONEN.md` box-1's `SKILL.md` pointer still resolves. `PROVINCE.md`
(`94a7a77e…`) unchanged; `SHONEN.md` itself untouched since r93.

**Verdict:** PASS — four `[~]`, zero `[x]`, form canonical against both the checker and an
independent seed diff, all 13 pointers live, cited hash an ancestor, and the checker
discriminates on three tamper classes.

## 2. Round-97 fleet-report landing set for L1

Authority chain: `templates/round-prompt.md:60-78` (§4 report contract), `:80-86` (§5
commit/push scope), `PROTOCOL.md:100-108` (five child-lane items), `:117-127`
(lands-last + commit-hash citation), `:138-139` (report name = roster id), `:144-153`
(minimum content), `:154-169` (stale-lane actuator), `:175-183` (content check),
`:237-242` (MANIFEST ledger, integrator scope), `:455-479` (commit scope, pathspec rule,
lane identity), `MISSION.md` §Push scope.

### 2.1 Primary artifact — the round report

| Item | Value |
|---|---|
| Path | `/home/vgpnk/Projects/shokunin/.ufo/reports/round-97/lore.md` |
| Repo | fleet repo (`/home/vgpnk/Projects/shokunin`), not the lane repo |
| Name | `<id>` = roster id `lore` (`MANIFEST.json` roster row `{"id": "lore", "name": "lore-shokunin", "rank": "shonen", …}`); any other name does not satisfy the contract (`PROTOCOL.md:138-139`) |
| State at seat open | ABSENT — `ls /home/vgpnk/Projects/shokunin/.ufo/reports/round-97/` → `No such file or directory` (the dir is created only when L1 files the report; lands last) |
| Precedent | r94 `be6eca9`, r95 `07ea34b`, r96 `5e038024` — each authored `lore-shokunin <lore@shokunin.local>`, subject `protocol: close lore rN (admitted) — fleet report + MANIFEST ledger append`; the r96 commit carries the report (82 lines) plus the `MANIFEST.json` rounds append |

### 2.2 Required sections, in order (`templates/round-prompt.md:64-74`)

1. **Work performed** — opens by naming the round's declared claims (r97: C1/calibration,
   C2/coverage, C3/depth — `LOG.md` "## Round 97 — declaration before dispatch
   (2026-10-17)") and their target axes; then one bullet per work item, **each carrying an
   evidence pointer** (path:line, command output, or commit hash).
2. **Landed changes** — every change **tied to a `LOG.md` entry and to the commit hash**
   that carries it.
3. **Before → after measurements** — one per claim, **each with the counting command and
   the commit it was measured against**.
4. **SHONEN** — one line per box of `SHONEN.md`: `[x]` only with a named non-author
   verifier, `[~]` with a resolvable evidence pointer, `[ ]` if untouched. For r97 all four
   lines must be `[~]` (same-lane seats are the lane; no promotion). The heading is
   mandatory — "A report without this heading does not satisfy the contract even if the
   same facts appear elsewhere in it" (`PROTOCOL.md:148-153`).

### 2.3 Evidence requirements (`PROTOCOL.md:144-153`, `:175-183`)

- Work performed **plus at least one evidence pointer**; changes landed in the child repo
  each tied to a `LOG.md` entry; **cross-domain evidence with the domain named**; a
  **checkable commit-hash citation** — the hash must exist in the lane repo and be an
  ancestor of lane `HEAD` (`git merge-base --is-ancestor <hash> HEAD`).
- **Marker rule** (`templates/round-prompt.md:75-78`): a contentless report = round
  **failed**; real committed work but missing sections = `ok` + minimum-content defect.
- **Lands last** (`PROTOCOL.md:117-127`): written only after the lane's child-repo work is
  committed, and it cites that commit's hash.
- **Stale-lane actuator** (`PROTOCOL.md:154-169`): the report must list any mission open
  longer than two driver ticks with `progressing` / `progressing-weak` / `silent` (age from
  the launch timestamp, not the tick counter).
- **Honest defect accounting** (r94–r96 precedent): failed-output gaps, late landings and
  misplaced reports are named, not smoothed.

### 2.4 Commit / push rules for the landing (`templates/round-prompt.md:80-86`, `PROTOCOL.md:455-472`)

- Round end: commit (`round-97`) inside the lane repo, then push; **also commit and push
  the report on the fleet repo**.
- Fleet-repo commit is **pathspec-limited**: `git commit -- .ufo/reports/round-97/lore.md`
  — never `commit -a` / `add -A` (the fleet repo is shared with sibling lanes).
- Main-repo commits cannot rely on `git config`; use
  `git -c user.name=lore-shokunin -c user.email=lore@shokunin.local commit …`
  (`PROTOCOL.md:476-479`).
- Push scope: fleet repo remote + own lane remote only; domain source trees read-only.
- `.ufo/waves/` (seat reports, receipt) is committed with the round's integration commit;
  `.ufo/state/` and `.ufo/watchdog.log` must never be committed by a lane.
- Corrections land as new commits, never by amending a cited one.

### 2.5 Round-97-specific items observed

- **Lane repo work L1 must commit** — producer-owned files (six producers, exclusive
  byte-ownership per the round declaration):
  - R1 `corpus/tools/map_obligations.py` (baseline at `f3e09f9`: `2b0ba815…`)
  - R2 `corpus/tools/map-obligations-contract.json` (baseline `97b76bb8…`) +
    `corpus/tools/README.md` (baseline `ba7d2ff1…`)
  - R3 `corpus/tools/dependency_freeze.py` (baseline `a3b57978…`) +
    `corpus/tools/dependency-freeze-contract.json` (baseline `c65ac3bd…`)
  - R4 `corpus/fixtures/r96-crossing-response/claim-excerpt-map.md` (cosmetic repair only;
    baseline `5093d72e…`) + `corpus/fixtures/r97-crossing-acknowledgment/`
    {entities,relations,contradictions,inspiration-note,source-excerpt} (byte copies of
    POST-REPAIR r96) + {sources,timeline}.json + fictional-excerpts.md
  - R5 `corpus/fixtures/r97-crossing-acknowledgment/README.md` (`d9387b7d…`, 18:49:14) +
    `claim-excerpt-map.md` (`49d4834e…`, 18:48:56) — both rewritten; no longer byte
    copies of r96
  - R6 `corpus/knowledge/r97-acknowledgment-scope-note.md` (`5e3b4225…`, landed 18:52:38;
    ABSENT at seat open)
  plus `LOG.md` (r97 declaration + results entry), `SCORECARD.md` (r97 rows), and
  `.ufo/waves/round-97/` bookkeeping (seat reports + receipt when written).
- **Fleet repo**: only `.ufo/reports/round-97/lore.md` is L1's to write; the
  `MANIFEST.json` `rounds[]` append is the integrator-of-record's act, not L1's
  (`PROTOCOL.md:237-242`).
- **L0**: `.ufo/l0-questions.md` carries `lore | round-1 | …` (line 33) and two kotodama
  questions; no r97 lore question appended at seat open.
- **No fleet prompt file** for this lane-round: `.ufo/prompts/lore-round-1.md` is the only
  `lore*` prompt — same as r93–r96; dispatch evidence rides `LOG.md` + the wave dir.
- **Watch item (carried defect class)**: the watchdog still does not gate this lane —
  `scripts/shokunin-watchdog.sh:14` `LANES="protocol aggregator kasegi kengaku kake
  kumitate kotoba kagi kama"` (no `lore`), `:45` `report_of() { [ -f
  "$SK/.ufo/reports/round-$2/$1.md" ]; }` (existence-only; the only greps are at `:80` and
  `:95` over launch/status output), contrary to `PROTOCOL.md:175-183`. The report content
  bar therefore rests on integrator review.
- **Mislanding watch (r94-F01 class)**: no stray r97 files at the fleet root —
  `find .ufo/waves/round-97 reports -path '*round-97*' -type f` → no output; fleet
  `git status --porcelain` → clean at seat open.

## 3. Poll log — producer artifacts and seat landings

Cadence 20 s, 40 samples, 18:43:03 → 18:56:03 (`POLL DONE 18:56:23`); raw log at
`.ufo/waves/round-97/seats/V36-scratch/poll.log`. Baselines at poll 0 (= r96 closure
`f3e09f9`, all re-verified via `git show f3e09f9:<path> | sha256sum`): R1 `2b0ba815…`,
R2 contract `97b76bb8…` / README `ba7d2ff1…`, R3 tool `a3b57978…` / contract `c65ac3bd…`,
R4 map `5093d72e…`, fixture ABSENT (0 files), R6 ABSENT, 0 seat reports, fleet report
absent.

| Event | Time | Evidence (poll i) |
|---|---|---|
| R4 r96 map repair first non-baseline | 18:43:42 | `r4m=e851f068…`, stable through poll 39 |
| r97 fixture 0 → 10 files | 18:44:23 | `fx=10` (poll 4) |
| R4's three modified files written | 18:44:30 | `ls -l` mtimes: fictional-excerpts.md, sources.json, timeline.json |
| R1 tool first non-baseline | 18:45:03 | `70795150…` (poll 6) → churn `68848885…`, `86b52949…` |
| R1 tool stable | from 18:45:43 | `r1=86b52949…` (poll 8) through poll 39 |
| R2 contract first non-baseline | 18:46:23 | `r2c=2142b991…` (poll 10), stable through poll 39 |
| R2 README first non-baseline | 18:47:23 | `r2r=6278e59b…` (poll 13), stable through poll 39 |
| R5 claim-excerpt-map.md written | 18:48:56 | mtime; first poll after it (i=17) |
| R5 README.md written | 18:49:14 | mtime |
| R3 tool first non-baseline | 18:51:43 | `fbaca38f…` (poll 26) → `7428dad4…`, `61cee7e5…` |
| R6 note first write | 18:51:43 | `56981af5…` (poll 26) → `1a9a5f91…`, `7a21948e…` |
| R3 tool stable | from 18:53:23 | `r3t=b06275f3…` (poll 31) through poll 39 |
| R3 contract first non-baseline | 18:53:23 | `8015e1f9…` (poll 31) → `625ccfac…`, `27273be2…` (poll 37+) |
| R6 note stable | from 18:52:43 | `r6=5e3b4225…` (poll 29) through poll 39 |
| Producer reports (R2, R4, R5, R1, R6, R3) | 18:49:31 → 18:56:23 | `ls -l` mtimes; `prods` 0→5 by poll 39, 6th (R3) landed 20 s after the last sample |
| Seat reports | 0 → 31 | first at 18:47:43 (poll 14); 37 `.md` incl. producers + this seat at final check 18:57 |

Final digests at 18:57:15 (`sha256sum`, full):

```
86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9  corpus/tools/map_obligations.py
2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41  corpus/tools/map-obligations-contract.json
6278e59b8df01c1cb63ca6080cb959999f400d95128b96e84e5476f4c4ebb992  corpus/tools/README.md
b06275f3bbdeabaab615138b3004703fce701a786af882d3b732828b37722130  corpus/tools/dependency_freeze.py
27273be27d33ad864f06d656f28dca8eabc9d76f6ebe62583372a88c9e64e781  corpus/tools/dependency-freeze-contract.json
e851f068cfd7ed02c97054df18729c4c5a9b8bf60d99d7c9116f427d765440de  corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
5e3b4225c30de8a2a75b675b59acb5c597b290e5a45f2caa01663da586e042b5  corpus/knowledge/r97-acknowledgment-scope-note.md
```

Fixture at cutoff: 10 files; `diff -rq corpus/fixtures/r96-crossing-response
corpus/fixtures/r97-crossing-acknowledgment` lists exactly the five declared
modifications (`claim-excerpt-map.md`, `fictional-excerpts.md`, `README.md`,
`sources.json`, `timeline.json`) and no other difference — the five byte-copy files
(entities, relations, contradictions, inspiration-note, source-excerpt) are byte-identical;
`entities.json` hashes `026af0bc…`, the value the r96 receipt pinned. Caveat: R3's freeze
contract was still moving at poll 37–39 (`27273be2…`, mtime 18:55:14) — it may not be the
producer's final revision; the round is open at this cutoff, which is expected.

Fleet report `/home/vgpnk/Projects/shokunin/.ufo/reports/round-97/lore.md` stayed **ABSENT**
through all 40 samples and at the 18:57 final check — expected: the report lands last,
after the lane commits.

## 4. Side observations (not verdict-bearing)

- **Negative-control method**: the F29 checker resolves its root as
  `Path(__file__).resolve().parents[4]`; the sandbox copy at
  `V36-scratch/negctl/a/b/c/d/check.py` therefore roots at `V36-scratch/negctl/`, with the
  five files it reads copied alongside; each tamper reverted from `SHONEN.md.bak` before
  the next.
- **R4's repair is in flight and matches the declaration's shape**: at poll 2–16 the r96
  map shows `2 insertions(+), 2 deletions(-)` — the 8-cell delimiter row repaired to the
  table's 7 columns (`|---|---|---|---|---|---:|---|---|` → `|---|---|---|---|---:|---|---|`)
  and the stale "new relation" sentence replaced with event wording; data rows untouched.
  The r97 fixture's `claim-excerpt-map.md` was copied after the repair landed (it is
  byte-equal to the repaired r96 file at poll 4+), consistent with the "byte copies of
  POST-REPAIR r96" requirement. Content adjudication belongs to the C1/C2/C3 verifier
  seats, not this seat.
- **Fleet repo is shared**: `git -C /home/vgpnk/Projects/shokunin status --porcelain` was
  clean at seat open and again at the 18:58 final check — no sibling in-flight edits
  visible at either instant, unlike r96. The lane tree at the same check carries exactly
  the round's declared write set: `M LOG.md`, `M corpus/tools/{map_obligations.py,
  map-obligations-contract.json,README.md,dependency_freeze.py,
  dependency-freeze-contract.json}`, `M corpus/fixtures/r96-crossing-response/
  claim-excerpt-map.md`, `?? corpus/fixtures/r97-crossing-acknowledgment/`,
  `?? corpus/knowledge/r97-acknowledgment-scope-note.md`, `?? .ufo/waves/round-97/` — all
  uncommitted (round open at this cutoff, expected).

## Bottom line

**PASS** — `SHONEN.md` is canonical with four `[~]` and zero `[x]` at HEAD `2393934`: the
mechanical form checker replays exit 0 (10/10 PASS) both before and after all six producer
reports/artifacts landed, an independent diff of the seed against `PROTOCOL.md:425-433`
matches modulo `<name>`, three tamper classes (mark flip to `[x]`, dropped evidence line,
added fifth box) each fail the checker with exit 1, all 13 evidence pointers resolve, the
cited hash `8e5a68d` is an ancestor of HEAD, and the file is byte-unchanged (`03b832c7…`,
empty `git diff HEAD`, identical to r93 `9c2eea3`). The round-97 fleet-report landing set
for L1 is enumerated with exact pointers (path `.ufo/reports/round-97/lore.md` on the fleet
repo — still ABSENT at the 18:57 cutoff, as expected; Work performed / Landed changes /
Before → after measurements / SHONEN in order; per-item evidence pointers; `LOG.md`-tied
landed changes; counting-command measurements; checkable commit-hash citation; `SHONEN`
heading mandatory; pathspec-limited fleet commit under lane identity; stale-lane actuator
line). Poll (20 s × 40, 18:43:03 → 18:56:03): all six producer artifacts landed — R1
`86b52949…`, R2 `2142b991…`/`6278e59b…`, R3 `b06275f3…`/`27273be2…` (contract still moving
at cutoff), R4 map repair `e851f068…` + fixture 10/10 with exactly the five declared
modifications and five byte copies, R5 `d9387b7d…`/`49d4834e…`, R6 `5e3b4225…`; all six
producer reports by 18:56:23; 37/64 seat reports in the lane seats dir at cutoff; no strays
at the fleet root; watchdog content-check gap re-confirmed (`shokunin-watchdog.sh:14,45`).
