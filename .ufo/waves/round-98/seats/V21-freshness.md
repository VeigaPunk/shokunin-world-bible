# V21 — freshness (round 98)

Seat: V21 freshness. Brief: *after producers* — the two dated correction addenda land with correct
current hashes (recompute the delivered tool hashes myself and compare against the addenda); no other
stale pins; metadata headers present. Leaf seat: no nested agents, no commits, no pushes, no network.
Only write: this report (absolute path) and `.ufo/waves/round-98/seats/V21-scratch/`. All commands ran
from the lane root `/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`/`sha256sum`; every write
path was absolute and verified to resolve under `lore-shokunin/`. Baseline r97 closure `9a3d648`
(pre-round bytes via `git show 9a3d648:<path>`); HEAD during the round `dd4df1b`; the wave tree
uncommitted. I did not verify C1/C2/C3 semantics (other seats' scope); this report covers the freshness
surface only.

**Poll-wait:** background poll (20 s cadence, 40 tries) started 20:28:33; it checked artifact state AND
producer reports each try. Artifacts: `corpus/fixtures/r98-clerk-filing/` populated from 20:28 (S3 JSON
complete by 20:30:52, S4 README/map by 20:30:41), `corpus/knowledge/r98-clerk-scope-note.md` present by
20:32:34, S1's `dependency_freeze.py` landed 20:31:49 (contract iterated `3a940a9f` → `c435239d` →
`153ebc5b` until 20:33:36), S2's tools README addendum landed 20:34:06. Producer reports: S3 20:31:25,
S4 20:32:06, S5 20:34:00, S2 20:34:53, S1 20:35:33 — **ALL-PRESENT at try 22, 20:35:34** (all five
reports; no stall escape needed, no all-reports poll ever waited on SELF). No verification ran against a
plan: my pre-freeze runs (noted as previews) touched only already-delivered bytes and every receipt below
was re-run on the frozen snapshot after all five reports existed. Snapshot stability: `sha256sum -c` on
the frozen lists at 20:41 → **11/11 OK and 10/10 OK, zero FAILED** (no byte moved after the freeze).

## Frozen snapshot verified (11 modified/new top-level bytes + the 10 r98 fixture files)

| byte | sha256 (12-hex) | mtime |
|---|---|---|
| `corpus/tools/dependency_freeze.py` | `03d04365cf00` | 20:31:49 |
| `corpus/tools/dependency-freeze-contract.json` | `153ebc5b2092` | 20:33:36 |
| `corpus/tools/README.md` | `1d299c16bf9a` | 20:34:06 |
| `corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md` | `80440d611224` | 20:28:34 |
| `corpus/knowledge/r95-aftermath-scope-note.md` | `8e9e1774c107` | 20:29:14 |
| `corpus/knowledge/r96-response-scope-note.md` | `a9b51f8ccd78` | 20:29:14 |
| `corpus/knowledge/r98-clerk-scope-note.md` | `1162262c7424` | 20:33:01 |
| `r98 …/README.md` | `32efc78f70e6` | 20:30:41 |
| `r98 …/claim-excerpt-map.md` | `c1099d0ee9ee` | 20:30:21 |
| `r98 …/entities.json` | `db2d8e5d3866` | 20:28 |
| `r98 …/sources.json` | `32ee15b1f3d7` | 20:28 |
| `r98 …/timeline.json` | `eb24e0848e59` | 20:28 |
| `r98 …/fictional-excerpts.md` | `29e384bf2eb2` | 20:28 |
| `r98 …/relations.json` | `c279254bc7de` | 20:28 (byte copy of r97) |
| `r98 …/contradictions.json` | `37517e5f3dc6` | 20:28 (byte copy of r97) |
| `r98 …/inspiration-note.md` | `58f5390e5928` | 20:28 (byte copy of r97) |
| `r98 …/source-excerpt.md` | `b5edc2fd3c2e` | 20:28 (byte copy of r97) |
| `corpus/fixtures/check_bible.py` | `ff9fd2aa6811` | unchanged |
| `corpus/tools/support_check.py` | `55a5eb275390` | unchanged |
| `corpus/tools/map_obligations.py` | `86b529496214` | unchanged |
| `corpus/tools/map-obligations-contract.json` | `2142b9917694` | unchanged |

