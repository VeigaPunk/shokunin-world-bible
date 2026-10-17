# V28 — freshness (round 96)

Seat: V28 freshness. Brief: *after producers* — stale-pin sweep of new bytes (no HEAD pins;
knowledge note metadata header; README commands replayable; r95 README wording carried into r96
stays accurate with updated counts). Leaf seat: no nested agents, no commits, no network. Only
write: this report; scratch under `.ufo/waves/round-96/seats/V28-scratch/`. All commands ran
from the lane root `/home/vgpnk/Projects/shokunin/lore-shokunin`. I did not verify C1/C2/C3
semantics (other seats' scope); this report covers freshness only.

**Poll-wait:** producers were polled (20 s cadence) from 17:38; all six producer reports
(`Q1-tool-hardening.md`, `Q2-contract-docs.md`, `Q3-dependency-freeze.md`, `Q4-fixture-json.md`,
`Q5-fixture-docs.md`, `Q6-knowledge-note.md`) were present by 17:52:22; no verification ran
against a plan. One poll task timed out on its 600 s background cap and was replaced; no
producer bytes were skipped.

## Frozen snapshot verified (16 new/modified bytes)

| byte | sha256 (12-hex prefix shown) | mtime |
|---|---|---|
| `corpus/tools/map_obligations.py` | `2b0ba815326b` | 17:47:24 |
| `corpus/tools/map-obligations-contract.json` | `97b76bb8b1fe` | 17:50:17 |
| `corpus/tools/README.md` | `965b29cd41a8` | 17:51:26 |
| `corpus/tools/dependency_freeze.py` | `a3b57978f0cb` | 17:44:37 |
| `corpus/tools/dependency-freeze-contract.json` | `7d568cc422cd` | 17:44:27 |
| `corpus/knowledge/r96-response-scope-note.md` | `6db32ca24f5e` | 17:47:02 |
| `corpus/fixtures/r96-crossing-response/README.md` | `ff52ced48bf4` | (Q5 report) |
| `corpus/fixtures/r96-crossing-response/claim-excerpt-map.md` | `5093d72eb3f2` | (Q5 report) |
| `corpus/fixtures/r96-crossing-response/fictional-excerpts.md` | `06b11bec604f` | (Q4 report) |
| `corpus/fixtures/r96-crossing-response/sources.json` | `9f973f634cf3` | (Q4 report) |
| `corpus/fixtures/r96-crossing-response/timeline.json` | `ea0225f9270d` | (Q4 report) |
| `entities.json` / `relations.json` / `contradictions.json` / `inspiration-note.md` / `source-excerpt.md` | `026af0bc…`, `c279254b…`, `37517e5f…`, `58f5390e…`, `b5edc2fd…` | byte copies of r95 (Q4 report) |

All six tool/note shas above match the shas quoted in the producer reports
(`sha256sum` vs `grep -oE '[0-9a-f]{64}'` on Q1/Q2/Q3/Q5 reports — exact matches). Snapshot
re-checked immediately before this report: unchanged.

## Check 1 — stale-pin sweep of new bytes (no HEAD pins): PASS

Sweep over all 16 bytes above:

```sh
for f in <the 16 files>; do grep -nE '\bHEAD\b|rev-parse|latest revision|current revision' "$f"; done
```

Observed: exactly one hit, a runtime call, not a stored pin:

```
corpus/tools/dependency_freeze.py:292:  result = subprocess.run(["git", "rev-parse", "HEAD"], ...)
```

`--freeze` runs this at freeze time and writes the resulting **fixed** sha into pin metadata
(`revision` fields = `60dba0c2aa344860b10a2fc63e00468d1b134f27`, the r95-closure SCORECARD
commit; resolvable, not HEAD-relative). `compare()` (`dependency_freeze.py:169-211`) reads
`events`/`relations` only; the digest check uses `content_sha256` — the `revision` label is not
used by verification. No delivered byte contains a live HEAD reference or a dangling pin.

Every revision pin quoted in new bytes resolves:

```sh
git show dcb2d92:corpus/tools/map_obligations.py | sha256sum        # d1c239ccb214…  (note's 17:43 revision)
git show dcb2d92:corpus/tools/map-obligations-contract.json | sha256sum  # 8173bb97592a…  (note's "r95 contract")
sha256sum corpus/fixtures/check_bible.py corpus/tools/support_check.py   # ff9fd2aa6811… / 55a5eb275390…
```

`6634e1768f1f…` (quoted in the note/report as the 17:46 re-run revision) is an in-flight
intermediate and is labeled as such. The r95 note's known debt pattern (a pin for a revision
that was never delivered) is not repeated with a false pin: every sha the r96 note names was
the true revision at its stated time (verified by mtime history and git).

## Check 2 — knowledge note metadata header: PASS

`corpus/knowledge/r96-response-scope-note.md:1-3` carries the r95 header format:
`source:` (cited-path list), `verified-at: 2026-10-17 …`, `recheck: …` — same shape as
`r95-aftermath-scope-note.md:1-3`. Spot-checked citations all resolve:

