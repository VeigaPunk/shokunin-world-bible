# Round 48 independent verifier

Baseline: commit `3487e9591d9d24c042107c661000621f748d057e` (`git archive` extracted to a separate temporary root). The working tree root was compared against that archive. This was an independent, non-author verification; no checker or corpus files were edited.

## Replay

Enumerated **95** immediate fixture directories present in the baseline and **474** fixture JSON paths. For each baseline fixture name, from the root directory of the extracted archive and from the current working-tree root, ran the identical argv `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<name>` (where `<name>` is that fixture’s immediate directory basename). Compared raw stdout bytes, raw stderr bytes, and exit status for each pair; all **95/95** pairs matched exactly. All **474/474** JSON files and the checker source were byte-identical.

## Corpus inventory and byte audit

The complete baseline `.shokunin/lore/corpus/` file inventory matched the working tree: no missing or added corpus paths. Exactly two corpus files differed, both Markdown maps: `fixtures/r41-vela-direct-bell/vela-clause-map.md` and `fixtures/r43-jorin-vela-sighting/vela-clause-map.md`. In each case the baseline SHA-256 is `72d0fcfeeadd115bd1e68855f6e6619d475ca22428f3a44b6699b52123e9df65`; current hashes are respectively `99ea6ef2df7d849efb6f9ab5886e6abd745f148f7d915a99e9b1ad9e777a3a9d` and `7195f46d359c3d889540fa198580c338c36dd2b90852eacbf6650a33506cfd17`.

Manual diff review: both revised maps quote their fixture-local excerpt’s direct wording, “heard the registry bell strike twice,” and distinguish Vela’s attributed identification from proof of an objective ringing. They characterize the existing claim/event’s “she took to be” wording as compatible but under-specific. The r40 control map, all excerpts, strength maps, README, and all remaining corpus files are byte-unchanged. This semantic assessment is limited to manual inspection; it is not checker proof.
