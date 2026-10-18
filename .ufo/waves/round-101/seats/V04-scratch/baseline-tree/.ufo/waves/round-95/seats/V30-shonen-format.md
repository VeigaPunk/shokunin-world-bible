# V30 — shonen-format (round-95 verification seat, lore-shokunin)

**Seat role:** (a) verify `SHONEN.md` still carries the canonical four-box form with four
`[~]` and zero `[x]` (run the round-93 mechanical checker if present, then verify the
evidence pointers independently); (b) enumerate the round-95 fleet-report landing set for
L1 (path, sections, evidence requirements per `templates/round-prompt.md`); (c) poll for
late seats. LEAF scope: read-only checks; this report is my only write.

**Revision tested:** lane HEAD `fb118c42038ed27a747eec704b9aab41bb4b2ebe` (`fb118c4 lore
r94: close round — SCORECARD admitted section + LOG closure`, r94 closure baseline).
Working tree at check time: `git status --porcelain` → ` M LOG.md`, `?? .ufo/waves/round-95/`,
`?? corpus/fixtures/r95-crossing-aftermath/` (round in flight).

## 1. `SHONEN.md` — canonical form, four `[~]`, zero `[x]` (PASS)

Mechanical checker present and replayed — **exit 0, 10/10 PASS**:

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
SHA256 SKILL.md c930675a4ca614ecd8845a9f27be6c2e0e1d3b547c477a39245c82272e1e31b5
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

`SHONEN.md` is byte-unchanged against HEAD (empty `git diff HEAD -- SHONEN.md`), and
`SHONEN.md` SHA-256 `03b832c7…` is identical to the digest the r94 F28 seat recorded at
`65a9329` — no drift across r94 closure → r95 mid-round.

Every path named in the four evidence lines resolves (13/13), and the one cited commit
exists and is an ancestor of HEAD:

```
RESOLVES SKILL.md, LOG.md, reports/round-1/baseline-probes.json, PROVINCE.md,
         .ufo/waves/round-93/recovery/R08-skill-check.py,
         .ufo/waves/round-93/deepseek/{F21,F29,F01,F31,F03,F24}.md,
         .ufo/waves/round-93/deepseek/{F25-replay.py,F14-postrepair-check.py}
$ grep -c "Fleet round 1 — calibration declaration before batched dispatch" LOG.md → 1
$ sed -n '3,11p' PROVINCE.md → owns/refuses/scope text (box4 pointer resolves in range)
$ git cat-file -t 8e5a68d → commit ; git merge-base --is-ancestor 8e5a68d HEAD → ANCESTOR yes
$ git log --oneline -1 8e5a68d → 8e5a68d lore r93: record DeepSeek review and resolve source precision findings
```

Governing gate text re-checked: `PROTOCOL.md:63-68` — `[x]` requires a reviewer who did not
author the round's changes, and a lane-dispatched subagent is still the lane; so the 64
round-95 seats cannot convert any box to `[x]`. `PROTOCOL.md:417` + `423-435` fix the
canonical seed and the marks-only-plus-one-evidence-line form.

**Verdict:** PASS — four `[~]`, zero `[x]`, form canonical, all pointers live.

## 2. Round-95 fleet-report landing set for L1

Authority chain: `templates/round-prompt.md` §4 (report contract) + §5 (commit/push),
`PROTOCOL.md:100-108` (five child-lane items), `PROTOCOL.md:117-153` (lands-last, minimum
content, SHONEN heading), `PROTOCOL.md:154-170` (stale-lane actuator), `PROTOCOL.md:455-471`
(commit/push scope, pathspec rule).

### 2.1 Primary artifact — the round report

| Item | Value |
|---|---|
| Path | `/home/vgpnk/Projects/shokunin/.ufo/reports/round-95/lore.md` |
| Repo | fleet repo (`/home/vgpnk/Projects/shokunin`), not the lane repo |
| Name | `<id>` = roster id `lore` (`MANIFEST.json` roster row `id: lore`); any other name does not satisfy the contract (`PROTOCOL.md:138-139`) |
| State at 16:2x | ABSENT — `ls /home/vgpnk/Projects/shokunin/.ufo/reports/round-95/` → `No such file or directory` (dir created only when L1 files the report) |
| Precedent | `round-93/lore.md` committed `2255b87` by `lore-shokunin <lore@shokunin.local>`; `round-94/lore.md` committed `be6eca9` by the same lane identity (swept into the protocol closure commit) |

