# Fleet round 1 — connector (R1Connect): sibling-overlap scan and one bounded calibration move

Static read-only work. No checker, measurement, test, build, or formatter was run by
this connector. Quoted CLI outputs are others' recorded observations
(`reports/round-1/current-baseline.json:4-10`, `reports/round-1/baseline-probes.json:5-11`,
`reports/round-85/r85-axis-adjudicator.md:46-55`); all other claims below are direct
file reads at the paths:lines given. No code, domain-source, or routing change; no
judgment, admission, or integration performed.

## 1. One bounded proposal

**Anchor the round's claimed gain in the stop-disclosure notice — detected on the
ambiguous-holder branch itself, not gated by `can_check_chain`, worded per the
existing "unassessed, not disproved" convention — and keep the two field-local
`ambiguous entity` lines as convention-compliance, not as the novelty.**

Mechanism (static, `corpus/fixtures/check_bible.py`):
- The two holder branches `:215-216` (`to_holder` count>1) and `:223-224`
  (`from_holder` count>1) set `valid = False` with **no appended diagnostic** — the
  only silent invalidations in the provenance loop; every other `valid=False` path
  voices one (`:204` tick, `:207`/`:210` empty holder, `:213`/`:221` dangling, `:226`
  source shape; `:108` via `source()`).
- Invalidation resets `previous_holder/previous_tick` and latches
  `can_check_chain = False` at `:234-237`; both continuity (`:242-245`) and tick-order
  (`:239-241`) comparisons live behind that gate at `:238` and the flag is never
  re-enabled inside the item (`:246-247` only update locals). Gate initial value also
  depends on `sources_available` and the item's own id count (`:183`), item loop scope
  per entity row (`:171`).
- Second-order trace on the disclosure surface: because the ambiguity tests at
  `:212-224` are evaluated **before** the stop at `:234-237`, a notice or diagnostic
  emitted inside those branches fires at the first ambiguous-holder record even when
  an earlier invalid record already stopped comparisons — exactly the placement the
  shared interface mandates. The opposite implementation (notice emitted under
  `if can_check_chain`) silently vanishes after an earlier stop; the inherited critic
  recorded that failure mode (`reports/round-1/critic.md:42`). No comparison
  resumption, identity choice, or byte change is implied by this placement.

