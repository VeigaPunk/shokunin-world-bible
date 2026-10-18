# V30 — adjacency verdict (round 98)

**Seat:** V30 (verdict-adjacency), round-98 single wave (64 seats), lane `lore-shokunin`.
**Subject:** the delivered r98 working tree vs baseline r97 closure `9a3d648` (HEAD is `dd4df1b` "lore r97: close round — SCORECARD admitted section", the committed r97-closure section that sits above the declared baseline; no r98 commit exists — hard rule, no commits).
**Scope of this seat:** `PROVINCE.md` byte-identity; no writes outside `lore-shokunin` and none inside it outside the declared producer byte-ownership; a rights/canon/mechanics language scan over every new r98 byte and every round diff; the r95 map repair's cosmesis (adjacency to the frozen r95 cluster); reports-vs-bytes ordering and stability. This seat makes **no** C1/C2/C3 verdict, no admission verdict, and no lore-truth ruling.
**Measurement freeze:** all five producer reports present at 20:35:33 (`S1-freeze-hygiene.md` last); every producer artifact mtime precedes its owner's report mtime (§A6). Frozen hash manifest taken 20:35:49, re-digested 20:36:2x, 20:36:31 and 20:37:32 — digest `62f65f2656dd0da092569b5209b630d1daca40633f3508279e9760d3ed1c3810` at every point (no post-freeze rewrites). All commands ran from `/home/vgpnk/Projects/shokunin/lore-shokunin`. This seat's only writes are this report plus declared scratch under `.ufo/waves/round-98/seats/V30-scratch/`.

## Poll-wait record (protocol compliance)

