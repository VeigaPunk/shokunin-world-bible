# V24 — adjacency (round 98)

**Seat:** V24 (adjacency), round-98 single wave, lane `lore-shokunin`.
**Subject:** the delivered r98 working tree vs baseline r97 closure `9a3d648` (lane HEAD `dd4df1b` "lore r97: close round — SCORECARD admitted section"; the wave tree is uncommitted, so every check is worktree-vs-baseline).
**Scope of this seat:** `PROVINCE.md` byte-identity, no writes outside `lore-shokunin` (whole-tree write attribution vs the declared producer byte-ownership S1–S5), and a rights/mechanics language scan over every new r98 byte and every round diff. This seat makes **no** C1/C2/C3 verdict, no admission verdict, and no lore-truth ruling.
**Measurement freeze:** all five producer reports present by 20:35:33 (`S1-freeze-hygiene.md` last; `S3` 20:31:25, `S4` 20:32:06, `S5` 20:34:00, `S2` 20:34:53). Every producer artifact mtime precedes its owner report mtime (§A5). Freeze manifests taken at 20:36:36 (`freeze-1.txt`, sha256 `efa4b41f…`), ~20:37:20 (`freeze-2`), 20:38:0x (`freeze-3`, `dd02ce6d…`) and 20:41:5x (`freeze-4`, `e85f4d11…`) — the 22 `SHA256` lines are **identical across all four** (only the self-referential `MANIFEST-DIGEST` line differs). `PROVINCE.md` re-digested at every point. All commands run from `/home/vgpnk/Projects/shokunin/lore-shokunin`. This seat's only writes are this report, declared scratch under `.ufo/waves/round-98/seats/V24-scratch/`, and one `/tmp` scratch file (`/tmp/v24-r97-fx.md`, a baseline copy made by the scan script).

## Poll-wait record (protocol compliance)

