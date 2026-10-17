# V24 — preservation census (round 96)

**Seat:** V24 `preservation-census`. Scope per seat spec: enumerate
`corpus/fixtures/` (expect 170), diff every inherited path against `dcb2d92`,
expected changes ONLY `map_obligations.py`, `map-obligations-contract.json`,
`tools/README.md` plus the new paths (`dependency_freeze.py`,
`dependency-freeze-contract.json`, `r96-crossing-response/**`,
`r96-response-scope-note.md`); name any W05 pin broken by inherited changes
(expected none — touched inherited files are unpinned tools/README class).

**Report path (only file written by this seat):** this file. Scratch:
`.ufo/waves/round-96/seats/V24-scratch/` (absolute
`/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-96/seats/V24-scratch/`,
4 files: `pin_check.py`, `copy_check.py`, `snap-a.sha256`, `snap-b.sha256`,
plus `dirs-base.txt`/`dirs-now.txt`/`dirs-final.txt`). No commit, no push, no
network, no nested agents. All commands run from the lane repo root.

**Baseline:** r95 closure `dcb2d92`; `git rev-parse HEAD` →
`60dba0c2aa344860b10a2fc63e00468d1b134f27`. `git diff --name-status dcb2d92..HEAD`
→ `M SCORECARD.md` only, so the one extra inherited diff row below is
baseline-attributable, not an r96 write.

**Snapshot:** taken after all six producer reports landed —
`Q1-tool-hardening.md`, `Q2-contract-docs.md`, `Q3-dependency-freeze.md`,
`Q4-fixture-json.md`, `Q5-fixture-docs.md`, `Q6-knowledge-note.md` all present
(Q2, the last, appeared ~17:51-03:00 after a 20 s-cadence poll). Snapshot window
**2026-10-17T17:52:37-03:00 → 17:54:40-03:00**; the 16 changed/new file hashes
were recomputed 45 s apart and were identical (`diff` of `snap-a.sha256` /
`snap-b.sha256` empty), so the snapshot is post-producer-write and stable.

## 1. Census — 170 dirs, delta exactly +1

```sh
find corpus/fixtures -mindepth 1 -maxdepth 1 -type d | wc -l   # → 170
find corpus/fixtures -type f | wc -l                           # → 1010
find corpus/fixtures -mindepth 1 -maxdepth 1 ! -type d         # → check_bible.py, README.md
```

Baseline `dcb2d92`:

```sh
git ls-tree -r dcb2d92 --name-only corpus/fixtures/ | awk -F/ 'NF>3 {print $3}' | sort -u | wc -l   # → 169
git ls-tree -r dcb2d92 --name-only corpus/fixtures/ | wc -l                                         # → 1000
```

Directory delta by `diff` of sorted name lists:

```text
166a167
> r96-crossing-response
```

169 → **170 dirs**, 1000 → **1010 files**, matching the declared C2 census
(169→170). Zero removed directories, zero removed files.

Arithmetic cross-check against the W05 pin (980 pinned fixture rows):

```sh
comm -13 <(pinned rows) <(find corpus/fixtures -type f | sort) | awk -F/ '{print $3}' | sort | uniq -c
     10 r94-paired-crossing
     10 r95-crossing-aftermath
     10 r96-crossing-response
```

1010 − 980 = 30 unpinned files, exactly the three post-pin fixture dirs
(r94, r95, r96) — no other unpinned fixture file exists.

## 2. Inherited-path diff vs `dcb2d92`

```sh
git diff --name-status dcb2d92
M  LOG.md
M  SCORECARD.md
M  corpus/tools/README.md
M  corpus/tools/map-obligations-contract.json
M  corpus/tools/map_obligations.py

git diff --name-status HEAD          # HEAD = 60dba0c
M  LOG.md
M  corpus/tools/README.md
M  corpus/tools/map-obligations-contract.json
M  corpus/tools/map_obligations.py

git diff --diff-filter=D --name-only dcb2d92   # (empty — no deletions)
git diff --diff-filter=R --name-status dcb2d92 # (empty — no renames)
git diff --summary dcb2d92                     # (empty — no mode changes)
```

Against the true r96 baseline (`HEAD` `60dba0c`) the working-tree change set is
exactly `LOG.md` (the round declaration, +67 lines, not producer-owned — same
class as r95) plus the three declared producer-owned tool files. `SCORECARD.md`
appears only in the `dcb2d92` view because the r95 close commit `60dba0c`
itself touched it (`dcb2d92..HEAD` = `M SCORECARD.md`); the working tree equals
that committed blob.

Owned new (untracked) paths outside `.ufo/` — the full set:

```text
corpus/fixtures/r96-crossing-response/  (10 files)
corpus/knowledge/r96-response-scope-note.md
corpus/tools/dependency_freeze.py
corpus/tools/dependency-freeze-contract.json
```

`git status --porcelain --untracked-files=all | grep -v '^?? \.ufo/'` returns
exactly these 13 `??` rows plus the 4 ` M` rows above. Untracked files under
`.ufo/` are confined to `.ufo/waves/round-96/` (seat reports and seat scratch);
`git status --porcelain --untracked-files=all -- .ufo/ | grep -v round-96` is
empty, so the r94/r95 wave artifacts are byte-intact.

