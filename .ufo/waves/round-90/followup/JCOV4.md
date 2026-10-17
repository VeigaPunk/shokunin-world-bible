# JCOV4 — Coverage judge #4 (fresh-eyes province audit), round 90 follow-up

Seat: JCOV4. Lane: world-bible / coverage (C2). Judged artifact state: delivered tree
`ca7f9ef1646cf3fcbe58747785a8cb2e9075ae13` (baseline `e97613c`).
Independent-audit order observed: maps → script → mode labels → PROVINCE refusals →
three-question rule, all before opening `.ufo/waves/round-90/C7.md`.

## Work performed

- Verified the delivered tree: `git rev-parse HEAD` → `ca7f9ef…`; at session start
  `git status --porcelain` showed no tracked modifications (only untracked `followup/`
  artifacts from sibling seats). Integrity re-check at the end of the session: all judged
  artifacts hash-match their committed blobs — `git show ca7f9ef:<path> | sha256sum` equals
  the worktree hash for `corpus/tools/support_check.py` (`66a3c4bb…`), `corpus/fixtures/check_bible.py`
  (`ff9fd2aa…`), `corpus/fixtures/r87-myth-cluster/claim-excerpt-map.md` (`8c1b600d…`) and
  `corpus/fixtures/r88-m3-maya-cluster/claim-excerpt-map.md` (`d314d22e…`); `git diff --stat HEAD -- corpus/`
  is empty. One **foreign** tracked modification appeared mid-session
  (`M .ufo/waves/round-90/followup/Q1-r90-debt.json`, +109/−84) — not written by this seat,
  outside my judged set, and not reverted by me. My only repository write is this file.
- Two 60 s wait-checks (dependency protocol): check 1 at `06:56:05` — `followup/` held only
  `Q1-r90-debt.json`; check 2 at `06:58:42` — `H2/H3/H4/JCAL1/JCAL2/JCAL5` artifacts present;
  by `07:00` the directory also held `CB1.md`, `JDEP2.md`, `JDEP3.md`, `JCOV3-denominators.json`,
  `JCOV5.md`, `Q2.md`. **No C7 follow-up document exists**; the required C7 comparison therefore
  uses the committed work-wave report `.ufo/waves/round-90/C7.md`.
- Read (delivered tree, read-only): `PROVINCE.md`, `corpus/knowledge/r88-sourced-inspiration-decision-table.md`
  (incl. the r90 R8/R9/R10 appendices), `corpus/knowledge/reference-ledger.md`, both cluster maps,
  both clusters' excerpts/notes/contradiction records, `corpus/tools/support_check.py`,
  `corpus/tools/README.md`, `.ufo/waves/round-90/wave-spec.md`, `.ufo/waves/round-90/M5.md`.
- Ran the delivered receipts, the freeze-then-verify (r88-I1) reconstruction, 12 coverage/mode-label
  control probes in `/tmp` scratch, and an obligation-denominator measurement. No repo write except
  this file; no commit/push; scratch removed after use (single 3-inode probe directory reused because
  `/tmp` was at 100 % inode use — `df -i /tmp` → `1048465/1048576`).
- Fresh-eyes discipline: prior critics were not read before the audit; sibling coverage artifacts
  (`JCOV3-denominators.json`, `JCOV5.md`) were deliberately **not** read, so this verdict is
  independent of them.

## Before → after measurements

All commands run from the repository root against the delivered tree. Probe clusters were minimal
copies holding only the map plus its cited excerpts; the delivered script was invoked unchanged.

### 1. Delivered receipts reproduce (C2's core claim)

```sh
python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster; echo "EXIT=$?"
python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster; echo "EXIT=$?"
```

```text
SOURCE-SUPPORT 22/22; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22
RESULT PASS
EXIT=0
SOURCE-SUPPORT 10/10; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 10/10
RESULT PASS
EXIT=0
```

Claim "r87 22/22, r88-m3 10/10" **reproduces exactly**, exit 0 on both. The R9 negative fixture
also behaves as documented:

```sh
python3 corpus/tools/support_check.py corpus/fixtures/r89-inspiration-paraphrase
```

```text
SOURCE-SUPPORT 0/0; RETELLING-SUPPORT-ONLY 1 entries (1/1 anchors); MODES 1/1
RESULT PASS
EXIT=0
```

### 2. Freeze-then-verify (r88-I1) — MATCH, no blocking finding

