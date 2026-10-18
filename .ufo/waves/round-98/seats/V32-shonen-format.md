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

(within the minute the producers' files joined: ` M
corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md`, `?? corpus/fixtures/r98-clerk-filing/`).

## 1. `SHONEN.md` — canonical, four `[~]`, zero `[x]` (PASS)

Mechanical checker (`.ufo/waves/round-93/deepseek/F29-shonen-format-check.py`) replayed
twice — at seat open and again after all five producer reports and artifacts had landed —
**exit 0, 10/10 PASS** both times (output below is the post-producer replay; the seat-open
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

Byte-unchanged — `git diff HEAD -- SHONEN.md | wc -l` → `0` (re-checked at the 20:43:30
cutoff) and `git diff 9a3d648 -- SHONEN.md | wc -l` → `0`; also `git diff 9c2eea3 --
SHONEN.md | wc -l` → `0` (the r93 commit that last touched it). Digest `03b832c7…`
equals the value recorded by the r94 F28, r95 V30, r96 V39 and r97 V36 seats — no drift
across five closures.

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
`.ufo/waves/round-93/deepseek/{F21,F29,F01,F25-replay.py,F31,F14-postrepair-check.py,F03,F24}.md`),
the LOG entry named in box 2 exists once (`grep -c "Fleet round 1 — calibration
declaration before batched dispatch" LOG.md` → `1`), the `PROVINCE.md:3-11` citation is in
range (owns/refuses/scope text), and the cited commit is real and an ancestor:

```
$ git cat-file -t 8e5a68d → commit
$ git merge-base --is-ancestor 8e5a68d HEAD → ANCESTOR yes
$ git log --oneline -1 8e5a68d → 8e5a68d lore r93: record DeepSeek review and resolve source precision findings
```

**Negative controls (the PASS is not vacuous).** Sandbox copy of the checker at
`V32-scratch/negctl/a/b/c/d/check.py` (its root resolves to `parents[4]` = the sandbox
dir, with `SHONEN.md`/`LOG.md`/`PROVINCE.md`/`SKILL.md`/`reports/round-1/baseline-probes.json`
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
| State at seat open | ABSENT — `ls /home/vgpnk/Projects/shokunin/.ufo/reports/round-98/` → `No such file or directory`; still ABSENT at the 20:43:30 cutoff (lands last) |
| Precedent | r94 `be6eca9`, r95 `07ea34b`, r96 `5e03802`, r97 `80ca9dd` — each authored `lore-shokunin <lore@shokunin.local>`, subject `protocol: close lore rN (admitted) — fleet report + MANIFEST ledger append`; each carries the report plus the `MANIFEST.json` rounds append in the one commit (r97: report 84 lines + MANIFEST 196-line diff) |

### 2.2 Required sections, in order (`templates/round-prompt.md:64-74`)

1. **Work performed** — opens by naming the round's declared claims (r98: C1/calibration,
   C2/coverage, C3/depth — `LOG.md:3086` "## Round 98 — declaration before dispatch
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
  byte-ownership per the round declaration `LOG.md:3135-3143`; baseline = `9a3d648`,
  hashes below captured via `git show 9a3d648:<path> | sha256sum`):
  - S1 `corpus/tools/dependency_freeze.py` (baseline `b06275f3…`; delivered `03d04365…`)
    + `corpus/tools/dependency-freeze-contract.json` (baseline `27273be2…`; delivered
    `153ebc5b…`)
  - S2 `corpus/tools/README.md` (baseline `8678abc1…`; delivered `1d299c16…`)
  - S3 `corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md` (repair only;
    baseline `30281ff1…`; delivered `80440d61…`) + `corpus/fixtures/r98-clerk-filing/`
    {entities,sources,timeline}.json + fictional-excerpts.md + byte copies of the other 7
    files from `9a3d648`
  - S4 `corpus/fixtures/r98-clerk-filing/README.md` (`32efc78f…`) + `claim-excerpt-map.md`
    (`c1099d0e…`)
  - S5 `corpus/knowledge/r98-clerk-scope-note.md` (ABSENT at seat open; delivered
    `1162262c…`) + dated correction addenda in
    `corpus/knowledge/r95-aftermath-scope-note.md` (baseline `f87ed42a…`; delivered
    `8e9e1774…`) and `corpus/knowledge/r96-response-scope-note.md` (baseline `6db32ca2…`;
    delivered `a9b51f8c…`)
  plus `LOG.md` (r98 declaration + results entry), `SCORECARD.md` (r98 rows; untouched at
  this cutoff), and `.ufo/waves/round-98/` bookkeeping (seat reports + receipt when
  written). The lane `git status --porcelain` at the 20:43:30 cutoff shows exactly this
  write set: ` M LOG.md`, ` M` r95 map, ` M` r95/r96 notes, ` M corpus/tools/README.md`,
  ` M` contract, ` M dependency_freeze.py`, `?? .ufo/waves/round-98/`, `?? 
  corpus/fixtures/r98-clerk-filing/`, `?? corpus/knowledge/r98-clerk-scope-note.md`.
- **Fleet repo**: only `.ufo/reports/round-98/lore.md` is L1's to write; the
  `MANIFEST.json` `rounds[]` append is the integrator-of-record's act, not L1's
  (`PROTOCOL.md:192-208`) — observed r94–r97 precedent lands both in one lane-authored
  commit (see 2.1). **Stray watch:** the fleet root gained one in-round untracked file,
  `baseline-analyze.txt` (105 bytes, mtime 20:30:10; content = `python3: can't open file
  '/home/vgpnk/Projects/shokunin/analyze.py'`), i.e. the r94-F01 session-cwd stray class
  recurred this round; recorded, not removed (read-only seat).
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

## 3. Poll log — producer artifacts and seat landings

Cadence 20 s, 40 samples, 20:28:52 → 20:41:52 (`POLL DONE 20:42:12`); raw log at
`.ufo/waves/round-98/seats/V32-scratch/poll.log` (script `poll.sh`, summarizer
`poll-summarize.py` in the same scratch dir). Baselines at poll 0 (= r97 closure
`9a3d648`, verified via `git show 9a3d648:<path> | sha256sum`): S1 tool `b06275f3…`,
S1 contract `27273be2…`, S2 README `8678abc1…`, S3 r95 map `30281ff1…`, S5 r95 note
`f87ed42a…`, S5 r96 note `6db32ca2…`, S5 r98 note ABSENT, r98 fixture ABSENT at seat open
(10 files by poll 0 — S3's byte copy landed 20:28:24), 0 producer reports, 0 seat
reports, fleet report absent.

| Event | Time | Evidence (poll i) |
|---|---|---|
| S3 r95 map first non-baseline | 20:28:52 | `s3m=80440d61…` (s0), stable through s39; whole-file diff vs `9a3d648` = exactly one prose line (`## Timeline normalization and scope`; data rows byte-unchanged) |
| r98 fixture set-hash churn | 20:28:52 → 20:30:52 | `fx=10` throughout; `fxh` 88646ef8 (s0) → b3f2cb10 (s4) → dcb7c9c0 (s5; S4 map mtime 20:30:21) → a2f0f34b (s6; S4 README mtime 20:30:41), stable through s39 |
| S5 r95/r96 note addenda | 20:29:32 | `s5b=8e9e1774…`, `s5c=a9b51f8c…` (s2), stable through s39 |
| S1 tool first non-baseline | 20:31:32 | `1a01fd17…` (s8) → `03d04365…` (s9, 20:31:52), stable s9–s39 |
| S1 contract first non-baseline | 20:31:32 | `3a940a9f…` (s8) → `c435239d…` (s13) → `153ebc5b…` (s15, 20:33:52), stable s15–s39 |
| S5 r98 note first write | 20:32:32 | `a73cd57b…` (s11) → `1162262c…` (s13, 20:33:12), stable s13–s39 |
| S2 README first non-baseline | 20:33:52 | `cefd7452…` (s15) → `1d299c16…` (s16, 20:34:12), stable s16–s39 |
| Producer reports | 20:31:12 → 20:35:32 | `prods` 0→1 @s7 (S3), →2 @s10 (S4), →3 @s15 (S5), →4 @s18 (S2), →5 @s20 (S1); final mtimes S3 20:31:25, S4 20:32:06, S5 20:34:00, S2 20:34:53, S1 20:35:33 (several rewritten after first sighting) |
| Seat reports | 0 → 57 | first at 20:29:52 (s3); 56 at 20:41:12 (s37); 57 `.md` incl. the 5 producers at the 20:43:30 final check |
| Fleet report | ABSENT | through all 40 samples and at the 20:43:30 final check — expected: the report lands last, after the lane commits |

Final digests at 20:42–20:43 (`sha256sum`, full):

```
03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b  corpus/tools/dependency_freeze.py
153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947  corpus/tools/dependency-freeze-contract.json
1d299c16bf9a0b34526f4a799cdd3117867f6d4d278866b66366b78700d79b84  corpus/tools/README.md
80440d61122488a267a4f0a58a55cb54d89c037d93160f1123e5fb3b2f396f61  corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md
1162262c742441115681d30be588039be4f1a026b755eeb7d15c9ba41952a4b8  corpus/knowledge/r98-clerk-scope-note.md
8e9e1774c1072bd1476d86977804e945301e4583acbfcb80a81b37a2334d4827  corpus/knowledge/r95-aftermath-scope-note.md
a9b51f8ccd78e0dcd8b5e890183068e48cdccd195065c43212211b65ee25f048  corpus/knowledge/r96-response-scope-note.md
db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984  corpus/fixtures/r98-clerk-filing/entities.json
32ee15b1f3d72d94f4228cbc9cefa69b7185d18b47bbe219833d7aaf30eed0f3  corpus/fixtures/r98-clerk-filing/sources.json
eb24e0848e597efa29ed858cb8557d8f3126a47e1231f9469d719257e191e7af  corpus/fixtures/r98-clerk-filing/timeline.json
29e384bf2eb2ab80858ace9423f29088a552553f87da7f6a9b694cbb050666de  corpus/fixtures/r98-clerk-filing/fictional-excerpts.md
32efc78f70e6de4f9670134080711923199e8693015d3ebea75a4a1ca6362926  corpus/fixtures/r98-clerk-filing/README.md
c1099d0ee9eece241ea1f796320a84453dfc6b6aec33b7b9dd7e39bbef4a94ba  corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md
```

Fixture at cutoff: 10 files; `diff -rq corpus/fixtures/r97-crossing-acknowledgment
corpus/fixtures/r98-clerk-filing` lists exactly six differing files
(`claim-excerpt-map.md`, `entities.json`, `fictional-excerpts.md`, `README.md`,
`sources.json`, `timeline.json`) and no other difference — the four byte-copy files
(`contradictions.json`, `inspiration-note.md`, `relations.json`, `source-excerpt.md`) are
byte-identical to r97. Caveat: the round is open at this cutoff — these are the delivered
revisions as polled; content adjudication belongs to the C1/C2/C3 verifier seats, not this
seat.

## 4. Side observations (not verdict-bearing)

- **Placeholder-poll hazard (S3 report D1, independently confirmed).** Between 20:28:24
  and 20:30:21/20:30:41 the r98 fixture's `README.md`/`claim-excerpt-map.md` existed with
  r97's bytes (S3's copy step; S4's rewrites landed at those mtimes), so an
  existence/count-only poll can be satisfied by a placeholder. This seat's poll hashes the
  whole fixture set (`fxh`) and saw the churn; a content check (e.g. `cmp` against r97 or
  the map's 20-row inventory) is required. The mirror case also occurred: S3's report
  (landed 20:31:12–25) says "README.md is still byte-identical to r97's README (S4's
  rewrite not yet landed)", but S4's rewrite had landed at 20:30:41 — S4's report records
  the same contradiction (its §"sha256 `32efc78f…` (r97's was `d9387b7d…`)"); observed
  evidence, not a verdict on either seat.
- **Digest-drift note**: `SKILL.md` `2b5bf27f…` vs the r97 seat's recorded `a2f1e4c6…`
  (r97 closure's 5+/5- registry-row pass); box-1 pointer still resolves. `SHONEN.md`
  `03b832c7…` and `PROVINCE.md` `94a7a77e…` unchanged.
- **Baseline vs HEAD**: HEAD `dd4df1b` is one commit past the declared baseline `9a3d648`;
  the extra commit touches only `SCORECARD.md` (+33 lines, r97 admission section). Wave-tree
  diffs against `9a3d648` are therefore exact for the producer files.
- **r95 map repair shape (observed)**: `git diff` vs `9a3d648` is exactly one prose line
  (the "new relation" sentence replaced with relation + tick-11 event wording); S3's
  report claims support_check/map_obligations receipts byte-identical pre/post and the r95
  freeze pin still PASS at `d541ae64…` — receipt re-verification belongs to the C2/C3
  seats.
- **Fleet repo**: clean at seat open; at the 20:43:30 cutoff exactly one untracked stray
  (`baseline-analyze.txt`, see 2.5). No r98 files under `.ufo/waves/round-98` outside the
  seats dir or under `reports/` (`find … -path '*round-98*' -type f` → only seat
  reports).
- **Seat-report count** at the 20:43:30 cutoff: 57 `.md` files (5 producers + 52
  verifier/judge seats); this report makes 58.

## Bottom line

**PASS** — `SHONEN.md` is canonical with four `[~]` and zero `[x]` at HEAD `dd4df1b`: the
mechanical form checker replays exit 0 (10/10 PASS) both before and after all five
producer reports/artifacts landed, an independent diff of the seed against
`PROTOCOL.md:425-432` matches modulo `<name>`, three tamper classes (mark flip to `[x]`,
dropped evidence line, added fifth box) each fail the checker with exit 1, all 13 evidence
pointers resolve, the cited hash `8e5a68d` is an ancestor of HEAD, and the file is
byte-unchanged (`03b832c7…`, empty `git diff HEAD`, identical to r93 `9c2eea3`). The
round-98 fleet-report landing set for L1 is enumerated with exact pointers (path
`.ufo/reports/round-98/lore.md` on the fleet repo — still ABSENT at the 20:43:30 cutoff,
as expected; Work performed / Landed changes / Before → after measurements / SHONEN in
order; per-item evidence pointers; `LOG.md`-tied landed changes; counting-command
measurements; checkable commit-hash citation; `SHONEN` heading mandatory;
pathspec-limited fleet commit under lane identity; stale-lane actuator line; five
producers' baseline→delivered hashes; one in-round fleet-root stray recorded). Poll
(20 s × 40, 20:28:52 → 20:41:52): all five producer artifacts landed — S1
`03d04365…`/`153ebc5b…`, S2 `1d299c16…`, S3 `80440d61…`, S4 `32efc78f…`/`c1099d0e…`, S5
`1162262c…`/`8e9e1774…`/`a9b51f8c…` — and all five producer reports by 20:35:32; r98
fixture 10/10 with exactly six differing and four byte-identical files vs r97; 57/64 seat
reports at cutoff; no strays under the round paths; fleet report absent; watchdog
content-check gap re-confirmed (`shokunin-watchdog.sh:14,45`).
