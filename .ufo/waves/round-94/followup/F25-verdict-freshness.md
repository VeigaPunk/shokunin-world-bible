# F25 — verdict-freshness (round-94 FOLLOW-UP)

**Seat:** F25. **Role:** independent per-axis verdict for **FRESHNESS** — were the
stale-pin/README-drift findings actually **repaired** on the delivered tree, or
merely **absent**? Basis: F17's findings, each re-checked on delivered bytes.
Read-only; this file is the sole artifact written.

Read state: HEAD `65a93298cb100fdbf5732ac6de55f01a683c02d8` (WORK checkpoint
`abbc3e0`, declaration `65a9329`), working tree clean (`git status --porcelain`
empty). Finding source: `.ufo/waves/round-94/followup/F17-freshness.md`
(mtime 15:43:59, 55 lines), whose own bottom line is
"FAIL — 2 README drifts … plus a stale HEAD-bound assertion … the `corpus/README.md`
'current' index omits r94". I re-ran every check behind its findings S1–S4 plus
its fresh-pin claims F-e/F-h.

## Verdict question, answered directly

**Not repaired, and not absent.** Every F17 finding reproduces on the delivered
bytes; the offending text/omissions are still present. Nothing was deleted to
make a finding disappear: `git diff --numstat 9c2eea3..abbc3e0 | awk '$2>0'`
returns no rows (zero deleted lines in the whole checkpoint), and
`corpus/README.md`, `corpus/tools/README.md`, `corpus/fixtures/README.md`,
`SKILL.md`, `PROTOCOL.md` are byte-identical to baseline `9c2eea3`
(`git diff --quiet` per file → identical). The drift is *declared pending*
(`.ufo/waves/round-94/work-receipt.json` `checkpoint_limits`: "W25
documentation/registry proposals remain unimplemented"; `LOG.md:2688` next
required work: "minimal documentation and registry integration from W25"),
so it is honest — but for the freshness axis it is **outstanding, not closed**.

## F17 finding S1 — new tool unregistered in `corpus/tools/README.md`

Re-run on delivered bytes:

```
$ grep -c "map_obligations\|map-obligations" corpus/tools/README.md
0
$ wc -l corpus/tools/README.md
86 corpus/tools/README.md
$ grep -n "map_obligations" SKILL.md ; echo exit=$?
exit=1          (no match)
$ ls -la corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json
-rw-r--r-- 2307  corpus/tools/map-obligations-contract.json
-rw-r--r-- 28264 corpus/tools/map_obligations.py
```

The tool exists and runs (see S-repair below) but is named nowhere in the tools
README or the gate registry. **Reproduces → unrepaired.**

## F17 finding S2 — `corpus/fixtures/README.md` has no r94 entry, census one behind

```
$ grep -in "r94\|round 94" corpus/fixtures/README.md ; echo exit=$?
exit=1          (no match)
$ sed -n '1124,1128p' corpus/fixtures/README.md
B1's 166 direct fixture directories were the **pre-work baseline** at
`87779a0`; the r93 delivered snapshot has 167, with `r93-m2-kojiki-cluster`
as the single added direct fixture directory. A fresh checker sweep of the
delivered set observed 167 directories, 33 exit-0 cases, 134 expected
exit-1 cases, 421 violation lines, no stderr, and no unexpected exit (overall
$ ls -d corpus/fixtures/*/ | wc -l
168
```

Delivered count is 168 (34 clean / 134 negative per F13 census and `LOG.md:2671`),
so the README's most recent census line is one behind and the new fixture is
undocumented. The line itself is a true r93 snapshot statement and says so
("not a pinned invariant", `:1129`). **Reproduces → unrepaired.**

## F17 finding S3 — `corpus/README.md` "current" index omits r94

```
$ grep -in "r94\|map_obligations" corpus/README.md ; echo exit=$?
exit=1          (no match)
```

`corpus/README.md:12` heads "## Current navigation and coverage (2026-10-17)";
the cluster list ends at r93 (`:16-20`). The dated current index names neither
`r94-paired-crossing` nor `map_obligations.py`. **Reproduces → unrepaired.**

## F17 finding S4 — stale HEAD-bound assertion at `r91-c9-watch.md:54`

```
$ sed -n '54p' corpus/knowledge/r91-c9-watch.md
Run from `lore-shokunin/` at HEAD `396c568cbf86bba2c4b7a4ce8bd69fc38bb33d1f`. Readiness polls (both pinned artifacts were present immediately):
$ git rev-parse HEAD
65a93298cb100fdbf5732ac6de55f01a683c02d8
$ git merge-base --is-ancestor 396c568cbf86bba2c4b7a4ce8bd69fc38bb33d1f HEAD && echo ancestor
ancestor
```

`396c568` is a real, older ancestor commit, so the section's premise ("at HEAD
396c568") cannot be reproduced as written at delivered HEAD. The section's
actionable pin is fresh (`ff9fd2aa…d1421` at `:73`, matching the delivered
checker). The file does carry dated supersessions (`:213` full-hash
replacement, `:215` row-2 phrase supersession) but **none touches `:54`'s
HEAD-bound premise** — the r93 repair pattern (`.ufo/waves/round-93/recovery/R10.md:39-47`
erratum) was not applied here. **Reproduces → unrepaired.** The companion open
item (no r94 re-check row yet) is declared pending at `LOG.md:2671`.

## What *was* repaired (checked so the verdict is not blind to real repairs)

