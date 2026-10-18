import json, sys
mode, src, dst = sys.argv[1], sys.argv[2], sys.argv[3]
if mode == "contract":
    c = json.load(open(src, encoding='utf-8'))
    del c['self_test']['expected']['repointed_edge']
    open(dst, 'w', encoding='utf-8').write(json.dumps(c, indent=2, ensure_ascii=False)+'\n')
    print(f"EDIT contract: expected now {len(c['self_test']['expected'])} cases; removed: repointed_edge")
else:
    s = open(src, encoding='utf-8').read()
    assert '    "repointed_edge",\n' in s
    s = s.replace('    "repointed_edge",\n', '', 1)
    open(dst, 'w', encoding='utf-8').write(s)
    print("EDIT tool: FROZEN_CASES line 'repointed_edge' removed (19 -> 18)")
