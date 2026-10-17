# V54 — crosscheck-depth (round 95)

Seat: V54 `verdict-crosscheck-depth`. Scope per seat spec: after V23 lands,
independently derive my own DEPTH verdict **from the evidence seats only** (not
from V23's text), then compare with V23 and explain any divergence. Leaf seat:
no nested agents, no commits, no network; this report plus my scratch dir
`.ufo/waves/round-95/seats/scratch/V54/` are my only writes.

Baseline: r94 closure `fb118c4` (HEAD unchanged through the round; delivered
revision = working tree: `M LOG.md`, `M corpus/tools/{map_obligations.py,
map-obligations-contract.json,README.md}`, `?? .ufo/waves/round-95/`,
`?? corpus/fixtures/r95-crossing-aftermath/`,
`?? corpus/knowledge/r95-aftermath-scope-note.md`).

Method (order matters for the crosscheck): I froze my own verdict from the
evidence-seat reports at `scratch/V54/my-verdict-frozen.md` (~16:30 local)
**before my first read of `V23-verdict-depth.md`**; only then did I read V23 and
compare. My own read-only replays are reported separately as secondary
corroboration, never as the derivation basis.

---

## 1. Evidence seats used (the basis of my independent verdict)

Depth-evidence cluster (7 designated seats, V23's own poll target):

| Seat | Report | Raw evidence it contributes (as I read it) |
|---|---|---|
| V08 c2-checker | `seats/V08-c2-checker.md` | `check_bible` CLEAN exit 0 twice on stable hashes; counts 5/1/4/4; `aftermath-missing-evin` tick 11 `depends_on == ["paired-crossing-decision"]`; independent ID-integrity scan CLEAN; r94 still CLEAN + untouched; byte copies exact, JSON pure appends; only negated duty/breach tokens. PASS |
| V09 c2-inherited-equality | `/home/vgpnk/Projects/shokunin/.ufo/waves/round-95/seats/V09-c2-inherited-equality.md` (**parent repo — misplaced, not in the lane's seats dir**; sha256 `a5c859ea1361ff549f5e28fd32b6cb3a0aaefaeb6d69294e2baa45e9657025b9`) | All 12 inherited JSON rows parsed-value identical with **key-order-sensitive** OrderedDict equality; r94 untouched at **blob level** (10/10 `git hash-object` = `fb118c4` blobs); excerpt 1116-byte prefix; new rows match spec; flags P3's "14 inherited rows" label vs 12 actual JSON rows (minor label slip). PASS |
| V10 c2-support-map | `seats/V10-c2-support-map.md` | `support_check` 15/15 + 2/2 PASS; `map_obligations` raw=15 mapped=15 PASS (settled rev `d1c239cc…`); 14 inherited map rows parse-value identical; census 169 total / 168 excluding r95; adversarial probes: J15 row deletion → `missing_obligation` exit 1, source-ID corruption → `source_id_mismatch` exit 1. PASS |
| V11 c2-anchors | `seats/V11-c2-anchors.md` | Own `grep -nF` + pure-Python scan: 15/15 JSON + 2/2 editorial anchors in-span; every inherited anchor byte-identical and at the same r94 line numbers; J15 anchor only at `fictional-excerpts.md:26` inside appended lines 21–31; zero drift. PASS |
| V12 c2-whole-claim | `seats/V12-c2-whole-claim.md` | Whole-proposition trace: all four note propositions map to excerpt clauses + JSON rows; description fields do not out-claim; all duty/breach/perpetual/identity mentions negated (13 classified lines); inheritance byte/value-exact; notes O1–O4. PASS |
| V13 c2-anti-overclaim | `seats/V13-c2-anti-overclaim.md` (landed 16:30:10) | Adversarial overclaim sweep of every new byte: no canon-truth/rights/perpetual/breach/identity overclaim survives unbounded; "the agreed bell" bounded by report frame in all layers; low-severity residuals (stale tool-scope phrase = under-claim; citation boundary 2 lines short; inherited ambiguity clause; no in-place bell gloss). PASS |
| V14 c2-dependency-probe | `seats/V14-c2-dependency-probe.md` | Dependency mutations on scratch copies: unknown id / tick inversion / removed tick-10 row all report exit 1; **dropping `depends_on` stays CLEAN exit 0** → `check_bible` has no dependency-presence rule (blind spot, reported not forced); live fixture byte-stable. PASS |

Corroborating seats (independent replicas / adjacent evidence) I also used:

- V35 `anchor-replica-2` — third independent method, 15/15 in-span, 0 misses; R9 declaration `12-29` vs J15 span `22-31` granularity nit. PASS.
- V36 `whole-claim-replica-2` — five adversarial broader-duty constructions all fail; "the agreed bell" = bounded referent gap, not an asserted duty. PASS.
- V50 `byte-prefix` — five files `cmp`-identical; excerpt exact 1116-byte prefix + 729-byte append; JSON append-only; r94 matches `fb118c4` blobs. PASS. (Adjacent note: r95 map is **not** a byte copy — namespace column rewritten; "14 inherited rows unchanged" holds at pointer/span/mode/anchor level.)
- V16 `preservation-mutations` — span break → `support_check` FAIL; dropped row → `missing_obligation`; source-ID → `source_id_mismatch`; schema-drift class → exit 1 vs old silent PASS; live fixture byte-identical throughout. PASS.
- V45 `census-paths` — all three checkers pass with repo-relative argv, stdout byte-identical across path forms. PASS (with a transient P2-contract caveat that later cleared).
- V43 `knowledge-note` — P5's note's receipts/pins reproduce; "reported non-performance" is a new observation class; minor citation-form observations. PASS.
- V20 `doc-parity` — pre-integration census 168 dirs / 34 exit0 / 134 exit1 / 421 violations; one added directory, zero changed inherited tuples.
- V17 `gates-boundary` — pinned byte classes (boundary doc, `check_bible.py`) unchanged across the whole round window.

No evidence seat reports a FAIL, a counterexample against the delivered fixture,
or a scope overclaim that survives unbounded.

## 2. My independent DEPTH verdict (frozen before reading V23)

**DEPTH — IMPROVED (bounded).** On the delivered bytes, C2's before→after
verifies: 5/1/3→5/1/4 entities/relations/events, 3→4 sources, 14→15 map
obligations (14 inherited rows unchanged + 1 new event row; no new
claims/entities/relations), `check_bible` CLEAN exit 0, census 168→169 with zero
inherited changes, and crossing-only scope with every duty/breach/perpetual/
identity token negated. The "first reported non-performance against a
crossing-scoped agreement" class is corroborated as new to the fixture corpus
(V43 §6 class note; my own scan in §4 below).

Bounds I attached (from evidence seats only):

- B1 one authored fixture; evidence is structural/lexical + hand review, not
  authentication/entailment (V08, V10, V12, V14 scopes).
- B2 `check_bible` cannot detect a dropped `depends_on` edge (V14 probe (a));
  the tick-11→tick-10 link is prose + map-asserted, not gate-enforced.
- B3 "14 inherited rows carried unchanged" holds at pointer/span/mode/anchor
  level; the map file itself is re-qualified, not a byte copy (V50 obs 1, V10).
- B4 "the agreed bell" referent gap (V12 O1, V36 §4A) — bounded ambiguity.
- B5 J15's edge wording encodes posteriority/reference, not a literal "depends
  on" clause (V12 O2) — precision note.
- B6 P3's "14 inherited rows" label vs 12 actual JSON rows (V09 Step 2) — label
  slip, equality itself verified.
- B7 evidence-cluster completeness: at my freeze V09's report was only at the
  parent path and V13 had not landed; both later confirmed PASS (V09 16:23:48
  parent path; V13 16:30:10 lane path) and neither changes the verdict.

## 3. V23's verdict (on disk, revision of 16:30:22)

> **DEPTH — IMPROVED (bounded).** … before r94 = 5/1/3 …, 3 sources, 14 map
> obligations … after r95 = 5/1/4, 4 sources, 15 map obligations (14 inherited
> rows carried unchanged + the new tick-11 event row …), `check_bible` CLEAN
> exit 0, census 168→169 with zero inherited changes, and the scope discipline
> (crossing-only; no breach/other-duty assertion) verified by adversarial
> whole-claim review. (V23 §7)

Named bounds in V23 §7: structural/lexical only; "first" is corpus-bounded;
checker blind spot (dropped `depends_on`); tool-revision flux (settled
`d1c239cc…`, 22-case contract); preservation at named levels (map not
byte-identical); carried ambiguities (bell referent, R9 declaration `12-29` vs
span `22-31`, `kind` flag). Bottom line: "PASS — DEPTH verdict: improved
(bounded) … two absent designated seats: V09/V13."

## 4. Comparison — convergence and divergence

**Convergence.** My independent verdict and V23's agree in class (improved,
bounded) and on every load-bearing measurement: 5/1/4, 4 sources, 14→15 map
obligations, CLEAN/PASS receipts, census 168→169, byte/value/prefix preservation,
scope discipline, and the dependency-presence blind spot. I re-derived each of
these from the evidence seats before reading V23; nothing in V23 changed my
verdict, and nothing in my basis contradicts V23's §2–§6.

**Divergences, explained:**

1. **"Two absent designated seats" is superseded.** V23's absence claim was
   true only through its poll cutoff (try 40, 16:30:04) and only lane-relative.
   V13 landed at 16:30:10 (6 s after cutoff), and V09's report existed since
   16:23:48 at the **parent** path
   `/home/vgpnk/Projects/shokunin/.ufo/waves/round-95/seats/V09-c2-inherited-equality.md`
   (a cwd-resolution stray of the kind V08's process note describes for
   V14/V30). I read both: **V09 PASS** (12 inherited rows key-order-sensitive
   equal; r94 blob-untouched) and **V13 PASS** (no surviving overclaim). Neither
   changes V23's verdict; V09 adds bound B6 (P3's "14 vs 12 rows" label slip)
   that V23 does not name, and V13's residuals are under-claims/citation-form
   only. V23's bottom-line phrase "two absent designated seats" should be read
   as "two seats not available at cutoff", not "two seats' evidence missing from
   the round".
2. **V23's report was revised during my crosscheck window** (mtime 16:30:22,
   size 13884 B). At the revision I first read (pre-16:30:22), §8's bullet read
   "V09/V10/V13 ABSENT at 16:26:25 …", which contradicted its own §6 (V10
   present, PASS, landed 16:28). The on-disk revision now reads "V09/V13 ABSENT
   through the poll cutoff (try 40, 16:30:04)" and is self-consistent. Verdict
   unaffected; recorded because report revision mid-crosscheck is a
   reproducibility observation.
