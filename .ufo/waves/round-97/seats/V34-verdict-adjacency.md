# V34 — verdict-adjacency (round 97)

**Seat:** V34 verdict-adjacency, round-97 single wave, lane `lore-shokunin`.
**Subject:** the delivered r97 working tree vs the declared baseline `f3e09f9` (`f3e09f9121ba6c42f2ea55a36b53e0e97bcf5e93`, "lore r96: freeze admitted wave + closure docs"); HEAD is `2393934` (`2393934237ea076366f3db6dceeff033edb52ab1`, "lore r96: close round — SCORECARD admitted section", a post-baseline r96-closure commit, `git diff f3e09f9 2393934` → `SCORECARD.md | 31 +++++`). No r97 commit exists (hard rule: no commits), so every measurement below is **worktree-vs-baseline**, not commit-range.
**Mandate:** one ADJACENCY verdict — province charter identity, province-scope diff of the round, no writes outside the lane, mythology content editorial-only in the new bytes, rights/canon/mechanics language scan, no commits/pushes. This seat makes no C1/C2/C3 verdict, no admission verdict, and no lore-truth ruling. Full battery, no placeholders.
**Measurement freeze:** all six producer reports present at 18:56:34 -03:00; every producer artifact mtime precedes its report mtime (§A7). Battery 18:57:0x–18:59:5x; delivered hashes re-measured at both ends and identical (`V34-scratch/freeze1.sha256` == `freeze2.sha256`, `diff` empty), plus a third confirmation at the last check (`STABLE`). All commands run from `/home/vgpnk/Projects/shokunin/lore-shokunin`. My only writes are this report and `.ufo/waves/round-97/seats/V34-scratch/` (`poll.sh`, `poll.log`, `freeze1.sha256`, `freeze2.sha256`, `r96-map-prerepair.md`, `r96-prerepair.sha256`).

## Poll-wait record (protocol compliance)

- First check 18:42:48: `art=6/17` (the 5 pre-existing tool files + the r96 map), `rep=0/6`. Loop 1: `.ufo/waves/round-97/seats/V34-scratch/poll.sh`, 40 tries × 20 s, log `V34-scratch/poll.log` (the shell task itself was reaped at its 900 s ceiling after readiness was already established by my own foreground watcher; the log is complete).
- Landing order observed: R4's r96 map repair 18:43:42 (hash changed `5093d72e…` → `e851f068…` mid-watch); r97 fixture JSON+md 18:44:16–18:44:30; R1 tool 18:45:37; R2 contract 18:46:12, README 18:47:13; R5 map 18:48:56 (from the r96 copy `e851f068…` to `49d4834e…`), README 18:49:14; R6 note 18:52:38; R3 tool iterated `fbaca38f…` → `7428dad4…` → `61cee7e5…` → final `b06275f3…` at 18:53:00, contract 18:55:14; reports R2 18:49:31, R4 18:50:14, R5 18:51:25, R1 18:52:25, R6 18:53:37, R3 18:56:23 — **6/6 at 18:56:34**.
- I verified only after the target bytes existed and all six producer reports were written; I never verified a plan. No ABSENT condition occurred. Interim states were recorded as observations only (e.g. at 18:44 the r97 `README.md`/`claim-excerpt-map.md` were still byte-identical copies of the repaired r96 files, `ff52ced4…`/`e851f068…`; R5 replaced both at 18:48:56/18:49:14 before its report).

---

## A1 — PROVINCE.md byte-identical to `f3e09f9`

```
$ sha256sum PROVINCE.md
94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa  PROVINCE.md
$ git show f3e09f9:PROVINCE.md | sha256sum
94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa  -
$ git hash-object PROVINCE.md
7c599c395e1710b6a7c7aca6d485c373bed6deb7
$ git rev-parse f3e09f9:PROVINCE.md
7c599c395e1710b6a7c7aca6d485c373bed6deb7
$ git diff f3e09f9 -- PROVINCE.md | wc -c
0
```

Blob identity, sha256 and the byte diff all agree; `PROVINCE.md` appears in neither the tracked diff nor the untracked list.

**Result: PASS — the charter that defines the province is untouched.**

---

## A2 — province-scope diff of the round

### A2.1 Change set