```sh
git -C <repo> show e97613c:corpus/fixtures/check_bible.py > corpus/fixtures/check_bible.py
patch -p1 --batch --quiet < .ufo/waves/round-90/patches/X2-c1-nullonly.patch
patch -p1 --batch --quiet < .ufo/waves/round-90/patches/X3-c1-tickonly.patch
sha256sum corpus/fixtures/check_bible.py
```

```text
reconstructed: ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
delivered    : ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
FREEZE-VERIFY: MATCH
```

X2+X3 composed on `e97613c` is byte-identical to the delivered checker (
`cmp -s` clean). C1's freeze obligation on the coverage-relevant artifact holds.

### 3. R9 enforcement controls (mode labels)

| Probe | Mutation of the delivered map/excerpt | Observed | Exit |
|---|---|---|---|
| anti-inflation | all 3 `gate-witness` rows + declaration-table row + excerpt declaration flipped `verbatim`→`paraphrase` | `SOURCE-SUPPORT 19/19; RETELLING-SUPPORT-ONLY 3 entries (3/3 anchors); MODES 22/22` | 0 |
| map-only flip | E1 row `verbatim`→`paraphrase`, excerpt still `verbatim` | `FAIL E1: … excerpt-mode=verbatim`, `FAIL: E1: delivery mode missing or mismatched` | 1 |
| single fact row (r88) | P1 row `verbatim`→`paraphrase` | `SOURCE-SUPPORT 9/9; … MODES 9/10` + FAIL | 1 |
| declaration row, referenced excerpt | each of the 5 r87 declaration rows flipped in turn | every flip FAILs (e.g. `FAIL: T3: delivery mode missing or mismatched`) | 1 |
| two declarations in one excerpt | appended a second, conflicting `Delivery mode (R9)` line | `…excerpt-mode=undeclared`, FAILs on all 3 gate rows | 1 |
| **unreferenced excerpt (Spence)** | r88 declaration row `source-excerpt.md:5` `verbatim`→`paraphrase` | `SOURCE-SUPPORT 10/10; … MODES 10/10; RESULT PASS` — **unchanged** | 0 |

Result: a matching anchor in a `paraphrase`/`summary` row can never enter `SOURCE-SUPPORT`
(denominator drops, row is re-labelled `retelling-support-only`) — C2(iii) is enforced, not
just documented. Mode labels are enforced **referentially**: only excerpts cited by fact rows are
validated; the r88 real-world `verbatim` label is not.

### 4. Span and containment controls

| Probe | Mutation | Observed | Exit |
|---|---|---|---|
| span flip | E1 locator `:7` → `:5-5` | `FAIL: E1: anchor hit outside declared line span 5-5 (hit lines: 7)` | 1 |
| line shift | one line injected near the top of the excerpt | anchors fall outside their spans → FAILs | 1 |
| path escape | E1 excerpt path → `/…/lore-shokunin/PROVINCE.md:7` | `FAIL: E1: excerpt path missing or outside cluster` | 1 |
| vacuity (all tables) | both r87 fact-table `ID` headers renamed / anchor column renamed | `FAIL: no Markdown table found with fact, excerpt path, delivery mode, and anchor columns` | 2 |

M5's span enforcement is live on the delivered tree; escape and vacuity are loud.

### 5. Silent-failure probes (new findings)

| Probe | Mutation | Observed | Exit |
|---|---|---|---|
| **silent row-drop** | rename only the 14-fact table's header `| ID | JSON fact and fields |` → `| Row | … |` | `SOURCE-SUPPORT 8/8; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 8/8` `RESULT PASS` — 14 rows left the receipt silently | 0 |
| **retelling anchor tolerance** | on the anti-inflation tree, replace one paraphrase row's anchor with a phrase absent from the excerpt | `RETELLING-SUPPORT-ONLY 3 entries (2/3 anchors)` `RESULT PASS` | 0 |
| **row-count padding** | duplicate one r88 fact row (same anchor/span) | `SOURCE-SUPPORT 11/11; … MODES 11/11` | 0 |

### 6. Obligation-denominator measurement (my own numbers)

```sh
python3 - <<'PY'   # per cluster: JSON obligations vs parsed map rows
entities/relations/timeline loaded; obligations = claims + first_appearance pointers + relations + events
PY
```

```text
r87-myth-cluster: JSON_obligations=22 | map rows=22 categories={'E': 6, 'R': 4, 'T': 4, 'H': 8} | row-covered=20/22
   NOT row-covered: entities[2].claims[0]        -> appears only in the prose crosswalk (map:56)
   NOT row-covered: entities[2].first_appearance -> appears only in the prose crosswalk (map:56)
r88-m3-maya-cluster: JSON_obligations=10 | map rows=10 categories={'P': 4, 'E': 4, 'T': 2} | row-covered=10/10
```

