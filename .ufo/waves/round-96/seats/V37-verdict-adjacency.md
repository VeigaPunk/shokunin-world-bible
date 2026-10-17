# V37 — verdict-adjacency (round 96)

**Seat:** V37 verdict-adjacency, round-96 single wave, lane `lore-shokunin`.
**Subject:** the delivered r96 working tree vs baseline r95 closure `dcb2d92` (`dcb2d928f53f35673744feaf114e3ac65e3d25ca`); HEAD is `60dba0c` (`60dba0c2aa344860b10a2fc63e00468d1b134f27`, "lore r95: close round — SCORECARD admitted section", a post-baseline r95-closure commit). No r96 commit exists (hard rule: no commits), so every measurement below is **worktree-vs-baseline**, not commit-range.
**Mandate:** read V31 (round-96 adjacency evidence seat), run my own PROVINCE diff and province-scope battery, issue exactly one ADJACENCY verdict. This seat makes no C1/C2/C3 verdict, no admission verdict, and no lore-truth ruling.
**Inputs read:** `.ufo/waves/round-96/seats/V31-adjacency.md` (214 lines; sha256 `8bd62e876bf2fd29ecf2c48080d34f13e2b833f9ec82e62483d37267706bf969` at my read; spot-checked line-identical after its last write). V31's own bottom line is PASS with caveats; I re-ran the load-bearing checks myself below rather than repeating its numbers.
**Measurement freeze:** all six producer reports present (Q2 last, 17:52:12); every producer artifact mtime precedes its report mtime (§3.6). My batteries ran 17:52:5x and 17:56:15 -03:00; the delivered hashes were identical at both ends (`.ufo/waves/round-96/seats/V37-scratch/freeze1.txt`, `freeze2.txt`; `diff` of the hash sections → empty). All commands run from `/home/vgpnk/Projects/shokunin/lore-shokunin`. My only writes are this report and my seat scratch under `.ufo/waves/round-96/seats/V37-scratch/`.

## Poll-wait record

- Seat start 17:38:49. First check 17:39:05: `corpus/fixtures/r96-crossing-response/` partially present (5 files), Q1–Q3 tool files absent, zero `Q*-*.md` reports. Slept 20 s per attempt.
- Loop 1 (`.ufo/waves/round-96/seats/V37-scratch/poll-v31.sh`, 40 tries × 20 s, 17:38:45–17:52:05): producers landed Q4 17:42, Q5 17:44, Q6 17:45, Q3 17:47; Q1/Q2 and V31 still absent at try 40 — the loop ended TIMEOUT with 5/6 producer reports.
- Loop 2 (V31-only, 40 tries, started 17:52:40): observed `V31-adjacency.md` at 17:54:05 (≈15 min after my first check, two loops, no ABSENT condition).
- I verified only after the target bytes existed and all six producer reports were written; I never verified a plan. Interim reports (V33/V34) were read but are other seats' scope.

---

## 1. My own PROVINCE diff

```
$ git hash-object PROVINCE.md
7c599c395e1710b6a7c7aca6d485c373bed6deb7
$ git rev-parse dcb2d92:PROVINCE.md
7c599c395e1710b6a7c7aca6d485c373bed6deb7
$ sha256sum PROVINCE.md
94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa  PROVINCE.md
$ git show dcb2d92:PROVINCE.md | sha256sum
94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa  -
$ git diff dcb2d92 -- PROVINCE.md | wc -c
0
```

Blob, sha256 and byte diff agree: the province charter is byte-identical across the round. `PROVINCE.md` is in neither the tracked diff nor the untracked list.

**Result: PASS — the charter that defines the province is untouched.**

---

## 2. Province-scope diff of the round

### 2.1 Change set

```
$ git diff --name-status HEAD
M	LOG.md
M	corpus/tools/README.md
M	corpus/tools/map-obligations-contract.json
M	corpus/tools/map_obligations.py

$ git diff --name-status dcb2d92
M	LOG.md
M	SCORECARD.md
M	corpus/tools/README.md
M	corpus/tools/map-obligations-contract.json
M	corpus/tools/map_obligations.py
```

