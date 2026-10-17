# JCOV4 — Coverage judge #4 (fresh-eyes province audit), round 89

Seat: coverage critic, fresh eyes. Judged on the delivered tree only
(`1b09f3f`, baseline `51b286b`, tracked tree clean). Prior critics
(`round-87/followup/JCOV*`, `round-88/followup/JCOV*`) were deliberately not
read before this audit; `C7.md` and `K1.md` were read only at the required
comparison step, after the independent findings below were formed.

## Work performed

- **Axes:** (1) do the four delivered in-world excerpts + the ETCSL ledger
  marker support the coverage claim under the D1/R5 support rule; (2) do they
  respect lore `PROVINCE.md` refusals; (3) do they keep the three-question rule
  (attribution / rights / AI-training permission) intact; (4) do they stay on
  lore's side of the kotodama boundary.
- Read, on the delivered tree: `PROVINCE.md`; the four new excerpts
  (`gate-witness`, `dune-register`, `shell-charter`, `tide-bell-tally`) and the
  pre-existing `lowwater-hymn-excerpt.md` + `symbolism-clause-map.md`; the r87
  cluster JSON; the `reference-ledger.md` ETCSL row (r89 diff); the R8–R10 rows
  and r89 integration notes in `r88-sourced-inspiration-decision-table.md`;
  `r89-cross-cluster-contradiction.md`; the R9 fixture
  (`r89-inspiration-paraphrase/`); `kotodama-shokunin/PROVINCE.md` + `SKILL.md`
  + the now-tracked `worldbible-integration-contract.md`; `l0-questions.md`.
- Ran the probes recorded below against the committed tree. Scratch was
  `/tmp`-only; the sole repository write by this seat is this report. No
  commit, push, or tracked edit.
- Two timed 60-second dependency checks were run (log
  `/tmp/lore-r89-jcov4-wait.log`); my dependencies (`C7.md`, `K1.md`) were
  already present, so the checks confirmed no new follow-up artifacts were
  needed before judging.

## Before → after measurements

**Fixture replays (delivered tree).** Exact commands and outputs:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-myth-cluster; echo "exit=$?"
python3 corpus/fixtures/check_bible.py corpus/fixtures/r89-inspiration-paraphrase; echo "exit=$?"
```

```text
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
```

**Fixed-string anchor sweep of the 14 new facts against the delivered excerpts.**
Exact command (S2 map anchors vs delivered excerpt files):

```sh
python3 - <<'PY'
from pathlib import Path
import json
root=Path('corpus/fixtures/r87-myth-cluster')
facts=json.loads(Path('.ufo/waves/round-89/patches/S2-fact-map.json').read_text())['facts']
matched=[]
for fact in facts:
    p=root/f"{fact['source_id']}-excerpt.md"
    hits=[i for i,line in enumerate(p.read_text().splitlines(),1) if fact['anchor_phrase'] in line] if p.exists() else []
    print(f"{fact['id']} {fact['source_id']} anchor_match_lines={hits}")
    if hits: matched.append(fact['id'])
