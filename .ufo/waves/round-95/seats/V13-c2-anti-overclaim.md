# V13 — c2-anti-overclaim (round 95)

**Seat:** V13, adversarial anti-overclaim critic for C2. **Artifacts judged (final delivered bytes):**
`corpus/fixtures/r95-crossing-aftermath/` (10 files: P3 JSON/MD + P4 `README.md`, `claim-excerpt-map.md`)
and `corpus/knowledge/r95-aftermath-scope-note.md`. Baseline `fb118c4`; lane HEAD unchanged
(`git status` at verification: `M LOG.md`, `M corpus/tools/map_obligations.py`,
`?? .ufo/waves/round-95/`, `?? corpus/fixtures/r95-crossing-aftermath/`,
`?? corpus/knowledge/r95-aftermath-scope-note.md`). No file outside this report was written.

**Poll record (P3–P5).** A 20 s-cadence poll saw P3's byte copies land 16:18, the three modified
files (sources/timeline/fictional-excerpts) and P3's report by 16:20–16:22; P4's README + map and
report by 16:21–16:22; P5's note 16:25 (an earlier 55-line version was superseded by the 57-line
final with the tool-revision block; final sha256 `f87ed42a…`, matching P5's report). No ABSENT
condition; nothing was verified before its producer bytes were present and complete
(counts gate: `timeline=4 sources=4`). Final artifact hashes I verified against:

```
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  relations.json
026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b  entities.json
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  contradictions.json
58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37  inspiration-note.md
b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd  source-excerpt.md
fd9e30e8d9ad40013be2172781d13d84ba219377c8433ff6e529ea8e1927e64a  sources.json
3c0faad6bf32f944f9f2a20f3bd15829044afa04f1a8837601903433b00ea177  timeline.json
0ef6734ae52d28656e75869d942d6b1e8e324b116977a2811b3b36dc0880b282  fictional-excerpts.md
9d27af4ac9644210d3ee1df26938a4a5592b8cbcfdb5d6fb880de6ccdb1bdd0b  README.md  (md5 5ccf979d… = P4's record)
30281ff1a497bbe66f23cbd8a49befb3319595f20990718a0ffe8050741a874a  claim-excerpt-map.md  (md5 a872889e… = P4's record)
f87ed42ad4d42143bb84f13539f2db8ca0d5f221aaf4eaffdbd6874b5ef1ab9a  r95-aftermath-scope-note.md
```

**Method.** (1) Read every new/modified byte in full (excerpt, sources, timeline, README, map,
knowledge note) plus the five byte-copy files against their r94 counterparts. (2) `cmp`/`sha256sum`/
`diff`/byte-prefix checks for the inheritance claims. (3) Token sweeps for each hunted class
(breach, perpetual-performance/alliance, canon-truth, rights, AI-training, authenticated-testimony,
identity, absolutes) over every new byte. (4) Re-execution of every executable claim cited in the
new bytes at the final tool revisions. (5) Citation spot-checks of every line/pointer the note and
map assert.

---

## 1. Relation row and fixture diff (C2 core confirmations)

**Relation row byte-identity — CONFIRMED.**

```
$ cmp corpus/fixtures/r94-paired-crossing/relations.json corpus/fixtures/r95-crossing-aftermath/relations.json
(empty)  →  IDENTICAL
$ sha256sum both
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  …r94-paired-crossing/relations.json
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  …r95-crossing-aftermath/relations.json
```

**Five byte copies — IDENTICAL** (`cmp -s` exit 0): `entities.json`, `contradictions.json`,
`inspiration-note.md`, `source-excerpt.md`, `relations.json`.