Attribution: `LOG.md` is the pre-dispatch r96 declaration (same convention as r94/r95). `SCORECARD.md`'s delta is **committed in `60dba0c`**, not an r96 write — `git diff HEAD -- SCORECARD.md | wc -c` → `0`, and it is exactly the r95 closure continuation that sits above the declared baseline (`git diff --stat dcb2d92 -- SCORECARD.md` → `1 file changed, 32 insertions(+)`). The remaining three tracked files are exactly the declared Q1/Q2 byte scope. No other tracked path changed: `git diff --stat dcb2d92 -- PROVINCE.md SHONEN.md SKILL.md README.md l0-questions.md .gitignore` → only SCORECARD's 32 lines, nothing else.

### 2.2 Blob-level corpus comparison (in-place edits cannot hide behind unchanged paths)

```
base corpus files: 1791
CHANGED: ['corpus/tools/README.md', 'corpus/tools/map-obligations-contract.json', 'corpus/tools/map_obligations.py']
ADDED: 13
  corpus/fixtures/r96-crossing-response/{README.md,claim-excerpt-map.md,contradictions.json,entities.json,fictional-excerpts.md,inspiration-note.md,relations.json,source-excerpt.md,sources.json,timeline.json}
  corpus/knowledge/r96-response-scope-note.md
  corpus/tools/dependency-freeze-contract.json
  corpus/tools/dependency_freeze.py
MISSING: []
```

Exactly the declared byte ownership: 3 modified tool files (Q1/Q2), 10 new fixture files (Q4/Q5), 1 knowledge note (Q6), 2 new tool files (Q3). This independently confirms C3's "zero corpus modifications beyond the two new tool files" and C2's "no new claims/entities/relations".

### 2.3 Untracked audit

```
untracked roots: {'.ufo': 18123, 'corpus': 13}
outside corpus/ and round-96 wave dir: []
```

Every untracked path outside `.ufo/waves/round-96/` is one of the 13 declared corpus additions; all other untracked volume is seat reports and verifier scratch inside the wave's declared area. `git diff --name-only dcb2d92 -- .ufo/waves/ | grep -v round-96` → empty (no past wave touched). No round-96 wave directory exists in the parent tree (`ls -d /home/vgpnk/Projects/shokunin/.ufo/waves/round-96` → No such file or directory), so the r94/r95 parent-tree stray defect did not recur. Round-96 top level holds only `seats/`, `scratch/`, `Q6-scratch/`, `V13-scratch/`, `V18-scratch/` — no stray files.

### 2.4 Inherited bytes frozen

```
$ git diff --stat HEAD -- corpus/fixtures/r95-crossing-aftermath corpus/fixtures/r94-paired-crossing corpus/fixtures/r88-m3-maya-cluster corpus/fixtures/r93-m2-kojiki-cluster corpus/fixtures/r87-myth-cluster
(empty)
$ for f in entities.json relations.json contradictions.json inspiration-note.md source-excerpt.md; do cmp -s r95/$f r96/$f && echo IDENTICAL $f; done
IDENTICAL entities.json / relations.json / contradictions.json / inspiration-note.md / source-excerpt.md
$ cmp corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md <(head -c 1845 corpus/fixtures/r96-crossing-response/fictional-excerpts.md) && echo prefix
r95 full content is prefix of r96
```

No earlier fixture was touched, and Q4's five declared byte copies are byte-identical to r95 (r95's `fictional-excerpts.md` is a strict byte prefix of r96's, not a rewrite).

### 2.5 New files are ordinary lane files

All 13 additions are regular mode-644 files (`find corpus/fixtures/r96-crossing-response -type f -printf '%m' | uniq -c` → `10 644`; the tool files and note `stat -c '%a'` → `644` each), zero symlinks (`find … -type l` → empty). No lane-root scratch residue: `ls -d map-obligations-self-test-* dependency-*` in the lane root → no output.

**Result: PASS — the round's change set is lane-local and exactly the declared byte ownership.**

---

## 3. Independent corroboration of V31's load-bearing claims

I re-ran the checks myself rather than repeating V31's numbers.

### 3.1 Census, counts, prefixes

```
$ ls -d corpus/fixtures/*/ | wc -l
170                       # 169 at r95 closure — matches C2's 169→170
entities 5 / relations 1 / events 5 / sources 5 / contradictions []
$ python3 -c "…b[:len(a)]==a…"   # timeline.json, sources.json vs r95
timeline.json True / sources.json True
```

The new event is tick-12 `response-evin-salt-court` (`entity_id: evin`, `place_id: salt-court`, `depends_on: ["aftermath-missing-evin"]`, `source_id: evin-response-note`) and the new source is `evin-response-note` — both as declared.

