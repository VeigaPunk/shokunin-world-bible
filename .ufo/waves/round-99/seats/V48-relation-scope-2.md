# V48 — relation-scope-2 (round 99)

- **Seat:** V48 relation-scope-2 (verifier). Lane repo: `/home/vgpnk/Projects/shokunin/lore-shokunin` (session cwd is the parent repo; every command below ran from the lane repo root with `python3`).
- **Baseline:** r98 closure `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`). Round-99 declaration in `LOG.md` (C1 full-file freeze pins; C2 lapse fixture + blind-spot table). Re-dispatch; the declaration was not rewritten.
- **Seat claim under test:** `corpus/fixtures/r99-window-lapse/relations.json` is byte-identical r98→r99; the map relation row is unchanged; no new relation semantics.
- **Writes:** this report only (absolute path), plus scratch `.ufo/waves/round-99/seats/V48-scratch/` (`poll.sh`, `poll.log`, `jrows.py`, `relcensus.py`, `baseline-relations.json`). No commits, no pushes, no network, no nested agents, nothing outside the lane.
- **Poll-wait record:** at 22:01:16 the r99 directory existed as an r98 byte copy for the map and README (both sha256 equal to r98: map `c1099d0e…`, README `32efc78f…`) while `fictional-excerpts.md` / `sources.json` / `timeline.json` were already being rewritten (mtime 22:01:13). No seat reports yet. Poll (20 s cadence, `.ufo/waves/round-99/seats/V48-scratch/poll.log`) gated on the ten fixture files **and** S3/S4 reports. S3's report was present from try 1 (22:02:03); S4's landed at try 7 → `ALL-PRESENT` at 22:04:03. No ABSENT, no stall-escape. Core verification ran only after that, on the post-S4 revision (map mtime 22:02:39, README mtime 22:03:19). Both producer reports were read in full. S5's report and `corpus/knowledge/r99-*` were still absent at 22:17:11 and again at 22:50:58; not used as evidence. Relation and map hashes were unchanged at that later check (`c279254b…`, `d2fe20e5…`).

## Verdict on the seat claim

| Sub-claim | Verdict | One-line evidence |
|---|---|---|
| `relations.json` byte-identical r98→r99 | **CONFIRMED** | sha256 `c279254b…` for r99 == r98 worktree == baseline blob `4265df5:corpus/fixtures/r98-clerk-filing/relations.json`; git blob `2804ae91`; `cmp` IDENTICAL both ways; 139 bytes; LF-only |
| Map relation row unchanged | **CONFIRMED (bounded)** | J11 (`relations.json#/0`) parsed-equal to r98 in all 8 cells except the path-qualified namespace cell (`r98-clerk-filing:` → `r99-window-lapse:`), the same transformation r97→r98 applied; anchor text byte-identical; exactly 1 relation row; map line 32 in both |
| No new relation semantics | **CONFIRMED (bounded)** | relation-type census 10 types unchanged, only `agreed_co_stewardship_for_this_crossing` 5→6 from the carried row; all 172 baseline `relations.json` files byte-unchanged; the only added map row is J21 `timeline.json#/7` (a tick-15 event, not a relation); `check_bible` CLEAN on `relations` |

## 1. `relations.json` byte-identity (r98 → r99, and against the baseline blob)

```
$ sha256sum corpus/fixtures/r98-clerk-filing/relations.json corpus/fixtures/r99-window-lapse/relations.json
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  corpus/fixtures/r98-clerk-filing/relations.json
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  corpus/fixtures/r99-window-lapse/relations.json
$ cmp corpus/fixtures/r98-clerk-filing/relations.json corpus/fixtures/r99-window-lapse/relations.json && echo CMP-R98-R99-IDENTICAL
CMP-R98-R99-IDENTICAL
$ git show 4265df5:corpus/fixtures/r98-clerk-filing/relations.json | sha256sum
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  -
$ git rev-parse 4265df5:corpus/fixtures/r98-clerk-filing/relations.json
2804ae91240dbf34753bf955d4fab9ffeab0a8df
$ git hash-object corpus/fixtures/r99-window-lapse/relations.json
2804ae91240dbf34753bf955d4fab9ffeab0a8df
$ cmp <(git show 4265df5:corpus/fixtures/r98-clerk-filing/relations.json) corpus/fixtures/r99-window-lapse/relations.json && echo CMP-BASELINE-IDENTICAL
CMP-BASELINE-IDENTICAL
$ wc -c corpus/fixtures/r99-window-lapse/relations.json
139 corpus/fixtures/r99-window-lapse/relations.json
$ cat -A corpus/fixtures/r99-window-lapse/relations.json
[$
  {$
    "from": "aru",$
    "to": "evin",$
    "type": "agreed_co_stewardship_for_this_crossing",$
    "source_id": "crossing-minute"$
  }$
]$
```