### 2.2 Required sections, in order (`templates/round-prompt.md:64-74`)

1. **Work performed** — opens by naming the round's declared claims (r95: C1/calibration,
   C2/depth, C3/coverage — `LOG.md` round-95 declaration tail) and their target axes; then
   one bullet per work item, **each carrying an evidence pointer** (path:line, command
   output, or commit hash).
2. **Landed changes** — every change **tied to a `LOG.md` entry and to the commit hash**
   that carries it.
3. **Before → after measurements** — one per claim, **each with the counting command and
   the commit it was measured against**.
4. **SHONEN** — one line per box of `SHONEN.md`: `[x]` only with a named non-author
   verifier, `[~]` with a resolvable evidence pointer, `[ ]` if untouched. For r95 all four
   lines must be `[~]` (same-lane seats are the lane; no promotion).

### 2.3 Evidence requirements (protocol minimum content, `PROTOCOL.md:144-153`, `178-183`)

- Work performed **plus at least one evidence pointer**; changes landed in the child repo
  each tied to a `LOG.md` entry; **cross-domain evidence with the domain named**; and a
  **checkable commit-hash citation** — the hash must exist in the lane repo and be an
  ancestor of lane `HEAD` (`git merge-base --is-ancestor <hash> HEAD`).
- The `SHONEN` heading is mandatory: "A report without this heading does not satisfy the
  contract even if the same facts appear elsewhere in it"; omission = conformance defect
  **and** disqualification as promotion evidence, re-filed next round.
- **Marker rule** (`templates/round-prompt.md:75-78`): a contentless report (placeholders,
  missing required sections, no evidence pointers) = round **failed**; real committed work
  but missing sections = `ok` + minimum-content conformance defect.
- **Lands last**: report written only after the lane's child-repo work is committed, and it
  cites that commit's hash (`PROTOCOL.md:117-127`).
- **Stale-lane actuator** (`PROTOCOL.md:154-170`): the report must list any mission open
  longer than two driver ticks with `progressing` / `progressing-weak` / `silent` (activity
  measured from the launch timestamp, not the tick counter).
- **Honest defect accounting** (r94 precedent, carried forward): failed-output gaps and
  uncredited seats are named, not smoothed.

### 2.4 Commit / push rules for the landing (`templates/round-prompt.md:80-86`, `PROTOCOL.md:455-471`)

- Round end: commit (`round-95`) inside the lane repo, then push; **also commit and push
  the report on the fleet repo**.
- Fleet-repo commit is **pathspec-limited**: `git commit -- .ufo/reports/round-95/lore.md`
  — never `commit -a` / `add -A` (sibling in-flight edits).
- Push scope: fleet repo remote + own lane remote only; domain source trees read-only.
- `.ufo/waves/` (seat reports, receipts, wave-spec) is committed with the round's
  integration commit; `.ufo/state/` and `.ufo/watchdog.log` must never be committed by a lane.
- Corrections land as new commits, never by amending a cited one; append-only files take
  appended correction entries.

### 2.5 Round-95-specific landing items observed

- Lane repo (L1 + producers): `corpus/tools/map_obligations.py` + contract JSON (P1/P2),
  `corpus/fixtures/r95-crossing-aftermath/` (P3/P4), `corpus/knowledge/r95-aftermath-scope-note.md`
  (P5), `LOG.md` round-95 entry, `SCORECARD.md` rows, `.ufo/waves/round-95/` bookkeeping
  (wave-spec, seat reports V01–V59 + P1–P5, dispatch receipts).
- Fleet repo: only `.ufo/reports/round-95/lore.md` is L1's to write; the `MANIFEST.json`
  `rounds[]` append is the protocol lane's integrator act, not L1's.