### 3.2 Gate receipts on the delivered revision (my own runs)

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response
CLEAN: schema, citations, relations, timeline; 0 violations          exit=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18; DISTINCT-ANCHORS 14/14
… 16 J-rows + 2 S-rows PASS … RECEIPT … SOURCE-SUPPORT 16/16; EDITORIAL-ANCHORS 2/2; MODES 18/18; VALIDATED-ROWS 18/18; RESULT PASS   exit=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response
OBLIGATIONS raw=16 mapped=16
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18
RESULT PASS                                                          exit=0
$ for d in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response; do python3 corpus/tools/dependency_freeze.py corpus/fixtures/$d; done
r88 DIGEST 15ef230e… PASS / r94 DIGEST 2527beb9… PASS / r95 DIGEST d541ae64… PASS / r96 DIGEST d422a9b3… PASS   all exit=0
```

The four `dependency_freeze` digests match the ones Q3's report pins; the 16/2/18 inventory matches C2's declared 16 map obligations (15 inherited + 1 new).

### 3.3 Mythology stays editorial-only

```
declared source ids: ['aru-aftermath-note','crossing-minute','evin-response-note','paired-clock','veil-verse']
bound source ids   : ['aru-aftermath-note','crossing-minute','evin-response-note','paired-clock']
all bound in declared fictional set: True
$ grep -n -i -E "spence|kojiki|chamberlain|gutenberg|inana|ovid|maya|kiche|etcs" corpus/fixtures/r96-crossing-response/*.json
(none)
```

No external comparator is bound as JSON support. The two Spence comparisons remain the `## Editorial rows` block, and its S01/S02 data rows are line-identical to r95 (`S01 r95==r96: True`, `S02 r95==r96: True`); the only block difference is a separator-row pipe count (see §5.2). Explicit refusals in the new bytes: `README.md:19` ("no in-world witness, cultural authority, or fictional canon … Rights and AI-training permission remain unassessed"), `claim-excerpt-map.md:41,56`, `r96-response-scope-note.md:7,61`, and the byte-copied `inspiration-note.md:13–21` open questions.

### 3.4 Rights/canon/mechanics + sibling-string scan (my own, wider pattern)

Pattern `rights|licen[cs]e|copyright|permission|canon|mechanic|gameplay|ruleset|damage|stats|balancing|public domain|training` over the 10 fixture files, the knowledge note, both Q3 files, and the Q1/Q2 tracked diffs → **23 hits, every one a refusal, an open question, a scope exclusion, or the JSON-Pointer sense of "canonical"** (e.g. `dependency-freeze-contract.json:4` "no chronology truth, entailment, source, rights, or canon judgment"; `map_obligations.py` diff hits are pointer-grammar wording; `corpus/tools/README.md` diff hit is the `dual_pointer` scan text). No mechanics/gameplay/ruleset/damage/stats/balancing/"public domain" occurrence anywhere. A sibling-path scan over the same set (`kotodama|game-dev|art-east-asian|sibling|\.\./`) → empty.

### 3.5 No sibling-lane or parent-tree writes attributable to r96

```
$ cd /home/vgpnk/Projects/shokunin && for d in *-shokunin; do n=$(find "$d" -newermt "2026-10-17 17:37" -type f -not -path "*/.git/*" | wc -l); [ "$n" -gt 0 ] && echo "$n $d"; done
3 kotodama-shokunin        # its own concurrent round-8/9 files (reports/round-8, examples, validation.json)
1169 lore-shokunin         # this lane's own round
$ grep -rl "r96-crossing-response\|evin-response-note\|response-evin-salt-court\|dependency_freeze\|dependency-freeze-contract" /home/vgpnk/Projects/shokunin/*-shokunin --include='*.md' --include='*.json' --include='*.py' | grep -v lore-shokunin
(empty)
```

The parent-level `MANIFEST.json` and `.ufo/l0-questions.md` (mtime 17:45) contain no r96 lore strings (`mentions round-96: False`, `lore r96 entries: 0`) — fleet-level files touched by other lanes' activity, not attributable to an r96 lore seat. No lore write to any sibling lane or domain source tree.

### 3.6 No commits, no pushes, no post-report rewrites

```
$ git rev-parse HEAD
60dba0c2aa344860b10a2fc63e00468d1b134f27
$ git reflog -2 --date=iso
60dba0c HEAD@{2026-10-17 17:32:53 -0300}: commit: lore r95: close round — SCORECARD admitted section
dcb2d92 HEAD@{2026-10-17 17:31:49 -0300}: commit: lore r95: freeze admitted wave + closure docs …
$ git for-each-ref --format='%(refname) %(objectname:short)'
refs/heads/main 60dba0c / refs/remotes/origin/main b8b50c8
```

No commit exists after dispatch; local `main` and `origin/main` are unchanged (no push evidence). Artifact mtimes all precede their producer reports: Q1 tool 17:47:24 → report 17:52:17; Q2 contract 17:50:17, README 17:51:26 → 17:52:12; Q3 17:44:27/17:44:37 → 17:47:26; Q4 files 17:38:26–17:40:16 → 17:47:19; Q5 17:43:09/17:43:17 → 17:45:37; Q6 note 17:47:02 → 17:47:16. Producer-pinned hashes match the current bytes (Q1/Q2 pin tool `2b0ba815…`, contract `97b76bb8…`, README `965b29cd…`; Q3 pins `a3b57978…`/`7d568cc4…`), and my two batteries 17:53 → 17:56 are hash-identical.

**Result: PASS — V31's load-bearing claims reproduce on the delivered revision.**

---

## 4. Verdict — ADJACENCY: **PASS**

The delivered r96 revision is province-clean. `PROVINCE.md` is byte-identical to the declared baseline `dcb2d92` (blob `7c599c39`, sha256 `94a7a77e…`, empty diff). The entire round's change set is lane-local and exactly the declared byte ownership (3 modified tool files, 13 new corpus files, the pre-dispatch `LOG.md` declaration; `SCORECARD.md` attributed to the committed r95-closure `60dba0c`), with no writes to sibling lanes, domain source trees, past waves, charters, or earlier fixtures, and no commits or pushes. Mythology remains editorial-only in the new bytes (no external comparator bound in any fixture JSON, the two Spence rows unchanged and labelled editorial, explicit no-witness/no-canon refusals throughout), the new in-world records are lore-owned fictional continuations, and the rights/canon/mechanics scan over every r96 new byte returns only refusals, open questions, scope exclusions, and JSON-Pointer "canonical" uses.

Caveats, all reported as found and none a province breach:

1. **Disclosed ephemeral `/tmp` scratch** — 5 in-window entries at `/tmp` depth 1 (`o1`, `o2`, `selftest-out.json`, `wl-copy-buffer-Cw59Sl`, `x02-poll.sh`; 4 regular files at all depths), the same class as r95's disclosed observation.
2. **Environment condition, machine-local** — at ~17:45 one of my redirects to `/tmp` failed with `No space left on device`; `/tmp` is a 16 G tmpfs whose inode table is exhausted (`df -i /tmp` → `1048576 total, 100% used, 0 free`) though bytes remain (45 % used). Not a province matter; other seats' `/tmp` scratch may have been affected.
3. **Markdown formatting nit inside the lane** — `claim-excerpt-map.md:44` has a separator row with 9 pipes against its header's 8 (r95's equivalent was 8). Cosmetic only; all gates pass. Flagged for the depth/coverage seats and the integrator.
4. **`dependency_freeze.py` self-test uses system temp** (`tempfile.TemporaryDirectory(prefix="dependency-freeze-self-test-")`, no `dir=ROOT`), unlike BR-05's lane-root scratch in `map_obligations.py`; no lane-root self-test residue observed this round (I did not run either `--self-test`).

## Limits

- Sibling-write coverage is a bounded in-window mtime sweep plus a string-leak grep, not a full cross-repo commit audit; kotodama's concurrent activity is attributed by path ownership, not process tracing.
- The `/tmp` counts are listings at a moment, not a complete machine-wide audit; the inode-exhaustion condition was observed, not root-caused.
- This seat re-ran only read-only gates; its only writes are this report and its scratch dir. V31's own `/tmp` count (5) and mine (6 including the `/tmp` directory itself) differ only by that inclusion.

---

**Bottom line: PASS — r96 stays inside the lore province on the delivered revision: charter byte-identical to `dcb2d92`, change set exactly the declared byte ownership with no sibling-lane, domain-tree, past-wave, commit or push activity, mythology editorial-only, and only refusal language in the new bytes; the sole caveats are disclosed `/tmp` scratch, a machine-local `/tmp` inode exhaustion observed mid-round, one cosmetic Markdown separator nit inside the lane, and the new tool's system-temp self-test scratch — none a province breach.**