- **r93-era repair still fresh:** `SCORECARD.md:78` (capability row
  "in-world excerpt support verification") was rewritten at closure `9c2eea3`
  (`git blame` → `9c2eea3b`), replacing the stale `22/22` wording with
  `14 JSON rows + 8 editorial rows … r88-m3 → 10 + 2 … r93 Kojiki → 12 + 3`.
  Re-ran all three on delivered bytes: r87 `SOURCE-SUPPORT 14/14;
  EDITORIAL-ANCHORS 8/8; MODES 22/22`, r88 `SOURCE-SUPPORT 10/10;
  EDITORIAL-ANCHORS 2/2; MODES 12/12`, r93 `SOURCE-SUPPORT 12/12;
  EDITORIAL-ANCHORS 3/3` — all exit 0, all matching the repaired text.
- **r94's own integration repair claim is real and verifiable:** the map-header
  mismatch recorded in `LOG.md:2672` was repaired; delivered
  `python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing`
  → `OBLIGATIONS raw=14 mapped=14` / `RESULT PASS` exit 0; r93 → `raw=12
  mapped=12` PASS exit 0; `--frozen .ufo/waves/round-94/frozen/map-obligations-r93`
  → `SNAPSHOT inputs=4 digests=verified … RESULT PASS` exit 0; `--self-test` →
  `RESULT PASS` exit 0.
- **Not a "silent deletion" case:** the one superseded prose block (the r94
  knowledge doc's prospective "planned r94 minute" wording at
  `corpus/knowledge/r94-cross-myth-design-comparison.md:12,17`) is retained and
  explicitly overridden by the append-only addendum (`:19-21`, "This addendum
  overrides only the preceding prospective statements…"), matching the lane's
  refusal of silent contradiction resolution. No stale text was removed anywhere
  in the checkpoint (zero deletions).

## Carried stale items F17's list did not cover (found independently)

- **`LOG.md:2312-2314` — unrepaired since r89 era.** Records
  "r87 `SOURCE-SUPPORT 22/22; … MODES 22/22` … r88-m3 `SOURCE-SUPPORT 10/10; …
  MODES 10/10`". `git blame` → `a7c6a177` (r89); unchanged by r93 and r94.
  Delivered checker prints r87 `14/14` + `8/8` editorial and r88 `MODES 12/12`.
  This is exactly the r93-F17 finding 2 item that a "later housekeeping round"
  was supposed to close; r94 did not close it.
- **`.ufo/waves/round-94/wave-spec.json` `followup` field is stale.** Delivered
  value: `{"requested_model":"opencode-go/deepseek-v4.1-flash","requested_seats":32,"status":"not-dispatched","result":null}`
  while `LOG.md:2687` declares a 40-seat dispatched FOLLOW-UP and the
  `followup/` directory held 30 seat reports at my check. The field was accurate
  when committed at `abbc3e0`; the `65a9329` declaration superseded it without
  updating it. (Same item F18 flagged; re-verified here, not repaired.)

## Live pins re-verified fresh (no false pin on the delivered tree)

- `sha256sum corpus/fixtures/check_bible.py` → `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`,
  identical to `wave-spec.json` `expected_preservation.checker_sha256`,
  `corpus/fixtures/README.md:1091`, `r91-c9-watch.md:6,49,73` and
  `boundary-doc-contract.json`.
- Legacy baseline `88c9b1d003f51738b9fa9b2921a939f94e7ebbc2369c4445a947b282cfed9b81`
  reproduces from the declared revision: `git show 5eb9451:corpus/fixtures/check_bible.py | sha256sum`.
- Boundary document pin `7f815a9389c415de906ecd4fe14795ee30d5935ae0ed13ee0a5c6b06a74ec33e`
  equals delivered `corpus/knowledge/holder-assessment-boundary.md`;
  `git diff --stat 65838f8 -- <doc> <checker>` is empty (byte-identical to the
  pinned revision). `boundary_doc_check.py` default → `CERTIFIED …` exit 0;
  `--self-test` → `SELF-TEST PASS` exit 0.
- Frozen r93 snapshot digests match live bytes (`expected.json` `inputs`):
  `entities.json 19f75678…` MATCH, `relations.json 32b79cd4…` MATCH,
  `timeline.json 69da079e…` MATCH, `claim-excerpt-map.md 17f0e812…` MATCH.
- `discriminate_check.py` → `checker_sha256=ff9fd2aa… matches_pin=True`,
  `RESULT: DISCRIMINATION HELD` exit 0.

## Limits

Bounded to pin currency and README/index agreement against delivered bytes at
HEAD `65a9329`; I did not re-run the full 168-directory checker sweep (only the
directory count), did not audit claim semantics, and did not judge whether L1
must close these items before admission — that is L1's ruling. F17's report was
read in full (55 lines) at 15:44.

**Bottom line: FAIL — no F17 freshness finding was repaired on the delivered
tree; S1–S4 all reproduce (tool unregistered in `corpus/tools/README.md` and
`SKILL.md`; `corpus/fixtures/README.md` and `corpus/README.md` still lack r94
entries; `r91-c9-watch.md:54` still HEAD-bound to `396c568`), plus two carried
stale records (`LOG.md:2312-2314`, `wave-spec.json` `followup` field) remain
unrepaired — declared pending, never concealed, with every live byte/digest pin
verified fresh and zero deleted lines, so the freshness axis is unimproved by
r94 rather than newly harmed.**
