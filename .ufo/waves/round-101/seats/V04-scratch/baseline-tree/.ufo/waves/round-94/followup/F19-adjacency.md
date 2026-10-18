# F19 — adjacency / province discipline

**Seat:** F19 (adjacency), round-94 FOLLOW-UP wave, lane `lore-shokunin`.
**Subject:** WORK candidate `abbc3e0` (baseline `9c2eea3`, follow-up declaration `65a9329`).
**Scope of this seat:** verify that the round stayed inside lore's province — PROVINCE.md untouched, no sibling-lane paths written, mythology kept as editorial comparison only, fictional records kept lore-owned, and rights/mechanics/canon-refusal boundaries intact. This seat makes no C1/C2 verdict, no admission verdict, and no lore-truth ruling.

All commands run from the lane root `/home/vgpnk/Projects/shokunin/lore-shokunin` on 2026-10-17.

---

## A1 — PROVINCE.md byte-unchanged vs `9c2eea3`

**Claim checked:** the r94 candidate did not edit the province charter.

```
$ git rev-parse 9c2eea3:PROVINCE.md   → 7c599c395e1710b6a7c7aca6d485c373bed6deb7
$ git rev-parse abbc3e0:PROVINCE.md   → 7c599c395e1710b6a7c7aca6d485c373bed6deb7
$ git rev-parse 65a9329:PROVINCE.md   → 7c599c395e1710b6a7c7aca6d485c373bed6deb7
$ git rev-parse HEAD:PROVINCE.md      → 7c599c395e1710b6a7c7aca6d485c373bed6deb7
$ git hash-object PROVINCE.md         → 7c599c395e1710b6a7c7aca6d485c373bed6deb7   (worktree)
$ git diff 9c2eea3 abbc3e0 -- PROVINCE.md | wc -c   → 0
$ sha256sum PROVINCE.md ; git show 9c2eea3:PROVINCE.md | sha256sum
  94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa  PROVINCE.md
  94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa  -
$ wc -c PROVINCE.md → 802
```

Blob identity is unchanged at baseline, candidate, declaration, HEAD, and the working tree; the byte diff is empty and the sha256 agrees across baseline blob and worktree file. `PROVINCE.md` is absent from `git show --name-status abbc3e0` and from `git diff --name-status 9c2eea3 abbc3e0`.

**Result: PASS.**

---

## A2 — no sibling-lane paths touched by `abbc3e0`

**Claim checked:** the commit wrote only inside `lore-shokunin/` and touched no sibling lane repository.

```
$ git show --name-only --pretty=format: abbc3e0 | awk -F/ '{print $1}' | sort | uniq -c
    139 .ufo
     13 corpus
      1 SCORECARD.md
      1 LOG.md

$ git show --name-only --pretty=format: abbc3e0 | grep -v -E '^(\.ufo/|corpus/|LOG\.md$|SCORECARD\.md$)'
  (empty)

$ git show --name-only --pretty=format: abbc3e0 | grep -E 'shokunin/'
  (empty)

$ git show --shortstat --pretty=format: abbc3e0
 154 files changed, 7554 insertions(+)

$ git show --numstat --pretty=format: abbc3e0 | awk '$2>0 {print "DELETIONS:", $0}'
  (empty)

$ git show --name-status --pretty=format: abbc3e0 | grep -v '^A'
 M	LOG.md
 M	SCORECARD.md
```

No path begins with any sibling lane name (`audio-`, `kagi-`, `kama-`, `chousa-`, `kotoba-`, `mado-`, `tabi-`, `tameshi-`, `kengaku-`, `mori-`, `kumitate-`, `kaidoku-`, `kasegi-`, `revenger-`, `game-dev-*`, `tsukuroi-`, `kotodama-`), and no path contains a `../` escape. Every change is an addition except two lane-local file modifications (`LOG.md`, `SCORECARD.md`); zero deletions across all 154 files. This matches `PROVINCE.md:11` — "Only writes this standalone lane repository (`lore-shokunin/`) … Sibling repositories and domain source trees remain read-only."