print(f"delivered_fixed_string_anchors={len(matched)}/{len(facts)}")
PY
```

Observed output:

```text
E1 gate-witness anchor_match_lines=[5]
E2 dune-register anchor_match_lines=[5]
E3 dune-register anchor_match_lines=[6]
E4 shell-charter anchor_match_lines=[7]
E5 shell-charter anchor_match_lines=[8]
E6 tide-bell-tally anchor_match_lines=[9]
R1 shell-charter anchor_match_lines=[9]
R2 shell-charter anchor_match_lines=[10]
R3 shell-charter anchor_match_lines=[11]
R4 dune-register anchor_match_lines=[7]
T1 gate-witness anchor_match_lines=[6]
T2 tide-bell-tally anchor_match_lines=[10]
T3 gate-witness anchor_match_lines=[7]
T4 dune-register anchor_match_lines=[8]
delivered_fixed_string_anchors=14/14
```

**Coverage denominator and pointer resolution.** Exact command:

```sh
python3 - <<'PY'
from pathlib import Path
import json
p=Path("corpus/fixtures/r87-myth-cluster")
sources={x["id"] for x in json.loads((p/"sources.json").read_text())}
entities=json.loads((p/"entities.json").read_text()); relations=json.loads((p/"relations.json").read_text()); events=json.loads((p/"timeline.json").read_text())
prose={x.stem.removesuffix("-excerpt"):x.read_text() for x in p.glob("*-excerpt.md")}
pointers=[e["first_appearance"] for e in entities]
claims=[(c["source_id"],c["statement"]) for e in entities for c in e["claims"]]
print("delivered_excerpts=",sorted(prose))
print("facts=",len(pointers)+len(claims)+len(relations)+len(events))
print("pointers_resolve=",sum(s in sources for s in pointers),"/",len(pointers))
print("claim_source_ids_resolve=",sum(s in sources for s,_ in claims),"/",len(claims))
PY
```

Observed output:

```text
delivered_excerpts= ['dune-register', 'gate-witness', 'lowwater-hymn', 'shell-charter', 'tide-bell-tally']
facts= 22
pointers_resolve= 7 / 7
claim_source_ids_resolve= 7 / 7
```

So the delivered denominator is 22 facts = 7 entity claims + 7 `first_appearance`
pointers + 4 relation edges + 4 timeline events. The 14 new excerpts cover the
14 previously metadata-only facts; the pre-existing hymn excerpt carries the
Gate claim and the 7 pointers resolve. 14/14 anchors + 7/7 pointers + 1 hymn
claim is a **lexical preflight pass, not whole-claim certification**.

**ETCSL ledger marker (three-question rule + delivery status).** Exact command
and output:

```sh
grep -n "external-only\|unverified\|not delivered" corpus/knowledge/reference-ledger.md
```

```text
8:| University of Oxford, Electronic Text Corpus of Sumerian Literature (ETCSL), ... | The rights status of ETCSL's modern presentation, editorial work, and translation has not been determined here; ... | AI-training permission has not been assessed or established; public accessibility and attribution do not imply permission. | external-only / text not delivered at lore; citation is a research lead with verified line locators, not delivered support. Motif-level comparison only: ... Not an in-world source or canon. |
```

The four-column shape is preserved; attribution (cell 1), rights (cell 2), and
AI-training permission (cell 3) stay in separate cells; the `Use here` cell
states delivery status and calls the citation a research lead, not delivered
support. No rights conclusion is asserted.

**Stale documentation probe.** Exact command and output:

```sh
grep -c "gate-witness-excerpt\|dune-register-excerpt\|shell-charter-excerpt\|tide-bell-tally-excerpt" corpus/fixtures/r87-myth-cluster/README.md
stat -c '%y %n' corpus/fixtures/r87-myth-cluster/README.md
git log --oneline -1 -- corpus/fixtures/r87-myth-cluster/README.md
```

```text
0
2026-10-17 01:37:02.919181544 -0300 corpus/fixtures/r87-myth-cluster/README.md
e4708cb lore r87 C3: r87-myth-cluster world-bible fixture ...
```

The cluster README is unchanged since r87 and mentions none of the four new
support excerpts. `corpus/fixtures/README.md` has Round 87 and Round 88
sections (`grep -n "Round 8"` → lines 1004, 1008) but no Round 89 section.

**Register presence probe.** `ls corpus/knowledge/cross-cluster-contradictions.md`
→ `No such file or directory` (the R10 live register is correctly not created).

**Real-world token scan of the new excerpts.** Exact command:

```sh
grep -niE "kojid|etcsl|sumer|inana|maya|spence|völusp|gutenberg|http" corpus/fixtures/r87-myth-cluster/*-excerpt.md
```

→ no matches. The four fictional excerpts introduce no real-world reference, so
the three-question ledger rule is not engaged by them.

## Findings & named debt

- **Coverage — improved (bounded).** The four excerpts land and deliver one
  source-local, grep-hittable anchor for each of the 14 previously
  metadata-only facts; the denominator is 22 and pointers/claims resolve 7/7.
  Both fixtures replay `CLEAN`, exit 0. On the delivered tree this is the
  strongest coverage state the lane has held for the r87 cluster.
- **PROVINCE refusals respected.** No canon is claimed without an in-world
  citation (each fact cites a delivered source); the Hara/Sen place
  disagreement is preserved and unresolved (`contradictions.json` is unchanged
  in `1b09f3f`; the two timeline events keep distinct places); no real-world
  rights claim is made; no game-mechanics verification is attempted. The
  ledger's `external-only` marker asserts no rights and keeps the three
  questions separate.
- **Named debt D1 — no in-corpus claim-to-excerpt map (agrees with C7).** The
  R5 support row requires the claim be mapped "to the exact delivered excerpt
  path and line span". On the delivered tree there is no such map inside the
  corpus: `r87-myth-cluster/` contains only `symbolism-clause-map.md` (hymn, 8
  clauses) and the excerpt files. The per-claim path/line evidence lives only
  in the wave-scratch `.ufo/waves/round-89/patches/M4-verify.json`. So the
  "22/22" is reproducible from scratch evidence, not certifiable from the
  delivered corpus alone. Bounded, not a harm: the anchors do match.
- **Named debt D2 — R9 delivery-mode declaration absent (new finding).** The
  four new excerpts declare no delivery mode (`verbatim` / `translation` /
  `paraphrase` / `summary`), and no claim-to-excerpt map entry carries one.
  R9's r89 integration note scopes the rule "from r89 onward" but says "the
  r87/r88 clusters are annotated at their next content touch". Delivering four
  new excerpts into the r87 cluster *is* a content touch at r89, so the
  exemption does not cleanly cover this case: the four excerpts are the
  cluster's newest content and carry no mode label. Either declare the mode on
  these excerpts (they read as authored source text → `verbatim` of the
  fictional source) or record explicitly why the r87 touch is exempt.
- **Named debt D3 — stale cluster documentation.** `r87-myth-cluster/README.md`
  (r87 mtime) documents only `lowwater-hymn-excerpt.md` and
  `symbolism-clause-map.md`; it names none of the four new support excerpts, and
  `corpus/fixtures/README.md` has no Round 89 section. A reader replaying the
  README cannot discover the support text this round delivered. This is the
  same documentation-parity class the r88 closure had to repair.
- **Soft residual D4 — ETCSL marker literal.** The marker reads
  `external-only / text not delivered at lore`. The decision table's passage row
  asks the passage be marked `external-only / unverified`; the r88 soft debt F3
  (literal token absent) is therefore only partly closed — delivery status is
  now explicit and unambiguous, but the literal `unverified` token is still not
  present. Low severity; the meaning is correct.
- **Kotodama boundary — respected, one seam named.** The four excerpts are
  narrow attributed in-world records for existing r87 source IDs; they specify
  no belief system, symbolic grammar, or generative model, so they are record
  inputs on lore's side, not a kotodama system. The seam worth recording: lore
  is now *authoring* in-world source prose (a watch clause, a tally, a witness
  slip) to substantiate its own metadata claims, which sits adjacent to
  kotodama's generative province. No violation — the kotodama contract
  (`worldbible-integration-contract.md`) is now **tracked** in kotodama-shokunin
  and its §1 still says "initial bilateral acknowledgement is pending", and lore
  holds no acknowledgement record (`grep -rn "kotodama-lore-adjacency"` in lore
  → none). The r88 L0 line stands; the contract's authorship question is now
  partly answered (kotodama authored it) but lore's read/ack is still open.

### Comparison with C7.md and K1.md

**C7.md — agreements:**

- R3 anchor/pledge boundary: agree. C7 found the M4 scratch patch missed the
  then-current R3 anchor; on the delivered tree the S2 map's R3 anchor was
  updated to the pledge-framed phrase and now matches `shell-charter-excerpt.md:11`
  (`anchor_match_lines=[11]`). The substantive point C7 raised — keep R3 as
  pledge, not performance — is preserved in the delivered excerpt and the S2
  `anchor_note`.
- Locator/denominator debt: agree, and it stands on the delivered tree (D1).
  C7 said "strong scratch evidence, not a delivered-tree 22/22 certification";
  I confirm the map with path/line fields is still absent from the corpus.
- M5 ledger marker pass: agree. C7 verified it on scratch; I verify the marker
  is in the delivered ledger row with four cells and separate questions.
- D3/R10 is a hypothetical format demo, not a landed comparison: agree — the
  delivered `r89-cross-cluster-contradiction.md` states the second cluster is
  "hypothetical; absent from this repository" and the live register is not
  created (probe above).

**C7.md — disagreements / refinements:**

- C7's headline "22/22 remains unclosed" is right as a *certification* claim
  but understates what did land: on the delivered tree the 14 anchors match
  14/14 and the denominator resolves 22/22 at the lexical preflight level. My
  verdict is "improved (bounded)" rather than "unclosed".
- C7 did not name the R9 delivery-mode gap (D2) or the stale r87 README (D3).
  These are fresh-eyes additions.

**K1.md — agreements:**

- Role fit: agree that the excerpts are lore-side record inputs, not chousa
  method artifacts and not a kotodama generative system. My independent read
  reaches the same conclusion; I add the authoring-seam note above.
- The excerpts "do not establish authenticity, event truth, or canon": agree —
  the sources' reliability notes say unverified and the contradiction stays
  unresolved.

**K1.md — refinement:**

- K1 recorded the kotodama contract as untracked and pending
  (`?? .../worldbible-integration-contract.md`, `tracked=no`). On the tree as I
  read it the file is now **tracked** in kotodama-shokunin
  (`git ls-files --error-unmatch` succeeds). The contract's own §1 still marks
  bilateral acknowledgement pending, so K1's substantive point (no accepted
  handoff) stands, but its tracked-state line is now stale.

## Handoff

- **Verdict recommendation: coverage — `improved` (bounded).** The four
  excerpts and the ledger marker land and do what C2 claimed at the anchor
  level (14/14; 22 denominator resolves; both fixtures `CLEAN`); no PROVINCE
  refusal, three-question, or kotodama-boundary violation. Bounds: (D1) the
  R5 claim→path/line map is not delivered in-corpus; (D2) the four excerpts
  carry no R9 delivery-mode declaration despite the r89 content touch; (D3) the
  r87 cluster README and the fixtures README are stale; (D4) the ETCSL marker
  omits the decision table's literal `unverified` token.
- **Recommended cheap repairs for the closure commit:** add a claim-to-excerpt
  map (path + line span + delivery mode) to `r87-myth-cluster/` reusing the S2
  anchors; update `r87-myth-cluster/README.md` and `corpus/fixtures/README.md`
  (Round 89 section); optionally align the ETCSL marker to the literal
  `external-only / unverified`.
- Only `.ufo/waves/round-89/followup/JCOV4.md` was written by this seat. No
  commit, push, patch, or tracked source change; sibling repos read-only.
