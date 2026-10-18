# V28 — adjacency (round 97)

**Seat:** V28 (adjacency), round-97 single wave, lane `lore-shokunin`.
**Subject:** the delivered r97 working tree vs baseline r96 closure `f3e09f9` (HEAD is `2393934` "r96: close round — SCORECARD admitted section", a post-baseline r96-closure commit). No r97 commit exists (hard rule: no commits), so every check below is a **worktree-vs-baseline** measurement.
**Scope of this seat:** `PROVINCE.md` byte-identity, no writes outside `lore-shokunin` (whole-tree write attribution vs the declared producer byte-ownership), and a rights/canon/mechanics language scan over every new r97 byte. This seat makes **no** C1/C2/C3 verdict, no admission verdict, and no lore-truth ruling.
**Measurement freeze:** all six producer reports present at 18:56:23 (`R3-freeze-hardening.md` last); every producer artifact mtime precedes its report mtime (§A6). Frozen hash manifest taken at 18:56:34; the same manifest re-digested at 18:58:21, 18:58:33 and 18:58:56 — digest `b88c9a172ba8311a3bc9693e00575b35e6a73729c2a05d39bd1bd8f798a6c0b8` at every point (no post-freeze rewrites). All commands run from `/home/vgpnk/Projects/shokunin/lore-shokunin`. This seat's only writes are this report plus declared scratch under `.ufo/waves/round-97/seats/V28-scratch/`.

## Poll-wait record (protocol compliance)

- First check 18:42:5x: fixture `r97-crossing-acknowledgment/` absent, note absent, zero `R*.md` reports; 20 s cadence.
- Loop 1 (background, 40 tries): observed the fixture fill in — 10/10 files by 18:44:25; `corpus/knowledge/r97-acknowledgment-scope-note.md` at 18:50:52; reports R2 18:49:31, R4 18:50:14, R5 18:51:25, R1 18:52:25, R6 18:53:37, R3 18:56:23. The background poller hit its ~13-minute ceiling just before the last report landed; the foreground loop detected **ALL-PRESENT at 18:56:23**.
- I verified only after all six producer reports and all artifacts existed; I never verified a plan. No ABSENT condition occurred.
- Mid-flight bytes did change while producers worked (e.g. `dependency-freeze-contract.json` was `8015e1f9…` at 18:53:37 and `27273be2…` at 18:55:14); the freeze below is strictly post-report, and stability was re-checked at three later points.

---

## A1 — `PROVINCE.md` byte-identical to `f3e09f9`

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

Blob identity, sha256, and the byte diff all agree. Re-checked at 18:58:56 after the whole battery: unchanged. The other province-level documents are likewise byte-identical to the baseline:

```
PROVINCE.md      IDENTICAL 7c599c395e1710b6a7c7aca6d485c373bed6deb7
SHONEN.md        IDENTICAL 561b3f8ce99e35200fcfa2269198a7f7f68f1a5e
SKILL.md         IDENTICAL 8e1dcf9f7f11675ce5d57b1d3fec66a4f929eae5
README.md        IDENTICAL 7c46413cf7781ae3cdbaa7bae7e265f7ddcbbe70
l0-questions.md  IDENTICAL f9fdff500e043c63d7bbfd0ffad90f8cfd66de4e
```

**Observed, reported exactly:** the untracked scan surfaces a *copy* of the charter under another seat's scratch — `?? .ufo/waves/round-97/seats/V36-scratch/negctl/PROVINCE.md`. It is byte-identical to the live charter (`cmp` → exit 0; sha256 `94a7a77e…` both), i.e. a verifier negative-control copy, not a mutation. The live charter is untouched.

**Result: PASS.**

---

## A2 — no writes outside `lore-shokunin` (and no writes outside declared byte-ownership inside it)

### A2.1 Whole-tree blob audit vs `f3e09f9`

Blob-level comparison of every tracked file outside `.ufo/` (worktree `git hash-object` vs `f3e09f9` tree), so in-place edits cannot hide behind unchanged path names:

