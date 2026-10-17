# F04 — c1-whole-claim: independent manual whole-proposition review

**Seat:** F04 (FOLLOW-UP wave, round 94) · **Role:** independent manual whole-claim review of the new authored in-world minute and every new proposition in `entities/relations/timeline`.
**Candidate reviewed:** WORK checkpoint `abbc3e0` (HEAD at review time `65a9329`; worktree clean except untracked `.ufo/waves/round-94/followup/`).
**Read-only:** no corpus writes, no commits; only this report written.

## Method

Read the delivered excerpt set (`source-excerpt.md`, `fictional-excerpts.md`), the three JSON record files, `claim-excerpt-map.md`, `sources.json`, `README.md`, `contradictions.json`, and the inherited r88 fixture. Traced each new proposition to a literal clause of the authored minute (`fictional-excerpts.md:17-20`) or to explicitly labeled editorial metadata (IDs, ticks, schema slots, conventions). Ran the declared replay commands and an independent raw-obligation census as completeness cross-checks.

## The new authored minute (source text, verified line numbers)

```
17 > The Chalk Stair is the named rain-dark crossing between Quiet Rise and Salt Court.
18 > After both Tick 9 entries above, Aru and Evin met at the Chalk Stair at tick 10.
19 > There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.
20 > Their tick-10 decision depends on both ninth-bell entries: Aru's north-lantern entry at Quiet Rise and Evin's south-bell entry at Salt Court. After agreeing to share stewardship for this crossing only, they chalked one temporary route mark together at the midpoint.
```

Line-number check command output (`python3` split of `fictional-excerpts.md`) matches the map's declared spans exactly: 17 (J05), 18 (J10), 19 (J11), 20 (J14).

## Proposition trace — new records (4 new obligations, all `crossing-minute`)

Completeness of this list is machine-checked: an independent census of every source-attributed field found `total source-attributed obligations: 14`, of which `attributed to crossing-minute (new): 4` — exactly `entities.json#/4/first_appearance`, `entities.json#/4/claims/0`, `relations.json#/0`, `timeline.json#/2` (output below).

### 1. `entities.json#/4` chalk-stair (`entities.json:50-61`)

| Proposition (pointer) | Clause / metadata source | Entailed? |
|---|---|---|
| `name: "Chalk Stair"` (`entities.json:53`) | `fictional-excerpts.md:17` "The Chalk Stair is the named rain-dark crossing" | Yes — literal |
| `id: "chalk-stair"` (`entities.json:51`) | Editorial slug of the name; IDs are labeled encodings at `claim-excerpt-map.md:48` | Yes — labeled editorial |
| `kind: "place"` (`entities.json:52`) | Normalization of "crossing between Quiet Rise and Salt Court" (`fictional-excerpts.md:17`); both endpoints are `kind: place` in inherited records | Yes — schema normalization, covered by the general non-literal-field caveat at `claim-excerpt-map.md:14` (see O1) |
| `first_appearance: "crossing-minute"` (`entities.json:54`) | Explicitly labeled convention at `README.md:13`: "identifies the source that first presents Chalk Stair as a specific place in the JSON bible, not the earliest occurrence of the words: the inherited r88 verse already uses 'chalk stair' as an unowned crossing metaphor" | Yes — labeled editorial convention (see O1; this is the sharpest point) |
| `claims/0.statement`: "The crossing minute places Aru and Evin together at the Chalk Stair after both tick-9 entries." (`entities.json:57`) | `fictional-excerpts.md:18`: "After both Tick 9 entries above, Aru and Evin met at the Chalk Stair at tick 10." | Yes — "met" = together; ordering phrase is verbatim |
| `claims/0.source_id: "crossing-minute"` (`entities.json:58`) | The minute is the authored source for this proposition | Yes — attribution |

### 2. `relations.json#/0` (`relations.json:2-7`)

