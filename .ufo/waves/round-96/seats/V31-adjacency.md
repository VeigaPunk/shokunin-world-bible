# V31 — adjacency (round 96)

**Seat:** V31 (adjacency), round-96 single wave, lane `lore-shokunin`.
**Subject:** the delivered r96 working tree vs baseline r95 closure `dcb2d92` (`dcb2d92`, declared baseline; HEAD is `60dba0c` "r95 close round — SCORECARD admitted section", a post-baseline r95-closure commit). No r96 commit exists (hard rule: no commits), so every check below is a **worktree-vs-baseline** measurement.
**Scope of this seat:** PROVINCE.md byte-identity, no writes outside `lore-shokunin`, mythology content stays editorial-only in the new bytes, and a rights/canon/mechanics language scan over the r96 byte set. This seat makes no C1/C2/C3 verdict, no admission verdict, and no lore-truth ruling.
**Measurement freeze:** all six producer reports present at 17:52:24 -03:00 (`Q2-contract-docs.md` last); every producer artifact mtime precedes its report mtime (§A5). Final battery 17:52:49–17:53:44 -03:00; delivered hashes re-measured at both ends of the battery and identical (`map_obligations.py` `2b0ba815…` stable from 17:47:24 through 17:53:44; Q2/Q3 files stable from 17:51:26 / 17:44:37). All commands run from `/home/vgpnk/Projects/shokunin/lore-shokunin`. This seat wrote no scratch files; its only write is this report.

## Poll-wait record (protocol compliance)

- First check 17:38:43: `corpus/fixtures/r96-crossing-response/` partially present (8/13 files), `corpus/tools/dependency_freeze.py`, `dependency-freeze-contract.json`, `corpus/knowledge/r96-response-scope-note.md` absent, zero `Q*-*.md` reports; slept 20 s per attempt (loop 1, 40 tries).
- Loop 1 observed the gate fill in: all 13 artifacts present at 17:44:23 (try 18); reports Q4 17:47:19, Q5 17:45:37, Q6 17:47:16, Q3 17:47:26, Q1 17:52:17, Q2 17:52:12.
- Loop 2 (targeting the last two) hit at 17:52:24: `Q1=1 Q2=1 tool=2b0ba815326b q2files_modified=2`. I verified only after the target bytes existed and all six producer reports were written; I never verified a plan. No ABSENT condition occurred.

---

## A1 — PROVINCE.md byte-identical to `dcb2d92`

```
$ sha256sum PROVINCE.md
94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa  PROVINCE.md
$ git show dcb2d92:PROVINCE.md | sha256sum
94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa  -
$ git hash-object PROVINCE.md
7c599c395e1710b6a7c7aca6d485c373bed6deb7
$ git rev-parse dcb2d92:PROVINCE.md
7c599c395e1710b6a7c7aca6d485c373bed6deb7
$ git diff dcb2d92 -- PROVINCE.md | wc -c
0
```

Blob identity, sha256, and the byte diff all agree; `PROVINCE.md` appears in neither the tracked diff nor the untracked list. The charter is untouched by the round.

**Result: PASS.**

---

## A2 — no writes outside `lore-shokunin`

### A2.1 Change set vs baseline (tracked + untracked)

```
$ git diff --name-status dcb2d92
M	LOG.md
M	SCORECARD.md
M	corpus/tools/README.md
M	corpus/tools/map-obligations-contract.json
M	corpus/tools/map_obligations.py
$ git diff --name-status HEAD
M	LOG.md
M	corpus/tools/README.md
M	corpus/tools/map-obligations-contract.json
M	corpus/tools/map_obligations.py
```

Attribution: `LOG.md` is the pre-dispatch r96 declaration (+67 lines, uncommitted, same convention as r94/r95). `SCORECARD.md` is **committed in `60dba0c`**, not an r96 write — `git diff HEAD -- SCORECARD.md | wc -c` → `0`; it is the r95 closure continuation that sits above the declared baseline. The remaining three tracked files are exactly the declared Q1/Q2 byte scope.