```sh
ls -d corpus/fixtures/*/ | wc -l            # 170 (note:57; 169 at r95 closure)
sed -n '27p;30p' corpus/fixtures/r96-crossing-response/sources.json   # evin-response-note id / reliability_note
sed -n '44p' corpus/fixtures/r96-crossing-response/timeline.json      # response-evin-salt-court id
sed -n '761p' corpus/fixtures/README.md     # "…the accounts conflict as **reports**. Neither wins."
python3 -c "import json; print(json.load(open('corpus/fixtures/r35-bell7-conflict/contradictions.json'))[0]['id'])"
# bell7-location-reports
```

`fictional-excerpts.md:33-42` with quoted lines 37-40 matches the delivered excerpt; the
`corpus/fixtures/README.md` Round 35 section exists at `:746` (Round 95 at `:1177`); decision
table `:226-230` exists. The note was updated at 17:47:02 (after my first read at 17:47:0x) to
record both receipt revisions — final bytes record the 17:46 in-flight revision honestly
("the r96 C1 hardening in flight; `--self-test` at that revision printed 22 case lines") plus
the 17:43 run at `d1c239cc…` with identical results, and instruct a re-run against the
delivered revision. My re-run confirms the quoted receipt values under the delivered revision
(`2b0ba815…`): identical `OBLIGATIONS raw=16 mapped=16` / `INVENTORY 16/16; 2/2; 18/18` /
`RESULT PASS` exit 0.

## Check 3 — README commands replayable: PASS

