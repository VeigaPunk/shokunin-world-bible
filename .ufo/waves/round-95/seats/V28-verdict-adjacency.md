# V28 — verdict-adjacency (round 95)

**Seat:** V28 verdict-adjacency, round-95 single wave, lane `lore-shokunin`.
**Subject:** the delivered r95 working tree vs baseline r94 closure `fb118c4` (`fb118c42038ed27a747eec704b9aab41bb4b2ebe`). No r95 commit exists (hard rule: no commits), so every measurement below is **worktree-vs-baseline**, not commit-range.
**Mandate:** read V22 (adjacency evidence seat), run my own PROVINCE diff, issue exactly one ADJACENCY verdict. This seat makes no C1/C2/C3 verdict, no admission verdict, and no lore-truth ruling.
**Inputs read:** `.ufo/waves/round-95/seats/V22-adjacency.md` (199 lines; poll-waited for it — first poll check 16:17:09, my loop observed `V22=[V22-adjacency.md]` at 16:31:48, 20 s cadence, well inside the 40-try cutoff). V22's own bottom line is PASS with caveats; I re-ran the load-bearing checks myself below rather than repeating its numbers.
**Measurement freeze:** all five producer reports present; P1 report 16:28:01, P2 report 16:29:32; producer artifact mtimes all precede their report mtimes (tool 16:26:27, contract 16:27:02, tools README 16:28:26, knowledge note 16:25:15). My final battery ran 16:31–16:34 -03:00; the tool blob was stable through it (`2077a145…`).

---

## 1. My own PROVINCE diff

### 1.1 The charter itself

```
$ git rev-parse fb118c4:PROVINCE.md
7c599c395e1710b6a7c7aca6d485c373bed6deb7
$ git hash-object PROVINCE.md
7c599c395e1710b6a7c7aca6d485c373bed6deb7
$ sha256sum PROVINCE.md
94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa  PROVINCE.md
$ git show fb118c4:PROVINCE.md | sha256sum
94a7a77e1810f37fff6aa89d427f6b0bdc2894ecb3527f598a045afda27262aa  -
$ git diff fb118c4 -- PROVINCE.md | wc -c
0
```

Blob, sha256, and the byte diff all agree: the province charter is byte-identical across the round.

### 1.2 Province-scope diff of the round

```
$ git diff --name-status fb118c4
M	LOG.md
M	corpus/tools/README.md
M	corpus/tools/map-obligations-contract.json
M	corpus/tools/map_obligations.py

$ git status --porcelain -uall | grep '^??' | grep -v '^?? \.ufo/waves/round-95/'
?? corpus/fixtures/r95-crossing-aftermath/README.md
?? corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md
?? corpus/fixtures/r95-crossing-aftermath/contradictions.json
?? corpus/fixtures/r95-crossing-aftermath/entities.json
?? corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md
?? corpus/fixtures/r95-crossing-aftermath/inspiration-note.md
?? corpus/fixtures/r95-crossing-aftermath/relations.json
?? corpus/fixtures/r95-crossing-aftermath/source-excerpt.md
?? corpus/fixtures/r95-crossing-aftermath/sources.json
?? corpus/fixtures/r95-crossing-aftermath/timeline.json
?? corpus/knowledge/r95-aftermath-scope-note.md
```

The tracked change set is exactly the three declared P1/P2 byte-owned tool files plus the pre-dispatch `LOG.md` declaration; the untracked set outside the round directory is exactly the 11 declared P3/P4/P5 corpus additions. Everything else untracked lives under `.ufo/waves/round-95/` (seat reports and seat scratch). Charter-adjacent and earlier-round bytes are untouched:

```
$ git diff --stat fb118c4 -- PROVINCE.md SHONEN.md SKILL.md README.md SCORECARD.md l0-questions.md \
    corpus/fixtures/r94-paired-crossing corpus/fixtures/r88-m3-maya-cluster \
    corpus/fixtures/r87-myth-cluster corpus/fixtures/r93-m2-kojiki-cluster | wc -l
0
```

`git diff --name-only fb118c4 -- .ufo/waves/ | grep -v round-95` → empty (no past wave touched).

