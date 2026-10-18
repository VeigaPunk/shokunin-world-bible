# R1B — sourced-inspiration decision-table review

## Work performed

- **Axes:** C3 contract fit (three distinct citation questions), completeness/enforceability of the excerpt-support rule, and fit to the selected M3 cluster's evidence.
- Reviewed the round-88 spec, `seed.md:8-16, 26-29`, `PROVINCE.md`, D1 and D2 tables/reports, D2's ledger rows, T1's cross-verification, M1/M2/M3 reports, and M5's convergence review.
- **Recommendation: land D1 only** as `corpus/knowledge/r88-sourced-inspiration-decision-table.md`. Do not merge D2's lifecycle table or its separate ledger-row template into the decision table. D1's six-column table includes explicit separate `Attribution`, `Rights status`, and `AI-training permission` columns, excerpt-delivery requirements, ledger registration, and conflict handling. D2's five-stage workflow has no three distinct citation-question columns; its companion ledger rows do not cure that table-contract omission.
- Before landing, make the in-world support rule below explicit in D1's “An in-world claim is attributed to a delivered excerpt” row. The intent is consistent with D1's OBS-1 and M1/M2 evidence discussion, but “every claim” could otherwise be read as covering only claims mapped to an external excerpt or inspiration note.

## Before → after measurements

No corpus or decision-table patch was applied in this review. The before/after change is a recommendation and a precise scope clarification for the integrator; final delivered-tree verification remains pending.

- After-report check, run in `lore-shokunin/`: `git diff --exit-code && git status --short --untracked-files=all -- .ufo/waves/round-88/R1B.md`
  - `git diff --exit-code` produced no output and succeeded (no tracked-file diff).
  - Status output: `?? .ufo/waves/round-88/R1B.md`.

- Baseline command, run in `lore-shokunin/`: `git status --short && git rev-parse HEAD`

  ```text
  ?? .ufo/waves/round-88/
  dfd1fbc3711f2b28597d74444819aca91fe6bc31
  ```

- Draft shape command, run in `lore-shokunin/`:

  ```sh
  python3 - <<'PY'
  from pathlib import Path
  for name in ('.ufo/waves/round-88/patches/D1-table.md', '.ufo/waves/round-88/patches/D2-decision-table.md', '.ufo/waves/round-88/patches/D2-ledger-rows.md'):
      lines = [line for line in Path(name).read_text().splitlines() if line.startswith('|')]
      header = [cell.strip() for cell in lines[0].strip('|').split('|')]
      rows = len(lines) - 2
      print(f'{name}: data_rows={rows}; columns={header}')
  PY
  ```

  Observed:

  ```text
  .ufo/waves/round-88/patches/D1-table.md: data_rows=7; columns=['Decision', 'Rule / output', 'Attribution', 'Rights status', 'AI-training permission', 'r87 / round-88 evidence and integration check']
  .ufo/waves/round-88/patches/D2-decision-table.md: data_rows=5; columns=['Lifecycle stage', 'Decision / acceptance gate', 'Excerpt and citation requirements', 'Verification against available candidates']
  .ufo/waves/round-88/patches/D2-ledger-rows.md: data_rows=2; columns=['Work / attribution', 'Rights question', 'AI-training permission question', 'Use here']
  ```

- Cross-verification evidence for the T1-flagged M1/M2 gaps (commands and outputs recorded by D1 on scratch-applied candidate patches):

  M1 command:

  ```sh
  python3 - <<'PY'
  from pathlib import Path
  p = Path('corpus/fixtures/r88-myth-cluster2')
  md = sorted(x.name for x in p.glob('*.md'))
  internal = [x for x in md if x not in {'README.md', 'inspiration-note.md', 'kojiki-excerpt.md', 'symbolism-index.md'}]
  print('markdown_files={}'.format(','.join(md)))
  print('delivered_inworld_source_text_files={}'.format(len(internal)))
  PY
  ```

  Observed: `markdown_files=README.md,inspiration-note.md,kojiki-excerpt.md,symbolism-index.md`; `delivered_inworld_source_text_files=0`.

  M2 command:

  ```sh
  python3 - <<'PY'
  from pathlib import Path
  import json
  root = Path('corpus/fixtures/r88-norse-cluster')
  entities = json.loads((root/'entities.json').read_text())
  source_ids = sorted({c['source_id'] for e in entities for c in e['claims']})
  texts = [p for p in root.glob('*.md') if p.name not in ('README.md','inspiration-note.md','voluspa-19-excerpt.md','symbolism-clause-map.md')]
  print(f'entity_claim_source_ids={source_ids}')
  print(f'potential_inworld_excerpt_files={[p.name for p in texts]}')
  print('delivered_hush_song_excerpt=' + str((root/'hush-lantern-excerpt.md').exists()))
  print('contradiction_record_present=' + str('hush-lantern-first-light-location' in (root/'contradictions.json').read_text()))
  PY
  ```

  Observed: `entity_claim_source_ids=['lantern-compact', 'root-wick-slip', 'salt-window-record']`; `potential_inworld_excerpt_files=['hush-lantern-excerpt.md']`; `delivered_hush_song_excerpt=True`; `contradiction_record_present=True`. The delivered hush-song text does not stand in for the three separately cited in-world sources.

