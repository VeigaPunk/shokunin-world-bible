# V09 c3-checker — round 98 seat report

- Seat: V09 (verifier, c3-checker). Lane repo: `/home/vgpnk/Projects/shokunin/lore-shokunin`; baseline `9a3d648` (pre-round bytes via `git show 9a3d648:<path>`). All commands run from the lane repo root with `python3`.
- Exclusive write path: this file (`.ufo/waves/round-98/seats/V09-c3-checker.md`, absolute). Scratch: `.ufo/waves/round-98/seats/V09-scratch/` (poll logs, census script + receipts, map-row comparator, hashes). No commits, no pushes, no network, no other writes.
- Poll-wait gate: S3-owned files + S3 report, with a strengthened content gate (r98 map obligations 20/20 PASS) after the placeholder hazard was observed. Poll log: `.ufo/waves/round-98/seats/V09-scratch/poll.log` and `poll2.log`.
  - `poll.sh` try=1 (20:28:39): S3 fixture files + r95 repair present; only `S3:report` missing.
  - `poll2.sh` (S3 report + map 20/20 PASS): try=1 (20:30:21) map still 17/20; try=2 (20:30:41) map green, only report missing; **POLL-DONE try=4 (20:31:21)**. S3 report mtime 20:31:01. No plan was ever verified; nothing fabricated.

## Seat checklist

| # | Requirement | Result |
|---|---|---|
| 1 | `check_bible` r98 CLEAN exit 0; counts 6 entities / 1 relation / 7 events / 7 sources | PASS |
| 2 | `clerk-filing-open` tick 14, `depends_on [acknowledgment-aru-records]` | PASS |
| 3 | `clerk-maren` passes schema (first_appearance resolves, claim cites `clerk-filing-note`) | PASS |
| 4 | r97 still CLEAN | PASS |
| 5 | C3 support: 20 map obligations (17 inherited + first_appearance + claim + event), inherited rows parsed-value identical, census 171→172, r95 repair receipts unchanged | PASS |

## 1. check_bible and counts (settled bytes, re-run after poll2 closed)

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r98-clerk-filing ; echo EXIT-R98=$?
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT-R98=0
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r97-crossing-acknowledgment ; echo EXIT-R97=$?
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT-R97=0
```

```
$ python3 -c "import json;[print(t, len(json.load(open('corpus/fixtures/r98-clerk-filing/%s.json'%t)))) for t in ('entities','relations','timeline','sources','contradictions')]"
entities 6
relations 1
timeline 7
sources 7
contradictions 0
```

Counts are exactly the declared 6/1/7 with 7 sources (contradictions correctly empty — the filing asserts no finding and no resolution).

## 2. Tick-14 filing event (exact parsed entry)

```
{"id": "clerk-filing-open", "tick": 14, "entity_id": "clerk-maren", "place_id": "chalk-stair",
 "depends_on": ["acknowledgment-aru-records"],
 "description": "At the Chalk Stair at tick 14, the clerk filed both pending accounts and recorded the matter OPEN, asserting no finding and no resolution.",
 "source_id": "clerk-filing-note"}
```

tick 14, actor `clerk-maren`, place `chalk-stair`, `depends_on == ["acknowledgment-aru-records"]`, source `clerk-filing-note` — all as declared.

## 3. clerk-maren schema resolution

```
{"id": "clerk-maren", "kind": "character", "name": "Maren", "first_appearance": "clerk-filing-note",
 "claims": [{"statement": "The filing note names Maren, the clerk of the Chalk Stair registry, as the officer who filed both pending accounts.",
             "source_id": "clerk-filing-note"}]}
```

`first_appearance` `clerk-filing-note` resolves in `sources.json` (row 7); the single claim cites `clerk-filing-note`. Dangling/duplicate audit over all three id spaces (entities, sources, events), every claim/first_appearance source, both relation endpoints (`from`/`to`), and every `depends_on` target:

```
dups {'entities': [], 'sources': [], 'events': []}
dangling []
```

## 4. Inheritance and preservation (independent, parsed-value + byte-prefix)

```
entities  pre 5  post 6  prefix_equal True
relations pre 1  post 1  prefix_equal True
timeline  pre 6  post 7  prefix_equal True
sources   pre 6  post 7  prefix_equal True
```

(`pre` = `git show 9a3d648:corpus/fixtures/r97-crossing-acknowledgment/<t>.json` parsed and compared as the post list's prefix.) `fictional-excerpts.md` is a byte prefix of r97's (53 lines) plus the appended Round 98 section (lines 54–64); `relations.json`, `contradictions.json`, `inspiration-note.md`, `source-excerpt.md` remain byte-identical to r97 (`sha256` equal pairwise).

## 5. C3 map obligations — 20/20, inherited rows identical

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r98-clerk-filing ; echo EXIT=$?
OBLIGATIONS raw=20 mapped=20
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22
RESULT PASS
EXIT=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing | grep -E "INVENTORY|RESULT"
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 18/18
RESULT PASS
```

