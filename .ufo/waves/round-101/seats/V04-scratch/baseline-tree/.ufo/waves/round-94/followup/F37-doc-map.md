# F37 — doc-map consistency (round 94 FOLLOW-UP)

Seat: F37 doc-map-consistency. Scope: documentation parity for the r94 WORK candidate (`abbc3e0`, parent `9c2eea3`) — (a) `corpus/fixtures/r94-paired-crossing/README.md` vs the delivered fixture and its `claim-excerpt-map.md`; (b) `corpus/fixtures/README.md` fixture-count claims vs the delivered 168; (c) stale claims inherited from prior-round README text. All commands run from `/home/vgpnk/Projects/shokunin/lore-shokunin`. No corpus file was modified; no commits.

## 1. r94 fixture README — claims vs delivered artifact

**1a. Inheritance claim (README:3) — TRUE.**
`README.md:3` claims "The four inherited entity records and two tick-9 events are copied by JSON value". Observed (`python3 -c` comparing parsed JSON):

```
r88 entities: 4  r94 entities: 5
r88[:4]==r94[:4]: True
r88 events: 2  r94 events: 3
r88 events==r94[:2]: True
r88 sources: ['veil-verse', 'paired-clock']
r94 sources: ['veil-verse', 'paired-clock', 'crossing-minute']
r94 first len(a) rows == r88 sources: True
```

`diff` of inherited prose is append-only: `fictional-excerpts.md` differs only by added lines 14–20 (the new minute); `source-excerpt.md` and `inspiration-note.md` are byte-identical (diff exit 0); `contradictions.json` identical (`[]`). The README's "source IDs, paired-clock excerpt wording, Spence excerpt, and inspiration context are retained" holds.

**1b. Count claim (README:3) — TRUE.** "counts 5 entities / 1 relation / 3 events": parsed counts are 5 entities (`entities.json`), 1 relation (`relations.json`), 3 events (`timeline.json`), matching the spec's 4/0/2→5/1/3.

**1c. 14-obligation inventory (README:19) — TRUE and tool-confirmed.**
`README.md:19`: "`claim-excerpt-map.md` has 14 source-attributed JSON pointer obligations and separately labeled editorial comparisons."
`claim-excerpt-map.md:3,5` declare "14 source-attributed JSON obligations (five first-appearance pointers, five entity claims, one relation, and three timeline events)" and "Expected inventory: 14 JSON facts; 2 editorial rows; 16 total mapped rows; 12 distinct excerpt anchors." The 5+5+1+3 breakdown matches the JSON: 5 entities each with 1 claim, 1 relation, 3 events = 14. Replay of the README's own commands (README:23–26):

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r94-paired-crossing
CLEAN: schema, citations, relations, timeline; 0 violations      (exit 0)

$ python3 corpus/tools/support_check.py corpus/fixtures/r94-paired-crossing
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16; DISTINCT-ANCHORS 12/12
SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 2/2; MODES 16/16; VALIDATED-ROWS 16/16
RESULT PASS                                                      (exit 0)
```

All 14 J-rows and both S-rows PASS with in-span anchors; no FAIL rows. So the map's declared 14/2/16/12 inventory is the tool's measured inventory.

**1d. "R9 modes" — NOT STATED in the README (not misstated).**
`grep -n "R9\|mode\|168\|167" corpus/fixtures/r94-paired-crossing/README.md` returned no matches (exit 1, empty output). The README contains no R9/mode sentence at all. Delivery modes are stated only in `claim-excerpt-map.md:7-12` (declarations table, both rows `verbatim`) and per-row; the tool reports `MODES 16/16`. So the seat's expectation that the README states R9 modes is unmet, but nothing stated is false — parity on modes is delegated to the map.

**1e. "Map row counts" — PARTIAL.** The README states the 14 JSON obligations and "separately labeled editorial comparisons" but does not state the 2 editorial / 16 total / 12-anchor counts; those are stated at `claim-excerpt-map.md:5` and confirmed by the tool. No contradiction between the two documents.

**1f. Sources statement — accurate but not exhaustive.** The README names `paired-clock` (README:7,11), `crossing-minute` (README:13), and the Spence comparison (README:17). It does not name `veil-verse` (`sources.json#/0`, retained inherited verse). No README sentence claims to enumerate all sources, and no r94 JSON fact cites `veil-verse`. Secondary observation: the r88 map declared the verse in its R9 declarations table (`corpus/fixtures/r88-m3-maya-cluster/claim-excerpt-map.md:13`: ``| `fictional-excerpts.md:7–8` | `veil-verse` | `verbatim` | Newly authored fictional verse; no JSON fact points to this source. |``), while the r94 map's declarations table (`claim-excerpt-map.md:9-12`) declares only the register+minute (`fictional-excerpts.md:12-20`) and Spence rows — the retained verse at `fictional-excerpts.md:7-8` is now undeclared. This is an inherited-declaration omission, not a false claim: `support_check.py` passes (exit 0) and the map's scope is "all 14 source-attributed JSON obligations", which exclude the verse. Flagged for the parent, not scored as a doc-map contradiction.

**1g. Other README factual claims spot-checked — all TRUE.** "event `entity_id` is Aru ... description and excerpt name both participants" (README:9) vs `timeline.json#/2` (`entity_id: "aru"`, description names Aru and Evin); "explicitly dependent on both named tick-9 entries" (README:9) vs `depends_on: ["aru-ninth-bell","evin-ninth-bell"]`; "relation records only ... agreement" (README:9) vs `relations.json#/0` type `agreed_co_stewardship_for_this_crossing`; "inherited empty `depends_on` arrays" (README:11) vs `timeline.json#/0,1` `[]`; "inherited r88 verse already uses 'chalk stair'" (README:13) vs byte-identical `fictional-excerpts.md:7`.