Content-level check (not just filenames): scanning all 13 new `corpus/` files for any sibling-lane path string or `../<lane>` reference returned zero hits.

```
$ for f in <13 new corpus files>; do grep -n -i -E '(audio-shokunin|kagi-shokunin|…|game-dev-2d|game-dev-3d|\.\./[a-z-]+-shokunin)' "$f"; done
  (empty)
```

The declaration commit `65a9329` likewise touches only `LOG.md` and `README.md` in this lane.

**Result: PASS.**

---

## A3 — mythology remains editorial comparison only; no in-world witness

**Claim checked:** the ETCSL / Spence / Kojiki material stays a bounded editorial comparison and does not become an in-world source or canon claim inside the new fixture.

JSON-level check — every source binding in the new fixture, walked programmatically:

```
$ python3 <walk source_id/first_appearance in corpus/fixtures/r94-paired-crossing/*.json>
contradictions.json []
entities.json [('first_appearance','crossing-minute'), ('first_appearance','paired-clock'),
               ('source_id','crossing-minute'), ('source_id','paired-clock')]
relations.json [('source_id','crossing-minute')]
sources.json []
timeline.json [('source_id','crossing-minute'), ('source_id','paired-clock')]
--- declared source ids in sources.json ---
['veil-verse', 'paired-clock', 'crossing-minute']
```

No external comparator is bound as JSON support. Direct string check for mythology names inside the fixture JSON:

```
$ grep -n -i -E '(spence|etcs|kojiki|chamberlain|terebess|gutenberg|inana)' corpus/fixtures/r94-paired-crossing/*.json
  (empty)
```

All three declared sources are explicitly fictional in-world records (`sources.json`: `"kind": "fictional poem" / "fictional register" / "fictional minute"`).

Checker-level separation of the two row classes (real run, both exit 0):

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing
OBLIGATIONS raw=14 mapped=14
RESULT PASS                                    (exit 0)

$ python3 corpus/tools/support_check.py corpus/fixtures/r94-paired-crossing
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16; DISTINCT-ANCHORS 12/12
… PASS J01 … PASS J14 (mode=verbatim; anchor=found)   ← JSON facts, all bound to in-world sources
… PASS S01: editorial-row … PASS S02: editorial-row    ← Spence rows, labelled editorial
SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 2/2; MODES 16/16; VALIDATED-ROWS 16/16
RESULT PASS                                    (exit 0)