- Poller `.ufo/waves/round-98/seats/V24-scratch/poll.sh`, 20 s cadence, 40 tries, `POLL_START 2026-10-17 20:28:22`, `POLL_END 2026-10-17 20:41:46 -0300 tries=40`. It logged report counts, the r98 fixture file count, the scope-note flag, and the four tool/repair file hashes every 20 s (`poll.log`).
- First check 20:28:22: `r98fix=0`, zero producer reports (only V15's verifier report existed). The r98 fixture appeared as 10 files at 20:28:24 — a wholesale byte-copy of `r97-crossing-acknowledgment` (all 10 hashes SAME as baseline) — i.e. the declared preserving base, mid-flight, **not verified**.
- Producer landing: `S3` 20:31:25, `S4` 20:32:06, `S5` 20:34:00, `S2` 20:34:53, `S1` 20:35:33. The poll line at 20:35:24 shows all five producer reports present (`reports=22`, `[S1-freeze-hygiene.md S2-tools-docs.md S3-fixture-author.md S4-fixture-docs.md S5-knowledge-notes.md …]`). No ABSENT condition; no stall escape needed; the 40-try window completed with `reports=56` (verifiers still landing). Endgame convention: my gate was the five producer reports, not all 64 seats — no all-reports poll was needed, and SELF (V24) was excluded from every count by construction.
- I verified only after all producer reports and all artifacts existed; I never verified a plan. First freeze 20:36:36 is strictly post-report.

---

## A1 — `PROVINCE.md` byte-identical to `9a3d648`

```
$ sha256sum PROVINCE.md
94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa  PROVINCE.md
$ git show 9a3d648:PROVINCE.md | sha256sum
94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa  -
$ git hash-object PROVINCE.md          → 7c599c395e1710b6a7c7aca6d485c373bed6deb7
$ git rev-parse 9a3d648:PROVINCE.md    → 7c599c395e1710b6a7c7aca6d485c373bed6deb7
$ git diff 9a3d648 -- PROVINCE.md | wc -c   → 0
```

Re-checked after the whole battery (20:41:5x, freeze-4): `94a7a77e…` unchanged. The other province-level documents are likewise byte-identical to the baseline:

```
PROVINCE.md      IDENTICAL 7c599c395e1710b6a7c7aca6d485c373bed6deb7
SHONEN.md        IDENTICAL 561b3f8ce99e35200fcfa2269198a7f7f68f1a5e
SKILL.md         IDENTICAL bf704be30cf263b881152451dcba5010facbccdd
README.md        IDENTICAL 7c46413cf7781ae3cdbaa7bae7e265f7ddcbbe70
l0-questions.md  IDENTICAL f9fdff500e043c63d7bbfd0ffad90f8cfd66de4e
```

**Result: PASS.**

---

## A2 — no writes outside `lore-shokunin` (and no lane writes outside declared byte-ownership)

### A2.1 Whole-tree blob audit vs `9a3d648` (`.ufo/` excluded)

Every tracked non-ufo file's worktree blob hash compared to its baseline blob (so in-place edits cannot hide behind unchanged names), plus the untracked non-ufo set (`audit_tree.py`; evidence `snap-final/`, `snap-final2/`, `snap-final3/` — identical runs):

```
baseline non-ufo tracked files: 2829
CHANGED (8):
  LOG.md                                            6f997b3e96cf -> 41618e66b14a
  SCORECARD.md                                      993b558803b1 -> 0bf27ca3c6ae
  corpus/tools/dependency_freeze.py                 001ad47390a0 -> 623b3501b580
  corpus/tools/dependency-freeze-contract.json      1f0a4dc03851 -> d4553282f69b
  corpus/tools/README.md                            e8bb96382a64 -> 8472cbd31dfb
  corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md  cff0ed25ca1f -> 3b5e4d272767
  corpus/knowledge/r95-aftermath-scope-note.md      724a6e033189 -> 784e649265ed
  corpus/knowledge/r96-response-scope-note.md       f6544868e523 -> 2d529b04badc
ADDED-UNTRACKED non-ufo (11): the 10 corpus/fixtures/r98-clerk-filing/ files + corpus/knowledge/r98-clerk-scope-note.md
MISSING: []; STAGED: []; WORKTREE-DELETED: []; MODIFIED-.ufo-tracked: []
```

Attribution against the declared byte-ownership:

- `dependency_freeze.py` + `dependency-freeze-contract.json` → **S1**; `corpus/tools/README.md` → **S2**; `r95-crossing-aftermath/claim-excerpt-map.md` (repair) + r98 fixture `entities/sources/timeline.json` + `fictional-excerpts.md` → **S3**; r98 `README.md` + `claim-excerpt-map.md` → **S4**; `corpus/knowledge/r98-clerk-scope-note.md` + the r95/r96 addenda → **S5**. Exactly the declared set — nothing extra, nothing missing.
- `LOG.md`: `git diff HEAD --numstat -- LOG.md` → `61  0  LOG.md` (append-only, zero deletions) = the pre-dispatch round-98 declaration block.
- `SCORECARD.md` is **not an r98 write**: `git diff HEAD -- SCORECARD.md | wc -c` → `0`; `git log -1 -- SCORECARD.md` → `dd4df1b lore r97: close round — SCORECARD admitted section` (33 insertions). Its 33-line delta vs `9a3d648` is the committed r97 closure sitting above the declared baseline.

### A2.2 Untracked audit (lane-internal)

`git status --porcelain -uall | grep '^??' | grep -v '^?? .ufo/'` → exactly 11 lines: the 10 declared fixture files + `corpus/knowledge/r98-clerk-scope-note.md`. No lane-root stray. All other untracked content is under `.ufo/waves/round-98/` (seat reports, per-seat scratch, `receipt.json`, and three `V14-poll*` files at the wave top level — lane-internal, reported under Observations, not a breach). New corpus files are regular mode-644 files; zero symlinks (`find … -type l | wc -l` → `0`).

### A2.3 Fleet-root / sibling-lane scan

```
$ find . -newermt "2026-10-17 20:25" -type f -not -path "./lore-shokunin/*" -not -path "*/.git/*"
./baseline-analyze.txt
./kotodama-shokunin/reports/round-12/{run-validation.py,validation.json,adjacency/ledger.json,defects/ledger.json,defects/routed.md,recount/ledger.json}
./kotodama-shokunin/reports/round-{8,9}/validation.json
./kotodama-shokunin/.scratch/r12-clone/reports/round-{5..12}/**
./MANIFEST.json
$ find . -newermt "2026-10-17 20:25" … | grep -i -E "lore|r98|clerk"   → (none)
$ ls -d /home/vgpnk/Projects/shokunin/.ufo/waves/round-98   → No such file or directory
$ git -C /home/vgpnk/Projects/shokunin status --porcelain   → ?? baseline-analyze.txt
```

- `MANIFEST.json` (fleet root): mtime 20:25:00, committed in parent commit `80ca9dd` "protocol: close lore r97 (admitted) — fleet report + MANIFEST ledger append" (20:25:00 -0300); `git diff HEAD -- MANIFEST.json` → 0 bytes. A committed orchestrator closure write, **not** an r98 seat write.
- `kotodama-shokunin` round-12 files are the sibling lane's own concurrent round (its `reports/round-12/**`, `.scratch/r12-clone/**`); no lore/r98-named file exists anywhere outside the lane. Sibling `PROVINCE.md` mtimes are all pre-round (latest `kotodama-shokunin` 2026-10-17 12:59; `lore-shokunin` 2026-10-15 01:49). No write to any sibling lane or domain source tree is attributable to an r98 lore seat.
- **Fleet-root stray (r94-F01 class), reported exactly:** `/home/vgpnk/Projects/shokunin/baseline-analyze.txt` — 105 bytes, mtime 2026-10-17 20:30:10 -0300, untracked in the parent repo, content verbatim: `python3: can't open file '/home/vgpnk/Projects/shokunin/analyze.py': [Errno 2] No such file or directory` — the shell-redirect artifact of a `python3 analyze.py > baseline-analyze.txt` run whose cwd was the fleet root. Not this seat's (my only writes are listed in the header). Independently observed and disclosed by S1, S2, S3 (D5), V01, V03, V04, V07, V10 and others. Attribution evidence, not conclusive: the stray appeared at 20:30:10, 4 s after `V57-scratch/analyze.py` was written (20:30:06), and V57's scratch holds a same-named 25 209-byte output at 20:30:29 plus an empty `watch.out` (20:30:08) — the coherent story is V57's first run from the wrong cwd. V20's snapshot also records `?? …/V57-scratch/baseline-analyze.txt`. No seat claims the file; it is left in place for L1 attribution/cleanup, and no measurement here rests on it.

### A2.4 System-temp scratch — observed, reported exactly

`find /tmp -maxdepth 1 -newermt "2026-10-17 20:25"` lists ~50 in-window entries, almost all r98-seat scratch: `df_9a3d648.py`, `df-r98-clerk-filing.out`, `v33-chain-r98-clerk-filing.txt`, `v59-legacy-*`/`v59-mirror-*`, `s2-r98`, `poll_s5.sh`, `r97map.md`, `v12-r97map.md`, `V07-contract-baseline.json`, `parent-baseline-top.txt`, `watch_stable.sh`, `omp-python-runner-1000`, etc. None is a sibling repository or domain source tree, so none breaches `PROVINCE.md`'s write boundary. Disclosed as protocol-level evidence, not smoothed over. **Self-disclosure:** this seat created `/tmp/v24-r97-fx.md` (baseline r97 `fictional-excerpts.md` copy for the prefix check).

**Result: PASS** — the delivered revision's writes are exactly the declared producer byte-ownership; one outside-lane fleet-root stray recorded with attribution evidence pointing to V57 (not part of the delivered revision).

---

## A3 — rights / mechanics language scan (all r98 new bytes + all round diffs)

Scan set: the 10 r98 fixture files, `corpus/knowledge/r98-clerk-scope-note.md`, and the `git diff 9a3d648` of `corpus/` (tools, r95 map repair, r95/r96 addenda). Evidence: `rights-final.txt` (sha256 `15f6290f…`); script `rights_scan.sh`.

```
A. mechanics/grant phrases in new bytes:
   grep -n -i -E "mechanic|gameplay|ruleset|damage|stats|balancing|hit ?point|dice|combat|level.?up|public domain|fair use|free to (use|reuse)|may be (used|reproduced)" $NEW_FILES
   → no output, rc=1
B. same pattern on round diffs (`^[+-]` lines): no output, rc=1
C. broader rights/permission/canon/training hits in new bytes: 29 lines —
   claim-excerpt-map.md 6, fictional-excerpts.md 7, inspiration-note.md 8, README.md 2, r98 note 6
D. adjacency strings `/home/|\.\./|/tmp/` in new bytes: no output, rc=1
E. sibling-lane names (kotodama|game-dev|art-east|kengaku|mado|tabi|sibling|/home/|\.\./) on `git diff 9a3d648 -- corpus/` `^[+-]` lines: no output, rc=1
F. external names (Spence|Kojiki|Chamberlain|Gutenberg|ETCSL|Inana|Ovid|Maya|Kiche|K'iche):
   r98 JSON files → no hits; note hit = `r88-m3-maya-cluster` (fixture path, grep -o → `maya`); README/map/inspiration-note/source-excerpt carry the carried Spence framing (see below)
```

Zero mechanics words and zero rights-grant phrases anywhere in the round's new bytes or diffs. Every hit of the broader pattern is a refusal, an open question, a bounded-record statement, or the JSON-Pointer sense of "canonical":

- `README.md:19` — "It is an editorial design prompt only … supplies no in-world witness, cultural authority, or fictional canon … Rights and AI-training permission remain unassessed; neither is granted or inferred here."; `:21` receipt "not whole-claim entailment, source authentication, chronology truth, rights, permission, or canon review".
- `claim-excerpt-map.md:1,16` — "canonical" only as JSON-Pointer naming ("canonical claim-to-excerpt map", "20 canonical pointers"); `:45` "they do not make Spence an in-world witness, assign cultural meaning, or add canon"; `:68` receipt "not … source authenticity, truth, rights, permission, or canon".
- `inspiration-note.md:9-21` (byte copy of r97) — `## Attribution question` / `## Rights question` / `## AI-training-permission question`, all stated open; "It is not an in-world source and supplies no fictional canon."
- `fictional-excerpts.md:5-57` — "attributed to in-world source ID …" (fictional attribution, not rights attribution).
- `r98-clerk-scope-note.md:3,8,39,72` — bounded-record and refusal lines ("not merged canon, not a finding, not an adjudication"; "None reads the note as testimony or decides truth, finding, chronology, adjudication, rights, permission, or canon").

The Spence material stays two separately labelled editorial rows (S01/S02 at `claim-excerpt-map.md:49-50`, under the `:45` scope sentence); the new authored content (`clerk-filing-note`, tick-14 event `clerk-filing-open`, entity `clerk-maren`) is in-world fiction with the declared no-finding bound; `contradictions.json` stays `[]` (byte copy).

**Result: PASS.**

---

## A4 — preservation copy and the r95 map repair (adjacency to the frozen cluster)

**Byte-copy integrity of the preserving copy** (r98 vs baseline r97):

```
SAME  contradictions.json 37517e5f  SAME  inspiration-note.md 58f5390e
SAME  relations.json c279254b       SAME  source-excerpt.md b5edc2fd
DIFF  README.md 32efc78f   DIFF claim-excerpt-map.md c1099d0e   (S4-authored)
DIFF  entities.json db2d8e5d  DIFF sources.json 32ee15b1  DIFF timeline.json eb24e084  DIFF fictional-excerpts.md 29e384bf  (S3-authored)
```

`fictional-excerpts.md` is a strict byte-prefix extension: r97's 3410 bytes are the prefix of r98's 4187 bytes (`head -c 3410 … | cmp` → `PREFIX-IDENTICAL`), matching the declared appended fourth beat.

**The r95 map repair is cosmetic-only:** `git diff 9a3d648 -- corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md` → one hunk, `+1/−1`, a prose sentence in "Timeline normalization and scope" (the stale "The new relation encodes…" wording replaced by "The relation encodes… the new tick-11 aftermath event records one reported non-arrival on one occasion"). No data row, anchor, span, pointer, or mode changed. The r95/r96 scope-note addenda are pure additions (`--numstat` → `14  0` each; zero removed lines).

**Result: PASS.**

---

## A5 — reports match the bytes (ordering and stability)

Every producer artifact mtime precedes its owner's report mtime — no post-report rewrites (epoch seconds compared):

| Seat | artifact (mtime) | report (mtime) |
|---|---|---|
| S1 | `dependency_freeze.py` 20:31:49, contract 20:33:36 | 20:35:33 |
| S2 | `corpus/tools/README.md` 20:34:06 | 20:34:53 |
| S3 | r95 map 20:28:34; fixture entities/sources/timeline/fictional-excerpts 20:28:55 | 20:31:25 |
| S4 | r98 `README.md` 20:30:41, `claim-excerpt-map.md` 20:30:21 | 20:32:06 |
| S5 | r98 note 20:33:01; r95/r96 addenda 20:29:14 | 20:34:00 |

Delivered hashes at freeze-1 (20:36:36): `PROVINCE.md 94a7a77e`, `dependency_freeze.py 03d04365`, contract `153ebc5b`, tools `README.md 1d299c16`, r95 map `80440d61`, r95 note `8e9e1774`, r96 note `a9b51f8c`, r98 note `1162262c`, r98 README `32efc78f`, r98 map `c1099d0e`, entities `db2d8e5d`, sources `32ee15b1`, timeline `eb24e084`, fictional-excerpts `29e384bf`, contradictions `37517e5f`, inspiration-note `58f5390e`, relations `c279254b`, source-excerpt `b5edc2fd`. All 22 SHA256 lines re-digested identically in freeze-2, freeze-3 and freeze-4 (20:41:5x) — no post-freeze rewrites; the whole-tree audit re-run at 20:41:5x is byte-identical to the 20:36:37 run (`changed=8 untracked_nonufo=11 missing=0`).

**Result: PASS.**

---

## Observations reported as found (not province breaches)

1. **Fleet-root stray `baseline-analyze.txt`** (§A2.3): the r94-F01 class recurred in-window; evidence points to V57, no seat claims it, left in place. Recorded for L1 attribution.
2. **V14 poll files at the wave top level** (`.ufo/waves/round-98/V14-poll.sh`, `V14-poll.log`, `V14-poll2.log`): lane-internal but outside the declared `seats/` + scratch convention (r97's top level held zero files). Reported, not cleaned.
3. **`/tmp` seat scratch** (§A2.4): ~50 in-window entries, several named for r98 fixtures/tools; the same disclosed class as r95–r97.
4. **`kotodama-shokunin` concurrent round 12** and the committed `MANIFEST.json` closure write: attributed away, not counted against this lane.
5. **`SCORECARD.md` vs the declared baseline**: its delta is the committed r97-closure commit `dd4df1b`; `git diff HEAD` is empty. Worth keeping explicit in closure arithmetic.
6. **Mid-flight byte churn, pre-freeze**: the fixture was a pure r97 copy at 20:28:24 and tool hashes moved until ~20:34; every measurement here is post-report and stability was re-verified four times, so no measurement rests on a mid-flight byte.

---

## Bottom line

**PASS** — `PROVINCE.md` is byte-identical to `9a3d648` (blob `7c599c39`, sha256 `94a7a77e…`; SHONEN/SKILL/README/l0-questions likewise) and the delivered revision's entire change set is lane-local and exactly the declared producer byte-ownership (8 tracked files changed — S1 tool pair, S2 README, S3 r95 repair, S5 addenda, LOG +61/−0 declaration, SCORECARD attributed to committed `dd4df1b` — plus the 11 declared new corpus files), the rights/mechanics scan returns zero mechanics words and zero rights-grant phrases with every rights/canon/permission hit a refusal or open question and no path/sibling-lane leakage, and the preservation copy is byte-verified (4 files identical, fictional-excerpts a strict prefix extension; r95 repair one +1/−1 prose hunk); the one caveat is an outside-lane fleet-root stray `baseline-analyze.txt` (105 B, 20:30:10, r94-F01 class, evidence pointing to V57, not part of the delivered revision) recorded here and left in place for L1 attribution.