**r96 fixture README** (3 commands, "Replay from the repository root"), replayed on the frozen
snapshot:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response
# CLEAN: schema, citations, relations, timeline; 0 violations          exit 0
python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response
# SOURCE-SUPPORT 16/16; EDITORIAL-ANCHORS 2/2; … MODES 18/18; VALIDATED-ROWS 18/18
# RESULT PASS                                                         exit 0
python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response
# OBLIGATIONS raw=16 mapped=16
# INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18
# RESULT PASS                                                         exit 0
```

**tools README, Round-96 addendum command:**

```sh
python3 corpus/tools/map_obligations.py --self-test
# SELF-TEST CASES 24/24 pinned … 24 SELF-TEST PASS lines … RESULT PASS  exit 0
```

**Earlier tools README commands still replay on the new revision** (no stale command):

```sh
python3 corpus/tools/map_obligations.py corpus/fixtures/r88-m3-maya-cluster   # raw=10 mapped=10 PASS exit 0
python3 corpus/tools/map_obligations.py corpus/fixtures/r93-m2-kojiki-cluster # raw=12 mapped=12 PASS exit 0
python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing   # raw=14 mapped=14 PASS exit 0
python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath # raw=15 mapped=15 PASS exit 0
python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93
# SNAPSHOT inputs=4 digests=verified … FROZEN expected=PASS/0 matched / RESULT PASS exit 0
# fail-closed preserved: r87-myth-cluster exit 2, r89-inspiration-paraphrase exit 2
```

**The addendum's two documented demos were replayed on scratch copies and reproduce the
printed outputs exactly** (not merely plausible):

```sh
# deletion class on a copy of r94-paired-crossing (claims key + map row removed)
OBLIGATIONS raw=13 mapped=13
INVENTORY JSON-FACTS 13/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 15/16 MISMATCH
FINDING inventory_mismatch: declared JSON-facts/editorial-rows/total-rows 14/2/16; observed 13/2/15
RESULT FAIL                                                            exit 1
# dual_pointer on a copy of r88-m3-maya-cluster (row P1 cell gains a second token)
FINDING dual_pointer: row P1 (line 23) names a second pointer token 'entities[0].claims[0]' alongside entities.json#/0/first_appearance
RESULT FAIL                                                            exit 1
```

**Q3 gate commands:** `python3 corpus/tools/dependency_freeze.py <fixture>` on the chain gives
`r88 2/2; 0 edges`, `r94 3/3; 2/2`, `r95 4/4; 3/3`, `r96 5/5; 4/4`, all `RESULT PASS` exit 0;
`--self-test` → `SELF-TEST 14/14 / RESULT PASS` exit 0.

## Check 4 — r95 README wording carried into r96 stays accurate with updated counts: PASS

`diff` of `r95-crossing-aftermath/README.md` (baseline copied before producers finished) vs
`r96-crossing-response/README.md`: every count-bearing line was updated, and verified against
the actual delivered JSON/Markdown:

- Line 3: "…five inherited entity records, the one inherited relation, the four inherited
  events, and the four inherited sources… added tick-12 response event and its note make the
  counts **5 entities / 1 relation / 5 events / 5 sources**" — matches `len()` of the delivered
  files (5/1/5/5).
- Line 7: namespace example moved to `(r95-crossing-aftermath, paired-clock)` /
  `(r96-crossing-response, paired-clock)`; added source `evin-response-note`, added event
  `response-evin-salt-court` — matches `sources.json` / `timeline.json`.
- Line 9: tick-11 now described as *inherited*; "new tick-12 event is ordered after and depends
  on that tick-11 report (`aftermath-missing-evin`)" — matches `timeline.json[4].depends_on`.
- Line 11: new unresolved-two-accounts bound; "The tick-12 event's `entity_id` is Evin" —
  matches `timeline.json[4].entity_id == "evin"`.
- Line 21: "**16** source-attributed JSON pointer obligations (the 15 inherited rows carried
  unchanged plus the new tick-12 event row)" — matches the map's J01–J16 and `support_check`
  16/16.
- Lines 26–28: replay commands point at `r96-crossing-response` (replayed above).
- Count-free paragraphs (ticks/edges editorial encoding, `first_appearance: crossing-minute`,
  Spence design prompt) are carried verbatim and remain true for r96.

The map's declaration matches the delivered bytes: `**Expected inventory:** 16 JSON facts;
2 editorial rows; 18 total mapped rows; 14 distinct excerpt anchors` vs `support_check`
`INVENTORY 16/16; 2/2; 18/18; DISTINCT-ANCHORS 14/14`. J15's anchor is at
`fictional-excerpts.md:26` (span 22-31) and J16's at `:37` (span 33-42), exactly the quoted
lines. The excerpt-range declaration `fictional-excerpts.md:12-40` follows the r95 convention
(r95 declared `12-29`; both end at the last quoted line, not the trailing scope line).

Tools README: the r95 sentences "22 expectations" / "22 SELF-TEST PASS lines" / "The inventory
line is a receipt, not a gate" are retained as delivered history but the Round-96 addendum
explicitly supersedes the gate sentence in place ("so this addendum supersedes the r95 sentence
'The inventory line is a receipt, not a gate'") and states the current 24-case count and the
still-open BR-05 residual — stale-by-design history with the correction stated, not a silent
stale claim.

## Observations (low severity, disclosed; none block freshness)

1. **Foreign scratch pin in the delivered freeze contract.** `dependency-freeze-contract.json`
   `pins` includes `c3red` → `fixture: ".ufo/waves/round-96/seats/V41-scratch/c3red"` (written
   by a verifier's `--freeze` probe). Q3 disclosed it and left it because V22/V33 receipts
   quote it. It is inert to chain verification (pins are keyed by basename and the chain is
   verified by the four corpus pins), but it embeds a round-scoped scratch path in a delivered
   byte; a closure-time cleanup would remove it (with the receipts' quoting noted).
2. **Freeze-time `revision` label semantics.** All five pins carry
   `revision: 60dba0c…` = HEAD at freeze time. For the r96 pin the content digests cover bytes
   that are not in `60dba0c` (untracked at freeze time), so the label reads as "when frozen",
   not "where the content lives". Inert to verification (`compare()` ignores `revision`); the
   contract does not document the field's meaning.
3. **Q6 note pins the in-flight revision, not the delivered one.** The note records
   `6634e176…` (17:46, in flight) and `d1c239cc…` (17:43, r95) but not the delivered
   `2b0ba815…`; it self-caveats ("Re-run all three commands against the delivered revision
   before citing these receipts"). I re-ran all three: receipt values identical under the
   delivered revision, so the recorded receipts remain true; the pin line itself is the same
   carried residual class as r95's P5 note ("stale tool-revision pin self-caveated,
   correctable next touch").
4. **Minor wording imprecision in the r96 map.** `claim-excerpt-map.md:18` says "The 15
   inherited rows carry the **r94** JSON pointers, excerpt anchors, spans, and delivery modes
   unchanged" — inherited from r95, where it was accurate for 14 rows; J15's pointer
   (`timeline.json#/3`) is r95-authored. "Previously delivered" would be exact. No count,
   pointer, or gate is affected.
5. **Q1 report §8 references an addendum that is not present** ("see the addendum below for the
   final state"); the report ends at its bottom line with the Q2-contract poll still PENDING.
   Report-only inconsistency; the 24-case contract landed at 17:50:17 and verifies 24/24 — the
   missing addendum's subject is independently confirmed here.

Environment note: `/tmp` was full for part of the round ("No space left on device"), matching
Q1's report; all my outputs were redirected to my scratch dir. No delivered byte depends on
`/tmp`.

## Bottom line

**PASS** — on the frozen r96 producer bytes (all six reports present), the stale-pin sweep
finds no HEAD pins or dangling revisions (only a runtime `git rev-parse HEAD` inside
`dependency_freeze.py --freeze`, storing fixed shas), the knowledge note carries the standard
metadata header with every spot-checked citation resolving, the r96 fixture README and tools
README commands all replay to their documented outputs (including both addendum demos,
24/24 self-test, chain 4/4 and r87/r89 fail-closed exit 2), and the r95 README wording carried
into r96 is accurate with every count updated (5/1/5/5, 16 obligations, 18 rows, 14 anchors,
census 170) — with five disclosed low-severity observations, none blocking.
