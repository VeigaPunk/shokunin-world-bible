# JCOV5 — r93 follow-up: sibling adjacency (Kojiki cluster + dossier vs chousa/kotodama)

Verdict evidence from the committed lore tree at `65838f8` (clean except the connector's own
uncommitted `l0-questions.md` +1 line and this `followup/` dir — both named below). Sibling
repos read-only: chousa read at `38f217e` (clean), kotodama read across `291c714` → `c610e0a`
→ `fe34faa` (HEAD moved mid-run; tracked in Findings #7). Full command/output pairs:
`JCOV5-probes.json` alongside this file.

## Work performed

- Inventoried the r93 Kojiki cluster's full referent set from the committed tree
  (`corpus/fixtures/r93-m2-kojiki-cluster/`): entities `teva`, `orni`, `slate-table`,
  `lorn-index`; events `teva-files-index`, `orni-marks-index`; sole source id
  `m2-record-archive`; 3 editorial rows anchored to Chamberlain 1882 translation lines 8–10;
  plus the dossier's fictional token `Kesh Hymn` (`corpus/knowledge/r93-r8-worked-example.md`).
- Word-boundary scans of both sibling repos at their committed HEADs for every referent token,
  after a bare-substring pre-scan (which produced false friends: "Calif**orni**a",
  "ad**orni**ment", hex `keSh`); reconciled every hit.
- Verified the three chousa method crossrefs quoted in
  `corpus/knowledge/r88-sourced-inspiration-decision-table.md:120-125` against chousa at
  `38f217e`, line range by line range.
- Traced the kotodama handoff contract
  (`corpus/knowledge/synthesis/worldbible-integration-contract.md`) hash across its commit
  history, diffed the change, checked it against the contract's own §1 re-read clause, and
  searched both lanes for read/acknowledgement records.
- Checked the L0 digest caveat in `l0-questions.md` — committed at `65838f8` vs the working
  tree (they differ; see Findings #2).
- Replayed the cluster's checkers and the dossier's traceability script from the lore root;
  ran the r87 `Reed` lookalike control; checked reference-graph direction (who cites whom).
- No wait-checks performed: the seat block named no pending dependencies to wait on. The
  kotodama lane moved under this seat mid-run (round-4 commit `fe34faa` at 12:19:35); state
  was re-pinned after the move and gaps noted (Findings #7).

## Before → after measurements

Axis J1 — sibling referent adjacency (cluster + dossier vs chousa/kotodama). Before: the r93
claim of zero shared referents covered only the two *prior lore* clusters; the sibling side
was unaudited. After: zero shared referents confirmed against both siblings.
`git grep -i -n -w -e teva -e orni -e lorn -e slate-table -e lorn-index -e m2-record-archive -e kesh -e M-17 HEAD --`
→ chousa `38f217e`: entity tokens **0 hits** (bare pre-scan's only hit was the sha256 hex
substring `keSh` in `.ufo/continuations/round-1.json:42` — false positive). Kotodama at
`291c714..fe34faa`: entity tokens **0 hits**; the only word hits are (a) Khalsa *kesh*, a
real-world Sikh term (`corpus/knowledge/culture-material/adornment-body-codes.md:59`,
`corpus/README.md:52`) — unrelated to the dossier's fictional *Kesh Hymn* — and (b) morpheme
id `M-17` in kotodama's D2 example culture
(`examples/culture-d2/components/03-morphosyntax.yml:211`, `packet.d2.yml:368`,
`reviews/15-pragmatics.md:22,111`, frozen round-3 gate copies) — a coincidental ID lookalike
to the cluster's *nickname* "M-17 margin-register cluster", different namespace and object
kind, not a referent. **Verdict: unchanged (claims hold; now verified sibling-side).**

Axis J2 — chousa crossrefs intact. Before: `r88-sourced-inspiration-decision-table.md:120-125`
asserts three chousa method crossrefs. After, at chousa `38f217e` (clean tree, so ranges are
as committed): `claim-verification-r2.md:45-58` = fail-closed source boundary + byte-exact
span check — **exact fit** for "claim-vs-source verification";
`anchor-boundaries-r4.md:31-37` = substring→token-boundary anchor semantics — **exact fit**
for "fixed-string anchor boundaries"; `archives-verified-r9.md:177-185` = residual archive
distortion, "verifying a conversion is not verifying the original", custody terminates at the
export — **on-topic**, but the lore gloss "archives verified against live sources" is looser
than the target text (cosmetic; no range is broken). Reverse direction: `git grep -i -n
lore-shokunin HEAD --` in chousa → **0 hits**; the reference graph is one-way (lore consumes
chousa's method), matching r88's "Chousa owns the research method; lore consumes it as record
craft". **Verdict: unchanged (intact).**

Axis J3 — kotodama contract state + the L0 digest caveat. Before (committed `65838f8`):
`l0-questions.md:5` (r89 row) presents the contract at `sha256 e834f503…` (commit `49ac1a5`)
as current, and records that lore holds no acknowledgement record. After:

- Hash trace: `git show 49ac1a5:<contract> | sha256sum` →
  `e834f50309bd93b11894e7f96d03f7000fc224a3a3ea4d654fd4d1aaaa0831f7`; `git show 291c714:…` →
  `50c4c2f25a728e69260b76d42f0d838a398cc4683a6149f74cceeec8fb7268c1`; identical at `c610e0a`,
  at `fe34faa`, and in the working tree; `git diff 291c714 fe34faa -- <contract>` → empty.
  Kotodama round 1 (`291c714`, 10:54:46) changed the file; nothing since.
- Content of the change: §2 only, 2 lines — the Star & Griesemer calibration moves from
  "original passage interpretation (to-verify)" to "definition at p. 393 corroborated by
  verbatim quotations in independent scholarly sources" (+ matching bibliography line).
  §1 untouched: contract_id `kotodama-lore-adjacency`, rev `1.0.0`, verification date
  `2026-10-17` all unchanged. So the digest changed **without a revision bump**, which
  triggers the contract's own §1 clause: "a changed revision/digest requires both lanes to
  re-read and acknowledge before importing under it."
- Kotodama lane side: re-read happened — `LOG.md:1462-1464` (round 2) records "Contract file
  digest verified: sha256:50c4c2f2…8fb7268c1"; `corpus/lessons/round-2-adjacency.md:88`
  records the full digest; `examples/handoff-packet.sample.md:21` and `handoff-packet.sample.yml:45,78`
  pin `50c4c2f2…`.
- Lore side: tracked corpus `grep -rn kotodama-lore-adjacency corpus/` → **0 hits**; the only
  committed lore-side record is the informational read record in
  `.ufo/waves/round-93/K1.md:5` (`file_sha256=50c4c2f2…`, `read_at=2026-10-17T11:15:15-03:00`,
  explicitly labeled "**not** a lane ratification"). The working tree adds an **uncommitted**
  round-93 L0 row (`git diff HEAD --stat` → `l0-questions.md | 1 +`;
  `git show HEAD:l0-questions.md | grep round-93` → no match) that documents exactly this
  drift and cites "kotodama HEAD fe34faa (contract file worktree-clean)" — a citation that is
  valid as of now (`fe34faa` landed 12:19:35) but not at lore's commit time (11:55:30).

**Verdict: unchanged posture; the caveat is real and now sharpened.** The committed r89 row
carries a stale digest until the working-tree r93 row lands in a closure commit.

Axis J4 — committed-tree artifact integrity (auditability of what was audited). Before/after
identical at `65838f8`: `python3 corpus/fixtures/check_bible.py corpus/fixtures/r93-m2-kojiki-cluster`
→ "CLEAN: schema, citations, relations, timeline; 0 violations", exit 0;
`python3 corpus/tools/support_check.py corpus/fixtures/r93-m2-kojiki-cluster` → "RECEIPT
JSON-FACTS 12; EDITORIAL-ROWS 3; TOTAL-ROWS 15 … SOURCE-SUPPORT 12/12; EDITORIAL-ANCHORS 3/3
… RESULT PASS", exit 0; the dossier's replay script → "R8 record fields: 5/5", exit 0. r87
control: `Reedwardens` (`r87-myth-cluster/entities.json:65`) and `Reed Bell`
(`timeline.json:8`) exist, consistent with the M-17 README's "lexical lookalike at generic
`Reed` only" claim for Chamberlain's "Central Land of Reed-Plains". Cluster + dossier mention
neither sibling (grep → 0 hits): sibling adjacency holds **by absence**, as the README
designs it. **Verdict: unchanged (healthy).**

## Findings & named debt

1. **Digest drift confirmed, benign in content, procedurally live.** `49ac1a5`→`291c714`
   changed only §2 source-calibration wording (a *strengthening*: to-verify → corroborated),
   but with no rev bump it trips the contract's own re-read-and-acknowledge clause. Kotodama
   has re-read (LOG + lesson + handoff samples all pin `50c4c2f2…`); lore's §1 read/record
   duty remains **pending operator ratification** — the open question is already framed in
   the working-tree L0 round-93 row.
2. **The r93 L0 row is uncommitted.** At the committed `65838f8`, the world bible still shows
   the stale r89 pin (`e834f503…` presented as current) and the r89 row's "0 files" grep
   claim (now superseded by the committed K1.md:5 wave record — wave artifacts only, tracked
   corpus still 0). The corrective row exists only as a working-tree `+1` line; it dies if the
   tree is reset before closure. Precision debt in that row: "Re-confirmed 2026-10-17 at lore
   65838f8 against kotodama HEAD fe34faa" is anachronistic on its face — `fe34faa` (12:19:35)
   post-dates lore's `65838f8` (11:55:30). The citation is real and current; the phrasing
   conflates lore's commit time with the re-check time. Fix wording before landing it.
3. **`M-17` ID lookalike across lanes.** Kotodama's D2 example uses morpheme id `M-17`; lore's
   r93 cluster is nicknamed "M-17". Different namespaces/kinds, zero referent risk today, but
   any report that uses bare "M-17" as an identifier in fleet-wide prose invites a false
   collision read — the same lesson as the cluster README's path-qualified source-ID rule.
   Cheap fix: say "lore M-17 (margin-register cluster)" vs "kotodama D2 M-17 (morpheme)".
4. **Kojiki thematic adjacency with zero referent overlap — and distinct translation
   lineages.** Kotodama covers the same Iwato episode as real-world comparative material
   (`myth-symbol/celestial-symbolism-calendars.md:8,39`; `civilizations/japan-heian.md:84`;
   `japan-edo.md:129,176`) via **Philippi 1968 / Heldt 2014** — not Chamberlain 1882, which
   exists nowhere in kotodama (its only "chamberlain" is a sixth-rank court official,
   `japan-heian.md:171`). So M-17's S1–S3 editorial rows thematically overlap kotodama's
   Iwato material while sharing no referent and no source artifact; lore explicitly keeps the
   Chamberlain deities external. This *strengthens* the no-textual-overlap claim.
5. **Chousa crossref gloss nuance.** The r88 table's "archives verified against live sources"
   glosses a range (`archives-verified-r9.md:177-185`) whose actual content is residual
   archive distortion and conversion≠original. On-topic, range intact; if that line is ever
   touched, tighten the gloss. Cosmetic only.
6. **M-17 README's self-declared gap has a sibling-side corollary.** The README defers the
   *integrated* zero-referent conclusion pending an M2-specific scan vs the prior lore
   clusters; this report supplies the sibling half (chousa/kotodama) so the eventual
   integrated claim can cite both halves rather than extrapolate.
7. **Kotodama is a moving target.** HEAD advanced `c610e0a`→`fe34faa` (round 4, REJECTED as
   declared) during this seat's run, and the tree was dirty again at report time (5+
   modified civilization/linguistics files, round-5 work in flight). The contract file itself
   is stable (`50c4c2f2…` since `291c714`, worktree-clean throughout). Any lane digesting
   kotodama state must re-pin HEAD at read time; kotodama's corpus contents as of `fe34faa`
   are what this report's scans cover (`git grep … HEAD` at `fe34faa`; the pre-move scans at
   `c610e0a`/`291c714` returned the same referent-zero result).

## Handoff

- **For the r93 closure committer:** land the working-tree `l0-questions.md` round-93 row
  (it documents the drift correctly); first fix the "at lore 65838f8 against kotodama HEAD
  fe34faa" anachronism (Findings #2). Until then the committed bible shows a stale digest pin.
- **For K1 / the connector:** the `K1.md:5` read record is correctly labeled informational;
  lore's §1 acknowledgement still needs the operator ratification the L0 row asks for. The
  ratify-or-bump decision (accept `50c4c2f2…` as rev 1.0.0, or direct kotodama to re-issue at
  1.1.0) is operator-level; both options are consistent with the contract's §1.
- **For the round-93 report writer:** the sibling-adjacency claim can cite this audit — zero
  shared referents vs chousa `38f217e` and kotodama `291c714..fe34faa` corpus; false friends
  named (Khalsa *kesh*, hex `keSh`, kotodama D2 morpheme `M-17`); chousa crossrefs verified
  range-exact (one gloss nuance named); reference graph one-way lore→chousa; cluster/dossier
  mention no sibling. Evidence with commands/outputs: `JCOV5-probes.json`.
- **Writes made:** this file and `JCOV5-probes.json` only, both inside the authorized
  `followup/JCOV5*` surface. No commits, no sibling-repo writes, no other tracked writes.
