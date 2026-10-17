# R93 M2 — M-17 margin-register cluster

This is a newly authored fictional record cluster with a narrow editorial comparison to three clauses in Basil Hall Chamberlain's 1882 English translation of *The Kojiki*, Part III, “The Door of the Heavenly Rock-Dwelling.” The source excerpt and the separate attribution, rights, and AI-training-permission questions are in `kojiki-chamberlain-excerpt.md` and `inspiration-note.md`. The translation remains external: no named deity, place, object, plot, or ritual is an in-world referent or canon.

`archive-record-excerpt.md` delivers prose for the sole fictional source ID. `claim-excerpt-map.md` maps all 12 source-attributed JSON facts and all three external editorial comparison rows, with line spans, R9 modes, and exact anchors. The Kojiki comparison rows are editorial only; no fictional JSON fact relies on the English translation as R5 support, and no R9 manual-review PASS is asserted. `support_check.py` is a lexical preflight, not review of whole-claim fidelity or rights.

Replay from the repository root:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r93-m2-kojiki-cluster
python3 corpus/tools/support_check.py corpus/fixtures/r93-m2-kojiki-cluster
```

## R10 comparison outcomes

Compared separately with `corpus/fixtures/r87-myth-cluster` and `corpus/fixtures/r88-m3-maya-cluster`. This cluster's only in-world entities are `teva` (Teva), `orni` (Orni), `slate-table` (Slate Table), and `lorn-index` (Lorn Index); its events are `teva-files-index` and `orni-marks-index`. The author-side normalized-key preflight covers entity IDs, display names, declared aliases/epithets, event IDs, and relation/timeline endpoints; it found no exact key shared with either existing cluster. No alias, epithet, translated name, or disguised identity is adopted. The historical/mythic names in the delivered Kojiki translation remain external and are not entities or aliases in this bible. Its translated term `Central Land of Reed-Plains` (`kojiki-chamberlain-excerpt.md:8,10`) is a lexical lookalike only to r87's `Reed Bell` and `Reedwardens` at the generic word `Reed`; M-17 adopts neither as a name or referent. Other prior-cluster names in this paragraph are explicit contrast references, not M-17 identities. Source IDs are compared only as path-qualified namespace pairs (`r93-m2-kojiki-cluster:m2-record-archive` versus each prior cluster's path and ID); bare source IDs are not referent identity evidence. Author-side semantic review found no shared identity/occasion candidate. M6's current report reviews M1's distinct `r93-myth-cluster3` candidate, not this M-17 cluster; an independent M2-specific scan and semantic review remain pending before any integrated zero-referent conclusion. No cross-cluster contradiction is asserted.
