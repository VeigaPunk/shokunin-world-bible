# Round 67 independent verifier

## Scope and commands

Baseline is old HEAD `262486d` (`git archive 262486d .shokunin/lore/corpus`). I extracted that tree to a temporary directory, enumerated fixture directories from its `fixtures/`, and confirmed 125 directories and 623 JSON files. For every directory, I ran both archived HEAD checker and current checker against that extracted original fixture data, capturing process exit status, stdout bytes, and stderr bytes:

```sh
python3 <archived-head>/.../fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture>
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture>
```

The commands ran with the archived tree as cwd, so the relative fixture paths resolve to the original HEAD fixture bytes. I also compared the archived and working-tree corpus by relative path and raw file bytes.

## Original corpus regression replay

- Original fixture directories enumerated: **125**; original fixture JSON files: **623**.
- Original fixture input bytes: identical between archive and working tree for all original fixture files (including all 623 JSON files).
- Raw checker tuple `(exit status, stdout bytes, stderr bytes)`: archived HEAD vs current checker **125/125 identical**. Mismatches: **0**.
- Full corpus: HEAD contained **1,298 files**. All original relative paths are present in the current corpus. Excluding the intentionally edited `fixtures/check_bible.py` and `fixtures/README.md`, **1,296/1,296** other original paths are byte-identical; mismatches/missing paths: **0**. Current tree adds 22 files under five r67 fixture directories and `corpus/README.md` (23 new corpus paths total). No original paths were removed.

This is replay evidence, not a claim that the proposed calibration change merits admission.

## New fixture differential audit

The fixture files were read as raw bytes. In the unavailable-index matched trio, all four shared files (`contradictions.json`, `relations.json`, `timeline.json`, `entities.json`) are byte-identical between the nonempty control, empty, and whitespace cases except `entities.json`; `sources.json` is absent in all three. Loaded control/empty cases have byte-identical `contradictions.json`, `relations.json`, `sources.json`, and `timeline.json`; only `entities.json` differs. Loaded control has a nonempty source table and claim source ID; loaded empty changes only the claim source ID to empty. Thus observed checker differences are tied to the intended claim field probe, with index availability held within each pair. No other fixture-file diffs found.

## Five current CLI outcomes

Command for each case (run from repository root):

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture>
```

All stderr outputs were **empty**. Exact stdout and exit status:

- `r67-claim-source-unavailable-control` — exit **1**:
  ```text
  VIOLATION: sources.json: cannot load JSON: [Errno 2] No such file or directory: '.shokunin/lore/corpus/fixtures/r67-claim-source-unavailable-control/sources.json'
  1 violation(s); no canon changed
  ```
- `r67-claim-source-unavailable-empty` — exit **1**:
  ```text
  VIOLATION: sources.json: cannot load JSON: [Errno 2] No such file or directory: '.shokunin/lore/corpus/fixtures/r67-claim-source-unavailable-empty/sources.json'
  VIOLATION: entities[0].claims[0]: expected nonempty statement and source_id
  2 violation(s); no canon changed
  ```
- `r67-claim-source-unavailable-whitespace` — exit **1**:
  ```text
  VIOLATION: sources.json: cannot load JSON: [Errno 2] No such file or directory: '.shokunin/lore/corpus/fixtures/r67-claim-source-unavailable-whitespace/sources.json'
  VIOLATION: entities[0].claims[0]: expected nonempty statement and source_id
  2 violation(s); no canon changed
  ```
- `r67-claim-source-loaded-empty` — exit **1**:
  ```text
  VIOLATION: entities[0].claims[0]: expected nonempty statement and source_id
  1 violation(s); no canon changed
  ```
- `r67-claim-source-loaded-control` — exit **0**:
  ```text
  CLEAN: schema, citations, relations, timeline; 0 violations
  ```

The unavailable-index negatives add a claim-local structural finding beyond the loader error; the unavailable control does not. This establishes the current checker’s behavior on these inputs only. It does not establish source identity/support, fictional-world evidence or absence, truth, canon, or rights. No candidate pass/admission or source-of-truth conclusion is claimed.

No checker, fixture, README, or LOG files were edited by this verifier; no commit, push, or merge.
