# V32 — shonen-format (round-98 verification seat, lore-shokunin)

**Seat role:** (a) mechanical check of `SHONEN.md` — canonical four-box form, four `[~]`,
zero `[x]` (round-93 form checker replayed at seat open and again after the producers'
artifacts landed, plus an independent seed-block diff against `PROTOCOL.md`, an
independent mark census, evidence-pointer and ancestry resolution, and three negative
controls proving the checker discriminates); (b) enumerate the round-98 fleet-report
landing set for L1 (path, sections, evidence bar, commit rules, round-specific items);
(c) poll the round's five producer artifacts and seat landings.
LEAF scope: read-only checks; this report is my only write outside my scratch dir
`.ufo/waves/round-98/seats/V32-scratch/`.

**Revision tested:** lane HEAD `dd4df1b36a64b513e75b46da04ee2f3f7f3eb6cb` (`dd4df1b lore
r97: close round — SCORECARD admitted section`, +33 lines SCORECARD.md only; parent and
declared round baseline `9a3d648`). Working tree at open: `git status --porcelain` →

```
 M LOG.md
?? .ufo/waves/round-98/
```

(plus, within the minute, ` M corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md`
and `?? corpus/fixtures/r98-clerk-filing/` as producers S3 started.)

## 1. `SHONEN.md` — canonical, four `[~]`, zero `[x]` (PASS)

Mechanical checker (`.ufo/waves/round-93/deepseek/F29-shonen-format-check.py`) replayed
twice — at seat open and again after the producer artifacts had landed — **exit 0,
10/10 PASS** both times:

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
SHA256 SKILL.md 2b5bf27fd1bc49da1e5cad979b3ca93d410d03c8c52bd49d8bc8b29a1c428b00
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

Byte-unchanged — `git diff HEAD -- SHONEN.md | wc -l` → `0` and `git diff 9a3d648 --
SHONEN.md | wc -l` → `0`; also `git diff 9c2eea3 -- SHONEN.md | wc -l` → `0` (the r93
commit that last touched it). Digest `03b832c7…` equals the value recorded by the r94
F28, r95 V30, r96 V39 and r97 V36 seats — no drift across five closures.

**Independent seed-block check (not the checker).** `PROTOCOL.md:425-432` (indented code
block) stripped of the 4-space indent and `<name>` → `lore-shokunin`:

```
frame match: True
box texts match (marks/evidence excluded): True
seed marks all '[ ]': True
  frame 1..4 OK; box 1..4 OK
```

Evidence pointers: every path named in the four evidence lines resolves (11/11 path
pointers `OK` plus `LOG.md` and `PROVINCE.md` — 13/13 total: `SKILL.md`, `LOG.md`,
`reports/round-1/baseline-probes.json`, `PROVINCE.md`,
`.ufo/waves/round-93/recovery/R08-skill-check.py`,
`.ufo/waves/round-93/deepseek/{F21,F29,F01,F25-replay.py,F31,F14-postrepair-check.py,F03,F24}`),
the LOG entry named in box 2 exists once (`grep -c "Fleet round 1 — calibration
declaration before batched dispatch" LOG.md` → `1`), the `PROVINCE.md:3-11` citation is in
range (owns/refuses/scope text), and the cited commit is real and an ancestor:

```
$ git cat-file -t 8e5a68d → commit
$ git merge-base --is-ancestor 8e5a68d HEAD → ANCESTOR yes
$ git log --oneline -1 8e5a68d → 8e5a68d lore r93: record DeepSeek review and resolve source precision findings
```

**Negative controls (the PASS is not vacuous).** Sandbox copy of the checker at
`V32-scratch/negctl/a/b/c/d/check.py` (root resolves to `parents[4]` = the sandbox dir,
with `SHONEN.md`/`LOG.md`/`PROVINCE.md`/`SKILL.md`/`reports/round-1/baseline-probes.json`
copied alongside); three separate tampers, each reverted before the next:

```
NEGCTL-1 first box [~]→[x]          → EXIT=1, FAIL no [x] promotion claim present
NEGCTL-2 box2 evidence line removed → EXIT=1, FAIL both [~] boxes carry their required pointer
NEGCTL-3 fifth box appended         → EXIT=1, FAIL four boxes, seed order and text
```

(Each sandbox run also reports `FAIL title matches seed modulo <name>` — an artifact of
the sandbox directory being named `negctl`, not a live-file defect.)