```
tracked-non-ufo base files: 2818
CHANGED: ['LOG.md', 'SCORECARD.md', 'corpus/fixtures/r96-crossing-response/claim-excerpt-map.md',
          'corpus/tools/README.md', 'corpus/tools/dependency-freeze-contract.json',
          'corpus/tools/dependency_freeze.py', 'corpus/tools/map-obligations-contract.json',
          'corpus/tools/map_obligations.py']
ADDED: corpus/fixtures/r97-crossing-acknowledgment/{README.md,claim-excerpt-map.md,contradictions.json,
       entities.json,fictional-excerpts.md,inspiration-note.md,relations.json,source-excerpt.md,
       sources.json,timeline.json}, corpus/knowledge/r97-acknowledgment-scope-note.md   (11 files)
MISSING: []
```

Attribution against the declared byte-ownership:

- `corpus/tools/map_obligations.py` → **R1**; `map-obligations-contract.json` + `corpus/tools/README.md` → **R2**; `dependency_freeze.py` + `dependency-freeze-contract.json` → **R3**; `r96-crossing-response/claim-excerpt-map.md` (repair) + the 5 JSON/markdown copies and `fictional-excerpts.md` → **R4**; r97 `README.md` + `claim-excerpt-map.md` → **R5**; `corpus/knowledge/r97-acknowledgment-scope-note.md` → **R6**.
- `LOG.md` is the pre-dispatch r97 declaration: `git diff --numstat f3e09f9 -- LOG.md` → `61  0  LOG.md` (61 added, 0 deleted = append-only; zero deletion lines).
- `SCORECARD.md` is **not an r97 write**: `git diff HEAD -- SCORECARD.md | wc -c` → `0`, and `git log -1 -- SCORECARD.md` → `2393934 lore r96: close round — SCORECARD admitted section`. Its 31-line delta vs `f3e09f9` is the committed r96-closure section that sits above the declared baseline.

Exactly the declared set — nothing extra, nothing missing, and no file outside the six producers' byte scope was modified.

### A2.2 Untracked audit (lane-internal)

```
$ git status --porcelain -uall | grep '^??' | grep -v '^?? .ufo/waves/round-97/'
?? corpus/fixtures/r97-crossing-acknowledgment/README.md
… (exactly the 11 declared corpus additions, 11 lines total) …
?? corpus/knowledge/r97-acknowledgment-scope-note.md
```

All other untracked content lives under `.ufo/waves/round-97/` — seat reports and per-seat scratch, the wave's declared write area. The round-97 top level contains only `seats/` (`find .ufo/waves/round-97 -maxdepth 1 -type f | wc -l` → `0`). New corpus files are regular mode-644 files, zero symlinks (`find … -type l | wc -l` → `0`; `find … -type f ! -perm 644 | wc -l` → `0`).

### A2.3 Fleet-root scan (sibling lanes / domain trees)

```
$ cd /home/vgpnk/Projects/shokunin && find . -newermt "2026-10-17 18:41" -type f -not -path "./lore-shokunin/*" -not -path "*/.git/*" | grep -v '^./kotodama-shokunin/'
(empty)
```

Interpretation, reported as found: every in-window sibling-lane path belongs to **`kotodama-shokunin`'s own concurrent round-10 activity** (57 files: its `reports/round-10/**`, `corpus/knowledge/**`, `.scratch/**`). A lore-name/`r97` filter over the same window returns nothing (`grep -i -E "lore|r97"` → empty). `ls -d .ufo/waves/round-97` in the parent → *No such file or directory* (the r94 parent-stray-wave defect class did not recur), and the parent repo `git status --porcelain` is empty. Sibling `PROVINCE.md` mtimes are all pre-round (latest `kotodama-shokunin` 2026-10-17_12:59; `lore-shokunin` 2026-10-15_01:49). No write to any sibling lane or domain source tree is attributable to an r97 lore seat.

### A2.4 System-temp scratch — observed, reported exactly

```
$ find /tmp -maxdepth 1 -newermt "2026-10-17 18:41" | sort
/tmp
/tmp/.bun-1000-71b650bef1b3e52c.node
/tmp/.bun-1000-89812e6e6a68aaeb.so
/tmp/.bun-1000-e83060072c005618.so
/tmp/fake-contract-backup.json
/tmp/opencode
```