| Proposition | Clause source | Entailed? |
|---|---|---|
| `from: "aru"`, `to: "evin"` (`relations.json:3-4`) | `fictional-excerpts.md:19` "they agreed" — antecedent "Aru and Evin" at line 18 | Yes |
| `type: "agreed_co_stewardship_for_this_crossing"` (`relations.json:5`) | `fictional-excerpts.md:19` "agreed, for this crossing only, to share stewardship of the Chalk Stair" | Yes — normalized identifier; "co-" = "share"; scope word "for_this_crossing" preserves "for this crossing only" |
| `source_id: "crossing-minute"` (`relations.json:6`) | Attribution | Yes |

### 3. `timeline.json#/2` (`timeline.json:20-31`)

| Proposition | Clause / metadata source | Entailed? |
|---|---|---|
| `id: "paired-crossing-decision"` (`timeline.json:21`) | Editorial event ID; labeled at `claim-excerpt-map.md:48` ("`depends_on` event IDs are editorial encodings") | Yes — labeled editorial |
| `tick: 10` (`timeline.json:22`) | `fictional-excerpts.md:18` "at tick 10"; integer encoding labeled at `claim-excerpt-map.md:48` | Yes |
| `entity_id: "aru"` (`timeline.json:23`) | Aru is a named participant (line 18). Single-actor schema slot; explicitly labeled at `README.md:9`: "its description and excerpt name both participants, so the field does not exclude Evin" | Yes — labeled schema limitation (see O2) |
| `place_id: "chalk-stair"` (`timeline.json:24`) | `fictional-excerpts.md:18` "met at the Chalk Stair" | Yes |
| `depends_on: ["aru-ninth-bell","evin-ninth-bell"]` (`timeline.json:25-28`) | `fictional-excerpts.md:20` "Their tick-10 decision depends on both ninth-bell entries: Aru's north-lantern entry at Quiet Rise and Evin's south-bell entry at Salt Court." The two IDs are the inherited events' IDs; ID encoding labeled at `claim-excerpt-map.md:48` and `README.md:11` | Yes — the dependency is asserted by the source itself, not inferred by the editor |
| `description`: "At the Chalk Stair, Aru and Evin agree to share stewardship for this crossing only, then chalk one temporary route mark." (`timeline.json:29`) | `fictional-excerpts.md:18` (place, actors), `:19` (agreement, "for this crossing only"), `:20` ("they chalked one temporary route mark") | Yes — see O3 on tense |
| `source_id: "crossing-minute"` (`timeline.json:30`) | Attribution | Yes |

No new proposition asserts an actor, place, or agreement beyond these clauses. The minute's extra detail "together at the midpoint" (line 20) is not promoted into JSON, and nothing claims it is.

## Envelope-style overreach check — none found

- **No contents claim.** No record asserts the JSON or excerpt reproduces the minute's full contents. The map's general caveat (`claim-excerpt-map.md:14`) states `verbatim` "names the delivered wording, not a claim that every normalized JSON field is a literal quotation", and `README.md:11` guards the opposite direction: inherited empty `depends_on` arrays "mean no earlier dependency is represented for those entries in this mapped sequence; they do not assert that no earlier event exists anywhere." Machine check: the raw JSON blob contains none of `alliance`, `perpetual`, `forever`, `always`, `continuing`, `entire`, `complete`, `witness`, `contents`, `every` (output below).
- **No perpetual performance.** Relation type carries `for_this_crossing`; source text says "for this crossing only" and "one temporary route mark" (lines 19-20); `sources.json:18` disclaims "continuing performance"; `claim-excerpt-map.md:48` "The new relation encodes only the agreement for this crossing, not perpetual performance or alliance"; `README.md:9` "It is not evidence of an alliance, a continuing practice, or perpetual performance."
- **No alliance claim.** No alliance term appears in any JSON field; three independent disclaimers (`README.md:9`, `claim-excerpt-map.md:48`, `sources.json:18`) bound the relation to a single crossing.
- A grep sweep for overreach vocabulary over the whole fixture returned only those disclaimer lines — no positive assertion of unbounded scope anywhere.

## Inherited-record preservation (context evidence)