- Poll 1 (background, 20 s cadence, 40 tries, started 20:28:32): first check 20:28:32 already saw the 10-file fixture (S3's copy step had landed; content landed later); r95 map modified by 20:28:52; r95/r96 note addenda by 20:29:32; `dependency_freeze.py` + contract by 20:31:32; `r98-clerk-scope-note.md` by 20:32:32; `corpus/tools/README.md` by 20:33:52 → `ALL-PRESENT t=20:33:52 n=17`.
- **Honest disclosure:** poll 1's report gate (`reports >= 5`) was satisfied by *verifier* reports, not producer reports — `S1-*.md` and `S2-*.md` were still absent at that point. I did not verify on that state.
- Poll 2 (targeted: wait for `S1-*.md` AND `S2-*.md` only; 20 s cadence, 40 tries): `POLL2 t=20:34:43 n=1 S1=0 S2=1`; `POLL2 t=20:35:03 n=2 S1=0 S2=1`; `POLL2 t=20:35:23 n=3 S1=1 S2=1` → `S1S2-PRESENT t=20:35:23`.
- I verified only after all five producer reports and all artifacts existed; I never verified a plan. No ABSENT condition occurred and no stall escape was needed. Endgame convention honoured: no poll waited for all reports, and none waited on SELF.
- Mid-flight bytes did change while producers worked (e.g. `dependency_freeze.py` was `1a01fd17…` when I first hashed it ~20:31:35 and `03d04365…` from 20:31:49; the contract was `3a940a9f…` then `153ebc5b…` from 20:33:36). The freeze below is strictly post-report; stability was re-checked three times afterwards.

---

## A1 — `PROVINCE.md` byte-identical to `9a3d648`

```
$ sha256sum PROVINCE.md
94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa  PROVINCE.md
$ git show 9a3d648:PROVINCE.md | sha256sum
94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa  -
$ git hash-object PROVINCE.md
7c599c395e1710b6a7c7aca6d485c373bed6deb7
$ git rev-parse 9a3d648:PROVINCE.md
7c599c395e1710b6a7c7aca6d485c373bed6deb7
$ git diff 9a3d648 -- PROVINCE.md | wc -c
0
```

Blob identity, sha256 and the byte diff all agree; re-checked after the whole battery (same three values). The other province-level documents are likewise byte-identical to the baseline:

```
PROVINCE.md      IDENTICAL 7c599c395e1710b6a7c7aca6d485c373bed6deb7
SHONEN.md        IDENTICAL 561b3f8ce99e35200fcfa2269198a7f7f68f1a5e
SKILL.md         IDENTICAL bf704be30cf263b881152451dcba5010facbccdd
README.md        IDENTICAL 7c46413cf7781ae3cdbaa7bae7e265f7ddcbbe70
l0-questions.md  IDENTICAL f9fdff500e043c63d7bbfd0ffad90f8cfd66de4e
```

**Result: PASS.**

---

## A2 — no writes outside `lore-shokunin` (and none inside it outside the declared byte-ownership)

### A2.1 Whole-tree blob audit vs `9a3d648`

Blob-level comparison of every tracked file outside `.ufo/` (worktree `git hash-object` vs `9a3d648` tree), so in-place edits cannot hide behind unchanged path names:

```
$ .ufo/waves/round-98/seats/V30-scratch/blob-audit.sh
tracked-non-ufo base files: 2829
CHANGED:
   LOG.md
   SCORECARD.md
   corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md
   corpus/knowledge/r95-aftermath-scope-note.md
   corpus/knowledge/r96-response-scope-note.md
   corpus/tools/README.md
   corpus/tools/dependency-freeze-contract.json
   corpus/tools/dependency_freeze.py
MISSING:
```

Attribution against the declared producer byte-ownership — exactly the declared set, nothing extra, nothing missing:

- `corpus/tools/dependency_freeze.py` + `dependency-freeze-contract.json` → **S1**; `corpus/tools/README.md` → **S2**; `r95-crossing-aftermath/claim-excerpt-map.md` (repair) + `r98-clerk-filing/` JSON tables and `fictional-excerpts.md` → **S3**; r98 `README.md` + `claim-excerpt-map.md` → **S4**; `r98-clerk-scope-note.md` + the two dated addenda → **S5**.
- `LOG.md` is the pre-dispatch r98 declaration: `git diff --numstat 9a3d648 -- LOG.md` → `61 0 LOG.md` (61 added, 0 deleted); deletion-line count `0`.
- `SCORECARD.md` is **not an r98 write**: `git diff HEAD -- SCORECARD.md | wc -c` → `0`, and `git log -1 -- SCORECARD.md` → `dd4df1b lore r97: close round — SCORECARD admitted section`. Its 33-line delta vs `9a3d648` is the committed r97-closure section above the declared baseline.

### A2.2 Untracked audit

```
$ git status --porcelain -uall | grep -c '^??'
44698
$ git status --porcelain -uall | grep '^??' | grep -c '^?? \.ufo/waves/round-98/'
44687
$ git status --porcelain -uall | grep '^??' | grep -v '^?? \.ufo/waves/round-98/' | grep -v -E '^\?\? corpus/(fixtures/r98-clerk-filing/|knowledge/r98-clerk-scope-note.md)'
(empty; rc=1)
```

44,698 untracked entries total: 44,687 under `.ufo/waves/round-98/` (seat reports, per-seat scratch, the wave-top-level files in §Observations 2) and exactly the 11 declared corpus additions outside it — `corpus/fixtures/r98-clerk-filing/` (10 files) + `corpus/knowledge/r98-clerk-scope-note.md`. New fixture files are regular mode-644, zero symlinks (`find … -type l | wc -l` → `0`; `find … -type f ! -perm 644 | wc -l` → `0`). Fixture census: `ls -d corpus/fixtures/*/ | wc -l` → **172** (171 at r97).

### A2.3 Fleet-root scan (sibling lanes / domain trees)

```
$ cd /home/vgpnk/Projects/shokunin && find . -newermt "2026-10-17 20:27" -type f -not -path "./lore-shokunin/*" -not -path "*/.git/*" | wc -l
9          (all under ./kotodama-shokunin/reports/round-12/** and its .scratch/r12-clone)
$ find . -maxdepth 1 -newermt "2026-10-17 20:27" -type f
./baseline-analyze.txt
$ ls -d .ufo/waves/round-98
no parent round-98 wave dir
```

Interpretation, reported as found: every in-window sibling path belongs to **`kotodama-shokunin`'s own concurrent round-12 activity** (9 files, its own reports/scratch). The parent-root file `baseline-analyze.txt` (20:30:10, 105 bytes) contains only the line `python3: can't open file '/home/vgpnk/Projects/shokunin/analyze.py': [Errno 2] No such file or directory` — no lore or r9x content (`grep -c -i -E "lore|r9[678]"` → `0`); it is not attributable to a lore seat and is reported, not smoothed over. There is no parent `.ufo/waves/round-98` directory (the r94-F01 parent-stray-wave class did not recur), and the parent repo `git status --porcelain` shows only that one untracked file. No write to any sibling lane or domain source tree is attributable to an r98 lore seat.

### A2.4 System-temp scratch — observed, reported exactly

```
$ find /tmp -maxdepth 1 -newermt "2026-10-17 20:27" | wc -l
58
```

~50 of those entries match lore-seat scratch patterns (`/tmp/df-<fixture>.out`, `/tmp/v33-chain-*`, `/tmp/v47-*`, `/tmp/v59-*`, `/tmp/s2-r98`, `/tmp/poll_s5.sh`, `/tmp/r95_base.md`, `/tmp/r96_base.md`, `/tmp/V07-contract-baseline.json`, …) — the same disclosed ephemeral-scratch class as r95/r96/r97, this round at higher volume. None is a sibling repository or domain source tree, so none breaches `PROVINCE.md`'s write boundary. **Self-disclosure:** this seat's only scratch is `.ufo/waves/round-98/seats/V30-scratch/` (poll scripts/logs, `blob-audit.sh`, `manifest.sh`, four freeze manifests, pre-repair r95 copy, receipt transcripts); I created no `/tmp` files.

**Result: PASS** (no writes to sibling lanes or domain source trees attributable to r98; lane-internal scratch volume and `/tmp` practice disclosed).

---

## A3 — external/mythology content stays editorial-only in the new bytes

**Byte-copy integrity of the preserving copy:**

```
$ for f in relations.json contradictions.json inspiration-note.md source-excerpt.md; do
    cmp corpus/fixtures/r98-clerk-filing/$f corpus/fixtures/r97-crossing-acknowledgment/$f && echo "IDENTICAL $f"; done
IDENTICAL relations.json
IDENTICAL contradictions.json
IDENTICAL inspiration-note.md
IDENTICAL source-excerpt.md
$ # strict prefix of the authored excerpts file:
r97=3410 r98=4187; head -c 3410 corpus/fixtures/r98-clerk-filing/fictional-excerpts.md | cmp - corpus/fixtures/r97-crossing-acknowledgment/fictional-excerpts.md
STRICT-BYTE-PREFIX
```

`README.md` and `claim-excerpt-map.md` are S4-authored (not copies); the six inherited JSON rows were verified parsed-equal (entities 5/5, sources 6/6, timeline 6/6; relations and contradictions identical), matching the README's own continuation statement.

**JSON-level separation:**

```
$ grep -rn -i -E "Spence|Kojiki|Chamberlain|Gutenberg|ETCSL|Inana|Ovid|Maya|Kiche|K'iche" corpus/fixtures/r98-clerk-filing/*.json
(no output; rc=1)
$ grep -n -i -E "Spence|Gutenberg|K'iche" corpus/knowledge/r98-clerk-scope-note.md
(no output; rc=1)
```

**Counts measured from the delivered JSON:** 6 entities / 1 relation / 0 contradictions / 7 timeline events / 7 sources; `check_bible.py corpus/fixtures/r98-clerk-filing` → `CLEAN: schema, citations, relations, timeline; 0 violations`, exit 0; `map_obligations.py` → `OBLIGATIONS raw=20 mapped=20` / `INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22` / `RESULT PASS` (rc=0); `support_check.py` → `RECEIPT JSON-FACTS 20; EDITORIAL-ROWS 2; TOTAL-ROWS 22` / `SOURCE-SUPPORT 20/20; EDITORIAL-ANCHORS 2/2; MODES 22/22; VALIDATED-ROWS 22/22` / `RESULT PASS` (rc=0).

**The Spence material remains two separately labelled editorial rows** (`claim-excerpt-map.md:40` "## Editorial rows (2 bounded Spence comparisons; not JSON facts)", rows S01/S02 at `:46-47`), and the new authored content is in-world fiction whose own reliability note bounds it (`sources.json:42`: "… It asserts no finding, no verdict, no reconciliation, and no resolution; it is not evidence of a breach, a continuing duty, a winner between the accounts, or an external historical fact."). `contradictions.json` stays `[]`.

**Explicit refusal lines in the new bytes (verbatim, non-exhaustive):**

- `corpus/fixtures/r98-clerk-filing/README.md:19` — "It supplies no in-world witness, cultural authority, or fictional canon, and asserts no cultural meaning. Rights and AI-training permission remain unassessed; neither is granted or inferred here."; `:21` — receipt "not whole-claim entailment, source authentication, chronology truth, rights, permission, or canon review".
- `claim-excerpt-map.md:45` — "they do not make Spence an in-world witness, assign cultural meaning, or add canon."; `:68` — "not manual whole-claim entailment or a verdict on source authenticity, truth, rights, permission, or canon".
- `corpus/knowledge/r98-clerk-scope-note.md:8` — "not merged canon, not a finding, not an adjudication, and not a verdict on any character"; `:39` — "None reads the note as testimony or decides truth, finding, chronology, adjudication, rights, permission, or canon."; `:72` — "Rights and AI-training permission remain unassessed here."
- `inspiration-note.md` (byte copy, r97 wording) — rights/AI-training questions stated open; "It is not an in-world source and supplies no fictional canon."

Light path-existence check of the note's cited records: all 20 distinct cited `corpus/...` paths exist (the three "missing" strings my first regex returned were brace-list citation artifacts, not real paths); the r10 precedent it cites exists (`corpus/fixtures/r10-registry-witness/registrar-copy-excerpt.md`, `sources.json`) and its quoted r10 discipline line resolves (`corpus/knowledge/2026-10-12-lore-decision-table.md:112` — "This is an authored second perspective, not external corroboration or canon resolution.").

**Result: PASS.**

---

## A4 — rights / canon / mechanics language scan (all r98 new bytes + all round diffs)

Scan set (82,644 bytes captured to scratch as `round-all-bytes.txt`): the `git diff 9a3d648` of `corpus/tools/` (all three files), the r95 map repair and the two knowledge-note addenda, plus the full delivered bytes of `corpus/knowledge/r98-clerk-scope-note.md` and all 10 r98 fixture files.

```
$ grep -n -i -E "mechanic|gameplay|ruleset|damage|stats|balancing|hit ?point|dice|combat|level.?up|public domain|fair use|free to (use|reuse)|may be (used|reproduced)|licensed under|permission is granted" round-all-bytes.txt
(no output; rc=1)
$ grep -n -E "/home/|\.\./|/tmp/|kotodama|game-dev|art-east|kengaku|mado|tabi" round-all-bytes.txt
(no output; rc=1)
```

Zero mechanics words, zero rights-grant phrases, zero absolute paths, zero `../` escapes, zero sibling-lane or domain-tree names anywhere in the round's new bytes or diffs. Every hit of the broader pattern `rights|licen[cs]e|copyright|permission|canon|training|attribut` is a refusal, an open question, a scope exclusion, or the JSON-Pointer sense of "canonical" (e.g. `claim-excerpt-map.md:1` "canonical claim-to-excerpt map", `:16` "20 canonical pointers"). The one scope sentence in the tool contract keeps the refusal form: `dependency-freeze-contract.json` — "no chronology truth, entailment, source, rights, or canon judgment; `--freeze` is scope-guarded to `corpus/fixtures/**` and every pin records the fixture's repo-relative path, which verification enforces (SCOPE-REFUSED / PATH-MISMATCH)".

**Result: PASS.**

---

## A5 — the r95 map repair is cosmetic-only (adjacency to the frozen r95 cluster)

```
$ git diff 9a3d648 -- corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md | grep -c '^@@'
1
$ git diff 9a3d648 -- corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md | grep -E '^[+-][^+-]' | cut -c1-80
-The inherited tick-9 entries … The new relation encodes only the agreement for this crossing, not perpetual …
+The inherited tick-9 entries … The relation encodes only the agreement for this crossing, not perpetual …
$ git diff 9a3d648 -- corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md | grep -E '^[+-]' | grep -c '^[+-]|'
0
```

Exactly one hunk, one in-place prose line (inside `## Timeline normalization and scope`), zero table rows, pointers, anchors, spans or modes changed. Receipts pre-repair vs post-repair, measured on the delivered revision (pre-repair reconstructed from `9a3d648` into my scratch, the other nine files copied from the delivered fixture since they are byte-identical to baseline):

```
pre support rc=0 / post support rc=0 ; pre map rc=0 / post map rc=0
$ diff r95-pre.support.txt r95-post.support.txt && echo SUPPORT-RECEIPTS-IDENTICAL
SUPPORT-RECEIPTS-IDENTICAL
$ diff r95-pre.map.txt r95-post.map.txt && echo MAP-RECEIPTS-IDENTICAL
MAP-RECEIPTS-IDENTICAL
```

Post-repair receipts: `support_check` → `RECEIPT JSON-FACTS 15; EDITORIAL-ROWS 2; TOTAL-ROWS 17` / `SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS 2/2; MODES 17/17; VALIDATED-ROWS 17/17` / `RESULT PASS`; `map_obligations` → `OBLIGATIONS raw=15 mapped=15` / `RESULT PASS`; both exit 0 and byte-identical to the pre-repair runs. The two dated note addenda are likewise append-only: `git diff --numstat 9a3d648` → `14 0` each, deletion-line count `0`, and the baseline bytes are a strict prefix of each delivered note (`cmp` on the first N bytes → identical).

**Result: PASS.**

---

## A6 — reports match the bytes (ordering and stability)

Every producer artifact mtime precedes its owner's report mtime — no post-report rewrites:

| Seat | artifact mtimes | report mtime |
|---|---|---|
| S1 | `dependency_freeze.py` 20:31:49, `dependency-freeze-contract.json` 20:33:36 | 20:35:33 |
| S2 | `corpus/tools/README.md` 20:34:06 | 20:34:53 |
| S3 | r95 map 20:28:34; r98 fixture JSON/excerpts 20:28:24–20:30:21 | 20:31:25 |
| S4 | r98 `claim-excerpt-map.md` 20:30:21, `README.md` 20:30:41 | 20:32:06 |
| S5 | r95/r96 addenda 20:29:14, `r98-clerk-scope-note.md` 20:33:01 | 20:34:00 |

Delivered hashes at freeze (20:35:49) — `PROVINCE.md 94a7a77e`, r95 map `80440d61`, r98 README `32efc78f`, r98 map `c1099d0e`, r98 entities `db2d8e5d`, relations `c279254b`, contradictions `37517e5f`, timeline `eb24e084`, sources `32ee15b1`, fictional-excerpts `29e384bf`, inspiration-note `58f5390e`, source-excerpt `b5edc2fd`, r98 note `1162262c`, r95 note `8e9e1774`, r96 note `a9b51f8c`, r97 note `5e3b4225`, `dependency_freeze.py 03d04365`, `dependency-freeze-contract.json 153ebc5b`, `corpus/tools/README.md 1d299c16` — re-digested identically at three later points (manifest digest `62f65f26…`). S1's report cites exactly the frozen tool/contract hashes (`03d04365…`, `153ebc5b…`). `HEAD` is still `dd4df1b` and `git reflog -1` shows no seat commit; no stash exists.

Timestamp integrity checked, not assumed: for the live `dependency_freeze.py` and contract `stat` gives `mtime == ctime` to the nanosecond (20:31:49.482566759 and 20:33:36.611874789) — the signature of an ordinary write, not a preserved/forged timestamp. The two content changes I observed mid-flight (`1a01fd17…` → `03d04365…`; `3a940a9f…` → `153ebc5b…`) both landed before the owning report, so no measurement here rests on a mid-flight byte.

**Result: PASS.**

---

## Observations reported as found (not province breaches)

1. **Mid-flight byte churn, pre-freeze.** `dependency_freeze.py` and the contract each changed once after my first hash (see A6); the r98 fixture README/map were r97 byte-copies until S4 authored them at 20:30; the r95/r96 notes carried r97 bytes until S5's addenda at 20:29. The freeze is strictly post-report.
2. **Wave-top-level writes by two verifier seats.** `.ufo/waves/round-98/` holds 4 files at its top level — `V14-poll.sh`, `V14-poll.log`, `V14-poll2.log` and V36's `receipt.json` (the wave presence-audit skeleton, `record_type: round-98-receipt`, 499 lines). In r97 the round top level held 0 files; the declared seat write areas are the report path and per-seat scratch. Lane-internal and inside the wave directory, so no boundary breach — recorded as a protocol-level deviation.
3. **Verifier scratch volume.** 44,687 of the 44,698 untracked entries live under `.ufo/waves/round-98/`; several are full fixture copies (e.g. `scratch/V01/base-fixture-src/`, `scratch/V03/handrun-delivered/{legacy,mismatch}/`), plus a root-level `v05-self-test-scratch/` that matches the `.gitignore` pattern and therefore does not surface in `git status`. Visible only as untracked volume; lane-internal.
4. **`/tmp` scratch practice** (§A2.4): 58 in-window entries, ~50 lore-seat artifacts; same class as r95–r97, disclosed.
5. **Parent-root `baseline-analyze.txt`** (20:30:10, 105 bytes, a python3 error dump with no lore content) — not attributable to a lore seat; the parent repo shows it untracked. Reported for the closure arithmetic.
6. **Doc contradiction in the delivered tools README (out of this seat's axis; flagged for the doc-parity seat).** `corpus/tools/README.md:230` (r97 supersession, still current text) states "Both tools' self-test scratch directories are created at the repository root and covered by `.gitignore` (`*-self-test-*/`)", while `:232` (r98 addendum) and `:99` (carried r94 text) state "the self-test scratch still lives under the repository root and is not gitignored — unchanged in r98". Empirically the gitignore sentence is correct and the BR-05 sentence is stale: `map_obligations.py:831` uses `prefix="map-obligations-self-test-"` and `dependency_freeze.py:544` uses `prefix="dependency-freeze-self-test-"`, and `git check-ignore -v map-obligations-self-test-abc/ dependency-freeze-self-test-abc/` returns `.gitignore:4:*-self-test-*/` for both (rc=0; the pattern is present in the baseline tree: `git show 9a3d648:.gitignore`). This is a doc-parity matter, not an adjacency harm; I report it exactly as found and make no ruling on it.

---

## Bottom line

**PASS** — `PROVINCE.md` is byte-identical to `9a3d648` (blob `7c599c39`, sha256 `94a7a77e…`, empty diff; SHONEN/SKILL/README/l0-questions likewise), the round's entire change set is lane-local and exactly the declared producer byte-ownership (8 tracked files changed: S1's tool + contract, S2's tools README, S3's r95 map repair, S5's two note addenda, plus `LOG.md` +61/−0 declaration and `SCORECARD.md` attributed to the committed r97 closure `dd4df1b`; 11 corpus files added; 172-fixture census) with zero writes to sibling lanes or domain source trees — the only caveats being disclosed `/tmp` and lane-internal scratch, two verifier files written at the wave top level, and one non-lore parent-root stray; mythology stays editorial-only in the new bytes (4 preserved files byte-identical to r97, excerpts a strict byte prefix, zero external names in any r98 JSON, Spence rows still 2 editorial rows, refusals present in README/map/note); the rights/mechanics scan over 82,644 bytes of new bytes and diffs returns zero mechanics words, zero rights-grant phrases, zero path or sibling-lane leakage; the r95 map repair is provably cosmetic (one hunk, one prose line, zero table rows, receipts byte-identical pre vs post) and the two note addenda are append-only strict prefixes; and every producer artifact precedes its report with the frozen manifest digest stable across four measurements.
