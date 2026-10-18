# V15 — preservation census (round 95)

Seat: V15 preservation-census. Scope per seat spec: enumerate `corpus/fixtures/`
(expect 169 dirs), diff every inherited path against `git show fb118c4`, and
verify the W05 pin file, naming each broken pin.

Snapshot revision: HEAD `fb118c4` with the round's working-tree writes present
(uncommitted). Snapshot window **2026-10-17T16:29:50-03:00 → 16:30:37-03:00**;
the three tool hashes were re-read 47 s apart and were identical, so the
snapshot is post-producer-write and stable. All five producer reports
(`P1-tool-code.md` … `P5-knowledge-note.md`) were on disk before the snapshot
(P2's, the last, appeared at ~16:28:45 after a 20 s-cadence poll of 40 tries).

This seat wrote only this report. No corpus or tool file was modified; no
scratch dir was declared or used; no commits, no network, no nested agents.

## 1. Census — 169 dirs, delta exactly +1

```sh
find corpus/fixtures -mindepth 1 -maxdepth 1 -type d | wc -l   # → 169
find corpus/fixtures -type f | wc -l                           # → 1000
```

Baseline `fb118c4` (via `git ls-tree -r fb118c4 --name-only corpus/fixtures/`):

```sh
git ls-tree -r fb118c4 --name-only corpus/fixtures/ | awk -F/ 'NF>3 {print $3}' | sort -u | wc -l   # → 168
git ls-tree -r fb118c4 --name-only corpus/fixtures/ | wc -l                                         # → 990
```

Directory and file deltas, computed by `comm` against those two baselines:

```text
  ADDED r95-crossing-aftermath          (only directory delta; 0 REMOVED)
  ADDED corpus/fixtures/r95-crossing-aftermath/{README.md,claim-excerpt-map.md,
        contradictions.json,entities.json,fictional-excerpts.md,inspiration-note.md,
        relations.json,source-excerpt.md,sources.json,timeline.json}
```

168 → **169 dirs**, 990 → **1000 files**, matching the declared C2 census
(168→169). Cross-check by arithmetic against the pin: 1000 current fixture files
− 980 pinned fixture rows = 20 unpinned files, and they are exactly
`r94-paired-crossing` (10) + `r95-crossing-aftermath` (10) — no other unpinned
file exists in `corpus/fixtures/`.

## 2. Inherited-path diff vs `fb118c4`

Authoritative, mode-aware check:

```sh
git diff --name-status fb118c4
M  LOG.md
M  corpus/tools/README.md
M  corpus/tools/map-obligations-contract.json
M  corpus/tools/map_obligations.py
```

No deletions, no mode changes, nothing else tracked changed. `git diff
--name-status fb118c4 -- .ufo/` is empty and `git status --porcelain
--untracked-files=all -- .ufo/` shows untracked files only under
`.ufo/waves/round-95/` (seat reports and seat scratch, allowed by the round):
the r94 wave artifacts are byte-intact.

Independent second method over **all 1780 inherited `corpus/` paths** (SHA-1 of
working-tree content via `git hash-object --stdin-paths` vs the blob SHA-1 from
`git ls-tree -r fb118c4`):

```sh
paste <(git ls-tree -r fb118c4 corpus/ | awk '{print $3}') \
      <(git ls-tree -r fb118c4 corpus/ | awk '{print $4}' | git hash-object --stdin-paths) \
      <(git ls-tree -r fb118c4 corpus/ | awk '{print $4}') | awk '$1!=$2 {print "CHANGED " $3}'
  CHANGED corpus/tools/README.md
  CHANGED corpus/tools/map-obligations-contract.json
  CHANGED corpus/tools/map_obligations.py
```

Repo-wide variant over all 6949 inherited paths: only `LOG.md` plus a symlink
false positive (§6.1).

Owned new (untracked) paths at snapshot — the full set outside `.ufo/`:

```text
corpus/fixtures/r95-crossing-aftermath/  (10 files, hashes in §5)
corpus/knowledge/r95-aftermath-scope-note.md
```

**Verdict:** the inherited change set is exactly the declared one —
`corpus/tools/map_obligations.py`, `corpus/tools/map-obligations-contract.json`,
`corpus/tools/README.md`, plus the new fixture tree and the new knowledge note.
No other inherited path changed anywhere in the repo. `LOG.md` is the one
changed path outside the declared producer-owned set; see §6.4.

## 3. W05 pin verification — one broken pin, pre-existing

Pin file: `.ufo/waves/round-94/work/W05-baseline-corpus.sha256` (984 rows: 980
fixture files + 4 tool inputs, built at `9c2eea3`). No r95 pin file exists yet —
`find .ufo/waves/round-95 -maxdepth 3 -name '*.sha256' -o -maxdepth 3 -iname
'*pin*'` returns only the seat report `V48-pins-fresh.md`, so the r94 W05 pin is
the only pin available to check.

```sh
sha256sum -c .ufo/waves/round-94/work/W05-baseline-corpus.sha256
corpus/fixtures/README.md: FAILED
sha256sum: WARNING: 1 computed checksum did NOT match
# 983 rows OK, 984 total, 0 missing paths
```

**Broken pin, named: `corpus/fixtures/README.md`.** Classification:

| Field | Value |
|---|---|
| pin row (`9c2eea3`) | `a13d1af36aed025a13d433bc72d8870713fdf6b1f332874d28df72c168b75e93` |
| blob at `fb118c4` | `01161b047f318c24e7c5e3ab0e763a07c6c90d97566dffc84682c46659651d91` |
| working tree now | `01161b047f318c24e7c5e3ab0e763a07c6c90d97566dffc84682c46659651d91` |

`git log --oneline -5 -- corpus/fixtures/README.md` shows the last writer is
`ac69044` ("lore r94: land admission conditions C-1..C-4,C-6 …"), and the
working-tree hash equals the `fb118c4` blob. So this pin was **already broken at
the r95 baseline by the r94 round**, not by any r95 write; the working tree
changed no byte of it during r95. It is the only broken pin among 984 rows.

Coverage note: the pin does **not** contain `corpus/tools/map_obligations.py`,
`corpus/tools/map-obligations-contract.json`, or `corpus/tools/README.md`
(`grep -c 'map_obligations\|map-obligations' <pin>` → 0; the pin's tool rows are
`support_check.py`, `discriminate_check.py`, `boundary_doc_check.py`,
`boundary-doc-contract.json`). The C1/C3 tool edits therefore cannot break any
pin row, and the three changed tool files are unpinned at r94. Conversely, all
980 pinned fixture rows still verify byte-for-byte except the README row above,
so no pinned fixture was disturbed by the round.

## 4. Preservation of the new fixture (C2 byte-copy claims)

`corpus/fixtures/r95-crossing-aftermath/` vs the `fb118c4` blobs of
`corpus/fixtures/r94-paired-crossing/`, SHA-256 of `git cat-file blob` vs the
working-tree file:

```text
IDENTICAL  contradictions.json   IDENTICAL  entities.json
IDENTICAL  inspiration-note.md  IDENTICAL  relations.json
IDENTICAL  source-excerpt.md
DIFFERS    fictional-excerpts.md   (declared modified)
DIFFERS    sources.json            (declared modified)
DIFFERS    timeline.json           (declared modified)
```

- `sources.json`: r94's 3 entries byte-identical in order, plus the new
  `aru-aftermath-note` entry (4 sources). `r95 sources[:3] == r94 sources`.
- `timeline.json`: r94's 3 events byte-identical in order, plus
  `aftermath-missing-evin` (tick 11, `entity_id: aru`, `place_id: chalk-stair`,
  `depends_on: ["paired-crossing-decision"]`, `source_id: aru-aftermath-note`).
- `fictional-excerpts.md`: r94 lines 1–20 preserved; the aftermath section is
  appended at lines 21–31, and the J15 anchor `Tick 11: I waited at the Chalk
  Stair through the agreed bell.` sits at line 26 inside the declared span 22–31.

Map-row inheritance (r95 map vs r94 map, normalizing the fixture path name
`r95-crossing-aftermath` → `r94-paired-crossing`): the J-row diff is a single
added line — **J01–J14 are identical** and only `| J15 |` is new
(`timeline.json#/3`). Editorial rows are 2 in both maps (J rows: 14 → 15).

Structural counts recomputed from the delivered JSON: 5 entities / 5
`first_appearance` / 5 claims / 1 relation / 4 events / 4 sources / 0
contradictions → 15 JSON obligations (5+5+1+4), matching the declared
14 inherited + 1 new.

## 5. Snapshot hashes and receipts at the delivered revision

Changed paths (SHA-256 at 16:30:37):

```text
d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108  corpus/tools/map_obligations.py
8173bb97592a377716866737e8fcb4043014c9814e77a6248500d301a39170db  corpus/tools/map-obligations-contract.json
5d033c9db8a72801c9b8d5e609e01cddf1ace668711e24d0476b8cbd6879a264  corpus/tools/README.md
f87ed42ad4d42143bb84f13539f2db8ca0d5f221aaf4eaffdbd6874b5ef1ab9a  corpus/knowledge/r95-aftermath-scope-note.md
9d27af4ac9644210d3ee1df26938a4a5592b8cbcfdb5d6fb880de6ccdb1bdd0b  corpus/fixtures/r95-crossing-aftermath/README.md
30281ff1a497bbe66f23cbd8a49befb3319595f20990718a0ffe8050741a874a  corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md
0ef6734ae52d28656e75869d942d6b1e8e324b116977a2811b3b36dc0880b282  corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md
fd9e30e8d9ad40013be2172781d13d84ba219377c8433ff6e529ea8e1927e64a  corpus/fixtures/r95-crossing-aftermath/sources.json
3c0faad6bf32f944f9f2a20f3bd15829044afa04f1a8837601903433b00ea177  corpus/fixtures/r95-crossing-aftermath/timeline.json
```

Unchanged (pinned) copies in the same dir: `contradictions.json`
`37517e5f…`, `entities.json` `026af0bc…`, `inspiration-note.md` `58f5390e…`,
`relations.json` `c279254b…`, `source-excerpt.md` `b5edc2fd…` — each equal to the
corresponding r94 blob hash.

Preservation-adjacent receipts observed at this revision (cross-checks for other
seats, not this seat's verdict): `check_bible` on the r95 fixture → `CLEAN:
schema, citations, relations, timeline; 0 violations`, exit 0; `map_obligations`
r95 → `OBLIGATIONS raw=15 mapped=15` / `15/15`, exit 0; r94 →
`raw=14 mapped=14` / `14/14`, exit 0; `--self-test` → `RESULT PASS`, exit 0
(contract `self_test.cases` length 22; r94 baseline was 20).

## 6. Observations, caveats, findings

**6.1 Symlink false positive in my hash sweep (methodology, not a repo change).**
The repo-wide `git hash-object` sweep flagged
`.ufo/waves/round-94/work/W16-scratch/cluster/escape.md`. It is a symlink
(`120000 blob 549f073e… → ../outside.md`); `git hash-object` follows symlinks and
hashed the target's bytes, while `git diff --name-status fb118c4 -- <path>` is
empty and `git status --porcelain -- <path>` clean. Not a change. `corpus/` has
0 symlinks at baseline, so the corpus sweep in §2 is unaffected.

**6.2 Transient repo-root scratch dirs during concurrent self-tests.** Two
snapshots caught untracked `map-obligations-self-test-<rand>/` trees at the repo
root (e.g. `-8x56x44x`, `-1t3xvon6`, `-k0fd7dlb`) while other seats ran
`--self-test`; the tool uses `tempfile.TemporaryDirectory(prefix="map-obligations-self-test-", dir=ROOT)`
(`corpus/tools/map_obligations.py:720`) and they vanish on run exit. Time-bounded
observation, not pollution at rest, and it does not touch `corpus/fixtures/`.
Consequence for census readers: `git status` at repo root is not stable while
verifiers are running; the `corpus/fixtures/` census is.

**6.3 One broken pin, inherited.** `corpus/fixtures/README.md` (§3). The r94 W05
pin is stale against its own baseline; a re-pin (or a documented exception) is
needed before the pin can be used as an r95/r96 preservation gate. No r95 pin
file exists at snapshot.

**6.4 `LOG.md` modified outside the declared producer-owned set.** Diff is
`57 0 LOG.md` (purely additive, 0 deletions) and is the round-95 declaration
reproduced in the LOG tail read at seat start; it is the L1 declaration write,
not a producer write. Reported so closure accounts for the fifth changed path.

**6.5 Producer reports.** All five present at snapshot (P1 `P1-tool-code.md`,
P2 `P2-contract-docs.md`, P3 `P3-fixture-json.md`, P4 `P4-fixture-docs.md`,
P5 `P5-knowledge-note.md`); nothing in this seat's scope was ABSENT.

## Findings summary

| # | Finding | Class |
|---|---|---|
| F-V15-1 | Inherited change set equals the declared set exactly; 0 unexpected inherited changes in 6949 paths | PASS |
| F-V15-2 | Census 169 dirs (+1 = `r95-crossing-aftermath`), 1000 files (+10), 0 removals | PASS |
| F-V15-3 | `corpus/fixtures/README.md` pin broken — pre-existing (r94 `ac69044`), not an r95 write | finding (inherited, owner: closure/re-pin) |
| F-V15-4 | All 980 pinned fixture rows otherwise intact; the three changed tool files are unpinned | PASS |
| F-V15-5 | New fixture preserves r94 byte-for-byte where declared (5 identical copies, 3 declared edits, J01–J14 unchanged, only J15 added) | PASS |
| F-V15-6 | Symlink false positive in my own sweep; transient `map-obligations-self-test-*` dirs at repo root during concurrent self-tests | methodology note |

Bottom line: **PASS** — census 169 dirs confirmed; the only inherited changes vs
`fb118c4` are the declared tool trio plus the new r95 fixture tree and knowledge
note (LOG.md being the additive round declaration); the W05 pin's single broken
row (`corpus/fixtures/README.md`) was already broken at baseline by r94 and no
r95 write broke any pin.
