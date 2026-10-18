# V35 — shonen-format (round-99 verification seat, lore-shokunin)

**Seat role:** (a) mechanical check of `SHONEN.md` — canonical four-box form, four `[~]`, zero `[x]` (round-93 form checker replayed at seat open and again after the poll window, plus an independent seed-block diff against `PROTOCOL.md`, an independent mark census, evidence-pointer and ancestry resolution, and negative controls on both a misnamed sandbox and a `lore-shokunin`-named root); (b) enumerate the round-99 fleet-report landing set for L1 (path, sections, evidence bar, commit rules, round-specific items); (c) poll the round's five producer artifacts and seat landings.
LEAF scope: read-only checks. Writes are only this report and scratch under `.ufo/waves/round-99/seats/V35-scratch/`.

**Revision tested:** lane HEAD `337f0fa52b02626b7687eedbb2d99fab30446fe4` (`337f0fa lore r99: record blocked dispatch attempt (xai-oauth credential pool missing) — zero increment`). Declared baseline is r98 freeze `4265df5e86e4121bde4125b649b89bb1676676a5` (`LOG.md:3204`); it is an ancestor of HEAD (`git merge-base --is-ancestor 4265df5 HEAD` → ancestor_yes). `git diff --stat 4265df5 HEAD` is only `LOG.md` +91 and `SCORECARD.md` +32: `111b9a3` is the r98 SCORECARD close; `337f0fa` is the blocked-attempt log. Producer paths are identical between `4265df5` and HEAD. This re-dispatch's wave tree is uncommitted.

`337f0fa` is not a round-work commit. It records zero increment and "no reports landed under `.ufo/waves/round-99/`" (`LOG.md:3267-3289`). Citing it, or `4265df5`, as the r99 work hash would not satisfy the lands-last citation rule.

## 1. `SHONEN.md` — canonical, four `[~]`, zero `[x]` (PASS)

Mechanical checker (`.ufo/waves/round-93/deepseek/F29-shonen-format-check.py`, sha256 `cb1223e7028468ba90ee1727bca130ea2920ba429dd1c4f929f21a67eaae0403`) replayed twice — at seat open (`2026-10-17T22:04:21-03:00`) and again after the poll (`2026-10-17T22:27:29-03:00`) — **exit 0, 10/10 PASS** both times. Post-poll replay (open replay printed the same ten PASS lines and the same three hashes):

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
SHA256 SKILL.md 22ffaa822ec7614fa85322f7fa07e6f369c0888e1107f9f297f76a14e18c20c5
SHA256 PROVINCE.md 94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa
CHECKER_EXIT=0
```

The check named "both [~] boxes" is implemented as every `[~]` box (`all(idx in evidence for … if m == "~")`). All four boxes are `[~]` and each has one evidence line, so the check is not vacuous on this file.

Mark census (independent of the checker), same at open and at 22:27:29:

```
$ grep -c '^- \[~\]' SHONEN.md   → 4
$ grep -c '^- \[x\]' SHONEN.md   → 0
$ grep -c '^- \[ \]' SHONEN.md   → 0
$ grep -c '^- \[' SHONEN.md      → 4
$ grep -n '\[x\]' SHONEN.md      → no match (grep exit 1)
```

Byte-unchanged — `git diff HEAD -- SHONEN.md | wc -l` → `0` (re-checked 22:27:29 and 22:37:57), `git diff 4265df5 -- SHONEN.md | wc -l` → `0`, `git diff 9c2eea3 -- SHONEN.md | wc -l` → `0`. Last commit that touches it: `9c2eea3 lore r93: close verified claims and correct historical admission records`. Digest `03b832c7…` equals the value recorded by the r94 F28, r95 V30, r96 V39, r97 V36, and r98 V32 seats.

**Independent seed-block check (not the checker).** `PROTOCOL.md:425-432` stripped of the 4-space indent, `<name>` → `lore-shokunin`:

```
frame match: True
box texts match (marks/evidence excluded): True
seed marks all '[ ]': True [' ', ' ', ' ', ' ']
live marks: ['~', '~', '~', '~']
```

Evidence pointers: every path named in the four evidence lines resolves (13/13 `OK`: `SKILL.md`, `LOG.md`, `reports/round-1/baseline-probes.json`, `PROVINCE.md`, `.ufo/waves/round-93/recovery/R08-skill-check.py`, `.ufo/waves/round-93/deepseek/{F21,F29,F01,F25-replay.py,F31,F14-postrepair-check.py,F03,F24}.md`). The LOG entry named in box 2 exists once (`LOG entry count: 1` for `Fleet round 1 — calibration declaration before batched dispatch`). `PROVINCE.md` has 11 lines; `:3-11` is in range and is the owns/sources/refuses/write-scope text. Cited commit is real and an ancestor:

```
$ git cat-file -t 8e5a68d → commit
$ git merge-base --is-ancestor 8e5a68d HEAD → ANCESTOR_yes
$ git log --oneline -1 8e5a68d → 8e5a68d lore r93: record DeepSeek review and resolve source precision findings
```

**Negative controls (the PASS is not vacuous).** Checker copied so `parents[4]` is the sandbox root. Two roots:

1. `V35-scratch/negctl/` — title check fails on every run because the directory is not named `lore-shokunin` (same artifact the r98 seat recorded). Discriminating failures on top of that title FAIL, each tamper reverted before the next; live `SHONEN.md` `cmp`-matched the bak afterwards (`LIVE_MATCHES_BAK`, digest still `03b832c7…`):

```
NEGCTL-1 first box [~]→[x]          → EXIT=1, FAIL no [x] promotion claim present
NEGCTL-2 box2 evidence line removed → EXIT=1, FAIL both [~] boxes carry their required pointer
                                      (also FAIL box2 LOG entry and baseline-probes checks)
