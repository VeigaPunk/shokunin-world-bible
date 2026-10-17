# V19 — freshness (round 95)

Seat: V19 freshness. Exclusive report path: `.ufo/waves/round-95/seats/V19-freshness.md`.
Repo root: `/home/vgpnk/Projects/shokunin/lore-shokunin`. Baseline: r94 closure `fb118c4`.
Measurement window: 2026-10-17 16:16–16:30 local (19:16–19:30Z). No commits, no pushes, no network,
no writes outside this report and `.ufo/waves/round-95/seats/scratch/V19/`.

Scope (as declared): poll for P3–P5; stale-pin sweep of new bytes; knowledge-note header; r95 README
replay commands run verbatim; r94 README wording carried into r95 README checked for accuracy;
report every stale item.

## 0. Poll record (P3–P5)

First check 16:16:21: `corpus/fixtures/r95-crossing-aftermath/` absent, knowledge note absent, no
producer reports in `seats/`. A 20 s-cadence background poller (40 tries max) watched all eleven
declared P3/P4/P5 paths plus the presence of P3/P4/P5 reports. No ABSENT condition arose.

| time (local) | event |
|---|---|
| 16:18:01–16:18:34 | P3 byte copies land; `sources.json` (1225 B) and `timeline.json` (1254 B) modified per spec |
| 16:21:10 | P4 `claim-excerpt-map.md` lands |
| 16:21:27 | P4 `README.md` lands |
| 16:22:57 | P5 `corpus/knowledge/r95-aftermath-scope-note.md` lands |
| 16:25:58 | P5 report present; P3/P4 reports present earlier |
| 16:26:27 / 16:27:02 | P1 final `map_obligations.py` / P2 `map-obligations-contract.json` land |
| 16:28:05 → 16:29:05 | full artifact-set digest identical (md5 of concatenated sha256 set `696eba461472d801b2bad74c142390ce` both times) |
| 16:29 | P2 report present |

Delivered hashes at the verified revision (all measured, not copied from producer reports):

```
d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108  corpus/tools/map_obligations.py
8173bb97592a377716866737e8fcb4043014c9814e77a6248500d301a39170db  corpus/tools/map-obligations-contract.json
5d033c9db8a72801c9b8d5e609e01cddf1ace668711e24d0476b8cbd6879a264  corpus/tools/README.md
f87ed42ad4d42143bb84f13539f2db8ca0d5f221aaf4eaffdbd6874b5ef1ab9a  corpus/knowledge/r95-aftermath-scope-note.md
30281ff1a497bbe66f23cbd8a49befb3319595f20990718a0ffe8050741a874a  corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md
9d27af4ac9644210d3ee1df26938a4a5592b8cbcfdb5d6fb880de6ccdb1bdd0b  corpus/fixtures/r95-crossing-aftermath/README.md
026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b  corpus/fixtures/r95-crossing-aftermath/entities.json
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  corpus/fixtures/r95-crossing-aftermath/relations.json
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  corpus/fixtures/r95-crossing-aftermath/contradictions.json
fd9e30e8d9ad40013be2172781d13d84ba219377c8433ff6e529ea8e1927e64a  corpus/fixtures/r95-crossing-aftermath/sources.json
3c0faad6bf32f944f9f2a20f3bd15829044afa04f1a8837601903433b00ea177  corpus/fixtures/r95-crossing-aftermath/timeline.json
0ef6734ae52d28656e75869d942d6b1e8e324b116977a2811b3b36dc0880b282  corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md
58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37  corpus/fixtures/r95-crossing-aftermath/inspiration-note.md
b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd  corpus/fixtures/r95-crossing-aftermath/source-excerpt.md
```

## 1. Stale-pin sweep of new bytes

New/modified non-scratch bytes this round (`git status --porcelain -uall`): `LOG.md` (round
declaration, 57 added lines, no pins in the added lines), `corpus/tools/{map_obligations.py,
map-obligations-contract.json,README.md}`, the ten `corpus/fixtures/r95-crossing-aftermath/*` files,
`corpus/knowledge/r95-aftermath-scope-note.md`, and the producer seat reports.