- No `.ufo/prompts/lore-round-95.md` exists at the fleet root (`ls .ufo/prompts/ | grep -c lore` → 1,
  the round-1 prompt only) — same as r93/r94; dispatch evidence for this lane rides
  `LOG.md` + the wave dir, not a prompt file (see §4).

## 3. Poll log — late seats and producer artifacts

Poll cadence per seat spec: 20 s, bounded. Target paths checked: P1
`corpus/tools/map_obligations.py`, P2 `corpus/tools/map-obligations-contract.json` (+
`corpus/tools/README.md`), P3/P4 `corpus/fixtures/r95-crossing-aftermath/` (10 files when
complete: 5 JSON/MD byte copies + modified `sources.json`/`timeline.json`/`fictional-excerpts.md`
+ README + claim-excerpt-map), P5 `corpus/knowledge/r95-aftermath-scope-note.md`, and seat
reports `.ufo/waves/round-95/seats/*.md`.

| Poll | Time (local) | P1 tool sha256[:16] | P2 contract sha256[:16] | fixture files | P5 | seat reports |
|---|---|---|---|---|---|---|
| 0 | 16:18 | `cc1df4dc406870b6` (= baseline) | `349a1956714c4496` (= baseline) | 8 | ABSENT | 1 (V38) |
| 1–10 | 16:19:50–16:22:50 | `cc1df4dc` → `c37f298b` → `28d308be` | `349a1956` (baseline) | 8 → 10 | ABSENT | 1 → 8 |
| 11–20 | 16:23:16–16:26:16 | `ca05159e` → `74a88346` → `8eb5051d` → `3f87fe8b` → `9224a684` | `349a1956` (baseline) | 10 | **PRESENT** (16:23) | 8 → 16 |
| 21–30 | 16:26:49–16:29:49 | `d1c239cc` (stable) | **`8173bb97`** (landed 16:27) | 10 | PRESENT | 16 → 31 |
| 31–40 | 16:30:21–16:33:21 | `d1c239cc` | `8173bb97` | 10 | PRESENT | 31 → 49 |
| 41–50 | 16:33:49–16:36:49 | `d1c239cc` | `8173bb97` | 10 | PRESENT | 50 → **54** (plateau from 16:35:09) |

Baseline digests (recorded pre-r95 by V38, re-confirmed here at poll 0): tool `cc1df4dc…`,
contract `349a1956…`. Landing times observed: P3 fixture complete 10/10 at 16:21:30 (poll 6);
P5 note at 16:23:16 (poll 11); P2 contract at 16:27:09 (poll 22); P1 tool first non-baseline
write 16:22:30 (poll 9), final digest `d1c239cc` stable from 16:26:49 (poll 21). The fleet
report `.ufo/reports/round-95/lore.md` stayed **ABSENT** through all 50 polls (round open; the
report lands last).

Final digests at 16:37 (`sha256sum`):

```
d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108  corpus/tools/map_obligations.py
8173bb97592a377716866737e8fcb4043014c9814e77a6248500d301a39170db  corpus/tools/map-obligations-contract.json
f87ed42ad4d42143bb84f13539f2db8ca0d5f221aaf4eaffdbd6874b5ef1ab9a  corpus/knowledge/r95-aftermath-scope-note.md
5d033c9db8a72801c9b8d5e609e01cddf1ace668711e24d0476b8cbd6879a264  corpus/tools/README.md
$ diff -rq corpus/fixtures/r94-paired-crossing corpus/fixtures/r95-crossing-aftermath
Files …/claim-excerpt-map.md differ ; …/fictional-excerpts.md differ ; …/README.md differ ;
…/sources.json differ ; …/timeline.json differ        (exactly the 5 declared modifications;
the other 5 files are byte copies)
```

Seat census at cutoff 16:36:49: 54 `.md` files in the lane seats dir; producers P1–P5 all
landed (P1-tool-code, P2-contract-docs, P3-fixture-json, P4-fixture-docs, P5-knowledge-note);
49 of 59 verifier seats landed. Verifier seats not present at cutoff: `V09, V18, V29, V30
(this seat — filed, see §4), V33, V46, V53, V56, V57, V59`. Lane tree at cutoff: `M LOG.md`,
`M corpus/tools/{map_obligations.py,map-obligations-contract.json,README.md}`,
`?? corpus/fixtures/r95-crossing-aftermath/`, `?? corpus/knowledge/r95-aftermath-scope-note.md`,
`?? .ufo/waves/round-95/` — no round work committed yet (lane HEAD still `fb118c4`), which is
consistent with the round being open at my cutoff.

