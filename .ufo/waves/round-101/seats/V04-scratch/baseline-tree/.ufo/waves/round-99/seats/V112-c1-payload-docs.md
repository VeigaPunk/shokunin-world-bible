# V112 — c1-payload-docs-consistency (round 99)

**Seat:** V112 (c1-payload-docs-consistency), round-99 single wave, lane `lore-shokunin`.
**Subject:** whether three surfaces agree on payload (ten files), case count (18), and chain (six): `corpus/tools/README.md`, the `SKILL.md` dependency-freeze row, and the contract `precedence` text.
**Not this seat:** no C1 admit/deny, no self-test replay, no pin-byte audit, no prose-tamper demo. Read-only except this report and `.ufo/waves/round-99/seats/V112-scratch/`. No commits, no pushes, no network, no nested agents.
**Baseline:** r98 closure `4265df5`. Declaration read from `LOG.md` (standing r99 declaration, unchanged).

## Poll-wait

Required before scoring: S1 report (`seats/S1*.md`, contract owner), S2 report (`seats/S2*.md`, README + SKILL freeze-row owner), and a git diff vs `4265df5` on all three surfaces. Cadence 20 s, 40 tries. Script: `.ufo/waves/round-99/seats/V112-scratch/poll.sh`. Log: `.ufo/waves/round-99/seats/V112-scratch/poll.log`.

```
TRY 1  2026-10-18T01:04:40Z  S1=[] S2=[] README_DIFF=[] SKILL_DIFF=[] CONTRACT_DIFF=29 lines
TRY 14 2026-10-18T01:09:00Z  S1=[] S2=[] README_DIFF=[] SKILL_DIFF=[] CONTRACT_DIFF=163 lines
TRY 40 2026-10-18T01:17:41Z  S1=[] S2=[] README_DIFF=[] SKILL_DIFF=[] CONTRACT_DIFF=163 lines
TIMEOUT 2026-10-18T01:18:01Z
```

`grep -c '^TRY ' .ufo/waves/round-99/seats/V112-scratch/poll.log` → `40`. Exit code of the poll process: 2. No all-reports poll was run (SELF subtraction not triggered). The 40-try cap is the bounded stall-escape; it is recorded, not extended.

Post-window recheck at `2026-10-18T01:32:53Z` (not an extra try): `ls .ufo/waves/round-99/seats/S1*.md` and `S2*.md` both `No such file or directory`. `S1-scratch/` holds only `before/`; `S2-scratch/` is empty (mtime `2026-10-17 22:00`). Present producer reports at that instant: `S3-fixture-author.md`, `S4-fixture-docs.md` only.

## Identity of the three surfaces

Lane root `/home/vgpnk/Projects/shokunin/lore-shokunin`, recheck `2026-10-18T01:30:38Z`:

```
$ python3 identity vs git show 4265df5:<path>
corpus/tools/README.md
  live 294dd56f29ce1fd40be3a80d365b33724c9cd1969d3f7b7abb271fd1adaaa207
  base 294dd56f29ce1fd40be3a80d365b33724c9cd1969d3f7b7abb271fd1adaaa207
  same True  bytes 32577
SKILL.md
  live 22ffaa822ec7614fa85322f7fa07e6f369c0888e1107f9f297f76a14e18c20c5
  base 22ffaa822ec7614fa85322f7fa07e6f369c0888e1107f9f297f76a14e18c20c5
  same True  bytes 16802
corpus/tools/dependency-freeze-contract.json
  live 8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628
  base 153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947
  same False bytes 25987
```

```
$ git diff --stat 4265df5 -- corpus/tools/README.md SKILL.md corpus/tools/dependency-freeze-contract.json
 corpus/tools/dependency-freeze-contract.json | 163 ++++++++++++++++++++++++---
 1 file changed, 146 insertions(+), 17 deletions(-)
```

```
$ rg -n -e 'Round-99|round 99|18 cases|ten declared|markdown_tamper|payload_schema' corpus/tools/README.md SKILL.md
(no matches)
```

README and SKILL.md are the r98 closure bytes. There is no round-99 addendum and no updated freeze row. Those two r99 surfaces did not land. The quotes below are the on-disk bytes, not an r99 delivery. They are not scored as a disagreement verdict.

## Surface 1 — `corpus/tools/README.md` (unchanged vs `4265df5`)

File ends at line 288. Last heading is the round-98 closure correction. Operative freeze sentences:

`corpus/tools/README.md:236-238`:

> Superseded 2026-10-17 (round 98): the persisted self-test carries 17 cases, and the chain is six fixtures verifying 6/6 clean.
> Superseded 2026-10-17 (round 98): 17 persisted cases, and `r97-crossing-acknowledgment` and `r98-clerk-filing` are now pinned, so the declared chain is six fixtures.
> The rest of that supersession still stands: the pin payload covers the five JSON tables only (fixture Markdown is still not pinned) and BR-01's markdown/prose half remains open.

`corpus/tools/README.md:272-279`:

> #### Contract `precedence` text and the 17th case
> The persisted self-test carries 17 cases: the 16 inherited cases … plus `self_test_mismatch` …
> `python3 corpus/tools/dependency_freeze.py --self-test   # SELF-TEST 17/17 / RESULT PASS, exit 0`