Sweep regex `\bHEAD\b|\bcommit\b|\bgit [a-z]|\bpinned?\b|sha256|[0-9a-f]{7,40}`, run over:

- **r95 fixture (10 files), r95 README, r95 claim-excerpt-map, knowledge note — clean (grep exit 1,
  no matches).** No HEAD, commit, `git` reference, "pin", sha256, or hex-hash token in any of them.
- P2's added lines (contract diff + `corpus/tools/README.md` diff) — clean.
- P1's added lines (`map_obligations.py` diff) — clean apart from digest-handling *code*
  (`SHA256 = re.compile(...)`, `hashlib.sha256(...)` at `:57,:481,:511,:611`), which is the
  frozen-digest feature, not a pin.
- Pre-existing (unmodified) hits only in `corpus/tools/README.md:33,36,53,68,79`, which cite the r90
  checker pin `e97613c` and boundary-doc revisions `65838f86…`/`5eb9451b…`; those lines are not new
  bytes and are outside this seat's rule.
- Producer reports `P1-tool-code.md`, `P3-fixture-json.md`, `P4-fixture-docs.md`,
  `P5-knowledge-note.md` carry evidence hashes by design; they are receipts, not delivered artifacts.

### FINDING F-1 — stale revision pin in the delivered knowledge note (already stale at hand-off)

`corpus/knowledge/r95-aftermath-scope-note.md:51` (durable, non-seat artifact) states:

> Tool revisions at these receipts (2026-10-17T16:25-03:00): `check_bible.py` sha256 `ff9fd2aa…`,
> `support_check.py` `55a5eb27…`, `map_obligations.py` `9224a684…`.

Measured against the delivered tree:

```
$ sha256sum corpus/tools/map_obligations.py corpus/tools/support_check.py corpus/fixtures/check_bible.py
d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108  corpus/tools/map_obligations.py
55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  corpus/tools/support_check.py
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
```

- `check_bible.py` `ff9fd2aa…` — current, matches the r91-c9-watch pin.
- `support_check.py` `55a5eb27…` — current.
- `map_obligations.py` `9224a684…` — **stale**: P1's final revision (`d1c239cc…`, mtime 16:26:27)
  landed after the note's 16:25:15 write. The pinned hash is not the delivered revision.

Mitigation present in the same paragraph: "The C1 tool revision was still in flight during this
round … Re-run all three commands against the delivered revision before citing these receipts." I did
re-run them (§3): all three receipts are green at the delivered revision, so the note's receipt
*values* remain accurate; only the revision pin is false. Severity: bounded but real — a durable
knowledge artifact now carries a content-hash pin that is already wrong at hand-off. Recommended
closure action: drop the `9224a684…` value (keeping the caveat) or re-pin to the closure revision.

## 2. Knowledge-note header

`corpus/knowledge/r95-aftermath-scope-note.md:1-3` opens with the required metadata, in the same
convention as `corpus/knowledge/r94-cross-myth-design-comparison.md`:

```
source: `corpus/fixtures/r95-crossing-aftermath/{sources.json,timeline.json,relations.json,fictional-excerpts.md,README.md,claim-excerpt-map.md,entities.json,contradictions.json,inspiration-note.md,source-excerpt.md}`; …
verified-at: 2026-10-17 — read every cited local record and excerpt in the delivered r95 fixture and its r94/r23 counterparts; no external URL was fetched in this pass.
recheck: before integrating any r95 aftermath claim, and whenever the aftermath note, the tick-11 event, … change; …
```

`source:` lists all ten files of the r95 fixture directory (verified: 10 listed, 10 present), plus the
r94/r23 counterparts and `fixtures/README.md`. **PASS.**

## 3. r95 README replay commands vs delivered behavior (run verbatim)

Extracted from `corpus/fixtures/r95-crossing-aftermath/README.md:25-29` and run from the repo root at
the delivered revision:

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0