All producer-reported hashes match my own recomputation (S1 §Owned and delivered; S2 §Byte state
verified; S3 report file-hash block `:145-148`; S4 report file hashes `:14-16`; S5 §header). `git status
--porcelain` shows exactly the declared set: `M LOG.md`, `M` r95 map,
`M` the two notes, `M` the three tools files, `??` r98 fixture, `??` r98 note, `??`
`.ufo/waves/round-98/` — nothing else.

## Check 1 — the two dated correction addenda, hashes recomputed: PASS

Both addenda present, dated, append-only (0 deletions):

```sh
git diff --stat 9a3d648 -- corpus/knowledge/ corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md
# r95 …/claim-excerpt-map.md   |  2 +-
# r95-aftermath-scope-note.md  | 14 ++++++++++++++
# r96-response-scope-note.md   | 14 ++++++++++++++
```

`corpus/knowledge/r95-aftermath-scope-note.md:59` and `r96-response-scope-note.md:63`:
`## Correction addendum (2026-10-17, round 98, S5 knowledge-notes seat)`. Each quotes a
`sha256sum corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json` block. I
recomputed the delivered bytes myself:

```sh
sha256sum corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json
# 86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9  corpus/tools/map_obligations.py
# 2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41  corpus/tools/map-obligations-contract.json
```

Both addenda's claimed current hashes (`86b52949…` / `2142b991…`) **match exactly**; both addenda's
"`check_bible.py` `ff9fd2aa…` and `support_check.py` `55a5eb27…` … still current" **match the delivered
bytes** (`ff9fd2aa6811…` / `55a5eb275390…`, unchanged this round).

The addenda's historical claims were verified against the full git history (all branches):

```sh
git log --all --format=%H -- corpus/tools/map_obligations.py | while read c; do
  git show $c:corpus/tools/map_obligations.py | sha256sum | cut -c1-12; done | sort -u
# 2b0ba815326b 86b529496214 cc1df4dc4068 d1c239ccb214     (exactly the four committed revisions)
git log --all --format=%H -- corpus/tools/map-obligations-contract.json | … | sort -u
# 2142b9917694 349a1956714c 8173bb97592a 97b76bb8b1fe
```

So `9224a684…`, `6634e176…` (and the r97 note's `70795150…`, the r95 note's `ca05159e…`) **never entered
the committed history** — the addenda's "in-flight intermediate, never committed" wording is accurate.
The r96 addendum's commit references check out: `dcb2d92` = r95 closure ("lore r95: freeze admitted
wave…"), and the revision mapping cc1df4dc=r94(abbc3e0), d1c239cc=r95(dcb2d92), 2b0ba815=r96(f3e09f9),
86b52949=r97(9d25df9), contract 8173bb97=r95(dcb2d92), 97b76bb8=r96(f3e09f9) — each verified with
`git show <commit>:<path> | sha256sum`.

The addenda's receipt-replay claims reproduce on the delivered revision (see §Supporting evidence):
r95 `15/15` + `raw=15 mapped=15` PASS, r96 `16/16` + `raw=16 mapped=16` PASS, and the r96 addendum's
"the r95 fixture … still reads `raw=15 mapped=15`" — all exit 0. The addenda do not touch any other
pin, and the r95 map repair they sit beside changed exactly one carried sentence
(`git diff 9a3d648 -- …claim-excerpt-map.md` → 1 insertion, 1 deletion; data rows byte-unchanged), with
no pin anywhere referencing the pre-repair map sha (`30281ff1…` does not appear in `corpus/`).

## Check 2 — no other stale pins: PASS (two observations, both non-blocking)