Independent second method over **all 1791 inherited `corpus/` paths** (SHA-1 of
working-tree content via `git hash-object --stdin-paths` vs the blob SHA-1 from
`git ls-tree -r dcb2d92 corpus/`):

```sh
paste <(git ls-tree -r dcb2d92 corpus/ | awk '{print $3}') \
      <(git ls-tree -r dcb2d92 corpus/ | awk '{print $4}' | git hash-object --stdin-paths) \
      <(git ls-tree -r dcb2d92 corpus/ | awk '{print $4}') | awk '$1!=$2 {print "CHANGED " $3}'
  CHANGED corpus/tools/README.md
  CHANGED corpus/tools/map-obligations-contract.json
  CHANGED corpus/tools/map_obligations.py
```

Repo-wide variant over all **8669 inherited paths**: the same three files, plus
`LOG.md`, plus `SCORECARD.md`, plus one symlink false positive (§6.1).

**Verdict:** the inherited change set is exactly the declared one — the three
tool files, plus the new fixture tree, the new knowledge note, and the two new
tool files. No other inherited path changed anywhere in the repo.

## 3. W05 pin verification — one broken pin, pre-existing (none broken by r96)

Pin file: `.ufo/waves/round-94/work/W05-baseline-corpus.sha256` (984 rows: 980
fixture files + 4 tool inputs, built at `9c2eea3`). No r96 pin file exists yet —
`find .ufo/waves/round-96 -iname '*.sha256'` returns only verifier scratch
(`V06/V09/V56` seat-local files), so the r94 W05 pin is the only authoritative
persisted content pin.

```sh
python3 .ufo/waves/round-96/seats/V24-scratch/pin_check.py
pin_rows=984 (fixture_rows=980 tool_rows=4)
ok=983 changed=1 missing=0
CHANGED corpus/fixtures/README.md
  pin a13d1af36aed025a13d433bc72d8870713fdf6b1f332874d28df72c168b75e93
  now f3733aad746f68fd2798ec1d9a72b50becf779375d272014e0e03fdbee11141c
exit=1
```

**Broken pin, named: `corpus/fixtures/README.md`** — the same row r95's V15
already reported broken, and r96 did not cause it:

| Field | Value |
|---|---|
| pin row (`9c2eea3`) | `a13d1af36aed025a13d433bc72d8870713fdf6b1f332874d28df72c168b75e93` |
| blob at `fb118c4` (r95 baseline) | `01161b047f318c24e7c5e3ab0e763a07c6c90d97566dffc84682c46659651d91` |
| blob at `dcb2d92` and at `60dba0c` | `f3733aad746f68fd2798ec1d9a72b50becf779375d272014e0e03fdbee11141c` |
| working tree now | `f3733aad746f68fd2798ec1d9a72b50becf779375d272014e0e03fdbee11141c` |

`git log --oneline -4 -- corpus/fixtures/README.md` → last writers `dcb2d92`
(r95 close), `ac69044` (r94), `4780cf0` (r93), `c4d4823` (r92). The working-tree
hash equals the `dcb2d92`/`60dba0c` blob, so r96 wrote no byte of this file;
the break is **inherited** (introduced at r94, rewritten at the r95 close, and
already named at r95 by V15). It is the only broken row among 984.

Coverage — no touched or new r96 file is pinned at all:

```sh
for n in map_obligations map-obligations-contract dependency_freeze dependency-freeze-contract; do
  grep -c "$n" .ufo/waves/round-94/work/W05-baseline-corpus.sha256; done   # → 0 0 0 0
grep -c 'corpus/tools/README.md' .ufo/waves/round-94/work/W05-baseline-corpus.sha256   # → 0
```

The pin's four tool rows (`support_check.py`, `discriminate_check.py`,
`boundary_doc_check.py`, `boundary-doc-contract.json`) all verify OK, and all
980 pinned fixture rows verify byte-for-byte except the README row above
(0 missing). **No W05 pin row is broken by any r96 inherited change** — the
touched inherited files are unpinned tools/README class, as expected.

## 4. Preservation of the new fixture (C2 byte-copy claims)

`corpus/fixtures/r96-crossing-response/` vs the `dcb2d92` blobs of
`corpus/fixtures/r95-crossing-aftermath/`, SHA-256 of `git cat-file blob` vs the
working-tree file:

```text
IDENTICAL  contradictions.json   IDENTICAL  entities.json
IDENTICAL  inspiration-note.md  IDENTICAL  relations.json
IDENTICAL  source-excerpt.md
DIFFERS    fictional-excerpts.md   (declared modified, Q4)
DIFFERS    sources.json            (declared modified, Q4)
DIFFERS    timeline.json           (declared modified, Q4)
DIFFERS    README.md               (Q5 write)
DIFFERS    claim-excerpt-map.md    (Q5 write)
```

