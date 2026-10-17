#!/bin/bash
prev=""
for i in $(seq 1 30); do
  cur=$(sha256sum corpus/tools/dependency_freeze.py 2>/dev/null | cut -c1-16)
  rep=$(ls .ufo/waves/round-96/seats/ 2>/dev/null | grep -E '^Q3.*\.md$' | head -1)
  echo "try $i: tool_hash=$cur stable=$([ "$cur" = "$prev" ] && echo yes || echo no) report=${rep:-none}"
  if [ -n "$rep" ] && [ "$cur" = "$prev" ]; then echo "READY report=$rep hash=$cur"; exit 0; fi
  prev=$cur
  sleep 20
done
echo "TIMEOUT"; exit 1