3. **Basis differences (additive, no conflict).** V23's stated basis: V08, V10,
   V11, V12, V14 + V35, V36, V44, V50, V20, V24 §3. Mine additionally used V09,
   V13, V16, V17, V43, V45. Conversely, V23 ran its own corpus-wide
   "first"-class bounding (§5: wording scan; r23 thing-not-found vs r83
   nonsighting) that I had taken from V43 §6. I re-ran that scan myself as a
   crosscheck (below): no non-r95 fixture carries the non-arrival wording class,
   and r23's note is "did not find it" (thing-not-found) — V23's bounding holds.
4. **Bound-set differences.** V23 names the R9 declaration `12-29` vs span
   `22-31` granularity nit and the `kind` flag; I names B6 (12-vs-14 label) and
   B5 (edge wording). The union is consistent; no bound conflicts, and both sets
   carry the blind spot and map-level preservation bounds.

## 5. My own replays (secondary corroboration; commands + observed output)

```
$ git ls-tree -d --name-only fb118c4 corpus/fixtures/ | wc -l   → 168
$ find corpus/fixtures -mindepth 1 -maxdepth 1 -type d | wc -l  → 169
$ git diff --stat fb118c4 -- corpus/fixtures/r94-paired-crossing \
    corpus/tools/support_check.py corpus/fixtures/check_bible.py → (empty; rc=0)

$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath
CLEAN: schema, citations, relations, timeline; 0 violations   exit=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
RESULT PASS                                                   exit=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing
OBLIGATIONS raw=14 mapped=14  …  RESULT PASS                  exit=0
$ python3 corpus/tools/map_obligations.py --self-test
22 × SELF-TEST PASS … RESULT PASS                             exit=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r95-crossing-aftermath
SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS 2/2; MODES 17/17; VALIDATED-ROWS 17/17
RESULT PASS                                                   exit=0

$ grep -rniE "did not come|did not arrive|didn't come|failed to come|no-show|never came|did not appear|did not show" corpus/
→ only corpus/knowledge/r95-aftermath-scope-note.md:13 (the round's own note, naming r23); zero fixture hits outside r95
$ grep -rn "did not find" corpus/fixtures/r23-note-class/
→ sella-absence-note-excerpt.md:5 "I did not find it there." (thing-not-found class)
```