**Result: PASS — the round's diff stays inside the lane and inside the declared byte-ownership; the charter that defines the province is unchanged.**

---

## 2. Independent corroboration of the adjacency evidence (V22)

### 2.1 No sibling-lane or domain-tree writes

```
$ cd /home/vgpnk/Projects/shokunin && for d in *-shokunin; do
    n=$(find "$d" -newermt "2026-10-17 16:16" -type f -not -path "*/.git/*" | wc -l); [ "$n" -gt 0 ] && echo "$n $d"; done
43 kotodama-shokunin
905 lore-shokunin
```

Only `kotodama-shokunin` (its own concurrent round-7 work — own reports/tools/examples, its own dirty tree) and `lore-shokunin` itself have in-window content writes. Content-level leak grep:

```
$ grep -rl "r95-crossing-aftermath\|aftermath-missing-evin\|aru-aftermath-note\|r95-aftermath-scope" \
    /home/vgpnk/Projects/shokunin/*-shokunin --include='*.md' --include='*.json' --include='*.py' | grep -v lore-shokunin
(empty)
```

Observed nuance, not a seat write: every sibling lane's `.git` **directory entry** (not contents) has mtime 16:17:16 — an external fleet scan; no sibling content file is attributable to an r95 lore seat.

### 2.2 Mythology stays editorial-only in the new bytes

```
$ grep -n -iE "(spence|etcs|kojiki|chamberlain|gutenberg|inana|ovid|kiche)" corpus/fixtures/r95-crossing-aftermath/*.json
(none)
$ python3 -c "…counts…"
entities 5 / relations 1 / events 4 / sources 4 / contradictions []
```

All four declared sources are `kind: fictional *`; the added `aru-aftermath-note` binds only in-world fiction. The inherited Spence material stays in the two `editorial-row` comparisons and the copied `inspiration-note.md`/`source-excerpt.md` (byte copies), with explicit refusals in the new bytes — e.g. `README.md:19` "It supplies no in-world witness, cultural authority, or fictional canon…"; `claim-excerpt-map.md:40` "they do not make Spence an in-world witness, assign cultural meaning, or add canon."; `r95-aftermath-scope-note.md:7` "not merged canon, not a breach finding, and not a verdict on any character."

Inheritance checks I ran myself:

```
$ for f in entities.json relations.json contradictions.json inspiration-note.md source-excerpt.md; do cmp -s r94/$f r95/$f && echo IDENTICAL $f; done
IDENTICAL entities.json / relations.json / contradictions.json / inspiration-note.md / source-excerpt.md
$ head -c 1116 corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md | cmp - <(git show fb118c4:…/r94-paired-crossing/fictional-excerpts.md)
r94 bytes are strict prefix
```

### 2.3 Rights / canon / mechanics scan over every r95 new byte

Pattern `public domain|licen[cs]e|copyright|permission|rights|canon|mechanic|gameplay|ruleset|damage|stats|balancing` over the 10 fixture files, the knowledge note, `corpus/tools/README.md` and the contract → **25 raw hits, every one a refusal, an open question, a scope limit, or the JSON-Pointer sense of "canonical"** (e.g. `inspiration-note.md:13,17` open `## Rights question` / `## AI-training-permission question`; `claim-excerpt-map.md:1,16` "canonical" pointers; `r95-aftermath-scope-note.md:32` "decides truth, breach, chronology, rights, permission, or canon" as a non-capability; `README.md:99` "does not judge … rights, permission, or canon"). No positive rights finding, no permission grant, no canon assertion, no mechanics term anywhere.

### 2.4 Delivered-revision pin and live tool behavior

My pin matches V22's independently:

```
$ git hash-object corpus/tools/map_obligations.py
2077a145cd00c5f88bfdbf3a00bf96139a546092
$ sha256sum corpus/tools/map_obligations.py
d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108
```

I ran the delivered self-test myself (22/22 PASS lines including the two new cases, `RESULT PASS`, exit 0) and confirmed it writes nothing into the corpus:

