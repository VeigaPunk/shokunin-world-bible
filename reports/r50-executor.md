# Round 50 executor — README-only correction

## Edit

Changed only `.shokunin/lore/corpus/fixtures/README.md`, replacing the stale present-tense guidance in the Round 43 paragraph. Neighboring Jorin description, checker commands, and remaining README text are unchanged. Novelty remains undecided; this report makes no axis verdict.

Exact replacement:

```diff
-phrases and warns that the inherited r41 `vela-clause-map.md` quotes the older
-r40 wording; use the actual r41 Vela excerpt and `strength-contrast-map.md`
-for that difference.
+phrases. The current r41 and r43 `vela-clause-map.md` files were corrected in
+r48 to quote their local direct excerpts; older creation-time reports accurately
+describe the formerly stale inherited maps. Use `strength-contrast-map.md` for
+the r40 tentative versus r41 direct wording and its fixed, weaker but compatible
+JSON summary—not as an objective bell claim.
```

README SHA-256 before: `c0252ed2308abb2f6f4865091d926c7d94cdadd5e564a7851df79c12d7ddc53c`  
README SHA-256 after: `9db3195ccebca979a75130581099c65f334e5502e53adca523c96e8c07c69ac4`

## Scope audit

`git status --porcelain -- .shokunin/lore/corpus`:

```text
 M .shokunin/lore/corpus/fixtures/README.md
```

Only README is modified in corpus. No source maps, excerpts, JSON, or checker files were touched. Outside corpus, pre-existing Round 50 LOG/scout changes remain untouched. No commit made.

## Structural checker replay

Executed from repository root with `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture>`. Exact raw results:

- r40-vela-listener: exit status `0`; stdout bytes `b'CLEAN: schema, citations, relations, timeline; 0 violations\n'`; stderr bytes `b''`.
- r41-vela-direct-bell: exit status `0`; stdout bytes `b'CLEAN: schema, citations, relations, timeline; 0 violations\n'`; stderr bytes `b''`.
- r43-jorin-vela-sighting: exit status `0`; stdout bytes `b'CLEAN: schema, citations, relations, timeline; 0 violations\n'`; stderr bytes `b''`.

These are structural checks only; they do not validate prose, bell claims, chronology, or canon.
