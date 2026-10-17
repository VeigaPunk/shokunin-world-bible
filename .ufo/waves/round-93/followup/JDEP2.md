# JDEP2 — Doc/tool attacker (round-93 follow-up)

Seat mission: hunt the boundary doc + cert tool for residual issues (the AST-anchor debt's practical impact; any anchor that resolves to wrong content); one new adversarial construction against the C9 gate. Evidence from the COMMITTED tree at `65838f8` only; all probes ran under `/tmp` and were removed afterwards. No tracked files were written except this report; nothing committed or pushed.

## Work performed

Axes: **(A) anchor-content integrity** — does every line ref in `corpus/knowledge/holder-assessment-boundary.md` resolve to the content it claims? **(B) C9-gate adversarial robustness** — can a doc that contradicts the tick ruling still certify? **(C) cert-tool residual defects** — crash paths, blind spots.

1. Baseline confirmed: HEAD `65838f867d6ece8e7b8bdcc4ffc667a08a1b785e`, tracked tree clean, `python3 corpus/tools/boundary_doc_check.py` → `CERTIFIED`, rc=0 (receipts 3/3, cases 14/14, anchors 2/2, h1=1, duplicates=0, markers=0). Sibling followup seats JCAL1 (census/pin) and JCAL3 (discrimination) do not overlap this lane. Seat block defined no dependencies; all inputs were present at HEAD immediately, so no wait-checks were needed.
2. Anchor census and content audit (scratch probe `/tmp/jdep2-anchor-probe.py`, deleted after run): the doc carries **127** `:NNN[-NNN]` colon-line refs; **6** attach to other files (`README.md`, `entities.json`, report `.md`s); the cert tool's own `ANCHOR` regex sees exactly **2** (the two full-form `check_bible.py:NNN` refs at doc lines 78 and 111). The remaining ~119 checker-context bare refs are invisible to the tool. The probe validated every checker-context ref against the delivered checker (428 lines) and, for the `5eb9451`-scoped family, against `git show 5eb9451:corpus/fixtures/check_bible.py` (330 lines), asserting each range contains a token from the doc's claim. 12 token assertions missed on probe-side heuristics only (e.g. `:82-83` says `if valid:` for "schema-valid rows collected"); every one was eyeballed against the dump and **all ~119 refs resolve to the claimed content — no live wrong-content anchor found**.
3. Adversarial C9 construction (the mission's named attack): copy of the delivered doc with (a) the decision-table sentence "Tick findings are NOT qualified …" replaced by "Tick findings inherit the same qualification: when a compared holder identity is not uniquely resolvable, the tick line is emitted with the `input-structural finding, not sourced-canon; ` prefix and an expected-holder note", (b) the limits bullet flipped from "Tick comparisons are not in this class … cannot qualify it" to "are in this class … qualifies the tick line like any chain finding", and (c) both required marker strings parked verbatim inside an added HTML comment (`<!-- superseded r90 wording preserved verbatim for history: Tick findings are NOT qualified by holder identity; tick order is an integer comparison. -->`). This doc now contradicts the delivered checker's actual behavior (delivered `check_bible.py:323-326` emits the bare tick line with no identity note; `r91-c1-tick-unresolved` pins it) — and it **certifies**. Receipt below.
4. Negative control: delivered doc + a fenced ```text block quoting the forbidden legacy literal `holder identity is not uniquely resolvable: {expected}` as superseded r87 history → **CERTIFICATION FAIL** rc=1. The gate cannot tell a quotation from a claim either.
5. Drift demo: bare-ref mutation `comparison gate (`:322`)` → `(`:325`)` (points into the tick block, semantically wrong) → still `CERTIFIED` rc=0, anchors still `2/2`.
6. Robustness edges: `--doc /tmp/nonexistent.md` and `--checker /tmp/nonexistent.py` both die with a raw `FileNotFoundError` traceback (rc=1). Fail-closed, but the `--doc` crash happens in `c9_semantics_check` before the intended `FAIL document` handler, and `--checker` crashes inside `checker_pin_check`.
7. Scratch (`/tmp/jdep2-c9-adversary.md`, `/tmp/jdep2-c9-negcontrol.md`, `/tmp/jdep2-drift.md`, `/tmp/jdep2-anchor-probe.py`) removed after capture; `git status --porcelain` shows only `?? .ufo/waves/round-93/followup/`.

## Before → after measurements

Baseline state of the cert tool (exact command, cwd `lore-shokunin/`):

```sh
python3 corpus/tools/boundary_doc_check.py
```

```text
CHECK receipt replay: PASS
CHECK code anchors: PASS
CHECK document structure: PASS
replay_receipts=3/3
replay_cases=14/14
anchors=2/2
h1_count=1
duplicate_headings=0
instruction_markers=0
CERTIFIED
```

rc=0. Anchor audit (exact command `python3 /tmp/jdep2-anchor-probe.py`, probe file since deleted; logic restated in Handoff):

```text
delivered_lines=428 baseline_lines=330
total_refs=127 checker_context=121 other_file_context=6
```

Full-form anchor dump (the tool's only 2): doc:78 `check_bible.py:212-224` "fits delivered(428)" — delivered lines 212-224 are the record-loop top + non-dict branch (`expected object`), while the doc scopes these lines to baseline `5eb9451`, where 212-224 are indeed the dangling/silent branches; doc:111 `check_bible.py:184` matches delivered content (`{location}.{endpoint}: ambiguous entity {entity_id!r}`).

Adversarial C9 doc (exact command `python3 corpus/tools/boundary_doc_check.py --doc /tmp/jdep2-c9-adversary.md`):

```text
CHECK receipt replay: PASS
CHECK code anchors: PASS
CHECK document structure: PASS
replay_receipts=3/3
replay_cases=14/14
anchors=2/2
h1_count=1
duplicate_headings=0
instruction_markers=0
CERTIFIED
```

rc=0 — **yes, it can pass.** Before: only the semantically correct doc certified. After: a doc asserting the opposite of the pinned C9 ruling and of delivered checker behavior also certifies, because the gate is substring presence and the markers survive in a comment. Negative control (`--doc /tmp/jdep2-c9-negcontrol.md`, fenced historical quote of the forbidden literal):

```text
FAIL: C9 semantics: required markers missing or a legacy tick-qualification claim present
CERTIFICATION FAIL
```

rc=1. Drift demo (`--doc /tmp/jdep2-drift.md`, bare `:322` → `:325`): identical all-PASS block, `anchors=2/2`, `CERTIFIED`, rc=0. Missing paths: `args=['--doc', '/tmp/jdep2-nonexistent.md'] rc=1 stderr_tail="FileNotFoundError: [Errno 2] No such file or directory: '/tmp/jdep2-nonexistent.md'"`; same shape for `--checker`.

## Findings & named debt

- **C9 semantics gate is a tripwire, not a semantics check.** `REQUIRED_C9_MARKERS` / `FORBIDDEN_LEGACY_TICK` are raw substrings over the whole doc text (comments and fences included, position-free). Demonstrated both failure directions with receipts: an adversarial doc contradicting the ruling certifies (markers parked in an HTML comment), and an honest historical quotation of the legacy string inside a fence fails. Any string-level gate remains bypassable by construction; the r94 fix should either validate the canonical decision-table sentence in prose-only context or accept the gate as tripwire-only and document that.
- **AST-anchor debt sized: 2 of 127 refs machine-checked, range-only.** The tool counts `anchors=2/2` while ~119 bare `:NNN` checker refs go uninspected; a semantically wrong bare ref (`:322`→`:325`) certifies unchanged. Practical impact today: **enforcement gap, not a live defect** — the full manual audit found zero wrong-content refs (every ref resolves to its claimed mechanism in the delivered 428-line checker, and the `5eb9451`-scoped family resolves in the 330-line baseline). One probe classification nuance: the checker-context count of 121 includes ~2 refs that attach to other files after all (e.g. the r87 decision-table `:104`), so the bare checker-ref count is ~119.
- **The one full-form baseline anchor is validated against the wrong revision.** doc:78's `check_bible.py:212-224` is explicitly a `5eb9451` baseline ref, but `check_anchors` range-checks it against the delivered 428-line file, where those lines are different code. The check is vacuous across revisions (false negative now; would false-positive if the delivered checker ever shrank below 224 lines). Fix shape: revision-qualified anchor grammar (e.g. `5eb9451@check_bible.py:212-224`) validated against `git show <rev>:…`.
- **Cert tool reads doc/checker before its own error handling.** `c9_semantics_check(pathlib.Path(args.doc).read_text())` and `checker_pin_check(args.checker)` dereference the raw paths before the guarded doc read, so a missing path crashes with a traceback instead of the intended `FAIL document` message. Fail-closed (rc≠0); cosmetic severity.
- **Design note (debt, not defect):** the pin and C9 gates live inside `boundary_doc_check.py` itself, which carries no self-integrity mechanism; and the gate demands C9 markers of *any* `--doc`, so the tool is single-document by construction. Both are acceptable for a round-scoped certifier but worth naming if it survives to r94.

## Handoff

- r94 candidate 1 (highest value): extend `check_anchors` to bare `:NNN` refs in checker context with content-signature validation. Seed logic (probe deleted per file-frugality, restated): regex `:(\d+)(?:-(\d+))?` over the doc, exclude refs whose 24 preceding chars contain `README.md|entities.json|.md|.json`, classify the rest as checker-context (minus the r87-table `:104`), and assert a claimed token per range; ~119 refs, all pass today, so landing it is a no-change event that converts the audit from manual to machine.
- r94 candidate 2: revision-qualified anchors for the `5eb9451` family (finding 3).
- r94 candidate 3: C9 gate hardening — prose-only marker requirement or canonical-sentence match, plus explicitly documenting the false-positive-on-quotation behavior (finding 1).
- r94 candidate 4 (cosmetic): move `c9_semantics_check`/`checker_pin_check` after the guarded reads (finding 4).
- For the C1/doc owner: no doc edits proposed this seat — the boundary doc itself is accurate (all ~119 refs verified); only the tool needs the debt work.
- Verify-clean: `git status --porcelain` = `?? .ufo/waves/round-93/followup/` only; scratch removed; `/tmp/jdep2-*` absent; no commits, no pushes, no sibling-repo writes.