```
$ git diff --name-status f3e09f9
M	LOG.md
M	SCORECARD.md
M	corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
M	corpus/tools/README.md
M	corpus/tools/dependency-freeze-contract.json
M	corpus/tools/dependency_freeze.py
M	corpus/tools/map-obligations-contract.json
M	corpus/tools/map_obligations.py

$ git diff --name-status HEAD
M	LOG.md
M	corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
M	corpus/tools/README.md
M	corpus/tools/dependency-freeze-contract.json
M	corpus/tools/dependency_freeze.py
M	corpus/tools/map-obligations-contract.json
M	corpus/tools/map_obligations.py
```

Attribution: `LOG.md` is the pre-dispatch r97 declaration (uncommitted, same convention as r94–r96). `SCORECARD.md`'s delta is **committed in `2393934`**, not an r97 write — `git diff HEAD -- SCORECARD.md | wc -c` → `0`, and it is exactly the r96 closure continuation sitting above the declared baseline. The remaining six modified files are exactly the declared byte ownership: R1 `map_obligations.py`; R2 `map-obligations-contract.json` + `README.md`; R3 `dependency_freeze.py` + `dependency-freeze-contract.json`; R4 `r96-crossing-response/claim-excerpt-map.md` (cosmetic repair only).

### A2.2 Blob-level corpus comparison (in-place edits cannot hide behind unchanged path names)

```
base corpus files: 1804
CHANGED: ['corpus/fixtures/r96-crossing-response/claim-excerpt-map.md',
          'corpus/tools/README.md', 'corpus/tools/dependency-freeze-contract.json',
          'corpus/tools/dependency_freeze.py', 'corpus/tools/map-obligations-contract.json',
          'corpus/tools/map_obligations.py']
ADDED count: 11
  A corpus/fixtures/r97-crossing-acknowledgment/{README.md,claim-excerpt-map.md,contradictions.json,
    entities.json,fictional-excerpts.md,inspiration-note.md,relations.json,source-excerpt.md,
    sources.json,timeline.json}
  A corpus/knowledge/r97-acknowledgment-scope-note.md
MISSING: []
```

Exactly the declared ownership: 6 modified files (4 tool files + 1 contract + the r96 map), 10 new fixture files (R4's 8 + R5's 2), 1 knowledge note (R6). No inherited fixture other than the declared r96 map was touched:

```
$ git diff --stat f3e09f9 -- corpus/fixtures/
 corpus/fixtures/r96-crossing-response/claim-excerpt-map.md | 4 ++--
 1 file changed, 2 insertions(+), 2 deletions(-)
```

### A2.3 Untracked audit (lane-internal)

```
$ git status --porcelain -uall | grep '^??' | grep -v '^?? .ufo/waves/round-97/'
?? corpus/fixtures/r97-crossing-acknowledgment/README.md
… (exactly the 11 declared corpus additions, 11 lines total) …
?? corpus/knowledge/r97-acknowledgment-scope-note.md
```

Every untracked path outside `.ufo/waves/round-97/` is one of the 11 declared corpus additions. All other untracked volume (8,719 paths under `.ufo/waves`, plus the transient lane-root self-test dirs in §O1) is seat reports and verifier scratch inside the wave's declared area. Round-97's top level holds only `seats/` — no stray files. No parent-tree stray wave directory: `ls -d /home/vgpnk/Projects/shokunin/.ufo/waves/round-97` → `No such file or directory` (the r94/r95 defect class did not recur). Past waves untouched: `git diff --name-only f3e09f9 -- .ufo/waves/ | grep -v round-97` → empty. Root docs untouched: `git diff --stat f3e09f9 -- PROVINCE.md SHONEN.md SKILL.md README.md l0-questions.md .gitignore corpus/README.md` → empty.

### A2.4 New files are ordinary lane files

All 10 r97 fixture files and the knowledge note are regular mode-644 files (`find … -printf '%m'` → `644` each; `find … -type l` → 0 symlinks); the five tool files are mode-644.

**Result: PASS — the round's change set is lane-local and exactly the declared byte ownership.**

---

## A3 — no writes outside `lore-shokunin`

### A3.1 Sibling lanes and domain trees

