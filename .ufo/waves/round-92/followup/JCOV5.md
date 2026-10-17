# JCOV5 — Sibling adjacency (round-92 FOLLOW-UP)

Seat JCOV5, world-bible lane. Mission: read-only check on the delivered tree `c4d4823`
(baseline `396c568`) — do the r92 artifacts (re-derived boundary doc, R8/R9 edge decisions,
Spence map rows, hardened support command, C9 watch re-check) read as chousa-shokunin or
kotodama-shokunin province; confirm the r90-landed chousa cross-references remain; note
kotodama's contract state.

Axes named: (1) **province fit** — each r92 artifact's action stays inside lore's declared
province; (2) **cross-reference integrity** — the r90 chousa pointers survive the r92 edits;
(3) **sibling-contract currency** — the kotodama adjacency contract's pinned/actual state and
lore's acknowledgement duty. Verdicts: (1) unchanged (fit holds), (2) unchanged (block
byte-identical), (3) unchanged on the lore side (still no ack) with a sibling-side divergence
recorded, below.

Scope discipline: tracked tree clean at start and end (`git status --porcelain
--untracked-files=no` → 0 lines; `git rev-parse HEAD` → `c4d4823…`); only untracked follow-up
artifacts moved. No commits/pushes; sibling repos read-only; this file is the seat's only
write; one scratch map under `/tmp` created and removed in-command (`ls` → "No such file or
directory").

## Work performed

- Read on the committed tree: `corpus/knowledge/holder-assessment-boundary.md` (671 lines),
  `corpus/knowledge/r88-sourced-inspiration-decision-table.md`, `corpus/knowledge/r91-c9-watch.md`,
  `corpus/tools/support_check.py` + `corpus/tools/README.md`, the r88-m3
  `claim-excerpt-map.md`, `corpus/fixtures/README.md` (r92 section), the r92 commit message
  and diffstat, `PROVINCE.md` (lore), and the r90 K1 method cross-reference block.
- Read-only sibling inspection: `chousa-shokunin/PROVINCE.md` and the three referenced chousa
  documents at their pointed spans; `kotodama-shokunin/PROVINCE.md`, its
  `corpus/knowledge/synthesis/worldbible-integration-contract.md` (committed blob and
  worktree copy), `SCORECARD.md`, `LOG.md`, and repo status; `l0-questions.md` and its history.
- Own measurements only: commit scope; extracted-block byte-diff of the chousa cross-reference
  block baseline→HEAD; `sha256sum` pins of the seven r92-touched/governing files; an
  added-line vocabulary scan of the r92 corpus diff; one support-check positive receipt and one
  failure probe; grep censuses for sibling names in lore's tree; sibling digest comparison and
  worktree status counts. Prior sibling artifacts were read afterwards as comparison only
  (E1/H1/H2/JCOV1/JCOV2/JCOV4/JDEP4/Q2), and are cited as corroboration, never as evidence.

## Before → after measurements

All commands from `/home/vgpnk/Projects/shokunin/lore-shokunin` unless a sibling path is named.

**1. Commit scope — 6 lore-side corpus files, zero sibling mentions.**

```sh
git diff --name-only 396c568 HEAD -- corpus/
git show --numstat HEAD | grep -i "chousa\|kotodama" | wc -l
```

```text
corpus/fixtures/README.md
corpus/fixtures/r88-m3-maya-cluster/claim-excerpt-map.md
corpus/knowledge/holder-assessment-boundary.md
corpus/knowledge/r88-sourced-inspiration-decision-table.md
corpus/knowledge/r91-c9-watch.md
corpus/tools/support_check.py
0
```

**2. Chousa cross-references — present and byte-identical to baseline.**

```sh
git show 396c568:corpus/knowledge/r88-sourced-inspiration-decision-table.md | sed -n '/Method cross-references/,$p' > /tmp/jcov5-baseline-refs.txt
sed -n '/Method cross-references/,$p' corpus/knowledge/r88-sourced-inspiration-decision-table.md > /tmp/jcov5-head-refs.txt
diff /tmp/jcov5-baseline-refs.txt /tmp/jcov5-head-refs.txt && echo "REFS IDENTICAL"
```

```text
REFS IDENTICAL
```

(The block sits at baseline `:126` and HEAD `:127` — shifted one line by the R8/R9 insert
above it; content unchanged.) Head block text, r92 lines 127-132:

```text
Method cross-references (r90, seat K1): R8/R9's screens re-derive limits already
documented by chousa-shokunin — claim-vs-source verification
(`chousa-shokunin/corpus/knowledge/claim-verification-r2.md:45-58`), archives
verified against live sources (`archives-verified-r9.md:177-185`), and
fixed-string anchor boundaries (`anchor-boundaries-r4.md:31-37`). Chousa owns
the research method; lore consumes it as record craft.
```

All three targets resolve in the sibling repo (files exist, cited spans in range):
`wc -l` → `claim-verification-r2.md 187`, `archives-verified-r9.md 267`,
`anchor-boundaries-r4.md 289`. Sampled content at the pointed spans: `claim-verification-r2.md:49-53`
= the source-boundary/refusal classes and byte-exact span check; `anchor-boundaries-r4.md:31-37`
= the substring/edge-boundary limit and round-4 falsifiable claim; `archives-verified-r9.md:177-185`
= the residual-distortion limit and "**verifying a conversion is not verifying the original**".
Observation, not a defect: the third label ("archives verified against live sources") is a
loose gloss of a span that states the archive-verification *limit*; r90 seat K1 printed these
same lines when it landed them (`.ufo/waves/round-90/K1.md:76-78`), so the pointer is
seat-verified, only its short label is coarse.

**3. Province-marker scan of the r92 added lines.** Added (`^+`) lines of
`git diff 396c568 HEAD -- corpus/`:

```text
source hierarchy: 0    hop: 0    citation chaining: 0    external fetch: 0
conlang: 0    phonology: 0    morphosynt: 0    naming system: 0    era periodization: 0
symbolism: 3    bibliograph: 2    translation: 4    printing: 4    edition: 2
```

Zero chousa-method markers and zero kotodama-generative markers; the counts are exactly the
two ambiguity surfaces reasoned below (Spence symbolism rows; R9 bibliographic/translation
gate). Literal sibling names in the whole r92 commit diff: `git diff 396c568 HEAD |
grep "^[+-].*\(chousa\|kotodama\)"` → no output.

**4. Artifact pins (delivered tree).**

```text
8e1fe8774a70f06c31efd783b4313a1639c1da4bcfd830be92134e8964536728  corpus/knowledge/holder-assessment-boundary.md
ee34c0d21c1b98cd5cd48eb482753e1187533eb3d438092cd1b1f32315e146a4  corpus/knowledge/r88-sourced-inspiration-decision-table.md
a6b2b9db92d494f390a414d1d84bfc4f074865f93e4ad4874cbfa7b9c95d9c77  corpus/knowledge/r91-c9-watch.md
55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  corpus/tools/support_check.py
bff849d19946c61bc30af43aea2fa6ec18e3dfe18f07e9cb97ea786e0f84728f  corpus/tools/README.md
b3b79fe5b5b9272b898b5714291739503c4250c415b3959032fcdba84a73fd43  corpus/fixtures/r88-m3-maya-cluster/claim-excerpt-map.md
e2eab01eef2f652626f39fb7543cf40c52248de1247cb18a0312504f28833ee1  corpus/fixtures/README.md
```

**5. Support command — one positive receipt, one failure probe.**

```sh
python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster
```

```text
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12; DISTINCT-ANCHORS 8/8
PASS S1: editorial-row; mode=verbatim; anchor=found; 5:> The beginning of this interesting book … He called out “Earth,” and the solid land appeared.
PASS S2: editorial-row; mode=verbatim; anchor=found; 5:> … He called out “Earth,” and the solid land appeared.
RECEIPT JSON-FACTS 10; EDITORIAL-ROWS 2; TOTAL-ROWS 12
SOURCE-SUPPORT 10/10; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 12/12; VALIDATED-ROWS 12/12
RESULT PASS
exit=0
```

Failure probe — committed r88-m3 map copied to `/tmp`, inventory line deleted, run with
`--map`, scratch removed in the same command:

```sh
sed -i '/^\*\*Expected inventory:\*\*/d' /tmp/jcov5-map.md
python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster --map /tmp/jcov5-map.md; echo "exit=$?"
```

```text
FAIL: map must contain exactly one expected inventory declaration
RESULT FAIL
exit=1
```

**6. Kotodama contract state (sibling, read-only).**

```sh
git -C kotodama-shokunin log --oneline -- corpus/knowledge/synthesis/worldbible-integration-contract.md
git -C kotodama-shokunin show 49ac1a5:corpus/knowledge/synthesis/worldbible-integration-contract.md | sha256sum
sha256sum kotodama-shokunin/corpus/knowledge/synthesis/worldbible-integration-contract.md
git -C kotodama-shokunin status --porcelain | awk '{print $1}' | sort | uniq -c
stat -c '%y %n' kotodama-shokunin/corpus/knowledge/synthesis/worldbible-integration-contract.md
```

```text
49ac1a5 corpus: mint finishing wave — synthesis 24, verification 12, civilizations 92 (128 sol-max)
e834f50309bd93b11894e7f96d03f7000fc224a3a3ea4d654fd4d1aaaa0831f7  -
50c4c2f25a728e69260b76d42f0d838a398cc4683a6149f74cceeec8fb7268c1  …/worldbible-integration-contract.md
    119 M
      2 ??
2026-10-17 10:28:12.827786510 -0300 …/worldbible-integration-contract.md
```

The file is at contract revision `1.0.0` (`:8`), and its own §1 states "Initial bilateral
acknowledgement is **pending** until those records exist" (`:12`). But the committed blob
digest (`e834f503…`, the digest lore's L0 round-89 line pins) is no longer the worktree
digest (`50c4c2f2…`): `git -C kotodama-shokunin diff` shows 2 changed lines (the Star &
Griesemer calibration cell and its bibliography line), mtime 10:28:12 — after lore's r92
commit (10:21:04) and uncommitted, with no `LOG.md` line naming the contract path
(`grep -n "worldbible-integration-contract" kotodama-shokunin/LOG.md` → 0 matches).

**7. lore-side kotodama presence and L0 state.**

```sh
git grep -n -i kotodama HEAD -- corpus/ | wc -l      # 0
git grep -n -i kotodama HEAD | wc -l                 # 323 (all .ufo/ wave records; corpus: none)
git log --oneline -3 -- l0-questions.md
```

```text
e97613c lore r89: closure — verdicts ruled (all improved, bounded; doc-parity harm repaired), round record
```

L0 lines stand unamended: round-87 (chousa source-method boundary question), round-88
(kotodama contract authoring), round-89 (contract landed; "lore holds no acknowledgement
record"; ratification request). The r92 wave touched neither L0 nor any tracked file outside
the six corpus paths.

**8. Artifact self-provenance (boundary doc).** `corpus/knowledge/holder-assessment-boundary.md:3-9`
still reads "Refreshed at round-90 closure … re-derived from the delivered tree at `ca7f9ef`"
and `verified-at: RUNTIME REPLAYED … round-90 seat CB1` — no r92 provenance line, unchanged
before → after. Corroborates CB.md:269 item 3 and JCOV4 §2; not re-derived here.

## Findings & named debt

**F1 — Verdict: the r92 artifacts read as lore province, never chousa's or kotodama's
(unchanged fit; no absorption, no harm).** Every one of the six committed paths acts on lore's
own declared property — "fictional-world records … with consistency verification and sourced
inspiration" (`PROVINCE.md`): the boundary doc explains the checker's provenance-disclosure
semantics; the R8/R9 rows govern whether a sourced element may sit in *supported canon*; the
Spence rows map authored in-world claims to a delivered excerpt inside a lore fixture; the
support command is the map/anchor preflight for lore's own fixture maps; the C9 watch is a
negative-decision watch on lore's checker; the README r92 section documents the preceding.
The added-line scan (§3) finds zero chousa-method and zero kotodama-craft vocabulary, and no
r92 line names either lane.

- **Rejected fit — chousa-shokunin** (deep-research method: question framing, source
  hierarchy, citation chaining, claim-vs-source verification, external-target approval). The
  closest surface is the R9 manual gate and receipt boundary (`r88-sourced-inspiration-decision-table.md:42-48`):
  bibliographic identity (printing/edition, translator, copy locator) *is* claim-vs-source
  verification vocabulary. It stays lore because the decision being made is a canon/record
  decision — grant or refuse R5 support to an in-world claim, i.e. whether an element may sit
  in supported canon — and the row says so itself ("an editorial screen, never a rights or
  canon determination", `:24-26`); the R9 mode/anchor machinery already lives in lore's own
  map format. The method ownership question is settled in place, not absorbed: the r90 block
  (§2) records "Chousa owns the research method; lore consumes it as record craft", and the
  L0 round-87 boundary line stands unamended. A transfer would require lore to define source
  hierarchy or hop rules for external research — not present in any r92 byte.
- **Rejected fit — kotodama-shokunin** (linguistic-cultural worldbuilding: conlang, myth and
  symbolic systems, era models, naming; hands off canon to lore). The closest surface is the
  two Spence comparison rows (`r88-m3-maya-cluster/claim-excerpt-map.md`, `S1`/`S2`) — K'iche
  creation symbolism, i.e. kotodama's declared generative material (the r87 K2 seat already
  ruled the analogous `r87-myth-cluster` stays in lore under the same contract: "kotodama
  *hands off* systems; lore records and verifies them"). It stays lore because no system is
  generated here: the rows are claim-to-excerpt *record* surgery inside an existing fixture —
  inventory 10 JSON facts + 2 editorial rows, the rows explicitly "not claims about K'iche
  symbolism or extra in-world canon" — and the checker counts them as editorial, never as
  JSON facts or source support (`EDITORIAL-ANCHORS 2/2`, §5). The kotodama contract's own §3
  split is the same: kotodama supplies variant relations; lore "records / decides" who holds a
  belief. Nothing in the r92 diff writes into kotodama's `corpus/knowledge/{linguistics,
  myth-symbol,culture-material,synthesis}` or generates a naming/era/lexicon artifact.
- **Harm check.** `git show --numstat HEAD | grep -i "chousa\|kotodama"` → 0 sibling-path
  mentions; `git grep -i kotodama HEAD -- corpus/` → 0 before and after; the one file carrying
  sibling references (decision table) is byte-identical in that region (§2). No r92 byte
  claims a sibling's method, genre, or authority.

**F2 — chousa cross-references: confirmed present, byte-identical, all three resolving**
(§2). No decay introduced by the r92 insert; only the loose label on the third pointer is
worth a future wording pass (`r92-province-adjacency` naming: label says "archives verified
against live sources" while the span states the verification *limit*; pointer seat-verified at
r90).

**F3 — kotodama contract state: committed rev 1.0.0, worktree ahead, bilateral ack still
pending on lore's side.** Observed, not adjudicated: the canonical copy's on-disk bytes now
differ from the committed blob (`e834f503…` → `50c4c2f2…`, 2 calibration lines, uncommitted,
sibling tree broadly dirty 119 M / 2 ??). Contract §1 requires both lanes to re-read on a
changed revision/digest and its §9 versioning table treats this class of correction as a PATCH
that publishes corrected bytes — the acknowledgement binds a digest, so a lore read/record
taken now would bind an unreleased digest. lore side: no
`kotodama-lore-adjacency` acknowledgement record anywhere under `corpus/` (F1 harm-check
grep), L0 round-89 line open and untouched by r92.

**Named debt (this seat's own receipts; prior-naming credited):**

- **D-JCOV5-1 (corroboration, already named):** doubled R8 label at
  `corpus/knowledge/r88-sourced-inspiration-decision-table.md:40` —
  `grep -c` of the doubled literal is 1 line; `grep -n "Failed-gate disposition"` shows one
  line with the marker twice. Independent first-naming: H1.md:121, H2.md:106, JCOV2.md:62,
  JCOV4.md:170/197, JCAL4.md:12, JDEP4.md:48, Q2.md:145. No claim content affected; repair =
  delete one fragment (parent authority).
- **D-JCOV5-2 (corroboration, already named):** `corpus/tools/README.md:16-21` still carries
  the pre-r92 "Named debt — S2 terminal-status contract" section ("Missing inventory exits 2",
  "No terminal failure summaries … until the checker is updated"), which the delivered checker
  contradicts — my probe (§5) exits 1 with `RESULT FAIL`. Q2.md:145 names it (dropped
  `patches/K1-tools-readme.patch`). This is the one place in the r92 surface where a
  *contract text* no longer describes the shipped tool.
- **D-JCOV5-3 (r92 wording lineage, already recorded by the E1 judge):** the r91 sentence
  "Withhold-scope precedence (decided r91): detail-level withholding wins over element-level"
  is gone from the delivered table (`grep -i "precedence"` → no match; followup/E1.md
  measures `withhold_scope_precedence 0`) and the r92 row does not say it supersedes it; the
  detail-level rule survives only as the r90 appendix's "Withhold only the affected detail …"
  plus the new inseparability branch. Reading the two together is consistent, but a future
  editor must not treat the absence as repeal — worth one supersession clause in a later pass.
- **D-JCOV5-4 (this seat's observation):** the R9 receipt boundary and the Spence-row scope
  note both delegate outward ("not a judgment … that a representation is faithful, permitted,
  or canonical … Review those matters under the corpus decision table"; "not claims about
  K'iche symbolism"), yet neither names chousa-kotodama as the method/adjacency owner — lore's
  corpus has zero kotodama mentions and the chousa naming exists only in the r90 block. If the
  next round wants the adjacency machine-readable, the natural home is one added line beside
  the r90 block, not new prose.

## Handoff

- **Deliverable:** this file only. No tracked write, no L0 append, no commit/push; sibling
  repos untouched (kotodama's dirty tree predates this seat — its newest edit mtime 10:28:12
  predates my first read; I created and removed one `/tmp` map, `ls` → "No such file or
  directory").
- **For L1 to rule:** F1 verdict (unchanged fit, all five artifact families lore-side, with
  the two rejected-fit paragraphs above as the province record); F2 (chousa refs confirmed —
  mission ask closed); F3 (kotodama contract state noted: rev 1.0.0, worktree-ahead digest
  `50c4c2f2…` vs L0-pinned `e834f503…`, bilateral ack pending, lore has no record).
- **Operational note for the L1/L0 path:** the round-89 L0 line's ratification request is
  still open and now interacts with F3 — if lore records its acknowledgement, state the
  digest it read, because the sibling's released bytes and worktree bytes differ at this
  moment; committing the sibling's two-line calibration edit would change the digest again.
- **Debts:** D-JCOV5-1/2/3 are corroborations of already-named items (repair needs parent
  authority; D-2 also needs the dropped `K1-tools-readme.patch` decision); D-JCOV5-4 is this
  seat's only new suggestion, low priority.
- Not verified by this seat (out of mission): the doc's anchor staleness, census numbers, and
  receipt arithmetic — covered by JCOV4/JDEP/JCAL seats; the boundary doc's provenance-line
  staleness is corroborated by JCOV4/CB only.