NEGCTL-3 fifth box appended         → EXIT=1, FAIL four boxes, seed order and text
```

2. `V35-scratch/namedroot/lore-shokunin/` — `parents[4].name` is `lore-shokunin`, so the title check is live. Untampered copy **EXIT=0, 10/10 PASS**. Same three tampers, each reverted; restored copy EXIT=0; live file untouched (`LIVE_UNTOUCHED`):

```
NAMEDROOT-1 [~]→[x]                 → EXIT=1, only FAIL is "no [x] promotion claim present"
NAMEDROOT-2 box2 evidence removed   → EXIT=1, FAIL required pointer + both box2 evidence checks
NAMEDROOT-3 fifth box appended      → EXIT=1, only FAIL is "four boxes, seed order and text"
```

Governing gate text re-checked: `PROTOCOL.md:63-68` — `[x]` requires a reviewer who did not author the round's changes, and "a subagent the lane dispatched is still the lane"; the 128 round-99 seats cannot convert any box to `[x]`. `PROTOCOL.md:417` and `:423-435` fix the canonical form (seed byte-identical modulo `<name>`; marks confined to the box character plus one indented evidence line per box).

**Digest note (not a defect):** `SKILL.md` at `4265df5` and in the working tree is `22ffaa82…`. The r98 V32 seat recorded `2b5bf27f…` before the r98 closure rewrote the freeze row; that earlier digest is not the current baseline. S2 has not edited `SKILL.md` this round (hash still `22ffaa82…` at 22:37:57). Box-1's `SKILL.md` pointer still resolves. `PROVINCE.md` (`94a7a77e…`) unchanged.

**Verdict:** PASS — four `[~]`, zero `[x]`, form canonical against both the checker and an independent seed diff, all pointers live, cited hash an ancestor, file byte-unchanged since r93, and the checker discriminates on three tamper classes when the sandbox root is named `lore-shokunin`.

## 2. Round-99 fleet-report landing set for L1

Authority chain: `templates/round-prompt.md:60-78` (§4 report contract), `:80-86` (§5 commit/push scope), `PROTOCOL.md:100-108` (five child-lane items), `:117-127` (lands-last + commit-hash citation), `:138-139` (report name = roster id), `:144-153` (minimum content), `:154-169` (stale-lane actuator), `:175-191` (content check, marker rule), `:192-208` (integrator of record), `:447` (`LOG.md` append-only), `:455-459` (wave/prompt commit scope), `:470-479` (pathspec + lane identity), `MISSION.md:77-87` (round end + push scope). Where a prompt or a prior round's practice conflicts with current `PROTOCOL.md`, the repo file wins (`PROTOCOL.md:91-92`).

### 2.1 Primary artifact — the round report

| Item | Value |
|---|---|
| Path | `/home/vgpnk/Projects/shokunin/.ufo/reports/round-99/lore.md` |
| Repo | fleet repo (`/home/vgpnk/Projects/shokunin`), not the lane repo |
| Name | `<id>` = roster id `lore` (`MANIFEST.json` `roster[10]` = `{"id": "lore", "name": "lore-shokunin", "domain": "fictional-world records + consistency verification", "rank": "shonen", "repo": "shokunin-world-bible", "minted": "2026-10-11"}`). Any other name does not satisfy the contract (`PROTOCOL.md:138-139`) |
| State | ABSENT at seat open (`ls` 22:01), through all 40 poll samples, and at 22:27:29, 22:30:19, and 22:37:57. Expected: the report lands last, after the lane's child-repo work is committed (`PROTOCOL.md:117-121`) |
| Precedent commits | r94 `be6eca9`, r95 `07ea34b`, r96 `5e03802`, r97 `80ca9dd`, r98 `9a74e25` — each `lore-shokunin <lore@shokunin.local>`, subject `protocol: close lore rN (admitted) — fleet report + MANIFEST ledger append`. `9a74e25` changes `.ufo/reports/round-98/lore.md` (81 lines) and `MANIFEST.json` (198-line diff). Last `rounds[]` entry is round 98 (`closed_at` `2026-10-17T21:37:26-03:00`); no round-99 row |

### 2.2 Required sections, in order (`templates/round-prompt.md:64-74`)

1. **Work performed** — opens by naming the round's declared claims and their target axes. Standing declaration is `LOG.md:3200` "## Round 99 — declaration before dispatch (2026-10-17)" (unchanged by this re-dispatch; the blocked attempt at `:3267` did not replace it). C1/calibration at `:3212` (full-file freeze pinning; ten files per chain fixture; schema versioned; any pinned-file edit → exit 2 `DIGEST-MISMATCH` naming the file; chain re-frozen via guarded `--freeze`, 6/6; self-test 17→18; BR-01 prose-half edit-detectable, not semantics-provable). C2/depth is one axis-move with two falsifiable components: component 1 at `:3225` (`corpus/fixtures/r99-window-lapse/`, fifth beat, 6/1/7→6/1/8, sources 7→8, 21 map obligations, CLEAN, census 172→173); component 2 at `:3238` (`corpus/knowledge/r99-gate-blind-spot-table.md`, every row replay-verified on the delivered revision). Then one bullet per work item, **each carrying an evidence pointer**.
2. **Landed changes** — every change **tied to a `LOG.md` entry and to the commit hash** that carries it. The results entry must be **appended**. `LOG.md:3200` and `:3267` are already committed in `337f0fa`; rewriting them in place would violate `PROTOCOL.md:123-124` and `:447`.
3. **Before → after measurements** — one per claim (C2's two components each), **each with the counting command and the commit it was measured against**. This seat did not run those counts. They are not verified here.
4. **SHONEN** — one line per box: `[x]` only with a named non-author verifier, `[~]` with a resolvable evidence pointer, `[ ]` if untouched. For r99 all four lines must be `[~]` (same-lane seats are the lane; no promotion). The heading is mandatory — "A report without this heading does not satisfy the contract even if the same facts appear elsewhere in it" (`PROTOCOL.md:148-153`). r98's filed report (`.ufo/reports/round-98/lore.md:59`) uses this heading with four `[~]` lines and an explicit no-`[x]` line.

### 2.3 Evidence requirements (`PROTOCOL.md:144-153`, `:175-191`)

- Work performed **plus at least one evidence pointer**; changes landed in the child repo each tied to a `LOG.md` entry; **cross-domain evidence with the domain named**; a **checkable commit-hash citation** — the hash must exist in the lane repo and be an ancestor of lane `HEAD` (`git merge-base --is-ancestor <hash> HEAD`).
- That hash is the lane repo's `HEAD` when the report is written, and it must be the commit that carries this re-dispatch's child-repo work. `337f0fa` exists and is an ancestor, but it records zero increment. `4265df5` is the declared baseline, not the r99 work commit. Neither satisfies lands-last for this re-dispatch.
- **Marker rule** (`templates/round-prompt.md:75-78`, `PROTOCOL.md:175-191`): a contentless report = round **failed**; real committed work but missing sections = `ok` + minimum-content defect.
- **Lands last** (`PROTOCOL.md:117-127`): written only after the lane's child-repo work is committed, and it cites that commit's hash. Uncommitted wave-tree files do not count as landed.
- **Stale-lane actuator** (`PROTOCOL.md:154-169`): the report must list any mission open longer than two driver ticks with `progressing` / `progressing-weak` / `silent` (age from the launch timestamp, not the tick counter).
- **Honest defect accounting** (r94–r98 precedent, and this seat's poll): failed-output gaps, late landings, ABSENT producers, and misplaced writes are named, not smoothed.

### 2.4 Commit / push rules (`templates/round-prompt.md:80-86`, `PROTOCOL.md:455-479`, `MISSION.md:77-87`)

- Round end: commit (`round-99`) inside the lane repo, then push; **also commit and push the report on the fleet repo**.
- Fleet-repo commit is **pathspec-limited to the report file**: `git commit -- .ufo/reports/round-99/lore.md` — never `commit -a` / `add -A` (`PROTOCOL.md:470-472`). The fleet repo is shared with sibling lanes.
- `MANIFEST.json` `rounds[]` append is the integrator-of-record's act, not L1's (`PROTOCOL.md:192-208`, `:451-452`). r94–r98 lore commits combined the report and the MANIFEST append under lore identity. That combination was already recorded as a scope/attribution defect (MANIFEST `rounds` idx 187, r91 closure-correction: "Fleet 3099d9f combined report/MANIFEST under lore identity, recorded scope defect"; idx 185 names the same class for `5de03da`). Contract text wins over that precedent. This seat does not authorize L1 to repeat it.
- Main-repo commits cannot rely on `git config`; use `git -c user.name=lore-shokunin -c user.email=lore@shokunin.local commit …` (`PROTOCOL.md:476-479`). Observed r98 author is that identity.
- Push scope: fleet repo remote + own lane remote only; domain source trees read-only (`MISSION.md:81-87`).
- `.ufo/waves/` (seat reports, receipt when written) is committed with the round's integration commit; `.ufo/state/` and `.ufo/watchdog.log` must never be committed by a lane (`PROTOCOL.md:455-459`).
- Corrections land as new commits, never by amending a cited one.

### 2.5 Round-99-specific items

Lane repo work the declaration assigns (`LOG.md:3257-3265`), with state at the poll cutoff and a 22:37:57 recheck. Baseline hashes are `git show 4265df5:<path> | sha256sum`. Content of C1/C2 is **not** adjudicated here — other seats own that, and ABSENT files are not verified from the declaration.

- S1 `corpus/tools/dependency_freeze.py` (baseline `03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b`; cutoff `6f81f8be19742372ddc6819f6cf50dad985fe2bca2bee2b6e7c579613f5f4067`) + `corpus/tools/dependency-freeze-contract.json` (baseline `153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947`; cutoff `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628`). Working tree vs HEAD at 22:27:29: `2 files changed, 206 insertions(+), 22 deletions(-)` (contract 163/…, tool 65/…). **S1 report ABSENT** (no `seats/S1*.md` through 22:37:57). Bytes changed; the producer's report did not land. Not verified as the C1 claim.
- S2 `corpus/tools/README.md` + `SKILL.md` freeze row. Both still baseline at 22:37:57 (`294dd56f29ce1fd40be3a80d365b33724c9cd1969d3f7b7abb271fd1adaaa207`, `22ffaa822ec7614fa85322f7fa07e6f369c0888e1107f9f297f76a14e18c20c5`). **ABSENT** — baseline bytes are not a landing. **S2 report ABSENT.**
- S3 `corpus/fixtures/r99-window-lapse/` JSON tables + `fictional-excerpts.md`, plus byte copies of the files it does not author. Directory present from before poll i=0 (10 files, no extras). Set-hash `347c1d92b13a09b69be4dbf8cae1e4876bfea9b0f3fd633e0412b56b402ee071` stable i=0 through i=39 and at 22:27:29. Report `S3-fixture-author.md` mtime `2026-10-17T22:01:40` size 5069. Content not adjudicated.
- S4 `corpus/fixtures/r99-window-lapse/README.md` (`b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049`) + `claim-excerpt-map.md` (`d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d`). Report `S4-fixture-docs.md` mtime `2026-10-17T22:03:54` size 9303. Both differ from r98. Content not adjudicated.
- S5 `corpus/knowledge/r99-gate-blind-spot-table.md` + `corpus/knowledge/r99-lapse-scope-note.md`. **ABSENT** at every poll sample and at 22:27:29, 22:30:19, and 22:37:57 (`ls` No such file; `find` under the lane found no `corpus/knowledge/r99-*`). **S5 report ABSENT.** Do not verify the planned table.
- Also still for L1, not present as r99 edits at 22:37:57: appended `LOG.md` results entry (hash unchanged `1f2ec354259ba6a4bebffe01fc949ef4ec8cd6a45fff512c8129adc05ee5f99a` through the poll and the 22:27 recheck), `SCORECARD.md` r99 rows (hash unchanged `9c67f5c83c82562b19e8b90df401c937a57423920167dd4f08473f95618a3c0e`), and `.ufo/waves/round-99/` bookkeeping (seat reports + receipt when written). No `receipt.json` under `.ufo/waves/round-99/` outside `seats/` at 22:27:29 (`find … -not -path '*/seats/*'` empty).
- **Fleet repo:** only `.ufo/reports/round-99/lore.md` is L1's to write. Still ABSENT. See §2.4 on MANIFEST.
- **L0:** `.ufo/l0-questions.md:33` is the open lore round-1 question; `:44` and `:45` are kotodama questions addressed at lore's intake. No r99 lore question appended.
- **No fleet prompt file** for this lane-round: `.ufo/prompts/lore-round-1.md` is the only `lore*` prompt (mtime 2026-10-15). `ls .ufo/prompts/ | grep round-99` → `NO_ROUND99_PROMPT`. Dispatch evidence rides `LOG.md` + the wave dir.
- **Watch item (carried defect class):** the watchdog still does not gate this lane. `scripts/shokunin-watchdog.sh:14` `LANES="protocol aggregator kasegi kengaku kake kumitate kotoba kagi kama"` (no `lore`). `:45` `report_of() { [ -f "$SK/.ufo/reports/round-$2/$1.md" ]; }` (existence-only; no content check), contrary to `PROTOCOL.md:175-191`. `.ufo/state/lore.round` is `1`, mtime 2026-10-15; `.ufo/state/lore.mission` is `2684656`, same day. The report content bar therefore rests on integrator review, not this driver.

Fixture vs `corpus/fixtures/r98-clerk-filing` at 22:14:55 (`diff -rq` + per-file sha256) and again at 22:27:29 (`diff -rq` lists the same five names only):

Identical to r98: `contradictions.json` `37517e5f…`, `entities.json` `db2d8e5d…`, `relations.json` `c279254b…`, `inspiration-note.md` `58f5390e…`, `source-excerpt.md` `b5edc2fd…`.

Differ: `sources.json` r98 `32ee15b1…` / r99 `8c215b38…`; `timeline.json` r98 `eb24e084…` / r99 `2cdb9fda…`; `fictional-excerpts.md` r98 `29e384bf…` / r99 `fefebaf9…`; `README.md` r98 `32efc78f…` / r99 `b9320941…`; `claim-excerpt-map.md` r98 `c1099d0e…` / r99 `d2fe20e5…`.

That is an observation of bytes, not a C2 pass. The round was still open; S2 and S5 had not landed.

## 3. Poll log — producer artifacts and seat landings

Cadence 20 s, 40 samples, `2026-10-17T22:04:21-03:00` → `2026-10-17T22:17:24-03:00` (`POLL DONE` and `POLL FINAL WRITTEN` both `22:17:24`). Raw log `.ufo/waves/round-99/seats/V35-scratch/poll.log` (40 `^i=` lines), changes `.ufo/waves/round-99/seats/V35-scratch/poll-changes.log`, final dump `poll-final.txt`. Self subtracted: count excludes `V35-shonen-format.md` (this file did not exist during the poll). Three samples recorded `sample_secs=1` (i=7, i=23, i=38); the other 37 were 0. Wall span 783 s / 39 intervals ≈ 20.08 s. Bounded slips, not fatal. No sample was skipped.

Pre-poll anchor (22:01:21): `git status --porcelain` was only `?? .ufo/waves/round-99/`. Tool files were not yet modified. Fixture directory already existed; several files still had 21:36 mtimes (r98 copy) while `fictional-excerpts.md`, `sources.json`, and `timeline.json` were already 22:01. S1's baseline→first-write edge and the fixture's pre-stable churn therefore happened before sample 0. The poll does not claim to have seen those edges.

| Event | Time | Evidence |
|---|---|---|
| S1 tool already non-baseline at i=0 | 22:04:21 | `1728ed892442…` (baseline `03d04365…`). First modification was between the 22:01:21 clean status and this sample |
| S1 tool second hash | 22:07:42 | i=10 `6f81f8be1974…`, stable i=10–i=39 and at 22:27:29 / 22:37 status still `M` |
| S1 contract churn | 22:04:21 → 22:09:02 | i=0 `73b28933…` → i=1 `8f9c1f53…` → i=14 `8c2561b0…`, stable i=14–i=39 and at the 22:27 recheck |
| S2 README + SKILL | unchanged | baseline hashes on all 40 samples and at 22:37:57. **ABSENT as a delivery** |
| r99 fixture | stable before i=0 | `fxn=10`, `fxh=347c1d92…`, `extra=none` on all 40 samples. Five files differ from r98, five byte-identical (see 2.5) |
| S5 both knowledge files | ABSENT | all 40 samples; `ls` failed at 22:27:29, 22:30:19, and 22:37:57 |
| Producer reports | 2/5 entire window | i=0 already `S3-fixture-author.md,S4-fixture-docs.md` (mtimes 22:01:40 and 22:03:54). Still only those two at 22:37:57. **S1, S2, S5 reports ABSENT.** A `find -name 'S*.md'` under the wave also hits scratch copies of `SKILL.md` and archived historical seats; those are not r99 producer reports. No `seats/S1*.md`, `S2*.md`, or `S5*.md` |
| Seat reports ex-self | 4 → 14 during the poll | i=0 = 4; i=39 = 14. Later spot checks, outside the protocol window: 20 at 22:27:29, 24 at 22:30:19, 51 at 22:37:57. Not 128. This report is additional and was excluded from those counts |
| Fleet report | ABSENT | all 40 samples and the 22:37:57 recheck. Expected (lands last) |
| `LOG.md` / `SCORECARD.md` | unchanged | `1f2ec354…` / `9c67f5c8…` on every change-record; still so at 22:27:29 |

Final digests at poll done (`sha256sum`, `poll-final.txt`):

```
6f81f8be19742372ddc6819f6cf50dad985fe2bca2bee2b6e7c579613f5f4067  corpus/tools/dependency_freeze.py
8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628  corpus/tools/dependency-freeze-contract.json
294dd56f29ce1fd40be3a80d365b33724c9cd1969d3f7b7abb271fd1adaaa207  corpus/tools/README.md
22ffaa822ec7614fa85322f7fa07e6f369c0888e1107f9f297f76a14e18c20c5  SKILL.md
d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d  corpus/fixtures/r99-window-lapse/claim-excerpt-map.md
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  corpus/fixtures/r99-window-lapse/contradictions.json
db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984  corpus/fixtures/r99-window-lapse/entities.json
fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d  corpus/fixtures/r99-window-lapse/fictional-excerpts.md
58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37  corpus/fixtures/r99-window-lapse/inspiration-note.md
b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049  corpus/fixtures/r99-window-lapse/README.md
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  corpus/fixtures/r99-window-lapse/relations.json
b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd  corpus/fixtures/r99-window-lapse/source-excerpt.md
8c215b38dc02400910ff935eab46ecf82b0381b63a75d092b03bd601a9915f15  corpus/fixtures/r99-window-lapse/sources.json
2cdb9fda5baae1a496b31c004a7e0a9345ac580b257da0d9a04c045214c4c069  corpus/fixtures/r99-window-lapse/timeline.json
```

`sha256sum` on the two S5 paths printed `No such file or directory`. Those paths stay **ABSENT**. Not a plan, not a partial table.

## 4. Side observations (not verdict-bearing)

- **Fleet-root stray (session-cwd class).** At seat open, `git -C /home/vgpnk/Projects/shokunin status --porcelain` was empty. At 22:27:29 it was `?? .ufo/waves/round-99/`. Confirmed path `/home/vgpnk/Projects/shokunin/.ufo/waves/round-99/` (fleet toplevel, not the lane). Directory mtime `2026-10-17 22:11:27 -0300`; `seats/` mtime `22:17:58`. `find` at 22:36:34: 8 files, all under `seats/V69-scratch/before/baseline-root/` (0-byte `dependency_freeze.py` and `dependency-freeze-contract.json`, empty `corpus/fixtures`) and `seats/V73-scratch/selftests/` (`boundary.err` 129 bytes, `map.err` 126, `freeze.err` 128; matching `.out` files 0 bytes). Recorded, not removed.
- **Lane stray into the previous wave.** At 22:36:34 and still at 22:37:57, lane `git status` included `?? .ufo/waves/round-98/seats/V58-scratch/original-run-resume-note.md`. It was not in the 22:27:29 non-wave status. Not this seat's write. Recorded, not removed.
- **Placeholder-poll hazard did not recur inside the poll window** for the r99 fixture: set-hash was already stable at i=0. It did occur before the poll (22:01 listing still had 21:36 mtimes on README and the map). An existence-only check in that minute would have accepted r98 bytes as the r99 docs. S4's rewrite had landed by i=0.
- **S1 kept rewriting after its first non-baseline bytes** (tool hash changed at i=10, contract at i=1 and i=14). A poll that stopped at first non-baseline would have frozen the wrong digest. Cutoff digest is the i=14+ stable pair, still the working-tree pair at 22:27. S1's report never appeared, so that stability is not a producer sign-off.
- **HEAD vs declared baseline:** HEAD `337f0fa` is two commits past `4265df5` (`111b9a3` SCORECARD only, `337f0fa` LOG only). Wave-tree diffs of producer files against `4265df5` match diffs against HEAD.
- **SKILL.md digest** `22ffaa82…` is the `4265df5` baseline, not the pre-closure digest the r98 seat recorded. Unchanged this round as of 22:37:57.

## Bottom line

**PASS** — `SHONEN.md` is canonical with four `[~]` and zero `[x]` at HEAD `337f0fa`: checker exit 0 (10/10) at 22:04:21 and again at 22:27:29, independent seed diff against `PROTOCOL.md:425-432` matches modulo `<name>`, named-root tampers (`[x]`, dropped box-2 evidence, fifth box) each exit 1 on only the intended checks, 13/13 pointers resolve, `8e5a68d` is an ancestor, digest `03b832c7…` unchanged since `9c2eea3`. The r99 fleet-report landing set is enumerated (path `.ufo/reports/round-99/lore.md` on the fleet repo, still ABSENT at 22:37:57 as expected; four sections in order; lands-last citation must be this re-dispatch's work commit, not `337f0fa` or `4265df5`; pathspec-limited report commit under lane identity; MANIFEST append is the integrator's, and the r94–r98 combined commits are a recorded attribution defect, not a license). Poll 40/40 (22:04:21→22:17:24, self subtracted): S1 bytes landed and stable (`6f81f8be…` / `8c2561b0…`) but **S1 report ABSENT**; **S2 ABSENT** (README and SKILL still baseline, report absent); S3/S4 fixture and reports present (10 files, five byte-identical to r98, five differ; content not adjudicated); **S5 ABSENT** (both knowledge files and the report), rechecked still absent at 22:37:57 — those deliveries are not verified. Fleet-root `.ufo/waves/round-99/` stray and a late `round-98` seat-scratch note recorded, not removed. Watchdog content-check gap re-confirmed (`shokunin-watchdog.sh:14,45`).