- `entities r88[0:4]==r94[0:4]: True`; `timeline r88==r94[0:2]: True` (parsed-value equality).
- `r88 fictional-excerpts is byte-prefix of r94: True` (484 of 1116 bytes; inherited verse and register wording unchanged).
- `source-excerpt.md: IDENTICAL`, `inspiration-note.md: IDENTICAL`, `contradictions.json: IDENTICAL`; `sources.json` entries `veil-verse` and `paired-clock` identical to r88.
- New fixture count: `r94 extra entity: chalk-stair | extra event: paired-crossing-decision`; `relations.json` 0→1.

## Observations (none is a claim failure)

- **O1 — normalized fields.** `kind: "place"` and the `first_appearance` convention are editorial normalizations, not literal excerpt wording. `first_appearance` is explicitly labeled at `README.md:13` (including the verse's prior metaphorical "chalk stair", retained at `fictional-excerpts.md:7-8`); `kind` has no field-specific label and relies on the general caveat at `claim-excerpt-map.md:14`. Neither adds un-entailed actor/place/agreement content.
- **O2 — single-actor schema slot.** `entity_id: "aru"` encodes only one of two named participants; explicitly labeled at `README.md:9`, and map row J14's anchor names both actors, so the limitation is visible to a reader.
- **O3 — tense normalization.** The timeline description uses present "agree"/"chalk" for the recorded past event ("agreed"/"chalked" in the source); bounded by "for this crossing only" and "temporary", so it does not assert present validity. The map's J14 anchor retains the source's past tense.
- **O4 — span granularity.** Map row J14 declares span 18-20 while the exact anchor string is entirely on line 20; fields do draw on line 18 (tick, place) and line 20 (dependency, description), so the span is defensible. `support_check.py` reports J14 "anchor=found; 20".
- **O5 — declared source with zero obligations.** `veil-verse` is declared in `sources.json:3-7` but no record is attributed to it, so it yields no raw obligation; this is consistent with the 14-obligation inventory (no unmapped obligation exists). Noted only.
- **O6 — omitted r88 analysis file (outside this seat's entailment scope).** r88 carries `symbolism-clause-map.md`; the r94 fixture does not. The contract required preserving excerpts and bibliography, and both are byte-checked above; stated as a fact for the coverage/inventory seats.

## Commands run and observed results

1. `python3 corpus/fixtures/check_bible.py corpus/fixtures/r94-paired-crossing` → `CLEAN: schema, citations, relations, timeline; 0 violations` (exit 0)
2. `python3 corpus/tools/support_check.py corpus/fixtures/r94-paired-crossing` → `INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16; DISTINCT-ANCHORS 12/12` … `RESULT PASS` (exit 0); J05 found at 17, J10 at 18, J11 at 19, J14 at 20
3. `python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing` → `OBLIGATIONS raw=14 mapped=14` / `RESULT PASS` (exit 0) — no unmapped raw obligation, supporting completeness of the trace above
4. Independent census (`python3`, source-attributed fields): `total source-attributed obligations: 14`; `attributed to crossing-minute (new): 4`; `by source: {'paired-clock': 10, 'crossing-minute': 4}`
5. Clause-substring entailment script: every new-record key phrase found on its cited line (`met at the Chalk Stair` → 18 True; `they agreed` / `for this crossing only` / `share stewardship of the Chalk Stair` → 19 True; `depends on both ninth-bell entries` / `north-lantern entry at Quiet Rise` / `south-bell entry at Salt Court` / `chalked one temporary route mark` → 20 True)
6. Overreach term sweep (`grep -rniE "alliance|perpetual|continuing|ongoing|forever|always|entire|complete contents|full contents|only record|nothing else|witness"`) → only disclaimer lines (`sources.json:18`, `README.md:9,17`, `claim-excerpt-map.md:39,48`); raw-JSON blob check → all ten probe terms False
7. Preservation diffs and parsed-value equality (outputs above); `git status --porcelain` → `?? .ufo/waves/round-94/followup/` only

## Bottom line

**PASS** — all four new `crossing-minute` obligations and every new actor/place/agreement proposition are entailed by `fictional-excerpts.md:17-20` or by explicitly labeled editorial metadata (IDs/ticks/schema slot/conventions), with no contents, perpetual-performance, or alliance overreach.
