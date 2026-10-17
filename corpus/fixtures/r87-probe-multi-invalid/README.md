Probe (round 87, C2 depth; closes JDEP3 U-6): one record carries BOTH an ambiguous from_holder and an unknown source. Expected: 6 findings, exit 1, in emission order: duplicate 'vault' id; ambiguous from_holder; the item-level stop notice; the per-record disclosure at [1] naming from_holder 'vault'; the unknown-source finding at [1]; the per-record disclosure at [2].

---

**r88 revision note** (commit at r88 closure; measured on the delivered tree: exit 1, 5 findings): delivered checker now reports 5 findings, reordered; the item-level notice is folded into per-record disclosures.