```
$ B=$(find corpus -type f | sort | xargs sha256sum | sha256sum | cut -d' ' -f1); python3 corpus/tools/map_obligations.py --self-test; A=$(…)
SELF-TEST PASS map_missing exit=2 findings=['map_missing']
SELF-TEST PASS invalid_arguments exit=2 findings=['invalid_arguments']
… 22 lines … RESULT PASS
exit=0
CORPUS UNCHANGED
```

### 2.5 BR-05 scratch — the one live boundary behavior

`map_obligations.py:56` `ROOT = Path(__file__).resolve().parents[2]`; `:720` `with tempfile.TemporaryDirectory(prefix="map-obligations-self-test-", dir=ROOT)`. During concurrent verifier self-tests I observed live scratch in the lane root:

```
$ git status --porcelain   (16:27)
?? map-obligations-self-test-s_dovblw/…
?? map-obligations-self-test-tat_6gyp/…
```

After my own run, `ls -d map-obligations-self-test-*` → none (auto-cleaned, no persistent residue). The residual is now explicitly documented by P2: `corpus/tools/README.md:99` ("Self-test scratch is created under the repository root and is not gitignored (bounded residual BR-05, relocation candidate for r95)") and `:103` ("unchanged in r95"). Lane-internal and self-cleaning, so not a province breach — reported as found.

---

## 3. Observations reported as found (not breaches)

1. **`/tmp` scratch practice.** `find /tmp -maxdepth 1 -newermt "2026-10-17 16:16" | grep -icE "r95|map_obligations|p1-|census"` → `27` lore-named entries (P1 probes, V-seat snapshots; V22 counted 43 with a wider pattern). P1's report discloses it. `/tmp` is machine-local, not a sibling repository or domain source tree, so not a `PROVINCE.md:11` breach; it is a protocol-level deviation from the round's stricter "write ONLY your exclusive report path plus seat-scratch" rule — bounded follow-up for the integrator.
2. **Seat scratch dirs** (`.ufo/waves/round-95/seats/*-scratch/`, `.ufo/waves/round-95/scratch/V20/`) are all inside the round directory; no stray lane files elsewhere.
3. **Mid-flight transients disclosed by producers** (P3's transient `self_test_contract` exit 2 while the contract still said 20 cases; P2's transient `invalid_arguments` gap). On the delivered bytes the contract declares 22 cases and my own `--self-test` run is 22/22 PASS exit 0; both transients are self-reported history, not present state.
4. **No post-report rewrites observed:** tool 16:26:27 < P1 report 16:28:01; contract 16:27:02 and tools README 16:28:26 < P2 report 16:29:32.

## Limits

- Sibling-write coverage is a bounded in-window mtime sweep (content files) plus a string-leak grep, not a full cross-repo commit audit; kotodama's concurrent activity is attributed by path ownership and its own commit history, not by process tracing.
- V22's `/tmp` count (43) and mine (27) differ because of pattern width; both are listings, neither is a complete machine-wide audit.
- This seat re-ran the delivered self-test (which transiently creates the BR-05 lane-root scratch) but no other mutating command; my only write is this report.

---

## Verdict — ADJACENCY: **PASS**

The delivered r95 revision is province-clean: `PROVINCE.md` is byte-identical to `fb118c4` (blob `7c599c39`, sha256 `94a7a77e…`, empty diff); the entire change set is the three declared P1/P2 tool files, the 11 declared P3/P4/P5 corpus additions, and the append-only `LOG.md` declaration, with no writes to sibling lanes, domain trees, past waves, charters, or earlier fixtures; mythology remains editorial-only (no external comparator bound in any fixture JSON, Spence rows labelled `editorial-row`, explicit no-witness/no-canon refusals in the new bytes); and the rights/canon/mechanics scan over every r95 new byte returns only refusals, open questions, and JSON-Pointer "canonical" uses. The only caveats are the disclosed, transient, lane-internal BR-05 self-test scratch under the repository root (`map_obligations.py:720`, documented at `corpus/tools/README.md:99,103`) and the disclosed `/tmp` scratch practice — both reported as found and neither a province breach.

**Bottom line: PASS — r95 stays inside the lore province on the delivered revision; the sole caveats are the disclosed transient BR-05 lane-root self-test scratch and the disclosed `/tmp` scratch practice, neither a sibling-lane or charter breach.**