$ python3 corpus/tools/support_check.py corpus/fixtures/r95-crossing-aftermath
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17; DISTINCT-ANCHORS 13/13
SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 17/17; VALIDATED-ROWS 17/17
RESULT PASS
exit=0

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
RESULT PASS
exit=0
```

All three commands match delivered behavior; the README quotes no outputs, so there is no
output-drift exposure. The README's count claims were measured against the bytes:
`entities 5 / relations 1 / events 4 / sources 4` (python JSON parse), 15 canonical map rows
(J01–J15), census `ls -d corpus/fixtures/*/ | wc -l` = **169** (was 168). **PASS.**

## 4. r94 README wording carried into r95 README

`diff -u r94-paired-crossing/README.md r95-crossing-aftermath/README.md` (26 → 29 lines); each
carried sentence audited against the bytes:

| carried r94 wording | r95 status |
|---|---|
| "explicit continuation of `r88-m3-maya-cluster`" | rewritten as "continuation of `r94-paired-crossing`, itself a continuation of `r88-m3-maya-cluster`" — accurate |
| "four inherited entity records and two tick-9 events … retained" | "five inherited entity records and the one inherited relation are copied by JSON value" — accurate (`cmp` byte-identical: entities, relations, contradictions, inspiration-note, source-excerpt) |
| counts "5 entities / 1 relation / 3 events" | "5 entities / 1 relation / 4 events / 4 sources" — updated and measured true |
| namespace examples `(r88…, paired-clock)` / `(r94…, paired-clock)` | updated to `(r94…)` / `(r95…)` — accurate |
| tick-9/tick-10 occasion paragraph; relation-not-alliance sentence | rewritten for the tick-11 event; "not evidence of an alliance, a continuing practice, perpetual performance, a standing duty, or an external historical fact" — accurate against timeline/sources |
| "integer ticks and event-ID edges … editorial encodings" | carried (now "excerpts"/"sources") — still true |
| "`first_appearance: crossing-minute` … inherited r88 verse already uses “chalk stair”" | carried verbatim — still true (entities byte-identical; verse at `fictional-excerpts.md:7-8` carried) |
| Spence / bounded-external-design-prompt paragraph | carried verbatim — still true (`source-excerpt.md`, `inspiration-note.md` byte-identical) |
| "`claim-excerpt-map.md` has 14 … obligations" | "15 … (the 14 inherited rows carried unchanged plus the new tick-11 event row)" — count updated and true |
| replay block | paths updated to r95, `map_obligations` added — all three verified exit 0 (§3) |

No stale carried statement found; every changed count was updated.

Minor precision observations (low severity, not staleness):

1. `README.md:11` "the record asserts no other duty, no breach, no continuing obligation, and no
   obligation beyond this crossing" — the excerpt (`fictional-excerpts.md:29`) says "no other duty,
   no breach, and no obligation beyond this crossing", and `sources.json#/3` says "not evidence of a
   breach, a continuing duty, a perpetual obligation". The README consolidates those into "no
   continuing obligation" without quoting; values are consistent, wording is a paraphrase.
2. `README.md:21` "(the 14 inherited rows carried unchanged plus the new tick-11 event row)" — J01–J14
   did change in the path-qualification column (`r94-paired-crossing:…` → `r95-crossing-aftermath:…`).
   `claim-excerpt-map.md:19` states this explicitly ("only the path-qualification column names this
   fixture's cluster path"), so the pair is accurate; the README parenthetical alone reads loosely.
3. r94's sentence explaining the tick-10 minute's single-actor-slot field is not carried (replaced by
   the tick-11 analogue). Coverage change, not staleness; the map's J14 row still covers the pointer.

## 5. Citation freshness (paths and line numbers)

- All 26 distinct repo-relative paths cited in the r95 README, map, and knowledge note exist
  (python sweep with brace expansion; MISSING: none).
- Line-number citations verified by `sed` against the delivered bytes: `sources.json:21` =
  `"id": "aru-aftermath-note",`; `timeline.json:33` = `"id": "aftermath-missing-evin",`;
  `claim-excerpt-map.md:36` = the J15 row; `:49` = normalization paragraph; `:51` = J15 explanation;
  `README.md:9/:11/:13` as cited; `r94-paired-crossing/README.md:9` contains the quoted "not evidence
  of an alliance, a continuing practice, or perpetual performance"; `r94 …/timeline.json:21` =
  `"id": "paired-crossing-decision",`; `corpus/fixtures/README.md:1154-1173` = the Round-94 section
  including the census re-declaration; `2026-10-12-lore-decision-table.md:226-230` = the Round-23
  witnessed-absence row containing the quoted "do not delete entities, clear occupancy, or treat the
  report as proof"; `r23-note-class/witnessed-absence-clause-map.md:1-3`; r23 event
  `strip-absence-note` present.
- Note's equality claims reproduced: `r95 timeline[:3] == r94 timeline` → `True`; `r95 sources[:3] ==
  r94 sources` → `True`; `contradictions.json` = `[]` in both.
- Note's receipt values reproduced at the delivered revision: §3 (all exit 0).

Adjacent observation (out of this seat's write scope, for the closure seat): the census
re-declaration at `corpus/fixtures/README.md:1173` states 168 fixture directories "measured at the
r94 delivered revision"; the tree now holds 169. It is explicitly labelled "not a pinned invariant",
so it is self-limiting rather than false — but it will need the Round-95 append at closure.

## 6. New-bytes behavior claims in P1/P2 artifacts (checked because they are new bytes)

- `map-obligations-contract.json` now persists 22 cases: `complete, missing, duplicate, phantom,
  source_id_mismatch, malformed_json, co_mapped_grammar, legacy_grammar, invalid_pointer,
  empty_segment, noncanonical_index, noncanonical_claim_index, foreign_path, traversal_path,
  symlink_path, frozen_complete, frozen_tampered, frozen_missing_digests, frozen_expected_failure,
  frozen_verdict_mismatch, map_missing, invalid_arguments`.
- P2's quoted `--self-test` behavior reproduced: 22 `SELF-TEST PASS` lines, `RESULT PASS`, exit 0.
- P2's addendum behavior quotes reproduced: r88 `exit 0` (`raw=10 mapped=10`, `INVENTORY JSON-FACTS
  10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12`); r87 `exit 2` `unsupported_map`; r89 `exit 2`
  `unsupported_map`; frozen replay `python3 corpus/tools/map_obligations.py --frozen
  .ufo/waves/round-94/frozen/map-obligations-r93` → `SNAPSHOT inputs=4 digests=verified` / `FROZEN
  expected=PASS/0 findings=none matched` / `RESULT PASS` exit 0.
- Transient mid-round state recorded (not a defect at delivery, but it is why F-1's pin is stale):
  between 16:24:43 and 16:26:27 the tool implemented 22 cases while the contract still declared 20,
  so `map_obligations.py --self-test` printed `FINDING self_test_contract: contract self-test cases do
  not match the implemented cases` / `RESULT ERROR`. P2's contract landed 16:27:02 and the pair is
  consistent again. Receipts captured in that window — including the note's `9224a684…` pin — are not
  receipts at the delivered revision.

## 7. Limits

This seat read delivered bytes only; it did not re-derive C1/C2/C3 semantics (other seats own those
verdicts), did not inspect the external Spence/ETCSL texts, and did not audit producer scratch. The
stale-pin rule was applied to new deliverable bytes; producer seat reports and pre-existing
`corpus/tools/README.md` lines legitimately cite historical pins as evidence.

## Bottom line

**PASS — freshness:** no HEAD/commit pins in any new deliverable byte, the knowledge note carries the
required `source`/`verified-at`/`recheck` header, and all three r95 README replay commands reproduce
delivered behavior (exit 0) at the verified revision; one stale item reported — the knowledge note
pins `map_obligations.py` sha256 `9224a684…` while the delivered tool is `d1c239cc…` (self-caveated,
receipt values re-verified green).