## 4. Side observations (not verdict-bearing)

- **Cross-repo path-resolution hazard — self + 2 siblings (defect class, needs L1 action).**
  The harness resolves relative write paths against the session cwd
  (`/home/vgpnk/Projects/shokunin`, the fleet root), not the lane repo: this seat's report
  first landed at `/home/vgpnk/Projects/shokunin/.ufo/waves/round-95/seats/V30-shonen-format.md`
  (10999 bytes, 16:19) instead of the lane path. It was moved to
  `lore-shokunin/.ufo/waves/round-95/seats/V30-shonen-format.md` at 16:37 (lane count 54 → 55).
  Two sibling seats show the same hazard **unresolved**:
  `find /home/vgpnk/Projects/shokunin/.ufo/waves/round-95 -type f` →
  `…/seats/V09-c2-inherited-equality.md`, `…/seats/V18-scope-creep.md` — i.e. V09 and V18 filed
  at the **fleet root**, untracked there (`git -C /home/vgpnk/Projects/shokunin status
  --porcelain` → `?? .ufo/waves/round-95/`), and absent from the lane seats dir (both were in my
  missing list). If left, those two reports are attribution-defective and outside the seat spec's
  declared path (`lore-shokunin/.ufo/waves/round-95/seats/`); L1 should move them or record the
  defect. Same class as the r94 F28 seat's F02-at-fleet-root observation.

- **Watchdog still does not gate this lane** (re-confirmation of the r94 F28/CC-12 finding):
  `/home/vgpnk/Projects/shokunin/scripts/shokunin-watchdog.sh:45` is
  `report_of() { [ -f "$SK/.ufo/reports/round-$2/$1.md" ]; }` — existence-only, no content
  validation — and `:14` `LANES="protocol aggregator kasegi kengaku kake kumitate kotoba kagi kama"`
  omits `lore`; `.ufo/state/lore.round` → `1` while the lane is on its 95th steered round.
  So the report content bar rests on integrator review, not the driver.
- **No fleet prompt file for this lane-round** (`.ufo/prompts/lore-round-95.md` absent), so
  the step-1 prompt-fidelity check has no artifact to read for r95; the declaration in
  `LOG.md` is the mission-content record.
- **`SHONEN.md` regeneration risk is nil this round**: no writer but the lane may touch it
  (`PROTOCOL.md:417`), and the file is byte-identical to the r94 closure revision.

## Bottom line

**PASS** — `SHONEN.md` is canonical with four `[~]`, zero `[x]`, and the mechanical form
checker replays exit 0 (10/10 PASS) at HEAD `fb118c4` and again after all five producer
artifacts landed; the file is byte-unchanged (`03b832c7…`, empty `git diff HEAD -- SHONEN.md`),
all 13 evidence pointers resolve, and the one cited hash `8e5a68d` is an ancestor of HEAD. The
round-95 fleet-report landing set for L1 is enumerated with exact pointers (path
`.ufo/reports/round-95/lore.md` on the fleet repo; Work performed / Landed changes /
Before → after measurements / SHONEN in order; per-item evidence pointers, `LOG.md`-tied
landed changes, counting-command measurements, checkable commit-hash citation, pathspec-limited
fleet commit). Poll: all producer artifacts landed (P1 `d1c239cc…`, P2 `8173bb97…`, P3/P4
fixture 10 files with exactly the 5 declared modifications, P5 `f87ed42a…`) and 54/64 seat
reports were in the lane seats dir at cutoff; `.ufo/reports/round-95/lore.md` was still ABSENT
at cutoff (round open, report lands last — expected). One defect recorded for L1: harness cwd
made three seat reports land at the fleet root instead of the lane path — this seat's was
corrected, `V09` and `V18` remain stranded there.
