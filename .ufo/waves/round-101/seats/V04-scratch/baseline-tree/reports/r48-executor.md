# Round 48 executor — Vela clause-map correction

## Scope and result

Corrected exactly these two active local maps to describe their own unchanged direct Vela excerpts:

- `.shokunin/lore/corpus/fixtures/r41-vela-direct-bell/vela-clause-map.md`
- `.shokunin/lore/corpus/fixtures/r43-jorin-vela-sighting/vela-clause-map.md`

Both now identify the local report as r41/r43 (not r40), quote “heard the registry bell strike twice,” and use one clause row for Vela-attributed direct hearing/identification. Each distinguishes this direct identification in her fictional, unverified report from proof that an objective registry bell rang. The unchanged JSON claim/event wording “she took to be” is logically compatible but weaker/under-specific, not false; the separate strength-contrast maps remain untouched. Date/Bell-7 is Vela’s unverified occasion/date claim, not authenticated chronology or a shared occasion. The maps retain broad harbor/east-steps location limits, non-sighting (not absence), source/citation limits, arbitrary tick 3 (not chronology/simultaneity), and no-corroboration/no-canon boundaries. No objective bell source, relation, or ledger row was added.

## Exact before/after byte and path audit

Before = index blob at current `HEAD`; after = working-tree bytes. The complete changed-path set is exactly the two existing Markdown paths above. Both old files were 2,183 bytes, SHA-256 `72d0fcfeeadd115bd1e68855f6e6619d475ca22428f3a44b6699b52123e9df65` (each); both new files are 2,545 bytes. r41 after SHA-256: `99ea6ef2df7d849efb6f9ab5886e6abd745f148f7d915a99e9b1ad9e777a3a9d`. r43 after SHA-256: `7195f46d359c3d889540fa198580c338c36dd2b90852eacbf6650a33506cfd17`. The two complete diffs are those from `git diff` for the named paths: each changes the stale heading and full quoted excerpt; replaces the two obsolete tentative sound-identification rows with one direct attributed identification row; clarifies the weaker compatible fixed claim/event and no shared-occasion/objective-proof limits; and replaces the present-tense unchanged-inheritance assertion with a disclosure that the r40 tentative map remains the control and the two active maps are corrected. r41/r43 corrected content is the same except its local r41/r43 heading.

All other paths are outside this edit. In particular, r40 map/source, both r41/r43 source excerpts, all JSON including fixed tables, both strength-contrast maps, checker, README, LOG and historical reports were not edited. The r40 map remains byte-identical in working tree to its pre-edit state. Historical statements that maps/excerpts were retained unchanged remain historical snapshots; they are not true of these two active map bytes after this repair. This report supersedes only the assertion of current unchanged status for these two maps, not the historical creation-time comparisons or other inherited-byte claims.

## Checker evidence (raw runs)

Invoked from repository root with `python3 .shokunin/lore/corpus/fixtures/check_bible.py <fixture-path>` separately for each target. Exact stdout, stderr and exit status:

- r40 control: stdout `CLEAN: schema, citations, relations, timeline; 0 violations\n`; stderr empty; exit 0.
- r41: stdout `CLEAN: schema, citations, relations, timeline; 0 violations\n`; stderr empty; exit 0.
- r43: stdout `CLEAN: schema, citations, relations, timeline; 0 violations\n`; stderr empty; exit 0.

These checker runs validate JSON/schema/citation/relation/timeline only; they do not assess Markdown clause-map accuracy, external truth, rights, or canon. No baseline-vs-current 95-fixture raw tuple replay was performed or claimed here. No commit made.