```
$ for d in /home/vgpnk/Projects/shokunin/*-shokunin; do n=$(find "$d" -newermt "2026-10-17 18:35" -type f -not -path "*/.git/*" | wc -l); echo "$n $(basename $d)"; done
0 audio-shokunin … 67 kotodama-shokunin … 6042 lore-shokunin … 0 tsukuroi-shokunin   (all others 0)
```

The only sibling-lane path touched in the window belongs to **`kotodama-shokunin`'s own concurrent rounds** (67 files); `lore-shokunin`'s 6,042 are this round's own seats/scratch. A lore-string leak scan returns nothing:

```
$ grep -rl "r97-crossing-acknowledgment\|acknowledgment-aru-records\|aru-acknowledgment-note\|r97-acknowledgment-scope-note" /home/vgpnk/Projects/shokunin/*-shokunin | grep -v lore-shokunin
(empty)
```

Parent-tree non-lane files in-window: `MANIFEST.json` (mtime 18:38:40) and `.ufo/l0-questions.md` (18:17:33) — fleet-level files; both contain **zero** r97 lore strings (`grep -c` → 0/0). No lore write to any sibling lane or domain source tree.

### A3.2 System-temp scratch — observed, reported exactly

```
$ find /tmp -maxdepth 1 -newermt "2026-10-17 18:35" | sort
/tmp
/tmp/.bun-1000-*.{node,so}   (3 bun runtime files)
/tmp/fake-contract-backup.json
/tmp/o
/tmp/opencode
$ sha256sum /tmp/fake-contract-backup.json
c65ac3bd4fc090d8696b5739a6e5971cc06aba4700ad7458b9f9b04a8e99a4d2  /tmp/fake-contract-backup.json
```

`fake-contract-backup.json` (18:44:18, 9,203 B) is byte-identical to the **r96-baseline** freeze contract (the pre-hardening bytes), i.e. a seat's backup copy of a lane artifact placed in system temp; `/tmp/o` (18:35:12) holds a self-test summary line; `/tmp/opencode` (18:56:42) is 40 B. None is a sibling repository or domain source tree, so none breaches `PROVINCE.md:11`. Disclosed as protocol-level evidence, not smoothed over. **Self-disclosure:** this seat created no `/tmp` files; all its scratch is under `V34-scratch/`.

**Result: PASS** (no writes to sibling lanes or domain source trees attributable to r97; `/tmp` scratch observed and disclosed).

---

## A4 — mythology content stays editorial-only in the new bytes

**JSON-level separation (r97 fixture):**

```
declared source ids: ['veil-verse','paired-clock','crossing-minute','aru-aftermath-note','evin-response-note','aru-acknowledgment-note']
map named source ids: ['aru-acknowledgment-note','aru-aftermath-note','crossing-minute','evin-response-note','paired-clock']
all named in declared fictional set: True
$ grep -n -i -E "spence|kojiki|chamberlain|gutenberg|inana|ovid|maya|kiche|k'iche|etcs" corpus/fixtures/r97-crossing-acknowledgment/*.json
(none)
```

No external comparator is bound as JSON support; the new authored note and event are in-world fiction. **Checker-level separation (real runs, exit 0):**

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r97-crossing-acknowledgment
CLEAN: schema, citations, relations, timeline; 0 violations          exit=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r97-crossing-acknowledgment
RECEIPT JSON-FACTS 17; EDITORIAL-ROWS 2; TOTAL-ROWS 19
SOURCE-SUPPORT 17/17; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 19/19; VALIDATED-ROWS 19/19
RESULT PASS                                                          exit=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r97-crossing-acknowledgment
OBLIGATIONS raw=17 mapped=17 / INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19
RESULT PASS                                                          exit=0
```

The Spence material stays in the two `editorial-row`s. Row-level comparison of the maps shows the **S rows byte-identical to r96** and the 16 inherited J rows identical modulo the expected fixture-qualified namespace token (`r96-crossing-response:` → `r97-crossing-acknowledgment:`):

```
J counts r96/r97: 16 17 | S counts: 2 2
S rows identical: True
inherited J01-J16 identical after namespace normalization: True
unexpected diffs: 0
new row J17: | J17 | `timeline.json#/5` (`tick`, `entity_id`, `place_id`, `depends_on`, `description`, `source_id`) | `aru-acknowledgment-note` | … | `fictional-excerpts.md` | 44-53 | `verbatim` | `Tick 13: I received Evin's response at the Chalk Stair.` |
```

The new event is tick-13 `acknowledgment-aru-records` (actor `aru`, place `chalk-stair`, `depends_on: ["response-evin-salt-court"]`), and its bound source carries the refusal in the bytes: "It records receipt only and is not evidence of a resolution, a reconciliation, an accusation, a winner between the accounts, a continuing duty, or an external historical fact" (`sources.json#/5`); `contradictions.json` remains `[]`. Explicit refusal lines in the new bytes: `README.md:19` ("no in-world witness, cultural authority, or fictional canon … Rights and AI-training permission remain unassessed; neither is granted or inferred here"), `README.md:21` and `claim-excerpt-map.md:59` (receipt "not … source authentication, chronology truth, rights, permission, or canon review"), `claim-excerpt-map.md:42`, and `r97-acknowledgment-scope-note.md:8` ("not merged canon, not a resolution finding, and not a verdict…").