Tool revisions at my replays: `map_obligations.py`
`d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108`, contract
`8173bb97592a377716866737e8fcb4043014c9814e77a6248500d301a39170db` (22 cases),
`check_bible.py` `ff9fd2aa…`, `support_check.py` `55a5eb27…`. Fixture hashes
stable across my whole window (all ten equal to V08/V10/V12 captures, e.g.
`claim-excerpt-map.md 30281ff1…`, `timeline.json 3c0faad6…`,
`fictional-excerpts.md 0ef6734a…`).

## 6. Effect of late evidence

None on the verdict. V09 (inherited equality) and V13 (anti-overclaim) are both
PASS and corroborate the same delivered bytes; V09's only new item is a
count-label slip in P3's report (equality itself holds); V13's items are
under-claims and citation-form notes. Had V23 had them at cutoff, its §6 list
would gain two PASS entries and its bound set the 12-vs-14 label item; the
verdict line would not move.

## 7. Process observations for the integrator (not verdict items)

- **V09's report is misplaced**: written to
  `/home/vgpnk/Projects/shokunin/.ufo/waves/round-95/seats/V09-c2-inherited-equality.md`
  (parent repo), not the lane's seats dir. It is a designated C2 evidence seat
  and must be collected into `.ufo/waves/round-95/seats/` at closure; its
  content is complete and PASS. `V30-shonen-format.md` also sits in the parent
  path (V23 §8 noted it).
- V23's report was edited after its first landing (16:30:22); the on-disk
  revision is the one to cite.
- P4's report "Addendum — post-P1 re-run" is still empty at my read (V12 §7,
  V23 §8 concur) — P4's receipt to fill.
- Transient `map-obligations-self-test-*` repo-root temp dirs appeared/cleaned
  (V17, V36); none remain.

## Bottom line

**PASS — crosscheck complete: my independent depth verdict, derived from the
evidence seats (V08, V09, V10, V11, V12, V13, V14 + replicas V35/V36/V50 and
adjacent V16/V17/V20/V43/V44/V45) before reading V23, matches V23's "DEPTH —
IMPROVED (bounded)"; the only divergences are editorial/additive (V23's
"V09/V13 absent" is cutoff-relative — both now exist and PASS, with V09 stranded
in the parent repo; V23's report was revised mid-crosscheck to drop a stale
V10-absent bullet; bound-set differences are a consistent union), and none
changes the verdict.**