`grep -n 'entities\[2\]' corpus/fixtures/r87-myth-cluster/claim-excerpt-map.md` → one hit, line 56
(the "Full D1 crosswalk" note). Row ids present: `E1 E2 E3 E4 E5 E6 R1 R2 R3 R4 T1 T2 T3 T4 H1…H8`.

Row-count semantics measured on the delivered r88 map via `support_check.parse_map`:
`rows=10 distinct_anchors=6 distinct(path,span)=2 distinct_excerpt_files=1`.

### 7. Province refusals and the three-question rule (independent checks)

| Surface | Command | Observed |
|---|---|---|
| canon without in-world citation | read both maps + scope notes | every cited in-world fact points at a delivered excerpt; hymn rows marked editorial, "not new canon" (`claim-excerpt-map.md:38,55`); Spence labeled "external comparison, not an in-world source" |
| silent contradiction resolution | `head -c 400 contradictions.json` (both) | r87 holds `moon-basin-vow-location` (Hara vs Sen, same single vow, incompatible places) and `claim-excerpt-map.md:54` says "Preserve both cited accounts as unresolved"; r88 `[]`, `relations.json` `[]` |
| cross-cluster register | `ls corpus/knowledge/ \| grep -c 'cross-cluster-contradictions.md'` | `0` — live register absent; only the r89 worked example `r89-cross-cluster-contradiction.md` |
| real-world rights claims | `grep -rniE "public domain\|license\|rights grant\|permission\|permitted\|prohibited"` over both maps, tool, README, both notes | no rights/permission assertion in any map or the tool; the only hits are the notes' `## AI-training-permission question` sections saying permission "has not been assessed or established"; ledger Spence row keeps attribution / rights / training in three separate cells, both questions open |
| three-question separation | `grep -n '^#' …inspiration-note.md` (both) | both notes carry `## Parallel cited`, `## Attribution question`, `## Rights question`, `## AI-training-permission question` |
| game-mechanics verification | `grep -rniE '\b(mechanics?\|gameplay\|damage\|balance)\b'` over maps, tool, README | zero hits |
| R9 mode vocabulary | `grep -hoE '`(verbatim\|translation\|paraphrase\|summary)`'` over delivered maps | 48 × `verbatim`, 1 × `paraphrase` (the r89 demo) — the tool's `MODES` set equals R9's four modes |

No PROVINCE refusal is breached by the maps, the tool, or the mode labels; the three-question rule
is untouched by the C2 artifacts (no merge, no inference).

### 8. C7 comparison (read after the independent audit)

Agreements:

- **C7-F1 confirmed independently.** C7: the r87 `22/22` "is not the requested 22-JSON-fact receipt …
  the final two JSON obligations are only prose cross-references and are not counted/validated."
  My measurement: 20/22 row-covered; `entities[2].claims[0]` and `entities[2].first_appearance`
  appear only in the map's prose crosswalk (line 56). The 22 rows are 14 JSON rows + 8 editorial hymn rows.
- **C7-F2 (R3 pledge scope) — delivered qualification present.** `claim-excerpt-map.md:53` states the
  charter records a pledge, not performance; the relation anchor cannot be read as completed watch.
- **C7-F4 (script scope) — confirmed, and widened.** Paraphrase/summary exclusion verified by the
  anti-inflation control; translation source/version identity left manual (README:14); I add the
  header-role silent row-drop (probe 5) and the padding/retelling-anchor residuals.
- **C7-F5/F6 — confirmed at the map/script level.** No canon/rights/contradiction breach; register
  empty (`live_register_present=False`-equivalent: file absent; r88 name sets disjoint is C7's check,
  the contradiction/relation empties are mine).

Disagreements:

- **C7-F3 does not describe the delivered tree.** C7 attacked M2 for listing the Spence passage as
  `external-only` **in the Delivery mode column**. The delivered `claim-excerpt-map.md:11` declares
  `verbatim` and moves `external-only` into the Status cell ("external comparison, not an in-world
  source. The underlying K'iche primary text is not reproduced (`external-only`)"). The delivered
  tree repaired the finding C7 raised against the pre-integration patch revision; C7's principle
  (separate delivery mode from external-source status) is satisfied in the delivery. Residual of mine
  that C7 did not have: that repaired label is now outside the receipt's coverage (probe 5/K1).
- **Emphasis.** C7's F1 leaves open whether the map text "covers" the 22 obligations; the delivered
  map is self-describing (line 3: "14 JSON facts … plus the 8 Low-Water Hymn clauses (22 mapped rows)";
  line 56 discloses the two prose-only obligations), so the artifact is honest — the debt is the
  *receipt number's* semantics, not hidden rows.

## Findings & named debt

- **F1 (debt, coverage tooling) — the tool's exit code is not a completeness receipt.** A fact table
  whose header loses its recognised `id` role leaves the receipt silently while the run still prints
  `RESULT PASS`, exit 0 (observed: 22-row map → `8/8`). Only a *total* absence of fact tables fails
  (`exit 2`). Suggest an expected-inventory assertion (`--expect-rows N` / row-role tags) in r91.
- **F2 (debt, mode labels) — labels are enforced only where facts point.** The r88 Spence row's
  `verbatim` label can be flipped to any R9 mode with exit 0 unchanged (PASS 10/10), because no fact
  row references `source-excerpt.md`; the two symbolism bullet comparisons
  (`source-excerpt.md:5` ×2, `fictional-excerpts.md:7`, `:8`) are likewise outside `N/N` though I
  confirmed all four anchors by direct `grep -nF` on the delivered lines. README already disclaims
  fidelity for these, so no support is over-claimed.
- **F3 (debt, receipt wording) — `r87 22/22` counts rows, not facts.** Composition 6E+4R+4T+8H;
  2 of the 22 JSON obligations are prose-only. The map (lines 3, 56) discloses this; the wave-level
  receipt should be re-worded or backed by an inventory check rather than read as JSON-fact coverage.
  r88's `10/10` is exactly its 10 JSON obligations — clean.
- **F4 (debt, minor) — retelling rows tolerate absent anchors** (`3 entries (2/3 anchors)`, exit 0)
  and the `N/N` counter has no de-duplication (one duplicated row → `11/11`). Neither can inflate
  source support; both can mislead a reader who skims only the exit code.
- **F5 (unexercised surface) — `translation` is support-eligible with no translator/version tie.**
  All 48 delivered mode labels are `verbatim` except the r89 paraphrase demo, so the delivered
  receipts contain zero translation rows; the README (line 14) disclaims the identification check.
  Consistent with the r90 R9 appendix, but not mechanically enforced — keep as named debt.
- **F6 (evidence note) — the Spence `verbatim` label is not independently verified here.** The cited
  Gutenberg URL was fetched and truncated before printed p. 209; a WebSearch hit on the 1913 scan at
  archive.org shows the sentence "called out "Earth," and the solid land appeared." — consistent with
  the delivered text but not a page/edition-exact verification. Bounded by README:14 and F2.
- **Blocking findings: none.** Freeze-verify MATCH; every claimed receipt reproduces.

Axes touched by this seat's evidence (coverage): **improved (bounded)** — maps, R9 labels, receipt
reproducibility, span enforcement, anti-inflation and refusal/three-question compliance all hold on
the delivered tree; five bounded residuals named above, none of which inflates source support.
Calibration/depth are other seats' axes; the only cross-axis evidence I produced is the freeze MATCH.

## Handoff

- Coverage verdict evidence for the r90 judgement: reproduced receipts (22/22, 10/10, r89 demo 0/0,
  all exit 0), freeze MATCH `ff9fd2aa…`, 12 control probes, obligation measurement 20/22 (r87) vs
  10/10 (r88).
- r91 candidates, in priority order: (1) inventory assertion so header-role drift cannot pass
  (`--expect-rows` or row-role tags); (2) receipt wording split for r87 (14 JSON rows + 8 editorial
  rows) or per-row role labels; (3) fail-or-warn on retelling rows whose anchor is not found;
  (4) consider de-duplicating `N/N` or reporting distinct excerpts/anchors beside it.
- For the parent/integrator: C7's R9-label finding (M2 `external-only` in the mode column) is **not**
  a live defect in the delivered tree — do not re-open it without re-reading `claim-excerpt-map.md:11`.
- Gaps: no C7 follow-up artifact exists (comparison used the wave report); sibling coverage artifacts
  `followup/JCOV3-denominators.json` and `followup/JCOV5.md` present but unread (fresh-eyes); no
  network-exact verification of the Spence label (F6). My only repo write is this file; it is
  untracked, no commit/push was made, and the tracked tree remains at `ca7f9ef`.
