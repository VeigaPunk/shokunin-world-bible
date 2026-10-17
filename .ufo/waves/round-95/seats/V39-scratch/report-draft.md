# V39 — dialect-audit-2 (round 95) [DRAFT SKELETON — superseded by final report]

Seat: V39 dialect-audit-2. Scope: after P1 lands, independently recount r88 raw
obligations by a different enumeration method than V05's; confirm the tool's
dialect output matches both enumerations one-to-one; confirm anchor/span/mode
agreement with the r88 map rows.

## Method
- enumerate_r88.py: standalone; method A = generic recursive walker (source_id
  fields -> parent pointer; first_appearance -> own pointer); method B = regex
  text cross-count per file vs parsed array lengths.
- parse_r88_map.py: my own markdown table reader + dialect translator
  (entities[i].first_appearance -> entities.json#/i/first_appearance; etc.)
- check_anchor_span_mode.py: span resolution + anchor substring + mode vs
  declarations table.
- build_probes.py / run_probes.py: differential one-to-one probes.

## Pre-P1 evidence
(placeholder)

## Post-P1 evidence
(placeholder)

## Bottom line
(placeholder)