`corpus/tools/README.md:261` heading: `Chain extended to six fixtures`. The chain list at `:264-265` is the six names `r88-m3-maya-cluster`, `r94-paired-crossing`, `r95-crossing-aftermath`, `r96-crossing-response`, `r97-crossing-acknowledgment`, `r98-clerk-filing`.

On this surface, as bytes: payload = five JSON tables; case count = 17; chain = six. No ten-file payload. No 18.

## Surface 2 — `SKILL.md` freeze row (unchanged vs `4265df5`)

`SKILL.md:96`:

> frozen chain: r88-m3-maya-cluster, r94-paired-crossing, r95-crossing-aftermath, r96-crossing-response, r97-crossing-acknowledgment, r98-clerk-filing

`SKILL.md:98`:

> 17 cases (r97 added `SCOPE-REFUSED`, `PATH-MISMATCH`; r98 added `self_test_mismatch`)

`SKILL.md:99`:

> content SHA-256 over the five JSON tables; exactly the six chain fixtures

`SKILL.md:100`:

> over the five JSON tables per fixture. … Bounds: the pin payload covers the JSON tables only — fixture Markdown (maps, excerpts) is not pinned; BR-01's markdown/prose half remains open.

On this surface, as bytes: payload = five JSON tables; case count = 17; chain = six (six names listed). No ten-file payload. No 18.

## Surface 3 — contract `precedence` (landed; S1 report still absent)

`corpus/tools/dependency-freeze-contract.json:6`, sha256 `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628`, stable from the try-14 growth (`2026-10-17 22:08:46 -0300`) through the `01:32:53Z` recheck. Verbatim `precedence` value:

> semantic inventory findings decide first (exit 1: REDUCTION-DETECTED, ADDITION-DETECTED, ENDPOINT-CHANGE); a content digest change the semantic inventory does not model exits 2 (DIGEST-MISMATCH) and names each changed pinned file, including the five Markdown files. Exit-2 (could-not-evaluate) checks run in this order and the first failing check decides: UNPINNED-FIXTURE (no pin for the fixture name) or CONTRACT-INVALID (unreadable contract, invalid pin, payload_schema_version other than 2, or a pin that does not digest all ten pinned files), FIXTURE-MISSING (fixture directory absent), PATH-MISMATCH (invoked path differs from the pin's recorded path), FILE-MISSING / MALFORMED-JSON / MALFORMED-MODEL (model build of the JSON tables), DIGEST-MISMATCH (inventory clean, any pinned-file bytes changed or missing), INVALID-ARGUMENTS (CLI usage), SELF-TEST-MISMATCH (--self-test observed outcome differs from the persisted case expectation); --freeze additionally raises SCOPE-REFUSED (target outside corpus/fixtures/**, or a same-named in-scope target that would rewrite an existing pin's recorded path) and FILE-MISSING when a declared pinned file is absent. A path-less legacy pin is migrated in place by --freeze instead of refused. Re-freeze is the payload upgrade path from a schema-1 JSON-only pin to payload_schema_version 2.

String checks on that field alone (`2026-10-18T01:30:38Z`): `PREC_HAS_ten True`, `PREC_HAS_18 False`, `PREC_HAS_six False`, length 1335. The precedence field names a ten-file payload (`all ten pinned files`, `five Markdown files`). It does not name case count 18. It does not name a chain of six.

Adjacent contract fields, not the precedence text, do state the other two numbers. Quoted so they are not confused with the precedence field. `scope` (`:5`):

> each pin (payload_schema_version 2) covers all ten declared files — five JSON tables plus README.md, claim-excerpt-map.md, fictional-excerpts.md, inspiration-note.md, and source-excerpt.md

`provenance_note` r99 clause (`:689`):

> r99 (S1 full-file pins): payload_schema_version 2 extends each pin from the five JSON tables to all ten declared files (README.md, claim-excerpt-map.md, fictional-excerpts.md, inspiration-note.md, source-excerpt.md added); schema_version 1 -> 2; the six chain fixtures were re-frozen through the guarded --freeze (payload upgrade; r88's extra symbolism-clause-map.md stays outside the declared ten); self-test grew 17->18 with markdown_tamper … BR-01's prose half is edit-detectable, not semantics-provable.

Same parse: `schema_version` 2, `payload_schema_version` 2, `pinned_files` length 10, `self_test.expected` length 18 (includes `markdown_tamper`), `pins` length 6, each pin `files` length 10 and `payload_schema_version` 2. Those counts are contract structure, not the three doc surfaces.

## Agreement

Not scored. Two of the three surfaces (README, SKILL freeze row) are the r98 baseline, byte-identical to `4265df5`. S2's report never appeared. Scoring those sentences as an r99 disagreement would be verifying a plan that was not delivered.

Observed, unscored, so a later reader does not have to re-read the quotes: if the baseline bytes were treated as the delivery, they would not agree with the landed precedence field. README and SKILL say five JSON tables, 17 cases, and six fixtures. Precedence says ten pinned files, and is silent on 18 and on six. README and SKILL agree with each other (both r98). Neither agrees with precedence on payload.

## Bottom line

ABSENT — S1 and S2 producer reports never landed in 40×20s polls (TIMEOUT 2026-10-18T01:18:01Z; still absent at 2026-10-18T01:32:53Z), and README plus the SKILL.md freeze row are still the r98 baseline, so the three-surface agreement was not verifiable.