Full sweep of every hash-shaped pin in `corpus/` (all `.md`/`.json`/`.py`), each classified against the
delivered bytes:

**Current and matching:** `r91-c9-watch.md` (`ff9fd2aa…` ×8 lines incl. full 64-hex),
`holder-assessment-boundary.md:535` (`ff9fd2aa…` at `ca7f9ef`, checker still byte-identical),
`fixtures/README.md:1091` (`ff9fd2aa…`), `r97-acknowledgment-scope-note.md:64` (`ff9fd2aa…`,
`55a5eb27…`, `86b52949…`), `r98-clerk-scope-note.md:64` (`ff9fd2aa…`, `55a5eb27…`, `86b52949…`,
`2142b991…`), both addenda's current pins, `tools/README.md:270` (`3c922d20a01bbd3f…`,
`59a0f4fa3d4a47e0…` = the contract's r97/r98 content digests — matched), contract pin digests
themselves (see below).

**Explicitly labeled historical/superseded, and accurate:** `tools/README.md:193` (`2b0ba815…` labeled
"Before (r96 revision)" — matches git history), `:228` (`e851f068…` r96 map digest; delivered r96 map =
`e851f068cfd7`), `fixtures/README.md:1175` (`a13d1af3…` W05 pin explicitly stated "no longer matches"),
`r87-provenance-chain-decision-table.md:11` (`3ae4134d…` at snapshot `2b48ca72` — verified:
`git show 2b48ca72:corpus/fixtures/check_bible.py | sha256sum` → `3ae4134d1d7d…`),
`holder-assessment-boundary.md:130/143` (`dcacffd6…`/`e2bb9639…` r88/r89-era checker comparisons,
labeled by round), `r95:51`/`r96:55` (original stale pins preserved as history + corrected by the
addenda), `r97:32` (`5093d72e…` pre-repair → `e851f068…` post-repair, accurate), `r97:64`
(`70795150…` labeled "an earlier run the same pass"), `r93-r8-worked-example.md:116` (`da934a7e…` is an
example-code dossier digest inside a python block, not a file pin).

**Contract pins:** all six pins resolve in the delivered chain (below); pin `revision` values
`60dba0c2` (r88/r94/r95), `2393934` (r96), `dd4df1b` (r97/r98) all resolve as commits; the contract's
provenance note's V46 mutation reference checks out — `37a425b97af6…` =
`.ufo/waves/round-97/seats/V46-scratch/r97-depdropped/timeline.json` (and its mirror copy) exactly.

