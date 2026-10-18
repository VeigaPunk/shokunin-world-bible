# V46 — relation-scope-2 (round 98)

- **Seat:** V46 relation-scope-2 (verifier). Lane repo: `/home/vgpnk/Projects/shokunin/lore-shokunin` (session cwd is the parent repo; every command below ran from the lane repo root with `python3`).
- **Baseline:** r97 closure `9a3d648`. Round-98 wave spec in `LOG.md` tail (C1/C2/C3).
- **Seat claim under test:** `corpus/fixtures/r98-clerk-filing/relations.json` is byte-identical r97→r98; the map relation row is unchanged; no new relation semantics.
- **Writes:** this report only (absolute path), plus scratch `.ufo/waves/round-98/seats/V46-scratch/` (`poll.sh`, `poll.log`, `jrows.py`, `relcensus.py`, `stable1.txt`, `stable2.txt`, `r95-map-baseline.md`, `baseline/`). No commits, no pushes, no network, no nested agents, nothing outside the lane.
- **Poll-wait record:** fixture directory absent at 20:27; appeared 20:28:24 as a 10-file r97 byte copy (placeholder phase). My poll (20 s cadence, 40 tries, `.ufo/waves/round-98/seats/V46-scratch/poll.log`) gated on fixture files **and** the S3/S4 reports; S3's report landed 20:31:08, S4's 20:32:08 → `ALL-PRESENT` at try 12. No ABSENT, no stall-escape needed. I did **not** verify the placeholder state: core verification ran on the post-S4 revision (S4's map 20:30:21, README 20:30:41), and hashes were confirmed stable 20:31:59 → 20:32:18 (§5). Both producer reports were read in full.

## Verdict on the seat claim

| Sub-claim | Verdict | One-line evidence |
|---|---|---|
| `relations.json` byte-identical r97→r98 | **CONFIRMED** | sha256 `c279254b…` for r98 == r97 worktree == baseline `9a3d648`; `cmp` IDENTICAL; 139 bytes; the file is also one of the four preserved files whose bytes equal the baseline r97 blob |
| Map relation row unchanged | **CONFIRMED** | J11 (`relations.json#/0`) parsed-equal to r97 in all 8 cells except the path-qualified namespace cell (`r97-crossing-acknowledgment:` → `r98-clerk-filing:`), the same transformation r96→r97 and r95→r96 applied; anchor text byte-identical; exactly 1 relation row in the map |
| No new relation semantics | **CONFIRMED (bounded)** | relation-type census 10 types unchanged, only `agreed_co_stewardship_for_this_crossing` 4→5 from the carried row; all 171 pre-existing `relations.json` files byte-unchanged; the only relation-type string in the r98 fixture is `relations.json:5`; the three added rows are the declared first_appearance/claim/event, none a relation; `check_bible` CLEAN on `relations` |

## 1. `relations.json` byte-identity (r97 → r98, and against the baseline blob)

```
$ sha256sum corpus/fixtures/r98-clerk-filing/relations.json corpus/fixtures/r97-crossing-acknowledgment/relations.json
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  corpus/fixtures/r98-clerk-filing/relations.json
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  corpus/fixtures/r97-crossing-acknowledgment/relations.json
$ cmp corpus/fixtures/r97-crossing-acknowledgment/relations.json corpus/fixtures/r98-clerk-filing/relations.json && echo CMP-IDENTICAL
CMP-IDENTICAL r97->r98
$ git show 9a3d648:corpus/fixtures/r97-crossing-acknowledgment/relations.json | sha256sum
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  -
$ wc -c corpus/fixtures/r98-clerk-filing/relations.json
139 corpus/fixtures/r98-clerk-filing/relations.json
$ cat -A corpus/fixtures/r98-clerk-filing/relations.json
[$
  {$
    "from": "aru",$
    "to": "evin",$
    "type": "agreed_co_stewardship_for_this_crossing",$
    "source_id": "crossing-minute"$
  }$
]$
```

The file is LF-only (no `^M`), and its parsed value is the single inherited row `aru → evin / agreed_co_stewardship_for_this_crossing / crossing-minute`. Cross-check that the four S3-preserved files equal the **baseline r97 blobs** (not merely the r97 worktree):

```
$ for f in relations.json contradictions.json inspiration-note.md source-excerpt.md; do a=$(git show 9a3d648:corpus/fixtures/r97-crossing-acknowledgment/$f | sha256sum | cut -d' ' -f1); b=$(sha256sum corpus/fixtures/r98-clerk-filing/$f | cut -d' ' -f1); [ "$a" = "$b" ] && echo "$f: r98 == baseline r97 ($a)"; done
relations.json: r98 == baseline r97 (c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9)
contradictions.json: r98 == baseline r97 (37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570)
inspiration-note.md: r98 == baseline r97 (58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37)
source-excerpt.md: r98 == baseline r97 (b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd)
```

The r97 fixture tree itself is untouched by the round: `git diff --stat 9a3d648 -- corpus/fixtures/r97-crossing-acknowledgment corpus/fixtures/r96-crossing-response corpus/fixtures/r94-paired-crossing` → empty.

## 2. Map relation row

Cell-by-cell comparison of every `J##` row of the r97 and r98 maps (script `.ufo/waves/round-98/seats/V46-scratch/jrows.py`; rows split on `|`, 8 cells = ID + 7 columns):

```
$ python3 .ufo/waves/round-98/seats/V46-scratch/jrows.py corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md
A rows: 19  B rows: 22
B-only: ['J18', 'J19', 'J20']  A-only: []
J01: cells=8/8 diffs=[(3, '`r97-crossing-acknowledgment:paired-clock`', '`r98-clerk-filing:paired-clock`')]
… (J02–J17 same single-cell diff at cell index 3) …
J11: cells=8/8 diffs=[(3, '`r97-crossing-acknowledgment:crossing-minute`', '`r98-clerk-filing:crossing-minute`')]
```

Every one of the 17 inherited rows (J01–J17) is parsed-equal to r97 in all 8 cells except the path-qualified namespace cell — the exact transformation r95→r96 and r96→r97 applied. Raw J11 rows (r97 map `:32`, r98 map `:32`), r98 shown with `cat -A` (trailing `$` = LF):

```
| J11 | `relations.json#/0` (`from`, `to`, `type`, `source_id`) | `crossing-minute` | `r97-crossing-acknowledgment:crossing-minute` | `fictional-excerpts.md` | 19 | `verbatim` | `There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.` |
| J11 | `relations.json#/0` (`from`, `to`, `type`, `source_id`) | `crossing-minute` | `r98-clerk-filing:crossing-minute` | `fictional-excerpts.md` | 19 | `verbatim` | `There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.` |$
```

Pointer, fields list, in-world source ID, excerpt path, span (19), mode, and anchor are byte-identical; only the namespace qualification differs. The anchor is a fixed-string hit at `fictional-excerpts.md:19` (`grep -c -F` → 1), and `support_check` confirms it (`PASS J11 … anchor=found; 19:> There, they agreed, for this crossing only, …`). Exactly one relation row exists in the map:

```
$ grep -c "relations.json#" corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md
1
$ sed -n '3p' corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md
Scope: all 20 source-attributed JSON obligations in this continuation (six first-appearance pointers, six entity claims, one relation, and seven timeline events), plus two separately labeled editorial comparisons. …
```

The three added rows are the declared new obligations, none a relation: J18 `entities.json#/5/first_appearance` (clerk-maren, span 60), J19 `entities.json#/5/claims/0` (span 59-60), J20 `timeline.json#/6` (tick-14 `clerk-filing-open`, span 55-64). The r98 map's inventory line matches: `**Expected inventory:** 20 JSON facts; 2 editorial rows; 22 total mapped rows; 18 distinct excerpt anchors.`

## 3. No new relation semantics

- **Type census (baseline `9a3d648` vs worktree, `corpus/fixtures/**`):**

```
BASELINE: files=171 rows=158 types=10     WORKTREE: files=172 rows=159 types=10
  135 carries / 9 allied_with / 4→5 agreed_co_stewardship_for_this_crossing / 3 consults /
  2 records_departure / 1 annotates / 1 filed_at / 1 keeps_watch_with / 1 records_at / 1 wields
```

  Same 10-type set; the only count change is `agreed_co_stewardship_for_this_crossing` 4→5, produced solely by the new fixture carrying the byte-identical inherited row. A per-file check shows no pre-existing file moved:

```
$ for p in $(git ls-tree -r --name-only 9a3d648 corpus/fixtures | grep 'relations\.json$'); do … done
all 171 baseline relations.json unchanged in worktree
```

- **Only relation-type occurrence in the r98 fixture:**

```
$ grep -rn "agreed_co_stewardship\|relations\.json\|relations" corpus/fixtures/r98-clerk-filing/ | head
corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md:32:| J11 | `relations.json#/0` … |
corpus/fixtures/r98-clerk-filing/relations.json:5:    "type": "agreed_co_stewardship_for_this_crossing",
```

  Nothing in entities/sources/timeline/README/excerpts asserts a second or differently-typed relation. The map mentions "relation" exactly twice (scope line 3, J11 row). The r98 excerpts are a pure append to r97's (`diff` → `53a54,64`, additions only), so the line-19 relation anchor wording is byte-inherited.
- **Gates on the delivered revision (my runs):**

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r98-clerk-filing
OBLIGATIONS raw=20 mapped=20
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22
RESULT PASS   (exit 0)

$ python3 corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 18/18
… PASS J11: source-support; mode=verbatim; anchor=found; 19:> There, they agreed, for this crossing only, …
SOURCE-SUPPORT 20/20; EDITORIAL-ROWS 2/2; MODES 22/22; VALIDATED-ROWS 22/22
RESULT PASS   (exit 0)

$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r98-clerk-filing
CLEAN: schema, citations, relations, timeline; 0 violations   (exit 0)
```

- **Adjacent (S3's r95 map repair, bounded):** the whole-file diff against the baseline is exactly one prose line in `## Timeline normalization and scope` (`1 insertion, 1 deletion`), and all 17 J-rows of the r95 map are parsed-equal baseline vs worktree (`jrows.py`: `A rows: 17  B rows: 17  B-only: []  A-only: []`). So the repair touched no data row, including r95's own J11 relation row. (S3/S4 report the r95 receipts byte-identical before/after; I did not re-run those myself — outside this seat.)

## 4. Bounded observations (reported, not failures)

1. **Placeholder-poll hazard (r98 map/README).** Because S3 byte-copied r97's `README.md` and `claim-excerpt-map.md` as placeholders, both paths existed with r97's bytes from 20:28:24 until S4's rewrites (map 20:30:21, README 20:30:41). My own poll's file leg was satisfied at try 1 (20:28:28) — but the report leg was not, so I held verification until the producer reports landed and re-checked content: map sha256 `c1099d0e…` ≠ r97's `49d4834e…`, README `32efc78f…` ≠ r97's `d9387b7d…`, map names `r98-clerk-filing` and 20 rows. Any existence-only poll on this round can be satisfied by the placeholder; recorded for the closure pass (S3 D1 and S4 A raise the same hazard).
2. **No standalone relation-bound sentence in the r98 map prose** (only the scope line and the J11 row mention "relation"), the same bounded observation V51 made for r97. The bound is not lost: it survives verbatim in the J11 anchor ("for this crossing only"), in `README.md:11` ("The crossing-only bound is likewise retained: the agreement covered this crossing only, and the record asserts no other duty, no breach, no continuing obligation, and no obligation beyond this crossing. It is not evidence of an alliance, …"), and in `sources.json` `crossing-minute.reliability_note` ("not evidence of continuing performance, a standing alliance, …"). No data row, pointer, anchor, span, or mode changed.
3. **S5's scope note landed after my first pass and independently corroborates this seat's claim.** At 20:32:26 `corpus/knowledge/r98-clerk-scope-note.md` was absent; it landed by 20:33 (sha256 `1162262c742441115681d30be588039be4f1a026b755eeb7d15c9ba41952a4b8`, 72 lines) and states the bound directly: line 27 `| Scope bound (inherited, unchanged) | `relations.json#/0`, byte-identical to r97 `relations.json#/0` | `agreed_co_stewardship_for_this_crossing`, source `crossing-minute`; excerpt `fictional-excerpts.md:19`: "for this crossing only" |`, and line 30 records the four preserved files byte-identical to r97 (verified by that seat with `cmp`). This is S5's independent check of the same byte-identity, not my evidence, but it agrees with mine. No S5 report was in `seats/` at my last listing.
4. **Parent-repo stray (not this lane's seat writes).** `git status --porcelain` in `/home/vgpnk/Projects/shokunin` shows untracked `baseline-analyze.txt` (105 B, mtime 20:30) containing `python3: can't open file '/home/vgpnk/Projects/shokunin/analyze.py': [Errno 2] No such file or directory` — the r94-F01 stray-write class, in the parent repo, not written by this seat (also reported by S3 D5); left untouched for L1 attribution. The lane tree itself shows zero strays (§5).
5. **Declared-hash agreement.** S4 declares map `c1099d0e…` / README `32efc78f…`; S3 declares entities `db2d8e5d…` / sources `32ee15b1…` / timeline `eb24e084…` / excerpts `29e384bf…`. All equal my observed values.

## 5. Hash stability and hygiene (final pass 20:33:44)

Full sha256 listing of the r98 fixture captured three times (`stable1.txt` 20:31:59, `stable2.txt` 20:32:18, `stable3.txt` 20:33:44) — `diff` empty across all three, `HASH-STABLE`:

```
c1099d0ee9eece241ea1f796320a84453dfc6b6aec33b7b9dd7e39bbef4a94ba  corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  corpus/fixtures/r98-clerk-filing/contradictions.json
db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984  corpus/fixtures/r98-clerk-filing/entities.json
29e384bf2eb2ab80858ace9423f29088a552553f87da7f6a9b694cbb050666de  corpus/fixtures/r98-clerk-filing/fictional-excerpts.md
58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37  corpus/fixtures/r98-clerk-filing/inspiration-note.md
32efc78f70e6de4f9670134080711923199e8693015d3ebea75a4a1ca6362926  corpus/fixtures/r98-clerk-filing/README.md
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  corpus/fixtures/r98-clerk-filing/relations.json
b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd  corpus/fixtures/r98-clerk-filing/source-excerpt.md
32ee15b1f3d72d94f4228cbc9cefa69b7185d18b47bbe219833d7aaf30eed0f3  corpus/fixtures/r98-clerk-filing/sources.json
eb24e0848e597efa29ed858cb8557d8f3126a47e1231f9469d719257e191e7af  corpus/fixtures/r98-clerk-filing/timeline.json
80440d61122488a267a4f0a58a55cb54d89c037d93160f1123e5fb3b2f396f61  corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md
49d4834e124fa6cfaa1a73cd5d1a7bc2cb59711c6233b418fe7485a17eedc94f  corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md
```

Lane `git status --porcelain` at the final pass: `M LOG.md`, `M corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md`, `M corpus/knowledge/r95-aftermath-scope-note.md`, `M corpus/knowledge/r96-response-scope-note.md`, `M corpus/tools/dependency-freeze-contract.json`, `M corpus/tools/dependency_freeze.py`, `?? .ufo/waves/round-98/`, `?? corpus/fixtures/r98-clerk-filing/` — all declared producer paths (S1/S3/S5 + the wave tree); no stray write from this seat, no commit.

## Non-claims

I verified relation bytes, the map relation row, the relation-type surface, the three gates above on the r98 fixture, and the r95 map's J-row stability. I did not judge C1's freeze-tooling behavior, C2's pin chain or the r97-edge discharge, S4's narrative quality beyond relation scope, the r95 repair's before/after receipts (read only), or entailment/canon/chronology; S5's scope note landed after my first pass and I read its relation lines only (its own byte-identity check is quoted as corroboration, not as my evidence).

## Bottom line

**PASS** — `corpus/fixtures/r98-clerk-filing/relations.json` is byte-identical r97→r98 (sha256 `c279254b…`, `cmp` IDENTICAL, 139 B, equal to the baseline `9a3d648` r97 blob, and one of four preserved files whose bytes equal their baseline blobs); the map's J11 relation row is unchanged in all cells except the declared path-qualified namespace column (`r97-crossing-acknowledgment:` → `r98-clerk-filing:`, the same transformation as r95→r96 and r96→r97); and no new relation semantics exist (single relation row; the 3 added rows are the declared first_appearance/claim/event; 10-type census unchanged with only the carried `agreed_co_stewardship_for_this_crossing` 4→5; all 171 pre-existing relations.json files byte-unchanged; map_obligations 20/20 PASS, support_check 20/20 PASS with the J11 anchor found at line 19, check_bible CLEAN) — with one bounded process observation recorded: the r98 map/README placeholders were r97 byte copies until S4's rewrites, so existence-only polls on this round can be satisfied by a placeholder (my verification ran only on the final revision, hash-stable across 20:31:59 → 20:32:18 → 20:33:44).