- Checker commands recorded by D1 for the scratch-applied candidates:

  ```sh
  python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-myth-cluster2
  python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-norse-cluster
  ```

  Observed for each: `CLEAN: schema, citations, relations, timeline; 0 violations` (exit 0). These outputs verify structure/source-ID resolution, not prose support. M5 recommends M3, whose paired-register source excerpts and cited Spence passage are delivered; use M3 plus M4's excerpt repair for the actual integration audit, rather than treating M1/M2 gaps as accepted exceptions.

## Findings & named debt

- **One table to land:** D1 is the only standalone draft that directly meets the contract's three-column citation-field requirement and provides operational locator, excerpt, per-claim support, and ledger rules. D2's lifecycle ordering is useful context but would require importing a second table and still would not supply the required fields inside the decision table. No merge is recommended.
- **“Every attributed claim” scope: yes, all in-world JSON assertions/attributions carrying a `source_id` must be covered**, whether or not they appear in an inspiration note or clause→element map. This includes each `entities.json` `claims[]` statement and `first_appearance` pointer, each `relations.json` edge, each `timeline.json` event, and equivalent source-attributed factual records. `sources.json` ID resolution alone is not source-text evidence. This follows the world-bible schema in `seed.md:8-16` and closes the reading ambiguity T1 identified.
- Suggested replacement/addition for D1's in-world support rule:

  > Resolve every in-world JSON assertion or attribution carrying a `source_id`—including entity claims and first-appearance pointers, relation edges, and timeline events—to its in-world source record and the corresponding delivered source text. For each assertion, record the excerpt path and line span plus a distinctive exact phrase or named anchor; run a fixed-string, line-numbered search. A missing source text, unresolved ID, or zero match fails support review. A match is only a lexical preflight: also review that the passage supports the entire assertion. Apply this rule whether or not the assertion appears in the inspiration note or symbolism map; metadata-only source IDs and a clean schema checker do not establish prose support.

- Under that rule, M1's `watch-register`, `assembly-minutes`, `shore-pact`, and `harbor-log` claims and M2's `lantern-compact`, `root-wick-slip`, and `salt-window-record` claims remain unauditable until their in-world texts are delivered or those claims are revised/re-sourced with delivered evidence. They are evidence gaps, not proof of falsity and not findings that the structural checker is broken. M3's delivered source material makes it the appropriate selected candidate to verify; final integration still needs the actual M3/M4 combined-tree audit.
- **Named debt:** the selected table and its evidence column have not been verified against an integrated delivered tree. At integration, apply the clarification, check each decision row against the selected M3 cluster and M4 excerpt repair, register the selected real-world source using the four-column ledger format, and record any unresolved support as a blocker rather than an exception.

## Handoff

- Recommendation for integration: copy `patches/D1-table.md` to `corpus/knowledge/r88-sourced-inspiration-decision-table.md`, with the explicit all-source-attributed-JSON scope clarification above. Do not land D2's table as a second canonical table or merge its separate row template into D1.
- Reviewed: `patches/D1-table.md`, `patches/D2-decision-table.md`, `patches/D2-ledger-rows.md`, plus T1 and the M1/M2/M3 and M5 reports. No peer artifact or tracked corpus file was modified; no commit or push was made.
- This report is the only R1B repository write: `.ufo/waves/round-88/R1B.md`. Final integration checks are still owed by the landing lane.