Why this synthesis and not the bare r56 lines: r56 was REJECTED because two accurate
locator lines added only navigability over an already-withheld comparison
(`reports/r56-axis-adjudicator.md:3,31,37,41`). r85 changed the material fact: a real
downstream break is reported verbatim under a unique holder (`current-baseline.json:6`)
and "entirely absent" under an ambiguous one (`current-baseline.json:7-8`;
`reports/round-85/r85-axis-adjudicator.md:50,107-115`), and a sealed non-author operator
formed a materially wrong defect model from the masked output alone
(`reports/round-85/r85-sealed-reviewer.md:29,66-74`), satisfying the falsifier's
action/**interpretation** disjunct (`r85-axis-adjudicator.md:115-119`). What the round
now owes the record is the disclosure the checker still lacks — "nowhere does the text
disclose that a duplicated holder suppresses the rest of that item's chain findings"
(`r85-axis-adjudicator.md:35-39`).

## 2. Affected round axes

- **calibration** (`AXES.md:15` — gaps named honestly): the notice makes the existing
  assessment boundary a property of the output; the proposal sharpens *what may be
  claimed*, harming nothing. This matches the declared tie-break
  (`SCORECARD.md:22-24`).
- **depth, coverage**: unchanged, deliberately — more report lines are not domain
  depth or coverage (`r85-axis-adjudicator.md:97-103`; `critic.md:72-73`); the
  5-gate sample's ceiling is not whole-domain calibration (`SCORECARD.md:31-32`).
- **adjacency** (fleet-level, `AXES.md:16`): the scan below names contested scope
  rather than absorbing it.

## 3. Reusable lore conventions (found, path:line)

1. Global duplicate **retained** + local `ambiguous …` at each reference:
   `corpus/fixtures/README.md:125-126` (sources), `:517-520` + resolution table
   `:526-527` (relation endpoints), `:184-187` (dependency: local report **and no
   tick comparison**), `:235-237`/`:257-259`/`:377-380` (place/actor exclusion).
   Code mirrors: `check_bible.py:108,167-168,279,281,313`. The holder fields are the
   last reference site without this pair — the new lines at
   `{record_label}.{from_holder|to_holder}: ambiguous entity {id!r}` reuse the
   `:168` phrasing verbatim, the format r56's candidate already emitted
   (`r56-axis-adjudicator.md:25-26`).
2. "unassessed, not disproved" — `README.md:385-386`; echo `r85-axis-adjudicator.md:146-147`.
3. "input-structural finding, not sourced-canon" prefix on chain findings —
   `check_bible.py:241,243,245`; `README.md:142-143`. The notice should follow this
   epistemic-status convention and must not name the hidden break.
4. Array order never selects a duplicate — `README.md:127,519-520`; report count is
   not multiplicity of defects — `README.md:144-145` (supports exactly-one-notice-per-item).
5. Holder IDs are entity IDs; kind "need not mean legal ownership" — `README.md:115-116`;
   ambiguous-ID behavior is "not silently interpreted as a valid chain" — `README.md:113-114`
   (the letter is kept today by `valid=False` at `:216/:224`; the round discloses the
   spirit).
6. Single-clone-delta fixture discipline — probes are `item-chain-valid` clones with
   only `entities.json` differing, `cmp -s` byte-identity on the rest
   (`r85-author.md:38-40`; `r85-axis-adjudicator.md:57-59`).
7. Telemetry under `corpus/live/runs/` is not an active fixture and not counted as
   coverage — `r85-author.md:84-85`; `r85-axis-adjudicator.md:100-103`.
8. Unavailable-table gating is distinct from ambiguity — `README.md:958,964`;
   `check_bible.py:97-101,183`: keep the notice trigger on holder *identity ambiguity*
   (counts at `:157-159` need only parsed entity rows), not on general chain
   ineligibility, or r60/r61 availability semantics get silently widened.

## 4. Sibling-overlap scan and contested scope (reported, not absorbed)

**Distinct by scan, no bleed found in this round's claim:**
- *Fictional provenance vs real-world rights/art ledger*: the move changes only
  entity-reference disclosure; `reference-ledger.md:3-11` keeps attribution, rights,
  and training permission as separate real-world questions; `README.md:533-534` and
  `r56-axis-adjudicator.md:41` explicitly forbid equating a provenance field with
  custody or rights. Nothing in the shared interface touches that layer.
- *Fictional tick order vs game mechanics*: `game-dev-2d-shokunin/PROVINCE.md:3` owns
  mechanics verification and `:10` refuses narrative canon ("contested scope is
  reported, not absorbed"); `game-dev-3d-shokunin/PROVINCE.md:34-36` refuses lore canon
  reciprocally; lore `PROVINCE.md:9` refuses game-mechanics verification. The shared
  word "tick" denotes the per-record ordering field
  (`check_bible.py:29,203,239-241`; `README.md:114-115`: "local to these explicit
  records, not linked automatically to timeline events") — not game loop timing, not
  the fleet driver's `TICK_SECONDS=450` (`shokunin.conf:11`, `MISSION.md:36`). Keep the
  notice's phrase "tick-order comparisons" inside the provenance record scope.
- *Probe holder IDs vs kagi*: fictional `vault`/`harbor` entity IDs
  (`current-baseline.json:6-9`, kagi = real "secrets and vault ops" `shokunin.conf:51`)
  are name collision only; `README.md:115-116` is the guard. Do not cite kagi evidence
  into lore scoring or vice versa.
- *Fleet routing*: `MISSION.md:14` (swe-class), `shokunin.conf:30-36` (host decides
  role routes; prompts name roles only), `dispatch.json:7` (operator route table
  `~/.omp/agent/config.yml:318-332`, unchanged). No overlap with the checker work
  beyond those statements; none edited here.

**Contested scope surfaced for the parent (not mine to reconcile):**
1. *Measurement-entrypoint name drift*: inherited `dispatch.json:13` and
   `critic.md:61` name `corpus/fixtures/measure_holder_calibration.py`; the current
   canonical assignment names `measure_holder_disclosure.py`. Same role, two names —
   integration must pick one before paths land. Neither name exists yet in
   `corpus/fixtures/` (full directory listing scanned; only `check_bible.py` present).
2. *Report-path drift*: `dispatch.json:11` places the connector artifact at
   `reports/round-1/connector.md`; this connector's assignment is
   `reports/round-1/r1-current-connector.md`. Preserve the inherited dispatch record;
   parent is sole index/integration owner.
3. *Gain-attribution tension with r56*: the literal second prong of the r56 falsifier
   ("changes an otherwise mistaken action", `r56-axis-adjudicator.md:41`) was met only
   via the *interpretation* disjunct (`r85-axis-adjudicator.md:115-119`); the sealed
   reviewer's first physical action was unchanged (`r85-sealed-reviewer.md:76-84`), and
   iterative rechecking neutralizes the mask (`r85-sealed-reviewer.md:94-96`;
   `r85-axis-adjudicator.md:140-146,177-180` reopen conditions). Report the gain as the
   assessment-boundary marker — claiming "detected the masked break" re-opens r56's
   materiality objection (`critic.md:9,15`).
4. *Sample-vs-replay scope*: the five gates are a targeted disclosure sample
   (`critic.md:63`); the admitted r86-repair condition also mandates the 133-tuple
   plus-probes replay (`r85-axis-adjudicator.md:167-169`; `SCORECARD.md:12`), which the
   parent runs separately (`shared interface`) — gate scores must not be presented as
   replacing it.
5. *Dangling named sibling*: `lore/PROVINCE.md:7,9` defers rights claims to
   "art-east-asian-design"; `game-dev-2d/PROVINCE.md:10` and `game-dev-3d/PROVINCE.md:34`
   defer asset-rights clearance to the same name. **Bound by scan**: no such lane
   directory in the fleet-root listing, no entry in `shokunin.conf:19-67` or
   `shokunin.conf.full-roster-20261015:19-67`, nothing in `MISSION.md:17-31`, no
   `/home/vgpnk/Projects/*art*` path; all fleet-wide matches for the name are PROVINCE.md
   refusal lines inside lane repos and their frozen baseline copies (40 files). Not
   this round's fix; a freshness question for the aggregator/protocol lanes.
6. *Root-path drift*: r83/r85/r56 reports and `fixtures/README.md` commands use the old
   `.shokunin/lore/corpus/...` root (`r85-sealed-reviewer.md:3-4`;
   `r85-axis-adjudicator.md:43-44`; `README.md:106,133-134`); current lane root is
   `corpus/...` (`current-baseline.json:3`, `baseline-probes.json:4`). Measurement
   entrypoint strings in new docs should follow the current root; historical quotes
   stay byte-frozen.

## 5. Gate-input availability (static, for the measurement executor)

At revision `5eb9451` the probe inputs exist under
`corpus/live/runs/round-85/probe-inputs/` (five dirs confirmed by listing):
gates 1-2 and the ambiguous-to direction can reuse `r85-control`,
`r85-unique-break-control`, and `r85-masked-ambiguous` / `r85-isolated-ambiguous`
as recorded. **No existing input exercises** dangling holders on both fields, an
ambiguous `from_holder` direction (`r85-sealed-reviewer.md:102-103`;
`r85-axis-adjudicator.md:151-152`), or ambiguity following an earlier invalid record —
those rows must be authored in the isolated temp tree per the single-clone-delta
convention (item 3.6) and remain unverified fiction (contract). Each ambiguity gate
needs a later valid record whose continuity/tick lines must be *absent* — that absence
is the non-resumption assertion (`critic.md:44`), since the masked probe itself has no
reversed downstream tick (`critic.md:44` citing probe records).

## 6. Risks

- Notice worded as break-detection, or scored as a saturation event → r56 objection
  returns; `SCORECARD.md:31-32` and §4.3-4.4 guards bind the wording.
- Notice guarded by `can_check_chain` (vanishes after an earlier stop) or flag kept
  across items (suppressed second notice) → false or missing scope disclosure
  (`critic.md:40-43`; per-item loop scope `check_bible.py:171-184`).
- Trigger conflated with source-unavailability (`:183`) → silently widens r60/r61
  availability semantics (§3.8).
- Integration picks either measurement filename without retiring the other → two
  entrypoints in one lane record (§4.1-4.2).
- Rights/mechanics language leaking into the notice or docs via the shared words
  "holder", "custody", "vault", "tick" → cross-domain bleed against `PROVINCE.md:9`
  and the reciprocal refusals (§4).

## 7. Verification

Connector exercised: file reads/`grep`/`glob` only, no commands beyond static
inspection. All §1 mechanism claims read directly from `check_bible.py` lines cited;
§3 conventions read from `README.md`, r56, r85 author/sealed/adjudicator, round-1
inherited artifacts; §4 bounds from the fleet-root listing, both `shokunin.conf`
variants, `MISSION.md`/`AXES.md`, sibling `PROVINCE.md` files, and a fleet-wide grep.
Scan caveat: a default (gitignore-respecting) grep of the fleet root returns **zero**
`art-east-asian-design` matches — lane repos are gitignored there; the bounded absence
in §4.5 rests on the `gitignore:false` re-scan plus directory listings.
Parent's integrated runs (not performed here): checker edit replay of all inherited
CLI triples and JSON-byte preservation, the five-gate measurement at
`5eb9451` and on the candidate, per `critic.md:65-67` acceptance conditions.