**Three modified files — strictly additive.** `diff` r94→r95 shows only additions; excerpts byte
prefix preserved (`1116 → 1845` bytes, `b[:1116] == a` → `True`): sources +1 row
(`aru-aftermath-note`, lines 20-25), timeline +1 row (`aftermath-missing-evin`, lines 32-42),
excerpts +section (lines 21-31). Parsed inheritance: `r95 timeline[:3] == r94 timeline` → `True`;
`r95 sources[:3] == r94 sources` → `True`; `contradictions` `[]` in both. Counts **5 entities /
1 relation / 4 events / 4 sources**; census `ls -d corpus/fixtures/*/ | wc -l` → **169** (168 at
r94). Map rows: **0 non-namespace differences across J01–J14** (script comparing all columns
except the path-qualification column), J15 new only — matching the map's own claim
(`claim-excerpt-map.md:18`). r94 fixture tree untouched (`git status` empty).

---

## 2. Class sweep — every suspect phrase and whether it is bounded in place

### breach / non-performance
| Suspect phrase | Location | Bounded in place? |
|---|---|---|
| "I assert no other duty, no breach, and no obligation beyond this crossing." | `fictional-excerpts.md:29` | Yes — the sentence itself is the bound |
| "It asserts no breach and no perpetual or continuing obligation; the crossing-scoped agreement above is unchanged, and the record supplies no other duty." | `fictional-excerpts.md:31` | Yes |
| "not evidence of a breach, a continuing duty, a perpetual obligation, or an external historical fact" | `sources.json:24` (new row) | Yes |
| "Aru reports waiting through the agreed bell and that Evin did not come; the note scopes the agreement to this crossing only and asserts no other duty or breach." | `timeline.json:40` | Yes — report-framed, negation in place |
| "the record asserts no other duty, no breach, no continuing obligation, and no obligation beyond this crossing. It is not evidence of an alliance, a continuing practice, perpetual performance, a standing duty, or an external historical fact." | `README.md:11` | Yes |
| "it asserts no breach, no continuing duty, and no obligation beyond this crossing, and the record supplies no other duty" | `claim-excerpt-map.md:51` | Yes |
| "not merged canon, not a breach finding, and not a verdict on any character" | `r95-aftermath-scope-note.md:7` | Yes |
| "the note reports a non-arrival; it does not establish world-absence, fault, or a broken obligation" | `r95-aftermath-scope-note.md:11` | Yes |
| "it is not proof that Evin was absent as world fact, not proof of any cause, and not independent corroboration" | `r95-aftermath-scope-note.md:29` | Yes |
| "Do not infer abandonment, fault, guilt, an alliance failure, or a standing duty." | `r95-aftermath-scope-note.md:30` | Yes |
| "the crossing-only scope is the reason a reported non-arrival is not automatically a breach" | `r95-aftermath-scope-note.md:37` | Yes |

No new byte asserts a breach, fault, or continuing duty outside a negating/scoping clause.

### perpetual-performance / alliance
| Suspect phrase | Location | Bounded in place? |
|---|---|---|
| "not evidence of continuing performance, a standing alliance, or an external historical fact" | `sources.json:18` (inherited, unchanged) | Yes |
| "It is not evidence of an alliance, a continuing practice, perpetual performance, a standing duty, or an external historical fact." | `README.md:11` | Yes |
| "The new relation encodes only the agreement for this crossing, not perpetual performance or alliance." | `claim-excerpt-map.md:49` (inherited wording) | Yes |

### canon-truth
| Suspect phrase | Location | Bounded in place? |
|---|---|---|
| "its metaphor is not an objective record or creation account" | `sources.json:6` (inherited) | Yes |
| "It supplies no in-world witness, cultural authority, or fictional canon, and asserts no cultural meaning." | `README.md:19` | Yes |
| "they do not make Spence an in-world witness, assign cultural meaning, or add canon" | `claim-excerpt-map.md:40` (inherited wording) | Yes |
| "neither is a contradiction, an occupancy change, or a fact about the world" | `r95-aftermath-scope-note.md:13` | Yes |

### rights / AI-training-permission
| Suspect phrase | Location | Bounded in place? |
|---|---|---|
| "Rights and AI-training permission remain unassessed; neither is granted or inferred here." | `README.md:19` | Yes |
| "Rights and AI-training permission remain unassessed here." | `r95-aftermath-scope-note.md:57` | Yes |
| "not … rights, permission, or canon review" | `README.md:21`; `claim-excerpt-map.md:53` | Yes |