## 2. `corpus/fixtures/README.md` fixture-count claims vs delivered 168 — FAIL as stated

**Delivered count measured = 168 direct fixture directories:**

```
$ find corpus/fixtures -mindepth 1 -maxdepth 1 -type d | wc -l
168
$ git ls-tree 9c2eea3:corpus/fixtures -d --name-only | wc -l ; git ls-tree abbc3e0:corpus/fixtures -d --name-only | wc -l ; git ls-tree HEAD:corpus/fixtures -d --name-only | wc -l
167 / 168 / 168
```

All 168 dirs contain at least one of the five bible JSON files; `r94-paired-crossing` is the 168th and the sole addition at `abbc3e0`. A sibling FOLLOW-UP census artifact independently records the same number (`F13-scratch/census-tuples.json:3` `"delivered_dirs": 168`; `census-bytes.json:176-177` `top_level_dirs_head_count/disk_count: 168`).

**The README does not contain this count.** `grep -w 168 corpus/fixtures/README.md` → no match. Its newest fixture-count statements (`corpus/fixtures/README.md:1124-1131`) are:

- `:1124-1126` — "B1's 166 direct fixture directories were the **pre-work baseline** at `87779a0`; the r93 delivered snapshot has 167, with `r93-m2-kojiki-cluster` as the single added direct fixture directory."
- `:1127-1131` — "A fresh checker sweep of the delivered set observed 167 directories, 33 exit-0 cases, 134 expected exit-1 cases, 421 violation lines ... These are snapshot counts, not a pinned invariant for future fixture additions."

No README statement is factually false — 167 was true for r93 and the paragraph explicitly scopes itself as a snapshot, not a pinned invariant. The failure is one of currency/completeness, not correctness: **the README carries no r94/168 update**, so the claimed parity with the delivered 168 is unmet. The README was last modified at `4780cf0` (r93): `git log --oneline -3 -- corpus/fixtures/README.md` → `4780cf0 lore r93: correct dossier verification and freeze bounded document checks` (then r92, r90). `git show --stat abbc3e0 -- corpus/` lists only the ten `r94-paired-crossing/` files, `corpus/knowledge/r94-cross-myth-design-comparison.md`, and the two `map_obligations` files — no README changes.

**The round itself planned those appends and they did not land.** WORK seat W25 proposed, in order:

- `W25.md:17` — append the `fixtures/r94-paired-crossing/README.md` entry to `corpus/README.md` (the corpus index).
- `W25.md:27` — "append a Round 94 subsection to `corpus/fixtures/README.md`".
- `W25.md:38` — append a Round 94 addendum to `corpus/tools/README.md`.

Observed: `grep -c "r94" corpus/README.md` → `0`; `corpus/fixtures/README.md` has no r94/Round 94 section (`grep -n "r94\|Round 94"` → no matches); `corpus/tools/README.md`'s last touch is `8e5a68d` (r93 review). So none of the three proposed documentation appends is present at HEAD. (W04:11 shows the wave was aware of the README's historical scoping and treated `:1124-1131` as the r93 record — consistent with, but not an execution of, W25's proposals.)

## 3. Stale claims inherited from prior-round README text — none found in the r94 README

- Verbatim-line scan of `r94-paired-crossing/README.md` against all other `corpus/fixtures/*/README.md`: the only shared line is the boilerplate "Replay from the repository root:" (shared with r87-myth-cluster, r87-probe-entry-shape, r87-probe-record-and-chain, r88-m3-maya-cluster, r89-inspiration-paraphrase, r93-m2-kojiki-cluster). No prior-round claim text was copied.
- Every backticked file reference in the r94 README resolves: `claim-excerpt-map.md` → `corpus/fixtures/r94-paired-crossing/claim-excerpt-map.md` OK; `support_check.py` → `corpus/tools/support_check.py` OK; `timeline.json` → fixture-local OK. No MISS rows.
- The r94 README does not reference files that exist only in r88 (`symbolism-clause-map.md` is not mentioned), so the deliberate non-copy of that file is not misrepresented.
- Adjacent: `corpus/knowledge/r94-cross-myth-design-comparison.md` carries a dated WORK-integration addendum (`:19-39`) that explicitly supersedes its own prospective "planned r94 minute" sentences (`:12`, `:17`), and its two receipts reproduce exactly (check_bible CLEAN exit 0; support_check PASS exit 0 with `14/14, 2/2, 16/16, 12/12, 16/16, 16/16`). Its metadata `source:` header (`:1`) does not list the `r94-paired-crossing/` files that the addendum later cites, and `corpus/README.md` does not list this knowledge record — minor navigation gaps, not claims.

## Bottom line

**FAIL (bounded)** — the r94 fixture's own README is accurate and reproducible on every claim it makes (inheritance, 5/1/3 counts, 14-obligation inventory; both replay commands reproduce exit 0), and no stale prior-round text was inherited; but `corpus/fixtures/README.md` has no r94/168 update (last count 167, scoped to the r93 snapshot; last touched at r93 `4780cf0`), so its fixture-count documentation does not match the measured delivered 168 — and the r94 appends W25 proposed for `corpus/README.md`, `corpus/fixtures/README.md`, and `corpus/tools/README.md` are absent at HEAD.
