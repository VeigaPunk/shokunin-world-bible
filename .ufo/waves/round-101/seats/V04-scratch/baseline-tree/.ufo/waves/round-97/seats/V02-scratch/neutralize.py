#!/usr/bin/env python3
"""Neutralize the dual_pointer emission in a scratch copy of the delivered tool.

Usage: neutralize.py <scratch_tool_path>
Locates the gating.append emission that emits the dual_pointer finding and
renames only that emitted id, leaving SELF_TEST_CASES tuple entries intact.
Exits non-zero if the emission site is not found exactly once.
"""
import re
import sys

path = sys.argv[1]
s = open(path, encoding="utf-8").read()
new, n = re.subn(r'gating\.append\(\s*\(\s*"dual_pointer"',
                 'gating.append(("dual_pointer_off"', s)
if n != 1:
    print(f"EMISSION_SITE_COUNT={n} (expected 1)")
    sys.exit(3)
open(path, "w", encoding="utf-8").write(new)
print("neutralized emission: dual_pointer -> dual_pointer_off (1 site)")