All 10 r95 filenames are present in the new dir and no extra name exists
(`only_in_new: []`, `only_in_old: []`). The five declared byte copies are
SHA-256-identical to the r95 blobs — the same hashes Q4 reports
(`contradictions 37517e5f…`, `entities 026af0bc…`, `inspiration-note 58f5390e…`,
`relations c279254b…`, `source-excerpt b5edc2fd…`).

Prefix inheritance of the two JSON tables (parsed-value comparison, not text):

```text
sources.json:  old len=4 new len=5 prefix_equal=True
  new entry: id=evin-response-note, title="Evin's Salt Court Response Note"
timeline.json: old len=4 new len=5 prefix_equal=True
  new entry: tick=12, entity_id=evin, place_id=salt-court,
             depends_on=['aftermath-missing-evin'], source_id=evin-response-note
```

**Source fixture untouched:** all 10 files of `corpus/fixtures/r95-crossing-aftermath/`
compare SAME against their `dcb2d92` blobs (0 CHANGED), so the "preserving copy"
claim did not disturb the r95 fixture.

Structural counts recomputed from the delivered JSON: entities 5 / relations 1 /
contradictions 0 / sources 5 / timeline events 5 — matching the declared
5 entities / 1 relation / 5 events / 5 sources (r95: 4 sources).

## 5. Snapshot hashes at the delivered revision (17:53:55, stable to 17:54:40)

Changed inherited paths:

```text
2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8  corpus/tools/map_obligations.py
97b76bb8b1fea97f166ef7586eba69c427ec15bbe7b34eb5345ec65c936493b6  corpus/tools/map-obligations-contract.json
965b29cd41a8af14293eb2e1948f58f310e58c6e752b8fe322c5445b20a91f24  corpus/tools/README.md
```

New paths:

```text
a3b57978f0cbf314389ee3f9862920a46cf109fca6d1eec488c39be0457f0980  corpus/tools/dependency_freeze.py
7d568cc422cda42297b7506a1a3e083e8798866efd16d58617bf4ea468576975  corpus/tools/dependency-freeze-contract.json
6db32ca24f5eff5baa3ebe589e8d3bcb6b256fec18dee2468211d7d0fae157c6  corpus/knowledge/r96-response-scope-note.md
ff52ced48bf4214721f248328d76da64a42773d44e78154ef1eaf6eb3558c456  corpus/fixtures/r96-crossing-response/README.md
5093d72eb3f22b249033d7ac4c1a85c7df7f5e09bfa673a598aee6a83045bfd8  corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
06b11bec604f6d68e4d4bc43e78093c00ce7fb8fb86c8cac153e24ee41cb2fe3  corpus/fixtures/r96-crossing-response/fictional-excerpts.md
9f973f634cf325a33047020407ffb67b0a0f0a1643e507ebd3771abf9fabf32d  corpus/fixtures/r96-crossing-response/sources.json
ea0225f9270db79685ea6f55828c2031d7ac67cd413b04f28b25770b208815b9  corpus/fixtures/r96-crossing-response/timeline.json
```

(the five byte copies keep the r95 hashes listed in §4; full list in
`.ufo/waves/round-96/seats/V24-scratch/snap-b.sha256`.)

## 6. Observations, caveats, findings

**6.1 Symlink false positive in the repo-wide sweep (methodology, not a repo
change).** `.ufo/waves/round-94/work/W16-scratch/cluster/escape.md` is a symlink
(`→ ../outside.md`); `git hash-object` follows symlinks, while
`git status --porcelain -- <path>` is empty and `git diff --name-status dcb2d92
-- <path>` is empty. Same artifact r95's V15 reported; not an r96 change.

**6.2 Corpus file arithmetic.** `find corpus -type f` → 1808, but 4 of those are
ignored `corpus/tools/__pycache__/*.pyc`; excluding them → **1804 = 1791
inherited + 13 new**, consistent with §1/§2. The `__pycache__` dir is
`.gitignore`d (`git status --porcelain --ignored=matching -- corpus/tools/__pycache__`
→ `!! corpus/tools/__pycache__/`), so it is not part of any change set.

**6.3 `LOG.md` is the one changed inherited file outside the producer-owned set**
(+67 lines, the round declaration) — the same class r95 carried, and it is
excluded from the W05 pin's coverage.

**6.4 Snapshot bound.** This census holds for the stated window; verifier seats
and L1 integration may still write under `.ufo/` (allowed) and `LOG.md` /
`SCORECARD.md` at closure. No corpus or tool file may change without breaking
the evidence above — the hashes in §5 are the freeze point.

## 7. Bottom line

**PASS** — census 169→170 dirs (1000→1010 files, delta exactly
`r96-crossing-response`); inherited diff vs `dcb2d92` is exactly the declared
set (`map_obligations.py`, `map-obligations-contract.json`, `tools/README.md`,
plus the 13 declared new files, and `SCORECARD.md` attributable to the r95
close commit); the W05 pin's only broken row (`corpus/fixtures/README.md`) is
pre-existing and untouched by r96, so no W05 pin is broken by any inherited r96
change; the five declared byte copies are hash-identical to the r95 source and
`r95-crossing-aftermath` itself is byte-untouched.