Map rows J01–J17 vs the r97 map (fresh comparator `V09-scratch/map_rows_v09.py`, all cells parsed): the only differing cell is column 3, the path-qualification namespace (`r97-crossing-acknowledgment:*` → `r98-clerk-filing:*`); `diffs_ignoring_namespace_col: []`. Editorial rows S01/S02 identical. The three new rows are exactly the declared obligations: J18 `entities.json#/5/first_appearance` (`clerk-maren`, anchor line 60), J19 `entities.json#/5/claims/0` (lines 59-60), J20 `timeline.json#/6` (lines 55-64), all resolving `r98-clerk-filing:clerk-filing-note`; the `**Expected inventory:**` line reads `20 JSON facts; 2 editorial rows; 22 total mapped rows; 18 distinct excerpt anchors`.

Interim evidence (before S4's map rewrite landed, 20:30:21): `map_obligations` failed with exactly the three expected findings and nothing else — `OBLIGATIONS raw=20 mapped=17`; `missing_obligation` for `entities.json#/5/first_appearance`, `entities.json#/5/claims/0`, `timeline.json#/6`. No phantom or extra obligation class; this independently matches S3's interim report.

## 6. Census 171→172 (fresh implementation, repo-relative argv)

Pre-state measured by excluding the new dir (`python3 V09-scratch/census_v09.py pre_excl_r98 r98-clerk-filing`), post-state on the settled tree:

```
pre : {"fixture_dirs": 171, "clean_exit0": 37, "negative_exit1": 134, "violation_lines": 421, "non_0_1_exits": []}
post: {"fixture_dirs": 172, "clean_exit0": 38, "negative_exit1": 134, "violation_lines": 421, "non_0_1_exits": []}
```

171→172 dirs, +1 clean, negative and violation lines unchanged, zero non-0/1 exits — exactly the declared delta, and the pre figure independently reproduces the r97 closure census 171/37/134/421.

## 7. r95 one-sentence repair — data rows untouched, receipts unchanged

```
$ git diff 9a3d648 -- corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md | grep -cE '^[+-]\|'
0        # zero table-row diff lines; the diff is exactly one prose line (49)
$ grep -c "new relation" <(git show 9a3d648:corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md)   -> 1
$ grep -c "new relation" corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md                     -> 0
```

Receipts on pre-repair bytes (restored from `9a3d648` into `V09-scratch/r95-pre/`) vs the delivered cluster — byte-identical:

```
map_obligations  pre: OBLIGATIONS raw=15 mapped=15; RESULT PASS (exit 0)
                 live: OBLIGATIONS raw=15 mapped=15; RESULT PASS (exit 0)
support_check    pre: SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS 2/2; MODES 17/17; VALIDATED-ROWS 17/17; RESULT PASS (exit 0)
                 live: identical lines; RESULT PASS (exit 0)
```

Map sha256 moved `30281ff1…` (closure blob) → `80440d61…` (delivered), matching S3's receipt.

## Verification stability

Final hashes (`V09-scratch/final-hashes.txt`) re-hashed after a 15 s settle window: unchanged (`STABLE-15s`). All r98 mtimes are ≤20:30:41 (JSON tables 20:28:55, map 20:30:21, README 20:30:41); the final gate batch ran 20:31:36+. Key hashes: entities `db2d8e5d…`, sources `32ee15b1…`, timeline `eb24e084…`, fictional-excerpts `29e384bf…`, map `c1099d0e…`, r95 map `80440d61…`.

## Caveats and cross-seat observations (evidence, not verdicts)

- **Placeholder-poll hazard confirmed.** The r98 `claim-excerpt-map.md` was byte-identical to r97's map from copy time (20:28:24) until S4's rewrite (20:30:21); an existence-only poll is satisfied by the placeholder. My first (existence-based) poll passed `missing2` on exactly this state; the strengthened gate (content: `raw=20 mapped=20` + PASS) was required to close the seat. This matches S3 report §D1.
- **Race in my first census run.** A first census launch (tagged `pre`) raced the fixture creation and captured the post state 172/38; the genuine pre figure was then measured by exclusion (171/37/134/421). Both receipts are retained in scratch.
- **S3 report §D1 stale clause.** It states the r98 `README.md` was still byte-identical to r97 at report time; my final check finds `README.md` differs from r97 (mtime 20:30:41, before the report's 20:31:01) and names `r98-clerk-filing` four times. No impact on C3; S4's rewrite had landed.
- Checker scope note: a CLEAN `check_bible`/map/support result is structural and lexical preflight only — no entailment, fidelity, authenticity, rights, or canon judgment.

## Bottom line

**PASS** — on the settled revision, r98-clerk-filing verifies independently as declared (CLEAN, 6/1/7/7, tick-14 `clerk-filing-open` → `[acknowledgment-aru-records]`, `clerk-maren` resolves via `clerk-filing-note`, inherited rows parsed-value identical, 20/20 map obligations, census 171→172), r97 stays CLEAN, and the r95 repair touched exactly one prose line with byte-identical receipts.