**Observation 1 (self-caveated in-flight reference, same class as r97's `70795150…`):**
`corpus/knowledge/r98-clerk-scope-note.md:64` records "S1's C1 revisions landed shortly after
(`dependency_freeze.py` `03d04365…`, contract `c435239d…` at 20:32:51-03:00)". The tool hash is the
delivered one; the **contract hash is S1's intermediate revision** — delivered is `153ebc5b…`. My poll
log independently confirms the timeline (`dfc=c435239d94da` at 20:32:54; `dfc=153ebc5b2092` at
20:33:54). The sentence is explicitly time-stamped, and the paragraph ends "re-measure the tool
revisions against the delivered revision before citing these receipts" — correctable next touch, not a
false pin; the addenda and tools README do not repeat the intermediate hash.

**Observation 2 (literal-wording blemish):** `tools/README.md:284` states
"`git diff 9a3d648 -- corpus/tools/` lists only `dependency_freeze.py` and `dependency-freeze-contract.json`".
Literally the diff also lists `README.md` itself:

```sh
git diff --name-only 9a3d648 -- corpus/tools/
# corpus/tools/README.md
# corpus/tools/dependency-freeze-contract.json
# corpus/tools/dependency_freeze.py
```

The intended claim (the only tool/contract changes are those two files) holds; the sentence as written
is imprecise about its own file. Low severity, no gate reads it.

**Pre-existing (not introduced this round):** `2026-10-12-malformed-error-patterns.md:9` names baseline
commit `b6ca1e90…`, which does not resolve in the current history; the file is unchanged since its r5
commit `60f4956` (`git diff --stat 9a3d648 -- …` empty), so this is a carried historical reference, not
a round-98 pin.

## Check 3 — metadata headers present: PASS

- `corpus/knowledge/r98-clerk-scope-note.md:1-4` carries the standard header — `source:`
  (cited-path list), `verified-at: 2026-10-17 …`, `recheck: …`, plus the declared
  `citation-convention:` line (same addition as the r97 note).
- `corpus/knowledge/r95-aftermath-scope-note.md:1-3` and `r96-response-scope-note.md:1-3` headers intact
  (the round's diffs are pure appends, `+14/-0` each), and both addenda headings carry the date
  `2026-10-17` and the round/seat label.
- `corpus/tools/README.md:230` heading:
  `### Round-98 addendum: … (2026-10-17)`.

## Supporting evidence (frozen revision, all exit 0)

```sh
python3 corpus/tools/dependency_freeze.py --self-test        # SELF-TEST 17/17 / RESULT PASS, exit 0
for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath \
         r96-crossing-response r97-crossing-acknowledgment r98-clerk-filing; do
  python3 corpus/tools/dependency_freeze.py "corpus/fixtures/$f"; done
# 6/6 RESULT PASS: r88 2/2; r94 3/3; r95 4/4; r96 5/5; r97 6/6; r98 7/7 (dependency-edges 0/0…6/6)
python3 corpus/tools/map_obligations.py --self-test           # SELF-TEST CASES 25/25 pinned / RESULT PASS, exit 0
```

Receipts re-run on the delivered revision (all exit 0; addenda/note claims reproduce):
r95 `check_bible` CLEAN / `support_check` `15/15` `17/17` / `map_obligations` `raw=15 mapped=15`;
r96 CLEAN / `16/16` `18/18` / `raw=16`; r97 CLEAN / `17/17` `19/19` / `raw=17`;
r98 CLEAN / `20/20` `22/22` / `raw=20`. Census `ls -d corpus/fixtures/*/ | wc -l` = **172**.

## Notes for L1 (read-only carried docs, not owned this round; none block freshness)

1. `corpus/README.md:38` — "16-case persisted self-test", chain "(r88-m3 → r94 → r95 → r96)", "the r97
   fixture is not yet pinned" → superseded by the delivered state (17 cases; six-fixture chain;
   r97+r98 pinned).
2. `SKILL.md:98` — "16 cases"; `SKILL.md:100` — "the frozen chain is the declared four fixtures
   (`r97-crossing-acknowledgment` unpinned as of r97 closure — r98 candidate); a path-less legacy pin
   cannot be refreshed in place (manual contract edit)" → superseded (six fixtures; r97+r98 pinned;
   path-less pins are now migrated by `--freeze`).
3. `corpus/fixtures/README.md` Round-97 section — "16 cases" / "declared four fixtures —
   `r97-crossing-acknowledgment` is not yet pinned (r98 candidate)"; no Round-98 section yet (census
   171 at r97 closure → **172** measured now). Closure-doc pass item, same class as r97's V25 notes.

## Bottom line

**PASS** — on the frozen delivered snapshot (all five producer reports present, all 21 declared bytes
sha-verified and stable at report time), the two dated correction addenda are present and append-only
and their current-hash claims (`86b52949…` / `2142b991…`, with `ff9fd2aa…` / `55a5eb27…` re-confirmed)
match my own recomputation of the delivered tools exactly, their historical revision claims are
git-verified, no other stale pin remains (every pin in `corpus/` resolves to delivered bytes or is
explicitly labeled historical/in-flight — the sole in-flight reference, the r98 note's `c435239d…`
timeline record, is self-caveated and correctable next touch), and the metadata headers are present
(r98 note source/verified-at/recheck/citation-convention; dated addendum headings), with all receipts,
the 17/17 self-test and the 6/6 chain re-run green on the frozen revision.