**Result: PASS.**

---

## A5 — rights / canon / mechanics language scan (all r97 new/changed bytes)

Pattern `rights|licen[cs]e|copyright|permission|canon|mechanic|gameplay|ruleset|damage|stats|balancing|public domain|training` over the 10 r97 fixture files, the knowledge note, both R3 tool files, and the R1/R2/R3 diffs:

- r97 fixture + note → 16 hits, **every one a refusal, an open question, a scope exclusion, or the JSON-Pointer sense of "canonical"** (`inspiration-note.md:13–21` rights/permission questions stated open; `claim-excerpt-map.md:1,16` "canonical" only in the pointer sense; `README.md:19,21`; `r97-acknowledgment-scope-note.md:8,41,70`).
- Tool diffs → **exactly 1 added matching line**: `dependency-freeze-contract.json` scope text "…no chronology truth, entailment, source, rights, or canon judgment" — a scope exclusion.
- No occurrence of `mechanic`, `gameplay`, `ruleset`, `damage`, `stats`, `balancing`, or "public domain" in any r97 new byte.

Sibling-path scan over the same set (`kotodama|game-dev|art-east-asian|sibling|\.\./`) returns one hit, checked and cleared: `corpus/tools/map_obligations.py:774` — `rows[0] = (…, "../entities.json#/0/first_appearance", …)` inside the `traversal_path` **self-test negative control** (a planted traversal pointer that must be rejected); the identical line exists at baseline (`git show f3e09f9:corpus/tools/map_obligations.py` line 752), so it is not an r97 introduction and not a path escape.

**Result: PASS.**

---

## A6 — no commits, no pushes, no post-report rewrites

```
$ git rev-parse HEAD
2393934237ea076366f3db6dceeff033edb52ab1
$ git for-each-ref --format='%(refname) %(objectname:short)'
refs/heads/main 2393934 / refs/remotes/origin/HEAD b8b50c8 / refs/remotes/origin/main b8b50c8
$ git reflog -3 --date=iso
2393934 HEAD@{2026-10-17 18:38:19 -0300}: commit: lore r96: close round — SCORECARD admitted section
f3e09f9 HEAD@{2026-10-17 18:37:17 -0300}: commit: lore r96: freeze admitted wave + closure docs …
60dba0c HEAD@{2026-10-17 17:32:53 -0300}: commit: lore r95: close round — SCORECARD admitted section
```

No commit exists after dispatch; local `main` and `origin/main` are unchanged (no push evidence). Artifact mtimes all precede their producer reports:

| producer | artifact mtimes | report mtime |
|---|---|---|
| R4 | r96 map 18:43:42; r97 fixture 18:44:16–18:44:30 | 18:50:14 |
| R1 | tool 18:45:37 | 18:52:25 |
| R2 | contract 18:46:12; README 18:47:13 | 18:49:31 |
| R5 | map 18:48:56; README 18:49:14 | 18:51:25 |
| R6 | note 18:52:38 | 18:53:37 |
| R3 | tool 18:53:00; contract 18:55:14 | 18:56:23 |

Producer-pinned hashes match the delivered bytes: R1 pins `86b52949…` (measured `86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9`); R2 pins `2142b991…`/`6278e59b…`; R3 pins `b06275f3…`/`27273be2…` — all equal to my freeze hashes. Delivered hashes were identical at 18:57 and 18:59 (`freeze1` == `freeze2`, and a third re-check `STABLE`).