$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r94-paired-crossing
CLEAN: schema, citations, relations, timeline; 0 violations    (exit 0)
```

Explicit refusal lines (verbatim, each one a negative statement about witness/canon status):

- `corpus/fixtures/r94-paired-crossing/README.md:17` — "It supplies no in-world witness, cultural authority, or fictional canon, and asserts no cultural meaning."
- `corpus/fixtures/r94-paired-crossing/claim-excerpt-map.md:39` — "they do not make Spence an in-world witness, assign cultural meaning, or add canon."
- `corpus/fixtures/r94-paired-crossing/inspiration-note.md:21` — "It is not an in-world source and supplies no fictional canon."
- `corpus/knowledge/r94-cross-myth-design-comparison.md:7` — "An outside passage never becomes an in-world witness."
- `corpus/knowledge/r94-cross-myth-design-comparison.md:25` — "no outside text is an in-world source or witness. The three source families and their fictional namespaces remain separate."
- `corpus/knowledge/r94-cross-myth-design-comparison.md:15-17` — the cross-row limits explicitly deny merging the clusters or "add[ing] a fourth source/canon link."

**Result: PASS.**

---

## A4 — fictional records remain lore-owned

**Claim checked:** the new in-world records sit inside lore's own corpus and no foreign-owned artifact was introduced.

- `PROVINCE.md:3` — "Owns: fictional-world records — entities (characters, places, factions, items), relations, timeline events — with consistency verification and sourced inspiration." All new records are exactly these kinds and live at `corpus/fixtures/r94-paired-crossing/` inside this lane.
- All 13 new `corpus/` files are regular files, mode `100644`, none a symlink, so no content is redirected outside the lane:

```
$ git ls-files -s <13 new corpus paths> | awk '{print $1, $4}'
100644 corpus/fixtures/r94-paired-crossing/README.md
100644 corpus/fixtures/r94-paired-crossing/claim-excerpt-map.md
100644 corpus/fixtures/r94-paired-crossing/contradictions.json
100644 corpus/fixtures/r94-paired-crossing/entities.json
100644 corpus/fixtures/r94-paired-crossing/fictional-excerpts.md
100644 corpus/fixtures/r94-paired-crossing/inspiration-note.md
100644 corpus/fixtures/r94-paired-crossing/relations.json
100644 corpus/fixtures/r94-paired-crossing/source-excerpt.md
100644 corpus/fixtures/r94-paired-crossing/sources.json
100644 corpus/fixtures/r94-paired-crossing/timeline.json
100644 corpus/knowledge/r94-cross-myth-design-comparison.md
100644 corpus/tools/map-obligations-contract.json
100644 corpus/tools/map_obligations.py

$ find corpus/fixtures/r94-paired-crossing corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json corpus/knowledge/r94-cross-myth-design-comparison.md -type l
  (empty)
```

- The new fixture is an addition, not a takeover of inherited history: the earlier fixtures are byte-unchanged across the round.

```
$ git diff --stat 9c2eea3 abbc3e0 -- corpus/fixtures/r88-m3-maya-cluster corpus/fixtures/r87-myth-cluster corpus/fixtures/r93-m2-kojiki-cluster
  (empty)
```

- Parsed counts of the new fixture are 5 entities / 1 relation / 3 events (inherited r88 snapshot 4/0/2), i.e. growth by addition only.

**Result: PASS.**

---

## A5 — mechanics and rights remain refused

**Claim checked:** the round does not assert game-mechanics verification or real-world rights findings.

`PROVINCE.md:9` — "Refuses: claiming canon without an in-world citation; silently resolving contradictions; real-world rights claims (art-east-asian-design); game mechanics verification (game-dev-2d)."

Scan of all 13 new `corpus/` files for `rights|licen[cs]e|copyright|permission|canon|mechanic|gameplay|ruleset`. Every hit is a refusal, a scope limit, or the unrelated JSON-pointer sense of "canonical" — no assertion of a rights finding, no mechanics claim:

- `README.md:17,19` — rights/permission "remain unassessed; neither is granted or inferred here"; the receipt is "not … rights, permission, or canon review".
- `claim-excerpt-map.md:39,50` — "or add canon"; "not … a verdict on source authenticity, truth, rights, permission, or canon".
- `inspiration-note.md:13-19` — `## Rights question` / `## AI-training-permission question`, both stated as open: "has not been determined for all jurisdictions", "has not been assessed or established … does not imply permission for training".
- `knowledge/r94-cross-myth-design-comparison.md:7,17,25` — "not merged canon or a cultural-history claim"; "Rights and AI-training permission are not assessed by this record"; "without transferring canon".
- `map-obligations-contract.json:3` — "no entailment, fidelity, chronology, rights, permission, or canon judgment".
- `map_obligations.py:143,158,164,171,660` and `claim-excerpt-map.md:1,16` — "canonical" occurs only in the JSON-Pointer sense ("canonical inline-code pointer", "canonical JSON Pointer", "canonical decimal", "14 canonical pointers"), never world canon.

No occurrence of `mechanic`, `gameplay`, `ruleset`, `damage`, `stats`, or `balancing` in any new `corpus/` file (separate targeted grep returned no hit in all 13 files). No rights grant, and no "public domain" assertion, appears anywhere in the new corpus files.