`/tmp/fake-contract-backup.json` (18:44:18, sha256 `c65ac3bd4fc090d8696b5739a6e5971cc06aba4700ad7458b9f9b04a8e99a4d2`) is a backup of the **pre-hardening** `dependency-freeze-contract.json` — the hash equals the r96-closure contract hash I measured before the round (`c65ac3bd…`), i.e. a seat's ephemeral backup, plausibly for the PATH-MISMATCH or scope-guard negative control. The `.bun-*`/`opencode` entries are unrelated runtime files. None is a sibling repository or domain source tree, so none breaches `PROVINCE.md`'s write boundary. Disclosed as protocol-level evidence, not smoothed over. **Self-disclosure:** this seat's only scratch is `.ufo/waves/round-97/seats/V28-scratch/` (poll script, two audit scripts, a reconstructed pre-repair r96 fixture copy, two receipt transcripts, `freeze-manifest.txt`); I created no `/tmp` files.

**Result: PASS** (no writes to sibling lanes or domain source trees attributable to r97; `/tmp` scratch observed and disclosed).

---

## A3 — external/mythology content stays editorial-only in the new bytes

**Byte-copy integrity of the preserving copy (R4's declared 5 files):**

```
IDENTICAL  entities.json      (sha256 026af0bc… == r96)
IDENTICAL  relations.json     (c279254b… == r96)
IDENTICAL  contradictions.json(37517e5f… == r96)
IDENTICAL  inspiration-note.md(58f5390e… == r96)
IDENTICAL  source-excerpt.md  (b5edc2fd… == r96)
```

`cmp` ×5 against the **post-repair** `r96-crossing-response`; since the repair touched only the map (§A5), these are also the r96 baseline bytes. `fictional-excerpts.md` is a strict byte-prefix: r96's 2588 bytes are the prefix of r97's 3410 bytes (`head -c 2588 … | cmp` → identical).

**JSON-level separation:**

```
declared source ids: ['veil-verse','paired-clock','crossing-minute','aru-aftermath-note','evin-response-note','aru-acknowledgment-note']
bound source ids  : ['aru-acknowledgment-note','aru-aftermath-note','crossing-minute','evin-response-note','paired-clock']
all bound in declared set: True
external-name scan (Spence|Kojiki|Chamberlain|Gutenberg|ETCSL|Inana|Ovid|Maya|Kiche|K'iche): no hits in any r97 JSON
```

**Counts measured from the delivered JSON:** 5 entities / 1 relation / 0 contradictions / 6 timeline events / 6 sources; census `ls -d corpus/fixtures/*/ | wc -l` = **171** (170 at r96).

**Explicit refusal lines in the new bytes (verbatim, non-exhaustive):**

- `corpus/fixtures/r97-crossing-acknowledgment/README.md:19` — "It supplies no in-world witness, cultural authority, or fictional canon, and asserts no cultural meaning. Rights and AI-training permission remain unassessed; neither is granted or inferred here."; `:21` — receipt "not whole-claim entailment, source authentication, chronology truth, rights, permission, or canon review".
- `claim-excerpt-map.md:42` — "they do not make Spence an in-world witness, assign cultural meaning, or add canon."; `:59` — receipt "not … source authenticity, truth, rights, permission, or canon".
- `corpus/knowledge/r97-acknowledgment-scope-note.md:3,8` — "not merged canon, not a resolution finding"; `:41` — "None reads the note as testimony or decides truth, breach, chronology, reconciliation, rights, permission, or canon."; `:70` — "Rights and AI-training permission remain unassessed here."
- `inspiration-note.md:13-21` (byte copy) — `## Rights question` / `## AI-training-permission question`, both open; "It is not an in-world source and supplies no fictional canon."

The Spence material remains two separately labelled editorial rows (S01/S02 at `claim-excerpt-map.md:46-47`, under the `:42` scope sentence); the new authored content (`aru-acknowledgment-note`, tick-13 event `acknowledgment-aru-records`) is in-world fiction whose own reliability note bounds it (`sources.json:36`: "It records receipt only and is not evidence of a resolution, a reconciliation, an accusation, a winner between the accounts, a continuing duty, or an external historical fact"); `contradictions.json` stays `[]`.

Light path-existence check of the note's cited records: all 12 cited paths exist (`EXISTS` ×12), and the cited sections resolve (`grep -c "Round 96" corpus/fixtures/README.md` → 2, `"Round 95"` → 2, `## Round 23` at `2026-10-12-lore-decision-table.md:226`).

**Result: PASS.**

---

## A4 — rights / canon / mechanics language scan (all r97 new bytes + all round diffs)

Scan set: the 10 r97 fixture files, `corpus/knowledge/r97-acknowledgment-scope-note.md`, and the `git diff f3e09f9` of the 5 tool files and the r96 map repair.

```
$ grep -n -i -E "mechanic|gameplay|ruleset|damage|stats|balancing|hit ?point|dice|combat|level.?up|public domain|fair use|free to (use|reuse)|may be (used|reproduced)" \
    corpus/fixtures/r97-crossing-acknowledgment/* corpus/knowledge/r97-acknowledgment-scope-note.md
(no output; rc=1)
$ git diff f3e09f9 -- corpus/tools/ corpus/fixtures/r96-crossing-response/claim-excerpt-map.md | grep -n -i -E "^[+-].*(mechanic|gameplay|ruleset|damage|stats|balancing|public domain|fair use|free to (use|reuse)|may be (used|reproduced))"
(no output; rc=1)
```

Zero mechanics words and zero rights-grant phrases anywhere in the round's new bytes or diffs. Every hit of the broader pattern `rights|licen[cs]e|copyright|permission|canon|training|attribut` is a refusal, an open question, a scope exclusion, or the JSON-Pointer sense of "canonical":

- `claim-excerpt-map.md:1,16` — "canonical" only as JSON-Pointer naming ("canonical claim-to-excerpt map", "17 canonical pointers"); `:42,:59` refusals.
- `inspiration-note.md:9-19` — attribution/rights/AI-training questions stated open ("has not been determined for all jurisdictions"; "does not imply permission for training").
- `fictional-excerpts.md:5-46` — "attributed to in-world source ID …" (fictional attribution, not rights attribution).
- `r97-acknowledgment-scope-note.md:3,8,26,41,70` — bounded-record and refusal lines.
- The only rights word in any tool diff is the refusal in the new contract scope: `dependency-freeze-contract.json` — "no chronology truth, entailment, source, rights, or canon judgment; `--freeze` is scope-guarded to `corpus/fixtures/**` and every pin records the fixture's repo-relative path, which verification enforces (SCOPE-REFUSED / PATH-MISMATCH)".

Adjacency-string checks (cross-province leakage):

```
$ grep -rn -E "/home/|\.\./|/tmp/" corpus/fixtures/r97-crossing-acknowledgment/ corpus/knowledge/r97-acknowledgment-scope-note.md
(no output; rc=1)
$ git diff f3e09f9 -- corpus/tools/ | grep -n -i -E "^[+-].*(kotodama|game-dev|art-east|kengaku|mado|tabi|sibling|/home/|\.\./)"
(no output; rc=1)
```

No absolute path, no `../` escape, no sibling-lane name, and no domain-tree path in any new byte or diff — the lane's `refuses: real-world rights claims (art-east-asian-design); game mechanics verification (game-dev-2d)` boundary is respected in the delivered bytes.

**Result: PASS.**

---

## A5 — the r96 map repair is cosmetic-only (adjacency to the frozen r96 cluster)

```
$ git diff f3e09f9 -- corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
-|---|---|---|---|---|---:|---|---|          (8-cell delimiter)
+|---|---|---|---|---:|---|---|            (7-cell delimiter)
-…The new relation encodes only the agreement for this crossing, not perpetual performance or alliance.
+…The new tick-12 event encodes only Evin's second account of the same crossing occasion; it asserts no
+ reconciliation, selects no winner between the accounts, and adds no duty beyond this crossing, not
+ perpetual performance or alliance.
```

Exactly two hunks: the delimiter row and one prose sentence. No data row, anchor, span, pointer, or mode changed.

Receipts, pre-repair vs post-repair, measured on the delivered revision (pre-repair reconstructed with `git show f3e09f9:…` into my scratch, the other nine files copied from the post-repair fixture since §A3 proves they are byte-identical):

```
pre rc=0 / post rc=0
$ diff r96-pre.support.txt r96-post.support.txt && echo SUPPORT-RECEIPTS-IDENTICAL
SUPPORT-RECEIPTS-IDENTICAL
$ diff r96-pre.map.txt r96-post.map.txt && echo MAP-RECEIPTS-IDENTICAL
MAP-RECEIPTS-IDENTICAL
```

Post-repair on the live fixture: `support_check.py` → `RECEIPT JSON-FACTS 16; EDITORIAL-ROWS 2; TOTAL-ROWS 18` / `SOURCE-SUPPORT 16/16; EDITORIAL-ANCHORS 2/2; MODES 18/18; VALIDATED-ROWS 18/18` / `RESULT PASS` (rc=0); `map_obligations.py` → `OBLIGATIONS raw=16 mapped=16` / `INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18` / `RESULT PASS` (rc=0). Both byte-identical to the pre-repair runs. The repair changes the map's prose only; the r96 receipts are unchanged, as claimed.

**Result: PASS.**

---

## A6 — reports match the bytes (ordering and stability)

Every producer artifact mtime precedes its owner's report mtime — no post-report rewrites:

| Seat | artifact mtimes | report mtime |
|---|---|---|
| R1 | `map_obligations.py` 18:45:37 | 18:52:25 |
| R2 | `map-obligations-contract.json` 18:46:12, `README.md` 18:47:13 | 18:49:31 |
| R3 | `dependency_freeze.py` 18:53:00, `dependency-freeze-contract.json` 18:55:14 | 18:56:23 |
| R4 | r96 map 18:43:42; fixture JSON 18:44:16–18:44:30 | 18:50:14 |
| R5 | r97 map 18:48:56, README 18:49:14 | 18:51:25 |
| R6 | scope note 18:52:38 | 18:53:37 |

Delivered hashes at freeze (18:56:34) — `PROVINCE.md 94a7a77e`, r96 map `e851f068`, r97 map `49d4834e`, r97 entities `026af0bc`, relations `c279254b`, contradictions `37517e5f`, timeline `73063a86`, sources `438fb513`, fictional-excerpts `8ba491cb`, inspiration-note `58f5390e`, source-excerpt `b5edc2fd`, r97 README `d9387b7d`, note `5e3b4225`, `map_obligations.py 86b52949`, `dependency_freeze.py b06275f3`, `map-obligations-contract.json 2142b991`, `dependency-freeze-contract.json 27273be2`, `README.md 6278e59b` — re-digested identically at 18:58:21, 18:58:33 and 18:58:56 (manifest digest `b88c9a17…`).

**Result: PASS.**

---

## Observations reported as found (not province breaches)

1. **Mid-flight byte churn, pre-freeze.** `dependency-freeze-contract.json` changed from `8015e1f9…` (18:53:37) to `27273be2…` (18:55:14), after R3's tool mtime; R3's report followed at 18:56:23. My freeze is post-report and stability was re-verified three times afterwards, so no measurement here rests on a mid-flight byte.
2. **`/tmp` scratch practice** (§A2.4): five in-window entries, one of them a pre-hardening contract backup; the same class as r95/r96 disclosed observations. Bounded follow-up candidate, not smoothed over.
3. **`SCORECARD.md` vs the declared baseline.** Its delta is the committed r96-closure commit `2393934`; `git diff HEAD` is empty, so it is not an r97 write. Worth keeping explicit in closure arithmetic, as in r96.
4. **`kotodama-shokunin` concurrent round 10.** 57 in-window sibling files, none lore-related; attributed away, not counted against this lane.
5. **Verifier scratch volume.** The round-97 seats tree carries many per-seat scratch directories (including V36's `negctl/PROVINCE.md` copy and V01/V03/V04/… scratch). Lane-internal and inside the declared seat-write area; visible only as untracked volume, not a breach.

---

## Bottom line

**PASS** — `PROVINCE.md` is byte-identical to `f3e09f9` (blob `7c599c39`, sha256 `94a7a77e…`, empty diff; SHONEN/SKILL/README/l0-questions likewise), the round's entire change set is lane-local and exactly the declared producer byte-ownership (6 tool files + r96 map repair modified, 11 corpus files added, `LOG.md` +61/−0 declaration, `SCORECARD.md` attributed to the committed r96 closure) with zero writes to sibling lanes or domain source trees — the only caveats being disclosed ephemeral `/tmp` scratch and lane-internal verifier scratch; mythology stays editorial-only in the new bytes (5 byte copies identical to post-repair r96, no external name in any r97 JSON, Spence rows remain 2 editorial rows, refusals present in README/map/note/inspiration-note); the rights/mechanics scan returns zero mechanics words and zero rights-grant phrases with every rights/permission/canon mention a refusal or open question; and the r96 map repair is provably cosmetic (two hunks, receipts byte-identical pre vs post).