**Result: PASS.**

---

## A7 — the r96 cosmetic repair stays inside its declared scope (r97-specific)

```
$ git show HEAD:corpus/fixtures/r96-crossing-response/claim-excerpt-map.md | sha256sum
5093d72eb3f22b249033d7ac4c1a85c7df7f5e09bfa673a598aee6a83045bfd8  -
$ sha256sum corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
e851f068cfd7ed02c97054df18729c4c5a9b8bf60d99d7c9116f427d765440de  corpus/…/claim-excerpt-map.md
```

`git diff HEAD` on that file is **exactly two lines**: the editorial delimiter row `|---|---|---|---|---|---:|---|---|` → `|---|---|---|---|---:|---|---|` (9 → 7 cells), and the closing sentence of the timeline-normalization paragraph `…The new relation encodes only the agreement for this crossing…` → `…The new tick-12 event encodes only Evin's second account of the same crossing occasion; it asserts no reconciliation, selects no winner between the accounts, and adds no duty beyond this crossing…`. Row-level check: 18/18 data rows byte-identical, the 16-pointer set identical, line count 56/56, no other line changed. Receipts on the repaired fixture are **unchanged from r96**:

```
$ python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response | tail -2
SOURCE-SUPPORT 16/16; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 18/18; VALIDATED-ROWS 18/18
RESULT PASS
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response | tail -2
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18
RESULT PASS
```

**Result: PASS.**

---

## A8 — r97 fixture inheritance is byte-exact (supporting evidence for the depth claim)

```
$ for f in entities.json relations.json contradictions.json inspiration-note.md source-excerpt.md; do cmp -s r96/$f r97/$f && echo IDENTICAL $f; done
IDENTICAL entities.json / relations.json / contradictions.json / inspiration-note.md / source-excerpt.md
r96 fictional-excerpts.md is a strict prefix of r97: True (2588 → 3410 bytes)
timeline.json r96 len 5 r97 len 6 prefix-equal True
sources.json  r96 len 5 r97 len 6 prefix-equal True
entities.json 5/5, relations.json 1/1, contradictions.json 0/0 prefix-equal True
$ ls -d corpus/fixtures/*/ | wc -l
171
$ for d in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response; do python3 corpus/tools/dependency_freeze.py corpus/fixtures/$d | tail -2; done
DIGEST 15ef230e… PASS / 2527beb9… PASS / d541ae64… PASS / d422a9b3… PASS    all exit=0
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r97-crossing-acknowledgment
FINDING UNPINNED-FIXTURE: no pin for 'r97-crossing-acknowledgment' … (pinned: ['r88-m3-maya-cluster','r94-paired-crossing','r95-crossing-aftermath','r96-crossing-response'])
RESULT ERROR                                                          exit=2
```

Census 170 → **171** as declared; the four pinned fixtures verify clean with the digests pinned since r96 (the r96 digest is unchanged by the repair, as the repair touched only the map file, not the pinned JSON); the r97 fixture itself is **not** pinned, so the tool fails closed with exit 2 — consistent with the declaration's chain-4/4 wording (see observation O3).

---

## Observations reported as found (not province breaches)