### identity-inference
| Suspect phrase | Location | Bounded in place? |
|---|---|---|
| "path qualification names the lookup namespace and does not imply a separate source, entity identity, or contradiction" | `README.md:7` — carried verbatim from r94 `README.md:7` | Yes (under-claim/ambiguous direction; r94 F20-2 precedent; not a new defect — V13-3) |
| "r95 records a speaker reporting that a named *person* did not arrive under a bounded agreement" | `r95-aftermath-scope-note.md:13` | Yes — names only, no identity claim |
| "source IDs remain cluster-local and path-qualified comparisons are not identity evidence" | `r95-aftermath-scope-note.md:57` | Yes |

No added byte upgrades a label, resemblance, or report into identity continuity evidence.

---

## 3. Blue-Seal-style inference drift hunt

- `occupied-slot` misnomer: **0** occurrences in the new bytes (checked; the corrected r88-closure
  naming is not re-broken).
- **"the agreed bell"** (`fictional-excerpts.md:26`) is the only new referent. It appears only
  inside the fictional first-person note, and every product byte keeps it inside Aru's report frame:
  `timeline.json:40` ("Aru reports waiting through the agreed bell…"), `README.md:9` ("records only
  Aru's report that he waited through the agreed bell"), map J15 anchor (`claim-excerpt-map.md:36`).
  No byte converts it to clock time, a duration, or a term of the agreement beyond the note. Bounded
  by the report frame; residual: no in-place gloss of its status (unlike the tick glossary at
  `README.md:13`) — V13-4.
- **"waited through the agreed bell" duration drift:** no duration or elapsed-time claim anywhere in
  the new bytes (sweep for time words shows only the tick labels, bounded at `README.md:13` and
  `claim-excerpt-map.md:49` as editorial encodings).
- **"Evin did not come" → objective absence:** bounded at `r95-aftermath-scope-note.md:11` and `:29`
  ("not proof that Evin was absent as world fact"), `README.md:9` ("records only Aru's report… does
  not … convert the non-arrival into a verdict"), `sources.json:24` (reliability note).
- **Event ID `aftermath-missing-evin`:** the "missing" label is bounded — `README.md:9` (report
  frame), `claim-excerpt-map.md:51` ("one non-arrival on one occasion"), `r95-aftermath-scope-note.md:31`
  (the ID is an editorial encoding, not literal source wording).
- **Class-name drift ("reported non-performance"):** bounded by `r95-aftermath-scope-note.md:7`
  ("not a breach finding") and `:11` ("does not establish world-absence, fault, or a broken
  obligation"). A corpus-wide grep for prior "did not come / did not arrive / never came / failed to
  arrive / did not show" report phrasing in fixture markdown found no occurrence outside r95
  (scan bound: that phrasing family only).
- **Absolutes sweep** (`never|always|guarantee|proven|definitiv|objectiv|exactly|proves|true|truth`):
  every hit is either inherited-and-negated, a verified-factual span statement, or a boundary
  statement (`README.md:21`, `claim-excerpt-map.md:51/53`, note:25/32/37/38/51).

---

## 4. Items not fully bounded in place (all low severity; none is an overclaim)

**V13-1 — stale tool-scope phrase (under-claim, safe direction).** `r95-aftermath-scope-note.md:32`:
"`map_obligations.py` covers raw-JSON↔map completeness and source-ID agreement only." On the
delivered revision the tool also emits `schema_drift` findings at exit 1 (P1 report §1: `:357`,
`:377-388`) and parses the legacy r88 dialect — both absent from the "only" list. The operative
bound in the same sentence ("None reads the note as testimony or decides truth, breach, chronology,
rights, permission, or canon") remains true. Under-description, not an overclaim; no admission
effect.

**V13-2 — citation boundary 2 lines short.** `r95-aftermath-scope-note.md:37` cites
`corpus/fixtures/README.md` Round 94 section as `:1154-1173`; the section actually runs `:1154-1175`
(heading at 1154, pin note ends 1175). The cited catalogue content is inside the cited span;
trivial.

**V13-3 — inherited ambiguous identity clause.** `README.md:7` reuses r94's "does not imply … entity
identity" wording flagged at r94 as F20-2 (under-claim/ambiguity direction). Carried verbatim; not a
new r95 defect.

**V13-4 — "the agreed bell" has no in-place gloss.** The one new referent is bounded only by the
report frame (all layers). It asserts no canon/right/permission/identity/performance fact; no byte
upgrades it. Low severity residual, no action required.

---

## 5. Executable claims re-run (final revisions)

| Claim (source) | Command | Observed |
|---|---|---|
| structural CLEAN (`README.md:26`; note:44) | `python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath` | `CLEAN: schema, citations, relations, timeline; 0 violations` exit 0 (checker sha `ff9fd2aa…`, unchanged) |
| lexical receipt 15/2/17/13 (`README.md:21`; note:46) | `python3 corpus/tools/support_check.py corpus/fixtures/r95-crossing-aftermath` | `JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17; DISTINCT-ANCHORS 13/13 … MODES 17/17; VALIDATED-ROWS 17/17` / `RESULT PASS` exit 0 (J15 anchor found at line 26) |
| 15 obligations (`README.md:21`; map:5; note:48) | `python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath` | `OBLIGATIONS raw=15 mapped=15` / `INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17` / `RESULT PASS` exit 0 — tool sha `d1c239cc…` identical before and after the run |
| r94 control | `… corpus/fixtures/r94-paired-crossing` | `raw=14 mapped=14` / `RESULT PASS` exit 0 |
| persisted self-test (C1, adjacent) | `… --self-test` | 22 `SELF-TEST PASS` lines (`map_missing exit=2`, `invalid_arguments exit=2` included), `RESULT PASS`, exit 0, stderr 0 bytes (contract sha `8173bb97…`) |

Note's receipt block (lines 44-48) matches observed outputs; the note's own re-run instruction
(`:51`) was honored — all three commands green at the final revisions above. The note's disclosure
of the transient in-flight tool revision `ca05159e…` (uncaught `ValueError` on both maps; P5 report
§Anomalies 1) is consistent with what I observed directly: tool hash churn
`3f87fe8b… → 9224a684… → d1c239cc…` and an intermediate `FINDING self_test_contract` ERROR while
P2's contract was still the 20-case revision. Final revision: green, contract updated.

**Citation spot-checks:** `sources.json:21` (`aru-aftermath-note` id) ✓; `timeline.json:33`
(`aftermath-missing-evin` id) ✓; `claim-excerpt-map.md:36` (J15) ✓; `fictional-excerpts.md:31` ✓;
r94 `timeline.json:21` id ✓; r94 `README.md:9` quote ✓; `2026-10-12-lore-decision-table.md:226-230`
✓; r23 `strip-absence-note` at `timeline.json#/2` ✓. P3's reported delivered hashes for its three
modified files reproduced exactly (`fd9e30e8…`, `3c0faad6…`, `0ef6734a…`).

---

## 6. Round-context observation (outside my four artifact groups; attributed)

P1's report (§6.1) records a contradiction between the C3 declaration text ("12/12 PASS" for r88)
and the measured tool output (`OBLIGATIONS raw=10 mapped=10`, `TOTAL-ROWS 12/12`): 12 is the r88
map's total row count (10 JSON facts + 2 editorial), not an obligation count. Recorded here as
observed evidence for the C3 adjudicating seats, not as my verdict.

---

## 7. Bottom line

**PASS** — the r95 relation row is byte-identical to r94's (sha `c279254b…`), the five byte copies
are byte-identical, the three modified files are strictly additive, and no canon-truth, rights,
AI-training-permission, perpetual-performance/alliance, breach, authenticated-testimony, or
identity-inference overclaim survives unbounded in any new byte; the sole new referent ("the agreed
bell") is bounded by the report frame in every layer, and the only stale phrase found (note:32
tool-scope "only") under-claims rather than over-claims.
