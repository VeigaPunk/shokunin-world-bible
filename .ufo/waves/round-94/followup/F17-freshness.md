# F17 — freshness (round-94 FOLLOW-UP)

Role: leaf freshness seat. Scope: hunt stale pins in the r94 candidate — old-HEAD assertions, stale M2 pins, README drift in `corpus/fixtures/README.md` and `corpus/tools/README.md` against delivered byte counts (expected 168 fixture dirs; new tool registered) — and verify the r94 knowledge record opens with source/verified-at/recheck metadata. Read-only; no corpus writes; no commits.

Measured state: HEAD `65a93298cb100fdbf5732ac6de55f01a683c02d8` (checkpoint `abbc3e0`, follow-up declaration `65a9329`), measured via `python3 .ufo/waves/round-93/deepseek/F14-postrepair-check.py` → `MEASURED_REVISION 65a93298cb100fdbf5732ac6de55f01a683c02d8`, `MEASURED_TREE fae200873819636358549113dcae47d054183c89`. Working tree clean.

## Stale items found

### S1 — `corpus/tools/README.md` does not register the new tool (README drift vs delivered bytes)

- `grep -c "map_obligations\|map-obligations" corpus/tools/README.md` → `0` (file is 86 lines). The README names `support_check.py` (4 mentions), `discriminate_check.py` (3), `boundary_doc_check.py` (3) and `boundary-doc-contract.json`; it names neither the new CLI nor its contract.
- Delivered bytes exist and work: `corpus/tools/map_obligations.py` (28264 bytes), `corpus/tools/map-obligations-contract.json` (2307 bytes), both added by `abbc3e0` (`git show --stat abbc3e0`). `python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing` → `OBLIGATIONS raw=14 mapped=14` / `RESULT PASS`, exit 0; same command on `corpus/fixtures/r93-m2-kojiki-cluster` → `raw=12 mapped=12` PASS.
- Same gap in the gate registry: `grep -n "map_obligations" SKILL.md` → no match; registry entries exist only for `boundary_doc_check` (SKILL.md:50), `discriminate_check` (SKILL.md:61), `support_check` (SKILL.md:72).
- Nuance: declared pending, not concealed — `.ufo/waves/round-94/work-receipt.json` `checkpoint_limits`: "W25 documentation/registry proposals remain unimplemented; the new gate has not been registered or admitted as a capability." SCORECARD.md:374 labels C2 a candidate. Still a README-vs-delivered-bytes registration gap, and it fails the seat's stated expectation that the new tool be registered.

### S2 — `corpus/fixtures/README.md` is one fixture behind and has no r94 entry

- `grep -in "r94\|round 94" corpus/fixtures/README.md` → exit 1, no match (file is 1152 lines). The new fixture is undocumented in this README: no section, no replay commands, no observed-exit receipt.
- Last census statement: `corpus/fixtures/README.md:1124-1128` — "B1's 166 direct fixture directories were the **pre-work baseline** at `87779a0`; the r93 delivered snapshot has 167 … A fresh checker sweep of the delivered set observed 167 directories, 33 exit-0 cases, 134 expected exit-1 cases, 421 violation lines".
- Delivered count is 168: `ls -d corpus/fixtures/*/ | wc -l` → `168` (0 matches for `__pycache__`), corroborated by the lane's own LOG.md:2671 — "A full repo-relative corpus run has 168 fixture directories, 34 clean, 134 intentional negative, 421 violation lines; the new fixture is the only addition".
- Nuance: `corpus/fixtures/README.md:1129` itself says these are "snapshot counts, not a pinned invariant for future fixture additions", and the 167 figure is accurate as an r93 statement. This is index/coverage drift (delivered r94 fixture absent; most recent count one behind), not a false historical claim.

### S3 — `corpus/README.md` navigation index omits r94 (same class, secondary)

- `corpus/README.md:12` heads "## Current navigation and coverage (2026-10-17)"; the myth-cluster list ends at `fixtures/r93-m2-kojiki-cluster/README.md` (`corpus/README.md:16-20`). `grep -in "r94\|map_obligations" corpus/README.md` → no match, so neither `r94-paired-crossing` nor `map_obligations.py` is reachable from the dated "current" index.

### S4 — `corpus/knowledge/r91-c9-watch.md:54` carries a stale HEAD-bound assertion

- Line 54: "Run from `lore-shokunin/` at HEAD `396c568cbf86bba2c4b7a4ce8bd69fc38bb33d1f`." Current HEAD is `65a93298…`, so the documented replay premise no longer holds and the section cannot be reproduced as written at the stated revision.
- Its actionable pin is still fresh: `sha256sum corpus/fixtures/check_bible.py` → `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`, identical to the hash printed in the same section (`r91-c9-watch.md:73`) and to `wave-spec.json` `expected_preservation.checker_sha256`.
- This is exactly the pattern r93 already classified as a finding and repaired for R10: `.ufo/waves/round-93/recovery/R10.md:39-47` erratum supersedes the historical HEAD-bound command with the content-pinned F14 replay ("contains no expected-HEAD assertion"), and SCORECARD.md:349 records "The R10 old-HEAD assertion and stale M2 pin were actual findings, repaired before admission". `r91-c9-watch.md:54` has no such dated erratum.
- Related open item, not a false claim: `r91-c9-watch.md:50` "Next re-check: r94" and `:219` "The next re-check is due in r94"; the check log (`:47-50`) has two rows and no r94 row. Declared pending in LOG.md:2671 — "W21 records the due r94 C9 checks; the watch record's final append is still pending."

