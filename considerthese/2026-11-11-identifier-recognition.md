# Lore: recognizing an identifier is not validating records

W3C's [xml:id](https://www.w3.org/TR/2005/REC-xml-id-20050909/), Recommendation, 9 September 2005, addresses consumers lacking declarations identifying ID attributes. Its processing layer recognizes xml:id without requiring validation or external declarations, extending XML's existing identifier model.

Sections 4–6 require normalization and ID assignment even for offending values. Uniqueness checking and error reporting are recommended; errors are nonfatal. Therefore, recognized ID status is not a clean validation result.

[Errata](https://www.w3.org/2005/09/xml-id-errata), 10 March 2010, clarify that validation still requires declarations in the relevant DTD or schema. Recognition does not exempt the attribute from grammar rules.

Curator inference: a lore importer should separately report target recognition, duplicate identifiers and grammar validity before trusting annotation links. The standard establishes neither cross-document identity nor canon. No importer tested.

Original commentary; no copied examples. Sources: ©2005 W3C; linked Document License 2023 requires source, copyright and status on copies and restricts derivatives.

Reviewed 2026-11-11. Unassimilated.

Destination: https://github.com/VeigaPunk/shokunin-world-bible, main, considerthese/2026-11-11-identifier-recognition.md.