1. **R3 moved the freeze self-test scratch from system temp to the lane root** — `dependency_freeze.py` line 411 (baseline) `tempfile.TemporaryDirectory(prefix="dependency-freeze-self-test-")` → line 517 (delivered) `…, dir=ROOT)`, matching the existing `map_obligations.py:831` precedent. R3 discloses and justifies this in its report (§4 item 4: "`/tmp` was inode-exhausted during this round … so the old `/tmp`-based scratch could not be relied on; no scratch dirs are left behind"). I independently observed the condition: `df -i /tmp` → `1048575/1048576 used (100%)` at 18:43, recovered to `15,694 used (2%)` by 18:57. A `git status` snapshot at 18:59 caught the transient lane-root dirs `dependency-freeze-self-test-i2abptt5/` and `map-obligations-self-test-s39eou49/` (concurrent verifier self-tests); both were gone at the next check and no lane-root self-test scratch persists at freeze. Lane-internal, so `PROVINCE.md`'s "only writes this standalone lane repository" holds; flagged because the BR-05 class (lane-root self-test scratch) now covers **both** tools and is visible to concurrent `git status` runs — bounded follow-up, not smoothed over.
2. **`/tmp` artifacts** — `/tmp/fake-contract-backup.json` (18:44:18; byte-identical to the r96-baseline freeze contract `c65ac3bd…`), `/tmp/o`, `/tmp/opencode`, three bun runtime files. Ephemeral seat scratch in system temp; none a sibling repository or domain source tree.
3. **r97 fixture not pinned in the freeze contract** — `dependency_freeze verify` on `corpus/fixtures/r97-crossing-acknowledgment` exits 2 `UNPINNED-FIXTURE`. This matches the declaration's "chain verifies 4/4 clean" (r88/r94/r95/r96) and is fail-closed behavior rather than a defect, but it means the r97 fixture has no digest pin; flagged for the coverage-verdict seats and the integrator to confirm it is intended, since a r98 round would inherit an unpinned fixture.
4. **Baseline/HEAD distinction** — declared baseline `f3e09f9`; HEAD `2393934` carries the committed r96 SCORECARD closure (+31 lines) and is not an r97 write (`git diff HEAD -- SCORECARD.md` → 0). Worth pinning in the closure arithmetic, as in r96.
5. **Verifier scratch volume** — 8,719 untracked paths under `.ufo/waves` (round-97 seats/scratch, including mutation copies of chain fixtures). Lane-internal and inside the declared seat-write area; visible only as untracked volume, not a breach.
6. **Mid-flight transients, disclosed or observed pre-report** — R4's repair landed 18:43:42, ~6.5 min before its report; R5's r97 `README.md`/`claim-excerpt-map.md` were r96 byte-copies (`ff52ced4…`/`e851f068…`) until 18:48:56/18:49:14; R3's tool hash moved through four values before its 18:56:23 report. All pre-report and settled at freeze; the delivered hashes are stable across my battery.

## Limits

- Sibling-write coverage is a bounded in-window mtime sweep (since 18:35) plus a string-leak grep, not a full cross-repo commit audit or process tracing; kotodama's concurrent activity is attributed by path ownership.
- The `/tmp` and lane-root scratch observations are listings at moments, not a machine-wide audit; the inode-exhaustion episode was observed, not root-caused.
- This seat ran only read-only gates (`check_bible`, `support_check`, `map_obligations`, `dependency_freeze` verify); it did **not** run `--self-test` (that would create scratch and belongs to the calibration/coverage seats). Its only writes are this report and `V34-scratch/`.
- A1–A6 mirror the r96 adjacency battery; A7/A8 are the r97-specific additions (repair scope, inheritance). No C1/C2/C3 verdict is offered.

---

**Bottom line: PASS — the delivered r97 revision is province-clean: `PROVINCE.md` is byte-identical to the declared baseline `f3e09f9` (blob `7c599c39`, sha256 `94a7a77e`, empty diff); the round's change set is lane-local and exactly the declared byte ownership (6 modified files — 4 tool files, the freeze contract, and the cosmetically repaired r96 map — plus 11 additions — 10 r97 fixture files and the knowledge note — with the `LOG.md` declaration uncommitted and `SCORECARD.md` attributed to the committed `2393934`), with no writes to sibling lanes, domain source trees, past waves, charters or earlier fixtures, and no commits or pushes; mythology stays editorial-only in the new bytes (no external comparator bound in any r97 JSON, Spence rows unchanged and labelled editorial, explicit no-witness/no-canon/no-resolution refusals throughout), the r96 repair is confined to two cosmetic lines with 18/18 data rows and 16/16 pointers untouched and its receipts unchanged, and the rights/canon/mechanics scan over every new byte returns only refusals, open questions, scope exclusions and JSON-Pointer "canonical" uses — the sole caveats being disclosed `/tmp` scratch (including a backup copy of the r96-baseline freeze contract), the observed `/tmp` inode exhaustion that motivated R3's lane-root self-test scratch (`dir=ROOT`, self-cleaning, none persisting at freeze), and the r97 fixture's absence from the freeze contract's pins (fail-closed exit 2, consistent with the declared 4/4 chain).**
