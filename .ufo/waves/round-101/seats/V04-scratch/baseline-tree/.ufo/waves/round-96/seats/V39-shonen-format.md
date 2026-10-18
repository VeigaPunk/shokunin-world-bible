# V39 — shonen-format (round-96 verification seat, lore-shokunin)

**Seat role:** (a) verify `SHONEN.md` still carries the canonical four-box form with four
`[~]` and zero `[x]` (mechanical checker replayed, plus independent census, pointer and
ancestry checks, plus a negative control proving the checker discriminates); (b) enumerate
the round-96 fleet-report landing set for L1 (path, sections, evidence bar, commit rules,
round-specific items); (c) poll the round's producer artifacts and seat landings. LEAF
scope: read-only checks; this report is my only write outside my scratch dir
`.ufo/waves/round-96/seats/V39-scratch/`.

**Revision tested:** lane HEAD `60dba0c2aa344860b10a2fc63e00468d1b134f27` (`60dba0c lore r95:
close round — SCORECARD admitted section`; its parent is the brief's baseline `dcb2d92`).
Lane tree at cutoff 17:53: `git status --short` →

```
 M LOG.md
 M corpus/tools/README.md
 M corpus/tools/map-obligations-contract.json
 M corpus/tools/map_obligations.py
?? .ufo/waves/round-96/
?? corpus/fixtures/r96-crossing-response/
?? corpus/knowledge/r96-response-scope-note.md
?? corpus/tools/dependency-freeze-contract.json
?? corpus/tools/dependency_freeze.py
```

No r96 commit yet (round open at cutoff; work uncommitted, expected).

## 1. `SHONEN.md` — canonical, four `[~]`, zero `[x]` (PASS)

Mechanical checker present (`.ufo/waves/round-93/deepseek/F29-shonen-format-check.py`),
replayed twice — once before producer writes (17:41) and once after all six producer
reports had landed (17:53). Both runs identical, **exit 0, 10/10 PASS**:

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
SHA256 SKILL.md 749b04d10506500b097883d83f38bba5b97c515313d61e0133d3fb751ce35c05
SHA256 PROVINCE.md 94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa
EXIT=0
```

Mark census (independent of the checker):

```
$ grep -c '^- \[~\]' SHONEN.md   → 4
$ grep -c '^- \[x\]' SHONEN.md   → 0
$ grep -c '^- \[ \]' SHONEN.md   → 0
$ grep -c '^- \[' SHONEN.md      → 4
```

Byte-unchanged against HEAD — `git diff HEAD -- SHONEN.md` is empty (0 lines) — and the
digest `03b832c7…` is identical to the one the r94 F28 seat recorded at `65a9329` and the
r95 V30 seat recorded at `fb118c4`: no drift across r94 closure → r95 → r96 mid-round.

**Negative control (the zero-`[x]` check is not vacuous).** A scratch copy of the checker
(root redirected to a sandbox tree) run against a tampered `SHONEN.md` whose first box mark
was flipped `[~]` → `[x]`:

```
$ python3 .../V39-scratch/negctl/a/b/c/d/check.py
FAIL title matches seed modulo <name>          ← sandbox dir is named negctl, expected
...
FAIL no [x] promotion claim present            ← the discriminating failure
NEGCTL EXIT=1
```

So a `[x]` write cannot pass silently; the PASS above is a real verdict on the live file.
(The second FAIL is a sandbox artifact — the checker's title check compares against the
containing directory name, `negctl` — not a live-file defect.)

Evidence pointers: every path named in the four evidence lines resolves (13/13 `OK`,
including `SKILL.md`, `.ufo/waves/round-93/recovery/R08-skill-check.py`,
`.ufo/waves/round-93/deepseek/{F21,F29,F01,F31,F03,F24}.md`,
`.ufo/waves/round-93/deepseek/{F25-replay.py,F14-postrepair-check.py}`,
`reports/round-1/baseline-probes.json`, `PROVINCE.md`), the LOG entry named in box 2 exists
once (`grep -c "Fleet round 1 — calibration declaration before batched dispatch" LOG.md` →
`1`), and the cited commit is real and an ancestor:

```
$ git cat-file -t 8e5a68d → commit
$ git merge-base --is-ancestor 8e5a68d HEAD → ANCESTOR yes
$ git log --oneline -1 8e5a68d → 8e5a68d lore r93: record DeepSeek review and resolve source precision findings
$ sed -n '3,11p' PROVINCE.md → owns/refuses/scope text present (box4 pointer resolves in range)
```

Governing gate text re-checked: `PROTOCOL.md:63-68` — `[x]` requires a reviewer who did not
author the round's changes, and "a subagent the lane dispatched is still the lane"; so the
64 round-96 seats cannot convert any box to `[x]`. `PROTOCOL.md:417` fixes the canonical
form (seed byte-identical modulo `<name>`; marks confined to the box character plus one
indented evidence line per box); `PROTOCOL.md:423-435` is the seed text.

Digest-drift note (not a defect): `SKILL.md` now hashes `749b04d1…` where the r95 V30 seat
recorded `c930675a…` at `fb118c4`; `git diff fb118c4..HEAD --stat -- SKILL.md` →
`1 file changed, 3 insertions(+), 3 deletions(-)`, carried by the r95 closure commit
`dcb2d92` ("…README/C9/SKILL updates"). `SHONEN.md` box-1's `SKILL.md` pointer still
resolves; `PROVINCE.md` (`94a7a77e…`) is unchanged. `SHONEN.md` itself was not touched by
the r95 closure (`git log --oneline -1 -- SHONEN.md` → `9c2eea3`, r93).

**Verdict:** PASS — four `[~]`, zero `[x]`, form canonical, all pointers live, and the
checker discriminates.

## 2. Round-96 fleet-report landing set for L1

Authority chain: `templates/round-prompt.md:60-90` (§4 report contract, §5 commit/push),
`PROTOCOL.md:100-108` (five child-lane items), `PROTOCOL.md:117-169` (lands-last, minimum
content, `SHONEN` heading, stale-lane actuator), `PROTOCOL.md:175-183` (content check),
`PROTOCOL.md:237-242` + `273-279` (MANIFEST ledger), `PROTOCOL.md:455-479` (commit scope,
pathspec rule, lane identity), `MISSION.md:81-90` (push scope, L0 side channel).

### 2.1 Primary artifact — the round report

| Item | Value |
|---|---|
| Path | `/home/vgpnk/Projects/shokunin/.ufo/reports/round-96/lore.md` |
| Repo | fleet repo (`/home/vgpnk/Projects/shokunin`), not the lane repo |
| Name | `<id>` = roster id `lore` (`MANIFEST.json` roster row: `{"id": "lore", "name": "lore-shokunin", "rank": "shonen", …}`); any other name does not satisfy the contract (`PROTOCOL.md:138-139`) |
| State at 17:53 | ABSENT — `ls /home/vgpnk/Projects/shokunin/.ufo/reports/round-96/` → `No such file or directory` (dir is created only when L1 files the report; lands last) |
| Precedent | r95 report committed `07ea34b45dbcc30542922fb123a6b2fe46b246a8` by `lore-shokunin <lore@shokunin.local>` (`git log -1 --format='%H %an <%ae> %s' -- .ufo/reports/round-95/lore.md`), 79 lines, headings `## Work performed` / `## Landed changes` / `## Before → after measurements` / `## SHONEN` / `## Axis and learning verdicts` |

### 2.2 Required sections, in order (`templates/round-prompt.md:64-74`)

1. **Work performed** — opens by naming the round's declared claims (r96: C1/calibration,
   C2/depth, C3/coverage — `LOG.md:2863` "## Round 96 — declaration before dispatch
   (2026-10-17)") and their target axes; then one bullet per work item, **each carrying an
   evidence pointer** (path:line, command output, or commit hash).
2. **Landed changes** — every change **tied to a `LOG.md` entry and to the commit hash**
   that carries it.
3. **Before → after measurements** — one per claim, **each with the counting command and
   the commit it was measured against**.
4. **SHONEN** — one line per box of `SHONEN.md`: `[x]` only with a named non-author
   verifier, `[~]` with a resolvable evidence pointer, `[ ]` if untouched. For r96 all four
   lines must be `[~]` (same-lane seats are the lane; no promotion). The heading is
   mandatory — "A report without this heading does not satisfy the contract even if the
   same facts appear elsewhere in it" (`PROTOCOL.md:148-153`).

### 2.3 Evidence requirements (minimum content, `PROTOCOL.md:144-153`, `175-183`)

- Work performed **plus at least one evidence pointer**; changes landed in the child repo
  each tied to a `LOG.md` entry; **cross-domain evidence with the domain named**; and a
  **checkable commit-hash citation** — the hash must exist in the lane repo and be an
  ancestor of lane `HEAD` (`git merge-base --is-ancestor <hash> HEAD`).
- **Marker rule** (`templates/round-prompt.md:75-78`): a contentless report (placeholders,
  missing required sections, no evidence pointers) = round **failed**; real committed work
  but missing sections = `ok` + minimum-content conformance defect.
- **Lands last** (`PROTOCOL.md:117-127`): the report is written only after the lane's
  child-repo work is committed, and it cites that commit's hash; corrections land as new
  commits, never by amending a cited one.
- **Stale-lane actuator** (`PROTOCOL.md:154-169`): the report must list any mission open
  longer than two driver ticks with `progressing` / `progressing-weak` / `silent` (age from
  the launch timestamp, not the tick counter).
- **Honest defect accounting** (r94/r95 precedent): failed-output gaps, late landings and
  misplaced reports are named, not smoothed.

### 2.4 Commit / push rules for the landing (`templates/round-prompt.md:80-86`, `PROTOCOL.md:455-472`, `MISSION.md:81-90`)

- Round end: commit (`round-96`) inside the lane repo, then push; **also commit and push
  the report on the fleet repo**.
- Fleet-repo commit is **pathspec-limited**: `git commit -- .ufo/reports/round-96/lore.md`
  — never `commit -a` / `add -A` (sibling in-flight edits, e.g. kotodama's untracked
  `reports/` and `mtk-zeichentragende.pdf` currently visible in `git -C
  /home/vgpnk/Projects/shokunin status --porcelain`).
- Main-repo commits cannot rely on `git config`; use
  `git -c user.name=lore-shokunin -c user.email=lore@shokunin.local commit …`
  (`PROTOCOL.md:476-479`). The r95 precedent commit `07ea34b` carries exactly that identity.
- Push scope: fleet repo remote + own lane remote only; domain source trees read-only.
- `.ufo/waves/` (seat reports, receipt, wave-spec) is committed with the round's
  integration commit; `.ufo/state/` and `.ufo/watchdog.log` must never be committed by a
  lane (`PROTOCOL.md:455-459`).

### 2.5 Round-96-specific items observed

- **Lane repo work L1 must commit** (digests at cutoff 17:52:59, `sha256sum`):

```
2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8  corpus/tools/map_obligations.py
97b76bb8b1fea97f166ef7586eba69c427ec15bbe7b34eb5345ec65c936493b6  corpus/tools/map-obligations-contract.json
965b29cd41a8af14293eb2e1948f58f310e58c6e752b8fe322c5445b20a91f24  corpus/tools/README.md
a3b57978f0cbf314389ee3f9862920a46cf109fca6d1eec488c39be0457f0980  corpus/tools/dependency_freeze.py
7d568cc422cda42297b7506a1a3e083e8798866efd16d58617bf4ea468576975  corpus/tools/dependency-freeze-contract.json
6db32ca24f5eff5baa3ebe589e8d3bcb6b256fec18dee2468211d7d0fae157c6  corpus/knowledge/r96-response-scope-note.md
```

  plus `LOG.md` (r96 declaration + results entry), `SCORECARD.md` (r96 rows), the
  `corpus/fixtures/r96-crossing-response/` tree (10 files; `diff -rq` vs r95 shows exactly
  the 5 declared modifications — `claim-excerpt-map.md`, `fictional-excerpts.md`,
  `README.md`, `sources.json`, `timeline.json` — with the other 5 files byte copies), and
  the `.ufo/waves/round-96/` bookkeeping (seat reports Q1–Q6 + V-seats, receipt when
  written; no `wave-spec.md` observed at cutoff).
- **Fleet repo**: only `.ufo/reports/round-96/lore.md` is L1's to write; the
  `MANIFEST.json` `rounds[]` append is the integrator-of-record's act, not L1's
  (`PROTOCOL.md:237-242`; r95 precedent entry: `{"round": 95, …, "lanes": {"lore": "ok"},
  …, "admitted": true, "verdicts": {…}}`).
- **L0**: `.ufo/l0-questions.md` carries one `lore | round-1 | …` line; no r96 lore
  question appended at cutoff. L0 durability is the integrator's (`PROTOCOL.md:504-510`).
- **No fleet prompt file** for this lane-round: `.ufo/prompts/` contains only
  `lore-round-1.md` — same as r93–r95; dispatch evidence rides `LOG.md` + the wave dir.
- **Watch item (carried defect classes, re-confirmed this round)**: the watchdog still
  does not gate this lane —
  `scripts/shokunin-watchdog.sh:14` `LANES="protocol aggregator kasegi kengaku kake
  kumitate kotoba kagi kama"` (no `lore`), `:45` `report_of() { [ -f
  "$SK/.ufo/reports/round-$2/$1.md" ]; }` (existence-only, no `SHONEN`/content grep —
  the only greps are at lines 80 and 95 over launch/status output), contrary to
  `PROTOCOL.md:175-183`. The report content bar therefore rests on integrator review.
- **Mislanding watch (r95 defect class)**: no stray r96 files at the fleet root —
  `find /home/vgpnk/Projects/shokunin/.ufo/waves/round-96 /home/vgpnk/Projects/shokunin/reports
  -path '*round-96*' -type f` → no output (fleet `.ufo/waves/round-96` does not exist;
  fleet `reports/` holds only `round-9`).

## 3. Poll log — producer artifacts and seat landings

Cadence 20 s, 40 samples, 17:39:59 → 17:52:59 (`POLL DONE 17:53:19`), raw log at
`.ufo/waves/round-96/seats/V39-scratch/poll.log`. Baselines at poll 0 (pre-write): Q1
`d1c239cc…` (= r95 final), Q2 contract `8173bb97…` / README `5d033c9d…` (= r95 final), Q3
files ABSENT, Q6 note ABSENT, fixture dir 8 files, 0 seat reports.

| Event | Time | Evidence |
|---|---|---|
| Q3 `dependency_freeze.py` first non-baseline | 17:43:19 | `q3p=f4b5208f…` |
| Fixture complete 10/10 files | 17:43:19 | `fx=10` |
| Q6 note first write | 17:44:19 | `q6=ff9ec308…` |
| Q1 tool first non-baseline | 17:44:19 | `q1=99c7d764…` |
| Q3 tool/contract stable | from 17:44:39 | `q3p=a3b57978…`, `q3c=7d568cc4…` |
| Q1 tool stable | from 17:47:39 | `q1=2b0ba815…` |
| Q6 note stable | from 17:47:19 | `q6=6db32ca2…` |
| Q2 contract first non-baseline | 17:50:59 | `q2c=97b76bb8…` |
| Q2 README stable | from 17:51:39 | `q2r=965b29cd…` |
| All six producer reports landed | 17:52:19 | `prods=6` |

Seat census at cutoff 17:52:59: **41 `.md` seat reports** in the lane seats dir = 6
producers (`Q1-tool-hardening`, `Q2-contract-docs`, `Q3-dependency-freeze`,
`Q4-fixture-json`, `Q5-fixture-docs`, `Q6-knowledge-note`) + 35 verifiers
(V01, V04–V09, V11–V23, V25, V26, V32–V34, V37, V45, V46, V48, V49, V51, V53–V57).
Verifier seats not yet present at cutoff (23): V02, V03, V10, V24, V27–V31, V35, V36,
V38–V44, V47, V50, V52, V58 — plus this seat (V39) filed after the cutoff. Round still
open; late landings are the r95 norm (three late landings there), not failures.

`/home/vgpnk/Projects/shokunin/.ufo/reports/round-96/lore.md` stayed **ABSENT** through
all 40 samples — expected: the report lands last, after the lane commits.

## 4. Side observations (not verdict-bearing)

- **Negative-control method**: the F29 checker resolves its root as
  `Path(__file__).resolve().parents[4]`, so the sandbox copy was placed at
  `V39-scratch/negctl/a/b/c/d/check.py` with `SHONEN.md`/`LOG.md`/`PROVINCE.md`/`SKILL.md`/
  `reports/round-1/baseline-probes.json` copied alongside; only the first box mark was
  tampered. Result: exit 1 with the `[x]` failure — the form checker is discriminating.
- **Fleet repo is shared**: while polling, the fleet repo gained sibling activity —
  `b372a53 close kotodama round-8 …` and untracked `reports/` + `mtk-zeichentragende.pdf`
  at the fleet root (kotodama's, not lore's). None of it is in lore's write scope; the
  r95 report commit precedent still stands as the lane's own path-limited act.
- **`SHONEN.md` regeneration risk is nil this round**: no writer but the lane may touch it
  (`PROTOCOL.md:417`), and the file is byte-identical to the r94/r95 closure revision
  (`03b832c7…`), re-verified after all six producer reports landed.

## Bottom line

**PASS** — `SHONEN.md` is canonical with four `[~]` and zero `[x]` at HEAD `60dba0c`: the
mechanical form checker replays exit 0 (10/10 PASS) before and after all producer writes, a
`[x]`-tamper negative control fails it (exit 1), all 13 evidence pointers resolve, the cited
hash `8e5a68d` is an ancestor of HEAD, and the file is byte-unchanged (`03b832c7…`, empty
`git diff HEAD`). The round-96 fleet-report landing set for L1 is enumerated with exact
pointers (path `.ufo/reports/round-96/lore.md` on the fleet repo — still ABSENT at cutoff,
as expected; Work performed / Landed changes / Before → after measurements / SHONEN in
order; per-item evidence pointers; `LOG.md`-tied landed changes; counting-command
measurements; checkable commit-hash citation; `SHONEN` heading mandatory; pathspec-limited
fleet commit under lane identity; stale-lane actuator line). Poll: all six producer reports
and their artifacts landed by 17:52:19 (Q1 `2b0ba815…`, Q2 `97b76bb8…`/`965b29cd…`, Q3
`a3b57978…`/`7d568cc4…`, fixture 10/10 with exactly the 5 declared modifications, Q6
`6db32ca2…`), 41/64 seat reports in the lane seats dir at cutoff, no stray r96 files at the
fleet root; watchdog content-check gap re-confirmed (`shokunin-watchdog.sh:14,45`).