Observed adjacent nuance, reported as found rather than smoothed: `.ufo/waves/round-94/work/W07.md:8` does mention that "Gutenberg's eBook page says public domain in the USA", but in the same sentence qualifies it — "this is not a global rights determination or AI-training permission." That is a work-wave artifact under `.ufo/` (not a corpus product file) and it does not assert a rights conclusion; the corpus-side records keep the question open as quoted above.

**Result: PASS.**

---

## A6 — observed side effect, not a province breach (reported as found)

`corpus/tools/map_obligations.py:42` defines `ROOT = Path(__file__).resolve().parents[2]` (the lane repo root), and line 604 creates its self-test scratch with `tempfile.TemporaryDirectory(prefix="map-obligations-self-test-", dir=ROOT)` — i.e. **inside the lane root, not the system temp directory**. Consequence observed live during this seat's run:

```
$ git status --porcelain
?? .ufo/waves/round-94/followup/
?? map-obligations-self-test-qe86iqrq/

$ ps -eo pid,etimes,args | grep map_obligations
694263       0 python3 corpus/tools/map_obligations.py --self-test
694279       0 /usr/bin/python3 …/map_obligations.py …/map-obligations-self-test-qe86iqrq/noncanonical_index
```

The directory was transient: an earlier one (`…-0nqa9eni`) was visible at one check and gone seconds later, and the second was created and removed by a concurrently running `--self-test` process (PID 694263). Assessment: **lane-internal and auto-cleaned, so it is not a sibling-lane or province violation** — but the scratch is visible as untracked residue in `git status` while a run is in flight, and a killed run would leave a `map-obligations-self-test-*/` directory in the lane root. Worth a bounded follow-up note (use the system temp dir, or `.ufo/` scratch) rather than a defect in this round's scope.

Related, checked and cleared: the string `"../entities.json#/0/first_appearance"` at `map_obligations.py:553` is a **self-test input case** (`case_name == "traversal_path"`) built inside that scratch directory, not a real path escape. The tool correctly rejects it:

```
$ python3 corpus/tools/map_obligations.py --self-test
SELF-TEST PASS traversal_path exit=2 findings=['unsafe_path']
SELF-TEST PASS symlink_path   exit=2 findings=['unsafe_path']
SELF-TEST PASS foreign_path   exit=2 findings=['foreign_path']
… (21 cases) …
RESULT PASS
```

Two further observations, both boundary-consistent and neither a breach:

- `corpus/knowledge/r94-cross-myth-design-comparison.md:17` retains the authoring-time prospective line "The planned r94 minute is an intended design target only until delivered and checked", which is stale after delivery. It is **explicitly and non-silently superseded** by the append-only addendum at `:19` — "This addendum overrides only the preceding prospective statements that the minute was not yet delivered or checked." PROVINCE refuses *silently* resolving contradictions; this correction is explicit and append-only, so it conforms.
- `contradictions.json` is `[]` in the new fixture, consistent with the declared intent that unchanged inherited facts are not contradictions.

---

## Bottom line

**PASS** — PROVINCE.md is byte-identical to `9c2eea3` (blob `7c599c3`, sha256 `94a7a77e…`, empty diff); `abbc3e0` writes only `.ufo/`, `corpus/`, `LOG.md`, `SCORECARD.md` with zero deletions and no sibling-lane or cross-lane path; all 14 JSON obligations bind only the fictional in-world sources `paired-clock`/`crossing-minute` while the Spence rows stay labelled editorial and every mythology reference explicitly disclaims in-world-witness status; the new records are lore-owned regular files inside this lane; and rights/mechanics remain refused with only open-question and refusal language present — the sole caveat being the tool's self-test scratch directory being created transiently in the lane root (`map_obligations.py:604`), which is lane-internal, auto-cleaned, and a follow-up note rather than a violation.