Blob-level comparison of the whole `corpus/` tree (worktree `git hash-object` vs `dcb2d92` tree), so in-place edits cannot hide behind unchanged path names:

```
base corpus files: 1791
CHANGED: ['corpus/tools/README.md', 'corpus/tools/map-obligations-contract.json', 'corpus/tools/map_obligations.py']
ADDED count: 13
  A corpus/fixtures/r96-crossing-response/{README.md,claim-excerpt-map.md,contradictions.json,entities.json,fictional-excerpts.md,inspiration-note.md,relations.json,source-excerpt.md,sources.json,timeline.json}
  A corpus/knowledge/r96-response-scope-note.md
  A corpus/tools/dependency-freeze-contract.json
  A corpus/tools/dependency_freeze.py
MISSING: []
```

Exactly the three declared tool files changed and exactly the 13 declared new corpus files added — the C3 claim "zero corpus modifications beyond the two new tool files" holds at byte level (Q3's two files are the only additions outside the fixture and the knowledge note). Inherited fixtures are byte-unchanged:

```
$ git diff --stat dcb2d92 -- corpus/fixtures/r95-crossing-aftermath corpus/fixtures/r94-paired-crossing corpus/fixtures/r88-m3-maya-cluster corpus/fixtures/r87-myth-cluster corpus/fixtures/r93-m2-kojiki-cluster | wc -l
0
$ git diff --stat dcb2d92 -- PROVINCE.md SHONEN.md SKILL.md README.md l0-questions.md | wc -l
0
$ git diff --name-only dcb2d92 -- .ufo/waves/ | grep -v round-96
(empty)
```

### A2.2 Untracked audit (lane-internal)

```
$ git status --porcelain -uall | grep '^??' | grep -v '^?? .ufo/waves/round-96/'
?? corpus/fixtures/r96-crossing-response/README.md
… (exactly the 13 declared corpus additions, 13 lines total) …
?? corpus/tools/dependency_freeze.py
```

Every untracked path outside `.ufo/waves/round-96/` is one of the 13 declared corpus additions. All other untracked content (17,900 paths at freeze) lives under `.ufo/waves/round-96/{seats,scratch,Q6-scratch,V13-scratch,V18-scratch}` — seat reports and verifier scratch (including mutation copies of chain fixtures under `seats/scratch/V17/`, `seats/V01-scratch/`), lane-internal and inside the wave's declared write area. The round-96 top level contains only `seats/`, `scratch/`, `Q6-scratch/`, `V13-scratch/`, `V18-scratch/` — no stray files. No lane-root scratch residue: `ls -d map-obligations-self-test-* dependency-freeze-self-test-*` → no output (BR-05-class lane-root scratch was not triggered in this round; I did not run `--self-test` myself). New files are regular mode-644 files, zero symlinks (`find … -type l` → empty).

### A2.3 Fleet-root scan (sibling lanes / domain trees)

```
$ cd /home/vgpnk/Projects/shokunin && find . -newermt "2026-10-17 17:35" -type f -not -path "./lore-shokunin/*" -not -path "*/.git/*"
./kotodama-shokunin/… (its own concurrent rounds 8/9: reports/round-8, reports/round-9, corpus/knowledge/civilizations, examples, LOG.md, SCORECARD.md, SKILL.md, .scratch/…)
./MANIFEST.json
./.ufo/l0-questions.md
./.ufo/reports/round-8/kotodama.md
```

Interpretation, reported as found: the only sibling-lane paths modified in the window belong to **`kotodama-shokunin`'s own concurrent rounds** (round-8 and round-9 reports, knowledge, examples and its own `.scratch/`); the parent-level `MANIFEST.json`, `.ufo/l0-questions.md`, and `.ufo/reports/round-8/kotodama.md` are fleet-level files written by other lanes' activity. No lore path appears among them; a lore-name/`r96` filter over the same window returns nothing. `/home/vgpnk/Projects/shokunin/.ufo/waves/round-96` does not exist (no parent-tree stray wave dir — the r94/r95 defect class did not recur). Sibling `PROVINCE.md` mtimes are all pre-round (latest: `kotodama-shokunin` 12:59; `lore-shokunin` 2026-10-15). No write to any sibling lane or domain source tree is attributable to an r96 lore seat.

### A2.4 System-temp scratch — observed, reported exactly

```
$ find /tmp -maxdepth 1 -newermt "2026-10-17 17:35" | sort
/tmp
/tmp/o1
/tmp/o2
/tmp/selftest-out.json
/tmp/wl-copy-buffer-Cw59Sl
/tmp/x02-poll.sh
```

Five in-window entries, plausibly verifier/producer ephemeral scratch (a poll helper, a self-test dump, two one-letter files, a clipboard buffer); none is a sibling repository or domain source tree, so none breaches `PROVINCE.md:11`. Disclosed as protocol-level evidence, not smoothed over. **Self-disclosure:** this seat created no `/tmp` files and no scratch dir at all; every check ran inline from the lane root.

**Result: PASS** (no writes to sibling lanes or domain source trees attributable to r96; `/tmp` scratch observed and disclosed).

---

## A3 — mythology content stays editorial-only in the new bytes

**JSON-level separation (walk of every `source_id` binding in the fixture):**

```
declared source ids: ['aru-aftermath-note', 'crossing-minute', 'evin-response-note', 'paired-clock', 'veil-verse']
bound source ids  : ['aru-aftermath-note', 'crossing-minute', 'evin-response-note', 'paired-clock']
all bound in declared fictional set: True
```

No external comparator is bound as JSON support, and no mythology name appears in any fixture JSON:

```
$ grep -n -i -E "spence|kojiki|chamberlain|gutenberg|inana|ovid|maya|kiche|k'iche|etcs" corpus/fixtures/r96-crossing-response/*.json
(none)
```

**Checker-level row-class separation (real runs on the delivered revision, all exit 0):**

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response
CLEAN: schema, citations, relations, timeline; 0 violations          exit=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response
RECEIPT JSON-FACTS 16; EDITORIAL-ROWS 2; TOTAL-ROWS 18
SOURCE-SUPPORT 16/16; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 18/18; VALIDATED-ROWS 18/18
RESULT PASS                                                          exit=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response
OBLIGATIONS raw=16 mapped=16
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18
RESULT PASS                                                          exit=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath   # regression on the hardened tool
OBLIGATIONS raw=15 mapped=15 / RESULT PASS                           exit=0
```

The Spence material stays in the two `editorial-row`s; all 16 JSON facts bind only fictional in-world sources. The editorial rows are unchanged: a row extraction of r95 vs r96 maps shows 2 editorial rows each and `S01`/`S02` line-identical (`S-rows identical: True`). The five inherited byte copies keep the r95 refusals verbatim.

**Explicit refusal lines in the new bytes (verbatim):**

- `corpus/fixtures/r96-crossing-response/README.md:19` — "It supplies no in-world witness, cultural authority, or fictional canon, and asserts no cultural meaning. Rights and AI-training permission remain unassessed; neither is granted or inferred here."
- `claim-excerpt-map.md:41` — "they do not make Spence an in-world witness, assign cultural meaning, or add canon."; `:56` — receipt "not … source authenticity, truth, rights, permission, or canon".
- `corpus/knowledge/r96-response-scope-note.md:7` — "This is a bounded knowledge record, not merged canon, not a contradiction finding, and not a verdict on any character."; `:61` — "Rights and AI-training permission remain unassessed here."
- `inspiration-note.md:13-21` (byte copy of r95) — `## Rights question` / `## AI-training-permission question`, both open; "It is not an in-world source and supplies no fictional canon."

The new authored content (`evin-response-note` + tick-12 event) is in-world fiction, not external myth, and carries its own bound in the bytes: "It asserts no accusation against Aru, selects no winner, and states that both first-person accounts stand unresolved. It records one crossing occasion only and is not evidence of a breach, a continuing duty, a perpetual obligation, or an external historical fact" (`sources.json#/4`); `contradictions.json` remains `[]`.

**Result: PASS.**

---

## A4 — rights / canon / mechanics language scan (all r96 new bytes)

Scan pattern `rights|licen[cs]e|copyright|permission|canon|mechanic|gameplay|ruleset|damage|stats|balancing|public domain|training` over: the 10 fixture files, `corpus/knowledge/r96-response-scope-note.md`, `corpus/tools/dependency_freeze.py`, `corpus/tools/dependency-freeze-contract.json`, the `map_obligations.py` diff, and the `README.md`/`map-obligations-contract.json` diffs. Every hit is a refusal, an open question, a scope exclusion, or the JSON-Pointer sense of "canonical" — no rights finding, no permission grant, no canon assertion, no mechanics claim:

- `claim-excerpt-map.md:1,16` — "canonical" only in the JSON-Pointer sense ("canonical claim-to-excerpt map", "16 canonical pointers"); `:41,:56` — refusals.
- `inspiration-note.md:13-19` — rights/permission questions stated open ("has not been determined for all jurisdictions"; "does not imply permission for training").
- `README.md:19,21` — rights/permission "remain unassessed; neither is granted or inferred here"; receipt "not … rights, permission, or canon review".
- `r96-response-scope-note.md:3,7,35,61` — "not merged canon"; "None reads either note as testimony or decides truth, breach, chronology, rights, permission, or canon"; "Rights and AI-training permission remain unassessed here."
- `dependency-freeze-contract.json:4` — scope line "no chronology truth, entailment, source, rights, or canon judgment".
- `map_obligations.py` diff — only JSON-Pointer "canonical" uses (docstring "canonical map", "one canonical inline-code pointer", "canonical decimal").
- `corpus/tools/README.md` diff — "canonical" only in the pointer-grammar sense (the new `dual_pointer` scan text: "a backticked or bare canonical `file.json#/…` pointer").

No occurrence of `mechanic`, `gameplay`, `ruleset`, `damage`, `stats`, `balancing`, or "public domain" in any r96 new byte. No sibling-lane path string (`kotodama`, `game-dev`, `art-east-asian`, `sibling`) and no `../` escape appears in any new byte or in the Q1/Q2 diffs (grep → empty).

**Result: PASS.**

---

## A5 — the new records are lore-owned and the reports match the bytes

- All 13 new corpus files are regular mode-644 files inside this lane, in the declared paths: `corpus/fixtures/r96-crossing-response/` (10), `corpus/knowledge/r96-response-scope-note.md`, `corpus/tools/dependency_freeze.py`, `corpus/tools/dependency-freeze-contract.json` — exactly the record kinds and tool files `PROVINCE.md`/the round declaration own. No symlinks, no non-regular files.
- The five declared byte copies are byte-identical to r95 (`cmp` → OK ×5: `entities.json`, `relations.json`, `contradictions.json`, `inspiration-note.md`, `source-excerpt.md`; sha256 pairs equal, e.g. entities `026af0bc…`, relations `c279254b…`, contradictions `37517e5f…`, inspiration-note `58f5390e…`, source-excerpt `b5edc2fd…`). `fictional-excerpts.md` is a strict byte-prefix: r95's 1845 bytes are the prefix of r96's 2588 bytes (`head -c 1845 | cmp` → identical). `timeline.json` and `sources.json` prefixes are parsed-equal to r95 (`r96[:4]==r95` → `True` both).
- Counts measured from the delivered JSON: 5 entities / 1 relation / 5 events / 5 sources; 16 source-attributed obligations (15 inherited rows + new J16); census `ls -d corpus/fixtures/*/ | wc -l` = **170** (169 at r95 closure). The new event is tick-12 `response-evin-salt-court` (`entity_id: evin`, `place_id: salt-court`, `depends_on: ["aftermath-missing-evin"]`, `source_id: evin-response-note`).
- Delivered hashes match the producer reports: Q1 tool `2b0ba815…`; Q2 contract `97b76bb8…`, README `965b29cd…`; Q3 tool `a3b57978…`, contract `7d568cc4…`; Q4 sources `9f973f63…`, timeline `ea0225f9…`, fictional-excerpts `06b11bec…`; Q5 README `ff52ced4…`, map `5093d72e…`. Q6's report states no hash of its note; I bound it independently: `6db32ca24f5eff5baa3ebe589e8d3bcb6b256fec18dee2468211d7d0fae157c6`, and its three claimed receipts re-run by me on the delivered revisions all PASS (§A3).
- Report-vs-byte ordering (no post-report rewrites observed): every producer artifact mtime precedes its report mtime — Q1 tool 17:47:24 → report 17:52:17; Q2 contract 17:50:17, README 17:51:26 → report 17:52:12; Q3 files 17:44:27/17:44:37 → report 17:47:26; Q4 files 17:38:26–17:40:16 → report 17:47:19; Q5 files 17:43:09/17:43:17 → report 17:45:37; Q6 note 17:47:02 → report 17:47:16. Delivered hashes stable across my whole battery (17:48 → 17:53:44).
- Fail-closed and chain controls on the delivered revision: `dependency_freeze.py` verify on the four chain fixtures → `r88 2/2 events`, `r94 3/3 events; 2 edges`, `r95 4/4; 3 edges`, `r96 5/5; 4 edges`, all `RESULT PASS` exit 0; `map_obligations.py` r95 regression PASS (§A3).

**Result: PASS.**

---

## Observations reported as found (not province breaches)

1. **Mid-flight transients, disclosed by producers** — Q4's joining-comma rewrite (17:39, before its receipts); Q6's receipt at an intermediate Q1 revision `6634e176…` (17:46, disclosed in its caveats); Q2's poll on Q1's landing. All pre-report and self-reported; on the delivered bytes Q1's tool is `2b0ba815…` and Q2's contract declares the 24-case set. I did not re-run `--self-test` (it would create scratch); the case lists are the C1 verifiers' scope, not this seat's.
2. **`/tmp` scratch practice** — five in-window entries (§A2.4), same class as r95's disclosed observation; bounded follow-up candidate, not smoothed over.
3. **`SCORECARD.md` vs the declared baseline** — its delta is the committed `60dba0c` r95-closure section; it is not an r96 write and not in the producers' byte scope. Worth pinning in the closure arithmetic so the baseline/HEAD distinction (`dcb2d92` vs `60dba0c`) is explicit.
4. **Verifier scratch volume** — ~17,900 untracked files under `.ufo/waves/round-96/` (mutation copies of chain fixtures under seat scratch dirs). Lane-internal and inside the declared seat-write area; visible only as untracked volume, not a breach.
5. **New tool scratch location** — `dependency_freeze.py` self-test uses `tempfile.TemporaryDirectory(prefix="dependency-freeze-self-test-")` **without** `dir=ROOT` (system temp, unlike BR-05's lane-root scratch in `map_obligations.py`); no lane-root self-test residue was observed this round.

---

## Bottom line

**PASS** — `PROVINCE.md` is byte-identical to `dcb2d92` (blob `7c599c39`, sha256 `94a7a77e…`, empty diff); the round's entire change set is lane-local and exactly the declared byte ownership (3 tool files modified, 13 corpus files added, `LOG.md` declaration; `SCORECARD.md` attributed to the committed r95-closure `60dba0c`), with zero writes to sibling lanes or domain source trees — the only caveats being disclosed ephemeral `/tmp` scratch (5 in-window entries) and ~17,900 lane-internal verifier scratch files under the round dir; mythology stays editorial-only in the new bytes (no external comparator bound in JSON, Spence rows labelled `editorial-row` and unchanged, explicit no-witness/no-canon refusals in README/map/note); and the rights/canon/mechanics scan over every r96 new byte returns only refusals, open questions, scope exclusions, and JSON-Pointer "canonical" uses.