Parsed value is the single inherited row (`python3`: `parsed_equal True`, keys `from` / `source_id` / `to` / `type`, length 1). Same blob across the arc:

```
$ git hash-object corpus/fixtures/r94-paired-crossing/relations.json \
    corpus/fixtures/r95-crossing-aftermath/relations.json \
    corpus/fixtures/r96-crossing-response/relations.json \
    corpus/fixtures/r97-crossing-acknowledgment/relations.json \
    corpus/fixtures/r98-clerk-filing/relations.json \
    corpus/fixtures/r99-window-lapse/relations.json
2804ae91240dbf34753bf955d4fab9ffeab0a8df
2804ae91240dbf34753bf955d4fab9ffeab0a8df
2804ae91240dbf34753bf955d4fab9ffeab0a8df
2804ae91240dbf34753bf955d4fab9ffeab0a8df
2804ae91240dbf34753bf955d4fab9ffeab0a8df
2804ae91240dbf34753bf955d4fab9ffeab0a8df
```

The r98 fixture tree itself is untouched by the round: `git diff --stat 4265df5 -- corpus/fixtures/r98-clerk-filing corpus/fixtures/r97-crossing-acknowledgment corpus/fixtures/r96-crossing-response corpus/fixtures/r95-crossing-aftermath corpus/fixtures/r94-paired-crossing` → empty. `relations.json` mtime stayed `2026-10-17 21:36:10 -0300` (the `git archive` member timestamp S3's report describes) through the final check; neither producer rewrote it.

S3's report independently declares `relations.json: identical=True base=139 now=139` against `4265df5:corpus/fixtures/r98-clerk-filing/relations.json`. That matches this seat's `cmp`.

## 2. Map relation row

Cell-by-cell comparison of every `J##` row (script `.ufo/waves/round-99/seats/V48-scratch/jrows.py`; rows split on `|`, 8 cells = ID + 7 columns):

```
$ python3 .ufo/waves/round-99/seats/V48-scratch/jrows.py corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md corpus/fixtures/r99-window-lapse/claim-excerpt-map.md
A rows: 20  B rows: 21
B-only: ['J21']
A-only: []
J01: cells=8/8 diffs=[(3, '`r98-clerk-filing:paired-clock`', '`r99-window-lapse:paired-clock`')]
J02: cells=8/8 diffs=[(3, '`r98-clerk-filing:paired-clock`', '`r99-window-lapse:paired-clock`')]
J03: cells=8/8 diffs=[(3, '`r98-clerk-filing:paired-clock`', '`r99-window-lapse:paired-clock`')]
J04: cells=8/8 diffs=[(3, '`r98-clerk-filing:paired-clock`', '`r99-window-lapse:paired-clock`')]
J05: cells=8/8 diffs=[(3, '`r98-clerk-filing:crossing-minute`', '`r99-window-lapse:crossing-minute`')]
J06: cells=8/8 diffs=[(3, '`r98-clerk-filing:paired-clock`', '`r99-window-lapse:paired-clock`')]
J07: cells=8/8 diffs=[(3, '`r98-clerk-filing:paired-clock`', '`r99-window-lapse:paired-clock`')]
J08: cells=8/8 diffs=[(3, '`r98-clerk-filing:paired-clock`', '`r99-window-lapse:paired-clock`')]
J09: cells=8/8 diffs=[(3, '`r98-clerk-filing:paired-clock`', '`r99-window-lapse:paired-clock`')]
J10: cells=8/8 diffs=[(3, '`r98-clerk-filing:crossing-minute`', '`r99-window-lapse:crossing-minute`')]
J11: cells=8/8 diffs=[(3, '`r98-clerk-filing:crossing-minute`', '`r99-window-lapse:crossing-minute`')]
J12: cells=8/8 diffs=[(3, '`r98-clerk-filing:paired-clock`', '`r99-window-lapse:paired-clock`')]
J13: cells=8/8 diffs=[(3, '`r98-clerk-filing:paired-clock`', '`r99-window-lapse:paired-clock`')]
J14: cells=8/8 diffs=[(3, '`r98-clerk-filing:crossing-minute`', '`r99-window-lapse:crossing-minute`')]
J15: cells=8/8 diffs=[(3, '`r98-clerk-filing:aru-aftermath-note`', '`r99-window-lapse:aru-aftermath-note`')]
J16: cells=8/8 diffs=[(3, '`r98-clerk-filing:evin-response-note`', '`r99-window-lapse:evin-response-note`')]
J17: cells=8/8 diffs=[(3, '`r98-clerk-filing:aru-acknowledgment-note`', '`r99-window-lapse:aru-acknowledgment-note`')]
J18: cells=8/8 diffs=[(3, '`r98-clerk-filing:clerk-filing-note`', '`r99-window-lapse:clerk-filing-note`')]
J19: cells=8/8 diffs=[(3, '`r98-clerk-filing:clerk-filing-note`', '`r99-window-lapse:clerk-filing-note`')]
J20: cells=8/8 diffs=[(3, '`r98-clerk-filing:clerk-filing-note`', '`r99-window-lapse:clerk-filing-note`')]
namespace-only inherited: 20 ['J01', 'J02', 'J03', 'J04', 'J05', 'J06', 'J07', 'J08', 'J09', 'J10', 'J11', 'J12', 'J13', 'J14', 'J15', 'J16', 'J17', 'J18', 'J19', 'J20']
other diffs: []
J11 line A 32 B 32
J11 cells equal except index 3: True
J11 anchor equal: True
J11 A anchor: `There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.`
J11 B anchor: `There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.`
```

Verbatim re-run saved at `.ufo/waves/round-99/seats/V48-scratch/jrows.out`. Same J11 cell-3-only diff as the 22:07:42 pass.

J11 specifically (cell 3 only):

```
J11: diffs=[(3, '`r98-clerk-filing:crossing-minute`', '`r99-window-lapse:crossing-minute`')]
```

Raw J11 rows (`cat -A`; trailing `$` = LF). r98 map `:32`, r99 map `:32`:

```
| J11 | `relations.json#/0` (`from`, `to`, `type`, `source_id`) | `crossing-minute` | `r98-clerk-filing:crossing-minute` | `fictional-excerpts.md` | 19 | `verbatim` | `There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.` |$
| J11 | `relations.json#/0` (`from`, `to`, `type`, `source_id`) | `crossing-minute` | `r99-window-lapse:crossing-minute` | `fictional-excerpts.md` | 19 | `verbatim` | `There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.` |$
```

Pointer, fields list, in-world source ID, excerpt path, span (19), mode, and anchor are byte-identical; only the namespace qualification differs. That is the map's own declared rule (r99 map line 18: "only the path-qualification column names this fixture's cluster path") and the same single-cell transformation r95→r96, r96→r97, and r97→r98 applied. Strict reading: the J11 line is not byte-identical as a whole. The unchanged claim holds for every cell except that mandated column.

The anchor is a fixed-string hit at `fictional-excerpts.md:19`, and the r99 excerpt is a byte-prefix extension of r98's (4187 bytes preserved, r99 is 5114; `line19_equal True`):

```
$ grep -nF 'There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.' corpus/fixtures/r99-window-lapse/fictional-excerpts.md
19:> There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.
```

Exactly one relation row in the map:

```
$ grep -c 'relations.json#' corpus/fixtures/r99-window-lapse/claim-excerpt-map.md
1
$ grep -c 'relation' corpus/fixtures/r99-window-lapse/claim-excerpt-map.md
2
```

The two hits are the scope line (line 3: "one relation, and eight timeline events") and the J11 row. The only added row is J21, a timeline event, not a relation:

```
| J21 | `timeline.json#/7` (`tick`, `entity_id`, `place_id`, `depends_on`, `description`, `source_id`) | `clerk-lapse-note` | `r99-window-lapse:clerk-lapse-note` | `fictional-excerpts.md` | 66-76 | `verbatim` | `Tick 15: The crossing-window named in the original minute has closed.` |
```

S4 declares map sha256 `d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d` and README `b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049`. Both equal this seat's measured values (22:04:09 and again 22:17:11).

## 3. No new relation semantics

- **Type census** (script `.ufo/waves/round-99/seats/V48-scratch/relcensus.py`; baseline `git show 4265df5:<path>` vs worktree `corpus/fixtures/*/relations.json`):

```
$ python3 .ufo/waves/round-99/seats/V48-scratch/relcensus.py
BASELINE files=172 rows=159 types=10
WORKTREE files=173 rows=160 types=10
  6 agreed_co_stewardship_for_this_crossing  CHANGED 5->6
  9 allied_with
  1 annotates
  135 carries
  3 consults
  1 filed_at
  1 keeps_watch_with
  1 records_at
  2 records_departure
  1 wields
new types: none
lost types: none
baseline relations.json checked=172 moved=0
all baseline relations.json unchanged in worktree
```

  `git diff --stat 4265df5 -- 'corpus/fixtures/**/relations.json'` was empty. Fixture-directory census (corrected command): `git ls-tree -d --name-only 4265df5:corpus/fixtures | wc -l` → 172; worktree `find corpus/fixtures -mindepth 1 -maxdepth 1 -type d | wc -l` → 173; the only new directory is `r99-window-lapse`. The +1 row is solely the new fixture carrying the byte-identical inherited row.

- **Only relation-type occurrence in the r99 fixture:** `grep -n -E 'relations\.json|agreed_co_stewardship|relation'` hits `relations.json:5` (the inherited type), the map's scope line and J11 row, and `README.md:3` ("the one inherited relation" copied by JSON value; counts "6 entities / 1 relation / 8 events / 8 sources"). Nothing in entities/sources/timeline/excerpts asserts a second or differently-typed relation. `sources.json` `crossing-minute.reliability_note` is unchanged in kind: "not evidence of continuing performance, a standing alliance, or an external historical fact." The appended lapse section (`fictional-excerpts.md:76`) states "the crossing-scoped agreement above is unchanged, and the matter stays open." README line 11 retains the crossing-only bound ("the agreement covered this crossing only … It is not evidence of an alliance, a continuing practice, perpetual performance, a standing duty…").

- **Gates on the delivered revision (this seat's runs, 22:09:23):**

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r99-window-lapse
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT:0

$ python3 corpus/tools/support_check.py corpus/fixtures/r99-window-lapse
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23; DISTINCT-ANCHORS 19/19
PASS J11: source-support; mode=verbatim; anchor=found; 19:> There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.
PASS J21: source-support; mode=verbatim; anchor=found; 70:> Tick 15: The crossing-window named in the original minute has closed.
RESULT PASS
EXIT:0

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r99-window-lapse
OBLIGATIONS raw=21 mapped=21
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23
RESULT PASS
EXIT:0
```

- **Tooling side (adjacent, bounded):** `git diff --stat 4265df5 -- corpus/tools/map_obligations.py corpus/tools/support_check.py corpus/fixtures/check_bible.py` is empty. `dependency_freeze.py` changed (+60/−5). The only relation-token line in that diff is the docstring wording "JSON content digests" → "content digests"; the triple description `(from, to, type)` is unchanged, and no `relations[` / triple-extraction line is in a changed hunk. The contract still scopes "relation endpoint triples (from, to, type)". Parsed pins (this seat, not a re-run of `--freeze`): r94–r98 each still record `[['aru', 'evin', 'agreed_co_stewardship_for_this_crossing']]` and `files.relations.json` = `c279254b…`; r88's pin still has `triples=[]`; `r99_pinned False` (pin names are the six chain fixtures only). C1's full-file digest extension does not add a relation type, endpoint rule, or reciprocity rule. I did not re-run `--freeze` or the freeze self-test.

## 4. Bounded observations (reported, not failures)

1. **Placeholder-poll hazard (r99 map/README).** S3 byte-copied r98's `README.md` and `claim-excerpt-map.md` and left them for S4 (S3 report: both `identical=True` to `4265df5` r98 at S3's write time; S3's "Not done" section says the map still says r98). At 22:01:16 both hashes still equaled r98. By ALL-PRESENT (22:04:03) they had been rewritten (map `d2fe20e5…` ≠ r98 `c1099d0e…`). An existence-only poll on this round is satisfied by the placeholder. This seat held verification until the S3 and S4 reports existed and then checked content. S3's statement that the map still says r98 is stale for the delivered tree; it does not contradict the relation-byte claim, which remained true before and after S4.
2. **Strict-reading caveat for the map row.** J11 is not byte-identical as a whole line. The only differing cell is the path-qualification column, which the map's declared rule requires and which every prior continuation of this arc applied. Anchor, pointer, span 19, mode, and source ID are byte-identical.
3. **S5 absent at final check.** `corpus/knowledge/r99-gate-blind-spot-table.md`, `corpus/knowledge/r99-lapse-scope-note.md`, and `.ufo/waves/round-99/seats/S5*.md` were absent at 22:17:11 and again at 22:50:58. No scope-note corroboration is claimed.
4. **Parent-repo scratch (not this seat).** `git -C /home/vgpnk/Projects/shokunin status --porcelain` showed untracked `.ufo/waves/round-99/`. That tree contains `seats/V69-scratch/` and `seats/V73-scratch/` only (listing at 22:23). This seat did not write there. Left untouched for L1 attribution.
5. **Declared-hash agreement.** S4 map `d2fe20e5…` / README `b9320941…` equal this seat's values. S3's relations.json identity claim equals this seat's `cmp`.

## 5. Hash stability and hygiene (final pass 22:17:11)

Relation-relevant hashes, measured at 22:04:09 (immediately after ALL-PRESENT) and again at 22:17:11 (after the three gate runs). `diff` of those values is empty for these paths. `relations.json` was already this hash at the 22:01:16 placeholder snapshot and its mtime never moved.

```
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  corpus/fixtures/r99-window-lapse/relations.json
d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d  corpus/fixtures/r99-window-lapse/claim-excerpt-map.md
b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049  corpus/fixtures/r99-window-lapse/README.md
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  corpus/fixtures/r98-clerk-filing/relations.json
c1099d0ee9eece241ea1f796320a84453dfc6b6aec33b7b9dd7e39bbef4a94ba  corpus/fixtures/r98-clerk-filing/claim-excerpt-map.md
```

Lane `git status --porcelain` at the final pass: `M corpus/tools/dependency-freeze-contract.json`, `M corpus/tools/dependency_freeze.py`, `?? .ufo/waves/round-99/`, `?? corpus/fixtures/r99-window-lapse/` — declared producer paths (S1 + the wave tree + S3/S4 fixture) plus this seat's report/scratch inside the wave tree. No stray write from this seat, no commit.

## Non-claims

I verified relation bytes, the map relation row, the relation-type surface, and the three gates above on the delivered r99 fixture. I did not judge C1's freeze-tool behavior beyond the relation-token diff and the parsed pin triples, C2 component 2 (S5's table was absent), S4's narrative quality beyond relation scope, entailment, canon, or chronology. `support_check` and `map_obligations` are lexical preflight, not whole-claim entailment.

## Bottom line

**PASS** — `corpus/fixtures/r99-window-lapse/relations.json` is byte-identical r98→r99 (sha256 `c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9`, git blob `2804ae91240dbf34753bf955d4fab9ffeab0a8df`, `cmp` IDENTICAL to the r98 worktree and to baseline `4265df5`, 139 B, same blob as r94–r98); the map's J11 relation row is unchanged in all cells except the declared path-qualified namespace column (`r98-clerk-filing:` → `r99-window-lapse:`, map line 32 both sides, anchor byte-identical at excerpt line 19); and no new relation semantics exist (single relation row; J21 is the only added row and is `timeline.json#/7`; 10-type census unchanged with only the carried `agreed_co_stewardship_for_this_crossing` 5→6; all 172 baseline relations.json files byte-unchanged; check_bible CLEAN, support_check J11 PASS, map_obligations 21/21 PASS) — with the bounded process observation that the r99 map/README were r98 byte copies until S4's rewrites, so existence-only polls can be satisfied by a placeholder (this verification ran only on the post-S4 revision, hashes stable 22:04:09 → 22:17:11).