## Fresh items verified (no stale pin found)

- **F-a — r94 knowledge metadata present.** `corpus/knowledge/r94-cross-myth-design-comparison.md:1` `source:`, `:2` `verified-at: 2026-10-17 …`, `:3` `recheck: …`, before the title at `:5`, matching wave-spec.md:35 "Knowledge opens with source/verified-at/recheck metadata". `grep -c "HEAD"` in that file → `0`.
- **F-b — cited source paths all exist.** Expanded the 20 paths in the `source:` line (five fixture/knowledge groups incl. `.ufo/waves/round-93/recovery/{R25.md,R26.md}`) → `cited paths: 20 missing: NONE`.
- **F-c — r94 knowledge JSON pointers resolve at delivered bytes.** `entities.json#/4` → `chalk-stair` (5 entities, `entities[4].claims` len 1); `relations.json#/0` → `aru→evin agreed_co_stewardship_for_this_crossing` (1 relation); `timeline.json#/2` → `paired-crossing-decision` tick 10, `depends_on ['aru-ninth-bell','evin-ninth-bell']` (3 events); `sources.json#/2` → `crossing-minute`. Counts 5/1/3 as declared.
- **F-d — r94 receipt claims reproduce at current bytes.** `python3 corpus/fixtures/check_bible.py corpus/fixtures/r94-paired-crossing` → `CLEAN: schema, citations, relations, timeline; 0 violations`, exit 0. `python3 corpus/tools/support_check.py corpus/fixtures/r94-paired-crossing` → `JSON-FACTS 14; EDITORIAL-ROWS 2; TOTAL-ROWS 16`, `SOURCE-SUPPORT 14/14 … MODES 16/16; VALIDATED-ROWS 16/16`, `RESULT PASS` — matching `r94-cross-myth-design-comparison.md:27,29`.
- **F-e — no stale M2 pin.** The r93 stale M2 pin (R10 recorded `599d2507…` vs post-repair `72e4b2b8…`) is covered by the dated erratum `.ufo/waves/round-93/recovery/R10.md:39-47`, and the content-pinned replay re-ran clean at current HEAD: `python3 .ufo/waves/round-93/deepseek/F14-postrepair-check.py` → `RESULT ALL CHECKS HELD`, `checks_failed=0`, exit 0, with its INFO line documenting the supersession. The r94 frozen snapshot pins are live: `.ufo/waves/round-94/frozen/map-obligations-r93/expected.json:4-7` digests equal the current `corpus/fixtures/r93-m2-kojiki-cluster/{entities,relations,timeline}.json` and `claim-excerpt-map.md` byte-for-byte (`sha256sum` all four match).
- **F-f — no HEAD/revision pins in new r94 files.** `grep -rn "HEAD\|9c2eea3\|abbc3e0\|65a9329\|revision"` over `corpus/fixtures/r94-paired-crossing/`, `corpus/tools/map_obligations.py`, `corpus/tools/map-obligations-contract.json`, `corpus/knowledge/r94-cross-myth-design-comparison.md` → no matches.
- **F-g — existing README receipt claims are fresh.** r87 `14/14` + `8/8` (22 rows), r88-m3 `10/10` + `2/2` (12 rows), r93 `12/12` + `3/3` (15 rows), all `RESULT PASS` exit 0, matching `corpus/fixtures/README.md:1117-1122,1145-1148`.
- **F-h — checker byte pin matches every record.** `sha256sum corpus/fixtures/check_bible.py` → `ff9fd2aa…d1421`, identical in wave-spec.json, `r91-c9-watch.md:73`, `corpus/fixtures/README.md:1091`.
- **F-i — receipt inventory claim matches disk.** `.ufo/waves/round-94/work-receipt.json` `standalone_seat_reports: 31`; `ls .ufo/waves/round-94/work/W*.md | wc -l` → `31`, and 0 files match `^W20` — the W20 failed-output gap is recorded, not smoothed.

## Observations (not stale pins)

- `corpus/fixtures/r94-paired-crossing/README.md:21-26` gives replay commands without recorded observed exits, unlike the r93 pattern (`corpus/fixtures/README.md:1117-1122`); the exits live in the knowledge doc (F-d). Author-side receipts only.
- `r93-r8-worked-example.md`, `r91-c9-watch.md`, and `r89-cross-cluster-contradiction.md` open with `#` titles and carry no `source:`/`verified-at:`/`recheck:` header; only the r94 record does. The wave spec requires the header for the r94 record only, so this is context, not an r94 regression.

## Limits

This seat checked pin currency and README/index agreement against delivered bytes at HEAD `65a9329`; it did not review claim semantics, source authentication, or the correctness of the census sweep itself. The S2 count was measured by directory listing and corroborated by LOG.md:2671, not by re-running the full 168-directory checker sweep.

**Bottom line: FAIL — 2 README drifts (new tool unregistered in `corpus/tools/README.md`; `corpus/fixtures/README.md` still at the r93 167-dir census with no r94 entry) plus a stale HEAD-bound assertion at `corpus/knowledge/r91-c9-watch.md:54`, and the `corpus/README.md` "current" index omits r94; all content, digest, receipt, and knowledge-metadata pins themselves are fresh and reproduce at `65a9329`.**