Governing gate text re-checked: `PROTOCOL.md:63-68` — `[x]` requires a reviewer who did
not author the round's changes, and "a subagent the lane dispatched is still the lane";
the 64 round-98 seats cannot convert any box to `[x]`. `PROTOCOL.md:417` fixes the
canonical form (seed byte-identical modulo `<name>`; marks confined to the box character
plus one indented evidence line per box).

**Digest-drift note (not a defect):** `SKILL.md` hashes `2b5bf27f…` where the r97 V36
seat recorded `a2f1e4c6…` at `2393934`; carried by the r97 closure (`git diff --stat
2393934..HEAD -- SKILL.md` → `1 file changed, 5 insertions(+), 5 deletions(-)` — the
closure's registry-row pass). `SHONEN.md` box-1's `SKILL.md` pointer still resolves.
`PROVINCE.md` (`94a7a77e…`) unchanged; `SHONEN.md` itself untouched since r93.

**Verdict:** PASS — four `[~]`, zero `[x]`, form canonical against both the checker and an
independent seed diff, all pointers live, cited hash an ancestor, and the checker
discriminates on three tamper classes.

## 2. Round-98 fleet-report landing set for L1

Authority chain: `templates/round-prompt.md:60-78` (§4 report contract), `:80-86` (§5
commit/push scope), `PROTOCOL.md:100-108` (five child-lane items), `:117-127`
(lands-last + commit-hash citation), `:138-139` (report name = roster id), `:144-153`
(minimum content), `:154-169` (stale-lane actuator), `:175-191` (content check, marker
rule), `:192-208` (integrator of record), `:455-459` (wave/prompt commit scope),
`:473-479` (lane identity, pathspec rule), `MISSION.md:81` §Push scope.

### 2.1 Primary artifact — the round report

| Item | Value |
|---|---|
| Path | `/home/vgpnk/Projects/shokunin/.ufo/reports/round-98/lore.md` |
| Repo | fleet repo (`/home/vgpnk/Projects/shokunin`), not the lane repo |
| Name | `<id>` = roster id `lore` (`MANIFEST.json` roster row `{"id": "lore", "name": "lore-shokunin", "domain": "fictional-world records + consistency verification", "rank": "shonen", …}`); any other name does not satisfy the contract (`PROTOCOL.md:138-139`) |
| State at seat open | ABSENT — `ls /home/vgpnk/Projects/shokunin/.ufo/reports/round-98/` → `No such file or directory` (the dir is created only when L1 files the report; lands last) |
| Precedent | r94 `be6eca9`, r95 `07ea34b`, r96 `5e03802`, r97 `80ca9dd` — each authored `lore-shokunin <lore@shokunin.local>`, subject `protocol: close lore rN (admitted) — fleet report + MANIFEST ledger append`; each carries the report plus the `MANIFEST.json` rounds append in the one commit (r97: report 84 lines + MANIFEST 196-line diff) |

### 2.2 Required sections, in order (`templates/round-prompt.md:64-74`)

1. **Work performed** — opens by naming the round's declared claims (r98: C1/calibration,
   C2/coverage, C3/depth — `LOG.md:3086-3143` "## Round 98 — declaration before dispatch
   (2026-10-17)", C1 at `:3098`, C2 at `:3107`, C3 at `:3115`) and their target axes; then
   one bullet per work item, **each carrying an evidence pointer** (path:line, command
   output, or commit hash).
2. **Landed changes** — every change **tied to a `LOG.md` entry and to the commit hash**
   that carries it.
3. **Before → after measurements** — one per claim, **each with the counting command and
   the commit it was measured against**.
4. **SHONEN** — one line per box of `SHONEN.md`: `[x]` only with a named non-author
   verifier, `[~]` with a resolvable evidence pointer, `[ ]` if untouched. For r98 all
   four lines must be `[~]` (same-lane seats are the lane; no promotion). The heading is
   mandatory — "A report without this heading does not satisfy the contract even if the
   same facts appear elsewhere in it" (`PROTOCOL.md:148-153`).

### 2.3 Evidence requirements (`PROTOCOL.md:144-153`, `:175-191`, `:328-358`)

- Work performed **plus at least one evidence pointer**; changes landed in the child repo
  each tied to a `LOG.md` entry; **cross-domain evidence with the domain named**; a
  **checkable commit-hash citation** — the hash must exist in the lane repo and be an
  ancestor of lane `HEAD` (`git merge-base --is-ancestor <hash> HEAD`).
- **Marker rule** (`templates/round-prompt.md:75-78`, `PROTOCOL.md:175-191`): a contentless
  report = round **failed**; real committed work but missing sections = `ok` +
  minimum-content defect.
- **Lands last** (`PROTOCOL.md:117-127`): written only after the lane's child-repo work is
  committed, and it cites that commit's hash.
- **Stale-lane actuator** (`PROTOCOL.md:154-169`): the report must list any mission open
  longer than two driver ticks with `progressing` / `progressing-weak` / `silent` (age
  from the launch timestamp, not the tick counter).
- **Honest defect accounting** (r94–r97 precedent): failed-output gaps, late landings and
  misplaced reports are named, not smoothed.

### 2.4 Commit / push rules for the landing (`templates/round-prompt.md:80-86`, `PROTOCOL.md:455-479`, `MISSION.md:81`)

- Round end: commit (`round-98`) inside the lane repo, then push; **also commit and push
  the report on the fleet repo**.
- Fleet-repo commit is **pathspec-limited**: `git commit -- .ufo/reports/round-98/lore.md`
  — never `commit -a` / `add -A` (the fleet repo is shared with sibling lanes).
- Main-repo commits cannot rely on `git config`; use
  `git -c user.name=lore-shokunin -c user.email=lore@shokunin.local commit …`
  (`PROTOCOL.md:476-479`).
- Push scope: fleet repo remote + own lane remote only; domain source trees read-only.
- `.ufo/waves/` (seat reports, receipt) is committed with the round's integration commit;
  `.ufo/state/` and `.ufo/watchdog.log` must never be committed by a lane.
- Corrections land as new commits, never by amending a cited one.

### 2.5 Round-98-specific items observed

- **Lane repo work L1 must commit** — producer-owned files (five producers, exclusive
  byte-ownership per the round declaration `LOG.md:3135-3143`; baseline = `9a3d648`):
  - S1 `corpus/tools/dependency_freeze.py` (baseline `b06275f3…`) +
    `corpus/tools/dependency-freeze-contract.json` (baseline `27273be2…`)
  - S2 `corpus/tools/README.md` (baseline `8678abc1…`)
  - S3 `corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md` (repair only;
    baseline `30281ff1…`) + `corpus/fixtures/r98-clerk-filing/` {entities,sources,timeline}.json
    + fictional-excerpts.md + byte copies of the other 7 files from `9a3d648`
  - S4 `corpus/fixtures/r98-clerk-filing/README.md` + `claim-excerpt-map.md`
  - S5 `corpus/knowledge/r98-clerk-scope-note.md` (ABSENT at seat open) + dated correction
    addenda in `corpus/knowledge/r95-aftermath-scope-note.md` (baseline `f87ed42a…`) and
    `corpus/knowledge/r96-response-scope-note.md` (baseline `6db32ca2…`)
  plus `LOG.md` (r98 declaration + results entry), `SCORECARD.md` (r98 rows), and
  `.ufo/waves/round-98/` bookkeeping (seat reports + receipt when written).
- **Fleet repo**: only `.ufo/reports/round-98/lore.md` is L1's to write; the
  `MANIFEST.json` `rounds[]` append is the integrator-of-record's act, not L1's
  (`PROTOCOL.md:192-208`) — observed r94–r97 precedent lands both in one lane-authored
  commit (see 2.1).
- **L0**: `.ufo/l0-questions.md` carries `lore | round-1 | …` (line 33) and kotodama
  questions (incl. kotodama round-2, addressed to lore's intake — still open); no r98 lore
  question appended at seat open.
- **No fleet prompt file** for this lane-round: `.ufo/prompts/lore-round-1.md` is the only
  `lore*` prompt — same as r93–r97; dispatch evidence rides `LOG.md` + the wave dir.
- **Watch item (carried defect class)**: the watchdog still does not gate this lane —
  `scripts/shokunin-watchdog.sh:14` `LANES="protocol aggregator kasegi kengaku kake
  kumitate kotoba kagi kama"` (no `lore`), `:45` `report_of() { [ -f
  "$SK/.ufo/reports/round-$2/$1.md" ]; }` (existence-only; no content check), contrary to
  `PROTOCOL.md:175-191`. The report content bar therefore rests on integrator review.
- **Mislanding watch (r94-F01 class)**: no stray r98 files at the fleet root —
  `find .ufo/waves/round-98 reports -path '*round-98*' -type f` → no output; fleet
  `git status --porcelain` → clean at seat open.

## 3. Poll log — producer artifacts and seat landings

{{POLL}}

## 4. Side observations (not verdict-bearing)

{{SIDE}}

## Bottom line

{{BOTTOM}}
